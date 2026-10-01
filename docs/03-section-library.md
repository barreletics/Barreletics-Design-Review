# 03 — Section Library

Every section lives in `shopify-build/sections/` and is referenced by its filename (without `.liquid`) in template JSON files.

All sections use inline `<style>` blocks for scoped CSS. No section loads external CSS files — global styles come from `design-tokens.css` and `barreletics-base.css` (see [Doc 05](05-asset-library.md)).

---

## Homepage Sections

### `hero.liquid`

50/50 split layout — copy on the left, full-bleed image on the right. `min-height: 75vh`. Image loads with `loading="eager"` and `fetchpriority="high"`.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Barre · Reformer · Megaformer · Pilates · Yoga" |
| `title` | text | "The Pilates Sock Era Is Over" |
| `body` | textarea | "360° grip performance skins..." |
| `cta_primary_text` | text | "Shop Now" |
| `cta_primary_url` | url | — |
| `cta_secondary_text` | text | "See Why →" |
| `cta_secondary_url` | url | — |
| `trust_line` | text | "Trusted by 1,000's of instructors · Made in USA" |
| `image` | image_picker | — |
| `image_alt` | text | "Studio session with Barreletics performance skins" |

**Blocks:** None  
**Templates:** `index.json`  
**Snippets:** `section-wrapper` (pattern reference only — snippet is documentation-only)  
**CSS:** Inline `<style>`. Grid → single-column at 768px.

### `hero-alt.liquid`

Identical layout and structure to `hero.liquid`. Different default copy ("Think Outside the Sock."). Created per D-041 for A/B testing hero messaging.

**Settings:** Same schema as `hero.liquid`.  
**Templates:** None currently (available as preset "Hero (Alt Concept)")

### `value-strip.liquid`

Horizontal strip of trust/value items with checkmark icons. Warm cream background (`--bg-alternate`), top/bottom borders.

| Setting | Type | Default |
|---|---|---|
| (none) | — | — |

**Blocks:** `item` — `icon` (text, default "✓"), `text` (text, default "360° locked grip")  
**Templates:** `index.json`, `product.json`, `collection.json`  
**CSS:** Inline. Flex layout, wraps on mobile.

### `disciplines.liquid`

Line-divider strip showing discipline names with proof statements. Horizontal flex layout with vertical dividers.

| Setting | Type | Default |
|---|---|---|
| `headline` | text | "Grip That Holds Where It Matters Most" |

**Blocks:** `discipline` — `discipline` (text), `proof` (text), `secondary` (checkbox, default false — dims item to 65% opacity)  
**Templates:** `index.json`, `collection.json`  
**CSS:** Inline. Flex → column on mobile.

### `social-proof.liquid`

3-column review card grid with aggregate rating header. Uses `review-card` snippet for each block.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Real Results" |
| `rating` | text | "4.9" |
| `review_count` | text | "294" |
| `all_reviews_url` | url | — |

**Blocks:** `review` — `rating` (range 1–5), `body` (textarea), `author` (text), `location` (text)  
**Templates:** `index.json`  
**Snippets:** `review-card`  
**CSS:** Inline. Grid 3→2→1 columns at breakpoints.

---

## PDP Sections

### `pdp-buy-box.liquid`

Full buy box with image gallery, variant selection (color swatches + size buttons), add-to-cart form, trust signals, and 4 accordion panels (Description, Care, Shipping, Returns). Includes Product JSON-LD schema with Judge.me aggregate rating.

**Loads both JS asset files:**
```
{{ 'variant-selector.js' | asset_url | script_tag }}
{{ 'cart.js' | asset_url | script_tag }}
```

Also injects `window.__pdpProduct = {{ product | json }}` for the variant selector.

| Setting | Type | Default |
|---|---|---|
| (none) | — | — |

**Blocks:** None  
**Templates:** `product.json`  
**Snippets:** None directly (uses inline accordion pattern)  
**CSS:** Inline. 2-column grid, gallery sticky on desktop. Single-column at 768px.  
**JS:** Inline IIFE for accordion toggle + `aria-expanded` management.

### `pdp-features.liquid`

"Built around one obsession: Grip." — 2-column feature grid with optional discipline icon strip.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Why Barreletics" |
| `title` | html | "Built around<br>one obsession: <strong>Grip.</strong>" |
| `show_disciplines` | checkbox | true |

**Blocks:** `feature` — `title` (text), `description` (textarea)  
**Templates:** `product.json`  
**CSS:** Inline. 2→1 column grid on mobile.

### `pdp-reviews.liquid`

Judge.me integration: Liquid header with metafield stats, featured reviews from blocks (merchant-curated), community reviews fetched client-side via Judge.me API.

| Setting | Type | Default |
|---|---|---|
| (none) | — | — |

**Blocks:** `featured_review` — `title` (text), `body` (textarea), `author` (text), `verified` (checkbox), `bg_gradient` (text)  
**Templates:** `product.json`  
**Snippets:** `review-card` (for JS-rendered community reviews, structure replicated in inline `buildReviewCard()`)  
**CSS:** Inline. Featured reviews: 2-column grid cards. Community: 3→2→1 column grid.  
**JS:** Inline IIFE fetches from Judge.me API, renders review cards client-side.

### `pdp-sock-math.liquid`

Cost comparison: Barreletics ($74 once) vs grip socks ($144/yr). Large typography price comparison + 2-column pros/cons grid.

| Setting | Type | Default |
|---|---|---|
| `headline` | text | "One pair. Done." |
| `subheadline` | text | "Your practice. Your pace..." |
| `our_price` | text | "$74" |
| `their_price` | text | "$144" |
| `savings_line` | text | "Save $70+ in year one..." |
| `cta_text` | text | "Shop Barreletics →" |
| `cta_url` | url | — |

**Blocks:** None  
**Templates:** `product.json`  
**CSS:** Inline. 2→1 column grid on mobile.

### `pdp-sticky-atc.liquid`

Thin wrapper around `sticky-atc` snippet. Appears when the buy box scrolls out of view.

| Setting | Type | Default |
|---|---|---|
| (none) | — | — |

**Blocks:** None  
**Templates:** `product.json`  
**Snippets:** `sticky-atc`

---

## Collection Section

### `collection-hero.liquid`

Collection intro with `collection.title` / `collection.description` and optional Open/Closed Sole comparison cards.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Two Versions. One Performance." |
| `title` | text | "Shop All Styles & Colors" (fallback) |
| `body` | textarea | "One patented grip system, two builds..." (fallback) |
| `show_sole_cards` | checkbox | true |
| `closed_image` | image_picker | — |
| `closed_desc` | textarea | "Full coverage including heel..." |
| `open_image` | image_picker | — |
| `open_desc` | textarea | "Open heel with a mid-foot vent..." |

**Blocks:** None  
**Templates:** `collection.json` (and all `collection.*.json` variants)

---

## Blog/Article Sections

### `article-content.liquid`

Full article layout: header (category tag, title, author, date), hero image, rich text body, share buttons (X, Facebook, Email), tag links, related articles grid (3-up). Includes BlogPosting JSON-LD.

| Setting | Type | Default |
|---|---|---|
| `show_related` | checkbox | true |
| `related_heading` | text | "Keep Reading" |

**Blocks:** None  
**Templates:** `article.json`

### `blog-listing.liquid`

Responsive article grid with featured images, titles, excerpts, author, date, category tags. Supports pagination.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "The Journal" |
| `title` | text | "The Barreletics Journal" |
| `subtitle` | text | "Studio tips, product insights, and performance stories." |
| `articles_per_page` | range (3–12, step 3) | 9 |

**Blocks:** None  
**Templates:** `blog.json`  
**CSS:** Inline. Grid 3→2→1 columns. Hover: image scale 1.03.

---

## Search

### `search-results.liquid`

Search page with input form, results grouped by type (Products, Journal, Pages), and empty state with suggested searches.

| Setting | Type | Default |
|---|---|---|
| (none) | — | — |

**Blocks:** None  
**Templates:** `search.json`  
**Snippets:** `product-card` (for product results)

---

## Supporting Page Sections

All supporting page sections follow a consistent pattern: centered header with eyebrow + title, alternating `section`/`section--cream` background bands, `section__inner--narrow` max-width.

### `page-about.liquid`

Brand story with intro, dark-section manifesto blockquote, values grid (blocks), Made in USA section. Includes Organization JSON-LD.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Our Story" |
| `title` | text | "Redefining Grip" |
| `intro_text` | richtext | (brand story) |
| `manifesto` | richtext | "We didn't improve the grip sock. We made it obsolete." |
| `values_heading` | text | "What We Stand For" |
| `made_in_usa_heading` | text | "Designed and Made in the USA" |
| `made_in_usa_text` | richtext | (manufacturing story) |

**Blocks:** `value` — `title` (text), `description` (textarea)  
**Templates:** `page.about.json`

### `page-faq.liquid`

Categorized FAQ with accordion groups. Each `faq_item` block specifies a `category` string — items are grouped/rendered by category. Includes FAQPage JSON-LD.

| Setting | Type | Default |
|---|---|---|
| `title` | text | "Frequently Asked Questions" |
| `subtitle` | textarea | "Everything you need to know..." |

**Blocks:** `faq_item` — `category` (text), `question` (text), `answer` (richtext)  
**Templates:** `page.faq.json`  
**JS:** Inline — one-at-a-time accordion behavior per category group.

### `page-contact.liquid`

2-column layout: contact form (name, email, subject dropdown, message) + sidebar (response time card, quick links nav). Uses `button` snippet for submit.

| Setting | Type | Default |
|---|---|---|
| `title` | text | "Get in Touch" |
| `subtitle` | textarea | "Have a question about fit..." |
| `button_text` | text | "Send Message" |
| `success_message` | text | "Thanks for reaching out..." |
| `info_heading` | text | "Response Time" |
| `response_time` | textarea | "We respond within 24-48 hours..." |

**Blocks:** None  
**Templates:** `page.contact.json`  
**Snippets:** `button`

### `page-size-guide.liquid`

Size chart table, color-specific fit notes (Dark Grey/Hot Coral/Blue run snug), fit tips grid. Uses `button` snippet for CTA.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Fit Guide" |
| `title` | text | "Size Guide" |
| `subtitle` | textarea | "Performance Skins are designed for a snug..." |
| `snug_colors_note` | textarea | "These colors run slightly snugger..." |
| `light_grey_note` | textarea | "Light Grey offers a slightly more relaxed fit..." |
| `cta_text` | text | "Shop Now" |
| `cta_url` | url | — |
| `cta_note` | textarea | "Still unsure? Contact us..." |

**Blocks:** `size_row` — `size_name`, `us_size`, `foot_length`, `best_for` (all text); `fit_tip` — `title`, `description`  
**Templates:** `page.size-guide.json`  
**Snippets:** `button`

### `page-compare.liquid`

Open vs Closed Sole side-by-side: visual product cards + feature comparison table + shared features note. Uses `button` snippet.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Two Versions. One Performance." |
| `title` | text | "Open Sole vs Closed Sole" |
| `subtitle` | textarea | "Same patented 360° grip..." |
| `product_a_name` | text | "Open Sole" |
| `product_a_desc` | textarea | — |
| `product_a_cta` | text | "Shop Open Sole" |
| `product_a_url` | url | — |
| `product_b_name` | text | "Closed Sole" |
| `product_b_desc` | textarea | — |
| `product_b_cta` | text | "Shop Closed Sole" |
| `product_b_url` | url | — |
| `shared_note` | textarea | "Both deliver the same patented 360° grip..." |

**Blocks:** `feature_row` — `feature` (text), `value_a` (text), `value_b` (text)  
**Templates:** `page.compare.json`  
**Snippets:** `button`

### `page-technology.liquid`

Technology deep-dive: feature cards, "How It Works" richtext, "Double Failure of Grip Socks" (dark section), materials grid, manufacturing section. Uses `button` snippet.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "The Technology" |
| `title` | text | "Patented 360° Grip Technology" |
| `subtitle` | textarea | "Not printed. Not glued..." |
| `how_heading` | text | "How It Works" |
| `how_it_works` | richtext | — |
| `double_failure_heading` | text | "The Double Failure of Grip Socks" |
| `double_failure_text` | richtext | — |
| `materials_heading` | text | "Materials" |
| `manufacturing_heading` | text | "Made in USA" |
| `manufacturing_text` | richtext | — |
| `cta_heading` | text | "Experience the Difference" |
| `cta_body` | textarea | — |
| `cta_text` | text | "Shop Performance Skins" |
| `cta_url` | url | — |

**Blocks:** `feature` — `title`, `description`; `material` — `title`, `description`  
**Templates:** `page.technology.json`  
**Snippets:** `button`

### `page-grip-comparison.liquid`

Category disruption / conversion asset. Dark hero, comparison table (Barreletics vs Grip Socks), Double Failure cards, Sock Math calculator, customer quotes, bottom CTA, FAQ accordion. Includes FAQPage JSON-LD.

**Blocks:** `comparison_row`, `quote`, `faq_item`  
**Templates:** `page.grip-comparison.json`  
**Snippets:** `button`

### `page-ambassador.liquid`

Ambassador program overview with benefits grid and application form (first/last name, email, Instagram, TikTok, discipline dropdown, message). Uses `button` snippet.

**Blocks:** `benefit` — `title`, `description`  
**Templates:** `page.ambassador.json`  
**Snippets:** `button`

### `page-shipping.liquid`

Shipping info: highlight cards, domestic/international sections, FAQ accordion. Includes inline FAQ accordion JS.

**Blocks:** `highlight` — `title`, `description`; `faq_item` — `question`, `answer`  
**Templates:** `page.shipping.json`

### `page-returns.liquid`

Return policy card, numbered step process, exchange info, international returns, FAQ accordion.

**Blocks:** `return_step` — `title`, `description`; `faq_item` — `question`, `answer`  
**Templates:** `page.returns.json`

### `page-warranty.liquid`

90-day warranty: covered vs not-covered split grid, numbered claim steps, international warranty.

**Blocks:** `covered` — `text`; `not_covered` — `text`; `claim_step` — `title`, `description`  
**Templates:** `page.warranty.json`

### `page-partners.liquid`

Partner programs **routing hub** (**D-048**, 2026-08-08): three cards linking out to the dedicated
`/pages/wholesale`, `/pages/studio-program` and `/pages/ambassador` pages, plus a general-inquiry
fallback form for people who don't know which program fits. Program CTAs are Theme Editor settings
(`*_cta_url`).

> **UPDATED 2026-08-08.** This entry previously read: *"Consolidated partner programs page (D-042):
> Wholesale, Studio Partners, Ambassadors on one page. Unified inquiry form at bottom. Replaces
> separate wholesale/studio/ambassador pages."* Owner direction 2026-08-08 reversed the fold —
> **D-048** in `planning/10-decision-log.md` supersedes D-042. `page-partners.liquid` no longer
> replaces the three program sections; it routes to them. Each program section below carries its own
> `BL-PARTNER-*` intake form. See `planning/partner-programs.md`.

**Blocks:** `wholesale_benefit`, `studio_benefit`, `ambassador_benefit` — each with `title`, `description`  
**Templates:** `page.partners.json`  
**Snippets:** `button`

### `page-wholesale.liquid`

Standalone wholesale inquiry: 2-column layout (content + form card). Volume dropdown (10-25, 25-50, 50-100, 100+).

**Blocks:** `benefit` — `title`, `description`  
**Templates:** `page.wholesale.json`  
**Snippets:** `button`

### `page-studio-program.liquid`

Studio partnership page with benefits grid, testimonials, and application form (studio name, contact, email, location, discipline, message).

**Blocks:** `benefit` — `title`, `description`; `testimonial` — `quote`, `name`, `studio`  
**Templates:** `page.studio-program.json`  
**Snippets:** `button`

---

## Shared / Reusable Sections

### `fifty-fifty.liquid`

Reusable 50/50 split — media (image or video placeholder) + copy. Supports reversed layout, custom background color.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | — |
| `title` | text | "Upgrade Your Grip. Upgrade Your Workout." |
| `body` | textarea | "Full-contact molded grip..." |
| `cta_text` | text | "Shop now" |
| `cta_url` | url | — |
| `image` | image_picker | — |
| `image_alt` | text | — |
| `video_url` | url | — |
| `video_caption` | text | — |
| `reverse` | checkbox | false |
| `bg_color` | color | #ffffff |

**Blocks:** None  
**Templates:** `index.json` (×2), `product.json` (×2), `collection.json` (×2), `page.about.json` (×2)

### `variant-grid.liquid`

Tabbed product grid with collection filtering (All / Closed / Open / One-Offs / Outdoor), size toggle (M/L), and links to size chart + compare page. Uses `product-card` snippet.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Two Versions. One Performance." |
| `title` | text | "Shop All Styles & Colors" |
| `body` | textarea | "One patented grip. Closed Sole or Open Sole..." |
| `collection` | collection | — |
| `products_per_page` | range (4–16, step 4) | 8 |
| `show_all_tab` | checkbox | false |
| `view_all_url` | url | — |

**Blocks:** None  
**Templates:** `index.json`, `product.json`, `collection.json`  
**Snippets:** `product-card`  
**JS:** Inline IIFE for tab filtering (shows/hides cards by `data-tags` attribute).

### `newsletter.liquid`

Email signup form: eyebrow, headline, body, email input, submit button, legal text. Posts to Shopify `/contact` endpoint.

| Setting | Type | Default |
|---|---|---|
| `eyebrow` | text | "Join the list" |
| `title` | text | "Join the list" |
| `body` | text | "New drops and studio stories. Once or twice a quarter — never spam." |
| `placeholder` | text | "Email address" |
| `button_text` | text | "Subscribe" |
| `legal` | text | "By subscribing you agree to receive marketing emails..." |

**Blocks:** None  
**Templates:** Appears on nearly every template (index, product, collection, article, blog, search, all page.* templates)

### `geo-section.liquid`

GEO/SEO content accordion (D-022). `<details>` elements with contextually relevant Q&A. Outputs FAQPage JSON-LD.

| Setting | Type | Default |
|---|---|---|
| `heading` | text | "Trusted in studios everywhere" |

**Blocks:** `geo_item` — `question` (text), `answer` (richtext)  
**Templates:** `index.json`, `product.json`, `collection.json`, most `page.*.json` templates

### `recommendations.liquid`

"You may also like" grid. Fetches from Shopify's `/recommendations/products.json` API client-side.

| Setting | Type | Default |
|---|---|---|
| `heading` | text | "You may also like" |
| `limit` | range (2–8, step 1) | 4 |

**Blocks:** None  
**Templates:** `product.json` (optional)  
**JS:** Inline IIFE — `fetch()` to recommendations API, client-side HTML rendering.

### `recently-viewed.liquid`

Recently viewed products tracked in `localStorage` (key: `barreletics_recently_viewed`). Max 8 stored, 4 displayed. Hidden (`display: none`) until items exist. Client-side rendering.

| Setting | Type | Default |
|---|---|---|
| `heading` | text | "Recently Viewed" |

**Blocks:** None  
**Templates:** `product.json` (optional)  
**JS:** Inline IIFE — reads/writes localStorage, renders cards.
