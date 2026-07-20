# 15 — Analytics Architecture

> Tracking integrations, event inventory, duplicate prevention strategy, and how to add new integrations.
> Source files: `snippets/analytics-head.liquid`, `snippets/analytics-events.liquid`, `snippets/meta-pixel.liquid`, `snippets/pinterest-tag.liquid`, `snippets/clarity.liquid`, `config/settings_schema.json`

---

## D-045: Production Tracking Strategy

**Decision (2026-07-19, Severity: Critical):**

Shopify native channel integrations are the **preferred** production implementation for GA4 and Meta. Theme-level snippets exist as **fallback only**. Never enable both simultaneously — causes duplicate tracking and corrupts analytics data.

| Integration | Preferred Source | Theme Snippet (Fallback) | Settings Key |
|------------|-----------------|------------------------|-------------|
| GA4 | Shopify Google & YouTube channel | `analytics-head.liquid` + `analytics-events.liquid` | `ga4_measurement_id` |
| Meta Pixel + CAPI | Shopify Meta & Instagram channel | `meta-pixel.liquid` | `meta_pixel_id` |
| Pinterest Tag | Theme-managed (no native channel) | `pinterest-tag.liquid` | `pinterest_tag_id` |
| Microsoft Clarity | Theme-managed | `clarity.liquid` | `clarity_project_id` |
| Help Scout | Theme-managed | `helpscout-beacon.liquid` | `helpscout_beacon_id` |
| Tidio | Theme-managed | `tidio-widget.liquid` | `tidio_widget_key` |
| Search Console | Theme-managed | `<meta>` tag in `theme.liquid` | `search_console_verification` |

**Rule:** Theme settings for GA4 and Meta Pixel must remain **blank** when Shopify native integrations are active.

---

## Snippet Placement in `layout/theme.liquid`

```
<head>
  ...
  {% render 'analytics-head' %}      ← GA4 gtag.js config
  {% render 'meta-pixel' %}          ← Meta Pixel base + PageView + ViewContent
  {% render 'pinterest-tag' %}       ← Pinterest base + page/viewcategory/pagevisit
  {% render 'clarity' %}             ← Clarity session recording
  ...
</head>
<body>
  ...
  {% render 'analytics-events' %}    ← GA4 ecommerce events (before </body>)
  {% render 'helpscout-beacon' %}
  {% render 'tidio-widget' %}
</body>
```

---

## GA4 Implementation

### Head snippet (`snippets/analytics-head.liquid`)

Loads `gtag.js` async from `googletagmanager.com`, configures with the measurement ID:

```js
gtag('config', settings.ga4_measurement_id, { 'send_page_view': true });
```

### Event snippet (`snippets/analytics-events.liquid`)

Placed before `</body>`. Guard: `if (typeof gtag === 'undefined') return;`.

#### Event inventory

| Event | Trigger | Page Type | Key Parameters |
|-------|---------|-----------|---------------|
| `view_item` | Page load | PDP (`request.page_type == 'product'`) | currency, value, items[{item_id, item_name, item_brand, item_category, item_variant, price, quantity}] |
| `view_item_list` | Page load | Collection (`request.page_type == 'collection'`) | item_list_id (handle), item_list_name (title), items[] (limit: 12) |
| `add_to_cart` | `cart:item-added` CustomEvent | Any (listener) | currency, value (price/100), items[{item_id, item_name, item_brand, item_variant, price, quantity}] |
| `begin_checkout` | Click `[data-checkout-button]` or `[name="checkout"]` | Any (listener) | currency, value, items[] (from Liquid cart.items) |
| `size_selector_click` | Click `[data-size-option]` | PDP | size_value |
| `sticky_atc_click` | Click `[data-sticky-atc]` | PDP | (none) |
| `cart_drawer_open` | Click `[data-cart-trigger]` | Any | (none) |

**Purchase event:** NOT in theme code. Shopify checkout is a separate domain — use Shopify's built-in GA4 integration or a Custom Pixel.

### `item_brand` value

Hardcoded as `'Barreletics'` in all event payloads.

### `item_id` resolution

Uses `product.selected_or_first_available_variant.sku` with fallback to `product.id`. In JS listeners, uses `item.sku || item.id`.

---

## Meta Pixel Implementation (`snippets/meta-pixel.liquid`)

### Base code

Standard `fbevents.js` loader. Initializes with `settings.meta_pixel_id`, fires `PageView`. Includes `<noscript>` pixel fallback.

### Event inventory

| Event | Trigger | Dedup event_id | Key Parameters |
|-------|---------|---------------|---------------|
| `PageView` | Page load (base code) | — | (none) |
| `ViewContent` | Page load on PDP | `'vc_' + product.id + '_' + Date.now()` | content_name, content_ids[], content_type, value, currency |
| `AddToCart` | `cart:item-added` CustomEvent | `'atc_' + item.id + '_' + Date.now()` | content_name, content_ids[], content_type, value, currency, num_items |
| `InitiateCheckout` | Click `[data-checkout-button]` or `[name="checkout"]` | `'ic_' + Date.now()` | value, currency, num_items, content_ids[], content_type |

**Purchase:** Handled by Shopify checkout via Meta & Instagram channel CAPI. Not in theme.

### Deduplication

Every event passes an `eventID` in the options object (second arg to `fbq`). Format: `prefix_id_timestamp`. This allows Shopify CAPI server-side events to deduplicate against browser-side events when both are active during testing.

---

## Pinterest Tag Implementation (`snippets/pinterest-tag.liquid`)

### Base code

Loads `core.js` from `s.pinimg.com`. Init includes enhanced match with customer email if logged in:

```js
pintrk('load', settings.pinterest_tag_id, { em: customer.email });
pintrk('page');
```

### Event inventory

| Event | Trigger | Page Type | Key Parameters |
|-------|---------|-----------|---------------|
| `page` | Page load (base code) | All | — |
| `viewcategory` | Page load | Collection | category (collection.title) |
| `pagevisit` | Page load | PDP | line_items[{product_name, product_id, product_category, product_price}] |
| `addtocart` | `cart:item-added` CustomEvent | Any | value, currency, line_items[] |
| `checkout` | Click `[data-checkout-button]` or `[name="checkout"]` | Any | value, currency, line_items[] (from Liquid cart.items) |

---

## Microsoft Clarity (`snippets/clarity.liquid`)

Single `<script>` in `<head>`. Loads Clarity tag with `settings.clarity_project_id`. No page-specific events — Clarity records all sessions automatically.

```js
(function(c,l,a,r,i,t,y){
  c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
  t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
  y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", settings.clarity_project_id);
```

---

## Graceful Degradation Pattern

Every tracking snippet wraps its entire output in a Liquid conditional:

```liquid
{% if settings.xxx_id != blank %}
  <!-- all script tags here -->
{% endif %}
```

If the setting is empty (blank string in Theme Settings), the snippet produces **zero output** — no script tags, no network requests, no console errors.

Settings schema (`config/settings_schema.json`, "Tracking & Integrations" group) includes an explicit warning paragraph:

> "Only use these fields if NOT using Shopify's native Google/Meta channel integrations. Using both will cause duplicate tracking events."

---

## How to Add a New Tracking Integration

1. **Add setting to `settings_schema.json`** — in the "Tracking & Integrations" group, add a `text` type setting with descriptive `id`, `label`, and `info` (include where to find the ID in the platform).

2. **Create snippet** — `snippets/{platform-name}.liquid`. Wrap in `{% if settings.new_setting_id != blank %}`. Load the platform's script, initialize with the setting value.

3. **Add render call to `theme.liquid`** — in `<head>` for tracking pixels, before `</body>` for widgets/beacons. Add a Liquid comment explaining the integration.

4. **Document in D-045** — update `planning/10-decision-log.md` with the new integration's preferred source (native channel vs theme-managed) and any duplicate prevention rules.

---

## Duplicate Prevention Strategy

```
Shopify Native Channels                    Theme Snippets
(GA4, Meta)                                (analytics-head, meta-pixel, etc.)
  │                                           │
  ├── Server-side events (CAPI)               ├── Browser-side events (gtag, fbq)
  ├── Fires: page_view, view_item,            ├── Fires: same events
  │   add_to_cart, begin_checkout,            │
  │   purchase                                │   purchase NOT fired (can't reach checkout)
  │                                           │
  └── BOTH ENABLED = DOUBLE COUNTING          └── Theme settings left BLANK when
      (except purchase, which only                 native channels are active
       native channels fire)
```

**Enforcement mechanism:** Theme settings default to blank strings. The `settings_schema.json` info text warns against enabling both. There is no runtime check — discipline is enforced by documentation and the D-045 decision.

**Safe to have both active temporarily:** Only during initial setup/testing. The `eventID` parameters on Meta events allow CAPI deduplication, but GA4 has no equivalent — GA4 duplicates cannot be deduped after the fact.

---

## Event Listener Pattern

All event snippets use a shared pattern for listening to cart and checkout actions:

```js
// Cart add — dispatched by cart.js (not yet implemented in cart.js as CustomEvent,
// but the listener is ready for it)
document.addEventListener('cart:item-added', function(e) {
  var item = e.detail;
  // fire platform-specific event
});

// Checkout click — delegated click handler
document.addEventListener('click', function(e) {
  var checkoutBtn = e.target.closest('[data-checkout-button], [name="checkout"]');
  if (checkoutBtn) {
    // fire platform-specific checkout event
  }
});
```

The checkout click selector matches both `[data-checkout-button]` (cart drawer) and `[name="checkout"]` (cart page form submit).

---

## Cross-references

- Data flow overview → [12-data-flow.md](./12-data-flow.md)
- Cart events that trigger tracking → [14-cart-flow.md](./14-cart-flow.md)
- Settings schema structure → [03-DESIGN-SYSTEM.md](./03-DESIGN-SYSTEM.md)
- D-045 full decision text → `planning/10-decision-log.md`
