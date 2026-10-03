#!/usr/bin/env python3
"""Fix unified pad range step counts (Shopify <=100 steps) in BATCH A sections."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build/sections")
BATCH = [
    "header.liquid",
    "announcement-strip.liquid",
    "footer.liquid",
    "value-strip.liquid",
    "disciplines.liquid",
    "press-cards.liquid",
    "visual-mosaic.liquid",
    "collab-hero.liquid",
    "collab-teaser.liquid",
    "home-juicer.liquid",
    "guarantee-band.liquid",
    "fullbleed-statement.liquid",
    "sale-banner.liquid",
    "geo-section.liquid",
    "studio-trust.liquid",
    "press-feature.liquid",
    "coperni-crosslink.liquid",
    "coperni-pdp-story.liquid",
]

# Unified slider ids → (min, max, step) — default must lie on grid
UNIFIED = {
    "text_pad_y": (0, 120, 2),
    "side_padding": (0, 96, 2),
    "text_pad_y_mobile": (0, 120, 2),
    "text_pad_x_mobile": (0, 48, 2),
}

# Fine-grain y (odd defaults like 5)
UNIFIED_Y_FINE = (0, 100, 1)

# Announcement side default 56 — need 56 on grid with step 2: 0-120 step 2 works (56 even)


def step_count(min_v: int, max_v: int, step: int) -> int:
    return (max_v - min_v) // step


def patch_range_block(text: str, setting_id: str, min_v: int, max_v: int, step: int) -> str:
    pat = (
        rf'("id": "{re.escape(setting_id)}"[\s\S]*?"min": )\d+([\s\S]*?"max": )\d+([\s\S]*?"step": )\d+'
    )

    def repl(m):
        return f"{m.group(1)}{min_v}{m.group(2)}{max_v}{m.group(3)}{step}"

    new, n = re.subn(pat, repl, text, count=1)
    if n == 0:
        return text
    return new


def patch_file(name: str) -> list[str]:
    path = ROOT / name
    text = path.read_text()
    orig = text
    reports: list[str] = []

    for sid, (min_v, max_v, step) in UNIFIED.items():
        if f'"id": "{sid}"' not in text:
            continue
        if sid == "text_pad_y" and name == "announcement-strip.liquid":
            min_v, max_v, step = UNIFIED_Y_FINE
        text = patch_range_block(text, sid, min_v, max_v, step)

    # sale-banner / announcement unified y may use 0 default — step 2 OK

    if text != orig:
        path.write_text(text)

    # Report unified ranges only
    for sid, (min_v, max_v, step) in UNIFIED.items():
        if f'"id": "{sid}"' not in path.read_text():
            continue
        if sid == "text_pad_y" and name == "announcement-strip.liquid":
            min_v, max_v, step = UNIFIED_Y_FINE
        sc = step_count(min_v, max_v, step)
        reports.append(f"{name}\t{sid}\t{min_v}-{max_v}\tstep {step}\tsteps={sc}")

    return reports


def main() -> None:
    all_reports: list[str] = []
    for name in BATCH:
        all_reports.extend(patch_file(name))

    out = Path("/opt/cursor/artifacts/batch-a-range-step-counts.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(all_reports) + "\n")
    print(out.read_text())


if __name__ == "__main__":
    main()
