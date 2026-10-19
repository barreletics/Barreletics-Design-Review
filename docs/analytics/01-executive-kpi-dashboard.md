# 01 — Executive KPI Dashboard

**Purpose:** Single scoreboard for daily and weekly business health.  
**Audience:** Founder / Owner; any executive operator.  
**Depends on:** [02](./02-north-star-metrics.md), [03](./03-ecommerce-kpi-definitions.md), [04](./04-marketing-attribution-framework.md), [07](./07-shopify-reporting-guide.md)  
**Related OS:** Operating System “Key Metrics to Watch” (when available on `main`).

---

## Design principles

1. **Shopify dollars first** — Net sales and orders from Shopify Admin are the headline.  
2. **Spend next** — Ad spend from Blend / platforms.  
3. **Efficiency with caveats** — ROAS and CAC always labeled by attribution source.  
4. **No vanity pack** — Impressions alone do not appear on the executive board.  
5. **Red flags over greenwash** — Prefer miss/anomaly callouts over celebration metrics.

---

## Daily board (≤10 minutes)

| KPI | Definition | Formula | Data source | Owner | Cadence | Target |
|-----|------------|---------|-------------|-------|---------|--------|
| **Net sales (DTC)** | Shopify net sales for the day (excl. tax; follow Shopify “Net sales” definition) | Sum of order net sales for date (timezone: store) | Shopify Admin → Analytics / Orders | Founder | Daily | TBD — set from 90-day baseline |
| **Orders** | Count of paid orders | Count of paid orders | Shopify | Founder / Ops | Daily | TBD — set from 90-day baseline |
| **AOV** | Average order value | Net sales ÷ Orders | Shopify | Marketing | Daily | TBD — set from 90-day baseline |
| **Ad spend (total)** | Media spend across active paid channels | Sum of platform spend | Blend (Meta + Google + Pinterest + others active) | Marketing | Daily | Stay within daily budget cap set by Founder |
| **Shopify-attributed paid revenue** | Revenue on orders with paid UTMs (esp. Meta) | Sum net sales where UTM/source = paid | Shopify (UTM / referring channel) | Marketing | Daily | Track vs spend; see [11](./11-roas-measurement-framework.md) |
| **Sessions** | Site sessions | Sessions | GA4 `300437005` | Marketing | Daily | TBD — set from 90-day baseline |
| **Stockouts (critical SKUs)** | Active grippy-shoe variants at 0 sellable | Count variants available = 0 in hero size/color matrix | Shopify Inventory | Ops | Daily | 0 critical stockouts on top sellers |

### Daily red flags

| Flag | Threshold | Action |
|------|-----------|--------|
| Shopify sales cliff | Day vs 7-day avg −40%+ with no planned promo pause | Run sales-drop diagnostic; check Meta vs Shopify gap |
| Spend without Shopify paid | Spend up, Shopify Meta-UTM flat | Pause scale; check webview / landing / pixel overclaim ([04](./04-marketing-attribution-framework.md), [05](./05-meta-ads-reporting-framework.md)) |
| Conversion collapse | ATC or purchase rate vs 7-day −50%+ | Funnel check ([16](./16-conversion-funnel-dashboard.md)) |
| Inventory hard stop | Hero Open/Closed Sole size sold out | Ops restock / suppress ads for OOS variants |

---

## Weekly board (≤30 minutes)

Include daily KPIs as weekly totals/averages, plus:

| KPI | Definition | Formula | Data source | Owner | Cadence | Target |
|-----|------------|---------|-------------|-------|---------|--------|
| **Revenue / session by channel** | Monetization efficiency of traffic | GA4 totalRevenue ÷ sessions by `sessionDefaultChannelGroup` | GA4 | Marketing | Weekly | Organic ~$2.21 · Email ~$2.25 · Paid Social ~$0.74 (baselines) |
| **Blended ROAS (Shopify)** | Revenue attributed in Shopify to paid ÷ spend | Shopify paid-channel net sales ÷ Blend spend | Shopify + Blend | Marketing | Weekly | TBD — set from 90-day baseline; never use Meta-only ROAS as sole gate |
| **Meta claimed vs Shopify Meta** | Overclaim gap | Meta purchases (or purchase value) ÷ Shopify Meta-UTM orders (or sales) | Meta Events Manager / Blend vs Shopify | Marketing | Weekly | Gap trend ↓; investigate if Meta ≫ Shopify |
| **Email revenue share** | Email contribution | Email-attributed net sales ÷ total net sales | Shopify + email platform | Marketing | Weekly | TBD — set from 90-day baseline |
| **New vs returning customers** | Acquisition vs retention mix | New customer orders ÷ total orders | Shopify | Founder | Weekly | TBD — set from 90-day baseline |
| **Refund / return rate** | Quality & fit pressure | Refunded amount ÷ net sales (or return units ÷ units sold) | Shopify | CS / Ops | Weekly | TBD — set from 90-day baseline |
| **Wholesale pipeline** | Open B2B opportunities | Count open inquiries + $ quoted | Help Scout / CRM notes | Wholesale | Weekly | Qualitative until CRM formalized |

---

## Layout recommendation (future build)

```
┌─────────────────────────────────────────────────────────┐
│  NET SALES · ORDERS · AOV          SPEND · SHOPIFY ROAS │
├───────────────────────────┬─────────────────────────────┤
│  Channel rev/session      │  Meta claimed vs Shopify    │
├───────────────────────────┼─────────────────────────────┤
│  Funnel snapshot          │  Inventory critical SKUs    │
└───────────────────────────┴─────────────────────────────┘
```

Documentation only — do not build this UI in this PR.

---

## Decision rules for executives

| Situation | Prefer | Avoid |
|-----------|--------|-------|
| “Are we making money today?” | Shopify net sales | GA4 totalRevenue alone |
| “Should we scale Meta?” | Shopify Meta-UTM ROAS + contribution margin ([12](./12-profitability-dashboard.md)) | Meta dashboard ROAS alone |
| “Is traffic quality OK?” | Channel rev/session vs benchmarks | Session count alone |
| “Is brand working?” | North stars in [02](./02-north-star-metrics.md) (monthly) | Vanity engagement |

---

## Ownership & cadence summary

| Cadence | Owner of pack | Reviewer |
|---------|---------------|----------|
| Daily | Marketing (or Founder if solo) | Founder |
| Weekly | Marketing + Ops inventory note | Founder |
| Monthly | See [20](./20-monthly-executive-review-process.md) | Founder |

---

## Cross-links

- Definitions → [03](./03-ecommerce-kpi-definitions.md)  
- Attribution → [04](./04-marketing-attribution-framework.md)  
- Profitability → [12](./12-profitability-dashboard.md)  
- Reporting how-to → [25](./25-reporting-sop.md)
