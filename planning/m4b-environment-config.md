# Production Configuration — External Identifiers

---
document: M4B Environment Configuration
status: 🟡 Pending Owner Input
created: 2026-07-19
depends_on: [m4b-integration-plan.md]
---

All values below must be provided by the Owner before launch.
Theme implementation references these as **Shopify theme settings** — never hardcoded in theme files.
To configure: **Shopify Admin → Online Store → Themes → Customize → Theme Settings → Tracking & Integrations**.

---

## Analytics & Tracking

| Integration | Config Key | Theme Setting ID | Value | Status |
|-------------|-----------|-----------------|-------|--------|
| GA4 | Measurement ID | `ga4_measurement_id` | _____ | Pending |
| Meta Pixel | Pixel ID | `meta_pixel_id` | _____ | Pending |
| Meta CAPI | Access Token | _(Shopify Admin config)_ | _____ | Pending |
| Pinterest Tag | Tag ID | `pinterest_tag_id` | _____ | Pending |
| Microsoft Clarity | Project ID | `clarity_project_id` | _____ | Pending |

### GA4 Measurement ID
- **Format:** `G-XXXXXXXXXX`
- **Where referenced:** `snippets/analytics-head.liquid` (gtag.js config), `snippets/analytics-events.liquid` (event firing)
- **How to obtain:** GA4 Admin → Data Streams → Web stream → Measurement ID (not the Property ID 300437005)
- **Where to configure:** Theme Settings → Tracking & Integrations → GA4 Measurement ID

### Meta Pixel ID
- **Format:** 15-16 digit number (e.g., `123456789012345`)
- **Where referenced:** `snippets/meta-pixel.liquid` (fbq init, noscript fallback, all standard events)
- **How to obtain:** Meta Business Manager → Events Manager → Data Sources → select Pixel → Pixel ID
- **Where to configure:** Theme Settings → Tracking & Integrations → Meta Pixel ID

### Meta CAPI Access Token
- **Format:** Long alphanumeric token
- **Where referenced:** Not in theme code — configured in Shopify Admin
- **How to obtain:** Meta Business Manager → Events Manager → Settings → Generate Access Token
- **Where to configure:** Shopify Admin → Settings → Customer events → Meta Pixel → CAPI settings
- **Note:** CAPI is server-side. Shopify's Meta & Instagram channel handles this automatically when connected. No theme code needed.

### Pinterest Tag ID
- **Format:** 13-digit number (e.g., `2612345678901`)
- **Where referenced:** `snippets/pinterest-tag.liquid` (pintrk load, noscript fallback, all events)
- **How to obtain:** Pinterest Business → Ads → Conversions → Tag Manager → Tag ID
- **Where to configure:** Theme Settings → Tracking & Integrations → Pinterest Tag ID

### Microsoft Clarity Project ID
- **Format:** 10-character alphanumeric (e.g., `abc1d2efgh`)
- **Where referenced:** `snippets/clarity.liquid` (Clarity script src)
- **How to obtain:** clarity.microsoft.com → Settings → Setup → Get tracking code → Project ID in script
- **Where to configure:** Theme Settings → Tracking & Integrations → Microsoft Clarity Project ID

---

## Reviews

| Integration | Config Key | Value | Status |
|-------------|-----------|-------|--------|
| Judge.me | App Install | _(Shopify Admin)_ | Pending |
| Judge.me | Metafield Sync | _(Judge.me Admin)_ | Pending |

### Judge.me
- **Where referenced:** `sections/pdp-reviews.liquid` (metafield reads: `judgeme.average_rating`, `judgeme.review_count`), `snippets/review-card.liquid` (rendering), `snippets/product-card.liquid` (star display on collection cards)
- **How to obtain:** Install Judge.me app from Shopify App Store (if not already installed)
- **Where to configure:** Shopify Admin → Apps → Judge.me → Settings → enable Metafield Sync, disable default widget rendering
- **Note:** No theme setting needed — Judge.me is an installed app. Theme reads metafields automatically once sync is active.

---

## Customer Support

| Integration | Config Key | Theme Setting ID | Value | Status |
|-------------|-----------|-----------------|-------|--------|
| Help Scout Beacon | Beacon ID | `helpscout_beacon_id` | _____ | Pending |
| Tidio | Widget Key | `tidio_widget_key` | _____ | Pending |

### Help Scout Beacon ID
- **Format:** UUID (e.g., `12345678-abcd-1234-efgh-123456789abc`)
- **Where referenced:** `snippets/helpscout-beacon.liquid` (Beacon init script)
- **How to obtain:** Help Scout → Beacon → Select beacon → Installation → Beacon ID in script
- **Where to configure:** Theme Settings → Tracking & Integrations → Help Scout Beacon ID. Leave blank to disable.

### Tidio Widget Key
- **Format:** Alphanumeric string (e.g., `abc123def456ghi789`)
- **Where referenced:** `snippets/tidio-widget.liquid` (widget script src)
- **How to obtain:** Tidio → Settings → Developer → Widget Key (or from embed script URL)
- **Where to configure:** Theme Settings → Tracking & Integrations → Tidio Widget Key. Leave blank to disable.

---

## Search & Commerce

| Integration | Config Key | Theme Setting ID | Value | Status |
|-------------|-----------|-----------------|-------|--------|
| Google Search Console | Verification Code | `search_console_verification` | _____ | Pending |
| Google Merchant Center | Merchant ID | _(Shopify Admin config)_ | _____ | Pending |

### Google Search Console Verification Code
- **Format:** Alphanumeric string (the `content` value of the meta tag)
- **Where referenced:** `layout/theme.liquid` (meta verification tag in `<head>`)
- **How to obtain:** Google Search Console → Settings → Ownership verification → HTML tag → copy the `content` value only
- **Where to configure:** Theme Settings → Tracking & Integrations → Google Search Console Verification

### Google Merchant Center
- **Where referenced:** No theme code — product feed handled by Shopify's Google & YouTube channel
- **How to obtain:** Create/access account at merchants.google.com
- **Where to configure:** Shopify Admin → Sales Channels → Google & YouTube → connect Merchant Center account, enable product sync
- **Note:** Product structured data (JSON-LD) is already on all PDPs. GMC reads the feed from Shopify, not theme code.

---

## Configuration Summary

| Config Method | Integrations |
|---------------|-------------|
| **Theme Settings** (Customize → Theme Settings → Tracking & Integrations) | GA4, Meta Pixel, Pinterest, Clarity, Help Scout Beacon, Tidio, Search Console |
| **Shopify Admin** (Sales Channels / Apps) | Judge.me, Meta CAPI, Google Merchant Center |
| **External Platform** (Owner logs in) | Help Scout saved replies, Tidio knowledge base |

---

## Activation Checklist

1. Open Shopify Admin → Online Store → Themes → Customize → Theme Settings → Tracking & Integrations
2. Paste each ID into the corresponding field
3. Save the theme
4. Verify each integration fires correctly (see `planning/m4b-verification-checklist.md`)
5. **Important:** If using Shopify's native Google/Meta channel integrations, do NOT also set the theme-level IDs — this prevents duplicate tracking
