# Cloud handoff — Help hub (2026-08-12)

**Branch:** `finish-home-collections`  
**Theme:** M4 `187144929571` only — **NEVER push until Andrew says approved / looks good / yes**  
**Workflow:** Preview → Andrew approves → **then** one push. Local HTML ≠ done.

## Desktop status

- Desktop **stands down** on Help until AWAITING cleared on M4.
- Authority mock: `docs/Barreletics Help - Definitive-v8.html`
- Pre-push preview (working tile links): `docs/HELP-PREPUSH-PREVIEW.html`
- Type law: `planning/help-family-type-law.md`
- Full prompt: `planning/cloud-prompt-help-family-2026-08-12.md`

## Cloud first job (Help hub only)

1. Confirm `page-help.liquid` + `page.help.json` match Help **v8** (tiles + → · no taxonomy eyebrows · support H1).
2. Ensure Admin page handle **`help`**, template suffix **`help`** (create if 404).
3. Show Andrew a preview (**theme dev** or confirm PREPUSH mock) — **do not push**.
4. After Andrew says **approved / looks good / yes** → **one** `shopify theme push --theme 187144929571` from `shopify-build/`.
5. Verify `https://barreletics.myshopify.com/pages/help?preview_theme_id=187144929571` = 200.
6. Status → AWAITING ANDREW · stop.

Optional same push (already in repo, type-law): `page-returns` · `page-contact` · `page-size-guide` · `main-page` — only if Andrew’s approve covers Help-family type pass.

## Destinations (theme hrefs after push)

| Tile | Path |
|---|---|
| FAQ | `/pages/faq` |
| Shipping & returns | `/pages/returns` |
| Start a return | `/pages/returns-portal` |
| Size chart | `/pages/performance-skins-size-chart` |
| Contact | `/pages/contact-us-form` |

No Track Order. No Returns Portal mock. No Contact Definitive-v1.

## Files Cloud may touch

```
shopify-build/sections/page-help.liquid
shopify-build/templates/page.help.json
shopify-build/sections/page-returns.liquid
shopify-build/sections/page-contact.liquid
shopify-build/sections/page-size-guide.liquid
shopify-build/sections/main-page.liquid
shopify-build/templates/page.returns.json
planning/page-template-registry.md
planning/sprint-queue.md
planning/m4-section-freeze.md   # forward note only if Help page freezes
```

## LOCKED — do not touch

From `planning/m4-section-freeze.md` + anti-revert:

- `footer.liquid` / footer-group · Join the list (NO 10%)
- `pdp-buy-box.liquid` · `product.json` · `product.open-sole.json` · `product.outdoor.json`
- `value-strip.liquid` (under-ATC / 4-up strip)
- `home-juicer.liquid` · Instagram
- `proof-numbers.liquid`
- `templates/index.json` spine
- Header nav #2 / `header-group` (unless Help link letter only — prefer registry note)
- Locked mocks in place: `Definitive-v16.html` · `Definitive-v19.html` · Help v3 Locked HTML · FAQ v4 Locked HTML
- One-off buy-box lock surfaces without letter

## Forbidden

- Push before Andrew approve
- Giving `127.0.0.1` as the final “done” link after push was requested
- Help v7 hairline · Track Order on hub · fake portal
- `git restore` / silent revert
