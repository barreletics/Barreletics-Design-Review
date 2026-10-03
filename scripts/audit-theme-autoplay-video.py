#!/usr/bin/env python3
"""Find theme files where autoplay video might play with sound (no muted)."""
import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build")
REPORT = ROOT / "qa" / "autoplay-video-sound-audit.md"

SKIP = ("backups/", "node_modules/")


def scan_file(path: Path) -> list[str]:
    issues = []
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)
    # video_tag with autoplay
    for m in re.finditer(r"video_tag:[\s\S]*?\}", text):
        block = m.group(0)
        if "autoplay" not in block.lower():
            continue
        if re.search(r"muted:\s*false", block):
            issues.append(f"{rel}: video_tag autoplay with muted:false")
        elif "muted" not in block:
            issues.append(f"{rel}: video_tag autoplay without muted:")
    # raw <video tags
    for m in re.finditer(r"<video[\s\S]*?>", text, re.I):
        tag = m.group(0)
        if "autoplay" not in tag.lower():
            continue
        if re.search(r"\bmuted\b", tag, re.I) is None:
            issues.append(f"{rel}: <video autoplay> without muted attribute")
    return issues


def main():
    all_issues = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in (".liquid", ".json"):
            continue
        if any(s in str(path) for s in SKIP):
            continue
        all_issues.extend(scan_file(path))

    lines = [
        "# Autoplay video sound audit",
        "",
        "Sections checked: `shopify-build/**/*.liquid` (excluding backups).",
        "",
        "**Policy:** Background/autoplay videos must always be muted (HTML + JS).",
        "",
    ]
    if all_issues:
        lines.append(f"**Risk findings:** {len(all_issues)}\n")
        for i in all_issues:
            lines.append(f"- {i}")
    else:
        lines.append(
            "**Risk findings:** 0 — no autoplay video markup without `muted` in theme liquid."
        )
        lines.append("")
        lines.append(
            "fifty-fifty + split-hero also use `snippets/bg-video-autoplay-script.liquid` to force `v.muted = true` and `play()` on load and `shopify:section:load`."
        )
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT.read_text())
    return 1 if all_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
