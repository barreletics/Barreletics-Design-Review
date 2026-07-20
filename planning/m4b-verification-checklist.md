# M4B Integration Verification Checklist

---
document: M4B Verification Checklist
status: 🟡 Ready for Verification (post-credentials)
created: 2026-07-19
depends_on: [m4b-environment-config.md, m4b-integration-plan.md]
---

## How to Use

After pasting production IDs into Theme Settings → Tracking & Integrations, verify each integration below. Every integration should pass all checks before launch.

---

## 1. GA4 (Google Analytics 4)

> ⚠️ **Pre-check (D-045):** Before enabling theme-level GA4 tracking, verify Shopify native Google & YouTube channel status. If the native channel is active and firing events, leave GA4 Measurement ID blank. Only ONE source must be active — native OR theme, never both.

| Field | Value |
|-------|-------|
| **Integration** | GA4 Enhanced Ecommerce |
| **Installation** | `snippets/analytics-head.liquid` (gtag.js loader), `snippets/analytics-events.liquid` (event layer) |
| **Configuration** | Theme Settings → Tracking & Integrations → GA4 Measurement ID |
| **Validation Method** | Open browser DevTools → Network tab → filter `collect?v=2` → verify beacon fires on page load. Or: GA4 Admin → Realtime → verify events appear |
| **Expected Behavior** | `page_view` on every page. `view_item` on PDP with product data. `view_item_list` on collection. `add_to_cart` when item added. `begin_checkout` on checkout click. Custom events on size select, sticky ATC, cart drawer open. |
| **Graceful Degradation** | When GA4 Measurement ID is blank: no `<script>` tags output, no gtag.js loaded, no console errors, no network requests |
| **Duplicate Prevention** | If using Shopify's native Google channel, leave Measurement ID blank. Native channel fires the same events server-side. Info text in Theme Settings warns about this. |
| **Rollback Procedure** | Clear the GA4 Measurement ID in Theme Settings → Save. All tracking stops immediately. |
| **Owner Action Required** | 1. Obtain Measurement ID from GA4 Admin → Data Streams. 2. Paste into Theme Settings. 3. Verify in GA4 Realtime. 4. Mark conversion events in GA4. |
| **Builder Action Required** | ✅ Complete — gtag.js, enhanced ecommerce events, graceful degradation, duplicate prevention notes |

### GA4 Event Verification Matrix

| Event | Trigger | Page Type | Parameters | Check |
|-------|---------|-----------|------------|-------|
| `page_view` | Automatic (gtag config) | All | — | ☐ |
| `view_item` | Page load | Product | item_id, item_name, item_brand, item_category, item_variant, price, currency | ☐ |
| `view_item_list` | Page load | Collection | item_list_id, item_list_name, items[] (up to 12) | ☐ |
| `add_to_cart` | `cart:item-added` event | Any (when adding) | item_id, item_name, item_brand, item_variant, price, quantity, currency | ☐ |
| `begin_checkout` | Click `[data-checkout-button]` | Cart drawer/page | items[], value, currency | ☐ |
| `purchase` | Shopify checkout | Thank you page | _(Shopify-managed, not theme code)_ | ☐ |
| `size_selector_click` | Click `[data-size-option]` | PDP | size_value | ☐ |
| `sticky_atc_click` | Click `[data-sticky-atc]` | PDP | — | ☐ |
| `cart_drawer_open` | Click `[data-cart-trigger]` | Any | — | ☐ |

---

## 2. Meta Pixel

> ⚠️ **Pre-check (D-045):** Before enabling theme-level Meta Pixel, verify Shopify native Meta & Instagram channel status. If the native channel is active and firing events, leave Meta Pixel ID blank. Only ONE source must be active — native OR theme, never both.

| Field | Value |
|-------|-------|
| **Integration** | Meta Pixel + CAPI (browser-side events) |
| **Installation** | `snippets/meta-pixel.liquid` (base code + all events) |
| **Configuration** | Theme Settings → Tracking & Integrations → Meta Pixel ID |
| **Validation Method** | Install Meta Pixel Helper Chrome extension → navigate site → verify events fire. Or: Meta Events Manager → Test Events → enter site URL → verify events |
| **Expected Behavior** | `PageView` on every page. `ViewContent` on PDP with content_ids, value. `AddToCart` on item add. `InitiateCheckout` on checkout click. Each event has unique `event_id` for CAPI deduplication. Noscript fallback image present. |
| **Graceful Degradation** | When Meta Pixel ID is blank: no fbevents.js loaded, no `<script>` or `<noscript>` tags output, no console errors |
| **Duplicate Prevention** | If using Shopify's native Meta & Instagram channel, leave Pixel ID blank. Info text warns about this. All events include `eventID` parameter for CAPI dedup. |
| **Rollback Procedure** | Clear the Meta Pixel ID in Theme Settings → Save. All pixel tracking stops immediately. |
| **Owner Action Required** | 1. Get Pixel ID from Events Manager. 2. Paste into Theme Settings. 3. Set up CAPI via Shopify Meta channel (server-side). 4. Verify in Events Manager (event dedup, match quality ≥ 6.0). |
| **Builder Action Required** | ✅ Complete — Pixel base code, standard events, event_id dedup, noscript fallback, CAPI setup documented |

### Meta Pixel Event Verification Matrix

| Event | Trigger | Parameters | Dedup ID Format | Check |
|-------|---------|------------|----------------|-------|
| `PageView` | Automatic (fbq init) | — | — | ☐ |
| `ViewContent` | PDP load | content_name, content_ids, content_type, value, currency | `vc_{product_id}_{timestamp}` | ☐ |
| `AddToCart` | `cart:item-added` | content_name, content_ids, content_type, value, currency, num_items | `atc_{item_id}_{timestamp}` | ☐ |
| `InitiateCheckout` | Checkout button click | value, currency, num_items, content_ids, content_type | `ic_{timestamp}` | ☐ |
| `Purchase` | Shopify checkout | _(Shopify-managed via CAPI)_ | _(auto)_ | ☐ |

---

## 3. Pinterest Tag

| Field | Value |
|-------|-------|
| **Integration** | Pinterest Conversion Tag |
| **Installation** | `snippets/pinterest-tag.liquid` (base code + events) |
| **Configuration** | Theme Settings → Tracking & Integrations → Pinterest Tag ID |
| **Validation Method** | Install Pinterest Tag Helper Chrome extension → navigate site → verify events fire green |
| **Expected Behavior** | `page` on every page. `pagevisit` on PDP with product data. `viewcategory` on collection with category name. `addtocart` on item add. `checkout` on checkout click. Enhanced match passes customer email if logged in. |
| **Graceful Degradation** | When Pinterest Tag ID is blank: no pintrk script loaded, no `<script>` or `<noscript>` tags output, no console errors |
| **Duplicate Prevention** | No Shopify native Pinterest channel exists — no duplication risk. Only one tag instance loads per page. |
| **Rollback Procedure** | Clear the Pinterest Tag ID in Theme Settings → Save. |
| **Owner Action Required** | 1. Get Tag ID from Pinterest Business → Conversions. 2. Paste into Theme Settings. 3. Verify with Tag Helper extension. |
| **Builder Action Required** | ✅ Complete — Tag base code, standard events, enhanced match, noscript fallback |

---

## 4. Microsoft Clarity

| Field | Value |
|-------|-------|
| **Integration** | Microsoft Clarity Session Recording |
| **Installation** | `snippets/clarity.liquid` (single script) |
| **Configuration** | Theme Settings → Tracking & Integrations → Microsoft Clarity Project ID |
| **Validation Method** | Visit site → wait 2-5 minutes → check clarity.microsoft.com dashboard → verify recording appears |
| **Expected Behavior** | Session recordings capture all pages. Heatmaps generate automatically. No PII exposed (Clarity masks by default). |
| **Graceful Degradation** | When Clarity Project ID is blank: no script output, no network requests, no console errors |
| **Duplicate Prevention** | Single script inclusion. No Shopify native equivalent. |
| **Rollback Procedure** | Clear the Clarity Project ID in Theme Settings → Save. |
| **Owner Action Required** | 1. Create project at clarity.microsoft.com. 2. Copy Project ID from Settings → Setup. 3. Paste into Theme Settings. 4. Verify recordings appear. |
| **Builder Action Required** | ✅ Complete — Clarity script with dynamic project ID |

---

## 5. Judge.me Reviews

| Field | Value |
|-------|-------|
| **Integration** | Judge.me (headless — data source only, per D-025) |
| **Installation** | `sections/pdp-reviews.liquid` (review section), `snippets/review-card.liquid` (card component) |
| **Configuration** | Shopify Admin → Apps → Judge.me → Settings |
| **Validation Method** | Load any PDP → verify star rating displays, review count shows, individual reviews render. Validate JSON-LD via Google Rich Results Test → confirm `AggregateRating` present. |
| **Expected Behavior** | PDP shows aggregate star rating + count from `judgeme.average_rating` / `judgeme.review_count` metafields. Community reviews load via Judge.me API. Review cards render with Barreletics design tokens. "Write a Review" button links to Judge.me review form. |
| **Graceful Degradation** | When Judge.me not installed or metafields empty: shows "No reviews yet — be the first!" message. API fetch fails gracefully with "Reviews are temporarily unavailable" fallback. No console errors. |
| **Duplicate Prevention** | Judge.me default widget must be disabled (D-025). Theme renders reviews with custom components — not Judge.me's widget CSS/JS. |
| **Rollback Procedure** | Re-enable Judge.me default widget in Judge.me admin. Theme custom display degrades to empty state. |
| **Owner Action Required** | 1. Confirm Judge.me app installed. 2. Enable metafield sync (judgeme.average_rating, judgeme.review_count). 3. Disable default widget rendering. 4. Verify metafields populate in Shopify Admin → Products. |
| **Builder Action Required** | ✅ Complete — Custom review rendering, metafield reads, API hydration, structured data, graceful empty/error states |

---

## 6. Help Scout Beacon

| Field | Value |
|-------|-------|
| **Integration** | Help Scout Beacon Chat Widget |
| **Installation** | `snippets/helpscout-beacon.liquid`, included in `layout/theme.liquid` before `</body>` |
| **Configuration** | Theme Settings → Tracking & Integrations → Help Scout Beacon ID |
| **Validation Method** | Set Beacon ID → visit site → verify chat widget appears in bottom-right corner. Click widget → verify contact form loads. If logged in as customer → verify name/email pre-filled. |
| **Expected Behavior** | Chat bubble in bottom-right (configurable in Help Scout admin). Logged-in customers auto-identified. Contact form submissions arrive in Help Scout inbox. |
| **Graceful Degradation** | When Help Scout Beacon ID is blank: no Beacon script loaded, no widget appears, no console errors |
| **Duplicate Prevention** | Only one Beacon instance. If also using Tidio, consider disabling one to avoid two chat widgets. |
| **Rollback Procedure** | Clear the Help Scout Beacon ID in Theme Settings → Save. Widget disappears immediately. |
| **Owner Action Required** | 1. Create Beacon in Help Scout admin. 2. Copy Beacon ID from installation code. 3. Paste into Theme Settings. 4. Create saved replies from `m4b-helpscout-alignment.md`. 5. Configure email forwarding. |
| **Builder Action Required** | ✅ Complete — Beacon script, customer identity pass-through, saved reply content documented |

---

## 7. Tidio AI Chat

| Field | Value |
|-------|-------|
| **Integration** | Tidio AI Chat Support |
| **Installation** | `snippets/tidio-widget.liquid`, included in `layout/theme.liquid` before `</body>` |
| **Configuration** | Theme Settings → Tracking & Integrations → Tidio Widget Key |
| **Validation Method** | Set Widget Key → visit site → verify Tidio chat widget appears. Ask sizing question → verify AI responds with Doc 07 content. |
| **Expected Behavior** | Chat widget loads. AI responds using trained knowledge base. Logged-in customers identified by name/email. Complex questions hand off to Help Scout. |
| **Graceful Degradation** | When Tidio Widget Key is blank: no Tidio script loaded, no widget appears, no console errors |
| **Duplicate Prevention** | If also using Help Scout Beacon, consider running only one chat widget at a time. Both can be toggled independently via Theme Settings. |
| **Rollback Procedure** | Clear the Tidio Widget Key in Theme Settings → Save. Widget disappears immediately. |
| **Owner Action Required** | 1. Import knowledge base from `m4b-tidio-knowledge-base.md`. 2. Configure conversation flows. 3. Set handoff rules (Tidio → Help Scout). 4. Style widget (primary: #1c1916, accent: #c45c3f). 5. Copy Widget Key → paste into Theme Settings. |
| **Builder Action Required** | ✅ Complete — Widget script, customer identity pass-through, knowledge base content documented |

---

## 8. Google Search Console

| Field | Value |
|-------|-------|
| **Integration** | Google Search Console Domain Verification |
| **Installation** | `layout/theme.liquid` `<head>` (meta tag, conditional) |
| **Configuration** | Theme Settings → Tracking & Integrations → Google Search Console Verification |
| **Validation Method** | Set verification code → view page source → confirm `<meta name="google-site-verification" content="...">` in head. Then: Search Console → verify ownership. |
| **Expected Behavior** | Meta verification tag renders in `<head>` on all pages. Google Search Console can verify domain ownership. |
| **Graceful Degradation** | When verification code is blank: no meta tag output. No effect on site. |
| **Duplicate Prevention** | N/A — verification tag is idempotent |
| **Rollback Procedure** | Clear the verification code in Theme Settings → Save. Does not affect existing GSC verification (once verified, meta tag can be removed). |
| **Owner Action Required** | 1. Open Google Search Console. 2. Add property for barreletics.com. 3. Choose "HTML tag" verification. 4. Copy the `content` value. 5. Paste into Theme Settings. 6. Click "Verify" in GSC. 7. Submit sitemap (`/sitemap.xml`). |
| **Builder Action Required** | ✅ Complete — Conditional meta tag in theme.liquid head |

---

## 9. Google Merchant Center

| Field | Value |
|-------|-------|
| **Integration** | Google Merchant Center Product Feed |
| **Installation** | No theme code — Shopify handles via Google & YouTube sales channel |
| **Configuration** | Shopify Admin → Sales Channels → Google & YouTube |
| **Validation Method** | GMC → Diagnostics → verify all products approved. Validate product structured data on PDPs via Rich Results Test. |
| **Expected Behavior** | Products sync from Shopify to GMC automatically. Free listings appear in Google Shopping. Product JSON-LD on PDPs includes required fields (name, price, availability, image, brand). |
| **Graceful Degradation** | N/A — no theme code involved. If channel disconnected, products stop syncing but site unaffected. |
| **Duplicate Prevention** | N/A — single feed source |
| **Rollback Procedure** | Pause product sync in Google & YouTube channel settings |
| **Owner Action Required** | 1. Install Google & YouTube channel. 2. Connect Merchant Center account. 3. Verify all products approved. 4. Enable free listings. 5. Confirm shipping settings match. |
| **Builder Action Required** | ✅ Complete — Product structured data on all PDPs (existing from M3) |

---

## Pre-Launch Verification Sequence

Run these checks in order after pasting all IDs:

0. ☐ **D-045 Duplicate Prevention Check:** Confirm only ONE tracking source is active for GA4 (native Google & YouTube channel OR theme-level snippet, never both). Confirm only ONE tracking source is active for Meta (native Meta & Instagram channel OR theme-level snippet, never both).
1. ☐ Open site in Chrome with DevTools Network tab open
2. ☐ Verify gtag.js loads (filter: `googletagmanager`)
3. ☐ Verify fbevents.js loads (filter: `fbevents`)
4. ☐ Verify pintrk loads (filter: `pinimg`)
5. ☐ Verify Clarity loads (filter: `clarity.ms`)
6. ☐ Navigate to collection page → verify `view_item_list` + `viewcategory` events
7. ☐ Navigate to PDP → verify `view_item` + `ViewContent` + `pagevisit` events
8. ☐ Add item to cart → verify `add_to_cart` + `AddToCart` + `addtocart` events
9. ☐ Click checkout → verify `begin_checkout` + `InitiateCheckout` + `checkout` events
10. ☐ Verify no console errors on any page
11. ☐ Verify Help Scout / Tidio widget appears (if configured)
12. ☐ View page source → verify Search Console meta tag present
13. ☐ Run Google Rich Results Test on a PDP → verify Product + AggregateRating schema
14. ☐ Check GA4 Realtime → verify events arriving
15. ☐ Check Meta Events Manager → Test Events → verify events arriving
