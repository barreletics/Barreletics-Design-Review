# PDP Working Entry — Barreletics

> ## ⛔ LOCKED — NEVER OVERWRITE v16 / v19 mocks in place
> **Prior fingerprint:** `docs/Barreletics PDP - Definitive-v16.html` @ git **`691f03b`**  
> **Current mock:** `docs/Barreletics PDP - Definitive-v19.html`  
> **Draft QA match:** theme **`187144929571`** ↔ `shopify-build/templates/product.json`  
> **Rule:** `.cursor/rules/pdp-hub-lock.mdc`  
> **Andrew letter:** 2026-08-01 — lock current PDP composition (draft + repo `product.json`).

**Status:** **v19 · Locked** (current) · **v16 · Locked / APPROVED** (prior fingerprint)  
**Current authority:** **`Definitive-v19.html`** mock **PLUS** draft-matched `product*.json` spines on theme **`187144929571`**.  
**2026-08-08 night LOCK — proportions (PDP only):** fifty-fifty **560** / pad **80** / mobile media **320** · fullbleeds **80vh / 60vh** · Open badge **rust** · Closed/Outdoor **charcoal** · buy-box type left as built (18 / lede 34–44 / price 36) · city FAQs last · **not sitewide** (Home fifty-fifty stays 640).  
**Prior iterations:** v18 (do not overwrite) · v17 · TypeOS-236a001 · July 17 — not authority  
**New experiments:** new version files only. Do **not** edit locked v16 or v19 HTML in place without Andrew letter.

**Open prior v16:** https://htmlpreview.github.io/?https://raw.githubusercontent.com/barreletics/Barreletics-Design-Review/691f03b/docs/Barreletics%20PDP%20-%20Definitive-v16.html  
**Open current mock:** `docs/Barreletics PDP - Definitive-v19.html`  
**Hub:** `docs/index.html` → Shop → **PDP v19 · Locked**  
**Shopify draft QA:** `https://barreletics.myshopify.com?preview_theme_id=187144929571` — push only when Andrew names theme ID  
**Spec:** `specs/frozen/pdp.md` · Freeze: `planning/m4-section-freeze.md`

## Which product each template serves — updated 2026-08-08 (Andrew CURRENT MESSAGE)

> **Andrew, 2026-08-08:** *"no make the existing pdp page the closed sole and change the open sole.
> we probably want to keep secure in every hold on both for the title?"*
>
> Freeze wording below is preserved as dated history. Current message wins; this registry moves
> **forward**, not back. **The spine order did not change** — this is a product-identity change only.

| Product | Handle | Template | Notes |
|---|---|---|---|
| Studio Performance Skin — **Closed Sole** | `best-reformer-pilates-legree-workout-shoes` | **`templates/product.json`** (the refined v19 spine) | Default product template. Badge = Closed Sole / charcoal. |
| Studio Performance Skin — **Open Sole** | `studio-performance-skin-footwear` | **`templates/product.open-sole.json`** | Badge = Open Sole / **rust** `#c45c3f` (LOCKED). |
| Grippy Water Shoes | `aquatic-performance-skins` | `templates/product.outdoor.json` | Unchanged, out of scope for this pass. |

**Buy-box lede is now identical on both sole pages** — *"Secure in every hold. / No sliding. No
resets."* (approved inventory, Problem/Solution). Differentiation lives in the badge, the short
description, features, the split, sock math, the review rail, imagery and the FAQ.

**Andrew's Admin step (cannot be done from the repo):** template assignment is per-product in
Shopify Admin → Product → Online store → Theme template. Set Open Sole to `product.open-sole`;
leave Closed Sole on **Default product**. Before 2026-08-08 the previous variant template was named
`product.closed-sole` — if that was ever selected on a product it no longer exists and must be
re-pointed.

Decision record: `planning/10-decision-log.md` → **D-049**. Freeze: `planning/m4-section-freeze.md`.

## Locked spine (`product.json` `order`) — 2026-08-01 (unchanged by the 2026-08-08 swap)

`pdp-buy-box` → `value-strip` → `pdp-features` → `disciplines` → `fifty-fifty-*` → `variant-grid` → `fifty-fifty-lifestyle` (quote) → `fullbleed-statement` (**TRANSFORM**) → `pdp-sock-math` (compact) → `fullbleed-lifestyle` (**media-only wow**) → `fifty-fifty-commit` → **`pdp-reviews`** (hybrid) → `fifty-fifty-numbers` → `guarantee-band` → `home-juicer` → `collection-faq` (FAQ+GEO · cities last) → `pdp-sticky-atc`

## Locked compositions (v19 + 2026-08-08 proportions)

1. **Trust architecture** — under ATC empty · 4-up strip · accordion policy · no page `studio-trust`
2. **Purchase stack** — living buy-box type · kit · badge Open=rust / Closed=charcoal · trust = Trusted by 1,000+ Instructors · H1 no sole dash
3. **Proportions (PDP only)** — fifty-fifty **560** · fullbleed **80/60** · gallery 1:1 · thumbs 72 — **Home stays 640**
4. **Variants 4×** — under Quick Add · LE/Sold Out badges required
5. **Reviews** — hybrid **`pdp-reviews`** (3 photo + 6 text)
6. **FAQ + GEO** — `collection-faq` · city items last
7. **Juicer** — after guarantee / before FAQ
8. **Footer** — Join the list (NO 10%) · no page newsletter

## Prior (v18)

v18 had ✓ Ships under ATC — superseded by v19 Alo trust split. File kept as prior; do not overwrite.

## Next

1. Visual QA on draft **`187144929571`** after push  
2. Admin: assign Open Sole → `product.open-sole` template  
3. Tweaks only when Andrew directs — do not invent  
