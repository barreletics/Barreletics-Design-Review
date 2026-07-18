# ADR-06: PDP Review Card Radius 12px vs System Max 4px (HIGH-005)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** High  
**Created:** 2026-07-13

---

## Problem

The PDP spec uses `border-radius: 12px` on review cards and justifier cards. The system design rule explicitly states a maximum of 2–4px and says "Never use 12–16px pill-card." The PDP uses the exact value the system prohibits. This is not a gray area — `12px` is the lower bound of the explicitly forbidden range.

## Evidence

| Source | Value | Exact location |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` lines 30–33 | "No radius by default. Where matured uses radius: 2px or 4px only. Never use pill-card style (12–16px radius)" | System rule under "Spacing & Borders" |
| `docs/03-DESIGN-SYSTEM.md` line 372 | "Buttons: Square (radius 0), black #050505" | Research Bible — square aesthetic |
| `docs/05-PDP-ARCHITECTURE.md` line 67 | `.review-card { border-radius: 12px }` | PDP review card component |
| `docs/05-PDP-ARCHITECTURE.md` line 80 | `.pdp-justifier__card { border-radius: 12px }` | PDP justifier/testimonial card |
| `docs/05-PDP-ARCHITECTURE.md` line 36 | `.pdp-gallery__hero { border-radius: 8px }` | PDP gallery hero image (also exceeds 4px max) |
| `docs/05-PDP-ARCHITECTURE.md` line 76 | `.pdp-motion__video { border-radius: 8px }` | PDP motion video container (also exceeds 4px max) |
| `docs/05-PDP-ARCHITECTURE.md` line 46 | `.pdp-buy__cta { border-radius: 6px }` | PDP CTA button (system says radius 0 for buttons) |

The PDP spec contains five distinct border-radius values (`3px`, `6px`, `8px`, `12px`, `50%` for swatches) — none of which conform to the system's "0px default, 2–4px max" rule. The `12px` on review and justifier cards is the most egregious violation.

## Source Files

- `docs/04-COMPONENT-LIBRARY.md` — lines 30–33 (system border-radius rule)
- `docs/03-DESIGN-SYSTEM.md` — line 372 (Research Bible square aesthetic)
- `docs/05-PDP-ARCHITECTURE.md` — lines 36, 46, 67, 76, 80 (PDP radius values)

## Line References

| File | Line(s) | What it defines |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` | 30 | "Border radius: No radius by default" |
| `docs/04-COMPONENT-LIBRARY.md` | 31 | "Cards: 0px (square)" |
| `docs/04-COMPONENT-LIBRARY.md` | 32 | "Where matured direction uses radius: 2px or 4px only" |
| `docs/04-COMPONENT-LIBRARY.md` | 33 | "Never use pill-card style (12–16px radius)" |
| `docs/05-PDP-ARCHITECTURE.md` | 67 | `.review-card { border-radius: 12px }` |
| `docs/05-PDP-ARCHITECTURE.md` | 80 | `.pdp-justifier__card { border-radius: 12px }` |
| `docs/05-PDP-ARCHITECTURE.md` | 36 | `.pdp-gallery__hero { border-radius: 8px }` |
| `docs/05-PDP-ARCHITECTURE.md` | 46 | `.pdp-buy__cta { border-radius: 6px }` |

## Dependencies

- **ADR-03 (Button Border-Radius):** The PDP CTA button at `6px` also violates the system's `0px` rule for buttons. Decisions on card radius and button radius should be consistent in philosophy — either system rules are strict or page-level overrides are permitted.
- **Shared `.review-card` CSS:** If a review card component is reused across PDP and other pages, the radius must be consistent or scoped.
- **Brand identity:** The system rule's angular aesthetic ("square cards, no pill shapes") is a deliberate brand choice. Overriding it changes the brand feel.

## Options

### Option A: PDP review/justifier cards are explicit exceptions — allow `12px`

Document `12px` as permitted specifically for review/testimonial and justifier cards on the PDP. Update `docs/04` to note this exception. Other PDP radius values (`8px` gallery, `6px` CTA) are addressed separately.

| Pros | Cons |
|---|---|
| Preserves the PDP designer's deliberate choice for softer testimonial cards | Directly contradicts the "Never use 12–16px" prohibition |
| Softer radius suits the informal, human tone of reviews/testimonials | Creates a precedent — other components will request similar exceptions |
| Minimal change to PDP spec | The system rule's "Never" language loses enforceability |
| Review cards are a distinct content type (user-generated) that may warrant different treatment | Must audit all future components against the expanded exception list |

### Option B: System rule wins — change PDP to 4px max

Update PDP review cards to `border-radius: 4px` and justifier cards to `4px`. The system rule stands as written. Also address `8px` gallery and `6px` CTA as separate line items.

| Pros | Cons |
|---|---|
| Clean, enforceable system rule with no exceptions | Overrides the PDP designer's deliberate choice |
| "Never use 12–16px" means exactly what it says | Review cards at 4px may feel too sharp for testimonial content |
| Consistent angular aesthetic across the entire site | Requires visual review — the PDP mock was approved with 12px |
| Simpler for developers — one rule, no judgment calls | Also must address gallery (8px) and CTA (6px) — cascade of changes |

### Option C: Revise the system rule — define a "content card" exception tier

Update docs/04 to read: "0px default; 2–4px for structural cards; up to 12px permitted for content/testimonial cards only." Define the qualifying component types.

| Pros | Cons |
|---|---|
| Accommodates the PDP design with a scoped, named exception | Weakens the "never" prohibition — must justify why 12px is now acceptable |
| Creates a principled distinction (structural vs content cards) | Must define exactly which components qualify as "content cards" |
| Review/testimonial cards are a reasonable exception class | Risk of scope creep ("what about FAQ cards? Product cards?") |
| Other PDP radius values (8px, 6px) still need separate resolution | Adds a classification layer to the design system |

## Repository Impact

- **Option A:** Add exception annotation to `docs/04-COMPONENT-LIBRARY.md` lines 30–33. Add note to `docs/05-PDP-ARCHITECTURE.md` line 67 documenting the approved exception. Record in `docs/10-DECISIONS.md`.
- **Option B:** Update `docs/05-PDP-ARCHITECTURE.md` lines 67 and 80 (change `12px` → `4px`). Also flag lines 36 (`8px`), 46 (`6px`), and 76 (`8px`) for separate resolution. No changes to docs/04.
- **Option C:** Rewrite `docs/04-COMPONENT-LIBRARY.md` lines 30–33 to include the content card exception tier. Record the rationale in `docs/10-DECISIONS.md`.
- **All options:** The PDP spec contains 5 non-conforming radius values. This ADR addresses the `12px` cards; the `8px` gallery, `6px` CTA, and `3px` badge should be resolved in follow-up ADRs or bundled into this decision.

## Shopify Impact

- A Shopify developer building the review section finds `.review-card { border-radius: 12px }` in the PDP spec but reads "Never use 12–16px" in the design system. The build is blocked until clarification is received.
- If the Shopify theme uses a global `--br-radius-card` token, its value (`0px` or `4px`) will conflict with the PDP's `12px`. The developer must either create a PDP-specific override or change the global token.
- Shopify's section rendering means review cards could appear on non-PDP pages (e.g., a homepage testimonial section). If `12px` is PDP-only, the Liquid template must scope the radius to the PDP context.
- Third-party review apps (Judge.me, Loox, etc.) inject their own card styles. If the Barreletics theme enforces `4px` but the app injects `12px`, the visual will be inconsistent unless the theme's CSS overrides the app.

## Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Developer follows system rule, builds 4px cards — mismatches approved PDP mock | High | Medium — visual mismatch with design intent | Resolve before PDP build |
| "Never" rule exception sets precedent for other pill-radius requests | Medium | Medium — design system authority erodes | If allowing exceptions, define a closed list of qualifying components |
| Review cards at 4px feel too sharp for testimonial content | Medium (if Option B) | Low — aesthetic preference, not functional | Prototype both values and get designer sign-off |
| Third-party review app styles conflict with chosen radius | Medium | Low — CSS override resolves it | Include app-override CSS in Shopify theme |
| Scope creep: FAQ cards, product cards request 12px exception | Medium (if Option C) | Medium — system rule becomes meaningless | Define the exception tier narrowly and enforce in code reviews |

## Decision Required From

**Architect (ChatGPT)** — Select Option A, B, or C. If A or C, specify whether the PDP's other non-conforming radius values (`8px` gallery, `6px` CTA, `3px` badge) are also approved exceptions or must be resolved separately.
