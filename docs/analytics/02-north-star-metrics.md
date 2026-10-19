# 02 — North Star Metrics

**Purpose:** Define the few metrics that indicate Barreletics is winning category creation *and* a healthy commerce engine.  
**Audience:** Founder / Owner; Marketing; SEO.  
**Depends on:** Brand North Star (`planning/01-brand-north-star.md`), Category Creation Strategy.  
**Related:** [01](./01-executive-kpi-dashboard.md), [06](./06-ga4-measurement-plan.md), SEO Platform (by name).

---

## Two-layer north star model

Barreletics has a **brand north star** (category creation) and a **commercial north star** (profitable DTC growth). Neither replaces the other.

| Layer | Question it answers | Primary metric |
|-------|---------------------|----------------|
| Brand | Are we making grip socks irrelevant? | Branded search + category-language shift |
| Commercial | Are we growing profitable demand? | Contribution profit after ads (proxy until full P&L) |

---

## Brand north star

### KPI: Branded search demand

| Field | Value |
|-------|-------|
| **Definition** | Search interest in “Barreletics” (and close variants) vs generic grip-sock queries |
| **Formula** | Branded search volume (Search Console clicks/impressions for brand queries) ÷ relevant category queries; track absolute branded clicks MoM |
| **Data source** | Google Search Console; optional keyword tools for category terms |
| **Owner** | Marketing / SEO |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline; directional goal: branded clicks ↑ and share of “grip sock alternative / performance skin” language ↑ |

### KPI: Category language shift (qualitative + content)

| Field | Value |
|-------|-------|
| **Definition** | Market talk moves from “best grip socks” → “grip sock alternatives” → “performance skins” / Barreletics |
| **Formula** | Scorecard: (1) % of Journal/SEO titles using category-creation framing, (2) share of support tickets mentioning socks vs Performance Skins, (3) ad creative primary message class |
| **Data source** | Content inventory; Help Scout tags; Meta creative audit |
| **Owner** | Founder (strategy); Marketing (execution) |
| **Reporting cadence** | Quarterly |
| **Target** | Qualitative gate in QBR ([21](./21-quarterly-business-review-framework.md)); no fake precision |

### KPI: Studio density signal

| Field | Value |
|-------|-------|
| **Definition** | Active studio / instructor relationships as proof of studio-first category presence |
| **Formula** | Count of active studio partners + qualified pipeline |
| **Data source** | Wholesale/Studio tracker (Help Scout / sheet) — see [19](./19-studio-kpi-dashboard.md) |
| **Owner** | Wholesale / Partnerships |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline |

---

## Commercial north star

### KPI: Contribution after ads (proxy)

| Field | Value |
|-------|-------|
| **Definition** | Money left after product COGS and paid media to fund ops, brand, and growth |
| **Formula** | Shopify net sales − COGS − refunds − paid media spend  
*(Full contribution margin in [12](./12-profitability-dashboard.md); use this proxy until shipping/payment fees are automated)* |
| **Data source** | Shopify + COGS sheet + Blend spend |
| **Owner** | Founder |
| **Reporting cadence** | Weekly (proxy) / Monthly (full) |
| **Target** | TBD — set from 90-day baseline; must stay positive on a rolling 4-week basis except planned launch invest periods |

### KPI: New customers acquired (net of refunds)

| Field | Value |
|-------|-------|
| **Definition** | First-time buyers who keep the order |
| **Formula** | Count of customers with first paid order in period − customers whose first order fully refunded |
| **Data source** | Shopify Customers / Orders |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Supporting commercial metric: LTV:CAC

| Field | Value |
|-------|-------|
| **Definition** | Whether acquisition payback is healthy |
| **Formula** | Blended LTV ÷ Blended CAC — see [09](./09-ltv-measurement-framework.md), [10](./10-cac-measurement-framework.md) |
| **Data source** | Shopify + Blend |
| **Owner** | Founder / Marketing |
| **Reporting cadence** | Monthly |
| **Target** | TBD — set from 90-day baseline; common DTC heuristic ≥3:1 is a *discussion* threshold, not a Barreletics lock until baseline exists |

---

## What is *not* a north star

- Meta ROAS alone  
- Instagram followers / likes  
- GA4 revenue without Shopify reconciliation  
- Session volume without channel quality  
- “Best grip sock” keyword ranking as a vanity win (category creation rejects sock-category imprisonment)

---

## Monthly north star readout (template)

1. Branded Search Console trend (up / flat / down)  
2. Contribution after ads (4-week)  
3. New customers + repeat purchase rate  
4. One category-creation evidence note (creative, Journal, wholesale conversation)  
5. Decision: invest / hold / cut paid — using Shopify-attributed economics

---

## Cross-links

- Executive board → [01](./01-executive-kpi-dashboard.md)  
- LTV / CAC → [09](./09-ltv-measurement-framework.md), [10](./10-cac-measurement-framework.md)  
- SEO measurement → [06](./06-ga4-measurement-plan.md) + SEO Platform docs (by name)  
- Brand strategy → `planning/01-brand-north-star.md`
