# Type OS global audit — 2026-07-31

**Authority:** `planning/m4-type-hierarchy.md` + `shopify-build/assets/design-tokens.css` (SETTLED)  
**Scope:** Align section CSS to Type OS tokens/classes. No redesign.

## Root cause

Sections had **local clamps + weight 400 `!important`** that overrode SETTLED roles (Display 500 / Standard 600 / Statement 500 / Hero 700). Product/features also used oversized `strong` and 26px/bold card titles outside H3.

## Fixed (token/class alignment)

| Area | Drift | Fix |
|------|--------|-----|
| Tokens | Had been weakened earlier | Restored SETTLED scale in `design-tokens.css` |
| PDP buy box | SEO title on hero scale; lede forced 400 | H3 product title; statement lede; lede body tokens |
| PDP features | Title `strong` → huge italic; cards 26/700 | Standard title; H3 cards; label/body tokens |
| Disciplines / problem / reviews / guarantee | Local 28–40 / 400 fights | Defer to `.h2-display` / `.h2-standard` / `.type-statement` |
| Variant grid / fifty-fifty | Wrong fallbacks (28–36 / 400) | SETTLED `--type-section-*` / `--type-h2-display-*` |
| Statement / fullbleed | Oversize / 400 | Statement tokens |
| Home UGC / juicer | Title clamp 400; juicer as Display | Standard class + no local clamp |
| Footer Join / Trusted | Local clamps | Section / statement tokens |
| Studio trust | Local clamp 400 | `.type-statement` |
| Sock math | Mobile headline → `--text-7xl` | Removed; sub → lede tokens |

## Left alone (out of Type OS marketing spine)

- `collab-hero` (intentional Cormorant campaign treatment)
- UI chrome (nav, tabs, price digits, badges)
- Sock-math price display figures (data display, not heading roles)

## Preview

Push only when Andrew names draft theme ID (M4 Visual QA `187144929571`).
