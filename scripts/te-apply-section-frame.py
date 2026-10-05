#!/usr/bin/env python3
"""Apply Shared — Section frame schema block to marketing sections (schema-only helper)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build/sections")

FRAME_BLOCK = [
    {"type": "header", "content": "Shared — Section frame"},
    {
        "type": "paragraph",
        "content": "OUTER inset from the page edges (margin). Top and bottom are independent; left & right = one control. Custom mobile OFF = mobile uses the same inset as desktop. Defaults 0 = full bleed.",
    },
    {
        "type": "checkbox",
        "id": "inset_custom_mobile",
        "label": "Custom mobile inset",
        "default": False,
        "info": "OFF (default): ignore the mobile inset sliders — mobile uses desktop Inset top / bottom / left & right. ON: use the mobile inset sliders instead.",
    },
    {"type": "range", "id": "inset_top", "label": "Inset top", "min": 0, "max": 96, "step": 4, "unit": "px", "default": 0},
    {"type": "range", "id": "inset_bottom", "label": "Inset bottom", "min": 0, "max": 96, "step": 4, "unit": "px", "default": 0},
    {
        "type": "range",
        "id": "inset_x",
        "label": "Inset left & right",
        "min": 0,
        "max": 96,
        "step": 4,
        "unit": "px",
        "default": 0,
        "info": "Same value on both sides.",
    },
    {
        "type": "range",
        "id": "inset_top_mobile",
        "label": "Inset top — mobile",
        "min": 0,
        "max": 64,
        "step": 4,
        "unit": "px",
        "default": 0,
        "info": "Only when Custom mobile inset is on.",
    },
    {
        "type": "range",
        "id": "inset_bottom_mobile",
        "label": "Inset bottom — mobile",
        "min": 0,
        "max": 64,
        "step": 4,
        "unit": "px",
        "default": 0,
    },
    {
        "type": "range",
        "id": "inset_x_mobile",
        "label": "Inset left & right — mobile",
        "min": 0,
        "max": 64,
        "step": 4,
        "unit": "px",
        "default": 0,
        "info": "Only when Custom mobile inset is on.",
    },
    {"type": "checkbox", "id": "hide_on_mobile", "label": "Hide on mobile", "default": False},
    {"type": "checkbox", "id": "hide_on_desktop", "label": "Hide on desktop", "default": False},
]


def frame_json_indent(indent: str = "    ") -> str:
    lines = [json.dumps(item, ensure_ascii=False) for item in FRAME_BLOCK]
    return ",\n".join(f"{indent}{line}" for line in lines)


def has_inset_schema(text: str) -> bool:
    return '"id": "inset_top"' in text and "inset_custom_mobile" in text


def insert_frame_before_closing_settings(text: str, before_pattern: str) -> str:
    """Insert frame block immediately before a marker inside settings array."""
    if has_inset_schema(text):
        return text
    block = frame_json_indent()
    # Insert before marker (keep marker)
    pat = re.compile(before_pattern, re.MULTILINE)
    m = pat.search(text)
    if not m:
        raise ValueError(f"Marker not found: {before_pattern!r}")
    return text[: m.start()] + block + ",\n" + text[m.start() :]


def main() -> None:
    print("Use manual patches; block JSON available via FRAME_BLOCK")
    print(frame_json_indent()[:200], "...")


if __name__ == "__main__":
    main()
