# Cart + bundles — deployment apply (HOLD until parent parity)

**Status:** `HOLD_SHOPIFY_UPLOAD` — parent executor must finish fresh `theme pull` + archive/parity on **DRAFT row (Nov 08 · Cart + bundles)** from `source-docs/THEMES.md` before any push.

**BOOT rule 1 (cited):** Numeric theme IDs appear **only** in `THEMES.md`. This file references **DRAFT row** / **LIVE row** — not IDs in commit messages or handoffs.

**Andrew authorization:** Direct “put it in the draft” (~1:29 PM ET 2026-11-08) after read-only confirmation. **No publish, no test orders, no Admin discounts, no live price changes** in this payload.

## 0. Preconditions (parent Mac, Shopify CLI 3.94.3)

1. `cd` to **fresh pull** of Nov08 draft theme (not stale Design Review `shopify-build/` copy alone).
2. Confirm theme role = **DRAFT row** in Admin matches `source-docs/THEMES.md`.
3. Archive/parity checksum parent bundle before merge.
4. Rebase **hunks** below onto pulled files (do **not** replace entire `settings_schema.json` or `settings_data.json` from repo).

## 1. Deterministic verification (before push)

From Design Review repo (implementation source):

```bash
cd shopify-build && npm run test:cart-bundle
```

Expect **11/11** pass (math + variant resolution).

## 2. Files — `shopify theme push --only` (minimal)

**Always new on target (safe full file push):**

```
assets/cart-bundle-promo.js
assets/cart-bundle-promo.css
snippets/cart-bundle-promo-config.liquid
```

**Add only if missing on fresh pull (else merge hunk):**

```
sections/main-cart.liquid
```

**Must merge with target baseline (see `hunks/` in payload):**

```
assets/cart.js
snippets/cart-drawer.liquid
layout/theme.liquid
sections/pdp-buy-box.liquid
config/settings_schema.json
```

`pdp-buy-box.liquid`: change is **removing duplicate** `cart.js` script tag (cart loads once from `theme.liquid`).

## 3. One-shot push command shape (after HOLD cleared)

Replace `THEME_ID` with **DRAFT row ID from THEMES.md** (parent already has it).

```bash
shopify theme push \
  --store barreletics \
  --theme THEME_ID \
  --only assets/cart-bundle-promo.js \
  --only assets/cart-bundle-promo.css \
  --only snippets/cart-bundle-promo-config.liquid \
  --only assets/cart.js \
  --only snippets/cart-drawer.liquid \
  --only layout/theme.liquid \
  --only sections/pdp-buy-box.liquid \
  --only sections/main-cart.liquid \
  --only config/settings_schema.json \
  --nodelete
```

Do **not** pass `--no-input` (unsupported on 3.94.3). Do **not** include `config/settings_data.json`.

## 4. Enable draft preview only (theme editor — no wholesale settings_data)

After push, in **Theme settings → Cart bundle preview (Nov08)**:

| Setting | Draft preview value | Notes |
|---------|---------------------|--------|
| Enable cart bundle preview | **Off** until smoke pass, then **On** | Default off in schema |
| Pair promo mode | `future_tiers` or `live_2for15` | Match promo Andrew wants visible in preview |
| Pants product handle | `lightly-padded-knee-yoga-pant-black` | See `pants-product-resolution.json` |
| Pants preview % / proposed cents | `35` / `9800` | Preview math only; live price **$89** unchanged |
| Pants default variant ID | **leave 0** | Forces size/color pickers via `/products/{handle}.js` |

**No** Shopify automatic discount creation in this step.

## 5. Smoke on draft preview URL

1. Add 2× Closed Sole Performance Skins → open cart drawer.
2. Confirm: nudge, green savings line, pants block, **size selects**, **Add yoga pants** disabled until size chosen.
3. Add pant → drawer qty/remove still works; subtotal still Shopify live prices; estimated row labeled preview.
4. Full cart `/cart` — same promo block + checkout form unchanged.
5. Flag **off** → no promo panel; cart behaves as before merge.

## 6. Explicit non-goals (this payload)

- LIVE row / publish
- `settings_data.json` replace
- Admin discount / price rules
- Claiming standalone HTML QA = Shopify render

## 7. Pants product resolution

See `pants-product-resolution.json` (public JSON 2026-11-08). Cart add uses **selected variant ID** after customer picks size (and color if shown). Fallback link: product page.
