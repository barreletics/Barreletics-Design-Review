# Content-page spacing audit (read-only)

**Date:** 2026-10-05  
**Theme:** `shopify-build/` (draft **187144929571**)  
**Branch reviewed:** `cursor/te-control-consolidation-f50b` (Shared **Section frame** controls on content sections; template JSON unchanged)  
**Method:** Template render order + computed CSS from section Liquid and global tokens (`design-tokens.css`, `barreletics-base.css`, `theme.liquid` section-gap OS). No theme code or JSON was modified for this audit.  
**Mobile breakpoint:** Theme CSS uses **`max-width: 768px`** (Shopify’s usual ~749–768 band). Values below label **Desktop (≥769px)** and **Mobile (≤768px)** unless noted.

**Reference tokens (global)**

| Token | Desktop | Mobile (≤768px) |
|--------|---------|------------------|
| `--section-padding-y` | 32px (Theme settings → section gap; default 32) | **48px** (`barreletics-base.css` overrides `:root` on pages) |
| `--section-padding-x` | 40px | 16px |
| `--section-padding-y-mobile` | — | 24px (used where sections reference it explicitly, e.g. Compare sub-blocks) |
| `--gap-a` (eyebrow → title) | 16px | 16px |
| `--gap-b` (title → body) | 20px | 20px |
| **Section frame insets** (TE) | All content templates in scope: **0** on top/bottom/x; `inset_custom_mobile`: off |

**Double-padding pattern:** Any two adjacent siblings with class `.section` each apply full vertical padding → **~64px desktop / ~96px mobile** between inner content blocks (32+32 or 48+48), unless a section overrides top/bottom (Compare intro does partially).

**North star:** More air on mobile intros and between policy blocks—closer to editorial about pages (e.g. [BetterMe About](https://betterme.world/about))—without new cream bands; prefer **white** canvases on help-family pages.

---

## Help (`templates/page.help.json`)

**Render order:** `page-returns` (single section type, **four** stacked `<section>` roots in Liquid).

### 1. `page-returns-head` (`section-frame` + `.section`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Space above H1** | 32px section pad-top only (no extra hero offset; sits under global header) | 48px section pad-top |
| **Eyebrow → H1** | Eyebrow empty in JSON → n/a | n/a |
| **H1 → lede** | 20px (`--gap-b`) | 20px |
| **Lede → primary CTA** | 24px (`--space-6`) | 24px |
| **CTA → jump nav** | 20px below CTA (`--space-5` on CTA block) | same |
| **Section pad bottom** | 32px | 48px |

**TE today:** Shared Section frame insets all **0**.

### 2. `page-returns-policy` (`.section` only, no frame)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad top / bottom** | 32px / 32px | 48px / 48px |
| **Gap to previous block** | 32px (head bottom) + 32px (policy top) = **64px** | **96px** |
| **Card grid gap** | 20px | 20px |
| **Card inner pad** | 28px | 28px |
| **Eyebrow → H2** | `--gap-a` / `--gap-b` via `.h2-standard` | same |

### 3. `page-returns-faq` (`.section.section--cream`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad top / bottom** | 32px / 32px | 48px / 48px |
| **Gap from policy** | 64px desktop / 96px mobile (stacked `.section`) | same |
| **Background** | `--bg-alternate` cream band | same |
| **Accordion row** | summary **18px** vertical; answer **20px** bottom pad | **No mobile override** (same 18px—feels tight vs FAQ page) |
| **H2 → list** | 24px (`--space-6`) | same |

### 4. `page-returns-cta` (`.section`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad top / bottom** | 32px / 32px | 48px / 48px |
| **Gap from FAQ** | 64px / 96px stacked section | same |
| **H2 → body → buttons** | `--gap-b`, then 24px to actions | CTA buttons stack full-width |

**Collisions / notes:** Help intro is **much tighter above H1** than FAQ (32–48px vs 56–104px). Cream FAQ band mid-page adds a stripe user asked to avoid expanding. Four `.section` siblings multiply vertical padding at every seam.

---

## Returns (`templates/page.returns.json`)

Identical structure and spacing to **Help** (same `page-returns` section and settings). Findings above apply 1:1.

---

## FAQ (`templates/page.faq.json`)

**Render order:** `page-faq` → `contact-cta`.

### 1. `page-faq` (`section-frame`, **not** `.section`)

**Template setting:** `bg_class`: **`cream`** (`#faf8f6`).

| Area | Desktop | Mobile |
|------|---------|--------|
| **Space above H1** | **104px** (`.page-faq__head` pad-top) + frame inset 0 | **56px** |
| **H1 → next (search)** | **40px** margin-bottom on H1 | **28px** |
| **Subtitle** | n/a in JSON | n/a |
| **Search → topics** | topics `margin-top: 30px` | **22px** |
| **Head → questions block** | `.page-faq__questions` **72px** pad-top | **40px** |
| **Section pad bottom** | **96px** on questions block | **64px** |
| **Topic group → group** | **56px** margin-bottom | **44px** |
| **Accordion summary** | **22px** vertical | **19px** |
| **Answer padding below** | **26px** | same |

**Accordion / FAQ mobile:** Rows use **19px** summary padding and **26px** answer tail; topic rail links **13px × 6px**—readable but dense when many items scroll.

**TE today:** Background → **white** (`bg_class: white`). Frame insets 0.

### 2. `contact-cta` (`section-frame`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad top / bottom** | **64px** / 64px (+ 1px top border) | **48px** / 48px |
| **Gap from FAQ** | FAQ questions bottom pad **96px** (64 mobile) then CTA **64px** (48 mobile) top—generous, not double `.section` | same |
| **Eyebrow → title → body** | 8px / 12px / 24px | title 28px size |

**Collisions:** Cream FAQ canvas butts into white CTA—acceptable if FAQ goes white; border-top on CTA still separates.

---

## Contact (`templates/page.contact.json`, `page.contact-us-form.json`)

**Render order:** `page-contact` (single `section-frame` + `.section`).

| Area | Desktop | Mobile |
|------|---------|--------|
| **Space above H1** | 32px section pad-top | 48px |
| **Eyebrow → H1** | no eyebrow | — |
| **H1 → subtitle** | **8px** (`--space-2`)—**tighter than help-family `--gap-b`** | same |
| **Subtitle → form** | **32px** (`--space-8`) | same |
| **Section pad bottom** | 32px | 48px |
| **Layout gap (form \| sidebar)** | 64px grid gap | **32px** stacked (`--space-8`) |

**TE today:** Frame insets 0. No inner padding sliders on this section.

---

## Size Guide (`templates/page.size-guide.json`)

**Render order:** `page-size-guide` → three Liquid `<section>` roots: head, body, optional CTA.

### 1. Head (`section-frame` + `.section.page-size__head`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Space above H1** | 32px section pad-top | 48px |
| **Eyebrow → H1** | **12px** (`--space-3`) | same |
| **H1 → subtitle** | subtitle margin 0 (relies on H1 **12px** bottom only) | title clamp smaller |
| **Section pad bottom** | 32px + hairline border-bottom | 48px |

### 2. Body (`.section.page-size__body`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad top / bottom** | 32px / 32px | 48px / 48px |
| **Seam from head** | **64px / 96px** double `.section` | same |
| **Stacked H2 blocks** | **56px** top margin on “Fit Notes” / “Fit Tips” | **44px** |
| **Note/tip cards** | 20–22px inner pad, 16px grid gap | same |

### 3. CTA (`.section.page-size__cta`, if enabled)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad** | 32px vertical | 48px |
| **Top border** | 1px `#d6cfc0` | same |

**TE today:** Head frame insets 0.

---

## Compare (`templates/page.compare.json`)

**Render order:** intro → products → table → optional close (close hidden in JSON—empty heading/notes).

### 1. Intro (`section-frame` + `.section.page-compare`)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Pad top / bottom** | **72px** top, **8px** bottom (override) | **48px** top, **4px** bottom |
| **Eyebrow → H1** | **16px** | same |
| **H1 → subtitle** | **20px** | same |

### 2. Products / table / close (`.section` with reduced vertical rhythm)

| Area | Desktop | Mobile |
|------|---------|--------|
| **Each block pad** | `--section-padding-y` (32px) unless overridden | `--section-padding-y-mobile` (**24px** in CSS fallback chain—not the global 48px override) |
| **Seam intro → products** | 8px + 32px ≈ **40px** (intentionally tight) | **4px + 24px ≈ 28px**—**very tight on phone** |

**TE today:** Intro frame insets 0.

---

## Press (`templates/page.press.json`)

**Render order:** `press-row` only.

| Area | Desktop | Mobile |
|------|---------|--------|
| **Outer pad** | **64px × 40px** on `.press-row` | **48px × 16px** |
| **Background** | `#faf8f6` (TE `bg_color`) | same |
| **“Press” heading (H1-style)** | margin **0 0 32px**; 12px padding-bottom + rule | **20px** bottom margin |
| **Grid → mentions** | 20px top margin on mentions | caps/sentence styles per TE |

**Note:** Heading uses **press-row** typography (26–32px / 600), not help-family H1 clamp—by design for home parity.

**TE today:** Section frame insets 0; `desktop_height` 620px drives grid height.

---

## Our Story (`templates/page.our-story.json`)

**Render order:** hero → intro → founder split → prototype split → values → joseph → facts → letter split → geo → close.

| # | Section | Space above “hero” title / H1 | Vertical section padding (top / bottom) | Mobile notes |
|---|---------|--------------------------------|----------------------------------------|--------------|
| 1 | `page-about-hero` | Full-bleed image; **no text H1** | Height **520px** default (TE `media_height`); mobile **460px** or aspect modes on `page.about` | `our-story` JSON lacks mobile height keys present on `page.about.json` |
| 2 | `page-about-intro` | **Origin statement — keep as-is** | `clamp(40px–72px)` top, `clamp(36px–64px)` bottom; bg default **cream** in schema | Mobile **32×20×28** pad; H1 **16px** to lede; pull quote **24px** top |
| 3 | `page-about-split` (founder) | H2 in copy column | Copy pad `clamp(28–56px)` × horizontal; media pad varies | Copy **8×20×32**; media **16×16×0** top |
| 4 | `page-about-split` (prototype) | same | **`cream_bg: true`** (existing band—do not add new) | same pattern |
| 5 | `page-about-values` | **What we stand for — keep card spacing as-is** | Section **56–96px** vertical; cards **20–28px** inner | Section **40×20**; heading **clamp** margins preserved |
| 6 | `page-about-joseph` | H2 | **48–80px** section; gallery **40–72px** | **28–36px** pads |
| 7 | `page-about-facts` | H2 “Made in the USA.” | **64–120px** section pad | **48×20** |
| 8 | `page-about-split` (letter) | body-only title | white bg | mobile media max 440px |
| 9 | `geo-section` | H2 | **0 top**, bottom `--section-padding-y` (32 / 48 mobile) | accordion **12px** row pad |
| 10 | `page-about-close` | H2 closing | **80–160px** campaign-like | **56×20** |

**Seams:** Intro **border-bottom** separates from founder; prototype cream band is intentional; no `.section` double-padding stack (custom pads per block).

**TE today:** Frame insets 0 on wired sections; intro bg color TE if ever moved off cream default.

---

## About (`templates/page.about.json`)

Same section order as Our Story with **richer TE** on hero (640/720 heights, portrait mobile) and typography defaults on intro/splits. **Spacing CSS is identical** to Our Story sections; differences are media height and copy blocks (e.g. Venice fact), not padding rules.

---

## Cross-page findings

1. **Help-family intro inconsistency:** FAQ dedicates **56–104px** above H1; Help/Returns/Contact/Size Guide rely on **32–48px** `.section` pad only → pages feel “stuck” under the header on mobile.
2. **Stacked `.section` siblings** on Help, Size Guide, and Compare multiply gutters (**64/96px**) without adding content rhythm; Compare ** intentionally** tightens seams but mobile **28px** intro→products may be too tight.
3. **Cream usage:** FAQ template **`bg_class: cream`**; Help FAQ band `.section--cream`; Press + Size table header + note cards use cream tints—conflicts with “prefer white” on support content.
4. **H1 → body cadence:** Contact **8px** title→subtitle; Size Guide **12px** eyebrow→title; Help **20px** title→lede—help-family `--gap-b` (20px) not applied uniformly.
5. **Shared Section frame (new):** All scoped sections expose TE inset sliders (default 0). **No template saves yet**—merchant can add outer margin without code, but **inner** intro air still requires section CSS or theme gap settings.
6. **Accordion density:** Full FAQ page rows (**19–22px** summary pad) vs Help quick FAQ (**18px**, no mobile bump)—mobile thumbs need **≥20–24px** vertical on summary for parity with editorial sites.

---

## Recommended content-page rhythm (white-forward)

Target **one help-family system** for Help, FAQ, Returns, Contact, Size Guide, Compare intros:

| Element | Desktop target | Mobile target |
|---------|----------------|---------------|
| Space above page H1 | **72–88px** below header (or 64px min) | **56–64px** |
| Eyebrow → H1 | **16px** (`--gap-a`) | same |
| H1 → lede/subtitle | **20–24px** | **20–24px** |
| Lede → first control / nav | **24–32px** | **24–32px** |
| Between major content bands | **48–56px** (avoid 96px “empty” stacks) | **40–48px** |
| Accordion summary (touch) | **22–24px** vertical | **24–28px** |
| Section frame inset (optional outer air) | 0–16px x | 0–12px x |

**Do not change:** `page-about-values` card grid/pad; `page-about-intro` origin typography and pull-quote spacing (TE bg may stay cream for that block only).

**No new cream bands** on Help/FAQ/Returns; keep table header tint in Size Guide if needed for legibility (micro-surface, not full-width band).

---

## Recommendations (TE vs code)

| # | Change | Type | Pages |
|---|--------|------|--------|
| R1 | Set FAQ **Background → white** (`bg_class`) | **Theme Editor** | FAQ |
| R2 | Help/Returns: remove or reduce **Quick answers** `.section--cream` (switch to white section class or TE bg if added) | **Code** (class on `page-returns-faq`) + optional TE later | Help, Returns |
| R3 | Align Help/Returns **head** top spacing with FAQ (**~72px desktop / 56px mobile** inner pad, or reduce reliance on bare `.section` 32/48) | **Code** (`page-returns.liquid` head styles) | Help, Returns |
| R4 | Collapse **double `.section` padding** between head/body on Size Guide (single wrapper or `padding-top: 0` on body + hairline) | **Code** | Size Guide |
| R5 | Contact: **H1 → subtitle** to `--gap-b` (20px) from 8px | **Code** | Contact |
| R6 | Compare mobile: **intro bottom / products top** ≥ **32px** combined seam | **Code** | Compare |
| R7 | FAQ + Help accordions: mobile **summary pad 24px**, group margin **48px** | **Code** | FAQ, Help |
| R8 | Press: optional TE **Background → #ffffff** if page should match white editorial press index | **Theme Editor** | Press |
| R9 | Content pages: TE **Inset top 16–24px** on first section only (Custom mobile on, mirror on phone) | **Theme Editor** (per template first section) | Any (quick test) |
| R10 | Theme settings → **Section gap** (global): raising mobile gap affects **all** pages—use only if willing to accept site-wide change | **Theme Editor** (global) | Site-wide |

---

## Top 5 highest-impact changes

1. **Unify help-family intro top air (R3)** — Brings Help/Returns/Contact/Size Guide in line with FAQ and BetterMe-like mobile breathing; fixes the largest perceived mobile squeeze.
2. **FAQ canvas white + drop Help mid-page cream FAQ band (R1 + R2)** — Meets “prefer white”; removes alternating support-page stripes without touching Our Story prototype band.
3. **Fix stacked `.section` seams on Help + Size Guide (R4 + policy stack code)** — Cuts **96px mobile dead zones** between head/policy/CTA blocks; content reads as one continuous page.
4. **Mobile accordion touch spacing (R7)** — FAQ + Help quick FAQ; low visual risk, high mobile UX gain.
5. **Compare mobile intro → product seam (R6)** — Prevents compare page from feeling crushed after the H1 on phones.

---

## Appendix: Template → section map

| Page template | Sections (order) |
|---------------|------------------|
| `page.help.json` | `page-returns` |
| `page.returns.json` | `page-returns` |
| `page.faq.json` | `page-faq`, `contact-cta` |
| `page.contact.json` | `page-contact` |
| `page.size-guide.json` | `page-size-guide` (×3 Liquid sections) |
| `page.compare.json` | `page-compare` (×3–4 Liquid sections) |
| `page.press.json` | `press-row` |
| `page.our-story.json` | about-hero → intro → 2× split → values → joseph → facts → letter → geo → close |
| `page.about.json` | same as our-story (TE-enriched hero/intro) |

---

*End of audit. Implement via follow-up PR(s); this file is documentation only.*
