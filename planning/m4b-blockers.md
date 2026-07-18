# M4B Blockers

---
document: M4B Blockers Log
status: 🟡 Active
created: 2026-07-18
---

## Active Blockers

### B-001: GA4 Measurement ID Unknown
**Severity:** Medium (code uses placeholder)
**What's blocked:** GA4 snippet has `G-XXXXXXXXXX` placeholder — events won't fire until replaced
**Owner action:** Provide Measurement ID from GA4 Admin > Data Streams > Web stream
**Builder prepared:** Full gtag.js + enhanced ecommerce implementation ready

### B-002: Meta Pixel ID Unknown
**Severity:** Medium (code uses placeholder)
**What's blocked:** Pixel snippet has `PIXEL_ID_HERE` placeholder — no Meta tracking until replaced
**Owner action:** Provide Pixel ID from Meta Business Manager > Events Manager
**Builder prepared:** Full pixel code + browser events + deduplication ready

### B-003: Pinterest Tag ID Unknown
**Severity:** Low (not launch-blocking)
**What's blocked:** Pinterest snippet has `PINTEREST_TAG_ID` placeholder
**Owner action:** Provide Tag ID from Pinterest Business > Conversions
**Builder prepared:** Full tag code + standard events ready

### B-004: Microsoft Clarity Project ID Unknown
**Severity:** Low (not launch-blocking)
**What's blocked:** Clarity snippet has `CLARITY_PROJECT_ID` placeholder
**Owner action:** Provide Project ID from clarity.microsoft.com > Settings
**Builder prepared:** Clarity script ready

### B-005: Help Scout Account Access
**Severity:** Medium (not launch-blocking but important for support quality)
**What's blocked:** Saved replies can't be created, email forwarding can't be configured
**Owner action:** Create saved replies from `m4b-helpscout-alignment.md`, configure forwarding
**Builder prepared:** All 10 saved replies written with approved copy

### B-006: Tidio Account Access
**Severity:** Medium (not launch-blocking)
**What's blocked:** Knowledge base can't be imported, flows can't be configured
**Owner action:** Import Q&A pairs from `m4b-tidio-knowledge-base.md`, configure widget
**Builder prepared:** All Q&A pairs formatted, conversation flows documented

### B-007: Judge.me App Configuration
**Severity:** High (affects review display on PDP)
**What's blocked:** Need to confirm metafield sync is active and default widget is disabled
**Owner action:** Verify in Judge.me app admin: metafield sync ON, default widget OFF
**Builder prepared:** Theme reads metafields correctly, custom rendering per D-025 complete

### B-008: Google Search Console Access
**Severity:** Low (monitoring only — not needed for launch code)
**What's blocked:** Can't verify domain, submit sitemap, or record baseline
**Owner action:** Verify domain, submit `/sitemap.xml`, record index coverage
**Builder prepared:** Canonical tags, sitemap (auto), robots.txt (auto) all in place

### B-009: Google Merchant Center Configuration
**Severity:** Low (enhancement, not launch-blocking)
**What's blocked:** Product feed sync can't be verified
**Owner action:** Confirm GMC account, install Google & YouTube channel, verify sync
**Builder prepared:** Product structured data on all PDPs with required fields

---

## Resolved Blockers

(None yet)

---

## Notes

- All Tier 1 integration CODE is complete with placeholders
- Owner needs to provide 4 IDs (GA4, Meta, Pinterest, Clarity) to activate tracking
- Help Scout + Tidio documentation is complete — Owner implements in their admin
- Judge.me requires app-level configuration check only (theme code is ready)
- No blockers prevent code deployment — only live data flow activation is blocked
