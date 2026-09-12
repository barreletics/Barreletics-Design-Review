#!/usr/bin/env python3
"""
Footer sweep QA — crop the sitewide footer out of a docs mock at a true viewport width.

Headless Chrome on macOS clamps its window to a 500px minimum, so --window-size=390,...
silently renders at 500px. The page is loaded in an iframe sized to the exact target
width inside a wider window, which gives a real viewport. Target files are never
modified; the harness is written next to them and deleted afterwards.

Usage:
    python3 planning/footer-sweep-qa/footer_shot.py --width 1440 --pages "Barreletics Contact - Definitive-v1.html"
    python3 planning/footer-sweep-qa/footer_shot.py --width 390
"""

import argparse
import json
import os
import re
import subprocess
import tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS = os.path.join(REPO, "docs")
OUTDIR = os.path.join(REPO, "planning", "footer-sweep-qa")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DEFAULT_PAGES = [
    "Barreletics Contact - Definitive-v1.html",
    "Barreletics Returns - Definitive-v3.html",
    "Barreletics Size Chart - Definitive-v1.html",
    "Barreletics Track Order - Definitive-v1.html",
    "Barreletics Returns Portal - Definitive-v1.html",
    "Barreletics Help - Definitive-v4.html",
    "Barreletics Journal - Definitive-v6.html",
    "Barreletics Collection - Definitive-v19.html",
    "Barreletics SEO - Best Grippy Socks - Definitive-v37.html",
]

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8"><title>fs</title>
<style>html,body{{margin:0;padding:0;background:#fff}}iframe{{display:block;border:0;margin:0}}</style>
</head><body>
<iframe id="f" width="{width}" height="{height}" src="{src}"></iframe>
<script>
function emit(obj) {{
  var s = document.createElement('script');
  s.type = 'application/json'; s.id = 'fs-result';
  s.textContent = JSON.stringify(obj).replace(/</g, '\\\\u003c');
  document.body.appendChild(s);
}}
window.addEventListener('load', function () {{
  setTimeout(function () {{
    try {{
      var d = document.getElementById('f').contentDocument;
      var f = d.querySelector('footer.site-footer') || d.querySelector('footer');
      var r = f.getBoundingClientRect();
      var body = d.body.getBoundingClientRect();
      emit({{
        footerTop: Math.floor(r.top), footerHeight: Math.ceil(r.height),
        pageHeight: Math.ceil(Math.max(body.bottom, d.body.scrollHeight)),
        heading: (f.querySelector('.fn-signup h2') || {{}}).textContent || '',
        checks: Array.prototype.map.call(
          f.querySelectorAll('.fn-value__text'), function (n) {{ return n.textContent; }})
      }});
    }} catch (e) {{ emit({{ error: String(e) }}); }}
  }}, 900);
}});
</script>
</body></html>
"""


CLIP_HARNESS = """<!doctype html>
<html><head><meta charset="utf-8"><title>fs-clip</title>
<style>html,body{{margin:0;padding:0;background:#fff}}iframe{{display:block;border:0;margin:0}}</style>
</head><body>
<iframe id="f" width="{width}" height="{box}" src="{src}"></iframe>
<script>
// Hide every ancestor sibling of the footer so the footer sits at the top of the document.
// Scrolling to the bottom instead is unreliable: lazy media and web fonts keep growing the
// page, so the scroll target moves while the screenshot is taken. This mutates only the
// in-memory iframe document — the file on disk is never touched.
setInterval(function () {{
  try {{
    var d = document.getElementById('f').contentDocument;
    var el = d.querySelector('footer.site-footer') || d.querySelector('footer');
    for (var n = el; n && n !== d.body; n = n.parentElement) {{
      var kids = n.parentElement.children;
      for (var i = 0; i < kids.length; i++) {{
        if (kids[i] !== n) kids[i].style.display = 'none';
      }}
    }}
    d.body.style.margin = '0';
    d.body.style.paddingTop = '0';
  }} catch (e) {{}}
}}, 150);
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


def harness_path(page, width, kind):
    return os.path.join(DOCS, "__fs-%s-%s-%d.html" % (kind, slug(page), width))


def write_harness(path, page, width, height):
    src = page.replace(" ", "%20").replace("&", "&amp;")
    with open(path, "w") as fh:
        fh.write(HARNESS.format(width=width, height=height, src=src))


def probe(page, width):
    h = harness_path(page, width, "probe")
    write_harness(h, page, width, 30000)
    try:
        r = run_chrome(["--window-size=%d,%d" % (max(width + 120, 500), 1200),
                        "--virtual-time-budget=6000", "--dump-dom", h])
        m = re.search(r'<script type="application/json" id="fs-result">(.*?)</script>',
                      r.stdout, re.S)
        if not m:
            return {"error": "no payload", "stderr": r.stderr[-400:]}
        return json.loads(m.group(1).replace("\\u003c", "<"))
    finally:
        if os.path.exists(h):
            os.remove(h)


def shoot(page, width, info, out_png):
    """Screenshot only the footer box."""
    box_h = info["footerHeight"] + 8
    h = harness_path(page, width, "shot")
    src = page.replace(" ", "%20").replace("&", "&amp;")
    with open(h, "w") as fh:
        fh.write(CLIP_HARNESS.format(width=width, src=src, box=box_h))
    tmp = os.path.join(tempfile.gettempdir(), "fs-raw-%d.png" % width)
    try:
        run_chrome(["--window-size=%d,%d" % (max(width, 500), box_h),
                    "--virtual-time-budget=9000", "--screenshot=" + tmp, h])
        if not os.path.exists(tmp):
            return False
        from PIL import Image
        im = Image.open(tmp)
        im.crop((0, 0, min(width, im.width), im.height)).save(out_png)
        return True
    finally:
        for f in (h, tmp):
            if os.path.exists(f):
                os.remove(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--pages", nargs="*", default=None)
    a = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)
    for p in (a.pages or DEFAULT_PAGES):
        if not os.path.exists(os.path.join(DOCS, p)):
            print("MISSING: %s" % p)
            continue
        info = probe(p, a.width)
        if info.get("error"):
            print("%-52s ERROR %s" % (p[:52], info["error"]))
            continue
        stale = "10%" in info["heading"] or any("10%" in c for c in info["checks"])
        png = os.path.join(OUTDIR, "%s-%dpx-footer.png" % (slug(p), a.width))
        ok = shoot(p, a.width, info, png)
        print("%-52s h=%-24s stale10=%s shot=%s"
              % (p[:52], info["heading"][:24], stale, "ok" if ok else "FAIL"))
        print("    checks: %s" % " | ".join(info["checks"]))


if __name__ == "__main__":
    main()
