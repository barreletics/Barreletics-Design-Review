# 14 — Cart Flow

> End-to-end AJAX cart: add-to-cart, drawer rendering, quantity management, free shipping bar, focus trap, error handling.
> Source files: `assets/cart.js`, `snippets/cart-drawer.liquid`, `sections/pdp-buy-box.liquid`

---

## Architecture

`cart.js` runs as an IIFE and exposes `window.BarreleticsCart` with public methods. The cart drawer is server-rendered by `cart-drawer.liquid` (included in `layout/theme.liquid`) and dynamically re-rendered by `renderDrawer()` after every cart mutation.

```
window.BarreleticsCart = {
  add:    addToCart(variantId, quantity),
  fetch:  fetchCart(),
  change: changeItem(lineKey, quantity),
  open:   openDrawer(),
  close:  closeDrawer()
}
```

---

## Add to Cart Flow

### Trigger

User clicks `.pdp-buy__cta` (the submit button inside `form#pdp-form`).

### Sequence

```
1. form#pdp-form submit event fires
   │
2. bindAddToCartForms() handler calls e.preventDefault()
   │  (guard: form.dataset.ajaxBound prevents double-binding)
   │
3. Button state: disabled=true, text="Adding…"
   │
4. addToCart(parseInt(idInput.value, 10), 1)
   │
   ├── POST /cart/add.js
   │   headers: { 'Content-Type': 'application/json' }
   │   body: { id: variantId, quantity: 1 }
   │
   ├── if !res.ok → throw Error('add-to-cart-failed')
   │
   ├── fetchCart()
   │   └── GET /cart.js  headers: { 'Accept': 'application/json' }
   │       └── returns full cart JSON
   │
   ├── renderDrawer(cart)
   ├── updateCartCount(cart.item_count)
   ├── announce('Item added to cart')
   └── openDrawer()
   │
5. .finally(): restore button text + disabled=false
   │
6. .catch(): showError(form, 'This item is currently unavailable')
```

### Button text restoration

In `.finally()`, the button checks `btn.getAttribute('data-price')` for stored price text. Falls back to `'Add to Cart'` if no price attribute exists.

---

## Cart Drawer Structure (`snippets/cart-drawer.liquid`)

```html
#cart-drawer (role="dialog", aria-modal="true", aria-hidden="true")
  ├── .cart-drawer__overlay [data-cart-close]
  └── aside.cart-drawer__panel
        ├── header.cart-drawer__header
        │     ├── h2.cart-drawer__title "Your Cart"
        │     └── button.cart-drawer__close [data-cart-close]
        ├── .cart-drawer__shipping-bar
        │     ├── .cart-drawer__shipping-progress
        │     │     └── #shipping-fill (width set by JS)
        │     └── #shipping-text
        ├── #cart-drawer-items (body, overflow-y: auto)
        │     ├── (empty state) .cart-drawer__empty
        │     │     └── "Your cart is empty" + "Shop Grippy Shoes" btn
        │     └── (items) .cart-drawer__item [data-line-key]
        │           ├── .cart-drawer__item-img (linked product image)
        │           ├── .cart-drawer__item-details
        │           │     ├── .cart-drawer__item-title
        │           │     ├── .cart-drawer__item-variant
        │           │     └── .cart-drawer__item-qty (−/span/+ buttons)
        │           └── .cart-drawer__item-right
        │                 ├── .cart-drawer__item-price
        │                 └── .cart-drawer__item-remove [data-remove-item]
        └── footer.cart-drawer__footer
              ├── .cart-drawer__subtotal (label + #cart-subtotal)
              ├── a.cart-drawer__view-cart (href="/cart")
              └── a.cart-drawer__checkout (href="/checkout", btn--primary)
```

Drawer slides in from the right. Panel: `width: 420px`, `max-width: 90vw`, `transform: translateX(100%)` → `translateX(0)` on `.is-open`.

---

## Rendering Cycle

### `renderDrawer(cart)`

Called after every `/cart/add.js` or `/cart/change.js` response.

**Empty cart** (`cart.item_count === 0`):
- Replaces `#cart-drawer-items` innerHTML with `.cart-drawer__empty` div containing "Your cart is empty" + `<a href="/collections/grippy-shoes" class="btn btn--primary">Shop Grippy Shoes</a>`
- Hides `.cart-drawer__footer` via `footer.style.display = 'none'`

**Cart with items:**
- Builds HTML string by iterating `cart.items`. For each item:
  - Image: `getSizedUrl(item.image, 160)`, 80×80px, lazy loaded
  - Title: `item.product_title` (escaped)
  - Variant: `item.variant_title` (escaped)
  - Quantity controls: `[data-qty-change="-1"]` and `[data-qty-change="1"]` buttons with current qty in `<span>`
  - Price: `formatMoney(item.final_line_price)`
  - Remove: `[data-remove-item]` button with `aria-label="Remove {title}"`
- Injects HTML into `#cart-drawer-items`
- Shows footer: `footer.style.display = ''`
- Updates `#cart-subtotal` with `formatMoney(cart.total_price)`
- Calls `updateShippingBar(cart.total_price)`
- Calls `bindDrawerControls()` to re-attach event listeners on new DOM

---

## Quantity Update

### Trigger

Click `[data-qty-change]` button (±1 delta).

### Sequence

```
1. Click handler reads data-qty-change delta (parseInt)
2. Finds parent [data-line-key] element → extracts line key
3. Reads current quantity from .cart-drawer__item-qty span (parseInt)
4. newQty = Math.max(0, currentQty + delta)
5. changeItem(key, newQty)
   │
   ├── POST /cart/change.js { id: key, quantity: newQty }
   │
   ├── renderDrawer(cart)
   ├── updateCartCount(cart.item_count)
   └── announce(newQty === 0 ? 'Item removed from cart' : 'Cart updated')
```

If `newQty` computes to 0 (e.g., decrementing from 1), the item is removed.

---

## Item Removal

Click `[data-remove-item]` → finds parent `[data-line-key]` → calls `changeItem(key, 0)`. Same flow as quantity update with quantity=0.

---

## Free Shipping Bar

### `updateShippingBar(totalCents)`

| Cart Total | Bar Width | Text |
|-----------|-----------|------|
| $0 | 0% | "$150.00 away from free shipping" |
| $75 | 50% | "$75.00 away from free shipping" |
| $150+ | 100% | "You qualify for free shipping!" |

Threshold: `FREE_SHIPPING_THRESHOLD = 15000` (cents, hardcoded in `cart.js` line 10).

```
pct = Math.min((totalCents / 15000) * 100, 100)
#shipping-fill.style.width = pct + '%'
```

The progress bar (`#shipping-fill`) animates via `transition: width var(--transition-base)`.

---

## Drawer Open / Close

### `openDrawer()`

1. Stores `document.activeElement` as `triggerEl` (for focus restoration)
2. `#cart-drawer.classList.add('is-open')`
3. `aria-hidden="false"`
4. `document.body.style.overflow = 'hidden'` (scroll lock)
5. Focuses first focusable element in `.cart-drawer__panel` (`button, [href], input`)

### `closeDrawer()`

1. `#cart-drawer.classList.remove('is-open')`
2. `aria-hidden="true"`
3. `document.body.style.overflow = ''` (scroll unlock)
4. Returns focus to `triggerEl` (the element that opened the drawer)

### External trigger

`cart-drawer.liquid` binds click on `[data-cart-trigger]` (the header cart icon) → `e.preventDefault()` → `BarreleticsCart.open()`.

---

## Focus Trap

Keyboard handler bound on `document` `keydown`. Only active when `#cart-drawer.classList.contains('is-open')`.

| Key | Behavior |
|-----|----------|
| `Escape` | `closeDrawer()` |
| `Tab` on last focusable | `e.preventDefault()` → focus first focusable |
| `Shift+Tab` on first focusable | `e.preventDefault()` → focus last focusable |

Focusable elements query:
```
button:not([disabled]), [href], input:not([disabled]),
select:not([disabled]), textarea:not([disabled]),
[tabindex]:not([tabindex="-1"])
```

Scoped to `.cart-drawer__panel` only (not the overlay).

---

## Error Handling

### `showError(form, message)`

1. Removes any existing `.pdp-buy__error` from the form
2. Creates `<p class="pdp-buy__error" role="alert">{message}</p>`
3. Appends to the form element
4. Auto-removes after 5000ms via `setTimeout`

Triggered by `.catch()` in the ATC flow when `/cart/add.js` returns `!res.ok`.

### Styling

```css
.pdp-buy__error {
  color: #c45c3f;
  font-size: var(--text-sm);
  margin: var(--space-2) 0 0;
}
```

---

## Screen Reader Announcements

`cart.js` creates a live region on init:

```html
<div aria-live="polite" aria-atomic="true" class="visually-hidden" id="cart-live-region"></div>
```

`announce(message)` sets `liveRegion.textContent = message`. Messages:

| Action | Announcement |
|--------|-------------|
| Item added | "Item added to cart" |
| Quantity changed | "Cart updated" |
| Item removed | "Item removed from cart" |

---

## Checkout Handoff

The checkout button in `.cart-drawer__footer` is a plain link: `<a href="/checkout" class="cart-drawer__checkout btn btn--primary">Checkout</a>`. Standard Shopify redirect — no JS interception.

"View Full Cart" links to `/cart` for the full cart page (if `cart_type` setting supports it).

---

## Cross-references

- Variant selection before ATC → [13-variant-selection-flow.md](./13-variant-selection-flow.md)
- Data flow diagrams → [12-data-flow.md](./12-data-flow.md)
- Analytics events on cart actions → [15-analytics-architecture.md](./15-analytics-architecture.md)
- Cart drawer component spec → [04-COMPONENT-LIBRARY.md](./04-COMPONENT-LIBRARY.md)
