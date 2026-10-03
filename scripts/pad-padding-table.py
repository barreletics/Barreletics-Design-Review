#!/usr/bin/env python3
"""Simulate batch-B section padding at defaults (108fff6-equivalent CSS rules)."""
from __future__ import annotations

# Theme token defaults (design-tokens + theme.liquid)
TOK = {
    "section_y": 32,
    "section_x": 40,
    "section_y_m": 24,
    "section_x_m": 20,
    "space_13": 64,
    "space_9": 40,
    "space_13_hero": 72,
}

WIDTHS = [375, 749, 768, 900, 1280]


def pad(section: str, w: int) -> tuple[int, int, int, int]:
    mobile = w <= 768
    if section == "pdp-features":
        return (48, 20, 48, 20) if mobile else (32, 40, 32, 40)
    if section == "pdp-sock-math":
        return (0, 0, TOK["section_y_m"], 0) if mobile else (0, 0, TOK["section_y"], 0)
    if section == "pdp-buy-box":
        if mobile:
            return (32, 16, 0, 16)
        if w <= 1024:
            return (40, 32, 40, 32)  # space-10 / space-8 approx
        return (40, 56, 48, 40)  # space-14 right, section-x left
    if section == "pdp-reviews":
        return (48, 16, 48, 16) if mobile else (TOK["section_y"], TOK["section_x"], TOK["section_y"], TOK["section_x"])
    if section == "variant-grid":
        return (TOK["section_y_m"], TOK["section_x_m"], 0, TOK["section_x_m"]) if mobile else (
            TOK["section_y"],
            TOK["section_x"],
            TOK["section_y"],
            TOK["section_x"],
        )
    if section == "collection-hero":
        if mobile:
            return (36, 20, 36, 20)
        return (56, 40, 40, 40)  # split baseline; text-only differs (72 top) — noted below
    if section in ("recently-viewed", "recommendations", "search-results", "blog-listing", "article-content"):
        if mobile:
            return (TOK["section_y_m"], TOK["section_x_m"], TOK["section_y_m"], TOK["section_x_m"])
        return (TOK["section_y"], TOK["section_x"], TOK["section_y"], TOK["section_x"])
    if section in ("main-cart", "contact-cta"):
        return (48, 16, 48, 16) if mobile else (64, 40, 64, 40)
    if section == "sole-cards":
        return (24, 16, 24, 16) if mobile else (24, 40, 24, 40)
    raise KeyError(section)


SECTIONS = [
    "pdp-features",
    "pdp-sock-math",
    "pdp-buy-box",
    "pdp-reviews",
    "variant-grid",
    "collection-hero",
    "recently-viewed",
    "recommendations",
    "sole-cards",
    "main-cart",
    "search-results",
    "blog-listing",
    "article-content",
    "contact-cta",
]

print("| Section | Width | top | right | bottom | left |")
print("|---------|-------|-----|-------|--------|------|")
for s in SECTIONS:
    for w in WIDTHS:
        t, r, b, l = pad(s, w)
        print(f"| {s} | {w} | {t} | {r} | {b} | {l} |")
print("\nNote: collection-hero text-only (non-split) desktop top is 72px at 108fff6; split row uses 56/40/40.")
