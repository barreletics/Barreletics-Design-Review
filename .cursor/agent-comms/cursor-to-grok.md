## 2026-10-02 — From Cursor (Grok 4.6) — TE live-preview + Press/nav + go-live slider pass

**Read this block. Do not re-scan the theme. Do not ask Andrew to paste the Cursor thread.**

**Theme:** draft `187144929571` only. Never live `185687998755`.
**Git:** `c0c0564` on `cursor/apparel-pdps-c982`
**File backup of current M4:** `backups/m4-qa-2026-10-02-pre-slider-hook/` (Shopify Theme Library is at the **20-theme cap** — no new unpublished copy).

### The issue Andrew hit

Theme Editor sliders / selects / checkboxes **do not move the page until Save**. He is on the page (Home, then Closed Sole). Not a wrong-tab bug. Save also used to write the last page he was on (Press) — treat that as a separate Admin/TE path issue; the **visual** bug is in our Liquid.

### What Cursor found

Shopify TE live-patches **only** `{% style %}` that contains `{{ section.settings.id }}`.

Save-only (broken live preview):
- inline `style="--var: {{ assign }}"`
- raw `<style>` that uses Liquid assigns
- HTML classes / `{% if %}` that change layout (reviews 3 vs 4 cols)

**Inventory (looked only, no mass edit):** almost every range slider in `shopify-build/sections/` is Save-only. Biggest: **`fifty-fifty.liquid`** — 16 sliders, every PDP + Home.

Already have a `{% style %}` hook (partial):
- `problem-section` — **Desktop min height** only
- `pdp-reviews` — photo show / desk 3|4 / rows / phone 1|2 + text-cards show
- `press-row` — desktop height
- `split-hero` / `visual-mosaic` — have `{% style %}` but most values are **assigns**, not `{{ section.settings.id }}` — may still need Save

### How the first ones were fixed (recipe — copy this)

Dual-write. Do **not** delete inline / `<style>`. Do **not** change schema, JSON, defaults, crops, or copy.

```liquid
{% style %}
  #shopify-section-{{ section.id }} {
    --pr-desk-media-min: {{ section.settings.min_height }}px;
  }
{% endstyle %}
```

Hard rules:
- `{{ section.settings.THE_ID }}` in the `{% style %}` block — **not** an assign
- **No** `{% render %}` inside `{% style %}` (broke fifty-fifty / problem when we tried; those two were reverted to `<style>`)
- One `.liquid` file per turn. Push that file only. He hard-refresh + drag, **no Save**. He says approved. Next file.

**Problem (Home “Never slip in Chair Pose”):** `sections/problem-section.liquid` — Desktop min height live. Leftover Save-only: phone photo height, space above bullets.

**Reviews (Closed Sole):** `sections/pdp-reviews.liquid` — photo cards were Liquid `{% if %}` + classes; TE did nothing. Now always render photo blocks (if they exist), show/cols/rows/phone via `{% style %}` CSS vars. Closed JSON still `show_photo_cards: false` (signed text-only). 2 rows needs more Photo review blocks (Closed has 3). Do not turn photos on in `product.json`.

### Andrew: fix ALL remaining sections before go-live

Safe order (one file, then stop):
1. **`fifty-fifty.liquid`** — wait for Andrew to say `go 50/50` if not already said in **his** Grok message
2. Problem leftovers (phone height, bullet gap)
3. `fullbleed-statement` → `pdp-sock-math` → `pdp-features`
4. About hero / About split → Press feature / press cards → Coperni story / crosslink / collab-hero
5. Collection hero, then shared insets last

**Do not touch unless Andrew names them in THAT message:** `pdp-buy-box`, footer, `home-juicer`, `proof-numbers`, `value-strip`, `product.json`, `index.json`. Chair Pose lock values stay (`chair-pose-yellow-fit.mdc` — COVER · 100 · P5A4949 · mmh 360). Never push Home `index.json` over TE.

### Other updates this session (already on draft + in `c0c0564`)

**Press + nav (Andrew: go):**
- Header `m4-menu`: **About Us** after Journal. Children: Our Story + Press
- Help dropdown: support only — FAQ · Contact · Returns (About Us **out**)
- Footer Learn: About Us · Press · Journal (+ existing). `footer.liquid` fallbacks include Press
- New page `/pages/press` = Home `press-row` (video + 4 cards), template `page.press.json`, handle `press`
- Docs forward: `planning/navigation-menu-spec.md`, `page-template-registry.md`, freeze banner 2026-10-02
- Live `Main menu` untouched

**Apparel:** yoga pants + v-neck templates on draft; Andrew said they look great. Buy-box liquid **not** touched.

**chrome.js:** scoped `shopify:section:load` video kick (did **not** fix sliders; leave it).

### Ask for Grok

1. New chat. Read this + `GROK-START-HERE.md`. Reply in `grok-to-cursor.md` (≤10 bullets).
2. Continue the `{% style %}` dual-write pass for go-live. One section per turn.
3. Do not restore. Do not batch-edit. Do not invent a shared snippet inside `{% style %}`.

---

## 2026-09-30 — From Cursor (Claude) — handoff (Andrew going to Claude)

**Read this file + `STATUS.md` + `CURSOR-TOUCHED-MAP.md`.** Image foundation P1–P8 on draft `187144929571`; gallery hotfix `b0d93c5`. Agent/token docs in `agent-comms/` — post-launch, not blocking go-live.

**Inventory restock (same evening):** Andrew saw draft preview out of sync with live after Admin restock. **Not caused by Cursor theme code** (no inventory logic changed). Andrew **found the issue** (Admin/ops — not M4 liquid); live was correct. **Andrew:** add one-line root cause to `STATUS.md` when you paste to Claude if you want it in canon.

**Claude — what’s next (Cursor lane):**
1. Andrew sign-off: draft PDP thumbs + swatch after `b0d93c5` (hard refresh on myshopify preview).
2. Go-live decision: publish draft M4 QA vs diff review — Andrew only; never live theme without explicit message.
3. Optional backlog: collection-hero media-img exception already exists; `recently-viewed` keep/delete; Home Open/Closed tab flash if still reported (variant-grid, not buy-box).
4. **Stop** new PDP buy-box edits unless coordinated with Grok (same file).

**Grok when back:** `GROK-START-HERE.md` + `GROK-TOKEN-RULES.md` — reply in `grok-to-cursor.md` only; TE/templates lane; do not re-audit P1–P8.

---

## 2026-09-30 — From Cursor (Claude) — PDP gallery hotfix `b0d93c5`

**Andrew reported:** PDP thumbs dead + large image flash on color/swatch change (after P7/P8 media-img).

**Root cause (not Grok regression on sizes/kit/copy):**
1. **Thumbs:** `.pdp-gallery__thumb` had `data-thumb-src` but **no JS** in theme repo to swap `#pdp-main-img` — clicks did nothing (predates or exposed by P7/P8; not fixed by reverting markup alone).
2. **Flash:** `variant-selector.js` set `mainImg.src = variant.featured_image.src` (full-res) while srcset was sized — brief oversized decode in hero frame.

**Fix (draft 187144929571 pushed):** commit `b0d93c5`
- `sections/pdp-buy-box.liquid`: inline gallery click handler (src/srcset from `data-thumb-src`, `is-active` on thumbs); `type="button"`; `.pdp-gallery__thumb .media-img { pointer-events: none }`.
- `assets/variant-selector.js`: hero `src` via `getSizedUrl(..., 800)` + 1200w in srcset (matches media-img widths).

**Lane:** Cursor only; Grok’s `pdp-buy-box` PDP logic untouched except gallery block + new script block after `variant-selector.js`.

**Claude ask:** Note for image-foundation record — P7/P8 should have included thumb-click wiring check in pre-gate (P8 JS report covered variant swap only). No revert of media-img requested unless Andrew re-tests and fails.

**Andrew:** Hard-refresh draft PDP — thumbs + swatch. If **Home** Open/Closed **tabs** still flash, that’s `variant-grid` (separate from this fix).

**Docs:** `CURSOR-TOUCHED-MAP.md` explains what P1–P8 means on storefront.

---

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
