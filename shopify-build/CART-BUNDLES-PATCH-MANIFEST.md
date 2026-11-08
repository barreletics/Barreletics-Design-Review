# Cart + bundles — patch manifest (canonical `shopify-build`)

**Target Shopify theme role:** Nov 08 **Cart + bundles** fresh-copy DRAFT (per BOOT rule 1: canonical theme source in repo; deploy only to the DRAFT row named in `THEMES.md` — prior Oct 26 draft untouched).

**Repo state:** This patch is against `Barreletics-Design-Review` / `shopify-build` on branch `cursor/cart-bundles-theme-df3e`. Live theme on store may be ahead — **NEEDS fresh Shopify draft pull/rebase** before `shopify theme push` so unrelated home/templates/settings are not overwritten.

## Changed / added files

| File | Action |
|------|--------|
| `assets/cart-bundle-promo.js` | **ADD** — preview math + DOM update |
| `assets/cart.js` | **EDIT** — call promo after drawer render; `cart:rendered` event |
| `snippets/cart-bundle-promo.liquid` | **ADD** — promo mount points |
| `snippets/cart-bundle-promo-assets.liquid` | **ADD** — JSON config + script (once per layout) |
| `snippets/cart-drawer.liquid` | **EDIT** — insert promo + assets |
| `sections/main-cart.liquid` | **ADD** — full cart (template already referenced it) |
| `config/settings_schema.json` | **EDIT** — "Cart bundles (preview)" settings (defaults only; **do not** wholesale replace `settings_data.json`) |
| `tests/cart-bundle-promo.test.mjs` | **ADD** — Node unit tests |

**Not touched:** `settings_data.json`, index/home templates, `variant-selector.js`, announcement / 2FOR15 flows.

## Deployment requirements

1. Pull latest **Cart + bundles** draft from Shopify into `shopify-build` (or merge this branch onto that pull).
2. Theme editor: enable **Enable bundle promo messaging** only on the draft for QA.
3. Configure real pair/pants discounts in **Shopify Admin** when approved — theme messaging does not activate checkout discounts.
4. Push with `shopify theme push --theme <DRAFT_ID from THEMES.md>` only after rebase; never publish without Andrew go-live naming the theme.

## Docs source read

`barreletics/alternate-projects` @ `ca0cd8af…` (BOOT, BUILD-PLAN-MIX-MATCH-ROTATION-2026-11-07) returned **404** on this agent token — implementation follows owner-approved spec in the parent task (pair tiers, pants cap, copy, flag off default).
