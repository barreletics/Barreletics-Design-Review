# 16 — Integration Architecture

---
document: 16 – Integration Architecture
version: 1.0
status: Draft
created: 2026-07-19
depends_on: [12-seo-geo-standards]
---

## Overview

All external integrations are configurable via Theme Settings → Tracking & Integrations in `config/settings_schema.json`. No integrations are hardcoded — every snippet guards output with `{% if settings.xxx != blank %}` and produces zero output when disabled.

## Integration Inventory

| Integration | Snippet(s) | Setting ID | Placement | Tier |
|---|---|---|---|---|
| GA4 | `analytics-head` + `analytics-events` | `ga4_measurement_id` | `<head>` + before `</body>` | Conditional (D-045) |
| Meta Pixel + CAPI | `meta-pixel` | `meta_pixel_id` | `<head>` | Conditional (D-045) |
| Pinterest Tag | `pinterest-tag` | `pinterest_tag_id` | `<head>` | Optional |
| Microsoft Clarity | `clarity` | `clarity_project_id` | `<head>` | Optional |
| Help Scout Beacon | `helpscout-beacon` | `helpscout_beacon_id` | before `</body>` | Optional |
| Tidio Chat | `tidio-widget` | `tidio_widget_key` | before `</body>` | Optional |
| Google Search Console | (inline in `theme.liquid`) | `search_console_verification` | `<head>` meta tag | Optional |

## Integration Tiers

- **Required:** None — all integrations are configurable and optional at the theme level.
- **Conditional (D-045):** GA4 and Meta Pixel. Shopify's native Google and Meta & Instagram sales channels are preferred. Theme snippets exist as fallback when native channels are not connected. Settings include warning paragraphs: "Only use these fields if NOT using Shopify's native Google/Meta channel integrations. Using both will cause duplicate tracking events."
- **Optional:** Pinterest Tag, Microsoft Clarity, Help Scout Beacon, Tidio Chat, Google Search Console verification. Enable by entering credentials in Theme Customizer.

## Credential Management

All credentials live in `config/settings_schema.json` under the `"Tracking & Integrations"` group. Never hardcoded in templates. Each setting has an `info` field explaining where to find the credential in the platform's admin.

Settings are string (`"type": "text"`) fields populated via Theme Customizer. The guard pattern in every snippet:

```liquid
{% if settings.<setting_id> != blank %}
  <!-- integration output -->
{% endif %}
```

---

## GA4 (Google Analytics 4)

**Snippets:** `snippets/analytics-head.liquid`, `snippets/analytics-events.liquid`
**Setting:** `ga4_measurement_id` (format: `G-XXXXXXXXXX`)
**Configuration:** Theme Customizer → Tracking & Integrations → GA4 Measurement ID

### Head snippet (`analytics-head.liquid`)

Loads `gtag.js` async from `googletagmanager.com` and calls `gtag('config', ...)` with `send_page_view: true`. Placed inside `<head>` via `{% render 'analytics-head' %}` in `theme.liquid`.

### Events snippet (`analytics-events.liquid`)

Placed before `</body>`. Fires enhanced ecommerce events based on page context:

| Event | Trigger | Page Type |
|---|---|---|
| `view_item` | Page load | PDP (`request.page_type == 'product'`) |
| `view_item_list` | Page load | Collection (`request.page_type == 'collection'`, first 12 products) |
| `add_to_cart` | `cart:item-added` custom event | Any |
| `begin_checkout` | Click on `[data-checkout-button]` or `[name="checkout"]` | Any |
| `size_selector_click` | Click on `[data-size-option]` | PDP |
| `sticky_atc_click` | Click on `[data-sticky-atc]` | PDP |
| `cart_drawer_open` | Click on `[data-cart-trigger]` | Any |

**Purchase event:** Not handled by theme code. Shopify checkout is a separate domain. Configured via Shopify Admin → Settings → Customer events or the native Google channel.

**Dependencies:** None. Self-contained. Requires only `ga4_measurement_id` to be non-blank.

---

## Meta Pixel

**Snippet:** `snippets/meta-pixel.liquid`
**Setting:** `meta_pixel_id`
**Configuration:** Theme Customizer → Tracking & Integrations → Meta Pixel ID

### Implementation

Loads `fbevents.js` from `connect.facebook.net`. Initializes pixel with `fbq('init', pixelId)` and fires `PageView` on every page load. Includes `<noscript>` fallback image.

### Events

| Event | Trigger | Deduplication |
|---|---|---|
| `PageView` | Every page load | None (base event) |
| `ViewContent` | PDP page load | `eventID: 'vc_{{ product.id }}_' + Date.now()` |
| `AddToCart` | `cart:item-added` custom event | `eventID: 'atc_' + item.id + '_' + Date.now()` |
| `InitiateCheckout` | Click on `[data-checkout-button]` or `[name="checkout"]` | `eventID: 'ic_' + Date.now()` |

**CAPI deduplication:** `eventID` parameters in browser events match server-side CAPI events sent by Shopify's Meta & Instagram channel. This prevents double-counting.

**Purchase event:** Handled by Shopify Admin Custom Pixel or the Meta & Instagram sales channel CAPI integration. Theme cannot fire on thank-you page.

**Dependencies:** None. Self-contained.

---

## Pinterest Tag

**Snippet:** `snippets/pinterest-tag.liquid`
**Setting:** `pinterest_tag_id`
**Configuration:** Theme Customizer → Tracking & Integrations → Pinterest Tag ID

### Implementation

Loads Pinterest `core.js` SDK. Initializes with `pintrk('load', tagId)`. If customer is logged in, passes hashed email via enhanced match: `{ em: customer.email }`.

### Events

| Event | Trigger | Page Type |
|---|---|---|
| `page` | Every page load | All |
| `viewcategory` | Page load | Collection |
| `pagevisit` | Page load | PDP (with `line_items` array) |
| `addtocart` | `cart:item-added` custom event | Any |
| `checkout` | Click on `[data-checkout-button]` or `[name="checkout"]` | Any |

**Dependencies:** None. Self-contained.

---

## Microsoft Clarity

**Snippet:** `snippets/clarity.liquid`
**Setting:** `clarity_project_id`
**Configuration:** Theme Customizer → Tracking & Integrations → Microsoft Clarity Project ID

### Implementation

Single `<script>` block loads Clarity tracking code from `clarity.ms/tag/{projectId}`. No page-specific events — Clarity records all sessions automatically (heatmaps, session replay).

**Dependencies:** None. Self-contained.

---

## Help Scout Beacon

**Snippet:** `snippets/helpscout-beacon.liquid`
**Setting:** `helpscout_beacon_id`
**Configuration:** Theme Customizer → Tracking & Integrations → Help Scout Beacon ID

### Implementation

Loads Help Scout Beacon v2 SDK from `beacon-v2.helpscout.net` async (on window `load` event). Initializes with `Beacon('init', beaconId)`. If `customer` is truthy (logged in), calls `Beacon('identify', { name, email })` to associate conversations with the Shopify customer.

**Placement:** Before `</body>` in `theme.liquid`.
**Styling:** Configured in Help Scout admin, not in theme code.
**Content:** See `planning/m4b-helpscout-alignment.md` for saved reply content.

**Dependencies:** None. Self-contained.

---

## Tidio Chat

**Snippet:** `snippets/tidio-widget.liquid`
**Setting:** `tidio_widget_key`
**Configuration:** Theme Customizer → Tracking & Integrations → Tidio Widget Key

### Implementation

Loads Tidio JS from `//code.tidio.co/{key}.js` async. If customer is logged in, listens for `tidioChat-ready` event, then calls `tidioChatApi.setContactProperties({ distinct_id, email, name })`.

**Placement:** Before `</body>` in `theme.liquid`.
**Knowledge base:** Trained from Doc 07. See `planning/m4b-tidio-knowledge-base.md` for Q&A pairs.

**Dependencies:** None. Self-contained.

---

## Google Search Console Verification

**Location:** Inline in `layout/theme.liquid` (not a separate snippet)
**Setting:** `search_console_verification`
**Configuration:** Theme Customizer → Tracking & Integrations → Google Search Console Verification

### Implementation

```liquid
{% if settings.search_console_verification != blank %}
  <meta name="google-site-verification" content="{{ settings.search_console_verification }}">
{% endif %}
```

Outputs a single `<meta>` tag in `<head>` for domain verification. Value is the content attribute from Search Console → Settings → Ownership verification → HTML tag method.

**Dependencies:** None.

---

## Adding a New Integration

1. **Add setting** to `config/settings_schema.json` in the `"Tracking & Integrations"` group under the appropriate header (Analytics, Customer support, or Search & verification).
2. **Create snippet** at `snippets/<integration-name>.liquid` with the guard pattern:
   ```liquid
   {% if settings.<new_setting_id> != blank %}
     <!-- integration code -->
   {% endif %}
   ```
3. **Add render call** to `layout/theme.liquid`:
   - Tracking/analytics → in `<head>` section (after existing analytics renders)
   - Widgets/chat → before `</body>` (after existing widget renders)
4. **Update decision log** with rationale and tier classification.
5. **Add preconnect** (optional): If the integration loads from an external domain, add `<link rel="preconnect" href="...">` in the preconnects section of `theme.liquid`.

---

## Cross-References

- Doc 18 (Help Scout Architecture) — Beacon config details and saved reply content
- Doc 19 (Tidio Architecture) — Widget config and AI knowledge base
- Doc 20 (SEO Architecture) — Structured data and meta tags (also in `theme.liquid`)
- `planning/m4b-helpscout-alignment.md` — Help Scout saved replies
- `planning/m4b-tidio-knowledge-base.md` — Tidio Q&A training data
