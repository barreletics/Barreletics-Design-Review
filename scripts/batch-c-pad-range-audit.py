#!/usr/bin/env python3
"""Audit range step counts for Batch C unified pad settings."""
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

PAD_IDS = {"text_pad_y", "side_padding", "text_pad_y_mobile", "text_pad_x_mobile"}


def extract_schema(path: Path) -> dict | None:
    text = path.read_text()
    m = re.search(r"\{% schema %\}\s*(\{.*\})\s*\{% endschema %\}", text, re.S)
    if not m:
        return None
    return json.loads(m.group(1))


def main() -> None:
    root = Path("/workspace/shopify-build/sections")
    rows = []
    bad = []
    for name in SECTIONS:
        path = root / f"{name}.liquid"
        schema = extract_schema(path)
        if not schema:
            bad.append((name, "no schema"))
            continue
        for s in schema.get("settings", []):
            if s.get("type") != "range":
                continue
            sid = s.get("id", "")
            if sid not in PAD_IDS:
                continue
            mn = s["min"]
            mx = s["max"]
            st = s["step"]
            default = s.get("default")
            steps = int((mx - mn) / st)
            on_grid = default is None or (default - mn) % st == 0
            ok = steps <= 100 and on_grid
            rows.append((name, sid, mn, mx, st, default, steps, on_grid, ok))
            if not ok:
                bad.append((name, sid, steps, on_grid))

    print("| Section | Setting | min | max | step | default | step count | default on grid | OK |")
    print("|---|---|---:|---:|---:|---:|---:|:---:|:---:|")
    for r in rows:
        print(
            f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {'yes' if r[8] else 'NO'} |"
        )
    if bad:
        print("\nFAIL:", len(bad), "issues")
        for b in bad:
            print(" ", b)
        raise SystemExit(1)
    print("\nAll pad ranges OK (step count <= 100, defaults on grid).")


if __name__ == "__main__":
    main()
