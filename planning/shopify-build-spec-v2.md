# Shopify Build Specification v2

---
document: shopify-build-spec-v2
version: 2.0
status: Active
created: 2026-07-18
supersedes: planning/shopify-build-specification.md (DRAFT, 2026-07-13)
milestone: 2 — Core Experience
depends_on: [03, 04, 05, 06, 09, 11, 12]
---

## 1. Theme Architecture

| Property | Value |
|----------|-------|
| Theme name | `barreletics-v2` |
| Base | OS 2.0 clean build (reference live theme for migration) |
| Sections Everywhere | Required — all templates use JSON format |
| Max content width | 1200px (hero: 1400px) |
| Build directory | `shopify-build/` (repo root) |

### Directory Structure

```
shopify-build/
├── assets/
│   ├── design-tokens.css          ← All CSS custom properties
│   ├── barreletics-base.css       ← Reset + typography + utilities
│   ├── component-header.css       ← (Phase 2)
│   ├── component-pdp.css          ← (Phase 2)
│   ├── component-collection.css   ← (Phase 2)
│   └── global.js                  ← Shared utilities (Phase 2)
├── config/
│   ├── settings_schema.json       ← Theme-level settings
│   └── settings_data.json         ← Default preset
├── layout/
│   ├── theme.liquid               ← Main layout wrapper
│   └── password.liquid            ← Password page
├── sections/
│   ├── section-ticker.liquid
│   ├── section-header.liquid
│   ├── section-hero.liquid
│   ├── section-pillar-strip.liquid
│   ├── section-split-50-50.liquid
│   ├── section-product-grid.liquid
│   ├── section-sock-math.liquid
│   ├── section-reviews.liquid
│   ├── section-faq.liquid
│   ├── section-newsletter.liquid
│   ├── section-guarantee.liquid
│   ├── section-footer.liquid
│   ├── section-collection-hero.liquid
│   ├── section-sole-chooser.liquid
│   ├── section-collection-grid.liquid
│   ├── section-founder.liquid
│   ├── section-manifesto.liquid
│   ├── section-closing.liquid
│   ├── section-coperni.liquid
│   └── ... (38 total per v1 spec)
├── snippets/
│   ├── announcement-strip.liquid  ← ✅ Built (Phase 1)
│   ├── header-nav.liquid          ← ✅ Built (Phase 1)
│   ├── footer.liquid              ← ✅ Built (Phase 1)
│   ├── product-card.liquid        ← ✅ Built (Phase 1)
│   ├── faq-accordion.liquid       ← ✅ Built (Phase 1)
│   ├── section-wrapper.liquid     ← ✅ Built (Phase 1)
│   ├── trust-strip.liquid         ← ✅ Built (Phase 1)
│   ├── button.liquid              ← ✅ Built (Phase 1)
│   ├── sticky-atc.liquid           ← ✅ Built (Phase 2, D-023)
│   ├── cart-drawer.liquid          ← ✅ Built (Phase 2, D-024)
│   ├── review-card.liquid          ← ✅ Built (Phase 2, D-025)
│   ├── geo-section.liquid          ← ✅ Built (Phase 2, D-022)
│   ├── breadcrumb.liquid           ← Phase 2
│   ├── icon-set.liquid             ← Phase 2
│   ├── price-display.liquid        ← Phase 2
│   ├── size-selector.liquid        ← Phase 2
│   ├── color-swatch.liquid         ← Phase 2
│   └── pagination.liquid           ← Phase 2
└── templates/
    ├── index.json                 ← Homepage
    ├── product.json               ← PDP
    ├── collection.json            ← Collection/Pillar
    ├── page.json                  ← Generic page
    ├── page.about.json            ← About page
    ├── article.json               ← Blog article
    ├── blog.json                  ← Blog index
    ├── cart.json                   ← Cart fallback
    └── 404.json                   ← Error page
```

---

## 2. Design Tokens

All tokens live in `shopify-build/assets/design-tokens.css` as CSS custom properties. Source: Doc 03 + Design System Skill + Decision Log (D-001 through D-007).

### Color Tokens

| Token | Variable | Value | Source |
|-------|----------|-------|--------|
| Charcoal | `--color-charcoal` | `#1c1916` | D-001, D-005 |
| Rust | `--color-rust` | `#c45c3f` | Doc 03 |
| Gold | `--color-gold` | `#d4af37` | D-007 |
| Body text | `--color-body` | `#4a4a4a` | D-001 |
| Muted | `--color-muted` | `#8a8a8a` | D-001 |
| Warm muted | `--color-warm-muted` | `#6b645a` | Doc 03 |
| Warm border | `--color-warm-border` | `#d6cfc0` | Doc 03 |
| Warm cream | `--color-warm-cream` | `#f5f2ec` | D-001 |
| Light bg | `--color-light-bg` | `#f9f9f9` | Doc 03 |
| Coral | `--color-coral` | `#e8927c` | D-005 (cart badge only) |

### Typography Tokens

| Element | Size | Weight | Line Height | Letter Spacing |
|---------|------|--------|-------------|----------------|
| H1 (product) | 44px → 32px mobile | 700 | 1.08 | -0.02em |
| H2 (section) | 40–42px → 32px mobile | 700 | 1.12–1.15 | -0.02em |
| Body | 15–16px | 400 | 1.6–1.7 | 0 |
| Eyebrow | 11px | 700 | — | 0.08em (default), 0.18em (manifesto) |
| Badge | 10px | 700 | — | 0.08em |
| CTA button | 13–15px | 700 | — | 0.06em |

### Border Radius (D-003, D-006)

| Element | Radius |
|---------|--------|
| Badge | 3px |
| Button / CTA | 4px |
| Variant card | 6px |
| Gallery / Video | 8px |
| Content card / Review | 12px |
| Swatch | 50% |

---

## 3. Liquid Component Map

Every component from Doc 04 mapped to its implementation file:

| # | Component | Snippet/Section | Status |
|---|-----------|----------------|--------|
| 1 | Announcement Ticker | `snippets/announcement-strip.liquid` | ✅ Phase 1 |
| 2 | Header / Nav | `snippets/header-nav.liquid` | ✅ Phase 1 |
| 3 | Hero Section | `sections/section-hero.liquid` | Phase 2 |
| 4 | Pillar Strip | `sections/section-pillar-strip.liquid` | Phase 2 |
| 5 | 50/50 Split | `sections/section-split-50-50.liquid` | Phase 2 |
| 6 | Product Card | `snippets/product-card.liquid` | ✅ Phase 1 |
| 7 | Product Grid | `sections/section-product-grid.liquid` | Phase 2 |
| 8 | Sock Math | `sections/section-sock-math.liquid` | Phase 2 |
| 9 | Benefit Grid | `sections/section-benefit-grid.liquid` | Phase 2 |
| 10 | Accordion (FAQ) | `snippets/faq-accordion.liquid` | ✅ Phase 1 |
| 11 | Reviews | `sections/section-reviews.liquid` + `snippets/review-card.liquid` | Phase 2 (D-025) |
| 12 | Guarantee | `sections/section-guarantee.liquid` | Phase 2 |
| 13 | Newsletter | `sections/section-newsletter.liquid` | Phase 2 |
| 14 | Footer | `snippets/footer.liquid` | ✅ Phase 1 |
| 15 | Founder Letter | `sections/section-founder.liquid` | Phase 2 |
| 16 | Manifesto | `sections/section-manifesto.liquid` | Phase 2 |
| 17 | Problem Section | `sections/section-problem.liquid` | Phase 2 |
| 18 | Closing Statement | `sections/section-closing.liquid` | Phase 2 |
| 19 | Credibility | `sections/section-credibility.liquid` | Phase 2 |
| 20 | Trust Badges | `snippets/trust-strip.liquid` | ✅ Phase 1 |
| 21 | Variant Grid | `sections/section-variant-grid.liquid` | Phase 2 |
| 22 | Range Section | `sections/section-product-grid.liquid` (variant) | Phase 2 |
| 23 | Sticky ATC | `snippets/sticky-atc.liquid` + `sections/pdp-sticky-atc.liquid` | ✅ Phase 2 (D-023) |
| 24 | Promo Tiles | `sections/section-promo-tiles.liquid` | Phase 2 |
| 25 | Association Strip | `sections/section-association.liquid` | Phase 2 |
| 26 | FAQ Section | `sections/section-faq.liquid` (uses accordion snippet) | Phase 2 |
| — | Button | `snippets/button.liquid` | ✅ Phase 1 |
| — | Section Wrapper | `snippets/section-wrapper.liquid` (pattern doc) | ✅ Phase 1 |

---

## 4. Section Architecture

### Homepage Sections (per Doc 06, approved Home prototype)

| Order | Section | File |
|-------|---------|------|
| 1 | Announcement Strip | `section-ticker.liquid` |
| 2 | Header | `section-header.liquid` |
| 3 | Hero (50/50 split) | `section-hero.liquid` |
| 4 | Problem Section | `section-problem.liquid` |
| 5 | Disciplines + Proof | `section-disciplines.liquid` |
| 6 | Variant Grid | `section-variant-grid.liquid` |
| 7 | 50/50 Split × 3 | `section-split-50-50.liquid` |
| 8 | Coperni Collaboration | `section-coperni.liquid` |
| 9 | Full-Bleed Statement | `section-closing.liquid` |
| 10 | Reviews | `section-reviews.liquid` |
| 11 | Instagram | `section-social-feed.liquid` |
| 12 | Guarantee | `section-guarantee.liquid` |
| 13 | Footer | `section-footer.liquid` |

### Collection Sections (per Doc 09, approved Collection prototype)

| Order | Section | File |
|-------|---------|------|
| 1 | Collection Hero | `section-collection-hero.liquid` |
| 2 | Pillar Strip | `section-pillar-strip.liquid` |
| 3 | Sole Type Chooser | `section-sole-chooser.liquid` |
| 4 | Product Grid + Filters | `section-collection-grid.liquid` |
| 5 | Benefit Grid (3 cards) | `section-benefit-grid.liquid` |
| 6 | 50/50 Category Creation | `section-split-50-50.liquid` |
| 7 | FAQ (4–6 items) | `section-faq.liquid` |
| 8 | GEO Content | `section-geo-content.liquid` |
| 9 | Newsletter | `section-newsletter.liquid` |

### PDP Sections (per Doc 05, approved PDP prototype)

| Order | Section | File |
|-------|---------|------|
| 1 | PDP Main (Gallery + Buy Box) | `section-pdp-main.liquid` |
| 2 | Pillar Strip | `section-pillar-strip.liquid` |
| 3 | 50/50 Split (×2) | `section-split-50-50.liquid` |
| 4 | Full-Bleed Statement | `section-closing.liquid` |
| 5 | Reviews | `section-reviews.liquid` |
| 6 | Cross-Sell Grid | `section-pdp-cross-sell.liquid` |
| 7 | FAQ | `section-faq.liquid` |
| 8 | GEO Content | `section-geo-content.liquid` |
| 9 | Newsletter | `section-newsletter.liquid` |

---

## 5. Template Architecture

All templates use OS 2.0 JSON format (section references).

| Template | File | Sections |
|----------|------|----------|
| Homepage | `templates/index.json` | 13+ sections per Homepage order + GEO (D-022) |
| Product | `templates/product.json` | PDP sections + Sticky ATC (D-023) + GEO (D-022) |
| Collection | `templates/collection.json` | Collection sections + GEO (D-022) |
| Cart | `templates/cart.json` | Full cart page fallback (D-024, primary = drawer) |
| Page | `templates/page.json` | Rich text + custom |
| Page (About) | `templates/page.about.json` | Founder + Manifesto + custom |
| Article | `templates/article.json` | Hero + body + related |
| Blog | `templates/blog.json` | Featured + grid |
| Cart | `templates/cart.json` | Fallback (primary UX = drawer) |
| 404 | `templates/404.json` | Headline + search + CTA |

---

## 6. Settings Schema

### Theme-level Settings (`settings_schema.json`)

```json
[
  {
    "name": "theme_info",
    "theme_name": "Barreletics v2",
    "theme_version": "2.0.0"
  },
  {
    "name": "Colors",
    "settings": [
      { "type": "color", "id": "color_primary", "label": "Primary text", "default": "#1c1916" },
      { "type": "color", "id": "color_accent", "label": "Accent", "default": "#c45c3f" },
      { "type": "color", "id": "color_body_text", "label": "Body text", "default": "#4a4a4a" },
      { "type": "color", "id": "color_bg_alternate", "label": "Alternate BG", "default": "#f5f2ec" },
      { "type": "color", "id": "color_border", "label": "Border", "default": "#d6cfc0" }
    ]
  },
  {
    "name": "Typography",
    "settings": [
      { "type": "font_picker", "id": "font_heading", "label": "Heading font", "default": "roboto_n7" },
      { "type": "font_picker", "id": "font_body", "label": "Body font", "default": "roboto_n4" }
    ]
  },
  {
    "name": "Social Media",
    "settings": [
      { "type": "url", "id": "social_instagram", "label": "Instagram" },
      { "type": "url", "id": "social_tiktok", "label": "TikTok" },
      { "type": "url", "id": "social_facebook", "label": "Facebook" }
    ]
  },
  {
    "name": "Cart",
    "settings": [
      { "type": "select", "id": "cart_type", "label": "Cart type", "default": "drawer", "options": [
        { "value": "drawer", "label": "Drawer" },
        { "value": "page", "label": "Page" }
      ]}
    ]
  },
  {
    "name": "Free Shipping",
    "settings": [
      { "type": "number", "id": "free_shipping_threshold", "label": "Free shipping threshold ($)", "default": 150 }
    ]
  }
]
```

---

## 7. Asset Strategy

### CSS Architecture

| File | Purpose | Loading |
|------|---------|---------|
| `design-tokens.css` | All CSS custom properties | Global (in `<head>`) |
| `barreletics-base.css` | Reset, typography, utilities, buttons | Global (in `<head>`) |
| `component-*.css` | Per-section styles | Conditional via `{% stylesheet %}` |

**Rules:**
- No hardcoded hex in component CSS — use `var(--token)` always
- Mobile-first responsive approach
- Critical CSS inlined for above-fold content (hero, header, ticker)
- Component CSS lazy-loaded via `<link>` with `media="print" onload="this.media='all'"`

### JavaScript Architecture

| File | Purpose |
|------|---------|
| `global.js` | Utilities (debounce, throttle, a11y helpers, scroll observer) |
| `ticker.js` | Announcement rotation |
| `cart-drawer.js` | Cart AJAX operations |
| `pdp-gallery.js` | Image zoom/swap |
| `collection-filter.js` | Filter/sort with URL sync |

**Rules:**
- No jQuery. Vanilla JS only.
- Defer all non-critical JS
- Use `IntersectionObserver` for lazy-loading and scroll effects
- All interactions degrade gracefully without JS

### Image Handling

- Shopify CDN for all images
- Use `image_url` filter with explicit widths: 300, 600, 900, 1200
- `srcset` and `sizes` on all `<img>` tags
- `loading="lazy"` on below-fold images
- `fetchpriority="high"` on hero/LCP images
- Aspect ratio containers to prevent layout shift

---

## 8. SEO Implementation

### Structured Data (JSON-LD in `<head>`)

| Schema | Template | Priority |
|--------|----------|----------|
| `Product` + `AggregateRating` | PDP | P0 |
| `FAQPage` | Any page with FAQ section | P0 |
| `BreadcrumbList` | All pages (except home) | P0 |
| `CollectionPage` | Collection templates | P1 |
| `Organization` | Homepage | P1 |
| `WebSite` + `SearchAction` | Homepage | P1 |

### Meta Tags (per Doc 12)

```liquid
{%- comment -%} Title tag format {%- endcomment -%}
{% case template.name %}
  {% when 'index' %}
    Barreletics — Performance Skins for Barre, Pilates & Reformer
  {% when 'product' %}
    {{ product.title }} — {{ product.metafields.custom.sole_type }} | Barreletics
  {% when 'collection' %}
    Grippy Shoes for Barre, Pilates & Reformer | Barreletics
  {% when 'article' %}
    {{ article.title }} | Barreletics Journal
{% endcase %}
```

### URL Structure

| Page | URL | Canonical |
|------|-----|-----------|
| Pillar Collection | `/collections/grippy-shoes` | Self |
| Open Sole | `/collections/open-sole` | Self |
| Closed Sole | `/collections/closed-sole` | Self |
| Compare | `/pages/compare-open-closed-sole` | Self |
| Journal | `/blogs/journal` | Self |

**Rules:**
- No indexed filter params (`noindex` on `?filter=` pages OR canonical to base)
- 301 redirects from `/blogs/blog/` to `/blogs/journal/`
- Breadcrumbs include `BreadcrumbList` schema

---

## 9. Performance Requirements

| Metric | Target |
|--------|--------|
| LCP | < 2.5s |
| FID/INP | < 100ms |
| CLS | < 0.1 |
| Total page weight | < 500KB (initial, gzipped) |

### Implementation

- **Critical CSS:** Inline above-fold styles (header, hero) in `<head>`
- **Lazy loading:** `loading="lazy"` on all images below fold
- **Font loading:** `font-display: swap` on Roboto; self-host woff2 subsets
- **JS defer:** All JavaScript loaded with `defer` attribute
- **Image optimization:** Shopify CDN automatic WebP/AVIF with explicit dimensions
- **Preconnect:** `fonts.googleapis.com`, `fonts.gstatic.com`, `cdn.shopify.com`

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|---------------|
| Skip to content | First focusable element in DOM |
| Keyboard navigation | All interactive elements focusable, logical tab order |
| ARIA landmarks | `role="banner"`, `role="main"`, `role="contentinfo"` |
| Focus indicators | Visible `:focus-visible` ring on all interactive elements |
| Color contrast | WCAG AA (4.5:1 text, 3:1 large text) |
| Touch targets | ≥ 44px on mobile |
| Reduced motion | `prefers-reduced-motion` disables all animations |
| Screen reader | `aria-expanded`, `aria-controls`, `aria-live` regions |
| Form labels | Every input has associated `<label>` or `aria-label` |
| Image alt | Descriptive alt text on all content images |

---

## 11. Component Reuse Matrix

| Component | Home | PDP | Collection | About | FAQ | Article |
|-----------|------|-----|-----------|-------|-----|---------|
| Announcement Strip | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Header/Nav | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Footer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Trust Strip | ✓ | ✓ | ✓ | — | — | — |
| Pillar Strip | ✓ | ✓ | ✓ | — | — | — |
| 50/50 Split | ✓ (×3) | ✓ (×2) | ✓ | ✓ | — | — |
| Product Card | ✓ | ✓ | ✓ | — | — | — |
| FAQ Accordion | — | ✓ | ✓ | — | ✓ | — |
| Button | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Reviews | ✓ | ✓ | — | — | — | — |
| Newsletter | ✓ | ✓ | ✓ | — | — | — |
| Guarantee | ✓ | ✓ | — | ✓ | — | — |
| Breadcrumb | — | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 12. Build Order

### Phase 1 — Build System (This Phase) ✅

1. `shopify-build/assets/design-tokens.css` ← All Foundation tokens
2. `shopify-build/assets/barreletics-base.css` ← Reset, typography, utilities
3. `shopify-build/snippets/announcement-strip.liquid`
4. `shopify-build/snippets/header-nav.liquid`
5. `shopify-build/snippets/footer.liquid`
6. `shopify-build/snippets/product-card.liquid`
7. `shopify-build/snippets/faq-accordion.liquid`
8. `shopify-build/snippets/section-wrapper.liquid`
9. `shopify-build/snippets/trust-strip.liquid`
10. `shopify-build/snippets/button.liquid`
11. `planning/shopify-build-spec-v2.md` ← This document

### Phase 2 — Pages (Next)

1. `layout/theme.liquid` — Main layout with token loading
2. `sections/section-hero.liquid` — Homepage hero
3. `sections/section-pdp-main.liquid` — PDP gallery + buy box
4. `sections/section-collection-hero.liquid` — Collection hero
5. `sections/section-pillar-strip.liquid` — Shared pillar strip
6. `sections/section-split-50-50.liquid` — Reusable split
7. `sections/section-variant-grid.liquid` — Product selection grid
8. `sections/section-product-grid.liquid` — Generic product grid
9. `sections/section-reviews.liquid` — Reviews section
10. `sections/section-sock-math.liquid` — Cost comparison
11. `sections/section-faq.liquid` — FAQ section wrapper
12. `sections/section-newsletter.liquid` — Newsletter
13. `sections/section-guarantee.liquid` — Guarantee
14. `sections/section-collection-grid.liquid` — Collection grid + filters
15. `sections/section-geo-content.liquid` — GEO accordion
16. `templates/index.json` — Homepage assembly
17. `templates/product.json` — PDP assembly
18. `templates/collection.json` — Collection assembly

### Phase 3 — Supporting Pages

1. Founder / About sections
2. Manifesto / Closing sections
3. Blog / Article templates
4. Compare page
5. Cart drawer
6. 404 / Search

### Phase 4 — Polish & Deploy

1. Performance optimization
2. Structured data validation
3. Cross-browser testing
4. Accessibility audit
5. Theme migration plan

---

## Architectural Notes

### Gaps Resolved (Decision Log D-022 through D-025)

1. **GEO Content section** — ✅ Resolved (D-022). Required on all major pages. `snippets/geo-section.liquid` + FAQPage schema.
2. **Sticky ATC visibility** — ✅ Resolved (D-023). Hidden when native CTA visible, appears on scroll-out. IntersectionObserver trigger.
3. **Cart drawer vs page** — ✅ Resolved (D-024). Drawer is primary (AJAX), full page is secondary. Both built.
4. **Judge.me integration** — ✅ Resolved (D-025). Judge.me as data source only. Custom rendering via `snippets/review-card.liquid`.

---

**Cross-references:**
- Design tokens → `03-design-system.md`, Design System Skill
- Components → `04-component-library.md`
- Page architectures → `05-pdp-architecture.md`, `06-homepage-architecture.md`, `09-collection-architecture.md`
- Navigation → `11-navigation-architecture.md`
- SEO → `12-seo-geo-standards.md`
- Decisions → `10-decision-log.md`
