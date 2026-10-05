# section-inset-vars audit (old vs new snippet logic)

## Methodology

- **Old:** `--section-inset-*-m` always from mobile slider settings.
- **New:** When `inset_custom_mobile` is not true, `--section-inset-*-m` copies desktop values.
- **Desktop** vars (`--section-inset-top/right/bottom/left`) are identical in old and new snippet logic.
- Compared tuple `(top, left/right, bottom, right/left)` for desktop and phone from each instance's JSON settings.
- Sources: `shopify-build/templates/*.json`, `shopify-build/sections/*.json` (header/footer groups).

## Sections that render `snippets/section-inset-vars.liquid`

**Count:** 48 (discovered via grep on `sections/*.liquid`)

- `sections/collab-hero.liquid`
- `sections/collab-teaser.liquid`
- `sections/contact-cta.liquid`
- `sections/coperni-crosslink.liquid`
- `sections/coperni-pdp-story.liquid`
- `sections/disciplines.liquid`
- `sections/fifty-fifty.liquid`
- `sections/fullbleed-statement.liquid`
- `sections/guarantee-band.liquid`
- `sections/home-juicer.liquid`
- `sections/main-page.liquid`
- `sections/page-about-close.liquid`
- `sections/page-about-facts.liquid`
- `sections/page-about-hero.liquid`
- `sections/page-about-intro.liquid`
- `sections/page-about-joseph.liquid`
- `sections/page-about-split.liquid`
- `sections/page-about-values.liquid`
- `sections/page-about.liquid`
- `sections/page-ambassador.liquid`
- `sections/page-compare.liquid`
- `sections/page-contact.liquid`
- `sections/page-faq.liquid`
- `sections/page-grip-comparison.liquid`
- `sections/page-help.liquid`
- `sections/page-partners.liquid`
- `sections/page-returns.liquid`
- `sections/page-shipping.liquid`
- `sections/page-size-guide.liquid`
- `sections/page-studio-program.liquid`
- `sections/page-technology.liquid`
- `sections/page-warranty.liquid`
- `sections/page-wholesale.liquid`
- `sections/pdp-reviews.liquid`
- `sections/pdp-sock-math.liquid`
- `sections/press-cards.liquid`
- `sections/press-feature.liquid`
- `sections/press-row.liquid`
- `sections/problem-section.liquid`
- `sections/proof-numbers.liquid`
- `sections/sale-banner.liquid`
- `sections/social-proof.liquid`
- `sections/split-hero.liquid`
- `sections/statement-band.liquid`
- `sections/studio-trust.liquid`
- `sections/value-strip.liquid`
- `sections/variant-grid.liquid`
- `sections/visual-mosaic.liquid`

**Placed instances scanned:** 211
**Desktop computed inset diffs (old vs new):** 0
**Phone computed inset diffs (old vs new):** 0

**Zero phone diffs** across all placed instances in git — shared snippet change does not alter computed inset CSS for any committed template/group JSON.

_Note: If a merchant sets non-zero desktop inset with `inset_custom_mobile` off only in Theme Editor (not in git), phone rendering would change under the new snippet; no such saves exist in this repo._

## All instances (desktop + phone computed vars)

| source:section | type | custom_m | desktop (old=new) | phone old | phone new | phone diff |
|---|---|---:|---|---|---|---|
| `templates/article:article-shop-banner` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:value-strip` | value-strip | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:fullbleed-workout` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:fifty-fifty-tees` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:reviews` | pdp-reviews | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:fifty-fifty-think-outside` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.apparel:fifty-fifty-leggings` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.closed-sole:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.closed-sole:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.gift-cards:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.hot-kits:fifty-fifty-kit-idea` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.hot-kits:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:fifty-fifty-disciplines` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:variant-grid` | variant-grid | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:pdp-sock-math` | pdp-sock-math | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:fullbleed-commit` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:fifty-fifty-grip` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:in-use-mosaic` | visual-mosaic | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:knock-socks` | statement-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:home-juicer` | home-juicer | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:upgrade-grip` | disciplines | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection:fullbleed-studio` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.limited-editions:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.limited-editions:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.new-arrivals:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.new-arrivals:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.one-offs:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.one-offs:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.open-sole:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.open-sole:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.outdoor:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.outdoor:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.sale:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/collection.sale:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:split_hero` | split-hero | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:visual-mosaic` | visual-mosaic | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:problem-section` | problem-section | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:variant-grid` | variant-grid | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:fifty-fifty-grip` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:fifty-fifty-one-pair` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:proof-numbers` | proof-numbers | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:press-feature-interni` | press-feature | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:statement-band` | statement-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:fullbleed-statement` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:disciplines` | disciplines | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:press-home` | press-cards | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:press-row` | press-row | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:home-juicer` | home-juicer | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:guarantee-band` | guarantee-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/index:collab-hero` | collab-hero | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-hero` | page-about-hero | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-intro` | page-about-intro | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-founder` | page-about-split | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-prototype` | page-about-split | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-values` | page-about-values | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-joseph` | page-about-joseph | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-facts` | page-about-facts | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-letter` | page-about-split | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.about:about-close` | page-about-close | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.ambassador:ambassador-content` | page-ambassador | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:seo-hero` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:variant-grid` | variant-grid | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:value-strip` | value-strip | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:pdp-sock-math` | pdp-sock-math | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:outgrew` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:never-loses` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:upgrade` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.best-grippy-socks:home-juicer` | home-juicer | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.collaborations:collab-hub` | page-help | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.compare-open-vs-closed:compare-content` | page-compare | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.compare:compare-content` | page-compare | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.contact-us-form:contact-form` | page-contact | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.contact:contact-form` | page-contact | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.faq:faq-content` | page-faq | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.faq:contact-cta` | contact-cta | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.free-people:fp-teaser` | collab-teaser | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.free-people:fp-video` | collab-hero | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.free-people:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.grip-comparison:grip-comparison` | page-grip-comparison | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.help:page-returns` | page-returns | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page:main` | main-page | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.judgeme_all_reviews:page-content` | main-page | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.judgeme_all_reviews:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-hero` | page-about-hero | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-intro` | page-about-intro | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-founder` | page-about-split | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-prototype` | page-about-split | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-values` | page-about-values | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-joseph` | page-about-joseph | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-facts` | page-about-facts | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-letter` | page-about-split | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.our-story:about-close` | page-about-close | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.partners:partners-portal` | page-wholesale | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.performance-skins-size-chart:size-guide` | page-size-guide | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.press:press-row` | press-row | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.returns-portal:page-content` | main-page | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.returns:page-returns` | page-returns | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.reviews:page-content` | main-page | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.reviews:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.shipping-retruns:page-returns` | page-returns | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.shipping:shipping-content` | page-shipping | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.size-chart:size-guide` | page-size-guide | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.size-guide:size-guide` | page-size-guide | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.start-a-retrun:page-content` | main-page | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.studio-program:studio-portal` | page-wholesale | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.technology:tech-content` | page-technology | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.warranty:warranty-content` | page-warranty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/page.wholesale:wholesale-content` | page-wholesale | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:coperni-crosslink` | coperni-crosslink | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:coperni-pdp-story` | coperni-pdp-story | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:disciplines` | disciplines | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:fifty-fifty-sock-era` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:variant-grid` | variant-grid | True | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:fullbleed-lifestyle` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:guarantee-band` | guarantee-band | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.coperni:home-juicer` | home-juicer | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:value-strip` | value-strip | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fifty-fifty-sock-era` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:variant-grid` | variant-grid | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fullbleed-statement` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:pdp-sock-math` | pdp-sock-math | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fullbleed-lifestyle` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:knock-socks` | statement-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fifty-fifty-numbers` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:guarantee-band` | guarantee-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:home-juicer` | home-juicer | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.in-studio-template:fifty-fifty-tired-socks` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:disciplines` | disciplines | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:fifty-fifty-sock-era` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:fullbleed-statement` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:pdp-sock-math` | pdp-sock-math | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:fullbleed-lifestyle` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:fifty-fifty-numbers` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:guarantee-band` | guarantee-band | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:home-juicer` | home-juicer | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:fifty-fifty-numbers` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:guarantee-band` | guarantee-band | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:home-juicer` | home-juicer | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-closed:fullbleed-lifestyle` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:fifty-fifty-numbers` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:guarantee-band` | guarantee-band | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:home-juicer` | home-juicer | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.one-off-open:fullbleed-lifestyle` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:value-strip` | value-strip | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fifty-fifty-sock-era` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:variant-grid` | variant-grid | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fullbleed-statement` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:pdp-sock-math` | pdp-sock-math | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fullbleed-lifestyle` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:knock-socks` | statement-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fifty-fifty-numbers` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:guarantee-band` | guarantee-band | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:home-juicer` | home-juicer | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.open-sole:fifty-fifty-tired-socks` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:disciplines` | disciplines | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:fifty-fifty-lifestyle` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:fullbleed-statement` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:fifty-fifty-commit` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:fifty-fifty-numbers` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:guarantee-band` | guarantee-band | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:home-juicer` | home-juicer | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:fifty-fifty-barefoot` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.outdoor:fifty-fifty-outdoor-works` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:value-strip` | value-strip | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:fifty-fifty-tees` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:variant-grid` | variant-grid | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:fifty-fifty-leggings` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:fullbleed-workout` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:reviews` | pdp-reviews | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:press_feature_m9tTbA` | press-feature | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.v-neck-tops:page_about_facts_EziCVR` | page-about-facts | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:value-strip` | value-strip | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:fifty-fifty-leggings` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:variant-grid` | variant-grid | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:fifty-fifty-tees` | fifty-fifty | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:fullbleed-workout` | fullbleed-statement | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:reviews` | pdp-reviews | False | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:press_feature_m9tTbA` | press-feature | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `templates/product.yoga-pants:page_about_facts_EziCVR` | page-about-facts | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
| `sections/header-group:sale_banner` | sale-banner | None | (0, 0, 0, 0) | (0, 0, 0, 0) | (0, 0, 0, 0) | no |
