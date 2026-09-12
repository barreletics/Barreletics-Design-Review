#!/usr/bin/env python3
"""Headless-Chrome QA sweep over the repo's preview HTML files.

macOS clamps headless windows to 500px wide, so the mobile pass drives a real
device-metrics override through CDP rather than --window-size (same approach the
partner-pages and pdp-variants harnesses use).

Checks per page x viewport: horizontal overflow, tap targets under 44px,
text under 12px that is not the approved 11px uppercase label, overlapping
sticky/fixed elements, broken images, and leaked Liquid delimiters.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9333

PAGES = [
    ("pdp-closed", "planning/pdp-variants-qa/preview-closed.html"),
    ("pdp-open", "planning/pdp-variants-qa/preview-open.html"),
    ("pdp-outdoor", "planning/pdp-variants-qa/preview-outdoor.html"),
    ("partners", "planning/partner-pages-qa/preview-partners.html"),
    ("wholesale", "planning/partner-pages-qa/preview-wholesale.html"),
    ("studio-program", "planning/partner-pages-qa/preview-studio-program.html"),
    ("ambassador", "planning/partner-pages-qa/preview-ambassador.html"),
    ("returns", "planning/returns-pages-qa/preview-returns.html"),
    ("returns-portal", "planning/returns-pages-qa/preview-returns-portal.html"),
    ("size-chart", "planning/returns-pages-qa/preview-size-chart.html"),
    ("compare", "planning/returns-pages-qa/preview-compare-open-vs-closed.html"),
    ("reviews", "planning/returns-pages-qa/preview-reviews.html"),
    ("free-people", "planning/returns-pages-qa/preview-free-people.html"),
]

VIEWPORTS = [("1440", 1440, 900), ("390", 390, 844)]

PROBE = r"""
(() => {
  const out = {overflow: [], tap: [], tiny: [], sticky: [], brokenImg: [], liquid: []};
  const vw = document.documentElement.clientWidth;
  out.docWidth = document.documentElement.scrollWidth;
  out.viewport = vw;
  const sel = (el) => {
    let s = el.tagName.toLowerCase();
    if (el.className && typeof el.className === 'string')
      s += '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.');
    return s;
  };
  const all = Array.from(document.querySelectorAll('body *'));
  for (const el of all) {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || r.width === 0 || r.height === 0) continue;

    if (r.right > vw + 1 || r.left < -1) {
      if (cs.position !== 'fixed')
        out.overflow.push({sel: sel(el), left: Math.round(r.left), right: Math.round(r.right)});
    }
    if (/^(a|button)$/i.test(el.tagName) || el.getAttribute('role') === 'button' ||
        (el.tagName === 'INPUT' && /button|submit|checkbox|radio/i.test(el.type || ''))) {
      if ((r.height < 44 || r.width < 44) && el.textContent.trim())
        out.tap.push({sel: sel(el), w: Math.round(r.width), h: Math.round(r.height),
                      text: el.textContent.trim().slice(0, 40)});
    }
    const kids = Array.from(el.childNodes).filter(n => n.nodeType === 3 && n.textContent.trim());
    if (kids.length) {
      const fs = parseFloat(cs.fontSize);
      const upper = cs.textTransform === 'uppercase';
      if (fs < 12 && !(Math.round(fs) === 11 && upper))
        out.tiny.push({sel: sel(el), size: fs, upper,
                       text: kids.map(n => n.textContent.trim()).join(' ').slice(0, 40)});
    }
    if (cs.position === 'fixed' || cs.position === 'sticky')
      out.sticky.push({sel: sel(el), top: Math.round(r.top), bottom: Math.round(r.bottom),
                       z: cs.zIndex, pos: cs.position});
    if (/\{\{|\{%/.test(el.textContent || '') && el.children.length === 0)
      out.liquid.push({sel: sel(el), text: el.textContent.trim().slice(0, 60)});
  }
  out.brokenImg = Array.from(document.images)
    .filter(i => i.complete && i.naturalWidth === 0)
    .map(i => i.currentSrc || i.src);
  for (let i = 0; i < out.sticky.length; i++)
    for (let j = i + 1; j < out.sticky.length; j++) {
      const a = out.sticky[i], b = out.sticky[j];
      if (a.bottom > b.top && b.bottom > a.top)
        out.overlapSticky = (out.overlapSticky || []).concat([[a.sel, b.sel]]);
    }
  return out;
})()
"""


def cdp(ws, method, params, _id=[0]):
    import websocket  # noqa
    _id[0] += 1
    ws.send(json.dumps({"id": _id[0], "method": method, "params": params}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get("id") == _id[0]:
            return msg


def main():
    try:
        import websocket  # noqa: F401
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "websocket-client"])
    import websocket

    profile = os.path.join(HERE, ".chrome-profile")
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--remote-debugging-port=%d" % PORT, "--remote-allow-origins=*",
         "--user-data-dir=" + profile,
         "--allow-file-access-from-files", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(60):
            try:
                urllib.request.urlopen("http://127.0.0.1:%d/json/version" % PORT, timeout=1)
                break
            except Exception:
                time.sleep(0.5)

        # Recent Chrome rejects GET on /json/new, so reuse the launch tab instead.
        tabs = json.load(urllib.request.urlopen("http://127.0.0.1:%d/json/list" % PORT))
        tab = next(t for t in tabs if t.get("type") == "page")
        ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=90)
        cdp(ws, "Page.enable", {})
        cdp(ws, "Runtime.enable", {})

        results = {}
        for name, rel in PAGES:
            path = os.path.join(REPO, rel)
            if not os.path.exists(path):
                results[name] = {"error": "missing " + rel}
                continue
            results[name] = {}
            for tag, w, h in VIEWPORTS:
                cdp(ws, "Emulation.setDeviceMetricsOverride",
                    {"width": w, "height": h, "deviceScaleFactor": 1,
                     "mobile": tag == "390"})
                cdp(ws, "Page.navigate", {"url": "file://" + path})
                time.sleep(3.5)
                r = cdp(ws, "Runtime.evaluate",
                        {"expression": PROBE, "returnByValue": True, "awaitPromise": False})
                results[name][tag] = r["result"]["result"].get("value", {"error": str(r)[:200]})
        ws.close()
    finally:
        proc.terminate()

    json.dump(results, open(os.path.join(HERE, "qa-sweep.json"), "w"), indent=2)

    for name, per in results.items():
        if "error" in per:
            print("%-16s %s" % (name, per["error"]))
            continue
        for tag, r in per.items():
            if "error" in r:
                print("%-16s %-5s ERROR %s" % (name, tag, r["error"][:90]))
                continue
            print("%-16s %-5s overflow=%-3d tap<44=%-3d tiny=%-3d brokenImg=%-3d stickyOverlap=%d"
                  % (name, tag, len(r["overflow"]), len(r["tap"]), len(r["tiny"]),
                     len(r["brokenImg"]), len(r.get("overlapSticky", []))))
            for k, label in (("overflow", "OVERFLOW"), ("tiny", "TINY"), ("brokenImg", "IMG404"),
                             ("liquid", "LIQUID")):
                for item in r[k][:6]:
                    print("      %s %s" % (label, json.dumps(item)[:150]))
            for item in r["tap"][:6]:
                print("      TAP %s" % json.dumps(item)[:150])


if __name__ == "__main__":
    main()
