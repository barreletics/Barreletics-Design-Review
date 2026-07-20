# 10 — PDP Architecture Reference

## Template Composition

Defined in `templates/product.json`. Section order:

```
pdp-buy-box          ← Gallery + purchase module + product schema
value-strip          ← Trust/value proposition bar
pdp-features         ← "Built around one obsession: Grip." + discipline icons
fifty-fifty (video)  ← "Yoga Socks Are Useless." + video embed
variant-grid         ← Cross-sell: "Shop all colors & styles." (8 products)
fifty-fifty (lifestyle) ← Customer quote on cream bg, reversed layout
pdp-sock-math        ← Cost comparison: $74 vs $144/yr
pdp-reviews          ← Judge.me reviews (featured + community)
geo-section          ← "Trusted by studios near you" Q&A accordion
newsletter           ← "10% off your first pair." email signup
pdp-sticky-atc       ← Fixed bottom bar (appears when buy box scrolls away)
```

---

## Buy Box Anatomy (`sections/pdp-buy-box.liquid`)

The buy box renders inside a `.pdp-hero` two-column grid (gallery left, purchase module right).

### Gallery

```
.pdp-gallery (sticky, top: var(--space-12))
  ├─ .pdp-gallery__hero
  │     └─ #pdp-main-img (eager, fetchpriority="high", srcset 400/600/800w)
  └─ .pdp-gallery__thumbs (if product.images.size > 1, limit: 5)
        └─ .pdp-gallery__thumb (button, data-thumb-src, first has .is-active)
```

### Purchase Module

```
.pdp-buy
  ├─ .pdp-buy__rating
  │     ├─ .pdp-buy__stars "★★★★★"
  │     ├─ .pdp-buy__rating-text "Trusted by 1,000+ Instructors"
  │     └─ a.pdp-buy__reviews-link href="#reviews" "Reviews →"
  │
  ├─ .pdp-buy__header
  │     ├─ h1.pdp-buy__seo-title (product.title)
  │     └─ span.pdp-buy__badge (variant metafield: custom.sole_type)
  │
  ├─ p.pdp-buy__name (tagline: "Secure in every hold. / No sliding. No resets.")
  ├─ p.pdp-buy__desc (product.description, stripped, truncated 180)
  │
  ├─ .pdp-buy__price-block
  │     ├─ span.pdp-buy__price-now (current_variant.price | money)
  │     └─ span.pdp-buy__price-meta "or 4 payments · free shipping over $150"
  │
  ├─ [for each option in product.options_with_values]
  │     └─ .pdp-buy__option [data-option-position="{{ option.position }}"]
  │           ├─ .pdp-buy__option-header
  │           │     ├─ .pdp-buy__option-label ("Color · <span#selected-color>" or "Size")
  │           │     └─ a.pdp-buy__size-link "Size Chart →" (Size option only)
  │           ├─ [Color] .pdp-buy__swatches
  │           │     └─ button.pdp-buy__swatch [data-color, aria-selected, is-active]
  │           │           └─ inline style: background mapped from handleized color name
  │           └─ [Size] .pdp-buy__sizes (2-col grid)
  │                 └─ button.pdp-buy__size-btn [data-size, is-active]
  │                       └─ span.pdp-buy__size-range (M: "Women 5–7.5 · Men 6–8",
  │                                                    L: "Women 8–10 · Men 8.5–11")
  │
  ├─ form#pdp-form (action="/cart/add" method="post")
  │     ├─ input[type="hidden" name="id" value=current_variant.id]
  │     └─ button.pdp-buy__cta.btn.btn--primary "Add to Cart — $XX"
  │
  ├─ .pdp-buy__trust (5 items)
  │     ├─ "✓ Ships 1–2 days"
  │     ├─ "✓ 30-day returns"
  │     ├─ "✓ 90-day warranty"
  │     ├─ "✓ Latex- & silicone-free"
  │     └─ "✓ Made in USA"
  │
  └─ .pdp-buy__accordions (4 <details> elements, data-pdp-accordion)
        ├─ Description (product.description, full HTML)
        ├─ Care & how to wear
        ├─ Shipping
        └─ 30-day returns + 90-day warranty
```

### Color Swatch Mapping

The `style="background: ..."` on each swatch uses a Liquid replace chain:

| Color Handle | Hex |
|-------------|-----|
| `onyx` | `#050505` |
| `dusty-rose` | `#e9d3cb` |
| `stone` | `#c9c5b8` |
| `sage` | `#7b8c84` |
| `espresso` | `#3d3530` |
| `mist` | `#b8c4c0` |

---

## Product JSON-LD Schema

Embedded as `<script type="application/ld+json">` in `pdp-buy-box.liquid` (lines 149–176):

```json
{
  "@type": "Product",
  "name": "...",
  "description": "...",
  "brand": { "@type": "Brand", "name": "Barreletics" },
  "image": "...",
  "url": "...",
  "sku": "...",
  "offers": {
    "@type": "Offer",
    "price": "...",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "...",
    "reviewCount": "..."
  }
}
```

`aggregateRating` is conditional — only rendered when `product.metafields.judgeme.review_count > 0`. Rating values come from Judge.me metafields: `judgeme.average_rating` and `judgeme.review_count`.

---

## Product Data Flow

```
Shopify Admin (product data)
  │
  ▼
{{ product | json }}   ← Liquid renders full product JSON
  │
  ▼
window.__pdpProduct    ← assigned in inline <script> in pdp-buy-box.liquid
  │
  ▼
variant-selector.js    ← reads window.__pdpProduct on init
  │
  ├─ state.options     ← tracks selected Color/Size positions
  ├─ resolveVariant()  ← matches options combo → variant object
  └─ updateVariant()   ← writes to DOM + dispatches event
       │
       ├─ input[name="id"].value = variant.id
       ├─ .pdp-buy__price-now text
       ├─ .pdp-buy__cta text + disabled state
       ├─ #pdp-main-img src + srcset
       ├─ URL ?variant= param
       └─ dispatches 'variant:changed' CustomEvent
              │
              ├─ sticky-atc.liquid script → updates sticky bar
              └─ analytics-events.liquid  → (informs next ATC event)
```

---

## Variant Selection Flow

1. User clicks a `.pdp-buy__swatch` (`data-color`) or `.pdp-buy__size-btn` (`data-size`)
2. `selectOption(position, value, ...)` in `variant-selector.js`:
   - Toggles `.is-active` on the clicked element, removes from siblings
   - Updates `aria-selected` on swatches
   - Stores value in `state.options[position]`
   - If Color option: updates `#selected-color` text
3. `updateVariant()`:
   - `resolveVariant()` iterates `product.variants`, comparing each variant's `options[]` array against `state.options`
   - On match: updates hidden `input[name="id"]`, price display, CTA button text ("Add to Cart — $XX" or "Sold Out"), main image, URL query param
   - Dispatches `variant:changed` with `{ variant, product }`
4. `updateAvailability()`:
   - For each size button, checks if any variant with the current color + that size has `available: true`
   - Unavailable sizes get `.is-unavailable`, `disabled`, and `aria-disabled="true"`

---

## Sticky ATC Relationship

Implemented across two files:
- `sections/pdp-sticky-atc.liquid` — section wrapper, renders `{% render 'sticky-atc' %}`
- `snippets/sticky-atc.liquid` — the actual bar

### Visibility

Uses `IntersectionObserver` watching `[data-buy-box]` (the `.pdp-hero` section element). When the buy box exits the viewport, `#sticky-atc` gets `.is-visible` (CSS: `transform: translateY(0)`) and `aria-hidden="false"`.

### Content

| Element | Selector | Content |
|---------|----------|---------|
| Thumbnail | `.sticky-atc__thumb` | Product featured image, 40×40 |
| Title | `.sticky-atc__title` | `product.title` |
| Price | `.sticky-atc__price` | Variant price (updated on `variant:changed`) |
| Size label | `#sticky-atc-size` | "Size: {variant.title}" (updated on `variant:changed`) |
| ATC button | `#sticky-atc-btn` | "Add to Cart — $XX" (updated on `variant:changed`) |

### Add to Cart

`#sticky-atc-btn` click → reads `data-variant-id` → `window.BarreleticsCart.add(vid, 1)`. Shows "Adding…" during request. On completion, the button text resets via a one-time `variant:changed` listener.

On mobile (`max-width: 768px`), `.sticky-atc__info` is hidden — only the size label and ATC button remain visible.

---

## PDP Features (`sections/pdp-features.liquid`)

Two-column grid of feature blocks (type `"feature"`, each with `title` and `description` settings). Default preset includes 4 features: "360° Grip", "No Slipping", "Stay in the Flow", "Built to Last".

Optional discipline strip (`show_disciplines: true`): horizontal row of 7 discipline icons — Barre, Pilates, Reformer, Megaformer, Lagree, Yoga, Mat Work. Each rendered as `.pdp-disciplines__item` with a placeholder `.pdp-disciplines__icon` circle and `.pdp-disciplines__name` label.

---

## Sock Math (`sections/pdp-sock-math.liquid`)

Side-by-side cost comparison: grip socks ($112–144/yr recurring) vs Barreletics ($74 once). Two-column `.sock-math__grid`:

- **Left column** (`.sock-math__col--theirs`): "Recurring cost" label, 3 negatives with ✗ marks
- **Right column** (`.sock-math__col--ours`): "One-time" badge in accent color, 3 positives with ✓ marks, coral left border, box shadow

All text content is configurable via section settings: `headline`, `subheadline`, `our_price`, `their_price`, `savings_line`, `cta_text`, `cta_url`.

---

## Reviews (`sections/pdp-reviews.liquid`)

### Data Source

Judge.me (D-025). The theme uses Judge.me as a data source only — all rendering is custom.

### Aggregate Stats

Read from Liquid metafields:
- `product.metafields.judgeme.average_rating` → displayed in header + Product JSON-LD
- `product.metafields.judgeme.review_count` → displayed in header + JSON-LD `reviewCount`

### Featured Reviews

Curated via section blocks (`type: "featured_review"`). Each block has settings: `title`, `body`, `author`, `verified` (checkbox), `bg_gradient`. Rendered as `.pdp-review-featured` cards in an alternating 2-column layout (even children swap media/content order via CSS `order`).

### Community Reviews

Fetched client-side via Judge.me API:

```
GET https://judge.me/api/v1/reviews?shop_domain={shop.permanent_domain}&product_handle={handle}&per_page=6
```

Rendered into `#jm-reviews-container` using an inline `buildReviewCard()` function that produces `.review-card` markup (matching `snippets/review-card.liquid` structure). Shows stars (filled ★ / empty ☆), title, body, optional photo, author name, verified badge, and formatted date.

### `snippets/review-card.liquid`

Server-side Liquid snippet for rendering review data with Schema.org `Review` microdata (`itemscope itemtype="https://schema.org/Review"`). Expected properties: `review.rating`, `review.title`, `review.body`, `review.author`, `review.location`, `review.date`, `review.photo`.

---

## GEO Section

Accordion Q&A section at the bottom of the PDP. Configured in `product.json` with 3 blocks (type `geo_item`):

1. "Trusted by reformer studios in Miami, LA, and NYC"
2. "Worn in barre studios from Dallas to San Francisco"
3. "Chosen by Pilates and Lagree athletes in Chicago, Austin, and beyond"

Each block has `question` (summary text) and `answer` (HTML body) settings.

---

## Script Loading on PDP

At the bottom of `sections/pdp-buy-box.liquid` (lines 523–541):

```liquid
<script>
  (function() {
    // Accordion aria-expanded toggle
  })();
</script>

<script>
  window.__pdpProduct = {{ product | json }};
</script>

{{ 'variant-selector.js' | asset_url | script_tag }}
{{ 'cart.js' | asset_url | script_tag }}
```

Order matters: product JSON must be assigned before `variant-selector.js` reads it. Both scripts use synchronous `<script>` tags.

The sticky ATC script in `snippets/sticky-atc.liquid` executes later in the page (it's the last section in the template order) and depends on both `variant:changed` events from `variant-selector.js` and `window.BarreleticsCart` from `cart.js`.

---

## Cross-References

- Variant selector and cart JS details → [06-javascript-architecture.md](06-javascript-architecture.md)
- Buy box CSS (`.pdp-buy__*`, `.pdp-gallery__*`) → [07-css-architecture.md](07-css-architecture.md)
- Product JSON-LD and Judge.me aggregate rating → schema and D-025
- Collection cross-sell via `variant-grid` on PDP → [09-collection-template-reference.md](09-collection-template-reference.md)
- Theme settings consumed by analytics on PDP → [08-theme-settings-reference.md](08-theme-settings-reference.md)
