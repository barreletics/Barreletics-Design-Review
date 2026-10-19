# 03 — Ecommerce KPI Definitions

**Purpose:** Canonical definitions for DTC commerce metrics.  
**Audience:** Founder, Marketing, Ops, CS.  
**Source of truth:** Shopify Admin unless noted.  
**Related:** [01](./01-executive-kpi-dashboard.md), [07](./07-shopify-reporting-guide.md), [16](./16-conversion-funnel-dashboard.md).

---

## Conventions

- **Store timezone:** Use Shopify store timezone for all day boundaries.  
- **Currency:** USD.  
- **Product context:** Primary SKUs are Open Sole / Closed Sole Grippy Shoes (~$74) + apparel; sizes M/L.  
- **Promo awareness:** Buy 2 Save 15% (`SAVE15`); newsletter 10%; free shipping over **$150** (ADR-02) — affects AOV and conversion.

---

## Core sales KPIs

### Net sales

| Field | Value |
|-------|-------|
| **Definition** | Revenue after discounts and returns adjustments as Shopify defines Net sales |
| **Formula** | Per Shopify Analytics “Net sales” (do not invent alternate discount handling) |
| **Data source** | Shopify |
| **Owner** | Founder |
| **Reporting cadence** | Daily / Weekly / Monthly |
| **Target** | TBD — set from 90-day baseline |

### Gross sales

| Field | Value |
|-------|-------|
| **Definition** | Pre-discount product sales |
| **Formula** | Shopify Gross sales |
| **Data source** | Shopify |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | Contextual only |

### Orders (paid)

| Field | Value |
|-------|-------|
| **Definition** | Count of paid orders (exclude cancelled/test if filtered) |
| **Formula** | Count(paid orders) |
| **Data source** | Shopify |
| **Owner** | Ops / Founder |
| **Reporting cadence** | Daily |
| **Target** | TBD — set from 90-day baseline |

### Average order value (AOV)

| Field | Value |
|-------|-------|
| **Definition** | Average net value per paid order |
| **Formula** | Net sales ÷ Orders |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Daily / Weekly |
| **Target** | TBD — set from 90-day baseline; watch free-shipping threshold ($150) pull-through |

### Units per order (UPO)

| Field | Value |
|-------|-------|
| **Definition** | Average units sold per order |
| **Formula** | Units sold ÷ Orders |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline; multi-pair / Open+Closed attach is strategic |

### Conversion rate (site)

| Field | Value |
|-------|-------|
| **Definition** | Share of sessions that purchase |
| **Formula** | Orders ÷ Sessions *(label source: Shopify sessions vs GA4 sessions — pick one per report; prefer Shopify for site CVR when available)* |
| **Data source** | Shopify Analytics and/or GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

---

## Funnel KPIs (summary — detail in 16)

### Add-to-cart rate

| Field | Value |
|-------|-------|
| **Definition** | Sessions with ATC ÷ sessions |
| **Formula** | Sessions with `add_to_cart` ÷ Sessions |
| **Data source** | GA4 (primary for funnel stages); Shopify for purchase |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Checkout rate

| Field | Value |
|-------|-------|
| **Definition** | Begin checkout ÷ sessions (or ÷ ATC sessions — label which) |
| **Formula** | `begin_checkout` ÷ Sessions *(or ÷ ATC)* |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Purchase rate from checkout

| Field | Value |
|-------|-------|
| **Definition** | Purchases ÷ begin_checkout |
| **Formula** | Purchases ÷ `begin_checkout` |
| **Data source** | GA4 + Shopify purchase truth |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

---

## Customer KPIs

### New customer rate

| Field | Value |
|-------|-------|
| **Definition** | Share of orders from first-time buyers |
| **Formula** | New customer orders ÷ Total orders |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Repeat purchase rate (period)

| Field | Value |
|-------|-------|
| **Definition** | Customers with ≥2 orders ÷ customers acquired in cohort window — see [08](./08-customer-cohort-framework.md) |
| **Formula** | Per cohort framework |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Customer count (active)

| Field | Value |
|-------|-------|
| **Definition** | Customers with ≥1 paid order in trailing 12 months |
| **Formula** | Distinct customers, T12M |
| **Data source** | Shopify |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Merchandising KPIs

### Sell-through (period)

| Field | Value |
|-------|-------|
| **Definition** | Units sold ÷ (units sold + ending inventory) for a style/size/color |
| **Formula** | Units sold ÷ (Units sold + Ending on-hand) |
| **Data source** | Shopify Inventory + sales |
| **Owner** | Ops |
| **Reporting cadence** | Monthly / biweekly manufacturing |
| **Target** | TBD — set from 90-day baseline |

### Attach rate (second pair / apparel)

| Field | Value |
|-------|-------|
| **Definition** | Orders containing ≥2 grippy pairs or shoe+apparel ÷ total shoe orders |
| **Formula** | Multi-category or multi-pair orders ÷ shoe orders |
| **Data source** | Shopify line items |
| **Owner** | Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Service & quality KPIs

### Refund rate

| Field | Value |
|-------|-------|
| **Definition** | Refund pressure on sales |
| **Formula** | Refunded amount ÷ Net sales *(or units refunded ÷ units sold)* |
| **Data source** | Shopify |
| **Owner** | CS |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Exchange / size issue rate

| Field | Value |
|-------|-------|
| **Definition** | Fit friction (M/L only; snug colors: Dark Grey, Hot Coral, Blue) |
| **Formula** | Size-related tickets or exchanges ÷ orders |
| **Data source** | Help Scout tags + Shopify |
| **Owner** | CS |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Explicitly out of scope here

Wholesale, ambassador, and studio economics → [17](./17-wholesale-kpi-dashboard.md)–[19](./19-studio-kpi-dashboard.md).  
Paid efficiency → [10](./10-cac-measurement-framework.md), [11](./11-roas-measurement-framework.md).
