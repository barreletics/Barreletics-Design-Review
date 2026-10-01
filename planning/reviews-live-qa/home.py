#!/usr/bin/env python3
"""Homepage reviews slot — before (curated social-proof) vs after (live Judge.me).

Andrew authorised the homepage move on 2026-08-08 ("probably use the live review,
however we may want to control them"). index.json is a radioactive surface, so the
change gets its own before/after rather than riding along with the PDP previews.

Before is rebuilt from the pre-swap index.json in git HEAD — read only, nothing is
restored to the working tree. After is rendered from the current index.json through
the same renderer the PDP harness uses.

    python3 planning/reviews-live-qa/home.py
"""

import html
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "planning", "pdp-variants-qa"))

import build as pdp  # noqa: E402  — reuse the real renderers and CSS

ASSETS = "../../shopify-build/assets"


def esc(s):
    return html.escape(s or "", quote=False)


def before_section():
    """The curated social-proof block as the homepage rendered it pre-swap."""
    src = subprocess.run(["git", "show", "HEAD:shopify-build/templates/index.json"],
                         capture_output=True, text=True, cwd=REPO).stdout
    d = json.loads(src)
    s = next(v for v in d["sections"].values() if v.get("type") == "social-proof")
    st = s["settings"]
    cards = ""
    for k in (s.get("block_order") or list(s["blocks"])):
        b = s["blocks"][k]
        if b["type"] != "review":
            continue
        bs = b["settings"]
        cards += ('<article class="qa-review"><div class="qa-review__img"><img src="%s" alt=""></div>'
                  '<div class="qa-review__body"><span class="qa-stars">★★★★★</span>'
                  '<p>%s</p><p class="qa-review__who">%s<span>%s</span></p></div></article>'
                  % (bs.get("image_url", ""), esc(bs.get("body", "")),
                     esc(bs.get("author", "")), esc(bs.get("location", ""))))
    return ('<section class="qa-social" style="background:#f5f2ec;">'
            '<header class="qa-social__head"><h2>%s</h2><p>%s</p></header>'
            '<div class="qa-reviews">%s</div></section>'
            % (esc(st.get("title", "")), esc(st.get("body", "")), cards))


def after_section():
    d = json.load(open(os.path.join(REPO, "shopify-build", "templates", "index.json")))
    return pdp.r_reviews(d["sections"]["reviews"], None)


LEGACY_CSS = """
.qa-social{padding:var(--section-padding-y) var(--section-padding-x)}
.qa-social__head{text-align:center;margin-bottom:40px}
.qa-social__head h2{font:400 clamp(28px,3vw,40px)/1.15 Roboto,sans-serif;margin:0 0 10px;
  letter-spacing:-.02em;color:#1c1916}
.qa-social__head p{font:400 15px/1.6 Roboto,sans-serif;color:#6b645a;margin:0}
.qa-reviews{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:1200px;margin:0 auto}
.qa-review{background:#fff}
.qa-review__img{aspect-ratio:16/10;background:#e8e2d8;overflow:hidden}
.qa-review__img img{width:100%;height:100%;object-fit:cover;display:block}
.qa-review__body{padding:22px 24px 24px}
.qa-review__body p{font:400 15px/1.55 Roboto,sans-serif;color:#4a4a4a;margin:10px 0 12px}
.qa-review__who{font:500 13px/1.5 Roboto,sans-serif!important;color:#1c1916!important;margin:0!important}
.qa-review__who span{display:block;font-weight:400;font-size:12px;color:#8a8a8a}
.qa-stars{color:#c45c3f;font-size:14px;letter-spacing:.1em}
.cmp-label{padding:12px 24px;color:#fff;font:700 12px/1.4 Roboto,sans-serif;
  letter-spacing:.14em;text-transform:uppercase}
.cmp-label span{display:block;font:400 12px/1.5 Roboto,sans-serif;letter-spacing:.04em;
  text-transform:none;color:#f0e6dd;margin-top:4px}
@media (max-width:768px){.qa-reviews{grid-template-columns:1fr}}
"""

SHELL = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Homepage reviews — {label}</title>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}/design-tokens.css">
<link rel="stylesheet" href="{assets}/barreletics-base.css">
<style>{section_css}</style>
<style>{harness_css}</style>
<style>{legacy_css}</style>
</head><body>
<div class="cmp-label" style="background:{bg}">{label}<span>{note}</span></div>
{body}
</body></html>
"""

PANELS = [
    ("home-before", "#6b645a", "Before — curated social-proof on the homepage",
     "9 hand-picked blocks in index.json. Six of the nine were fabricated reviews.",
     before_section),
    ("home-after", "#1c1916", "After — live Judge.me, store scope",
     "Judge.me all-reviews widget renders at runtime; static preview shows the labelled stand-in.",
     after_section),
]


def main():
    made = []
    for name, bg, label, note, fn in PANELS:
        page = os.path.join(HERE, "%s.html" % name)
        with open(page, "w") as fh:
            fh.write(SHELL.format(assets=ASSETS, section_css=pdp.collect_css(),
                                  harness_css=pdp.HARNESS_CSS, legacy_css=LEGACY_CSS,
                                  bg=bg, label=label, note=note, body=fn()))
        made.append(page)
        print("built %s" % os.path.relpath(page, REPO))

    shots = []
    for page in made:
        out = page.replace(".html", "-1440.png")
        pdp.shoot_desktop(page, out, 1440, 3400)
        print("  shot %s" % os.path.basename(out))
        shots.append(out)
    combo = os.path.join(HERE, "HOME-REVIEWS-BEFORE-AFTER-1440px.png")
    pdp.compose([(shots[0], "Before — curated"), (shots[1], "After — live Judge.me")], combo)
    print("composed %s" % os.path.basename(combo))


if __name__ == "__main__":
    main()
