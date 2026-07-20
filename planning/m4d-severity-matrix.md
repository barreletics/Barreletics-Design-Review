# M4D — Production Issue Severity Matrix

**Purpose:** Classify production issues by severity to determine response time, notification protocol, and escalation path.

---

## Severity Levels

| Severity | Definition | Response Time | Owner Notification | Examples |
|----------|-----------|---------------|-------------------|----------|
| **P0 — Critical** | Site down, checkout broken, data loss risk | Immediate — rollback if not fixable in 5 min | Immediate call/text | 500 errors on all pages, payment processing failure, homepage completely blank, checkout unreachable, security breach |
| **P1 — High** | Major feature broken, revenue directly impacted | Within 1 hour | Within 30 minutes (call/text) | Cart not adding items, variant selection broken, pricing displaying incorrectly, mobile site completely unusable, all forms broken |
| **P2 — Medium** | Feature degraded, workaround exists | Within 4 hours | Within 2 hours (message) | One collection page broken, search not returning results, one form not submitting, reviews section not loading, one redirect broken |
| **P3 — Low** | Cosmetic issue, minor UX impact | Within 24 hours | Daily summary | Spacing slightly off on one page, animation glitch, minor typo, hover state missing on one element, icon alignment |
| **P4 — Enhancement** | Improvement opportunity, not a defect | Next sprint / backlog | Weekly review | Performance optimization opportunity, UX refinement idea, accessibility improvement beyond AA compliance |

---

## Escalation Paths

### P0 — Critical

```
Builder detects issue
    → Attempt fix (5-minute window max)
    → If not fixable: ROLLBACK immediately (per m4d-rollback-procedure.md)
    → Call/text Owner immediately
    → Document: what happened, when, customer impact estimate
    → Begin root cause analysis within 1 hour
```

### P1 — High

```
Builder or Owner detects issue
    → Builder investigates (30-minute window)
    → Notify Owner within 30 minutes with status
    → Determine: fix forward or rollback?
        → Fix available and testable: deploy fix, verify
        → Fix unclear or risky: discuss rollback with Owner
    → Document issue and resolution
```

### P2 — Medium

```
Builder or Owner detects issue
    → Builder investigates within 4 hours
    → Notify Owner within 2 hours
    → Fix forward (rollback not warranted for P2)
    → Document for post-stabilization review
```

### P3 — Low

```
Anyone detects issue
    → Log in issues list
    → Include in daily summary to Owner
    → Fix during next available work session
    → No immediate action required
```

### P4 — Enhancement

```
Anyone identifies opportunity
    → Add to post-stabilization backlog
    → Review during weekly sync
    → Prioritize against other backlog items
```

---

## Decision Guide: "Is This a Rollback?"

| Question | If YES | If NO |
|----------|--------|-------|
| Can customers complete a purchase? | Continue | → P0 Rollback |
| Does the homepage load? | Continue | → P0 Rollback |
| Does navigation work? | Continue | → P0 Rollback |
| Do product pages load? | Continue | → P0 Rollback |
| Is pricing correct? | Continue | → P1 (rollback if widespread) |
| Does mobile work at all? | Continue | → P1 (assess rollback) |
| Is it just one page or feature? | → P2 fix forward | Assess breadth |
| Is it cosmetic only? | → P3 log it | Assess functional impact |

---

## Issue Log Template

When logging any production issue:

```
Issue ID: P[severity]-[number] (e.g., P2-001)
Reported by: [Owner / Builder / Customer]
Reported at: [date/time]
Severity: [P0-P4]
Description: [What's wrong]
Pages affected: [URLs]
Steps to reproduce: [1, 2, 3]
Customer impact: [None / Low / Medium / High]
Screenshot/evidence: [link or inline]
Status: [Investigating / Fix deployed / Resolved / Won't fix]
Resolution: [What was done]
Resolved at: [date/time]
```

---

## Contact Information

Fill in before launch:

| Role | Name | Phone | Email | Availability |
|------|------|-------|-------|-------------|
| Owner | | | | |
| Builder | | | | |
| Shopify Support | — | — | support@shopify.com | 24/7 |
