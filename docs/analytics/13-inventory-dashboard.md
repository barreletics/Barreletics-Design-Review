# 13 — Inventory Dashboard

**Purpose:** Stock health for Studio Performance Skins (and apparel) to protect sales and ads.  
**Audience:** Ops, Founder, Marketing (for OOS ad suppression).  
**Related:** [14](./14-product-performance-dashboard.md), manufacturing forecast skill (by name).

---

## Context

Primary inventory matrix: **Open Sole / Closed Sole × color × size (M/L)**. Manufacturing batches (e.g. 400–500 pair budgets) make weeks-of-cover and velocity critical.

---

## KPI set

### On-hand units

| Field | Value |
|-------|-------|
| **Definition** | Sellable units available |
| **Formula** | Sum available inventory (by variant) |
| **Data source** | Shopify Inventory |
| **Owner** | Ops |
| **Reporting cadence** | Daily |
| **Target** | Cover plan per SKU; TBD thresholds from baseline |

### Weeks of cover

| Field | Value |
|-------|-------|
| **Definition** | Inventory duration at recent sell rate |
| **Formula** | On-hand ÷ (Units sold last 28 days ÷ 4) |
| **Data source** | Shopify |
| **Owner** | Ops |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline / production lead times |

### Stockout count (critical)

| Field | Value |
|-------|-------|
| **Definition** | Hero variants at zero available |
| **Formula** | Count(variants where available = 0 AND tagged critical) |
| **Data source** | Shopify |
| **Owner** | Ops |
| **Reporting cadence** | Daily |
| **Target** | 0 on top-seller matrix |

### Sell-through %

| Field | Value |
|-------|-------|
| **Definition** | Movement of a batch or period stock |
| **Formula** | Units sold ÷ (Units sold + Ending on-hand) |
| **Data source** | Shopify |
| **Owner** | Ops |
| **Reporting cadence** | Biweekly / Monthly |
| **Target** | TBD — set from 90-day baseline |

### Inventory value (at cost)

| Field | Value |
|-------|-------|
| **Definition** | Capital tied in stock |
| **Formula** | Σ (On-hand × unit COGS) |
| **Data source** | Shopify + COGS |
| **Owner** | Founder / Ops |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Aged inventory

| Field | Value |
|-------|-------|
| **Definition** | Units with low velocity / long cover |
| **Formula** | Units where weeks of cover > threshold OR no sale in N days |
| **Data source** | Shopify |
| **Owner** | Ops / Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline; trigger merchandising or promo (brand-safe) |

---

## Alert rules

| Alert | Trigger | Action |
|-------|---------|--------|
| Hard OOS | Critical variant = 0 | Suppress ads for that variant; update size UI; reorder |
| Low cover | Weeks cover < lead time buffer | Prioritize production allocation |
| Dead stock | No sales 60d+ with stock | Marketing plan or bundle |

---

## Views

1. Heatmap: Style × Color × Size availability  
2. Velocity rank: 28-day units  
3. Cover vs production ETA  
4. Apparel vs footwear capital split  

---

## Cross-links

- Product performance → [14](./14-product-performance-dashboard.md)  
- Profitability → [12](./12-profitability-dashboard.md)  
- Executive daily → [01](./01-executive-kpi-dashboard.md)  
- Shopify guide → [07](./07-shopify-reporting-guide.md)
