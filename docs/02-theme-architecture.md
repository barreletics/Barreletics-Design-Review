# 02 — Theme Architecture

## Shopify Theme Structure

```
shopify-build/
├── layout/theme.liquid          ← Master wrapper (1 file)
├── templates/*.json             ← Page composition (33 files + 7 customer)
├── sections/*.liquid            ← Self-contained UI blocks (34 files)
├── snippets/*.liquid            ← Reusable partials (24 files)
├── assets/*.{css,js}            ← Stylesheets + JavaScript (4 files)
├── config/settings_schema.json  ← Setting definitions
├── config/settings_data.json    ← Current setting values
└── locales/en.default.json      ← Translation strings
```

**Rendering hierarchy**: Layout → Template → Sections → Snippets → Assets

## `theme.liquid` — Page Orchestration

Every page on the site is wrapped by `shopify-build/layout/theme.liquid`. It controls the full HTML document structure.

### `<head>` (lines 1–148)

| Concern | Implementation |
|---|---|
| Title | Template-aware: `{product.title} \| Barreletics`, `{collection.title} \| Barreletics Grippy Shoes`, etc. |
| Meta description | `page_description` from Shopify |
| Canonical URL | `{{ canonical_url }}` |
| Open Graph | Per-template OG tags (product, article, collection, blog, fallback). Fallback image: `og-default.jpg` asset. |
| Twitter Card | `summary_large_image` |
| Preconnects | `fonts.googleapis.com`, `fonts.gstatic.com`, `cdn.shopify.com`, `googletagmanager.com`, `connect.facebook.net` |
| Search Console | Conditional meta verification via `settings.search_console_verification` |
| Analytics (head) | `{% render 'analytics-head' %}` — GA4 gtag.js |
| Meta Pixel | `{% render 'meta-pixel' %}` — Facebook pixel base code + ViewContent |
| Pinterest Tag | `{% render 'pinterest-tag' %}` — Pinterest base code + pagevisit/viewcategory |
| Clarity | `{% render 'clarity' %}` — Microsoft Clarity session recording |
| Fonts | Google Fonts — Roboto (weights 300–800) via `<link>` |
| CSS | `design-tokens.css` then `barreletics-base.css` — both loaded globally as `<link>` stylesheet tags |
| Schema (all pages) | Inline Organization JSON-LD (`name`, `url`, `logo`) |
| Schema (homepage) | Conditional WebSite + SearchAction JSON-LD |
| Schema (collection) | `{% render 'collection-schema' %}` |
| Schema (article) | `{% render 'article-schema' %}` |
| Shopify head | `{{ content_for_header }}` |

### `<body>` (lines 150–212)

Rendered in this order:

1. **Body class** — `template-{{ template.name }}` with optional suffix
2. **Skip link** — `<a href="#main-content" class="skip-link">Skip to content</a>`
3. **Announcement strip** — `{% render 'announcement-strip' %}` — rotating promo messages
4. **Header/Nav** — `{% render 'header-nav' %}` — fixed header, desktop dropdown + mobile drawer
5. **Main content** — `<main id="main-content">{{ content_for_layout }}</main>` — template sections render here
6. **Footer** — `{% render 'footer' %}` — 4-column grid (Shop, Support, Company, Newsletter)
7. **Cart drawer** — `{% render 'cart-drawer' %}` — slide-in AJAX cart (D-024)
8. **Analytics events** — `{% render 'analytics-events' %}` — GA4 enhanced ecommerce
9. **Help Scout** — `{% render 'helpscout-beacon' %}` — support chat widget
10. **Tidio** — `{% render 'tidio-widget' %}` — AI chat widget
11. **Skip link styles** — inline `<style>` block
12. **Reduced motion** — inline `<style>` with `@media (prefers-reduced-motion: reduce)`

## Template JSON Architecture

Templates are JSON files that compose sections by reference. They contain no Liquid — only section type references, settings overrides, and render order.

### Example: `index.json`

```json
{
  "sections": {
    "hero": { "type": "hero", "settings": { ... } },
    "value-strip": { "type": "value-strip", "settings": {} },
    "disciplines": { "type": "disciplines", "settings": { ... } },
    "variant-grid": { "type": "variant-grid", "settings": { ... } },
    "fifty-fifty-grip": { "type": "fifty-fifty", "settings": { ... } },
    "social-proof": { "type": "social-proof", "settings": { ... } },
    "fifty-fifty-sock-math": { "type": "fifty-fifty", "settings": { ... } },
    "geo-section": { "type": "geo-section", "settings": { ... }, "blocks": { ... } },
    "newsletter": { "type": "newsletter", "settings": { ... } }
  },
  "order": [
    "hero", "value-strip", "disciplines", "variant-grid",
    "fifty-fifty-grip", "social-proof", "fifty-fifty-sock-math",
    "geo-section", "newsletter"
  ]
}
```

Key points:
- `"sections"` maps instance keys to section types with per-instance settings
- `"order"` controls render sequence
- The same section type can appear multiple times (e.g., `fifty-fifty` appears twice on homepage)
- Block data (e.g., geo items, review cards) is defined inline in the template JSON

### Template Inventory

| Template | Sections Used (in order) |
|---|---|
| `index.json` | hero, value-strip, disciplines, variant-grid, fifty-fifty ×2, social-proof, geo-section, newsletter |
| `product.json` | pdp-buy-box, value-strip, pdp-features, fifty-fifty ×2, variant-grid, pdp-sock-math, pdp-reviews, geo-section, newsletter, pdp-sticky-atc |
| `collection.json` | collection-hero, value-strip, variant-grid, disciplines, fifty-fifty ×2, geo-section, newsletter |
| `article.json` | article-content, newsletter |
| `blog.json` | blog-listing, newsletter |
| `search.json` | search-results, newsletter |
| `page.about.json` | fifty-fifty, page-about, fifty-fifty, geo-section, newsletter |
| `page.faq.json` | page-faq, geo-section, newsletter |
| `page.*.json` | Corresponding `page-*` section + shared sections (geo-section, newsletter) |
| `collection.*.json` | Same structure as `collection.json` with setting overrides per collection |

## Request Flow

```
URL hit
  → Shopify routing resolves template (e.g., /products/onyx-closed → product.json)
    → Template JSON defines section order
      → Each section renders its Liquid template (e.g., pdp-buy-box.liquid)
        → Sections {% render %} snippets as needed (e.g., product-card, review-card)
        → Sections include inline <style> blocks for scoped CSS
        → Sections include inline <script> blocks for component JS
      → CSS from assets/ loaded globally in <head> via theme.liquid
      → JS from assets/ loaded by pdp-buy-box.liquid on PDP pages only
```

## Global Includes

These snippets render on every page via `theme.liquid`:

| Snippet | Location | Purpose |
|---|---|---|
| `announcement-strip` | Body top | Rotating promotional messages |
| `header-nav` | After announcement | Fixed navigation + mobile drawer |
| `footer` | After `</main>` | 4-column footer with newsletter |
| `cart-drawer` | After footer | AJAX slide-in cart |
| `analytics-head` | `<head>` | GA4 gtag.js initialization |
| `analytics-events` | Before `</body>` | GA4 enhanced ecommerce events |
| `meta-pixel` | `<head>` | Meta/Facebook pixel + events |
| `pinterest-tag` | `<head>` | Pinterest conversion tracking |
| `clarity` | `<head>` | Microsoft Clarity session recording |
| `helpscout-beacon` | Before `</body>` | Help Scout support widget |
| `tidio-widget` | Before `</body>` | Tidio AI chat widget |

Conditional global includes (rendered by `theme.liquid` based on template):
- `collection-schema` — collection pages only
- `article-schema` — article pages only

## Theme Settings Architecture

### `settings_schema.json` — Setting Groups

| Group | Key Settings |
|---|---|
| **Colors** | `color_charcoal` (#1c1916), `color_body_text` (#4a4a4a), `color_muted` (#8a8a8a), `color_white`, `color_warm_cream` (#f5f2ec), `color_coral` (#e8927c), `color_rust` (#c45c3f), `color_gold` (#d4af37), `color_border` (#e5e0d8), `color_warm_border` (#d6cfc0) |
| **Typography** | `type_font_family` (Roboto), `type_base_size` (16px), `type_heading_scale` (100%) |
| **Layout** | `max_width` (1200px), `section_padding_x` (24px) |
| **Announcement bar** | `announcement_enabled`, `announcement_message_1`–`3`, `announcement_rotation_speed` (4s) |
| **Cart** | `cart_type` (drawer/page), `cart_show_free_shipping_bar`, `cart_free_shipping_threshold` ($150) |
| **Social media** | URLs for Instagram, TikTok, Facebook, Pinterest, YouTube |
| **Favicon & branding** | `favicon`, `og_default_image` |
| **Tracking & Integrations** | `ga4_measurement_id`, `meta_pixel_id`, `pinterest_tag_id`, `clarity_project_id`, `helpscout_beacon_id`, `tidio_widget_key`, `search_console_verification` |
| **Free shipping** | `free_shipping_threshold` ($150), `free_shipping_message` |

### `settings_data.json`

Stores current values for all settings defined in the schema. Updated via the Shopify theme customizer or direct JSON editing.
