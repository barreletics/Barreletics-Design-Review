#!/usr/bin/env python3
"""
Computed-type probe for the Blog / Article / About previews.

Reads back the rendered font-size / weight / line-height / letter-spacing for the
type-bearing selectors on each surface, so Type OS conformance is checked against
what the browser computes rather than by reading CSS. Uses the same iframe trick
as build.py so 390px is a real 390px viewport.

Usage:
    python3 planning/blog-about-type-qa/verify.py            # 1440 and 390
    python3 planning/blog-about-type-qa/verify.py --width 390
"""

import argparse
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

TARGETS = {
    "blog": [
        ".blog-listing__header .eyebrow",
        ".blog-listing__title",
        ".blog-listing__subtitle",
        ".blog-card__tag",
        ".blog-card__title",
        ".blog-card__excerpt",
        ".blog-card__meta",
        ".blog-card__author",
        ".blog-listing__page-info",
    ],
    "article": [
        ".article__category",
        ".article__title",
        ".article__meta",
        ".article__body",
        ".article__body h2",
        ".article__body h3",
        ".article__body li",
        ".article__share-link",
        ".article__tag",
        ".article__related-title",
        ".article__related-name",
        ".article__related-date",
    ],
    "about": [
        ".page-about__eyebrow",
        ".page-about__title",
        ".page-about__intro",
        ".page-about__manifesto",
        ".page-about__values-title",
        ".page-about__value-title",
        ".page-about__value-body",
        ".page-about__usa-title",
        ".page-about__usa-body",
    ],
}

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0}}iframe{{display:block;border:0}}</style>
</head><body>
<iframe id="f" width="{width}" height="{height}" src="{src}"></iframe>
<script>
var SELS = {sels};
window.addEventListener('load', function () {{
  setTimeout(function () {{
    var out = {{}};
    try {{
      var d = document.getElementById('f').contentDocument;
      var w = document.getElementById('f').contentWindow;
      out.vw = d.documentElement.clientWidth;
      out.rows = SELS.map(function (s) {{
        var el = d.querySelector(s);
        if (!el) return {{ sel: s, missing: true }};
        var cs = w.getComputedStyle(el);
        return {{ sel: s, size: cs.fontSize, weight: cs.fontWeight,
                 lh: cs.lineHeight, ls: cs.letterSpacing,
                 family: cs.fontFamily.split(',')[0].replace(/['"]/g, '') }};
      }});
    }} catch (e) {{ out.error = String(e); }}
    var s = document.createElement('script');
    s.type = 'application/json'; s.id = 'probe';
    s.textContent = JSON.stringify(out);
    document.body.appendChild(s);
  }}, 900);
}});
</script>
</body></html>
"""


def probe(page, width):
    sels = TARGETS[page]
    harness = os.path.join(HERE, "__verify-harness.html")
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=9000,
                                src="preview-%s.html" % page,
                                sels=json.dumps(sels)))
    try:
        r = subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--allow-file-access-from-files", "--force-device-scale-factor=1",
             "--window-size=%d,900" % max(width + 110, 500),
             "--virtual-time-budget=6000", "--dump-dom", harness],
            capture_output=True, text=True, timeout=180)
        m = re.search(r'<script type="application/json" id="probe">(.*?)</script>',
                      r.stdout, re.S)
        return json.loads(m.group(1)) if m else {"error": "no payload"}
    finally:
        if os.path.exists(harness):
            os.remove(harness)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, nargs="*", default=[1440, 390])
    a = ap.parse_args()
    for width in a.width:
        print("\n=== %dpx ===" % width)
        for page in TARGETS:
            res = probe(page, width)
            print("\n-- %s (vw=%s)" % (page, res.get("vw", res.get("error"))))
            for row in res.get("rows", []):
                if row.get("missing"):
                    print("   %-34s MISSING" % row["sel"])
                    continue
                print("   %-34s %-8s w=%-4s lh=%-8s ls=%-9s %s"
                      % (row["sel"], row["size"], row["weight"], row["lh"],
                         row["ls"], row["family"]))


if __name__ == "__main__":
    main()
