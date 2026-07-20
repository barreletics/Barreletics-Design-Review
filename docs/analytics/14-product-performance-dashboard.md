# 14 — Product Performance Dashboard

**Purpose:** SKU / style / color performance for merchandising and production.  
**Audience:** Founder, Ops, Marketing.  
**Related:** [13](./13-inventory-dashboard.md), [15](./15-collection-performance-dashboard.md), [03](./03-ecommerce-kpi-definitions.md).

---

## Hierarchy

1. **Product type** — Open Sole Grippy Shoes, Closed Sole, Outdoor context, Apparel  
2. **Colorway**  
3. **Size** — M / L (note snugger: Dark Grey, Hot Coral, Blue)  
4. **Variant SKU**

---

## KPI set

### Units sold

| Field | Value |
|-------|-------|
| **Definition** | Units sold in period by product cut |
| **Formula** | Sum line item quantities |
| **Data source** | Shopify |
| **Owner** | Ops / Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Net sales by product

| Field | Value |
|-------|-------|
| **Definition** | Revenue contribution |
| **Formula** | Sum net sales by product/variant |
| **Data source** | Shopify |
| **Owner** | Founder |
| **Reporting cadence** | Weekly |
| **Target** | Mix goals TBD |

### Product conversion (PDP)

| Field | Value |
|-------|-------|
| **Definition** | Purchase rate from PDP views |
| **Formula** | Purchases of product ÷ `view_item` for product *(GA4)* or Shopify product conversion if used |
| **Data source** | GA4 + Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Return rate by product

| Field | Value |
|-------|-------|
| **Definition** | Quality/fit issues by SKU |
| **Formula** | Returned units ÷ Sold units (or refund $ ÷ sales $) |
| **Data source** | Shopify + CS tags |
| **Owner** | CS / Ops |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline; watch snug colors |

### Attach / cross-sell

| Field | Value |
|-------|-------|
| **Definition** | Co-purchase of Open+Closed or shoe+apparel |
| **Formula** | See [08](./08-customer-cohort-framework.md) attach KPIs |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Velocity (units / day)

| Field | Value |
|-------|-------|
| **Definition** | Sell rate for production planning |
| **Formula** | Units sold ÷ Days in period |
| **Data source** | Shopify |
| **Owner** | Ops |
| **Reporting cadence** | Weekly / biweekly |
| **Target** | Inputs to manufacturing allocation |

---

## Ranking views

| View | Sort by | Action |
|------|---------|--------|
| Heroes | Net sales | Protect inventory + creative |
| Rising | WoW velocity | Ensure stock |
| Laggards | Low sales + high stock | Creative or sunset path |
| High return | Return rate | Fit messaging / QC |

---

## Category Creation note

Product pages and creatives should frame Performance Skins vs grip socks — measure creative class in Meta ([05](./05-meta-ads-reporting-framework.md)), not only SKU velocity.

---

## Cross-links

- Inventory → [13](./13-inventory-dashboard.md)  
- Collections → [15](./15-collection-performance-dashboard.md)  
- Funnel → [16](./16-conversion-funnel-dashboard.md)
