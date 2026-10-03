# Unified pads review fix (post a613fdf)

## Snippet fallback chain

`unified-text-pads-vars.liquid` and `unified-text-pads-te-style.liquid` now resolve pads as:

**legacy (template JSON) → unified slider (only when non-blank) → per-section render default** (`y_d` / `side_d` / `y_m` / `x_m` passed into the render).

Unified range settings have **no schema `default`**, so unsaved instances stay blank and legacy + render defaults apply (no forced 96/64/80/20). TE preview uses the same chain and **no `!important`**.

## Per-section render defaults (new slider labels match these)

| Section | y_d | side_d | y_m | x_m | Legacy keys wired in liquid |
|---|---:|---:|---:|---:|---|
| announcement-strip | 5 | 56 | 8 | 16 | pad_y, pad_x, pad_y_mobile |
| article-content | 96 | 40 | 80 | 20 | — |
| blog-listing | 96 | 40 | 80 | 20 | — |
| collab-hero | 96 | 40 | 80 | 20 | — |
| collab-teaser | 40 | 20 | 40 | 16 | — |
| collection-faq | 32 | 40 | 24 | 20 | — |
| collection-hero | 56 | 40 | 36 | 20 | text_spacing_mobile (y_m) |
| contact-cta | 96 | 40 | 80 | 20 | — |
| coperni-crosslink | 24 | 40 | 80 | 20 | — |
| coperni-pdp-story | 28 | 32 | 80 | 20 | — |
| disciplines | 64 | 40 | 48 | 16 | pad_y, pad_y_mobile |
| footer | 48 | 40 | 40 | 20 | — |
| fullbleed-statement | 80 | 40 | 80 | 20 | — |
| geo-section | 32 | 40 | 24 | 20 | — |
| guarantee-band | 20 | 24 | 80 | 20 | — |
| header | 12 | 40 | 12 | 16 | header_pad_y, header_pad_x |
| home-juicer | 12 | 28 | 80 | 20 | — |
| main-cart | 96 | 40 | 80 | 20 | — |
| main-page | 96 | 40 | 80 | 20 | — |
| page-about-close | 14 | 28 | 56 | 20 | — |
| page-about-facts | 48 | 20 | 48 | 20 | — |
| page-about-hero | 96 | 40 | 80 | 20 | — |
| page-about-intro | 32 | 20 | 32 | 20 | — |
| page-about-joseph | 56 | 48 | 28 | 20 | — |
| page-about-split | 56 | 48 | 36 | 20 | media_max_px / media_max_px_mobile (height TE) |
| page-about-values | 40 | 20 | 40 | 20 | — |
| page-ambassador | 96 | 40 | 80 | 20 | — |
| page-compare | 96 | 40 | 80 | 20 | — |
| page-contact | 96 | 40 | 80 | 20 | — |
| page-faq | 96 | 40 | 80 | 20 | — |
| page-grip-comparison | 96 | 40 | 80 | 20 | — |
| page-help | 96 | 40 | 80 | 20 | — |
| page-returns | 96 | 40 | 80 | 20 | — |
| page-shipping | 96 | 40 | 80 | 20 | — |
| page-size-guide | 96 | 40 | 80 | 20 | — |
| page-technology | 96 | 40 | 80 | 20 | — |
| page-warranty | 96 | 40 | 80 | 20 | — |
| page-wholesale | 96 | 40 | 80 | 20 | — |
| pdp-buy-box | 40 | 40 | 32 | 16 | — |
| pdp-features | 32 | 40 | 24 | 20 | pad_top, pad_top_mobile |
| pdp-reviews | 96 | 40 | 80 | 20 | — |
| pdp-sock-math | 96 | 40 | 80 | 20 | pad_top |
| pdp-sticky-atc | 12 | 40 | 10 | 20 | — |
| press-cards | 48 | 40 | 32 | 20 | padding_y, padding_x |
| press-feature | 48 | 40 | 80 | 20 | — |
| press-row | 64 | 40 | 48 | 16 | — |
| proof-numbers | 88 | 40 | 64 | 20 | — |
| recently-viewed | 96 | 40 | 80 | 20 | — |
| recommendations | 96 | 40 | 80 | 20 | — |
| sale-banner | 10 | 56 | 10 | 24 | pad_y |
| search-results | 96 | 40 | 80 | 20 | — |
| sole-cards | 24 | 40 | 24 | 16 | section_pad |
| statement-band | 96 | 40 | 56 | 20 | — |
| studio-trust | 96 | 40 | 80 | 20 | — |
| value-strip | 28 | 40 | 20 | 16 | padding_y, padding_y_mobile |
| variant-grid | 10 | 24 | 80 | 20 | — |
| visual-mosaic | 16 | 16 | 12 | 12 | pad_top, pad_x |

`fifty-fifty`, `problem-section`, and `split-hero` keep their existing in-section pad logic (not migrated to shared snippets on this branch).

## Template instances with legacy pad values (read-only scan)

These still store legacy keys; liquid prefers legacy over blank unified sliders:

| Template | Section type | Legacy key | Saved value |
|---|---|---|---|
| index.json, collection.json | disciplines | pad_y / pad_y_mobile | 64 / 64 |
| index.json | press-cards | padding_y / padding_x | 40 / 40 |
| index.json, collection.json | visual-mosaic | pad_x | 16 |
| collection.json | collection-hero | text_spacing_mobile | 36 |
| product.in-studio-template.json, product.open-sole.json | value-strip | padding_y | 28 |
| several collection/product templates | value-strip | padding_y | 20 |
| many product/collection templates | fifty-fifty | vertical_padding | 80 or 88 |

Header group (`sections/header-group.json`) still stores legacy `pad_y` on announcement instances (9–10px).

## Schema / TE fixes in this pass

- Repaired orphaned “Layout — text padding” blocks (all section schemas parse as valid JSON).
- Removed unified range **defaults** and erroneous **min_height** / **mobile_media_height** defaults where they overwrote legacy height.
- **announcement-strip:** removed duplicate legacy `pad_y` / `pad_x` / `pad_y_mobile` ids; added `aria_label` gate field.
- **header:** legacy hide uses `aria_label` (field added); TE targets `.site-header__inner`.
- **disciplines:** single legacy `pad_y` / `pad_y_mobile` pair (hidden); unified + legacy wired.
- **guarantee-band / home-juicer / page-about-close:** TE selectors retargeted to section wrappers with correct render defaults.
- **page-about-split:** `section_gap_mobile` scoped to phone; `heading_level` rendered; height TE prefers legacy `media_max_px` when unified blank.

## Theme Check

Run: `shopify theme check` from `shopify-build/` (log: `/opt/cursor/artifacts/theme-check-unified-pads-fix.log`).

Summary after fix pass: **175 files, 428 offenses (300 errors, 128 warnings)** — pre-existing missing customer account sections and baseline theme noise; **0 invalid section schema JSON** in `sections/*.liquid`.
