# 11 — Navigation Architecture

> Technical reference for header, footer, mobile menu, and announcement strip.
> Source files: `snippets/header-nav.liquid`, `snippets/footer.liquid`, `snippets/announcement-strip.liquid`

---

## Header (`snippets/header-nav.liquid`)

The `<header>` element uses class `.site-header` with `data-site-header` and `role="banner"`.

### Scroll behavior

| State | Class | Background | Border |
|-------|-------|-----------|--------|
| Top of page (scrollY ≤ 8) | — | `transparent` | `transparent` |
| Scrolled (scrollY > 8) | `.is-scrolled` | `var(--color-white)` | `var(--color-warm-border)` |

Applied by `checkScroll()` — toggles `.is-scrolled` on `[data-site-header]`. Bound to `scroll` with `{ passive: true }`. Called once on load for initial state.

```
position: fixed; top: 0; left: 0; right: 0; z-index: var(--z-header)
transition: background 200ms ease, border-color 200ms ease
```

### Inner layout

`.site-header__inner` — flexbox, `height: 56px`, `max-width: var(--max-width)`, `padding: 0 var(--section-padding-x)`. Contains three children in source order:

1. **Hamburger** — `.site-header__hamburger` (`display: none` on desktop, `display: flex` below 768px). Attributes: `data-mobile-menu-toggle`, `aria-expanded="false"`, `aria-controls="mobile-menu"`, `aria-label="Open menu"`. 44×44px touch target.

2. **Logo** — `a.site-header__logo` with `aria-label="{{ shop.name }}"`. Inner `span.site-header__logo-text` renders `BARRELETICS` (15px, `var(--weight-bold)`, `var(--tracking-brand)`, uppercase).

3. **Primary nav** — `nav.site-header__nav` with `aria-label="Main navigation"`. Contains `ul.site-header__nav-list` (flexbox, `gap: 28px`).

### Primary nav items

| Label | href | Subnav? |
|-------|------|---------|
| Grippy Shoes | `/collections/grippy-shoes` | Yes — `.site-header__nav-item--has-sub` |
| Apparel | `/collections/apparel` | Yes |
| Collaborations | `/collections/collaborations` | No |
| Journal | `/blogs/journal` | No |

**Grippy Shoes subnav** (`ul.site-header__subnav`):

| Label | href |
|-------|------|
| Shop All | `/collections/grippy-shoes` |
| Open Sole | `/collections/open-sole` |
| Closed Sole | `/collections/closed-sole` |
| Outdoor | `/collections/outdoor` |
| Compare Styles | `/pages/compare-open-closed-sole` |

**Apparel subnav:**

| Label | href |
|-------|------|
| Shop All Apparel | `/collections/apparel` |
| Tops | `/collections/tops` |
| Bottoms | `/collections/bottoms` |

### Desktop dropdown behavior

`.site-header__subnav` is positioned `absolute`, `top: 100%`, `left: -12px`. Default state: `opacity: 0`, `pointer-events: none`, `transform: translateY(4px)`. Activated by:

```css
.site-header__nav-item--has-sub:hover .site-header__subnav,
.site-header__nav-item--has-sub:focus-within .site-header__subnav {
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
}
```

Transition uses `var(--transition-fast)` for both `opacity` and `transform`. Box shadow: `var(--shadow-md)`. Border radius: `var(--radius-card-sm)`.

### Utility actions

`.site-header__actions` — flexbox, `gap: 20px`. All action links are 44×44px touch targets.

| Action | href | Class modifier | Visibility |
|--------|------|---------------|------------|
| Help | `/pages/faq` | `.site-header__action--help` | Hidden below 768px (`display: none`) |
| Account | `/account` | — | Always visible |
| Cart | `/cart` | `.site-header__cart` | Always visible |

**Cart badge:** `span.site-header__cart-badge[data-cart-count]` renders inside the cart link when `cart.item_count > 0`. Coral dot (16×16px, `border-radius: 50%`, `background: var(--color-coral)`, 9px white bold text). Updated by `cart.js` via `updateCartCount()` which targets `[data-cart-count]`.

The cart link has `data-cart-trigger` — `cart-drawer.liquid` binds a click listener that calls `BarreleticsCart.open()` with `e.preventDefault()`.

---

## Mobile Navigation

### Structure

`.mobile-menu` (`id="mobile-menu"`, `data-mobile-menu`, `aria-hidden="true"`) is a fixed overlay (`inset: 0`, `z-index: var(--z-modal)`). Default state: `pointer-events: none`, `visibility: hidden`.

Children:
1. **Overlay** — `.mobile-menu__overlay[data-mobile-menu-close]`, semi-transparent background `rgba(28, 25, 22, 0.4)`, opacity 0 → 1 on `.is-open`.
2. **Drawer** — `.mobile-menu__drawer` (`role="dialog"`, `aria-label="Navigation menu"`). Left-anchored, `width: 300px`, `max-width: 85vw`. Slides in via `transform: translateX(-100%) → translateX(0)`, transition: `var(--transition-base)`.

### Open/close

| Trigger | Action |
|---------|--------|
| Click hamburger (`[data-mobile-menu-toggle]`) | `openMenu()` — adds `.is-open`, sets `aria-hidden="false"`, sets hamburger `aria-expanded="true"`, locks body scroll |
| Click overlay or close button (`[data-mobile-menu-close]`) | `closeMenu()` — removes `.is-open`, sets `aria-hidden="true"`, sets hamburger `aria-expanded="false"`, restores body scroll |
| Press `Escape` (any key) | `closeMenu()` if `.is-open` is present |

### Accordion sub-items

Parent items (`.mobile-menu__item--parent`) contain a `button.mobile-menu__toggle` with `aria-expanded="false"`. On click:

```js
var expanded = item.getAttribute('data-expanded') === 'true';
item.setAttribute('data-expanded', expanded ? 'false' : 'true');
toggle.setAttribute('aria-expanded', expanded ? 'false' : 'true');
```

Sub-list (`.mobile-menu__sub`) visibility is CSS-driven:

```css
.mobile-menu__sub { display: none; }
.mobile-menu__item--parent[data-expanded="true"] .mobile-menu__sub { display: block; }
```

### Mobile nav items

Primary list mirrors desktop. Sub-items for Grippy Shoes and Apparel match desktop dropdowns exactly.

**Utility links** (`.mobile-menu__utility`, separated by border-top):

| Label | href |
|-------|------|
| About Us | `/pages/about` |
| FAQ | `/pages/faq` |
| Contact Us | `/pages/contact` |
| Returns & Exchanges | `/pages/returns` |

---

## Footer (`snippets/footer.liquid`)

`<footer class="site-footer" data-theme="dark" role="contentinfo">`. Background: `var(--color-charcoal)`. Text: `var(--color-white)`.

### Grid layout

`.site-footer__grid` — CSS grid, `grid-template-columns: 1fr 1fr 1fr 1.2fr`, `gap: 40px`. Collapses to `1fr` below 768px.

| Column | Heading | Links |
|--------|---------|-------|
| Shop | "Shop" | All Grippy Shoes, Open Sole, Closed Sole, Outdoor, Apparel |
| Support | "Support" | FAQ, Shipping, Returns, Warranty, Contact Us |
| Company | "Company" | About Us, Journal, Collaborations, Compare Styles |
| Newsletter | "Join the List" | Email form |

### Newsletter form

Uses Shopify `{% form 'customer' %}` with `id="footer-newsletter"`. Hidden input `contact[tags]="newsletter"`. Text: "Sign up for 10% off your first order." Privacy note: "No spam. Unsubscribe anytime."

### Footer bottom

`.site-footer__bottom` — flexbox, `justify-content: space-between`, separated by `border-top: 1px solid rgba(255,255,255,0.1)`.

**Social links** (`.site-footer__social`):

| Platform | URL | Attributes |
|----------|-----|-----------|
| Instagram | `https://instagram.com/barreletics` | `rel="noopener noreferrer" target="_blank"` |
| TikTok | `https://tiktok.com/@barreletics` | same |
| Facebook | `https://facebook.com/barreletics` | same |

**Copyright:** `© {year} {shop.name}. All rights reserved.` — year is dynamic via `{{ 'now' | date: '%Y' }}`.

---

## Announcement Strip (`snippets/announcement-strip.liquid`)

### Rendering

Iterates `section.blocks`. Each block renders as `.announcement-strip__slide[data-slide-index]`. First slide gets `.is-active`. If `block.settings.link_url` is set, renders as `a.announcement-strip__link`; otherwise as `<span>`.

Wrapped in a guard: `{% if slides.size > 0 %}`.

### Styling

- Background: `var(--color-charcoal)`, padding: `10px var(--section-padding-x)`
- Slides: `position: absolute`, `inset: 0`, `opacity: 0`, 12px semibold uppercase white text
- Active slide: `.is-active` → `opacity: 1`, `pointer-events: auto`
- Transition: `opacity 320ms ease`

### Rotation logic

```
Interval: 4000ms (4s)
Crossfade: 320ms opacity transition
```

Script runs inside an IIFE. Guards: exits if `≤ 1` slide or if `prefers-reduced-motion: reduce` matches (static first slide).

Hover pauses rotation via `mouseenter`/`mouseleave` toggling a `paused` flag checked by `setInterval`.

```css
@media (prefers-reduced-motion: reduce) {
  .announcement-strip__slide { transition: none; }
}
```

---

## Configuration: Hardcoded Navigation

Navigation links are hardcoded in `header-nav.liquid` and `footer.liquid` — they do **not** use Shopify's `linklists` / navigation menus. Changing nav structure requires editing the snippet source.

**Design decisions:**
- **D-008:** Flat primary nav with "Grippy Shoes" (not "Performance Skins") — instant comprehension for search and mobile conversion. "Performance Skins" lives in page content (H1s, product descriptions), not wayfinding.
- **D-009:** Blog → Journal rename — all nav links point to `/blogs/journal`.
- **D-030:** V2 pattern for non-breaking updates — nav changes follow append-only conventions to avoid breaking existing page references.

---

## Cross-references

- Design tokens used by nav components → [03-DESIGN-SYSTEM.md](./03-DESIGN-SYSTEM.md)
- Cart drawer opened from header → [14-cart-flow.md](./14-cart-flow.md)
- Analytics events on nav interactions → [15-analytics-architecture.md](./15-analytics-architecture.md)
- Component specifications → [04-COMPONENT-LIBRARY.md](./04-COMPONENT-LIBRARY.md)
