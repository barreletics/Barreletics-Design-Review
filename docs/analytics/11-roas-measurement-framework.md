# 11 — ROAS Measurement Framework

**Purpose:** Define Return on Ad Spend with explicit revenue attribution.  
**Audience:** Founder, Marketing.  
**Related:** [04](./04-marketing-attribution-framework.md), [05](./05-meta-ads-reporting-framework.md), [10](./10-cac-measurement-framework.md), [12](./12-profitability-dashboard.md).

---

## Definition

**ROAS = Attributed revenue ÷ Ad spend**

The only debate that matters is **which revenue**. Barreletics always labels ROAS with its revenue source.

---

## ROAS variants (required labels)

### Shopify-channel ROAS (decision ROAS)

| Field | Value |
|-------|-------|
| **Definition** | Revenue recorded on Shopify for a paid channel ÷ that channel’s spend |
| **Formula** | Shopify net sales (channel UTM filter) ÷ Channel spend (Blend) |
| **Data source** | Shopify + Blend |
| **Owner** | Marketing / Founder |
| **Reporting cadence** | Daily / Weekly |
| **Target** | TBD — set from 90-day baseline |

Examples: `ROAS_Shopify_Meta`, `ROAS_Shopify_Google`.

### Blended paid ROAS

| Field | Value |
|-------|-------|
| **Definition** | All Shopify paid-tagged net sales ÷ all paid spend |
| **Formula** | Σ Shopify paid-channel net sales ÷ Σ Blend paid spend |
| **Data source** | Shopify + Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Platform ROAS (diagnostic)

| Field | Value |
|-------|-------|
| **Definition** | Ad platform reported conversion value ÷ spend |
| **Formula** | Platform purchase value ÷ Spend |
| **Data source** | Meta / Google / Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Daily |
| **Target** | Not a business target |

### GA4 channel ROAS (directional)

| Field | Value |
|-------|-------|
| **Definition** | GA4 totalRevenue for Paid Social (etc.) ÷ spend |
| **Formula** | GA4 channel totalRevenue ÷ Spend |
| **Data source** | GA4 + Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | Cross-check only; Paid Social rev/session ~$0.74 informs quality |

---

## MER (Marketing Efficiency Ratio)

| Field | Value |
|-------|-------|
| **Definition** | Total new sales efficiency vs total ad spend (blended, channel-agnostic) |
| **Formula** | Shopify net sales (DTC) ÷ Total paid media spend |
| **Data source** | Shopify + Blend |
| **Owner** | Founder |
| **Reporting cadence** | Weekly / Monthly |
| **Target** | TBD — set from 90-day baseline |

MER captures halo / dark social better than last-click ROAS but hides weak channels — use **with** channel ROAS, not instead.

---

## Contribution ROAS (preferred economic view)

| Field | Value |
|-------|-------|
| **Definition** | Whether ads produce contribution, not just top-line |
| **Formula** | (Shopify attributed net sales − COGS − refunds on those orders) ÷ Spend  
*Approx if line-level COGS hard: attributed net sales × gross margin % ÷ spend* |
| **Data source** | Shopify + COGS + Blend |
| **Owner** | Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline; scale only when contribution ROAS supports goals in [12](./12-profitability-dashboard.md) |

---

## Benchmarks & guardrails

| Signal | Guidance |
|--------|----------|
| Paid Social GA4 rev/session ~$0.74 | Expect tighter Shopify ROAS scrutiny than Email/Organic |
| Meta platform ROAS ≫ Shopify Meta ROAS | Overclaim — do not scale |
| Shopify Meta ROAS healthy, MER weak | Leakage elsewhere or organic decline — investigate |
| High ROAS on tiny spend | Not a scaling plan |

---

## Reporting table (weekly)

| Channel | Spend | Shopify revenue | ROAS_Shopify | Platform ROAS | Notes |
|---------|-------|-----------------|--------------|---------------|-------|
| Meta | | | | | |
| Google | | | | | |
| Pinterest | | | | | |
| **Total paid** | | | | | MER companion |

---

## Cross-links

- Attribution → [04](./04-marketing-attribution-framework.md)  
- Meta → [05](./05-meta-ads-reporting-framework.md)  
- CAC → [10](./10-cac-measurement-framework.md)  
- Profitability → [12](./12-profitability-dashboard.md)
