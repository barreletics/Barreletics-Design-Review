# 07 — Shopify Reporting Guide

**Purpose:** How to use Shopify Admin as the system of record for commerce.  
**Audience:** Founder, Marketing, Ops, CS.  
**Related:** [03](./03-ecommerce-kpi-definitions.md), [04](./04-marketing-attribution-framework.md), [13](./13-inventory-dashboard.md).

---

## Truth statement

**Shopify dollars are ground truth.** When diagnosing sales cliffs, Meta “purchases,” or GA4 revenue, start from Shopify paid orders and work outward.

---

## Primary reports & pulls

| Need | Where in Shopify | Notes |
|------|------------------|-------|
| Net sales, orders, AOV | Analytics → Reports / Overview | Store timezone |
| Sales by channel / referrer | Acquisition / sales by referring channel or UTM exports | Paid reconciliation |
| Product / variant sales | Sales by product / variant | Style, color, size |
| Inventory | Products → Inventory | Sellable qty |
| Customers new vs returning | Customers / acquisition reports | Cohort inputs |
| Discounts | Sales by discount | `SAVE15`, newsletter codes |
| Refunds | Finances / returns reports | Quality signal |
| Abandoned checkouts | Orders → Abandoned checkouts | Gateway=null patterns in diagnostics |

MCP / API tools may also pull orders (`user-shopify-store` / Admin GraphQL) for custom analyses — same definitions apply.

---

## Core Shopify KPIs (pointer)

Full formulas in [03](./03-ecommerce-kpi-definitions.md). Minimum executive set:

| KPI | Definition | Formula | Data source | Owner | Cadence | Target |
|-----|------------|---------|-------------|-------|---------|--------|
| Net sales | Shopify net sales | Per Shopify | Shopify | Founder | Daily | TBD — set from 90-day baseline |
| Orders | Paid orders | Count | Shopify | Founder | Daily | TBD — set from 90-day baseline |
| AOV | Avg order value | Net sales ÷ Orders | Shopify | Marketing | Daily | TBD — set from 90-day baseline |
| Units sold | Units | Sum line quantities | Shopify | Ops | Weekly | TBD — set from 90-day baseline |
| Discount rate | Discount depth | Discounts ÷ Gross sales | Shopify | Marketing | Weekly | TBD — set from 90-day baseline |
| Refund rate | Refund pressure | Refunds ÷ Net sales | Shopify | CS | Weekly | TBD — set from 90-day baseline |

---

## UTM / paid channel reporting

### KPI: Meta-UTM net sales

| Field | Value |
|-------|-------|
| **Definition** | Net sales on orders tagged with Meta/Facebook/Instagram paid UTMs |
| **Formula** | Sum net sales where utm_source ∈ {facebook, instagram, meta, fb, ig} AND medium indicates paid *(maintain exact filter list in Data Dictionary)* |
| **Data source** | Shopify order UTM fields |
| **Owner** | Marketing |
| **Reporting cadence** | Daily / Weekly |
| **Target** | Used in Shopify Meta ROAS ([11](./11-roas-measurement-framework.md)) |

Maintain filter aliases in [23](./23-data-dictionary.md).

---

## Order hygiene for analytics

| Rule | Why |
|------|-----|
| Exclude test orders from packs | Avoid fake revenue |
| Tag wholesale orders | Keep DTC metrics clean ([17](./17-wholesale-kpi-dashboard.md)) |
| Note manual draft orders | Founder comps / replacements |
| Preserve UTMs at checkout | Attribution integrity |
| Document gateway=null abandons when debugging | Checkout myth falsification |

---

## Inventory reporting

See [13](./13-inventory-dashboard.md). Shopify Inventory is source for on-hand and availability used in ad suppression and manufacturing forecasts.

### KPI: Weeks of cover (variant)

| Field | Value |
|-------|-------|
| **Definition** | How long stock lasts at recent velocity |
| **Formula** | On-hand ÷ (Units sold in last 28 days ÷ 4) |
| **Data source** | Shopify |
| **Owner** | Ops |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline / manufacturing calendar |

---

## Customer reporting

| Report | Use |
|--------|-----|
| First-time vs returning | Acquisition mix |
| Customers by location | GEO qualification input |
| RFM-style exports (custom) | LTV / cohorts ([08](./08-customer-cohort-framework.md), [09](./09-ltv-measurement-framework.md)) |

---

## Daily Shopify checklist

1. Net sales & orders vs yesterday / 7-day avg  
2. Top products sold  
3. Any spike in refunds or cancels  
4. Critical OOS variants  
5. Export or note Meta-UTM sales if paid was heavy  

---

## Cross-links

- Ecommerce definitions → [03](./03-ecommerce-kpi-definitions.md)  
- Attribution filters → [04](./04-marketing-attribution-framework.md)  
- Inventory → [13](./13-inventory-dashboard.md)  
- Product performance → [14](./14-product-performance-dashboard.md)  
- Reporting SOP → [25](./25-reporting-sop.md)
