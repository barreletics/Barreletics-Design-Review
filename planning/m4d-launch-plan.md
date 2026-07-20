# M4D — Launch Preparation Plan

**Gate:** M4D — Launch  
**Status:** 🟡 In Progress  
**Entry Criterion:** M4C Validation locked (D-047)  
**Exit Criterion:** Theme live, test transaction verified, 24-hour monitoring clean

---

## Critical Rule

The 15 N/A validation items from M4C **MUST** be validated during M4D with actual evidence from the deployed Shopify preview or production. No feature work. Only fixes discovered during launch validation.

---

## Pre-Launch Checklist

### Responsibility: Owner

- [ ] Provide all tracking IDs (per `m4b-environment-config.md`)
  - GA4 Measurement ID
  - Meta Pixel ID
  - Pinterest Tag ID
  - Microsoft Clarity Project ID
  - Google Search Console verification code
  - Help Scout Beacon ID
  - Tidio Public Key
- [ ] Complete Policy Freeze Gate sign-off (shipping, returns, warranty, pricing, discounts, wholesale, studio, ambassador terms)
- [ ] Approve hero headline concept (D-041 — choose between current and alternative)
- [ ] Provide production assets (favicon, OG image, logo variants)
- [ ] Review and approve all "Needs Review" content items from content inventory
- [ ] Confirm collection structure (which collections to create)
- [ ] Review and approve redirect map
- [ ] Confirm Judge.me app installed and metafield sync enabled
- [ ] Confirm Help Scout saved replies updated (per `m4b-helpscout-alignment.md`)
- [ ] Confirm Tidio knowledge base imported (per `m4b-tidio-knowledge-base.md`)

### Responsibility: Builder

- [ ] Insert tracking IDs into theme settings (after Owner provides)
- [ ] Upload theme to Shopify as unpublished preview
- [ ] Configure theme settings with production values
- [ ] Create navigation menus per `m4a-navigation-config.md`
- [ ] Create required collections (only those approved by Owner)
- [ ] Create supporting pages
- [ ] Populate metafields
- [ ] Configure forms routing
- [ ] Upload production assets

### Responsibility: Joint

- [ ] Run the 15 deferred M4C validations on preview environment (with evidence) — see `m4d-deferred-validations.md`
- [ ] Verify purchase flow end-to-end on preview
- [ ] Verify all integrations fire correctly
- [ ] Lighthouse audit on preview
- [ ] Real device testing (minimum: iPhone Safari, Android Chrome, Desktop Chrome)

---

## Backup & Rollback

- [ ] Export current live theme as .zip backup
- [ ] Document current theme ID for rollback reference
- [ ] Test rollback procedure: verify backup theme can be published
- [ ] Document rollback trigger criteria (what constitutes a rollback-worthy issue) — see `m4d-decision-tree.md`
- [ ] Document rollback procedure (step-by-step for Owner or Builder) — see `m4d-rollback-procedure.md`
- [ ] Capture pre-launch analytics baseline (Owner provides GA4 screenshot/export)

---

## Theme Publish Sequence

1. Final preview verification (all M4C deferred items pass with evidence)
2. Schedule maintenance window (low-traffic period — check GA4 for optimal time)
3. Publish new theme

**Immediately verify:**
- [ ] Homepage loads
- [ ] Navigation works
- [ ] A product page loads
- [ ] Add to Cart works
- [ ] Checkout reachable
- [ ] Mobile loads correctly

**Monitor for 15 minutes:**
- [ ] No JavaScript errors in console
- [ ] No 404 errors
- [ ] Analytics firing
- [ ] No customer complaints

See `m4d-decision-tree.md` for go/rollback decision at each checkpoint.

---

## Real Transaction Test

- [ ] Place test order with real payment method
- [ ] Verify order appears in Shopify admin
- [ ] Verify analytics event fired (if tracking IDs configured)
- [ ] Verify email confirmation received
- [ ] Cancel/refund test order
- [ ] Document test transaction ID and result

---

## Immediate Monitoring (First 24 Hours)

- [ ] Check for 404 errors (Shopify admin → Analytics → Reports)
- [ ] Check redirect functionality (test 5 sample redirects)
- [ ] Monitor site speed (Shopify speed report)
- [ ] Check mobile rendering on real devices
- [ ] Monitor Help Scout for customer issues
- [ ] Check GA4 real-time for traffic flow
- [ ] Verify no revenue disruption

See `m4d-monitoring-plan.md` for hour-by-hour schedule and `m4d-24h-checklist.md` for the full 24-hour checklist.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| `m4d-deferred-validations.md` | 15 N/A items from M4C with evidence methods |
| `m4d-rollback-procedure.md` | Step-by-step rollback |
| `m4d-dns-checklist.md` | DNS verification |
| `m4d-theme-publish-checklist.md` | Publish procedure |
| `m4d-launch-day-timeline.md` | Hour-by-hour launch schedule |
| `m4d-monitoring-plan.md` | 24-hour monitoring |
| `m4d-24h-checklist.md` | Post-launch verification |
| `m4d-7day-stabilization.md` | Week 1 stabilization |
| `m4d-severity-matrix.md` | Issue classification |
| `m4d-decision-tree.md` | Go/rollback logic |
| `m4d-owner-launch-checklist.md` | Owner's personal checklist |
