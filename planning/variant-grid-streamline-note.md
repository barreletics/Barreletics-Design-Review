# Variant Grid streamline note — 2026-07-30

## Kept
- Open / Closed / One-Offs / Outdoor tabs (enable + label + product each)
- Variant cards via `variant-card` (Home WORKING chrome)
- Size M/L, Compare + Size chart, 2-row See all (`VARIANTS-GRID.md`)
- Header chrome (eyebrow / title / body) unchanged

## Removed / not ported from `br-variants` / early stub
- ~4.5k-line TE style sprawl (fonts, paddings, badge color matrices)
- Dual one-off pickers (`product_4` / `product_5`) → one One-Offs product
- Hardcoded `all_products[...]` fallbacks that forced every tab on
- Mega-collection + tag-filter stub
- Duplicate per-tab Liquid loops → `variant-grid-panel` snippet

## TE wiring
Theme Editor → **Variant Grid** → **Tabs — enable + product per tab**  
Turn a tab off with its Show checkbox, or leave the product blank.
