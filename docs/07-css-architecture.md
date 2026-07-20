# 07 — CSS Architecture

## Philosophy

Vanilla CSS only — no Sass, no Tailwind, no CSS framework. Theming is handled through CSS custom properties defined in a single design-tokens file. Section-specific styles live inline in each section's `<style>` block; there are no per-section CSS files.

## File Inventory

| File | Scope | Loaded by |
|------|-------|-----------|
| `assets/design-tokens.css` | Global | `{{ 'design-tokens.css' \| asset_url \| stylesheet_tag }}` in `layout/theme.liquid` |
| `assets/barreletics-base.css` | Global | `{{ 'barreletics-base.css' \| asset_url \| stylesheet_tag }}` in `layout/theme.liquid` |
| Inline `<style>` per section/snippet | Scoped to section | Embedded in each `.liquid` file |

Both global CSS files are loaded in `<head>` (lines 109–110 of `layout/theme.liquid`), making them render-blocking by design for critical styles.

---

## `design-tokens.css`

All custom properties are declared on `:root`. A `[data-theme="dark"]` selector overrides semantic tokens for dark sections.

### Naming Convention

| Prefix | Purpose | Examples |
|--------|---------|----------|
| `--color-*` | Raw palette values | `--color-charcoal: #1c1916`, `--color-rust: #c45c3f`, `--color-gold: #d4af37`, `--color-coral: #e8927c`, `--color-warm-cream: #f5f2ec` |
| `--text-*` (semantic) | Text color by role | `--text-primary`, `--text-body`, `--text-muted`, `--text-warm-muted` |
| `--bg-*` | Background by role | `--bg-primary`, `--bg-alternate`, `--bg-card`, `--bg-dark` |
| `--border-*` | Border colors | `--border-default` |
| `--accent-*` | Accent by purpose | `--accent-primary` (rust), `--accent-stars` (gold) |
| `--font-*` | Font family | `--font-family`, `--font-mono` |
| `--weight-*` | Font weights | `--weight-light: 300` through `--weight-bold: 700` |
| `--text-{size}` | Font sizes | `--text-xs: 10px` through `--text-8xl: 52px` |
| `--leading-*` | Line heights | `--leading-tight: 1.08` through `--leading-loose: 1.7` |
| `--tracking-*` | Letter spacing | `--tracking-tight: -0.02em` through `--tracking-manifesto: 0.18em`, `--tracking-brand: 0.14em` |
| `--space-*` | Spacing scale | `--space-0: 0` through `--space-16: 96px` (4 px base) |
| `--section-padding-*` | Section-level padding | `--section-padding-y: 64px`, `--section-padding-x: 40px`, mobile variants |
| `--max-width*` | Layout widths | `--max-width: 1200px`, `--max-width-hero: 1400px`, `--max-width-narrow: 760px`, `--max-width-copy: 540px` |
| `--grid-gap*` | Grid gaps | `--grid-gap: 28px`, `--grid-gap-sm: 20px`, `--grid-gap-lg: 40px` |
| `--radius-*` | Border radii | `--radius-badge: 3px`, `--radius-button: 6px`, `--radius-card-sm: 6px`, `--radius-gallery: 8px`, `--radius-card: 12px`, `--radius-swatch: 50%` |
| `--shadow-*` | Box shadows | `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-text` |
| `--transition-*` | Transition durations | `--transition-fast: 0.2s ease`, `--transition-base: 0.3s ease`, `--transition-slow: 0.4s ease`, `--transition-ticker: 0.32s ease` |
| `--z-*` | Z-index scale | `--z-base: 0` → `--z-toast: 70` (increments of 10) |

### Semantic Color Layer

Raw colors map to semantic purpose via `var()` references:

```
--color-charcoal  →  --text-primary, --bg-dark
--color-body      →  --text-body
--color-muted     →  --text-muted
--color-warm-muted → --text-warm-muted
--color-white     →  --bg-primary
--color-warm-cream → --bg-alternate
--color-light-bg  →  --bg-card
--color-warm-border → --border-default
--color-rust      →  --accent-primary
--color-gold      →  --accent-stars
```

### Dark Theme Override

`[data-theme="dark"]` reassigns semantic tokens:

```css
[data-theme="dark"] {
  --text-primary: var(--color-white);
  --text-body: rgba(255, 255, 255, 0.85);
  --text-muted: rgba(255, 255, 255, 0.6);
  --bg-primary: var(--color-charcoal);
  --border-default: rgba(255, 255, 255, 0.15);
}
```

Used by `snippets/footer.liquid` via `data-theme="dark"` on `<footer>`. Any section can opt in by adding the attribute.

### Breakpoints

Defined as comments only (not custom properties, since `@media` queries cannot use them):

```
480px   (sm)
768px   (md)
1024px  (lg)
1200px  (xl)
1400px  (2xl)
```

---

## `barreletics-base.css`

### Reset

```css
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
```

### Body Defaults

```css
body {
  font-family: var(--font-family);
  font-size: var(--text-base);        /* 15px */
  font-weight: var(--weight-regular); /* 400 */
  line-height: var(--leading-relaxed);/* 1.6 */
  color: var(--text-primary);
  background: var(--bg-primary);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

### Element Resets

| Element | Reset |
|---------|-------|
| `img, video` | `display: block; max-width: 100%; height: auto` |
| `a` | Inherits `--text-primary`, no decoration; underline on hover |
| `button` | `font-family: inherit; cursor: pointer` |
| `ul, ol` | `list-style: none` |
| `h1–h6` | `font-weight: var(--weight-bold); line-height: var(--leading-heading)` |

### Typography Scale Classes

| Class | Size | Line Height | Extra |
|-------|------|-------------|-------|
| `.h1` / `h1` | `--text-6xl` (44px) | `--leading-tight` (1.08) | `--tracking-tight` |
| `.h2` / `h2` | `--text-5xl` (40px) | `--leading-snug` (1.12) | `--tracking-tight` |
| `.h3` / `h3` | `--text-4xl` (36px) | `--leading-heading` (1.15) | — |
| `.h4` / `h4` | `--text-2xl` (28px) | `--leading-heading` (1.15) | — |
| `.body-lg` | `--text-md` (16px) | `--leading-relaxed` (1.6) | `--text-body` color |
| `.body` | `--text-base` (15px) | `--leading-relaxed` (1.6) | `--text-body` color |
| `.body-sm` | 14px | `--leading-relaxed` (1.6) | `--text-body` color |
| `.eyebrow` | `--text-sm` (11px) | — | Bold, uppercase, `--tracking-widest`, `--text-muted` |
| `.eyebrow--accent` | — | — | `--accent-primary` color |
| `.eyebrow--manifesto` | — | — | `--tracking-manifesto` (0.18em) |

### Button System

Base class `.btn`: inline-flex, 16px 32px padding, 13px font, bold, `--tracking-wider`, uppercase, `--radius-button`, transition on background/color/border-color.

| Modifier | Background | Text | Hover |
|----------|------------|------|-------|
| `.btn--primary` | `--color-charcoal` | `--color-white` | bg → `--accent-primary` |
| `.btn--secondary` | transparent | `--color-charcoal` | bg → charcoal, text → white |
| `.btn--inverted` | `--color-white` | `--color-charcoal` | opacity 0.9 |
| `.btn--full` | — | — | `width: 100%` |
| `.btn--lg` | — | — | 18px 36px padding, 15px font |
| `.btn--sm` | — | — | 10px 20px padding, 12px font |

### Section Wrapper

| Class | Padding |
|-------|---------|
| `.section` | `--section-padding-y` `--section-padding-x` |
| `.section--narrow` | `--space-10` y, same x |
| `.section--flush` | 0 |
| `.section--cream` | bg → `--bg-alternate` |
| `.section--dark` | bg → `--bg-dark`, color → white |

| Inner Class | Max Width |
|-------------|-----------|
| `.section__inner` | `--max-width` (1200px) |
| `.section__inner--wide` | `--max-width-hero` (1400px) |
| `.section__inner--narrow` | `--max-width-narrow` (760px) |

### Grid Utilities

```css
.grid     { display: grid; gap: var(--grid-gap); }
.grid--2  { grid-template-columns: repeat(2, 1fr); }
.grid--3  { grid-template-columns: repeat(3, 1fr); }
.grid--4  { grid-template-columns: repeat(4, 1fr); }
```

### Focus Indicators (WCAG 2.1 AA §2.4.7)

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

### Accessibility Utilities

| Class | Purpose |
|-------|---------|
| `.visually-hidden` | Clips element to 1×1px, remains accessible to screen readers |
| `.skip-link` | Hidden above viewport; positioned at `top: 8px` on `:focus` |

### Badges

```css
.badge {
  background: var(--accent-primary);
  color: var(--color-white);
  padding: 4px 10px;
  font-size: var(--text-xs);
  font-weight: var(--weight-bold);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
  border-radius: var(--radius-badge);
}
```

### Stars

```css
.stars     { color: var(--accent-stars); font-size: 14px; letter-spacing: 0.12em; }
.stars--lg { font-size: 18px; }
```

---

## Responsive Strategy

**Mobile-first with max-width overrides.** The base CSS is written for all viewports; `@media (max-width: ...)` queries adapt for smaller screens.

### Global Breakpoints (in `barreletics-base.css`)

**At `max-width: 1024px`:**
- `.grid--4` → 2 columns
- `.grid--3` → 2 columns

**At `max-width: 768px`:**
- Root variables reassigned: `--section-padding-y: 48px`, `--section-padding-x: 16px`
- `.h1`, `.h2` → `--text-3xl` (32px)
- `.h3` → `--text-2xl` (28px)
- `.grid--2`, `.grid--3`, `.grid--4` → 1 column

### Reduced Motion

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

This rule appears in both `barreletics-base.css` and `layout/theme.liquid` (redundant but harmless — the latter acts as a safety net). The announcement strip also checks `prefers-reduced-motion` in JS to skip its rotation entirely.

---

## Section-Specific Styles

All section-level CSS is written inline in `<style>` blocks within each `.liquid` file. There are **no separate CSS files per section**.

### Naming Convention

Each section uses a BEM-like prefix scoped to the section:

| Section | Prefix | Example Classes |
|---------|--------|-----------------|
| `pdp-buy-box.liquid` | `.pdp-buy__*`, `.pdp-gallery__*`, `.pdp-accordion__*` | `.pdp-buy__swatch`, `.pdp-gallery__thumb.is-active` |
| `pdp-features.liquid` | `.pdp-features__*`, `.pdp-feature__*`, `.pdp-disciplines__*` | `.pdp-features__eyebrow`, `.pdp-disciplines__strip` |
| `pdp-reviews.liquid` | `.pdp-reviews__*`, `.pdp-review-featured__*` | `.pdp-reviews__stars`, `.pdp-review-featured__body` |
| `pdp-sock-math.liquid` | `.sock-math__*` | `.sock-math__ours`, `.sock-math__check` |
| `header-nav.liquid` | `.site-header__*`, `.mobile-menu__*` | `.site-header__subnav`, `.mobile-menu__drawer` |
| `announcement-strip.liquid` | `.announcement-strip__*` | `.announcement-strip__slide.is-active` |
| `cart-drawer.liquid` | `.cart-drawer__*` | `.cart-drawer__panel`, `.cart-drawer__shipping-fill` |
| `footer.liquid` | `.site-footer__*` | `.site-footer__grid`, `.site-footer__submit` |
| `sticky-atc.liquid` | `.sticky-atc__*` | `.sticky-atc__btn`, `.sticky-atc__thumb` |
| `review-card.liquid` | `.review-card__*` | `.review-card__stars`, `.review-card__verified` |

### State Classes

| Class | Applied by | Purpose |
|-------|-----------|---------|
| `.is-active` | JS | Active swatch, size, thumb, slide |
| `.is-open` | JS | Mobile menu, cart drawer |
| `.is-scrolled` | JS | Header after scroll > 8px |
| `.is-visible` | JS | Sticky ATC bar |
| `.is-unavailable` | JS | Out-of-stock size button |
| `.btn--disabled` | JS | Disabled CTA state |

---

## How to Add New Styles

1. Use design tokens for **all** color, spacing, font, radius, shadow, and transition values
2. Add an inline `<style>` block in the section `.liquid` file
3. Use a BEM-like prefix matching the section name (e.g., `.my-section__element`)
4. Add responsive overrides at `max-width: 1024px` and `max-width: 768px` inside the same `<style>` block
5. For dark sections, apply `data-theme="dark"` on the container — semantic tokens auto-adapt
6. Never create separate `.css` files per section

---

## Cross-References

- Token values and decision log → Design System Skill
- JS classes toggled dynamically → [06-javascript-architecture.md](06-javascript-architecture.md)
- Theme settings that map to colors/typography → [08-theme-settings-reference.md](08-theme-settings-reference.md)
