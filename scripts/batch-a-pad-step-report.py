#!/usr/bin/env python3
"""List step counts for unified pad ranges in BATCH A sections."""
import json
import re
from pathlib import Path

SECTIONS = Path("/workspace/shopify-build/sections")
FILES = [
    "header.liquid", "announcement-strip.liquid", "footer.liquid", "value-strip.liquid",
    "disciplines.liquid", "press-cards.liquid", "visual-mosaic.liquid", "collab-hero.liquid",
    "collab-teaser.liquid", "home-juicer.liquid", "guarantee-band.liquid",
    "fullbleed-statement.liquid", "sale-banner.liquid", "geo-section.liquid",
    "studio-trust.liquid", "press-feature.liquid", "coperni-crosslink.liquid",
    "coperni-pdp-story.liquid",
]
IDS = {"text_pad_y", "side_padding", "text_pad_y_mobile", "text_pad_x_mobile"}

rows = []
for fn in FILES:
    text = (SECTIONS / fn).read_text()
    for sid in IDS:
        m = re.search(
            rf'"id": "{sid}"[\s\S]*?"min": (\d+)[\s\S]*?"max": (\d+)[\s\S]*?"step": (\d+)[\s\S]*?"default": (\d+)',
            text,
        )
        if not m:
            continue
        lo, hi, step, default = map(int, m.groups())
        steps = (hi - lo) // step
        on_grid = (default - lo) % step == 0
        rows.append({
            "section": fn.replace(".liquid", ""),
            "id": sid,
            "min": lo,
            "max": hi,
            "step": step,
            "default": default,
            "step_count": steps,
            "default_on_grid": on_grid,
            "ok": steps <= 100 and on_grid,
        })

out = Path("/opt/cursor/artifacts/batch-a-range-step-counts.json")
out.write_text(json.dumps(rows, indent=2) + "\n")
bad = [r for r in rows if not r["ok"]]
print(f"ranges={len(rows)} bad={len(bad)}")
for r in rows:
    flag = "OK" if r["ok"] else "BAD"
    print(f"{flag}\t{r['section']}\t{r['id']}\t{r['min']}-{r['max']} step {r['step']} steps={r['step_count']} default={r['default']}")
