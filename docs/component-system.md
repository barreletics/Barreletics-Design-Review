# Component System — Permanent UI Library

---
document: Component System
version: 1.0
status: 🔵 Ready for Review
last_modified: 2026-07-19
depends_on: [03-design-system, 04-component-library, design-tokens.css]
source_of_truth_tokens: shopify-build/assets/design-tokens.css
source_of_truth_base: shopify-build/assets/barreletics-base.css
---

## Purpose

Permanent UI library for Barreletics. A senior developer or designer should be able to look up any reusable pattern, understand its anatomy, variants, usage rules, responsive behavior, and accessibility requirements — then implement without inventing new styles.

**Rules:**
- Always use design tokens (`var(--*)`). Never hardcode hex/px values in section styles.
- Foundation Doc 04 (`planning/04-component-library.md`) defines intent; this document defines the implemented system.
- Token reference: `docs/23-design-token-reference.md`.
- Retired claims must never appear in trust/value/UI copy (`planning/RETIRED_CLAIMS.md`).

---

## 1. Buttons

**Snippet:** `shopify-build/snippets/button.liquid`  
**Base classes:** `.btn`, `.btn--primary`, `.btn--secondary`, `.btn--inverted`, `.btn--sm`, `.btn--lg`, `.btn--full`

### Anatomy

```liquid
{% render 'button',
  label: 'Shop Now',
  url: '/collections/grippy-shoes',
  style: 'primary',
  size: 'md'
%}
```

| Parameter | Values | Default |
|-----------|--------|---------|
| `label` | string (required) | — |
| `url` | string → renders `<a>` | omit → `<button>` |
| `style` | `primary` \| `secondary` \| `inverted` | `primary` |
| `size` | `sm` \| `md` \| `lg` | `md` |
| `full` | boolean | `false` |
| `type` | `button` \| `submit` | `button` |
| `disabled` | boolean | `false` |
| `aria_label` | string | optional |
| `class` | extra class | optional |

### Variants

| Variant | Class | Visual |
|---------|-------|--------|
| Primary | `.btn--primary` | Charcoal fill (`--color-charcoal`), white text; hover → rust (`--accent-primary`) |
| Secondary | `.btn--secondary` | Transparent, charcoal border/text; hover → charcoal fill |
| Inverted | `.btn--inverted` | White fill on dark sections; hover opacity 0.9 |
| Full width | `.btn--full` | `width: 100%` |
| Small | `.btn--sm` | `padding: 10px 20px; font-size: 12px` |
| Medium (default) | `.btn` | `padding: 16px 32px; font-size: 13px` |
| Large | `.btn--lg` | `padding: 18px 36px; font-size: 15px` |

**Shared tokens:** `--radius-button` (6px, D-003), `--weight-bold`, `--tracking-wider`, uppercase, `--transition-fast` (0.2s).

### States

| State | Behavior |
|-------|----------|
| Default | As variant |
| Hover | Color/background swap per variant |
| Focus-visible | 2px charcoal outline, 2px offset (white outline on dark) |
| Disabled | `disabled` + `aria-disabled="true"`; link variant uses `tabindex="-1"` |
| Loading | Not in base snippet yet — if added: disable click, announce via `aria-busy` |

### Quick Add (collection cards)

Outlined control on product cards (collection/grid context). Hover fills. Distinct from primary CTA — action is “add,” not navigate. Must include `aria-label` including product title.

### Text / Link CTA

Underline + letter-spacing for secondary actions inside copy blocks. Prefer real buttons for primary conversion actions.

### Button Rules

1. Prefer **one primary** CTA per section; secondary optional.
2. Label: action-oriented, 2–4 words. Never “Click Here” or “Submit.”
3. Use inverted only on `.section--dark` / charcoal backgrounds.
4. Touch target ≥ 44×44px on mobile.

---

## 2. Cards

### Product Card

**Snippet:** `product-card.liquid`

| Element | Spec |
|---------|------|
| Anatomy | Image container → optional badge → title → price → installment hint → Quick Add |
| Tokens | Border via `--border-default` / light border; radius `--radius-card` (12px) |
| Hover | Subtle lift/shadow; transition ~320ms (`--transition-ticker` / base) |
| Responsive | Equal-height grid cells; image aspect consistent within a grid |
| A11y | Product link wraps title; Quick Add has descriptive `aria-label` |

**Parameters (typical):** product object, show badge, show quick add, minimal variant.

### Review Card

**Snippet:** `review-card.liquid`  
**Decisions:** radius 12px (D-006), star color `--accent-stars` / `#d4af37` (D-007)

| Element | Spec |
|---------|------|
| Anatomy | Stars → quote → author → location → date → optional verified badge → optional photo |
| Variants | Compact (grid), expanded (full-width), horizontal (media + text) |
| A11y | Stars: `aria-label="X out of 5 stars"` |

### Feature Card

Used in PDP features / benefit grids: icon or number + heading + short description. Variants: icon-led, number-led, stat-led.

### Comparison Card

Open Sole vs Closed Sole side-by-side. Shared attributes highlighted. Used on collection hero / compare page.

### Card Rules

- Tokens only — no hardcoded colors/radii.
- Responsive stack on mobile.
- Equal height per row in CSS Grid.
- Consistent image aspect ratio within a grid.

---

## 3. Grids

### Product Grid

**Section:** `variant-grid.liquid` (+ collection templates, `recommendations.liquid`, `recently-viewed.liquid`)

| Viewport | Columns |
|----------|---------|
| Desktop (≥1024) | 4 |
| Tablet (~768–1023) | 3 |
| Mobile (<768) | 2 |

- Max width: `--max-width-hero` (1400px) for wide merchandising; content often `--max-width` (1200px).
- Gap: `--grid-gap` (28px) / `--grid-gap-sm` (20px).
- Tab filters (typical): All / Closed / Open / One-Offs / Outdoor — must be keyboard accessible.

### Content Grid

Trust strips, feature blocks, footer columns. Utility classes: `.grid`, `.grid--2`, `.grid--3`, `.grid--4`.

### Grid Rules

- CSS Grid or Flexbox only (no floats).
- Gaps from spacing tokens.
- Side padding: `--section-padding-x` (40px) desktop, `--section-padding-x-mobile` (16px) mobile.

---

## 4. Trust Rows / Value Strips

### Trust Strip

**Snippet:** `trust-strip.liquid`

| Item | Spec |
|------|------|
| Anatomy | Icon + label pairs, horizontal |
| Approved claims | 360° Grip · Made in USA · 30-Day Returns · Free Shipping $150+ |
| Variants | Standard (light), inverted (dark), compact |
| Icons | Decorative → `aria-hidden="true"` |

### Value Strip

**Section:** `value-strip.liquid`  
Stat/number + label. Larger type for numbers. Horizontal desktop; 2-column mobile.

### Rules

- Claims from Doc 07 only.
- Never: free shipping $75, studio trial, heat-activated grip, warranty covers wear (see `RETIRED_CLAIMS.md`).

---

## 5. FAQs / Accordions

**Snippet:** `faq-accordion.liquid`

| Item | Spec |
|------|------|
| Markup | Prefer native `<details>`/`<summary>` |
| Behavior | One-at-a-time open recommended |
| Layout | Max-width `--max-width-narrow` (760px), centered |
| Borders | Top/bottom `1px solid` warm border token |
| Schema | FAQPage JSON-LD for FAQ instances |
| Content | Questions/answers from Doc 07 only |

**Rules:** Never nest accordions. Keep answers canonical (adapt format, not facts).

---

## 6. Image Galleries

### PDP Gallery

- Main image + thumbnail strip; swap on variant change.
- Thumbnails below on mobile.
- Descriptive `alt` on every product image.
- Lazy-load below-fold images.

### Lifestyle / Marketing Images

| Aspect | Use |
|--------|-----|
| 16:9 | Banners |
| 4:3 | Cards |
| 1:1 | Square social/product |
| 3:4 | Portrait lifestyle |

**50/50:** full-bleed media panel + copy panel (`fifty-fifty.liquid`).  
**Rules:** Decorative images `aria-hidden`; WebP preferred; keep file sizes lean.

---

## 7. Review Modules

| Module | Source | Notes |
|--------|--------|-------|
| Summary bar | Judge.me metafields | Stars + aggregate + count — never hardcode |
| Review grid | `pdp-reviews.liquid` + `review-card.liquid` | “Read all” + “Write a Review” |
| Carousel | Optional | If used: arrows + `aria-live` for slide changes |

**Rules (D-025):** Custom rendering, Judge.me data. Never mark unverified as Verified Purchase. Empty state: “No reviews yet — be the first.”

---

## 8. Feature Blocks

### 50/50 Split

**Section:** `fifty-fifty.liquid`

- Panels: media + copy (eyebrow, heading, body, CTA).
- Variants: image-left / image-right.
- Mobile: stack, media on top.

### Full-Width Statement

Single large headline; optional cream/dark background.

### Stat Block

Number + label (+ optional description) for value strips and feature rows.

---

## 9. Hero Variations

| Hero | Section | Notes |
|------|---------|-------|
| Home 50/50 | `hero.liquid` | Headline, subhead, body, CTA(s); white or warm cream (`#f5f2ec` / `--bg-alternate`) |
| Hero Alt | `hero-alt.liquid` | D-041 alternate messaging; same structure |
| Collection | `collection-hero.liquid` | Eyebrow + title + description; Open vs Closed cards |

**Hero Rules:**
- One hero per page.
- CTA required.
- Mobile: copy above image.
- Headline scannable (≈8 words max preferred).
- Eyebrow rotation (home): respects `prefers-reduced-motion`.

---

## 10. Section Templates

Standard anatomy:

```html
<section class="[section-name] section" id="[section-id]">
  <div class="[section-name]__inner section__inner">
    <!-- optional eyebrow -->
    <p class="section-eyebrow">...</p>
    <h2 class="section-heading">...</h2>
    <!-- content -->
    <!-- optional CTA -->
  </div>
</section>
```

| Token / Class | Value / Role |
|---------------|--------------|
| `--section-padding-y` | 64px desktop |
| `--section-padding-y-mobile` | 48px |
| `--section-padding-x` | 40px |
| `--section-padding-x-mobile` | 16px |
| `.section__inner` | max-width 1200px |
| `.section__inner--wide` | 1400px |
| `.section__inner--narrow` | 760px |
| `.section--cream` | warm cream bg |
| `.section--dark` | charcoal bg |

**Snippet helper:** `section-wrapper.liquid` for consistent padding/background options.

---

## 11. Spacing System

From `design-tokens.css` (canonical — prefer these names over informal xs/sm aliases):

| Token | Value | Typical use |
|-------|-------|-------------|
| `--space-1` | 4px | Tight internal |
| `--space-2` | 8px | Related gap |
| `--space-3` | 12px | Compact UI |
| `--space-4` | 16px | Standard content gap |
| `--space-6` | 24px | Component internal |
| `--space-8` | 32px | Between blocks |
| `--space-9` | 40px | Side padding align |
| `--space-10` | 48px | Mobile section Y |
| `--space-12` | 64px | Desktop section Y |
| `--space-14` | 80px | Large breaks |
| `--space-16` | 96px | Extra-large |

**Rules:** Token variables only. Vertical rhythm between sections via section padding tokens. Component internals use smaller steps.

---

## 12. Animation System

| Animation | Property | Duration | Token |
|-----------|----------|----------|-------|
| Button hover | background/color | 0.2s | `--transition-fast` |
| Card hover | transform/shadow | ~0.3–0.32s | `--transition-base` / `--transition-ticker` |
| Accordion | height/open | ~0.3s | `--transition-base` |
| Cart drawer | transform | ~0.3s | ease-out |
| Announcement rotate | opacity | 0.32s | `--transition-ticker` |
| Sticky ATC | transform | ~0.2s | `--transition-fast` |
| Mobile menu | transform | ~0.3s | ease-out |

**Rules:**
- Honor `prefers-reduced-motion: reduce` (already in `barreletics-base.css`).
- No animation > 400ms (`--transition-slow` is 0.4s max).
- No decorative entrance animations on page load.
- Focus indicators: immediate (no delay).

---

## 13. Responsive Rules

| Name | Width | Behavior |
|------|-------|----------|
| Mobile | < 768px | Stack, 2-col product grid, hamburger nav |
| Tablet | 768–1023px | 3-col grids, transitional |
| Desktop | 1024–1399px | Full layout |
| Wide | ≥ 1400px | Constrain to max-width tokens |

**Patterns:**
- Mobile-first `min-width` queries preferred for new CSS.
- 50/50 → stack; product grid 4 → 3 → 2.
- Side padding 40 → 16; section Y 64 → 48.
- Touch targets ≥ 44×44px.

---

## 14. Naming Standards

### CSS (BEM-inspired)

- Block: `.product-card`
- Element: `.product-card__title`
- Modifier: `.btn--primary`, `.section--dark`

### Liquid files

| Type | Pattern | Example |
|------|---------|---------|
| Section | `kebab-case.liquid` | `fifty-fifty.liquid` |
| Snippet | `kebab-case.liquid` | `trust-strip.liquid` |
| Template | `page.name.json` / `collection.name.json` | `page.faq.json` |

### Tokens

`--category-name` (e.g. `--color-charcoal`, `--space-6`, `--radius-button`)

### JavaScript

- Functions: `camelCase`
- Custom events: `kebab-case` (e.g. `variant:changed`)
- Prefer `[data-*]` selectors

### Content IDs / Schema

- Section IDs: kebab-case (`#product-faq`)
- Theme settings: snake_case (`heading_text`)

---

## 15. Component Inventory Map

### Snippets (UI)

| Snippet | Role |
|---------|------|
| `button.liquid` | CTA system |
| `product-card.liquid` | Merchandising card |
| `review-card.liquid` | Review unit |
| `faq-accordion.liquid` | FAQ/accordion |
| `trust-strip.liquid` | Trust row |
| `section-wrapper.liquid` | Section chrome |
| `announcement-strip.liquid` | Top ticker |
| `header-nav.liquid` | Global header |
| `footer.liquid` | Global footer |
| `sticky-atc.liquid` | PDP sticky bar |
| `cart-drawer.liquid` | Mini-cart |
| `breadcrumb.liquid` | Breadcrumbs + schema |
| `geo-section.liquid` | GEO content block |
| `related-links.liquid` | Internal linking |

### Sections (page composition)

| Section | Role |
|---------|------|
| `hero.liquid` / `hero-alt.liquid` | Home heroes |
| `collection-hero.liquid` | Collection intro |
| `value-strip.liquid` | Stats strip |
| `variant-grid.liquid` | Tabbed product grid |
| `disciplines.liquid` | Discipline grid |
| `fifty-fifty.liquid` | Feature split |
| `social-proof.liquid` | Reviews band |
| `newsletter.liquid` | Email capture |
| `pdp-buy-box.liquid` | PDP purchase UI |
| `pdp-features.liquid` | Feature cards |
| `pdp-sock-math.liquid` | Value math |
| `pdp-reviews.liquid` | Review module |
| `recommendations.liquid` / `recently-viewed.liquid` | Cross-sell |

Integration snippets (analytics, Help Scout, Tidio, pixels) are documented in `docs/15-analytics-architecture.md` and M4B docs — not UI library components.

---

## 16. Accessibility Baseline

| Requirement | Implementation |
|-------------|----------------|
| Focus | `:focus-visible` 2px outline |
| Skip link | `.skip-link` in theme |
| Reduced motion | Global media query disables non-essential motion |
| Icons | Decorative → `aria-hidden` |
| Forms | Labels associated; errors announced |
| Drawers/menus | `aria-expanded`, focus trap where implemented |
| Color | Charcoal/rust on cream/white — do not introduce low-contrast accents |

---

## Cross-References

- Design System → `planning/03-design-system.md`
- Foundation components → `planning/04-component-library.md`
- Section library → `docs/03-section-library.md`
- Snippet library → `docs/04-snippet-library.md`
- CSS architecture → `docs/07-css-architecture.md`
- Tokens → `docs/23-design-token-reference.md`
- A11y decisions → `docs/22-accessibility-decisions.md`
