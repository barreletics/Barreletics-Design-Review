# 08 — Customer Cohort Framework

**Purpose:** Measure retention and repurchase for Barreletics DTC buyers.  
**Audience:** Founder, Marketing.  
**Related:** [09](./09-ltv-measurement-framework.md), [03](./03-ecommerce-kpi-definitions.md).

---

## Why cohorts matter

Grip shoes are durable (“one pair replaces eight” socks). Repurchase cadence differs from consumable apparel. Cohorts prevent mistaking slow-but-healthy repurchase for “churn.”

---

## Cohort definitions

### Acquisition cohort

| Field | Value |
|-------|-------|
| **Definition** | Customers whose **first paid order** falls in a calendar month (or week) |
| **Formula** | Group customers by month(first_order_date) |
| **Data source** | Shopify Customers / Orders |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly |
| **Target** | N/A — structural |

### Channel cohort (optional cut)

| Field | Value |
|-------|-------|
| **Definition** | Acquisition cohort further split by first-order UTM/channel |
| **Formula** | First-order attribution label ([04](./04-marketing-attribution-framework.md)) |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly |
| **Target** | Compare Paid Social vs Organic vs Email quality |

---

## Retention KPIs

### Repeat purchase rate (RPR) — 90-day

| Field | Value |
|-------|-------|
| **Definition** | Share of cohort with a second paid order within 90 days of first order |
| **Formula** | Customers with ≥2 orders within 90d ÷ Cohort size |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly (lagged — wait 90d before scoring a cohort) |
| **Target** | TBD — set from 90-day baseline |

### Repeat purchase rate — 180-day / 365-day

| Field | Value |
|-------|-------|
| **Definition** | Same as RPR with longer windows (better for durable goods) |
| **Formula** | Customers with ≥2 orders within N days ÷ Cohort size |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Quarterly |
| **Target** | TBD — set from 90-day baseline |

### Time to second order (median)

| Field | Value |
|-------|-------|
| **Definition** | Typical gap between order 1 and order 2 |
| **Formula** | Median(second_order_date − first_order_date) among repeaters |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Quarterly |
| **Target** | TBD — set from 90-day baseline; informs email cadence |

### Cohort revenue retention

| Field | Value |
|-------|-------|
| **Definition** | Net sales from cohort in month N after acquisition |
| **Formula** | Sum net sales from cohort members in period N ÷ Cohort acquisition net sales (month 0) |
| **Data source** | Shopify |
| **Owner** | Founder / Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Product-path cohorts (Barreletics-specific)

| Cohort cut | Why |
|------------|-----|
| First product: Open Sole vs Closed Sole | Cross-sell opportunity |
| First order: single pair vs multi-pair | Bundle / SAVE15 behavior |
| First order included apparel | Attach strategy |
| Color snugness note (Dark Grey / Hot Coral / Blue) | Fit/return risk |

### KPI: Open→Closed (or reverse) attach within 180 days

| Field | Value |
|-------|-------|
| **Definition** | Buyers who add the other sole type after first purchase |
| **Formula** | Customers who bought both sole types within 180d ÷ Open-or-Closed first-time buyers |
| **Data source** | Shopify line items |
| **Owner** | Marketing |
| **Reporting cadence** | Quarterly |
| **Target** | TBD — set from 90-day baseline |

---

## Reporting views

1. **Triangle / heatmap:** Cohort month × months since acquisition → RPR or revenue  
2. **Channel quality:** RPR and LTV by first-touch channel  
3. **Product path:** Second product mix  

Documentation only — spreadsheet or BI later.

---

## Rules

- Exclude fully refunded first orders from cohort size when measuring quality.  
- Wholesale accounts excluded from DTC cohorts ([17](./17-wholesale-kpi-dashboard.md)).  
- Ambassadors with heavy comps tagged separately ([18](./18-ambassador-kpi-dashboard.md)).

---

## Cross-links

- LTV → [09](./09-ltv-measurement-framework.md)  
- CAC → [10](./10-cac-measurement-framework.md)  
- Monthly review → [20](./20-monthly-executive-review-process.md)
