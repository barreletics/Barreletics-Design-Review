# 09 — LTV Measurement Framework

**Purpose:** Define Lifetime Value for Barreletics customers without fake precision.  
**Audience:** Founder, Marketing.  
**Related:** [08](./08-customer-cohort-framework.md), [10](./10-cac-measurement-framework.md), [12](./12-profitability-dashboard.md).

---

## Principles

1. Prefer **observed** LTV from cohorts over speculative multi-year models until history is deep.  
2. Report **gross LTV** (net sales) and **contribution LTV** (after COGS/refunds) separately.  
3. Durable footwear → longer windows (180d / 365d) matter more than 30-day LTV alone.  
4. Always pair LTV with CAC from the **same attribution definition**.

---

## LTV variants

### Observed LTV (historical)

| Field | Value |
|-------|-------|
| **Definition** | Cumulative net sales per customer from first order through window end |
| **Formula** | Sum of customer net sales in window ÷ Customers in cohort  
Window examples: 90d, 180d, 365d from first order |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Predicted LTV (optional later)

| Field | Value |
|-------|-------|
| **Definition** | Model-based expected future value |
| **Formula** | TBD method (not locked) — e.g. simple: Observed_365d × retention factor |
| **Data source** | Shopify + model sheet |
| **Owner** | Founder |
| **Reporting cadence** | Quarterly if used |
| **Target** | Do not use for budget until validated against observed |

### Contribution LTV

| Field | Value |
|-------|-------|
| **Definition** | Customer value after product cost and refunds (before or after ads — label clearly) |
| **Formula** | (Net sales − COGS − refunds) cumulative per customer ÷ customers  
*Ads excluded here; ads live in CAC* |
| **Data source** | Shopify + COGS |
| **Owner** | Founder |
| **Reporting cadence** | Monthly / Quarterly |
| **Target** | TBD — set from 90-day baseline |

---

## Blended vs channel LTV

| Type | Formula note | Use |
|------|--------------|-----|
| **Blended LTV** | All DTC customers | Company health |
| **Channel LTV** | Cohort by first-order channel | Judge Paid Social vs Organic quality |
| **Product-entry LTV** | By first SKU type | Merchandising |

### KPI: LTV:CAC (blended)

| Field | Value |
|-------|-------|
| **Definition** | Payback quality of acquisition |
| **Formula** | Blended Observed LTV (chosen window) ÷ Blended CAC ([10](./10-cac-measurement-framework.md)) |
| **Data source** | Shopify + Blend |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline; discuss ≥3:1 only as a heuristic until baseline locked |

---

## Window selection guide

| Window | Use when |
|--------|----------|
| 90-day | Fast read on email/flows and early second pair |
| 180-day | Better for Open/Closed cross-sell |
| 365-day | Annual planning ([22](./22-annual-planning-framework.md)) |

Always label the window in the metric name: `LTV_180d`, not bare “LTV.”

---

## Exclusions

- Wholesale customers  
- Fully refunded one-and-done fraud/test  
- Heavy comp / influencer gifts (tag and exclude or segment)

---

## Readout template

1. `LTV_90d` / `LTV_180d` blended  
2. Same by Paid Social vs Organic vs Email first touch  
3. Contribution LTV vs gross LTV gap (refund/COGS pressure)  
4. LTV:CAC vs prior month  
5. Decision: scale channels with strong LTV:CAC on **Shopify** attribution

---

## Cross-links

- Cohorts → [08](./08-customer-cohort-framework.md)  
- CAC → [10](./10-cac-measurement-framework.md)  
- Profitability → [12](./12-profitability-dashboard.md)  
- North star → [02](./02-north-star-metrics.md)
