# M4D — Launch Decision Tree

**Purpose:** Visual decision flowchart for go/rollback determinations at each launch checkpoint. Follow top-to-bottom after theme publish.

---

## Post-Publish Decision Flow

```
THEME PUBLISHED
    │
    ├── Homepage loads?
    │   ├── YES → Continue ▼
    │   └── NO → ██ ROLLBACK IMMEDIATELY (P0) ██
    │
    ├── Navigation works?
    │   ├── YES → Continue ▼
    │   └── NO → ██ ROLLBACK (P0) ██
    │
    ├── PDP loads with product data?
    │   ├── YES → Continue ▼
    │   └── NO → ██ ROLLBACK (P0) ██
    │
    ├── Add to Cart works?
    │   ├── YES → Continue ▼
    │   └── NO → ██ ROLLBACK (P0) ██
    │
    ├── Checkout reachable?
    │   ├── YES → Continue ▼
    │   └── NO → ██ ROLLBACK (P0) ██
    │
    ├── Mobile loads correctly?
    │   ├── YES → Continue ▼
    │   └── NO → Assess severity ▼
    │       ├── Completely unusable (can't navigate/buy) → ██ ROLLBACK (P1) ██
    │       └── Degraded but functional → LOG (P2), continue ▼
    │
    ├── JS console errors?
    │   ├── NONE → Continue ▼
    │   └── ERRORS → Assess impact ▼
    │       ├── Affects purchase flow (cart/checkout/variant) → ██ ROLLBACK (P0) ██
    │       ├── Affects major feature (search/forms/nav) → LOG (P1), assess fix
    │       └── Cosmetic only (animation, hover, non-critical) → LOG (P3), continue ▼
    │
    ├── Analytics firing?
    │   ├── YES → Continue ▼
    │   └── NO → LOG (P2), continue ▼
    │           (Analytics failure is NOT rollback-worthy.
    │            Revenue still flows. Fix forward.)
    │
    ├── Redirects working?
    │   ├── ALL pass → Continue ▼
    │   ├── SOME fail → LOG (P2), continue (fix redirect entries)
    │   └── ALL fail → LOG (P1), investigate (possible systemic issue)
    │
    ├── Test transaction succeeds?
    │   ├── YES → ✅ DECLARE LAUNCH SUCCESSFUL
    │   └── NO → Assess ▼
    │       ├── Payment processor error → ██ ROLLBACK (P0) ██
    │       ├── Cart/checkout theme error → ██ ROLLBACK (P0) ██
    │       └── Test-specific issue (wrong card, etc.) → Retry once, then assess
    │
    └── ✅ LAUNCH SUCCESSFUL → Begin monitoring plan
```

---

## Decision Principles

1. **When in doubt, rollback.** The backup theme is the safe state. A rollback takes 2 minutes. A broken storefront loses revenue every minute.

2. **Rollback is NOT failure.** It's the planned safety mechanism. The new theme can be re-launched after fixing the issue.

3. **Revenue-impacting issues = immediate rollback.** If customers cannot complete purchases, every minute costs money.

4. **Non-revenue issues = fix forward.** Analytics, cosmetics, minor page issues — log them and fix without rollback.

5. **Owner has final authority.** If Owner says rollback, rollback. No debate during launch window.

---

## Post-Decision Actions

### After "ROLLBACK" Decision

1. Follow `m4d-rollback-procedure.md` immediately
2. Notify Owner (if Builder initiated)
3. Begin root cause analysis within 1 hour
4. Fix issue on preview theme
5. Re-validate
6. Schedule new launch window

### After "LAUNCH SUCCESSFUL" Decision

1. Notify Owner: "Launch successful. Entering monitoring phase."
2. Begin `m4d-monitoring-plan.md` hour-by-hour checks
3. Keep all monitoring tools open for 4 hours
4. Complete `m4d-24h-checklist.md` at the 24-hour mark

### After "LOG and Continue" Decision

1. Record the issue using the template in `m4d-severity-matrix.md`
2. Assign severity (P1–P3)
3. Continue with remaining launch checks
4. Fix during monitoring phase or next work session
5. Include in daily summary to Owner

---

## Quick Reference: Rollback vs. Fix Forward

| Rollback (do it now) | Fix Forward (log and continue) |
|----------------------|-------------------------------|
| Homepage blank/500 | One supporting page broken |
| Checkout unreachable | Analytics not firing |
| Payment broken | Minor styling issue |
| Cart completely non-functional | One redirect broken |
| Product pages all broken | Search results slightly off |
| Pricing wrong sitewide | Animation glitch |
| Navigation completely broken | One form not submitting |
