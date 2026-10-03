#!/usr/bin/env python3
"""Fix Batch C unified pad range min/max/step to satisfy Shopify <=100 steps rule."""
from __future__ import annotations

import json
import re
from pathlib import Path

SECTIONS = [
    "page-about-split",
    "page-about-close",
    "page-about-facts",
    "page-about-intro",
    "page-about-joseph",
    "page-about-values",
    "page-about-hero",
    "page-faq",
    "main-page",
    "page-ambassador",
    "page-compare",
    "page-contact",
    "page-grip-comparison",
    "page-help",
    "page-returns",
    "page-shipping",
    "page-size-guide",
    "page-technology",
    "page-warranty",
    "page-wholesale",
]

Y_RANGE = {"min": 0, "max": 120, "step": 2}
SIDE_RANGE = {"min": 0, "max": 96, "step": 1}
X_M_RANGE = {"min": 0, "max": 48, "step": 1}


def patch_schema(settings: list) -> int:
    n = 0
    for s in settings:
        if s.get("type") != "range":
            continue
        sid = s.get("id")
        if sid in ("text_pad_y", "text_pad_y_mobile"):
            for k, v in Y_RANGE.items():
                if s.get(k) != v:
                    s[k] = v
                    n += 1
        elif sid == "side_padding":
            for k, v in SIDE_RANGE.items():
                if s.get(k) != v:
                    s[k] = v
                    n += 1
        elif sid == "text_pad_x_mobile":
            for k, v in X_M_RANGE.items():
                if s.get(k) != v:
                    s[k] = v
                    n += 1
    return n


def main() -> None:
    root = Path("/workspace/shopify-build/sections")
    total = 0
    for name in SECTIONS:
        path = root / f"{name}.liquid"
        text = path.read_text()
        m = re.search(r"(\{% schema %\}\s*)(\{.*\})(\s*\{% endschema %\})", text, re.S)
        if not m:
            print("skip", name)
            continue
        schema = json.loads(m.group(2))
        changed = patch_schema(schema.get("settings", []))
        if changed:
            new_json = json.dumps(schema, indent=2)
            new_text = text[: m.start(2)] + new_json + text[m.end(2) :]
            path.write_text(new_text)
            total += changed
            print(name, changed, "fields")
    print("total field updates", total)


if __name__ == "__main__":
    main()
