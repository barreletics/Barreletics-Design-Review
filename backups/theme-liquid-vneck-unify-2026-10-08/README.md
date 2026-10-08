# theme.liquid backup — before tee heading-unify (2026-10-08)

Draft theme `187144929571` only. Never live.

| File | md5 |
|---|---|
| `theme.liquid.pre-vneck-unify` | `255b4ede1307197efccf0e42b0644831` |

Revert (no `--force`):

```
cp backups/theme-liquid-vneck-unify-2026-10-08/theme.liquid.pre-vneck-unify shopify-build/layout/theme.liquid
shopify theme push --theme 187144929571 --path shopify-build --only layout/theme.liquid --nodelete
```
