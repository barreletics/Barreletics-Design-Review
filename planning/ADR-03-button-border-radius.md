# ADR-03: Button Border-Radius (CRIT-003)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** Critical  
**Created:** 2026-07-13

---

## Problem Statement

The Component Library declares all buttons as square (`border-radius: 0px`). The PDP mock uses `6px` border-radius on CTA and size-selector buttons. A developer building the PDP must choose between the system rule and the PDP-specific mock.

## Conflicting Values

| Source | Value |
|---|---|
| `docs/04-COMPONENT-LIBRARY.md` line 37 | All buttons square (`border-radius: 0px`) |
| `docs/05-PDP-ARCHITECTURE.md` line 46 | `.pdp-buy__cta` uses `border-radius: 6px` |
| `docs/05-PDP-ARCHITECTURE.md` lines 230–231 | Size selector buttons use `border-radius: 6px` |

## Source Files

- `docs/04-COMPONENT-LIBRARY.md` — line 37
- `docs/05-PDP-ARCHITECTURE.md` — lines 46, 230–231

## Why the Conflict Exists

The PDP mock was designed as a standalone prototype before the system-level border-radius rule was established. The Component Library's "all square" rule was defined separately and was never reconciled against the PDP spec.

## Impact if Unresolved

- A developer following the Component Library will build square PDP buttons.
- A developer following the PDP spec will build rounded PDP buttons.
- The two outcomes look noticeably different and affect perceived brand consistency.
- QA cannot determine which is "correct" without an authoritative decision.

## Options

### Option A: PDP is an explicit exception

Document `6px` as a PDP-specific override in both `docs/04` and `docs/10`. System rule remains `0px` everywhere else.

| Pros | Cons |
|---|---|
| Preserves the PDP designer's intent | Creates a precedent for page-specific overrides |
| No visual change to the PDP mock | Complicates the "all buttons are square" system rule |
| Minimal document changes needed | Other pages may request similar exceptions |

### Option B: System rule wins — update PDP to 0px

Change PDP mock to use `border-radius: 0px` on all buttons. Requires visual review to confirm the result is acceptable.

| Pros | Cons |
|---|---|
| Clean, consistent system rule | PDP may look harsh/angular without rounded affordances |
| No exceptions to manage | Overrides the PDP designer's deliberate choice |
| Simpler for developers — one rule everywhere | Requires re-evaluation of PDP visual design |

### Option C: Compromise — 0px for CTA, 6px for size pills

Primary CTA button stays square (system rule). Size selector pills use `6px` (different UI affordance — selection chip vs action button).

| Pros | Cons |
|---|---|
| Distinguishes button types by visual affordance | Still an exception to the system rule for size pills |
| CTA aligns with system; pills feel like selection controls | Requires clear documentation of when 6px is permitted |
| Reasonable UX rationale for the distinction | May invite "what about other pill-like elements?" questions |

## Files Affected

- `docs/04-COMPONENT-LIBRARY.md`
- `docs/05-PDP-ARCHITECTURE.md`
- `docs/10-DECISIONS.md`

## Dependencies

- ADR-06 (Review Card Radius) — border-radius exceptions are a pattern; decisions here set precedent.
- Any shared button component in Shopify Liquid/CSS.

## Decision Required From

**Architect (ChatGPT)** — Select Option A, B, or C, or propose an alternative.
