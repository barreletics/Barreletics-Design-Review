#!/usr/bin/env python3
"""Validate every shopify-build template against the section schemas it references."""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TPL = os.path.join(ROOT, "shopify-build", "templates")
SEC = os.path.join(ROOT, "shopify-build", "sections")

SETTING_CONTAINERS = {"header", "paragraph"}


def load_schema(section_type):
    path = os.path.join(SEC, section_type + ".liquid")
    if not os.path.exists(path):
        return None, None
    src = open(path, encoding="utf-8").read()
    m = re.search(r"\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}", src, re.S)
    if not m:
        return src, None
    try:
        return src, json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return src, {"__error__": str(e)}


def keys_from(settings_list):
    keys = set()
    for s in settings_list or []:
        if s.get("type") in SETTING_CONTAINERS:
            continue
        if "id" in s:
            keys.add(s["id"])
    return keys


def walk_templates():
    files = []
    for dirpath, _, names in os.walk(TPL):
        for n in sorted(names):
            if n.endswith(".json"):
                files.append(os.path.join(dirpath, n))
    return sorted(files)


def main():
    report = {
        "json_errors": [],
        "missing_sections": [],
        "schema_parse_errors": [],
        "bad_setting_keys": [],
        "bad_block_types": [],
        "bad_block_setting_keys": [],
        "empty_string_settings": [],
        "order_mismatch": [],
        "used_settings": defaultdict(set),
    }
    schemas = {}

    for path in walk_templates():
        rel = os.path.relpath(path, ROOT)
        try:
            data = json.loads(open(path, encoding="utf-8").read())
        except Exception as e:
            report["json_errors"].append(f"{rel}: {e}")
            continue
        if not isinstance(data, dict):
            continue
        sections = data.get("sections") or {}
        order = data.get("order") or []
        for sid in order:
            if sid not in sections:
                report["order_mismatch"].append(f"{rel}: order id '{sid}' has no section entry")
        for sid in sections:
            if order and sid not in order:
                report["order_mismatch"].append(f"{rel}: section '{sid}' not in order (will not render)")

        for sid, sec in sections.items():
            stype = sec.get("type")
            if not stype:
                report["json_errors"].append(f"{rel}: section '{sid}' missing type")
                continue
            if stype not in schemas:
                schemas[stype] = load_schema(stype)
            src, schema = schemas[stype]
            if src is None:
                report["missing_sections"].append(f"{rel}: section '{sid}' -> sections/{stype}.liquid MISSING")
                continue
            if schema is None:
                report["schema_parse_errors"].append(f"sections/{stype}.liquid: no {{% schema %}} block")
                continue
            if "__error__" in schema:
                report["schema_parse_errors"].append(f"sections/{stype}.liquid: {schema['__error__']}")
                continue

            valid = keys_from(schema.get("settings"))
            for k, v in (sec.get("settings") or {}).items():
                if k not in valid:
                    report["bad_setting_keys"].append(f"{rel}: {sid} ({stype}).settings.{k} NOT IN SCHEMA")
                else:
                    report["used_settings"][stype].add(k)
                if isinstance(v, str) and v.strip() == "":
                    report["empty_string_settings"].append(f"{rel}: {sid} ({stype}).{k} = \"\"")

            blocks = sec.get("blocks") or {}
            btypes = {b.get("type"): keys_from(b.get("settings")) for b in (schema.get("blocks") or [])}
            for bid, blk in blocks.items():
                bt = blk.get("type")
                if bt not in btypes:
                    report["bad_block_types"].append(f"{rel}: {sid} ({stype}) block '{bid}' type '{bt}' NOT IN SCHEMA")
                    continue
                for k, v in (blk.get("settings") or {}).items():
                    if k not in btypes[bt]:
                        report["bad_block_setting_keys"].append(
                            f"{rel}: {sid} ({stype}) block '{bid}' [{bt}].{k} NOT IN SCHEMA")
                    else:
                        report["used_settings"][stype + "#" + bt].add(k)
                    if isinstance(v, str) and v.strip() == "":
                        report["empty_string_settings"].append(f"{rel}: {sid} ({stype}) block {bid} [{bt}].{k} = \"\"")
            bo = sec.get("block_order")
            if bo:
                for b in bo:
                    if b not in blocks:
                        report["order_mismatch"].append(f"{rel}: {sid} block_order '{b}' missing from blocks")
                for b in blocks:
                    if b not in bo:
                        report["order_mismatch"].append(f"{rel}: {sid} block '{b}' not in block_order")

    # orphaned settings
    orphans = []
    for stype, (src, schema) in sorted(schemas.items()):
        if not schema or "__error__" in schema:
            continue
        declared = keys_from(schema.get("settings"))
        used = report["used_settings"].get(stype, set())
        for k in sorted(declared - used):
            orphans.append(f"sections/{stype}.liquid: setting '{k}' unused by any template")
    report["orphaned_settings"] = orphans
    report["used_settings"] = {k: sorted(v) for k, v in report["used_settings"].items()}

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schema-report.json")
    json.dump(report, open(out, "w"), indent=2)

    for key in ["json_errors", "missing_sections", "schema_parse_errors", "bad_setting_keys",
                "bad_block_types", "bad_block_setting_keys", "order_mismatch"]:
        items = report[key]
        print(f"\n=== {key.upper()} ({len(items)}) ===")
        for i in items:
            print("  " + i)
    print(f"\n=== EMPTY STRING SETTINGS ({len(report['empty_string_settings'])}) ===")
    for i in report["empty_string_settings"]:
        print("  " + i)
    print(f"\n=== ORPHANED SETTINGS ({len(orphans)}) === (see json)")


if __name__ == "__main__":
    main()
