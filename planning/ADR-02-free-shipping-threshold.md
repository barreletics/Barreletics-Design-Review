# ADR-02: Free Shipping Threshold (CRIT-002)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** Critical  
**Created:** 2026-07-13

---

## Problem Statement

`docs/05-PDP-ARCHITECTURE.md` (APPROVED) contains both `$75` and `$150` for the free shipping threshold within the same document. A developer reading the spec encounters contradictory copy.

## Conflicting Values

| Location in `docs/05-PDP-ARCHITECTURE.md` | Value | Status |
|---|---|---|
| Line 195 | $150 | ✓ Updated |
| Line 264 | $75 | ✗ Stale |
| Line 2197 | $75 | ✗ Stale |
| Line 2295 | $75 | ✗ Stale |
| Line 2360 | $75 | ✗ Stale |
| Line 2212 | $150 | ✓ Updated |

### Cross-references

- `docs/10-DECISIONS.md` C-010 declares this RESOLVED at $150.
- `docs/08-LIVE-SITE-COPY-AUDIT.md` confirms $150 as the current threshold.

## Source Files

- `docs/05-PDP-ARCHITECTURE.md` — lines 195, 264, 2197, 2212, 2295, 2360

## Why the Conflict Exists

The PDP spec was originally written when the free shipping threshold was $75. During a later update, some instances were changed to $150 but others were missed. The document was approved with both values present.

## Impact if Unresolved

- A developer implementing the PDP shipping bar may use $75 if they encounter those lines first.
- Copy/paste from the wrong section produces incorrect customer-facing messaging.
- The live site already uses $150, so $75 references are factually wrong.

## Options

### Option A: Replace all $75 with $150 in docs/05

Add an inline comment noting the change and referencing C-010.

| Pros | Cons |
|---|---|
| Eliminates all ambiguity | Modifies an APPROVED document |
| Aligns docs/05 with docs/10 and docs/08 | Loses traceability of the original $75 value |
| Prevents implementation errors | Requires re-review of the APPROVED status |

### Option B: Leave docs/05 as-is; add a conflict note at the top

Treat docs/05 as a "lossless" capture of the original PDP spec. Add a header note stating that all $75 references should be read as $150 per C-010.

| Pros | Cons |
|---|---|
| Preserves the original document exactly | Developer must read the header note to avoid errors |
| No re-approval needed for content changes | Increases cognitive load — two values in one document |
| Maintains audit trail of the original spec | Easy to miss the header note in a long document |

## Files Affected

- `docs/05-PDP-ARCHITECTURE.md`

## Dependencies

- `docs/10-DECISIONS.md` C-010 — already resolved at $150.
- `docs/08-LIVE-SITE-COPY-AUDIT.md` — confirms $150.
- Any Shopify Liquid template implementing the shipping bar.

## Decision Required From

**Architect (ChatGPT)** — Select Option A or B.
