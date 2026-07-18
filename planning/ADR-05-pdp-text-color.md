# ADR-05: PDP Text Color #1c1916 vs #050505 (HIGH-002)

**Status:** UNRESOLVED — Awaiting Architect decision  
**Severity:** High  
**Created:** 2026-07-13

---

## Problem

The PDP spec and the matured homepage override both use `#1c1916` (warm dark brown) for body text, while the base design system token is `#050505` (cool near-black). A developer following base tokens produces a visibly different result than one following the PDP spec or matured homepage. The question is whether the system token should be updated, the PDP should reference the override mechanism, or the divergence is intentional.

## Evidence

| Source | Value | Exact location |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` line 20 | `#050505` | Color Palette: "Text (primary): #050505" |
| `docs/03-DESIGN-SYSTEM.md` line 374 | `#050505` | Research Bible core rule: "Colors: text=#050505" |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` line 42 | `--br-text: #050505` | Base CSS custom property definition |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` line 4210 | `--br-text: #1c1916` | `[data-matured="on"]` override block |
| `docs/05-PDP-ARCHITECTURE.md` line 24 | `body { color: #1c1916 }` | PDP body element — hardcoded, no token reference |
| `docs/05-PDP-ARCHITECTURE.md` line 42 | `color: #1c1916` | `.pdp-buy__name` heading color |
| `docs/05-PDP-ARCHITECTURE.md` line 44 | `color: #1c1916` | `.pdp-buy__price-now` price color |
| `docs/05-PDP-ARCHITECTURE.md` line 56 | `color: #1c1916` | `.pdp-section__title` color |

The PDP spec uses `#1c1916` in at least 8 CSS declarations (lines 24, 25, 42, 44, 46, 51, 56, 73) — it is the dominant ink color throughout the PDP, hardcoded directly rather than via `var(--br-text)`.

## Source Files

- `docs/04-COMPONENT-LIBRARY.md` — line 20
- `docs/03-DESIGN-SYSTEM.md` — line 374
- `docs/06-HOMEPAGE-ARCHITECTURE.md` — lines 42, 4210
- `docs/05-PDP-ARCHITECTURE.md` — lines 24, 25, 42, 44, 46, 51, 56, 73

## Line References

| File | Line(s) | What it defines |
|---|---|---|
| `docs/04-COMPONENT-LIBRARY.md` | 20 | System color palette — primary text `#050505` |
| `docs/03-DESIGN-SYSTEM.md` | 374 | Research Bible — "text=#050505" |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` | 42 | Base token `--br-text: #050505` |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` | 4206–4210 | Matured override `[data-matured="on"] { --br-text: #1c1916 }` |
| `docs/05-PDP-ARCHITECTURE.md` | 24 | PDP body text `color: #1c1916` (hardcoded) |
| `docs/05-PDP-ARCHITECTURE.md` | 42, 44, 56 | PDP heading, price, section title — all `#1c1916` |

## Dependencies

- **ADR-01 (Color Palette Values):** The warm-vs-neutral palette direction directly determines which ink tone is canonical.
- **ADR-07 (Star Rating Color):** Star color contrast ratios differ against `#1c1916` vs `#050505` backgrounds. `#d4af37` was likely chosen to pair with `#1c1916`.
- **Matured toggle mechanism:** The `[data-matured="on"]` attribute in `docs/06` controls the homepage override. If matured becomes permanent, the override is dead code.
- **Accessibility (WCAG):** Both values pass WCAG AA against `#ffffff`, but contrast ratios differ: `#050505` ≈ 19.5:1, `#1c1916` ≈ 15.3:1. Both are well above 4.5:1 minimum.

## Options

### Option A: Make `#1c1916` canonical everywhere — retire `#050505`

Update `--br-text` base token to `#1c1916`. Remove the `[data-matured="on"]` text override (it becomes the default). Update docs/04 and docs/03.

| Pros | Cons |
|---|---|
| Matches current production visual (matured homepage + PDP) | Permanently discards the cooler near-black option |
| Single source of truth — no override needed | Requires updating 3 source documents (docs/03, docs/04, docs/06 base token) |
| Aligns PDP and homepage without architectural changes | If matured direction is ever rolled back, token must change again |
| Warmer ink suits an athletic/lifestyle brand | Departs from the Research Bible original specification |

### Option B: Keep `#050505` as base token — formalize `#1c1916` as matured override

The `[data-matured="on"]` mechanism is the intended architectural solution. PDP should reference `var(--br-text)` instead of hardcoding `#1c1916`, and the PDP page should set `data-matured="on"`.

| Pros | Cons |
|---|---|
| Preserves the original token for non-matured contexts | PDP currently hardcodes `#1c1916` in 8+ declarations — significant refactoring |
| Clean architectural separation (base vs override) | Two "valid" text colors create developer confusion |
| Allows rollback to `#050505` if matured is reverted | Developers must understand the matured toggle to use the correct color |
| Research Bible and Component Library remain unchanged | Every new PDP element must remember to use `var(--br-text)` under `data-matured` |

### Option C: Accept divergence — PDP intentionally uses warmer ink

PDP uses `#1c1916` by design to complement product photography. Homepage uses `#050505` base with matured override. Document that page types have different text warmth.

| Pros | Cons |
|---|---|
| No source documents need to change | "What color is body text?" has no single answer |
| Respects each page designer's contextual intent | Inconsistent text color across page types in the live store |
| PDP's warmer tone suits its product photography context | Harder to maintain — any new page type must decide which ink to use |
| Least disruption to existing specs | A shared component (e.g., footer) used on both pages shows different text colors |

## Repository Impact

- **Option A:** Update `docs/04-COMPONENT-LIBRARY.md` line 20, `docs/03-DESIGN-SYSTEM.md` line 374, `docs/06-HOMEPAGE-ARCHITECTURE.md` line 42 (base token). Remove or simplify the `[data-matured="on"]` text override at line 4210.
- **Option B:** Refactor `docs/05-PDP-ARCHITECTURE.md` — replace 8+ hardcoded `#1c1916` values with `var(--br-text)` and add `data-matured="on"` to PDP wrapper. No changes to docs/03 or docs/04.
- **Option C:** Add a note to `docs/10-DECISIONS.md` documenting the intentional divergence. No file changes.
- **All options:** Record decision in `docs/10-DECISIONS.md`.

## Shopify Impact

- A Shopify developer building theme sections encounters `--br-text` in the CSS custom properties. The base value is `#050505`. If they build the PDP following the PDP spec, they hardcode `#1c1916` and bypass the token system entirely.
- If a shared component (navigation, footer, newsletter) is placed on both the homepage and PDP, its text color will differ unless the matured override is applied consistently.
- Shopify's Online Store 2.0 theme architecture uses `settings_schema.json` for color settings. If `#050505` is in the schema but `#1c1916` is in the CSS, the theme editor shows the wrong color to the merchant.
- The `[data-matured="on"]` toggle has no Shopify theme equivalent unless it's wired to a theme setting or metafield — the mechanism itself needs implementation planning.

## Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Developer builds PDP with `#050505` (following system token) — mismatches approved mock | High | Medium — visible warm/cool shift vs design intent | Resolve before PDP build begins |
| Shared components render different text colors on different pages | Medium | High — navigation/footer color shifts between pages | Ensure all page wrappers use the same token resolution |
| Matured direction is rolled back after `#050505` is retired (Option A) | Low | Medium — requires token revert | Keep `#050505` documented as the pre-matured value in decisions log |
| PDP hardcoded values drift further from tokens over time (Option C) | High | Medium — PDP becomes an unmaintainable island | If Option C, document explicitly and flag in code reviews |
| Accessibility audit flags inconsistent contrast ratios | Low | Low — both pass WCAG AA by wide margin | Document both contrast ratios in the decision record |

## Decision Required From

**Architect (ChatGPT)** — Select Option A, B, or C. If B, specify whether the `[data-matured="on"]` toggle should be permanent or remain a feature flag.
