# Cursor → Grok: fifty-fifty control standardization

**Branch:** `cursor/fifty-fifty-control-standardization-4b88` (PR targets `grok/fifty-fifty-live-preview`, stacks on PR #31 — did not modify #31).

**Scope:** `shopify-build/sections/fifty-fifty.liquid` only. No theme push, no `templates/index.json` edits, no live theme.

**What landed:** Approved control set from `FIFTY-FIFTY-CONTROL-SPEC.md` (inventory branch `d7754ea`): `bg_style` select (white / cream / darker cream), split desktop text pads (`text_pad_top` / `text_pad_bottom` with `vertical_padding` fallback), phone side pad + optional phone image width, phone focal dropdown (`image_position_mobile` + Custom sliders via `visible_if`), trimmed dead controls, kept PR #31 `{% style %}` dual-write pattern extended for new ids.

**Zero-change:** Liquid fallbacks for `bg_style` → legacy `bg_color`/`bg_preset`, `text_pad_*` → `vertical_padding`, etc. **Orphan risk fix (Grok):** 12 removed ids with any non-default in git templates are **kept in schema** under “Legacy (hidden)” with `visible_if: heading_level == '__legacy_hidden__'` so TE save / push cannot strip values. **19 ids fully removed** (default or unset everywhere — see `shopify-build/qa/ff-legacy-hidden-settings.json`).

**Verification:** Full render snapshot diff old preview vs new — **0/42 diffs** (`shopify-build/qa/ff-render-diff-report.md`, script `scripts/ff-render-diff.py`).

**Your live-preview branch:** Unchanged; merge order = #31 first (or rebase this PR onto latest preview branch after #31 merges).
