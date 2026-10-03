# Unified text pads migration report

All migrated sections use the same four Theme Editor control **ids** and order as `fifty-fifty.liquid`. **Labels show each section’s real render default** (not a global 96/64/80/20). Range settings have **no schema default** so blank instances fall back to legacy JSON keys, then liquid render defaults.

Shared snippets: `unified-text-pads-vars.liquid`, `unified-text-pads-te-style.liquid` — **legacy → unified (if set) → render default**; TE preview without `!important`.

See `unified-pads-review-fix-report.md` for the full per-section default table and template legacy instances.

| Section | Old pad settings | New pad settings | Render defaults (y_d, side_d, y_m, x_m) | Notes |
|---|---|---|---|---|
| announcement-strip | pad_x, pad_y, pad_y_mobile | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 5, 56, 8, 16 | Selector .announcement-strip; TE preview snippet |
| article-content | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| blog-listing | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| collab-hero | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| collab-teaser | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 40, 20, 40, 16 | Selector .collab-teaser; TE preview snippet |
| collection-faq | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 32, 40, 24, 20 | Selector .section-frame; TE preview snippet |
| collection-hero | Media type, Mobile text spacing, Photo height, Show trust line, text_spacing_mobile | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 56, 40, 36, 20 | Selector .coll-hero--split, .coll-hero:not(.coll-hero--split); TE preview snippet |
| contact-cta | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| coperni-crosslink | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 24, 40, 80, 20 | Selector .csb-content; TE preview snippet |
| coperni-pdp-story | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 28, 32, 80, 20 | Selector .coperni-story__note; TE preview snippet |
| disciplines | pad_y, pad_y_mobile | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 64, 40, 48, 16 | Selector .discipline-film__inner; TE preview snippet |
| fifty-fifty | — (pre-unified) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | — | Skipped — already had fifty-fifty pad set |
| footer | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 48, 40, 40, 20 | Selector .section-frame; TE preview snippet |
| fullbleed-statement | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 80, 40, 80, 20 | Selector .fullbleed-statement__content; TE preview snippet |
| geo-section | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 32, 40, 24, 20 | Selector .section-frame; TE preview snippet |
| guarantee-band | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 20, 24, 80, 20 | Selector .guarantee-item; TE preview snippet |
| header | header_pad_x, header_pad_y | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 12, 40, 12, 16 | Selector .site-header; TE preview snippet |
| home-juicer | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 12, 28, 80, 20 | Selector .home-juicer__see-more; TE preview snippet |
| main-cart | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| main-page | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-about-close | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 14, 28, 56, 20 | Selector .page-about-close__cta; TE preview snippet |
| page-about-facts | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 48, 20, 48, 20 | Selector .page-about-facts; TE preview snippet |
| page-about-hero | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-about-intro | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 32, 20, 32, 20 | Selector .page-about-intro; TE preview snippet |
| page-about-joseph | Body size, Body weight, Heading size override, Heading weight | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 56, 48, 28, 20 | Selector .page-about-joseph__copy; TE preview snippet |
| page-about-split | — (pre-unified) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | — | Skipped — already had fifty-fifty pad set |
| page-about-values | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 40, 20, 40, 20 | Selector .page-about-values; TE preview snippet |
| page-ambassador | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-compare | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-contact | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-faq | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-grip-comparison | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-help | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-returns | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-shipping | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-size-guide | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-technology | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-warranty | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| page-wholesale | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| pdp-buy-box | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| pdp-features | pad_bottom, pad_bottom_mobile, pad_top, pad_top_mobile | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 32, 40, 24, 20 | Selector .pdp-features; TE preview snippet |
| pdp-reviews | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| pdp-sock-math | pad_bottom, pad_top | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| pdp-sticky-atc | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 12, 40, 10, 20 | Selector .section-frame; TE preview snippet |
| press-cards | padding_x, padding_y | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 48, 40, 32, 20 | Selector .press-cards; TE preview snippet |
| press-feature | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 48, 40, 80, 20 | Selector .twin-frame; TE preview snippet |
| press-row | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 64, 40, 48, 16 | Selector .press-row; TE preview snippet |
| problem-section | — (pre-unified) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | — | Skipped — already had fifty-fifty pad set |
| proof-numbers | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 88, 40, 64, 20 | Selector .proof-numbers; TE preview snippet |
| recently-viewed | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| recommendations | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| sale-banner | pad_y | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 10, 56, 10, 24 | Selector .sale-banner; TE preview snippet |
| search-results | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| sole-cards | section_pad | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 24, 40, 24, 16 | Selector .sole-cards-band; TE preview snippet |
| split-hero | — (pre-unified) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | — | Skipped — already had fifty-fifty pad set |
| statement-band | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 56, 20 | Selector .statement-band; TE preview snippet |
| studio-trust | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 96, 40, 80, 20 | Selector .section-frame; TE preview snippet |
| value-strip | — (pre-unified) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | — | Skipped — already had fifty-fifty pad set |
| variant-grid | (hardcoded / theme tokens) | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 10, 24, 80, 20 | Selector .variants-tab; TE preview snippet |
| visual-mosaic | pad_bottom, pad_top, pad_x | text_pad_y, side_padding, text_pad_y_mobile, text_pad_x_mobile | 16, 16, 12, 12 | Selector .visual-mosaic; TE preview snippet |
