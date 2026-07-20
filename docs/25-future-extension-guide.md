# 25 — Future Extension Guide

---
document: 25 – Future Extension Guide
status: Reference
last_modified: 2026-07-19
depends_on: [02-theme-architecture, 11-navigation-architecture, 16-integration-architecture]
---

## Overview

Step-by-step guides for extending the Barreletics Shopify theme. Each procedure assumes familiarity with Liquid templating, the token system (`docs/23-design-token-reference.md`), and the file structure (`docs/02-theme-architecture.md`).

---

## 1. Add a New Page Type

**Example:** Adding a `/pages/studio-finder` page.

1. Create the section: `shopify-build/sections/page-studio-finder.liquid`
   - Include a `<style>` block using design tokens
   - Add `{% schema %}` with settings and presets
   - Follow existing page sections (e.g., `page-faq.liquid`, `page-contact.liquid`) as reference

2. Create the template: `shopify-build/templates/page.studio-finder.json`
   ```json
   {
     "sections": {
       "page-studio-finder": {
         "type": "page-studio-finder",
         "settings": {}
       },
       "geo-section": {
         "type": "geo-section",
         "settings": { "heading": "Studios using Barreletics" },
         "blocks": {}
       },
       "newsletter": {
         "type": "newsletter",
         "settings": {}
       }
     },
     "order": ["page-studio-finder", "geo-section", "newsletter"]
   }
   ```

3. Add breadcrumb handling in `snippets/breadcrumb.liquid`:
   - The `{% when 'page' %}` case already handles generic pages with `{{ page.title }}`
   - If the page needs a parent crumb (e.g., "Resources > Studio Finder"), add a conditional on `page.handle`

4. Add navigation links:
   - Desktop nav: add `<li>` in `snippets/header-nav.liquid` under the appropriate list (primary nav or subnav)
   - Mobile menu: add corresponding `<li>` in `.mobile-menu__list` or `.mobile-menu__utility`
   - Footer: add link in appropriate column in `snippets/footer.liquid`

5. In Shopify Admin: create the page at Pages → Add page, set the template to `page.studio-finder`

---

## 2. Add a New Section

**Example:** Adding a testimonial carousel section.

1. Create `shopify-build/sections/testimonial-carousel.liquid`:
   ```liquid
   {% comment %}
     Testimonial Carousel — rotating customer quotes
   {% endcomment %}

   <section class="testimonials section" aria-label="Customer testimonials">
     <div class="section__inner">
       <!-- section markup using design tokens -->
     </div>
   </section>

   <style>
     .testimonials { /* styles using var(--space-x), var(--text-x), etc. */ }
   </style>

   {% schema %}
   {
     "name": "Testimonial Carousel",
     "settings": [
       { "type": "text", "id": "heading", "label": "Section heading" }
     ],
     "blocks": [
       {
         "type": "testimonial",
         "name": "Testimonial",
         "settings": [
           { "type": "text", "id": "quote", "label": "Quote" },
           { "type": "text", "id": "author", "label": "Author name" }
         ]
       }
     ],
     "presets": [{ "name": "Testimonial Carousel" }]
   }
   {% endschema %}
   ```

2. Add to template JSON files where the section should appear:
   ```json
   "testimonial-carousel": {
     "type": "testimonial-carousel",
     "settings": { "heading": "What instructors say" }
   }
   ```
   Add the section key to the `"order"` array at the desired position.

3. Rules:
   - All colors via `var(--token)` — never raw hex
   - Use `.section` and `.section__inner` wrapper classes for consistent padding/max-width
   - Include `aria-label` on the section element
   - Images use `loading="lazy"` unless above-the-fold

---

## 3. Add a New Snippet/Component

**Example:** Adding a reusable "trust badge row" snippet.

1. Create `shopify-build/snippets/trust-badges.liquid`:
   ```liquid
   {% comment %}
     Trust Badges Row
     Parameters:
       badges (array) — optional override; defaults to standard set
     Usage: {% render 'trust-badges' %}
   {% endcomment %}

   <div class="trust-badges">
     <span><strong>✓</strong> Free Shipping Over $150</span>
     <span><strong>✓</strong> 30-Day Returns</span>
     <span><strong>✓</strong> Made in USA</span>
   </div>

   <style>
     .trust-badges { display: flex; gap: var(--space-5); font-size: 12px; color: var(--text-muted); }
   </style>
   ```

2. Include in sections via `{% render 'trust-badges' %}`.

3. To pass parameters:
   ```liquid
   {% render 'trust-badges', show_warranty: true %}
   ```

4. Rules:
   - Document parameters in the `{% comment %}` block at the top
   - Snippets cannot access variables from the parent scope (Liquid isolation) — pass everything explicitly
   - Keep `<style>` blocks minimal; shared styles belong in `barreletics-base.css`

---

## 4. Add a New Collection Template

**Example:** Adding a "Best Sellers" collection.

1. Create `shopify-build/templates/collection.best-sellers.json`:
   ```json
   {
     "sections": {
       "collection-hero": {
         "type": "collection-hero",
         "settings": {
           "eyebrow": "Fan Favorites",
           "title": "Best Sellers",
           "body": "The styles instructors reach for most.",
           "show_sole_cards": false
         }
       },
       "variant-grid": {
         "type": "variant-grid",
         "settings": { "show_all_tab": false, "products_per_page": 8 }
       },
       "newsletter": {
         "type": "newsletter",
         "settings": {}
       }
     },
     "order": ["collection-hero", "variant-grid", "newsletter"]
   }
   ```

2. No new sections needed — reuse `collection-hero`, `variant-grid`, `value-strip`, `disciplines`, `fifty-fifty`, `geo-section`, `newsletter` with different settings (per D-032).

3. In Shopify Admin:
   - Create the collection at Products → Collections
   - Assign the template: in the collection editor, select "collection.best-sellers" from the Template dropdown

4. Add navigation links in `header-nav.liquid` if the collection should appear in nav.

---

## 5. Add a New Product Type

No template changes needed. The single `templates/product.json` handles all product types (grippy shoes, apparel, accessories, future socks).

1. In Shopify Admin: create the product with appropriate options (Color, Size) and variants
2. Assign to relevant collection(s)
3. The PDP template automatically renders:
   - Color swatches (if Color option exists)
   - Size buttons (if Size option exists)
   - Price from variant data
   - Gallery from product images
   - Structured data from product metafields

4. If the product needs a sole-type badge, set the `custom.sole_type` metafield on variants (rendered in `pdp-buy-box.liquid:49`).

---

## 6. Add a New Integration

**Example:** Adding Klaviyo email tracking.

1. Add setting to `shopify-build/config/settings_schema.json` in the "Tracking & Integrations" group:
   ```json
   {
     "type": "text",
     "id": "klaviyo_public_key",
     "label": "Klaviyo Public API Key",
     "info": "Found in Klaviyo → Settings → API Keys. Leave blank to disable."
   }
   ```

2. Create snippet: `shopify-build/snippets/klaviyo-tracking.liquid`:
   ```liquid
   {% if settings.klaviyo_public_key != blank %}
     <script async src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id={{ settings.klaviyo_public_key }}"></script>
   {% endif %}
   ```

3. Add render call to `layout/theme.liquid`:
   ```liquid
   {%- comment -%} Klaviyo {%- endcomment -%}
   {% render 'klaviyo-tracking' %}
   ```

4. Update `planning/10-decision-log.md` with a new decision entry documenting the integration.

5. Key rules:
   - Always guard with `{% if settings.xxx != blank %}`
   - Load scripts `async`
   - Respect D-045: if the integration overlaps with Shopify native channels, document the conflict

---

## 7. Add a New Tracking Pixel

Same as integration but with placement specifics:

1. Place in `<head>` section of `theme.liquid` (via snippet render) for pixels that need to fire before page content loads (GA4, Meta Pixel, Pinterest)
2. Place in `<body>` bottom for non-critical pixels (Clarity, Help Scout, Tidio)
3. For page-specific events (view_item, add_to_cart), add to `snippets/analytics-events.liquid` or create a dedicated events snippet rendered only on relevant templates

---

## 8. Extend the Design Token System

1. Add new custom property to `:root` in `shopify-build/assets/design-tokens.css`:
   ```css
   --new-category-name: value;
   ```

2. Follow naming convention:
   - Raw value: `--color-{name}`, `--space-{n}`, `--radius-{context}`
   - Semantic: `--{role}` (e.g., `--text-accent`, `--bg-overlay`)

3. If semantic, map to a raw token:
   ```css
   --text-accent: var(--color-rust);
   ```

4. If the token affects dark sections, add override in `[data-theme="dark"]` block:
   ```css
   [data-theme="dark"] {
     --text-accent: var(--color-coral);
   }
   ```

5. Document in this repo's token reference (`docs/23-design-token-reference.md`).

---

## 9. Add a New Navigation Item

### Desktop Navigation

Edit `shopify-build/snippets/header-nav.liquid`:

**Primary nav item** (lines 32–57 area):
```html
<li class="site-header__nav-item">
  <a href="/pages/new-page">New Page</a>
</li>
```

**With subnav dropdown:**
```html
<li class="site-header__nav-item site-header__nav-item--has-sub">
  <a href="/collections/new">New</a>
  <ul class="site-header__subnav" role="list">
    <li><a href="/collections/new">Shop All</a></li>
    <li><a href="/collections/sub-category">Sub Category</a></li>
  </ul>
</li>
```

### Mobile Menu

Same file, in the `.mobile-menu__list` (lines 97–115 area):
```html
<li class="mobile-menu__item">
  <a href="/pages/new-page">New Page</a>
</li>
```

For expandable sub-menu, use the `mobile-menu__item--parent` pattern with a `<button class="mobile-menu__toggle">`.

### Footer

Edit `shopify-build/snippets/footer.liquid` — add link in the appropriate column's list.

---

## 10. Add GEO Content to a New Page

1. In the page's template JSON (e.g., `templates/page.new-page.json`), add the `geo-section` section:
   ```json
   "geo-section": {
     "type": "geo-section",
     "settings": {
       "heading": "Contextual heading for this page"
     },
     "blocks": {
       "geo-item-1": {
         "type": "geo_item",
         "settings": {
           "question": "Region-specific question or heading",
           "answer": "<p>Answer with local context, studio names, city references.</p>"
         }
       },
       "geo-item-2": {
         "type": "geo_item",
         "settings": {
           "question": "Another regional question",
           "answer": "<p>Detailed answer with product-relevant local content.</p>"
         }
       }
     }
   }
   ```

2. Add `"geo-section"` to the template's `"order"` array.

3. The `sections/geo-section.liquid` automatically:
   - Renders an accordion UI
   - Generates FAQPage JSON-LD structured data
   - Applies consistent styling

4. Content rules (per D-022):
   - GEO content must be premium editorial — not keyword blocks
   - Include city/region names naturally
   - Reference real studio types and disciplines
   - Each block should be independently useful content

---

## 11. Create a New Help Scout Saved Reply

1. Source content from `planning/07-product-knowledge-base.md` (the Master Knowledge Base)
2. Rewrite in conversational email tone (warm, efficient, first-person brand voice)
3. Structure: greeting → direct answer → supporting detail → next step (link to relevant page)
4. Ensure factual claims match the Knowledge Base exactly — only words/tone may differ
5. Create in Help Scout → Saved Replies with clear naming: `[Category] - Topic`
6. Cross-reference: `planning/m4b-helpscout-alignment.md` for existing saved reply content

---

## 12. Update the Knowledge Base and Cascade Changes

Per `planning/13-knowledge-architecture.md`, the update cascade is:

1. **Update the source:** Edit `planning/07-product-knowledge-base.md`
2. **Website:** Update relevant section content (PDP accordions, FAQ, Compare page, pillar pages)
3. **Help Scout:** Update affected saved replies and macros
4. **Tidio AI:** Update affected Q&A pairs
5. **ManyChat:** Update affected content flows
6. **Wholesale/Studio materials:** Update at next refresh cycle

**Rules:**
- Facts originate ONLY from the Knowledge Base
- No downstream system may invent facts — only reformat approved ones
- If a downstream system reveals a correction needed, fix the Knowledge Base first, then cascade
- Log policy-level changes in `planning/10-decision-log.md`

**Example:** Shipping threshold changes from $150 to $175:
1. Update Knowledge Base Topic 15 (Shipping)
2. Website: `cart.js` FREE_SHIPPING_THRESHOLD, announcement strip settings, PDP trust row, cart drawer text
3. Help Scout: shipping macro
4. Tidio: shipping Q&A pair
5. Settings schema default value

---

## 13. Barreletics Socks Launch Preparation

The theme architecture already supports a sock product line. No structural changes required.

### Steps

1. **Create products in Shopify Admin:**
   - Add sock products with appropriate options (Size, Color, Style)
   - Upload product images
   - Set pricing and inventory
   - Add `custom.sole_type` metafield if applicable

2. **Create collection(s):**
   - Create a "Socks" collection in Shopify Admin
   - Assign template suffix if a unique collection layout is needed (e.g., `collection.socks.json`)
   - Otherwise, the default `collection.json` template works — `variant-grid` renders products from any collection

3. **Add to navigation:**
   - Add "Socks" to `header-nav.liquid` desktop nav (as a new primary item or under an existing parent)
   - Add to mobile menu
   - Add to footer if appropriate

4. **Variant grid tab filtering:**
   - `sections/variant-grid.liquid` supports tab filtering via `data-tags` attribute
   - Tag products appropriately for tab categories

5. **Update GEO content:**
   - Add sock-specific GEO blocks to the collection's `geo-section`
   - Add to PDP `geo-section` if sock-specific FAQs exist

6. **Update Knowledge Base and cascade:**
   - Add sock product specs, sizing, care to `planning/07-product-knowledge-base.md`
   - Cascade to Help Scout, Tidio, website content per procedure #12

7. **Template capabilities already in place:**
   - `templates/product.json` handles any product type (single template for all products)
   - `variant-selector.js` handles any combination of Color + Size options
   - `cart.js` handles any product add-to-cart
   - Collection templates support sub-collections (D-032)

---

**Cross-references:**
- Theme architecture → `docs/02-theme-architecture.md`
- Design tokens → `docs/23-design-token-reference.md`
- Navigation architecture → `docs/11-navigation-architecture.md`
- Knowledge architecture → `planning/13-knowledge-architecture.md`
- Integration architecture → `docs/16-integration-architecture.md`
- Decision Log → `planning/10-decision-log.md`
- Settings schema → `shopify-build/config/settings_schema.json`
