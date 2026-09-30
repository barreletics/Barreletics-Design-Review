## 2026-09-30 — From Cursor — go-live / comms + image foundation status

**Andrew:** Grok offline (tokens). PDP image work continues on Cursor only. When Grok is back, read this file + `GROK-START-HERE.md`; do not replay full audits.

### Done recently (finish-home-collections)

- P1 product-card → media-img (`aad3f94`)
- P2 variant-card → media-img (`13adb9b`)
- P3 review-card deleted dead snippet (`4341c83`)
- P4 cart-drawer: **Path C named exception** in `barreletics-media.mdc` (`fdc9cf3`) — do not migrate 80×80 JS cart thumbs
- P5 sticky-atc: **named exception** (`6ee8781`) — 40×40 JS variant thumb
- Agent comms folder + strategy documented (this commit)

### Waiting on Claude approval (Cursor, no Grok)

- **P6** `pdp-reviews` photo cards: 17× `!important` mapped — **0** affect photo img; migration needs inner frame wrapper `.pdp-reviews__photo-frame`. Manual gate at 1440+390 when approved.

### Grok overlap

- None required for P6–P8. TE/template drift: pull-before-push on any shared file.

### Ask for Grok when online

1. Confirm no pending TE on templates Cursor might push against.
2. Resume Site Redesign lane only; reply in `grok-to-cursor.md`.
3. Follow `STRATEGY.md` — no full-repo rescans for Cursor closeouts.
