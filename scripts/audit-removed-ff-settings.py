#!/usr/bin/env python3
"""Audit removed fifty-fifty setting ids vs git template values."""
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

TEMPLATES = Path("/workspace/shopify-build/templates")
LIQUID = Path("/workspace/shopify-build/sections/fifty-fifty.liquid")


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
        st = s["type"]
        if "default" in s:
            d[sid] = s["default"]
        elif st == "checkbox":
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
            yield f"{path.stem}:{key}", sec.get("settings") or {}


old_liquid = subprocess.check_output(
    ["git", "show", "origin/grok/fifty-fifty-live-preview:shopify-build/sections/fifty-fifty.liquid"],
    cwd="/workspace",
    text=True,
)
old_schema = schema_from_liquid(old_liquid)
new_schema = schema_from_liquid(LIQUID.read_text())
old_ids = {s["id"] for s in old_schema["settings"] if "id" in s}
new_ids = {s["id"] for s in new_schema["settings"] if "id" in s}
removed = sorted(old_ids - new_ids)
old_def = defaults(old_schema)

# Effective value: stored or schema default when key missing
def effective(s, sid):
    if sid in s:
        return s[sid]
    return old_def.get(sid)


needs_hidden = set()
fully_remove = set()
detail = defaultdict(list)

for rid in removed:
    defv = old_def.get(rid)
    any_non_default = False
    any_key_present = False
    for name, s in iter_instances():
        if rid in s:
            any_key_present = True
        eff = effective(s, rid)
        if eff != defv:
            any_non_default = True
            detail[rid].append((name, s.get(rid, "<absent>"), eff, defv))
    # Absent keys still get default on save — but vertical_padding absent IS 88 which equals default
    # bg_color absent -> #ffffff; sock-era needs that — default IS #ffffff so OK for strip?
    # If merchant saves after bg_style added, bg_color dropped — we lose explicit #faf8f6 if only bg_color stored
    # So ANY key present with value that affects render must stay
    if any_key_present or any_non_default:
        needs_hidden.add(rid)
    else:
        fully_remove.add(rid)

print("REMOVED IDS — keep hidden (non-default or key present in ≥1 instance):")
for rid in sorted(needs_hidden):
    ex = detail[rid]
    print(f"  {rid}: {len(ex)} instances with effective != default")
    if ex:
        print(f"    e.g. {ex[0]}")

print("\nREMOVED IDS — safe to omit from schema entirely:")
for rid in sorted(fully_remove):
    print(f"  {rid} (default everywhere, keys absent)")

# Also list keys present in JSON even if value equals default (Shopify may still strip if not in schema)
present_counts = defaultdict(int)
for _, s in iter_instances():
    for rid in removed:
        if rid in s:
            present_counts[rid] += 1
print("\nKEY PRESENT COUNT (any value) for removed ids:")
for rid in removed:
    if present_counts[rid]:
        print(f"  {rid}: {present_counts[rid]}/42")
