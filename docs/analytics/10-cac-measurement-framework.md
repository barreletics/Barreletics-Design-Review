# 10 — CAC Measurement Framework

**Purpose:** Define Customer Acquisition Cost with explicit spend and customer counts.  
**Audience:** Founder, Marketing.  
**Related:** [09](./09-ltv-measurement-framework.md), [11](./11-roas-measurement-framework.md), [04](./04-marketing-attribution-framework.md).

---

## Definition doctrine

**CAC = acquisition spend ÷ new customers acquired**, with both sides defined and labeled.

Never mix Meta-claimed purchasers in the denominator with Blend spend in the numerator without calling it **platform CPA** (not CAC).

---

## CAC variants

### Blended CAC (primary)

| Field | Value |
|-------|-------|
| **Definition** | Cost to acquire a new DTC customer across paid channels (optionally + measurable variable acquisition costs) |
| **Formula** | Paid media spend (Blend: Meta + Google + Pinterest + other active) ÷ New customers (Shopify first orders in period)  
*Optional v2:* (Paid media + measurable affiliate/ambassador commissions) ÷ New customers |
| **Data source** | Blend + Shopify |
| **Owner** | Marketing / Founder |
| **Reporting cadence** | Weekly / Monthly |
| **Target** | TBD — set from 90-day baseline; must be judged vs Contribution LTV ([09](./09-ltv-measurement-framework.md)) |

### Channel CAC (e.g. Meta CAC)

| Field | Value |
|-------|-------|
| **Definition** | Cost to acquire new customers attributed to a channel on Shopify |
| **Formula** | Channel spend ÷ New customers with first order attributed to that channel (Shopify UTMs) |
| **Data source** | Blend + Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Platform CPA (diagnostic — not CAC)

| Field | Value |
|-------|-------|
| **Definition** | Ad platform’s cost per claimed purchase |
| **Formula** | Spend ÷ Platform-reported purchases |
| **Data source** | Meta / Google / Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Daily |
| **Target** | Diagnostic only |

---

## Who counts as a “new customer”

| Include | Exclude |
|---------|---------|
| First paid Shopify order in period | Returning customers |
| Kept orders (not fully refunded within X days — define X operationally, default 14d) | Test orders |
| DTC storefront | Wholesale accounts |
| | Pure gift/comp with $0 |

### KPI: New customers

| Field | Value |
|-------|-------|
| **Definition** | Count of customers with first paid order in period meeting inclusion rules |
| **Formula** | Count(distinct customer_id where first_order_date in period AND inclusion) |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Daily / Weekly |
| **Target** | TBD — set from 90-day baseline |

---

## Spend scope

| In blended CAC spend | Out (unless Founder adds) |
|----------------------|---------------------------|
| Meta, Google Ads, Pinterest, Microsoft as active | Creative production retainers (track separately as opex) |
| | Salaries |
| | Shopify / tools SaaS |
| | Brand PR retainers (optional later) |

Document any expansion of spend scope in [24](./24-metric-governance.md).

---

## Payback

### KPI: CAC payback (months)

| Field | Value |
|-------|-------|
| **Definition** | Months of contribution to recover CAC |
| **Formula** | Blended CAC ÷ (Contribution profit per customer per month)  
*Simple proxy:* CAC ÷ (Contribution LTV_90d / 3) for quarterly feel — label proxy |
| **Data source** | Shopify + COGS + Blend |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Decision rules

| Signal | Action |
|--------|--------|
| Meta CAC ↑ but LTV_180d Meta cohort healthy | Tolerable if contribution positive |
| Meta CAC ↑ and Shopify Meta ROAS ↓ | Cut or restructure creatives/landings |
| Blended CAC ↓ only because Organic filled denominator | Do not celebrate paid efficiency |
| Platform CPA ≪ Shopify Meta CAC | Attribution overclaim — trust Shopify |

---

## Cross-links

- LTV → [09](./09-ltv-measurement-framework.md)  
- ROAS → [11](./11-roas-measurement-framework.md)  
- Profitability → [12](./12-profitability-dashboard.md)  
- Attribution → [04](./04-marketing-attribution-framework.md)
