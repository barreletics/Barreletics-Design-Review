# Home page spacing audit — draft theme 187144929571

**Date:** 2026-10-05  
**Scope:** `templates/index.json` render order (active sections only unless noted).  
**Method:** Read-only — template JSON + section Liquid/CSS + global tokens (`design-tokens.css`, `layout/theme.liquid`). No storefront render in this pass.  
**Breakpoints:** Theme mixes **749px**, **767px**, **768px**, and **560px**; mobile figures below call out the rule that applies. Where you asked for **≤749px**, both 749- and 768-based rules are noted when they differ.

**Global rhythm inputs (Theme settings → Layout):**

| Token | Default (CSS) | Wired from TE |
|--------|----------------|---------------|
| `--section-padding-y` | 32px | `settings.section_gap` |
| `--section-padding-y-mobile` | 24px | `settings.section_gap_mobile` |
| `--section-padding-x` / `-mobile` | 40px / 20px | fixed in tokens (+ 16px x on some `@768` overrides) |
| `--gap-a` / `--gap-b` / `--gap-c` | 16 / 20 / 32px | code-only type cadence |
| Shared **Section frame** `inset_*` | 0 on Home | margin on `.section-frame` (`barreletics-base.css`) |

All Home sections use **inset 0** in `index.json` unless stated.

---

## Render order summary

| # | Section ID | Type | Status |
|---|------------|------|--------|
| 1 | `split_hero` | split-hero | active |
| 2 | `visual-mosaic` | visual-mosaic | active |
| 3 | `problem-section` | problem-section | active |
| 4 | `variant-grid` | variant-grid | active |
| 5 | `fifty-fifty-grip` | fifty-fifty | active |
| 6 | `proof-numbers` | proof-numbers | active |
| 7 | `fifty-fifty-one-pair` | fifty-fifty | active |
| 8 | `reviews` | pdp-reviews | active |
| 9 | `press-feature-interni` | press-feature | active |
| 10 | `statement-band` | statement-band | active |
| 11 | `fullbleed-statement` | fullbleed-statement | active |
| 12 | `disciplines` | disciplines | active |
| 13 | `press-home` | press-cards | **disabled** |
| 14 | `press-row` | press-row | active |
| 15 | `guarantee-band` | guarantee-band | active |
| 16 | `home-juicer` | home-juicer | active |
| 17 | `collab-hero` | collab-hero | **disabled** |

---

## 1. Split hero (`split_hero`)

**Vertical padding (inside section)**

| | Desktop (≥769) | Mobile (≤768) |
|---|----------------|---------------|
| Section shell | None — full-bleed grid, 92vh media column | None — stacked media + copy |
| Copy column | `72px 56px` (`split-hero.css`) | `var(--hero-copy-pad-y-mobile)` top + sides `24px`, bottom `var(--space-10)` → **52px / 24px / 40px** (`design-tokens.css`) |
| Media | Fills column; no inner pad | 4:5 aspect, max-height 78vh |

**TE / JSON:** `inset_*` 0. Trust: `trust_gap` 10, `trust_below` 16.

**Inner gaps (copy stack)**  
Trust → title: `--sh-trust-below` (16 mobile / `--gap-a` desktop). Title → body: **16px** (mobile CSS). Body → CTA: **28px** (mobile). CTA row gap: **16px**.

**Gap to next section (visual-mosaic)**  
Hero has **no bottom padding**; mosaic `pad_top` **16px** → **~16px** between hero copy/media edge and mosaic content (plus 0 insets). **No double-padding.**

---

## 2. Visual mosaic (`visual-mosaic`)

**Vertical padding**

| | Desktop | Mobile |
|---|---------|--------|
| Section | `pad_top` / `pad_bottom` **16px** each (JSON) | ≤767: same vars; ≤560: **12px** top/sides, bottom **`var(--vm-gap)`** (= **4px** with current `grid_gap`) |
| Horizontal | `pad_x` **16px** (560: **12px**) | same |

**Inner gaps**  
Grid `grid_gap` **4px** (JSON). Tile title margin bottom **10px** (≤560). Hero row span 2 on 2-col mobile.

**Gap to next (problem-section)**  
Mosaic bottom **16px** (12+4 on narrow phones) + problem **cover-flush** outer pad **0** → transition is **tight**; cream problem band starts flush under mosaic.

---

## 3. Problem section (`problem-section`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Default | **72px 40px** on `.problem-section` | **48px 16px** on `.problem-inner` (cover-flush); section shell **0** |
| Cover flush (Home) | Section **0**; copy column `.problem-inner` **72px 40px** | Media **600px** tall (`mobile_media_height`); copy **48px 16px** |
| Media column | Flush 50/50 — **no inner pad** | Fixed height clip; **0 gap** to copy when flush |

**TE:** `copy_stack_gap` **12** (list block spacing). `bg_color` `#faf8f6` (panel — not an extra outer band).

**Inner gaps**  
Title → body: `--gap-b` (20px). Copy stack: `--pr-copy-stack-gap` **12px** between body and list block. List items: **14px** vertical pad, **12px** icon gap. CTA block `margin-top` **28px**. Mobile layout gap media↔copy: **0** (flush) or **28px** (inset mode).

**Gap to next (variant-grid)**  
Problem copy bottom pad **72px** (desk) / **48px** (mob) + variant-grid top **`--section-padding-y`** **32px** / **`--section-padding-y-mobile`** **24px** → **~104px desk / ~72px mob** (stacked paddings, same white/cream adjacency: white grid on `#ffffff`).

---

## 4. Variant grid (`variant-grid`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Home (not collection) | Top/bottom **`--section-padding-y`** (**32px** default) | Top **`--section-padding-y-mobile`** (**24px**); **bottom 0** (explicit CSS) |
| Horizontal | `--section-padding-x` (40px) | `--section-padding-x-mobile` (20px) |

**Inner gaps**  
Head → toolbar: `margin-bottom` **40px** (`--space-9`); head title → body **16px**. Grid: **28px / 56px** col/row gap desktop; mobile **10px / 20px**. Card content pad **18px** desk; **14px 10px 16px** mobile. Toolbar gap **12px**.

**Gap to next (fifty-fifty-grip)**  
**Critical:** mobile **0 bottom pad** on grid + fifty-fifty mobile **`padding-top: 0`** → **zero outer rhythm** between shop grid and first 50/50 (media meets cards). Desktop: **32px** (grid bottom) + **32px** (ff `section_gap`) = **64px** unless overridden.

---

## 5. Fifty-fifty — Never loses grip (`fifty-fifty-grip`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Shopify section wrapper | `padding-block` = `section_gap` **32px** (JSON) | **`padding-top: 0`**, **`padding-bottom: section_gap_mobile` **0**** |
| Text column | **`text_pad_y` default 96px** top/bottom (JSON lacks `text_pad_y` → **96px**); sides **64px** | **`text_pad_y_mobile` absent** — legacy `text_pad_top_mobile: 32` in JSON **not read** → renders **80px** top/bottom; sides **20px** |
| Media | Flush cover; min-height **620px** | Height **`--split-media-h-mobile`** (theme default **500px**); square aspect on grip section |

**Special code:** `#never-loses-grip` wrapper forces **`padding-bottom: 16px`** (desk) and kills next section’s top inset — pairs with cream `#faf8f6`.

**Inner gaps**  
Title → body **20px**; body → CTA **32px** (`--gap-b` / `--gap-c`).

**Gap to next (proof-numbers)**  
Desk: **16px** (hack bottom) + proof **88px** top → **104px** inside cream/white handoff. Mobile: **0** ff bottom + proof **64px** top → **64px**.

---

## 6. Proof numbers (`proof-numbers`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Band | **88px 40px** (hard-coded) | **64px 20px** |

**Inner gaps**  
Eyebrow → title **16px**; head → grid **32px**. Stats grid: **0 gap** desk (vertical dividers); mobile **28px** row gap. Stat → label **10px**; label → detail **8px**.

**Gap to next (fifty-fifty-one-pair)**  
Proof bottom **88px** / **64px** + ff top **32px** / **0** → **120px** desk / **64px** mob. Both white/cream borders may visually merge — borders add 1px lines, not air.

---

## 7. Fifty-fifty — One pair (`fifty-fifty-one-pair`)

Same mechanics as §5 with `bg_color` **#ffffff**, `section_gap` **32**, `section_gap_mobile` **0**, same stale legacy phone pad keys. Stretch media on mobile (not square).

**Gap to next (reviews)**  
Mobile: **0** ff bottom + reviews top **`--section-padding-y-mobile`** **24px** → **24px**. Desktop: **32+32 = 64px**.

---

## 8. Reviews (`reviews` / `pdp-reviews`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Section | **`--section-padding-y`** / **`--section-padding-x`** | **48px 16px** (overrides token 24) |

**Inner gaps**  
Header stack gap **20px** (16px ≤749). Featured card pad **22–24px**. Text card grid gap **20px**; card internal **12px**. Community label margins **20px / 12px**.

**Gap to next (press-feature)**  
Desk: **32+48** top ≈ **80px** between bands. Mobile: **48+40** ≈ **88px** (reviews bottom 48 + press-feature top 40).

---

## 9. Press feature / twin frame (`press-feature-interni`)

**Vertical padding**

| | Desktop | Mobile (≤749) |
|---|---------|----------------|
| `.twin-frame` | **48px 40px 56px** | **40px 16px 48px** |

**TE heights:** desktop **520px**, mobile **280px** per frame.

**Inner gaps**  
Frames row gap **12px** (10px mobile). Caption pad **28px 24px 8px** (20px 8px 0 mobile). Eyebrow → title **8px**; title → body **10px**.

**Gap to next (statement-band)**  
White statement follows cream twin: **~56px + 96px** desk (**152px** stacked) / **48px + 56px** mob (**104px**). Statement top border adds hairline, not space.

---

## 10. Statement band (`statement-band`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Band | **96px 40px** | **56px 20px** |

**JSON:** `bg_color` **#ffffff** (Home knock-socks line).

**Inner gaps**  
Line → subhead **16px** (`--gap-a`); subhead → CTA **32px** (`--gap-c`).

**Gap to next (fullbleed)**  
Statement bottom **96px** / **56px** + fullbleed media-only **0** pad → air is **only** from statement padding above the flush image (fullbleed is edge-to-edge).

---

## 11. Full-bleed statement (`fullbleed-statement`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Media-only (Home) | **0** — height **120vh** (`height_desktop`) | **0** pad; height **`--split-media-h-mobile`** (**500px** with `height_mobile: 0`) |
| With copy (not Home) | Content **80px 40px** | **56px 16px** |

**Inner gaps**  
N/A on Home (`show_text: false`).

**Gap to next (disciplines)**  
Image sits flush on white disciplines; **no between-section pad** — only disciplines’ **`pad_y` 64px** top (+ border-top 1px).

---

## 12. Disciplines (`disciplines`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Inner | **`pad_y` 64px** + `--section-padding-x` | **`pad_y_mobile` 64px** + 16px x; extra **`space_below_mobile` 0** |

**Inner gaps**  
Headline → tags **20px**; tags row **12px 8px** flex gap; **24px** padding-top above tag border.

**Gap to next (press-row)**  
Both on cream `#faf8f6` / press `#faf8f6` — **64px** disciplines bottom + **64px** press-row top → **128px** desk (**double cream band** — same color, so reads as one continuous field with **128px** internal air). Mobile: **64+48 = 112px**.

---

## 13. Press row (`press-row`) — `mobile_layout: grid`

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Section | **64px 40px** | **48px 16px** |

**Grid gaps (current repo)**  
Desktop hero+cards grid: **`gap: 10px`** (not 24px in this branch). Eyebrow → grid **24px** margin. Mobile grid (≤520, `press-row--m-grid`): **`gap: 10px`**.

**Inner gaps**  
Hero copy pad **24px 28px 28px**; label → line **8px**. Card foot **12px 14px 14px**; title → caption **2px**.

**Gap to next (guarantee-band)**  
Cream → white: **64px + 32px** token ≈ **96px** desk; **48px + 24px** ≈ **72px** mob (guarantee uses token on home).

---

## 14. Guarantee band (`guarantee-band`)

**Vertical padding**

| | Desktop | Mobile (≤560) |
|---|---------|----------------|
| Section | **`--section-padding-y`** (32 default; CSS fallback **64px** on `.guarantee-section`) | **`--section-padding-y-mobile`** (**48px**) |

Note: rule says `var(--section-padding-y, 64px)` — if theme `section_gap` stays **32**, **32px** applies, not 64.

**Inner gaps**  
Head → grid **40px**; column pad **20px 24px**; title → detail **10px**. CTA wrap **32px** top.

**Gap to next (home-juicer)**  
Both white: **32+32** (or **64+32** if fallback wins) desk; mobile **48+24** min.

---

## 15. Home juicer / Instagram (`home-juicer`)

**Vertical padding**

| | Desktop | Mobile (≤768) |
|---|---------|----------------|
| Section | **`--section-padding-y`** (fallback **64px** in rule) | **`--section-padding-y-mobile`** (**48px** fallback) |

**Inner gaps**  
Eyebrow → title **16px**; title → body **20px**; body → feed **32px**; feed min-height **560px** desk (**0** mobile).

**Gap to footer**  
Last active section — bottom pad sets page end feel (**32–64px** desk depending on token).

---

## Disabled on Home (reference only)

- **`press-home`** (`press-cards`): would add **`padding_y` 40**, `gap` 16 — not rendered.  
- **`collab-hero`**: stage padding/gaps — not rendered.

---

## Collision / rhythm issues (mobile-first)

1. **Variant grid → 50/50 weld:** grid **padding-bottom: 0** + fifty-fifty **`padding-top: 0`** → hardest seam on Home.  
2. **50/50 stack:** `section_gap_mobile: 0` on both ff sections — no outer air between grip / proof / one-pair transitions except inner text pad and proof band.  
3. **Legacy TE keys:** `text_pad_top_mobile: 32` in JSON **does not affect output** (`text_pad_y_mobile` drives CSS; absent → **80px**). Editor shows stale values.  
4. **Mosaic → problem:** only **16px** (or **12+4**) before full-width cream problem — feels cramped vs editorial sites.  
5. **Same-background stacking:** cream press-row on cream disciplines **adds** padding but **no hue change** — reads flat.  
6. **Breakpoint scatter:** 749 vs 768 vs 767 changes which rule fires near tablet width.  
7. **Press-row grid gap:** repo **10px**; product brief mentions **24px** — confirm intended target on this theme.

---

## Recommended vertical rhythm (BetterMe-style breathing)

Use a **small step scale** everywhere you add air (do not shrink cards or 50/50 media flush):

| Step | px | Use for |
|------|-----|---------|
| **S** | 16 | Eyebrow→title, tight grid gaps (mosaic tiles) |
| **M** | 24 | Theme mobile **section gap** default; between major blocks on phone |
| **L** | 32 | Theme desktop **section gap**; title→body adjacency when denser |
| **XL** | 48 | Phone section vertical pad (problem copy, press, reviews-class) |
| **XXL** | 64 | Desktop band pad (disciplines, guarantee-class) when not full-bleed |

**Copy stack (keep globally):** `--gap-a` 16 / `--gap-b` 20 / `--gap-c` 32 — already aligned with BetterMe-like headline breathing.

### Theme Editor (no code)

| Change | Where |
|--------|--------|
| Raise **Section gap (mobile)** `section_gap_mobile` **24 → 32** (or **40** for stronger About-like feel) | Theme settings → Layout |
| Optionally raise **Section gap (desktop)** **32 → 40** | Same |
| **Visual mosaic:** `pad_top` / `pad_bottom` **16 → 24** or **32** | Home → Visual mosaic |
| **Fifty-fifty (both):** set **`section_gap_mobile` to 24** (currently **0**) | Per-section TE |
| **Fifty-fifty (both):** set **`text_pad_y_mobile` to 48–56** (sync intent; remove reliance on dead legacy keys) | Per-section TE |
| **Disciplines:** `pad_y_mobile` **64 → 48** if double-cream with press feels tall; or **`space_below_mobile` 16** before press | Disciplines section |
| **Problem section:** `copy_stack_gap` **12 → 16** | Problem section |
| **Shared frame:** selective **`inset_bottom_mobile` 16–24** on mosaic or variant-grid only if you want page-edge inset without code | Section frame controls |

### Code changes

| Change | Rationale |
|--------|-----------|
| **variant-grid:** restore **bottom** `padding-bottom: var(--section-padding-y-mobile)` on Home (remove `0` override) | Fixes mobile weld to 50/50 |
| **fifty-fifty:** default `section_gap_mobile` **24** when unset (keep **0** on PDP if needed) | Restores mobile band without touching media flush |
| **press-row:** set grid **`gap: 24px`** at ≤900 and mobile grid (keep hero/card sizes) | Matches stated layout intent; repo still **10px** |
| **visual-mosaic:** bump ≤560 bottom pad from **`var(--vm-gap)`** to **`max(var(--vm-gap), 16px)`** or tie to `pad_bottom` | Stops 4px tail on small phones |
| **Migrate JSON:** map legacy `text_pad_top_mobile` → `text_pad_y_mobile` on save or read fallback in Liquid | TE truth matches render |
| **Optional:** unify mobile breakpoints to **768** for section padding queries | Predictable QA at 749px |

**Constraints respected:** no new cream bands; 50/50 **cover flush** unchanged; press-row structure preserved; card min-heights not reduced.

---

## Top 5 highest-impact changes

| Rank | Change | Type | Effect |
|------|--------|------|--------|
| **1** | Fix **variant-grid mobile bottom padding** (remove 0) | Code | Largest single seam: shop grid → first 50/50 |
| **2** | **Fifty-fifty `section_gap_mobile` 24** (both Home instances) | TE (+ code default) | Air between stacked 50/50s and proof band on phone |
| **3** | Raise global **`section_gap_mobile`** 24 → **32–40** | TE | Lifts all token-based sections (reviews, guarantee, juicer) |
| **4** | Set **`text_pad_y_mobile` 48–56** on both fifty-fifties; fix legacy JSON drift | TE + code fallback | Reduces overly tall 80px phone copy pads; aligns editor |
| **5** | **Visual mosaic** pad **16 → 24–32** + optional **press-row gap 24px** | TE + code | More editorial space after hero and inside press grid without shrinking cards |

---

## Files referenced

- `shopify-build/templates/index.json`
- `shopify-build/assets/design-tokens.css`, `split-hero.css`, `barreletics-base.css`
- `shopify-build/layout/theme.liquid` (section gap OS)
- Sections: `split-hero`, `visual-mosaic`, `problem-section`, `variant-grid`, `fifty-fifty`, `proof-numbers`, `pdp-reviews`, `press-feature`, `statement-band`, `fullbleed-statement`, `disciplines`, `press-row`, `guarantee-band`, `home-juicer`
- `shopify-build/snippets/section-inset-vars.liquid`

---

## Proof / validation (follow-up)

This audit is **code-derived**. Confirm on draft theme **187144929571** with browser devtools at **375px** and **1440px**: measure `#shopify-section-*` computed `padding`/`margin` on seams called out in §Collision and Top 5.
