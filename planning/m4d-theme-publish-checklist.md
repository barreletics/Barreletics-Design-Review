# M4D — Shopify Theme Publish Checklist

**Purpose:** Step-by-step procedure for publishing the Barreletics theme to production. Follow exactly in order. Do not skip steps.

---

## Pre-Publish Gate

All of these must be TRUE before proceeding:

- [ ] All 15 deferred M4C validations PASS with evidence (`m4d-deferred-validations.md`)
- [ ] Owner has approved launch (verbal or written)
- [ ] Backup theme exported and ID recorded
- [ ] Rollback procedure reviewed by Owner and Builder
- [ ] DNS snapshot captured (`m4d-dns-checklist.md`)
- [ ] Analytics baseline captured (GA4 screenshot of last 7 days)
- [ ] Launch day timeline confirmed (`m4d-launch-day-timeline.md`)
- [ ] Team notified of maintenance window

---

## Publish Procedure

### Step 1: Final Preview Verification

- [ ] Open preview theme in Shopify admin → Online Store → Themes → Preview
- [ ] Verify homepage loads with correct hero, sections, footer
- [ ] Verify one PDP loads with correct buy box, features, reviews section
- [ ] Verify collection page loads with product grid
- [ ] Verify cart drawer opens on Add to Cart
- [ ] Confirm: "Preview looks correct — ready to publish"

### Step 2: Backup Current Live Theme

- [ ] Shopify admin → Online Store → Themes
- [ ] On the current live theme, click **⋯ → Download theme file**
- [ ] Save .zip file with name: `barreletics-backup-[YYYY-MM-DD].zip`
- [ ] Record current live theme ID: `________________`
- [ ] Record current live theme name: `________________`

### Step 3: Record Pre-Publish State

- [ ] Note exact time: `________________`
- [ ] Open GA4 Realtime to observe traffic baseline
- [ ] Open Shopify admin → Orders (note most recent order number)

### Step 4: Notify Team

- [ ] Message Owner: "Publishing theme now. Monitoring for 15 minutes. Will confirm go/rollback."
- [ ] Ensure Builder has Shopify admin open in a separate tab

### Step 5: Publish New Theme

- [ ] Shopify admin → Online Store → Themes
- [ ] On the new theme, click **⋯ → Publish**
- [ ] Confirm publish
- [ ] Note exact publish time: `________________`

### Step 6: Immediate Verification (T+0 to T+5min)

Open `barreletics.com` in an **incognito/private browser window**:

- [ ] **Homepage loads** — hero visible, navigation present, footer visible
- [ ] **Navigation works** — click "Grippy Shoes" → collection loads
- [ ] **PDP loads** — click a product → buy box, images, price visible
- [ ] **Add to Cart works** — select size, click Add to Cart → cart drawer opens
- [ ] **Checkout reachable** — click Checkout in cart drawer → Shopify checkout loads
- [ ] **Mobile loads** — open on phone or DevTools mobile → site renders correctly

**Decision point:** If ANY of the above fail → see `m4d-decision-tree.md` → likely ROLLBACK.

### Step 7: Console and Error Check (T+5min)

- [ ] Open DevTools (F12) → Console tab
- [ ] Navigate: homepage → collection → PDP → open cart drawer
- [ ] **Zero critical JavaScript errors** (warnings are acceptable)
- [ ] Network tab: no failed requests (red entries) for theme assets

### Step 8: Tracking Verification (T+5 to T+10min)

- [ ] GA4 Realtime → verify your pageview appears (if GA4 ID configured)
- [ ] DevTools → Network → filter "gtag" or "collect" → verify beacon fires
- [ ] DevTools → Network → filter "facebook" or "fbevents" → verify pixel fires (if Meta ID configured)

### Step 9: Redirect Spot-Check (T+10min)

Test 5 redirects from `m4a-redirect-map.md`:

- [ ] Redirect 1: `________________` → `________________` ✅/❌
- [ ] Redirect 2: `________________` → `________________` ✅/❌
- [ ] Redirect 3: `________________` → `________________` ✅/❌
- [ ] Redirect 4: `________________` → `________________` ✅/❌
- [ ] Redirect 5: `________________` → `________________` ✅/❌

### Step 10: Key Pages Check (T+10 to T+15min)

Verify these pages load without errors:

- [ ] `/pages/faq`
- [ ] `/pages/about`
- [ ] `/pages/contact`
- [ ] `/pages/shipping`
- [ ] `/pages/returns`
- [ ] `/blogs/journal`

### Step 11: Payment Verification (T+15min)

- [ ] Place a test order with real payment method
- [ ] Verify order appears in Shopify admin → Orders
- [ ] Verify email confirmation received
- [ ] Cancel/refund test order
- [ ] Test transaction ID: `________________`

### Step 12: 15-Minute Decision

- [ ] All steps above pass → **DECLARE "GO"** → notify Owner
- [ ] Any P0 failure → **ROLLBACK** → follow `m4d-rollback-procedure.md`
- [ ] P1 or P2 issue → **ASSESS** → can it be fixed forward? Discuss with Owner.

### Step 13: Begin Monitoring

- [ ] Transition to `m4d-monitoring-plan.md` for hour-by-hour checks
- [ ] Keep Shopify admin, GA4, and Help Scout open for the next 4 hours
- [ ] Notify Owner: "Launch successful. Entering monitoring phase."
