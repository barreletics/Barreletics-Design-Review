# 17 — Wholesale KPI Dashboard

**Purpose:** Measure B2B / wholesale pipeline and partner health.  
**Audience:** Wholesale / Partnerships, Founder.  
**Context:** Manual wholesale via Help Scout / forms; **~50% off MSRP (INTERNAL — never publish)**; 10-pair opening minimum.  
**Related:** Operating System wholesale section (by name), Growth Engine wholesale resources (by name), [12](./12-profitability-dashboard.md).

---

## Principles

1. Keep wholesale **out of DTC MER/ROAS** unless explicitly segmented.  
2. Pipeline may live in Help Scout + spreadsheet until CRM exists — still report.  
3. Never expose wholesale discount publicly in marketing analytics packs.

---

## Pipeline KPIs

### Wholesale inquiries

| Field | Value |
|-------|-------|
| **Definition** | New wholesale form / email inquiries |
| **Formula** | Count new inquiries in period |
| **Data source** | Help Scout / form |
| **Owner** | Wholesale |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Qualified opportunities

| Field | Value |
|-------|-------|
| **Definition** | Inquiries meeting studio/retail fit criteria |
| **Formula** | Count qualified |
| **Data source** | Tracker |
| **Owner** | Wholesale |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Win rate

| Field | Value |
|-------|-------|
| **Definition** | Closed-won ÷ qualified |
| **Formula** | Closed-won ÷ Qualified opportunities |
| **Data source** | Tracker |
| **Owner** | Wholesale |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Time to first order

| Field | Value |
|-------|-------|
| **Definition** | Speed of onboarding |
| **Formula** | Median(days from inquiry to first wholesale order) |
| **Data source** | Tracker + Shopify |
| **Owner** | Wholesale |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Revenue KPIs

### Wholesale net sales

| Field | Value |
|-------|-------|
| **Definition** | B2B revenue (tagged wholesale) |
| **Formula** | Sum net sales on wholesale-tagged orders |
| **Data source** | Shopify (tags/channels) |
| **Owner** | Founder / Wholesale |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Average wholesale order value

| Field | Value |
|-------|-------|
| **Definition** | Typical opening / reorder size |
| **Formula** | Wholesale net sales ÷ Wholesale orders |
| **Data source** | Shopify |
| **Owner** | Wholesale |
| **Reporting cadence** | Monthly |
| **Target** | Respect 10-pair minimum; TBD $ target |

### Wholesale gross profit

| Field | Value |
|-------|-------|
| **Definition** | Margin after COGS at wholesale price |
| **Formula** | Wholesale net sales − COGS |
| **Data source** | Shopify + COGS |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Active wholesale accounts

| Field | Value |
|-------|-------|
| **Definition** | Accounts with order in trailing 180 days |
| **Formula** | Count distinct wholesale customers T180 |
| **Data source** | Shopify |
| **Owner** | Wholesale |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

### Reorder rate

| Field | Value |
|-------|-------|
| **Definition** | Share of accounts placing a second order within 180 days |
| **Formula** | Accounts with ≥2 wholesale orders in window ÷ Accounts with ≥1 |
| **Data source** | Shopify |
| **Owner** | Wholesale |
| **Reporting cadence** | Quarterly |
| **Target** | TBD — set from 90-day baseline |

---

## Operational KPIs

| KPI | Definition | Formula | Source | Owner | Cadence | Target |
|-----|------------|---------|--------|-------|---------|--------|
| Quote → order conversion | Quotes that become orders | Orders ÷ Quotes sent | Tracker | Wholesale | Monthly | TBD — set from 90-day baseline |
| Fulfillment SLA hit rate | On-time wholesale ship | On-time ÷ Wholesale orders | Ops | Ops | Monthly | TBD — set from 90-day baseline |

---

## Cross-links

- Studio (often related but separate) → [19](./19-studio-kpi-dashboard.md)  
- Profitability → [12](./12-profitability-dashboard.md)  
- Do not mix into Meta ROAS → [11](./11-roas-measurement-framework.md)
