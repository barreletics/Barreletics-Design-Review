# TE control consolidation — draft theme 187144929571 (git only)

**Date:** 2026-10-05  
**Visual intent:** Schema + wiring only; defaults preserve current CSS (insets 0, custom mobile off).

## Priority holdouts

| Section | bg TE | Shared — Section frame | Media adj (existing) |
|---------|-------|------------------------|-------------------------|
| `fifty-fifty` | bg_style / panel | Added `inset_*` + custom mobile; band gap stays section-specific | Yes (unchanged) |
| `problem-section` | bg_preset / bg_color | Added full frame block | Yes |
| `press-cards` | bg_color | Added full frame block | Block-level image fit |
| `press-feature` | bg_color | Wired + schema | Desktop/mobile fit + position |
| `press-row` | bg_color | Wired + schema | Hero/card media |
| `pdp-sock-math` | Liquid template bg | Wired + schema | image_crop / frame |
| `collab-teaser` | bg_color | Header + custom mobile + mobile insets | N/A |
| `visual-mosaic` | pad / tiles | Renamed Page inset → Shared; `inset_custom_mobile` | Tile + section media fit |

**`origin-statement.liquid`:** Not present in repo. Closest match: `page-about-intro` (About origin copy) — now has frame + bg.

## Also updated (remaining marketing / content gaps)

- `contact-cta`, `sale-banner`, `social-proof`, `studio-trust`
- All `page-*` sections in `shopify-build/sections/` (frame wire + schema; bg where added with defaults matching prior look)
- `page-about-joseph` (article root wired)
- `page-returns` (schema frame; liquid was already wired)
- `fullbleed-statement` (Shared frame parity: custom mobile + mobile sliders; desktop-only fullbleed copy preserved)

## Intentionally skipped

| Area | Why |
|------|-----|
| `header`, `footer`, `main-cart` | Chrome — not full Shared marketing migration |
| `pdp-buy-box`, `pdp-sticky-atc` | Commerce modules |
| `announcement-strip` | Separate visibility model |
| `collection-hero`, `hero`, `split-hero` (already gold) | Already at Shared pattern or hero-specific |
| `coperni-crosslink`, `coperni-pdp-story` | PDP/collab commerce story — partial inset wire only |
| `pdp-reviews` | Reviews commerce module |
| Template JSON | Not modified (inset audit: 0 phone diffs vs new snippet) |

## Proof

- `python3 scripts/audit-section-inset-vars.py` → 211 instances, **0 phone diffs**
- `python3 scripts/lock-scan.py` → pre-existing template/lock mismatches on index/open-sole; **no template JSON edited in this pass**

## Shopify push (Andrew / Mac)

`SHOPIFY_ADMIN_ACCESS_TOKEN` not set in cloud env. Push draft **187144929571** only:

```bash
cd shopify-build
shopify theme push --theme 187144929571 --only \
  sections/fifty-fifty.liquid \
  sections/problem-section.liquid \
  sections/press-cards.liquid \
  sections/press-feature.liquid \
  sections/press-row.liquid \
  sections/pdp-sock-math.liquid \
  sections/collab-teaser.liquid \
  sections/visual-mosaic.liquid \
  sections/fullbleed-statement.liquid \
  sections/contact-cta.liquid \
  sections/sale-banner.liquid \
  sections/social-proof.liquid \
  sections/studio-trust.liquid \
  sections/page-about-intro.liquid \
  sections/page-about-joseph.liquid \
  sections/page-returns.liquid
# …add other changed page-* files from git diff --name-only
```

Then pull-verify changed files on the remote theme.
