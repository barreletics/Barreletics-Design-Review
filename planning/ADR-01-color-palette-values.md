# ADR-01: Color Palette Values (CRIT-001)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** Critical  
**Created:** 2026-07-13

---

## Problem Statement

Two APPROVED documents declare different color values for the same design tokens. Implementation will produce visually different results depending on which document is followed.

## Conflicting Values

| Token | `docs/04-COMPONENT-LIBRARY.md` (lines 23–26) | `docs/06-HOMEPAGE-ARCHITECTURE.md` (CSS `:root`, lines 40–45) |
|---|---|---|
| Alt background | `#f9f7f2` | `#f9f9f9` |
| Text (soft) | `#6a6a6a` | `#4a4a4a` |
| Text (muted) | `#999999` | `#8a8a8a` |
| Line (border) | `#e5e2db` | `#e6e6e6` |

### Additional references

- `docs/10-DECISIONS.md` (D-007) uses the docs/06 values.
- `docs/03-DESIGN-SYSTEM.md` uses the docs/06 values.
- `docs/06-HOMEPAGE-ARCHITECTURE.md` (line 38) explicitly states: *"cream/plum palette in Shopify settings_data.json is dead code."*

## Source Files

- `docs/04-COMPONENT-LIBRARY.md` — lines 23–26
- `docs/06-HOMEPAGE-ARCHITECTURE.md` — lines 40–45 (CSS `:root` block)
- `docs/03-DESIGN-SYSTEM.md`
- `docs/10-DECISIONS.md` — D-007

## Why the Conflict Exists

`docs/04` was written summarizing from a design handoff that used warm tones. `docs/06` was extracted from actual CSS `:root` tokens in the matured homepage HTML. The two were never reconciled.

## Impact if Unresolved

- The warm `#f9f7f2` alt-background is visibly cream-toned; `#f9f9f9` is neutral grey. A developer following docs/04 will produce a noticeably warmer page than one following docs/06.
- Text contrast ratios differ between the two sets (e.g., `#6a6a6a` vs `#4a4a4a` on white backgrounds).
- Border/line colors will feel warm or neutral depending on the source followed.

## Options

### Option A: Adopt docs/06 values everywhere

Canonical values: `#f9f9f9`, `#4a4a4a`, `#8a8a8a`, `#e6e6e6`  
Treat docs/04 values as from an earlier design pass.

| Pros | Cons |
|---|---|
| Matches actual CSS tokens in the matured homepage | Discards the intentionally warm palette from the handoff |
| Already used by docs/03, docs/06, and docs/10 (majority) | Requires updating docs/04 |
| Neutral grey is safer for accessibility contrast | Loses the distinctive "cream" brand warmth |

### Option B: Adopt docs/04 values everywhere

Canonical values: `#f9f7f2`, `#6a6a6a`, `#999999`, `#e5e2db`  
Treat as intentionally warmer brand direction.

| Pros | Cons |
|---|---|
| Preserves the warm, distinctive brand feel | Contradicts the matured CSS tokens actually in production |
| Aligns with original design handoff intent | Requires updating docs/03, docs/06, and docs/10 |
| Warmer tones may better suit athletic/premium positioning | `#999999` text on white may have accessibility concerns |

### Option C: Document both as valid contexts

Warm palette for certain sections (e.g., brand storytelling), neutral palette for others (e.g., product/commerce).

| Pros | Cons |
|---|---|
| Preserves both design intentions | Increases implementation complexity |
| Allows contextual brand expression | Developers need clear rules for which palette to use where |
| No document needs to be "wrong" | Risk of inconsistent application without strict guidelines |

## Files Affected

- `docs/04-COMPONENT-LIBRARY.md`
- `docs/06-HOMEPAGE-ARCHITECTURE.md`
- `docs/03-DESIGN-SYSTEM.md`
- `docs/10-DECISIONS.md`

## Dependencies

- ADR-05 (PDP Text Color) — text color decisions may interact with soft/muted text palette choices.
- Any Shopify `settings_data.json` cleanup depends on which palette is canonical.

## Decision Required From

**Architect (ChatGPT)** — Select Option A, B, or C, or propose a hybrid.
