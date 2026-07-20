# 12 — Data Flow

> How product, cart, review, tracking, and settings data moves through the theme.
> Source files: `layout/theme.liquid`, `sections/pdp-buy-box.liquid`, `assets/variant-selector.js`, `assets/cart.js`, `snippets/analytics-events.liquid`, `snippets/review-card.liquid`, `config/settings_schema.json`

---

## Product Data Flow

```
Shopify Admin (product)
  │
  ├──▸ Liquid {{ product }} ──▸ HTML (rendered fields)
  │     ├── product.title         → h1.pdp-buy__seo-title
  │     ├── product.description   → p.pdp-buy__desc (strip_html, truncate: 180)
  │     ├── product.featured_image → #pdp-main-img (srcset: 400w, 600w, 800w)
  │     ├── product.options_with_values → .pdp-buy__swatch / .pdp-buy__size-btn
  │     └── selected_or_first_available_variant.price → .pdp-buy__price-now, .pdp-buy__cta text
  │
  └──▸ {{ product | json }} ──▸ <script>window.__pdpProduct = ...;</script>
        │
        └──▸ variant-selector.js reads window.__pdpProduct
              ├── product.options    → state.options keys (1-indexed positions)
              ├── product.variants   → resolveVariant() iterates to find match
              └── variant.featured_image.src → updateVariant() swaps #pdp-main-img
```

**Key detail:** `pdp-buy-box.liquid` renders the product data twice — once as HTML for initial paint (SEO/no-JS fallback), once as JSON for JS variant resolution. The JSON blob is the single source of truth for `variant-selector.js`.

---

## Cart Data Flow

### Add to Cart

```
User clicks .pdp-buy__cta (form#pdp-form submit)
  │
  ▼
bindAddToCartForms() intercepts (e.preventDefault())
  │
  ├── Sets button text "Adding…" + disabled=true
  │
  ▼
addToCart(variantId, 1)
  │
  ├── POST /cart/add.js  { id: variantId, quantity: 1 }
  │     └── if !res.ok → throw Error('add-to-cart-failed')
  │
  ▼
fetchCart()
  │
  ├── GET /cart.js → full cart JSON object
  │
  ▼
renderDrawer(cart) ──▸ updateCartCount(cart.item_count) ──▸ announce('Item added to cart')
  │
  ▼
openDrawer()
  │
  ├── #cart-drawer.classList.add('is-open')
  ├── aria-hidden="false"
  ├── document.body.style.overflow = 'hidden'
  └── focus first focusable element in .cart-drawer__panel
```

### Quantity Change

```
User clicks [data-qty-change] (+/− button)
  │
  ▼
Read current qty from .cart-drawer__item-qty span
  │
  ├── newQty = Math.max(0, currentQty + delta)
  │
  ▼
changeItem(lineKey, newQty)
  │
  ├── POST /cart/change.js  { id: lineKey, quantity: newQty }
  │
  ▼
renderDrawer(cart) ──▸ updateCartCount() ──▸ announce('Cart updated' | 'Item removed')
```

### Item Removal

```
User clicks [data-remove-item]
  │
  ▼
changeItem(lineKey, 0) ──▸ same flow as quantity change
  │
  └── announce('Item removed from cart')
```

### Free Shipping Bar

```
updateShippingBar(totalCents)
  │
  ├── pct = Math.min((totalCents / 15000) * 100, 100)
  ├── #shipping-fill.style.width = pct + '%'
  │
  └── totalCents >= 15000 ? "You qualify for free shipping!"
                           : "$XX away from free shipping"
```

Threshold is hardcoded in `cart.js` as `FREE_SHIPPING_THRESHOLD = 15000` (cents = $150).

---

## Review Data Flow

```
Judge.me (external service, data source only)
  │
  ├──▸ product.metafields.judgeme.average_rating
  ├──▸ product.metafields.judgeme.review_count
  │
  ▼
pdp-buy-box.liquid
  │
  ├── Assigns: jm_rating_schema, jm_count_schema
  ├── Renders JSON-LD aggregateRating (if count > 0):
  │     "@type": "AggregateRating"
  │     ratingValue: {{ jm_rating_schema }}
  │     reviewCount: {{ jm_count_schema }}
  │
  └── Individual reviews ──▸ {% render 'review-card', review: review_object %}
        │
        └── review-card.liquid renders:
              ├── .review-card__stars (filled ★ vs empty ☆, loop 1..5)
              ├── .review-card__title (itemprop="name")
              ├── .review-card__body (itemprop="reviewBody")
              ├── .review-card__photo (optional, image_url: width: 400)
              └── .review-card__footer (author, location, date with itemprop)
```

Review rendering is fully custom — Judge.me is data source only (D-025). Each `review-card` is an `<article>` with `itemscope itemtype="https://schema.org/Review"`.

---

## Tracking Data Flow

```
Page Load (theme.liquid <head>)
  │
  ├──▸ analytics-head.liquid
  │     └── gtag('config', GA4_ID, { send_page_view: true })
  │
  ├──▸ meta-pixel.liquid
  │     ├── fbq('init', PIXEL_ID)
  │     └── fbq('track', 'PageView')
  │
  ├──▸ pinterest-tag.liquid
  │     ├── pintrk('load', TAG_ID, { em: customer.email })
  │     └── pintrk('page')
  │
  └──▸ clarity.liquid
        └── clarity('script', PROJECT_ID)


Page-Specific Events (before </body> via analytics-events.liquid + inline in pixel snippets)
  │
  ├── PDP: gtag view_item / fbq ViewContent / pintrk pagevisit
  ├── Collection: gtag view_item_list / pintrk viewcategory
  │
  ▼
User Action (ATC / checkout click)
  │
  ├── Event: 'cart:item-added' (CustomEvent from cart.js)
  │     ├── gtag('event', 'add_to_cart', ...)
  │     ├── fbq('track', 'AddToCart', ..., { eventID })
  │     └── pintrk('track', 'addtocart', ...)
  │
  ├── Click: [data-checkout-button] or [name="checkout"]
  │     ├── gtag('event', 'begin_checkout', ...)
  │     ├── fbq('track', 'InitiateCheckout', ..., { eventID })
  │     └── pintrk('track', 'checkout', ...)
  │
  └── Custom GA4 events:
        ├── size_selector_click — click [data-size-option]
        ├── sticky_atc_click — click [data-sticky-atc]
        └── cart_drawer_open — click [data-cart-trigger]
```

Purchase events are **not** in theme code — handled by Shopify checkout (separate domain). See [15-analytics-architecture.md](./15-analytics-architecture.md) for full event inventory.

---

## Settings Data Flow

```
Theme Customizer (Shopify Admin)
  │
  ▼
config/settings_data.json (persisted values)
  │
  ▼
Liquid {{ settings.* }}
  │
  ├── Tracking IDs (graceful degradation pattern):
  │     ├── settings.ga4_measurement_id    → analytics-head.liquid
  │     ├── settings.meta_pixel_id         → meta-pixel.liquid
  │     ├── settings.pinterest_tag_id      → pinterest-tag.liquid
  │     ├── settings.clarity_project_id    → clarity.liquid
  │     ├── settings.helpscout_beacon_id   → helpscout-beacon.liquid
  │     └── settings.tidio_widget_key      → tidio-widget.liquid
  │
  ├── UI Configuration:
  │     ├── settings.announcement_enabled  → announcement strip visibility
  │     ├── settings.cart_type             → "drawer" (default) or "page"
  │     ├── settings.free_shipping_threshold → cart drawer shipping bar text
  │     └── settings.search_console_verification → <meta> tag in <head>
  │
  └── Design tokens:
        ├── settings.color_* → CSS custom properties via design-tokens.css
        ├── settings.type_*  → font family, base size, heading scale
        └── settings.max_width, section_padding_x → layout constraints
```

**Graceful degradation:** Every tracking snippet wraps in `{% if settings.xxx_id != blank %}`. If the setting is empty (blank string), zero HTML output — no broken script tags, no console errors.

---

## Cross-references

- Variant selection state machine → [13-variant-selection-flow.md](./13-variant-selection-flow.md)
- Cart drawer rendering details → [14-cart-flow.md](./14-cart-flow.md)
- Full analytics event inventory → [15-analytics-architecture.md](./15-analytics-architecture.md)
- Design tokens and CSS custom properties → [03-DESIGN-SYSTEM.md](./03-DESIGN-SYSTEM.md)
