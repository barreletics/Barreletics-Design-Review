# 24 — Metric Governance

**Purpose:** Who owns definitions, how targets change, and how disputes resolve.  
**Audience:** Founder, Marketing, Ops.  
**Related:** [23](./23-data-dictionary.md), `planning/DECISION_FRAMEWORK.md`.

---

## Governance principles

1. **One definition per metric name** — if two formulas exist, rename one.  
2. **Shopify wins revenue disputes** unless Founder documents an exception.  
3. **No silent target changes** — log date, old value, new value, reason.  
4. **TBD is valid** — better than fake precision; promote after 90-day baseline.  
5. **Docs before dashboards** — change this library before changing a future BI tile.

---

## Ownership matrix

| Domain | Definition owner | Data steward | Approver for changes |
|--------|------------------|--------------|----------------------|
| Revenue, orders, AOV | Founder | Ops / Marketing | Founder |
| Paid spend, ROAS, CAC | Marketing | Marketing | Founder |
| GA4 events / channels | Marketing | Marketing | Founder |
| Inventory / cover | Ops | Ops | Founder |
| LTV / cohorts | Marketing | Marketing | Founder |
| Wholesale / studio | Partnerships | Partnerships | Founder |
| Ambassador | Marketing | Marketing | Founder |
| Brand north star | Founder | Marketing / SEO | Founder |

---

## KPI change control

### When Builder/Marketing may proceed without Founder

- Fixing a broken filter to match an **already approved** definition  
- Adding a new *cut* (e.g. same ROAS by campaign) without renaming  
- Correcting a typo in docs

### When Founder approval is required

- Changing formula (e.g. CAC spend scope)  
- Changing attribution truth hierarchy  
- Setting or changing numeric targets  
- Adding platform-claimed metrics to executive scoreboard  
- Blending wholesale into DTC MER

Log strategic metric decisions similarly to `planning/10-decision-log.md` (Decision ID optional: `M-###`).

---

## Target lifecycle

| Stage | Meaning |
|-------|---------|
| `TBD — set from 90-day baseline` | Collect; do not manage to fiction |
| `Baseline proposed` | 90 days observed; proposed number in Monthly Review |
| `Locked` | Founder approved; used in packs |
| `Revised` | QBR/Annual change with log entry |

### KPI: Definition compliance rate

| Field | Value |
|-------|-------|
| **Definition** | Share of executive pack metrics that cite this library |
| **Formula** | Metrics with doc link ÷ Metrics in pack |
| **Data source** | Pack audit |
| **Owner** | Marketing |
| **Reporting cadence** | Quarterly |
| **Target** | 100% for executive pack |

---

## Dispute resolution

```
Reporter flags conflict → Marketing gathers Shopify vs other sources
→ Compare to docs 03/04/11 → If still unclear, Founder decides
→ Update Data Dictionary + relevant framework doc same day
```

---

## Dual-tracking prohibition

Never enable Shopify native GA4/Meta **and** theme pixels simultaneously ([`docs/15-analytics-architecture.md`](../15-analytics-architecture.md)). Governance treats dual-tracking as a **P0 data quality incident**.

---

## Review cadence

| Review | Cadence | Owner |
|--------|---------|-------|
| Dictionary hygiene | Monthly | Marketing |
| Target promotion TBD→Locked | Monthly / QBR | Founder |
| Full governance audit | Annual | Founder |

---

## Cross-links

- Dictionary → [23](./23-data-dictionary.md)  
- Reporting SOP → [25](./25-reporting-sop.md)  
- Decision framework → `planning/DECISION_FRAMEWORK.md`
