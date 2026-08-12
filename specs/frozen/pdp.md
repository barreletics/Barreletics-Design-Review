# Frozen Spec — PDP

---
status: v19 Locked + draft-matched · proportions LOCKED 2026-08-08 night · v16 Locked prior
surface: Product (`templates/product.json` Closed · `product.open-sole.json` · `product.outdoor.json`)
authority_mock: `docs/Barreletics PDP - Definitive-v19.html`
authority_draft: theme `187144929571` (M4 Visual QA) ↔ `shopify-build/templates/product*.json`
authority_locked_prior: `docs/Barreletics PDP - Definitive-v16.html` @ `691f03b`
updated: 2026-08-08
---

> ## ⛔ NEVER OVERWRITE LOCKED MOCK FILES
> v16 @ `691f03b` and v19 HTML = locked. New versions only.  
> Do not edit Definitive-v16 or Definitive-v19 in place without Andrew letter.  
> Do not thrash `product.json` spine without Andrew letter.  
> **QA match:** draft `187144929571` is the Shopify match for this lock.  
> **2026-08-01:** living authority for strip / fullbleeds / spine = current `product.json` (no new mock).

## Locked spine order (`product.json`)

`pdp-buy-box` → `value-strip` → `pdp-features` → `disciplines` → `fifty-fifty-sock-era` → `variant-grid` → `fifty-fifty-lifestyle` (quote) → `fullbleed-statement` (**TRANSFORM YOUR PRACTICE**) → `pdp-sock-math` (compact) → `fullbleed-lifestyle` (**media-only wow** · Stef running) → `fifty-fifty-commit` → `social-proof` → `fifty-fifty-numbers` (Think outside the sock!) → `guarantee-band` (centered 3-up) → `home-juicer` → `collection-faq` (FAQ+GEO) → `pdp-sticky-atc`

**Absent on page (HARD):** `studio-trust` · page-level `newsletter`

## Proportions LOCKED 2026-08-08 (Andrew — PDP only, not sitewide)

> Match Definitive-v19 section/image scale. Home fifty-fifty stays **640**.

| Surface | Locked value | Notes |
|---------|--------------|-------|
| `fifty-fifty` on PDP templates | `min_height: **560**` · `vertical_padding: **80**` · `mobile_media_height: **320**` | Not Home WORKING 640 |
| `fullbleed-statement` + lifestyle wow | `height_desktop: **80**` · `height_mobile: **60**` | Was drifted 90/100 + 70 |
| Buy gallery | aspect **1:1** · thumbs **72×72** · `object-fit: cover` | Already on lock |
| Buy-box type (living) | SEO title **18/600** · lede `clamp(34–44)/400` · price via `--text-4xl` (**36**) · ATC Type OS CTA | Keep as built — do not thrash to mock 15/32 unless letter |
| Sole badge | **Open = rust** `#c45c3f` · **Closed/Outdoor = charcoal** `#1c1916` | CURRENT MESSAGE 2026-08-08 |
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
| DP-RV | **Reviews = hybrid `pdp-reviews`** — 3 curated photo + 6 curated text (product knowledge quotes) · TE for real photos |
| DP-SM | **Sock math compact** — One pair. Done. · empty CTA |
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
- **Composition:** reviews → title / lede → price → muted `or 4 × $18.50` → color/size → qty+CTA → **empty under ATC** → quiet Complete the kit → accordion
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
| `fifty-fifty-*` (PDP) | **`min_height: 560`** · pad 80 · mobile media 320 · cover |
| `fifty-fifty-lifestyle` | `content_style: quote` · stars on · cream `#f5f2ec` |
| `pdp-sock-math` | Compact · “One pair. Done.” · **no review quote** · `cta_text: ""` |
| `fifty-fifty-commit` | reverse · cream · video |
| `pdp-reviews` | Hybrid 3 photo + 6 text · “Real people. Real results.” |
| `fifty-fifty-numbers` | `content_style: statement` · eyebrow Grip, Support, Comfort · title Think outside the sock! · Shop now → `#buy` |
| `guarantee-band` | Centered 3-up · Our promise · Built on guarantees… · 30 / 90 / Built to Last |
| `home-juicer` | Follow the movement · @barreletics · `max_height: 0` · feed `barreletics` |
| `collection-faq` | FAQ blocks + GEO blocks merged · heading “Everything you need to know.” |
| `pdp-sticky-atc` | Present |

## Gallery thumbs (v19)

- 4 visible · horizontal touch-scroll if overflow · **no arrow buttons**

## Critical includes
- Trust: **4-up Free shipping strip** + accordion detail — **no under-ATC trust row**
- Purchase stack Option A on buy-box
- Variants 4× under Quick Add + LE/Sold Out badges
- TRANSFORM fullbleed + lifestyle wow placement
- Reviews via `social-proof` · FAQ+GEO via `collection-faq` · Juicer on page · guarantee 3-up
- Newsletter / footer Join the list — no 10% · **no page newsletter**
