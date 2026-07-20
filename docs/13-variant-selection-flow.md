# 13 — Variant Selection Flow

> Step-by-step walkthrough of how option clicks resolve to Shopify variants and update the buy box.
> Source files: `assets/variant-selector.js`, `sections/pdp-buy-box.liquid`

---

## Overview

```
Page load → window.__pdpProduct (JSON) → variant-selector.js init()
  → Build state.options from active swatches/buttons
  → User clicks swatch/size → selectOption() → resolveVariant() → updateVariant()
  → updateAvailability() disables unavailable sizes
```

---

## Step 1: Page Load — Liquid Renders Product JSON

`pdp-buy-box.liquid` (line 536) renders the product object as a global:

```html
<script>
  window.__pdpProduct = {{ product | json }};
</script>
```

Then loads the controller:

```html
{{ 'variant-selector.js' | asset_url | script_tag }}
```

The Liquid template also renders the initial buy box HTML using `product.selected_or_first_available_variant`:
- Hidden input: `<input type="hidden" name="id" value="{{ current_variant.id }}">`
- CTA text: `Add to Cart — {{ current_variant.price | money }}`
- Price: `.pdp-buy__price-now` shows `{{ current_variant.price | money }}`
- Color swatches: `.pdp-buy__swatch[data-color]` with `.is-active` and `aria-selected` on selected value
- Size buttons: `.pdp-buy__size-btn[data-size]` with `.is-active` on selected value

This means the page is functional without JS (form submits to `/cart/add` with the default variant ID).

---

## Step 2: Init — Build State and Bind Events

`variant-selector.js` runs as an IIFE. Guard: exits immediately if `!product || !product.variants`.

### DOM element cache (`els`)

| Key | Selector | Purpose |
|-----|----------|---------|
| `form` | `#pdp-form` | ATC form |
| `variantInput` | `#pdp-form input[name="id"]` | Hidden variant ID |
| `priceNow` | `.pdp-buy__price-now` | Current price display |
| `ctaBtn` | `.pdp-buy__cta` | Add to Cart button |
| `mainImg` | `#pdp-main-img` | Hero product image |
| `selectedColor` | `#selected-color` | Color name label |
| `swatches` | `.pdp-buy__swatch` (all) | Color swatch buttons |
| `sizeBtns` | `.pdp-buy__size-btn` (all) | Size option buttons |

### State initialization

`init()` iterates `product.options` (array of option names like `['Color', 'Size']`). For each option:

1. Computes `position = index + 1` (Shopify uses 1-indexed option positions)
2. Finds DOM container via `[data-option-position="N"]`
3. If container not found → skip (handles single-variant products with no option UI)
4. Reads current active value via `getActiveValue(container, selector, attr)` — finds element with `.is-active` class, returns its data attribute value
5. Stores in `state.options[position]`
6. Binds click listeners on each swatch/button → calls `selectOption()`

After binding, calls `updateVariant()` and `updateAvailability()` for initial state.

---

## Step 3: Color Swatch Click

User clicks `.pdp-buy__swatch[data-color="Sage"]`:

```
click → selectOption(position, "Sage", container, '.pdp-buy__swatch', 'data-color')
```

### `selectOption(position, value, container, selector, attr)`

1. Iterates all elements matching `selector` within `container`
2. For each: `match = el.getAttribute(attr) === value`
3. Toggles `.is-active` class based on match
4. If element has `aria-selected` attribute, sets it to `"true"` or `"false"`
5. Sets `state.options[position] = value`
6. If position matches the Color option position and `els.selectedColor` exists, updates `#selected-color` textContent to the new value
7. Calls `updateVariant()`
8. Calls `updateAvailability()`

---

## Step 4: Size Button Click

User clicks `.pdp-buy__size-btn[data-size="L"]`:

```
click → selectOption(position, "L", container, '.pdp-buy__size-btn', 'data-size')
```

Same `selectOption()` flow as color. Size buttons do not have `aria-selected` — they use `aria-disabled` for availability state (set by `updateAvailability()`).

---

## Step 5: `resolveVariant()`

Builds a `selected` array from `state.options` in position order (1, 2, ... N).

Iterates `product.variants`. For each variant, compares `variant.options[j]` against `selected[j]` for all option positions. Returns the first variant where all options match.

Returns `null` if no variant matches (defensive — should not happen with valid product data).

```
state.options = { 1: "Sage", 2: "L" }
selected = ["Sage", "L"]

product.variants.forEach → compare variant.options === ["Sage", "L"]
  → match found → return variant object
```

---

## Step 6: `updateVariant()`

Called after every option change. If `resolveVariant()` returns `null`, exits early (no DOM changes).

| Action | Target | Detail |
|--------|--------|--------|
| Set variant ID | `#pdp-form input[name="id"]` | `variant.id` |
| Update price | `.pdp-buy__price-now` | `formatMoney(variant.price)` — e.g. `$42` |
| Update CTA (available) | `.pdp-buy__cta` | text: `"Add to Cart — $42"`, `disabled=false`, removes `.btn--disabled` |
| Update CTA (unavailable) | `.pdp-buy__cta` | text: `"Sold Out"`, `disabled=true`, adds `.btn--disabled` |
| Swap image | `#pdp-main-img` | `src` = variant.featured_image.src, `srcset` rebuilt at 400w/600w/800w via `getSizedUrl()` |
| Update URL | browser address bar | `history.replaceState` sets `?variant=VARIANT_ID` via `updateUrl()` |
| Dispatch event | `document` | `new CustomEvent('variant:changed', { detail: { variant, product } })` |

### `formatMoney(cents)`

Converts cents integer to display string: `'$' + (cents / 100).toFixed(2).replace(/\.00$/, '')`. Examples: `4200 → "$42"`, `4250 → "$42.50"`.

### `getSizedUrl(src, width)`

Transforms Shopify CDN URLs to request specific widths: replaces pattern `.(ext)` with `_WIDTHx.(ext)`.

---

## Step 7: `updateAvailability()`

Determines which size buttons should be disabled based on the currently selected color.

1. Finds the position index for "Color" and "Size" options via `product.options` array
2. If no "Size" option exists, returns (nothing to disable)
3. For each `.pdp-buy__size-btn`:
   - Gets the button's `data-size` value
   - Checks if **any** variant exists where: `colorMatch && sizeMatch && variant.available`
   - `colorMatch`: if no color option, always true; otherwise `variant.options[colorPos - 1] === state.options[colorPos]`
   - If no available variant: adds `.is-unavailable`, sets `disabled=true`, sets `aria-disabled="true"`
   - If available: removes `.is-unavailable`, sets `disabled=false`, sets `aria-disabled="false"`

### Visual result of `.is-unavailable`

```css
.pdp-buy__size-btn.is-unavailable {
  opacity: 0.35;
  cursor: not-allowed;
  text-decoration: line-through;
}
```

---

## Step 8: Edge Cases

| Scenario | Behavior |
|----------|----------|
| Single-variant product | `product.has_only_default_variant == true` in Liquid → option containers not rendered → `init()` finds no `[data-option-position]` containers → skips binding, still calls `updateVariant()` with default variant |
| All sizes unavailable for a color | Every `.pdp-buy__size-btn` gets `.is-unavailable` + `disabled=true`. If user already had a size selected, `resolveVariant()` still returns the (unavailable) variant → CTA shows "Sold Out" |
| No matching variant | `resolveVariant()` returns `null` → `updateVariant()` exits early → no DOM changes, previous state preserved |
| URL has `?variant=` param | Shopify Liquid uses it to set `product.selected_or_first_available_variant` → HTML renders with correct initial state → `init()` reads `.is-active` elements → state matches URL |

---

## Step 9: Accessibility

| Element | Attribute | Behavior |
|---------|----------|----------|
| Color swatches | `aria-selected="true/false"` | Toggled by `selectOption()` |
| Color swatches | `aria-label="{{ value }}"` | Color name announced (e.g. "Sage") |
| Size buttons | `aria-disabled="true/false"` | Set by `updateAvailability()` |
| CTA button | text content | Screen reader announces "Add to Cart — $42" or "Sold Out" on change |
| URL | `?variant=` | Updated via `replaceState` — does not trigger navigation/announcement |
| `variant:changed` | CustomEvent | Other components (analytics, sticky ATC) can listen and respond |

---

## Cross-references

- Product data JSON origin → [12-data-flow.md](./12-data-flow.md)
- Cart add flow after CTA click → [14-cart-flow.md](./14-cart-flow.md)
- Analytics events fired on variant change → [15-analytics-architecture.md](./15-analytics-architecture.md)
- Buy box component spec → [05-PDP-ARCHITECTURE.md](./05-PDP-ARCHITECTURE.md)
