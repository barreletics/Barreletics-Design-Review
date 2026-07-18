# Hero Section — Architectural Review Preparation

**Date:** 2026-07-13  
**Source:** PDP Complete v49.html, docs/04-COMPONENT-LIBRARY.md, Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html, barreletics-decisions-2026-07-09.json, sections/hero.html  
**Purpose:** Inventory only — no recommendations, no styling, no redesign

---

## 1. CURRENT PRODUCTION HERO IN PDP COMPLETE v49

The PDP v49 Hero is a **two-column grid layout** (lines 138–259).

---

### COMPONENT 1: Hero Container

**Lines:** 138–140, 259  
**Purpose:** Wraps the entire above-the-fold PDP experience  

```html
<!-- HERO -->
<section style="background:#fff;">
<section class="pdp-hero" style="display:grid;grid-template-columns:1fr 1fr;gap:64px;max-width:1400px;margin:0 auto;padding:64px 80px 64px 40px;align-items:flex-start;">
```

**Specifications:**
| Property | Value |
|----------|-------|
| Display | grid |
| Columns | 1fr 1fr |
| Gap | 64px |
| Max-width | 1400px |
| Padding | 64px 80px 64px 40px |
| Alignment | flex-start |
| Background | #fff |
| Mobile (≤768px) | single column, gap 32px, padding 32px 16px |

**CSS class definition (line 19):**
```css
.pdp-hero { display: none; grid-template-columns: 1fr 1fr; gap: 64px; max-width: 1400px; margin: 0 auto; padding: 64px 40px; align-items: flex-start; }
```

---

### COMPONENT 2: Product Gallery (Left Column)

**Lines:** 143–153  
**Purpose:** Sticky product image with thumbnail navigation  

```html
<div class="pdp-gallery">
  <div class="pdp-gallery__hero">
    <img id="v10-main-img" src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800" alt="Studio Performance Skin — Onyx" />
  </div>
  <div style="display:flex;gap:6px;margin-top:8px;">
    <button onclick="v10Thumb(this,'...')" style="width:72px;height:72px;border:2px solid #1c1916;background:#f9f9f9;padding:0;cursor:pointer;overflow:hidden;flex-shrink:0;">
      <img ... alt="View 1" />
    </button>
    <!-- 3 more thumbnail buttons with border:1px solid #e6e6e6 -->
  </div>
</div>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Position | sticky |
| Top | 64px |
| Hero image aspect-ratio | 1:1 |
| Hero image border-radius | 8px |
| Hero image background | #f9f9f9 |
| Thumbnail size | 72×72px |
| Thumbnail gap | 6px |
| Active thumbnail border | 2px solid #1c1916 |
| Inactive thumbnail border | 1px solid #e6e6e6 |
| Thumbnail count | 4 |
| Mobile | position: static (loses sticky) |

**CSS class definitions (lines 21–23):**
```css
.pdp-gallery { display: flex; flex-direction: column; gap: 16px; position: sticky; top: 64px; }
.pdp-gallery__hero { aspect-ratio: 1; background: #f9f9f9; overflow: hidden; border-radius: 8px; }
.pdp-gallery__hero img { width: 100%; height: 100%; object-fit: cover; display: block; }
```

**JavaScript (lines 262–266):**
```javascript
function v10Thumb(btn, src) {
  document.querySelectorAll('.pdp-hero button[onclick^="v10Thumb"]').forEach(b => b.style.border = '1px solid #e6e6e6');
  btn.style.border = '2px solid #1c1916';
  document.getElementById('v10-main-img').src = src;
}
```

---

### COMPONENT 3: Star Rating Row

**Lines:** 159–163  
**Purpose:** Social proof + anchor link to reviews section  

```html
<div style="display:flex;align-items:center;gap:10px;">
  <span class="pdp-buy__stars" style="font-size:14px;letter-spacing:1px;">★★★★★</span>
  <span style="font-size:13px;font-weight:400;color:#4a4a4a;">Trusted by 1000's of Instructors</span>
  <span style="color:#d6cfc0;">·</span>
  <a href="#reviews" style="font-size:12px;color:#8a8a8a;font-weight:400;">Reviews →</a>
</div>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Layout | flex, center-aligned, gap 10px |
| Star color | #d4af37 (from CSS class line 27) |
| Star font-size | 14px (inline override of class 16px) |
| Star letter-spacing | 1px (inline override of class 2px) |
| Trust text | 13px, weight 400, color #4a4a4a |
| Separator | · character, color #d6cfc0 |
| Reviews link | 12px, color #8a8a8a, weight 400, anchors to #reviews |

**CSS class definition (line 27):**
```css
.pdp-buy__stars { font-size: 16px; color: #d4af37; letter-spacing: 2px; }
```

---

### COMPONENT 4: SEO Title + Product Type Badge

**Lines:** 169–171  
**Purpose:** H1 for SEO (Shopify product title) + visual sole-type indicator  

```html
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;">
  <h1 style="font-size:18px;letter-spacing:0;color:#2d2926;font-weight:600;margin:0;">Best Grippy Shoes for Barre, Pilates &amp; Yoga</h1>
  <span class="pdp-buy__badge">Closed Sole</span>
</div>
```

**Specifications:**
| Property | Value |
|----------|-------|
| H1 font-size | 18px |
| H1 font-weight | 600 |
| H1 color | #2d2926 |
| H1 letter-spacing | 0 |
| Badge background | #c45c3f (terracotta) |
| Badge color | #fff |
| Badge font-size | 10px |
| Badge font-weight | 700 |
| Badge text-transform | uppercase |
| Badge letter-spacing | 0.08em |
| Badge padding | 4px 10px |
| Badge border-radius | 3px |

**CSS class definition (line 26):**
```css
.pdp-buy__badge { display: inline-block; background: #c45c3f; color: #fff; padding: 4px 10px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; border-radius: 3px; }
```

---

### COMPONENT 5: Marketing Headline

**Lines:** 174  
**Purpose:** Emotional hook — the brand claim that drives conversion  

```html
<p class="pdp-buy__name" style="margin:0;">
  <span style="font-weight:300;">Secure in every hold.</span><br/>
  <span style="font-weight:700;">No sliding. No resets.</span>
</p>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Font-size | 44px |
| Line-height | 1.08 |
| Color | #1c1916 |
| Line 1 weight | 300 (light) |
| Line 2 weight | 700 (bold) |
| Mobile font-size | 32px |

**CSS class definition (line 28):**
```css
.pdp-buy__name { font-size: 44px; font-weight: 700; line-height: 1.08; margin: 0; color: #1c1916; }
```

---

### COMPONENT 6: Product Description

**Lines:** 176  
**Purpose:** One-sentence product explanation below the headline  

```html
<p class="pdp-buy__desc" style="margin-top:20px;max-width:40ch;line-height:1.65;font-weight:400;color:#5a5248;">The premium grip system that replaces traditional grip socks—built for reformer, barre, Pilates and Megaformer.</p>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Font-size | 16px (from class) |
| Color | #5a5248 (inline override of class #4a4a4a) |
| Line-height | 1.65 (inline override of class 1.6) |
| Max-width | 40ch |
| Font-weight | 400 |
| Margin-top | 20px |

**CSS class definition (line 29):**
```css
.pdp-buy__desc { font-size: 16px; color: #4a4a4a; margin: 0; line-height: 1.6; }
```

---

### COMPONENT 7: Price Block

**Lines:** 180–183  
**Purpose:** Primary price display + payment/shipping info  

```html
<div style="padding:16px 0;border-top:1px solid #e6e6e6;border-bottom:1px solid #e6e6e6;">
  <span class="pdp-buy__price-now">$74</span>
  <span style="font-size:13px;color:#8a8a8a;margin-left:8px;">or 4 payments · free shipping over $150</span>
</div>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Price font-size | 36px |
| Price font-weight | 700 |
| Price color | #1c1916 |
| Meta text font-size | 13px |
| Meta text color | #8a8a8a |
| Container padding | 16px 0 |
| Borders | 1px solid #e6e6e6 top and bottom |
| Shipping threshold shown | $150 |

**CSS class definition (lines 30–31):**
```css
.pdp-buy__price-now { font-size: 36px; font-weight: 700; color: #1c1916; }
.pdp-buy__price-meta { font-size: 13px; color: #8a8a8a; }
```

**NOTE:** Price block text says "$150" — this is the ADR-02 conflict ($75 vs $150). The accordion Shipping section (line 251) says "$75".

---

### COMPONENT 8: Color Swatches

**Lines:** 186–208  
**Purpose:** Color variant selection with visual indicator  

```html
<div style="padding:16px 0;border-bottom:1px solid #e6e6e6;">
  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px;">
    <span style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;">Color · <span id="v10-color-name">Onyx</span></span>
    <a href="#variants" style="font-size:12px;text-decoration:none;color:#8a8a8a;font-weight:400;">View all colors →</a>
  </div>
  <div class="pdp-buy__swatches" style="gap:6px;flex-wrap:wrap;row-gap:6px;">
    <button class="pdp-buy__swatch" style="background:#050505;" aria-selected="true" aria-label="Onyx" onclick="v10Color(...)"></button>
    <!-- 10 more standard swatches -->
    <div style="position:relative;display:inline-flex;">
      <button class="pdp-buy__swatch" style="background:#c8b99a;" aria-label="Coperni" onclick="v10Color(...)"></button>
      <span style="position:absolute;top:-2px;right:-2px;background:#2563eb;color:#fff;font-size:8px;font-weight:700;padding:1px 4px;border-radius:2px;line-height:1.4;pointer-events:none;">LE</span>
    </div>
  </div>
</div>
```

**Colors present (12 total):**
| Swatch | Hex | Label |
|--------|-----|-------|
| 1 | #050505 | Onyx |
| 2 | #e9d3cb | Dusty Rose |
| 3 | #c9c5b8 | Stone |
| 4 | #7b8c84 | Sage |
| 5 | #fff | White |
| 6 | #d4a78a | Terracotta |
| 7 | #3d3530 | Espresso |
| 8 | #b8c4c0 | Mist |
| 9 | #e8e0d0 | Cream |
| 10 | #8b7355 | Mocha |
| 11 | #5c6b5e | Forest |
| 12 | #c8b99a | Coperni (LE badge) |

**Specifications:**
| Property | Value |
|----------|-------|
| Swatch size | 23px width/height |
| Swatch border-radius | 50% (circle) |
| Swatch padding | 9px |
| Swatch box-sizing | content-box (actual rendered size ~41px) |
| Active state | border: 2px solid #1c1916, aria-selected="true" |
| Hover state | border-color: #9a9182 |
| Inactive border | 2px solid transparent |
| LE badge | background #2563eb, 8px font, absolute positioned |
| Label display | 12px, weight 700, uppercase, 0.06em spacing |
| "View all" link | 12px, #8a8a8a, anchors to #variants |

**CSS class definitions (lines 34–37):**
```css
.pdp-buy__swatches { display: flex; gap: 8px; flex-wrap: wrap; }
.pdp-buy__swatch { width: 23px; height: 23px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; transition: all 0.2s; padding: 9px; box-sizing: content-box; background-clip: content-box; }
.pdp-buy__swatch:hover { border-color: #9a9182; }
.pdp-buy__swatch[aria-selected="true"] { border-color: #1c1916; outline: none; }
```

**JavaScript (lines 267–272):**
```javascript
function v10Color(btn, name, src) {
  document.querySelectorAll('.pdp-buy__swatch').forEach(s => s.removeAttribute('aria-selected'));
  btn.setAttribute('aria-selected','true');
  document.getElementById('v10-color-name').textContent = name;
  document.getElementById('v10-main-img').src = src;
}
```

---

### COMPONENT 9: Size Selector

**Lines:** 211–219  
**Purpose:** Size variant selection (M/L only)  

```html
<div style="padding:16px 0;border-bottom:1px solid #e6e6e6;">
  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px;">
    <span style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;">Size</span>
    <a href="#" style="font-size:12px;text-decoration:none;color:#1c1916;border-bottom:1px solid #1c1916;padding-bottom:1px;">Size Chart →</a>
  </div>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;">
    <button style="padding:14px;border:1px solid #e6e6e6;background:#faf9f7;text-align:center;cursor:pointer;font-size:14px;font-weight:600;border-radius:6px;font-family:inherit;" onclick="v10Size(this,'M')">M<span style="display:block;font-size:11px;color:#8a8a8a;font-weight:400;margin-top:4px;">Women 5–7.5 · Men 6–8</span></button>
    <button style="padding:14px;border:2px solid #1c1916;background:#faf9f7;text-align:center;cursor:pointer;font-size:14px;font-weight:600;border-radius:6px;font-family:inherit;" onclick="v10Size(this,'L')">L<span style="display:block;font-size:11px;color:#8a8a8a;font-weight:400;margin-top:4px;">Women 8–10 · Men 8.5–11</span></button>
  </div>
</div>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Layout | 2-column grid, gap 12px |
| Button padding | 14px |
| Button border-radius | 6px (**ADR-03 conflict**) |
| Button background | #faf9f7 |
| Button font-size | 14px |
| Button font-weight | 600 |
| Active border | 2px solid #1c1916 |
| Inactive border | 1px solid #e6e6e6 |
| Size range text | 11px, #8a8a8a, weight 400 |
| "Size Chart" link | 12px, #1c1916, underlined |
| Label | 12px, weight 700, uppercase, 0.06em spacing |

**JavaScript (lines 273–278):**
```javascript
function v10Size(btn, name) {
  document.querySelectorAll('[onclick^="v10Size"]').forEach(s => { s.style.border='1px solid #e6e6e6'; s.style.background='#faf9f7'; });
  btn.style.border = '2px solid #1c1916';
  btn.style.background = '#f9f9f9';
}
```

---

### COMPONENT 10: Add to Cart CTA

**Lines:** 223  
**Purpose:** Primary conversion action  

```html
<button class="pdp-buy__cta">Add to cart · $74</button>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Width | 100% |
| Padding | 18px |
| Background | #1c1916 |
| Color | #fff |
| Font-size | 15px |
| Font-weight | 700 |
| Letter-spacing | 0.06em |
| Text-transform | uppercase |
| Border | none |
| Border-radius | 4px (**ADR-03 conflict**) |
| Hover background | #c45c3f (terracotta) |
| Font-family | inherit |

**CSS class definition (lines 32–33):**
```css
.pdp-buy__cta { width: 100%; padding: 18px; background: #1c1916; color: #fff; font-size: 15px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; border: none; border-radius: 4px; cursor: pointer; font-family: inherit; }
.pdp-buy__cta:hover { background: #c45c3f; }
```

---

### COMPONENT 11: Trust Row

**Lines:** 226–231  
**Purpose:** Reduce purchase anxiety with shipping/return/safety assurances  

```html
<div style="display:flex;gap:20px;flex-wrap:wrap;font-size:12px;color:#8a8a8a;padding:12px 0;border-top:1px solid #e6e6e6;">
  <span><b style="color:#1c1916;">✓</b> Ships 1–2 days</span>
  <span><b style="color:#1c1916;">✓</b> 30-day returns</span>
  <span><b style="color:#1c1916;">✓</b> 90-day warranty</span>
  <span><b style="color:#1c1916;">✓</b> Latex- &amp; silicone-free</span>
</div>
```

**Specifications:**
| Property | Value |
|----------|-------|
| Layout | flex, wrap, gap 20px |
| Font-size | 12px |
| Text color | #8a8a8a |
| Checkmark color | #1c1916 (bold) |
| Border-top | 1px solid #e6e6e6 |
| Padding | 12px 0 |
| Items | 4 trust signals |

**Trust claims:**
1. Ships 1–2 days
2. 30-day returns
3. 90-day warranty
4. Latex- & silicone-free

---

### COMPONENT 12: Product Accordion

**Lines:** 234–257  
**Purpose:** Expandable information sections (Description, Care, Shipping, Returns)  

```html
<div style="border-top:1px solid #e6e6e6;">
  <details style="border-bottom:1px solid #e6e6e6;">
    <summary style="padding:14px 0;font-size:14px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;">Description <span>+</span></summary>
    <div style="padding:0 0 16px;font-size:14px;color:#4a4a4a;line-height:1.7;">
      <!-- content -->
    </div>
  </details>
  <!-- 3 more <details> items -->
</div>
```

**Accordion items:**

| # | Title | Content summary |
|---|-------|----------------|
| 1 | Description | Full product description (2 paragraphs) |
| 2 | Care & how to wear | How to put on + cleaning instructions |
| 3 | Shipping | "Free shipping on orders over $75. Standard 3–5 days. Express 1–2 days." |
| 4 | 30-day returns + 90-day warranty | Return conditions + warranty coverage |

**Specifications:**
| Property | Value |
|----------|-------|
| Element | native `<details>/<summary>` |
| Summary padding | 14px 0 |
| Summary font-size | 14px |
| Summary font-weight | 600 |
| Summary color | inherit (#1c1916) |
| Toggle indicator | + character (right-aligned) |
| Body font-size | 14px |
| Body color | #4a4a4a |
| Body line-height | 1.7 |
| Body padding | 0 0 16px |
| Separator | border-bottom: 1px solid #e6e6e6 |

**NOTE:** Accordion item 3 (Shipping) says "$75" — contradicts the price block which says "$150". This is ADR-02.

---

### COMPONENT 13: Hero Toggle (CSS defined, NOT rendered in v49)

**Lines:** 15–17 (CSS only)  
**Purpose:** Toggle between hero variants (e.g., Open Sole vs Closed Sole hero)  

```css
.hero-toggle { display: flex; gap: 8px; margin-bottom: 24px; }
.hero-toggle__btn { padding: 8px 16px; border: 1px solid #d6cfc0; background: #fff; cursor: pointer; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; transition: all 0.2s; }
.hero-toggle__btn[data-active="true"] { background: #1c1916; color: #fff; border-color: #1c1916; }
```

**Status:** CSS exists but **no HTML buttons are rendered** in v49. The toggle JS is present (lines 662–670) but has no matching DOM elements. This is a dormant capability.

**JavaScript (lines 662–670):**
```javascript
document.querySelectorAll('.hero-toggle__btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const version = this.dataset.version;
    document.querySelectorAll('.pdp-hero').forEach(hero => hero.removeAttribute('data-active'));
    document.querySelector(`[data-version="${version}"]`).setAttribute('data-active', 'true');
    document.querySelectorAll('.hero-toggle__btn').forEach(b => b.removeAttribute('data-active'));
    this.setAttribute('data-active', 'true');
  });
});
```

---

## 2. DESIGN MATRIX HERO (Section 01)

**From `barreletics-decisions-2026-07-09.json`:**

```
"01": {
  "name": "Hero",
  "decision": "Keep",
  "owner": "Cowork",
  "notes": "Create the option to have the see in action button. Use the eyebrow from current",
  "version": "custom"
}
```

**From `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html`:**
- Section ID: 01
- Name: Hero
- Description: "Opening statement"
- Decision: **Keep** (with modifications)

**CEO directives for Hero:**
1. Add a "See in Action" button option
2. Use the eyebrow rotator from the current live site
3. Version: "custom" (not pure current, not pure matured)

---

## 3. COMPONENT LIBRARY HERO (docs/04)

**From `docs/04-COMPONENT-LIBRARY.md` (lines 91–110):**

| Component | Documented |
|-----------|-----------|
| Purpose | Communicate core brand promise with rotating messaging |
| Business goal | Set brand tone and communicate key differentiator |
| User goal | Understand what Barreletics is |
| Design rules | Full viewport width and height, centered text overlay |
| Hero image | barreletics.com/cdn/shop/files/IMG_2917.jpg |
| Mobile | Stack vertically, reduce image height, maintain full bleed |
| Desktop | Full bleed, centered layout |
| Eyebrow rotation | Multiple rotating statements (3.5s cycle per animation rules) |

**Placement rules (docs/04 line 1035–1036):**
- Hero → Directly below header
- Pillar strip → After hero (all pages)

---

## 4. COMPARISON MATRIX

| Element | v49 PDP Hero | Design Matrix | Component Library | Conflict? |
|---------|-------------|---------------|-------------------|-----------|
| Layout | 2-col grid (gallery + buy) | Not specified | Full viewport, centered text | **YES** — different page types |
| Eyebrow rotator | NOT present | "Use the eyebrow from current" | Yes — rotating statements | **YES** — Matrix says add it |
| "See in Action" button | NOT present | "Create the option" | Not mentioned | **YES** — Matrix says add it |
| Hero image | Product photo (sticky gallery) | Not specified | Full-bleed lifestyle photo (IMG_2917.jpg) | **Context** — PDP vs Homepage |
| Star rating | Present (above title) | Not mentioned | Not mentioned | No conflict |
| Color swatches | Present (12 colors) | Not mentioned | Not mentioned | No conflict |
| Size selector | Present (M/L grid) | Not mentioned | Not mentioned | No conflict |
| CTA | "Add to cart · $74" | Not mentioned | Not mentioned | No conflict |
| Accordion | 4 items (details/summary) | Not mentioned | Not mentioned | No conflict |
| Trust row | 4 checkmarks | Not mentioned | Not mentioned | No conflict |

---

## 5. COMPONENTS AVAILABLE IN DESIGN MATRIX / COMPONENT LIBRARY — NOT IN v49 HERO

| Component | Source | What it provides | Currently missing from v49 |
|-----------|--------|-----------------|---------------------------|
| **Eyebrow rotator** | Design Matrix decision, Component Library, sections/hero.html | Rotating text statements above headline (3.5s cycle) | Not present in v49 Hero |
| **"See in Action" button** | Design Matrix CEO note | CTA linking to video/motion content | Not present in v49 Hero |
| **Full-bleed lifestyle background** | Component Library (IMG_2917.jpg reference) | Full viewport hero with centered overlay | v49 uses product gallery instead (PDP context) |
| **Hero toggle buttons** | v49 CSS (lines 15–17, defined but unused in v49) | Ability to switch between hero variants | CSS exists but no toggle buttons rendered |

---

## 6. COMPONENTS THAT CONFLICT WITH v49 HERO

| Component | Conflict | Nature |
|-----------|----------|--------|
| **Full-viewport hero** (Component Library) | v49 Hero is a 2-column product layout, not full-bleed | **Context conflict** — Component Library describes a Homepage hero; v49 is a PDP hero. These are different page types. |
| **Centered text overlay** (Component Library) | v49 has text in right column alongside gallery | Same context conflict — Homepage vs PDP |
| **border-radius: 8px** on gallery image | Design System says 0px for all elements | **ADR-03 conflict** (already documented) |
| **CTA border-radius: 4px** | Design System says 0px buttons | **ADR-03 conflict** (already documented) |
| **Size selector border-radius: 6px** | Design System says 0px buttons | **ADR-03 conflict** (already documented) |

---

## 7. COMPONENTS THAT COULD STRENGTHEN v49 HERO WITHOUT REDESIGNING

| Component | Source | How it fits | Implementation notes |
|-----------|--------|-------------|---------------------|
| **Eyebrow rotator** | Design Matrix + Component Library | Add above star rating row as a thin animated text strip | Non-destructive addition; CSS from sections/hero.html already exists |
| **"See in Action" link/button** | Design Matrix CEO note | Add as secondary link below trust row or within accordion | Minimal change — link to Motion section (#motion) already on page |
| **Hero toggle** (Closed/Open Sole) | v49 CSS already defines `.hero-toggle` | Allow switching the hero between product types without leaving page | CSS already written (lines 15–17); just needs HTML buttons rendered |

---

## SUMMARY

- **v49 Hero is a PDP hero** (product gallery + buy box). It is NOT a homepage hero.
- **Component Library describes a Homepage hero** (full-bleed, centered text, lifestyle image).
- **These are architecturally different components** serving different pages.
- **Design Matrix decision:** Keep the hero structure but add eyebrow rotator + "See in Action" button.
- **3 non-destructive additions** are available from existing repository assets.
- **3 border-radius conflicts** are already tracked in ADR-03.
- **No redesign required** to incorporate the Matrix directives.
