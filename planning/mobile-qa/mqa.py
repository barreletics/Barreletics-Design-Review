#!/usr/bin/env python3
"""
Barreletics mobile QA sweep — iframe harness runner.

Why an iframe: headless Chrome on macOS clamps its window to a 500px minimum, so
--window-size=390,900 silently renders at 500px and only crops the screenshot.
An iframe sized to exactly 390px inside a 500px window gives a real 390px
viewport. The harness reads the iframe's document via --allow-file-access-from-files
and emits findings as JSON, so target pages are never modified.

Usage:
    python3 planning/mobile-qa/mqa.py                 # sweep the default page set at 390px
    python3 planning/mobile-qa/mqa.py --width 360     # small-Android spot check
    python3 planning/mobile-qa/mqa.py --pages "Barreletics PDP - Definitive-v19.html"
    python3 planning/mobile-qa/mqa.py --no-shots      # audit only, skip PNGs
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS = os.path.join(REPO, "docs")
OUTDIR = os.path.join(REPO, "planning", "mobile-qa")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Current-authority mocks under mobile QA.
DEFAULT_PAGES = [
    "Barreletics Home - Definitive-WORKING.html",
    "Barreletics PDP - Definitive-v19.html",
    "Barreletics Collection - Definitive-v18.html",
    "Barreletics FAQ - Definitive-v6.html",
    "Barreletics Help - Definitive-v3.html",
    "Barreletics Returns - Definitive-v3.html",
    "Barreletics SEO - Best Grippy Socks - Definitive-v36.html",
    "Barreletics Journal - Definitive-v5.html",
    "Barreletics Size Chart - Definitive-v1.html",
    "Barreletics Contact - Definitive-v1.html",
]

# Runs in the harness (parent) against the iframe document. Never touches the target file.
PROBE_JS = r"""
function mqaProbe(doc, win) {
  // The probe iframe is deliberately taller than the content so everything lays out
  // and lazy media loads; that makes documentElement.scrollHeight useless as a page
  // height, so measure the body box instead.
  var bodyRect = doc.body ? doc.body.getBoundingClientRect() : { bottom: 0 };
  var out = {
    vw: doc.documentElement.clientWidth,
    bodyOverflowX: doc.body ? win.getComputedStyle(doc.body).overflowX : 'n/a',
    scrollWidth: Math.max(doc.documentElement.scrollWidth, doc.body ? doc.body.scrollWidth : 0),
    pageHeight: Math.ceil(Math.max(bodyRect.bottom, doc.body ? doc.body.scrollHeight : 0)),
    overflow: [], overflowInScroller: [], tapTargets: [], smallText: [], stickies: [],
    counts: {}
  };
  var VW = out.vw;

  function label(el) {
    var s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    var cls = (el.getAttribute('class') || '').trim().split(/\s+/).filter(Boolean).slice(0, 3);
    if (cls.length) s += '.' + cls.join('.');
    return s;
  }
  function snippet(el) {
    var t = (el.textContent || '').replace(/\s+/g, ' ').trim();
    return t.length > 60 ? t.slice(0, 60) + '\u2026' : t;
  }
  function visible(el, cs, r) {
    if (cs.display === 'none' || cs.visibility === 'hidden') return false;
    if (parseFloat(cs.opacity) === 0) return false;
    if (r.width <= 0 || r.height <= 0) return false;
    return true;
  }
  // An ancestor that scrolls or clips horizontally means the overflow is contained
  // and the page itself will not scroll sideways, so it is not a real defect.
  // body { overflow-x: hidden } is a page-wide band-aid, not a real scroller: it hides
  // the sideways scrollbar while the content stays clipped. Stop before body so those
  // offenders still get reported.
  function inScroller(el) {
    var p = el.parentElement;
    while (p && p !== doc.body && p !== doc.documentElement) {
      var ox = win.getComputedStyle(p).overflowX;
      if (ox === 'auto' || ox === 'scroll' || ox === 'hidden' || ox === 'clip') return label(p) + ' [' + ox + ']';
      p = p.parentElement;
    }
    return null;
  }

  var all = doc.querySelectorAll('*');
  out.counts.elements = all.length;
  var offenders = new Set();

  for (var i = 0; i < all.length; i++) {
    var el = all[i];
    var tag = el.tagName.toLowerCase();
    if (tag === 'script' || tag === 'style' || tag === 'head' || tag === 'meta' || tag === 'link') continue;
    var cs = win.getComputedStyle(el);
    var r = el.getBoundingClientRect();
    if (!visible(el, cs, r)) continue;

    // 1. horizontal overflow
    var right = r.left + r.width;
    if (right > VW + 1 || r.left < -1) {
      offenders.add(el);
      var rec = {
        sel: label(el), text: snippet(el),
        left: Math.round(r.left * 10) / 10,
        right: Math.round(right * 10) / 10,
        width: Math.round(r.width * 10) / 10,
        over: Math.round((right - VW) * 10) / 10,
        scroller: inScroller(el),
        pos: cs.position,
        nowrap: cs.whiteSpace === 'nowrap' || cs.whiteSpace === 'pre',
        minW: cs.minWidth
      };
      rec.rootCause = !offenders.has(el.parentElement);
      (rec.scroller ? out.overflowInScroller : out.overflow).push(rec);
    }

    // 2. tap targets under 44px tall
    if (/^(a|button|summary|input|select|textarea)$/.test(tag) || el.getAttribute('role') === 'button') {
      if (tag === 'input' && /^(hidden)$/.test(el.type || '')) continue;
      if (r.height < 44 && r.height > 0 && r.width > 0) {
        out.tapTargets.push({
          sel: label(el), text: snippet(el),
          h: Math.round(r.height * 10) / 10,
          w: Math.round(r.width * 10) / 10
        });
      }
    }

    // 3. body copy rendered under 12px
    var hasOwnText = false;
    for (var n = 0; n < el.childNodes.length; n++) {
      var cn = el.childNodes[n];
      if (cn.nodeType === 3 && cn.nodeValue.trim().length > 1) { hasOwnText = true; break; }
    }
    if (hasOwnText) {
      var fs = parseFloat(cs.fontSize);
      if (fs && fs < 12) {
        out.smallText.push({ sel: label(el), text: snippet(el), px: Math.round(fs * 100) / 100 });
      }
    }

    // 4. sticky / fixed inventory (overlap analysis done downstream)
    if (cs.position === 'sticky' || cs.position === 'fixed') {
      out.stickies.push({
        sel: label(el), text: snippet(el), pos: cs.position,
        top: cs.top, bottom: cs.bottom,
        z: cs.zIndex,
        h: Math.round(r.height * 10) / 10,
        y: Math.round(r.top * 10) / 10
      });
    }
  }

  function byOver(a, b) { return b.over - a.over; }
  out.overflow.sort(byOver);
  out.overflowInScroller.sort(byOver);
  out.tapTargets.sort(function (a, b) { return a.h - b.h; });
  out.counts.overflowTotal = out.overflow.length;
  out.counts.overflowRoots = out.overflow.filter(function (o) { return o.rootCause; }).length;
  out.overflow = out.overflow.slice(0, 60);
  out.overflowInScroller = out.overflowInScroller.slice(0, 20);
  out.tapTargets = out.tapTargets.slice(0, 60);
  out.smallText = out.smallText.slice(0, 40);
  return out;
}
"""

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8"><title>mqa</title>
<style>html,body{{margin:0;padding:0;background:#fff}}iframe{{display:block;border:0;margin:0}}</style>
</head><body>
<iframe id="f" width="{width}" height="{height}" src="{src}"></iframe>
<script>
{probe}
function emit(obj) {{
  var s = document.createElement('script');
  s.type = 'application/json';
  s.id = 'mqa-result';
  s.textContent = JSON.stringify(obj).replace(/</g, '\\\\u003c');
  document.body.appendChild(s);
}}
window.addEventListener('load', function () {{
  setTimeout(function () {{
    try {{
      var f = document.getElementById('f');
      emit(mqaProbe(f.contentDocument, f.contentWindow));
    }} catch (e) {{
      emit({{ error: String(e) }});
    }}
  }}, {settle});
}});
</script>
</body></html>
"""


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace(".html", "")).strip("-")


def run_chrome(args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                           "--hide-scrollbars", "--allow-file-access-from-files",
                           "--force-device-scale-factor=1"] + args,
                          capture_output=True, text=True, timeout=300)


def probe(page, width, height, settle=1200):
    """Render `page` in a `width`px iframe and return the JSON findings."""
    src = page.replace(" ", "%20").replace("&", "&amp;")
    harness = os.path.join(DOCS, "__mqa-harness-%s-%d.html" % (slug(page), width))
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=height, src=src,
                                probe=PROBE_JS, settle=settle))
    try:
        win_w = max(width + 110, 500)  # Chrome clamps windows to 500px minimum
        r = run_chrome(["--window-size=%d,%d" % (win_w, min(height + 40, 30000)),
                        "--virtual-time-budget=6000", "--dump-dom", harness])
        m = re.search(r'<script type="application/json" id="mqa-result">(.*?)</script>',
                      r.stdout, re.S)
        if not m:
            return {"error": "no result payload", "stderr": r.stderr[-500:]}
        return json.loads(m.group(1).replace("\\u003c", "<"))
    finally:
        if os.path.exists(harness):
            os.remove(harness)


def screenshot(page, width, page_height, out_png):
    """Full-page PNG at a true `width`px viewport, cropped free of the harness gutter."""
    h = min(int(page_height) + 20, 16000)
    src = page.replace(" ", "%20").replace("&", "&amp;")
    harness = os.path.join(DOCS, "__mqa-shot-%s-%d.html" % (slug(page), width))
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=h, src=src, probe="", settle=200))
    tmp = os.path.join(tempfile.gettempdir(), "mqa-raw.png")
    try:
        run_chrome(["--window-size=%d,%d" % (max(width + 110, 500), h),
                    "--virtual-time-budget=8000", "--screenshot=" + tmp, harness])
        if not os.path.exists(tmp):
            return False
        try:
            from PIL import Image
            im = Image.open(tmp)
            im.crop((0, 0, min(width, im.width), im.height)).save(out_png)
        except Exception:
            shutil.copy(tmp, out_png)
        return True
    finally:
        for f in (harness, tmp):
            if os.path.exists(f):
                os.remove(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=390)
    ap.add_argument("--pages", nargs="*", default=None)
    ap.add_argument("--no-shots", action="store_true")
    ap.add_argument("--json-out", default=None)
    a = ap.parse_args()

    pages = a.pages if a.pages else DEFAULT_PAGES
    os.makedirs(OUTDIR, exist_ok=True)
    results = {}

    for p in pages:
        if not os.path.exists(os.path.join(DOCS, p)):
            print("MISSING: %s" % p, file=sys.stderr)
            continue
        r = probe(p, a.width, 24000)
        # Stickies are meaningless in a 24000px-tall iframe; re-measure them against a
        # real phone viewport so top/bottom stacking is representative.
        short = probe(p, a.width, 844)
        if not short.get("error"):
            r["stickies"] = short.get("stickies", [])
            r["stickyViewport"] = 844
        results[p] = r
        if r.get("error"):
            print("%-58s ERROR %s" % (p[:58], r["error"]))
            continue
        if r["vw"] != a.width:
            print("%-58s HARNESS BROKEN vw=%s" % (p[:58], r["vw"]))
            continue
        print("%-58s vw=%s overflow=%d(roots %d) tap<44=%d text<12=%d sticky=%d h=%d"
              % (p[:58], r["vw"], r["counts"]["overflowTotal"], r["counts"]["overflowRoots"],
                 len(r["tapTargets"]), len(r["smallText"]), len(r["stickies"]), r["pageHeight"]))
        if not a.no_shots:
            png = os.path.join(OUTDIR, "%s-%dpx.png" % (slug(p), a.width))
            screenshot(p, a.width, r["pageHeight"], png)

    out = a.json_out or os.path.join(OUTDIR, "findings-%dpx.json" % a.width)
    with open(out, "w") as fh:
        json.dump(results, fh, indent=1)
    print("\nJSON: %s" % out)


if __name__ == "__main__":
    main()
