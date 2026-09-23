#!/usr/bin/env python3
"""
Returns / size-chart / compare / free-people / reviews page QA harness.

These six pages 404 on the M4 Visual QA draft theme because their Shopify Admin template
suffixes name templates that only exist in the old live theme. This harness renders the
new suffix-matched templates for real so they can be reviewed before anything is pushed:
template JSON goes in as `section.settings` / `section.blocks`, the section Liquid runs
through python-liquid with snippets resolved out of shopify-build/snippets, and the
stylesheets are linked live out of shopify-build/assets.

Two of the pages render `{{ page.content }}` — the Admin-authored page body. That body is
where the ReturnZap portal embed lives, so the harness pulls the real live bodies down and
feeds them in, which is the only way to prove the embed survives the new template. Live
bodies are cached in .cache/ (verbatim evidence, not source copy — see README).

Mobile: macOS headless Chrome clamps windows to 500px, so 390px comes from a CDP
Emulation.setDeviceMetricsOverride on an oversized window, not from --window-size.

Usage:
    python3 planning/returns-pages-qa/build.py                 # validate, render, shoot
    python3 planning/returns-pages-qa/build.py --no-shots      # validate + render only
    python3 planning/returns-pages-qa/build.py --offline       # skip the live body fetch
"""

import argparse
import base64
import http.client
import json
import os
import re
import shutil
import socket
import subprocess
import tempfile
import time

import websocket  # websocket-client

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
BUILD = os.path.join(REPO, "shopify-build")
SECTIONS = os.path.join(BUILD, "sections")
SNIPPETS = os.path.join(BUILD, "snippets")
TEMPLATES = os.path.join(BUILD, "templates")
CACHE = os.path.join(HERE, ".cache")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ASSETS = "../../shopify-build/assets"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# name -> template filename, live URL the Admin page body comes from (None = no body used),
# and the live template fingerprint used to locate that body in the live HTML.
# Each live page has two repo templates: the one named for the Admin suffix, and the one
# named for the handle. Both are rendered — a returns template that stops rendering
# page.content silently deletes the ReturnZap portal, so every one of them gets audited.
PAGES = {
    "returns": {
        "template": "page.shipping-retruns.json",
        "live": "https://barreletics.com/pages/returns",
        "fingerprint": "26590735466787",
    },
    "returns-handle-template": {
        "template": "page.returns.json",
        "live": "https://barreletics.com/pages/returns",
        "fingerprint": "26590735466787",
    },
    "returns-portal": {
        "template": "page.start-a-retrun.json",
        "live": "https://barreletics.com/pages/returns-portal",
        "fingerprint": "26590735630627",
    },
    "returns-portal-handle-template": {
        "template": "page.returns-portal.json",
        "live": "https://barreletics.com/pages/returns-portal",
        "fingerprint": "26590735630627",
    },
    "size-chart": {"template": "page.size-chart.json"},
    "compare-open-vs-closed": {"template": "page.compare-open-vs-closed.json"},
    "free-people": {
        "template": "page.free-people.json",
        "live": "https://barreletics.com/pages/free-people",
        "fingerprint": None,  # live template has no page-body section at all
    },
    "reviews": {
        "template": "page.judgeme_all_reviews.json",
        "live": "https://barreletics.com/pages/reviews",
        "fingerprint": None,  # live body is rendered by a Judge.me .liquid template
    },
}

FALLBACK_TITLES = {
    "returns": "SHIPPING, RETURNS & FAQ",
    "returns-handle-template": "SHIPPING, RETURNS & FAQ",
    "returns-portal": "Start a Return or Exchange",
    "returns-portal-handle-template": "Start a Return or Exchange",
    "free-people": "Free People",
    "reviews": "REVIEWS",
}


# ------------------------------------------------------------------- schema validation


def section_schema(section_type):
    src = open(os.path.join(SECTIONS, section_type + ".liquid")).read()
    m = re.search(r"\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}", src, re.S)
    if not m:
        raise RuntimeError("%s has no {%% schema %%}" % section_type)
    return json.loads(m.group(1))


def validate(template_file):
    """Every section type must exist and every setting key must be in its schema."""
    problems = []
    tpl = json.load(open(os.path.join(TEMPLATES, template_file)))
    for sid in tpl["order"]:
        if sid not in tpl["sections"]:
            problems.append("%s: order references missing section %r" % (template_file, sid))
            continue
        conf = tpl["sections"][sid]
        stype = conf["type"]
        path = os.path.join(SECTIONS, stype + ".liquid")
        if not os.path.exists(path):
            problems.append("%s: section type %r has no sections/%s.liquid"
                            % (template_file, stype, stype))
            continue
        schema = section_schema(stype)
        allowed = {s["id"] for s in schema.get("settings", []) if "id" in s}
        for key in conf.get("settings", {}):
            if key not in allowed:
                problems.append("%s / %s: setting %r not in %s schema"
                                % (template_file, sid, key, stype))
        block_settings = {b["type"]: {s["id"] for s in b.get("settings", []) if "id" in s}
                          for b in schema.get("blocks", [])}
        for bid, block in conf.get("blocks", {}).items():
            btype = block.get("type")
            if btype not in block_settings:
                problems.append("%s / %s: block type %r not in %s schema"
                                % (template_file, bid, btype, stype))
                continue
            for key in block.get("settings", {}):
                if key not in block_settings[btype]:
                    problems.append("%s / %s (%s): setting %r not in %s schema"
                                    % (template_file, bid, btype, key, stype))
        if not schema.get("presets"):
            problems.append("%s: section %r has no presets (contract requires them)"
                            % (template_file, stype))
    return problems


# --------------------------------------------------------------------------- live body


def live_body(name, conf, offline):
    """Return {title, content} for the page object, pulling the real Admin body content."""
    if "live" not in conf:
        return None
    os.makedirs(CACHE, exist_ok=True)
    body_path = os.path.join(CACHE, "%s-body.html" % name)
    meta_path = os.path.join(CACHE, "%s-meta.json" % name)

    if not (offline and os.path.exists(body_path)):
        try:
            # curl, not urllib: urllib uses its own CA bundle, which is not populated on
            # this machine, so every https fetch fails certificate verification.
            html = subprocess.run(
                ["curl", "-sSL", "-A", UA, conf["live"]],
                capture_output=True, check=True, timeout=60).stdout.decode("utf-8", "replace")
            title, content = extract_body(html, conf.get("fingerprint"))
            with open(body_path, "w") as fh:
                fh.write(content)
            with open(meta_path, "w") as fh:
                json.dump({"title": title, "source": conf["live"],
                           "fetched": time.strftime("%Y-%m-%dT%H:%M:%S")}, fh, indent=1)
        except Exception as e:
            print("  ! live fetch failed for %s (%r) — using cache if present" % (name, e))

    title = FALLBACK_TITLES.get(name, name)
    if os.path.exists(meta_path):
        title = json.load(open(meta_path)).get("title") or title
    content = open(body_path).read() if os.path.exists(body_path) else ""
    return {"title": title, "content": content}


def extract_body(html, fingerprint):
    """Pull the page title and page.content out of the live theme's page section."""
    if not fingerprint:
        return None, ""
    marker = '<section id="shopify-section-template--%s__main"' % fingerprint
    if marker not in html:
        return None, ""
    start = html.index(marker)
    block = html[start:html.index("</section>", start)]
    title = None
    m = re.search(r'<h1 class="section-header__title">\s*(.*?)\s*</h1>', block, re.S)
    if m:
        title = re.sub(r"\s+", " ", m.group(1)).strip()
    # The live theme wraps page.content in .rte — that inner HTML *is* page.content.
    m = re.search(r'<div class="rte rte--nomargin">(.*)</div>\s*$', block, re.S)
    content = m.group(1).strip() if m else ""
    return title, content


# ------------------------------------------------------------------------------ render


def strip_shopify_tags(src):
    src = re.sub(r"\{%-?\s*schema\s*-?%\}.*?\{%-?\s*endschema\s*-?%\}", "", src, flags=re.S)
    src = re.sub(r"\{\{\s*(section|block)\.shopify_attributes\s*\}\}", "", src)
    return src


def render_section(env, section_type, conf, page):
    src = strip_shopify_tags(open(os.path.join(SECTIONS, section_type + ".liquid")).read())
    order = conf.get("block_order") or list(conf.get("blocks", {}))
    blocks = [
        {
            "id": bid,
            "type": conf["blocks"][bid]["type"],
            "settings": conf["blocks"][bid].get("settings", {}),
            "shopify_attributes": "",
        }
        for bid in order
    ]
    ctx = {
        "section": {
            "id": "qa-" + section_type,
            "settings": conf.get("settings", {}),
            "blocks": blocks,
            "shopify_attributes": "",
        },
        "page": page or {"title": "", "content": ""},
    }
    return env.from_string(src).render(**ctx)


STICKY_HEADER = """<div class="header-section" data-qa-sticky>
  <header class="site-header">
    <div class="site-header__inner" style="max-width:var(--max-width);margin:0 auto;
         display:flex;align-items:center;justify-content:space-between;
         padding:18px var(--section-padding-x);">
      <span class="type-label">Barreletics</span>
      <span class="type-label">Shop &nbsp; Learn &nbsp; Journal &nbsp; Help</span>
    </div>
  </header>
</div>"""


def build_page(name, conf, offline):
    from liquid import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader(SNIPPETS, ext=".liquid"))
    env.filters.setdefault("json", json.dumps)

    page = live_body(name, conf, offline)
    tpl = json.load(open(os.path.join(TEMPLATES, conf["template"])))
    body = "\n".join(render_section(env, tpl["sections"][sid]["type"],
                                    tpl["sections"][sid], page)
                     for sid in tpl["order"])
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — returns pages QA</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ASSETS}/design-tokens.css">
<link rel="stylesheet" href="{ASSETS}/barreletics-base.css">
<link rel="stylesheet" href="{ASSETS}/chrome.css">
</head><body>
{STICKY_HEADER}
{body}
</body></html>
"""


# ------------------------------------------------------------------------------ chrome


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Chrome:
    def __init__(self, width, height):
        self.port = free_port()
        scratch = os.path.join(HERE, ".chrome-profiles")
        os.makedirs(scratch, exist_ok=True)
        self.profile = tempfile.mkdtemp(prefix="returnsqa-", dir=scratch)
        self.proc = subprocess.Popen(
            [CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
             "--no-default-browser-check", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--allow-file-access-from-files",
             "--remote-debugging-port=%d" % self.port, "--remote-allow-origins=*",
             "--user-data-dir=" + self.profile,
             "--window-size=%d,%d" % (width, height), "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.ws = None
        self._id = 0
        self._connect()

    def _connect(self):
        deadline = time.time() + 45
        last = None
        while time.time() < deadline:
            try:
                conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
                conn.request("GET", "/json/list")
                raw = conn.getresponse().read()
                conn.close()
                for t in json.loads(raw):
                    if t.get("type") == "page":
                        self.ws = websocket.create_connection(
                            t["webSocketDebuggerUrl"], timeout=60,
                            max_size=256 * 1024 * 1024)
                        return
            except Exception as e:
                last = e
                time.sleep(0.4)
        raise RuntimeError("could not attach to headless Chrome: %r" % (last,))

    def send(self, method, params=None):
        self._id += 1
        mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError("%s: %s" % (method, msg["error"]))
                return msg.get("result", {})

    def evaluate(self, expr):
        r = self.send("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                           "awaitPromise": True})
        if r.get("exceptionDetails"):
            raise RuntimeError(json.dumps(r["exceptionDetails"])[:800])
        return r["result"].get("value")

    def close(self):
        try:
            if self.ws:
                self.ws.close()
        finally:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except Exception:
                self.proc.kill()
            shutil.rmtree(self.profile, ignore_errors=True)


# ------------------------------------------------------------------------------- audit

AUDIT = r"""
(() => {
  const vw = document.documentElement.clientWidth;
  const out = { vw, pageHeight: document.documentElement.scrollHeight,
                overflow: [], smallTap: [], liquidErrors: [],
                returnZap: null, portalLinks: [], headings: [] };

  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (r.right > vw + 1 || r.left < -1) {
      out.overflow.push({ sel: path(el), left: Math.round(r.left),
                          right: Math.round(r.right), w: Math.round(r.width) });
    }
  }

  const INTERACTIVE = 'a[href], button, input:not([type=hidden]), select, textarea, summary';
  for (const el of document.querySelectorAll(INTERACTIVE)) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    let h = r.height, w = r.width;
    const lab = el.closest('label');
    if (lab && lab !== el) {
      const lr = lab.getBoundingClientRect();
      h = Math.max(h, lr.height); w = Math.max(w, lr.width);
    }
    if (h < 44 || w < 44) {
      out.smallTap.push({ sel: path(el), w: Math.round(w * 10) / 10,
                          h: Math.round(h * 10) / 10,
                          text: (el.textContent || el.value || el.type || '')
                                  .replace(/\s+/g, ' ').trim().slice(0, 48) });
    }
  }

  // A section that failed to render leaves its Liquid tag in the text.
  const text = document.body.innerText || '';
  for (const m of text.matchAll(/\{\{[^}]{0,80}\}\}|\{%[^%]{0,80}%\}/g)) {
    out.liquidErrors.push(m[0]);
  }

  // The whole point of the returns templates: does the ReturnZap embed survive?
  const rz = document.querySelector('return-zap');
  if (rz) out.returnZap = { shopId: rz.getAttribute('shop-id'),
                            script: !!document.querySelector('script[src*="returnzap"]') };
  for (const a of document.querySelectorAll('a[href*="returns-portal"]')) {
    out.portalLinks.push((a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40));
  }
  for (const h of document.querySelectorAll('h1, h2')) {
    out.headings.push(h.tagName + ': ' + (h.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60));
  }

  function path(el) {
    const bits = [];
    for (let n = el; n && n.nodeType === 1 && bits.length < 3; n = n.parentElement) {
      let s = n.tagName.toLowerCase();
      if (n.id) { s += '#' + n.id; bits.unshift(s); break; }
      const c = (n.getAttribute('class') || '').trim().split(/\s+/).filter(Boolean)[0];
      if (c) s += '.' + c;
      bits.unshift(s);
    }
    return bits.join(' > ');
  }
  return out;
})()
"""


def shoot(ch, out_png, width, full_height):
    clip = {"x": 0, "y": 0, "width": width, "height": full_height, "scale": 1}
    shot = ch.send("Page.captureScreenshot",
                   {"format": "png", "clip": clip, "captureBeyondViewport": True})
    with open(out_png, "wb") as fh:
        fh.write(base64.b64decode(shot["data"]))


def run(name, path, width, no_shots):
    ch = Chrome(max(width, 500) + 140, 1200)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")
        ch.send("Emulation.setDeviceMetricsOverride",
                {"width": width, "height": 900, "deviceScaleFactor": 1,
                 "mobile": width < 700})
        ch.send("Page.navigate", {"url": "file://" + path})
        time.sleep(2.5)
        data = ch.evaluate(AUDIT)
        data["_meta"] = {"page": name, "width": width}
        if not no_shots:
            shoot(ch, os.path.join(HERE, "%s-%dpx.png" % (name, width)),
                  width, min(data["pageHeight"], 16000))
            # Fold shot: the part Andrew judges first, readable without a 15k-px scroll.
            shoot(ch, os.path.join(HERE, "%s-%dpx-fold.png" % (name, width)),
                  width, min(data["pageHeight"], 1400))
        with open(os.path.join(HERE, "%s-%dpx.json" % (name, width)), "w") as fh:
            json.dump(data, fh, indent=1)
        return data
    finally:
        ch.close()


def summarise(name, width, d):
    print("  %-24s %4dpx  height %6d  overflow %d  tap<44 %d  liquid-leaks %d  return-zap %s"
          % (name, width, d["pageHeight"], len(d["overflow"]), len(d["smallTap"]),
             len(d["liquidErrors"]), d["returnZap"] or "-"))
    for item in d["overflow"][:5]:
        print("      OVERFLOW %s" % json.dumps(item))
    for leak in d["liquidErrors"][:5]:
        print("      LIQUID LEAK %r" % leak)
    if d["portalLinks"]:
        print("      portal links (%d): %s" % (len(d["portalLinks"]), d["portalLinks"][:4]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-shots", action="store_true")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--pages", nargs="*", default=list(PAGES))
    ap.add_argument("--widths", nargs="*", type=int, default=[1440, 390])
    a = ap.parse_args()

    print("schema validation")
    problems = []
    for name in a.pages:
        problems += validate(PAGES[name]["template"])
    if problems:
        for p in problems:
            print("  FAIL %s" % p)
        raise SystemExit("schema validation failed — not rendering")
    print("  OK — every section type exists and every setting key is in its schema")

    report = {}
    for name in a.pages:
        html = build_page(name, PAGES[name], a.offline)
        path = os.path.join(HERE, "preview-%s.html" % name)
        with open(path, "w") as fh:
            fh.write(html)
        print("built %s (%d KB)" % (os.path.relpath(path, REPO), len(html) // 1024))
        for w in a.widths:
            d = run(name, path, w, a.no_shots)
            summarise(name, w, d)
            report["%s@%d" % (name, w)] = {
                "height": d["pageHeight"],
                "overflow": len(d["overflow"]),
                "smallTap": len(d["smallTap"]),
                "liquidLeaks": len(d["liquidErrors"]),
                "returnZap": d["returnZap"],
                "portalLinks": len(d["portalLinks"]),
            }
    with open(os.path.join(HERE, "audit-summary.json"), "w") as fh:
        json.dump(report, fh, indent=1)
    print("wrote %s" % os.path.relpath(os.path.join(HERE, "audit-summary.json"), REPO))


if __name__ == "__main__":
    main()
