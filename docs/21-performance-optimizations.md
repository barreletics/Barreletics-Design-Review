# 21 — Performance Optimizations

---
document: 21 – Performance Optimizations
status: Reference
last_modified: 2026-07-19
depends_on: [02-theme-architecture, 07-css-architecture, 06-javascript-architecture]
---

## Overview

The Barreletics theme is engineered for minimal payload: two CSS files, two JS files (PDP-only), no frameworks, no build tools. Every performance decision favors first-paint speed and Shopify CDN optimization.

---

## Image Optimization

### Hero / Gallery Images

The PDP main product image (`pdp-buy-box.liquid`) uses eager loading with high fetch priority:

```liquid
<img
  id="pdp-main-img"
  src="{{ product.featured_image | image_url: width: 800 }}"
  srcset="{{ product.featured_image | image_url: width: 400 }} 400w,
          {{ product.featured_image | image_url: width: 600 }} 600w,
          {{ product.featured_image | image_url: width: 800 }} 800w"
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="{{ product.featured_image.alt | default: product.title | escape }}"
  loading="eager"
  fetchpriority="high"
>
```

- **`loading="eager"`** — browser fetches immediately (above-the-fold)
- **`fetchpriority="high"`** — signals to the browser this is LCP-critical
- **Responsive srcset** — 400w, 600w, 800w breakpoints for product images
- **`sizes` attribute** — full-width on mobile (`100vw`), half-width on desktop (`50vw`)

### Thumbnails

Gallery thumbnails load at 160px width with lazy loading:

```liquid
<img src="{{ image | image_url: width: 160 }}" alt="View {{ forloop.index }}" width="72" height="72" loading="lazy">
```

Explicit `width` and `height` attributes prevent layout shift (CLS).

### All Other Images

Every image below the fold uses `loading="lazy"`:
- Cart drawer item images (`cart-drawer.liquid:50–55`)
- Product card images in collections
- Section imagery (fifty-fifty, disciplines, etc.)

### Shopify CDN

All image URLs use the `image_url` Liquid filter, which routes through Shopify's CDN with automatic WebP conversion, resizing, and edge caching. No manual image optimization required.

---

## CSS Strategy

### Two Global Files Only

```
layout/theme.liquid:
  {{ 'design-tokens.css' | asset_url | stylesheet_tag }}
  {{ 'barreletics-base.css' | asset_url | stylesheet_tag }}
```

| File | Purpose | Size |
|------|---------|------|
| `assets/design-tokens.css` | Custom properties (colors, spacing, typography, radii, shadows, z-index) | ~150 lines |
| `assets/barreletics-base.css` | Reset, typography scale, buttons, grid, section wrappers, focus indicators, accessibility utilities | ~190 lines |

No CSS framework (no Tailwind, Bootstrap, or Foundation). Total CSS payload is minimal with zero unused framework bloat.

### Section-Specific Styles

Each section includes a `<style>` block scoped to its own classes:

```liquid
<!-- In sections/pdp-buy-box.liquid -->
<style>
  .pdp-hero { display: grid; grid-template-columns: 1fr 1fr; ... }
  .pdp-gallery__hero { aspect-ratio: 1; ... }
  ...
</style>
```

This pattern:
- Loads CSS only when the section renders
- Avoids specificity conflicts between sections
- Keeps each section self-contained and portable

### Custom Properties Enable Runtime Theming

Semantic tokens (`--text-primary`, `--bg-primary`, `--border-default`) map to raw color values in `:root`. Dark sections override via `[data-theme="dark"]` without duplicating rules — the same CSS works for both light and dark contexts.

---

## JavaScript Strategy

### Vanilla JS Only

No jQuery, React, Vue, or any framework. All interactivity is written in plain ES5-compatible JavaScript.

### Two JS Files (PDP Only)

```liquid
{%- comment -%} Loaded ONLY in sections/pdp-buy-box.liquid {%- endcomment -%}
{{ 'variant-selector.js' | asset_url | script_tag }}
{{ 'cart.js' | asset_url | script_tag }}
```

| File | Purpose | Lines |
|------|---------|-------|
| `assets/variant-selector.js` | Resolves option combinations to variant IDs, updates price/image/URL/availability | ~190 |
| `assets/cart.js` | AJAX add-to-cart, drawer rendering, quantity changes, focus trap, live region | ~320 |

These are loaded at the bottom of `pdp-buy-box.liquid` (after the DOM elements they target), avoiding render-blocking.

### Inline Section JS

All other JavaScript is inline within section `<script>` blocks:
- `header-nav.liquid` — scroll detection, mobile menu open/close, accordion toggles
- `pdp-buy-box.liquid` — accordion `toggle` event for `aria-expanded`
- `cart-drawer.liquid` — cart trigger click binding
- `announcement-strip.liquid` — message rotation with setInterval

### IIFE Pattern

Both JS files and all inline scripts use the Immediately Invoked Function Expression pattern to prevent global namespace pollution:

```javascript
(function () {
  'use strict';
  // all logic scoped here
})();
```

The only intentional global is `window.BarreleticsCart` (public API for cart operations).

---

## Font Loading

Single font family loaded from Google Fonts in `layout/theme.liquid`:

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```

- **`display=swap`** — text renders immediately with fallback font, swaps when Roboto loads (no FOIT)
- **Weights loaded:** 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold), 800 (extra-bold)
- **Fallback stack:** `'Roboto', -apple-system, BlinkMacSystemFont, sans-serif` (defined in `--font-family` token)

---

## Preconnects

All preconnect hints are in `layout/theme.liquid` `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<link rel="preconnect" href="https://connect.facebook.net" crossorigin>
```

The `crossorigin` attribute is required for CORS-enabled resources (fonts, CDN assets, tracking pixels).

---

## Critical Rendering Path

### Render-Blocking (Intentional, Small)

- `design-tokens.css` — required for all layout (custom properties)
- `barreletics-base.css` — required for typography and reset

Both files are intentionally small (<200 lines each), making the render-blocking cost minimal.

### Non-Render-Blocking

- **JS files** — loaded at the bottom of their containing section, not in `<head>`
- **Tracking scripts** — all load asynchronously (see below)
- **Google Fonts** — `display=swap` prevents blocking text paint

### Script Loading for Tracking

All tracking integrations load asynchronously via dedicated snippets rendered in `layout/theme.liquid`:

| Snippet | Script | Loading |
|---------|--------|---------|
| `analytics-head.liquid` | gtag.js | `async` attribute |
| `meta-pixel.liquid` | fbevents.js | Inline loader (non-blocking) |
| `pinterest-tag.liquid` | pintrk core.js | `async` attribute |
| `clarity.liquid` | clarity.js | `async` inline loader |
| `helpscout-beacon.liquid` | Help Scout embed | `async` (body) |
| `tidio-widget.liquid` | Tidio embed | `async` (body) |

All are conditionally gated — if the setting ID is blank, the snippet outputs nothing:

```liquid
{% if settings.ga4_measurement_id != blank %}
  <!-- GA4 script loads here -->
{% endif %}
```

---

## Shopify-Specific Optimizations

### Server-Side Rendering

Liquid templates render server-side on Shopify's infrastructure. The browser receives complete HTML — no client-side hydration step. This means:
- First Contentful Paint is HTML delivery time
- No JavaScript required for initial page display
- Search engines see full content without JS execution

### `content_for_header`

```liquid
{{ content_for_header }}
```

Required Shopify tag in `<head>` — includes Shopify's analytics, preview bar (for unpublished themes), and required platform scripts. Positioned last in `<head>` to not delay our critical CSS.

### Image CDN with `image_url` Filter

```liquid
{{ product.featured_image | image_url: width: 800 }}
```

The `image_url` filter generates URLs pointing to Shopify's CDN which:
- Automatically converts to WebP where supported
- Serves from edge nodes closest to the user
- Handles responsive resizing server-side
- Caches aggressively

---

## Performance Budget Summary

| Resource | Count | Loading |
|----------|-------|---------|
| Global CSS files | 2 | Render-blocking (small) |
| JS files | 2 | PDP only, bottom of section |
| Font families | 1 (Roboto) | `display=swap` |
| Preconnects | 5 | `<head>` |
| Tracking scripts | 6 max | All async, conditionally gated |
| Frameworks/libraries | 0 | — |

---

**Cross-references:**
- CSS architecture → `docs/07-css-architecture.md`
- JavaScript architecture → `docs/06-javascript-architecture.md`
- Design tokens → `docs/23-design-token-reference.md`
- Theme structure → `docs/02-theme-architecture.md`
