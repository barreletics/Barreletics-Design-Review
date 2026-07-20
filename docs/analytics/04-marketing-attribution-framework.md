# 04 — Marketing Attribution Framework

**Purpose:** Rules for assigning credit when Shopify, GA4, and Meta disagree.  
**Audience:** Founder, Marketing.  
**Related:** [05](./05-meta-ads-reporting-framework.md), [06](./06-ga4-measurement-plan.md), [07](./07-shopify-reporting-guide.md), [11](./11-roas-measurement-framework.md).

---

## Core doctrine

| Priority | System | Use for |
|----------|--------|---------|
| 1 | **Shopify** | Revenue, orders, UTM/source on the order, customer identity |
| 2 | **Blend / ad platforms** | Spend, delivery, auction diagnostics |
| 3 | **GA4** | Sessions, pathing, channel groups, *directional* revenue |
| 4 | **Meta claimed conversions** | Creative learning signals only — **not** P&L |

**Rule:** Never scale paid media solely because Meta or GA4 report purchases that Shopify does not show under paid UTMs.

---

## Attribution models in use

### A. Shopify last-click / channel (decision model)

| Field | Value |
|-------|-------|
| **Definition** | Credit as recorded on the Shopify order (UTM, referring channel, sales channel) |
| **Formula** | Group net sales by Shopify `utm_source` / `utm_medium` / `utm_campaign` (and channel reports) |
| **Data source** | Shopify Orders |
| **Owner** | Marketing |
| **Reporting cadence** | Daily / Weekly |
| **Target** | N/A — process metric; hygiene target: ≥95% of paid landings carry UTMs |

### B. GA4 default channel group (diagnostic)

| Field | Value |
|-------|-------|
| **Definition** | Session-scoped channel classification |
| **Formula** | GA4 `sessionDefaultChannelGroup` with metrics sessions, activeUsers, totalRevenue |
| **Data source** | GA4 property `300437005` |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | Channel rev/session: Organic ~$2.21 · Email ~$2.25 · Paid Social ~$0.74 |

### C. Meta attribution window (platform claim)

| Field | Value |
|-------|-------|
| **Definition** | Meta’s modeled/clicked/viewed conversions in Ads Manager |
| **Formula** | Platform-reported purchases or purchase value ÷ spend = Meta ROAS |
| **Data source** | Meta / Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Daily (monitor) / Weekly (reconcile) |
| **Target** | Do not set business targets on Meta ROAS alone; track **claim ratio** below |

### KPI: Meta overclaim ratio

| Field | Value |
|-------|-------|
| **Definition** | How much Meta overstates vs Shopify Meta-UTM truth |
| **Formula** | Meta purchase count (or value) ÷ Shopify Meta-UTM order count (or net sales) |
| **Data source** | Meta + Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline; investigate if ratio rises sharply week over week |

---

## UTM standards (required for paid)

Minimum on every paid click URL:

| Param | Example | Notes |
|-------|---------|-------|
| `utm_source` | `facebook`, `instagram`, `google`, `pinterest` | Lowercase |
| `utm_medium` | `paid_social`, `cpc`, `paid` | Stable taxonomy |
| `utm_campaign` | Campaign name or ID | Match Blend campaign naming |
| `utm_content` | Ad/creative ID | Creative reporting |
| `utm_term` | Optional | Audience or keyword |

External UTM guide (owner machine): `/Users/andrewnehra/Documents/Claude/Projects/Barreletics social/utm-tracking/UTM-GUIDE.md`  
Growth Engine (by name) owns campaign URL construction; this doc owns how credit is counted.

---

## Channel taxonomy (canonical labels)

| Label | Includes | Truth for revenue |
|-------|----------|-------------------|
| Paid Social | Meta, Pinterest paid | Shopify UTMs |
| Paid Search | Google Ads / Microsoft | Shopify UTMs |
| Organic Search | SEO / brand / non-brand | Shopify + GA4 |
| Email | Flows + campaigns | Shopify / ESP |
| Direct | Typed / bookmark / dark social leakage | Shopify; investigate dark social |
| Referral | Studios, affiliates, PR | Investigate high $/session, low volume |
| Wholesale | Manual B2B orders | Tag in Shopify / notes — not Meta |

---

## Reconciliation workflow (weekly)

1. Pull Shopify net sales by UTM/source.  
2. Pull Blend spend by platform.  
3. Compute Shopify-paid ROAS ([11](./11-roas-measurement-framework.md)).  
4. Pull Meta claimed purchases/value.  
5. Compute overclaim ratio.  
6. If Meta ≫ Shopify: check CAPI duplicates, iOS webview, landing homepage vs PDP, InitiateCheckout vs Purchase mismatches.  
7. Founder decision uses **Shopify economics**, not Meta claim.

---

## Special cases

### Instagram / Facebook in-app browser

Mobile webview can inflate mid-funnel death. Treat ATC/checkout drops on Paid Social Safari/webview as operational risk (see Meta mid-funnel ATC skill / in-app webview skill by name). Attribution still uses Shopify order UTMs when present.

### Dark social / influencer

Orders may land as Direct. Use discount codes or unique UTMs for ambassadors ([18](./18-ambassador-kpi-dashboard.md)).

### Wholesale / studio

Do not attribute B2B invoice revenue to Meta. Separate channel in Shopify.

---

## Decision matrix

| Question | Use |
|----------|-----|
| Did we make money? | Shopify net sales |
| Which paid channel paid back? | Shopify UTM revenue ÷ Blend spend |
| Is Meta learning / auction healthy? | Meta delivery metrics ([05](./05-meta-ads-reporting-framework.md)) |
| Is organic/email valuable? | GA4 rev/session benchmarks |
| Is pixel broken? | Meta Events Manager vs Shopify purchase timeline |

---

## Cross-links

- Meta reporting → [05](./05-meta-ads-reporting-framework.md)  
- GA4 plan → [06](./06-ga4-measurement-plan.md)  
- ROAS → [11](./11-roas-measurement-framework.md)  
- CAC → [10](./10-cac-measurement-framework.md)  
- Tech events → `docs/15-analytics-architecture.md`
