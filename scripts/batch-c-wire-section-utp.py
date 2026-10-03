#!/usr/bin/env python3
"""Wire unified text pads on Batch C .section-root pages (storefront + TE selector)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build/sections")

OLD_VARS = "y_d: 96, side_d: 40, y_m: 80, x_m: 20"
NEW_VARS = "y_d: 32, side_d: 40, y_m: 48, x_m: 16"

UTP_CSS = """
<style>
  #shopify-section-{{ section.id }} {{TE_SELECTOR}} {
    padding-top: var(--utp-y-d, var(--section-padding-y));
    padding-bottom: var(--utp-y-d, var(--section-padding-y));
    padding-left: var(--utp-side-d, var(--section-padding-x));
    padding-right: var(--utp-side-d, var(--section-padding-x));
  }
  @media (max-width: 768px) {
    #shopify-section-{{ section.id }} {{TE_SELECTOR}} {
      padding-top: var(--utp-y-m, var(--section-padding-y));
      padding-bottom: var(--utp-y-m, var(--section-padding-y));
      padding-left: var(--utp-x-m, var(--section-padding-x));
      padding-right: var(--utp-x-m, var(--section-padding-x));
    }
  }
</style>
"""

# section file -> TE/storefront selector (child of #shopify-section-id wrapper)
CONFIG = {
    "page-contact": ".page-contact__root",
    "page-shipping": ".page-shipping__root",
    "page-warranty": ".page-warranty__root",
    "page-technology": ".page-tech__root",
    "page-ambassador": ".page-ambassador__root",
    "page-compare": ".page-compare",
    "page-wholesale": ".page-wholesale__head",
    "page-size-guide": ".page-size__head",
    "page-returns": ".page-returns-head",
    "page-grip-comparison": ".page-grip__root",
    "page-help": ".page-help",
    "main-page": ".page-content",
}


def add_root_class(text: str, name: str) -> str:
    if name == "page-contact":
        return text.replace(
            '<section\n  class="section"\n  id="shopify-section-{{ section.id }}"',
            '<section\n  class="page-contact__root section"\n  id="shopify-section-{{ section.id }}"',
            1,
        )
    if name == "page-shipping":
        return text.replace(
            '<section class="section" id="shopify-section-{{ section.id }}"',
            '<section class="page-shipping__root section" id="shopify-section-{{ section.id }}"',
            1,
        )
    if name == "page-warranty":
        return text.replace(
            '<section class="section" id="shopify-section-{{ section.id }}"',
            '<section class="page-warranty__root section" id="shopify-section-{{ section.id }}"',
            1,
        )
    if name == "page-technology":
        return text.replace(
            '<section class="section" id="shopify-section-{{ section.id }}"',
            '<section class="page-tech__root section" id="shopify-section-{{ section.id }}"',
            1,
        )
    if name == "page-ambassador":
        return text.replace(
            '<section class="section" id="shopify-section-{{ section.id }}"',
            '<section class="page-ambassador__root section" id="shopify-section-{{ section.id }}"',
            1,
        )
    if name == "page-grip-comparison":
        return text.replace(
            '<section class="section section--dark" id="shopify-section-{{ section.id }}"',
            '<section class="page-grip__root section section--dark" id="shopify-section-{{ section.id }}"',
            1,
        )
    return text


def patch_schema_defaults(text: str) -> str:
    m = re.search(r"(\{% schema %\}\s*)(\{.*\})(\s*\{% endschema %\})", text, re.S)
    if not m:
        return text
    schema = json.loads(m.group(2))
    for s in schema.get("settings", []):
        if s.get("id") == "text_pad_y" and s.get("default") == 96:
            s["default"] = 32
            s["label"] = s["label"].replace("(default 96)", "(default 32)")
        if s.get("id") == "text_pad_y_mobile" and s.get("default") == 80:
            s["default"] = 48
            s["label"] = s["label"].replace("(default 80)", "(default 48)")
        if s.get("id") == "text_pad_x_mobile" and s.get("default") == 20:
            s["default"] = 16
            s["label"] = s["label"].replace("(default 20)", "(default 16)")
    new_json = json.dumps(schema, indent=2)
    return text[: m.start(2)] + new_json + text[m.end(2) :]


def main() -> None:
    for name, sel in CONFIG.items():
        path = ROOT / f"{name}.liquid"
        text = path.read_text()
        if OLD_VARS not in text:
            print("skip vars", name)
            continue
        text = text.replace(OLD_VARS, NEW_VARS)
        text = add_root_class(text, name)
        marker = "{% render 'unified-text-pads-te-style'"
        css = UTP_CSS.replace("{{TE_SELECTOR}}", sel)
        if css.strip() not in text.replace(" ", ""):
            text = text.replace(marker, css + "\n" + marker, 1)
        text = re.sub(
            r"\{% render 'unified-text-pads-te-style', selector: '[^']*', y_d: 32, side_d: 40, y_m: 48, x_m: 16 %\}",
            f"{{% render 'unified-text-pads-te-style', selector: '{sel}', y_d: 32, side_d: 40, y_m: 48, x_m: 16 %}}",
            text,
            count=1,
        )
        text = patch_schema_defaults(text)
        path.write_text(text)
        print("patched", name)


if __name__ == "__main__":
    main()
