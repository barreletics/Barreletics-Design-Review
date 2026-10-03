#!/usr/bin/env python3
"""Plain-English inventory of TE controls Andrew may not need (usage counts from git JSON)."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("/workspace/shopify-build")
TEMPLATES = ROOT / "templates"
REPORT = ROOT / "qa" / "te-controls-andrew-review.md"

SECTIONS = {
    "fifty-fifty": ROOT / "sections" / "fifty-fifty.liquid",
    "split-hero": ROOT / "sections" / "split-hero.liquid",
}

# Controls that stay visible but Andrew rarely touches (curated + auto: never changed from default).
ALWAYS_LIST = {
    "split-hero": {
        "hide_on_mobile": "Hide the whole hero on phone",
        "hide_on_desktop": "Hide the whole hero on desktop",
        "aria_label": "Override screen-reader name (heading is usually enough)",
        "image_url": "Fallback hero image URL when Shopify picker is empty",
        "image_pos_x": "Custom desktop focal — horizontal % (only if focal = Custom)",
        "image_pos_y": "Custom desktop focal — vertical %",
        "image_pos_x_mobile": "Custom phone focal — horizontal %",
        "image_pos_y_mobile": "Custom phone focal — vertical %",
        "image_zoom": "Desktop zoom % (fine-tune crop)",
        "image_zoom_mobile": "Phone zoom %",
        "inset_top_mobile": "Phone frame margin top (only when separate phone margins on)",
        "inset_bottom_mobile": "Phone frame margin bottom",
        "inset_x_mobile": "Phone frame margin left/right",
        "trust_url": "Custom trust strip link URL",
        "video_controls": "Legacy: show video controls (hidden; was never on in git)",
        "heading_level": "Heading tag level (H1 vs H2) — SEO tweak",
        "title_size": "Override hero title font size",
        "title_weight": "Override hero title weight",
        "body_size": "Override body font size",
        "body_weight": "Override body weight",
        "cta_size": "Override CTA button size",
    },
    "fifty-fifty": {
        "hide_on_mobile": "Hide this 50/50 block on phone",
        "hide_on_desktop": "Hide on desktop",
        "anchor_id": "Jump-link ID for in-page anchors",
        "aria_label": "Override screen-reader name",
        "image_url": "External still image URL",
        "image_asset": "Legacy theme asset filename for image",
        "poster_url": "Poster URL when using mp4 URL",
        "video_url": "External mp4 URL (vs Shopify video picker)",
        "focal_x": "Custom desktop focal horizontal %",
        "focal_y": "Custom desktop focal vertical %",
        "focal_x_mobile": "Custom phone focal horizontal %",
        "focal_y_mobile": "Custom phone focal vertical %",
        "mobile_media_width": "Phone image width below 100%",
        "media_aspect": "Square frame shape vs fill height",
        "media_aspect_mobile": "Phone square frame (legacy hidden)",
        "heading_level": "Heading tag level",
        "heading_class": "Extra CSS class on heading",
        "eyebrow": "Small line above heading (most pages use heading only)",
        "quote_author_case": "Quote author uppercase styling (legacy)",
        "quote_italic": "Quote italic (legacy)",
        "stat_1_label": "Legacy stat row labels",
        "stat_1_value": "Legacy stat values",
        "stat_2_label": "Legacy stat row",
        "stat_2_value": "Legacy stat row",
        "stat_3_label": "Legacy stat row",
        "stat_3_value": "Legacy stat row",
        "stat_3_emphasis": "Legacy stat emphasis",
        "body_size": "Legacy body size (locked; no visual effect)",
        "title_weight": "Legacy title weight",
        "vertical_padding": "Legacy single desktop pad slider",
        "bg_color": "Legacy custom panel colour picker",
        "mobile_text_height": "Legacy min text column height on phone",
        "section_gap_mobile": "Extra space after section on phone",
        "cta_url": "Custom CTA URL when link target is Custom",
        "trust_url": "Custom trust link URL",
    },
}


def load_json(path: Path):
    raw = path.read_text(encoding="utf-8")
    if raw.lstrip().startswith("/*"):
        raw = raw[raw.index("*/") + 2 :]
    return json.loads(raw)


def schema_defaults(liquid_path: Path) -> dict:
    text = liquid_path.read_text(encoding="utf-8")
    m = re.search(r"\{% schema %\}([\s\S]*?)\{% endschema %\}", text)
    if not m:
        return {}
    data = json.loads(m.group(1))
    out = {}
    for s in data.get("settings") or []:
        sid = s.get("id")
        if sid and "default" in s:
            out[sid] = s["default"]
    return out


def iter_instances(stype: str):
    for path in sorted(TEMPLATES.glob("*.json")):
        try:
            data = load_json(path)
        except (json.JSONDecodeError, ValueError):
            continue
        for key, sec in (data.get("sections") or {}).items():
            if sec.get("type") == stype and sec.get("disabled") is not True:
                yield f"{path.stem}:{key}", sec.get("settings") or {}


def count_usage(stype: str) -> tuple[int, dict]:
    defaults = schema_defaults(SECTIONS[stype])
    instances = list(iter_instances(stype))
    n = len(instances)
    non_default = defaultdict(int)
    absent = defaultdict(int)
    for _loc, settings in instances:
        for sid, dflt in defaults.items():
            if sid not in settings:
                absent[sid] += 1
                continue
            val = settings[sid]
            if val != dflt:
                non_default[sid] += 1
    return n, dict(non_default), dict(absent), defaults


def main():
    lines = [
        "# Theme Editor controls — Andrew review (do not remove)",
        "",
        "Plain-English list of controls you probably rarely need. **Usage** = instances in git `templates/*.json` where the value differs from schema default (or key missing when default matters).",
        "",
    ]
    for stype in ("split-hero", "fifty-fifty"):
        n, non_def, absent, defaults = count_usage(stype)
        lines.append(f"## {stype} ({n} placed instances)")
        lines.append("")
        catalog = ALWAYS_LIST.get(stype, {})
        for sid, plain in sorted(catalog.items(), key=lambda x: x[1].lower()):
            changed = non_def.get(sid, 0)
            miss = absent.get(sid, 0)
            d = defaults.get(sid, "—")
            lines.append(
                f"- **{plain}** (`{sid}`) — changed from default on **{changed}/{n}** instances; key absent **{miss}/{n}**; schema default: `{d!r}`."
            )
        lines.append("")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
