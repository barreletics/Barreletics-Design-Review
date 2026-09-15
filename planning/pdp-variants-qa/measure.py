#!/usr/bin/env python3
"""Measure the three PDP previews: section-boundary gaps and image crop.

Two questions this answers, both of which were previously argued by eye:

1. Vertical rhythm — for every pair of adjacent sections, the *ink gap*: the
   empty band between the last painted thing in the upper section and the first
   painted thing in the lower one. That is what the eye reads as "space between
   sections", and unlike summing declared padding it accounts for collapsed
   margins, full-bleed media that runs to the section edge, and inner wrappers.

2. Cover crop — for every image rendered with object-fit:cover, how many source
   pixels fall outside the box on each edge. `fifty-fifty` media went full-bleed
   cover on 2026-08-08, so square product shots can lose their top or bottom.

macOS clamps headless Chrome windows to 500px, so 390px comes from a CDP
device-metrics override rather than --window-size.

Usage:
    python3 planning/pdp-variants-qa/measure.py            # both viewports
    python3 planning/pdp-variants-qa/measure.py --tag after
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9345
BASE = "http://127.0.0.1:8787/planning/pdp-variants-qa"

PAGES = ["closed", "open", "outdoor"]
VIEWPORTS = [("1440", 1440, 900, False), ("390", 390, 844, True)]

PROBE = r"""
(() => {
  const PAINTED = new Set(['IMG', 'VIDEO', 'SVG', 'CANVAS', 'HR', 'INPUT',
                           'BUTTON', 'TEXTAREA', 'SELECT']);

  // "Ink" = something that actually marks the page: a text node, a replaced
  // element, or a box the eye can see because it has its own border or a
  // background different from its parent. Whitespace-only wrappers are skipped
  // so padding on a wrapper counts as gap, not as content. Without the
  // border/background arm, a bordered card reads as ending where its last
  // paragraph ends, which overstates the gap by the card's own padding.
  function paints(cs) {
    const bw = ['borderTopWidth', 'borderBottomWidth', 'borderLeftWidth', 'borderRightWidth'];
    for (const p of bw)
      if (parseFloat(cs[p]) > 0 && cs[p.replace('Width', 'Style')] !== 'none') return true;
    return false;
  }
  function isInk(el) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return false;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    if (PAINTED.has(el.tagName)) return true;
    for (const n of el.childNodes)
      if (n.nodeType === 3 && n.textContent.trim()) return true;
    if (paints(cs)) return true;
    const parent = el.parentElement;
    if (parent && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' &&
        cs.backgroundColor !== getComputedStyle(parent).backgroundColor) return true;
    return false;
  }

  function inkBounds(section) {
    let top = Infinity, bottom = -Infinity;
    for (const el of section.querySelectorAll('*')) {
      if (!isInk(el)) continue;
      const r = el.getBoundingClientRect();
      if (r.top < top) top = r.top;
      if (r.bottom > bottom) bottom = r.bottom;
    }
    return {top, bottom};
  }

  const sections = Array.from(document.body.children).filter(el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none') return false;
    if (cs.position === 'fixed' || cs.position === 'sticky') return false;
    if (el.classList.contains('qa-banner')) return false;
    return el.getBoundingClientRect().height > 0;
  });

  const rows = sections.map(el => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const ink = inkBounds(el);
    return {
      name: (el.className || el.tagName).toString().split(/\s+/)
              .filter(c => c && !/^(section-frame|align-)/.test(c)).slice(0, 2).join('.')
            || el.tagName.toLowerCase(),
      top: Math.round(r.top + window.scrollY),
      bottom: Math.round(r.bottom + window.scrollY),
      height: Math.round(r.height),
      padTop: Math.round(parseFloat(cs.paddingTop)),
      padBottom: Math.round(parseFloat(cs.paddingBottom)),
      marTop: Math.round(parseFloat(cs.marginTop)),
      marBottom: Math.round(parseFloat(cs.marginBottom)),
      // Whitespace between the section edge and its first/last painted thing.
      leadIn: isFinite(ink.top) ? Math.round(ink.top - r.top) : null,
      leadOut: isFinite(ink.bottom) ? Math.round(r.bottom - ink.bottom) : null
    };
  });

  const gaps = [];
  for (let i = 0; i < rows.length - 1; i++) {
    const a = rows[i], b = rows[i + 1];
    gaps.push({
      boundary: a.name + ' → ' + b.name,
      upper: a.name, lower: b.name,
      // rect-to-rect slack (collapsed margins show up here)
      between: b.top - a.bottom,
      upperTail: a.leadOut, lowerHead: b.leadIn,
      inkGap: (a.leadOut || 0) + (b.top - a.bottom) + (b.leadIn || 0)
    });
  }

  // ---- cover-crop audit -------------------------------------------------
  const crops = [];
  for (const img of Array.from(document.images)) {
    const cs = getComputedStyle(img);
    if (cs.objectFit !== 'cover') continue;
    const r = img.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    const nw = img.naturalWidth, nh = img.naturalHeight;
    if (!nw || !nh) { crops.push({src: img.currentSrc || img.src, error: 'not loaded'}); continue; }
    // cover: scale = max(boxW/natW, boxH/natH)
    const scale = Math.max(r.width / nw, r.height / nh);
    const drawnW = nw * scale, drawnH = nh * scale;
    const overflowX = drawnW - r.width, overflowY = drawnH - r.height;
    // object-position resolves to a percentage/length pair
    const [px, py] = cs.objectPosition.split(' ');
    function frac(v, over) {
      if (v.endsWith('%')) return parseFloat(v) / 100;
      if (v === 'left' || v === 'top') return 0;
      if (v === 'right' || v === 'bottom') return 1;
      if (v === 'center') return 0.5;
      const n = parseFloat(v);
      return over ? n / over : 0.5;
    }
    const fx = frac(px || 'center', overflowX), fy = frac(py || px || 'center', overflowY);
    const cropTop = overflowY * fy, cropBottom = overflowY * (1 - fy);
    const cropLeft = overflowX * fx, cropRight = overflowX * (1 - fx);
    // find an owning section for readability
    let owner = img.closest('section, div.faq');
    let ownerName = owner ? (owner.className || '').toString().split(/\s+/)
                              .filter(c => c && c !== 'section-frame')[0] || owner.tagName : '?';
    let slot = img.closest('[data-slot]');
    crops.push({
      section: ownerName,
      slot: slot ? slot.getAttribute('data-slot') : null,
      alt: (img.alt || '').slice(0, 60),
      src: (img.currentSrc || img.src).split('/').pop().split('?')[0],
      natural: nw + 'x' + nh,
      naturalAR: +(nw / nh).toFixed(3),
      box: Math.round(r.width) + 'x' + Math.round(r.height),
      boxAR: +(r.width / r.height).toFixed(3),
      objectPosition: cs.objectPosition,
      // source pixels lost per edge (in original image px, not screen px)
      lostTopPx: Math.round(cropTop / scale),
      lostBottomPx: Math.round(cropBottom / scale),
      lostLeftPx: Math.round(cropLeft / scale),
      lostRightPx: Math.round(cropRight / scale),
      lostTopPct: +(100 * (cropTop / scale) / nh).toFixed(1),
      lostBottomPct: +(100 * (cropBottom / scale) / nh).toFixed(1),
      lostLeftPct: +(100 * (cropLeft / scale) / nw).toFixed(1),
      lostRightPct: +(100 * (cropRight / scale) / nw).toFixed(1),
      upscale: +(scale).toFixed(2)
    });
  }

  return {sections: rows, gaps, crops,
          docHeight: document.documentElement.scrollHeight};
})()
"""


def cdp(ws, method, params, _id=[0]):
    _id[0] += 1
    ws.send(json.dumps({"id": _id[0], "method": method, "params": params}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get("id") == _id[0]:
            return msg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="before")
    a = ap.parse_args()

    try:
        import websocket  # noqa: F401
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "websocket-client"])
    import websocket

    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--remote-debugging-port=%d" % PORT, "--remote-allow-origins=*",
         "--user-data-dir=" + os.path.join(HERE, ".measure-profile"),
         "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(60):
            try:
                urllib.request.urlopen("http://127.0.0.1:%d/json/version" % PORT, timeout=1)
                break
            except Exception:
                time.sleep(0.5)
        tabs = json.load(urllib.request.urlopen("http://127.0.0.1:%d/json/list" % PORT))
        tab = next(t for t in tabs if t.get("type") == "page")
        ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=120)
        cdp(ws, "Page.enable", {})
        cdp(ws, "Runtime.enable", {})

        out = {}
        for slug in PAGES:
            out[slug] = {}
            for vtag, w, h, mobile in VIEWPORTS:
                cdp(ws, "Emulation.setDeviceMetricsOverride",
                    {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": mobile})
                cdp(ws, "Page.navigate", {"url": "%s/preview-%s.html" % (BASE, slug)})
                time.sleep(6)
                r = cdp(ws, "Runtime.evaluate",
                        {"expression": PROBE, "returnByValue": True})
                val = r["result"]["result"].get("value")
                out[slug][vtag] = val if val else {"error": str(r)[:300]}
        ws.close()
    finally:
        proc.terminate()

    path = os.path.join(HERE, "measure-%s.json" % a.tag)
    json.dump(out, open(path, "w"), indent=2)
    print("wrote %s" % os.path.relpath(path, REPO))

    for slug in PAGES:
        for vtag, _, _, _ in VIEWPORTS:
            d = out[slug][vtag]
            if "error" in d:
                print("%s %s ERROR %s" % (slug, vtag, d["error"][:120]))
                continue
            print("\n===== %s @ %spx  (doc %dpx)" % (slug, vtag, d["docHeight"]))
            print("  %-56s %6s %6s %6s %6s" % ("boundary", "tail", "slack", "head", "GAP"))
            for g in d["gaps"]:
                print("  %-56s %6s %6s %6s %6s" % (
                    g["boundary"][:56], g["upperTail"], g["between"], g["lowerHead"], g["inkGap"]))


if __name__ == "__main__":
    main()
