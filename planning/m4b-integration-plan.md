# M4B Integration Plan

---
document: M4B Integration Plan
status: 🟡 In Progress
created: 2026-07-18
depends_on: [M4A locked, MILESTONES-4-5-6-ROADMAP §M4B]
---

## Purpose

Complete execution plan for M4B Integrations gate. Defines every integration required for launch, what Builder can do independently, what requires Owner account access, and verification tests for each.

---

## Tier 1: Required Launch Integrations (Must Have Before Go-Live)

### 1.1 Judge.me

**Purpose:** Review data source for PDP, collection cards, social proof section.

| Item | Detail |
|------|--------|
| Current state | App likely installed on live store; renders with default widget |
| New theme approach | D-025: Headless rendering via metafields. Judge.me is data source only — Barreletics templates render reviews. |

**Builder can do without credentials:**
- Verify `sections/pdp-reviews.liquid` reads `judgeme.average_rating` and `judgeme.review_count` metafields
- Verify `snippets/review-card.liquid` uses correct metafield references
- Verify `snippets/product-card.liquid` star display reads Judge.me metafields
- Add Judge.me widget JavaScript hooks (`jdgm-widget`, `jdgm-rev-widg`, `data-jdgm-product-id`) as placeholders
- Verify structured data (`AggregateRating`) pulls from Judge.me metafield values
- Document metafield sync verification steps

**Requires Owner account access:**
- Judge.me app admin → confirm metafield sync is active
- Judge.me app admin → disable default widget rendering (theme handles display)
- Judge.me app admin → confirm review import from existing store data
- Verify metafield data populates in Shopify admin (Products → Metafields)

**Configuration checklist:**
- [ ] Judge.me app installed and active
- [ ] Metafield sync enabled (judgeme.average_rating, judgeme.review_count)
- [ ] Default widget disabled (custom rendering per D-025)
- [ ] Review display verified on PDP
- [ ] Star ratings verified on collection product cards
- [ ] Social proof section pulling real reviews
- [ ] Structured data `AggregateRating` validated via Rich Results Test

**Verification test:** Load any PDP → confirm star rating displays, review count shows, individual reviews render with correct typography/spacing. Validate JSON-LD contains `AggregateRating` with correct values.

**Rollback:** Re-enable Judge.me default widget rendering if custom display fails.

---

### 1.2 GA4 (Google Analytics 4)

**Purpose:** Session tracking, enhanced ecommerce, conversion measurement.

| Item | Detail |
|------|--------|
| Property ID | 300437005 |
| Current state | Likely configured on live theme via Shopify's built-in GA4 integration or custom snippet |
| New theme approach | gtag.js implementation with enhanced ecommerce data layer |

**Builder can do without credentials:**
- Create `snippets/analytics-head.liquid` — Google tag container with Property ID 300437005
- Create `snippets/analytics-events.liquid` — Enhanced ecommerce event tracking
- Implement standard events: `page_view`, `view_item`, `view_item_list`, `add_to_cart`, `begin_checkout`, `purchase`
- Implement custom events: `size_selector_click`, `sticky_atc_click`, `cart_drawer_open`
- Include snippets in `layout/theme.liquid`
- Configure data layer with product/collection context

**Requires Owner account access:**
- GA4 admin → verify data stream configuration
- GA4 admin → confirm enhanced ecommerce is enabled
- GA4 admin → verify conversion events are marked
- GA4 admin → confirm cross-domain tracking settings (if needed)
- GA4 Realtime → verify events firing post-deploy

**Configuration checklist:**
- [ ] gtag.js snippet installed in theme head
- [ ] Data stream ID confirmed (from GA4 admin)
- [ ] `page_view` fires on all pages
- [ ] `view_item` fires on PDP with correct product data
- [ ] `view_item_list` fires on collection pages
- [ ] `add_to_cart` fires with product/variant/price data
- [ ] `begin_checkout` fires on checkout initiation
- [ ] `purchase` fires (via Shopify checkout — documented, not custom-built)
- [ ] Custom events configured and firing
- [ ] GA4 Realtime shows incoming data

**Verification test:** Browse site → add to cart → initiate checkout. Confirm all events appear in GA4 Realtime with correct parameters.

**Rollback:** Remove analytics snippets from theme.liquid include. No data loss — just stops new event collection.

---

### 1.3 Meta Pixel + CAPI

**Purpose:** Conversion tracking for Meta (Facebook/Instagram) advertising, audience building, ROAS measurement.

| Item | Detail |
|------|--------|
| Pixel ID | Owner provides (from Meta Business Manager) |
| Current state | Likely installed via Shopify's native Meta integration or custom pixel |
| New theme approach | Custom pixel code with standard events + CAPI via Shopify's server-side integration |

**Builder can do without credentials:**
- Create `snippets/meta-pixel.liquid` — Pixel base code with placeholder ID
- Implement browser-side events: `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`
- Implement event deduplication via `event_id` parameter
- Document CAPI setup steps (Shopify admin → Settings → Customer events)
- Configure content_type, content_ids, value, currency parameters

**Requires Owner account access:**
- Meta Business Manager → Pixel ID
- Meta Business Manager → CAPI access token generation
- Shopify admin → Meta & Instagram sales channel → CAPI configuration
- Meta Events Manager → verify event matching and deduplication
- Meta Events Manager → confirm Event Match Quality score

**Configuration checklist:**
- [ ] Pixel base code installed with correct Pixel ID
- [ ] `PageView` fires on all pages
- [ ] `ViewContent` fires on PDP with content_ids, content_type, value, currency
- [ ] `AddToCart` fires with content_ids, content_type, value, currency, content_name
- [ ] `InitiateCheckout` fires with content_ids, value, currency, num_items
- [ ] `Purchase` fires (via Shopify checkout integration)
- [ ] Event deduplication configured (event_id matches between browser and CAPI)
- [ ] CAPI connected and server events flowing
- [ ] Event Match Quality ≥ 6.0 in Events Manager

**Verification test:** Complete a test purchase flow. Verify in Meta Events Manager: all events received, browser + server events deduplicated (not double-counted), Event Match Quality good.

**Rollback:** Remove pixel snippet. CAPI can be disabled in Shopify admin Meta channel settings.

---

### 1.4 Google Search Console

**Purpose:** Index monitoring, crawl error detection, search performance tracking post-launch.

| Item | Detail |
|------|--------|
| Current state | Likely verified for barreletics.com domain |
| New theme approach | No theme code changes needed — verification is domain-level |

**Builder can do without credentials:**
- Verify sitemap generation (Shopify auto-generates at `/sitemap.xml`)
- Document verification steps
- Prepare redirect verification plan (monitor post-launch)
- Verify `robots.txt` is standard Shopify format (auto-generated)
- Ensure all pages have canonical tags (already in `theme.liquid`)

**Requires Owner account access:**
- GSC → confirm site is verified
- GSC → submit sitemap (`/sitemap.xml`)
- GSC → check current index coverage (baseline)
- GSC → monitor 404 errors post-launch
- GSC → request indexing for new key pages if needed

**Configuration checklist:**
- [ ] Domain verified in GSC
- [ ] Sitemap submitted (`/sitemap.xml`)
- [ ] Current index baseline recorded
- [ ] No crawl errors on new pages
- [ ] Redirects not generating soft 404s
- [ ] Canonical tags present and correct on all pages

**Verification test:** After launch, check GSC Coverage report daily for 7 days. Confirm no increase in 404s, no excluded pages that should be indexed.

**Rollback:** N/A — GSC is monitoring only, no rollback needed.

---

### 1.5 Google Merchant Center

**Purpose:** Free product listings in Google Shopping, product feed for potential paid Shopping campaigns.

| Item | Detail |
|------|--------|
| Current state | May already have product feed configured via Shopify's Google & YouTube channel |
| New theme approach | Shopify handles product feed automatically via Google & YouTube sales channel |

**Builder can do without credentials:**
- Verify Product structured data (JSON-LD) on all PDPs includes required GMC fields
- Ensure `offers`, `availability`, `price`, `priceCurrency`, `image`, `name`, `description` in schema
- Verify `gtin` / `mpn` / `brand` fields in product schema (if available in Shopify product data)
- Document GMC setup/verification steps

**Requires Owner account access:**
- Google Merchant Center → confirm account exists and is verified
- Shopify admin → Google & YouTube channel → confirm product sync
- GMC → verify no disapproved products
- GMC → confirm shipping settings match Shopify shipping rates
- GMC → check free listings eligibility

**Configuration checklist:**
- [ ] Google & YouTube sales channel installed
- [ ] Product feed syncing (all active products)
- [ ] No product disapprovals in GMC
- [ ] Shipping settings configured in GMC
- [ ] Free listings enabled (if eligible)
- [ ] Product structured data validated on PDPs

**Verification test:** After product sync, check GMC Diagnostics for errors. Verify all 5 products appear as approved.

**Rollback:** Pause product feed in Shopify Google & YouTube channel settings.

---

## Tier 2: Important But Not Blocking Launch

### 2.1 Help Scout

**Purpose:** Customer support inbox, saved replies aligned with Doc 07, optional Beacon widget.

| Item | Detail |
|------|--------|
| Current state | Unknown — may already be active for email support |
| Approach | Saved replies from Knowledge Base, contact form routing, optional Beacon |

**Builder can do without credentials:**
- Create `planning/m4b-helpscout-alignment.md` — Map Doc 07 topics to saved replies
- Document exact approved copy for each saved reply
- Document Beacon widget configuration (placement, styling, triggers)
- Verify contact form (`page-contact.liquid`) submission routing
- Verify partner inquiry form routing

**Requires Owner account access:**
- Help Scout admin → create/update saved replies
- Help Scout admin → configure email forwarding (Shopify notifications → Help Scout)
- Help Scout admin → Beacon widget installation (if used)
- Help Scout admin → team assignment rules
- Help Scout admin → auto-replies and workflows

**Configuration checklist:**
- [ ] Help Scout account active
- [ ] Email forwarding configured (Shopify → Help Scout)
- [ ] Saved replies created (all Doc 07 topics)
- [ ] Contact form submissions arriving in Help Scout
- [ ] Partner inquiry form submissions arriving in Help Scout
- [ ] Beacon widget installed (if applicable)
- [ ] Auto-reply configured for new inquiries

**Verification test:** Submit contact form and partner inquiry form → verify both arrive in Help Scout with correct metadata.

**Rollback:** Forms still submit to Shopify default endpoint if Help Scout forwarding disabled.

---

### 2.2 Tidio AI

**Purpose:** AI-powered chat support trained on Doc 07 Knowledge Base.

| Item | Detail |
|------|--------|
| Current state | Unknown — may already be active on live site |
| Approach | Train on Doc 07, conversation flows, handoff to Help Scout |

**Builder can do without credentials:**
- Create `planning/m4b-tidio-knowledge-base.md` — Q&A pairs from Doc 07 formatted for Tidio training
- Document conversation flow recommendations
- Document human handoff rules (when to escalate)
- Prepare widget styling spec (matching brand tokens)

**Requires Owner account access:**
- Tidio admin → create/import knowledge base
- Tidio admin → configure conversation flows
- Tidio admin → set handoff rules (Tidio → Help Scout)
- Tidio admin → widget styling and placement
- Tidio admin → enable/disable on specific pages

**Configuration checklist:**
- [ ] Tidio account active
- [ ] Knowledge base populated with Doc 07 content
- [ ] Conversation flows configured (sizing, shipping, returns)
- [ ] Handoff rules set (complex questions → Help Scout)
- [ ] Widget styled to match brand (colors, positioning)
- [ ] Widget appears on correct pages

**Verification test:** Open chat → ask sizing question → confirm AI responds with Doc 07-accurate content. Ask complex question → confirm handoff to human.

**Rollback:** Disable Tidio widget. Customer support reverts to email/form only.

---

### 2.3 Pinterest Tag

**Purpose:** Conversion tracking for Pinterest advertising.

| Item | Detail |
|------|--------|
| Tag ID | Owner provides (from Pinterest Business) |
| Approach | Custom tag code with standard events |

**Builder can do without credentials:**
- Create `snippets/pinterest-tag.liquid` — Base tag with placeholder ID
- Implement events: `pagevisit`, `viewcategory`, `addtocart`, `checkout`
- Include in `theme.liquid`

**Requires Owner account access:**
- Pinterest Business → Tag ID
- Pinterest Business → verify events receiving
- Pinterest Business → product catalog sync (if applicable)

**Configuration checklist:**
- [ ] Pinterest tag base code installed
- [ ] `pagevisit` fires on all pages
- [ ] `viewcategory` fires on collection pages
- [ ] `addtocart` fires on add to cart
- [ ] `checkout` fires on checkout initiation
- [ ] Tag Helper Chrome extension confirms events

**Verification test:** Use Pinterest Tag Helper to verify events fire correctly across page types.

**Rollback:** Remove pinterest-tag snippet include from theme.liquid.

---

### 2.4 Microsoft Clarity

**Purpose:** Session recording, heatmaps, user behavior insights.

| Item | Detail |
|------|--------|
| Project ID | Owner provides (from Clarity dashboard) |
| Approach | Single script snippet in theme head |

**Builder can do without credentials:**
- Create `snippets/clarity.liquid` — Clarity tracking script with placeholder project ID
- Include in `theme.liquid`

**Requires Owner account access:**
- Clarity dashboard → Project ID
- Clarity dashboard → verify recordings appearing
- Clarity dashboard → configure smart events (if desired)

**Configuration checklist:**
- [ ] Clarity script installed
- [ ] Recordings appearing in dashboard
- [ ] Heatmaps generating on key pages (homepage, PDP, collection)
- [ ] No PII exposure (masked by default)

**Verification test:** Visit site → check Clarity dashboard for recording within 5 minutes.

**Rollback:** Remove clarity snippet include from theme.liquid.

---

## Tier 3: Conditional (Owner Confirmation Required)

### 3.1 Klaviyo

**Status:** ⚪ Unconfirmed — do not build until Owner confirms active subscription.

| Item | Detail |
|------|--------|
| What would be needed | API key, list IDs, flow configuration |
| Current newsletter | Uses Shopify native `{% form 'customer' %}` with "newsletter" tag |

**If confirmed, Builder would need to:**
- Replace Shopify native newsletter form with Klaviyo embedded form
- Configure welcome email flow
- Configure abandoned cart flow
- Configure post-purchase flow
- Set up customer segments (by product type, discipline, purchase history)

**Builder can prepare now:**
- Newsletter form markup is already built (works with Shopify native or Klaviyo)
- Document Klaviyo integration steps
- Note: Current newsletter form can work without Klaviyo — tags contacts in Shopify for segmentation

---

### 3.2 Shopify Markets (International)

**Status:** ⚪ Unconfirmed — depends on international selling plans.

| Item | Detail |
|------|--------|
| What would be needed | Market definitions, currency settings, shipping zones |

**If confirmed:**
- Multi-currency display on product cards/PDP
- Geo-detection or market selector
- International shipping rate configuration
- Duties/taxes configuration
- Translated content (if multi-language)

**Builder can prepare now:**
- Theme already uses `{{ product.price | money }}` which respects Markets
- No hardcoded currency symbols in templates
- Document Markets setup steps

---

### 3.3 Other Live Store Apps (Audit Required)

**Status:** Requires Owner to provide list of currently installed apps.

Known from theme analysis:
- **Judge.me** — Covered in Tier 1
- **Juicer** (social feed widget) — Flagged in asset inventory. Evaluate if needed for new theme.
- **Any SMS/loyalty apps** — Unknown. Document if discovered.

**Owner action:** Provide full app list from Shopify admin > Apps.

---

## Integration Verification Matrix

| Integration | Tier | Status | Builder Work | Owner Work | Verification Test | Pass/Fail |
|-------------|------|--------|-------------|-----------|-------------------|-----------|
| Judge.me | 1 | 🟡 In Progress | Theme hooks, metafield references, structured data | App config, widget disable, metafield sync confirm | PDP review display + JSON-LD validation | ☐ |
| GA4 | 1 | 🟡 In Progress | gtag.js snippet, enhanced ecommerce events, data layer | Data stream confirm, conversion marking, Realtime verify | All events in GA4 Realtime during test flow | ☐ |
| Meta Pixel + CAPI | 1 | 🟡 In Progress | Pixel code, browser events, event_id dedup | Pixel ID, CAPI token, Events Manager verify | Test purchase + Events Manager dedup check | ☐ |
| Google Search Console | 1 | ⚪ Owner | Sitemap verification, canonical tags (done) | Site verify, sitemap submit, baseline record | GSC Coverage clean post-launch | ☐ |
| Google Merchant Center | 1 | ⚪ Owner | Product schema on PDPs (done) | GMC account, product feed sync, approvals | All products approved in GMC Diagnostics | ☐ |
| Help Scout | 2 | 🟡 In Progress | Saved reply content, form routing docs | Account config, forwarding, Beacon install | Form submission → Help Scout arrival | ☐ |
| Tidio AI | 2 | 🟡 In Progress | Knowledge base content, flow docs | Account config, KB import, widget install | Chat Q&A accuracy + handoff test | ☐ |
| Pinterest Tag | 2 | 🟡 In Progress | Tag snippet, standard events | Tag ID, event verification | Tag Helper confirms all events | ☐ |
| Microsoft Clarity | 2 | 🟡 In Progress | Clarity snippet | Project ID, dashboard verify | Recording appears within 5 min | ☐ |
| Klaviyo | 3 | ⚪ Unconfirmed | Newsletter form already compatible | Confirm subscription, API key, flow setup | Email flow triggers correctly | ☐ |
| Shopify Markets | 3 | ⚪ Unconfirmed | Theme already Markets-compatible | Market definitions, currencies, shipping | Multi-currency displays correctly | ☐ |

---

## Integration Dependency Order

```
1. Judge.me (metafield sync → enables review display)
2. GA4 (analytics baseline → enables all measurement)
3. Meta Pixel + CAPI (advertising measurement → enables ROAS tracking)
4. Google Search Console (monitoring → enables SEO tracking)
5. Google Merchant Center (product feed → enables free listings)
---
6. Pinterest Tag (advertising measurement)
7. Microsoft Clarity (behavioral insights)
8. Help Scout (customer support quality)
9. Tidio AI (automated support)
```

---

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Judge.me metafield sync not working | Fall back to Judge.me API call in Liquid; document manual metafield entry |
| GA4 events not firing | Test in preview first; use GA4 DebugView; fall back to Shopify native analytics |
| Meta Pixel double-firing (no dedup) | Implement event_id on every event; verify in Events Manager test events |
| CAPI configuration complexity | Rely on Shopify's native Meta channel for CAPI; avoid custom server-side |
| Tidio conflicts with brand voice | All responses trained from Doc 07 only; human handoff for edge cases |
| Too many scripts hurting performance | Audit script load impact; defer non-critical (Clarity, Pinterest) post-LCP |

---

## Summary

- **Tier 1 (launch-blocking):** 5 integrations — Builder can prepare all code; Owner provides credentials and verification
- **Tier 2 (important):** 4 integrations — Builder prepares content and snippets; Owner configures platforms
- **Tier 3 (conditional):** 2-3 integrations — Awaiting Owner confirmation before any work
- **Builder-independent work available:** ~70% of Tier 1 + Tier 2 implementation
- **Estimated Owner sessions needed:** 2-3 (credentials + verification)
