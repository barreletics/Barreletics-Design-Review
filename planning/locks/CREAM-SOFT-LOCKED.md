# Cream soft LOCKED — sitewide

**Confirmed:** Andrew 2026-09-14 (Help Quick Answers + sitewide)  
**Only cream:** `#faf8f6`  
**Retired forever:** `#f5f2ec` (and `#f7f5f2`, `#f8f6f4`, `#fff8f0`)

## Tokens
```
--color-warm-cream: #faf8f6;
--color-warm-cream-soft: #faf8f6;
--bg-alternate: var(--color-warm-cream-soft);
```

## Help Quick Answers
`sections/page-help.liquid` → `.page-help__grid-wrap` background `#faf8f6`.

## Guardrails
| Layer | Path |
| --- | --- |
| Letter | `planning/locks/CREAM-SOFT-LOCKED.md` |
| Machine | `sitewide.lock.json` → `tokens.cream` / `cream_bands` / `forbidden_cream_hex` |
| Scanner | `scripts/lock-scan.py` fails on forbidden cream hex in shopify-build |
| Rule | `.cursor/rules/cream-band-LOCKED.mdc` (alwaysApply) |

## Before push
`python3 scripts/lock-scan.py .` — no `#f5f2ec` in theme files.
