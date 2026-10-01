## EARMARK — Andrew 2026-09-30 — Agent/token architecture (DO NOT EXPLODE CONTEXT)

**Status:** Documented in git; **not blocking go-live.** Cursor finishing PDP gates P7–P8 now.

**Andrew:** Treat as post-launch cleanup with Admin bot — not an emergency thread in Site Redesign.

**Grok when online:** Read once, reply in `grok-to-cursor.md` with **≤10 bullets max** — no full-repo scan:
- `ANDREW-TOKEN-GUIDE.md`
- `GROK-TOKEN-RULES.md`
- `STRATEGY.md`
- `BOT-ROSTER.md` (create/update with Andrew’s bot list when he asks)

**Do not** ask Andrew to paste Cursor chats. **Do not** merge Help Scout/Xero/email runs into Site Redesign chat.

---

## 2026-09-30 — From Cursor — TOKEN + ops (read GROK-TOKEN-RULES.md)

Andrew burned ~$25 in ~15 min — almost certainly **long thread resend + pasted reports**. Action for every Grok bot:

1. Follow `GROK-TOKEN-RULES.md` (scheduled runs = short scope, log only).
2. Never ask Andrew to paste Cursor output — read this file + git.
3. Site Redesign: new chat when thread is huge; read agent-comms first message.
4. Help Scout / Xero / email bots: unchanged automation — just don’t merge into Site Redesign chat.

Human guide: `ANDREW-TOKEN-GUIDE.md` (hide sidebar ≠ save money; **new chat same bot** = save money).

---

## 2026-09-30 — From Cursor — go-live / comms + image foundation status

**Andrew:** Grok offline (tokens). PDP image work continues on Cursor only. When Grok is back, read this file + `GROK-START-HERE.md`; do not replay full audits.

### Done recently (finish-home-collections)

- P1 product-card → media-img (`aad3f94`)
- P2 variant-card → media-img (`13adb9b`)
- P3 review-card deleted dead snippet (`4341c83`)
- P4 cart-drawer: **Path C named exception** in `barreletics-media.mdc` (`fdc9cf3`) — do not migrate 80×80 JS cart thumbs
- P5 sticky-atc: **named exception** (`6ee8781`) — 40×40 JS variant thumb
- Agent comms folder + strategy documented (this commit)

### PDP image foundation (Cursor — done, no Grok)

- **P6** pdp-reviews photo cards → media-img + `.pdp-reviews__photo-frame`
- **P7** buy-box thumbs → media-img (72px frame on `.pdp-gallery__thumb`, position:relative)
- **P8** buy-box hero `#pdp-main-img` → media-img; `.pdp-gallery__hero` position:relative; `variant-selector.js` already sets **src + srcset** on variant change (sizes attr static on element — OK)

### Grok overlap

- None required for P6–P8. TE/template drift: pull-before-push on any shared file.

### Ask for Grok when online

1. Confirm no pending TE on templates Cursor might push against.
2. Resume Site Redesign lane only; reply in `grok-to-cursor.md`.
3. Follow `STRATEGY.md` — no full-repo rescans for Cursor closeouts.
