# M4D — Launch Day Timeline

**Purpose:** Hour-by-hour schedule for theme launch day. Each checkpoint includes a decision point: **Proceed / Hold / Rollback.**

---

## T-24h — Final Preview Audit

**Owner + Builder**

- [ ] Complete final preview audit on Shopify preview theme
- [ ] All 15 deferred M4C validations confirmed PASS with evidence
- [ ] Owner provides written launch approval
- [ ] Team notification sent: "Launch scheduled for [date/time]"
- [ ] Confirm Owner availability for launch window + 2 hours post-publish

**Decision:** All preview validations pass and Owner approves → **Proceed** to T-12h prep.

---

## T-12h — Baseline Capture

**Builder (Owner provides GA4 access)**

- [ ] Capture DNS snapshot (`m4d-dns-checklist.md` pre-launch section)
- [ ] Capture analytics baseline:
  - GA4 last 7 days: sessions, users, revenue by channel (screenshot)
  - Shopify admin: orders and revenue for last 7 days (screenshot)
- [ ] Verify backup theme .zip export is complete and saved
- [ ] Verify backup theme ID is recorded in `m4d-rollback-procedure.md`

**Decision:** Baseline captured, backup verified → **Proceed.**

---

## T-4h — Final Content Review

**Joint**

- [ ] Final content review: spot-check 5 pages for correct copy
- [ ] Verify all tracking IDs are entered in Theme Settings
- [ ] Run one test transaction on preview (if Shopify allows)
- [ ] Confirm Help Scout / Tidio are ready (or documented as pending IDs)

**Decision:** Content correct, tracking configured → **Proceed.**

---

## T-2h — Team Standup

**Owner + Builder**

- [ ] Brief standup (5 minutes):
  - Confirm roles: who publishes, who monitors, who communicates
  - Review rollback procedure (`m4d-rollback-procedure.md`)
  - Confirm communication plan (who to contact if issues arise)
- [ ] Confirm Owner will be available for the next 4 hours
- [ ] Confirm Builder will be available for the next 8 hours

**Decision:** Both parties available and aligned → **Proceed.**

---

## T-1h — Final Preparation

**Builder**

- [ ] Final backup of current live theme (even if already done — one more for safety)
- [ ] Notify support team: "Theme change happening in ~1 hour. Watch for customer reports."
- [ ] Open monitoring tools:
  - Shopify admin (Orders, Analytics)
  - GA4 Realtime
  - Help Scout inbox
  - Browser with `barreletics.com` ready

**Decision:** All tools open, support notified → **Proceed to publish.**

---

## T-0 — Theme Publish

**Builder (Owner on standby)**

- [ ] Follow `m4d-theme-publish-checklist.md` Steps 1–5 exactly
- [ ] Record exact publish time: `________________`
- [ ] Notify Owner: "Theme published. Starting verification."

---

## T+5min — Immediate Verification

**Builder**

- [ ] Homepage loads ✅/❌
- [ ] Navigation works ✅/❌
- [ ] PDP loads with product data ✅/❌
- [ ] Add to Cart works ✅/❌
- [ ] Checkout reachable ✅/❌
- [ ] Mobile loads correctly ✅/❌

**Decision:**
- All pass → **Proceed** to T+15min
- Any fail → Consult `m4d-decision-tree.md` → likely **ROLLBACK**

---

## T+15min — Full Page Audit

**Builder**

- [ ] JS console: zero critical errors
- [ ] Analytics beacons firing (GA4, Meta if configured)
- [ ] 5 sample redirects working
- [ ] Key supporting pages load (FAQ, About, Contact, Shipping, Returns)
- [ ] No unexpected 404s

**Decision:**
- All clear → **Proceed** to T+30min
- P0 issue → **ROLLBACK**
- P1/P2 issue → Assess with Owner → Fix forward or hold

---

## T+30min — Customer-Facing Check

**Joint**

- [ ] Place test order with real payment method
- [ ] Verify order in Shopify admin
- [ ] Verify email confirmation
- [ ] Cancel/refund test order
- [ ] Check Help Scout — any customer complaints?
- [ ] Check social media — any customer reports?

**Decision:**
- Test order succeeds, no complaints → **Proceed** to hourly monitoring
- Test order fails → **ROLLBACK** (P0)
- Customer complaints about broken functionality → Assess severity

---

## T+1h — First Status Check

**Builder (report to Owner)**

- [ ] GA4 Realtime: traffic flowing normally
- [ ] Shopify admin: any new orders since launch? Normal volume?
- [ ] Help Scout: any theme-related tickets?
- [ ] Console: still clean on re-check
- [ ] Site speed: subjectively feels normal

**Report to Owner:** "[Time] — 1-hour check: [all clear / issue summary]"

---

## T+2h — Second Status Check

**Builder (report to Owner)**

- [ ] Repeat T+1h checks
- [ ] Compare order count to same time period last week
- [ ] Any new 404s in Shopify reports?
- [ ] Any tracking anomalies in GA4?

**Report to Owner:** "[Time] — 2-hour check: [all clear / issue summary]"

---

## T+4h — Third Status Check

**Builder (report to Owner)**

- [ ] All previous checks
- [ ] Revenue comparison: within expected range vs. baseline?
- [ ] Conversion rate: normal?
- [ ] Run PageSpeed Insights on homepage — score acceptable?

**Decision:**
- All metrics normal → **Declare "all clear"** for active monitoring phase
- Any anomaly → Investigate and report to Owner
- Persistent P1 issue unfixed → Discuss rollback with Owner

**Report to Owner:** "[Time] — 4-hour check: [all clear / monitoring continues with reduced frequency]"

---

## T+8h — End of Active Monitoring

**Builder**

- [ ] Final comprehensive check (all items from T+4h)
- [ ] Document any issues encountered and their status
- [ ] Transition to passive monitoring (check morning and evening)

**Report to Owner:** "[Time] — Active monitoring complete. No critical issues. Transitioning to daily checks per `m4d-24h-checklist.md`."

---

## T+24h — Full 24-Hour Review

**Joint**

- [ ] Complete `m4d-24h-checklist.md`
- [ ] Compare 24-hour metrics to baseline:
  - Revenue
  - Order count
  - Conversion rate
  - Bounce rate
  - Page load time
- [ ] Review all Help Scout tickets from past 24 hours
- [ ] Document any issues and resolutions
- [ ] Decision: Transition to 7-day stabilization (`m4d-7day-stabilization.md`)

**Report to Owner:** "24-hour review complete. [Summary]. Transitioning to 7-day stabilization."
