#!/usr/bin/env python3
"""List range step counts for unified pad settings in batch-B sections."""
import json
import re
import sys
from pathlib import Path

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

PAD_IDS = {"text_pad_y", "side_padding", "text_pad_y_mobile", "text_pad_x_mobile"}


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "shopify-build" / "sections"
    fail = False
    rows = []
    for name in SECTIONS:
        path = root / f"{name}.liquid"
        text = path.read_text()
        m = re.search(r"{% schema %}\s*(\{.*\})\s*{% endschema %}", text, re.S)
        if not m:
            print(f"{name}: no schema", file=sys.stderr)
            fail = True
            continue
        schema = json.loads(m.group(1))
        for s in schema.get("settings", []):
            sid = s.get("id")
            if sid not in PAD_IDS:
                continue
            mn, mx, step = s["min"], s["max"], s["step"]
            steps = (mx - mn) // step
            ok = steps <= 100
            on_grid = (s["default"] - mn) % step == 0
            rows.append((name, sid, mn, mx, step, steps, ok, on_grid, s["default"]))
            if not ok or not on_grid:
                fail = True

    print("| Section | Setting | min | max | step | step count | OK | default on grid | default |")
    print("|---------|---------|-----|-----|------|------------|----|-----------------|---------|")
    for r in rows:
        name, sid, mn, mx, step, steps, ok, on_grid, default = r
        print(
            f"| {name} | {sid} | {mn} | {mx} | {step} | {steps} | "
            f"{'yes' if ok else 'NO'} | {'yes' if on_grid else 'NO'} | {default} |"
        )
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
