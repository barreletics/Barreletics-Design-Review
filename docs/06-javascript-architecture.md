# 06 — JavaScript Architecture

## Philosophy

The theme ships zero frameworks — no jQuery, no React, no bundler. All JavaScript is vanilla ES5-compatible, written as IIFEs for scope isolation. Forms degrade gracefully: the `#pdp-form` POSTs to `/cart/add` natively; JS enhances it with AJAX.

## File Inventory

| File | Pattern | Scope | Loaded by |
|------|---------|-------|-----------|
| `assets/variant-selector.js` | IIFE | PDP only | `{{ 'variant-selector.js' \| asset_url \| script_tag }}` in `sections/pdp-buy-box.liquid` |
| `assets/cart.js` | IIFE | PDP only (cart drawer available globally via layout) | `{{ 'cart.js' \| asset_url \| script_tag }}` in `sections/pdp-buy-box.liquid` |
| Inline `<script>` in `sections/pdp-buy-box.liquid` | IIFE | PDP | Accordion toggle + product JSON assignment |
| Inline `<script>` in `snippets/header-nav.liquid` | IIFE | All pages | Scroll detection, mobile menu |
| Inline `<script>` in `snippets/announcement-strip.liquid` | IIFE | All pages | Slide rotation |
| Inline `<script>` in `snippets/cart-drawer.liquid` | IIFE | All pages | Cart trigger click binding |
| Inline `<script>` in `snippets/sticky-atc.liquid` | IIFE | PDP | IntersectionObserver + variant sync |

Both `variant-selector.js` and `cart.js` are loaded at the bottom of `sections/pdp-buy-box.liquid` (lines 540–541), so they only execute on product pages.

---

## `variant-selector.js`

### Data Source

The script reads `window.__pdpProduct`, set by an inline `<script>` in `pdp-buy-box.liquid`:

```liquid
window.__pdpProduct = {{ product | json }};
```

If `window.__pdpProduct` or `.variants` is falsy, the IIFE returns immediately.

### State

```js
var state = {
  options: {}   // keyed by Shopify option position (1-based)
};
```

### DOM Element References (`els` object)

| Key | Selector | Purpose |
|-----|----------|---------|
| `form` | `#pdp-form` | The add-to-cart form |
| `variantInput` | `#pdp-form input[name="id"]` | Hidden input holding the active variant ID |
| `priceNow` | `.pdp-buy__price-now` | Displayed price |
| `ctaBtn` | `.pdp-buy__cta` | "Add to Cart" button |
| `mainImg` | `#pdp-main-img` | Hero product image |
| `selectedColor` | `#selected-color` | Color name label next to "Color ·" |
| `swatches` | `.pdp-buy__swatch` (NodeList) | Color swatch buttons |
| `sizeBtns` | `.pdp-buy__size-btn` (NodeList) | Size option buttons |

### Functions

| Function | Signature | Responsibility |
|----------|-----------|----------------|
| `init()` | `()` | Iterates `product.options`, binds click listeners on swatches/sizes, calls `updateVariant()` and `updateAvailability()` |
| `getActiveValue()` | `(container, selector, attr)` | Returns the `attr` value of the `.is-active` element inside `container` |
| `selectOption()` | `(position, value, container, selector, attr)` | Toggles `.is-active` on option buttons, updates `state.options[position]`, updates color label, calls `updateVariant()` + `updateAvailability()` |
| `getColorPosition()` | `()` | Returns the 1-based position of the "Color" option, or `-1` |
| `resolveVariant()` | `()` | Builds a selected-options array from `state.options`, iterates `product.variants` to find a match. Returns the variant object or `null` |
| `updateVariant()` | `()` | Calls `resolveVariant()`, then updates: hidden input value, price text, CTA text/disabled state, main image `src`/`srcset`, URL query param. Dispatches `variant:changed` event |
| `updateAvailability()` | `()` | For each size button, checks if any variant matching the current color + that size is `available`. Toggles `.is-unavailable` class and `disabled`/`aria-disabled` attributes |
| `updateUrl()` | `(variantId)` | Uses `history.replaceState` to set `?variant=<id>` without navigation |
| `formatMoney()` | `(cents)` | Returns `$X.XX` (strips `.00`). Cents ÷ 100 |
| `getSizedUrl()` | `(src, width)` | Inserts `_<width>x` before the file extension for Shopify CDN resizing |

### Initialization

```
DOMContentLoaded (or immediate if DOM ready)
  └─ init()
       ├─ bind click listeners per option
       ├─ updateVariant()
       └─ updateAvailability()
```

---

## `cart.js`

### Constants

```js
var FREE_SHIPPING_THRESHOLD = 15000;  // $150 in cents
```

### Public API (`window.BarreleticsCart`)

| Method | Maps to | Signature |
|--------|---------|-----------|
| `.add()` | `addToCart` | `(variantId, quantity)` → Promise |
| `.fetch()` | `fetchCart` | `()` → Promise |
| `.change()` | `changeItem` | `(lineKey, quantity)` → Promise |
| `.open()` | `openDrawer` | `()` |
| `.close()` | `closeDrawer` | `()` |

### `addToCart(variantId, quantity)`

1. POST `/cart/add.js` with `{ id, quantity }`
2. Calls `fetchCart()` to get updated cart state
3. `renderDrawer(cart)` — rebuilds drawer HTML
4. `updateCartCount(cart.item_count)` — updates all `[data-cart-count]` badges
5. `announce('Item added to cart')` — sets `aria-live` region text
6. `openDrawer()` — slides drawer in

### `fetchCart()`

GET `/cart.js` → returns parsed JSON cart object.

### `changeItem(lineKey, quantity)`

POST `/cart/change.js` with `{ id: lineKey, quantity }`. Re-renders drawer, updates count, announces change. Quantity `0` removes the item.

### Drawer Open/Close

- `openDrawer()`: adds `.is-open` to `#cart-drawer`, sets `aria-hidden="false"`, locks body scroll, moves focus into drawer, stores `triggerEl` for focus restoration.
- `closeDrawer()`: removes `.is-open`, restores `aria-hidden="true"`, unlocks scroll, returns focus to `triggerEl`.

### Rendering (`renderDrawer`)

Rebuilds `#cart-drawer-items` innerHTML from the cart JSON. Empty state links to `/collections/grippy-shoes`. Each item renders with `[data-line-key]`, quantity ±1 buttons (`[data-qty-change]`), and a remove button (`[data-remove-item]`). Updates `#cart-subtotal` and calls `updateShippingBar()`.

### `updateShippingBar(totalCents)`

Calculates fill percentage against `FREE_SHIPPING_THRESHOLD` (15000 cents = $150). Sets `#shipping-fill` width and `#shipping-text` message.

### `updateCartCount(count)`

Finds all `[data-cart-count]` elements, sets their `textContent` to count, hides them when count is 0.

### Event Binding

**`bindAddToCartForms()`** — intercepts `#pdp-form` submit:
1. `e.preventDefault()`
2. Disables CTA, sets text to "Adding…"
3. Calls `addToCart(parseInt(idInput.value, 10), 1)`
4. On error, appends `.pdp-buy__error` with `role="alert"` (auto-removed after 5 s)
5. Restores CTA text on `.finally()`
6. Uses `data-ajaxBound` flag to prevent double-binding

**`bindDrawerControls()`** — binds qty ±, remove, and close buttons inside `#cart-drawer`. Uses `data-bound` flags; re-called after `renderDrawer()` to bind new DOM.

### Accessibility

- **`aria-live` region**: `#cart-live-region` (`.visually-hidden`, `aria-live="polite"`, `aria-atomic="true"`) — `announce(message)` sets its `textContent`
- **Focus trap**: on `Tab`/`Shift+Tab` inside `.cart-drawer__panel`, wraps focus between first and last focusable element
- **Escape**: closes drawer

### Error Display

`showError(form, message)` appends a `<p class="pdp-buy__error" role="alert">` to the form, auto-removed via `setTimeout` after 5 s.

---

## Custom Event System

### `variant:changed`

Dispatched by `variant-selector.js` → `updateVariant()`:

```js
document.dispatchEvent(new CustomEvent('variant:changed', {
  detail: { variant: variant, product: product }
}));
```

**Listeners:**
- `snippets/sticky-atc.liquid` inline script — updates sticky bar price, size label, variant ID, thumbnail, CTA text/disabled state
- `snippets/analytics-events.liquid` — (indirectly, the variant data flows into the next add-to-cart)

### `cart:item-added`

Referenced in analytics snippets (`snippets/analytics-events.liquid`, `snippets/meta-pixel.liquid`, `snippets/pinterest-tag.liquid`). Listeners fire `add_to_cart` (GA4), `AddToCart` (Meta Pixel), and `addtocart` (Pinterest) events using `e.detail` item data.

### Click Delegation in Analytics

`snippets/analytics-events.liquid` uses `document.addEventListener('click', ...)` with `closest()` checks:

| Selector | GA4 Event |
|----------|-----------|
| `[data-checkout-button]`, `[name="checkout"]` | `begin_checkout` |
| `[data-size-option]` | `size_selector_click` |
| `[data-sticky-atc]` | `sticky_atc_click` |
| `[data-cart-trigger]` | `cart_drawer_open` |

---

## Inline Scripts

### `sections/pdp-buy-box.liquid`

Two inline scripts:

1. **Accordion toggle** — listens for `toggle` event on each `[data-pdp-accordion]` `<details>` element, syncs `aria-expanded` on the `<summary>`.

2. **Product JSON** — `window.__pdpProduct = {{ product | json }};` — makes the full Shopify product object available to `variant-selector.js`.

### `snippets/header-nav.liquid`

| Feature | Implementation |
|---------|---------------|
| Scroll detection | `window.addEventListener('scroll', checkScroll, { passive: true })`. Toggles `.is-scrolled` on `[data-site-header]` when `scrollY > 8` |
| Mobile menu open | `[data-mobile-menu-toggle]` click → adds `.is-open` to `[data-mobile-menu]`, sets `aria-hidden="false"`, `aria-expanded="true"`, locks body scroll |
| Mobile menu close | `[data-mobile-menu-close]` click or `Escape` key → removes `.is-open`, restores `aria-hidden`, `aria-expanded`, body scroll |
| Parent item accordion | `.mobile-menu__toggle` click → toggles `data-expanded` attribute on `.mobile-menu__item--parent`, syncs `aria-expanded` |

### `snippets/announcement-strip.liquid`

- Rotates slides every 4000 ms via `setInterval`
- Toggles `.is-active` class between `[data-slide-index]` elements
- `paused` flag set on `mouseenter`/`mouseleave`
- If `window.matchMedia('(prefers-reduced-motion: reduce)').matches` is true, the rotation never starts — first slide remains static

### `snippets/cart-drawer.liquid`

Binds click on all `[data-cart-trigger]` elements (the cart icon in the header). Calls `e.preventDefault()` then `window.BarreleticsCart.open()`.

### `snippets/sticky-atc.liquid`

| Feature | Implementation |
|---------|---------------|
| Show/hide | `IntersectionObserver` watches `[data-buy-box]`. When the buy box exits the viewport, adds `.is-visible` and sets `aria-hidden="false"` on `#sticky-atc` |
| Variant sync | Listens for `variant:changed` custom event. Updates `#sticky-atc-btn` variant ID, price, disabled/text state. Updates `.sticky-atc__price` and `#sticky-atc-size` text. Updates `.sticky-atc__thumb` src |
| Add to cart | `#sticky-atc-btn` click → `window.BarreleticsCart.add(vid, 1)`. Shows "Adding…" while pending |

---

## Script Loading Strategy

```
layout/theme.liquid
  <head>
    └─ analytics-head.liquid (gtag.js, async)
    └─ meta-pixel.liquid (fbevents.js, async)
    └─ pinterest-tag.liquid (core.js, async)
    └─ clarity.liquid (clarity tag, async)
  </head>
  <body>
    └─ announcement-strip.liquid  → inline <script> (IIFE)
    └─ header-nav.liquid          → inline <script> (IIFE)
    └─ {{ content_for_layout }}
    │   └─ [on PDP] pdp-buy-box.liquid
    │       ├─ inline <script> (accordion toggle)
    │       ├─ inline <script> (window.__pdpProduct)
    │       ├─ {{ 'variant-selector.js' | asset_url | script_tag }}
    │       └─ {{ 'cart.js' | asset_url | script_tag }}
    │   └─ [on PDP] sticky-atc.liquid → inline <script> (IIFE)
    └─ cart-drawer.liquid         → inline <script> (IIFE)
    └─ analytics-events.liquid    → inline <script> (IIFE)
    └─ helpscout-beacon.liquid    → external script (async)
    └─ tidio-widget.liquid        → external script (async)
  </body>
```

All external asset scripts (`variant-selector.js`, `cart.js`) use `{{ '...' | asset_url | script_tag }}` which produces a synchronous `<script>` tag. They execute in document order after the product JSON assignment above them.

---

## Cross-References

- Product data flow and variant selection UX → [10-pdp-architecture-reference.md](10-pdp-architecture-reference.md)
- Design tokens used in JS-toggled classes → [07-css-architecture.md](07-css-architecture.md)
- Theme settings consumed by analytics scripts → [08-theme-settings-reference.md](08-theme-settings-reference.md)
