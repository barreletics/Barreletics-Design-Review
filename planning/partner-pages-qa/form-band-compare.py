#!/usr/bin/env python3
"""
Form-band tone comparison — one page, five variants of the white → warm transition.

Owner question 2026-08-08: "I like how you go to the warm section where the form is, but I
don't know if I love it... maybe it's just more subtle, going from the white to the form
section."

The palette has exactly ONE warm background token (--color-warm-cream #f5f2ec, aliased to
--bg-alternate). There is no subtler warm neutral in design-tokens.css, so nothing here mixes
a new brand colour: the softer options are either the existing token at reduced strength over
white, an existing token used as-is, or the existing token with the seam eased.

Renders the real wholesale hero + form for each variant, clipped to the transition zone so the
five tiles can be compared without scrolling past a full form each time. Shipping templates are
untouched.

Usage:
    python3 planning/partner-pages-qa/form-band-compare.py            # build + shoot
    python3 planning/partner-pages-qa/form-band-compare.py --no-shots
"""

import argparse
import json
import os

import build as harness

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "form-band-compare.html")

CREAM = "#f5f2ec"
WHITE = "#ffffff"


def mix(a, b, pct):
    """pct% of a over b, both #rrggbb. Used only to show the existing token at part strength."""
    a = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(x * pct + y * (1 - pct)) for x, y in zip(a, b))


CREAM_50 = mix(CREAM, WHITE, 0.50)
CREAM_35 = mix(CREAM, WHITE, 0.35)

VARIANTS = [
    ("A", "Current — what ships now",
     "<code>--bg-alternate</code> / <code>--color-warm-cream</code> · %s · hard edge" % CREAM,
     "background: %s;" % CREAM),
    ("B", "Same token, half strength over white",
     "<code>--bg-alternate</code> at 50%%, resolves to %s · warm kept, step halved" % CREAM_50,
     "background: %s;" % CREAM_50),
    ("C", "Same token, one third strength over white",
     "<code>--bg-alternate</code> at 35%%, resolves to %s · the most subtle warm step" % CREAM_35,
     "background: %s;" % CREAM_35),
    ("D", "Current tone, seam drawn instead of abrupt",
     "%s + 1px <code>--border-default</code> %s on the top edge · tone unchanged"
     % (CREAM, "#d6cfc0"),
     "background: %s; border-top: 1px solid #d6cfc0;" % CREAM),
    ("E", "Current tone, no hard edge at all",
     "%s with a 120px white-to-cream fade at the top · tone unchanged, transition eased" % CREAM,
     "background: linear-gradient(to bottom, %s 0px, %s 120px), %s;"
     % (WHITE, CREAM, CREAM)),
]

NOTE = """The palette carries one warm background: <code>--color-warm-cream #f5f2ec</code>
(aliased <code>--bg-alternate</code>). <code>--bg-card #f9f9f9</code> is a neutral grey, not a
warm tone, and <code>--color-warm-border #d6cfc0</code> is a border weight — too dark for a
band. So there is no subtler warm neutral already in the system to switch to. B and C are the
existing token at reduced strength; D and E leave the tone alone and change only the edge."""


def tile(code, name, detail, css, body):
    return f"""
<section class="cmp">
  <div class="cmp__label">
    <span class="cmp__code">{code}</span>
    <span class="cmp__name">{name}</span>
    <span class="cmp__detail">{detail}</span>
  </div>
  <div class="cmp__frame">
    <div class="cmp__page" style="--band: 0;">
      <style>#band-{code} .section--cream {{ {css} }}</style>
      <div id="band-{code}">{body}</div>
    </div>
  </div>
</section>"""


def build():
    tpl = json.load(open(os.path.join(harness.TEMPLATES, "page.wholesale.json")))
    sid = tpl["order"][0]
    body = harness.render_section(tpl["sections"][sid]["type"], tpl["sections"][sid])

    tiles = "\n".join(tile(c, n, d, css, body) for c, n, d, css in VARIANTS)

    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Form band tone — pick one</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{harness.ASSETS}/design-tokens.css">
<link rel="stylesheet" href="{harness.ASSETS}/barreletics-base.css">
<link rel="stylesheet" href="{harness.ASSETS}/chrome.css">
<style>
  body {{ margin: 0; background: #ffffff; }}

  .cmp__intro {{
    max-width: 760px;
    margin: 0 auto;
    padding: 48px 20px 8px;
    font-family: var(--font-family);
  }}
  .cmp__intro h1 {{
    font-size: 24px; font-weight: 700; color: var(--text-primary); margin: 0 0 12px;
  }}
  .cmp__intro p {{
    font-size: 14px; line-height: 1.7; color: var(--text-body); margin: 0 0 12px;
  }}
  .cmp__intro code, .cmp__detail code {{
    font-family: var(--font-mono, monospace); font-size: 0.92em;
    background: #f5f2ec; padding: 1px 5px; border-radius: 3px;
  }}

  .cmp {{ max-width: 1240px; margin: 0 auto; padding: 28px 20px 0; }}

  .cmp__label {{
    display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap;
    font-family: var(--font-family); padding: 0 0 10px;
  }}
  .cmp__code {{
    font-size: 13px; font-weight: 700; color: #ffffff; background: var(--text-primary);
    width: 26px; height: 26px; border-radius: 50%;
    display: inline-flex; align-items: center; justify-content: center; flex: 0 0 auto;
  }}
  .cmp__name {{ font-size: 16px; font-weight: 700; color: var(--text-primary); }}
  .cmp__detail {{ font-size: 13px; color: var(--text-body); }}

  /* Clipped to the transition zone: the white above, the seam, and the first fields.
     That is the thing being judged, and it keeps five variants scannable. */
  .cmp__frame {{
    border: 1px solid #e6e2da;
    border-radius: 8px;
    overflow: hidden;
    height: 620px;
  }}
  .cmp__page {{ height: 100%; overflow: hidden; }}
  .cmp__page .section {{ padding-top: 40px; padding-bottom: 40px; }}
  .cmp__page .type-hero {{ font-size: 40px; }}

  @media (max-width: 768px) {{
    .cmp__frame {{ height: 560px; }}
    .cmp__page .type-hero {{ font-size: 30px; }}
  }}
</style>
</head><body>
<div class="cmp__intro">
  <h1>Form band tone — pick one</h1>
  <p>{NOTE}</p>
  <p>Same wholesale page, same content, in every tile. Only the form band changes. Nothing here
  is live — the shipping templates still use A.</p>
</div>
{tiles}
<div class="cmp__intro"><p>&nbsp;</p></div>
</body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-shots", action="store_true")
    a = ap.parse_args()

    html = build()
    with open(OUT, "w") as fh:
        fh.write(html)
    print("built %s (%d KB)" % (os.path.relpath(OUT, harness.REPO), len(html) // 1024))
    print("  A %s   B %s   C %s" % (CREAM, CREAM_50, CREAM_35))

    if a.no_shots:
        return
    for width in (1440, 390):
        d = harness.run("form-band-compare", OUT, width, mobile=(width < 700), no_shots=False)
        print("  %4dpx  height %5d  overflow %d  tap<44 %d  sticky-clash %d"
              % (width, d["pageHeight"], len(d["overflow"]), len(d["smallTap"]),
                 len(d["stickyOverlap"])))


if __name__ == "__main__":
    main()
