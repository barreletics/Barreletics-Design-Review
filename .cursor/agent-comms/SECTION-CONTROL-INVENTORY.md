# Section control inventory (Theme Editor) — read-only

**Author:** Grok Bot · **Date:** 2026-10-02 · **Branch:** `grok/section-control-inventory` (from `grok/section-live-preview-inventory` @ `3429d89`)
**Strictly read-only:** no theme files, templates, settings or schema changed; nothing pushed to Shopify; live theme `185687998755` and draft `187144929571` untouched. PR #31 left as draft.

## Sources
- **Schema / code:** `shopify-build/sections/*.liquid` at `c0c0564`; `fifty-fifty.liquid` taken from `grok/fifty-fifty-live-preview` (`dc96103`, PR #31, tested working by Andrew).
- **"Used" column = GIT FALLBACK, not a live pull of the draft.** Draft `187144929571` could not be read: Shopify CLI on the box has no logged-in session (device-login prompt), and the repo's read-only Admin API script (`scripts/shopify-admin-gql.sh`, client-credentials app) lacks the `read_themes` scope. Values come from `shopify-build/templates/*.json` + `sections/*-group.json` at commit **`c0c0564`** ("Save Press IA, apparel PDPs, and TE live-preview hooks", 2026-10-02 16:53 ET) — the newest template sync on any branch (earlier syncs were `theme pull` from the draft per `planning/m4-section-freeze.md`). Any TE edits made in the draft after that commit are not reflected. `config/settings_data.json` is global theme settings (not section settings) and was not needed.
- **Live in TE** (rule from the live-preview inventory): `yes ({% style %})` = setting read directly in a `{% style %}` block → live-patched; `yes (content re-render)` = text/media/link content; `Save-only` = drives inline `style=`, `<style>` with assigns, class/`{% if %}` toggles; `Save-only (snippet)` = only read via `section-inset-vars` / `type-override-vars` etc.; `n/a (unused in code)` = never read by Liquid (dead control).
- **Non-default** = key present in a template instance with a value different from the schema default. Format `template:sectionKey=value`; counts are `non-default/instances`.
- **Recommendation rules:** dead control → remove; content → keep; visual control set non-default anywhere → keep; visual control at default in every instance → remove (hardcode default). A control in use with a non-default value is never "remove" without a migration note. Nothing here reverts any setting. Locked sections (`pdp-buy-box`, `footer`, `home-juicer`, `proof-numbers`, `value-strip`) are listed for completeness only — do not touch unless Andrew names them.
- **Caveat:** fifty-fifty was reviewed line-by-line. Other sections use the mechanical rules above; settings that are read in Liquid but neutralised by a global lock or a hardcoded `!important` (e.g. heading size/weight after the 2026-09-27 heading lock) may show as `keep`/`Save-only` — re-check each section by hand in its cleanup PR. Low-instance sections (e.g. split-hero, 1 instance) score many removals simply because one instance rarely changes everything.

## Summary
- **60 sections**, **1222 controls** (1090 section settings + 132 block settings; header/paragraph labels excluded).
- Recommendation totals: **keep 747 · remove 471 · merge 4**.
- Live in TE: live via `{% style %}` **35** · content re-render **579** · Save-only **572** · dead (unused in code) **36**.
- Controls set non-default in at least one template: **470**.
- Sections placed in no template/group (whole-section removal candidates): `recently-viewed`, `sole-cards`, `studio-trust`.

### Most removable controls (unlocked, placed sections)
| Section | Controls | Remove | Merge | Keep | Dead in code | Instances |
|---|---|---|---|---|---|---|
| `split-hero` | 57 | 39 | 0 | 18 | 3 | 1 |
| `fifty-fifty` | 76 | 32 | 4 | 40 | 2 | 42 |
| `visual-mosaic` | 50 | 25 | 0 | 25 | 1 | 2 |
| `collab-hero` | 51 | 18 | 0 | 33 | 1 | 2 |
| `problem-section` | 31 | 17 | 0 | 14 | 0 | 1 |
| `statement-band` | 27 | 17 | 0 | 10 | 4 | 4 |
| `variant-grid` | 43 | 16 | 0 | 27 | 1 | 22 |
| `disciplines` | 22 | 15 | 0 | 7 | 4 | 5 |
| `fullbleed-statement` | 43 | 15 | 0 | 28 | 3 | 19 |
| `header` | 21 | 12 | 0 | 9 | 0 | 1 |
| `main-page` | 17 | 12 | 0 | 5 | 1 | 5 |
| `pdp-reviews` | 43 | 12 | 0 | 31 | 1 | 15 |
| `press-feature` | 30 | 12 | 0 | 18 | 0 | 3 |
| `guarantee-band` | 25 | 11 | 0 | 14 | 2 | 8 |
| `page-about-facts` | 18 | 11 | 0 | 7 | 0 | 4 |

### Proposed cleanup order (one section per PR)
Each PR: schema removal + dead-Liquid removal for that one section only, hardcode the default where a control is removed, pull-verify templates first, no JSON/value edits except the noted migrations (which are no-visual-change). Order = fifty-fifty first (Andrew flagged it), then most removable controls, locked sections excluded, unused sections last.
1. `fifty-fifty` — remove 32, merge 4
2. `split-hero` — remove 39, merge 0
3. `visual-mosaic` — remove 25, merge 0
4. `collab-hero` — remove 18, merge 0
5. `problem-section` — remove 17, merge 0
6. `statement-band` — remove 17, merge 0
7. `variant-grid` — remove 16, merge 0
8. `disciplines` — remove 15, merge 0
9. `fullbleed-statement` — remove 15, merge 0
10. `header` — remove 12, merge 0
11. `main-page` — remove 12, merge 0
12. `pdp-reviews` — remove 12, merge 0
13. `press-feature` — remove 12, merge 0
14. `guarantee-band` — remove 11, merge 0
15. `page-about-facts` — remove 11, merge 0
16. `announcement-strip` — remove 10, merge 0
17. `page-faq` — remove 9, merge 0
18. `press-row` — remove 9, merge 0
19. `pdp-features` — remove 8, merge 0
20. `press-cards` — remove 8, merge 0
21. `collection-hero` — remove 7, merge 0
22. `coperni-crosslink` — remove 7, merge 0
23. `sale-banner` — remove 7, merge 0
24. `blog-listing` — remove 6, merge 0
25. `collab-teaser` — remove 6, merge 0
26. `coperni-pdp-story` — remove 6, merge 0
27. `page-about-intro` — remove 6, merge 0
28. `page-about-values` — remove 6, merge 0
29. `page-help` — remove 6, merge 0
30. `page-about-joseph` — remove 5, merge 0
31. `page-about-split` — remove 5, merge 0
32. `page-size-guide` — remove 5, merge 0
33. `pdp-sock-math` — remove 5, merge 0
34. `page-about-close` — remove 4, merge 0
35. `page-contact` — remove 4, merge 0
36. `page-returns` — remove 4, merge 0
37. `pdp-sticky-atc` — remove 2, merge 0
38. `article-content` — remove 1, merge 0
39. `page-compare` — remove 1, merge 0
40. `recommendations` — remove 1, merge 0
41. Unused sections (delete file each in its own PR after confirming not in the draft): `recently-viewed`, `sole-cards`, `studio-trust`
- Excluded (locked): `footer`, `home-juicer`, `pdp-buy-box`, `proof-numbers`, `value-strip`.

## fifty-fifty — extra care (42 instances in 15 templates)
Key findings: the 2026-09-27 global heading lock left **heading_register, body_size dead**, and title_size/title_weight/heading_size_override only affect quote text or nothing. The **stats** mode (stat_* fallbacks, stat_bar_color, `stat` block) is used by **0** instances; "statement" content_style is a no-op. Presets duplicated by colour pickers (bg_preset, media_bg_preset) and position presets duplicated by focal sliders (image_position) are merge/remove candidates. All in-use values stay as they are; removals listed are either never changed or currently have no visual effect.

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `video` | video | — | yes (content re-render) | **1/42** collection:fifty-fifty-disciplines=shopify://files/videos/Adobe_Spark_Vid… (disabled) | **keep** | content; 1 instance uses Shopify video |
| `video_url` | text | — | yes (content re-render) | **13/42** collection.apparel:fifty-fifty-think-outsid=https://barreletics.com/cdn/shop/video…; index:fifty-fifty-grip=https://cdn.shopify.com/s/files/1/0045…; product.coperni:fifty-fifty-sock-era=https://cdn.shopify.com/s/files/1/0045… +10 more · values: https://barreletics.com/cdn/shop/video…×7, https://cdn.shopify.com/s/files/1/0045…×3, https://cdn.shopify.com/videos/c/o/v/c…×2, https://cdn.shopify.com/videos/c/o/v/d…×1 | **keep** | content; 13 instances |
| `image` | image_picker | — | yes (content re-render) | **8/42** collection:fifty-fifty-disciplines=shopify://shop_images/Copy_of_barrelet… (disabled); collection:fifty-fifty-grip=shopify://shop_images/IMG_2704.jpg; index:fifty-fifty-one-pair=shopify://shop_images/Lindsay_Chat.png +5 more · values: shopify://shop_images/View_recent_phot…×2, shopify://shop_images/P5A4949.jpg×2, shopify://shop_images/Copy_of_barrelet…×1, shopify://shop_images/IMG_2704.jpg×1 | **keep** | content; 8 instances |
| `poster_url` | text | — | yes (content re-render) | **8/42** collection.apparel:fifty-fifty-think-outsid=https://barreletics.com/cdn/shop/produ…; collection:fifty-fifty-grip=https://barreletics.com/cdn/shop/files…; index:fifty-fifty-grip=https://barreletics.com/cdn/shop/produ… +5 more · values: https://barreletics.com/cdn/shop/produ…×7, https://barreletics.com/cdn/shop/files…×1 | **keep** | content; 8 instances (video posters) |
| `image_asset` | text | — | yes (content re-render) | **3/42** product.outdoor:fifty-fifty-commit=outdoor-dock-adventures.jpg; product.outdoor:fifty-fifty-numbers=outdoor-water-50-50-blue.jpg; product.outdoor:fifty-fifty-barefoot=outdoor-paddle-caribbean.jpg | **merge** | → image_url (3 product.outdoor instances use theme-asset filenames; migrate to CDN URL first) |
| `image_url` | text | — | yes (content re-render) | **33/42** collection.apparel:fifty-fifty-tees=https://cdn.shopify.com/s/files/1/0045…; collection.apparel:fifty-fifty-think-outsid=https://barreletics.com/cdn/shop/produ…; collection.apparel:fifty-fifty-leggings=https://cdn.shopify.com/s/files/1/0045… +30 more · values: https://barreletics.com/cdn/shop/produ…×14, https://cdn.shopify.com/s/files/1/0045…×12, https://barreletics.com/cdn/shop/files…×5, https://www.juicer.io/api/media/598642…×1 | **keep** | primary media source in 33/42 |
| `image_alt` | text | — | yes (content re-render) | **30/42** collection.apparel:fifty-fifty-tees=Barreletics performance fabric tee; collection.apparel:fifty-fifty-think-outsid=Barreletics Performance Skins in studio; collection.apparel:fifty-fifty-leggings=Barreletics super-high rise reinforced… +27 more · values: Open Sole coral on foot×4, Barreletics performance fabric tee×3, Barreletics super-high rise reinforced…×3, Open Sole blue on foot×2 | **keep** | a11y; 30 instances |
| `image_mobile` | image_picker | — | yes (content re-render) | **8/42** collection.apparel:fifty-fifty-leggings=shopify://shop_images/phone-apparel-su…; page.best-grippy-socks:outgrew=shopify://shop_images/phone-multi-imag…; product.in-studio-template:fifty-fifty-sock-era=shopify://shop_images/te-pick-ig-studi… +5 more · values: shopify://shop_images/phone-apparel-su…×3, shopify://shop_images/te-pick-ig-studi…×2, shopify://shop_images/phone-open-sole-…×2, shopify://shop_images/phone-multi-imag…×1 | **keep** | 8 instances use a phone crop |
| `media_fit` | select | cover | Save-only | **1/42** page.best-grippy-socks:outgrew=fit | **keep** | 1 instance (best-grippy-socks/outgrew = fit); schema note says cover is the standard — consider merging with image_fit_mobile later |
| `image_fit_mobile` | select | cover | Save-only | **1/42** product.coperni:fifty-fifty-lifestyle=fit | **merge** | → media_fit with a "phone only" option; 1 instance (coperni/lifestyle = fit) — migrate that value |
| `image_position` | select | center | yes ({% style %}) | **11/42** product.coperni:fifty-fifty-lifestyle=custom; product:fifty-fifty-lifestyle=custom; product.one-off-closed:fifty-fifty-lifestyle=custom +8 more · values: custom×11 | **merge** | → focal_x/focal_y only: every non-default use (11) is "custom"; presets unused. Migration: keep custom behaviour as the only mode |
| `focal_x` | range | 50 | yes ({% style %}) | **2/42** index:fifty-fifty-one-pair=100; product.outdoor:fifty-fifty-commit=38 | **keep** | live; 2 instances |
| `focal_y` | range | 50 | yes ({% style %}) | **10/42** product.coperni:fifty-fifty-commit=40; product.in-studio-template:fifty-fifty-lifestyle=72; product:fifty-fifty-lifestyle=85 +7 more · values: 85×5, 40×2, 72×2, 78×1 | **keep** | live; 10 instances |
| `image_scale` | range | 100 | yes ({% style %}) | default (42) | **remove** | never changed (schema says scale 100 standard); live but unused |
| `contain_width` | range | 72 | yes ({% style %}) | default (42) | **remove** | never changed; only applies to contain fit, which no instance uses |
| `media_bg_preset` | select | custom | yes ({% style %}) | default (42) | **remove** | never changed; media_bg colour covers it (21 uses) |
| `media_bg` | color | #ffffff | yes ({% style %}) | **21/42** collection.apparel:fifty-fifty-think-outsid=#faf8f6; collection.apparel:fifty-fifty-leggings=#faf8f6; collection:fifty-fifty-disciplines=#faf8f6 (disabled) +18 more · values: #faf8f6×6, #f9f9f9×5, #efe9dd×4, #3a7eb8×2 | **keep** | 21 instances (letterbox colour) |
| `min_height` | range | 560 | yes ({% style %}) | **4/42** index:fifty-fifty-grip=620; index:fifty-fifty-one-pair=620; page.best-grippy-socks:outgrew=640 +1 more · values: 620×2, 640×2 | **keep** | live; 4 instances (620/640) |
| `media_column_pct` | range | 50 | yes ({% style %}) | **1/42** index:fifty-fifty-one-pair=54 | **keep** | live; 1 instance (index/one-pair = 54) |
| `mobile_media_height` | range | 0 | yes ({% style %}) | **3/42** product.coperni:fifty-fifty-lifestyle=400; product.in-studio-template:fifty-fifty-lifestyle=360; product.open-sole:fifty-fifty-lifestyle=360 | **keep** | live; 3 lifestyle instances |
| `mobile_text_height` | range | 0 | yes ({% style %}) | default (42) | **remove** | never changed; forced 0 on all product templates anyway |
| `text_pad_top_mobile` | range | 96 | yes ({% style %}) | **10/42** index:fifty-fifty-grip=32; index:fifty-fifty-one-pair=32; product.in-studio-template:fifty-fifty-sock-era=32 +7 more · values: 32×10 | **keep** | live; 10 instances = 32 (note: schema info says "LOCKED PDP standard 96" but 8 PDP instances use 32) |
| `text_pad_bottom_mobile` | range | 96 | yes ({% style %}) | **2/42** index:fifty-fifty-grip=32; index:fifty-fifty-one-pair=32 | **merge** | → text_pad_top_mobile as one "Text pad — phone" (bottom already defaults to top). Migration: only index grip/one-pair set it, both equal to top (32) |
| `media_aspect` | select | stretch | Save-only | **1/42** index:fifty-fifty-grip=square | **keep** | 1 instance (index/grip = square) |
| `media_aspect_mobile` | select | stretch | Save-only | default (42) | **remove** | never changed; Save-only |
| `content_style` | select | standard | Save-only | **2/42** product:fifty-fifty-lifestyle=quote; product.outdoor:fifty-fifty-lifestyle=quote | **keep** | 2 instances use quote (product, product.outdoor lifestyle); trim options: "statement" is a no-op since global heading lock, "stats" unused |
| `eyebrow` | text | — | yes (content re-render) | **13/42** collection.apparel:fifty-fifty-tees=Made in the USA; collection.apparel:fifty-fifty-think-outsid=Trusted by 1,000's of Athletes; collection.apparel:fifty-fifty-leggings=Made in the USA +10 more · values: Made in the USA×6, One-Off colors×2, Trusted by 1,000's of Athletes×1, The idea×1 | **keep** | content; 13 instances |
| `heading_register` | select | display | n/a (unused in code) | default (42) | **remove** | dead: ignored since global heading system 2026-09-27 |
| `title` | textarea | Never loses shape. Never loses grip. | yes (content re-render) | **41/42** collection.apparel:fifty-fifty-tees=Performance Fabric V-Neck & Tank Top T…; collection.apparel:fifty-fifty-think-outsid=Think Outside the Sock; collection.apparel:fifty-fifty-leggings=Super-High Rise Reinforced Knee Yoga T… +38 more · values: Performance Fabric V-Neck & Tank Top T…×3, Super-High Rise Reinforced Knee Yoga T…×3, The Pilates sock era is over.×3, Studio workouts will never be the same.×2 | **keep** | content |
| `heading_size_override` | number | — | Save-only | default (42) | **remove** | never set; contradicts global locked heading; Save-only |
| `heading_level` | select | h2 | Save-only | default (42) | **keep** | SEO/semantics; cheap |
| `title_size` | select | default | Save-only | default (42) | **remove** | never set; now only sizes quote text (heading is locked) |
| `title_weight` | select | 400 | Save-only | **2/42** index:fifty-fifty-grip=default; index:fifty-fifty-one-pair=default | **remove** | 2 instances (index grip/one-pair) hold "default", which renders identically to schema default 400 → no visual change. Migration: none needed |
| `body` | textarea | Built to hold when it matters most—so … | yes (content re-render) | **41/42** collection.apparel:fifty-fifty-tees=Softness, versatility, and comfort: li…; collection.apparel:fifty-fifty-think-outsid=The ultimate grip shoe, a smarter alte…; collection.apparel:fifty-fifty-leggings=Italian 4-way stretch compression with… +38 more · values: One pair. Every class. No replacements…×4, ×4, Softness, versatility, and comfort: li…×3, Italian 4-way stretch compression with…×3 | **keep** | content |
| `body_size` | select | default | n/a (unused in code) | **42/42** collection.apparel:fifty-fifty-tees=17; collection.apparel:fifty-fifty-think-outsid=17; collection.apparel:fifty-fifty-leggings=17 +39 more · values: 17×40, 16×2 | **remove** | dead: body locked at 17px. Migration note: all 42 instances store a value (40×17, index grip/one-pair = 16) but it has no effect today; removing changes nothing visually |
| `body_weight` | select | default | Save-only | default (42) | **remove** | never set; Save-only |
| `cta_text` | text | Shop Now | yes (content re-render) | **35/42** collection.apparel:fifty-fifty-think-outsid=Shop Grippy Shoes; collection.hot-kits:fifty-fifty-kit-idea=Shop Grippy Shoes; page.best-grippy-socks:outgrew=Shop the Performance Skin +32 more · values: Shop now×20, Shop Grippy Shoes×2, Read all reviews →×2, Read all reviews×2 | **keep** | content |
| `cta_size` | select | default | Save-only | default (42) | **remove** | never set; Save-only |
| `cta_style` | select | solid | Save-only | default (42) | **remove** | never set (all solid); Save-only |
| `cta_bg_color` | color | #c45c3f | yes ({% style %}) | default (42) | **remove** | never set; live but always brand rust — hardcode |
| `cta_border_color` | color | #c45c3f | yes ({% style %}) | default (42) | **remove** | never set; hardcode (defaults to bg) |
| `cta_text_color` | color | #ffffff | yes ({% style %}) | default (42) | **remove** | never set; hardcode |
| `cta_link_target` | select | custom | Save-only | **32/42** index:fifty-fifty-grip=#variants; index:fifty-fifty-one-pair=#variants; product.coperni:fifty-fifty-sock-era=#variants +29 more · values: #variants×14, #buy×12, #reviews×4, #shop×2 | **keep** | 32 instances (#variants/#buy/#reviews/#shop) |
| `cta_url` | text | — | yes (content re-render) | **10/42** collection.apparel:fifty-fifty-tees=/products/barreletics-performance-fabr…; collection.apparel:fifty-fifty-think-outsid=/collections/barre-pilates-yoga-shoe-s…; collection.apparel:fifty-fifty-leggings=/products/lightly-padded-knee-yoga-pan… +7 more · values: #grid×4, /products/barreletics-performance-fabr…×2, /collections/barre-pilates-yoga-shoe-s…×2, /products/lightly-padded-knee-yoga-pan…×2 | **keep** | 10 instances |
| `show_trust_strip` | checkbox | false | Save-only | **10/42** product.in-studio-template:fifty-fifty-sock-era=true; product.in-studio-template:fifty-fifty-lifestyle=true; product.in-studio-template:fifty-fifty-commit=true +7 more · values: true×10 | **keep** | 10 instances on |
| `trust_text` | text | — | yes (content re-render) | **9/42** product.coperni:fifty-fifty-lifestyle=Trusted by 1,000+ Instructors; product.in-studio-template:fifty-fifty-lifestyle=Trusted by 1,000s of Practitioners; product.in-studio-template:fifty-fifty-commit=Studio trusted +6 more · values: Trusted by 1,000s×4, Trusted by 1,000s of Practitioners×2, Studio trusted×2, Trusted by 1,000+ Instructors×1 | **keep** | 9 instances |
| `show_quote_stars` | checkbox | true | Save-only | **12/42** collection:fifty-fifty-disciplines=false (disabled); collection:fifty-fifty-grip=false; page.best-grippy-socks:outgrew=false +9 more · values: false×12 | **keep** | only matters for content_style=quote (2 instances, both at default=on). Note: 12 non-quote instances store false = no effect |
| `quote_italic` | checkbox | true | yes ({% style %}) | default (42) | **remove** | never changed; live |
| `quote_author` | text | — | yes (content re-render) | **2/42** product:fifty-fifty-lifestyle=Kimberly; product.outdoor:fifty-fifty-lifestyle=Denise | **keep** | 2 quote instances |
| `quote_author_case` | select | uppercase | Save-only | default (42) | **remove** | never changed; Save-only |
| `quote_meta` | text | — | yes (content re-render) | **2/42** product:fifty-fifty-lifestyle=Knoxville, US · 4-year customer; product.outdoor:fifty-fifty-lifestyle=San Antonio, US · Grippy Water Shoes | **keep** | 2 quote instances |
| `stat_bar_color` | color | #c45c3f | yes ({% style %}) | default (42) | **remove** | "stats" content_style used by 0 instances |
| `stat_1_value` | text | — | yes (content re-render) | default (42) | **remove** | stats mode unused (0 instances) |
| `stat_1_label` | text | — | yes (content re-render) | default (42) | **remove** | stats mode unused |
| `stat_2_value` | text | — | yes (content re-render) | default (42) | **remove** | stats mode unused |
| `stat_2_label` | text | — | yes (content re-render) | default (42) | **remove** | stats mode unused |
| `stat_3_value` | text | — | yes (content re-render) | default (42) | **remove** | stats mode unused |
| `stat_3_label` | text | — | yes (content re-render) | default (42) | **remove** | stats mode unused |
| `stat_3_emphasis` | checkbox | true | Save-only | **3/42** product:fifty-fifty-numbers=false; product.one-off-closed:fifty-fifty-numbers=false; product.one-off-open:fifty-fifty-numbers=false | **remove** | stats mode unused; 3 "numbers" instances store false but render no stats → no effect |
| `reverse` | checkbox | false | Save-only | **15/42** collection.apparel:fifty-fifty-tees=true; index:fifty-fifty-grip=true; page.best-grippy-socks:upgrade=true +12 more · values: true×15 | **keep** | 15 instances |
| `mobile_stack_order` | select | media_first | Save-only | **7/42** collection.apparel:fifty-fifty-tees=copy_first; collection.apparel:fifty-fifty-think-outsid=copy_first; collection.apparel:fifty-fifty-leggings=copy_first +4 more · values: copy_first×7 | **keep** | 7 instances copy_first |
| `column_gap` | range | 0 | yes ({% style %}) | **2/42** product.coperni:fifty-fifty-sock-era=64; product.coperni:fifty-fifty-lifestyle=56 | **keep** | live; 2 coperni instances |
| `side_padding` | range | 64 | yes ({% style %}) | default (42) | **remove** | never changed; hardcode 64 |
| `vertical_padding` | range | 88 | yes ({% style %}) | **28/42** product.coperni:fifty-fifty-sock-era=80; product.coperni:fifty-fifty-lifestyle=80; product.coperni:fifty-fifty-commit=80 +25 more · values: 80×28 | **keep** | live; 28 instances = 80 (consider changing default to 80 in a later PR) |
| `media_radius` | range | 0 | yes ({% style %}) | default (42) | **remove** | never changed; brand is square corners |
| `bg_preset` | select | custom | yes ({% style %}) | default (42) | **remove** | never changed; bg_color covers it (29 uses) |
| `bg_color` | color | #ffffff | yes ({% style %}) | **29/42** collection.apparel:fifty-fifty-tees=#faf8f6; collection.apparel:fifty-fifty-think-outsid=#faf8f6; collection.apparel:fifty-fifty-leggings=#faf8f6 +26 more · values: #faf8f6×29 | **keep** | 29 instances (#faf8f6) |
| `anchor_id` | text | — | yes (content re-render) | **7/42** collection:fifty-fifty-disciplines=upgrade-grip (disabled); index:fifty-fifty-grip=never-loses-grip; index:fifty-fifty-one-pair=one-pair +4 more · values: tired-of-slipping×2, upgrade-grip×1, never-loses-grip×1, one-pair×1 | **keep** | 7 instances (in-page links) |
| `aria_label` | text | — | yes (content re-render) | **5/42** collection:fifty-fifty-disciplines=Upgrade your grip (disabled); page.best-grippy-socks:outgrew=We outgrew grip socks; page.best-grippy-socks:upgrade=Upgrade your grip +2 more · values: Upgrade your grip×2, Tired of slipping in your yoga socks?×2, We outgrew grip socks×1 | **keep** | a11y; 5 instances |
| `section_gap` | range | 32 | yes ({% style %}) | **3/42** product.coperni:fifty-fifty-sock-era=0; product.coperni:fifty-fifty-lifestyle=0; product.coperni:fifty-fifty-commit=0 | **keep** | live; 3 coperni instances = 0 |
| `section_gap_mobile` | range | 0 | yes ({% style %}) | **4/42** collection:fifty-fifty-disciplines=24 (disabled); collection:fifty-fifty-grip=24; page.best-grippy-socks:outgrew=24 +1 more · values: 24×4 | **keep** | live; 4 instances = 24 (ignored on product templates) |
| `hide_on_mobile` | checkbox | false | Save-only | default (42) | **keep** | generic visibility switch; unused but cheap (could drop) |
| `hide_on_desktop` | checkbox | false | Save-only | default (42) | **keep** | generic visibility switch; unused but cheap (could drop) |
| `stat.value` | text | 360° | yes (content re-render) | no instances | **remove** | stat block type: 0 blocks in any template |
| `stat.label` | text | grip surface | yes (content re-render) | no instances | **remove** | stat block: unused |
| `stat.emphasis` | checkbox | false | Save-only | no instances | **remove** | stat block: unused |

## All other sections (alphabetical)

### `announcement-strip` — "Announcement strip"
Instances: 1 in 1 file(s): sections/header-group · keep 5 / remove 10 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `enabled` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `font_size` | range | 12 | Save-only | **1/1** sections/header-group:announcement_strip=13 | **keep** | in use: non-default in 1/1 |
| `pad_y` | range | 5 | Save-only | **1/1** sections/header-group:announcement_strip=9 | **keep** | in use: non-default in 1/1 |
| `pad_x` | range | 56 | Save-only | **1/1** sections/header-group:announcement_strip=48 | **keep** | in use: non-default in 1/1 |
| `item_gap` | range | 12 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `announce_distribute` | select | center | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `letter_spacing` | range | 3 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `promo_weight` | select | 700 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `max_width` | range | 1320 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `bg_color` | color | #faf8f6 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `text_color` | color | #5a544c | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `promo_color` | color | #2e2a26 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `rotation_speed` | range | 4 | n/a (unused in code) | default (1) | **remove** | dead: not read by any Liquid |
| `message.text` | text | Free Shipping Over $150 | yes (content re-render) | **3/4** sections/header-group:announcement_strip=Buy 2 save 10% · Use SAVE2; sections/header-group:announcement_strip=🇺🇸 Made in USA; sections/header-group:announcement_strip=30 Day Returns | **keep** | content; set in 3/4 |
| `message.link_url` | url | — | yes (content re-render) | **1/4** sections/header-group:announcement_strip=/pages/returns | **keep** | content; set in 1/4 |

### `article-content` — "Article Content"
Instances: 1 in 1 file(s): article · keep 1 / remove 1 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `show_related` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `related_heading` | text | Keep Reading | yes (content re-render) | default (1) | **keep** | content |

### `blog-listing` — "Blog Listing"
Instances: 1 in 1 file(s): blog · keep 11 / remove 6 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | The journal | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | From the Studio | yes (content re-render) | default (1) | **keep** | content |
| `subtitle` | textarea | Studio care, founder notes, and pose-p… | yes (content re-render) | **1/1** blog:blog-listing=Studio care, founder notes, and pose-p… | **keep** | content; set in 1/1 |
| `show_topics` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `topics_all_label` | text | All | yes (content re-render) | default (1) | **keep** | content |
| `show_featured` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `featured_article` | article | — | yes (content re-render) | **1/1** blog:blog-listing=news/what-to-wear-to-barre-and-pilates… | **keep** | content; set in 1/1 |
| `featured_label` | text | Featured | yes (content re-render) | default (1) | **keep** | content |
| `show_read_time` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `featured_cta_label` | text | Read the guide | yes (content re-render) | default (1) | **keep** | content |
| `image_shape` | select | landscape | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `articles_per_page` | range | 9 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `empty_text` | text | No articles yet. Check back soon. | yes (content re-render) | default (1) | **keep** | content |
| `contain_handles` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `contain_backdrop` | color | #faf8f6 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `topic.label` | text | Care | yes (content re-render) | **4/5** blog:blog-listing=Founder; blog:blog-listing=Movement; blog:blog-listing=Story +1 more · values: Founder×1, Movement×1, Story×1, Wellness×1 | **keep** | content; set in 4/5 |
| `topic.tag` | text | Care | yes (content re-render) | **4/5** blog:blog-listing=Founder; blog:blog-listing=Movement; blog:blog-listing=Story +1 more · values: Founder×1, Movement×1, Story×1, Wellness×1 | **keep** | content; set in 4/5 |

### `collab-hero` — "Collab hero"
Instances: 2 in 2 file(s): index, page.free-people · keep 33 / remove 18 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Limited Edition × Paris 2026 | yes (content re-render) | **1/2** page.free-people:fp-video= | **keep** | content; set in 1/2 |
| `badge_text` | text | — | yes (content re-render) | **1/2** page.free-people:fp-video=Available at Free People | **keep** | content; set in 1/2 |
| `badge_bg_color` | color | #C4859B | Save-only | **1/2** index:collab-hero=#c4859b (disabled) | **keep** | in use: non-default in 1/2 |
| `title` | textarea | <strong>Barreletics × Coperni</strong>… | yes (content re-render) | **1/2** page.free-people:fp-video=<em>Barreletics</em> · Free People | **keep** | content; set in 1/2 |
| `title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body` | textarea | A Pilates shoe designed for comfort, g… | yes (content re-render) | **1/2** page.free-people:fp-video=Same grip. Same stability. Available e… | **keep** | content; set in 1/2 |
| `body_size` | select | default | Save-only | **1/2** index:collab-hero=16 (disabled) | **keep** | in use: non-default in 1/2 |
| `cta_text` | text | See the collaboration | yes (content re-render) | **1/2** page.free-people:fp-video= | **keep** | content; set in 1/2 |
| `cta_style` | select | solid | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `cta_bg_color` | color | #ffffff | Save-only | **1/2** page.free-people:fp-video=#1c1916 | **keep** | in use: non-default in 1/2 |
| `cta_border_color` | color | #ffffff | Save-only | **1/2** page.free-people:fp-video=#1c1916 | **keep** | in use: non-default in 1/2 |
| `cta_text_color` | color | #1c1916 | Save-only | **1/2** page.free-people:fp-video=#ffffff | **keep** | in use: non-default in 1/2 |
| `cta_link_target` | select | custom | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `cta_url` | text | https://barreletics.com/products/barre… | yes (content re-render) | **1/2** page.free-people:fp-video= | **keep** | content; set in 1/2 |
| `video` | video | — | yes (content re-render) | **1/2** index:collab-hero=shopify://files/videos/Coperni 3.mov (disabled) | **keep** | content; set in 1/2 |
| `video_url` | text | https://barreletics.com/cdn/shop/video… | yes (content re-render) | **1/2** page.free-people:fp-video=https://barreletics.com/cdn/shop/video… | **keep** | content; set in 1/2 |
| `image` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `poster_url` | text | https://barreletics.com/cdn/shop/files… | yes (content re-render) | **1/2** page.free-people:fp-video= | **keep** | content; set in 1/2 |
| `layout` | select | stage_grid | Save-only | **1/2** page.free-people:fp-video=editorial | **keep** | in use: non-default in 1/2 |
| `section_gap_top` | range | 0 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `section_gap_top_mobile` | range | 0 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `height_desktop` | select | 105 | Save-only | **1/2** page.free-people:fp-video=80 | **keep** | in use: non-default in 1/2 |
| `height_mobile` | select | 78 | Save-only | **1/2** page.free-people:fp-video=70 | **keep** | in use: non-default in 1/2 |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (2) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (2) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (2) | **keep** | visibility switch; never used but cheap |
| `tile_grid` | select | row | Save-only | **1/2** index:collab-hero=2x2 (disabled) | **keep** | in use: non-default in 1/2 |
| `tile_size` | range | 100 | Save-only | **1/2** index:collab-hero=80 (disabled) | **keep** | in use: non-default in 1/2 |
| `tile_fit` | select | contain | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `tile_focus` | select | center | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `tile_gap` | range | 0 | Save-only | **1/2** index:collab-hero=16 (disabled) | **keep** | in use: non-default in 1/2 |
| `media_radius` | range | 0 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `tile_radius` | range | 0 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `enabled` | checkbox | true | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `meta` | text | Closed Sole · Special Release · One Run | yes (content re-render) | **1/2** page.free-people:fp-video=#LetUsKnockYourSocksOff | **keep** | content; set in 1/2 |
| `anchor_id` | text | coperni | yes (content re-render) | **1/2** page.free-people:fp-video=free-people-film | **keep** | content; set in 1/2 |
| `aria_label` | text | Coperni x Barreletics Collaboration ca… | yes (content re-render) | **1/2** page.free-people:fp-video=Free People collaboration | **keep** | content; set in 1/2 |
| `tile.image` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `tile.image_url` | text | — | yes (content re-render) | **2/2** index:collab-hero=https://barreletics.com/cdn/shop/files… (disabled); index:collab-hero=https://barreletics.com/cdn/shop/files… (disabled) | **keep** | content; set in 2/2 |
| `tile.alt` | text | — | yes (content re-render) | **2/2** index:collab-hero=Barreletics × Coperni Closed Sole (disabled); index:collab-hero=Coperni runway detail (disabled) | **keep** | content; set in 2/2 |
| `tile.link` | url | — | yes (content re-render) | **2/2** index:collab-hero=https://barreletics.com/products/barre… (disabled); index:collab-hero=https://barreletics.com/products/barre… (disabled) | **keep** | content; set in 2/2 |
| `tile.tile_eyebrow` | text | — | yes (content re-render) | default (2) | **keep** | content |
| `tile.tile_title` | text | — | yes (content re-render) | default (2) | **keep** | content |
| `tile.tile_body` | textarea | — | yes (content re-render) | default (2) | **keep** | content |

### `collab-teaser` — "Collab teaser"
Instances: 1 in 1 file(s): page.free-people · keep 11 / remove 6 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `anchor_id` | text | collab-teaser | yes (content re-render) | **1/1** page.free-people:fp-teaser=free-people | **keep** | content; set in 1/1 |
| `aria_label` | text | Collaboration | yes (content re-render) | **1/1** page.free-people:fp-teaser=Free People × Barreletics | **keep** | content; set in 1/1 |
| `eyebrow` | text | In Collaboration with Free People | yes (content re-render) | default (1) | **keep** | content |
| `show_ornament` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `headline` | html | Something <em>wild</em> this way walks. | yes (content re-render) | default (1) | **keep** | content |
| `subhead` | text | Free People × Barreletics | yes (content re-render) | default (1) | **keep** | content |
| `badge_text` | text | — | yes (content re-render) | **1/1** page.free-people:fp-teaser=Only at Free People | **keep** | content; set in 1/1 |
| `badge_bg_color` | color | — | Save-only | **1/1** page.free-people:fp-teaser=#C4859B | **keep** | in use: non-default in 1/1 |
| `body` | textarea | Performance meets poetry. A footwear s… | yes (content re-render) | **1/1** page.free-people:fp-teaser=Performance meets poetry. A footwear s… | **keep** | content; set in 1/1 |
| `meta` | text | Spring 2026 · Stay wild | yes (content re-render) | default (1) | **keep** | content |
| `bg_color` | color | #FBF7F2 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `accent_color` | color | #C4859B | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `inset_top` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |

### `collection-faq` — "Collection FAQ"
Instances: 12 in 12 file(s): collection, collection.apparel, page.best-grippy-socks, product, product.coperni, product.in-studio-template, product.one-off-closed, product.one-off-open … · keep 5 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | Questions from the studio | yes (content re-render) | **1/12** product.coperni:collection-faq=Everything you need to know. | **keep** | content; set in 1/12 |
| `bg_class` | select | cream | Save-only | **4/12** collection.apparel:collection-faq=white; page.best-grippy-socks:collection-faq=white; product.v-neck-tops:collection-faq=white +1 more · values: white×4 | **keep** | in use: non-default in 4/12 |
| `use_studio_bank` | checkbox | false | Save-only | **6/12** product.coperni:collection-faq=true; product.in-studio-template:collection-faq=true; product:collection-faq=true +3 more · values: true×6 | **keep** | in use: non-default in 6/12 |
| `faq_item.question` | text | — | yes (content re-render) | **59/59** collection.apparel:collection-faq=How should I size the high-rise yoga p…; collection.apparel:collection-faq=Are the knees padded or reinforced?; collection.apparel:collection-faq=Will the tees and pants pill? +56 more · values: How should I size the high-rise yoga p…×3, Are the knees padded or reinforced?×3, Will the tees and pants pill?×3, What workouts are they built for?×3 | **keep** | content; set in 59/59 |
| `faq_item.answer` | richtext | — | yes (content re-render) | **59/59** collection.apparel:collection-faq=<p><strong>Size down.</strong> Super-h…; collection.apparel:collection-faq=<p><strong>Reinforced, not bulky pads.…; collection.apparel:collection-faq=<p><strong>No.</strong> Performance fa… +56 more · values: <p><strong>Size down.</strong> Super-h…×3, <p><strong>Reinforced, not bulky pads.…×3, <p><strong>No.</strong> Performance fa…×3, <p>Barre, mat Pilates, reformer, Class…×3 | **keep** | content; set in 59/59 |

### `collection-hero` — "Collection Hero"
Instances: 11 in 11 file(s): collection, collection.apparel, collection.closed-sole, collection.gift-cards, collection.hot-kits, collection.limited-editions, collection.new-arrivals, collection.one-offs … · keep 29 / remove 7 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `show_trust` | checkbox | true | Save-only | **1/11** collection.apparel:collection-hero=false | **keep** | in use: non-default in 1/11 |
| `trust_text` | text | Trusted by 1,000's of instructors & st… | yes (content re-render) | default (11) | **keep** | content |
| `eyebrow` | text | — | yes (content re-render) | **10/11** collection.apparel:collection-hero=Apparel; collection.closed-sole:collection-hero=Closed Sole; collection.gift-cards:collection-hero=Gift Cards +7 more · values: Apparel×1, Closed Sole×1, Gift Cards×1, Coming soon×1 | **keep** | content; set in 10/11 |
| `title` | text | Secure in Every Hold | yes (content re-render) | **10/11** collection.apparel:collection-hero=Performance Apparel Engineered to Move!; collection.closed-sole:collection-hero=; collection.gift-cards:collection-hero= +7 more · values: ×9, Performance Apparel Engineered to Move!×1 | **keep** | content; set in 10/11 |
| `body` | inline_richtext | No sliding. No resets. Pick Closed or … | yes (content re-render) | **11/11** collection.apparel:collection-hero=High-rise compression leggings and sof…; collection.closed-sole:collection-hero=Heel and foot fully covered. Closed So…; collection.gift-cards:collection-hero=Not sure which style or size? Let them… +8 more · values: High-rise compression leggings and sof…×1, Heel and foot fully covered. Closed So…×1, Not sure which style or size? Let them…×1, A sock made for Performance Skins with…×1 | **keep** | content; set in 11/11 |
| `cta_text` | text | Shop Now | yes (content re-render) | **1/11** collection.apparel:collection-hero= | **keep** | content; set in 1/11 |
| `cta_url` | text | #grid | yes (content re-render) | default (11) | **keep** | content |
| `secondary_cta_text` | text | See why → | yes (content re-render) | **2/11** collection.apparel:collection-hero=; collection:collection-hero= | **keep** | content; set in 2/11 |
| `secondary_cta_url` | text | #pose | yes (content re-render) | **1/11** collection:collection-hero=#no-socks | **keep** | content; set in 1/11 |
| `aria_label` | text | Collection hero | yes (content re-render) | default (11) | **keep** | content |
| `mobile_stack_order` | select | media_first | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `media_type` | select | image | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `media_column_pct` | range | 48 | Save-only | **1/11** collection:collection-hero=50 | **keep** | in use: non-default in 1/11 |
| `media_height` | range | 480 | Save-only | **1/11** collection:collection-hero=660 | **keep** | in use: non-default in 1/11 |
| `image_zoom` | range | 100 | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `media_fill` | select | inset | Save-only | **1/11** collection:collection-hero=bleed | **keep** | in use: non-default in 1/11 |
| `image` | image_picker | — | yes (content re-render) | **1/11** collection:collection-hero=shopify://shop_images/Screenshot_2026-… | **keep** | content; set in 1/11 |
| `image_url` | text | — | yes (content re-render) | **1/11** collection:collection-hero=https://barreletics.com/cdn/shop/produ… | **keep** | content; set in 1/11 |
| `image_alt` | text | — | yes (content re-render) | **1/11** collection:collection-hero=Barreletics Performance Skin — secure … | **keep** | content; set in 1/11 |
| `image_mobile` | image_picker | — | yes (content re-render) | **1/11** collection:collection-hero=shopify://shop_images/IMG_2917.jpg | **keep** | content; set in 1/11 |
| `aspect_ratio_mobile` | select | natural | Save-only | **1/11** collection:collection-hero=portrait | **keep** | in use: non-default in 1/11 |
| `image_fit_mobile` | select | cover | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `video_fit_mobile` | select | cover | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `text_height_mobile` | range | 0 | Save-only | **1/11** collection:collection-hero=510 | **keep** | in use: non-default in 1/11 |
| `text_spacing_mobile` | range | 36 | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `video` | video | — | yes (content re-render) | default (11) | **keep** | content |
| `video_url` | text | — | yes (content re-render) | default (11) | **keep** | content |
| `show_sole_cards` | checkbox | false | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `closed_image` | image_picker | — | yes (content re-render) | **1/11** collection:collection-hero=shopify://shop_images/Dusty_Rose.png | **keep** | content; set in 1/11 |
| `closed_url` | url | — | yes (content re-render) | default (11) | **keep** | content |
| `closed_best_for` | text | you want heel and foot fully covered. | yes (content re-render) | default (11) | **keep** | content |
| `closed_desc` | textarea | Heel and foot fully covered. 360° grip… | yes (content re-render) | **10/11** collection.apparel:collection-hero=; collection.closed-sole:collection-hero=; collection.gift-cards:collection-hero= +7 more · values: ×10 | **keep** | content; set in 10/11 |
| `open_image` | image_picker | — | yes (content re-render) | **1/11** collection:collection-hero=shopify://shop_images/Rvian_Green_Fina… | **keep** | content; set in 1/11 |
| `open_url` | url | — | yes (content re-render) | default (11) | **keep** | content |
| `open_best_for` | text | you want a more grounded, barefoot fee… | yes (content re-render) | default (11) | **keep** | content |
| `open_desc` | textarea | Heel exposed, mid-foot breathing hole.… | yes (content re-render) | **10/11** collection.apparel:collection-hero=; collection.closed-sole:collection-hero=; collection.gift-cards:collection-hero= +7 more · values: ×10 | **keep** | content; set in 10/11 |

### `contact-cta` — "Contact CTA"
Instances: 1 in 1 file(s): page.faq · keep 5 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Still have questions? | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | Get in touch. | yes (content re-render) | default (1) | **keep** | content |
| `body` | textarea | Can't find what you're looking for? Co… | yes (content re-render) | **1/1** page.faq:contact-cta=Sizing, orders, or claims? Contact us … | **keep** | content; set in 1/1 |
| `cta_text` | text | Contact Us | yes (content re-render) | default (1) | **keep** | content |
| `cta_url` | url | — | yes (content re-render) | default (1) | **keep** | content |

### `coperni-crosslink` — "Coperni crosslink"
Instances: 1 in 1 file(s): product.coperni · keep 16 / remove 7 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `anchor_id` | text | coperni | yes (content re-render) | default (1) | **keep** | content |
| `aria_label` | text | Barreletics × Coperni | yes (content re-render) | default (1) | **keep** | content |
| `eyebrow` | text | This style has a limited edition · 2026 | yes (content re-render) | default (1) | **keep** | content |
| `title` | html | Barreletics<br>&times; Coperni | yes (content re-render) | default (1) | **keep** | content |
| `body` | textarea | The Closed Sole, as seen on the Copern… | yes (content re-render) | default (1) | **keep** | content |
| `meta` | text | Closed Sole · Special Release · One Run | yes (content re-render) | default (1) | **keep** | content |
| `btn_label` | text | Shop the collaboration | yes (content re-render) | default (1) | **keep** | content |
| `btn_url` | url | — | yes (content re-render) | default (1) | **keep** | content |
| `btn_new_tab` | checkbox | false | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `bg_image` | image_picker | — | yes (content re-render) | default (1) | **keep** | content |
| `bg_image_url` | text | https://cdn.shopify.com/s/files/1/0045… | yes (content re-render) | default (1) | **keep** | content |
| `shoe_image` | image_picker | — | yes (content re-render) | default (1) | **keep** | content |
| `shoe_image_url` | text | https://cdn.shopify.com/s/files/1/0045… | yes (content re-render) | **1/1** product.coperni:coperni-crosslink=https://cdn.shopify.com/s/files/1/0045… | **keep** | content; set in 1/1 |
| `banner_height` | range | 480 | Save-only | **1/1** product.coperni:coperni-crosslink=1200 | **keep** | in use: non-default in 1/1 |
| `shoe_size` | range | 100 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `shoe_position_y` | range | 0 | Save-only | **1/1** product.coperni:coperni-crosslink=100 | **keep** | in use: non-default in 1/1 |
| `overlay_opacity` | range | 55 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `overlay_opacity_mobile` | range | 40 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `inset_top` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |

### `coperni-pdp-story` — "Coperni PDP story"
Instances: 1 in 1 file(s): product.coperni · keep 15 / remove 6 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `label` | text | The collaboration | yes (content re-render) | default (1) | **keep** | content |
| `quote` | textarea | Open, gripping, and free from all cons… | yes (content re-render) | **1/1** product.coperni:coperni-pdp-story=Open, gripping, and free from all cons… | **keep** | content; set in 1/1 |
| `body_1` | textarea | Coperni × Barreletics is a collaborati… | yes (content re-render) | **1/1** product.coperni:coperni-pdp-story=Coperni × Barreletics is a collaborati… | **keep** | content; set in 1/1 |
| `body_2` | textarea | These shoes were created to support th… | yes (content re-render) | **1/1** product.coperni:coperni-pdp-story=These shoes were created to support th… | **keep** | content; set in 1/1 |
| `note_label` | text | On the runway | yes (content re-render) | default (1) | **keep** | content |
| `note_text` | textarea | Footwear shifts too: the collection in… | yes (content re-render) | **1/1** product.coperni:coperni-pdp-story=Footwear shifts too: the collection in… | **keep** | content; set in 1/1 |
| `video` | video | — | yes (content re-render) | default (1) | **keep** | content |
| `video_url` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `video_caption` | text | Coperni 2026 · Paris | yes (content re-render) | **1/1** product.coperni:coperni-pdp-story=Coperni 2026 Paris Fashion Week | **keep** | content; set in 1/1 |
| `video_height_mobile` | range | 72 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `video_max_height_desktop` | range | 720 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `lead_image_height_mobile` | range | 52 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `inset_top` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `anchor_id` | text | coperni-story | yes (content re-render) | default (1) | **keep** | content |
| `aria_label` | text | Coperni collaboration story | yes (content re-render) | default (1) | **keep** | content |
| `runway_image.image` | image_picker | — | yes (content re-render) | default (3) | **keep** | content |
| `runway_image.image_url` | text | — | yes (content re-render) | **3/3** product.coperni:coperni-pdp-story=https://cdn.shopify.com/s/files/1/0045…; product.coperni:coperni-pdp-story=https://cdn.shopify.com/s/files/1/0045…; product.coperni:coperni-pdp-story=https://cdn.shopify.com/s/files/1/0045… | **keep** | content; set in 3/3 |

### `disciplines` — "Disciplines"
Instances: 5 in 5 file(s): collection, index, product, product.coperni, product.outdoor · keep 7 / remove 15 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `headline` | textarea | Upgrade your grip. Upgrade your workout. | yes (content re-render) | **1/5** product.outdoor:disciplines=Anywhere you'd go barefoot, but better. | **keep** | content; set in 1/5 |
| `heading_size_override` | number | — | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `heading_role` | select | display | n/a (unused in code) | default (5) | **remove** | dead: not read by any Liquid |
| `title_size` | select | default | n/a (unused in code) | default (5) | **remove** | dead: not read by any Liquid |
| `title_weight` | select | default | n/a (unused in code) | **4/5** collection:upgrade-grip=400; product.coperni:disciplines=400; product:disciplines=400 +1 more · values: 400×4 | **remove** | dead: not read by any Liquid; migration: 4 saved value(s) have no effect, drop keys |
| `subhead` | textarea | — | yes (content re-render) | default (5) | **keep** | content |
| `pad_y` | range | 64 | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `pad_y_mobile` | range | 64 | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `hide_tags_mobile` | checkbox | false | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `space_below_mobile` | range | 0 | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `bg_color` | color | #faf8f6 | Save-only | **1/5** index:disciplines=#ffffff | **keep** | in use: non-default in 1/5 |
| `aria_label` | text | Built for every studio discipline | yes (content re-render) | **1/5** product.outdoor:disciplines=Built for outdoors | **keep** | content; set in 1/5 |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (5) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (5) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (5) | **keep** | visibility switch; never used but cheap |
| `discipline.discipline` | text | Barre | yes (content re-render) | **26/30** collection:upgrade-grip=Reformer; collection:upgrade-grip=Megaformer; collection:upgrade-grip=Lagree +23 more · values: Reformer×4, Megaformer×4, Lagree×4, Pilates×4 | **keep** | content; set in 26/30 |

### `footer` 🔒 locked — "Footer"
Instances: 1 in 1 file(s): sections/footer-group · keep 26 / remove 10 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `show_studio_trust` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `studio_trust_title` | text | Trusted by 1,000's of instructors & st… | yes (content re-render) | default (1) | **keep** | content |
| `studio_trust_subhead` | textarea | Dig into deep lunges and every positio… | yes (content re-render) | **1/1** sections/footer-group:footer=Dig into deep lunges and every positio… | **keep** | content; set in 1/1 |
| `trust_theme` | select | light | Save-only | **1/1** sections/footer-group:footer=dark | **keep** | in use: non-default in 1/1 |
| `trust_title_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `trust_body_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_newsletter` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `join_theme` | select | light | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `join_title_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `join_body_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `newsletter_heading` | text | Join the list | yes (content re-render) | default (1) | **keep** | content |
| `newsletter_text` | textarea | New colorways and studio stories. | yes (content re-render) | default (1) | **keep** | content |
| `newsletter_cta` | text | Subscribe | yes (content re-render) | default (1) | **keep** | content |
| `newsletter_privacy` | text | By subscribing you agree to receive ma… | yes (content re-render) | default (1) | **keep** | content |
| `show_checklist` | checkbox | false | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `check_1` | text | New drops and studio stories first | yes (content re-render) | default (1) | **keep** | content |
| `check_2` | text | Early access to new colorways and limi… | yes (content re-render) | default (1) | **keep** | content |
| `check_3` | text | Studio partner discounts and events | yes (content re-render) | default (1) | **keep** | content |
| `check_4` | text | Care tips to extend the life of your p… | yes (content re-render) | default (1) | **keep** | content |
| `columns_theme` | select | light | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `menu` | link_list | — | yes (content re-render) | **1/1** sections/footer-group:footer=footer | **keep** | content; set in 1/1 |
| `menu_heading` | text | Explore | n/a (unused in code) | default (1) | **remove** | dead: not read by any Liquid |
| `shop_heading` | text | Shop | yes (content re-render) | default (1) | **keep** | content |
| `menu_shop` | link_list | — | yes (content re-render) | **1/1** sections/footer-group:footer=footer-shop | **keep** | content; set in 1/1 |
| `learn_heading` | text | Learn | yes (content re-render) | default (1) | **keep** | content |
| `menu_learn` | link_list | — | yes (content re-render) | **1/1** sections/footer-group:footer=footer-learn | **keep** | content; set in 1/1 |
| `support_heading` | text | Support | yes (content re-render) | default (1) | **keep** | content |
| `menu_support` | link_list | — | yes (content re-render) | **1/1** sections/footer-group:footer=footer-support | **keep** | content; set in 1/1 |
| `connect_heading` | text | Connect | yes (content re-render) | default (1) | **keep** | content |
| `menu_connect` | link_list | — | yes (content re-render) | default (1) | **keep** | content |
| `instagram_url` | url | — | yes (content re-render) | **1/1** sections/footer-group:footer=https://www.instagram.com/barreletics/ | **keep** | content; set in 1/1 |
| `tiktok_url` | url | — | yes (content re-render) | default (1) | **keep** | content |
| `facebook_url` | url | — | yes (content re-render) | default (1) | **keep** | content |
| `pinterest_url` | url | — | yes (content re-render) | default (1) | **keep** | content |
| `email_url` | url | — | yes (content re-render) | **1/1** sections/footer-group:footer=https://barreletics.com/pages/contact-… | **keep** | content; set in 1/1 |
| `usa_line` | text | Made in USA | yes (content re-render) | default (1) | **keep** | content |

### `fullbleed-statement` — "Fullbleed statement"
Instances: 19 in 14 file(s): article, collection, collection.apparel, index, page.best-grippy-socks, product, product.coperni, product.in-studio-template … · keep 28 / remove 15 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `show_text` | checkbox | true | Save-only | **10/19** collection.apparel:fullbleed-workout=false; index:fullbleed-statement=false; product.coperni:fullbleed-lifestyle=false +7 more · values: false×10 | **keep** | in use: non-default in 10/19 |
| `eyebrow` | text | — | yes (content re-render) | default (19) | **keep** | content |
| `title` | text | You commit to the class. Commit to the… | yes (content re-render) | **19/19** article:article-shop-banner=Shop Performance Skins.; collection.apparel:fullbleed-workout=BRING YOUR WORKOUT TO LIFE; collection:fullbleed-commit=Never slip in Chair Pose +16 more · values: ×8, BRING YOUR WORKOUT TO LIFE×3, Hold every pose.×3, Shop Performance Skins.×1 | **keep** | content; set in 19/19 |
| `heading_size_override` | number | — | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `title_role` | select | statement | n/a (unused in code) | **7/19** collection:fullbleed-commit=display; collection:fullbleed-studio=display; page.best-grippy-socks:seo-hero=display +4 more · values: display×7 | **remove** | dead: not read by any Liquid; migration: 7 saved value(s) have no effect, drop keys |
| `title_size` | select | default | n/a (unused in code) | default (19) | **remove** | dead: not read by any Liquid |
| `title_weight` | select | default | n/a (unused in code) | **8/19** collection:fullbleed-commit=400; collection:fullbleed-studio=400; page.best-grippy-socks:seo-hero=400 +5 more · values: 400×8 | **remove** | dead: not read by any Liquid; migration: 8 saved value(s) have no effect, drop keys |
| `body` | textarea | — | yes (content re-render) | **4/19** collection:fullbleed-commit=Never slip again in side plank; collection:fullbleed-studio=Same grip, same stability through ever…; page.best-grippy-socks:seo-hero=Searching for Pilates socks, yoga sock… +1 more · values: Never slip again in side plank×1, Same grip, same stability through ever…×1, Searching for Pilates socks, yoga sock…×1, Built to hold when it matters most, th…×1 | **keep** | content; set in 4/19 |
| `body_size` | select | default | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `cta_text` | text | Shop Now | yes (content re-render) | **16/19** article:article-shop-banner=Shop now; collection.apparel:fullbleed-workout=; index:fullbleed-statement= +13 more · values: ×11, Shop now×5 | **keep** | content; set in 16/19 |
| `cta_style` | select | solid | Save-only | **3/19** collection:fullbleed-commit=outline; collection:fullbleed-studio=outline; page.best-grippy-socks:never-loses=outline | **keep** | in use: non-default in 3/19 |
| `cta_bg_color` | color | #ffffff | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `cta_border_color` | color | #ffffff | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `cta_text_color` | color | #1c1916 | Save-only | **3/19** collection:fullbleed-commit=#ffffff; collection:fullbleed-studio=#ffffff; page.best-grippy-socks:never-loses=#ffffff | **keep** | in use: non-default in 3/19 |
| `cta_link_target` | select | custom | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `cta_url` | text | — | yes (content re-render) | **9/19** article:article-shop-banner=/collections/in-studio-grip; collection:fullbleed-commit=#grid; collection:fullbleed-studio=#grid +6 more · values: #grid×4, #buy×4, /collections/in-studio-grip×1 | **keep** | content; set in 9/19 |
| `video` | video | — | yes (content re-render) | **2/19** collection:fullbleed-studio=shopify://files/videos/Adobe_Spark_Vid…; page.best-grippy-socks:never-loses=shopify://files/videos/Barreletics_Ret… | **keep** | content; set in 2/19 |
| `video_url` | text | — | yes (content re-render) | **10/19** collection.apparel:fullbleed-workout=https://cdn.shopify.com/s/files/1/0045…; page.best-grippy-socks:never-loses=https://cdn.shopify.com/s/files/1/0045…; product.in-studio-template:fullbleed-lifestyle=https://cdn.shopify.com/videos/c/o/v/c… +7 more · values: https://cdn.shopify.com/s/files/1/0045…×4, https://cdn.shopify.com/videos/c/o/v/c…×2, https://barreletics.com/cdn/shop/video…×2, https://cdn.shopify.com/videos/c/o/v/2…×1 | **keep** | content; set in 10/19 |
| `image` | image_picker | — | yes (content re-render) | **7/19** article:article-shop-banner=shopify://shop_images/A43U1678.jpg; collection:fullbleed-commit=shopify://shop_images/te-pick-ig-studi…; collection:fullbleed-studio=shopify://shop_images/te-pick-ig-studi… +4 more · values: shopify://shop_images/te-pick-ig-studi…×2, shopify://shop_images/In_Studio_Perfor…×2, shopify://shop_images/A43U1678.jpg×1, shopify://shop_images/Red_Foot_-_Chat.…×1 | **keep** | content; set in 7/19 |
| `poster_url` | text | — | yes (content re-render) | **6/19** collection:fullbleed-commit=https://barreletics.com/cdn/shop/produ…; collection:fullbleed-studio=https://barreletics.com/cdn/shop/produ…; page.best-grippy-socks:never-loses=https://barreletics.com/cdn/shop/produ… +3 more · values: https://barreletics.com/cdn/shop/produ…×5, https://www.juicer.io/api/media/598642…×1 | **keep** | content; set in 6/19 |
| `image_asset` | text | — | yes (content re-render) | default (19) | **keep** | content |
| `image_url` | text | https://barreletics.com/cdn/shop/files… | yes (content re-render) | **18/19** article:article-shop-banner=; collection.apparel:fullbleed-workout=https://barreletics.com/cdn/shop/produ…; collection:fullbleed-commit=https://barreletics.com/cdn/shop/produ… +15 more · values: https://barreletics.com/cdn/shop/produ…×13, ×3, https://barreletics.com/cdn/shop/files…×1, https://www.juicer.io/api/media/598642…×1 | **keep** | content; set in 18/19 |
| `image_alt` | text | — | yes (content re-render) | **12/19** article:article-shop-banner=Barreletics Performance Skins in blue …; collection:fullbleed-studio=Studio workouts — Barreletics; page.best-grippy-socks:seo-hero=Performance Skins — full-underfoot gri… +9 more · values: Open Sole in studio×2, Open Sole studio workout×2, Barreletics in studio — Pilates and ba…×2, Barreletics Performance Skins in blue …×1 | **keep** | content; set in 12/19 |
| `image_mobile` | image_picker | — | yes (content re-render) | **3/19** article:article-shop-banner=shopify://shop_images/P5A4927.jpg; product.coperni:fullbleed-lifestyle=shopify://shop_images/phone-coperni-ru…; product:fullbleed-statement=shopify://shop_images/phone-multi-imag… | **keep** | content; set in 3/19 |
| `height_desktop` | select | 64 | Save-only | **19/19** article:article-shop-banner=80; collection.apparel:fullbleed-workout=70; collection:fullbleed-commit=80 +16 more · values: 80×11, 70×3, 90×2, 120×1 | **keep** | in use: non-default in 19/19 |
| `height_mobile` | range | 0 | Save-only | **2/19** product.one-off-closed:fullbleed-lifestyle=60; product.one-off-open:fullbleed-lifestyle=60 | **keep** | in use: non-default in 2/19 |
| `phone_match_image` | checkbox | false | Save-only | **2/19** article:article-shop-banner=true; page.best-grippy-socks:seo-hero=true | **keep** | in use: non-default in 2/19 |
| `image_fit_mobile` | select | cover | Save-only | **2/19** product.in-studio-template:fullbleed-statement=contain; product.open-sole:fullbleed-statement=contain | **keep** | in use: non-default in 2/19 |
| `media_bg_mobile` | color | — | Save-only | **2/19** product.in-studio-template:fullbleed-statement=#4a4a4a; product.open-sole:fullbleed-statement=#4a4a4a | **keep** | in use: non-default in 2/19 |
| `mobile_full_bleed` | checkbox | false | Save-only | **3/19** article:article-shop-banner=true; index:fullbleed-statement=true; product.coperni:fullbleed-lifestyle=true | **keep** | in use: non-default in 3/19 |
| `show_overlay` | checkbox | true | Save-only | **2/19** index:fullbleed-statement=false; page.best-grippy-socks:seo-hero=false | **keep** | in use: non-default in 2/19 |
| `overlay_opacity` | range | 55 | Save-only | **10/19** article:article-shop-banner=30; collection:fullbleed-commit=25; collection:fullbleed-studio=25 +7 more · values: 30×2, 25×2, 15×2, 0×1 | **keep** | in use: non-default in 10/19 |
| `media_fit` | select | cover | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `focal_x` | range | 50 | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `focal_y` | range | 50 | Save-only | **1/19** product.outdoor:fullbleed-statement=70 | **keep** | in use: non-default in 1/19 |
| `media_radius` | range | 0 | Save-only | default (19) | **remove** | default in all 19 instance(s); hardcode default |
| `aria_label` | text | — | yes (content re-render) | **5/19** article:article-shop-banner=Shop Performance Skins; collection:fullbleed-commit=Never slip in Chair Pose; collection:fullbleed-studio=Never slip in Chair Pose +2 more · values: Never slip in Chair Pose×2, Shop Performance Skins×1, Full-underfoot grip×1, Never loses grip×1 | **keep** | content; set in 5/19 |
| `inset_top` | range | 0 | Save-only (snippet) | default (19) | **remove** | shared inset never changed in 19 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (19) | **remove** | shared inset never changed in 19 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (19) | **remove** | shared inset never changed in 19 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (19) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (19) | **keep** | visibility switch; never used but cheap |

### `geo-section` — "GEO Content"
Instances: 7 in 7 file(s): collection.closed-sole, collection.open-sole, collection.outdoor, page.about, page.grip-comparison, page.our-story, page.technology · keep 6 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | Trusted in studios everywhere | yes (content re-render) | **7/7** collection.closed-sole:geo-section=Why studios choose Closed Sole; collection.open-sole:geo-section=Why studios choose Open Sole; collection.outdoor:geo-section=Where Outdoor grippy shoes perform +4 more · values: Barreletics, in brief×2, Why studios choose Closed Sole×1, Why studios choose Open Sole×1, Where Outdoor grippy shoes perform×1 | **keep** | content; set in 7/7 |
| `title_size` | select | default | Save-only | **2/7** page.about:about-geo=15; page.our-story:about-geo=15 | **keep** | in use: non-default in 2/7 |
| `question_size` | select | default | Save-only | **2/7** page.about:about-geo=16; page.our-story:about-geo=16 | **keep** | in use: non-default in 2/7 |
| `body_size` | select | default | Save-only | **2/7** page.about:about-geo=16; page.our-story:about-geo=16 | **keep** | in use: non-default in 2/7 |
| `geo_item.question` | text | — | yes (content re-render) | **24/24** collection.closed-sole:geo-section=Best grippy shoes for reformer footwork; collection.closed-sole:geo-section=Closed Sole grippy shoes for barre cla…; collection.closed-sole:geo-section=Grippy shoes for Lagree and Megaformer +21 more · values: What is Barreletics?×2, Open Sole or Closed Sole?×2, How does this relate to Joseph Pilates…×2, Where are Performance Skins made?×2 | **keep** | content; set in 24/24 |
| `geo_item.answer` | richtext | — | yes (content re-render) | **24/24** collection.closed-sole:geo-section=<p>Reformer carriage work demands tota…; collection.closed-sole:geo-section=<p>Relevé stability, pulse-work precis…; collection.closed-sole:geo-section=<p>Megaformer platforms demand maximum… +21 more · values: <p>Barreletics makes patented Performa…×2, <p>Closed Sole is heel and foot fully …×2, <p>Joseph Pilates designed Contrology …×2, <p>Made in the USA. Designed and manuf…×2 | **keep** | content; set in 24/24 |

### `guarantee-band` — "Guarantee Band"
Instances: 8 in 8 file(s): index, product, product.coperni, product.in-studio-template, product.one-off-closed, product.one-off-open, product.open-sole, product.outdoor · keep 14 / remove 11 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | — | yes (content re-render) | **7/8** product.coperni:guarantee-band=Our promise; product.in-studio-template:guarantee-band=Our promise; product:guarantee-band=Our promise +4 more · values: Our promise×7 | **keep** | content; set in 7/8 |
| `title` | text | Zero risk. All grip. | yes (content re-render) | **7/8** product.coperni:guarantee-band=Built on guarantees, not guesses.; product.in-studio-template:guarantee-band=Built on guarantees, not guesses.; product:guarantee-band=Built on guarantees, not guesses. +4 more · values: Built on guarantees, not guesses.×7 | **keep** | content; set in 7/8 |
| `heading_size_override` | number | — | Save-only | default (8) | **remove** | default in all 8 instance(s); hardcode default |
| `title_role` | select | statement | n/a (unused in code) | **8/8** index:guarantee-band=display; product.coperni:guarantee-band=display; product.in-studio-template:guarantee-band=display +5 more · values: display×8 | **remove** | dead: not read by any Liquid; migration: 8 saved value(s) have no effect, drop keys |
| `body` | textarea | Returns, warranty, and shipping that m… | yes (content re-render) | **7/8** product.coperni:guarantee-band=30-day returns for indoor try-on. 90-d…; product.in-studio-template:guarantee-band=30-day returns for indoor try-on. 90-d…; product:guarantee-band=30-day returns for indoor try-on. 90-d… +4 more · values: 30-day returns for indoor try-on. 90-d…×7 | **keep** | content; set in 7/8 |
| `cta_text` | text | — | yes (content re-render) | **7/8** product.coperni:guarantee-band=See details →; product.in-studio-template:guarantee-band=See details →; product:guarantee-band=See details → +4 more · values: See details →×7 | **keep** | content; set in 7/8 |
| `cta_style` | select | solid | Save-only | **7/8** product.coperni:guarantee-band=outline; product.in-studio-template:guarantee-band=outline; product:guarantee-band=outline +4 more · values: outline×7 | **keep** | in use: non-default in 7/8 |
| `cta_bg_color` | color | #1c1916 | Save-only | default (8) | **remove** | default in all 8 instance(s); hardcode default |
| `cta_border_color` | color | #1c1916 | Save-only | default (8) | **remove** | default in all 8 instance(s); hardcode default |
| `cta_text_color` | color | #ffffff | Save-only | **7/8** product.coperni:guarantee-band=#1c1916; product.in-studio-template:guarantee-band=#1c1916; product:guarantee-band=#1c1916 +4 more · values: #1c1916×7 | **keep** | in use: non-default in 7/8 |
| `cta_url` | url | — | yes (content re-render) | **7/8** product.coperni:guarantee-band=/pages/help#returns; product.in-studio-template:guarantee-band=/pages/help#returns; product:guarantee-band=/pages/help#returns +4 more · values: /pages/help#returns×7 | **keep** | content; set in 7/8 |
| `anchor_id` | text | guarantee | yes (content re-render) | default (8) | **keep** | content |
| `aria_label` | text | Guarantee | yes (content re-render) | default (8) | **keep** | content |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (8) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (8) | **remove** | shared inset never changed in 8 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (8) | **remove** | shared inset never changed in 8 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (8) | **remove** | shared inset never changed in 8 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (8) | **remove** | shared inset never changed in 8 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (8) | **remove** | shared inset never changed in 8 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (8) | **remove** | shared inset never changed in 8 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (8) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (8) | **keep** | visibility switch; never used but cheap |
| `point.title` | text | Free Shipping | yes (content re-render) | **24/25** index:guarantee-band=30-Day Returns; index:guarantee-band=90-Day Warranty; index:guarantee-band=Made in USA +21 more · values: 30-Day Returns×8, 90-Day Warranty×8, Built to Last×7, Made in USA×1 | **keep** | content; set in 24/25 |
| `point.detail` | text | On orders over $150 | yes (content re-render) | **24/25** index:guarantee-band=Returned items must be clean, unworn, …; index:guarantee-band=Defects only — not wear or accidents.; index:guarantee-band=No latex, no silicone +21 more · values: Returned items must be clean, unworn, …×8, Never loses grip.×7, Defects only, not wear or accidents.×6, Defects only — not wear or accidents.×2 | **keep** | content; set in 24/25 |
| `point.text` | text | — | yes (content re-render) | default (25) | **keep** | content |

### `header` — "Header"
Instances: 1 in 1 file(s): sections/header-group · keep 9 / remove 12 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `logo` | image_picker | — | yes (content re-render) | default (1) | **keep** | content |
| `menu` | link_list | — | yes (content re-render) | **1/1** sections/header-group:header=m4-menu | **keep** | content; set in 1/1 |
| `help_menu` | link_list | — | yes (content re-render) | **1/1** sections/header-group:header=help-menu | **keep** | content; set in 1/1 |
| `show_help` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_account` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_cart` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_action_labels` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `logo_height` | range | 22 | Save-only | **1/1** sections/header-group:header=56 | **keep** | in use: non-default in 1/1 |
| `logo_height_mobile` | range | 22 | Save-only | **1/1** sections/header-group:header=39 | **keep** | in use: non-default in 1/1 |
| `sticky_header` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `nav_link_size` | select | default | Save-only | **1/1** sections/header-group:header=16 | **keep** | in use: non-default in 1/1 |
| `nav_gap` | range | 28 | Save-only | **1/1** sections/header-group:header=50 | **keep** | in use: non-default in 1/1 |
| `nav_weight` | select | 400 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `action_link_size` | select | 14 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `action_gap` | range | 18 | Save-only | **1/1** sections/header-group:header=16 | **keep** | in use: non-default in 1/1 |
| `nav_distribute` | select | center | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `header_max_width` | range | 1320 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `header_pad_y` | range | 12 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `header_pad_x` | range | 56 | Save-only | **1/1** sections/header-group:header=48 | **keep** | in use: non-default in 1/1 |
| `header_bg` | color | #ffffff | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `header_text` | color | #4a4a4a | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |

### `home-juicer` 🔒 locked — "Juicer Instagram"
Instances: 10 in 10 file(s): collection, index, page.best-grippy-socks, product, product.coperni, product.in-studio-template, product.one-off-closed, product.one-off-open … · keep 11 / remove 10 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Follow the movement | yes (content re-render) | **1/10** page.best-grippy-socks:home-juicer=@barreletics | **keep** | content; set in 1/10 |
| `title` | text | @barreletics | yes (content re-render) | **1/10** page.best-grippy-socks:home-juicer=Studio workouts and footwear will neve… | **keep** | content; set in 1/10 |
| `body` | text | Real practitioners. Real studios. Real… | yes (content re-render) | default (10) | **keep** | content |
| `cta_text` | text | Follow on Instagram → | yes (content re-render) | default (10) | **keep** | content |
| `profile_url` | url | — | yes (content re-render) | **10/10** collection:home-juicer=https://www.instagram.com/barreletics/; index:home-juicer=https://www.instagram.com/barreletics/; page.best-grippy-socks:home-juicer=https://www.instagram.com/barreletics/ +7 more · values: https://www.instagram.com/barreletics/×10 | **keep** | content; set in 10/10 |
| `anchor_id` | text | instagram | yes (content re-render) | default (10) | **keep** | content |
| `feed_id` | text | barreletics | yes (content re-render) | default (10) | **keep** | content |
| `posts_per_page` | number | 12 | Save-only | **8/10** index:home-juicer=6; product.coperni:home-juicer=6; product.in-studio-template:home-juicer=6 +5 more · values: 6×8 | **keep** | in use: non-default in 8/10 |
| `max_pages` | number | 1 | Save-only | default (10) | **remove** | default in all 10 instance(s); hardcode default |
| `enable_see_more` | checkbox | true | Save-only | default (10) | **remove** | default in all 10 instance(s); hardcode default |
| `max_height` | range | 0 | Save-only | default (10) | **remove** | default in all 10 instance(s); hardcode default |
| `bg_color` | color | #ffffff | Save-only | **1/10** page.best-grippy-socks:home-juicer=#faf8f6 | **keep** | in use: non-default in 1/10 |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (10) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (10) | **remove** | shared inset never changed in 10 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (10) | **remove** | shared inset never changed in 10 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (10) | **remove** | shared inset never changed in 10 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (10) | **remove** | shared inset never changed in 10 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (10) | **remove** | shared inset never changed in 10 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (10) | **remove** | shared inset never changed in 10 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (10) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (10) | **keep** | visibility switch; never used but cheap |

### `main-cart` — "Main Cart"
Instances: 1 in 1 file(s): cart · keep 0 / remove 0 / merge 0

_No settings._

### `main-page` — "Page content"
Instances: 5 in 5 file(s): page, page.judgeme_all_reviews, page.returns-portal, page.reviews, page.start-a-retrun · keep 5 / remove 12 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `show_header` | checkbox | true | Save-only | **2/5** page.judgeme_all_reviews:page-content=false; page.reviews:page-content=false | **keep** | in use: non-default in 2/5 |
| `eyebrow` | text | — | yes (content re-render) | **2/5** page.returns-portal:page-content=Returns & Exchanges; page.start-a-retrun:page-content=Returns & Exchanges | **keep** | content; set in 2/5 |
| `fallback_title` | text | Page | yes (content re-render) | **4/5** page.judgeme_all_reviews:page-content=Reviews; page.returns-portal:page-content=Start a Return or Exchange; page.reviews:page-content=Reviews +1 more · values: Reviews×2, Start a Return or Exchange×2 | **keep** | content; set in 4/5 |
| `subtitle` | textarea | — | yes (content re-render) | default (5) | **keep** | content |
| `title_size` | select | default | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `content_width` | select | narrow | Save-only | **2/5** page.returns-portal:page-content=wide; page.start-a-retrun:page-content=wide | **keep** | in use: non-default in 2/5 |
| `background` | select | white | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (5) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (5) | **remove** | shared inset never changed in 5 instance(s); Save-only |

### `page-about-close` — "About — Close"
Instances: 2 in 2 file(s): page.about, page.our-story · keep 6 / remove 4 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | Let us knock your socks off | yes (content re-render) | default (2) | **keep** | content |
| `body` | text | One pair. All-over grip. Built for the… | yes (content re-render) | default (2) | **keep** | content |
| `cta_text` | text | Shop Performance Skins | yes (content re-render) | default (2) | **keep** | content |
| `cta_url` | url | — | yes (content re-render) | **2/2** page.about:about-close=/collections/barre-pilates-yoga-shoe-s…; page.our-story:about-close=/collections/barre-pilates-yoga-shoe-s… | **keep** | content; set in 2/2 |
| `aria_label` | text | Shop Performance Skins | yes (content re-render) | default (2) | **keep** | content |
| `title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | **1/2** page.our-story:about-close=300 | **keep** | in use: non-default in 1/2 |
| `body_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `cta_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |

### `page-about-facts` — "About — Facts"
Instances: 4 in 4 file(s): page.about, page.our-story, product.v-neck-tops, product.yoga-pants · keep 7 / remove 11 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | Made in the USA. | yes (content re-render) | default (4) | **keep** | content |
| `lede` | richtext | <p>Designed and manufactured in Michig… | yes (content re-render) | **3/4** page.about:about-facts=<p>Designed and manufactured in Michig…; page.our-story:about-facts=<p>Designed and manufactured in Michig…; product.v-neck-tops:page_about_facts_EziCVR=<p>Designed and manufactured in the US… | **keep** | content; set in 3/4 |
| `aria_label` | text | Made in the USA | yes (content re-render) | default (4) | **keep** | content |
| `title_size` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `fact_title_size` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `fact_title_weight` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `show_mentions` | checkbox | true | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `mentions_hide_mobile` | checkbox | false | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `mentions_style_desktop` | select | caps | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `mentions_style_mobile` | select | sentence | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `mentions_name_size` | select | 16 | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `mentions_lead` | text | Also featured in | yes (content re-render) | default (4) | **keep** | content |
| `mentions_items` | text | Free People, INTERNI, ITSLIQUID, Anthr… | yes (content re-render) | default (4) | **keep** | content |
| `fact.title` | text | — | yes (content re-render) | **16/16** page.about:about-facts=Coperni; page.about:about-facts=Venice; page.about:about-facts=195 countries +13 more · values: Coperni×4, 195 countries×4, 1,000+ instructors×4, Free People×3 | **keep** | content; set in 16/16 |
| `fact.description` | text | — | yes (content re-render) | **16/16** page.about:about-facts=Spring-Summer 2026 runway, Paris.; page.about:about-facts=Biennale Arte 2026.; page.about:about-facts=Shipped worldwide. +13 more · values: Shipped worldwide.×4, Trusted in studio.×4, Spring 2026.×3, Spring-Summer 2026 runway, Paris.×2 | **keep** | content; set in 16/16 |

### `page-about-hero` — "About — Hero"
Instances: 2 in 2 file(s): page.about, page.our-story · keep 9 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `image` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `image_url` | text | https://barreletics.com/cdn/shop/produ… | yes (content re-render) | default (2) | **keep** | content |
| `image_alt` | text | Two women in Performance Skins | yes (content re-render) | default (2) | **keep** | content |
| `aria_label` | text | Barreletics in motion | yes (content re-render) | default (2) | **keep** | content |
| `media_height` | range | 520 | Save-only | **1/2** page.about:about-hero=640 | **keep** | in use: non-default in 1/2 |
| `media_position` | select | center | Save-only | **1/2** page.about:about-hero=top | **keep** | in use: non-default in 1/2 |
| `media_height_mobile` | range | 460 | Save-only | **1/2** page.about:about-hero=720 | **keep** | in use: non-default in 1/2 |
| `aspect_ratio_mobile` | select | natural | Save-only | **1/2** page.about:about-hero=portrait | **keep** | in use: non-default in 1/2 |
| `media_position_mobile` | select | center | Save-only | **1/2** page.about:about-hero=top | **keep** | in use: non-default in 1/2 |

### `page-about-intro` — "About — Intro"
Instances: 2 in 2 file(s): page.about, page.our-story · keep 5 / remove 6 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Our story | yes (content re-render) | default (2) | **keep** | content |
| `lede` | richtext | <p>Patented Performance Skins for barr… | yes (content re-render) | default (2) | **keep** | content |
| `byline` | text | Stefanie Miller, Founder | yes (content re-render) | default (2) | **keep** | content |
| `pull_quote` | text | We didn't improve the grip sock. We ma… | yes (content re-render) | default (2) | **keep** | content |
| `aria_label` | text | Our story | yes (content re-render) | default (2) | **keep** | content |
| `title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `pull_quote_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `pull_quote_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |

### `page-about-joseph` — "About — Joseph"
Instances: 2 in 2 file(s): page.about, page.our-story · keep 9 / remove 5 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `gallery_aria` | text | Joseph Pilates archival photographs | yes (content re-render) | default (2) | **keep** | content |
| `image_1` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `image_1_url` | text | https://barreletics.com/cdn/shop/files… | yes (content re-render) | default (2) | **keep** | content |
| `image_1_alt` | text | Archival photograph of Joseph Pilates … | yes (content re-render) | default (2) | **keep** | content |
| `image_2` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `image_2_url` | text | https://barreletics.com/cdn/shop/files… | yes (content re-render) | default (2) | **keep** | content |
| `image_2_alt` | text | Archival photograph of Joseph Pilates … | yes (content re-render) | default (2) | **keep** | content |
| `title` | text | Joseph Pilates built the method around… | yes (content re-render) | default (2) | **keep** | content |
| `body` | richtext | — | yes (content re-render) | **2/2** page.about:about-joseph=<p>Joseph Pilates developed his method…; page.our-story:about-joseph=<p>Joseph Pilates developed his method… | **keep** | content; set in 2/2 |
| `heading_size_override` | number | — | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mobile_stack_order` | select | media_first | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |

### `page-about-split` — "About — Split"
Instances: 6 in 2 file(s): page.about, page.our-story · keep 11 / remove 5 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `aria_label` | text | Story section | yes (content re-render) | **6/6** page.about:about-founder=Stefanie Miller — founder; page.about:about-prototype=From prototype to Performance Skins; page.about:about-letter=Letter from the founder +3 more · values: Stefanie Miller — founder×2, From prototype to Performance Skins×2, Letter from the founder×2 | **keep** | content; set in 6/6 |
| `title` | text | — | yes (content re-render) | **4/6** page.about:about-founder=Fashion trained the eye. The studio se…; page.about:about-prototype=The idea became the product.; page.our-story:about-founder=Fashion trained the eye. The studio se… +1 more · values: Fashion trained the eye. The studio se…×2, The idea became the product.×2 | **keep** | content; set in 4/6 |
| `body` | richtext | — | yes (content re-render) | **6/6** page.about:about-founder=<p>A former career as a fashion model …; page.about:about-prototype=<p>One day, stuck in side plank and sl…; page.about:about-letter=<p>Every pair is made to perform, and … +3 more · values: <p>A former career as a fashion model …×2, <p>One day, stuck in side plank and sl…×2, <p>Every pair is made to perform, and …×2 | **keep** | content; set in 6/6 |
| `image` | image_picker | — | yes (content re-render) | default (6) | **keep** | content |
| `image_url` | text | — | yes (content re-render) | **6/6** page.about:about-founder=https://barreletics.com/cdn/shop/files…; page.about:about-prototype=https://barreletics.com/cdn/shop/files…; page.about:about-letter=https://barreletics.com/cdn/shop/files… +3 more · values: https://barreletics.com/cdn/shop/files…×6 | **keep** | content; set in 6/6 |
| `image_alt` | text | — | yes (content re-render) | **6/6** page.about:about-founder=Stefanie Miller, founder of Barreletics; page.about:about-prototype=Early Performance Skin prototypes; page.about:about-letter=Stefanie Miller, founder of Barreletics +3 more · values: Stefanie Miller, founder of Barreletics×4, Early Performance Skin prototypes×2 | **keep** | content; set in 6/6 |
| `heading_size_override` | number | — | Save-only | default (6) | **remove** | default in all 6 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (6) | **remove** | default in all 6 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (6) | **remove** | default in all 6 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (6) | **remove** | default in all 6 instance(s); hardcode default |
| `reverse` | checkbox | false | Save-only | **2/6** page.about:about-prototype=true; page.our-story:about-prototype=true | **keep** | in use: non-default in 2/6 |
| `mobile_stack_order` | select | media_first | Save-only | default (6) | **remove** | default in all 6 instance(s); hardcode default |
| `media_column_pct` | range | 50 | Save-only | **2/6** page.about:about-letter=48; page.our-story:about-letter=48 | **keep** | in use: non-default in 2/6 |
| `cream_bg` | checkbox | false | Save-only | **2/6** page.about:about-prototype=true; page.our-story:about-prototype=true | **keep** | in use: non-default in 2/6 |
| `media_max_px` | range | 760 | Save-only | **4/6** page.about:about-prototype=500; page.about:about-letter=620; page.our-story:about-prototype=500 +1 more · values: 500×2, 620×2 | **keep** | in use: non-default in 4/6 |
| `media_max_px_mobile` | range | 480 | Save-only | **5/6** page.about:about-prototype=360; page.about:about-letter=440; page.our-story:about-founder=780 +2 more · values: 360×2, 440×2, 780×1 | **keep** | in use: non-default in 5/6 |

### `page-about-values` — "About — Values"
Instances: 2 in 2 file(s): page.about, page.our-story · keep 4 / remove 6 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | What we stand for | yes (content re-render) | default (2) | **keep** | content |
| `aria_label` | text | What we stand for | yes (content re-render) | default (2) | **keep** | content |
| `title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `card_title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `card_title_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `value.title` | text | — | yes (content re-render) | **10/10** page.about:about-values=Performance over promise; page.about:about-values=Category creation; page.about:about-values=Durability as design +7 more · values: Performance over promise×2, Category creation×2, Durability as design×2, Commitment match×2 | **keep** | content; set in 10/10 |
| `value.description` | textarea | — | yes (content re-render) | **10/10** page.about:about-values=Every claim we make is backed by the p…; page.about:about-values=We're not competing in the grip sock m…; page.about:about-values=Products should outlast the hype cycle… +7 more · values: Every claim we make is backed by the p…×2, We're not competing in the grip sock m…×2, Products should outlast the hype cycle…×2, You show up 6 days a week. Your gear s…×2 | **keep** | content; set in 10/10 |

### `page-ambassador` — "Ambassador Page"
Instances: 1 in 1 file(s): page.ambassador · keep 6 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Ambassador program | yes (content re-render) | default (1) | **keep** | content |
| `body` | richtext | <p>For instructors and practitioners w… | yes (content re-render) | **1/1** page.ambassador:ambassador-content=<p>For instructors and practitioners w… | **keep** | content; set in 1/1 |
| `consent_text` | textarea | I understand this is an application, n… | yes (content re-render) | default (1) | **keep** | content |
| `submit_text` | text | Submit application | yes (content re-render) | default (1) | **keep** | content |
| `success_message` | textarea | Application received. We reply within … | yes (content re-render) | **1/1** page.ambassador:ambassador-content=Application received. We reply within … | **keep** | content; set in 1/1 |
| `form_token` | text | BL-PARTNER-AMBASSADOR | yes (content re-render) | default (1) | **keep** | content |

### `page-compare` — "Compare Page"
Instances: 2 in 2 file(s): page.compare, page.compare-open-vs-closed · keep 21 / remove 1 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Two versions. One performance. | yes (content re-render) | default (2) | **keep** | content |
| `title` | text | Open Sole vs Closed Sole | yes (content re-render) | default (2) | **keep** | content |
| `subtitle` | textarea | Both perform identically — same grip, … | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=Both perform identically: same grip, s…; page.compare:compare-content=Both perform identically: same grip, s… | **keep** | content; set in 2/2 |
| `product_a` | product | — | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=studio-performance-skin-footwear; page.compare:compare-content=studio-performance-skin-footwear | **keep** | content; set in 2/2 |
| `product_a_image` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `product_a_name` | text | Open Sole | yes (content re-render) | default (2) | **keep** | content |
| `product_a_desc` | textarea | Heel exposed, mid-foot breathing hole.… | yes (content re-render) | default (2) | **keep** | content |
| `product_a_cta` | text | Shop Open Sole | yes (content re-render) | default (2) | **keep** | content |
| `product_a_url` | url | — | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=/products/studio-performance-skin-foot…; page.compare:compare-content=/products/studio-performance-skin-foot… | **keep** | content; set in 2/2 |
| `product_b` | product | — | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=best-reformer-pilates-legree-workout-s…; page.compare:compare-content=best-reformer-pilates-legree-workout-s… | **keep** | content; set in 2/2 |
| `product_b_image` | image_picker | — | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=shopify://shop_images/A14_TopBottom_Gr…; page.compare:compare-content=shopify://shop_images/A14_TopBottom_Gr… | **keep** | content; set in 2/2 |
| `product_b_name` | text | Closed Sole | yes (content re-render) | default (2) | **keep** | content |
| `product_b_desc` | textarea | Heel and foot fully covered. Same grip… | yes (content re-render) | default (2) | **keep** | content |
| `product_b_cta` | text | Shop Closed Sole | yes (content re-render) | default (2) | **keep** | content |
| `product_b_url` | url | — | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=/products/best-reformer-pilates-legree…; page.compare:compare-content=/products/best-reformer-pilates-legree… | **keep** | content; set in 2/2 |
| `shared_note` | textarea | Both deliver the same molded 360° full… | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=; page.compare:compare-content= | **keep** | content; set in 2/2 |
| `bottom_cta_heading` | text | Not sure? Start with the pair that mat… | n/a (unused in code) | **2/2** page.compare-open-vs-closed:compare-content=; page.compare:compare-content= | **remove** | dead: not read by any Liquid; migration: 2 saved value(s) have no effect, drop keys |
| `bottom_cta_label` | text | Shop All | yes (content re-render) | default (2) | **keep** | content |
| `bottom_cta_url` | url | — | yes (content re-render) | **2/2** page.compare-open-vs-closed:compare-content=/collections/barre-pilates-yoga-shoe-s…; page.compare:compare-content=/collections/barre-pilates-yoga-shoe-s… | **keep** | content; set in 2/2 |
| `feature_row.feature` | text | — | yes (content re-render) | **16/16** page.compare-open-vs-closed:compare-content=Heel; page.compare-open-vs-closed:compare-content=Mid-foot; page.compare-open-vs-closed:compare-content=Feel +13 more · values: Heel×2, Mid-foot×2, Feel×2, Toe splay×2 | **keep** | content; set in 16/16 |
| `feature_row.value_a` | text | — | yes (content re-render) | **16/16** page.compare-open-vs-closed:compare-content=Heel exposed: direct contact with the …; page.compare-open-vs-closed:compare-content=Mid-foot breathing hole; page.compare-open-vs-closed:compare-content=More grounded, barefoot feel +13 more · values: Heel exposed: direct contact with the …×2, Mid-foot breathing hole×2, More grounded, barefoot feel×2, Natural toe splay×2 | **keep** | content; set in 16/16 |
| `feature_row.value_b` | text | — | yes (content re-render) | **16/16** page.compare-open-vs-closed:compare-content=Heel and foot fully covered; page.compare-open-vs-closed:compare-content=Covered through the mid-foot; page.compare-open-vs-closed:compare-content=Second-skin coverage underfoot +13 more · values: Heel and foot fully covered×2, Covered through the mid-foot×2, Second-skin coverage underfoot×2, Natural toe splay×2 | **keep** | content; set in 16/16 |

### `page-contact` — "Contact Page"
Instances: 2 in 2 file(s): page.contact, page.contact-us-form · keep 6 / remove 4 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Get in Touch | yes (content re-render) | default (2) | **keep** | content |
| `subtitle` | textarea | Have a question about fit, orders, or … | yes (content re-render) | default (2) | **keep** | content |
| `title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `button_text` | text | Send Message | yes (content re-render) | default (2) | **keep** | content |
| `success_message` | text | Thanks for reaching out. We'll get bac… | yes (content re-render) | default (2) | **keep** | content |
| `info_heading` | text | Response Time | yes (content re-render) | default (2) | **keep** | content |
| `response_time` | textarea | We respond to all inquiries within 24-… | yes (content re-render) | default (2) | **keep** | content |

### `page-faq` — "FAQ Page"
Instances: 1 in 1 file(s): page.faq · keep 8 / remove 9 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Frequently Asked Questions | yes (content re-render) | default (1) | **keep** | content |
| `subtitle` | textarea | — | yes (content re-render) | default (1) | **keep** | content |
| `bg_class` | select | cream | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `title_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `question_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_search` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `search_placeholder` | text | Search sizing, shipping, grip, returns… | yes (content re-render) | default (1) | **keep** | content |
| `show_topics` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `contact_url` | url | — | yes (content re-render) | **1/1** page.faq:faq-content=/pages/contact-us-form | **keep** | content; set in 1/1 |
| `show_related` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `related_title` | text | More help | yes (content re-render) | default (1) | **keep** | content |
| `faq_item.category` | text | Orders & shipping | yes (content re-render) | **26/30** page.faq:faq-content=Product; page.faq:faq-content=Product; page.faq:faq-content=Product +23 more · values: Product×9, Care & durability×7, Fit & sizing×6, Policies×4 | **keep** | content; set in 26/30 |
| `faq_item.question` | text | — | yes (content re-render) | **30/30** page.faq:faq-content=How fast do orders ship?; page.faq:faq-content=What does shipping cost?; page.faq:faq-content=Do you ship internationally? +27 more · values: How fast do orders ship?×1, What does shipping cost?×1, Do you ship internationally?×1, My tracking says delivered but I don't…×1 | **keep** | content; set in 30/30 |
| `faq_item.answer` | richtext | — | yes (content re-render) | **30/30** page.faq:faq-content=<p>Orders process within 24-48 hours a…; page.faq:faq-content=<p><strong>Free</strong> on Continenta…; page.faq:faq-content=<p>Yes, we ship to 195 countries via F… +27 more · values: <p>Hand wash with warm soapy water. Th…×2, <p>Orders process within 24-48 hours a…×1, <p><strong>Free</strong> on Continenta…×1, <p>Yes, we ship to 195 countries via F…×1 | **keep** | content; set in 30/30 |

### `page-grip-comparison` — "Grip Comparison Page"
Instances: 1 in 1 file(s): page.grip-comparison · keep 27 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | Barreletics vs Grip Socks | yes (content re-render) | default (1) | **keep** | content |
| `hero_subtitle` | textarea | The grip sock fails two ways simultane… | yes (content re-render) | default (1) | **keep** | content |
| `hero_cta_text` | text | Shop Performance Skins — $74 | yes (content re-render) | **1/1** page.grip-comparison:grip-comparison=Shop Performance Skins · $74 | **keep** | content; set in 1/1 |
| `hero_cta_url` | url | — | yes (content re-render) | **1/1** page.grip-comparison:grip-comparison=/collections/barre-pilates-yoga-shoe-s… | **keep** | content; set in 1/1 |
| `table_heading` | text | Side-by-Side Comparison | yes (content re-render) | default (1) | **keep** | content |
| `double_failure_heading` | text | The Double Failure of Grip Socks | yes (content re-render) | default (1) | **keep** | content |
| `failure_1_text` | textarea | Silicone dots are a surface applicatio… | yes (content re-render) | default (1) | **keep** | content |
| `failure_2_text` | textarea | Fabric absorbs perspiration during cla… | yes (content re-render) | **1/1** page.grip-comparison:grip-comparison=Fabric absorbs perspiration during cla… | **keep** | content; set in 1/1 |
| `sock_math_heading` | text | The Math: Grip Socks vs Barreletics | yes (content re-render) | default (1) | **keep** | content |
| `sock_cost_per_pair` | text | $14-18 | yes (content re-render) | default (1) | **keep** | content |
| `sock_pairs_per_year` | text | 6-8 | yes (content re-render) | default (1) | **keep** | content |
| `sock_annual_cost` | text | $112-144 | yes (content re-render) | default (1) | **keep** | content |
| `barreletics_price` | text | $74 | yes (content re-render) | default (1) | **keep** | content |
| `savings_text` | textarea | Save $38-70 in year one alone. Every y… | yes (content re-render) | default (1) | **keep** | content |
| `bottom_cta_heading` | text | Ready to Upgrade? | yes (content re-render) | default (1) | **keep** | content |
| `bottom_cta_body` | textarea | One pair. 360° grip. No more replacing… | yes (content re-render) | default (1) | **keep** | content |
| `bottom_cta_text` | text | Shop Now — $74 | yes (content re-render) | **1/1** page.grip-comparison:grip-comparison=Shop Now · $74 | **keep** | content; set in 1/1 |
| `bottom_cta_url` | url | — | yes (content re-render) | **1/1** page.grip-comparison:grip-comparison=/collections/barre-pilates-yoga-shoe-s… | **keep** | content; set in 1/1 |
| `comparison_row.feature` | text | — | yes (content re-render) | **8/8** page.grip-comparison:grip-comparison=Grip Type; page.grip-comparison:grip-comparison=Material; page.grip-comparison:grip-comparison=Cost +5 more · values: Grip Type×1, Material×1, Cost×1, Lifespan×1 | **keep** | content; set in 8/8 |
| `comparison_row.barreletics` | text | — | yes (content re-render) | **8/8** page.grip-comparison:grip-comparison=360° injection-molded full-contact sur…; page.grip-comparison:grip-comparison=Non-porous: doesn't absorb sweat; page.grip-comparison:grip-comparison=$74 one-time purchase +5 more · values: 360° injection-molded full-contact sur…×1, Non-porous: doesn't absorb sweat×1, $74 one-time purchase×1, 1,000 classes. Another customer is on …×1 | **keep** | content; set in 8/8 |
| `comparison_row.grip_socks` | text | — | yes (content re-render) | **8/8** page.grip-comparison:grip-comparison=Silicone dots printed or glued on fabric; page.grip-comparison:grip-comparison=Fabric: absorbs moisture; page.grip-comparison:grip-comparison=$14-18/pair × 6-8 pairs/year = $112-14… +5 more · values: Silicone dots printed or glued on fabric×1, Fabric: absorbs moisture×1, $14-18/pair × 6-8 pairs/year = $112-14…×1, 6-8 weeks before grip fails×1 | **keep** | content; set in 8/8 |
| `quote.quote` | textarea | — | yes (content re-render) | **2/2** page.grip-comparison:grip-comparison=I was buying new grip socks every 6-8 …; page.grip-comparison:grip-comparison=Did the math after a year. I would hav… | **keep** | content; set in 2/2 |
| `quote.author` | text | — | yes (content re-render) | **2/2** page.grip-comparison:grip-comparison=Verified Buyer; page.grip-comparison:grip-comparison=Verified Buyer | **keep** | content; set in 2/2 |
| `quote.context` | text | — | yes (content re-render) | **2/2** page.grip-comparison:grip-comparison=Reformer, 5 days/week; page.grip-comparison:grip-comparison=Barre, 6 days/week | **keep** | content; set in 2/2 |
| `faq_item.question` | text | — | yes (content re-render) | **5/5** page.grip-comparison:grip-comparison=Are Barreletics really better than gri…; page.grip-comparison:grip-comparison=How much do grip socks actually cost p…; page.grip-comparison:grip-comparison=Why do grip socks stop working? +2 more · values: Are Barreletics really better than gri…×1, How much do grip socks actually cost p…×1, Why do grip socks stop working?×1, Can I still use Barreletics at studios…×1 | **keep** | content; set in 5/5 |
| `faq_item.answer` | richtext | — | yes (content re-render) | **5/5** page.grip-comparison:grip-comparison=<p>Yes, in every measurable category: …; page.grip-comparison:grip-comparison=<p>At $14-18 per pair and replacing ev…; page.grip-comparison:grip-comparison=<p>Two reasons: (1) The silicone dots … +2 more · values: <p>Yes, in every measurable category: …×1, <p>At $14-18 per pair and replacing ev…×1, <p>Two reasons: (1) The silicone dots …×1, <p>Barreletics serve the same purpose …×1 | **keep** | content; set in 5/5 |

### `page-help` — "Help hub"
Instances: 1 in 1 file(s): page.collaborations · keep 6 / remove 6 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | How Can We Help? | yes (content re-render) | **1/1** page.collaborations:collab-hub=Collaborations | **keep** | content; set in 1/1 |
| `lede` | textarea | Answers, policy, sizing, and contact —… | yes (content re-render) | **1/1** page.collaborations:collab-hub=Built with people who move the culture… | **keep** | content; set in 1/1 |
| `title_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `grid_band` | select | cream | Save-only | **1/1** page.collaborations:collab-hub=white | **keep** | in use: non-default in 1/1 |
| `card_title_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `card_title_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `destination.title` | text | FAQ | yes (content re-render) | **2/2** page.collaborations:collab-hub=Coperni; page.collaborations:collab-hub=Free People | **keep** | content; set in 2/2 |
| `destination.body` | textarea | — | yes (content re-render) | **2/2** page.collaborations:collab-hub=Closed Sole for Paris: Barreletics × C…; page.collaborations:collab-hub=On the floor at Free People. Same grip. | **keep** | content; set in 2/2 |
| `destination.url` | url | — | yes (content re-render) | **2/2** page.collaborations:collab-hub=/products/barreletics-x-coperni-closed…; page.collaborations:collab-hub=/pages/free-people | **keep** | content; set in 2/2 |

### `page-returns` — "Help / Returns"
Instances: 3 in 3 file(s): page.help, page.returns, page.shipping-retruns · keep 25 / remove 4 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | — | yes (content re-render) | default (3) | **keep** | content |
| `title` | text | Help | yes (content re-render) | default (3) | **keep** | content |
| `lede` | textarea | 30 days to try on indoors for fit. 90-… | yes (content re-render) | **3/3** page.help:page-returns=30-day returns for indoor try-on. 90-d…; page.returns:page-returns=30-day returns for indoor try-on. 90-d…; page.shipping-retruns:page-returns=30-day returns for indoor try-on. 90-d… | **keep** | content; set in 3/3 |
| `title_size` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `portal_url` | url | — | yes (content re-render) | **3/3** page.help:page-returns=/pages/returns-portal; page.returns:page-returns=/pages/returns-portal; page.shipping-retruns:page-returns=/pages/returns-portal | **keep** | content; set in 3/3 |
| `size_url` | url | — | yes (content re-render) | **3/3** page.help:page-returns=/pages/performance-skins-size-chart; page.returns:page-returns=/pages/performance-skins-size-chart; page.shipping-retruns:page-returns=/pages/performance-skins-size-chart | **keep** | content; set in 3/3 |
| `contact_url` | url | — | yes (content re-render) | **3/3** page.help:page-returns=/pages/contact-us-form; page.returns:page-returns=/pages/contact-us-form; page.shipping-retruns:page-returns=/pages/contact-us-form | **keep** | content; set in 3/3 |
| `start_cta_label` | text | Start a return | yes (content re-render) | default (3) | **keep** | content |
| `returns_heading` | text | Returns & exchanges | yes (content re-render) | default (3) | **keep** | content |
| `returns_body` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<p>Returns and exchanges are accepted …; page.returns:page-returns=<p>Returns and exchanges are accepted …; page.shipping-retruns:page-returns=<p>Returns and exchanges are accepted … | **keep** | content; set in 3/3 |
| `warranty_heading` | text | 90-day warranty | yes (content re-render) | default (3) | **keep** | content |
| `warranty_body` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<p>Every pair of Barreletics Performan…; page.returns:page-returns=<p>Every pair of Barreletics Performan…; page.shipping-retruns:page-returns=<p>Every pair of Barreletics Performan… | **keep** | content; set in 3/3 |
| `warranty_covered` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<ul><li>Manufacturing defects</li><li>…; page.returns:page-returns=<ul><li>Manufacturing defects</li><li>…; page.shipping-retruns:page-returns=<ul><li>Manufacturing defects</li><li>… | **keep** | content; set in 3/3 |
| `warranty_not_covered` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<ul><li>Normal wear and tear</li><li>A…; page.returns:page-returns=<ul><li>Normal wear and tear</li><li>A…; page.shipping-retruns:page-returns=<ul><li>Normal wear and tear</li><li>A… | **keep** | content; set in 3/3 |
| `shipping_heading` | text | Free over $150 | yes (content re-render) | default (3) | **keep** | content |
| `shipping_body` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<ul><li><strong>Free shipping</strong>…; page.returns:page-returns=<ul><li><strong>Free shipping</strong>…; page.shipping-retruns:page-returns=<ul><li><strong>Free shipping</strong>… | **keep** | content; set in 3/3 |
| `exchanges_heading` | text | Size exchanges | yes (content re-render) | default (3) | **keep** | content |
| `exchanges_body` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<p>Exchanges must be initiated within …; page.returns:page-returns=<p>Exchanges must be initiated within …; page.shipping-retruns:page-returns=<p>Exchanges must be initiated within … | **keep** | content; set in 3/3 |
| `intl_heading` | text | International orders & returns | yes (content re-render) | default (3) | **keep** | content |
| `intl_body` | richtext | — | yes (content re-render) | **3/3** page.help:page-returns=<p><strong>Duties and taxes are charge…; page.returns:page-returns=<p><strong>Duties and taxes are charge…; page.shipping-retruns:page-returns=<p><strong>Duties and taxes are charge… | **keep** | content; set in 3/3 |
| `faq_heading` | text | Quick answers | yes (content re-render) | default (3) | **keep** | content |
| `cta_title` | text | Need a hand? | yes (content re-render) | default (3) | **keep** | content |
| `cta_body` | textarea | Sizing, claims, or a stuck return — Co… | yes (content re-render) | **3/3** page.help:page-returns=Sizing, claims, or a stuck return? Con…; page.returns:page-returns=Sizing, claims, or a stuck return? Con…; page.shipping-retruns:page-returns=Sizing, claims, or a stuck return? Con… | **keep** | content; set in 3/3 |
| `cta_portal_label` | text | Start a return | yes (content re-render) | default (3) | **keep** | content |
| `cta_label` | text | Contact | yes (content re-render) | default (3) | **keep** | content |
| `cta_refund_note` | textarea | Refunds are processed within 72 hours … | yes (content re-render) | default (3) | **keep** | content |

### `page-shipping` — "Shipping Page"
Instances: 1 in 1 file(s): page.shipping · keep 11 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Shipping | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | Shipping Information | yes (content re-render) | default (1) | **keep** | content |
| `subtitle` | textarea | Fast, reliable shipping to 195 countri… | yes (content re-render) | default (1) | **keep** | content |
| `domestic_heading` | text | Domestic Shipping | yes (content re-render) | default (1) | **keep** | content |
| `domestic_text` | richtext | <p>Orders ship within 1-2 business day… | yes (content re-render) | **1/1** page.shipping:shipping-content=<p>Orders ship within 1-2 business day… | **keep** | content; set in 1/1 |
| `international_heading` | text | International Shipping | yes (content re-render) | default (1) | **keep** | content |
| `international_text` | richtext | <p>We ship to 195 countries via FedEx … | yes (content re-render) | **1/1** page.shipping:shipping-content=<p>We ship to 195 countries via FedEx … | **keep** | content; set in 1/1 |
| `highlight.title` | text | — | yes (content re-render) | **3/3** page.shipping:shipping-content=Ships in 1-2 Days; page.shipping:shipping-content=Free Over $150; page.shipping:shipping-content=195 Countries | **keep** | content; set in 3/3 |
| `highlight.description` | textarea | — | yes (content re-render) | **3/3** page.shipping:shipping-content=Orders processed and shipped within 1-…; page.shipping:shipping-content=Free shipping on all domestic orders o…; page.shipping:shipping-content=International shipping via FedEx Inter… | **keep** | content; set in 3/3 |
| `faq_item.question` | text | — | yes (content re-render) | **4/4** page.shipping:shipping-content=How long does shipping take?; page.shipping:shipping-content=Do I get a tracking number?; page.shipping:shipping-content=What about duties and taxes for intern… +1 more · values: How long does shipping take?×1, Do I get a tracking number?×1, What about duties and taxes for intern…×1, Can I change my shipping address after…×1 | **keep** | content; set in 4/4 |
| `faq_item.answer` | richtext | — | yes (content re-render) | **4/4** page.shipping:shipping-content=<p>Domestic orders ship within 1-2 bus…; page.shipping:shipping-content=<p>Yes. You'll receive a shipping conf…; page.shipping:shipping-content=<p>They're charged at checkout. In mos… +1 more · values: <p>Domestic orders ship within 1-2 bus…×1, <p>Yes. You'll receive a shipping conf…×1, <p>They're charged at checkout. In mos…×1, <p>Contact us immediately after placin…×1 | **keep** | content; set in 4/4 |

### `page-size-guide` — "Size Guide Page"
Instances: 3 in 3 file(s): page.performance-skins-size-chart, page.size-chart, page.size-guide · keep 15 / remove 5 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Fit Guide | yes (content re-render) | default (3) | **keep** | content |
| `title` | text | Size Guide | yes (content re-render) | default (3) | **keep** | content |
| `subtitle` | textarea | Two sizes, and at the 7.5 overlap the … | yes (content re-render) | **3/3** page.performance-skins-size-chart:size-guide=Two sizes, and at the 7.5 overlap the …; page.size-chart:size-guide=Two sizes, and at the 7.5 overlap the …; page.size-guide:size-guide=Two sizes, and at the 7.5 overlap the … | **keep** | content; set in 3/3 |
| `title_size` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `body_size` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `body_weight` | select | default | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `snug_colors_note` | textarea | Dark Grey, Hot Coral, and Blue run sli… | yes (content re-render) | default (3) | **keep** | content |
| `light_grey_note` | textarea | Black and Light Grey offer a slightly … | yes (content re-render) | default (3) | **keep** | content |
| `cta_text` | text | Shop Now | yes (content re-render) | default (3) | **keep** | content |
| `cta_url` | url | — | yes (content re-render) | **3/3** page.performance-skins-size-chart:size-guide=/collections/barre-pilates-yoga-shoe-s…; page.size-chart:size-guide=/collections/barre-pilates-yoga-shoe-s…; page.size-guide:size-guide=/collections/barre-pilates-yoga-shoe-s… | **keep** | content; set in 3/3 |
| `cta_note` | textarea | Still unsure? Contact us and we'll hel… | yes (content re-render) | **3/3** page.performance-skins-size-chart:size-guide=Still unsure? Contact us with your usu…; page.size-chart:size-guide=Still unsure? Contact us with your usu…; page.size-guide:size-guide=Still unsure? Contact us with your usu… | **keep** | content; set in 3/3 |
| `show_related` | checkbox | true | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `related_title` | text | More help | yes (content re-render) | default (3) | **keep** | content |
| `size_row.size_name` | text | — | yes (content re-render) | **6/6** page.performance-skins-size-chart:size-guide=M; page.performance-skins-size-chart:size-guide=L; page.size-chart:size-guide=M +3 more · values: M×3, L×3 | **keep** | content; set in 6/6 |
| `size_row.us_size` | text | — | yes (content re-render) | **6/6** page.performance-skins-size-chart:size-guide=5.5–7.5; page.performance-skins-size-chart:size-guide=7.5–11; page.size-chart:size-guide=5.5–7.5 +3 more · values: 5.5–7.5×3, 7.5–11×3 | **keep** | content; set in 6/6 |
| `size_row.mens_size` | text | — | yes (content re-render) | **6/6** page.performance-skins-size-chart:size-guide=—; page.performance-skins-size-chart:size-guide=Up to 10.5; page.size-chart:size-guide=— +3 more · values: —×3, Up to 10.5×3 | **keep** | content; set in 6/6 |
| `size_row.kids_size` | text | — | yes (content re-render) | **6/6** page.performance-skins-size-chart:size-guide=2–5; page.performance-skins-size-chart:size-guide=—; page.size-chart:size-guide=2–5 +3 more · values: 2–5×3, —×3 | **keep** | content; set in 6/6 |
| `fit_tip.title` | text | — | yes (content re-render) | **12/12** page.performance-skins-size-chart:size-guide=Between sizes? Width decides.; page.performance-skins-size-chart:size-guide=Narrow feet; page.performance-skins-size-chart:size-guide=How they should feel +9 more · values: Between sizes? Width decides.×3, Narrow feet×3, How they should feel×3, How to place them×3 | **keep** | content; set in 12/12 |
| `fit_tip.description` | textarea | — | yes (content re-render) | **12/12** page.performance-skins-size-chart:size-guide=7.5 sits in both rows on purpose. Don'…; page.performance-skins-size-chart:size-guide=Take the Medium if you're a narrow 7.5…; page.performance-skins-size-chart:size-guide=Secure, not pinching, and not sliding … +9 more · values: 7.5 sits in both rows on purpose. Don'…×3, Take the Medium if you're a narrow 7.5…×3, Secure, not pinching, and not sliding …×3, The ball of your foot sits where your …×3 | **keep** | content; set in 12/12 |

### `page-technology` — "Technology Page"
Instances: 1 in 1 file(s): page.technology · keep 18 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | The Technology | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | Patented 360° Grip Technology | yes (content re-render) | default (1) | **keep** | content |
| `subtitle` | textarea | Not printed. Not glued. Injection-mold… | yes (content re-render) | default (1) | **keep** | content |
| `how_heading` | text | How It Works | yes (content re-render) | default (1) | **keep** | content |
| `how_it_works` | richtext | <p>Traditional grip socks use silicone… | yes (content re-render) | **1/1** page.technology:tech-content=<p>Traditional grip socks use silicone… | **keep** | content; set in 1/1 |
| `double_failure_heading` | text | The Double Failure of Grip Socks | yes (content re-render) | default (1) | **keep** | content |
| `double_failure_text` | richtext | <p><strong>Failure #1: The grip wears … | yes (content re-render) | **1/1** page.technology:tech-content=<p><strong>Failure #1: The grip wears … | **keep** | content; set in 1/1 |
| `materials_heading` | text | Materials | yes (content re-render) | default (1) | **keep** | content |
| `manufacturing_heading` | text | Made in USA | yes (content re-render) | default (1) | **keep** | content |
| `manufacturing_text` | richtext | <p>Every pair of Barreletics is manufa… | yes (content re-render) | default (1) | **keep** | content |
| `cta_heading` | text | Experience the Difference | yes (content re-render) | default (1) | **keep** | content |
| `cta_body` | textarea | One pair. 360° grip. Made to last year… | yes (content re-render) | default (1) | **keep** | content |
| `cta_text` | text | Shop Performance Skins | yes (content re-render) | default (1) | **keep** | content |
| `cta_url` | url | — | yes (content re-render) | **1/1** page.technology:tech-content=/collections/barre-pilates-yoga-shoe-s… | **keep** | content; set in 1/1 |
| `feature.title` | text | — | yes (content re-render) | **4/4** page.technology:tech-content=360° Full-Contact Grip; page.technology:tech-content=Injection-Molded; page.technology:tech-content=Non-Porous Surface +1 more · values: 360° Full-Contact Grip×1, Injection-Molded×1, Non-Porous Surface×1, Wipes clean×1 | **keep** | content; set in 4/4 |
| `feature.description` | textarea | — | yes (content re-render) | **4/4** page.technology:tech-content=Not dots. Not strips. The entire sole …; page.technology:tech-content=The grip is created during manufacturi…; page.technology:tech-content=Unlike fabric, our material doesn't ab… +1 more · values: Not dots. Not strips. The entire sole …×1, The grip is created during manufacturi…×1, Unlike fabric, our material doesn't ab…×1, Non-porous, so it wipes clean. Nothing…×1 | **keep** | content; set in 4/4 |
| `material.title` | text | — | yes (content re-render) | **4/4** page.technology:tech-content=Non-Porous; page.technology:tech-content=Wipes clean; page.technology:tech-content=Latex-Free +1 more · values: Non-Porous×1, Wipes clean×1, Latex-Free×1, Silicone-Free×1 | **keep** | content; set in 4/4 |
| `material.description` | textarea | — | yes (content re-render) | **4/4** page.technology:tech-content=Doesn't absorb sweat or odor. Rinse cl…; page.technology:tech-content=Non-porous, so it wipes clean. Nothing…; page.technology:tech-content=Safe for those with latex sensitivitie… +1 more · values: Doesn't absorb sweat or odor. Rinse cl…×1, Non-porous, so it wipes clean. Nothing…×1, Safe for those with latex sensitivitie…×1, No silicone dots or adhesives. The gri…×1 | **keep** | content; set in 4/4 |

### `page-warranty` — "Warranty Page"
Instances: 1 in 1 file(s): page.warranty · keep 9 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Warranty | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | 90-Day Warranty | yes (content re-render) | default (1) | **keep** | content |
| `subtitle` | textarea | Every pair of Barreletics is backed by… | yes (content re-render) | default (1) | **keep** | content |
| `international_heading` | text | International Warranty Claims | yes (content re-render) | default (1) | **keep** | content |
| `international_text` | richtext | <p>International customers do not need… | yes (content re-render) | **1/1** page.warranty:warranty-content=<p>International customers do not need… | **keep** | content; set in 1/1 |
| `covered.text` | text | — | yes (content re-render) | **4/4** page.warranty:warranty-content=Grip separation from the sole; page.warranty:warranty-content=Strap detachment or failure; page.warranty:warranty-content=Material splitting or cracking (not fr… +1 more · values: Grip separation from the sole×1, Strap detachment or failure×1, Material splitting or cracking (not fr…×1, Manufacturing irregularities affecting…×1 | **keep** | content; set in 4/4 |
| `not_covered.text` | text | — | yes (content re-render) | **5/5** page.warranty:warranty-content=Normal wear from regular use; page.warranty:warranty-content=Cosmetic changes (color fading, surfac…; page.warranty:warranty-content=Damage from improper care +2 more · values: Normal wear from regular use×1, Cosmetic changes (color fading, surfac…×1, Damage from improper care×1, Damage from use on abrasive or uninten…×1 | **keep** | content; set in 5/5 |
| `claim_step.title` | text | — | yes (content re-render) | **4/4** page.warranty:warranty-content=Contact Support; page.warranty:warranty-content=Send Photos; page.warranty:warranty-content=We Review +1 more · values: Contact Support×1, Send Photos×1, We Review×1, Resolution×1 | **keep** | content; set in 4/4 |
| `claim_step.description` | textarea | — | yes (content re-render) | **4/4** page.warranty:warranty-content=Email our support team with your order…; page.warranty:warranty-content=Include clear photos showing the defec…; page.warranty:warranty-content=Our team reviews your claim within 2-3… +1 more · values: Email our support team with your order…×1, Include clear photos showing the defec…×1, Our team reviews your claim within 2-3…×1, Approved claims receive a replacement …×1 | **keep** | content; set in 4/4 |

### `page-wholesale` — "Wholesale Page"
Instances: 3 in 3 file(s): page.partners, page.studio-program, page.wholesale · keep 5 / remove 0 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Wholesale | yes (content re-render) | default (3) | **keep** | content |
| `body` | richtext | <p>Studios, instructors, retailers, an… | yes (content re-render) | **3/3** page.partners:partners-portal=<p>Studios, instructors, retailers, an…; page.studio-program:studio-portal=<p>Studios, instructors, retailers, an…; page.wholesale:wholesale-content=<p>Studios, instructors, retailers, an… | **keep** | content; set in 3/3 |
| `submit_text` | text | Submit | yes (content re-render) | default (3) | **keep** | content |
| `success_message` | textarea | Got it. We reply within 2–3 business d… | yes (content re-render) | **3/3** page.partners:partners-portal=Got it. We reply within 2-3 business d…; page.studio-program:studio-portal=Got it. We reply within 2-3 business d…; page.wholesale:wholesale-content=Got it. We reply within 2-3 business d… | **keep** | content; set in 3/3 |
| `form_token` | text | BL-PARTNER-APPLY | yes (content re-render) | default (3) | **keep** | content |

### `pdp-buy-box` 🔒 locked — "PDP Buy Box"
Instances: 9 in 9 file(s): product, product.coperni, product.in-studio-template, product.one-off-closed, product.one-off-open, product.open-sole, product.outdoor, product.v-neck-tops … · keep 17 / remove 10 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `lede_line_1` | text | Secure in every hold. | yes (content re-render) | **5/9** product.one-off-closed:pdp-buy-box=Limited color. Limited run.; product.one-off-open:pdp-buy-box=Limited color. Limited run.; product.outdoor:pdp-buy-box=Perfect for +2 more · values: Limited color. Limited run.×2, Perfect for×1, Softness. Versatility. Comfort.×1, Focus on your workout.×1 | **keep** | content; set in 5/9 |
| `lede_line_2` | text | No sliding. No resets. | yes (content re-render) | **5/9** product.one-off-closed:pdp-buy-box=Once it's gone, it's gone.; product.one-off-open:pdp-buy-box=Once it's gone, it's gone.; product.outdoor:pdp-buy-box=outdoor adventures. +2 more · values: Once it's gone, it's gone.×2, outdoor adventures.×1, Lightweight. Doesn't pill.×1, High-rise compression.×1 | **keep** | content; set in 5/9 |
| `short_description` | textarea | The premium grip system that replaces … | yes (content re-render) | **8/9** product.coperni:pdp-buy-box=On the Paris runway: Fashion Week 2026.; product.in-studio-template:pdp-buy-box=Grippy shoes designed for Barre, Pilat…; product.one-off-closed:pdp-buy-box=Exclusive Closed Sole one-off colorway… +5 more · values: Grippy shoes designed for Barre, Pilat…×2, On the Paris runway: Fashion Week 2026.×1, Exclusive Closed Sole one-off colorway…×1, Exclusive Open Sole one-off colorways.…×1 | **keep** | content; set in 8/9 |
| `hero_image_mode` | select | admin_order | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `hero_color` | text | — | yes (content re-render) | default (9) | **keep** | content |
| `hero_media_index` | range | 1 | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `thumb_count` | range | 7 | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `show_rating_row` | checkbox | true | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `rating_text` | text | Trusted by 1,000+ Instructors | yes (content re-render) | default (9) | **keep** | content |
| `reviews_anchor` | text | #reviews | yes (content re-render) | default (9) | **keep** | content |
| `show_payment_line` | checkbox | false | n/a (unused in code) | **7/9** product.coperni:pdp-buy-box=true; product.in-studio-template:pdp-buy-box=true; product:pdp-buy-box=true +4 more · values: true×7 | **remove** | dead: not read by any Liquid; migration: 7 saved value(s) have no effect, drop keys |
| `payment_line` | text | or 4 × $18.50 | yes (content re-render) | default (9) | **keep** | content |
| `show_size_chart_link` | checkbox | true | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `size_chart_url` | url | — | yes (content re-render) | **2/9** product.v-neck-tops:pdp-buy-box=/pages/yoga-pants-t-shirt-size-guide; product.yoga-pants:pdp-buy-box=/pages/yoga-pants-size-guide | **keep** | content; set in 2/9 |
| `show_trust_row` | checkbox | false | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `show_sole_badge` | checkbox | true | Save-only | **2/9** product.v-neck-tops:pdp-buy-box=false; product.yoga-pants:pdp-buy-box=false | **keep** | in use: non-default in 2/9 |
| `sole_badge` | text | — | yes (content re-render) | **7/9** product.coperni:pdp-buy-box=Limited Edition; product.in-studio-template:pdp-buy-box=Open Sole; product:pdp-buy-box=Closed Sole +4 more · values: Open Sole×3, Closed Sole×2, Limited Edition×1, Outdoor×1 | **keep** | content; set in 7/9 |
| `sole_badge_color` | select | rust | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `show_soon_size` | checkbox | false | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `show_oneoff_link` | checkbox | true | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `show_kit_links` | checkbox | true | Save-only | **8/9** product.coperni:pdp-buy-box=false; product.in-studio-template:pdp-buy-box=false; product.one-off-closed:pdp-buy-box=false +5 more · values: false×8 | **keep** | in use: non-default in 8/9 |
| `size_soon_note` | text | — | yes (content re-render) | default (9) | **keep** | content |
| `description_accordion_body` | textarea | — | yes (content re-render) | **6/9** product.coperni:pdp-buy-box=Limited-edition Closed Sole for the Co…; product.in-studio-template:pdp-buy-box=Designed for Barre, Pilates, Reformer,…; product:pdp-buy-box=Designed for Barre, Pilates, Reformer,… +3 more · values: Designed for Barre, Pilates, Reformer,…×3, Limited-edition Closed Sole for the Co…×1, Super cozy, ultra-light performance T-…×1, Luxury compression leggings built for …×1 | **keep** | content; set in 6/9 |
| `description_footnote` | textarea | — | yes (content re-render) | **1/9** product.outdoor:pdp-buy-box=Like any footwear, Barreletics won't c… | **keep** | content; set in 1/9 |
| `note_accordion_label` | text | — | yes (content re-render) | **1/9** product.outdoor:pdp-buy-box=Good to know | **keep** | content; set in 1/9 |
| `note_accordion_body` | textarea | — | yes (content re-render) | **1/9** product.outdoor:pdp-buy-box=Like any footwear, Barreletics won't c… | **keep** | content; set in 1/9 |
| `shipping_accordion` | textarea | Complimentary shipping on orders over … | yes (content re-render) | **9/9** product.coperni:pdp-buy-box=Complimentary shipping on orders over …; product.in-studio-template:pdp-buy-box=Complimentary shipping on orders over …; product:pdp-buy-box=Complimentary shipping on orders over … +6 more · values: Complimentary shipping on orders over …×9 | **keep** | content; set in 9/9 |

### `pdp-features` — "PDP Features"
Instances: 11 in 11 file(s): collection, collection.apparel, product, product.coperni, product.in-studio-template, product.one-off-closed, product.one-off-open, product.open-sole … · keep 9 / remove 8 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | Why Barreletics | yes (content re-render) | **4/11** collection.apparel:apparel-fabric-proof=Why Barreletics Apparel; product.outdoor:pdp-features=Outdoor; product.v-neck-tops:pdp-features=Why these tees +1 more · values: Why Barreletics Apparel×1, Outdoor×1, Why these tees×1, Why these pants×1 | **keep** | content; set in 4/11 |
| `title` | html | Built around<br>one obsession: <strong… | yes (content re-render) | **11/11** collection.apparel:apparel-fabric-proof=Fabric that earns its keep.; collection:no-socks-features=No socks.<br>Just <strong>grip.</strong>; product.coperni:pdp-features=Built around one obsession: <strong>Gr… +8 more · values: Built around one obsession: <strong>Gr…×4, Fabric that earns its keep.×3, Same grip. Limited color.×2, No socks.<br>Just <strong>grip.</strong>×1 | **keep** | content; set in 11/11 |
| `heading_size_override` | number | — | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `title_size` | select | 56 | n/a (unused in code) | **4/11** collection.apparel:apparel-fabric-proof=40; collection:no-socks-features=44; product.in-studio-template:pdp-features=default +1 more · values: default×2, 40×1, 44×1 | **remove** | dead: not read by any Liquid; migration: 4 saved value(s) have no effect, drop keys |
| `title_weight` | select | 400 | n/a (unused in code) | **4/11** collection.apparel:apparel-fabric-proof=default; collection:no-socks-features=default; product.in-studio-template:pdp-features=default +1 more · values: default×4 | **remove** | dead: not read by any Liquid; migration: 4 saved value(s) have no effect, drop keys |
| `body_size` | select | default | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `bg_color` | color | #ffffff | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `pad_top` | range | 32 | Save-only | **2/11** collection.apparel:apparel-fabric-proof=64; collection:no-socks-features=64 | **keep** | in use: non-default in 2/11 |
| `pad_bottom` | range | 32 | Save-only | **2/11** collection.apparel:apparel-fabric-proof=64; collection:no-socks-features=64 | **keep** | in use: non-default in 2/11 |
| `pad_top_mobile` | range | 24 | n/a (unused in code) | **2/11** collection.apparel:apparel-fabric-proof=48; collection:no-socks-features=48 | **remove** | dead: not read by any Liquid; migration: 2 saved value(s) have no effect, drop keys |
| `pad_bottom_mobile` | range | 24 | n/a (unused in code) | **2/11** collection.apparel:apparel-fabric-proof=48; collection:no-socks-features=48 | **remove** | dead: not read by any Liquid; migration: 2 saved value(s) have no effect, drop keys |
| `footnote` | textarea | — | yes (content re-render) | **1/11** product.outdoor:pdp-features=*Like any footwear, they won't create … | **keep** | content; set in 1/11 |
| `show_disciplines` | checkbox | false | Save-only | default (11) | **remove** | default in all 11 instance(s); hardcode default |
| `aria_label` | text | Product features | yes (content re-render) | **4/11** collection.apparel:apparel-fabric-proof=Fabric that earns its keep.; collection:no-socks-features=No socks. Just grip.; product.v-neck-tops:pdp-features=Fabric that earns its keep. +1 more · values: Fabric that earns its keep.×3, No socks. Just grip.×1 | **keep** | content; set in 4/11 |
| `anchor_id` | text | — | yes (content re-render) | **4/11** collection.apparel:apparel-fabric-proof=fabric; collection:no-socks-features=no-socks; product.v-neck-tops:pdp-features=fabric +1 more · values: fabric×3, no-socks×1 | **keep** | content; set in 4/11 |
| `feature.title` | text | 360° Grip | yes (content re-render) | **57/58** collection.apparel:apparel-fabric-proof=Made in the USA; collection.apparel:apparel-fabric-proof=Italian 4-way stretch; collection.apparel:apparel-fabric-proof=Reinforced knees +54 more · values: Built to Last×7, Natural Toe Splay×7, Second-Skin×7, No Sliding. No Resets.×6 | **keep** | content; set in 57/58 |
| `feature.description` | textarea | Every direction. Every movement. | yes (content re-render) | **57/58** collection.apparel:apparel-fabric-proof=Cut and sewn stateside, not a mystery …; collection.apparel:apparel-fabric-proof=Sculpting compression that moves with …; collection.apparel:apparel-fabric-proof=Built-up panels where barre and Pilate… +54 more · values: No stretching out. No replacing socks.×7, Locked-in grip through holds, transiti…×6, Grip and stability that let you move w…×6, Unbeatable traction on studio floors, …×6 | **keep** | content; set in 57/58 |

### `pdp-reviews` — "Reviews"
Instances: 15 in 15 file(s): collection, collection.apparel, index, page.best-grippy-socks, page.judgeme_all_reviews, page.reviews, product, product.coperni … · keep 31 / remove 12 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `band_context` | select | pdp | Save-only | **5/15** collection.apparel:reviews=collection; collection:reviews=collection; page.best-grippy-socks:reviews=home +2 more · values: collection×2, reviews_page×2, home×1 | **keep** | in use: non-default in 5/15 |
| `title` | text | Real people. Real results. | yes (content re-render) | **1/15** product.outdoor:reviews=Real people. Real outdoors. | **keep** | content; set in 1/15 |
| `body` | text | See the difference. Feel the grip. | yes (content re-render) | **6/15** collection.apparel:reviews=From the studio floor.; page.judgeme_all_reviews:reviews=Verified reviews from the barre, Pilat…; page.reviews:reviews=Verified reviews from the barre, Pilat… +3 more · values: From the studio floor.×3, Verified reviews from the barre, Pilat…×2, ×1 | **keep** | content; set in 6/15 |
| `bg_color` | color | #ffffff | Save-only | **1/15** page.best-grippy-socks:reviews=#faf8f6 | **keep** | in use: non-default in 1/15 |
| `show_photo_cards` | checkbox | true | yes ({% style %}) | **13/15** collection.apparel:reviews=false; collection:reviews=false; index:reviews=false +10 more · values: false×13 | **keep** | in use: non-default in 13/15 |
| `photo_cards_per_row` | select | 3 | yes ({% style %}) | **2/15** page.judgeme_all_reviews:reviews=4; page.reviews:reviews=4 | **keep** | in use: non-default in 2/15 |
| `photo_card_rows` | select | 1 | yes ({% style %}) | default (15) | **remove** | default in all 15 instance(s); hardcode default |
| `photo_cards_per_row_mobile` | select | 1 | yes ({% style %}) | default (15) | **remove** | default in all 15 instance(s); hardcode default |
| `show_text_cards` | checkbox | true | yes ({% style %}) | **2/15** page.judgeme_all_reviews:reviews=false; page.reviews:reviews=false | **keep** | in use: non-default in 2/15 |
| `community_label` | text | More from the community | yes (content re-render) | **1/15** product.outdoor:reviews= | **keep** | content; set in 1/15 |
| `text_cards_initial` | range | 0 | Save-only | **1/15** index:reviews=3 | **keep** | in use: non-default in 1/15 |
| `text_cards_initial_mobile` | range | 2 | Save-only | **1/15** index:reviews=3 | **keep** | in use: non-default in 1/15 |
| `text_cards_expand` | checkbox | false | Save-only | **1/15** index:reviews=true | **keep** | in use: non-default in 1/15 |
| `all_reviews_label` | text | Read reviews → | yes (content re-render) | **3/15** index:reviews=More stories →; page.judgeme_all_reviews:reviews=; page.reviews:reviews= | **keep** | content; set in 3/15 |
| `all_reviews_url` | url | — | yes (content re-render) | **13/15** collection.apparel:reviews=/pages/reviews; collection:reviews=/pages/reviews; index:reviews=/pages/reviews +10 more · values: /pages/reviews×13 | **keep** | content; set in 13/15 |
| `show_live_text` | checkbox | true | Save-only | **13/15** collection.apparel:reviews=false; collection:reviews=false; index:reviews=false +10 more · values: false×13 | **keep** | in use: non-default in 13/15 |
| `show_aggregate` | checkbox | false | Save-only | **14/15** collection.apparel:reviews=true; collection:reviews=true; page.best-grippy-socks:reviews=true +11 more · values: true×14 | **keep** | in use: non-default in 14/15 |
| `anchor_id` | text | reviews | yes (content re-render) | default (15) | **keep** | content |
| `inset_top` | range | 0 | Save-only (snippet) | default (15) | **remove** | shared inset never changed in 15 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (15) | **remove** | shared inset never changed in 15 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (15) | **remove** | shared inset never changed in 15 instance(s); Save-only |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (15) | **remove** | dead: not read by any Liquid |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (15) | **remove** | shared inset never changed in 15 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (15) | **remove** | shared inset never changed in 15 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (15) | **remove** | shared inset never changed in 15 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (15) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (15) | **keep** | visibility switch; never used but cheap |
| `featured_review.rating` | range | 5 | Save-only | default (8) | **remove** | default in all 8 instance(s); hardcode default |
| `featured_review.body` | textarea | Where have you been all my life? These… | yes (content re-render) | **7/8** collection:reviews=Where have you been all my life? These…; product.coperni:reviews=Where have you been all my life? These…; product.in-studio-template:reviews=I've tried several grip socks. The gri… +4 more · values: Where have you been all my life? These…×3, I've tried several grip socks. The gri…×2, This pair is my second purchased, my f…×1, WORTH IT! My Pilates game completely c…×1 | **keep** | content; set in 7/8 |
| `featured_review.author` | text | Verified buyer | yes (content re-render) | **4/8** product.in-studio-template:reviews=Leslie S.; product.one-off-closed:reviews=Kimberly; product.one-off-open:reviews=Leslie S. +1 more · values: Leslie S.×2, Kimberly×1, Cristina Gonzalez×1 | **keep** | content; set in 4/8 |
| `featured_review.location` | text | Pilates | yes (content re-render) | **4/8** product.in-studio-template:reviews=Katy, US; product.one-off-closed:reviews=Knoxville, US; product.one-off-open:reviews=Katy, US +1 more · values: Katy, US×2, Knoxville, US×1, Verified buyer×1 | **keep** | content; set in 4/8 |
| `photo_review.image` | image_picker | — | yes (content re-render) | default (38) | **keep** | content |
| `photo_review.image_url` | text | — | yes (content re-render) | **32/38** collection.apparel:reviews=https://cdn.shopify.com/s/files/1/0045…; collection.apparel:reviews=https://cdn.shopify.com/s/files/1/0045…; collection.apparel:reviews=https://cdn.shopify.com/s/files/1/0045… +29 more · values: https://review-images.judgeme.com/barr…×26, https://cdn.shopify.com/s/files/1/0045…×5, https://barreletics.com/cdn/shop/produ…×1 | **keep** | content; set in 32/38 |
| `photo_review.title` | text | — | yes (content re-render) | **17/38** page.judgeme_all_reviews:reviews=Yoga and Beyond; page.reviews:reviews=Yoga and Beyond; product.in-studio-template:reviews=Sock era: over. +14 more · values: Consistent grip. Real confidence.×3, Great for travel yoga.×3, Best for barre & Pilates.×3, Yoga and Beyond×2 | **keep** | content; set in 17/38 |
| `photo_review.body` | textarea | — | yes (content re-render) | **38/38** collection.apparel:reviews=These are really good for weak knees! …; collection.apparel:reviews=I'm a Pilates instructor and I love th…; collection.apparel:reviews=I feel so much more stable and safe du… +35 more · values: I have tried several brands of grips s…×6, These grippy shoes are the best most c…×6, Use these for heated yoga and they are…×5, I'm a Pilates instructor and I love th…×3 | **keep** | content; set in 38/38 |
| `photo_review.author` | text | — | yes (content re-render) | **38/38** collection.apparel:reviews=KLP; collection.apparel:reviews=Jennifer K.; collection.apparel:reviews=Anna W. +35 more · values: Leslie S.×6, B P.×6, Jo-z×5, Jennifer K.×3 | **keep** | content; set in 38/38 |
| `photo_review.location` | text | — | yes (content re-render) | **35/38** collection.apparel:reviews=Verified Purchase; collection.apparel:reviews=Pilates instructor; collection.apparel:reviews=Fullerton, US +32 more · values: Katy, US×6, Philadelphia, US×6, Baltimore, US×5, Verified Purchase×4 | **keep** | content; set in 35/38 |
| `photo_review.rating` | range | 5 | Save-only | default (38) | **remove** | default in all 38 instance(s); hardcode default |
| `text_review.title` | text | — | yes (content re-render) | **30/66** product.in-studio-template:reviews=Secure from the first class.; product.in-studio-template:reviews=Plank without fear.; product.in-studio-template:reviews=After spinal fusion, still steady. +27 more · values: Way too expensive? Game changer.×3, Skeptical. Worth it.×3, After the first class…×3, Always in my bag.×3 | **keep** | content; set in 30/66 |
| `text_review.body` | textarea | — | yes (content re-render) | **66/66** collection.apparel:reviews=Luxury compression with reinforced kne…; collection.apparel:reviews=The performance tees are soft, light, …; collection.apparel:reviews=Size down on the yoga pants. The high … +63 more · values: I was looking for a 'good' pair of Pil…×6, I'm a Pilates instructor and I love th…×4, I am a full-time Barre instructor and …×3, I was dreading going back to Pilates a…×3 | **keep** | content; set in 66/66 |
| `text_review.author` | text | — | yes (content re-render) | **66/66** collection.apparel:reviews=Studio regular; collection.apparel:reviews=Verified Purchase; collection.apparel:reviews=Verified Purchase +63 more · values: Wendy B.×6, Verified Purchase×5, Jennifer K.×4, Laura P.×3 | **keep** | content; set in 66/66 |
| `text_review.location` | text | — | yes (content re-render) | **66/66** collection.apparel:reviews=Verified Purchase; collection.apparel:reviews=US; collection.apparel:reviews=US +63 more · values: Verified Purchase×6, Grayslake, US×6, US×5, Pilates instructor×4 | **keep** | content; set in 66/66 |
| `text_review.rating` | range | 5 | Save-only | default (66) | **remove** | default in all 66 instance(s); hardcode default |

### `pdp-sock-math` — "Sock Math"
Instances: 5 in 5 file(s): collection, page.best-grippy-socks, product, product.in-studio-template, product.open-sole · keep 33 / remove 5 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `headline` | text | One pair. Done. | yes (content re-render) | **5/5** collection:pdp-sock-math=One pair.; page.best-grippy-socks:pdp-sock-math=One pair.; product.in-studio-template:pdp-sock-math=One pair. +2 more · values: One pair.×5 | **keep** | content; set in 5/5 |
| `heading_size_override` | number | — | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `done_line` | text | — | yes (content re-render) | **5/5** collection:pdp-sock-math=Done.; page.best-grippy-socks:pdp-sock-math=Done.; product.in-studio-template:pdp-sock-math=Done. +2 more · values: Done.×5 | **keep** | content; set in 5/5 |
| `punch` | text | — | yes (content re-render) | **5/5** collection:pdp-sock-math=This ends that.; page.best-grippy-socks:pdp-sock-math=This ends that.; product.in-studio-template:pdp-sock-math=This ends that. +2 more · values: This ends that.×5 | **keep** | content; set in 5/5 |
| `cycle_foot` | text | — | yes (content re-render) | **5/5** collection:pdp-sock-math=Yoga socks are useless.; page.best-grippy-socks:pdp-sock-math=Yoga socks are useless.; product.in-studio-template:pdp-sock-math=Yoga socks are useless. +2 more · values: Yoga socks are useless.×5 | **keep** | content; set in 5/5 |
| `title_size` | select | default | n/a (unused in code) | default (5) | **remove** | dead: not read by any Liquid |
| `title_weight` | select | 400 | n/a (unused in code) | default (5) | **remove** | dead: not read by any Liquid |
| `subheadline` | text | Smarter than grip socks. Your practice… | yes (content re-render) | **5/5** collection:pdp-sock-math=Last month you said grip socks were a …; page.best-grippy-socks:pdp-sock-math=Last month you said grip socks were a …; product.in-studio-template:pdp-sock-math=Last month you said grip socks were a … +2 more · values: Last month you said grip socks were a …×5 | **keep** | content; set in 5/5 |
| `body_size` | select | default | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `cta_text` | text | — | yes (content re-render) | **2/5** product.in-studio-template:pdp-sock-math=Shop now; product.open-sole:pdp-sock-math=Shop now | **keep** | content; set in 2/5 |
| `cta_link_target` | select | #variants | Save-only | **3/5** collection:pdp-sock-math=#grid; product.in-studio-template:pdp-sock-math=custom; product.open-sole:pdp-sock-math=custom | **keep** | in use: non-default in 3/5 |
| `cta_url` | text | — | yes (content re-render) | **2/5** product.in-studio-template:pdp-sock-math=#buy; product.open-sole:pdp-sock-math=#buy | **keep** | content; set in 2/5 |
| `show_trust_strip` | checkbox | false | Save-only | **2/5** product.in-studio-template:pdp-sock-math=true; product.open-sole:pdp-sock-math=true | **keep** | in use: non-default in 2/5 |
| `trust_text` | text | — | yes (content re-render) | **2/5** product.in-studio-template:pdp-sock-math=Instructor trusted; product.open-sole:pdp-sock-math=Instructor trusted | **keep** | content; set in 2/5 |
| `layout` | select | compact | Save-only | **5/5** collection:pdp-sock-math=editorial; page.best-grippy-socks:pdp-sock-math=editorial; product.in-studio-template:pdp-sock-math=editorial +2 more · values: editorial×5 | **keep** | in use: non-default in 5/5 |
| `show_prices` | checkbox | true | Save-only | **1/5** collection:pdp-sock-math=false | **keep** | in use: non-default in 1/5 |
| `image` | image_picker | — | yes (content re-render) | **3/5** collection:pdp-sock-math=shopify://shop_images/te-pick-ig-real-…; product.in-studio-template:pdp-sock-math=shopify://shop_images/50072453_2448236…; product.open-sole:pdp-sock-math=shopify://shop_images/50072453_2448236… | **keep** | content; set in 3/5 |
| `image_url` | text | — | yes (content re-render) | **5/5** collection:pdp-sock-math=https://www.juicer.io/api/media/598644…; page.best-grippy-socks:pdp-sock-math=https://www.juicer.io/api/media/598644…; product.in-studio-template:pdp-sock-math=https://cdn.shopify.com/s/files/1/0045… +2 more · values: https://www.juicer.io/api/media/598644…×3, https://cdn.shopify.com/s/files/1/0045…×2 | **keep** | content; set in 5/5 |
| `image_alt` | text | — | yes (content re-render) | **5/5** collection:pdp-sock-math=Outdoor class; page.best-grippy-socks:pdp-sock-math=Outdoor class; product.in-studio-template:pdp-sock-math=Putting on Open Sole +2 more · values: Outdoor class×3, Putting on Open Sole×2 | **keep** | content; set in 5/5 |
| `image_crop` | select | center center | Save-only | default (5) | **remove** | default in all 5 instance(s); hardcode default |
| `image_frame` | range | 480 | Save-only | **1/5** collection:pdp-sock-math=560 | **keep** | in use: non-default in 1/5 |
| `image_frame_mobile` | range | 360 | Save-only | **2/5** collection:pdp-sock-math=560; product.in-studio-template:pdp-sock-math=0 | **keep** | in use: non-default in 2/5 |
| `image_unframed` | checkbox | false | Save-only | **2/5** product.in-studio-template:pdp-sock-math=true; product.open-sole:pdp-sock-math=true | **keep** | in use: non-default in 2/5 |
| `pad_top` | range | 0 | Save-only | **3/5** collection:pdp-sock-math=32; product.in-studio-template:pdp-sock-math=80; product.open-sole:pdp-sock-math=80 | **keep** | in use: non-default in 3/5 |
| `pad_bottom` | range | 0 | Save-only | **3/5** collection:pdp-sock-math=64; product.in-studio-template:pdp-sock-math=80; product.open-sole:pdp-sock-math=80 | **keep** | in use: non-default in 3/5 |
| `quote` | textarea | — | yes (content re-render) | default (5) | **keep** | content |
| `quote_cite` | text | — | yes (content re-render) | default (5) | **keep** | content |
| `theirs_label` | text | Grip Socks | yes (content re-render) | **5/5** collection:pdp-sock-math=The cycle; page.best-grippy-socks:pdp-sock-math=The cycle; product.in-studio-template:pdp-sock-math=The sock cycle +2 more · values: The cycle×3, The sock cycle×2 | **keep** | content; set in 5/5 |
| `their_price` | text | $112–144 | yes (content re-render) | **5/5** collection:pdp-sock-math=$144–$336; page.best-grippy-socks:pdp-sock-math=$144–$336; product.in-studio-template:pdp-sock-math=$144–$336 +2 more · values: $144–$336×5 | **keep** | content; set in 5/5 |
| `theirs_1` | text | Replace every 6–8 weeks | yes (content re-render) | **5/5** collection:pdp-sock-math=Silicone never grips. Fabric stretches…; page.best-grippy-socks:pdp-sock-math=Silicone never grips. Fabric stretches…; product.in-studio-template:pdp-sock-math=Silicone never grips. Fabric stretches… +2 more · values: Silicone never grips. Fabric stretches…×5 | **keep** | content; set in 5/5 |
| `theirs_2` | text | Grip degrades with washing | yes (content re-render) | **5/5** collection:pdp-sock-math=; page.best-grippy-socks:pdp-sock-math=; product.in-studio-template:pdp-sock-math= +2 more · values: ×5 | **keep** | content; set in 5/5 |
| `theirs_3` | text | 6–8 pairs per year minimum | yes (content re-render) | **5/5** collection:pdp-sock-math=; page.best-grippy-socks:pdp-sock-math=; product.in-studio-template:pdp-sock-math= +2 more · values: ×5 | **keep** | content; set in 5/5 |
| `ours_label` | text | Barreletics | yes (content re-render) | **5/5** collection:pdp-sock-math=The pair; page.best-grippy-socks:pdp-sock-math=The pair; product.in-studio-template:pdp-sock-math=The pair +2 more · values: The pair×5 | **keep** | content; set in 5/5 |
| `our_price` | text | $74 | yes (content re-render) | default (5) | **keep** | content |
| `ours_1` | text | 1,000 classes. Year four. | yes (content re-render) | **5/5** collection:pdp-sock-math=360° grip; page.best-grippy-socks:pdp-sock-math=360° grip; product.in-studio-template:pdp-sock-math=360° grip +2 more · values: 360° grip×5 | **keep** | content; set in 5/5 |
| `ours_2` | text | Grip never degrades | yes (content re-render) | **5/5** collection:pdp-sock-math=Secure in every hold.; page.best-grippy-socks:pdp-sock-math=Secure in every hold.; product.in-studio-template:pdp-sock-math=Secure in every hold. +2 more · values: Secure in every hold.×5 | **keep** | content; set in 5/5 |
| `ours_3` | text | One pair, every class | yes (content re-render) | **5/5** collection:pdp-sock-math=; page.best-grippy-socks:pdp-sock-math=; product.in-studio-template:pdp-sock-math= +2 more · values: ×5 | **keep** | content; set in 5/5 |
| `aria_label` | text | Cost comparison | yes (content re-render) | default (5) | **keep** | content |

### `pdp-sticky-atc` — "Sticky Add to Cart"
Instances: 9 in 9 file(s): product, product.coperni, product.in-studio-template, product.one-off-closed, product.one-off-open, product.open-sole, product.outdoor, product.v-neck-tops … · keep 1 / remove 2 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `hero_image_mode` | select | admin_order | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `hero_color` | text | — | yes (content re-render) | default (9) | **keep** | content |
| `hero_media_index` | range | 1 | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |

### `press-cards` — "Press cards"
Instances: 1 in 1 file(s): index · keep 19 / remove 8 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | PRESS | yes (content re-render) | **1/1** index:press-home=Press (disabled) | **keep** | content; set in 1/1 |
| `bg_color` | color | #faf8f6 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `columns_desktop` | range | 3 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `columns_mobile` | select | 1 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `gap` | range | 16 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `card_radius` | range | 0 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `padding_y` | range | 48 | Save-only | **1/1** index:press-home=40 (disabled) | **keep** | in use: non-default in 1/1 |
| `padding_x` | range | 40 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_ratio` | select | 4 / 5 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `video_mode` | select | autoplay | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `card.media_type` | select | image | Save-only | **1/3** index:press-home=video (disabled) | **keep** | in use: non-default in 1/3 |
| `card.image_fit` | select | cover | Save-only | **2/3** index:press-home=contain (disabled); index:press-home=contain (disabled) | **keep** | in use: non-default in 2/3 |
| `card.image` | image_picker | — | yes (content re-render) | **2/3** index:press-home=shopify://shop_images/Interni_Blog_Mag… (disabled); index:press-home=shopify://shop_images/Interni_Blog_Mag… (disabled) | **keep** | content; set in 2/3 |
| `card.image_url` | text | — | yes (content re-render) | **1/3** index:press-home=https://cdn.shopify.com/s/files/1/0045… (disabled) | **keep** | content; set in 1/3 |
| `card.video` | video | — | yes (content re-render) | **1/3** index:press-home=shopify://files/videos/Coperni 3.mov (disabled) | **keep** | content; set in 1/3 |
| `card.video_url` | text | — | yes (content re-render) | **1/3** index:press-home=https://barreletics.com/cdn/shop/video… (disabled) | **keep** | content; set in 1/3 |
| `card.poster` | image_picker | — | yes (content re-render) | default (3) | **keep** | content |
| `card.poster_url` | text | — | yes (content re-render) | **1/3** index:press-home=https://barreletics.com/cdn/shop/files… (disabled) | **keep** | content; set in 1/3 |
| `card.eyebrow` | text | — | yes (content re-render) | default (3) | **keep** | content |
| `card.title` | text | — | yes (content re-render) | **3/3** index:press-home=Coperni (disabled); index:press-home=INTERNI (disabled); index:press-home=ITSLIQUID · Venice (disabled) | **keep** | content; set in 3/3 |
| `card.caption` | textarea | — | yes (content re-render) | **3/3** index:press-home=Paris Fashion Week (disabled); index:press-home=Sano come un piede (disabled); index:press-home=Biennale arte 2026 (disabled) | **keep** | content; set in 3/3 |
| `card.link` | url | — | yes (content re-render) | **3/3** index:press-home=https://barreletics.com/products/barre… (disabled); index:press-home=/blogs/news/barreletics-in-interni (disabled); index:press-home=/blogs/news (disabled) | **keep** | content; set in 3/3 |
| `card.link_label` | text | — | yes (content re-render) | default (3) | **keep** | content |
| `card.hide_on_desktop` | checkbox | false | Save-only | default (3) | **keep** | visibility switch; never used but cheap |
| `card.hide_on_mobile` | checkbox | false | Save-only | default (3) | **keep** | visibility switch; never used but cheap |

### `press-feature` — "Twin frame"
Instances: 3 in 3 file(s): index, product.v-neck-tops, product.yoga-pants · keep 18 / remove 12 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `aria_label` | text | Product in use | yes (content re-render) | default (3) | **keep** | content |
| `desktop_height` | range | 520 | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `mobile_height` | range | 280 | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `bg_color` | color | #faf8f6 | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `caption_bg` | color | #faf8f6 | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_1_type` | select | image | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_1_image` | image_picker | — | yes (content re-render) | **3/3** index:press-feature-interni=shopify://shop_images/Stef-_Yulia_Chat…; product.v-neck-tops:press_feature_m9tTbA=shopify://shop_images/Home-hero-Stef-2…; product.yoga-pants:press_feature_m9tTbA=shopify://shop_images/Home-hero-Stef-2… | **keep** | content; set in 3/3 |
| `media_1_image_url` | text | — | yes (content re-render) | **1/3** index:press-feature-interni=https://cdn.shopify.com/s/files/1/0045… | **keep** | content; set in 1/3 |
| `media_1_video` | video | — | yes (content re-render) | **2/3** product.v-neck-tops:press_feature_m9tTbA=shopify://files/videos/clip03-1080x144…; product.yoga-pants:press_feature_m9tTbA=shopify://files/videos/clip03-1080x144… | **keep** | content; set in 2/3 |
| `media_1_video_url` | text | — | yes (content re-render) | default (3) | **keep** | content |
| `media_1_alt` | text | — | yes (content re-render) | **1/3** index:press-feature-interni=Barreletics in use | **keep** | content; set in 1/3 |
| `media_1_fit` | select | cover | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_1_position` | select | center | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_1_fit_mobile` | select | cover | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_1_position_mobile` | select | center | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_2_type` | select | image | Save-only | **3/3** index:press-feature-interni=video; product.v-neck-tops:press_feature_m9tTbA=video; product.yoga-pants:press_feature_m9tTbA=video | **keep** | in use: non-default in 3/3 |
| `media_2_image` | image_picker | — | yes (content re-render) | **1/3** index:press-feature-interni=shopify://shop_images/IMG_9841.jpg | **keep** | content; set in 1/3 |
| `media_2_image_url` | text | — | yes (content re-render) | default (3) | **keep** | content |
| `media_2_video` | video | — | yes (content re-render) | **2/3** product.v-neck-tops:press_feature_m9tTbA=shopify://files/videos/FCEC6774-C786-4…; product.yoga-pants:press_feature_m9tTbA=shopify://files/videos/FCEC6774-C786-4… | **keep** | content; set in 2/3 |
| `media_2_video_url` | text | — | yes (content re-render) | default (3) | **keep** | content |
| `media_2_alt` | text | — | yes (content re-render) | **1/3** index:press-feature-interni=Barreletics in use | **keep** | content; set in 1/3 |
| `media_2_fit` | select | cover | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_2_position` | select | center | Save-only | **2/3** product.v-neck-tops:press_feature_m9tTbA=bottom; product.yoga-pants:press_feature_m9tTbA=bottom | **keep** | in use: non-default in 2/3 |
| `media_2_fit_mobile` | select | cover | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `media_2_position_mobile` | select | center | Save-only | default (3) | **remove** | default in all 3 instance(s); hardcode default |
| `eyebrow` | text | IN USE | yes (content re-render) | default (3) | **keep** | content |
| `title` | text | Built for the work. | yes (content re-render) | default (3) | **keep** | content |
| `body` | textarea | — | yes (content re-render) | default (3) | **keep** | content |
| `hide_on_mobile` | checkbox | false | Save-only | default (3) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (3) | **keep** | visibility switch; never used but cheap |

### `press-row` — "Press row"
Instances: 2 in 2 file(s): index, page.press · keep 21 / remove 9 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | Press | yes (content re-render) | default (2) | **keep** | content |
| `heading_style` | select | eyebrow | Save-only | **1/2** page.press:press-row=standard | **keep** | in use: non-default in 1/2 |
| `desktop_height` | range | 620 | yes ({% style %}) | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `bg_color` | color | #faf8f6 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `video` | video | — | yes (content re-render) | **2/2** index:press-row=shopify://files/videos/Coperni 3.mov; page.press:press-row=shopify://files/videos/Coperni 3.mov | **keep** | content; set in 2/2 |
| `video_url` | text | — | yes (content re-render) | default (2) | **keep** | content |
| `poster` | image_picker | — | yes (content re-render) | default (2) | **keep** | content |
| `poster_url` | text | https://barreletics.com/cdn/shop/files… | yes (content re-render) | default (2) | **keep** | content |
| `hero_label` | text | Barreletics × Coperni | yes (content re-render) | default (2) | **keep** | content |
| `hero_line` | text | Limited edition · Paris 2026 | yes (content re-render) | default (2) | **keep** | content |
| `mobile_layout` | select | stack | Save-only | **2/2** index:press-row=grid; page.press:press-row=grid | **keep** | in use: non-default in 2/2 |
| `hide_on_mobile` | checkbox | false | Save-only | default (2) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (2) | **keep** | visibility switch; never used but cheap |
| `show_mentions` | checkbox | true | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mentions_hide_mobile` | checkbox | false | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mentions_style_desktop` | select | caps | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mentions_style_mobile` | select | sentence | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mentions_name_size` | select | 16 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mentions_lead` | text | Also featured in | yes (content re-render) | default (2) | **keep** | content |
| `mentions_items` | text | Free People, Anthropologie (Fall 2026) | yes (content re-render) | default (2) | **keep** | content |
| `card.image` | image_picker | — | yes (content re-render) | **4/8** index:press-row=shopify://shop_images/Screenshot_2026-…; index:press-row=shopify://shop_images/Interni_Layout_C…; page.press:press-row=shopify://shop_images/Screenshot_2026-… +1 more · values: shopify://shop_images/Screenshot_2026-…×2, shopify://shop_images/Interni_Layout_C…×2 | **keep** | content; set in 4/8 |
| `card.image_url` | text | — | yes (content re-render) | **4/8** index:press-row=https://barreletics.com/cdn/shop/files…; index:press-row=https://cdn.shopify.com/s/files/1/0045…; page.press:press-row=https://cdn.shopify.com/s/files/1/0045… +1 more · values: https://barreletics.com/cdn/shop/files…×2, https://cdn.shopify.com/s/files/1/0045…×2 | **keep** | content; set in 4/8 |
| `card.title` | text | Press | yes (content re-render) | **8/8** index:press-row=Runway; index:press-row=Collaboration; index:press-row=INTERNI +5 more · values: Runway×2, Collaboration×2, INTERNI×2, Venice · Biennale Arte 2026×2 | **keep** | content; set in 8/8 |
| `card.caption` | text | — | yes (content re-render) | **8/8** index:press-row=Paris Fashion Week; index:press-row=Spring–Summer 2026; index:press-row=Sano come un piede +5 more · values: Paris Fashion Week×2, Spring–Summer 2026×2, Sano come un piede×2, ITSLIQUID×2 | **keep** | content; set in 8/8 |
| `card.link` | url | — | yes (content re-render) | **8/8** index:press-row=https://barreletics.com/products/barre…; index:press-row=/pages/collaborations; index:press-row=https://barreletics.com/blogs/news/bar… +5 more · values: https://barreletics.com/products/barre…×2, /pages/collaborations×2, https://barreletics.com/blogs/news/bar…×2, /blogs/news/barreletics-venice-biennal…×2 | **keep** | content; set in 8/8 |
| `card.media_fit` | select | cover | Save-only | default (8) | **remove** | default in all 8 instance(s); hardcode default |
| `card.media_position` | select | center | Save-only | **2/8** index:press-row=top; page.press:press-row=top | **keep** | in use: non-default in 2/8 |
| `card.placeholder_gradient` | checkbox | false | Save-only | default (8) | **remove** | default in all 8 instance(s); hardcode default |
| `card.hide_on_desktop` | checkbox | false | Save-only | default (8) | **keep** | visibility switch; never used but cheap |
| `card.hide_on_mobile` | checkbox | false | Save-only | default (8) | **keep** | visibility switch; never used but cheap |

### `problem-section` — "Problem section"
Instances: 1 in 1 file(s): index · keep 14 / remove 17 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Never slip in Chair Pose | yes (content re-render) | default (1) | **keep** | content |
| `heading_size_override` | number | — | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `body` | textarea | Never slip again in side plank or flat… | yes (content re-render) | default (1) | **keep** | content |
| `cta_text` | text | Shop Now | yes (content re-render) | default (1) | **keep** | content |
| `cta_style` | select | solid | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_bg_color` | color | #c45c3f | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_border_color` | color | #c45c3f | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_text_color` | color | #ffffff | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_url` | url | — | yes (content re-render) | default (1) | **keep** | content |
| `video` | video | — | yes (content re-render) | **1/1** index:problem-section=shopify://files/videos/clip01-1080x144… | **keep** | content; set in 1/1 |
| `video_url` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `video_asset` | text | — | yes (content re-render) | **1/1** index:problem-section=chair-pose-home.mp4 | **keep** | content; set in 1/1 |
| `image` | image_picker | — | yes (content re-render) | default (1) | **keep** | content |
| `mobile_media_height` | range | 520 | Save-only | **1/1** index:problem-section=600 | **keep** | in use: non-default in 1/1 |
| `media_fit` | select | cover | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_fit_mobile` | select | cover | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `desktop_split` | select | 50_50 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `min_height` | range | 860 | yes ({% style %}) | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_aspect` | select | stretch | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_aspect_mobile` | select | stretch | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `bg_preset` | select | custom | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `bg_color` | color | #faf8f6 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_bg_preset` | select | custom | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_bg` | color | #ffffff | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `reverse` | checkbox | false | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `mobile_stack_order` | select | media_first | Save-only | **1/1** index:problem-section=copy_first | **keep** | in use: non-default in 1/1 |
| `copy_stack_gap` | range | 12 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `anchor_id` | text | problem | yes (content re-render) | default (1) | **keep** | content |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `item.text` | text | Grip socks that peel, stretch out, and… | yes (content re-render) | **3/4** index:problem-section=Flat back chair & water ski — resettin…; index:problem-section=Reformer footwork — adjusting between …; index:problem-section=Deep lunges on barre, reformer & Megaf… | **keep** | content; set in 3/4 |

### `proof-numbers` 🔒 locked — "Proof numbers"
Instances: 1 in 1 file(s): index · keep 9 / remove 10 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `enabled` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `anchor_id` | text | numbers | yes (content re-render) | default (1) | **keep** | content |
| `aria_label` | text | Proof in numbers | yes (content re-render) | default (1) | **keep** | content |
| `eyebrow` | text | Proof | yes (content re-render) | default (1) | **keep** | content |
| `title` | text | Built for the ones who show up. | yes (content re-render) | default (1) | **keep** | content |
| `heading_size_override` | number | — | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `tone` | select | white | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (1) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `stat.stat` | text | 1,000's | yes (content re-render) | **2/3** index:proof-numbers=1,000+; index:proof-numbers=USA | **keep** | content; set in 2/3 |
| `stat.label` | text | Instructors & studios | yes (content re-render) | **2/3** index:proof-numbers=Classes on one pair; index:proof-numbers=Made in USA | **keep** | content; set in 2/3 |
| `stat.detail` | text | — | yes (content re-render) | **3/3** index:proof-numbers=Trusted in real class rooms; index:proof-numbers=One customer. One pair.; index:proof-numbers=No latex. No silicone. | **keep** | content; set in 3/3 |

### `recently-viewed` — "Recently Viewed"
Instances: 0 in 0 file(s) (unused) · keep 0 / remove 1 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | Recently Viewed | yes (content re-render) | no instances | **remove** | section not placed in any template/group |

### `recommendations` — "Product Recommendations"
Instances: 1 in 1 file(s): cart · keep 1 / remove 1 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `heading` | text | You may also like | yes (content re-render) | default (1) | **keep** | content |
| `limit` | range | 4 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |

### `sale-banner` — "Sale banner"
Instances: 1 in 1 file(s): sections/header-group · keep 3 / remove 7 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `enabled` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_on_desktop` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_on_mobile` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `text` | text | Buy 2 save 10% \| Use SAVE2 | yes (content re-render) | default (1) | **keep** | content |
| `link_url` | url | — | yes (content re-render) | default (1) | **keep** | content |
| `bg_color` | color | #faf8f6 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `text_color` | color | #1c1916 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `font_weight` | select | 500 | Save-only | **1/1** sections/header-group:sale_banner=400 | **keep** | in use: non-default in 1/1 |
| `font_size` | range | 15 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `pad_y` | range | 10 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |

### `search-results` — "Search Results"
Instances: 1 in 1 file(s): search · keep 0 / remove 0 / merge 0

_No settings._

### `sole-cards` — "Sole cards"
Instances: 0 in 0 file(s) (unused) · keep 0 / remove 15 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `bg_color` | color | #ffffff | Save-only | no instances | **remove** | section not placed in any template/group |
| `image_scale` | range | 100 | Save-only | no instances | **remove** | section not placed in any template/group |
| `image_frame` | range | 400 | Save-only | no instances | **remove** | section not placed in any template/group |
| `image_pad` | range | 0 | Save-only | no instances | **remove** | section not placed in any template/group |
| `section_pad` | range | 24 | Save-only | no instances | **remove** | section not placed in any template/group |
| `card_padding` | range | 28 | Save-only | no instances | **remove** | section not placed in any template/group |
| `aria_label` | text | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `closed_image` | image_picker | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `closed_url` | url | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `closed_best_for` | text | you want heel and foot fully covered. | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `closed_desc` | textarea | Heel and foot fully covered. 360° grip… | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `open_image` | image_picker | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `open_url` | url | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `open_best_for` | text | you want a more grounded, barefoot fee… | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `open_desc` | textarea | Heel exposed, mid-foot breathing hole.… | yes (content re-render) | no instances | **remove** | section not placed in any template/group |

### `split-hero` — "Split hero"
Instances: 1 in 1 file(s): index · keep 18 / remove 39 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | The Pilates Sock Era is Over | yes (content re-render) | default (1) | **keep** | content |
| `heading_level` | select | h1 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `title_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `body` | richtext | <p>Outperforms barre socks, Pilates so… | yes (content re-render) | default (1) | **keep** | content |
| `body_size` | select | default | Save-only | **1/1** index:split_hero=16 | **keep** | in use: non-default in 1/1 |
| `body_weight` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_text` | text | Shop Now | yes (content re-render) | default (1) | **keep** | content |
| `cta_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_style` | select | solid | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_bg_color` | color | #c45c3f | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_border_color` | color | #c45c3f | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_text_color` | color | #ffffff | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_link_target` | select | #variants | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `cta_url` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `tag_text` | text | #letusknockyoursocksoff | yes (content re-render) | default (1) | **keep** | content |
| `tag_link_target` | select | #knock-socks | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `tag_url` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `media_type` | select | image | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `video` | video | — | yes (content re-render) | default (1) | **keep** | content |
| `video_url` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `image` | image_picker | — | yes (content re-render) | **1/1** index:split_hero=shopify://shop_images/barreletixx_stef… | **keep** | content; set in 1/1 |
| `image_url` | text | https://barreletics.com/cdn/shop/produ… | yes (content re-render) | default (1) | **keep** | content |
| `image_alt` | text | Barreletics Performance Skins — grip t… | yes (content re-render) | default (1) | **keep** | content |
| `video_controls` | checkbox | false | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_pos_x` | range | 50 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_pos_y` | range | 50 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_zoom` | range | 100 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_pos_x_mobile` | range | 50 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_pos_y_mobile` | range | 50 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `image_zoom_mobile` | range | 100 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_height` | range | 100 | yes ({% style %}) | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `media_column_pct` | range | 62 | Save-only | **1/1** index:split_hero=50 | **keep** | in use: non-default in 1/1 |
| `media_radius` | range | 0 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `bg_color` | color | #ffffff | yes ({% style %}) | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `reverse_layout` | checkbox | false | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `mobile_stack_order` | select | media_first | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_trust` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `show_stars` | checkbox | true | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `star_color` | color | #d4af37 | n/a (unused in code) | **1/1** index:split_hero=#c45c3f | **remove** | dead: not read by any Liquid; migration: 1 saved value(s) have no effect, drop keys |
| `star_size` | range | 14 | n/a (unused in code) | default (1) | **remove** | dead: not read by any Liquid |
| `trust_text_size` | select | default | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `trust_gap` | range | 10 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `trust_below` | range | 16 | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `trust_text` | richtext | <p>Trusted by 1,000's of instructors &… | yes (content re-render) | default (1) | **keep** | content |
| `trust_link_target` | select | #reviews | Save-only | default (1) | **remove** | default in all 1 instance(s); hardcode default |
| `trust_url` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `aria_label` | text | — | yes (content re-render) | default (1) | **keep** | content |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (1) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (1) | **remove** | shared inset never changed in 1 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (1) | **keep** | visibility switch; never used but cheap |

### `statement-band` — "Statement band"
Instances: 4 in 4 file(s): collection, index, product.in-studio-template, product.open-sole · keep 10 / remove 17 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `eyebrow` | text | — | yes (content re-render) | default (4) | **keep** | content |
| `title` | text | Let us knock your socks off | yes (content re-render) | **1/4** collection:knock-socks=Let us knock your socks off! | **keep** | content; set in 1/4 |
| `heading_size_override` | number | — | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `title_role` | select | statement | n/a (unused in code) | **4/4** collection:knock-socks=display; index:statement-band=display; product.in-studio-template:knock-socks=display +1 more · values: display×4 | **remove** | dead: not read by any Liquid; migration: 4 saved value(s) have no effect, drop keys |
| `title_size` | select | default | n/a (unused in code) | default (4) | **remove** | dead: not read by any Liquid |
| `title_weight` | select | default | n/a (unused in code) | **3/4** collection:knock-socks=400; product.in-studio-template:knock-socks=400; product.open-sole:knock-socks=400 | **remove** | dead: not read by any Liquid; migration: 3 saved value(s) have no effect, drop keys |
| `subhead` | text | Safely push harder in every studio move. | yes (content re-render) | default (4) | **keep** | content |
| `body_size` | select | default | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `bg_color` | color | #faf8f6 | Save-only | **1/4** index:statement-band=#ffffff | **keep** | in use: non-default in 1/4 |
| `cta_text` | text | Shop Now | yes (content re-render) | **2/4** product.in-studio-template:knock-socks=Shop now; product.open-sole:knock-socks=Shop now | **keep** | content; set in 2/4 |
| `cta_style` | select | solid | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `cta_bg_color` | color | #1c1916 | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `cta_border_color` | color | #1c1916 | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `cta_text_color` | color | #ffffff | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `cta_link_target` | select | custom | Save-only | default (4) | **remove** | default in all 4 instance(s); hardcode default |
| `cta_url` | text | — | yes (content re-render) | **3/4** collection:knock-socks=#grid; product.in-studio-template:knock-socks=#buy; product.open-sole:knock-socks=#buy | **keep** | content; set in 3/4 |
| `anchor_id` | text | knock-socks | yes (content re-render) | default (4) | **keep** | content |
| `aria_label` | text | — | yes (content re-render) | default (4) | **keep** | content |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (4) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (4) | **remove** | shared inset never changed in 4 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (4) | **remove** | shared inset never changed in 4 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (4) | **remove** | shared inset never changed in 4 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (4) | **remove** | shared inset never changed in 4 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (4) | **remove** | shared inset never changed in 4 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (4) | **remove** | shared inset never changed in 4 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (4) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (4) | **keep** | visibility switch; never used but cheap |

### `studio-trust` — "Studio trust"
Instances: 0 in 0 file(s) (unused) · keep 0 / remove 4 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `title` | text | Trusted by 1,000's of instructors & st… | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `subhead` | textarea | Dig into deep lunges and every positio… | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `geo_item.question` | text | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |
| `geo_item.answer` | richtext | — | yes (content re-render) | no instances | **remove** | section not placed in any template/group |

### `value-strip` 🔒 locked — "Value Strip"
Instances: 18 in 18 file(s): collection.apparel, collection.closed-sole, collection.hot-kits, collection.limited-editions, collection.new-arrivals, collection.one-offs, collection.open-sole, collection.outdoor … · keep 6 / remove 9 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `aria_label` | text | Value propositions | yes (content re-render) | **4/18** collection.apparel:value-strip=Product benefits; page.best-grippy-socks:value-strip=Product benefits; product.v-neck-tops:value-strip=Product benefits +1 more · values: Product benefits×4 | **keep** | content; set in 4/18 |
| `bg_color` | color | #faf8f6 | Save-only | default (18) | **remove** | default in all 18 instance(s); hardcode default |
| `padding_y` | range | 28 | Save-only | **4/18** collection.apparel:value-strip=20; page.best-grippy-socks:value-strip=20; product.v-neck-tops:value-strip=20 +1 more · values: 20×4 | **keep** | in use: non-default in 4/18 |
| `padding_y_mobile` | range | 24 | Save-only | **4/18** collection.apparel:value-strip=16; page.best-grippy-socks:value-strip=16; product.v-neck-tops:value-strip=16 +1 more · values: 16×4 | **keep** | in use: non-default in 4/18 |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | default (18) | **remove** | dead: not read by any Liquid |
| `inset_top` | range | 0 | Save-only (snippet) | default (18) | **remove** | shared inset never changed in 18 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (18) | **remove** | shared inset never changed in 18 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (18) | **remove** | shared inset never changed in 18 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (18) | **remove** | shared inset never changed in 18 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (18) | **remove** | shared inset never changed in 18 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (18) | **remove** | shared inset never changed in 18 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | **2/18** product.in-studio-template:value-strip=true; product.open-sole:value-strip=true | **keep** | in use: non-default in 2/18 |
| `hide_on_desktop` | checkbox | false | Save-only | **2/18** product.in-studio-template:value-strip=true; product.open-sole:value-strip=true | **keep** | in use: non-default in 2/18 |
| `item.text` | text | Made in USA | yes (content re-render) | **30/40** collection.apparel:value-strip=Free exchanges; collection.apparel:value-strip=30-day returns; collection.apparel:value-strip=Doesn't pill +27 more · values: 30-day returns×10, 90-day warranty×7, Free shipping over $150×6, Free exchanges×4 | **keep** | content; set in 30/40 |
| `item.show_on_mobile` | checkbox | true | Save-only | default (40) | **remove** | default in all 40 instance(s); hardcode default |

### `variant-grid` — "Variant Grid"
Instances: 22 in 22 file(s): collection, collection.apparel, collection.closed-sole, collection.gift-cards, collection.limited-editions, collection.new-arrivals, collection.one-offs, collection.open-sole … · keep 27 / remove 16 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `bg_color` | color | — | Save-only | **5/22** collection:variant-grid=#ffffff; index:variant-grid=#ffffff; page.best-grippy-socks:variant-grid=#ffffff +2 more · values: #ffffff×5 | **keep** | in use: non-default in 5/22 |
| `eyebrow` | text | Two versions. One performance. | yes (content re-render) | **22/22** collection.apparel:variant-grid=Shop the range; collection.closed-sole:variant-grid=Closed Sole Collection; collection.gift-cards:variant-grid=Gift Cards +19 more · values: ×11, Shop the range×3, Closed Sole Collection×1, Gift Cards×1 | **keep** | content; set in 22/22 |
| `title` | text | Shop all colors & styles | yes (content re-render) | **12/22** collection.apparel:variant-grid=Shop All Styles & Colors; collection.closed-sole:variant-grid=Every Closed Sole Style; collection.gift-cards:variant-grid=Choose an Amount +9 more · values: ×5, Shop All Styles & Colors×3, Every Closed Sole Style×1, Choose an Amount×1 | **keep** | content; set in 12/22 |
| `title_size` | select | default | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `title_weight` | select | default | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `body` | textarea | Grip shoes for Barre, Pilates, Yoga—se… | yes (content re-render) | **21/22** collection.apparel:variant-grid=Reinforced-knee yoga pants and perform…; collection.closed-sole:variant-grid=Full-wrap coverage with 360° grip. Cho…; collection.gift-cards:variant-grid=Delivered instantly via email. Never e… +18 more · values: Grip shoes for Barre, Pilates, Yoga—Se…×6, Reinforced-knee yoga pants and perform…×3, Grip shoes for barre, Pilates, and yog…×2, Full-wrap coverage with 360° grip. Cho…×1 | **keep** | content; set in 21/22 |
| `body_size` | select | default | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `use_current_product` | checkbox | false | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `card_messaging` | select | meta | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `show_closed` | checkbox | true | Save-only | **4/22** collection.one-offs:variant-grid=false; collection.open-sole:variant-grid=false; collection.outdoor:variant-grid=false +1 more · values: false×4 | **keep** | in use: non-default in 4/22 |
| `label_closed` | text | Closed Sole | yes (content re-render) | **3/22** collection.apparel:variant-grid=Yoga Pants; product.v-neck-tops:variant-grid=Yoga Pants; product.yoga-pants:variant-grid=Yoga Pants | **keep** | content; set in 3/22 |
| `product_closed` | product | — | yes (content re-render) | **15/22** collection.apparel:variant-grid=lightly-padded-knee-yoga-pant-black; collection.closed-sole:variant-grid=best-reformer-pilates-legree-workout-s…; collection:variant-grid=best-reformer-pilates-legree-workout-s… +12 more · values: best-reformer-pilates-legree-workout-s…×12, lightly-padded-knee-yoga-pant-black×3 | **keep** | content; set in 15/22 |
| `show_open` | checkbox | true | Save-only | **4/22** collection.closed-sole:variant-grid=false; collection.one-offs:variant-grid=false; collection.outdoor:variant-grid=false +1 more · values: false×4 | **keep** | in use: non-default in 4/22 |
| `label_open` | text | Open Sole | yes (content re-render) | **3/22** collection.apparel:variant-grid=T-Shirts; product.v-neck-tops:variant-grid=T-Shirts; product.yoga-pants:variant-grid=T-Shirts | **keep** | content; set in 3/22 |
| `product_open` | product | — | yes (content re-render) | **15/22** collection.apparel:variant-grid=barreletics-performance-fabric-yoga-t-…; collection:variant-grid=studio-performance-skin-footwear; collection.open-sole:variant-grid=studio-performance-skin-footwear +12 more · values: studio-performance-skin-footwear×12, barreletics-performance-fabric-yoga-t-…×3 | **keep** | content; set in 15/22 |
| `show_oneoffs` | checkbox | true | Save-only | **17/22** collection.apparel:variant-grid=false; collection.closed-sole:variant-grid=false; collection:variant-grid=false +14 more · values: false×17 | **keep** | in use: non-default in 17/22 |
| `label_oneoffs` | text | One-Offs | yes (content re-render) | default (22) | **keep** | content |
| `product_oneoffs` | product | — | yes (content re-render) | **11/22** collection:variant-grid=one-off-colors-closed-sole; collection.one-offs:variant-grid=barreletics-x-coperni-closed-sole; index:variant-grid=one-off-colors-closed-sole +8 more · values: one-off-colors-closed-sole×8, barreletics-x-coperni-closed-sole×2, one-off-colors-open-sole×1 | **keep** | content; set in 11/22 |
| `show_outdoor` | checkbox | true | Save-only | **16/22** collection.apparel:variant-grid=false; collection.closed-sole:variant-grid=false; collection:variant-grid=false +13 more · values: false×16 | **keep** | in use: non-default in 16/22 |
| `label_outdoor` | text | Outdoor | yes (content re-render) | default (22) | **keep** | content |
| `product_outdoor` | product | — | yes (content re-render) | **11/22** collection:variant-grid=aquatic-performance-skins; collection.outdoor:variant-grid=aquatic-performance-skins; index:variant-grid=aquatic-performance-skins +8 more · values: aquatic-performance-skins×11 | **keep** | content; set in 11/22 |
| `show_all_tab` | checkbox | false | Save-only | **2/22** collection:variant-grid=true; page.best-grippy-socks:variant-grid=true | **keep** | in use: non-default in 2/22 |
| `default_tab` | select | closed | Save-only | **11/22** collection:variant-grid=all; collection.one-offs:variant-grid=oneoffs; collection.open-sole:variant-grid=open +8 more · values: open×6, all×2, outdoor×2, oneoffs×1 | **keep** | in use: non-default in 11/22 |
| `initial_rows` | range | 2 | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `see_all` | select | expand | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `see_all_label` | text | See all colors & styles | yes (content re-render) | **5/22** collection.apparel:variant-grid=See all styles; collection:variant-grid=See more; page.best-grippy-socks:variant-grid=See more +2 more · values: See all styles×3, See more×2 | **keep** | content; set in 5/22 |
| `see_all_url` | url | — | yes (content re-render) | default (22) | **keep** | content |
| `max_variants` | range | 48 | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `anchor_id` | text | variants | yes (content re-render) | **5/22** collection.apparel:variant-grid=shop; collection:variant-grid=grid; page.best-grippy-socks:variant-grid=grid +2 more · values: shop×3, grid×2 | **keep** | content; set in 5/22 |
| `show_size_filter` | checkbox | true | Save-only | **3/22** collection.apparel:variant-grid=false; product.v-neck-tops:variant-grid=false; product.yoga-pants:variant-grid=false | **keep** | in use: non-default in 3/22 |
| `show_utility_links` | checkbox | true | Save-only | default (22) | **remove** | default in all 22 instance(s); hardcode default |
| `show_compare_link` | checkbox | true | Save-only | **3/22** collection.apparel:variant-grid=false; product.v-neck-tops:variant-grid=false; product.yoga-pants:variant-grid=false | **keep** | in use: non-default in 3/22 |
| `size_chart_url` | url | — | yes (content re-render) | **3/22** collection.apparel:variant-grid=/pages/yoga-pants-t-shirt-size-guide; product.v-neck-tops:variant-grid=/pages/yoga-pants-t-shirt-size-guide; product.yoga-pants:variant-grid=/pages/yoga-pants-t-shirt-size-guide | **keep** | content; set in 3/22 |
| `compare_url` | url | — | yes (content re-render) | default (22) | **keep** | content |
| `inset_custom_mobile` | checkbox | false | n/a (unused in code) | **1/22** product.coperni:variant-grid=true | **remove** | dead: not read by any Liquid; migration: 1 saved value(s) have no effect, drop keys |
| `inset_top` | range | 0 | Save-only (snippet) | default (22) | **remove** | shared inset never changed in 22 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (22) | **remove** | shared inset never changed in 22 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (22) | **remove** | shared inset never changed in 22 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (22) | **remove** | shared inset never changed in 22 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (22) | **remove** | shared inset never changed in 22 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (22) | **remove** | shared inset never changed in 22 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (22) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (22) | **keep** | visibility switch; never used but cheap |

### `visual-mosaic` — "Visual mosaic"
Instances: 2 in 2 file(s): collection, index · keep 25 / remove 25 / merge 0

| Setting | Type | Default | Live in TE | Used in draft (git @c0c0564) | Rec | Reason |
|---|---|---|---|---|---|---|
| `featured_layout` | select | working | Save-only | **1/2** index:visual-mosaic=featured_row | **keep** | in use: non-default in 1/2 |
| `show_overlay` | checkbox | true | Save-only | **2/2** collection:in-use-mosaic=false; index:visual-mosaic=false | **keep** | in use: non-default in 2/2 |
| `title_size` | select | default | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `title_size_mobile` | select | default | Save-only | **2/2** collection:in-use-mosaic=26; index:visual-mosaic=26 | **keep** | in use: non-default in 2/2 |
| `title_shadow` | checkbox | true | Save-only | **2/2** collection:in-use-mosaic=false; index:visual-mosaic=false | **keep** | in use: non-default in 2/2 |
| `tile_height` | range | 268 | Save-only | **2/2** collection:in-use-mosaic=380; index:visual-mosaic=296 | **keep** | in use: non-default in 2/2 |
| `grid_gap` | range | 12 | Save-only | **2/2** collection:in-use-mosaic=8; index:visual-mosaic=4 | **keep** | in use: non-default in 2/2 |
| `corner_radius` | range | 4 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `pad_top` | range | 16 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `pad_bottom` | range | 16 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `pad_x` | range | 16 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `default_link_target` | select | #variants | Save-only | **1/2** collection:in-use-mosaic=custom | **keep** | in use: non-default in 1/2 |
| `default_link_url` | text | — | yes (content re-render) | **1/2** collection:in-use-mosaic=#grid | **keep** | content; set in 1/2 |
| `aria_label` | text | Studio proof | yes (content re-render) | **1/2** collection:in-use-mosaic=Shoes in use | **keep** | content; set in 1/2 |
| `columns` | range | 3 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `media_fit` | select | cover | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `hero_column_wide` | checkbox | true | Save-only | **1/2** collection:in-use-mosaic=false | **keep** | in use: non-default in 1/2 |
| `mobile_columns` | select | 2 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mobile_hero_full_width` | checkbox | true | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mobile_hero_row_span` | range | 2 | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `aspect_ratio_mobile` | select | portrait | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `image_fit_mobile` | select | cover | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `video_fit_mobile` | select | cover | Save-only | default (2) | **remove** | default in all 2 instance(s); hardcode default |
| `mobile_tile_height` | range | 320 | Save-only | **2/2** collection:in-use-mosaic=264; index:visual-mosaic=264 | **keep** | in use: non-default in 2/2 |
| `inset_top` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_bottom` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_x` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_top_mobile` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_bottom_mobile` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `inset_x_mobile` | range | 0 | Save-only (snippet) | default (2) | **remove** | shared inset never changed in 2 instance(s); Save-only |
| `hide_on_mobile` | checkbox | false | Save-only | default (2) | **keep** | visibility switch; never used but cheap |
| `hide_on_desktop` | checkbox | false | Save-only | default (2) | **keep** | visibility switch; never used but cheap |
| `tile.title` | text | — | yes (content re-render) | **5/9** index:visual-mosaic=Secure in every hold; index:visual-mosaic=Durability; index:visual-mosaic=Balance +2 more · values: Secure in every hold×1, Durability×1, Balance×1, Breathability×1 | **keep** | content; set in 5/9 |
| `tile.cta_text` | text | — | yes (content re-render) | **1/9** index:visual-mosaic=Shop Now | **keep** | content; set in 1/9 |
| `tile.link_target` | select | default | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `tile.link_url` | text | — | yes (content re-render) | default (9) | **keep** | content |
| `tile.video` | video | — | yes (content re-render) | **2/9** collection:in-use-mosaic=shopify://files/videos/IMG_5897_00e51a…; index:visual-mosaic=shopify://files/videos/clip03-1080x144… | **keep** | content; set in 2/9 |
| `tile.video_url` | text | — | yes (content re-render) | default (9) | **keep** | content |
| `tile.image` | image_picker | — | yes (content re-render) | **8/9** collection:in-use-mosaic=shopify://shop_images/Lindsay_Reformer…; collection:in-use-mosaic=shopify://shop_images/InStudioPerforma…; collection:in-use-mosaic=shopify://shop_images/Copy_of_barrelet… +5 more · values: shopify://shop_images/InStudioPerforma…×2, shopify://shop_images/Copy_of_barrelet…×2, shopify://shop_images/Lindsay_Reformer…×1, shopify://shop_images/Square_Pink.png×1 | **keep** | content; set in 8/9 |
| `tile.poster_url` | text | — | yes (content re-render) | default (9) | **keep** | content |
| `tile.image_url` | text | — | yes (content re-render) | **4/9** index:visual-mosaic=https://barreletics.com/cdn/shop/files…; index:visual-mosaic=https://barreletics.com/cdn/shop/produ…; index:visual-mosaic=https://barreletics.com/cdn/shop/produ… +1 more · values: https://barreletics.com/cdn/shop/files…×2, https://barreletics.com/cdn/shop/produ…×2 | **keep** | content; set in 4/9 |
| `tile.alt` | text | Barreletics in studio | yes (content re-render) | **7/9** collection:in-use-mosaic=Performance Skins in studio; collection:in-use-mosaic=Performance Skins in class; collection:in-use-mosaic=Performance Skins in use +4 more · values: Performance Skins in studio×2, Performance Skins in class×1, Performance Skins in use×1, Durability×1 | **keep** | content; set in 7/9 |
| `tile.size` | select | sm | Save-only | **1/9** index:visual-mosaic=hero | **keep** | in use: non-default in 1/9 |
| `tile.size_mobile` | select | default | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `tile.hide_on_mobile` | checkbox | false | Save-only | **1/9** index:visual-mosaic=true | **keep** | in use: non-default in 1/9 |
| `tile.hide_on_desktop` | checkbox | false | Save-only | default (9) | **keep** | visibility switch; never used but cheap |
| `tile.column_span` | select | 1 | n/a (unused in code) | default (9) | **remove** | dead: not read by any Liquid |
| `tile.text_color` | select | white | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `tile.content_position` | select | bottom-left | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |
| `tile.media_position` | select | center center | Save-only | default (9) | **remove** | default in all 9 instance(s); hardcode default |

