#!/usr/bin/env python3
"""Report CTA/trust href resolution for split-hero + fifty-fifty instances in git templates."""
import json
from pathlib import Path

TEMPLATES = Path("/workspace/shopify-build/templates")


def load_template_json(path: Path):
    raw = path.read_text()
    if raw.lstrip().startswith("/*"):
        raw = raw[raw.index("*/") + 2 :]
    return json.loads(raw)


def href(target_key, custom_url):
    t = target_key or "custom"
    if t and t != "custom":
        return t
    return custom_url or "(blank → theme default collection URL in liquid)"


def main():
    lines = ["# CTA / trust href audit (git templates)", ""]
    for path in sorted(TEMPLATES.glob("*.json")):
        try:
            data = load_template_json(path)
        except (json.JSONDecodeError, ValueError):
            continue
        for key, sec in data.get("sections", {}).items():
            st = sec.get("type")
            s = sec.get("settings") or {}
            if st == "split-hero":
                lines.append(f"## split-hero `{path.stem}:{key}`")
                lines.append(f"- CTA target `{s.get('cta_link_target', 'custom')}` → href `{href(s.get('cta_link_target'), s.get('cta_url'))}`")
                lines.append(f"- Trust target `{s.get('trust_link_target', 'custom')}` → href `{href(s.get('trust_link_target'), s.get('trust_url'))}`")
                lines.append(f"- Tag target `{s.get('tag_link_target', 'custom')}` → href `{href(s.get('tag_link_target'), s.get('tag_url'))}`")
                lines.append(f"- image_url set: {bool(s.get('image_url'))} (fallback when Shopify image empty)")
                lines.append("")
            if st == "fifty-fifty":
                if s.get("cta_text") or s.get("cta_link_target") or s.get("cta_url"):
                    lines.append(f"## fifty-fifty `{path.stem}:{key}`")
                    lines.append(f"- CTA target `{s.get('cta_link_target', 'custom')}` → href `{href(s.get('cta_link_target'), s.get('cta_url'))}`")
                    lines.append("")
    out = Path("/workspace/shopify-build/qa/cta-trust-url-audit.md")
    out.write_text("\n".join(lines))
    print(out.read_text())


if __name__ == "__main__":
    main()
