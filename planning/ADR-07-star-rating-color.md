# ADR-07: Star/Rating Color #fbc02d vs #d4af37 (HIGH-006)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** High  
**Created:** 2026-07-13

---

## Problem

The PDP spec uses `#d4af37` (dark antique gold) for star ratings while the system token and homepage CSS use `#fbc02d` (bright Material Design amber). Stars on the PDP will be a noticeably different gold than stars elsewhere on the site. A customer navigating from homepage to PDP sees a color shift in the star ratings.

## Evidence

| Source | Value | Exact location |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` line 22 | `#fbc02d` | Color Palette: "Star (rating): #fbc02d" |
| `docs/03-DESIGN-SYSTEM.md` line 374 | `#fbc02d` | Research Bible core rule: "star=#fbc02d" |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` line 55 | `--br-star: #fbc02d` | Homepage CSS custom property definition — "gold star color" |
| `docs/05-PDP-ARCHITECTURE.md` line 41 | `color: #d4af37` | `.pdp-buy__stars` — PDP hero star rating |
| `docs/05-PDP-ARCHITECTURE.md` line 71 | `color: #d4af37` | `.review-stars` — PDP review card star rating |

### Visual Comparison

- **`#fbc02d`** — Brighter, more yellow gold. Material Design amber-600. RGB(251, 192, 45). High saturation, high luminance.
- **`#d4af37`** — Darker, richer, antique/metallic gold. RGB(212, 175, 55). Lower luminance, more muted. Sometimes called "old gold."

The hue shift is approximately 5° and the luminance difference is ~15%. Side by side, `#fbc02d` reads as "bright yellow-gold" and `#d4af37` reads as "dark warm gold." On a white background, the contrast ratio of `#fbc02d` is ~2.1:1 (fails WCAG AA for text) while `#d4af37` is ~3.0:1 (still fails AA but is closer).

## Source Files

- `docs/04-COMPONENT-LIBRARY.md` — line 22
- `docs/03-DESIGN-SYSTEM.md` — line 374
- `docs/06-HOMEPAGE-ARCHITECTURE.md` — line 55
- `docs/05-PDP-ARCHITECTURE.md` — lines 41, 71

## Line References

| File | Line(s) | What it defines |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` | 22 | System token — "Star (rating): #fbc02d" |
| `docs/03-DESIGN-SYSTEM.md` | 374 | Research Bible — "star=#fbc02d" |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` | 55 | CSS custom property `--br-star: #fbc02d` |
| `docs/05-PDP-ARCHITECTURE.md` | 41 | PDP hero stars `.pdp-buy__stars { color: #d4af37 }` |
| `docs/05-PDP-ARCHITECTURE.md` | 71 | PDP review stars `.review-stars { color: #d4af37 }` |

## Dependencies

- **ADR-05 (PDP Text Color):** If PDP text resolves to `#1c1916` (warm brown), the darker `#d4af37` may have been chosen to harmonize with that warmer palette. If PDP text resolves to `#050505`, the brighter `#fbc02d` may be more appropriate.
- **ADR-01 (Color Palette Values):** The warm-vs-neutral palette direction affects which gold feels more cohesive with the overall brand.
- **ADR-06 (Review Card Radius):** Review cards contain star ratings. If review card styling is being revisited, star color should be resolved simultaneously.
- **CSS token `--br-star`:** The homepage uses `var(--br-star)`. The PDP hardcodes the value. Resolution must address whether PDP should reference the token.
- **Accessibility:** Neither gold passes WCAG AA for text on white, but stars are decorative/iconic, not informational text. The numeric rating adjacent to stars provides the accessible value.

## Options

### Option A: Use `#fbc02d` everywhere — system token wins

Update PDP to reference `var(--br-star)` or hardcode `#fbc02d`. Three source documents already agree on this value.

| Pros | Cons |
|---|---|
| Consistent star color across all pages — no shift between homepage and PDP | Brighter gold may not pair as well with PDP's warmer `#1c1916` palette |
| Single token, no exceptions — simple for developers | Overrides the PDP designer's deliberate contextual choice |
| Three source documents agree (docs/03, docs/04, docs/06) | If PDP retains `#1c1916` text (ADR-05), `#fbc02d` may feel too "poppy" against it |
| Material Design amber is a well-established convention | Requires updating docs/05 lines 41 and 71 |

### Option B: Use `#d4af37` everywhere — PDP value wins

Update the system token and homepage CSS to use the darker antique gold. Update docs/03, docs/04, and docs/06.

| Pros | Cons |
|---|---|
| Richer, more premium-feeling gold suits an athletic brand | Requires updating 3 source documents and 1 CSS token |
| Better contrast ratio on white backgrounds (3.0:1 vs 2.1:1) | Departs from the Material Design amber convention |
| Darker gold pairs well with both `#050505` and `#1c1916` text | Only one source document (PDP) currently uses this value |
| More distinctive — avoids the generic "Google review star" look | May appear muddy/dull on non-white backgrounds (e.g., `#f9f7f2` alt bg) |

### Option C: Keep both — PDP intentionally uses darker gold

Document that the PDP uses `#d4af37` to harmonize with its warmer `#1c1916` text palette, while the homepage and other pages use `#fbc02d` against the `#050505` base palette. The difference is contextual.

| Pros | Cons |
|---|---|
| Respects each designer's contextual choice | Two "gold" colors in the design system — confusing for developers |
| Darker gold may have better contrast on PDP's warmer background | Star color shifts visibly when customer navigates homepage → PDP |
| No source documents need to change | Harder to maintain — token system has an exception for a single page type |
| Least disruption to existing specs | A shared star-rating component can't have a single style — must be context-aware |

## Repository Impact

- **Option A:** Update `docs/05-PDP-ARCHITECTURE.md` lines 41 and 71 (change `#d4af37` → `#fbc02d` or `var(--br-star)`). No changes to other docs.
- **Option B:** Update `docs/04-COMPONENT-LIBRARY.md` line 22, `docs/03-DESIGN-SYSTEM.md` line 374, and `docs/06-HOMEPAGE-ARCHITECTURE.md` line 55 (change `#fbc02d` → `#d4af37`).
- **Option C:** Add documentation note to `docs/10-DECISIONS.md` explaining the intentional divergence. No file changes.
- **All options:** Record decision rationale in `docs/10-DECISIONS.md`. If Option A or B, verify that the chosen gold works against all background colors in the palette (`#ffffff`, `#f9f7f2`, `#f9f9f9`, `#f5f2ec`).

## Shopify Impact

- A Shopify developer building a star-rating snippet or Liquid partial uses `var(--br-star)`, which resolves to `#fbc02d`. If they then build the PDP and follow the PDP spec, they hardcode `#d4af37` — the same component shows two colors.
- Third-party review apps (Judge.me, Loox, Stamped) inject star colors via their own CSS. The Barreletics theme must override app stars to match the chosen gold, or accept inconsistency with injected widgets.
- Shopify's `settings_schema.json` can expose star color as a theme setting. If the merchant changes it, both homepage and PDP should update — but only if PDP references the token instead of hardcoding.
- If stars are rendered as SVG (common in Shopify themes), the fill color is set via CSS `color` or `fill`. The chosen gold must be tested in both SVG and Unicode star rendering contexts.

## Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Star color shifts between homepage and PDP — customer notices inconsistency | High (if Option C) | Medium — erodes perceived polish | Resolve to a single value (Option A or B) |
| Chosen gold looks wrong against one of the background colors in the palette | Medium | Medium — stars on `#f9f7f2` alt-bg may lack contrast | Test both golds against all 4 background colors before deciding |
| Third-party review app injects different star color | Medium | Low — CSS override resolves | Include app-override CSS in Shopify theme for star color |
| PDP hardcoded values drift further from tokens if not refactored | High (if Option C) | Medium — PDP becomes a maintenance island | If keeping both, at minimum refactor PDP to use a `--pdp-star` token |
| Designer chose `#d4af37` intentionally to pair with warm palette — overriding loses that nuance | Medium (if Option A) | Low — aesthetic preference | Document the rationale in decisions log; prototype both before finalizing |

## Decision Required From

**Architect (ChatGPT)** — Select Option A, B, or C. If the decision depends on ADR-05 (PDP text color), note the dependency and specify which combination of text color + star color is preferred.
