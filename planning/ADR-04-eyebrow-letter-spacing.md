# ADR-04: Eyebrow Letter-Spacing (HIGH-001)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** High  
**Created:** 2026-07-13

---

## Problem

Four different `letter-spacing` values and two different `font-weight` values exist for eyebrow elements across APPROVED documents. A developer building any new section has no unambiguous default. The spread from `0.06em` to `0.18em` is a 3× range — visually distinct at every step.

## Evidence

| Source | `letter-spacing` | `font-weight` | Exact location |
|---|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` line 12 | `0.14em` | 700 | System rule: "Eyebrows (labels): 12px / font-weight 700 / letter-spacing 0.14em / uppercase" |
| `docs/03-DESIGN-SYSTEM.md` line 371 | `0.14em` | 700 | Research Bible core rule: "Eyebrows: 12px/700/0.14em/uppercase" |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` CSS `--t-eyebrow` token | `0.08em` | 600 | Matured homepage CSS token extracted from production HTML |
| `docs/05-PDP-ARCHITECTURE.md` line 40 | `0.08em` | 700 | `.pdp-buy__badge { letter-spacing: 0.08em }` |
| `docs/05-PDP-ARCHITECTURE.md` line 55 | `0.08em` | 700 | `.pdp-section__label { letter-spacing: 0.08em }` |
| `docs/04-COMPONENT-LIBRARY.md` line 576 | `0.18em` | — | Manifesto section eyebrow (component-specific) |
| `docs/04-COMPONENT-LIBRARY.md` line 668 | `0.06em` | 600 | Closing CTA eyebrow (component-specific) |

The Research Bible (`docs/03` line 371) and Component Library header (`docs/04` line 12) agree on `0.14em / 700`. The PDP spec (`docs/05` lines 40, 55) and homepage CSS token both use `0.08em`. Two additional one-off values (`0.18em`, `0.06em`) appear in individual component specs within `docs/04`.

## Source Files

- `docs/04-COMPONENT-LIBRARY.md` — lines 12, 576, 668
- `docs/03-DESIGN-SYSTEM.md` — line 371
- `docs/06-HOMEPAGE-ARCHITECTURE.md` — CSS `--t-eyebrow` token definition
- `docs/05-PDP-ARCHITECTURE.md` — lines 40, 55, 59, 81

## Line References

| File | Line(s) | What it defines |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` | 12 | System typography rule (0.14em / 700) |
| `docs/03-DESIGN-SYSTEM.md` | 371 | Research Bible core rule (0.14em / 700) |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` | CSS vars block | `--t-eyebrow` token (0.08em / 600) |
| `docs/05-PDP-ARCHITECTURE.md` | 40 | PDP badge eyebrow (0.08em / 700) |
| `docs/05-PDP-ARCHITECTURE.md` | 55 | PDP section label (0.08em / 700) |
| `docs/04-COMPONENT-LIBRARY.md` | 576 | Manifesto section (0.18em) |
| `docs/04-COMPONENT-LIBRARY.md` | 668 | Closing CTA (0.06em / 600) |

## Dependencies

- **ADR-05 (PDP Text Color):** Eyebrow color rendering depends on the text color baseline chosen.
- **CSS tokens:** Any shared `.eyebrow`, `--t-eyebrow`, or `.pdp-section__label` class in the Shopify theme inherits this decision.
- **Component Library typography scale:** This is the first token in the type scale; changing it sets precedent for how other type tokens are resolved.
- **docs/03-DESIGN-SYSTEM.md** line 396–398 explicitly flags this conflict and defers to Architect.

## Options

### Option A: `0.14em / 700` as system default

Matches Research Bible + Component Library header. Component-level overrides (`0.18em`, `0.06em`, `0.08em`) treated as documented exceptions.

| Pros | Cons |
|---|---|
| Two independent source documents agree (docs/03, docs/04 header) | Contradicts the matured CSS tokens and PDP spec |
| Preserves earliest design intent | Wider spacing may feel dated vs the tighter matured look |
| Bold weight (700) is more assertive for labels | Requires updating docs/06 CSS token and PDP badge/label classes |
| Clear single default for new sections | 4 existing component specs become exceptions needing documentation |

### Option B: `0.08em / 600` as system default

Matches actual CSS tokens in matured homepage and PDP production pages.

| Pros | Cons |
|---|---|
| Matches production CSS in matured pages + PDP | Contradicts the Research Bible and Component Library header |
| Tighter spacing reads as more refined/modern | Requires updating docs/03 line 371 and docs/04 line 12 |
| Semi-bold (600) is current trend for eyebrows | Only the homepage CSS token explicitly uses weight 600 — PDP uses 700 with 0.08em |
| Fewer files to update if PDP and homepage are treated as canonical | Manifesto (0.18em) and closing CTA (0.06em) still need exception documentation |

### Option C: Two tiers — hero-grade and compact

- `0.14em / 700` for "hero-grade" eyebrows (section labels, major headings)
- `0.08em / 600` for "compact" eyebrows (inline badges, component labels, PDP elements)

| Pros | Cons |
|---|---|
| Preserves both design intentions without declaring either wrong | Adds complexity — developers must classify each eyebrow |
| Creates meaningful visual hierarchy within the eyebrow class | Requires clear documentation defining which tier applies where |
| No source document is entirely invalidated | Manifesto (0.18em) and closing CTA (0.06em) still don't fit either tier cleanly |
| Matches observed usage patterns (large sections use wider, small elements use tighter) | Two tokens to maintain instead of one |

## Repository Impact

- **docs/03-DESIGN-SYSTEM.md** — line 371 must be updated if Option B or C is chosen.
- **docs/04-COMPONENT-LIBRARY.md** — line 12 must be updated if Option B is chosen; lines 576 and 668 need exception annotations under any option.
- **docs/06-HOMEPAGE-ARCHITECTURE.md** — CSS `--t-eyebrow` token must be updated if Option A is chosen.
- **docs/05-PDP-ARCHITECTURE.md** — lines 40, 55, 59, 81 must be updated if Option A is chosen.
- **docs/10-DECISIONS.md** — Record the decision and rationale.

## Shopify Impact

- A developer building the Shopify theme encounters `.eyebrow` or `--t-eyebrow` in the CSS. If the token says `0.08em` but the design system doc says `0.14em`, they must stop and ask which is correct — blocking the build.
- If the PDP and homepage are built by different developers, each may follow their respective spec, producing visible inconsistency in the live store.
- The `.pdp-buy__badge` and `.pdp-section__label` classes are PDP-specific — if a global `.eyebrow` utility is created for the Shopify theme, it will conflict with these PDP classes unless the relationship is documented.
- Shopify's theme editor exposes typography settings; if a merchant adjusts letter-spacing globally, the interaction with component-level overrides is unpredictable.

## Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Developer uses wrong value, ships inconsistent eyebrows | High (conflict exists in approved docs) | Medium — visual inconsistency across pages | Resolve this ADR before Shopify build begins |
| Two-tier system (Option C) leads to ambiguous classification | Medium | Low — worst case, wrong tier is used and later corrected | Provide a lookup table mapping every component to its tier |
| Changing the Research Bible value undermines trust in docs/03 | Low | Medium — sets precedent that Research Bible can be overridden | Document the override rationale in docs/10-DECISIONS.md |
| Component-level overrides (0.18em, 0.06em) proliferate | Medium | Medium — type system becomes unpredictable | Cap permitted overrides in the decision and enforce via CSS linting |

## Decision Required From

**Architect (ChatGPT)** — Select Option A, B, or C, or propose an alternative. Specify whether the component-level overrides (manifesto `0.18em`, closing CTA `0.06em`) are permitted, deprecated, or eliminated.
