# Press spacing refine — QA & deploy (draft theme `187144929571`)

## Intent

Keep the existing **Press row** layout unchanged: large Coperni hero video on the left, four smaller cards in a 2×2 stack on the right. **Only** increase gutters between those cards so the band breathes (see mock `mocks/press-real-layout-air.png`).

No cream bands added, no scan/text card conversion, no fifty-fifty or other section edits.

## Files to push (Shopify CLI)

From repo root, with store auth and **draft theme only**:

```bash
shopify theme push \
  --theme 187144929571 \
  --only sections/press-row.liquid
```

Path on disk: `shopify-build/sections/press-row.liquid` → theme path `sections/press-row.liquid`.

## What changed

| Location | Before | After |
|----------|--------|-------|
| `.press-row__grid` desktop/tablet gutter | `10px` | `24px` |
| `.press-row--m-grid .press-row__grid` (phone two-by-two) | `10px` | `24px` |

Caperni video overscale/cover behavior and magazine **contain** rules on cards are untouched.

## Visual QA (after push)

1. Home → **Press** section: Coperni video still fills left column; four cards still 2×2 on the right.
2. Gutter between hero and right column is visibly wider; vertical gaps between the four cards match.
3. INTERNI / contain cards still show full page art (no crop regression).
4. Phone: stack and two-by-two layouts inherit the same 24px card gutters where the grid applies.

## Revert

**Backup (pre-refine, `gap: 10px`, synced from `finish-home-collections`):**

`shopify-build/sections/archive/press-row.liquid.bak-gap10-2026-10-05`

```bash
cp shopify-build/sections/archive/press-row.liquid.bak-gap10-2026-10-05 shopify-build/sections/press-row.liquid
shopify theme push --theme 187144929571 --only sections/press-row.liquid
```

Or restore the two lines in `press-row.liquid` to `gap: 10px` (desktop grid ~line 228, mobile grid ~line 416) and push again.

## Note on `press-home` / `press-cards`

Home JSON may still include a disabled `press-home` section (`type: press-cards`). **Live home press band uses `press-row`.** This change does not modify `press-cards.liquid` or `templates/index.json`.
