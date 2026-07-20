# Barreletics Analytics & Executive Intelligence Platform (M5)

**Status:** Documentation only — measurement system definition  
**Audience:** Founder / Owner, future executive operators, Marketing, Ops  
**Goal:** An executive can understand how Barreletics measures business health and make decisions from this doc set alone  
**Last updated:** 2026-07-20  
**Branch / PR:** `m5-analytics-platform` (does not merge open PRs #9–#14)

---

## How to use this library

1. Start with **[01 Executive KPI Dashboard](./01-executive-kpi-dashboard.md)** for the daily/weekly scoreboard.
2. Read **[02 North Star Metrics](./02-north-star-metrics.md)** for brand vs commercial north stars.
3. Use definition docs (**03–11**) when a number is disputed.
4. Use dashboard specs (**12–19**) when building or reviewing reports (future implementation).
5. Use cadence docs (**20–22**) for monthly / quarterly / annual rituals.
6. Use **[23 Data Dictionary](./23-data-dictionary.md)**, **[24 Metric Governance](./24-metric-governance.md)**, and **[25 Reporting SOP](./25-reporting-sop.md)** for naming, ownership, and how to pull numbers.

**Truth hierarchy (always):**

1. **Shopify Admin** = ground truth for revenue, orders, customers, inventory  
2. **Blend / ad platforms** = spend and platform-claimed conversions (may overclaim)  
3. **GA4 (property `300437005`)** = sessions, channel mix, on-site behavior, *directional* revenue  

When Meta ROAS looks healthy but Shopify Meta-UTM paid is flat, trust Shopify and investigate attribution — do not scale from Meta alone.

---

## Document map (25)

| # | Document | Purpose |
|---|----------|---------|
| 01 | [Executive KPI Dashboard](./01-executive-kpi-dashboard.md) | Daily/weekly scoreboard of business health |
| 02 | [North Star Metrics](./02-north-star-metrics.md) | Brand category-creation + commercial north stars |
| 03 | [Ecommerce KPI Definitions](./03-ecommerce-kpi-definitions.md) | Core DTC commerce metrics |
| 04 | [Marketing Attribution Framework](./04-marketing-attribution-framework.md) | Shopify vs GA4 vs Meta / Blend rules |
| 05 | [Meta Ads Reporting Framework](./05-meta-ads-reporting-framework.md) | Auction, creative, ROAS guardrails |
| 06 | [Google Analytics 4 Measurement Plan](./06-ga4-measurement-plan.md) | Property, events, channel benchmarks |
| 07 | [Shopify Reporting Guide](./07-shopify-reporting-guide.md) | Admin reports as source of truth |
| 08 | [Customer Cohort Framework](./08-customer-cohort-framework.md) | Retention and repurchase cohorts |
| 09 | [LTV Measurement Framework](./09-ltv-measurement-framework.md) | Lifetime value methods |
| 10 | [CAC Measurement Framework](./10-cac-measurement-framework.md) | Customer acquisition cost |
| 11 | [ROAS Measurement Framework](./11-roas-measurement-framework.md) | Return on ad spend (multi-source) |
| 12 | [Profitability Dashboard](./12-profitability-dashboard.md) | Contribution margin and unit economics |
| 13 | [Inventory Dashboard](./13-inventory-dashboard.md) | Stock health for grip shoes |
| 14 | [Product Performance Dashboard](./14-product-performance-dashboard.md) | SKU / style / color velocity |
| 15 | [Collection Performance Dashboard](./15-collection-performance-dashboard.md) | Collection merchandising health |
| 16 | [Conversion Funnel Dashboard](./16-conversion-funnel-dashboard.md) | Session → ATC → checkout → purchase |
| 17 | [Wholesale KPI Dashboard](./17-wholesale-kpi-dashboard.md) | B2B pipeline and partner health |
| 18 | [Ambassador KPI Dashboard](./18-ambassador-kpi-dashboard.md) | Ambassador program measurement |
| 19 | [Studio KPI Dashboard](./19-studio-kpi-dashboard.md) | Studio partnership measurement |
| 20 | [Monthly Executive Review Process](./20-monthly-executive-review-process.md) | Monthly ritual agenda |
| 21 | [Quarterly Business Review Framework](./21-quarterly-business-review-framework.md) | QBR structure |
| 22 | [Annual Planning Framework](./22-annual-planning-framework.md) | Yearly targets and capital allocation |
| 23 | [Data Dictionary](./23-data-dictionary.md) | Canonical field names and sources |
| 24 | [Metric Governance](./24-metric-governance.md) | Who owns definitions; change control |
| 25 | [Reporting SOP](./25-reporting-sop.md) | How to produce daily/weekly/monthly packs |

---

## How this relates to other platforms (by name)

These sibling systems may still live on open PRs. Reference by name; do not assume their files are on `main`.

| System | Typical location / PR theme | Relationship to Analytics |
|--------|----------------------------|---------------------------|
| **Operating System** | `docs/operating-system.md` (PR theme: `operating-system`, often #10) | Ops runbooks tell *what to do*; Analytics tells *what to measure*. OS “Key Metrics to Watch” should align with docs 01–02 here. Prefer reviewing Analytics **after** Operating System for dependency clarity. |
| **Growth Engine** | Growth / campaign framework PR | Campaign UTMs, landing pages, and CRO experiments feed Attribution (04), Funnel (16), Meta (05), and Monthly Review (20). |
| **SEO Platform** | SEO architecture / GEO docs | Organic Search revenue/session (~$2.21) and brand-search north star live in 02 and 06; SEO content calendar is an input, not owned here. |
| **Technical analytics architecture** | `docs/15-analytics-architecture.md` (on main) | Theme/event plumbing. This M5 set defines *business KPIs and reporting*; tech doc defines *how pixels fire*. |

---

## Roles (founder-led)

| Role | Analytics ownership |
|------|---------------------|
| **Founder / Owner** | Approves targets, profitability, pricing, partnership economics; final call on disputed metrics |
| **Marketing** | Paid media, attribution hygiene, email, Meta/GA4 interpretation |
| **Ops** | Inventory, fulfillment, product availability signals |
| **CS** | Support volume, return/exchange reasons (inputs to product quality) |
| **Wholesale / Partnerships** | Wholesale, studio, ambassador pipeline metrics |

One person may wear multiple hats. When roles conflict on a number, Founder decides and Metric Governance (24) logs the decision.

---

## KPI documentation standard

Every KPI in this library must specify:

| Field | Meaning |
|-------|---------|
| **Definition** | Plain-language what it measures |
| **Formula** | Explicit calculation |
| **Data source** | System of record |
| **Owner** | Role accountable for accuracy and action |
| **Reporting cadence** | Daily / weekly / monthly / quarterly |
| **Target** | Numeric goal, benchmark, or `TBD — set from 90-day baseline` |

---

## Connected data sources (current)

| Source | Covers | Notes |
|--------|--------|-------|
| Shopify | Orders, revenue, products, inventory, customers | **Revenue truth** |
| GA4 property `300437005` | Sessions, users, channel, geo, page | Directional revenue |
| Blend (Meta, Google Ads, Pinterest, etc.) | Spend, impressions, clicks, platform ROAS | Spend truth; conversion claims need Shopify cross-check |
| Meta Ads Manager / Events Manager | Auction + pixel/CAPI claims | Overclaim risk vs Shopify Meta-UTM |

**Channel revenue/session benchmarks (GA4):** Organic Search ~$2.21 · Email ~$2.25 · Paid Social ~$0.74 · Referral high $/session, low volume.

---

## Category Creation Strategy (measurement implication)

Barreletics replaces grip socks with **Studio Performance Skins** — we do not optimize only for “grip sock” keyword volume. Brand and SEO north stars include **branded search**, **grip sock alternative** language share, and studio density — not sock-category CPC alone. See [02 North Star Metrics](./02-north-star-metrics.md).

---

## What this PR does *not* include

- No live dashboards, Looker/Sheets builds, or theme code  
- No merge of open PRs #9–#14  
- No invented precision targets where baselines do not exist (`TBD — set from 90-day baseline`)
