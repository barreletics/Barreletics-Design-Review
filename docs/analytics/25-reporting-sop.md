# 25 — Reporting SOP

**Purpose:** Step-by-step how to produce daily, weekly, and monthly Barreletics analytics packs.  
**Audience:** Marketing operator / Founder.  
**Related:** [01](./01-executive-kpi-dashboard.md), [20](./20-monthly-executive-review-process.md), [23](./23-data-dictionary.md).

---

## General rules

1. Pull **Shopify first**, then Blend spend, then GA4, then Meta claims.  
2. Label every ROAS/CAC with revenue source.  
3. Use store timezone; state date range in the pack header.  
4. If a source is down, ship partial pack with gaps marked — do not invent.  
5. Never paste secrets (service account JSON, tokens) into packs or chat.

---

## Daily pack (≤10 minutes)

### Owner

Marketing (or Founder).

### Steps

1. **Shopify:** Net sales, orders, AOV for yesterday (and MTD optional).  
2. **Blend:** Total spend by platform yesterday.  
3. **Shopify UTMs:** Meta-paid net sales (filter per [23](./23-data-dictionary.md)).  
4. **Compute:** `roas_shopify_meta` = Meta-UTM net sales ÷ Meta spend.  
5. **GA4 (optional spot):** Sessions; Paid Social vs sitewide if sales odd.  
6. **Inventory:** Any critical OOS on Open/Closed heroes.  
7. **Flags:** Apply red flags from [01](./01-executive-kpi-dashboard.md).  
8. **Ship:** Short note to Founder (chat/email) — 5–8 lines max.

### Daily KPI checklist

| KPI | Definition | Formula | Source | Owner | Cadence | Target |
|-----|------------|---------|--------|-------|---------|--------|
| Net sales | Shopify net sales | Sum | Shopify | Founder | Daily | TBD — set from 90-day baseline |
| Orders | Paid orders | Count | Shopify | Founder | Daily | TBD — set from 90-day baseline |
| Spend | Media cost | Sum | Blend | Marketing | Daily | Budget |
| ROAS_Shopify_Meta | Decision ROAS | Meta-UTM sales ÷ Meta spend | Shopify+Blend | Marketing | Daily | TBD — set from 90-day baseline |
| Critical OOS | Hero stockouts | Count | Shopify | Ops | Daily | 0 |

---

## Weekly pack (≤30–45 minutes)

### Owner

Marketing; Ops adds inventory; CS adds refund note if spike.

### Steps

1. Complete daily metrics as **week totals**.  
2. **GA4:** Channel report — sessions, activeUsers, totalRevenue by `sessionDefaultChannelGroup`; compute rev/session vs benchmarks (Organic ~$2.21, Email ~$2.25, Paid Social ~$0.74).  
3. **Blend:** Spend by platform; CPM/CPC/frequency for Meta.  
4. **Reconcile:** Meta claimed purchases/value vs Shopify Meta-UTM; compute overclaim ratio ([04](./04-marketing-attribution-framework.md)).  
5. **Funnel:** ATC and checkout rates; Paid Social vs sitewide ([16](./16-conversion-funnel-dashboard.md)).  
6. **Shopify:** New vs returning; refund rate; top products.  
7. **Inventory:** Weeks of cover on top 10 variants.  
8. **Partnerships (light):** New wholesale/studio inquiries count.  
9. **Decisions proposed:** Scale / hold / cut — Founder approves.  
10. **Archive:** Save pack with date `YYYY-MM-DD-weekly`.

### Weekly KPI checklist (additions)

| KPI | Definition | Formula | Source | Owner | Cadence | Target |
|-----|------------|---------|--------|-------|---------|--------|
| Rev/session by channel | Channel quality | Revenue ÷ sessions | GA4 | Marketing | Weekly | Benchmarks above |
| Meta overclaim ratio | Trust gap | Meta claims ÷ Shopify Meta | Meta+Shopify | Marketing | Weekly | TBD — set from 90-day baseline |
| Blended CAC | Acquisition cost | Spend ÷ new customers | Blend+Shopify | Marketing | Weekly | TBD — set from 90-day baseline |
| MER | Efficiency | Net sales ÷ paid spend | Shopify+Blend | Founder | Weekly | TBD — set from 90-day baseline |

---

## Monthly pack

Follow [20](./20-monthly-executive-review-process.md). Build from weekly archives; add LTV/cohort slices ([08](./08-customer-cohort-framework.md), [09](./09-ltv-measurement-framework.md)), contribution ([12](./12-profitability-dashboard.md)), and north stars ([02](./02-north-star-metrics.md)).

**Due:** T−2 business days before Monthly Review.

---

## Tooling cheatsheet

| Task | Tool |
|------|------|
| Shopify orders/revenue | Admin Analytics or MCP `user-shopify-store` |
| GA4 channel/geo/page | `ga_run_report` on property `300437005` |
| Meta/Google/Pinterest spend | Blend `smart_query_*` with business context: Barreletics, fitness gear, goal=purchases/ROAS |
| Meta auction deep-dive | Meta Ads Manager / marketing skills by name |

### Daily briefing prompt (optional)

> Give me today's Barreletics marketing summary: GA4 sessions + revenue by channel, top ad spend vs revenue by platform from Blend, any ROAS flags or spend anomalies, and Shopify orders by geography.

Always re-check Shopify dollars before acting on the briefing.

---

## Quality checklist before sending

- [ ] Date range and timezone stated  
- [ ] Shopify numbers present  
- [ ] ROAS/CAC labeled by source  
- [ ] Anomalies explained or marked “investigating”  
- [ ] No dual-tracking suspicion left unmentioned if metrics look “too perfect”  
- [ ] Actions have owners  

---

## Incident SOP (sales cliff / ROAS mirage)

1. Freeze scale decisions.  
2. Shopify paid order timeline + UTM check.  
3. Compare Meta claimed vs Shopify Meta-UTM.  
4. Funnel by device/landing.  
5. Inventory / site uptime falsification.  
6. Founder decision.  
7. Log outcome for Monthly Review.

---

## Cross-links

- Executive board → [01](./01-executive-kpi-dashboard.md)  
- Governance → [24](./24-metric-governance.md)  
- Dictionary → [23](./23-data-dictionary.md)  
- Index → [README](./README.md)
