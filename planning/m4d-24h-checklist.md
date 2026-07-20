# M4D — 24-Hour Post-Launch Checklist

**Purpose:** Comprehensive verification at the 24-hour mark after theme publish. Completion of this checklist is required before transitioning to 7-day stabilization.

---

## Revenue & Orders

- [ ] Revenue compared to same day last week (no unexpected drop >20%)
- [ ] Order count compared to same day last week
- [ ] Average order value within normal range
- [ ] No stuck/failed orders in Shopify admin

## Conversion & Traffic

- [ ] Conversion rate compared to baseline (no drop >30%)
- [ ] Session count in GA4 comparable to baseline
- [ ] Bounce rate not significantly elevated
- [ ] Traffic by channel flowing normally (organic, direct, paid, email)

## Technical Health

- [ ] Page load time stable (PageSpeed Insights — homepage, PDP, collection)
- [ ] Zero critical JavaScript errors (check Console on 3 pages)
- [ ] No mixed content warnings
- [ ] All CSS/JS assets loading (DevTools → Network → no red/failed requests)

## Functionality

- [ ] Cart and checkout fully operational (verified by test or real orders)
- [ ] All forms tested:
  - [ ] Contact form
  - [ ] Newsletter signup
  - [ ] Partner inquiry form
- [ ] Search functioning (test 2 queries)
- [ ] Cart drawer opens and closes correctly
- [ ] Variant selection works on PDP

## Navigation & Redirects

- [ ] All main navigation links work
- [ ] All footer links work
- [ ] All redirects functioning (spot-check 5 from redirect map)
- [ ] No unexpected 404s in Shopify reports

## Integrations

- [ ] GA4 data flowing (check Reports → Realtime)
- [ ] Meta Pixel data flowing (if ID configured)
- [ ] Pinterest Tag data flowing (if ID configured)
- [ ] Clarity recording sessions (if ID configured)
- [ ] Help Scout Beacon loading (if ID configured)
- [ ] Tidio widget loading (if ID configured)
- [ ] Judge.me reviews displaying (if metafield sync enabled)

## Mobile

- [ ] Mobile experience verified on real iPhone (Safari)
- [ ] Mobile experience verified on real Android (Chrome)
- [ ] No horizontal overflow
- [ ] Touch targets adequate
- [ ] Cart drawer functional on mobile

## Customer Experience

- [ ] No customer complaints related to theme change (Help Scout)
- [ ] No social media reports of issues
- [ ] Email confirmation templates still working (verified by test order or real orders)

## SEO

- [ ] Sitemap accessible at `/sitemap.xml`
- [ ] `robots.txt` accessible and correct
- [ ] No new crawl errors in Google Search Console (if verified)
- [ ] Structured data still present (spot-check one PDP in Rich Results Test)

---

## 24-Hour Verdict

- [ ] **All checks pass** → Transition to `m4d-7day-stabilization.md`
- [ ] **Non-critical issues remain** → Document in issues log, proceed to stabilization
- [ ] **Critical issue discovered** → Assess rollback per `m4d-decision-tree.md`

**Completed by:** `________________`  
**Date/Time:** `________________`  
**Verdict:** `________________`
