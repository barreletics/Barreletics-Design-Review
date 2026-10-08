# theme.liquid backup — before narrowing tee/yoga unify (2026-10-08)

Draft `187144929571` only.

| File | md5 |
|---|---|
| `theme.liquid.pre-narrow` | `6a4abeae40ea119915f0b09b0e1d7c64` |

Revert:

```
cp backups/theme-liquid-narrow-unify-2026-10-08/theme.liquid.pre-narrow shopify-build/layout/theme.liquid
shopify theme push --theme 187144929571 --path shopify-build --only layout/theme.liquid --nodelete
```
