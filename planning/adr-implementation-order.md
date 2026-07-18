# ADR Implementation Order

**Generated:** 2026-07-13  
**Purpose:** Safest sequence to implement ADR decisions with minimal merge conflicts

---

## File Touch Map

| File | ADRs That Touch It |
|------|-------------------|
| docs/03-DESIGN-SYSTEM.md | ADR-01, ADR-04, ADR-05, ADR-07 |
| docs/04-COMPONENT-LIBRARY.md | ADR-01, ADR-03, ADR-04, ADR-06, ADR-07 |
| docs/05-PDP-ARCHITECTURE.md | ADR-02, ADR-03, ADR-04, ADR-05, ADR-06, ADR-07 |
| docs/06-HOMEPAGE-ARCHITECTURE.md | ADR-01, ADR-04, ADR-05, ADR-07 |
| docs/07-COPY-GUIDE.md | ADR-01 (if warm palette retired) |
| docs/10-DECISIONS.md | ALL (decision recording) |

---

## Recommended Implementation Sequence

### Batch 1: Foundation — Palette Direction

**ADRs:** ADR-01 (Color Palette)  
**Priority:** Must resolve first — downstream decisions depend on this.

| Files Modified | Lines Affected | Conflict Risk |
|----------------|---------------|---------------|
| docs/04 (if Option A) | 23–26, 29, 130 | Low — isolated lines |
| docs/03, docs/06 (if Option B) | 03: 120–125; 06: 40–45, 5595–5600 | Medium — token blocks |
| docs/10 | 63 | Low |

**Rationale:** ADR-05 and ADR-07 both depend on knowing whether the palette is warm or neutral. ADR-04's muted text color also derives from this. Resolving ADR-01 first eliminates cascading uncertainty.

**Rollback strategy:** Revert the 4–6 token lines changed. No structural changes; purely value swaps within existing token definitions.

---

### Batch 2: Text Color — Follows Palette

**ADRs:** ADR-05 (PDP Text Color)  
**Priority:** Resolves after palette direction is known.

| Files Modified | Lines Affected | Conflict Risk |
|----------------|---------------|---------------|
| docs/04 line 20 (if Option A) | 1 line | Low |
| docs/03 lines 122, 374 (if Option A) | 2 lines | Low |
| docs/06 lines 42, 4210, 5597 (if Option A) | 3 lines | Low |
| docs/05 lines 24, 25, 42, 44, 46, 51, 56, 60, 73, 83, 88, 94, 97, 99 (if Option B) | 14+ lines | Medium |
| docs/10 | 63 | Low |

**Rationale:** Text color determines star color harmony (ADR-07). Must come before ADR-07.

**Rollback strategy:**
- Option A: revert 6 token-definition lines across 3 files
- Option B: revert `var(--br-text)` replacements back to `#1c1916` in docs/05 (all in CSS block lines 24–99)

---

### Batch 3: Star Color — Follows Text Color

**ADRs:** ADR-07 (Star Rating Color)  
**Priority:** Depends on ADR-05 resolution for color harmony.

| Files Modified | Lines Affected | Conflict Risk |
|----------------|---------------|---------------|
| docs/05 lines 41, 71, 552 (if Option A) | 3 lines | Low |
| docs/03 line 130, 374; docs/04 line 22; docs/06 line 55, 5610 (if Option B) | 5 lines | Low |
| docs/10 | 63 | Low |

**Rationale:** Small, contained change. Low risk of conflicts with any other batch.

**Rollback strategy:** Single hex-value swap in 2–5 locations. Trivially reversible.

---

### Batch 4: Radius Philosophy — Sets Precedent

**ADRs:** ADR-03 (Button Radius) + ADR-06 (Review Card Radius)  
**Bundle rationale:** Both address the same question — "are PDP radius overrides permitted?" Resolving together ensures philosophical consistency and avoids touching docs/05 twice.

| Files Modified | Lines Affected | Conflict Risk |
|----------------|---------------|---------------|
| docs/05 lines 46, 67, 80, 230–231, 36, 76, 541, 561 | 8–10 lines | Low (all in CSS block) |
| docs/04 lines 30–33, 37 | 4–5 lines | Low |
| docs/10 D-003, D-038 | 2 entries | Low |

**Rationale:** These two ADRs share a dependency and touch the same files. Implementing together prevents merge conflicts from touching the same CSS block in docs/05 twice. No dependency on palette/text color decisions.

**Rollback strategy:** Revert specific `border-radius` values in docs/05 CSS block. If docs/04 rule text was modified, restore original wording.

---

### Batch 5: Shipping Threshold — Independent

**ADRs:** ADR-02 (Free Shipping Threshold)  
**Priority:** Can run any time — no dependency on other ADRs.

| Files Modified | Lines Affected | Conflict Risk |
|----------------|---------------|---------------|
| docs/05 lines 264, 2197, 2295, 2360 | 4 lines | Very Low |
| docs/10 | note | Low |

**Rationale:** Purely a copy correction. Touches only docs/05 and only at 4 isolated locations spread across 2000+ lines. Zero interaction with any other ADR.

**Rollback strategy:** Change `$150` back to `$75` at 4 locations. No structural impact.

---

### Batch 6: Eyebrow Letter-Spacing — Most Complex

**ADRs:** ADR-04 (Eyebrow Letter-Spacing)  
**Priority:** Last — most complex, benefits from all prior decisions being stable.

| Files Modified | Lines Affected | Conflict Risk |
|----------------|---------------|---------------|
| docs/04 line 12 | 1 line | Low |
| docs/03 lines 149, 371, 394–398 | 3–5 lines | Low |
| docs/06 line 76 | 1 line (token comment) | Low |
| docs/05 lines 40, 55, 59, 81 (if Option A) | 4 lines | Low |
| docs/10 | conflict entry update | Low |

**Rationale:** This is the most complex conflict (4 different values, hundreds of CSS occurrences). By running last, all other changes to docs/03, docs/04, docs/05, and docs/06 are already settled. The changes here are to rule definitions (not to the hundreds of CSS occurrences which remain as-is once the rule is defined).

**Rollback strategy:** Revert the system rule text in docs/04 line 12 and docs/03 line 371. Token definition changes are 1-line edits.

---

## Parallel Execution Groups

The following can be executed in parallel without conflict:

| Group | ADRs | Condition |
|-------|------|-----------|
| A | ADR-02 | Always safe in parallel with anything |
| B | ADR-03 + ADR-06 | Safe in parallel with Batch 1–3 (different line ranges in docs/05) |
| C | ADR-01 → ADR-05 → ADR-07 | Must be sequential within group |

**Maximum parallelism plan:**
```
Time →
─────────────────────────────────────────────────
[ADR-01] → [ADR-05] → [ADR-07] → [ADR-04]
[ADR-02] ─────────────────────────────────────
[ADR-03 + ADR-06] ────────────────────────────
```

---

## Conflict Risk Summary

| Batch | Files | Conflict Risk | Reason |
|-------|-------|---------------|--------|
| 1 (ADR-01) | docs/04 or docs/03+06 | **Low** | Token value swaps in dedicated color sections |
| 2 (ADR-05) | docs/05, docs/03, docs/04, docs/06 | **Medium** | If Option B: 14+ lines in docs/05 CSS block |
| 3 (ADR-07) | docs/05, docs/03, docs/04, docs/06 | **Low** | 2–5 single hex swaps |
| 4 (ADR-03+06) | docs/05, docs/04 | **Low** | All in CSS block or rule definitions |
| 5 (ADR-02) | docs/05 | **Very Low** | 4 isolated lines, no structural changes |
| 6 (ADR-04) | docs/04, docs/03, docs/05, docs/06 | **Medium** | Rule definition changes — conceptually complex but few lines |

---

## Overall Risk Mitigation

1. **Branch strategy:** Implement each batch on a separate branch, merge sequentially. This ensures any line-number shifts from earlier batches are visible before the next batch begins.

2. **docs/10 coordination:** Every batch writes to docs/10-DECISIONS.md. To avoid conflicts, write all decision records in a single final commit after all ADRs are resolved, or append to the end of the file.

3. **docs/05 is the hottest file:** Touched by 6 of 7 ADRs. The changes are in different sections (CSS block at top, HTML at lines 190–265, matured HTML at 2190–2360), so merge conflicts are unlikely if batches are sequential.

4. **Verification gate:** After each batch, run the verification grep checks from the implementation checklists before proceeding to the next batch. This catches any unintended side effects.

5. **Atomic rollback:** Each batch's changes are small enough (4–14 lines) that a `git revert` on the batch commit cleanly undoes the work without touching other batches.
