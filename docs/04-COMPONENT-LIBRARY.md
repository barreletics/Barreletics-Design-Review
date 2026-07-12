# Component Library

**Status:** Draft  
**Purpose:** Reusable components, patterns, and usage guidelines

---

## Interactions & Behavior

| Component | Behavior |
|---|---|
| **Ticker** | 3-slide auto-rotator, 4s interval, opacity crossfade 320ms ease. Pause on hover. `ticker.js`. |
| **Header** | Sticky on scroll. Adds a 1px bottom hairline (`--br-line`) on scroll > 8px. Cart badge dot (`--br-accent`) visible only when items > 0. |
| **Hero CTAs** | Primary: `Shop performance skins` → Collection. Secondary: `See how it grips` → in-page anchor `#why-it-works`. |
| **Sock ⇄ Skin toggle** | Cross-fade between two image states + swap two stat figures. 240ms ease-out. State persists via aria-pressed. |
| **Variant card hover** | Image scales 1.02 over 320ms ease-out. Caption underline draws in. |
| **PDP gallery** | Click thumbnail → swap main. Pinch/double-tap to zoom on touch. Keyboard ←/→ to advance. |
| **PDP size picker** | Size pills toggle aria-pressed; out-of-stock = strikethrough + cursor not-allowed. |
| **Accordion (PDP specs)** | One open at a time. 200ms height transition. |
| **Reviews "Load more"** | Append next 6 reviews; no full pagination. |
| **Collection filter row** | Inline chips, multi-select within a facet, exclusive between facets. URL-syncs via query params. |
| **Article pull-quotes** | Static. No animation. |

**Reduced motion.** All animations gate on `@media (prefers-reduced-motion: no-preference)`. Final state must be visible without animation.

---

## Buttons

One primary, one secondary, one tertiary. No drop shadows, no gradients, no rounded corners.

```
--btn-text-size: 14px;
--btn-pad-y:     14px;
--btn-pad-x:     28px;
--btn-radius:    0px;    /* square, matches Shopify "button_style":"square" */
--btn-letter:    0.06em;
--btn-weight:    600;
```

Variants: `primary` = ink fill / white text; `secondary` = ink outline / ink text on bg; `tertiary` = text + arrow, no border.

---

## Hairlines & Radii

Borders are 1px solid `--br-line`. Cards have **no radius** by default. Where the matured direction uses radius (rare), it is 2px or 4px — never the 12–16px pill-card look from the live site.

---

## Component Sections

### Ticker
- 3-slide auto-rotator
- 4s interval
- Opacity crossfade 320ms ease
- Pause on hover
- Implemented via `ticker.js`

### Header
- Sticky on scroll
- Centered logo nav with category links left, account + cart right
- 1px bottom hairline (`--br-line`) adds on scroll > 8px
- Cart badge dot (`--br-accent`) visible only when items > 0

### Hero CTAs
- Primary CTA: "Shop performance skins" → Collection
- Secondary CTA: "See how it grips" → in-page anchor `#why-it-works`

### Sock ⇄ Skin Toggle
- Cross-fade between two image states
- Swap two stat figures on toggle
- 240ms ease-out transition
- State persists via aria-pressed

### Variant Card Hover
- Image scales 1.02x
- 320ms ease-out transition
- Caption underline draws in

### PDP Gallery
- Click thumbnail to swap main image
- Pinch/double-tap to zoom on touch devices
- Keyboard ←/→ to navigate

### PDP Size Picker
- Size pills toggle aria-pressed state
- Out-of-stock pills: strikethrough + cursor not-allowed

### Accordion (PDP Specs)
- One section open at a time
- 200ms height transition

### Reviews Load More
- Append next 6 reviews
- No full pagination

### Collection Filter Row
- Inline chips (not sidebar)
- Multi-select within a facet
- Exclusive between facets
- URL-syncs via query params

### Article Pull-Quotes
- Static (no animation)
