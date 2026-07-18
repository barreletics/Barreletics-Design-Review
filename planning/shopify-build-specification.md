# Shopify Build Specification

**Status:** DRAFT  
**Date:** 2026-07-13  
**Purpose:** Build-ready engineering spec for the Barreletics Shopify theme redesign  
**Sources:** docs/03-DESIGN-SYSTEM.md, docs/04-COMPONENT-LIBRARY.md, IMPLEMENTATION-ROADMAP-Jul2026.md, barreletics-decisions-2026-07-09.json

---

## THEME ARCHITECTURE

| Property | Value |
|----------|-------|
| Theme name | `barreletics-v2` |
| Base theme | None (clean OS 2.0 build; reference current live theme for migration) |
| Shopify OS 2.0 | **Required** — sections everywhere, JSON templates |
| Liquid version | Latest stable |
| Max content width | 1200px |
| Gutters | 32px desktop / 16px mobile |

### Directory Structure

```
barreletics-v2/
├── assets/
│   ├── base.css                   ← Reset + design tokens
│   ├── component-ticker.css
│   ├── component-header.css
│   ├── component-hero.css
│   ├── component-product-card.css
│   ├── component-pdp.css
│   ├── component-collection.css
│   ├── component-article.css
│   ├── component-sock-math.css
│   ├── component-split.css
│   ├── component-footer.css
│   ├── ticker.js
│   ├── pdp-gallery.js
│   ├── cart-drawer.js
│   ├── collection-filter.js
│   ├── predictive-search.js
│   ├── global.js                  ← Shared utilities (debounce, throttle, a11y helpers)
│   ├── Roboto-Light.woff2         ← 300
│   ├── Roboto-Regular.woff2       ← 400
│   ├── Roboto-Medium.woff2        ← 500
│   ├── Roboto-SemiBold.woff2      ← 600
│   ├── Roboto-Bold.woff2          ← 700
│   ├── JetBrainsMono-Regular.woff2
│   └── icons/                     ← SVG sprite or inline
├── config/
│   ├── settings_schema.json       ← Theme-level settings (colors, fonts, socials)
│   └── settings_data.json         ← Default preset
├── layout/
│   ├── theme.liquid               ← Main layout
│   └── password.liquid            ← Password page layout
├── locales/
│   └── en.default.json
├── sections/
│   ├── (see SECTION MAP below)
│   └── ...
├── snippets/
│   ├── (see SNIPPET MAP below)
│   └── ...
└── templates/
    ├── (see TEMPLATE MAP below)
    └── ...
```

---

## TEMPLATE MAP

All templates use OS 2.0 JSON format.

| Template | File | Notes |
|----------|------|-------|
| Home | `templates/index.json` | 13+ sections, top-to-bottom per design |
| Product | `templates/product.json` | Gallery + buy box + cross-sell |
| Collection | `templates/collection.json` | Hero + filter + grid + editorial breaks |
| Page | `templates/page.json` | Generic content page |
| Page (About) | `templates/page.about.json` | Founder story, manifesto |
| Article | `templates/article.json` | 720px content column, JetBrains Mono eyebrows |
| Blog | `templates/blog.json` | Featured article + 2-up card grid |
| Cart | `templates/cart.json` | Fallback cart page (primary UX is cart drawer) |
| 404 | `templates/404.json` | Minimal: headline + search + CTA to collection |
| Search | `templates/search.json` | Predictive search + results grid |
| Password | `templates/password.json` | Brand lockscreen with newsletter |
| Gift card | `templates/gift_card.liquid` | Shopify standard (Liquid required) |

---

## SECTION MAP

### Global (appear on every page)

| Section | File | Settings Schema | Block Types |
|---------|------|-----------------|-------------|
| Announcement Ticker | `section-ticker.liquid` | `slides` (array, max 5), `interval_ms` (default 4000), `bg_color`, `text_color` | `slide` — text, link_url, link_text |
| Header | `section-header.liquid` | `logo` (image), `logo_width`, `sticky` (bool), `menu` (link_list), `show_search` (bool), `cart_type` (drawer/page) | `nav-link` — label, url, mega_menu (bool) |
| Footer | `section-footer.liquid` | `bg_color`, `text_color`, `newsletter_heading`, `newsletter_subtext`, `show_social`, `copyright` | `link-column` — heading, menu; `social-link` — platform, url |

### Home Page

| Section | File | Settings Schema | Block Types |
|---------|------|-----------------|-------------|
| Hero | `section-hero.liquid` | `image`, `image_mobile`, `eyebrow` (text), `heading`, `body`, `cta_primary_text`, `cta_primary_url`, `cta_secondary_text`, `cta_secondary_url`, `overlay_opacity`, `layout` (split/full-bleed) | `eyebrow-slide` — text (for rotating eyebrow) |
| Pillar Strip | `section-pillar-strip.liquid` | `heading` (optional), `bg_color`, `columns_desktop` (3-6) | `pillar` — icon (image), label, description |
| 50/50 Split | `section-split-50-50.liquid` | `layout` (image-left/image-right), `image`, `video_url`, `eyebrow`, `heading`, `body`, `cta_text`, `cta_url`, `show_trust_line` (bool), `bg_color`, `height` (420px fixed) | `stat` — value, label |
| Product Grid | `section-product-grid.liquid` | `collection`, `heading`, `columns_desktop` (3-4), `show_quick_add` (bool), `rows` (1-4) | `product-card` — auto from collection |
| Variant Grid | `section-variant-grid.liquid` | `heading`, `subheading`, `tab_1_label` (Closed Sole), `tab_1_collection`, `tab_2_label` (Open Sole), `tab_2_collection`, `show_size_selector` (bool) | `variant-card` — product, image, color_name, price |
| Sock Math | `section-sock-math.liquid` | `eyebrow`, `heading`, `subtext`, `sock_price`, `sock_subtitle`, `barreletics_price`, `barreletics_subtitle`, `cta_text`, `cta_url`, `bg_color` | `comparison-row` — label, sock_value, barreletics_value; `benefit-cell` — number, title, description |
| Promo Tiles | `section-promo-tiles.liquid` | `heading` (optional) | `tile` — image, label, label_style (LE/New/Bestseller), heading, body, cta_text, cta_url |
| Disciplines | `section-disciplines.liquid` | `heading`, `subheading`, `bg_color` | `discipline` — name, description, image, cta_url |
| Reviews | `section-reviews.liquid` | `heading`, `subheading`, `reviews_count` (initial load), `show_load_more` (bool) | `review-card` — stars, name, text, verified (bool), date |
| Testimonial | `section-testimonial.liquid` | `quote`, `author`, `role`, `stars` (1-5), `image` (optional), `bg_color` | — |
| Founder Note | `section-founder.liquid` | `image`, `eyebrow`, `quote`, `body`, `signature_name`, `signature_title`, `bg_color` | `detail-line` — text |
| Association Strip | `section-association.liquid` | `eyebrow`, `statement`, `fine_print` | `brand` — name, logo (image) |
| Credibility | `section-credibility.liquid` | `eyebrow`, `heading`, `subtext`, `bg_color` | `studio-cell` — image, caption, count; `logo` — name |
| Manifesto | `section-manifesto.liquid` | `eyebrow`, `subtitle`, `rotation_speed_ms` (default 700), `bg_color` | `statement` — text |
| Problem | `section-problem.liquid` | `eyebrow`, `heading`, `body`, `image` | `old-solution` — text (rendered with strikethrough) |
| Closing Statement | `section-closing.liquid` | `eyebrow`, `heading`, `subtitle`, `cta_text`, `cta_url`, `bg_color` | — |
| Newsletter | `section-newsletter.liquid` | `heading`, `subtext`, `placeholder_text`, `button_text`, `bg_color`, `provider` (Klaviyo/native) | — |
| Guarantee | `section-guarantee.liquid` | `heading`, `subheading` | `guarantee` — icon (image), title, description |
| FAQ | `section-faq.liquid` | `heading`, `subheading` | `question` — question, answer (richtext) |
| Coperni Collab | `section-coperni.liquid` | `video_url`, `image_fallback`, `eyebrow`, `heading`, `body`, `cta_text`, `cta_url`, `le_badge` (bool) | — |
| Journal Cards | `section-journal-cards.liquid` | `blog`, `heading`, `posts_count` (3-6) | `article-card` — auto from blog |
| Social Feed | `section-social-feed.liquid` | `heading`, `juicer_feed_id` | — |

### PDP (Product Detail Page)

| Section | File | Settings Schema | Block Types |
|---------|------|-----------------|-------------|
| PDP Main | `section-pdp-main.liquid` | `show_vendor` (bool), `show_sku` (bool), `show_trust_row` (bool), `gallery_layout` (stacked/thumbnails), `enable_zoom` (bool), `sticky_buy_box` (bool) | `trust-badge` — icon, text; `tab` — title, content (richtext) |
| PDP Sock vs Skin | `section-pdp-comparison.liquid` | `heading`, `layout` (2-col editorial) | `column` — heading, body, image |
| PDP Accordion | `section-pdp-accordion.liquid` | `heading` | `panel` — title, content (richtext) |
| PDP Cross-sell | `section-pdp-cross-sell.liquid` | `heading`, `collection`, `max_products` (3-4) | — |
| Sticky ATC | `section-sticky-atc.liquid` | `show_on_mobile` (bool), `show_on_desktop` (bool) | — |

### Collection

| Section | File | Settings Schema | Block Types |
|---------|------|-----------------|-------------|
| Collection Hero | `section-collection-hero.liquid` | `show_description` (bool), `image` (optional hero image) | — |
| Sole Type Chooser | `section-sole-chooser.liquid` | `heading` | `sole-card` — image, title, description, collection_url |
| Collection Filter Row | `section-collection-filter.liquid` | `enable_filtering` (bool), `filter_style` (chips/dropdown), `enable_sorting` (bool) | — |
| Collection Grid | `section-collection-grid.liquid` | `columns_desktop` (3-4), `show_quick_add` (bool), `editorial_break_interval` (every N cards) | `editorial-break` — quote, author |

### Article / Blog

| Section | File | Settings Schema | Block Types |
|---------|------|-----------------|-------------|
| Article Hero | `section-article-hero.liquid` | `show_author` (bool), `show_date` (bool), `show_category` (bool) | — |
| Article Body | `section-article-body.liquid` | `max_width` (720px default) | `pull-quote` — text; `image-break` — image, caption |
| Blog Hero | `section-blog-hero.liquid` | `featured_article` (article ref), `layout` (full-width/split) | — |
| Blog Grid | `section-blog-grid.liquid` | `columns_desktop` (2-3), `posts_per_page` (6-12) | — |

### Utility

| Section | File | Settings Schema | Block Types |
|---------|------|-----------------|-------------|
| Rich Text | `section-rich-text.liquid` | `heading`, `content` (richtext), `max_width`, `alignment` | — |
| Image Banner | `section-image-banner.liquid` | `image`, `image_mobile`, `heading`, `body`, `cta_text`, `cta_url`, `overlay_opacity` | — |
| Custom Liquid | `section-custom-liquid.liquid` | `liquid_code` (textarea) | — |

**Total sections: 38**

---

## SNIPPET MAP

| Snippet | File | Used By |
|---------|------|---------|
| CSS Variables | `snippets/css-variables.liquid` | `theme.liquid` — all design tokens as CSS custom properties |
| Product Card | `snippets/product-card.liquid` | Product grid, variant grid, cross-sell, collection grid |
| Review Card | `snippets/review-card.liquid` | Reviews section, PDP reviews |
| Icon Set | `snippets/icon-set.liquid` | Global — SVG sprite (cart, search, menu, chevron, arrow, star, close, check, strikethrough) |
| Price Display | `snippets/price-display.liquid` | Product card, PDP buy box, cart — handles sale price (ink-bold, not red), compare-at |
| Size Selector | `snippets/size-selector.liquid` | PDP, quick-add modal — pill buttons with aria-pressed, strikethrough for OOS |
| Color Swatch | `snippets/color-swatch.liquid` | PDP, product card — circle swatches with outline on active |
| Benefit Pill | `snippets/benefit-pill.liquid` | Pillar strip, benefit grids — icon + label |
| Announcement Slide | `snippets/announcement-slide.liquid` | Ticker section |
| Breadcrumb | `snippets/breadcrumb.liquid` | PDP, collection, article — structured data compatible |
| Cart Line Item | `snippets/cart-line-item.liquid` | Cart drawer, cart page |
| LE Badge | `snippets/le-badge.liquid` | Product card, PDP — "Limited Edition" chip (`--br-le` / `--br-le-bg`) |
| Trust Row | `snippets/trust-row.liquid` | PDP — Free shipping · 30-day returns · 90-day warranty |
| Article Card | `snippets/article-card.liquid` | Blog grid, journal cards section |
| Pagination | `snippets/pagination.liquid` | Collection, blog |

---

## ASSETS

### CSS Files

| File | Purpose |
|------|---------|
| `base.css` | Reset, design tokens (`:root` variables), typography ramp, button system, grid utilities |
| `component-*.css` | Per-section styles, loaded conditionally via `{% stylesheet %}` or `<link>` with `media` |

### JS Files

| File | Purpose | Size Target |
|------|---------|-------------|
| `global.js` | Debounce, throttle, trap-focus, cart API wrapper, section rendering | < 8 KB gzip |
| `ticker.js` | Announcement bar rotator (4s interval, 320ms crossfade) | < 2 KB |
| `pdp-gallery.js` | Thumbnail swap, pinch-zoom, keyboard nav | < 4 KB |
| `cart-drawer.js` | AJAX cart drawer open/close, line item updates | < 4 KB |
| `collection-filter.js` | Chip toggle, URL param sync, AJAX re-render | < 3 KB |
| `predictive-search.js` | Fetch API → predictive search endpoint | < 3 KB |

### Fonts

| Font | Weights | Format | Usage |
|------|---------|--------|-------|
| Roboto | 300, 400, 500, 600, 700 | WOFF2 | All body, headings, buttons, nav |
| JetBrains Mono | 400 | WOFF2 | Eyebrow labels on technical sections, grip-spec captions only |

### SVG Icons

Cart, search, menu (hamburger), close (X), chevron-down, chevron-right, arrow-right, star-filled, star-empty, check, strikethrough, account, minus, plus, zoom.

All inline SVG via `icon-set.liquid` snippet — no external icon font.

---

## FONTS

### Loading Strategy

```html
<!-- In theme.liquid <head> -->
<link rel="preload" href="{{ 'Roboto-Regular.woff2' | asset_url }}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{{ 'Roboto-SemiBold.woff2' | asset_url }}" as="font" type="font/woff2" crossorigin>
```

- Preload Regular (400) and SemiBold (600) — most used weights
- Remaining weights load via `@font-face` in `base.css` with `font-display: swap`
- JetBrains Mono loads on-demand (not preloaded — used sparingly)
- **No Google Fonts CDN** — self-host all files for performance and privacy

---

## IMAGES

### CDN Strategy

- All product/editorial images served via Shopify CDN (`cdn.shopify.com`)
- Use Shopify's built-in image transforms: `| image_url: width: 800`
- Serve WebP automatically (Shopify CDN handles format negotiation)

### Required Image Sizes

| Context | Desktop | Mobile | Aspect Ratio |
|---------|---------|--------|--------------|
| Hero | 1920×1080 | 750×900 | 16:9 / 5:6 |
| Product card | 800×800 | 400×400 | 1:1 |
| 50/50 split | 960×420 | 750×420 | Custom (fixed 420px height) |
| Article hero | 1440×600 | 750×500 | 12:5 / 3:2 |
| Blog card | 600×450 | 400×300 | 4:3 |
| Promo tile | 600×450 | 750×450 | 4:3 |
| PDP gallery main | 1200×1200 | 750×750 | 1:1 |
| PDP gallery thumb | 120×120 | 80×80 | 1:1 |

### Placeholder vs Final

Photography in design mocks is placeholder from `barreletics.com/cdn/` and stand-in CDNs. Brand team provides final art-directed photography per page before launch. All `<img>` must have meaningful `alt` text.

### Lazy Loading

- Hero image: **eager** (`loading="eager"`, `fetchpriority="high"`)
- All below-fold images: `loading="lazy"`, `decoding="async"`

---

## METAFIELDS / METAOBJECTS

### Product Metafields

| Namespace.Key | Type | Purpose |
|---------------|------|---------|
| `custom.sole_type` | `single_line_text` | "Closed Sole" or "Open Sole" |
| `custom.grip_material` | `single_line_text` | Proprietary grip compound info |
| `custom.care_instructions` | `multi_line_text` | Rinse & reuse instructions |
| `custom.discipline_tags` | `list.single_line_text` | Barre, Reformer, Megaformer, Pilates, Yoga, Lagree |
| `custom.is_limited_edition` | `boolean` | Triggers LE badge on cards and PDP |
| `custom.sock_math_comparison` | `boolean` | Show condensed sock math on this product's PDP |
| `custom.cross_sell_products` | `list.product_reference` | Manual cross-sell overrides |

### Collection Metafields

| Namespace.Key | Type | Purpose |
|---------------|------|---------|
| `custom.hero_image` | `file_reference` | Optional collection-specific hero |
| `custom.sole_type_description` | `multi_line_text` | Sole type explainer copy |
| `custom.editorial_quote` | `single_line_text` | Quote for editorial breaks in grid |
| `custom.editorial_author` | `single_line_text` | Attribution for editorial quote |

### Page Metafields

| Namespace.Key | Type | Purpose |
|---------------|------|---------|
| `custom.page_eyebrow` | `single_line_text` | Eyebrow text for page hero |
| `custom.founder_image` | `file_reference` | Founder portrait for About page |

---

## NAVIGATION

### Header Nav (Desktop)

```
[Grippy Footwear ▾]  [Apparel]  [Collaborations]  [Journal]  [About Us]     [🔍] [👤] [🛒]
                                    ← Logo (centered) →
```

- Grippy Footwear: mega menu → Closed Sole, Open Sole, Limited Edition, All Footwear
- Apparel: direct link
- Collaborations: direct link (Coperni page)
- Journal: → /blogs/journal (not "Blog")
- About Us: direct link

### Footer Nav

4 columns:
1. **Shop** — Closed Sole, Open Sole, Limited Edition, All Products, Gift Cards
2. **Learn** — Journal, About Us, Sock vs. Skin, Size Guide
3. **Support** — Contact, Shipping & Returns, FAQ, Warranty
4. **Legal** — Privacy Policy, Terms of Service, Accessibility

### Mobile Nav

- Hamburger icon (left) opens slide-out drawer
- Accordion-style sub-menus
- Same link hierarchy as desktop
- Close on selection or escape key
- Cart icon always visible (right)

---

## SEARCH

### Predictive Search

- Activate on 2+ characters typed
- Show: products (4 max), collections (2 max), articles (2 max)
- Use Shopify's `predictive_search` resource
- Display product thumbnail, title, price
- "View all results →" link at bottom

### Results Template

- `templates/search.json`
- Product results in same card format as collection grid
- Article results as article cards
- "No results" state with suggested collections

---

## FILTERING

### Collection Filter Row

- **Style:** Inline horizontal chips (not sidebar)
- **Facets:** Discipline, Sole Type, Colorway, Price
- **Behavior:**
  - Multi-select within a facet (e.g., multiple colors)
  - Exclusive between facets where logical (e.g., one sole type)
  - URL-syncs via query params (`?filter.v.option.color=Black&sort_by=price-ascending`)
  - AJAX re-render (no full page reload)
  - Active filter chips show with ✕ dismiss
- **Mobile:** Horizontal scroll row, tap to toggle
- **Desktop:** Full-width wrapping row

---

## CART

### Cart Drawer (Primary)

- Opens on "Add to Cart" success
- Slide-in from right, 400px wide desktop
- Contents: line items, quantity stepper, remove button, subtotal, free shipping progress bar ($150 threshold), checkout CTA
- Discount code input
- "Continue Shopping" link
- Close on overlay click or escape key

### Cart Page (Fallback)

- `templates/cart.json`
- Same line item display as drawer
- Full-width layout for JS-disabled users

### Line Item Display

- Product image (80×80), title, variant (sole type / color / size), quantity stepper, line price
- "Remove" link (text, not icon-only for accessibility)

### Discount Display

- Applied discounts show below subtotal
- Discount code input with "Apply" button
- Error state for invalid codes

---

## HEADER

| Behavior | Specification |
|----------|---------------|
| Sticky | `position: sticky; top: 0; z-index: 40` |
| Background | Transparent until scroll > 8px, then `--br-bg` with 1px bottom hairline (`--br-line`) |
| Cart badge | 8px coral dot (`--br-accent`), top-right of cart icon, visible when items > 0 |
| Mobile hamburger | Left side, opens slide-out nav drawer |
| Logo | Centered, SVG wordmark |
| Transition | Background + hairline fade in over 200ms |

---

## FOOTER

| Element | Specification |
|---------|---------------|
| Background | Dark (`--br-text` / #050505) |
| Text | White, muted white for secondary links |
| Layout | 4 columns desktop, single column mobile |
| Newsletter | Horizontal input + button, Klaviyo integration |
| Social icons | Instagram, TikTok, Facebook — hover opacity shift |
| Copyright | `© {year} Barreletics. All rights reserved.` |
| Padding | 56px vertical |

---

## ANNOUNCEMENT BAR

| Property | Value |
|----------|-------|
| Slides | 3 (configurable up to 5) |
| Default slides | SAVE15 promo · Made in USA / free shipping over $150 · 1,000+ instructors |
| Interval | 4000ms |
| Transition | Opacity crossfade, 320ms ease |
| Pause | On hover |
| Reduced motion | Crossfade disabled, shows first slide static |
| Background | Dark (`--br-text`) or configurable |
| Text | White, 12px uppercase, 0.08em letter-spacing |

---

## APP DEPENDENCIES

| App | Purpose | Integration Point |
|-----|---------|-------------------|
| **JudgeMe** | Product reviews & ratings | Reviews section (PDP + Home), aggregate rating structured data, star snippets on product cards |
| **Juicer** | Social media feed aggregation | Social feed section (Home footer area), embed via Juicer JS widget |
| **Shop Pay** | Installment payments | PDP buy box — "4 interest-free payments of $XX" line below price |
| **Klaviyo** | Email/SMS marketing | Newsletter section form submission, back-in-stock alerts, post-purchase flows |
| **Google Analytics 4** | Analytics | `gtag.js` via theme.liquid, enhanced ecommerce events |

### App Loading

- JudgeMe: load JS only on pages with reviews (PDP, reviews section)
- Juicer: load only on Home (section-level lazy load)
- Klaviyo: newsletter form endpoint, minimal JS
- GA4: load in `<head>` (required for accurate tracking)

---

## PERFORMANCE CHECKLIST

### Core Web Vitals Targets

| Metric | Target | Strategy |
|--------|--------|----------|
| LCP | < 2.5s | Preload hero image + fonts, minimize render-blocking CSS |
| FID / INP | < 200ms | Defer non-critical JS, event delegation |
| CLS | < 0.1 | Explicit image dimensions, font-display: swap, reserve ticker height |

### Image Optimization

- [x] WebP via Shopify CDN automatic format negotiation
- [x] `loading="lazy"` on all below-fold images
- [x] `fetchpriority="high"` on hero/LCP image
- [x] Explicit `width` and `height` attributes on all `<img>`
- [x] `srcset` with 400, 800, 1200, 1600 breakpoints
- [x] Art direction via `<picture>` for hero (desktop vs mobile crop)

### CSS / JS

- [x] Critical CSS inlined in `<head>` (above-fold styles only)
- [x] Component CSS loaded per-section via `{% style %}` or conditional `<link>`
- [x] JS deferred with `defer` attribute
- [x] No jQuery dependency
- [x] Total JS budget: < 30 KB gzip (excluding third-party apps)

### Font Loading

- [x] Self-hosted WOFF2 (no Google Fonts CDN round-trip)
- [x] Preload 2 most-used weights (400, 600)
- [x] `font-display: swap` on all `@font-face`
- [x] JetBrains Mono loaded on-demand only

---

## ACCESSIBILITY CHECKLIST

- [x] **44px touch targets** — All buttons, links, form inputs minimum 44×44px tap area
- [x] **Reduced motion** — All animations gated on `@media (prefers-reduced-motion: no-preference)`; final state visible without animation
- [x] **ARIA labels** — `aria-pressed` on toggles (size pills, sole type), `aria-expanded` on accordions, `aria-label` on icon-only buttons (cart, search, menu)
- [x] **Keyboard navigation** — Full tab order, Enter/Space activation, Escape to close modals/drawers, arrow keys for gallery and size picker
- [x] **Color contrast** — WCAG AA minimum (4.5:1 normal text, 3:1 large text). `--br-text` (#050505) on `--br-bg` (#ffffff) = 19.5:1 ✓
- [x] **Focus indicators** — Visible focus ring (2px solid `--br-text`, 2px offset) on all interactive elements. Never `outline: none` without replacement.
- [x] **Skip to content** — Hidden skip link as first focusable element in `theme.liquid`
- [x] **Form labels** — All inputs have associated `<label>` elements (not placeholder-only)
- [x] **Alt text** — All images have descriptive alt text; decorative images use `alt=""`
- [x] **Semantic HTML** — Proper heading hierarchy (one `<h1>` per page), `<nav>`, `<main>`, `<footer>`, `<article>`

---

## SEO CHECKLIST

### Structured Data (JSON-LD)

- [x] **Product** — name, image, description, sku, brand, offers (price, availability, url)
- [x] **AggregateRating** — ratingValue, reviewCount (from JudgeMe)
- [x] **BreadcrumbList** — Home > Collection > Product (or Home > Journal > Article)
- [x] **Organization** — name, logo, url, sameAs (social links)
- [x] **WebSite** — SearchAction for sitelinks searchbox

### Meta Tags

- [x] Unique `<title>` per page — `{Page Title} | Barreletics`
- [x] Unique `<meta name="description">` per page (150-160 chars)
- [x] `<meta property="og:*">` for social sharing (title, description, image, type)
- [x] `<meta name="twitter:card" content="summary_large_image">`

### Technical SEO

- [x] Canonical URLs on all pages (`<link rel="canonical">`)
- [x] XML Sitemap (Shopify auto-generates)
- [x] `robots.txt` — allow all, disallow `/admin`, `/cart`, `/checkouts`
- [x] Clean URL structure (no query param indexing for filters)
- [x] "Blog" → "Journal" in all navigation, URLs (`/blogs/journal`)
- [x] 301 redirects for any changed URLs during migration

---

## ANALYTICS CHECKLIST

### GA4 Events

| Event | Trigger | Parameters |
|-------|---------|------------|
| `page_view` | Every page load | `page_title`, `page_location` |
| `view_item` | PDP load | `currency`, `value`, `items[]` (id, name, category, price, variant) |
| `view_item_list` | Collection page load | `item_list_id`, `item_list_name`, `items[]` |
| `add_to_cart` | Add to cart click | `currency`, `value`, `items[]` |
| `remove_from_cart` | Remove from cart | `currency`, `value`, `items[]` |
| `begin_checkout` | Checkout button click | `currency`, `value`, `items[]` |
| `purchase` | Order confirmation | `transaction_id`, `value`, `currency`, `tax`, `shipping`, `items[]` |
| `search` | Search submitted | `search_term` |
| `select_item` | Product card click | `item_list_id`, `items[]` |

### Enhanced Ecommerce

- GA4 property: **300437005**
- Implement via `gtag.js` in `theme.liquid`
- Data layer push for all cart/checkout events
- UTM parameter preservation through cart

---

## MIGRATION CHECKLIST

### Content to Migrate

- [x] All product data (titles, descriptions, images, variants, prices)
- [x] All collections and collection descriptions
- [x] Blog posts (rename "Blog" → "Journal" in navigation)
- [x] Pages (About, FAQ, Contact, policies)
- [x] Menus / navigation structure
- [x] Customer accounts and order history (Shopify retains)
- [x] Metafield data (existing product metafields)
- [x] Discount codes and automatic discounts
- [x] Shipping rates and zones

### URLs to Preserve

- [x] `/products/*` — no change needed
- [x] `/collections/*` — no change needed
- [x] `/blogs/journal/*` — redirect if old path was `/blogs/blog/*`
- [x] `/pages/*` — no change needed
- [x] Custom landing pages — 301 redirect map required

### Customer Data

- Shopify retains all customer data during theme switch
- No customer migration required
- Test: login, order history, saved addresses post-switch

---

## QA CHECKLIST

### Desktop Browsers

- [x] Chrome (latest 2 versions)
- [x] Safari (latest 2 versions)
- [x] Firefox (latest 2 versions)
- [x] Edge (latest 2 versions)

### Mobile Devices

- [x] iOS Safari (iPhone 13+)
- [x] Android Chrome (Pixel 6+, Samsung Galaxy S22+)
- [x] iPad Safari

### Breakpoint Testing

- [x] 375px (iPhone SE / small mobile)
- [x] 428px (iPhone 14 Pro Max)
- [x] 768px (tablet / breakpoint boundary)
- [x] 1024px (small desktop / iPad landscape)
- [x] 1440px (standard desktop)
- [x] 1920px (large desktop)

### Functional Testing

- [x] Cart: add, update quantity, remove, discount code, checkout link
- [x] PDP: variant selection (sole type, color, size), gallery, zoom, add to cart
- [x] Collection: filtering, sorting, pagination, grid display
- [x] Search: predictive search, results page, no-results state
- [x] Navigation: all links, mobile hamburger, sticky header, cart badge
- [x] Ticker: rotation, pause on hover, reduced motion
- [x] Newsletter: Klaviyo form submission, success/error states
- [x] Checkout: Shopify checkout flow, Shop Pay, payment methods
- [x] 404: page displays, search works, CTA links to collection

---

## LAUNCH CHECKLIST

- [ ] **DNS** — Domain pointed to Shopify (or already configured)
- [ ] **SSL** — SSL certificate active and auto-renewing (Shopify manages)
- [ ] **Theme publish** — Publish new theme from "Unpublished themes" in admin
- [ ] **App activation** — JudgeMe, Juicer, Klaviyo, Shop Pay verified and active
- [ ] **Analytics verification** — GA4 receiving events (page_view, add_to_cart, purchase). Verify property 300437005
- [ ] **Performance baseline** — Run Lighthouse on Home, PDP, Collection. Record scores
- [ ] **301 redirects** — Import redirect CSV for any changed URLs
- [ ] **Robots.txt** — Verify no accidental noindex
- [ ] **Sitemap** — Submit updated sitemap to Google Search Console
- [ ] **Social sharing** — Test og:image and og:description on Facebook, Twitter, LinkedIn
- [ ] **Email flows** — Verify Klaviyo signup, abandoned cart, post-purchase flows trigger
- [ ] **Payment test** — Complete test order with each payment method
- [ ] **Mobile spot-check** — Quick walk-through on physical iPhone and Android device
- [ ] **Stakeholder sign-off** — Final approval from brand team

---

## ROLLBACK CHECKLIST

- [ ] **Keep previous theme** — Do NOT delete current theme after publish; rename to `barreletics-v1-backup-{date}`
- [ ] **Test revert** — Before launch, practice the publish → revert cycle in a dev store
- [ ] **Revert procedure:** Admin → Online Store → Themes → `barreletics-v1-backup` → Publish
- [ ] **Monitoring window** — 48 hours post-launch: monitor conversion rate, bounce rate, Core Web Vitals
- [ ] **Data rollback** — Theme switch does not affect products, orders, customers. No data rollback needed unless custom metafield schema was changed
- [ ] **App state** — JudgeMe, Klaviyo, Juicer survive theme switch. Verify post-rollback
- [ ] **Redirect cleanup** — If rollback needed, remove any 301s that reference new-theme-only URLs

---

## RISK REGISTER

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| 1 | **Hero LCP > 2.5s** — Large hero image causes slow Largest Contentful Paint | Medium | High | Preload hero, serve 1200px max on mobile, use `fetchpriority="high"`, test on 3G throttle |
| 2 | **JudgeMe integration breaks** — Review widget fails to render or loses reviews during migration | Low | High | Test in unpublished theme first. JudgeMe uses product IDs (unchanged). Contact JudgeMe support pre-launch |
| 3 | **Variant grid complexity** — Custom-built variant grid (per decision notes: "heavy coding") requires significant refactoring | High | Medium | Prototype variant grid section first. Reuse existing custom code where possible. Budget extra time |
| 4 | **Color compliance drift** — Developer uses black/orange from design prototypes instead of warm/neutral palette per decision matrix | Medium | Medium | Add color linting to CI. Document "NO black/orange" rule in settings_schema.json comments. Theme check on every PR |
| 5 | **Klaviyo form breaks** — Newsletter form stops submitting or double-opts-in | Low | Medium | Test form submission in staging. Use Klaviyo's embed form (not custom AJAX) for reliability |
| 6 | **Mobile nav not implemented** — Hamburger menu is "currently hidden" per Component Library — needs full build | High | High | Prioritize mobile nav in Phase 2 (global components). Block launch without working mobile nav |
| 7 | **Free shipping threshold mismatch** — Copy references $75 (old) instead of $150 (current) | Low | Low | Centralize threshold in `settings_schema.json` as a single setting. Reference in ticker, cart, PDP trust row |
| 8 | **Third-party JS bloat** — JudgeMe + Juicer + Klaviyo + GA4 scripts push total JS over budget | Medium | Medium | Lazy-load Juicer and JudgeMe. Audit third-party scripts with WebPageTest. Set performance budget alert |
| 9 | **Eyebrow letter-spacing conflict** — 0.08em (design handoff) vs 0.14em (Research Bible) unresolved | High | Low | Requires Architect decision before build. Document in ADR-04. Default to 0.08em (design handoff) unless overridden |
| 10 | **Cart drawer accessibility** — Slide-in drawer without proper focus trapping fails a11y audit | Medium | Medium | Implement focus trap (first/last element loop), escape to close, return focus to trigger on close |
| 11 | **SEO URL breakage** — Blog rename (blog → journal) or collection restructuring loses indexed URLs | Medium | High | Crawl current site pre-migration. Create comprehensive 301 redirect map. Monitor 404s in Search Console for 30 days |
| 12 | **Undecided sections block launch** — 5 sections (04, 15, 24, 25, 29) need decisions per roadmap | High | Medium | Gate Phase 3 on decisions. Ship with placeholder sections or exclude from initial launch. Track in decision log |
| 13 | **Content photography not ready** — All design photos are placeholders; brand team art direction required | Medium | High | Set hard deadline for photo delivery 2 weeks before launch. Have fallback plan with existing product photos |
| 14 | **Checkout customization limits** — Shopify Plus may be required for some checkout UI changes | Low | Medium | Confirm Shopify plan level. Use Shopify's native checkout — do not customize unless on Plus |

---

**END OF SPECIFICATION**
