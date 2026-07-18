# QA Review: 10-DECISIONS.md

**Reviewer:** Cursor (Build Engineer)  
**Date:** 2026-07-13  
**Document:** docs/10-DECISIONS.md  
**Status:** PENDING REVIEW  
**Lines:** 1,092

---

## Document Purpose

Complete chronological decision log. Contains every design decision (D-001–D-041), brand decision (B-001–B-016), naming decision (N-001–N-006), product decision (P-001–P-011), business decision (BZ-001–BZ-013), section decision (CEO review), operational decision (O-001–O-009), implementation decision (I-001–I-012), component placement rules, page architecture decisions, implementation roadmap summary, and a source conflicts register (C-001–C-010).

---

## Source Coverage

**Sources listed in header (line 6):** Barreletics_Research_Bible.md, barreletics-decisions-2026-07-09.json, IMPLEMENTATION-ROADMAP-Jul2026.md, Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html, docs/02–09, manychat-kb/, WORKFLOW.md, docs/04-COMPONENT-LIBRARY.md, docs/05-PDP-ARCHITECTURE.md

**Problem with "docs/02–09":** This range notation is imprecise. The document actually references:
- docs/02-BRAND-SYSTEM.md — ✓ (line 326, 333, etc.)
- docs/03-DESIGN-SYSTEM.md — ✓ (lines 18, 42, 75, etc.)
- docs/04-COMPONENT-LIBRARY.md — ✓ (lines 18, 34, 50, etc.)
- docs/05-PDP-ARCHITECTURE.md — ✓ (lines 63, 276, 283, etc.)
- docs/06-HOMEPAGE-ARCHITECTURE.md — ✓ (lines 42, 67, 132, etc.)
- docs/08-LIVE-SITE-COPY-AUDIT.md — ✓ (line 589)
- docs/09-PRODUCT-KNOWLEDGE.md — ✓ (lines 445, 453, 459, etc.)
- **NOT docs/07-COPY-GUIDE.md** — never referenced

**Verdict:** Header should list specific docs referenced instead of the imprecise "docs/02–09" range.

---

## Citation Coverage

**Total decision entries:** 100+ (D-001–D-041, B-001–B-016, N-001–N-006, P-001–P-011, BZ-001–BZ-013, O-001–O-009, I-001–I-012, plus section decisions and page architecture)  
**Entries with Source: citations:** All named decisions have Source: lines.  
**CEO section decisions (lines 647–823):** Sourced collectively to barreletics-decisions-2026-07-09.json and IMPLEMENTATION-ROADMAP-Jul2026.md.

**Coverage quality:** Very good. Every decision block has at least one Source: line.

---

## Missing Sources

1. **docs/07-COPY-GUIDE.md** — listed in the "docs/02–09" range but never actually referenced. Should either be explicitly excluded or a reference added.
2. **docs/01-BRAND-NORTH-STAR.md** — not listed in header Sources, not referenced in the body. Several brand decisions (B-001 through B-016) originate from content also in docs/01.

---

## Contradictions

### MEDIUM: SAVE15 vs save15

| Location | Value |
|----------|-------|
| BZ-006 (line 593) | "Code: SAVE15" |
| docs/09 line 25 | "code: save15" |

Cross-document casing inconsistency. Both documents should use the same casing.

### MEDIUM: P-002 Size Range vs docs/09

| Location | Large size |
|----------|-----------|
| P-002 (line 492) | "Large (W 8–11 / M up to 10.5)" |
| docs/09 line 36 (Closed Sole size table) | L: W 7.5–11 |
| manychat-kb/03-sizing-chart.md | L: W 7.5–11 |

P-002 says Large starts at W 8, but the source material says W 7.5. This is a factual error in docs/10.

### MINOR: Collection Section Count

Line 1034 says "Collection — Matured Direction (7 Sections)" but only lists 6 numbered items:
1. Ticker + header
2. Collection hero
3. Sole-type chooser
4. Filter row
5. Product grid
6. Footer

The "7" in the heading doesn't match the 6 listed items. (docs/03 also lists 7 sections but includes "Editorial break" as section 6 and "Footer" as section 7.)

---

## Duplications

| Content | Also appears in | Severity |
|---------|----------------|----------|
| Design token values (D-007, D-016, D-017) | docs/03 (canonical source) | Expected |
| Brand decisions (B-001–B-016) | docs/02 (source document) | Expected |
| Product decisions (P-001–P-011) | docs/09 (product catalog) | Expected |
| Page architecture (Home/PDP/Collection orders) | docs/03 (Design System) | Expected |
| Source Conflicts Register (C-001–C-010) | docs/03, docs/09 (partial overlap) | Expected |

**Analysis:** docs/10 is the decision log — it is expected to reference and catalog decisions from other documents. This is its purpose. The duplications are by design.

---

## Unsupported Claims

None identified. Every decision is sourced. The CEO section decisions preserve verbatim notes (with typos intact) — this is good practice for a decision log.

---

## Known Gaps

### Coverage Gaps

1. **No decisions sourced from docs/07 (Copy Guide).** If the "docs/02–09" range in the header implies coverage of docs/07, there should be at least one decision referencing it, or docs/07 should be excluded from the range.

2. **No decisions sourced from docs/01 (Brand North Star).** The foundational brand document should be referenced for brand-level decisions.

3. **Coperni at $115 — no inventory note.** P-001 (line 482) lists Coperni at $115 but doesn't note that M size has -1 inventory (oversold/effectively discontinued for that size). docs/09 flags this in its Data Quality section.

4. **CEO section decisions — some undecided.** Sections 04, 15, 24, 25, 29 are marked undecided (lines 671, 736, 787, 793, 819). These are open items that need resolution. The document preserves them correctly — this is not a defect, but a gap that should be tracked.

### Structural Gaps

5. **No "Open Questions" summary.** The CEO section decisions contain 5 undecided items and several "Status: Open question" items (I-009, I-011, I-012). These should be collected into a summary section for easy tracking.

---

## Exact Fixes Required

1. **Line 6** — Replace "docs/02–09" with specific list: "docs/02-BRAND-SYSTEM.md, docs/03-DESIGN-SYSTEM.md, docs/04-COMPONENT-LIBRARY.md, docs/05-PDP-ARCHITECTURE.md, docs/06-HOMEPAGE-ARCHITECTURE.md, docs/08-LIVE-SITE-COPY-AUDIT.md, docs/09-PRODUCT-KNOWLEDGE.md"

2. **Line 492 (P-002)** — Change "Large (W 8–11 / M up to 10.5)" to "Large (W 7.5–11 / M up to 10.5)" to match manychat-kb/03-sizing-chart.md and docs/09 line 36.

3. **Line 593 (BZ-006)** — Verify live site discount code casing. Align with docs/09 (currently "SAVE15" here vs "save15" in docs/09).

4. **Line 1034** — Change "7 Sections" to "6 Sections" OR add the missing "Editorial break" item from docs/03 as item 6, moving Footer to item 7.

5. **Line 482 (P-001, Coperni)** — Add note: "Note: M size at -1 inventory (see docs/09 Data Quality Flags)."

---

## Final Recommendation

**CONDITIONAL**

The decision log is comprehensive and well-organized — 100+ decisions across 11 categories with consistent formatting and source citations. The CEO section decisions are preserved verbatim (typos and all), which is exactly right for a decision log. The five fixes above are all straightforward: the P-002 size range error (W 8–11 should be W 7.5–11) is the most important since it's a factual inaccuracy. Fix these and this passes.
