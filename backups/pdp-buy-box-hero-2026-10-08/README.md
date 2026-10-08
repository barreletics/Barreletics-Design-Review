# pdp-buy-box.liquid hero backups (2026-10-08)

Draft theme `187144929571` only. Never live.

| File | When | md5 |
|---|---|---|
| `pdp-buy-box.pre-4x5-square.liquid` | Before 4:5 hybrid (1:1 cover frame) | `7035ea0d5a9992ee82d4c6e45810fc07` |
| `pdp-buy-box.pre-apparel-cover.liquid` | After 4:5 hybrid, before apparel cover | `2e7f9c7185e86bcd682c16122859b4d5` |

Revert to this file (no `--force`):

```
cp backups/pdp-buy-box-hero-2026-10-08/pdp-buy-box.pre-apparel-cover.liquid shopify-build/sections/pdp-buy-box.liquid
shopify theme push --theme 187144929571 --path shopify-build --only sections/pdp-buy-box.liquid --nodelete
```

To restore the pre-4:5 square frame, use `pdp-buy-box.pre-4x5-square.liquid` instead.
