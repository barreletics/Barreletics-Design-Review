#!/usr/bin/env python3
"""Ensure all range setting labels in Batch C are <= 70 chars."""
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


def main() -> None:
    root = Path("/workspace/shopify-build/sections")
    bad = []
    for name in SECTIONS:
        text = (root / f"{name}.liquid").read_text()
        m = re.search(r"\{% schema %\}\s*(\{.*\})\s*\{% endschema %\}", text, re.S)
        schema = json.loads(m.group(1))
        for s in schema.get("settings", []):
            if s.get("type") != "range":
                continue
            lab = s.get("label", "")
            n = len(lab)
            ok = n <= 70
            print(f"{name} {s.get('id')}: {n} {'OK' if ok else 'TOO LONG'} | {lab}")
            if not ok:
                bad.append((name, s.get("id"), n, lab))
    if bad:
        raise SystemExit(f"{len(bad)} labels exceed 70 chars")
    print("All range labels OK.")


if __name__ == "__main__":
    main()
