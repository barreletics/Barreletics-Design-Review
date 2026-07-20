# M4D — Hour-by-Hour Monitoring Plan

**Purpose:** Structured monitoring schedule for the first 24 hours post-launch. Each check has an owner, tool, and expected result.

---

## Monitoring Schedule

### Hour 0–1 (Immediately Post-Publish)

| Check | Owner | Tool | Expected Result | Actual |
|-------|-------|------|-----------------|--------|
| Site loads, no blank pages | Builder | Browser (incognito) | All major pages render | |
| Zero critical JS errors | Builder | Browser DevTools → Console | No red errors | |
| GA4 analytics firing | Builder | GA4 Realtime report | Pageview events visible | |
| Meta Pixel firing (if ID set) | Builder | DevTools → Network → "fbevents" | Pixel beacon fires | |
| Pinterest Tag firing (if ID set) | Builder | DevTools → Network → "pintrk" | Tag beacon fires | |
| Transactions working | Joint | Shopify Admin → Orders | Test order succeeds | |
| Cart drawer functional | Builder | Browser → Add to Cart | Drawer opens, items display | |
| Mobile rendering correct | Builder | Phone or DevTools mobile | No overflow, readable | |

### Hour 1–4 (Active Monitoring)

| Check | Owner | Tool | Expected Result | Actual |
|-------|-------|------|-----------------|--------|
| Customer complaints | Owner | Help Scout inbox | None related to theme | |
| 404 errors | Builder | Shopify Admin → Analytics → Reports | Zero unexpected 404s | |
| Redirect functionality | Builder | Browser → test 5 URLs from redirect map | All 301 correctly | |
| Order flow intact | Owner | Shopify Admin → Orders | Orders coming in normally | |
| Forms working | Builder | Submit test contact form | Form submits, appears in Shopify | |
| Search functioning | Builder | Site search → query a product | Results appear | |

### Hour 4–8 (Reduced Monitoring)

| Check | Owner | Tool | Expected Result | Actual |
|-------|-------|------|-----------------|--------|
| Revenue tracking | Owner | Shopify Admin → Analytics | Normal order volume | |
| Site speed | Builder | PageSpeed Insights | Performance score ≥50 (Shopify baseline) | |
| Conversion rate | Owner | Shopify Admin → Analytics | No significant drop | |
| Help Scout volume | Owner | Help Scout dashboard | Normal ticket volume | |
| Clarity recordings (if ID set) | Builder | Microsoft Clarity dashboard | Sessions recording | |

### Hour 8–24 (Passive Monitoring)

| Check | Owner | Tool | Expected Result | Actual |
|-------|-------|------|-----------------|--------|
| Overall stability | Joint | All channels | No new issues reported | |
| Daily revenue comparison | Owner | Shopify Admin | Within baseline range | |
| GA4 data integrity | Builder | GA4 → Reports | Data flowing, no gaps | |
| Structured data | Builder | Google Search Console (if verified) | No new errors | |
| Bounce rate | Builder | GA4 → Pages and screens | No significant increase | |

---

## Escalation Triggers

During monitoring, immediately escalate if any of these occur:

| Trigger | Severity | Action |
|---------|----------|--------|
| Site goes down | P0 | Rollback immediately → notify Owner |
| Checkout stops working | P0 | Rollback immediately → notify Owner |
| Revenue drops to zero for >30 minutes during business hours | P0 | Investigate → likely rollback |
| Multiple customers report same issue | P1 | Investigate → notify Owner within 30 min |
| Tracking stops firing | P2 | Investigate → fix forward → notify Owner within 2 hours |
| Cosmetic issue reported | P3 | Log for fix → notify Owner in daily summary |

See `m4d-severity-matrix.md` for full severity definitions and response times.

---

## Monitoring Tools Quick Reference

| Tool | URL / Access | What to Check |
|------|-------------|---------------|
| Shopify Admin | `barreletics.myshopify.com/admin` | Orders, themes, analytics |
| GA4 | `analytics.google.com` (Property 300437005) | Realtime, acquisition, events |
| Google Search Console | `search.google.com/search-console` | Indexing, errors |
| PageSpeed Insights | `pagespeed.web.dev` | Performance, accessibility |
| Help Scout | `secure.helpscout.net` | Customer tickets |
| Microsoft Clarity | `clarity.microsoft.com` | Session recordings, heatmaps |
| Browser DevTools | F12 / Cmd+Option+I | Console, Network, Coverage |

---

## Handoff

At T+8h, Builder sends Owner a summary:

```
Launch Day Report — [Date]
Published at: [time]
Status: [All Clear / Issues Noted]

Checks completed:
- Immediate verification: PASS
- Console errors: NONE
- Analytics: FIRING
- Test transaction: PASS
- Redirects: [X/5] working
- Customer complaints: NONE
- Revenue: [normal/above/below] baseline

Issues (if any):
- [Issue description] — [Status: fixed/monitoring/escalated]

Next: Transitioning to daily monitoring per m4d-24h-checklist.md
```
