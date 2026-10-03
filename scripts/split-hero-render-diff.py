#!/usr/bin/env python3
"""Split-hero render snapshot: legacy x/y/zoom vs new focal mapping (git templates)."""
import json
import sys
from pathlib import Path

TEMPLATES = Path("/workspace/shopify-build/templates")


def load_template_json(path: Path):
    raw = path.read_text()
    if raw.lstrip().startswith("/*"):
        raw = raw[raw.index("*/") + 2 :]
    return json.loads(raw)


def legacy_xy(s):
    return (
        s.get("image_pos_x", 50),
        s.get("image_pos_y", 50),
        s.get("image_zoom", 100),
        s.get("image_pos_x_mobile", s.get("image_pos_x", 50)),
        s.get("image_pos_y_mobile", s.get("image_pos_y", 50)),
        s.get("image_zoom_mobile", s.get("image_zoom", 100)),
    )


def resolve_pos(sh_pos, s):
    if sh_pos == "custom" or sh_pos is None:
        px = s.get("image_pos_x", 50)
        py = s.get("image_pos_y", 50)
        if sh_pos is None and px == 50 and py == 50:
            return 50, 50
        if sh_pos is None:
            return px, py
        return px, py
    mapping = {
        "top left": (0, 0),
        "top": (50, 0),
        "top right": (100, 0),
        "left": (0, 50),
        "center": (50, 50),
        "right": (100, 50),
        "bottom left": (0, 100),
        "bottom": (50, 100),
        "bottom right": (100, 100),
    }
    return mapping.get(sh_pos, (50, 50))


def new_xy(s):
    sh_pos = s.get("image_position")
    if sh_pos is None:
        px, py = s.get("image_pos_x", 50), s.get("image_pos_y", 50)
        sh_pos = "center" if px == 50 and py == 50 else "custom"
    ix, iy = resolve_pos(sh_pos, s)
    iz = s.get("image_zoom", 100)
    pm = s.get("image_position_mobile", "same")
    if pm in ("same", None, ""):
        return ix, iy, iz, ix, iy, s.get("image_zoom_mobile", iz)
    if pm == "custom":
        return (
            ix,
            iy,
            iz,
            s.get("image_pos_x_mobile", ix),
            s.get("image_pos_y_mobile", iy),
            s.get("image_zoom_mobile", iz),
        )
    mx, my = resolve_pos(pm, s)
    return ix, iy, iz, mx, my, s.get("image_zoom_mobile", iz)


def main():
    fails = []
    count = 0
    for path in sorted(TEMPLATES.glob("*.json")):
        try:
            data = load_template_json(path)
        except (json.JSONDecodeError, ValueError):
            continue
        for key, sec in data.get("sections", {}).items():
            if sec.get("type") != "split-hero":
                continue
            count += 1
            s = sec.get("settings") or {}
            old = legacy_xy(s)
            new = new_xy(s)
            if old != new:
                fails.append((f"{path.stem}:{key}", old, new))
    out = Path("/workspace/shopify-build/qa/split-hero-render-diff-report.md")
    lines = [
        "# Split-hero focal migration diff",
        "",
        f"Instances: **{count}**",
        f"Diffs: **{len(fails)}**",
        "",
    ]
    if fails:
        for name, old, new in fails:
            lines.append(f"- `{name}` old={old} new={new}")
    else:
        lines.append("Zero diffs — legacy image_pos_* values match new focal resolver.")
    out.write_text("\n".join(lines) + "\n")
    print(out.read_text())
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
