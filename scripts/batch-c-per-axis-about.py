#!/usr/bin/env python3
"""Convert combined fixed-pad flags to per-axis for about + faq sections."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/workspace/shopify-build/sections")

FILES = {
    "page-about-intro": ("pai", "page-about-intro"),
    "page-about-close": ("pac", "page-about-close"),
    "page-about-facts": ("paf", "page-about-facts"),
    "page-about-values": ("pav", "page-about-values"),
    "page-about-joseph": ("paj", "page-about-joseph__copy", "page-about-joseph"),
}

FAQ = "page-faq"


def patch_combined_flags(text: str, prefix: str, block_class: str) -> str:
    text = re.sub(
        rf"assign {prefix}_fixed_d = false\n  if section\.settings\.text_pad_y != {prefix}_y_d_def or section\.settings\.side_padding != {prefix}_side_d_def\n    assign {prefix}_fixed_d = true\n  endif\n  assign {prefix}_fixed_m = false\n  if section\.settings\.text_pad_y_mobile != {prefix}_y_m_def or section\.settings\.text_pad_x_mobile != {prefix}_x_m_def\n    assign {prefix}_fixed_m = true\n  endif",
        f"""assign {prefix}_fixed_d_y = false
  if section.settings.text_pad_y != {prefix}_y_d_def
    assign {prefix}_fixed_d_y = true
  endif
  assign {prefix}_fixed_d_x = false
  if section.settings.side_padding != {prefix}_side_d_def
    assign {prefix}_fixed_d_x = true
  endif
  assign {prefix}_fixed_m_y = false
  if section.settings.text_pad_y_mobile != {prefix}_y_m_def
    assign {prefix}_fixed_m_y = true
  endif
  assign {prefix}_fixed_m_x = false
  if section.settings.text_pad_x_mobile != {prefix}_x_m_def
    assign {prefix}_fixed_m_x = true
  endif""",
        text,
    )
    text = text.replace(
        f"{% if {prefix}_fixed_d %} {block_class}--fixed-pad-d{% endif %}{% if {prefix}_fixed_m %} {block_class}--fixed-pad-m{% endif %}",
        f"{{% if {prefix}_fixed_d_y %}} {block_class}--fixed-pad-d-y{{% endif %}}{{% if {prefix}_fixed_d_x %}} {block_class}--fixed-pad-d-x{{% endif %}}{{% if {prefix}_fixed_m_y %}} {block_class}--fixed-pad-m-y{{% endif %}}{{% if {prefix}_fixed_m_x %}} {block_class}--fixed-pad-m-x{{% endif %}}",
    )
    return text


def patch_css_block(text: str, block_class: str, copy_sel: str | None = None) -> str:
    sel = copy_sel or block_class
    old_d = f"#shopify-section-{{{{ section.id }}}} .{block_class}--fixed-pad-d {{"
    if old_d not in text:
        return text
    # generic replacement for intro-style blocks on root element
    pat = re.compile(
        rf"#shopify-section-\{{\{{ section\.id \}}\}} \.{re.escape(block_class)}--fixed-pad-d \{{[^}}]+\}}\n",
        re.S,
    )
    repl_d = f"""@media (min-width: 769px) {{
    #shopify-section-{{{{ section.id }}}} .{block_class}--fixed-pad-d-y {{
      padding-top: var(--utp-y-d);
      padding-bottom: var(--utp-y-d);
    }}
    #shopify-section-{{{{ section.id }}}} .{block_class}--fixed-pad-d-x {{
      padding-left: var(--utp-side-d);
      padding-right: var(--utp-side-d);
    }}
  }}
"""
    text = pat.sub(repl_d, text, count=1)
    pat_m = re.compile(
        rf"#shopify-section-\{{\{{ section\.id \}}\}} \.{re.escape(block_class)}--fixed-pad-m \{{[^}}]+\}}\n",
        re.S,
    )
    repl_m = f"""#shopify-section-{{{{ section.id }}}} .{block_class}--fixed-pad-m-y {{
      padding-top: var(--utp-y-m);
      padding-bottom: var(--utp-y-m);
    }}
    #shopify-section-{{{{ section.id }}}} .{block_class}--fixed-pad-m-x {{
      padding-left: var(--utp-x-m);
      padding-right: var(--utp-x-m);
    }}
"""
    text = pat_m.sub(repl_m, text, count=1)
    if copy_sel and copy_sel != block_class:
        # joseph targets __copy
        text = text.replace(f".{block_class}--fixed-pad-d-y", f".{copy_sel}--fixed-pad-d-y").replace(
            f".{block_class}--fixed-pad-d-x", f".{copy_sel}--fixed-pad-d-x"
        ).replace(f".{block_class}--fixed-pad-m-y", f".{copy_sel}--fixed-pad-m-y").replace(
            f".{block_class}--fixed-pad-m-x", f".{copy_sel}--fixed-pad-m-x"
        )
    return text


def main() -> None:
    for name, spec in FILES.items():
        prefix, *rest = spec
        block = rest[0] if len(rest) == 1 else rest[1]
        copy = rest[0] if len(rest) == 2 else None
        path = ROOT / f"{name}.liquid"
        text = path.read_text()
        text = patch_combined_flags(text, prefix, block)
        text = patch_css_block(text, block if not copy else block, copy)
        path.write_text(text)
        print("patched", name)


if __name__ == "__main__":
    main()
