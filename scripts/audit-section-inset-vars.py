#!/usr/bin/env python3
"""
Audit old vs new section-inset-vars.liquid computed CSS vars per placed instance.

Old snippet: mobile vars always from mobile sliders (desktop vars unchanged).
New snippet: when inset_custom_mobile is falsy, mobile vars = desktop vars.

Scans templates/*.json and sections/*.json (header/footer groups).
"""
import json
import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build")
TEMPLATES = ROOT / "templates"
SECTION_GROUPS = ROOT / "sections"
SECTIONS_LIQUID = ROOT / "sections"
REPORT = ROOT / "qa" / "section-inset-vars-audit.md"


def discover_snippet_sections() -> list[str]:
    names = []
    for path in sorted(SECTIONS_LIQUID.glob("*.liquid")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "section-inset-vars" in text:
            names.append(path.stem)
    return names


def load_json(path: Path):
    raw = path.read_text(encoding="utf-8")
    if raw.lstrip().startswith("/*"):
        raw = raw[raw.index("*/") + 2 :]
    return json.loads(raw)


def resolve_inset_x(s, desktop=True):
    if desktop:
        v = s.get("inset_x")
        if v is None or v == "":
            v = s.get("inset_left")
            if v is None or v == "":
                v = s.get("inset_right")
        return 0 if v is None or v == "" else int(v)
    v = s.get("inset_x_mobile")
    if v is None or v == "":
        v = s.get("inset_left_mobile")
        if v is None or v == "":
            v = s.get("inset_right_mobile")
    return 0 if v is None or v == "" else int(v)


def compute(s, mode: str):
    top = int(s.get("inset_top") or 0)
    bottom = int(s.get("inset_bottom") or 0)
    x = resolve_inset_x(s, True)
    desktop = (top, x, bottom, x)
    if mode == "old":
        top_m = int(s.get("inset_top_mobile") or 0)
        bottom_m = int(s.get("inset_bottom_mobile") or 0)
        x_m = resolve_inset_x(s, False)
    else:
        custom = s.get("inset_custom_mobile")
        if custom is True:
            top_m = int(s.get("inset_top_mobile") or 0)
            bottom_m = int(s.get("inset_bottom_mobile") or 0)
            x_m = resolve_inset_x(s, False)
        else:
            top_m, bottom_m, x_m = top, bottom, x
    phone = (top_m, x_m, bottom_m, x_m)
    return {
        "desktop": desktop,
        "phone": phone,
        "inset_custom_mobile": s.get("inset_custom_mobile"),
    }


def iter_instances(snippet_sections: set[str]):
    json_paths = sorted(TEMPLATES.glob("*.json"))
    json_paths.extend(sorted(SECTION_GROUPS.glob("*.json")))
    for path in json_paths:
        try:
            data = load_json(path)
        except (json.JSONDecodeError, ValueError):
            continue
        rel = path.relative_to(ROOT)
        for key, sec in (data.get("sections") or {}).items():
            st = sec.get("type")
            if st in snippet_sections:
                yield str(rel.with_suffix("")), key, st, sec.get("settings") or {}


def main():
    snippet_sections = discover_snippet_sections()
    snippet_set = set(snippet_sections)
    instances = list(iter_instances(snippet_set))

    diffs = []
    desktop_diffs = []
    for tmpl, key, st, s in instances:
        old = compute(s, "old")
        new = compute(s, "new")
        if old["phone"] != new["phone"]:
            diffs.append((tmpl, key, st, old, new))
        if old["desktop"] != new["desktop"]:
            desktop_diffs.append((tmpl, key, st, old, new))

    lines = [
        "# section-inset-vars audit (old vs new snippet logic)",
        "",
        "## Methodology",
        "",
        "- **Old:** `--section-inset-*-m` always from mobile slider settings.",
        "- **New:** When `inset_custom_mobile` is not true, `--section-inset-*-m` copies desktop values.",
        "- **Desktop** vars (`--section-inset-top/right/bottom/left`) are identical in old and new snippet logic.",
        "- Compared tuple `(top, left/right, bottom, right/left)` for desktop and phone from each instance's JSON settings.",
        "- Sources: `shopify-build/templates/*.json`, `shopify-build/sections/*.json` (header/footer groups).",
        "",
        "## Sections that render `snippets/section-inset-vars.liquid`",
        "",
        f"**Count:** {len(snippet_sections)} (discovered via grep on `sections/*.liquid`)",
        "",
    ]
    for name in snippet_sections:
        lines.append(f"- `sections/{name}.liquid`")

    lines.extend(
        [
            "",
            f"**Placed instances scanned:** {len(instances)}",
            f"**Desktop computed inset diffs (old vs new):** {len(desktop_diffs)}",
            f"**Phone computed inset diffs (old vs new):** {len(diffs)}",
            "",
        ]
    )

    if desktop_diffs:
        lines.append("## Desktop diffs (unexpected)\n")
        for tmpl, key, st, old, new in desktop_diffs:
            lines.append(f"- `{tmpl}:{key}` ({st}): {old['desktop']} → {new['desktop']}")
        lines.append("")

    if diffs:
        lines.append("## Phone diffs (old → new)\n")
        for tmpl, key, st, old, new in diffs:
            lines.append(f"### `{tmpl}:{key}` (`{st}`)\n")
            lines.append(f"- `inset_custom_mobile`: {new['inset_custom_mobile']!r}")
            lines.append(f"- Desktop vars: `{old['desktop']}` (unchanged by snippet)")
            lines.append(f"- Phone OLD: `{old['phone']}`")
            lines.append(f"- Phone NEW: `{new['phone']}`")
            lines.append("")
        lines.append(
            "**Action required:** Revert `snippets/section-inset-vars.liquid` and localize new inset behavior to fifty-fifty / split-hero only.\n"
        )
    else:
        lines.append(
            "**Zero phone diffs** across all placed instances in git — shared snippet change does not alter computed inset CSS for any committed template/group JSON.\n"
        )
        lines.append(
            "_Note: If a merchant sets non-zero desktop inset with `inset_custom_mobile` off only in Theme Editor (not in git), phone rendering would change under the new snippet; no such saves exist in this repo._\n"
        )

    lines.append("## All instances (desktop + phone computed vars)\n")
    lines.append(
        "| source:section | type | custom_m | desktop (old=new) | phone old | phone new | phone diff |"
    )
    lines.append("|---|---|---:|---|---|---|---|")
    for tmpl, key, st, s in instances:
        old = compute(s, "old")
        new = compute(s, "new")
        d = old["phone"] != new["phone"]
        lines.append(
            f"| `{tmpl}:{key}` | {st} | {new['inset_custom_mobile']!r} | {old['desktop']} | {old['phone']} | {new['phone']} | {'**YES**' if d else 'no'} |"
        )

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {REPORT} ({len(instances)} instances, {len(diffs)} phone diffs)")
    return 1 if diffs else 0


if __name__ == "__main__":
    raise SystemExit(main())
