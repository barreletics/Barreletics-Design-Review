#!/usr/bin/env python3
"""Static padding at schema defaults for Batch C (108fff6-aligned literals + token fallbacks)."""
from __future__ import annotations

# (section, selector note, desktop TRBL, mobile TRBL at defaults)
ROWS = [
    ("page-about-split", ".page-about-split__copy", "clamp Y / clamp X", "8/20/32/20"),
    ("page-about-intro", ".page-about-intro", "clamp", "32/20/28/20"),
    ("page-about-close", ".page-about-close", "clamp", "56/20/56/20"),
    ("page-about-facts", ".page-about-facts", "clamp", "48/20/48/20"),
    ("page-about-values", ".page-about-values", "clamp", "40/20/40/20"),
    ("page-about-joseph", ".page-about-joseph__copy", "clamp", "28/20/36/20"),
    ("page-about-hero", ".page-about-hero", "0", "0"),
    ("page-faq", ".page-faq__questions", "72/40/96/40", "40/20/64/20"),
    ("main-page", ".page-content", "32/40/32/40 (tokens)", "48/16/48/16"),
    ("page-contact", ".page-contact__root", "32/40/32/40", "48/16/48/16"),
    ("page-help", ".page-help", "32/40/32/40", "48/16/48/16"),
    ("page-faq head", ".page-faq__head", "104/40/0/40", "56/20/0/20"),
]

print("| Section / target | Desktop T/R/B/L | Mobile T/R/B/L |")
print("|---|---|---|")
for r in ROWS:
    print(f"| {r[0]} {r[1]} | {r[2]} | {r[3]} |")
print("\nWidths 375–1280: clamp sections vary by viewport; table shows 108fff6 rules at defaults.")
