# Sticky / fixed audit — shipping theme (`shopify-build/`)

**Date:** 2026-08-07 · **Scope:** does the FAQ-mock `overflow-x: hidden` sticky defect exist in the shipping theme?
**Method:** measured, not inferred. `planning/mobile-qa/sticky-probe.py` · raw data `planning/mobile-qa/sticky-probe-results.json`

---

## Headline

| Element | Mobile (390px) | Desktop (1280px) |
|---|---|---|
| **Sticky Add to Cart** (`pdp-sticky-atc`) | **NOT broken** — holds the viewport bottom at every scroll depth | not broken |
| **Sticky header** (`.site-header`) | **WAS broken** — scrolled fully off screen. **Fixed.** | **Also was broken.** Fixed. |
| PDP gallery sticky column | `position: static` — deliberate, correct | sticks correctly |

**The reported `overflow-x: hidden` root cause does not exist in `shopify-build/`.** No `html` or `body`
overflow rule exists anywhere in the theme's CSS, Liquid, or layout. The sticky header was broken by a
**different** and unrelated cause: the Shopify section-group wrapper.

---

## 1. `overflow-x` sweep — clean

Searched every `shopify-build/assets/*.css`, `sections/*.liquid`, `snippets/*.liquid`, `layout/*.liquid`.

* `assets/barreletics-base.css:9` — `html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }`
* `assets/barreletics-base.css:10-19` — `body { … }` typography and colour only

Neither sets `overflow`, `overflow-x`, or `overflow-y`. Measured confirmation: computed
`html` and `body` `overflow-x` = `visible` at both widths.

Every other `overflow` in the theme is a legitimate local clip or touch-scroller
(card media, gallery thumbs, variant tabs, trust strip, mobile drawer). **None of them is an
ancestor of any sticky or fixed element.** No `transform`, `filter`, `perspective`, `will-change`,
or `contain` was found on any ancestor of a sticky/fixed element either — the ancestor-chain
walk in the probe reports zero breakers for both the header and the ATC bar.

## 2. Sticky / fixed inventory

| Element | File | Position | Verdict |
|---|---|---|---|
| Sticky ATC bar | `snippets/sticky-atc.liquid:51` (via `sections/pdp-sticky-atc.liquid`) | `fixed` | Works |
| Site header | `assets/chrome.css:59` | `sticky` | Was broken → fixed |
| Mobile menu | `assets/chrome.css:222` | `fixed` | Works |
| Cart drawer | `snippets/cart-drawer.liquid:90` | `fixed` | Works |
| PDP gallery column | `sections/pdp-buy-box.liquid:356` | `sticky`, forced `static` ≤768px at `:773-775` | Correct as designed |
| Contact info column | `sections/page-contact.liquid:225` | `sticky` | Works desktop; no travel in the mobile single column (cosmetic only) |

`snippets/header-nav.liquid` also defines `.site-header { position: fixed }`, but that snippet is
**orphaned** — nothing renders it. It is dead code and does not affect the storefront.

## 3. Sticky ATC — proven working

`.sticky-atc` is `position: fixed; bottom: 0`. Fixed positioning is **not** affected by `overflow`
on `html`/`body`; only `transform`/`filter`/`will-change`/`contain` on an ancestor breaks it, and
none is present.

Measured at a verified 390×844 viewport, bar forced visible, `atcBottom` = distance from viewport
top to the bar's bottom edge (should equal viewport height 844 at all times):

```
scrollY=0     atcBottom=844
scrollY=1500  atcBottom=844
scrollY=3000  atcBottom=844
scrollY=5787  atcBottom=844   (document bottom)
```

It also stayed pinned in the deliberately sabotaged `html,body{overflow-x:hidden}` control, which
confirms the mechanism: that CSS gotcha kills `sticky`, not `fixed`.

Supporting checks: the IntersectionObserver target `[data-buy-box]` exists
(`sections/pdp-buy-box.liquid:52`) and renders before the ATC section in the locked `product.json`
spine, and `window.BarreleticsCart` is defined (`assets/cart.js:297`), so the button's add-to-cart
path is live. **No evidence that the sticky ATC contributes to the Paid Social add-to-cart collapse.**

## 4. Sticky header — the real bug, and the fix

### Root cause

`layout/theme.liquid:88` renders `{% sections 'header-group' %}`. Shopify wraps every section-group
member in its own `<div id="shopify-section-…" class="shopify-section shopify-section-group-header-group …">`.
`assets/chrome.css` put `position: sticky` on the inner `<header class="site-header">`.

A sticky element can only travel inside its **parent's** box. That wrapper div is exactly header
height — measured **57px** for a 57px header — so the header had **zero scroll room** and scrolled
away like a static element. This is a structural Shopify-OS-2.0 issue, unrelated to overflow, and it
affected **desktop as well as mobile**.

### Measured proof (`headerTop` should stay at 0 once stuck)

| Variant | scrollY 0 | 1500 | 3000 | bottom |
|---|---|---|---|---|
| Before fix, real Shopify DOM @390px | 36 | **−1464** | **−2964** | **−5751** |
| Control: header with no wrapper @390px | 36 | 0 | 0 | 0 |
| **After fix, real Shopify DOM @390px** | 36 | **0** | **0** | **0** |
| **After fix, real Shopify DOM @1280px** | 36 | **0** | **0** | **0** |

`36` at rest is the announcement strip height; the strip scrolls away and the header then pins at 0,
which is the intended behaviour.

### Fix applied

1. **`shopify-build/assets/chrome.css:53-57`** — new rule making the section wrapper the sticky
   element. `.header-section` is already emitted onto the wrapper by the header schema's
   `"class": "header-section"` (`sections/header.liquid:194`), so no markup change was needed.

```css
.header-section { position: sticky; top: 0; z-index: var(--z-header); }
```

2. **`shopify-build/sections/header.liquid:26-29`** — the existing Theme Editor **Sticky header**
   checkbox previously worked by adding `.site-header--static` to the inner header, which no longer
   controls anything. When the toggle is off the section now scopes its own wrapper back to static:

```liquid
{%- unless sticky_header -%}
  <style>#shopify-section-{{ section.id }} { position: static; }</style>
{%- endunless -%}
```

Verified: with the toggle off the header scrolls away as before (`headerTop` −1464 / −2964).

The existing `.site-header { position: sticky }` rule was **left in place** — inside a
zero-room wrapper it is inert, and removing it would change nothing while widening the diff.
Desktop layout, spacing, z-order, and the locked footer CSS are untouched.

## 5. Correction to the original lead

The two QA findings were **not** the same root cause.

`docs/Barreletics PDP - Definitive-v19.html` has **no sticky header and no sticky ATC markup at all** —
it is a page mock, not a full theme, and it has no `html`/`body` `overflow-x` either. So
"PDP v19 has no sticky nav on mobile" is a property of the mock's scope, not a bug the mock inherited.
The FAQ v7 `overflow-x` finding is real for that mock but does not propagate to `shopify-build/`.

## 6. Needs Andrew's decision

* **Nothing blocking.** The fix is behaviour-restoring only; it does not alter any locked composition
  or the PDP spine.
* **Not deployed.** No `shopify` CLI command was run and no theme ID was authorised. This needs a push
  to a disposable draft (`187144929571` M4 Visual QA) and visual sign-off before it can be frozen.
* **Optional, pre-existing:** the sticky header creates a stacking context, so the mobile menu
  (`--z-modal: 60`) is capped beneath the announcement strip (`--z-header + 1 = 41`) when the menu is
  opened at the very top of the page. This behaviour predates the fix and is unchanged by it. Worth a
  look on the draft, but only cosmetic.
