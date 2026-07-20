# M4D — Owner Launch Checklist

**Purpose:** Everything the Owner must personally verify, approve, or complete before, during, and after launch. This is the Owner's single reference document.

---

## Before Launch

### Tracking & Integrations (provide to Builder)

- [ ] GA4 Measurement ID provided
- [ ] Meta Pixel ID provided
- [ ] Pinterest Tag ID provided
- [ ] Microsoft Clarity Project ID provided
- [ ] Google Search Console verification code provided
- [ ] Help Scout Beacon ID provided
- [ ] Tidio Public Key provided

### Policy & Content Approvals

- [ ] Policy Freeze Gate completed — all terms signed off:
  - [ ] Shipping terms
  - [ ] Return terms (30-day, new sellable condition)
  - [ ] Warranty language (90-day manufacturing defects)
  - [ ] Pricing (all product prices confirmed)
  - [ ] Discounts / promo codes (which are active?)
  - [ ] Free shipping threshold ($150 confirmed)
  - [ ] Wholesale terms (internal only, not displayed)
  - [ ] Studio Program terms (internal only, not displayed)
  - [ ] Ambassador terms (internal only, not displayed)
- [ ] Hero headline chosen (D-041):
  - Option A: "The Pilates Sock Era Is Over" (current `hero.liquid`)
  - Option B: "Think Outside the Sock." (alt `hero-alt.liquid`)
  - **Chosen:** `________________`
- [ ] Content inventory reviewed — all "Needs Review" items approved
- [ ] Redirect map reviewed and approved
- [ ] Collection structure confirmed (which collections to create)

### Production Assets (deliver to Builder)

- [ ] Favicon file (`.ico` or `.png`)
- [ ] Open Graph image (1200×630px recommended)
- [ ] Logo variants (if different from current)
- [ ] Any product photography updates

### App Configuration (Owner completes in admin)

- [ ] Judge.me app installed
- [ ] Judge.me metafield sync enabled
- [ ] Judge.me default widget disabled (custom rendering per D-025)
- [ ] Help Scout saved replies created (per `m4b-helpscout-alignment.md`)
- [ ] Tidio knowledge base imported (per `m4b-tidio-knowledge-base.md`)

### Team Readiness

- [ ] Support team briefed on new site design
- [ ] Launch window communicated to team
- [ ] Owner available for launch window + 2 hours post-publish
- [ ] Owner has Shopify admin access confirmed
- [ ] Owner has Help Scout access confirmed

---

## During Launch

### At T-0 (Theme Publish)

- [ ] Confirm availability — Builder is about to publish
- [ ] Have personal mobile device ready for testing
- [ ] Have Help Scout open in a browser tab

### At T+5min (Immediate Verification)

- [ ] Builder reports initial verification results
- [ ] Open `barreletics.com` on personal phone
- [ ] Confirm site looks correct on your device

### At T+15min (Go/Rollback Decision)

- [ ] Review Builder's verification report
- [ ] Check Help Scout — any customer complaints?
- [ ] **Declare "GO" or "ROLLBACK"**
  - GO: "Launch approved. Continue monitoring."
  - ROLLBACK: "Rollback now. [Reason]."

### At T+30min (Test Transaction)

- [ ] Place test order with real payment method on personal device
- [ ] Verify order confirmation email received
- [ ] Verify order appears in Shopify admin
- [ ] Confirm to Builder: "Test order successful" or "Test order failed — [details]"

### At T+1h and T+2h (Status Checks)

- [ ] Review Builder's status report
- [ ] Check Help Scout for any theme-related tickets
- [ ] Confirm: "All clear" or "Issue: [details]"

---

## After Launch

### 24-Hour Review

- [ ] Review `m4d-24h-checklist.md` results from Builder
- [ ] Compare revenue to prior week (Shopify admin → Analytics)
- [ ] Review Help Scout tickets from past 24 hours
- [ ] Confirm: "24-hour review satisfactory" or "Concerns: [details]"

### 7-Day Stabilization

- [ ] Review daily summaries from Builder (Days 1–3)
- [ ] Review weekly summary from Builder (Day 7)
- [ ] Check SEO rankings for key terms (if accessible)
- [ ] Review customer feedback patterns

### Stabilization Complete

- [ ] 7 days with no critical issues
- [ ] Revenue within expected range
- [ ] No customer complaints related to theme
- [ ] **Declare stabilization complete:** "M4D stabilization approved. Theme is production-stable."

---

## Quick Contacts

| Role | Contact | When to Use |
|------|---------|-------------|
| Builder | [contact info] | Any technical issue |
| Shopify Support | support@shopify.com | Platform issues |
| Help Scout | [admin URL] | Customer complaints |

---

## Key Documents Reference

| Document | When You Need It |
|----------|-----------------|
| `m4d-launch-plan.md` | Full launch plan overview |
| `m4d-rollback-procedure.md` | If rollback is needed |
| `m4d-decision-tree.md` | Go/rollback decision guide |
| `m4d-severity-matrix.md` | How to classify an issue |
| `m4d-24h-checklist.md` | 24-hour review |
| `m4d-7day-stabilization.md` | Week 1 monitoring |
| `m4b-environment-config.md` | Tracking ID reference |
| `m4b-helpscout-alignment.md` | Help Scout saved reply content |
| `m4b-tidio-knowledge-base.md` | Tidio knowledge base content |
