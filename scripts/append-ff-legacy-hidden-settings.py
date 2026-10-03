#!/usr/bin/env python3
"""Append always-hidden legacy setting defs to fifty-fifty schema (non-strippable)."""
import json
import re
import subprocess
from pathlib import Path

LIQUID = Path("/workspace/shopify-build/sections/fifty-fifty.liquid")
TEMPLATES = Path("/workspace/shopify-build/templates")
VISIBLE_IF = "{{ section.settings.heading_level == '__legacy_hidden__' }}"


def load_template_json(path: Path):
    raw = path.read_text()
    if raw.lstrip().startswith("/*"):
        raw = raw[raw.index("*/") + 2 :]
    return json.loads(raw)


def schema_from_liquid(text: str):
    m = re.search(r"\{% schema %\}\n(.*)\n\{% endschema %\}", text, re.S)
    return json.loads(m.group(1))


def defaults(schema):
    d = {}
    for s in schema.get("settings", []):
        if "id" not in s:
            continue
        sid = s["id"]
        if "default" in s:
            d[sid] = s["default"]
        elif s["type"] == "checkbox":
            d[sid] = False
        else:
            d[sid] = None
    return d


def iter_instances():
    for path in sorted(TEMPLATES.glob("*.json")):
        try:
            data = load_template_json(path)
        except (json.JSONDecodeError, ValueError):
            continue
        for key, sec in data.get("sections", {}).items():
            if sec.get("type") != "fifty-fifty":
                continue
            yield sec.get("settings") or {}


def effective(s, sid, old_def):
    return s[sid] if sid in s else old_def.get(sid)


def main():
    old_liquid = subprocess.check_output(
        [
            "git",
            "show",
            "origin/grok/fifty-fifty-live-preview:shopify-build/sections/fifty-fifty.liquid",
        ],
        cwd="/workspace",
        text=True,
    )
    old_schema = schema_from_liquid(old_liquid)
    text = LIQUID.read_text()
    new_schema = schema_from_liquid(text)
    old_by_id = {s["id"]: s for s in old_schema["settings"] if "id" in s}
    new_ids = {s["id"] for s in new_schema["settings"] if "id" in s}
    removed = sorted(set(old_by_id) - new_ids)
    old_def = defaults(old_schema)

    keep_hidden = []
    fully_removed = []
    for rid in removed:
        non_default = False
        for s in iter_instances():
            if effective(s, rid, old_def) != old_def.get(rid):
                non_default = True
                break
        if non_default:
            keep_hidden.append(rid)
        else:
            fully_removed.append(rid)

    # Strip prior legacy block if re-run
    settings = [s for s in new_schema["settings"] if s.get("content") != "Legacy (hidden — do not edit)"]

    settings.append({"type": "header", "content": "Legacy (hidden — do not edit)"})
    settings.append(
        {
            "type": "paragraph",
            "content": "Preserves stored values on Theme Editor save. Not shown in the panel.",
        }
    )
    for rid in keep_hidden:
        leg = dict(old_by_id[rid])
        leg["label"] = f"Legacy: {leg.get('label', rid)}"
        leg["visible_if"] = VISIBLE_IF
        settings.append(leg)

    new_schema["settings"] = settings
    new_block = "{% schema %}\n" + json.dumps(new_schema, indent=2) + "\n{% endschema %}\n"
    s0 = text.index("{% schema %}")
    s1 = text.index("{% endschema %}") + len("{% endschema %}")
    LIQUID.write_text(text[:s0] + new_block + text[s1:])

    report = {
        "keep_hidden": keep_hidden,
        "fully_removed": fully_removed,
        "hidden_count": len(keep_hidden),
    }
    out = Path("/opt/cursor/artifacts/ff-legacy-hidden-settings.json")
    out.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
