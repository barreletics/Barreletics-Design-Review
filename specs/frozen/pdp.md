# Frozen Spec — PDP

---
status: Closed PDP SIGNED 2026-08-16 · v19 Locked lineage · proportions LOCKED 2026-08-08 night · v16 Locked prior
surface: Product (`templates/product.json` Closed · `product.open-sole.json` · `product.outdoor.json`)
authority_mock: `docs/Barreletics PDP - Definitive-v19.html` (lineage — do not overwrite)
authority_draft: theme `187144929571` (M4 Visual QA) ↔ current `shopify-build/templates/product.json`
authority_locked_prior: `docs/Barreletics PDP - Definitive-v16.html` @ `691f03b`
updated: 2026-09-08
---

> ## ⛔ NEVER OVERWRITE LOCKED MOCK FILES
> v16 @ `691f03b` and v19 HTML = locked. New versions only.  
> Do not edit Definitive-v16 or Definitive-v19 in place without Andrew letter.  
> Do not thrash `product.json` spine without Andrew letter.  
> **QA match:** draft `187144929571` is the Shopify match for this lock.  
> **2026-08-01:** living authority for strip / fullbleeds / spine = current `product.json` (no new mock).

## Locked spine order (`product.json`)

`pdp-buy-box` → `value-strip` → `pdp-features` → `fifty-fifty-sock-era` → `variant-grid` → `fifty-fifty-lifestyle` (Kimberly quote) → `fullbleed-statement` (**TRANSFORM YOUR PRACTICE**) → `pdp-sock-math` (**editorial L**) → `fullbleed-lifestyle` (**media-only wow** · video · 80/60) → `fifty-fifty-commit` → `reviews` (`pdp-reviews`) → `fifty-fifty-numbers` (Think outside the sock!) → `guarantee-band` (centered 3-up) → `home-juicer` → `collection-faq` (FAQ+GEO) → `pdp-sticky-atc`

**Forward 2026-09-08:** Upgrade / `disciplines` **OFF** Closed. Do not restore.

**SIGNED 2026-08-16 (Closed only):** no extra wow section. Wow = `fullbleed-lifestyle` at 80vh / 60vh. Swap media in-slot only. Open / Outdoor not signed.

**Forward 2026-09-08 — Closed phone QC (M4).** Buy-box: price under lede, no hairlines, ATC = Add to Cart, Shop Pay under button. Phone thumbs: all 7 visible. 50/50 phone: photo 550, text pad **104/104 LOCKED**. Features + guarantees 48/48. TRANSFORM phone: natural collage + 32 cream. Reviews phone: 4 cards + More reviews →. Upgrade off Closed. Home unchanged. Never overwrite v16/v19 HTML.

**Absent on page (HARD):** `studio-trust` · page-level `newsletter`

## Proportions LOCKED 2026-08-08 (Andrew — PDP only, not sitewide)

> Match Definitive-v19 section/image scale. Home fifty-fifty stays **640**.

| Surface | Locked value | Notes |
|---------|--------------|-------|
| `fifty-fifty` on PDP templates | Desktop `min_height: **560**` · pad **80**. Phone: photo **550** · text pad **104/104** · no min-height box | Not Home WORKING 640. Pad is layout, not Type OS. |
| `fullbleed-statement` + lifestyle wow | Desktop **80/60**. Phone TRANSFORM = natural collage + **32 cream** | Lifestyle wow stays video/vh |
| Buy gallery | aspect **1:1** · phone **all 7 thumbs visible** · desktop 72px row | No arrow buttons |
| Buy-box type (living) | SEO title **18/600** · lede `clamp(34–44)/400` · price via `--text-4xl` (**36**) · ATC Type OS CTA | Keep as built — do not thrash to mock 15/32 unless letter |
| Sole badge | **Closed + Open + Outdoor = rust** `#c45c3f` (OWNER 2026-08-11 — never charcoal on Closed) | TE black/charcoal/blue honored |
| Trust line | `Trusted by 1,000+ Instructors` | Never invent review counts · H1 has **no** sole dash |
| FAQ cities | NYC / LA / London·Melbourne (/ Toronto) **last** under Everything you need to know | |

## Applied decisions

| ID | Choice |
|----|--------|
| DP-02 | **v19 Locked** = current full-page PDP (mock + draft spine) · **v16 Locked** prior @ `691f03b` · **2026-08-01** strip refinements · **2026-08-08** proportions + Open/Closed templates |
| DP-07 | Buy-box micro-quotes; quiet Complete the kit · Hot Pilates / Hot Yoga · `#buy` |
| DP-12 | Variant grid = Draft Home Option A chrome (meta pill · tabs · **LE/Sold Out badges required**) |
| DP-PS | **Purchase stack LOCKED** — Option A + empty under ATC + kit Option A |
| DP-4X | **Variants 4× LOCKED** — under Quick Add |
| DP-TR | **Trust split LOCKED 2026-08-01** — **4-up strip** (Made in USA · Free shipping over $150 · 30/90) · no under-ATC repeat · accordion detail · no page studio-trust · no strip links by default |
| DP-RV | **Reviews = `pdp-reviews`** live Judge.me (same spine index). Hybrid curated cards are history. |
| DP-SM | **Sock math editorial L on Closed** — v8 copy · Juicer 5986441 · 480 cover. Compact left for Coperni. |
| DP-FB | **TRANSFORM** + **lifestyle wow** at **80vh / 60vh** (proportions lock 2026-08-08) |
| DP-PROP | **PDP fifty-fifty 560 / fullbleed 80·60** — not sitewide; Home stays 640 |
| DP-LS | **Lifestyle = fifty-fifty quote** · **Numbers = Think outside the sock!** statement |
| DP-GQ | **Guarantee centered 3-up** |
| DP-FAQ | **FAQ + GEO merged in `collection-faq`** · city GEO last |
| DP-JG | **`home-juicer` on PDP** after guarantee / before FAQ |
| DP-NL | **No page newsletter** — footer Join the list only (NO 10%) |

## Trust split — LOCKED 2026-08-01 (current `product.json`)

- **Authority:** `product.json` `value-strip` / buy-box accordion (v19 mock = lineage; strip labels follow Shopify spine)
- **Value strip (scan · 4-up):** Made in USA · Free shipping over $150 · 30-day returns · 90-day warranty
- **Strip links:** none by default
- **Under ATC:** nothing (`show_trust_row: false`)
- **Accordion (detail):** Description · Care · Shipping · 30-day returns + 90-day warranty
- **Shipping accordion copy:** Complimentary shipping on orders over $150. Orders ship within 1–2 business days. Standard delivery 3–5 business days; express 1–2 business days available at checkout.
- **Do not** reintroduce ✓ ships/30/90 under ATC, Non-toxic/latex/silicone strip items, or page `studio-trust` without Andrew letter

## Purchase stack — LOCKED (v19 + draft)

- **Authority:** `Definitive-v19.html` `#buy` · `product.json` `pdp-buy-box`
- **Composition (forward 2026-09-08):** reviews → title / lede → **$74** → color name + size → **Add to Cart** (no price · no qty) → Shop Pay → **empty under ATC** → accordion. Short desc in Description accordion (closed). No typed 4× under $74.
- **Complete the kit:** quiet label + Hot Pilates / Hot Yoga links + hint
- **Title sole badge:** TE optional (CURRENT MESSAGE Aug 9) — show on/off · color **Black/charcoal** `#1c1916` · **Rust orange** `#c45c3f` · **Blue (live strip)** `#458CD9` · Open default rust · Closed default black · label override → `custom.sole_type` → handle/title fallback (Open/Closed Sole · Outdoor · One-Off) · quiet v16 `.pdp-buy__badge` pill

## Variants 4× payments — LOCKED

- **Authority:** `docs/pdp-4x-payments-options.html` Option A · Under Quick Add
- **Applied:** `product.json` `variant-grid` · mock v19 `#variants`
- **Composition:** Name → meta pill → $74 → Quick Add → quiet `or 4 × $18.50`
- **Hard:** no dual pills · LE/Sold Out badges REQUIRED · Sold Out = grey disabled button
- **Theme:** `use_current_product: false` · `card_messaging: meta` · `initial_rows: 2` · `see_all: expand` · tabs Closed/Open/One-Offs/Outdoor

## Mid / lower page — LOCKED draft composition

| Section | Settings / notes |
|---------|------------------|
| `fullbleed-statement` | **TRANSFORM** · type-on-media · **80vh / 60vh** · CTA Shop now → `#buy` |
| `fullbleed-lifestyle` | **Media-only wow** · `show_text: false` · **80vh / 60vh** · after sock-math / before commit |
| `fifty-fifty-*` (PDP) | Desktop **560** / pad **80**. Phone photo **550** · pad **104/104** · cover |
| `fifty-fifty-lifestyle` | `content_style: quote` · stars on · cream `#f5f2ec` |
| `pdp-sock-math` | Compact · “One pair. Done.” · **no review quote** · `cta_text: ""` |
| `fifty-fifty-commit` | reverse · cream · video |
| `pdp-reviews` | Phone **4** cards · **More reviews →** · `/pages/reviews` |
| `fifty-fifty-numbers` | `content_style: statement` · eyebrow Grip, Support, Comfort · title Think outside the sock! · Shop now → `#buy` |
| `guarantee-band` | Centered 3-up · Our promise · Built on guarantees… · 30 / 90 / Built to Last |
| `home-juicer` | Follow the movement · @barreletics · `max_height: 0` · feed `barreletics` |
| `collection-faq` | FAQ blocks + GEO blocks merged · heading “Everything you need to know.” |
| `pdp-sticky-atc` | Present |

## Gallery thumbs (forward 2026-09-08)

- Phone **all 7 visible** (grid) · no arrow buttons · desktop 72px row may scroll

## Critical includes
- Trust: **4-up Free shipping strip** + accordion detail — **no under-ATC trust row**
- Purchase stack Option A on buy-box
- Variants 4× under Quick Add + LE/Sold Out badges
- TRANSFORM fullbleed + lifestyle wow placement
- Reviews via `pdp-reviews` · FAQ+GEO via `collection-faq` · Juicer on page · guarantee 3-up
- Newsletter / footer Join the list — no 10% · **no page newsletter**
