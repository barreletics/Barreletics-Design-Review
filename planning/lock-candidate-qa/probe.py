#!/usr/bin/env python3
"""
Computed-type probe + screenshots for the four unlocked lock-candidate mocks.

Reads back rendered font-size / weight / line-height / letter-spacing for the
type-bearing selectors on each candidate, so Type OS conformance is judged from
what the browser computes rather than from reading CSS.

Headless Chrome on macOS clamps the window to a 500px minimum, so mobile widths
are produced by hosting the page in a fixed-width iframe inside a harness page
(same technique as planning/blog-about-type-qa/build.py).

Usage:
    python3 planning/lock-candidate-qa/probe.py --tag before
    python3 planning/lock-candidate-qa/probe.py --tag after --shots
"""

import argparse
import json
import os
import re
import subprocess
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(REPO, "docs")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PAGES = {
    "collection-v19": {
        "file": "Barreletics Collection - Definitive-v19.html",
        "sels": [
            ".coll-hero__eyebrow", ".coll-hero__title", ".coll-hero__body",
            ".sole-card__tag", ".sole-card__title",
            ".dp-item__discipline", ".disciplines-proof__headline",
            ".lifestyle-break__line", ".pose-band__title", ".pose-band__body",
            ".split-text h2", ".reviews-head__title", ".faq-head__title",
            ".var-card__name", ".fn-signup h2",
        ],
    },
    "seo-v37": {
        "file": "Barreletics SEO - Best Grippy Socks - Definitive-v37.html",
        "sels": [
            ".hero-fullbleed__eyebrow", ".hero-fullbleed__title",
            ".hero-fullbleed__lede",
            ".seo-problem-line__title", ".discipline-film__line",
            ".lifestyle-break__line", ".pose-band__title",
            ".sole-card__tag", ".sole-card__title", ".dp-item__discipline",
            ".disciplines-proof__headline", ".split-text h2",
            ".reviews-head__title", ".ig-head__title", ".sock-math__title",
            ".faq-head__title", ".sock-math-col__label", ".fn-signup h2",
        ],
    },
    "journal-v6": {
        "file": "Barreletics Journal - Definitive-v6.html",
        "sels": [
            ".journal-eyebrow", ".journal-title", ".journal-lede",
            ".feature__meta", ".feature__title",
            ".article-card__meta", ".article-card__title",
            ".variants-head__title", ".journal-faq h2", ".fn-signup h2",
        ],
    },
    "help-v4": {
        "file": "Barreletics Help - Definitive-v4.html",
        "sels": [
            ".page-eyebrow", ".page-title", ".page-lede",
            ".hub-card__label", ".hub-card__title",
            ".page-cta__title", ".fn-signup h2",
        ],
    },
}

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;background:#fff}}iframe{{display:block;border:0}}</style>
</head><body>
<iframe id="f" width="{width}" height="{height}" src="{src}"></iframe>
<script>
var SELS = {sels};
window.addEventListener('load', function () {{
  setTimeout(function () {{
    var out = {{}};
    try {{
      var fr = document.getElementById('f');
      var d = fr.contentDocument, w = fr.contentWindow;
      out.vw = d.documentElement.clientWidth;
      out.rows = SELS.map(function (s) {{
        var el = d.querySelector(s);
        if (!el) return {{ sel: s, missing: true }};
        var cs = w.getComputedStyle(el);
        return {{ sel: s, size: cs.fontSize, weight: cs.fontWeight,
                 lh: cs.lineHeight, ls: cs.letterSpacing }};
      }});
    }} catch (e) {{ out.error = String(e); }}
    var s = document.createElement('script');
    s.type = 'application/json'; s.id = 'probe';
    s.textContent = JSON.stringify(out);
    document.body.appendChild(s);
  }}, 1200);
}});
</script>
</body></html>
"""


def src_url(page):
    path = os.path.join(DOCS, PAGES[page]["file"])
    return "file://" + urllib.parse.quote(path)


def write_harness(page, width, height):
    harness = os.path.join(HERE, "__harness-%s-%d.html" % (page, width))
    with open(harness, "w") as fh:
        fh.write(HARNESS.format(width=width, height=height,
                                src=src_url(page),
                                sels=json.dumps(PAGES[page]["sels"])))
    return harness


def run_chrome(args, timeout=240):
    return subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
         "--hide-scrollbars", "--allow-file-access-from-files",
         "--force-device-scale-factor=1"] + args,
        capture_output=True, text=True, timeout=timeout)


def probe(page, width):
    harness = write_harness(page, width, 9000)
    try:
        r = run_chrome(["--window-size=%d,1000" % max(width + 120, 520),
                        "--virtual-time-budget=9000", "--dump-dom", harness])
        m = re.search(
            r'<script type="application/json" id="probe">(.*?)</script>',
            r.stdout, re.S)
        return json.loads(m.group(1)) if m else {"error": "no probe payload"}
    finally:
        os.path.exists(harness) and os.remove(harness)


def shoot(page, width, tag):
    """Full-page screenshot at a true `width` viewport via the iframe harness."""
    harness = write_harness(page, width, 4200)
    out = os.path.join(HERE, "%s-%s-%dpx.png" % (page, tag, width))
    try:
        run_chrome(["--window-size=%d,4200" % max(width + 120, 520),
                    "--virtual-time-budget=9000",
                    "--screenshot=%s" % out, harness])
        return out
    finally:
        os.path.exists(harness) and os.remove(harness)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="before")
    ap.add_argument("--width", type=int, nargs="*", default=[1440, 390])
    ap.add_argument("--pages", nargs="*", default=list(PAGES))
    ap.add_argument("--shots", action="store_true")
    a = ap.parse_args()

    results = {}
    for width in a.width:
        print("\n================ %dpx ================" % width)
        for page in a.pages:
            res = probe(page, width)
            results.setdefault(page, {})[str(width)] = res
            print("\n-- %s  (measured vw=%s)" % (page, res.get("vw") or res.get("error")))
            for row in res.get("rows", []):
                if row.get("missing"):
                    print("   %-32s MISSING" % row["sel"])
                    continue
                print("   %-32s %-8s w=%-4s lh=%-8s ls=%s"
                      % (row["sel"], row["size"], row["weight"],
                         row["lh"], row["ls"]))
            if a.shots:
                shoot(page, width, a.tag)

    with open(os.path.join(HERE, "measurements-%s.json" % a.tag), "w") as fh:
        json.dump(results, fh, indent=2)
    print("\nWrote measurements-%s.json" % a.tag)


if __name__ == "__main__":
    main()
