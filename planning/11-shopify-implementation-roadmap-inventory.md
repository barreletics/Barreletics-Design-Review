# Shopify Implementation Roadmap — Complete HTML Prototype Inventory

**Date:** July 13, 2026  
**Status:** BACKGROUND PREPARATION — Planning Only  
**Source:** Full repository audit of Barreletics-Design-Review  

---

## Table of Contents

1. [Repository Structure Overview](#1-repository-structure-overview)
2. [Canonical Prototypes (Build From These)](#2-canonical-prototypes)
3. [Section Maturation Studies (sections/)](#3-section-maturation-studies)
4. [Standalone Root Prototypes](#4-standalone-root-prototypes)
5. [Homepage Version History (files/)](#5-homepage-version-history)
6. [Design Review Archive (barreletics-design-review/)](#6-design-review-archive)
7. [Reusable Snippets to Extract](#7-reusable-snippets-to-extract)
8. [Shared CSS/JS Bundles](#8-shared-cssjs-bundles)
9. [Template Assignments](#9-template-assignments)
10. [Migration Sequence](#10-migration-sequence)
11. [Estimated Shopify File Structure](#11-estimated-shopify-file-structure)

---

## 1. Repository Structure Overview

```
Barreletics-Design-Review/
├── files/                          16 HTML homepage versions (v10–v24), v24 canonical
├── sections/                       39 HTML maturation studies, each with embedded CSS
├── Root HTML                       PDP v36, Design System v1.0, Section 26/27/28, matrices
├── barreletics-design-review/      Original design handoff archive (Matured pages, articles, CSS, JS)
│   ├── Barreletics Design Review/  Canonical matured pages + article variants + CSS/JS
│   ├── Barreletics_All_Versions/   v10–v24 homepage duplicates
│   ├── project/                    Earlier project folder with version subdirs
│   └── design_handoff_barreletics 2/  Handoff pages
├── docs/                           13 markdown specification documents
└── planning/                       This file
```

**Total HTML files:** ~300 (most are version history / duplicates)  
**Unique build-relevant prototypes:** ~25 distinct sections + 3 page templates

---

## 2. Canonical Prototypes (Build From These)

These are the **approved, latest-version** prototypes to build the Shopify theme from.

### 2.1 Homepage — `files/Barreletics_Home_v24.html`

| Field | Value |
|-------|-------|
| **Path** | `files/Barreletics_Home_v24.html` |
| **Renders** | Complete homepage with all sections: ticker, header, hero, problem/solution, media-text splits, disciplines, manifesto, credibility, product range, sock math, reviews, Coperni, founder letter, social feed, footer |
| **Shopify Mapping** | `templates/index.json` → references ~20 sections |
| **CSS** | Embedded `<style>` block (~4800 lines), design tokens in `:root`, full component styles |
| **JS Dependencies** | Vanilla JS: ticker rotator, slogan rotator, hero eyebrow rotator, Juicer social embed (`assets.juicer.io/embed.js`) |
| **Images** | 25+ Shopify CDN images (product shots, lifestyle, Coperni runway, shutterstock) |
| **Data Bindings** | `product.title`, `product.price`, `product.variants`, `product.images`, `product.metafields` for reviews/stats, collection for product grid, blog articles for journal cards |
| **Migration Complexity** | **Complex** — must decompose monolith into ~20 separate Liquid sections |
| **Dependencies** | Design system tokens, all homepage sections |

### 2.2 PDP — `Barreletics-PDP-v36-Jul2026.html`

| Field | Value |
|-------|-------|
| **Path** | `Barreletics-PDP-v36-Jul2026.html` |
| **Renders** | Full product detail page: hero (gallery + buy panel), brand benefits, variant grid with tab switching (closed/open sole), reviews, value comparison, motion grid, justifier quotes, FAQ accordion, newsletter |
| **Shopify Mapping** | `templates/product.json` → `sections/pdp-hero.liquid`, `sections/pdp-benefits.liquid`, `sections/pdp-variants.liquid`, `sections/pdp-reviews.liquid`, `sections/pdp-comparison.liquid`, `sections/pdp-faq.liquid`, `sections/pdp-newsletter.liquid` |
| **CSS** | Embedded `<style>` (~114 lines of component CSS), inline styles throughout |
| **JS Dependencies** | `v10Thumb()` gallery switcher, `v10Color()` swatch handler, `v10Size()` size selector, `switchTab()` variant tab toggle, `switchSize()` size filter, FAQ accordion toggle |
| **Images** | 12+ product images (Black, Dusty Rose, Stone, Coperni, etc.) from barreletics.com CDN |
| **Data Bindings** | `product.*` (title, price, variants, images, description), `product.metafields.reviews`, structured data (JSON-LD Product schema), color swatches from variant options |
| **Migration Complexity** | **Complex** — needs full Shopify product object integration, variant switching, cart AJAX, structured data |
| **Dependencies** | Product card snippet, swatch snippet, review snippet |

### 2.3 Design System — `Barreletics-DesignSystem-v1_0-Jul2026.html`

| Field | Value |
|-------|-------|
| **Path** | `Barreletics-DesignSystem-v1_0-Jul2026.html` |
| **Renders** | Complete design system reference: color palette, typography specimens, spacing scale, button variants, badge system, card components, grid system, audit table |
| **Shopify Mapping** | Not a customer-facing page — extracts to `assets/barreletics-tokens.css` and `snippets/` for component patterns |
| **CSS** | Embedded `<style>` (~140 lines), defines canonical token values |
| **JS Dependencies** | None |
| **Images** | Product card images from CDN |
| **Data Bindings** | None (reference only) |
| **Migration Complexity** | **Medium** — extract tokens to CSS custom properties file, create snippet library |
| **Dependencies** | None (foundational) |

### 2.4 Matured Homepage — `barreletics-design-review/Barreletics Design Review/Barreletics Home - Matured.html`

| Field | Value |
|-------|-------|
| **Path** | `barreletics-design-review/Barreletics Design Review/Barreletics Home - Matured.html` |
| **Renders** | Approved "matured direction" homepage — the final design-reviewed version |
| **Shopify Mapping** | Same as v24 but represents the design-approved direction |
| **CSS** | External: `maturation-styles.css`, `home-matured.css`, plus embedded audit stylesheet |
| **JS Dependencies** | `home-tweaks.jsx` (React via Babel), `ticker.js` |
| **Data Bindings** | Same as v24 |
| **Migration Complexity** | **Complex** — canonical source alongside v24 |
| **Dependencies** | External CSS files in same directory |

### 2.5 Matured PDP — `barreletics-design-review/Barreletics Design Review/Barreletics PDP - Matured.html`

| Field | Value |
|-------|-------|
| **Path** | `barreletics-design-review/Barreletics Design Review/Barreletics PDP - Matured.html` |
| **Renders** | Approved "matured direction" PDP |
| **Shopify Mapping** | Same as PDP v36 |
| **CSS** | External: `pdp-styles.css`, `maturation-styles.css` |
| **JS Dependencies** | `pdp-tweaks.jsx` |
| **Migration Complexity** | **Complex** |

### 2.6 Matured Collection — `barreletics-design-review/Barreletics Design Review/Barreletics Collection - Matured.html`

| Field | Value |
|-------|-------|
| **Path** | `barreletics-design-review/Barreletics Design Review/Barreletics Collection - Matured.html` |
| **Renders** | Collection page with filter bar, product grid, sort options |
| **Shopify Mapping** | `templates/collection.json` → `sections/collection-hero.liquid`, `sections/collection-grid.liquid` |
| **CSS** | External stylesheets |
| **JS Dependencies** | Filter/sort JS |
| **Data Bindings** | `collection.title`, `collection.products`, product card data, filter tags |
| **Migration Complexity** | **Medium** |

### 2.7 Blog Index — `barreletics-design-review/Barreletics Design Review/Barreletics Blog.html`

| Field | Value |
|-------|-------|
| **Path** | `barreletics-design-review/Barreletics Design Review/Barreletics Blog.html` |
| **Renders** | Blog listing page with article cards |
| **Shopify Mapping** | `templates/blog.json` → `sections/blog-grid.liquid` |
| **CSS** | External stylesheets |
| **Data Bindings** | `blog.articles`, `article.title`, `article.image`, `article.excerpt`, `article.published_at` |
| **Migration Complexity** | **Simple** |

### 2.8 Article Templates — `barreletics-design-review/Barreletics Design Review/Barreletics Article*.html`

| File | Renders |
|------|---------|
| `Barreletics Article.html` | Base article template |
| `Barreletics Article 02 Founder.html` | Founder story variant |
| `Barreletics Article 03 Coperni.html` | Coperni collaboration article |
| `Barreletics Article 04 Teacher.html` | Teacher/instructor story |
| `Barreletics Article 05 Retire.html` | "Retire your grip socks" article |
| `Barreletics Article 06 Barefoot.html` | Barefoot science article |

| Field | Value |
|-------|-------|
| **Shopify Mapping** | `templates/article.json` → `sections/article-hero.liquid`, `sections/article-body.liquid`, `sections/article-related.liquid` |
| **CSS** | External stylesheets |
| **Data Bindings** | `article.title`, `article.content`, `article.image`, `article.author`, `article.tags`, `blog.articles` for related |
| **Migration Complexity** | **Simple** — single template handles all variants via Liquid conditionals or metafields |

---

## 3. Section Maturation Studies (`sections/`)

All 39 files in `sections/` are **maturation study documents** — each is a full HTML page containing a study chrome wrapper (header, ToC, card layout) plus embedded "Current" vs "Matured" renderings of a specific homepage section.

**Common structure:** Each file contains ~5,300 lines of identical study chrome CSS (~170KB), plus the unique section content embedded within `.real-content` divs. The study chrome is NOT for production — only the matured section content inside each is relevant.

### Named Sections (unique section types)

| # | File | Section Name | Shopify Section | Data Bindings | CSS | JS | Images | Complexity | Dependencies |
|---|------|-------------|-----------------|---------------|-----|-----|--------|------------|-------------|
| 1 | `hero.html` | Hero Section | `sections/hero.liquid` | None (static copy), optional metafield for rotating eyebrows | Embedded (matured palette vars) | Eyebrow rotation interval | Hero background image/video | Medium | Ticker, header |
| 2 | `manifesto.html` | Brand Manifesto | `sections/manifesto.liquid` | None (static copy) | Embedded | None | Background texture optional | Simple | None |
| 3 | `manifesto2.html` | Brand Manifesto v2 | Same as above (variant) | None | Embedded | None | None | Simple | None |
| 4 | `problem.html` | The Problem Statement | `sections/problem-statement.liquid` | None (static copy) | Embedded | None | Optional lifestyle image | Simple | None |
| 5 | `problem2.html` | Problem Statement v2 | Same as above (variant) | None | Embedded | None | None | Simple | None |
| 6 | `disciplines.html` | Disciplines Index | `sections/disciplines.liquid` | Optional: metaobject for discipline list | Embedded | None | Discipline icons/images | Medium | None |
| 7 | `range.html` | Product Range | `sections/product-range.liquid` | `collection.products`, product card data | Embedded | Hover effects | Product images from CDN | Complex | Product card snippet |
| 8 | `variants.html` | Product Variants Grid | `sections/variant-grid.liquid` | `product.variants`, `collection.products` | Embedded | Tab switching, size filter | Product variant images | Complex | Product card snippet |
| 9 | `testimonial.html` | Customer Testimonials | `sections/testimonials.liquid` | Metafield or metaobject for reviews | Embedded | Optional carousel | Customer photos | Medium | Review card snippet |
| 10 | `credibility.html` | Credibility Band | `sections/credibility-band.liquid` | Static or metafield stats | Embedded | Counter animation optional | Logo images | Simple | None |
| 11 | `founder-letter.html` | Founder Letter | `sections/founder-letter.liquid` | Static copy or page content | Embedded | None | Founder photo | Simple | None |
| 12 | `founder2.html` | Founder Section v2 | Same as above (variant) | Same | Embedded | None | Same | Simple | None |
| 13 | `sock-math.html` | Sock Math Comparison | `sections/value-comparison.liquid` | Static pricing data or metafield | Embedded | None | None | Simple | None |
| 14 | `assoc.html` | Association / Credibility | `sections/association-band.liquid` | Static or metafield for logos/stats | Embedded | None | Partner/press logos | Simple | None |
| 15 | `split-section.html` | Media + Text Split v1 | `sections/media-text-split.liquid` | Optional: image/video from settings | Embedded | Video autoplay | Lifestyle image or video | Medium | None |
| 16 | `split-section2.html` | Media + Text Split v2 | Same section (alternate layout) | Same | Embedded | Same | Same | Medium | None |
| 17 | `split-section3.html` | Media + Text Split v3 | Same section (third variant) | Same | Embedded | Same | Same | Medium | None |
| 18 | `closing-statement.html` | Closing CTA | `sections/closing-cta.liquid` | None (static copy) | Embedded (~37 lines, minimal) | None | None | **Simple** | None |

### Numbered Sections (from decision matrix)

All numbered sections share the identical ~170KB study chrome wrapper. The unique content within each maps to a homepage section.

| # | File | Section Name (from title/matrix) | Shopify Section | Complexity |
|---|------|--------------------------------|-----------------|------------|
| 01 | `01-section.html` | Hero | `sections/hero.liquid` | Medium |
| 03 | `03-section.html` | 50/50 Progress / Trusted By | `sections/trusted-by.liquid` | Simple |
| 04 | `04-section.html` | Section 04 (undecided) | TBD | TBD |
| 06 | `06-section.html` | Section 06 (refactor) | TBD | Medium |
| 07 | `07-section.html` | Section 07 (refactor) | TBD | Medium |
| 08 | `08-section.html` | Section 08 (refactor) | TBD | Medium |
| 09 | `09-section.html` | The Problem (keep matured) | `sections/problem-statement.liquid` | Simple |
| 10 | `10-section.html` | Section 10 (refactor) | TBD | Medium |
| 12 | `12-section.html` | Section 12 (refactor) | TBD | Medium |
| 13 | `13-section.html` | Section 13 (refactor) | TBD | Medium |
| 14 | `14-section.html` | Section 14 (refactor) | TBD | Medium |
| 15 | `15-section.html` | Section 15 (undecided) | TBD | TBD |
| 18 | `18-section.html` | Section 18 (refactor) | TBD | Medium |
| 19 | `19-section.html` | Section 19 (refactor) | TBD | Medium |
| 20 | `20-section.html` | Section 20 (refactor) | TBD | Medium |
| 21 | `21-section.html` | Section 21 (refactor) | TBD | Medium |
| 23 | `23-section.html` | Section 23 (refactor) | TBD | Medium |
| 24 | `24-section.html` | Section 24 (undecided) | TBD | TBD |
| 25 | `25-section.html` | Section 25 (undecided) | TBD | TBD |
| 26 | `26-section.html` | Notes from Studio (refactor) | `sections/blog-cards.liquid` | Simple |
| 29 | `29-section.html` | Section 29 (undecided) | TBD | TBD |

---

## 4. Standalone Root Prototypes

### 4.1 Section 26 — Notes from the Studio

| Field | Value |
|-------|-------|
| **Path** | `Section-26-NotesFromStudio.html` |
| **Renders** | Blog/journal card grid — 3 cards with image, meta, title |
| **Shopify Mapping** | `sections/blog-cards.liquid` |
| **CSS** | Embedded (~130 lines), uses warm palette vars |
| **JS** | None |
| **Images** | 3 CDN images (Multi_Image.jpg, barreletixxjumpingtogether.jpg, Copreni_Final_More_grey.png) |
| **Data Bindings** | `blog.articles` (title, image, excerpt, tags for meta category, published_at for read time) |
| **Complexity** | **Simple** |
| **Dependencies** | Article card snippet |

### 4.2 Section 27 — FAQ

| Field | Value |
|-------|-------|
| **Path** | `Section-27-FAQ.html` |
| **Renders** | Accordion FAQ section — eyebrow, heading, 6 `<details>` items |
| **Shopify Mapping** | `sections/faq.liquid` (reusable on Home + PDP) |
| **CSS** | Embedded (~120 lines), warm palette with `<details>` styling |
| **JS** | None (native `<details>` element) |
| **Images** | None |
| **Data Bindings** | Section schema blocks (type: "faq_item") with `question` and `answer` fields |
| **Complexity** | **Simple** |
| **Dependencies** | None |

### 4.3 Section 28 — Newsletter Signup

| Field | Value |
|-------|-------|
| **Path** | `Section-28-Newsletter.html` |
| **Renders** | Email capture with eyebrow, heading, description, email input + CTA, fine print |
| **Shopify Mapping** | `sections/newsletter.liquid` (reusable on Home + PDP) |
| **CSS** | Embedded (~140 lines), responsive flex → column on mobile |
| **JS** | None (form submission handled by Shopify/Klaviyo) |
| **Images** | None |
| **Data Bindings** | Section settings for heading, description, CTA text, discount code display |
| **Complexity** | **Simple** |
| **Dependencies** | Klaviyo or Shopify newsletter integration |

### 4.4 Section Decision Matrix

| Field | Value |
|-------|-------|
| **Path** | `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` |
| **Renders** | Interactive preview panel + section list with decisions (Keep/Refactor/Undecided) |
| **Shopify Mapping** | N/A — internal planning tool |
| **Complexity** | N/A |

### 4.5 matrix-20260707.html

| Field | Value |
|-------|-------|
| **Path** | `matrix-20260707.html` |
| **Renders** | Section decision matrix with iframe preview and decision sidebar |
| **Shopify Mapping** | N/A — internal planning tool |
| **Complexity** | N/A |

### 4.6 Everything Index

| Field | Value |
|-------|-------|
| **Path** | `Barreletics-Everything-Index.html` |
| **Renders** | Master index of all sections with current vs matured comparison, embedded study chrome |
| **Shopify Mapping** | N/A — reference document containing all section renderings in one page |
| **Complexity** | N/A |

### 4.7 index.html (root)

| Field | Value |
|-------|-------|
| **Path** | `index.html` |
| **Renders** | Simple redirect/link page |
| **Shopify Mapping** | N/A |
| **Complexity** | N/A |

---

## 5. Homepage Version History (`files/`)

These are **historical iterations only** — do NOT build from these. v24 is canonical.

| File | Description | Status |
|------|-------------|--------|
| `Barreletics_Home_v10.html` | Early version (~112KB) | Superseded |
| `Barreletics_Home_v11.html` | ~130KB | Superseded |
| `Barreletics_Home_v12.html` | ~129KB | Superseded |
| `Barreletics_Home_v13.html` | ~134KB | Superseded |
| `Barreletics_Home_v14.html` | ~134KB | Superseded |
| `Barreletics_Home_v15.html` | ~135KB | Superseded |
| `Barreletics_Home_v16.html` | ~136KB | Superseded |
| `Barreletics_Home_v17.html` | ~138KB | Superseded |
| `Barreletics_Home_v18.html` | ~143KB | Superseded |
| `Barreletics_Home_v19.html` | ~142KB | Superseded |
| `Barreletics_Home_v20.html` | ~146KB | Superseded |
| `Barreletics_Home_v21.html` | ~151KB | Superseded |
| `Barreletics_Home_v22.html` | ~151KB | Superseded |
| `Barreletics_Home_v23.html` | ~151KB | Superseded |
| **`Barreletics_Home_v24.html`** | **~152KB — CANONICAL** | **Build from this** |
| `index.html` | Directory index | N/A |

---

## 6. Design Review Archive (`barreletics-design-review/`)

### 6.1 Canonical Matured Pages (in `Barreletics Design Review/`)

| File | Type | Status |
|------|------|--------|
| `Barreletics Home - Matured.html` | Homepage | **CANONICAL** — build reference |
| `Barreletics PDP - Matured.html` | Product page | **CANONICAL** — build reference |
| `Barreletics Collection - Matured.html` | Collection page | **CANONICAL** — build reference |
| `Barreletics Article.html` | Article base template | **CANONICAL** |
| `Barreletics Article 02–06 *.html` | Article variants (5) | **CANONICAL** |
| `Barreletics Blog.html` | Blog index | **CANONICAL** |
| `Barreletics Audit.html` | Design audit document | Reference only |
| `Barreletics Maturation Study.html` | Current vs matured comparison | Reference only |
| `Barreletics Wireframes.html` | Lo-fi wireframes | Reference only |
| `Section 15 - Variant Grid v28.html` | Standalone variant grid study | Reference for variant grid section |
| `Barreletics Home v2–v10.html` | Earlier home explorations (9 files) | Superseded |
| `Barreletics PDP v2.html` | Earlier PDP exploration | Superseded |
| `Barreletics Collection.html` | Earlier collection exploration | Superseded |

### 6.2 External CSS/JS Assets (in `Barreletics Design Review/`)

| File | Purpose | Shopify Target |
|------|---------|----------------|
| `audit-styles.css` | Primary token + component stylesheet | Extract tokens → `assets/barreletics-tokens.css` |
| `maturation-styles.css` | Matured-direction stylesheet | Extract → `assets/barreletics-base.css` |
| `home-matured.css` | Home-only matured overrides | `assets/section-home.css` or inline |
| `pdp-styles.css` | PDP-only styles | `assets/section-pdp.css` or inline |
| `pages-extras.css` | Cross-page extras (tab strip, etc.) | `assets/barreletics-components.css` |
| `section-mocks.css` | Section catalog styles | N/A (dev reference) |
| `wireframes-styles.css` | Wireframe-only | N/A |
| `ticker.js` | Ticker bar rotation logic | `assets/ticker.js` |
| `audit-behavior.js` | Audit page interactions | N/A |
| `home-tweaks.jsx` | React tweaks panel for home | N/A (dev tool) |
| `pdp-tweaks.jsx` | React tweaks panel for PDP | N/A (dev tool) |
| `audit-tweaks.jsx` | Audit tweaks | N/A |
| `tweaks-panel.jsx` | Shared tweaks panel | N/A |

### 6.3 Duplicate/Archive Directories

| Directory | Contents | Status |
|-----------|----------|--------|
| `Barreletics_All_Versions/` | v10–v24 homepage duplicates (identical to `files/`) | Ignore — use `files/` |
| `project/` | Earlier project folder with version subdirectories | Superseded |
| `design_handoff_barreletics 2/` | Earlier handoff with subset of pages | Superseded |
| `versions/` (multiple) | Date-stamped version archives | Superseded |

---

## 7. Reusable Snippets to Extract

These patterns appear across multiple sections/templates and should be built as Liquid snippets.

### 7.1 `snippets/product-card.liquid`
- **Used in:** Homepage range section, PDP variants grid, collection page
- **Source:** v24 lines 345–433 (variant cards), PDP v36 lines 345–458
- **Props:** product object, show_badge, show_size, show_price, show_cta
- **Features:** Hover scale effect, LE badge, "Notify Me" vs "Add to Cart", size pill

### 7.2 `snippets/section-header.liquid`
- **Used in:** Every content section on Home and PDP
- **Source:** Pattern: eyebrow (11–12px uppercase) + h2 heading + optional description
- **Props:** eyebrow_text, heading, description, alignment (center/left)

### 7.3 `snippets/review-card.liquid`
- **Used in:** PDP reviews section, homepage testimonials
- **Source:** PDP v36 lines 488–519
- **Props:** image, stars, quote, author_name, author_title

### 7.4 `snippets/color-swatch.liquid`
- **Used in:** PDP hero buy panel, collection page filters
- **Source:** PDP v36 lines 190–206
- **Props:** color_hex, color_name, variant_image_url, selected state, LE badge

### 7.5 `snippets/faq-item.liquid`
- **Used in:** FAQ section (home + PDP)
- **Source:** Section-27-FAQ.html, PDP v36 FAQ section
- **Props:** question, answer, open_by_default

### 7.6 `snippets/newsletter-form.liquid`
- **Used in:** Newsletter section (home + PDP)
- **Source:** Section-28-Newsletter.html, PDP v36 newsletter section
- **Props:** heading, description, cta_text, fine_print, integration (Klaviyo/Shopify)

### 7.7 `snippets/article-card.liquid`
- **Used in:** Blog cards section, blog index, related articles
- **Source:** Section-26-NotesFromStudio.html
- **Props:** article object, show_meta, show_image

### 7.8 `snippets/badge.liquid`
- **Used in:** Product cards, PDP hero, collection grid
- **Source:** Design System v1.0 (badge system)
- **Props:** type (le, sole, size, new, soldout), text

### 7.9 `snippets/media-text-split.liquid`
- **Used in:** Homepage split sections, PDP brand section
- **Source:** split-section.html, split-section2.html, split-section3.html
- **Props:** media_type (image/video), media_url, heading, body, cta, layout (media-left/media-right)

### 7.10 `snippets/trust-badges.liquid`
- **Used in:** PDP buy panel, checkout
- **Source:** PDP v36 lines 225–229
- **Props:** badges array (ships, returns, warranty, allergen-free)

---

## 8. Shared CSS/JS Bundles

### 8.1 CSS Architecture

```
assets/
├── barreletics-tokens.css      ← Design tokens (:root custom properties)
│                                  Source: DesignSystem v1.0 + v24 :root block
│                                  Colors, typography scale, spacing scale, button tokens
│
├── barreletics-base.css        ← Global resets, typography, base components
│                                  Source: maturation-styles.css + v24 global rules
│                                  Reset, body, links, images, utility classes
│
├── barreletics-components.css  ← Shared component styles
│                                  Source: pages-extras.css + component patterns from v24
│                                  Buttons, badges, cards, forms, accordions
│
├── section-hero.css            ← Hero section styles (or embed in section)
├── section-pdp.css             ← PDP-specific styles
│                                  Source: pdp-styles.css
│
└── (section-specific CSS)      ← Inline in each section's <style> tag per Shopify pattern
```

### 8.2 Design Token Values (from v24 `:root`)

```css
/* Brand Colors */
--br-bg: #ffffff;
--br-alt-bg: #f9f9f9;
--br-alt-bg-2: #f3f3f3;
--br-text: #050505;
--br-text-soft: #4a4a4a;
--br-text-mute: #8a8a8a;
--br-line: #e6e6e6;
--br-accent: #f97250;        /* Cart badge only */
--br-star: #fbc02d;
--br-button: #050505;
--br-button-text: #ffffff;

/* Matured Palette (warm direction) */
--m-bg: #f1ede4;
--m-ink: #1c1916;
--m-soft: #6b645a;
--m-mute: #9a9182;
--m-line: #e2dccf;
--m-dark: #24201b;
--m-accent: #c45c3f;         /* Terracotta */

/* Typography */
--t-font: 'Roboto', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
--t-eyebrow: 12px;
--t-body: 16px;
--t-h4: 28px;
--t-h3: 36px;
--t-h2: 44px;
--t-h1: 56px;

/* Spacing */
--sp-4: 16px; --sp-5: 24px; --sp-6: 32px; --sp-7: 48px; --sp-8: 64px;

/* Buttons */
--btn-radius: 0px;
--btn-pad-y: 14px;
--btn-pad-x: 28px;
--btn-weight: 600;
```

### 8.3 JavaScript

| File | Purpose | Source |
|------|---------|--------|
| `assets/ticker.js` | Announcement bar rotation (crossfade, 5s interval, pause on hover) | v24 lines 4855–4868, `ticker.js` |
| `assets/pdp-interactions.js` | Gallery thumb switching, color swatch selection, size selection, variant tab toggle, FAQ accordion | PDP v36 inline scripts |
| `assets/rotating-text.js` | Hero eyebrow rotation + slogan rotation | v24 lines 4898–4941 |

**External dependencies:**
- Google Fonts: Roboto 300–700 (load via `<link>` or `@import`)
- Juicer social feed: `assets.juicer.io/embed.js` + `assets.juicer.io/embed.css` (for social UGC section)

---

## 9. Template Assignments

### 9.1 `templates/index.json` (Homepage)

Sections in order (derived from v24 structure):

1. `sections/ticker-bar.liquid` — Announcement bar
2. `sections/header.liquid` — Navigation (global)
3. `sections/hero.liquid` — Hero with rotating eyebrow
4. `sections/trusted-by.liquid` — 50/50 progress / credibility stats
5. `sections/problem-statement.liquid` — "The Problem" section
6. `sections/media-text-split.liquid` — Image + text (configurable layout)
7. `sections/disciplines.liquid` — Discipline grid (barre, Pilates, etc.)
8. `sections/manifesto.liquid` — Brand manifesto
9. `sections/credibility-band.liquid` — Stats/proof band
10. `sections/product-range.liquid` — Product grid from collection
11. `sections/value-comparison.liquid` — Sock math / cost comparison
12. `sections/testimonials.liquid` — Customer reviews
13. `sections/founder-letter.liquid` — Founder section
14. `sections/association-band.liquid` — Coperni / press logos
15. `sections/blog-cards.liquid` — Journal / Notes from Studio
16. `sections/faq.liquid` — FAQ accordion
17. `sections/newsletter.liquid` — Email capture
18. `sections/closing-cta.liquid` — Final CTA (dark bg)
19. `sections/social-feed.liquid` — Juicer UGC feed
20. `sections/footer.liquid` — Footer (global)

### 9.2 `templates/product.json` (PDP)

Sections in order (from PDP v36):

1. `sections/ticker-bar.liquid`
2. `sections/header.liquid`
3. `sections/pdp-hero.liquid` — Gallery + buy panel (2-column)
4. `sections/pdp-benefits.liquid` — "Why Barreletics" 4-grid
5. `sections/pdp-variants.liquid` — Variant grid with tab switching
6. `sections/pdp-reviews.liquid` — Review cards with images
7. `sections/pdp-comparison.liquid` — Value comparison (3-col)
8. `sections/pdp-motion.liquid` — Motion/video grid
9. `sections/pdp-justifier.liquid` — Quote cards
10. `sections/faq.liquid` — Reused from homepage
11. `sections/newsletter.liquid` — Reused from homepage
12. `sections/footer.liquid`

### 9.3 `templates/collection.json`

1. `sections/header.liquid`
2. `sections/collection-hero.liquid` — Collection title + description
3. `sections/collection-grid.liquid` — Product grid with filters
4. `sections/newsletter.liquid`
5. `sections/footer.liquid`

### 9.4 `templates/blog.json`

1. `sections/header.liquid`
2. `sections/blog-hero.liquid` — Blog title
3. `sections/blog-grid.liquid` — Article card grid
4. `sections/newsletter.liquid`
5. `sections/footer.liquid`

### 9.5 `templates/article.json`

1. `sections/header.liquid`
2. `sections/article-hero.liquid` — Article header with image
3. `sections/article-body.liquid` — Rich text content
4. `sections/article-related.liquid` — Related articles grid
5. `sections/newsletter.liquid`
6. `sections/footer.liquid`

---

## 10. Migration Sequence

### Phase 0: Foundation (Week 1)
**Build order: tokens → globals → snippets → then sections**

| Step | Task | Source | Output | Effort |
|------|------|--------|--------|--------|
| 0.1 | Extract design tokens | DesignSystem v1.0, v24 `:root` | `assets/barreletics-tokens.css` | 2h |
| 0.2 | Base stylesheet | maturation-styles.css, v24 globals | `assets/barreletics-base.css` | 4h |
| 0.3 | Component stylesheet | v24 component patterns | `assets/barreletics-components.css` | 4h |
| 0.4 | Product card snippet | v24 + PDP v36 card pattern | `snippets/product-card.liquid` | 4h |
| 0.5 | Section header snippet | Universal eyebrow + heading | `snippets/section-header.liquid` | 1h |
| 0.6 | Badge snippet | DesignSystem badge system | `snippets/badge.liquid` | 1h |
| 0.7 | Review card snippet | PDP v36 review card | `snippets/review-card.liquid` | 2h |
| 0.8 | Color swatch snippet | PDP v36 swatch pattern | `snippets/color-swatch.liquid` | 3h |
| 0.9 | Trust badges snippet | PDP v36 trust line | `snippets/trust-badges.liquid` | 1h |
| 0.10 | Article card snippet | Section 26 card pattern | `snippets/article-card.liquid` | 2h |

**Phase 0 total: ~24h (3 days)**

### Phase 1: Global Components (Week 1–2)
**Header, footer, ticker — used on every page**

| Step | Task | Source | Output | Effort |
|------|------|--------|--------|--------|
| 1.1 | Ticker bar section | v24 ticker + ticker.js | `sections/ticker-bar.liquid` | 4h |
| 1.2 | Header / navigation | v24 header markup | `sections/header.liquid` | 8h |
| 1.3 | Footer | v24 footer (5-col grid) | `sections/footer.liquid` | 4h |
| 1.4 | Newsletter section | Section-28 + PDP newsletter | `sections/newsletter.liquid` | 3h |
| 1.5 | FAQ section | Section-27 + PDP FAQ | `sections/faq.liquid` | 3h |

**Phase 1 total: ~22h (3 days)**

### Phase 2: Homepage Sections (Week 2–3)
**Build sections in page order, top to bottom**

| Step | Task | Source | Output | Effort |
|------|------|--------|--------|--------|
| 2.1 | Hero section | hero.html (matured), v24 hero | `sections/hero.liquid` | 8h |
| 2.2 | Trusted-by band | 03-section.html, v24 | `sections/trusted-by.liquid` | 3h |
| 2.3 | Problem statement | problem.html (matured), 09-section | `sections/problem-statement.liquid` | 3h |
| 2.4 | Media + text split | split-section*.html | `sections/media-text-split.liquid` | 6h |
| 2.5 | Disciplines grid | disciplines.html | `sections/disciplines.liquid` | 4h |
| 2.6 | Brand manifesto | manifesto.html | `sections/manifesto.liquid` | 3h |
| 2.7 | Credibility band | credibility.html | `sections/credibility-band.liquid` | 3h |
| 2.8 | Product range | range.html, v24 product grid | `sections/product-range.liquid` | 6h |
| 2.9 | Value comparison | sock-math.html | `sections/value-comparison.liquid` | 4h |
| 2.10 | Testimonials | testimonial.html | `sections/testimonials.liquid` | 4h |
| 2.11 | Founder letter | founder-letter.html | `sections/founder-letter.liquid` | 3h |
| 2.12 | Association band | assoc.html | `sections/association-band.liquid` | 3h |
| 2.13 | Blog cards | Section-26-NotesFromStudio.html | `sections/blog-cards.liquid` | 3h |
| 2.14 | Closing CTA | closing-statement.html | `sections/closing-cta.liquid` | 2h |
| 2.15 | Social feed | v24 Juicer embed | `sections/social-feed.liquid` | 2h |

**Phase 2 total: ~57h (7 days)**

### Phase 3: PDP (Week 3–4)
**The most complex template — product data integration**

| Step | Task | Source | Output | Effort |
|------|------|--------|--------|--------|
| 3.1 | PDP hero (gallery + buy) | PDP v36 hero section | `sections/pdp-hero.liquid` | 16h |
| 3.2 | PDP benefits grid | PDP v36 brand section | `sections/pdp-benefits.liquid` | 4h |
| 3.3 | PDP variant grid | PDP v36 variants + Section 15 | `sections/pdp-variants.liquid` | 12h |
| 3.4 | PDP reviews | PDP v36 reviews | `sections/pdp-reviews.liquid` | 4h |
| 3.5 | PDP value comparison | PDP v36 comparison | `sections/pdp-comparison.liquid` | 4h |
| 3.6 | PDP motion grid | PDP v36 motion section | `sections/pdp-motion.liquid` | 4h |
| 3.7 | PDP justifier quotes | PDP v36 justifier | `sections/pdp-justifier.liquid` | 3h |
| 3.8 | Cart AJAX integration | N/A (new) | `assets/cart.js` + snippets | 8h |
| 3.9 | Structured data (JSON-LD) | PDP v36 schema | `snippets/product-schema.liquid` | 3h |

**Phase 3 total: ~58h (7 days)**

### Phase 4: Collection + Blog + Article (Week 4–5)

| Step | Task | Source | Output | Effort |
|------|------|--------|--------|--------|
| 4.1 | Collection hero | Collection - Matured.html | `sections/collection-hero.liquid` | 3h |
| 4.2 | Collection grid + filters | Collection - Matured.html | `sections/collection-grid.liquid` | 12h |
| 4.3 | Blog hero + grid | Blog.html | `sections/blog-hero.liquid`, `sections/blog-grid.liquid` | 6h |
| 4.4 | Article template | Article*.html (all 6) | `sections/article-hero.liquid`, `sections/article-body.liquid`, `sections/article-related.liquid` | 8h |
| 4.5 | Template JSON files | N/A | `templates/*.json` | 4h |

**Phase 4 total: ~33h (4 days)**

### Phase 5: Refactor Sections (Week 5–6)
**Sections marked "refactor" in decision matrix — depends on design decisions**

| Step | Task | Sections | Effort |
|------|------|----------|--------|
| 5.1 | Color compliance audit | All sections — remove black/orange | 4h |
| 5.2 | Refactor batch 1 (high priority) | 06, 07, 08, 10 | 16h |
| 5.3 | Refactor batch 2 | 12, 13, 14, 18 | 16h |
| 5.4 | Refactor batch 3 | 19, 20, 21, 23 | 16h |
| 5.5 | Clarify decisions | 04, 15, 24, 25, 29 | Blocked on design |

**Phase 5 total: ~52h (6–7 days) — partially blocked**

### Total Estimated Effort

| Phase | Effort | Duration |
|-------|--------|----------|
| Phase 0: Foundation | 24h | 3 days |
| Phase 1: Globals | 22h | 3 days |
| Phase 2: Homepage | 57h | 7 days |
| Phase 3: PDP | 58h | 7 days |
| Phase 4: Collection/Blog/Article | 33h | 4 days |
| Phase 5: Refactors | 52h | 6 days |
| **Total** | **~246h** | **~30 working days (6 weeks)** |

---

## 11. Estimated Shopify File Structure

```
barreletics-theme/
├── layout/
│   └── theme.liquid                    ← Main layout (loads tokens + base CSS)
│
├── templates/
│   ├── index.json                      ← Homepage (20 sections)
│   ├── product.json                    ← PDP (12 sections)
│   ├── collection.json                 ← Collection (5 sections)
│   ├── blog.json                       ← Blog index (5 sections)
│   ├── article.json                    ← Article (6 sections)
│   ├── page.json                       ← Generic page
│   ├── 404.json                        ← 404 page
│   └── cart.json                       ← Cart page
│
├── sections/
│   ├── ticker-bar.liquid               ← Announcement bar
│   ├── header.liquid                   ← Navigation
│   ├── footer.liquid                   ← Footer
│   ├── hero.liquid                     ← Homepage hero
│   ├── trusted-by.liquid               ← Credibility stats bar
│   ├── problem-statement.liquid        ← The Problem section
│   ├── media-text-split.liquid         ← Configurable image+text split
│   ├── disciplines.liquid              ← Discipline grid
│   ├── manifesto.liquid                ← Brand manifesto
│   ├── credibility-band.liquid         ← Stats band
│   ├── product-range.liquid            ← Product collection grid
│   ├── value-comparison.liquid         ← Sock math / cost comparison
│   ├── testimonials.liquid             ← Review cards
│   ├── founder-letter.liquid           ← Founder section
│   ├── association-band.liquid         ← Partner/press logos
│   ├── blog-cards.liquid               ← Journal article cards
│   ├── faq.liquid                      ← FAQ accordion (reusable)
│   ├── newsletter.liquid               ← Email capture (reusable)
│   ├── closing-cta.liquid              ← Dark CTA section
│   ├── social-feed.liquid              ← Juicer UGC embed
│   ├── pdp-hero.liquid                 ← PDP gallery + buy panel
│   ├── pdp-benefits.liquid             ← "Why Barreletics" grid
│   ├── pdp-variants.liquid             ← Variant grid with tabs
│   ├── pdp-reviews.liquid              ← PDP review cards
│   ├── pdp-comparison.liquid           ← PDP value comparison
│   ├── pdp-motion.liquid               ← Motion/video grid
│   ├── pdp-justifier.liquid            ← Quote/justifier cards
│   ├── collection-hero.liquid          ← Collection header
│   ├── collection-grid.liquid          ← Collection product grid
│   ├── blog-hero.liquid                ← Blog header
│   ├── blog-grid.liquid                ← Blog article grid
│   ├── article-hero.liquid             ← Article header
│   ├── article-body.liquid             ← Article content
│   └── article-related.liquid          ← Related articles
│
├── snippets/
│   ├── product-card.liquid             ← Reusable product card
│   ├── section-header.liquid           ← Eyebrow + heading pattern
│   ├── review-card.liquid              ← Review card component
│   ├── color-swatch.liquid             ← Color swatch button
│   ├── faq-item.liquid                 ← FAQ accordion item
│   ├── newsletter-form.liquid          ← Newsletter form component
│   ├── article-card.liquid             ← Blog article card
│   ├── badge.liquid                    ← Product badge (LE, size, etc.)
│   ├── media-split-block.liquid        ← Media+text block
│   ├── trust-badges.liquid             ← Trust badge row
│   ├── product-schema.liquid           ← JSON-LD structured data
│   └── css-variables.liquid            ← CSS custom properties output
│
├── assets/
│   ├── barreletics-tokens.css          ← Design tokens
│   ├── barreletics-base.css            ← Global styles
│   ├── barreletics-components.css      ← Shared components
│   ├── ticker.js                       ← Announcement bar rotation
│   ├── pdp-interactions.js             ← Gallery, swatches, variants
│   ├── rotating-text.js                ← Hero eyebrow + slogan rotation
│   ├── cart.js                         ← AJAX cart
│   └── barreletics-logo.png            ← Brand mark
│
└── config/
    ├── settings_schema.json            ← Theme settings schema
    └── settings_data.json              ← Theme settings values
```

**Total new files: ~55** (34 sections + 12 snippets + 6 assets + 3 templates)

---

## Appendix: Image Asset Registry

All images referenced across prototypes, grouped by source:

### Product Images (barreletics.com CDN)
- `Outside_Black-600x600_*.jpg` — Black closed sole
- `Dusty_Rose_*.png` — Dusty Rose
- `A14_TopBottom_LightGrey-*.jpg` — Light Grey / Stone
- `Copreni_Final_More_grey.png` — Coperni collaboration
- `Yellow.jpg` — Yellow shoe
- `Yellow_Image-Blue_Shoe*.jpg` — Yellow bg, blue shoe

### Lifestyle / Hero Images
- `IMG_2917.jpg` — Hero pink foot
- `Multi_Image.jpg` — Multi-image pink composite
- `P5A50992*.jpg` — Barre class
- `View_recent_photos.png` — Pilates/reformer
- `P5A7000_blue_background_2.jpg` — Blue bg studio
- `barrletixx_blue_pants_FINAL*.jpg` — Blue pants
- `IMG_5051.jpg` — Lifestyle shot
- `shutterstock_image-2.jpg` — B&W stock
- `IMG_2697.jpg` — Woman with straps
- `barreletixxstefrunningpinkbackground.jpg` — Stef running

### Coperni Assets
- `Copreni_Final_More_grey.png` — Product shot
- `Screenshot_2026-03-20_at_6.53.30_PM.png` — Runway 1
- `Screenshot_2026-03-21_at_3.04.37_PM.png` — Runway 2

### Videos (Shopify CDN)
- `d11716a75dc64da7ba1a5521e39d942b.mov` — Pink foot drop
- `250a03bea9fd4242a756b51f8760235c.mp4` — Action v1
- `c6323baf4755466f9e7c89426798e8f2.mp4` — Action v2
- `a521325325ff48e2a3fee59b9f6906bb.mov` — Action v3
- `59871813adec446c95448a683d221ef0.mov` — Workout
- Slip-it-on and Rinse videos (vp hosted)
- `d7ca87eac5034642851089c63af6a2d8.mov` — Coperni runway

### Brand Assets
- `barreleticslogo.png` — Full logo
- `barreleticsmark.png` — Favicon / mark

---

## Appendix: Critical Design Rules (from Decision Matrix)

1. **NO orange + black combinations** — warm or neutral only
2. **Accent color:** Terracotta `#c45c3f` (matured) or coral `#f97250` (cart badge only)
3. **Font:** Roboto only, weights 300–700
4. **Border radius:** 0px default, max 4px where matured direction specifies
5. **Button style:** Square (`border-radius: 0px`), no shadows, no gradients
6. **Max content width:** 1200–1320px
7. **Gutters:** 32px desktop, 16px mobile
8. **Section padding:** 80px vertical desktop, 40–48px mobile

---

## PROTOTYPE-TO-SHOPIFY MAPPING

Cross-reference of every prototype HTML file that maps to a Shopify deliverable. CEO decisions sourced from `barreletics-decisions-2026-07-09.json`; architecture from `docs/03-DESIGN-SYSTEM.md` and `docs/04-COMPONENT-LIBRARY.md`.

### Homepage Prototypes

| Source HTML | CEO Decision | Target Shopify File(s) | Required Settings Schema | Content to Migrate |
|---|---|---|---|---|
| `files/Barreletics_Home_v24.html` | N/A (canonical build source) | `templates/index.json` + 20 sections | All homepage section schemas | All homepage section content, copy, images, videos |
| `barreletics-design-review/Barreletics Design Review/Barreletics Home - Matured.html` | N/A (design-approved direction) | Same — design reference for matured palette/layout | Matured token values for `settings_schema.json` | Matured direction copy and styling cues |
| `sections/hero.html` + `01-section.html` | **Keep** (custom blend) — "Add 'See in action' button. Use eyebrow from current." Owner: Cowork | `sections/hero.liquid` | `heading`, `subheading`, `eyebrow_messages` (list), `bg_image`, `bg_video`, `primary_cta_text`, `primary_cta_url`, `secondary_cta_text`, `secondary_cta_url` | Hero headline, 5 rotating eyebrow messages, CTA copy, hero image (IMG_2917.jpg) |
| `sections/problem.html` + `09-section.html` | **Keep** (matured) — "current, mature 1, and mature 2 are all good" | `sections/problem-statement.liquid` | `eyebrow`, `heading`, `body`, `items` (block list with strikethrough text) | Problem statement copy, old-solution list |
| `03-section.html` | **Keep** (custom blend) — "Keep 'Trusted by' rating from current." Owner: Cowork | `sections/trusted-by.liquid` | `heading`, `subheading`, `stat_1_number`, `stat_1_label`, `stat_2_number`, `stat_2_label`, `image`, `stars_visible` | Trusted-by stats, star rating, image |
| Section 17 (in v24) | **Keep** (current) — "modification of current 50/50 section… few aesthetic updates and font changes" | `sections/media-text-split.liquid` (instance) | `heading`, `body`, `image`, `video_url`, `layout` (media-left/media-right), `show_trusted_line`, `bg_color` | "Never slip in chair pose" copy, Multi_Image.jpg |
| `sections/split-section.html` / `split-section2.html` / `split-section3.html` | Sections 20, 21: **Refactor** (matured) — "shared 50/50 section with functionality options?" | `sections/media-text-split.liquid` | `heading`, `body`, `media_type` (image/video), `media_url`, `layout`, `show_trusted_line`, `bg_color`, `text_color` | Split copy variants, lifestyle images, pink foot video |
| `sections/disciplines.html` + `08-section.html` | **Refactor** (matured) — "excellent — can we have settings to tweak once built?" | `sections/disciplines.liquid` | `eyebrow`, `heading`, blocks: `discipline_card` (name, description, image, link) | Discipline names (Barre, Reformer, Megaformer), descriptions, images |
| `sections/manifesto.html` / `manifesto2.html` | N/A (included in homepage flow) | `sections/manifesto.liquid` | `eyebrow`, `statements` (rotating text list), `subtitle`, `voice_tags` (list) | Manifesto rotating statements, voice tags |
| `sections/credibility.html` + `06-section.html` | **Refactor** (current) — "update in JudgeMe, display images, maybe more than one layout?" Owner: Cowork | `sections/credibility-band.liquid` | `eyebrow`, `heading`, `subtext`, blocks: `credibility_cell` (image, caption, stat), `logo_bar` (logos) | Studio images/captions, partner logos, stat numbers |
| `sections/range.html` | N/A (homepage product grid) | `sections/product-range.liquid` | `collection` (collection picker), `heading`, `eyebrow`, `max_products`, `columns` | Collection handle, product grid config |
| `sections/sock-math.html` + Section 19 | **Refactor** — "excellent but huge, black and orange sucks, needs more neutral with punch" | `sections/value-comparison.liquid` | `eyebrow`, `heading`, `subtext`, `card_1_*` (label, price, subtitle, rows), `card_2_*`, blocks: `benefit_cell` (number, title, description), `cta_text`, `cta_url` | Sock math pricing ($336 vs $74), comparison rows, 6-cell benefit grid, CTA |
| `sections/testimonial.html` | N/A (homepage reviews) | `sections/testimonials.liquid` | `eyebrow`, `heading`, blocks: `review` (stars, quote, author_name, author_title, image) | Customer quotes, names, titles, photos |
| `sections/founder-letter.html` / `founder2.html` | N/A (homepage founder) | `sections/founder-letter.liquid` | `eyebrow`, `quote`, `body`, `signature_name`, `signature_title`, `image`, `bg_color` | Founder quote, body text, signature, photo |
| `sections/assoc.html` | N/A (association band) | `sections/association-band.liquid` | `statement`, `fine_print`, blocks: `logo` (name, image_url) | "Free People favorite. Coperni chosen." copy, partner names |
| `Section-26-NotesFromStudio.html` + Section 26 | **Refactor** (current) — "great for blog, orange?" | `sections/blog-cards.liquid` | `blog` (blog picker), `heading`, `eyebrow`, `max_articles`, `show_meta` | Blog handle, "Notes from the Studio" heading |
| `sections/closing-statement.html` | N/A | `sections/closing-cta.liquid` | `eyebrow`, `heading`, `subtitle`, `cta_text`, `cta_url`, `bg_color` | Closing CTA headline and copy |
| v24 social feed embed | Section 29: **Undecided** — "can we code Juicer to make it look how we want?" | `sections/social-feed.liquid` | `juicer_feed_id`, `heading`, `eyebrow`, `max_posts` | Juicer feed ID |
| `Section-27-FAQ.html` + Section 27 | **Refactor** (current) — "excellent, for PDP bottom for SEO — no orange" | `sections/faq.liquid` | `eyebrow`, `heading`, blocks: `faq_item` (question, answer) | FAQ questions and answers (6 items) |
| `Section-28-Newsletter.html` + Section 28 | **Refactor** (current) — "very good but black and orange NO" | `sections/newsletter.liquid` | `eyebrow`, `heading`, `description`, `cta_text`, `fine_print`, `discount_code` | Newsletter CTA copy, fine print |

### PDP Prototypes

| Source HTML | CEO Decision | Target Shopify File(s) | Required Settings Schema | Content to Migrate |
|---|---|---|---|---|
| `Barreletics-PDP-v36-Jul2026.html` | N/A (canonical PDP source) | `templates/product.json` + 12 sections | All PDP section schemas | Full PDP content, structured data |
| `barreletics-design-review/Barreletics Design Review/Barreletics PDP - Matured.html` | N/A (matured design direction) | Same — design reference | Matured styling tokens | Matured PDP styling cues |
| PDP v36 hero section | N/A | `sections/pdp-hero.liquid` | Product object auto-binds; settings: `gallery_layout`, `show_trust_row`, `trust_items` (blocks) | Gallery images, trust row copy |
| PDP v36 benefits | N/A | `sections/pdp-benefits.liquid` | `heading`, blocks: `benefit` (icon, title, description) | 6 benefit items (Reformer-ready, No twist, etc.) |
| PDP v36 variants + `sections/variants.html` + Sections 12, 14, 15 | **Refactor** — "V28, variant grid and color sections are great, merge all variant sections, mostly aesthetic" | `sections/pdp-variants.liquid` | `heading`, `collection` (for cross-sell), `tab_1_label`, `tab_2_label`, `show_size_filter` | Closed/Open sole tabs, color swatches, size pills |
| PDP v36 reviews | Section 06: **Refactor** — "update in JudgeMe, display images" | `sections/pdp-reviews.liquid` | `heading`, `reviews_per_page`, `show_images`, `judgeme_widget` | JudgeMe integration code |
| PDP v36 comparison | N/A | `sections/pdp-comparison.liquid` | `heading`, `columns` (blocks with icon, title, stat) | Comparison stats (vs grip socks) |
| PDP v36 motion grid | Section 23: **Refactor** — "good but not sure if it nails it, think about mobile" | `sections/pdp-motion.liquid` | blocks: `media_cell` (video_url, image, caption) | Motion/workout videos |
| PDP v36 justifier quotes | N/A | `sections/pdp-justifier.liquid` | blocks: `quote` (text, author, role, image) | Justifier quote copy |
| PDP v36 JSON-LD | N/A | `snippets/product-schema.liquid` | Auto from product object | Structured data template |

### Collection Prototypes

| Source HTML | CEO Decision | Target Shopify File(s) | Required Settings Schema | Content to Migrate |
|---|---|---|---|---|
| `barreletics-design-review/Barreletics Design Review/Barreletics Collection - Matured.html` | N/A (canonical) | `templates/collection.json` → `sections/collection-hero.liquid`, `sections/collection-grid.liquid` | Hero: `show_description`, `show_image`; Grid: `products_per_page`, `filter_facets`, `sort_options`, `columns_desktop`, `columns_mobile` | Collection titles, descriptions, filter configuration |

### Blog & Article Prototypes

| Source HTML | CEO Decision | Target Shopify File(s) | Required Settings Schema | Content to Migrate |
|---|---|---|---|---|
| `barreletics-design-review/Barreletics Design Review/Barreletics Blog.html` | N/A (canonical) | `templates/blog.json` → `sections/blog-hero.liquid`, `sections/blog-grid.liquid` | Hero: `heading`; Grid: `articles_per_page`, `show_featured`, `columns` | Blog title, layout config |
| `barreletics-design-review/Barreletics Design Review/Barreletics Article*.html` (6 files) | N/A (canonical) | `templates/article.json` → `sections/article-hero.liquid`, `sections/article-body.liquid`, `sections/article-related.liquid` | Hero: `show_author`, `show_date`, `show_tags`; Body: `content_width` (720px); Related: `max_articles` | Article template structure, 720px content column |

### Design System / Foundation Prototypes

| Source HTML | Target Shopify File(s) | Content to Migrate |
|---|---|---|
| `Barreletics-DesignSystem-v1_0-Jul2026.html` | `assets/barreletics-tokens.css`, `snippets/css-variables.liquid` | All `:root` token values (colors, typography, spacing, buttons) |
| `barreletics-design-review/Barreletics Design Review/audit-styles.css` | `assets/barreletics-tokens.css` | Primary token + component definitions |
| `barreletics-design-review/Barreletics Design Review/maturation-styles.css` | `assets/barreletics-base.css` | Matured-direction base styles |
| `barreletics-design-review/Barreletics Design Review/pdp-styles.css` | Section-scoped `<style>` in PDP sections | PDP-specific component styles |
| `barreletics-design-review/Barreletics Design Review/ticker.js` | `assets/ticker.js` | Ticker rotation logic (crossfade, 5s, pause on hover) |
| v24 inline JS (lines 4855–4941) | `assets/rotating-text.js` | Eyebrow + slogan rotation |
| PDP v36 inline JS | `assets/pdp-interactions.js` | Gallery, swatch, size, variant tab, FAQ accordion JS |

### Sections Requiring CEO Clarification Before Build

| Section # | Name | CEO Status | Blocker |
|---|---|---|---|
| 04 | Coperni + Free People | **Undecided** — no notes | Needs decision: keep, refactor, or cut |
| 15 | v28 Original Variant Grid | **Undecided** — "keep and merge with other variant sections" | Needs final merge spec with Sections 12/14 |
| 24 | Content 2 | **Undecided** — "do we have more than one option and ability to add picture?" | Needs decision on whether this is a 50/50 variant |
| 25 | Coperni Collab | **Undecided** — "this is not good enough, do we use our existing?" | Needs redesign or use current live section |
| 29 | Final CTA / Social | **Undecided** — "can we code Juicer to make it look how we want?" | Needs Juicer customization feasibility check |

---

## REQUIRED TEMPLATES

Every Shopify JSON template required for the theme:

| Template | File | Sections Referenced | Notes |
|---|---|---|---|
| **Homepage** | `templates/index.json` | ~20 sections (hero through footer) | Most complex template; all homepage sections |
| **Product (PDP)** | `templates/product.json` | ~12 sections (pdp-hero through footer) | Highest-revenue page; build priority per docs/03 |
| **Collection** | `templates/collection.json` | 5 sections (hero, grid, newsletter, footer) | Reuses product-card and filter snippets |
| **Blog Index** | `templates/blog.json` | 5 sections (hero, grid, newsletter, footer) | Featured article + card grid |
| **Article** | `templates/article.json` | 6 sections (hero, body, related, newsletter, footer) | Single template handles all 6 article variants via content |
| **Page** | `templates/page.json` | Generic: header, page-content, newsletter, footer | For static pages (About, Contact, Sizing Guide, etc.) |
| **Cart** | `templates/cart.json` | Cart contents, cross-sell rail, trust badges | AJAX cart preferred per PDP v36 architecture |
| **404** | `templates/404.json` | Error message, search, product suggestions | Branded 404 with warm palette |
| **Search** | `templates/search.json` | Search results grid, filters | Uses product-card snippet |
| **Customers** | `templates/customers/*.json` | Login, register, account, order, reset password | Standard Shopify customer templates |

---

## REQUIRED SECTIONS

Every Shopify section needed, with source prototype, settings schema, and block types.

### Global Sections (every page)

| Section | File | Source Prototype | Settings Schema | Block Types |
|---|---|---|---|---|
| **Ticker Bar** | `sections/ticker-bar.liquid` | v24 ticker + `ticker.js` | `speed` (range, default 5s), `bg_color`, `text_color` | `slide` (text, link_url) |
| **Header** | `sections/header.liquid` | v24 header | `logo` (image), `logo_width`, `sticky` (checkbox), `menu` (link_list) | `nav_link` (label, url, has_dropdown) |
| **Footer** | `sections/footer.liquid` | v24 footer (5-col grid) | `bg_color`, `text_color`, `show_newsletter`, `show_social`, `copyright` | `column` (title, menu), `social_link` (platform, url) |

### Homepage Sections

| Section | File | Source Prototype | Settings Schema | Block Types |
|---|---|---|---|---|
| **Hero** | `sections/hero.liquid` | `sections/hero.html`, `01-section.html` | `heading`, `subheading`, `bg_image`, `bg_video`, `primary_cta_text`, `primary_cta_url`, `secondary_cta_text`, `secondary_cta_url`, `overlay_opacity` | `eyebrow_message` (text) |
| **Trusted By** | `sections/trusted-by.liquid` | `03-section.html` | `heading`, `subheading`, `image`, `show_stars`, `star_count` | `stat` (number, label) |
| **Problem Statement** | `sections/problem-statement.liquid` | `sections/problem.html`, `09-section.html` | `eyebrow`, `heading`, `body`, `image` | `old_solution` (text, strikethrough: true) |
| **Media + Text Split** | `sections/media-text-split.liquid` | `split-section*.html`, Sections 17/20/21 | `heading`, `body`, `media_type` (image/video), `media_url`, `layout` (media-left/media-right), `show_trusted_line`, `bg_color`, `text_color`, `cta_text`, `cta_url` | None (single block) |
| **Disciplines** | `sections/disciplines.liquid` | `sections/disciplines.html`, `08-section.html` | `eyebrow`, `heading`, `columns` (2/3/4) | `discipline_card` (name, description, image, link_url) |
| **Manifesto** | `sections/manifesto.liquid` | `sections/manifesto.html` | `eyebrow`, `subtitle`, `rotation_speed` (range), `bg_color` | `statement` (text) |
| **Credibility Band** | `sections/credibility-band.liquid` | `sections/credibility.html`, `06-section.html` | `eyebrow`, `heading`, `subtext`, `bg_color` | `credibility_cell` (image, caption, stat_number, stat_label), `logo` (name, image) |
| **Product Range** | `sections/product-range.liquid` | `sections/range.html` | `collection` (collection picker), `eyebrow`, `heading`, `max_products`, `columns_desktop` (3/4), `show_quick_add` | None (renders via product-card snippet) |
| **Value Comparison** | `sections/value-comparison.liquid` | `sections/sock-math.html` | `eyebrow`, `heading`, `subtext`, `competitor_label`, `competitor_price`, `competitor_subtitle`, `brand_label`, `brand_price`, `brand_subtitle`, `cta_text`, `cta_url`, `bg_color` | `comparison_row` (label, competitor_value, brand_value), `benefit_cell` (number, title, description) |
| **Testimonials** | `sections/testimonials.liquid` | `sections/testimonial.html` | `eyebrow`, `heading`, `layout` (carousel/grid) | `review` (stars, quote, author_name, author_title, image) |
| **Founder Letter** | `sections/founder-letter.liquid` | `sections/founder-letter.html` | `eyebrow`, `quote`, `body`, `signature_name`, `signature_title`, `image`, `bg_color` | None |
| **Association Band** | `sections/association-band.liquid` | `sections/assoc.html` | `statement`, `fine_print`, `bg_color` | `partner_logo` (name, image) |
| **Blog Cards** | `sections/blog-cards.liquid` | `Section-26-NotesFromStudio.html` | `blog` (blog picker), `eyebrow`, `heading`, `max_articles` (default 3), `show_meta` | None (renders via article-card snippet) |
| **FAQ** | `sections/faq.liquid` | `Section-27-FAQ.html` | `eyebrow`, `heading`, `one_open_at_a_time` (checkbox) | `faq_item` (question, answer) |
| **Newsletter** | `sections/newsletter.liquid` | `Section-28-Newsletter.html` | `eyebrow`, `heading`, `description`, `cta_text`, `fine_print`, `discount_code`, `integration` (shopify/klaviyo) | None |
| **Closing CTA** | `sections/closing-cta.liquid` | `sections/closing-statement.html` | `eyebrow`, `heading`, `subtitle`, `cta_text`, `cta_url`, `bg_color` | None |
| **Social Feed** | `sections/social-feed.liquid` | v24 Juicer embed | `juicer_feed_id`, `eyebrow`, `heading`, `max_posts`, `custom_css` | None |
| **Promo Tiles** | `sections/promo-tiles.liquid` | Section 18 | `heading`, `eyebrow` | `tile` (image, label, copy, cta_text, cta_url) |

### PDP Sections

| Section | File | Source Prototype | Settings Schema | Block Types |
|---|---|---|---|---|
| **PDP Hero** | `sections/pdp-hero.liquid` | PDP v36 hero | `gallery_layout` (stacked/thumbnails), `show_trust_row`, `show_quantity`, `show_dynamic_checkout` | `trust_item` (icon, text) |
| **PDP Benefits** | `sections/pdp-benefits.liquid` | PDP v36 benefits grid | `heading`, `columns` (3/4/6) | `benefit` (icon, title, description) |
| **PDP Variants** | `sections/pdp-variants.liquid` | PDP v36 + `variants.html` + Sections 12/14/15 | `heading`, `collection`, `tab_1_label` (default "Closed Sole"), `tab_2_label` (default "Open Sole"), `show_size_filter` | None (product data driven) |
| **PDP Reviews** | `sections/pdp-reviews.liquid` | PDP v36 reviews | `heading`, `reviews_per_page` (default 6), `show_images`, `show_load_more` | None (JudgeMe driven) |
| **PDP Comparison** | `sections/pdp-comparison.liquid` | PDP v36 comparison | `heading`, `subheading` | `column` (icon, title, stats), `row` (label, values) |
| **PDP Motion** | `sections/pdp-motion.liquid` | PDP v36 motion grid | `heading` | `media_cell` (type: image/video, url, caption) |
| **PDP Justifier** | `sections/pdp-justifier.liquid` | PDP v36 justifier | `heading` | `quote` (text, author_name, author_role, image) |

### Collection Sections

| Section | File | Source Prototype | Settings Schema | Block Types |
|---|---|---|---|---|
| **Collection Hero** | `sections/collection-hero.liquid` | Collection - Matured.html | `show_description`, `show_image`, `bg_color` | None |
| **Collection Grid** | `sections/collection-grid.liquid` | Collection - Matured.html | `products_per_page` (default 12), `columns_desktop` (3/4), `columns_mobile` (1/2), `enable_filtering`, `enable_sorting`, `filter_type` (inline/drawer) | `filter_facet` (label, type) |

### Blog & Article Sections

| Section | File | Source Prototype | Settings Schema | Block Types |
|---|---|---|---|---|
| **Blog Hero** | `sections/blog-hero.liquid` | Barreletics Blog.html | `heading`, `show_rss` | None |
| **Blog Grid** | `sections/blog-grid.liquid` | Barreletics Blog.html | `articles_per_page`, `columns` (2/3), `show_featured` | None |
| **Article Hero** | `sections/article-hero.liquid` | Barreletics Article*.html | `show_author`, `show_date`, `show_tags`, `show_featured_image` | None |
| **Article Body** | `sections/article-body.liquid` | Barreletics Article*.html | `content_width` (default 720px), `show_share` | None |
| **Article Related** | `sections/article-related.liquid` | Barreletics Article*.html | `heading` (default "More from the Journal"), `max_articles` (default 3) | None |

---

## REQUIRED SNIPPETS

Reusable Liquid snippets extracted from cross-cutting patterns.

| Snippet | File | Used In | Props / Render Args |
|---|---|---|---|
| **CSS Variables** | `snippets/css-variables.liquid` | `layout/theme.liquid` | Outputs all `:root` custom properties from theme settings |
| **Product Card** | `snippets/product-card.liquid` | product-range, pdp-variants, collection-grid | `product`, `show_badge`, `show_size`, `show_price`, `show_quick_add`, `columns` |
| **Section Header** | `snippets/section-header.liquid` | Every content section | `eyebrow`, `heading`, `description`, `alignment` (center/left) |
| **Review Card** | `snippets/review-card.liquid` | testimonials, pdp-reviews | `stars`, `quote`, `author_name`, `author_title`, `image` |
| **Color Swatch** | `snippets/color-swatch.liquid` | pdp-hero, collection-grid | `color_hex`, `color_name`, `variant_image_url`, `selected`, `show_le_badge` |
| **FAQ Item** | `snippets/faq-item.liquid` | faq section | `question`, `answer`, `open_by_default` |
| **Newsletter Form** | `snippets/newsletter-form.liquid` | newsletter section | `heading`, `description`, `cta_text`, `fine_print`, `integration` |
| **Article Card** | `snippets/article-card.liquid` | blog-cards, blog-grid, article-related | `article`, `show_meta`, `show_image`, `show_excerpt` |
| **Badge** | `snippets/badge.liquid` | product-card, pdp-hero, collection-grid | `type` (le/sole/size/new/soldout), `text` |
| **Media Split Block** | `snippets/media-split-block.liquid` | media-text-split section | `media_type`, `media_url`, `heading`, `body`, `cta`, `layout` |
| **Trust Badges** | `snippets/trust-badges.liquid` | pdp-hero, cart | `badges` array (icon, text): ships, returns, warranty, allergen-free |
| **Product Schema** | `snippets/product-schema.liquid` | pdp-hero | Auto from `product` object — outputs JSON-LD Product structured data |
| **Cart Drawer** | `snippets/cart-drawer.liquid` | layout/theme.liquid | `cart` object, line items, totals, cross-sell |

---

## REQUIRED METAFIELDS

### Product Metafields

| Namespace.Key | Type | Purpose | Used In |
|---|---|---|---|
| `custom.sole_type` | `single_line_text_field` | "Closed Sole" or "Open Sole" — drives variant grid tabs | pdp-variants, collection-grid filters, product-card badge |
| `custom.grip_technology` | `rich_text_field` | Grip tech description per product | pdp-hero buy box, PDP benefits |
| `custom.care_instructions` | `rich_text_field` | Care/wash instructions | PDP accordion |
| `custom.materials` | `rich_text_field` | Materials/specs | PDP accordion |
| `reviews.rating` | `rating` | JudgeMe aggregate rating (auto-synced) | product-card, pdp-hero, structured data |
| `reviews.rating_count` | `number_integer` | JudgeMe review count (auto-synced) | product-card, pdp-hero, structured data |
| `custom.grip_lifespan` | `single_line_text_field` | e.g. "4+ years proven" — used in sock math comparison | value-comparison, pdp-comparison |
| `custom.is_limited_edition` | `boolean` | Flags LE products for badge display | product-card badge, collection-grid |
| `custom.color_hex` | `single_line_text_field` | Hex color for swatch rendering (e.g. "#1a1a1a") | color-swatch snippet |
| `custom.size_guide_url` | `url` | Link to size guide page | pdp-hero size picker |

### Collection Metafields

| Namespace.Key | Type | Purpose | Used In |
|---|---|---|---|
| `custom.hero_image` | `file_reference` | Collection banner image | collection-hero |
| `custom.hero_description` | `rich_text_field` | Extended collection description | collection-hero |
| `custom.sole_type_filter` | `single_line_text_field` | Default sole type for this collection | collection-grid filter presets |

### Page Metafields

| Namespace.Key | Type | Purpose | Used In |
|---|---|---|---|
| `custom.page_layout` | `single_line_text_field` | Layout variant selector (e.g. "full-width", "narrow") | page template |

---

## REQUIRED PRODUCT DATA

What must exist in Shopify Admin before theme launch:

### Products

| Data Point | Required State | Source |
|---|---|---|
| **Product titles** | All products titled consistently (e.g. "Barreletics Closed Sole — Black") | Current Shopify products |
| **Descriptions** | Rich text descriptions with grip technology, use case, care info | PDP v36 content + docs/09 product knowledge |
| **Variants** | Every product must have: Sole Type (Closed/Open) × Color × Size (M/L minimum) | Current variant matrix |
| **Variant images** | Every color variant must have its own set of product images (front, back, sole, on-foot, detail) | Current CDN images + new photography |
| **Product images** | Min 5 images per product: front, back, sole, on-foot lifestyle, detail/texture | CDN assets listed in Image Asset Registry |
| **Prices** | All prices set (currently $74 base) | Current Shopify pricing |
| **Compare-at prices** | Set if running "was/now" pricing; sale price displays as ink-bold (not red per design system) | Brand team decision |
| **Metafields** | All custom metafields populated (sole_type, grip_technology, care_instructions, materials, color_hex, is_limited_edition) | See Required Metafields above |
| **Tags** | Discipline tags (barre, reformer, pilates, megaformer, yoga), sole type tags, color tags | For collection filtering |
| **SEO titles & descriptions** | Product-level SEO metadata | SEO team / copy guide |
| **Structured data** | JSON-LD Product schema auto-generated from product data via `product-schema.liquid` | Automated from above data |

### Collections

| Collection | Products | Purpose |
|---|---|---|
| All Grippy Footwear | All shoe products | Main collection page |
| Closed Sole | All closed-sole variants | Filtered view |
| Open Sole | All open-sole variants | Filtered view |
| Limited Edition | LE products (Coperni, etc.) | LE showcase |
| Best Sellers | Top-selling products | Homepage product range section |

### Blog / Articles

| Blog Handle | Required Articles | Purpose |
|---|---|---|
| `journal` (not "blog") | Founder story, Coperni collaboration, Teacher profile, "Retire your grip socks", Barefoot science, + ongoing editorial | Blog index, blog-cards homepage section, article-related |

---

## REQUIRED APP INTEGRATIONS

| App | Purpose | Integration Points | Configuration Needed |
|---|---|---|---|
| **JudgeMe** | Product reviews and ratings | `sections/pdp-reviews.liquid`, `sections/testimonials.liquid`, `snippets/review-card.liquid`, product metafields (rating, rating_count) | Widget styling to match design system (no orange, warm/neutral palette); image reviews enabled per CEO notes; aggregate rating sync to product metafields |
| **Juicer** | Social media UGC feed | `sections/social-feed.liquid` — embeds `assets.juicer.io/embed.js` + `embed.css` | Feed ID configuration; custom CSS overlay to match brand palette (CEO: "can we code Juicer to make it look how we want?"); max posts setting |
| **Shop Pay** | Installment payments | PDP buy box (`sections/pdp-hero.liquid`), cart | Dynamic checkout button; installment messaging below price ("or 4 payments of $18.50 with Shop Pay") |
| **Klaviyo** | Email marketing / newsletter | `sections/newsletter.liquid`, `snippets/newsletter-form.liquid` | Form integration, list assignment, SAVE15 welcome discount flow |
| **Google Fonts** | Typography | `layout/theme.liquid` `<head>` | Roboto 300,400,500,600,700 — preconnect + display=swap |
| **Shopify Analytics** | Conversion tracking | `layout/theme.liquid` | Standard Shopify analytics + enhanced ecommerce |
| **GA4** | Analytics | `layout/theme.liquid` or Google Tag Manager | Property ID: 300437005 (per workspace rules) |

---

## DEPENDENCIES

What must be completed or confirmed before Shopify theme build begins:

### Design Decisions (Blocked)

1. **Sections 04, 15, 24, 25, 29** — CEO must finalize keep/refactor/cut decisions
2. **Variant grid merge spec** — How Sections 12, 14, 15 combine into one pdp-variants section
3. **Coperni section direction** — Section 25: redesign or reuse existing live section?
4. **Juicer customization scope** — Section 29: what CSS overrides are feasible with Juicer embed?
5. **Eyebrow letter-spacing** — Resolve 0.08em (design handoff) vs 0.14em (Research Bible) conflict

### Content / Assets

6. **Final photography** — Brand team must provide art-directed product + lifestyle photos (current CDN images are placeholder per docs/03)
7. **Product metafield data** — sole_type, grip_technology, care_instructions, materials, color_hex for every product
8. **Blog content** — All 6+ articles written and ready for Shopify blog creation (use "Journal" not "Blog")
9. **FAQ content** — Finalized Q&A pairs for homepage + PDP FAQ sections
10. **Legal copy** — Privacy policy, Terms of Service, Accessibility statement

### Technical

11. **Online Store 2.0 confirmation** — Docs/03 asks: "Is the theme currently on OS 2.0?" — must confirm yes before build
12. **$150 free shipping threshold** — Confirmed current (per docs/03 notes); ensure announcement ticker and trust badges reflect this
13. **Shopify product variant structure** — Confirm SKU availability for Closed Sole / Open Sole / Limited Edition taxonomy
14. **JudgeMe review data** — Existing reviews must be preserved during theme switch
15. **Domain and DNS** — barreletics.com DNS stable for theme publish

---

## RISKS

| Risk | Severity | Mitigation |
|---|---|---|
| **5 undecided sections** (04, 15, 24, 25, 29) block full homepage build | **High** | Build all decided sections first (Phases 0–4); hold Phase 5 for clarification. Sections are modular — undecided sections can be added post-launch. |
| **Monolith decomposition complexity** — v24 homepage is a single 152KB HTML file with ~4800 lines of embedded CSS that must be split into ~20 independent Liquid sections | **High** | Strict extraction order (tokens → globals → snippets → sections). Test each section in isolation via theme customizer. |
| **PDP variant switching** — complex JS for sole-type tabs, color swatches, size pills, cart AJAX must work with Shopify's variant/option system | **High** | Build variant logic against Shopify's native variant API. Avoid custom variant hacks. Test with real product data early. |
| **Color compliance** — CEO mandate "NO orange + black" but multiple prototype sections still use `#f97250` accent and `#050505` backgrounds together | **Medium** | Run color audit in Phase 5; replace all orange CTAs/headings with matured palette. Coral restricted to cart badge only per design system. |
| **JudgeMe styling** — Reviews app injects its own CSS/HTML that may conflict with design system | **Medium** | Use JudgeMe's custom CSS override feature. Test early with real reviews. CEO wants image reviews displayed. |
| **Juicer customization** — CEO asks "can we code Juicer to make it look how we want?" — limited CSS control over third-party embed | **Medium** | Evaluate Juicer's custom CSS options and API. May need CSS overrides or alternative social feed approach. |
| **Mobile experience** — CEO flagged concerns about Section 23 (video/content) on mobile; 50/50 splits must stack properly | **Medium** | All sections must be tested at 375px minimum viewport. Touch targets 44px per docs/04. Breakpoint at 768px. |
| **Photography placeholder risk** — Docs/03 states "photography is placeholder" — final imagery may require layout adjustments | **Medium** | Build with flexible image containers (object-fit: cover, aspect-ratio settings). Final photography swap should be non-breaking. |
| **Performance** — 20+ homepage sections, Google Fonts, Juicer embed, JudgeMe widget, product images = heavy page | **Low** | Lazy-load below-fold images, defer non-critical JS, use Shopify's image CDN with responsive srcset, preconnect Google Fonts. |
| **Theme publish disruption** — Switching from current live theme to new build could cause downtime or broken links | **Low** | Build on unpublished theme. Full QA before publish. Maintain URL parity for SEO. |

---

## BUILD SEQUENCE

Ordered steps from start to launch, incorporating implementation order from docs/03 (tokens first → PDP highest priority → Home → Collection → Articles/Blog).

### Pre-Build (Week 0)
1. Confirm Online Store 2.0 status
2. Resolve eyebrow letter-spacing conflict (0.08em vs 0.14em)
3. Collect all product metafield data
4. Set up development theme (unpublished)

### Phase 0: Foundation (Week 1) — 24h
5. Extract design tokens → `assets/barreletics-tokens.css`
6. Build `snippets/css-variables.liquid` (outputs `:root` from theme settings)
7. Build base stylesheet → `assets/barreletics-base.css`
8. Build component stylesheet → `assets/barreletics-components.css`
9. Build all snippets: product-card, section-header, badge, review-card, color-swatch, trust-badges, article-card, faq-item, newsletter-form, media-split-block, product-schema
10. Create `layout/theme.liquid` with Google Fonts, CSS includes, JS defers

### Phase 1: Global Components (Week 1–2) — 22h
11. Build `sections/ticker-bar.liquid` + `assets/ticker.js`
12. Build `sections/header.liquid` (sticky, centered logo, cart badge)
13. Build `sections/footer.liquid` (5-col grid, dark bg)
14. Build `sections/newsletter.liquid` (reusable home + PDP)
15. Build `sections/faq.liquid` (reusable home + PDP)

### Phase 2: PDP (Week 2–3) — 58h ← **Build priority per docs/03: highest-revenue page**
16. Build `sections/pdp-hero.liquid` (gallery + buy panel, variant picker, trust row)
17. Build `assets/pdp-interactions.js` (gallery, swatches, size pills, tabs)
18. Build `sections/pdp-benefits.liquid`
19. Build `sections/pdp-variants.liquid` (sole-type tabs, cross-sell grid)
20. Build `sections/pdp-reviews.liquid` (JudgeMe integration)
21. Build `sections/pdp-comparison.liquid`
22. Build `sections/pdp-motion.liquid`
23. Build `sections/pdp-justifier.liquid`
24. Build `assets/cart.js` (AJAX cart + cart drawer)
25. Build `snippets/product-schema.liquid` (JSON-LD)
26. Create `templates/product.json`
27. **PDP QA checkpoint** — test with real products

### Phase 3: Homepage (Week 3–4) — 57h
28. Build `sections/hero.liquid` + `assets/rotating-text.js`
29. Build `sections/trusted-by.liquid`
30. Build `sections/problem-statement.liquid`
31. Build `sections/media-text-split.liquid` (configurable for all 50/50 instances)
32. Build `sections/disciplines.liquid`
33. Build `sections/manifesto.liquid`
34. Build `sections/credibility-band.liquid`
35. Build `sections/product-range.liquid`
36. Build `sections/value-comparison.liquid` (sock math)
37. Build `sections/testimonials.liquid`
38. Build `sections/founder-letter.liquid`
39. Build `sections/association-band.liquid`
40. Build `sections/blog-cards.liquid`
41. Build `sections/closing-cta.liquid`
42. Build `sections/social-feed.liquid` (Juicer embed)
43. Create `templates/index.json`
44. **Homepage QA checkpoint**

### Phase 4: Collection + Blog + Article (Week 4–5) — 33h
45. Build `sections/collection-hero.liquid`
46. Build `sections/collection-grid.liquid` (filters, sorting)
47. Build `sections/blog-hero.liquid` + `sections/blog-grid.liquid`
48. Build `sections/article-hero.liquid` + `sections/article-body.liquid` + `sections/article-related.liquid`
49. Create `templates/collection.json`, `templates/blog.json`, `templates/article.json`
50. Create `templates/page.json`, `templates/404.json`, `templates/cart.json`, `templates/search.json`
51. **Collection/Blog QA checkpoint**

### Phase 5: Refactors + Polish (Week 5–6) — 52h
52. Color compliance audit — remove all orange/black violations across all sections
53. Refactor batch 1 (Sections 06, 07, 08, 10) — high priority
54. Refactor batch 2 (Sections 12, 13, 14, 18)
55. Refactor batch 3 (Sections 19, 20, 21, 23)
56. Await CEO decisions on Sections 04, 15, 24, 25, 29 — build if decided

### Phase 6: Integration + QA (Week 6) — 16h
57. JudgeMe styling and integration QA
58. Juicer feed styling
59. Klaviyo newsletter form integration
60. Shop Pay installment messaging
61. GA4 + conversion tracking verification
62. Full cross-browser + mobile QA
63. Performance audit (Lighthouse, Core Web Vitals)
64. Accessibility audit (WAVE, axe)

### Phase 7: Launch
65. Final stakeholder review on unpublished theme
66. Content freeze — no more edits
67. Theme publish
68. Post-launch monitoring (GA4, Shopify analytics, error tracking)

---

## QA CHECKLIST

### Desktop QA (≥ 768px)

- [ ] All sections render at 1200–1320px max content width
- [ ] 32px gutters maintained on all content sections
- [ ] 80px vertical section padding on all sections
- [ ] Multi-column grids display correctly (2-col splits, 3-col product grids, 4-col footers)
- [ ] Hover states functional: product card 1.02x scale, caption underline draw, button opacity
- [ ] Sticky header adds hairline on scroll > 8px
- [ ] Cart badge dot visible only with items > 0
- [ ] Ticker rotates (5s interval, crossfade 320ms, pause on hover)
- [ ] Hero eyebrow rotation (3.5s cycle, 5 messages)
- [ ] PDP gallery: thumbnail click swaps main image, keyboard ←/→ navigation
- [ ] PDP size picker: aria-pressed toggle, out-of-stock strikethrough
- [ ] PDP variant tabs: Closed Sole / Open Sole toggle works
- [ ] FAQ accordion: one-open-at-a-time, 200ms height transition
- [ ] Collection filters: inline chips, URL sync via query params
- [ ] Value comparison (sock math): dark bg, correct pricing ($336 vs $74)
- [ ] No orange + black combinations anywhere (coral cart badge only)
- [ ] All buttons square (border-radius: 0px), no shadows, no gradients
- [ ] Roboto font loaded correctly (weights 300–700)
- [ ] All images load from Shopify CDN (no broken images)
- [ ] AJAX cart: add-to-cart works without page reload
- [ ] JSON-LD structured data validates (Google Rich Results Test)
- [ ] All internal links resolve (no 404s)
- [ ] Newsletter form submits successfully (Klaviyo/Shopify)

### Mobile QA (< 768px)

- [ ] All 2-column layouts stack to single column
- [ ] Full-width images and cards at mobile viewport
- [ ] Hamburger navigation replaces horizontal nav
- [ ] Hamburger opens drawer/modal, closes on selection or escape
- [ ] Sticky Add to Cart button appears on PDP (fixed bottom)
- [ ] Touch targets minimum 44×44px on all interactive elements
- [ ] Font sizes readable at 375px viewport width (clamp() floors)
- [ ] Section padding reduces to 40–48px vertical
- [ ] Gutters reduce to 16px
- [ ] PDP gallery: pinch/double-tap to zoom functional
- [ ] Product cards display correctly at 1–2 columns
- [ ] Collection filter: drawer or inline scroll (not sidebar)
- [ ] Footer columns stack single column
- [ ] Ticker readable at mobile width
- [ ] No horizontal scroll on any page
- [ ] Cart drawer functional on mobile
- [ ] Newsletter form usable with mobile keyboard
- [ ] Videos play inline (no fullscreen takeover unless tapped)

### Accessibility Requirements

- [ ] `@media (prefers-reduced-motion: no-preference)` gates ALL animations
- [ ] Final state of all animations visible without animation
- [ ] All interactive elements keyboard-navigable (tab order logical)
- [ ] Visible focus indicators on all focusable elements
- [ ] `aria-pressed` on all toggle buttons (sole type tabs, size pills, sock⇄skin)
- [ ] `aria-expanded` on all accordion/dropdown elements (FAQ, mobile nav)
- [ ] All `<img>` tags have descriptive `alt` text
- [ ] Color is not the sole carrier of information (stars have text equivalent, badges have text)
- [ ] All form `<input>` elements have associated `<label>` elements
- [ ] Minimum 4.5:1 contrast ratio on all text (WCAG AA)
- [ ] Touch targets 44×44px minimum (per docs/04)
- [ ] Page landmarks (`<main>`, `<nav>`, `<header>`, `<footer>`) present
- [ ] Skip-to-content link as first focusable element
- [ ] Screen reader announces cart item count changes
- [ ] PDP size selector communicates out-of-stock state to assistive technology

### Performance

- [ ] Lighthouse Performance score ≥ 80 on mobile
- [ ] Largest Contentful Paint < 2.5s
- [ ] Cumulative Layout Shift < 0.1
- [ ] First Input Delay < 100ms
- [ ] Below-fold images lazy-loaded
- [ ] Google Fonts preconnected and display=swap
- [ ] Non-critical JS deferred
- [ ] Juicer embed deferred / lazy-loaded
- [ ] Responsive images with srcset and sizes attributes

---

## CONTENT MIGRATION REQUIREMENTS

Content that must transfer from the current live site (or be created) for the new theme:

### From Current Shopify Store

| Content Type | Migration Method | Notes |
|---|---|---|
| **Products** (titles, descriptions, images, variants, pricing) | Already in Shopify — theme reads directly | Add missing metafields (sole_type, grip_technology, etc.) |
| **Collections** | Already in Shopify — update descriptions/images if needed | May need new collections: "Closed Sole", "Open Sole", "Limited Edition" |
| **Customer accounts** | No migration needed — Shopify native | Template styling only |
| **Orders / order history** | No migration needed — Shopify native | Template styling only |
| **Navigation menus** | Update via Shopify Admin → Navigation | New nav structure: Grippy Footwear, Apparel, Collaborations, Journal, About Us |
| **Pages** (About, Contact, FAQ, Sizing) | Already in Shopify — restyle with new templates | May need content updates to match brand voice |
| **Blog posts** | Rename blog from "Blog" → "Journal" | Create 6 article variants from prototypes if not already published |
| **JudgeMe reviews** | Persists across theme changes | Verify widget styling matches new design |
| **Announcement bar messages** | Re-enter in ticker section settings | 3 slides: SAVE15 promo, Made in USA, Social proof |
| **Footer links & legal pages** | Re-enter in footer section settings | Privacy, Terms, Accessibility, Returns, Sizing Guide |
| **Theme settings** | Fresh configuration in new theme | All section settings, color overrides, logo upload |

### New Content to Create

| Content | Owner | Priority | Used In |
|---|---|---|---|
| **Product metafield data** for every product (sole_type, grip_technology, care_instructions, materials, color_hex) | Brand team + dev | **Critical** — blocks PDP build | pdp-hero, pdp-comparison, collection filters |
| **FAQ Q&A pairs** (6+ items) | Copy team | **High** | faq section (home + PDP) |
| **Founder letter copy** (quote, body, signature) | CEO/founder | **High** | founder-letter section |
| **Manifesto rotating statements** (3–5 statements) | Copy team | **High** | manifesto section |
| **Ticker announcement slides** (3 slides) | Marketing | **High** | ticker-bar section |
| **Journal articles** (6 articles per prototype variants) | Content team | **Medium** | blog-grid, blog-cards, article templates |
| **Collection descriptions** (per collection) | Copy team | **Medium** | collection-hero |
| **Alt text for all images** | Content team | **Medium** | Accessibility compliance |
| **SEO meta titles & descriptions** (per product, collection, page) | SEO team | **Medium** | `<head>` metadata |
| **Final art-directed photography** | Brand team / photographer | **Medium** — current CDN images are placeholder | Hero, splits, product shots, lifestyle |
| **Social links** (Instagram, TikTok, etc.) | Marketing | **Low** | footer, social-feed |
| **Size guide content** | Product team | **Low** | PDP size guide link/modal |
| **404 page copy** | Copy team | **Low** | 404 template |

### URL Parity Requirements

Maintain these URL structures to preserve SEO:
- `/products/*` — product pages (Shopify native, no change)
- `/collections/*` — collection pages (Shopify native, no change)
- `/blogs/journal/*` — article pages (rename from "blog" to "journal" if handle changes)
- `/pages/*` — static pages (Shopify native, no change)
- Verify no broken internal links after theme switch
- Set up 301 redirects for any URL structure changes
