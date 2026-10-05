# Spacing audit — PDP & Shop All (read-only)

**Date:** 2026-10-05  
**Theme (git):** `shopify-build/` → draft **187144929571**  
**Branch audited:** `cursor/te-control-consolidation-f50b` (Shared section frame controls present)  
**Goal:** More editorial vertical rhythm on phone (reference: [betterme.world/about](https://betterme.world/about)) without changing layouts, colors, media fit, 50/50 flush media, card footprint, or adding new cream bands.

**Method:** Template JSON render order + section Liquid/CSS defaults. No theme code or JSON was modified for this audit.

**Breakpoints note:** Most spacing CSS uses **`max-width: 768px`** for phone; type tweaks often use **`749px`**. Below, **mobile** means **≤768px** unless noted as **≤749px**.

---

## Global rhythm (what actually drives “air”)

| Token / control | Desktop (>768) | Mobile (≤768) | Where set |
|-----------------|----------------|---------------|-----------|
| `--section-padding-y` | Theme **Section gap (desktop)** default **32px** | At ≤768, base CSS also sets `--section-padding-y: 48px` (affects sections that read this var on phone) | `layout/theme.liquid`, `barreletics-base.css` |
| `--section-padding-y-mobile` | — | Theme **Section gap (mobile)** default **24px**; **PDP override → 32px** on product templates | `layout/theme.liquid` |
| `--section-padding-x` / `-mobile` | 40px | 16px (20px in tokens file; theme uses 16px at 768) | tokens + base |
| `--gap-a` / `--gap-b` / `--gap-c` | 16 / 20 / 32px | same | `design-tokens.css` |
| **Section frame inset** | `inset_top/bottom/x` → **margin** on `.section-frame` | Same sliders unless **Custom mobile inset** ON | `section-inset-vars.liquid` + TE per section |
| Shop All grid open | `--pad-grid-page-open` **72px** top | **56px** top | `variant-grid.liquid` when collection / first section |

**Shared section frame (TE):** Most marketing sections expose **Shared — Section frame** (inset 0–96px desktop, optional mobile). Template JSON on audited pages keeps insets at **0** — spacing is almost entirely from section-internal padding + a few wrapper rules (notably fifty-fifty).

---

## Buy box area only (`pdp-buy-box`)

Commerce chrome unchanged; spacing-only readout.

| Area | Desktop | Mobile (≤768) | TE? |
|------|---------|---------------|-----|
| Section outer pad | `40px` top, `48px` bottom; horizontal `var(--section-padding-x)` + `var(--space-14)` | `32px` top (`--space-8`), **0 bottom**; horizontal `16px` | **No** — CSS locked |
| Gallery ↔ buy column gap | 48px | 32px (`--space-8`) | No |
| Buy stack internal gap | 14px | 14px (unchanged) | No |
| Buy column bottom pad | 32px | 0 (hero bottom pad removed on phone) | No |
| Title block (phone) | — | `margin-bottom: 16px` on header | No |

**Between buy box and first content section:** On Open/Closed PDPs the first block is often **50/50** or **variant grid**. Buy box ends flush on mobile (`padding-bottom: 0`); the next section’s **top** padding/inset defines the gutter — often **0** on fifty-fifty wrapper top (see below) → **tight handoff** on phone.

**Sticky ATC:** Fixed bar ~`10–12px` vertical pad + button; **no sitewide `padding-bottom` on `<body>`** for clearance. Last sections (FAQ, juicer) rely on natural height; on short viewports FAQ triggers can sit near the bar when sticky is visible. **Do not fix by shrinking cards** — use **bottom inset** on late-page sections or a small global footer pad (code).

---

## Product templates — scope

| Template file | Typical product | Notes |
|---------------|-----------------|--------|
| `product.open-sole.json` | Open Sole (`studio-performance-skin-footwear`) | Richest stack; reference below |
| `product.json` | Closed Sole (default PDP) | Same rhythm family; `disciplines` band; value-strip disabled |
| `product.in-studio-template.json` | Alternate Open Sole layout | Matches open-sole spacing pattern |
| Other `product*.json` | Apparel, Coperni, one-offs, outdoor | Same section types; one-offs slimmer stack |

Below: **Open Sole** render order (Closed Sole follows same section types with minor order/settings diffs).

---

## Open Sole PDP — below buy box (render order)

### 1. `value-strip`

| | Desktop | Mobile |
|---|---------|--------|
| Inner vertical pad | TE `padding_y` **28px** (template) | TE `padding_y_mobile` **24px** |
| Section frame inset | 0 | 0 |
| **Status** | **Hidden** on mobile and desktop in template | — |

### 2. `fifty-fifty` — “sock era”

| | Desktop | Mobile |
|---|---------|--------|
| Wrapper `padding-block` (band air) | TE `section_gap` **32px** top & bottom | Wrapper top **0**, bottom **`section_gap_mobile` forced 0 on product** (liquid override) |
| Text column pad | `text_pad_y` default **96px** T/B; side **64px** | **`text_pad_y_mobile` default 80px** T/B (legacy `text_pad_top_mobile` in JSON **not read**) |
| Media ↔ copy | Column gap 0 (flush 50/50) | Stacked; media height **theme** `--split-media-h-mobile` (500px) if `mobile_media_height` 0 |
| Inner copy gaps | title→body **20px**, body→CTA **32px** | same |
| Same-bg neighbor | `#faf8f6` panel | Next section white grid — **32px** wrapper gap desktop only |

**Between sections:** Desktop **32px** wrapper + possible **96px** text pad reads as generous; mobile **0** wrapper bottom → grid/header starts immediately after text **80px** bottom pad.

### 3. `variant-grid` — `#variants`

| | Desktop | Mobile |
|---|---------|--------|
| Section pad | `var(--section-padding-y)` **32px** T/B; X 40px | Top **32px** (`--section-padding-y-mobile` on PDP); **bottom 0** (explicit mobile rule) |
| Head → toolbar | head `margin-bottom` **40px** (`--space-9`) | **28px** |
| Toolbar | pad **14px** T/B; gap **16px** | pad **12px**; gap **12px** |
| **Product grid** | cols 4; **column-gap 28px**, **row-gap 56px** | 2 cols; **column-gap 10px**, **row-gap 20px** |
| Card interior | per `product-card` snippet **18px** pad | same |
| Frame inset (TE) | 0 | 0 |

**Collision:** Mobile **zero bottom pad** on grid → next section (`pdp-features`) relies on its **own top pad** only; no inter-section margin (insets 0).

### 4. `pdp-features`

| | Desktop | Mobile |
|---|---------|--------|
| Section T/B pad | TE `pad_top/bottom` **32px** (template) | Liquid **hardcodes 48px** T/B — **TE `pad_top_mobile` / `pad_bottom_mobile` ignored** |
| Header → grid | **24px** | **24px** |
| Feature grid gap | **24px × 48px** | **18px** stack |
| Feature title → body | **8px** | **8px** |

Borders top+bottom on section → visual separation even when external gap is 0.

### 5. `fifty-fifty` — lifestyle

Template sets legacy `text_pad_top_mobile` **96** / `text_pad_bottom_mobile` **96** — **not applied**; effective phone text pad **80px** unless `text_pad_y_mobile` set in TE.

| | Desktop | Mobile |
|---|---------|--------|
| Wrapper band | `section_gap` **32px** | wrapper bottom **0** (PDP) |
| `mobile_media_height` | — | **360px** (template) vs default 500 |
| bg | `#faf8f6` | same |

### 6. `fullbleed-statement` — “Hold every pose”

| | Desktop | Mobile |
|---|---------|--------|
| Outer section pad | **0** (full bleed) | **0**; height **theme** photo/video mobile height |
| Copy overlay pad | **80px × 40px** | **56px × 16px** |
| Media-only sibling | — | Phone photo mode can add **32px** cream pad around image on PDP only |

No wrapper band between neighbors — **hard edge** to prev/next section color blocks.

### 7. `pdp-sock-math` (editorial)

| | Desktop | Mobile |
|---|---------|--------|
| Section T/B | TE `pad_top/bottom` **80px** (template) | Editorial: **`pad_top` + `pad_bottom + 48px`** extra bottom; copy pad **48×20** |
| Copy → CTA | **28px** | **28px** (CTA) |
| Image frame | TE `image_frame_mobile` **360** | fixed height band |

### 8. `fullbleed-statement` — lifestyle video (text off)

Media-only; mobile height from theme video token (**500px** default). No inter-section inset.

### 9–13. Additional `fifty-fifty`, `statement-band`, `reviews`

**Fifty-fifty (commit, tired-socks, numbers):** Same rules — desktop wrapper **32px**; mobile wrapper gap **0**; text pad **80px** default phone; `section_gap` **32** desktop.

**`statement-band` (knock socks):** Inner pad **96×40** desktop → **56×20** mobile; cream band borders. No TE vertical sliders — fixed CSS.

**`pdp-reviews`:** Pad **`var(--section-padding-y)`** / mobile **`var(--section-padding-y-mobile)`** → **32px** on PDP phone; head **`margin-bottom 32px`**; text card grids **16px** gap on phone.

### 14. `guarantee-band`

| | Desktop | Mobile |
|---|---------|--------|
| Section pad | **`var(--section-padding-y)`** (often 32; CSS fallback 64) | **48px** fixed on product at ≤560px |
| Head → grid | **40px** | **40px** |
| Column grid | 3-up, **0 gap** (borders) | 1-col stack |

### 15. `home-juicer`

| | Desktop | Mobile |
|---|---------|--------|
| Section pad | **64px** fallback / `--section-padding-y` | **`--section-padding-y-mobile`** (PDP **32px**) |
| Eyebrow→title→body | **16 / 20 / 32px** | same |
| Feed min-height | **560px** desktop | **0** on mobile (good — less empty air) |

### 16. `collection-faq`

| | Desktop | Mobile |
|---|---------|--------|
| Section pad | **`var(--section-padding-y)` × `var(--section-padding-x)`** | **No mobile-specific FAQ pad** — uses same vars (32×16 on PDP) |
| Heading → items | **40px** | **40px** |
| Accordion row | **20px** T/B per trigger | trigger **15px** type |

**Sticky overlap risk:** FAQ is last content before sticky section; accordion at bottom of page + **no extra bottom inset**.

### 17. `pdp-sticky-atc`

Not a layout section; fixed **bottom** chrome. See buy box + FAQ notes.

---

## Closed Sole (`product.json`) — deltas from Open Sole

- **Order:** `disciplines` cream band after sock-math; no `knock-socks` / extra fifty-fifty blocks in default JSON.
- **`pdp-features`:** TE pad not overridden in JSON → desktop **32px**; mobile still **48px** from liquid hardcode.
- **`value-strip`:** disabled.
- Same **variant-grid** mobile **0 bottom** and **fifty-fifty** mobile **0 wrapper gap** behavior.

---

## Shop All — `collection.json` (+ siblings)

**Render order ( notable ):**
`variant-grid` → `collection-hero` → `upgrade-grip` (disciplines) → … → `collection-faq`.

### `variant-grid` (first — `#grid`)

| | Desktop | Mobile |
|---|---------|--------|
| Top pad | **72px** (grid-open ruler) | **56px** |
| Bottom pad | **32px** (`--section-padding-y`) | **0** |
| Grid gaps | **28 / 56px** | **10 / 20px** |

### `collection-hero`

| | Desktop | Mobile |
|---|---------|--------|
| Section pad | bleed vs contained modes; copy **56–72px** vertical | TE **`text_spacing_mobile` 36px** on copy column (template) |
| vs grid above | Grid bottom **32px** desktop / **0** mobile + hero own top pad → mobile can feel **stacked without gutter** |

### `no-socks-features` (`pdp-features`)

TE **64px** T/B desktop, **48px** mobile in JSON — mobile TE still **ignored** by liquid (**48px** either way).

### `visual-mosaic` (in-use)

TE **`pad_top/bottom` 16px**, **`grid_gap` 8px**, mobile tile height **264px** — intentionally tight mosaic; not primary “breathing” band.

### `collection-faq`

Cream background; same FAQ padding vars as PDP.

**Other collection templates** (`collection.open-sole.json`, `closed-sole.json`, etc.): same section types; compare grid-open flag via section index / collection template — spacing rules identical.

---

## Double-padding & collisions (summary)

| Pattern | Where | Effect |
|---------|-------|--------|
| **PDP fifty-fifty mobile wrapper gap = 0** | All product `fifty-fifty` | TE `section_gap_mobile` **ignored** on product; sections **stack with no band air** on phone |
| **Legacy FF JSON keys unused** | `vertical_padding`, `text_pad_top_mobile`, … | Template values **do not change CSS**; only `text_pad_y` / `text_pad_y_mobile` / `section_gap` matter |
| **Variant grid mobile bottom 0** | PDP + Shop All grid | Removes **between-section** buffer; next section top pad only |
| **Same cream `#faf8f6` back-to-back** | FF + statement-band + sock-math | Reads as one continuous field on mobile (borders/wrapper gap 0) — not extra cream *bands*, but **less scroll rhythm** |
| **Fullbleed ↔ solid** | FF / features / fullbleed | **No wrapper gap** on mobile; sharp transitions |
| **pdp-features mobile TE ignored** | All PDP/collection feature bands | JSON `pad_top_mobile` **24/48/64** has **no effect** |
| **Shop All: grid then hero** | `collection.json` | Grid **56px** top open + hero content pad; mobile grid **bottom 0** → tight coupling |

---

## Recommended vertical rhythm (BetterMe-like breathing)

**Principles:** Add **margin-between-sections** and **consistent phone section pads** without new cream strips, without shrinking variant cards, without changing 50/50 flush media or cover fit.

| Tier | Desktop target | Mobile target (≤768) |
|------|----------------|----------------------|
| Between major sections | **40–48px** effective gutter (wrapper + inset) | **32–40px** between stacked blocks |
| Standard content section T/B | **48–64px** | **40–48px** |
| Fifty-fifty text column T/B (phone) | — | **88–96px** when copy sits under media |
| Shop All grid | keep **72/56** top open | row-gap **24–28px** (minor +4–8 vs today) |
| FAQ / footer of page | + **16–24px** bottom **inset** when sticky ATC present | same |

### Marking: Theme Editor vs code

| # | Change | Type | Rationale |
|---|--------|------|-----------|
| 1 | **Theme settings → Layout → Section gap (mobile)** **24 → 36–40** (desktop **32 → 40** optional) | **TE** | Lifts all sections using `--section-padding-y-mobile` (reviews, juicer, FAQ, guarantee) in one move |
| 2 | Per-section **Shared — Section frame → Inset bottom 16–24px** on `collection-faq`, `home-juicer`, `pdp-reviews` on PDP/Shop All | **TE** | Sticky ATC clearance without layout redesign |
| 3 | **Fifty-fifty → Text pad top & bottom — phone (`text_pad_y_mobile`)** **80 → 96** on high-traffic PDP blocks; **Section gap (desktop)** **32 → 40** where cream meets white | **TE** | Uses wired controls; adds copy air under phone media |
| 4 | **Variant grid → Inset bottom 24–32px (mobile)** via Shared frame on PDP/Shop All instances | **TE** | Fixes **0 bottom pad** without altering grid gaps or card size |
| 5 | **Stop forcing `--ff-section-gap-m: 0` on product** in `fifty-fifty.liquid`; honor TE `section_gap_mobile` (e.g. **24px**) | **Code** | Single highest-leverage fix for PDP “flat scroll” on phone |
| 6 | **Wire `pdp-features` `pad_top_mobile` / `pad_bottom_mobile` from TE** (remove hardcoded 48) | **Code** | Makes template/TE spacing honest |
| 7 | **Variant grid mobile row-gap** **20 → 24–28px** (keep column-gap 10) | **Code** (or theme token) | Shop All / PDP grid breathes slightly; card size unchanged |
| 8 | Optional **body.template-product padding-bottom** ≈ sticky bar height when sticky visible | **Code** | Safety net for FAQ overlap |

---

## Top 5 highest-impact changes

1. **Code — PDP fifty-fifty honor mobile section gap**  
   Remove product-only `section_gap_m = 0` / `--ff-section-gap-m: 0 !important`. Set TE default **24–32px** on key blocks. *Impact:* Space between every phone stacked 50/50 and adjacent sections; matches editorial scroll on About-style pages.

2. **TE — Global Section gap (mobile) 32 → 40** on draft theme  
   PDP already bumps product to 32; raising theme default helps collection + shared bands. Pair with **desktop 40** if Shop All still feels tight.

3. **TE — Variant grid Shared frame inset bottom 24px (mobile custom inset 24)** on Shop All + PDP `#variants`  
   Fixes documented **bottom 0** collision without touching **10×20** card grid or card padding.

4. **Code — `pdp-features` respect `pad_top_mobile` / `pad_bottom_mobile`**  
   Unlock per-template TE (e.g. Shop All **64/48** intent) and allow **40–48px** phone pads without giant desktop change.

5. **TE + code — Sticky-safe footer rhythm**  
   TE **inset bottom 20–24** on last content sections (`collection-faq`, `home-juicer`) **plus** optional small code pad on `body.template-product`. Prevents overlap without shrinking FAQ rows or cards.

---

## Files referenced

- Templates: `templates/product.open-sole.json`, `product.json`, `product.in-studio-template.json`, `collection.json`, other `product*.json` / `collection*.json`
- Sections: `pdp-buy-box.liquid`, `fifty-fifty.liquid`, `variant-grid.liquid`, `pdp-features.liquid`, `fullbleed-statement.liquid`, `pdp-sock-math.liquid`, `statement-band.liquid`, `pdp-reviews.liquid`, `guarantee-band.liquid`, `home-juicer.liquid`, `collection-faq.liquid` + `snippets/faq-accordion.liquid`
- Global: `layout/theme.liquid`, `assets/barreletics-base.css`, `assets/design-tokens.css`, `snippets/section-inset-vars.liquid`

---

## Out of scope (per brief)

- Visual browser QA on live draft (not run in cloud read-only pass)
- Flow, checkout, sticky ATC JS behavior changes
- New cream bands, card redesign, or 50/50 media inset changes
