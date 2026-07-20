# 22 — Accessibility Decisions

---
document: 22 – Accessibility Decisions
status: Reference
last_modified: 2026-07-19
depends_on: [02-theme-architecture, 07-css-architecture]
---

## Overview

The Barreletics theme targets WCAG 2.1 AA compliance with systematic implementation across all components. Accessibility is built into the architecture — not bolted on.

---

## Skip Navigation

`layout/theme.liquid` includes a skip link as the first focusable element in `<body>`:

```html
<a href="#main-content" class="skip-link">Skip to content</a>
```

The main content landmark:

```html
<main id="main-content" role="main" tabindex="-1">
  {{ content_for_layout }}
</main>
```

### Skip Link Styling

Defined inline in `theme.liquid` (lines 182–199):
- Hidden above viewport (`top: -100%`)
- Appears on focus at `top: 16px`
- Styled with charcoal background (`var(--color-charcoal)`), white text
- `z-index: 9999` to appear above all content
- `border-radius: var(--radius-button)` (6px)

A duplicate `.skip-link` class also exists in `barreletics-base.css` (lines 137–149) with `top: -100%` → `top: 8px` on focus, centered via `translateX(-50%)`.

---

## Focus Management

### Cart Drawer

`assets/cart.js` implements full focus management for the cart drawer dialog:

**Open:** `openDrawer()` (line 80–88)
1. Stores `triggerEl = document.activeElement` (the element that triggered the open)
2. Adds `is-open` class, sets `aria-hidden="false"`
3. Locks body scroll (`document.body.style.overflow = 'hidden'`)
4. Focuses the first focusable element inside the drawer

**Close:** `closeDrawer()` (line 90–97)
1. Removes `is-open` class, sets `aria-hidden="true"`
2. Restores body scroll
3. Returns focus to `triggerEl` (`triggerEl.focus()`)

**Focus Trap:** `cart.js` (lines 285–316)
- Listens for `Tab` keydown when drawer is open
- Queries all focusable elements within `.cart-drawer__panel`
- On Tab at last element → wraps to first
- On Shift+Tab at first element → wraps to last
- Escape key closes the drawer

### Mobile Menu

`snippets/header-nav.liquid` (lines 366–392):
- `openMenu()` — adds `is-open`, sets `aria-hidden="false"`, sets toggle `aria-expanded="true"`, locks body scroll
- `closeMenu()` — removes `is-open`, sets `aria-hidden="true"`, sets toggle `aria-expanded="false"`, restores scroll
- Escape key closes menu (line 382)
- Overlay click closes menu (bound to `[data-mobile-menu-close]`)

### PDP Accordions

`sections/pdp-buy-box.liquid` (lines 524–530):
- `<details>` elements with `data-pdp-accordion` attribute
- JS listens for `toggle` event on each `<details>`
- Sets `aria-expanded` on the `<summary>` to match `item.open` state

---

## Focus-Visible Indicators

Defined in `assets/barreletics-base.css` (lines 112–121):

```css
:focus-visible {
  outline: 2px solid var(--color-charcoal);
  outline-offset: 2px;
}

[data-theme="dark"] :focus-visible,
.section--dark :focus-visible {
  outline-color: var(--color-white);
}

:focus:not(:focus-visible) {
  outline: none;
}
```

- `:focus-visible` — keyboard users get a 2px solid charcoal outline with 2px offset
- Dark sections/`[data-theme="dark"]` — outline switches to white
- `:focus:not(:focus-visible)` — mouse/touch users see no outline (prevents visual noise on click)

---

## ARIA Patterns

### Color Swatches (`pdp-buy-box.liquid`)

```html
<button
  class="pdp-buy__swatch"
  aria-label="{{ value }}"
  aria-selected="{% if value == option.selected_value %}true{% else %}false{% endif %}"
  data-color="{{ value }}"
>
</button>
```

`variant-selector.js` (lines 63–68) toggles `aria-selected` on selection:

```javascript
if (el.hasAttribute('aria-selected')) {
  el.setAttribute('aria-selected', match ? 'true' : 'false');
}
```

### Size Buttons (`variant-selector.js`)

`updateAvailability()` (lines 147–165) sets `aria-disabled` based on variant stock:

```javascript
btn.setAttribute('aria-disabled', !available ? 'true' : 'false');
```

Unavailable sizes are also visually indicated with `is-unavailable` class and `disabled` property.

### Cart Drawer (`snippets/cart-drawer.liquid`)

```html
<div
  id="cart-drawer"
  class="cart-drawer"
  aria-hidden="true"
  aria-label="Shopping cart"
  role="dialog"
  aria-modal="true"
>
```

- `role="dialog"` + `aria-modal="true"` — announces as modal dialog
- `aria-hidden` toggled by `openDrawer()`/`closeDrawer()` in `cart.js`
- `aria-label="Shopping cart"` — labels the dialog for screen readers

### Mobile Menu (`snippets/header-nav.liquid`)

```html
<div class="mobile-menu" id="mobile-menu" data-mobile-menu aria-hidden="true">
  ...
  <div class="mobile-menu__drawer" role="dialog" aria-label="Navigation menu">
```

Toggle button:
```html
<button
  class="site-header__hamburger"
  data-mobile-menu-toggle
  aria-expanded="false"
  aria-controls="mobile-menu"
  aria-label="Open menu"
>
```

- `aria-hidden` on container toggled by open/close functions
- `aria-expanded` on hamburger toggle reflects menu state
- `aria-controls="mobile-menu"` links button to the controlled element
- `aria-label` on drawer and toggle provide accessible names
- Accordion sub-menu toggles set `aria-expanded` on `<button class="mobile-menu__toggle">`

### Breadcrumb (`snippets/breadcrumb.liquid`)

```html
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol class="breadcrumb__list" role="list">
    ...
    <li class="breadcrumb__item breadcrumb__item--current" aria-current="page">
      {{ product.title }}
    </li>
  </ol>
</nav>
```

- `aria-label="Breadcrumb"` — identifies the navigation landmark
- `aria-current="page"` — marks the current page in the trail
- Separators use `aria-hidden="true"` on the `›` character

### Announcement Strip

The announcement strip snippet uses `role="region"` with `aria-label` for screen reader identification. Message rotation is managed by JS with `setInterval`.

### Live Region (Cart Status)

`assets/cart.js` (lines 12–19) creates a live region on initialization:

```javascript
liveRegion = document.createElement('div');
liveRegion.setAttribute('aria-live', 'polite');
liveRegion.setAttribute('aria-atomic', 'true');
liveRegion.className = 'visually-hidden';
liveRegion.id = 'cart-live-region';
document.body.appendChild(liveRegion);
```

The `announce()` function (line 250) updates this region:
- "Item added to cart" — after successful add
- "Cart updated" — after quantity change
- "Item removed from cart" — after removal

Screen readers announce these messages without disrupting the user's current focus.

---

## Heading Hierarchy

| Level | Usage | Location |
|-------|-------|----------|
| H1 | Product title | `pdp-buy-box.liquid` → `.pdp-buy__seo-title` |
| H1 | Page title (home, collection) | Hero sections |
| H2 | Cart drawer title ("Your Cart") | `cart-drawer.liquid` → `.cart-drawer__title` |
| H2 | Section headings | Throughout sections |
| H3 | Footer column headings | `footer.liquid` |
| H3 | Card headings | Review cards, product cards |

Each page has exactly one H1. Sections use H2/H3 appropriate to their nesting depth.

---

## Color Contrast

| Combination | Ratio | WCAG Level | Usage |
|-------------|-------|------------|-------|
| Charcoal `#1c1916` on white `#ffffff` | 15.3:1 | AAA | Primary headings, navigation |
| Body `#4a4a4a` on white `#ffffff` | 7.7:1 | AA | Body text, descriptions |
| Muted `#8a8a8a` on white `#ffffff` | 3.5:1 | — | Non-critical labels, captions only |
| Gold stars `#d4af37` | — | Decorative | Numeric rating provides accessible value |
| White on charcoal `#1c1916` | 15.3:1 | AAA | Dark sections, buttons |

The muted color (`#8a8a8a`) is intentionally below AA for large text. It is used only for supplementary labels (breadcrumb separators, metadata, price annotations) where the information is also conveyed through other means.

Gold stars are decorative — the text "Trusted by 1,000+ Instructors" and linked review count provide the accessible information.

---

## Reduced Motion

Implemented in two locations for redundancy:

### `assets/barreletics-base.css` (lines 186–192)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### `layout/theme.liquid` (lines 203–211, inline `<style>`)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Both use `0.01ms` (not `0`) to avoid breaking JS that depends on `transitionend` or `animationend` events. The announcement strip JS also checks `window.matchMedia('(prefers-reduced-motion: reduce)')` and skips message rotation if true.

---

## Touch Target Sizing

All interactive elements maintain a minimum 44×44px touch target:

### Header Navigation (`header-nav.liquid`)

| Element | Implementation |
|---------|---------------|
| `.site-header__hamburger` | `min-width: 44px; min-height: 44px` |
| `.site-header__action` (Help, Account, Cart) | `min-width: 44px; min-height: 44px` |
| `.mobile-menu__close` | `min-width: 44px; min-height: 44px; padding: 12px` |
| `.mobile-menu__toggle` | `min-height: 44px` |
| `.mobile-menu__sub li a` | `min-height: 44px; padding: 10px 0` |
| `.mobile-menu__utility li a` | `min-height: 44px; padding: 10px 0` |

### Footer

| Element | Implementation |
|---------|---------------|
| `.site-footer__links a` | `min-height: 44px` via padding |
| `.site-footer__social a` | `min-width: 44px; min-height: 44px` |
| `.site-footer__submit` | Meets minimum via button padding |

### Cart Drawer

All buttons (close, quantity +/−, remove, checkout) meet 44px minimum through padding and min-height.

### Breadcrumb

`.breadcrumb__link` uses `min-height: 44px; display: inline-flex; align-items: center;` to ensure tap targets.

---

## Keyboard Navigation

| Key | Behavior |
|-----|----------|
| Tab | Follows DOM order through all interactive elements |
| Shift+Tab | Reverse tab order |
| Escape | Closes cart drawer, closes mobile menu |
| Enter/Space | Activates buttons, opens accordions |
| Tab (in cart drawer) | Trapped within `.cart-drawer__panel` when open |

### Focus Order

DOM order defines tab order. No `tabindex` values above 0 are used. The only `tabindex="-1"` is on `<main id="main-content">` to allow programmatic focus from the skip link.

---

## Visually Hidden Utility

`assets/barreletics-base.css` (lines 125–135):

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

Used for:
- Cart live region announcements (`cart.js` creates an element with this class)
- Any content that must be accessible to screen readers but not visible

---

## Decorative Elements

All decorative SVGs use `aria-hidden="true"`:

```html
<svg width="20" height="14" viewBox="0 0 20 14" fill="none" aria-hidden="true">
```

Star ratings use `aria-hidden="true"` on the visual stars with separate text providing the accessible value:

```html
<span class="pdp-buy__stars" aria-hidden="true">★★★★★</span>
<span class="pdp-buy__rating-text">Trusted by 1,000+ Instructors</span>
```

---

## Form Accessibility

- PDP form uses a hidden input (`input[name="id"]`) for variant ID — not user-facing
- Submit button text includes price context ("Add to Cart — $74")
- Error messages use `role="alert"` (`cart.js:243`)
- Quantity buttons have explicit `aria-label` ("Decrease quantity", "Increase quantity")
- Remove buttons have contextual `aria-label` ("Remove {{ item.title }}")

---

**Cross-references:**
- Focus indicators in CSS → `docs/07-css-architecture.md`
- Design tokens (colors, radii) → `docs/23-design-token-reference.md`
- Cart drawer architecture → `docs/12-data-flow.md`
- QA validation results → `planning/m4c-qa-report.md` (A11Y-001 through A11Y-013)
