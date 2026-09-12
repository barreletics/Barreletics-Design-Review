#!/usr/bin/env python3
"""
Partner page QA harness — renders the four partner templates and audits them.

The partner pages ship as Liquid sections composed by templates/page.*.json, so they
cannot be opened in a browser directly. This script renders each template for real:
it feeds the template JSON in as `section.settings` / `section.blocks` and runs the
section Liquid through python-liquid, with the handful of Shopify-only tags
({% schema %}, {% form %}, {% render %}) shimmed. Stylesheets are linked live out of
shopify-build/assets, so a preview always reflects the current working tree — edit a
section, re-run, re-shoot.

A sticky header stand-in carrying the real `.header-section` / `.site-header` classes
is included so anchor-jump CTAs can be checked against the sticky chrome.

Mobile: macOS headless Chrome clamps windows to 500px, so 390px comes from a CDP
Emulation.setDeviceMetricsOverride on an oversized window (same approach as
planning/header-type-qa/probe.py), not from --window-size.

Usage:
    python3 planning/partner-pages-qa/build.py              # render, shoot, audit
    python3 planning/partner-pages-qa/build.py --no-shots   # render + audit only
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
TEMPLATES = os.path.join(BUILD, "templates")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ASSETS = "../../shopify-build/assets"

PAGES = {
    "ambassador": "page.ambassador.json",
    "studio-program": "page.studio-program.json",
    "wholesale": "page.wholesale.json",
    "partners": "page.partners.json",
}


# --------------------------------------------------------------------------- render


def strip_shopify_tags(src):
    """Reduce a Shopify section to Liquid python-liquid can parse."""
    src = re.sub(r"\{%-?\s*schema\s*-?%\}.*?\{%-?\s*endschema\s*-?%\}", "", src, flags=re.S)
    src = re.sub(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", "", src, flags=re.S)

    # {% form 'contact' %} posts to /contact; the QA render only needs the element.
    src = re.sub(
        r"\{%-?\s*form\s+'contact'\s*-?%\}",
        '<form method="post" action="/contact#contact_form" id="contact_form" '
        'accept-charset="UTF-8">',
        src,
    )
    src = re.sub(r"\{%-?\s*endform\s*-?%\}", "</form>", src)

    # form.posted_successfully? / form.errors are never truthy on a GET render.
    src = src.replace("form.posted_successfully?", "false").replace("form.errors", "false")

    src = re.sub(r"\{\{\s*(section|block)\.shopify_attributes\s*\}\}", "", src)
    src = re.sub(r"\{%-?\s*render\s+'button'([^%]*?)-?%\}", _button, src)
    return src


def _button(match):
    """Inline snippets/button.liquid for the one call signature the partner pages use."""
    raw = match.group(1)
    args = {k: v for k, v in re.findall(r"(\w+):\s*'([^']*)'", raw)}
    label = re.search(r"label:\s*([\w.]+)", raw)
    style = args.get("style") or "primary"
    size = args.get("size") or "md"
    btype = args.get("type") or "button"
    cls = "btn btn--%s%s" % (style, " btn--lg" if size == "lg" else "")
    text = "{{ %s }}" % label.group(1) if label else "Submit"
    return '<button type="%s" class="%s">%s</button>' % (btype, cls, text)


def render_section(section_type, conf):
    from liquid import Environment

    env = Environment()
    env.filters.setdefault("default_errors", lambda v: "")
    env.filters.setdefault("json", json.dumps)

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
        }
    }
    return env.from_string(src).render(**ctx)


# Stand-in for header-group: real classes and real height, no menu data required.
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


def build_page(name):
    tpl = json.load(open(os.path.join(TEMPLATES, PAGES[name])))
    body = "\n".join(render_section(tpl["sections"][sid]["type"], tpl["sections"][sid])
                     for sid in tpl["order"])
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — partner page QA</title>
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


# ---------------------------------------------------------------------------- chrome


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Chrome:
    def __init__(self, width, height):
        self.port = free_port()
        # Keep the throwaway profile inside the repo: the system temp dir is not always
        # writable to the process running this script, and Chrome fails silently if the
        # profile cannot be created.
        scratch = os.path.join(HERE, ".chrome-profiles")
        os.makedirs(scratch, exist_ok=True)
        self.profile = tempfile.mkdtemp(prefix="partnerqa-", dir=scratch)
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
                # http.client, not urllib: urllib honours HTTP(S)_PROXY, which sends
                # loopback DevTools requests to a proxy that cannot answer them.
                conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
                conn.request("GET", "/json/list")
                raw = conn.getresponse().read()
                conn.close()
                for t in json.loads(raw):
                    if t.get("type") == "page":
                        self.ws = websocket.create_connection(
                            t["webSocketDebuggerUrl"], timeout=60,
                            max_size=128 * 1024 * 1024)
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


# ----------------------------------------------------------------------------- audit

AUDIT = r"""
(() => {
  const vw = document.documentElement.clientWidth;
  const out = { vw, docScrollWidth: document.documentElement.scrollWidth,
                pageHeight: document.documentElement.scrollHeight,
                overflow: [], smallTap: [], smallText: [], stickyOverlap: [] };

  // --- horizontal overflow: elements painting past the right edge or left of zero
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (r.right > vw + 1 || r.left < -1) {
      out.overflow.push({ sel: path(el), left: Math.round(r.left),
                          right: Math.round(r.right), w: Math.round(r.width) });
    }
  }

  // --- tap targets: interactive elements smaller than 44x44
  //     Labels wrapping a checkbox are measured as the whole hit area, which is what
  //     a finger actually gets, so a small <input> inside a big <label> is not a miss.
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

  // --- text under 12px, measured on elements that actually paint their own text
  for (const el of document.querySelectorAll('body *')) {
    const own = Array.from(el.childNodes)
      .filter(n => n.nodeType === 3 && n.textContent.trim())
      .map(n => n.textContent.trim()).join(' ');
    if (!own) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < 12) {
      out.smallText.push({ sel: path(el), fontSize: fs,
                           text: own.replace(/\s+/g, ' ').slice(0, 60) });
    }
  }

  // --- sticky / fixed chrome vs the in-page anchors the CTAs jump to
  const sticky = Array.from(document.querySelectorAll('body *')).filter(el => {
    const p = getComputedStyle(el).position;
    return p === 'sticky' || p === 'fixed';
  }).map(el => ({ sel: path(el), pos: getComputedStyle(el).position,
                  h: Math.round(el.getBoundingClientRect().height) }));
  out.sticky = sticky;

  const stickyH = sticky.reduce((m, s) => Math.max(m, s.h), 0);
  for (const a of document.querySelectorAll('a[href^="#"]')) {
    const id = a.getAttribute('href').slice(1);
    const target = id && document.getElementById(id);
    if (!target) { out.stickyOverlap.push({ anchor: a.getAttribute('href'),
                                            problem: 'target missing' }); continue; }
    // After a hash jump the target's top sits at scroll origin minus its
    // scroll-margin-top, so the usable clearance is that margin plus whatever padding
    // sits above the first heading. Anything less than the sticky band is hidden.
    const heading = target.querySelector('h1,h2,h3');
    const pad = heading
      ? heading.getBoundingClientRect().top - target.getBoundingClientRect().top : 0;
    const margin = parseFloat(getComputedStyle(target).scrollMarginTop) || 0;
    const clearance = pad + margin;
    if (clearance < stickyH) {
      out.stickyOverlap.push({ anchor: a.getAttribute('href'), stickyH,
                               scrollMarginTop: margin,
                               clearance: Math.round(clearance),
                               problem: 'heading lands under sticky header' });
    }
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


def run(name, path, width, mobile, no_shots):
    ch = Chrome(max(width, 500) + 140, 1200)
    try:
        ch.send("Page.enable")
        ch.send("Runtime.enable")
        ch.send("Emulation.setDeviceMetricsOverride",
                {"width": width, "height": 900, "deviceScaleFactor": 1, "mobile": mobile})
        ch.send("Page.navigate", {"url": "file://" + path})
        time.sleep(2.5)
        data = ch.evaluate(AUDIT)
        data["_meta"] = {"page": name, "width": width, "mobile": mobile}
        if not no_shots:
            shoot(ch, os.path.join(HERE, "%s-%dpx.png" % (name, width)),
                  width, min(data["pageHeight"], 16000))
        with open(os.path.join(HERE, "%s-%dpx.json" % (name, width)), "w") as fh:
            json.dump(data, fh, indent=1)
        return data
    finally:
        ch.close()


def summarise(name, width, d):
    print("  %-14s %4dpx  height %5d  overflow %d  tap<44 %d  text<12px %d  sticky-clash %d"
          % (name, width, d["pageHeight"], len(d["overflow"]),
             len(d["smallTap"]), len(d["smallText"]), len(d["stickyOverlap"])))
    for k, label in (("overflow", "OVERFLOW"), ("stickyOverlap", "STICKY")):
        for item in d[k][:6]:
            print("      %s %s" % (label, json.dumps(item)))
    seen = set()
    for item in d["smallTap"][:40]:
        key = item["sel"]
        if key in seen:
            continue
        seen.add(key)
        print("      TAP  %s  %sx%s  %r" % (item["sel"], item["w"], item["h"], item["text"]))
    seen = set()
    for item in d["smallText"][:40]:
        key = (item["sel"], item["fontSize"])
        if key in seen:
            continue
        seen.add(key)
        print("      TEXT %s  %spx  %r" % (item["sel"], item["fontSize"], item["text"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-shots", action="store_true")
    ap.add_argument("--pages", nargs="*", default=list(PAGES))
    ap.add_argument("--widths", nargs="*", type=int, default=[1440, 390])
    a = ap.parse_args()

    report = {}
    for name in a.pages:
        html = build_page(name)
        path = os.path.join(HERE, "preview-%s.html" % name)
        with open(path, "w") as fh:
            fh.write(html)
        print("built %s (%d KB)" % (os.path.relpath(path, REPO), len(html) // 1024))
        for w in a.widths:
            d = run(name, path, w, mobile=(w < 700), no_shots=a.no_shots)
            summarise(name, w, d)
            report["%s@%d" % (name, w)] = {
                "height": d["pageHeight"],
                "overflow": len(d["overflow"]),
                "smallTap": len(d["smallTap"]),
                "smallText": len(d["smallText"]),
                "stickyOverlap": len(d["stickyOverlap"]),
            }
    with open(os.path.join(HERE, "audit-summary.json"), "w") as fh:
        json.dump(report, fh, indent=1)


if __name__ == "__main__":
    main()
