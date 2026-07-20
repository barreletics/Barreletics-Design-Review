# 12 — Profitability Dashboard

**Purpose:** Unit economics and contribution views for executive decisions.  
**Audience:** Founder (primary), Marketing.  
**Related:** [09](./09-ltv-measurement-framework.md), [10](./10-cac-measurement-framework.md), [11](./11-roas-measurement-framework.md), [02](./02-north-star-metrics.md).

---

## Scope

This is **not** a full audited P&L. It is a management contribution model for DTC (+ optional wholesale margin later).

---

## KPI set

### Gross profit (product)

| Field | Value |
|-------|-------|
| **Definition** | Sales after product cost |
| **Formula** | Net sales − COGS |
| **Data source** | Shopify + COGS sheet / landed cost |
| **Owner** | Founder / Ops |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Gross margin %

| Field | Value |
|-------|-------|
| **Definition** | Product margin rate |
| **Formula** | Gross profit ÷ Net sales |
| **Data source** | Same |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Contribution after ads

| Field | Value |
|-------|-------|
| **Definition** | Gross profit left after paid media (proxy commercial north star) |
| **Formula** | Gross profit − Refunds − Paid media spend  
*(Optionally also − shipping + payment fees when tracked)* |
| **Data source** | Shopify + COGS + Blend |
| **Owner** | Founder |
| **Reporting cadence** | Weekly (proxy) / Monthly |
| **Target** | TBD — set from 90-day baseline; rolling 4-week positive except planned invest windows |

### Contribution margin %

| Field | Value |
|-------|-------|
| **Definition** | Contribution after ads as % of net sales |
| **Formula** | Contribution after ads ÷ Net sales |
| **Data source** | Same |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Profit per order

| Field | Value |
|-------|-------|
| **Definition** | Average contribution per paid order |
| **Formula** | Contribution after ads ÷ Orders |
| **Data source** | Same |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Break-even ROAS

| Field | Value |
|-------|-------|
| **Definition** | ROAS needed for ads to break even on contribution |
| **Formula** | 1 ÷ Gross margin % *(adjust if variable shipping/fees included)* |
| **Data source** | COGS model |
| **Owner** | Founder |
| **Reporting cadence** | Quarterly or when COGS/pricing changes |
| **Target** | Reference line for [11](./11-roas-measurement-framework.md) |

---

## Product-level economics (grippy shoes)

| Cut | Why |
|-----|-----|
| Open Sole vs Closed Sole | Mix shift |
| Colorways | Sell-through + discounting |
| Apparel vs footwear | Margin mix |
| Discounted vs full price | Promo efficiency (`SAVE15`, newsletter 10%) |

### KPI: Promo dilution

| Field | Value |
|-------|-------|
| **Definition** | Margin lost to discounts |
| **Formula** | Discount amount ÷ Gross sales |
| **Data source** | Shopify |
| **Owner** | Marketing / Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Wholesale note

Wholesale is ~50% off MSRP (**internal**). Track wholesale contribution separately — do not blend into DTC MER without labeling ([17](./17-wholesale-kpi-dashboard.md)).

---

## Dashboard layout (future)

```
Net sales → COGS → Gross profit → Refunds → Ad spend → Contribution
                 ↘ Margin %              ↘ Break-even ROAS
Channel ROAS vs break-even | LTV:CAC | Inventory aged stock risk
```

---

## Cross-links

- North star → [02](./02-north-star-metrics.md)  
- LTV / CAC / ROAS → [09](./09-ltv-measurement-framework.md)–[11](./11-roas-measurement-framework.md)  
- Inventory cash → [13](./13-inventory-dashboard.md)  
- Monthly review → [20](./20-monthly-executive-review-process.md)
