# 05 — Asset Library

All assets live in `shopify-build/assets/`. The theme uses exactly 4 asset files.

## File Inventory

| File | Type | Size Role | Load Location |
|---|---|---|---|
| `design-tokens.css` | CSS | Design system custom properties | Global — `<head>` via `theme.liquid` |
| `barreletics-base.css` | CSS | Reset, typography, utilities, components | Global — `<head>` via `theme.liquid` |
| `variant-selector.js` | JS | PDP variant selection controller | PDP only — `pdp-buy-box.liquid` |
| `cart.js` | JS | AJAX cart controller | PDP only — `pdp-buy-box.liquid` |

## CSS Load Order

Both CSS files load globally in `theme.liquid` `<head>` as `<link>` stylesheet tags:

```liquid
{{ 'design-tokens.css' | asset_url | stylesheet_tag }}
{{ 'barreletics-base.css' | asset_url | stylesheet_tag }}
```

`design-tokens.css` loads first — `barreletics-base.css` depends on its custom properties.

---

## `design-tokens.css`

Single `:root` block defining all CSS custom properties. Governed by `planning/03-design-system.md` and Decision Log entries D-001 through D-007.

### Color Palette

| Token | Value | Usage |
|---|---|---|
| `--color-charcoal` | `#1c1916` | Primary text, dark backgrounds, buttons |
| `--color-rust` | `#c45c3f` | Accent/CTA, badges, "not covered" indicators |
| `--color-gold` | `#d4af37` | Star ratings only |
| `--color-body` | `#4a4a4a` | Body text |
| `--color-muted` | `#8a8a8a` | Secondary/meta text |
| `--color-warm-muted` | `#6b645a` | Warm-toned muted text |
| `--color-warm-border` | `#d6cfc0` | Default borders |
| `--color-warm-cream` | `#f5f2ec` | Alternate/card backgrounds |
| `--color-light-bg` | `#f9f9f9` | Card/input backgrounds |
| `--color-white` | `#ffffff` | Primary background |
| `--color-coral` | `#e8927c` | Cart badge only |

### Semantic Aliases

| Token | Maps To |
|---|---|
| `--text-primary` | `--color-charcoal` |
| `--text-body` | `--color-body` |
| `--text-muted` | `--color-muted` |
| `--text-warm-muted` | `--color-warm-muted` |
| `--bg-primary` | `--color-white` |
| `--bg-alternate` | `--color-warm-cream` |
| `--bg-card` | `--color-light-bg` |
| `--bg-dark` | `--color-charcoal` |
| `--border-default` | `--color-warm-border` |
| `--accent-primary` | `--color-rust` |
| `--accent-stars` | `--color-gold` |

### Typography

| Token | Value |
|---|---|
| `--font-family` | `'Roboto', -apple-system, BlinkMacSystemFont, sans-serif` |
| `--weight-light` | 300 |
| `--weight-regular` | 400 |
| `--weight-medium` | 500 |
| `--weight-semibold` | 600 |
| `--weight-bold` | 700 |

**Font Size Scale:** `--text-xs` (10px) → `--text-8xl` (52px). See `design-tokens.css` lines 47–57 for exact values.

**Line Heights:** `--leading-tight` (1.08) through `--leading-loose` (1.7).

**Letter Spacing:** `--tracking-tight` (-0.02em) through `--tracking-brand` (0.14em). `--tracking-eyebrow` = 0.08em.

### Spacing

4px base unit: `--space-1` (4px) through `--space-16` (96px). Section padding: `--section-padding-y` (64px), `--section-padding-x` (40px), with mobile overrides (48px/16px).

### Layout

| Token | Value |
|---|---|
| `--max-width` | 1200px |
| `--max-width-hero` | 1400px |
| `--max-width-narrow` | 760px |
| `--max-width-copy` | 540px |
| `--grid-gap` | 28px |
| `--grid-gap-sm` | 20px |
| `--grid-gap-lg` | 40px |

### Border Radius (D-003, D-006)

| Token | Value | Usage |
|---|---|---|
| `--radius-badge` | 3px | Badges, size toggles |
| `--radius-button` | 6px | Buttons, inputs |
| `--radius-card-sm` | 6px | Small cards, dropdowns |
| `--radius-gallery` | 8px | Image containers |
| `--radius-card` | 12px | Cards |
| `--radius-swatch` | 50% | Color swatches |

### Shadows

| Token | Value |
|---|---|
| `--shadow-sm` | `0 1px 3px rgba(28,25,22,0.06)` |
| `--shadow-md` | `0 4px 16px rgba(28,25,22,0.08)` |
| `--shadow-lg` | `0 8px 32px rgba(28,25,22,0.12)` |

### Transitions

| Token | Value |
|---|---|
| `--transition-fast` | 0.2s ease |
| `--transition-base` | 0.3s ease |
| `--transition-slow` | 0.4s ease |
| `--transition-ticker` | 0.32s ease |

### Z-Index Scale

`--z-base` (0) → `--z-toast` (70). Key layers: `--z-sticky` (20), `--z-header` (40), `--z-modal` (60).

### Dark Mode Override

`[data-theme="dark"]` selector overrides semantic tokens for dark sections (white text, charcoal bg, transparent white borders).

---

## `barreletics-base.css`

Global stylesheet providing reset, typography scale, button system, section wrappers, grid utilities, accessibility helpers, and responsive breakpoints.

### Reset
Standard box-sizing reset, smooth scrolling, antialiased font rendering.

### Typography Classes

| Class | Size | Weight | Usage |
|---|---|---|---|
| `.h1` / `h1` | `--text-6xl` (44px) | bold | Page headings |
| `.h2` / `h2` | `--text-5xl` (40px) | bold | Section headings |
| `.h3` / `h3` | `--text-4xl` (36px) | bold | Subsection headings |
| `.h4` / `h4` | `--text-2xl` (28px) | bold | Card headings |
| `.body-lg` | `--text-md` (16px) | regular | Large body text |
| `.body` | `--text-base` (15px) | regular | Default body text |
| `.body-sm` | 14px | regular | Small body text |
| `.eyebrow` | `--text-sm` (11px) | bold | Uppercase labels |
| `.eyebrow--accent` | — | — | Rust-colored eyebrow |

### Button System

| Class | Appearance |
|---|---|
| `.btn` | Base: inline-flex, 16px 32px padding, 13px bold uppercase |
| `.btn--primary` | Charcoal bg, white text → rust on hover |
| `.btn--secondary` | Transparent, charcoal border → fills charcoal on hover |
| `.btn--inverted` | White bg, charcoal text |
| `.btn--full` | `width: 100%` |
| `.btn--lg` | 18px 36px padding, 15px font |
| `.btn--sm` | 10px 20px padding, 12px font |

### Section Wrappers

Documented in [Doc 04 — `section-wrapper.liquid`](04-snippet-library.md#section-wrapperliquid).

### Grid Utilities

| Class | Columns |
|---|---|
| `.grid` | Base: display grid, gap `--grid-gap` |
| `.grid--2` | 2 columns |
| `.grid--3` | 3 columns → 2 at 1024px → 1 at 768px |
| `.grid--4` | 4 columns → 2 at 1024px → 1 at 768px |

### Focus Indicators (WCAG 2.1 AA)

`:focus-visible` — 2px solid charcoal outline, 2px offset. Dark sections use white outline. `:focus:not(:focus-visible)` removes outline for mouse users.

### Accessibility Helpers

| Class | Purpose |
|---|---|
| `.visually-hidden` | Screen-reader-only content |
| `.skip-link` | Skip to main content — hidden until focused |

### Other Utilities

| Class | Purpose |
|---|---|
| `.badge` | Rust background pill (10px text, uppercase) |
| `.stars` | Gold star rating text (14px, 0.12em spacing) |
| `.stars--lg` | 18px star rating |

### Responsive Breakpoints

| Breakpoint | Effect |
|---|---|
| `≤1024px` | `.grid--4` and `.grid--3` → 2 columns |
| `≤768px` | Section padding reduces (48px/16px). Headings scale down. All grids → 1 column. |

### Reduced Motion

`@media (prefers-reduced-motion: reduce)` — all animations/transitions set to 0.01ms, scroll-behavior: auto.

---

## `variant-selector.js`

PDP variant selection controller. ~190 lines. IIFE, `'use strict'`.

**Loaded by:** `pdp-buy-box.liquid` via `{{ 'variant-selector.js' | asset_url | script_tag }}`

**Expects:** `window.__pdpProduct` — full Shopify product JSON, set by `pdp-buy-box.liquid`:
```liquid
<script>window.__pdpProduct = {{ product | json }};</script>
```

### Behavior

1. **Init:** Reads product options (Color, Size), binds click handlers to swatches (`.pdp-buy__swatch`) and size buttons (`.pdp-buy__size-btn`).
2. **Option selection:** Updates `is-active` class and `aria-selected` attribute on the clicked element's group. Updates `#selected-color` text for Color option.
3. **Variant resolution:** Iterates `product.variants` to find the variant matching all selected options.
4. **DOM updates on match:**
   - Hidden `input[name="id"]` → variant ID
   - `.pdp-buy__price-now` → formatted price
   - `.pdp-buy__cta` → "Add to Cart — $X" or "Sold Out" (disabled)
   - `#pdp-main-img` → variant's featured image (src + srcset)
   - URL → `?variant={id}` via `history.replaceState`
5. **Availability:** Cross-checks Color × Size combos. Marks unavailable sizes with `.is-unavailable` (35% opacity, strikethrough, disabled).
6. **Custom event:** Dispatches `variant:changed` with `{ variant, product }` detail. Consumed by `sticky-atc.liquid` and `analytics-events.liquid`.

### Key Functions

| Function | Purpose |
|---|---|
| `resolveVariant()` | Match selected options → variant object |
| `updateVariant()` | Sync price, CTA, image, URL, dispatch event |
| `updateAvailability()` | Disable unavailable size buttons |
| `formatMoney(cents)` | `$X.XX` formatting (drops `.00`) |
| `getSizedUrl(src, width)` | Shopify CDN image resizing |

---

## `cart.js`

AJAX cart controller. ~325 lines. IIFE, `'use strict'`.

**Loaded by:** `pdp-buy-box.liquid` via `{{ 'cart.js' | asset_url | script_tag }}`

### Public API — `window.BarreleticsCart`

| Method | Signature | Description |
|---|---|---|
| `add` | `(variantId, quantity) → Promise` | POST `/cart/add.js`, re-fetch cart, render drawer, open drawer |
| `fetch` | `() → Promise` | GET `/cart.js` |
| `change` | `(lineKey, quantity) → Promise` | POST `/cart/change.js` (set to 0 to remove) |
| `open` | `() → void` | Open cart drawer, trap focus |
| `close` | `() → void` | Close cart drawer, restore focus |

### Cart Drawer Rendering

`renderDrawer(cart)` rebuilds `#cart-drawer-items` innerHTML from cart JSON:
- Line items with image, title, variant, quantity +/- buttons, price, remove button
- Empty state: "Your cart is empty" + Shop CTA
- Updates `#cart-subtotal` text
- Calls `updateShippingBar(totalCents)` — fills progress bar toward `FREE_SHIPPING_THRESHOLD` (15000 cents = $150)
- Re-binds all drawer controls after each render

### Form Interception

Binds to `#pdp-form` submit event, prevents default, calls `addToCart()`. Shows "Adding…" state on button.

### Keyboard Handling

- **Escape:** Closes drawer
- **Tab:** Focus trap within `.cart-drawer__panel` (wraps first ↔ last focusable element)

### Accessibility

- Creates `#cart-live-region` (`aria-live="polite"`) for announcing "Item added to cart" / "Cart updated" / "Item removed from cart"
- Cart drawer uses `role="dialog"`, `aria-modal="true"`, `aria-hidden` toggle
- Returns focus to trigger element on close

### Custom Event

`cart:item-added` is expected by `analytics-events.liquid`, `meta-pixel.liquid`, and `pinterest-tag.liquid` for tracking. The event is dispatched by the Shopify cart API response — consuming sections fire tracking accordingly.

---

## Image & Font Requirements

### Fonts

**Roboto** — loaded from Google Fonts in `theme.liquid` `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```

Weights used: 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold), 800 (extra-bold — sock math headlines).

### Expected Theme Assets

| Asset | Usage |
|---|---|
| `og-default.jpg` | Open Graph fallback image (set via `settings.og_default_image` or referenced in `theme.liquid`) |
| `logo.png` | Referenced by `organization-schema.liquid`, `article-schema.liquid`, and Organization JSON-LD in `theme.liquid` |

### Image Handling

All product/content images use Shopify's CDN with responsive `srcset`:
- Widths: typically 400w, 600w, 800w (PDP) or 600w, 900w, 1200w (hero/split)
- `sizes` attribute tuned per-component
- Hero and gallery images: `loading="eager"`, `fetchpriority="high"`
- All other images: `loading="lazy"`
- Product card images: `width="600" height="600"` for aspect-ratio hints
