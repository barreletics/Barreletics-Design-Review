#!/usr/bin/env python3
"""Remove unconditional utp padding blocks; set te-style defaults for held-back sections."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build/sections")

# y_d, side_d, y_m, x_m
DEFAULTS = {
    "main-page": (32, 40, 32, 16),
    "page-ambassador": (32, 40, 32, 16),
    "page-compare": (72, 40, 48, 16),
    "page-contact": (32, 40, 32, 16),
    "page-grip-comparison": (32, 40, 32, 16),
    "page-help": (32, 40, 32, 16),
    "page-returns": (32, 40, 32, 16),
    "page-shipping": (32, 40, 32, 16),
    "page-size-guide": (32, 40, 32, 16),
    "page-technology": (32, 40, 32, 16),
    "page-warranty": (32, 40, 32, 16),
    "page-wholesale": (72, 40, 56, 16),
}

UTP_BLOCK = re.compile(
    r"\n\n<style>\n  #shopify-section-\{\{ section\.id \}\} \.[^{]+ \{[^<]+</style>\n",
    re.S,
)


def patch_te_line(text: str, y_d: int, side_d: int, y_m: int, x_m: int) -> str:
    pat = re.compile(
        r"\{% render 'unified-text-pads-te-style', selector: '([^']+)', y_d: \d+, side_d: \d+, y_m: \d+, x_m: \d+ %\}"
    )
    rep = (
        f"{{% render 'unified-text-pads-te-style', selector: '\\1', "
        f"y_d: {y_d}, side_d: {side_d}, y_m: {y_m}, x_m: {x_m} %}}"
    )
    return pat.sub(rep, text, count=1)


def patch_vars_in_style(text: str, y_d: int, side_d: int, y_m: int, x_m: int) -> str:
    old = re.compile(
        r"\{% render 'unified-text-pads-vars', y_d: \d+, side_d: \d+, y_m: \d+, x_m: \d+ %\}"
    )
    new = (
        f"{{% render 'unified-text-pads-vars', y_d: {y_d}, side_d: {side_d}, "
        f"y_m: {y_m}, x_m: {x_m} %}}"
    )
    return old.sub(new, text)


def remove_utp_override_style(text: str) -> str:
    # Remove block starting with #shopify-section and utp-y-d
    start = text.find("#shopify-section-{{ section.id }}")
    while start != -1:
        chunk = text[start : start + 200]
        if "utp-y-d" in chunk or "utp-y-m" in chunk:
            # find opening <style> before this
            style_start = text.rfind("<style>", 0, start)
            style_end = text.find("</style>", start) + len("</style>")
            if style_start != -1 and style_end > style_start:
                text = text[:style_start] + text[style_end:]
                start = text.find("#shopify-section-{{ section.id }}")
                continue
        start = text.find("#shopify-section-{{ section.id }}", start + 1)
    return text


def patch_schema_mobile_defaults(text: str, y_m: int, x_m: int) -> str:
    text = re.sub(
        r'("id": "text_pad_y_mobile",\s*\n\s*"label": )[^\n]+(\n\s*"min":)',
        rf'\1"Text pad top & bottom — phone (default {y_m})"\2',
        text,
        count=1,
    )
    text = re.sub(
        r'("id": "text_pad_y_mobile",[\s\S]*?"default": )\d+',
        rf"\g<1>{y_m}",
        text,
        count=1,
    )
    text = re.sub(
        r'("id": "text_pad_x_mobile",[\s\S]*?"default": )\d+',
        rf"\g<1>{x_m}",
        text,
        count=1,
    )
    return text


def main() -> None:
    for name, (y_d, side_d, y_m, x_m) in DEFAULTS.items():
        path = ROOT / f"{name}.liquid"
        text = path.read_text()
        text = remove_utp_override_style(text)
        text = patch_vars_in_style(text, y_d, side_d, y_m, x_m)
        text = patch_te_line(text, y_d, side_d, y_m, x_m)
        if name in ("main-page", "page-compare", "page-wholesale") or True:
            text = patch_schema_mobile_defaults(text, y_m, x_m)
        # desktop y/side schema defaults for compare/wholesale
        if name == "page-compare":
            text = re.sub(
                r'("id": "text_pad_y",[\s\S]*?"default": )\d+',
                r"\g<1>72",
                text,
                count=1,
            )
        if name == "page-wholesale":
            text = re.sub(
                r'("id": "text_pad_y",[\s\S]*?"default": )\d+',
                r"\g<1>72",
                text,
                count=1,
            )
            text = re.sub(
                r'("id": "text_pad_y_mobile",[\s\S]*?"default": )\d+',
                r"\g<1>56",
                text,
                count=1,
            )
        path.write_text(text)
        print("patched", name)


if __name__ == "__main__":
    main()
