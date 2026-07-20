# M4B Blockers

---
document: M4B Blockers Log
status: 🟡 Active — credential-dependent only
created: 2026-07-18
updated: 2026-07-19
---

## Active Blockers

All remaining blockers are **credential-dependent only**. All Builder code work is complete. Each blocker resolves by pasting a single value into Theme Settings → Tracking & Integrations, or configuring an external platform.

### B-001: GA4 Measurement ID
**Severity:** Medium
**What's blocked:** GA4 events won't fire until Measurement ID is set
**Resolution:** Theme Settings → Tracking & Integrations → GA4 Measurement ID
**How to obtain:** GA4 Admin → Data Streams → Web stream → Measurement ID (format: G-XXXXXXXXXX)
**Builder status:** ✅ Complete — gtag.js + enhanced ecommerce + graceful degradation

### B-002: Meta Pixel ID
**Severity:** Medium
**What's blocked:** No Meta conversion tracking until Pixel ID is set
**Resolution:** Theme Settings → Tracking & Integrations → Meta Pixel ID
**How to obtain:** Meta Business Manager → Events Manager → Pixel ID
**Builder status:** ✅ Complete — Pixel code + standard events + event_id dedup + noscript fallback

### B-003: Pinterest Tag ID
**Severity:** Low (not launch-blocking)
**What's blocked:** No Pinterest conversion tracking
**Resolution:** Theme Settings → Tracking & Integrations → Pinterest Tag ID
**How to obtain:** Pinterest Business → Ads → Conversions → Tag Manager
**Builder status:** ✅ Complete — Tag code + events + enhanced match

### B-004: Microsoft Clarity Project ID
**Severity:** Low (not launch-blocking)
**What's blocked:** No session recording or heatmaps
**Resolution:** Theme Settings → Tracking & Integrations → Microsoft Clarity Project ID
**How to obtain:** clarity.microsoft.com → Settings → Setup
**Builder status:** ✅ Complete — Clarity script with dynamic ID

### B-005: Help Scout Account Configuration
**Severity:** Medium (not launch-blocking)
**What's blocked:** Saved replies, email forwarding, Beacon widget
**Resolution:** 1. Create saved replies from `m4b-helpscout-alignment.md`. 2. Configure email forwarding. 3. Copy Beacon ID → Theme Settings.
**Builder status:** ✅ Complete — Beacon snippet, saved reply content documented

### B-006: Tidio Account Configuration
**Severity:** Medium (not launch-blocking)
**What's blocked:** AI knowledge base, conversation flows, widget
**Resolution:** 1. Import Q&A from `m4b-tidio-knowledge-base.md`. 2. Configure flows. 3. Copy Widget Key → Theme Settings.
**Builder status:** ✅ Complete — Widget snippet, knowledge base content documented

### B-007: Judge.me App Configuration
**Severity:** High (affects review display on PDP)
**What's blocked:** Metafield sync must be active, default widget must be disabled
**Resolution:** Judge.me app admin → metafield sync ON, default widget OFF
**Builder status:** ✅ Complete — Custom review rendering, metafield reads, API hydration

### B-008: Google Search Console Verification
**Severity:** Low (monitoring only)
**What's blocked:** Domain verification for SEO monitoring
**Resolution:** 1. Get verification code from GSC. 2. Paste into Theme Settings → Search Console Verification. 3. Verify in GSC. 4. Submit `/sitemap.xml`.
**Builder status:** ✅ Complete — Conditional meta tag in theme.liquid

### B-009: Google Merchant Center Configuration
**Severity:** Low (enhancement)
**What's blocked:** Product feed sync, free Shopping listings
**Resolution:** Install Google & YouTube channel in Shopify Admin → connect GMC account
**Builder status:** ✅ Complete — Product structured data on all PDPs (existing from M3)

### B-010: Meta CAPI Access Token
**Severity:** Medium (needed for server-side dedup)
**What's blocked:** Server-side conversion events (browser events work without this)
**Resolution:** Meta Business Manager → Events Manager → Settings → Generate Access Token → configure via Shopify Meta channel
**Builder status:** ✅ Complete — CAPI setup documented, browser events include event_id for dedup

---

## Resolved Blockers

(None resolved yet — all require Owner credentials)

---

## Summary

| Category | Blockers | Resolution Method |
|----------|---------|------------------|
| **Theme Settings paste** (30 seconds each) | B-001, B-002, B-003, B-004, B-008 | Paste ID into Theme Settings → Save |
| **Theme Settings + platform config** | B-005, B-006 | Paste key + configure platform admin |
| **App admin only** | B-007 | Judge.me admin toggle |
| **Shopify Admin only** | B-009, B-010 | Sales channel / app configuration |

**All Builder code work is complete.** Next step: Owner pastes production IDs and validates.
