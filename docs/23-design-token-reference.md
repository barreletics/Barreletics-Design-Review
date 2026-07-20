# 23 — Design Token Reference

---
document: 23 – Design Token Reference
status: Reference
last_modified: 2026-07-19
depends_on: [07-css-architecture]
source_file: shopify-build/assets/design-tokens.css
decisions: D-001, D-003, D-004, D-006, D-007
---

## Overview

All design tokens are defined as CSS custom properties in `shopify-build/assets/design-tokens.css`. This is the v49 canonical token set, governed by decisions D-001 through D-007 in `planning/10-decision-log.md`.

**Rule:** Never use raw hex values in section `<style>` blocks. Always reference tokens via `var(--token-name)`.

---

## Colors (Raw Palette)

| Token | Value | Usage |
|-------|-------|-------|
| `--color-charcoal` | `#1c1916` | Primary text, headings, dark backgrounds (D-001) |
| `--color-rust` | `#c45c3f` | CTA accent, badges, error states |
| `--color-gold` | `#d4af37` | Star ratings only (D-007) |
| `--color-body` | `#4a4a4a` | Body copy, descriptions |
| `--color-muted` | `#8a8a8a` | Captions, metadata, non-critical labels |
| `--color-warm-muted` | `#6b645a` | Warm-toned muted text (GEO, shipping bar) |
| `--color-warm-border` | `#d6cfc0` | Header scroll border, warm dividers |
| `--color-warm-cream` | `#f5f2ec` | Alternate section backgrounds |
| `--color-light-bg` | `#f9f9f9` | Card backgrounds, gallery backgrounds |
| `--color-white` | `#ffffff` | Primary background |
| `--color-coral` | `#e8927c` | Cart badge only |

---

## Colors (Semantic)

Semantic tokens map to raw palette values and are the preferred interface for section authors.

| Token | Maps To | Usage |
|-------|---------|-------|
| `--text-primary` | `var(--color-charcoal)` | Headings, primary UI text |
| `--text-body` | `var(--color-body)` | Paragraphs, descriptions |
| `--text-muted` | `var(--color-muted)` | Secondary labels, metadata |
| `--text-warm-muted` | `var(--color-warm-muted)` | GEO triggers, shipping text |
| `--bg-primary` | `var(--color-white)` | Page background |
| `--bg-alternate` | `var(--color-warm-cream)` | Alternating section background |
| `--bg-card` | `var(--color-light-bg)` | Card surfaces, gallery bg |
| `--bg-dark` | `var(--color-charcoal)` | Dark section backgrounds |
| `--border-default` | `var(--color-warm-border)` | Dividers, input borders |
| `--accent-primary` | `var(--color-rust)` | CTAs, badges, active states |
| `--accent-stars` | `var(--color-gold)` | Star rating color |

---

## Typography

### Font Families

| Token | Value | Usage |
|-------|-------|-------|
| `--font-family` | `'Roboto', -apple-system, BlinkMacSystemFont, sans-serif` | All text |
| `--font-mono` | `'JetBrains Mono', monospace` | Code references (if needed) |

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `--weight-light` | `300` | Hero subtext, decorative |
| `--weight-regular` | `400` | Body copy |
| `--weight-medium` | `500` | Subnav links, breadcrumb current |
| `--weight-semibold` | `600` | Section headings, nav items, accordion triggers |
| `--weight-bold` | `700` | H1–H6, CTAs, eyebrows, badges |

### Font Sizes

| Token | Value | Usage |
|-------|-------|-------|
| `--text-xs` | `10px` | Badges, smallest labels |
| `--text-sm` | `11px` | Eyebrows, breadcrumb, GEO triggers |
| `--text-base` | `15px` | Body text default |
| `--text-md` | `16px` | Body-lg class, descriptions |
| `--text-lg` | `18px` | PDP product title (H1), cart drawer title |
| `--text-xl` | `21px` | — |
| `--text-2xl` | `28px` | H4, section subheadings |
| `--text-3xl` | `32px` | Mobile H1/H2 |
| `--text-4xl` | `36px` | H3, price display |
| `--text-5xl` | `40px` | H2 desktop |
| `--text-6xl` | `44px` | H1 desktop, PDP hero name |
| `--text-7xl` | `48px` | — |
| `--text-8xl` | `52px` | — |

### Line Heights

| Token | Value | Usage |
|-------|-------|-------|
| `--leading-tight` | `1.08` | H1, hero headlines |
| `--leading-snug` | `1.12` | H2 |
| `--leading-heading` | `1.15` | H3–H6 |
| `--leading-normal` | `1.5` | Breadcrumb, UI elements |
| `--leading-relaxed` | `1.6` | Body copy |
| `--leading-loose` | `1.7` | Accordion content, long-form |

### Letter Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--tracking-tight` | `-0.02em` | H1, H2 headlines |
| `--tracking-normal` | `0` | Body text |
| `--tracking-wide` | `0.04em` | — |
| `--tracking-wider` | `0.06em` | Nav items, option labels, CTA buttons |
| `--tracking-widest` | `0.08em` | Eyebrows, badges (D-004) |
| `--tracking-eyebrow` | `0.08em` | Alias for eyebrow default (D-004) |
| `--tracking-manifesto` | `0.18em` | Manifesto section exception (D-004) |
| `--tracking-brand` | `0.14em` | Logo wordmark |

---

## Spacing

### Scale

| Token | Value |
|-------|-------|
| `--space-0` | `0` |
| `--space-1` | `4px` |
| `--space-2` | `8px` |
| `--space-3` | `12px` |
| `--space-4` | `16px` |
| `--space-5` | `20px` |
| `--space-6` | `24px` |
| `--space-7` | `28px` |
| `--space-8` | `32px` |
| `--space-9` | `40px` |
| `--space-10` | `48px` |
| `--space-11` | `56px` |
| `--space-12` | `64px` |
| `--space-13` | `72px` |
| `--space-14` | `80px` |
| `--space-15` | `88px` |
| `--space-16` | `96px` |

### Section Padding

| Token | Value | Context |
|-------|-------|---------|
| `--section-padding-y` | `64px` | Vertical padding (desktop) |
| `--section-padding-x` | `40px` | Horizontal padding (desktop) |
| `--section-padding-y-mobile` | `48px` | Vertical padding (≤768px) |
| `--section-padding-x-mobile` | `16px` | Horizontal padding (≤768px) |

Mobile overrides are applied via `@media (max-width: 768px)` in `barreletics-base.css`:
```css
:root {
  --section-padding-y: 48px;
  --section-padding-x: 16px;
}
```

---

## Layout

| Token | Value | Usage |
|-------|-------|-------|
| `--max-width` | `1200px` | Default content container |
| `--max-width-hero` | `1400px` | Hero sections, PDP grid |
| `--max-width-narrow` | `760px` | Article content, narrow pages |
| `--max-width-copy` | `540px` | Single-column copy blocks |
| `--grid-gap` | `28px` | Default grid gap |
| `--grid-gap-sm` | `20px` | Compact grid gap |
| `--grid-gap-lg` | `40px` | Spacious grid gap |

---

## Border Radius (D-003, D-006)

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-badge` | `3px` | Badges, quantity controls |
| `--radius-button` | `6px` | CTA buttons, size selectors, skip link (D-003) |
| `--radius-card-sm` | `6px` | Thumbnails, cart item images, dropdowns |
| `--radius-gallery` | `8px` | Gallery hero image, video containers |
| `--radius-card` | `12px` | Review cards, justifier cards, content cards (D-006) |
| `--radius-swatch` | `50%` | Color swatches (circular) |

---

## Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 3px rgba(28, 25, 22, 0.06)` | Subtle elevation (cards at rest) |
| `--shadow-md` | `0 4px 16px rgba(28, 25, 22, 0.08)` | Dropdowns, subnav panels |
| `--shadow-lg` | `0 8px 32px rgba(28, 25, 22, 0.12)` | Cart drawer panel, modals |
| `--shadow-text` | `0 2px 24px rgba(0, 0, 0, 0.3)` | Text over images (hero overlays) |

All shadow colors use the charcoal RGB (`28, 25, 22`) for warm consistency rather than pure black.

---

## Transitions

| Token | Value | Usage |
|-------|-------|-------|
| `--transition-fast` | `0.2s ease` | Hover states, button interactions |
| `--transition-base` | `0.3s ease` | Drawer open/close, overlay fade |
| `--transition-slow` | `0.4s ease` | Page-level transitions |
| `--transition-ticker` | `0.32s ease` | Announcement strip message rotation |

---

## Z-Index Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--z-base` | `0` | Default stacking |
| `--z-dropdown` | `10` | Subnav dropdowns |
| `--z-sticky` | `20` | Sticky ATC bar, sticky gallery |
| `--z-overlay` | `30` | Background overlays |
| `--z-header` | `40` | Fixed site header |
| `--z-nav` | `50` | Navigation above header |
| `--z-modal` | `60` | Cart drawer, mobile menu |
| `--z-toast` | `70` | Toast notifications, skip link |

---

## Breakpoints

Documented as commented-out reference values (not usable as custom properties in media queries):

| Name | Value | Usage |
|------|-------|-------|
| `--bp-sm` | `480px` | Small mobile |
| `--bp-md` | `768px` | Tablet / mobile breakpoint |
| `--bp-lg` | `1024px` | Tablet landscape |
| `--bp-xl` | `1200px` | Desktop (matches `--max-width`) |
| `--bp-2xl` | `1400px` | Wide desktop (matches `--max-width-hero`) |

Use `@media (max-width: 768px)` directly — CSS custom properties cannot be used in media query expressions.

---

## Dark Theme Overrides

Applied via `[data-theme="dark"]` selector on section containers:

```css
[data-theme="dark"] {
  --text-primary: var(--color-white);
  --text-body: rgba(255, 255, 255, 0.85);
  --text-muted: rgba(255, 255, 255, 0.6);
  --bg-primary: var(--color-charcoal);
  --border-default: rgba(255, 255, 255, 0.15);
}
```

Sections using `data-theme="dark"` automatically inherit inverted text and border colors without any additional CSS. Focus indicators also switch to white outline (handled in `barreletics-base.css`).

---

## Naming Convention

| Pattern | Example | Usage |
|---------|---------|-------|
| `--color-{name}` | `--color-charcoal` | Raw palette values |
| `--{semantic-role}` | `--text-primary`, `--bg-dark` | Semantic tokens (preferred for use in sections) |
| `--text-{size}` | `--text-lg` | Font size scale |
| `--weight-{name}` | `--weight-bold` | Font weights |
| `--leading-{name}` | `--leading-tight` | Line heights |
| `--tracking-{name}` | `--tracking-wider` | Letter spacing |
| `--space-{n}` | `--space-8` | Spacing scale (4px increments) |
| `--radius-{context}` | `--radius-card` | Border radius by component type |
| `--shadow-{size}` | `--shadow-md` | Elevation shadows |
| `--transition-{speed}` | `--transition-fast` | Timing |
| `--z-{layer}` | `--z-modal` | Stacking order |
| `--max-width-{variant}` | `--max-width-hero` | Container widths |

---

## How to Add a New Token

1. Add the custom property to the `:root` block in `assets/design-tokens.css`
2. Follow the naming convention above
3. If semantic, map to an existing raw token: `--new-semantic: var(--color-existing);`
4. If it affects dark sections, add an override in the `[data-theme="dark"]` block
5. Document the decision in `planning/10-decision-log.md` if it affects the visual system
6. Never use raw hex in sections — always reference the token

---

## Decision Log References

| Decision | What It Governs |
|----------|-----------------|
| D-001 | Color palette values (warm charcoal, cream, body, muted) |
| D-003 | Button border-radius = 6px (supersedes 0px) |
| D-004 | Eyebrow letter-spacing = 0.08em (manifesto exception: 0.18em) |
| D-006 | Review card border-radius = 12px |
| D-007 | Star color = `#d4af37` antique gold (supersedes `#fbc02d`) |

---

**Cross-references:**
- Design System Foundation → `planning/03-design-system.md`
- CSS architecture → `docs/07-css-architecture.md`
- Design System Skill → `.cursor/skills/barreletics-design-system/SKILL.md`
- Component specifications → `docs/04-COMPONENT-LIBRARY.md`
