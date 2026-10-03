# Unified pads — second review fix

## Snippet fallback (vars + TE style)

Parameters `y_d`, `side_d`, `y_m`, `x_m` **must match** the `default` on the four unified range settings in that section’s schema.

1. If unified slider value **≠** schema default → use unified (merchant moved the slider).
2. Else if legacy argument is **not blank** → use legacy (template JSON still stores old keys).
3. Else → use unified value (= schema default).

## Per-section schema defaults (labels match)

| Section | text_pad_y | side_padding | text_pad_y_mobile | text_pad_x_mobile | Legacy wired |
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
| page-about-split | 56 | 48 | 36 | 20 | media_max_px / media_max_px_mobile (height) |
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

**Not modified on this branch (reverted to `108fff6`):** `fifty-fifty`, `problem-section`, `split-hero` — already verified on the split-section stack; no unified-pad migration required there for this PR.

## Theme Check vs `108fff6`

| Run | Files | Offenses | Errors | Warnings |
|---|---:|---:|---:|---:|
| Baseline `108fff6` | 170 | 155 | 33 | 122 |
| After second-review fix | 175 | 155 | 33 | 122 |

**Offense diff count (unique file + check):** **0 new**, **0 removed** (`ValidSchema` / missing `default`: **0**).

Logs: `/opt/cursor/artifacts/theme-check-baseline-108fff6.log`, `/opt/cursor/artifacts/theme-check-second-review-fix.log`.
