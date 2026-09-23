# FAQ Background LOCKED — cream default

**Confirmed:** Andrew 2026-09-14 — control looks great; default cream; lock it.

## Law
1. TE control **Background** on `collection-faq` and `page-faq`: **Cream (`#faf8f6`)** or **White**.
2. **Default = cream** (schema + templates).
3. Cream = soft `#faf8f6` only (sitewide cream lock). Never darker.
4. White only when explicitly set for that page.

## Intentional white exceptions (keep)
| Template | Section |
| --- | --- |
| `collection.apparel.json` | `collection-faq` |
| `page.best-grippy-socks.json` | `collection-faq` |

All PDP `collection-faq` + Shop All + `/pages/faq` → cream unless Andrew letters a white exception.

## Files
- `sections/collection-faq.liquid` / `page-faq.liquid` — schema select
- `snippets/faq-accordion.liquid` — `.faq--cream` / `.faq--white`
- Machine: `sitewide.lock.json` → `faq_background`

## Never
- Hardcode FAQ bg without the TE select
- Dark cream `#f5f2ec`
- Flip defaults back to white sitewide
