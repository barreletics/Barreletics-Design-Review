# Implementation Dependency Graph

**Status:** DRAFT  
**Date:** 2026-07-13  
**Purpose:** Safest implementation order based on component, data, and app dependencies  
**Sources:** docs/03-DESIGN-SYSTEM.md (suggested order lines 335-348), docs/04-COMPONENT-LIBRARY.md, barreletics-decisions-2026-07-09.json

---

## CRITICAL PATH

Each phase depends on the previous. This is the sequence where a delay in any task cascades forward.

```
Phase 1: Foundation (Week 1)
  ├── T01  Design tokens → css-variables.liquid snippet
  ├── T02  Font loading (self-hosted Roboto + JetBrains Mono)
  ├── T03  Base layout (theme.liquid, settings_schema.json)
  ├── T04  Icon set snippet (SVG sprite)
  └── T05  Button system (primary / secondary / tertiary)

Phase 2: Global Chrome (Week 1–2)
  ├── T06  Header section (depends: T01 tokens, T04 icons, T05 buttons)
  │   ├── Desktop nav (centered logo, category links)
  │   ├── Sticky behavior + hairline on scroll
  │   └── Cart badge (coral dot)
  ├── T07  Mobile navigation (depends: T06 header)
  │   └── Hamburger drawer, accordion sub-menus
  ├── T08  Footer section (depends: T01 tokens, T05 buttons)
  │   └── 4-column layout, newsletter form, social links
  ├── T09  Announcement ticker (depends: T01 tokens)
  │   └── 3-slide rotator, ticker.js
  └── T10  Breadcrumb snippet (depends: T01 tokens)

Phase 3: Cart Infrastructure (Week 2)
  ├── T11  Cart drawer (depends: T06 header for trigger, T04 icons)
  │   ├── AJAX cart API wrapper
  │   ├── Line item snippet
  │   ├── Free shipping progress bar ($150 threshold)
  │   └── Focus trap + accessibility
  ├── T12  Cart page fallback (depends: T11 cart drawer — shared snippets)
  └── T13  Price display snippet (depends: T01 tokens)
       └── Sale price = ink-bold (not red), compare-at strikethrough

Phase 4: PDP — Highest Revenue Page (Week 2–3)
  ├── T14  PDP main section (depends: T01, T05, T11 cart, T13 price)
  │   ├── Gallery (thumbnail swap, zoom, keyboard nav) → pdp-gallery.js
  │   ├── Buy box (title, price, variant selector, ATC button)
  │   ├── Size selector snippet (pills, aria-pressed, OOS strikethrough)
  │   ├── Color swatch snippet
  │   └── Trust row snippet (free shipping, returns, warranty)
  ├── T15  PDP accordion section (depends: T01 tokens)
  │   └── Specs, materials, care — one open at a time
  ├── T16  PDP reviews integration (depends: JudgeMe app installed)
  │   └── Summary + 3 quotes + "read all" link
  ├── T17  PDP sock-vs-skin comparison (depends: T01 tokens)
  ├── T18  PDP cross-sell section (depends: T19 product card)
  └── T19  Product card snippet (depends: T01, T05, T13 price, T04 icons)
       └── Image, name, sole type, price, swatch row, hover state

Phase 5: Home Page (Week 3–4)
  ├── T20  Hero section (depends: T01, T05 buttons)
  │   └── Full-bleed split, rotating eyebrow, 2 CTAs
  ├── T21  Pillar strip section (depends: T01, T04 icons)
  ├── T22  50/50 split section (depends: T01, T05 — reusable with settings)
  │   └── 3 instances on Home (chair pose, progress, never loses grip)
  ├── T23  Variant grid section (depends: T19 product card, T11 cart)
  │   └── Closed Sole / Open Sole tabs, color picker, add to cart
  ├── T24  Sock math section (depends: T01 tokens, T05 buttons)
  ├── T25  Disciplines section (depends: T01 tokens)
  ├── T26  Testimonial section (depends: T01 tokens)
  ├── T27  Founder note section (depends: T01 tokens)
  ├── T28  Association strip (depends: T01 tokens)
  ├── T29  Credibility section (depends: T01 tokens)
  ├── T30  Manifesto section (depends: T01 tokens)
  ├── T31  Problem section (depends: T01 tokens)
  ├── T32  Closing statement section (depends: T01 tokens, T05 buttons)
  ├── T33  Newsletter section (depends: T01, T05, Klaviyo)
  ├── T34  Guarantee section (depends: T01, T04 icons)
  └── T35  FAQ section (depends: T01 tokens)

Phase 6: Collection Page (Week 4–5)
  ├── T36  Collection hero section (depends: T01 tokens)
  ├── T37  Sole type chooser (depends: T01, T05 buttons)
  ├── T38  Collection filter row (depends: T01 — collection-filter.js)
  │   └── Inline chips, URL param sync, AJAX re-render
  ├── T39  Collection grid section (depends: T19 product card, T38 filters)
  │   └── 3-up desktop, 2-up tablet, 1-up mobile + editorial breaks
  └── T40  Collection template wiring (depends: T36–T39)

Phase 7: Content Pages (Week 5)
  ├── T41  Article template (depends: T01, T10 breadcrumb)
  │   └── 720px column, JetBrains Mono eyebrows, pull-quotes
  ├── T42  Blog template (depends: T19 product card → reuse as article card)
  │   └── Featured article + 2-up grid
  ├── T43  Article card snippet (depends: T01 tokens)
  └── T44  Social feed section / Juicer (depends: Juicer app)

Phase 8: Utility & Polish (Week 5–6)
  ├── T45  Search (predictive-search.js + results template)
  ├── T46  404 template
  ├── T47  Password template
  ├── T48  Metafield definitions (product, collection, page)
  ├── T49  Structured data (Product, AggregateRating, BreadcrumbList, Organization)
  ├── T50  GA4 enhanced ecommerce events
  ├── T51  Accessibility audit pass (focus traps, ARIA, keyboard nav, skip link)
  ├── T52  Performance audit (Lighthouse, WebPageTest, JS budget)
  └── T53  Strip review chrome (pg-tab-strip, tweaks panels)
```

---

## PARALLEL OPPORTUNITIES

Tasks within the same phase that have **no shared dependencies** and can run simultaneously.

### Phase 1 (all parallel)
- T01 tokens + T02 fonts + T04 icons can be built simultaneously by same or different devs

### Phase 2 (two parallel tracks)
- **Track A:** T06 Header → T07 Mobile nav
- **Track B:** T08 Footer + T09 Ticker (independent of header)
- T10 Breadcrumb: independent, can run with either track

### Phase 3 + Phase 4 (partial overlap)
- T15 Accordion + T17 Sock-vs-skin can start as soon as T01 is done (don't need cart)
- T16 Reviews integration can start once JudgeMe is installed (independent of PDP main)
- T13 Price display can be built during Phase 2 (only needs tokens)

### Phase 5 (high parallelism — most sections only depend on T01)
- **Track A (content sections):** T20 Hero, T21 Pillar, T22 Splits, T24 Sock math, T25 Disciplines, T26 Testimonial, T27 Founder, T30 Manifesto, T31 Problem, T32 Closing — all independent of each other
- **Track B (data-dependent):** T23 Variant grid (needs product card + cart), T33 Newsletter (needs Klaviyo)
- **Track C (simple):** T28 Association, T29 Credibility, T34 Guarantee, T35 FAQ

### Phase 6 + Phase 7 (overlap possible)
- T41 Article + T42 Blog can start during Phase 6 (don't depend on collection)
- T45 Search can start any time after Phase 2

### Phase 8 (all parallel)
- T49 Structured data, T50 GA4 events, T51 a11y audit, T52 performance audit — all independent

---

## RISK POINTS

### Cascading Delay Risks

| Bottleneck | What it blocks | Cascade severity |
|-----------|----------------|-----------------|
| **T01 Design tokens** | Everything. No section can be built without tokens | **Critical** — 1 day delay = 1 day delay on entire project |
| **T06 Header** | Mobile nav (T07), cart drawer trigger (T11), every page layout | **High** — header bugs propagate to every template |
| **T11 Cart drawer** | PDP add-to-cart (T14), variant grid add-to-cart (T23), checkout flow | **High** — broken cart = broken conversion |
| **T19 Product card** | PDP cross-sell (T18), home variant grid (T23), collection grid (T39), blog cards (T42) | **High** — shared component used on 4+ pages |
| **T38 Collection filters** | Collection grid (T39), collection template (T40) | **Medium** — can ship collection without filters initially |

### Integration Failure Risks

| Integration | Risk | Mitigation |
|------------|------|------------|
| **JudgeMe → Reviews** | Widget script conflicts, missing reviews after migration | Test in unpublished theme. Reviews tied to product IDs (unchanged). Have fallback static reviews |
| **Klaviyo → Newsletter** | Form endpoint change, double opt-in misconfiguration | Use Klaviyo's official Shopify integration. Test signup in staging |
| **Juicer → Social feed** | Custom styling limitations, widget not matching design tokens | Scope CSS to Juicer container. Accept some styling compromises or build custom feed |
| **GA4 → Ecommerce events** | Missing events, incorrect product data, broken purchase tracking | Test with GA4 DebugView before launch. Verify every event fires on staging |
| **Variant grid custom code** | Existing heavy custom code (per decision notes) may conflict with new theme structure | Prototype early. Allocate extra time. May need full rebuild vs refactor |

### Decision Blockers

| Decision needed | Blocks | Status |
|----------------|--------|--------|
| Section 04 (Coperni + FP) | Association strip content | **Undecided** |
| Section 15 (v28 original) | Variant grid merge strategy | **Undecided** |
| Section 24 (Content 2) | Additional content section layout | **Undecided** |
| Section 25 (Coperni collab) | Coperni section design — "not good enough, do we use existing?" | **Undecided** |
| Section 29 (Final CTA / Juicer) | Social feed approach — custom Juicer styling vs. matured design | **Undecided** |
| Eyebrow letter-spacing | 0.08em vs 0.14em — affects all eyebrow components | **Needs ADR** |
| Color palette | Warm (#eae5da) vs white (#ffffff) background per decision matrix | **Partially resolved** |

---

## TASK LIST

| ID | Task | Depends On | Blocks | Complexity | Can Parallelize With |
|----|------|-----------|--------|------------|---------------------|
| T01 | Design tokens (CSS variables snippet) | — | All sections | **S** | T02, T04 |
| T02 | Font loading (self-host Roboto + JetBrains Mono) | — | All sections (visual) | **S** | T01, T04 |
| T03 | Base layout (theme.liquid, settings_schema) | T01, T02 | All templates | **M** | — |
| T04 | Icon set snippet (SVG sprite) | — | T06, T08, T11, T14 | **S** | T01, T02 |
| T05 | Button system (3 variants in base.css) | T01 | T06, T08, T14, T20+ | **S** | T04 |
| T06 | Header section (desktop) | T01, T04, T05 | T07, T11 | **M** | T08, T09 |
| T07 | Mobile navigation (hamburger drawer) | T06 | Launch | **M** | T08 |
| T08 | Footer section | T01, T05 | — | **M** | T06, T09 |
| T09 | Announcement ticker | T01 | — | **S** | T06, T08 |
| T10 | Breadcrumb snippet | T01 | T41 (article) | **S** | T06–T09 |
| T11 | Cart drawer (AJAX, focus trap) | T06, T04 | T14, T23 | **L** | T08, T09 |
| T12 | Cart page fallback | T11 | — | **S** | T13 |
| T13 | Price display snippet | T01 | T14, T19, T23 | **S** | T06–T09 |
| T14 | PDP main section (gallery + buy box) | T01, T05, T11, T13 | T16, T17, T18 | **L** | T15 |
| T15 | PDP accordion (specs, materials, care) | T01 | — | **S** | T14 |
| T16 | PDP reviews (JudgeMe integration) | T14, JudgeMe app | — | **M** | T17, T18 |
| T17 | PDP sock-vs-skin comparison | T01 | — | **S** | T16 |
| T18 | PDP cross-sell rail | T19 | — | **S** | T16, T17 |
| T19 | Product card snippet | T01, T05, T13, T04 | T18, T23, T39, T42 | **M** | T14, T15 |
| T20 | Hero section (split, rotating eyebrow) | T01, T05 | — | **M** | T21–T35 |
| T21 | Pillar strip section | T01, T04 | — | **S** | T20, T22–T35 |
| T22 | 50/50 split section (reusable, 3 instances) | T01, T05 | — | **M** | T20, T21, T24–T35 |
| T23 | Variant grid section | T19, T11 | — | **L** | T20–T22, T24–T35 |
| T24 | Sock math section | T01, T05 | — | **M** | T20–T23, T25–T35 |
| T25 | Disciplines section | T01 | — | **S** | T20–T24, T26–T35 |
| T26 | Testimonial section | T01 | — | **S** | T20–T25, T27–T35 |
| T27 | Founder note section | T01 | — | **S** | T20–T26, T28–T35 |
| T28 | Association strip | T01 | — | **S** | T20–T27, T29–T35 |
| T29 | Credibility section | T01 | — | **S** | T20–T28, T30–T35 |
| T30 | Manifesto section | T01 | — | **M** | T20–T29, T31–T35 |
| T31 | Problem section | T01 | — | **S** | T20–T30, T32–T35 |
| T32 | Closing statement section | T01, T05 | — | **S** | T20–T31, T33–T35 |
| T33 | Newsletter section (Klaviyo) | T01, T05, Klaviyo app | — | **M** | T20–T32, T34–T35 |
| T34 | Guarantee section | T01, T04 | — | **S** | T20–T33, T35 |
| T35 | FAQ section | T01 | — | **S** | T20–T34 |
| T36 | Collection hero section | T01 | T40 | **S** | T37, T38, T41 |
| T37 | Sole type chooser | T01, T05 | T40 | **S** | T36, T38, T41 |
| T38 | Collection filter row | T01 | T39, T40 | **M** | T36, T37, T41 |
| T39 | Collection grid section | T19, T38 | T40 | **M** | T41, T42 |
| T40 | Collection template wiring | T36–T39 | — | **S** | T41, T42 |
| T41 | Article template | T01, T10 | — | **M** | T36–T40, T42 |
| T42 | Blog template | T43 | — | **M** | T36–T41 |
| T43 | Article card snippet | T01 | T42 | **S** | T41 |
| T44 | Social feed section (Juicer) | Juicer app | — | **M** | T41–T43, T45 |
| T45 | Predictive search + results template | T01, T19 | — | **M** | T41–T44 |
| T46 | 404 template | T01, T05 | — | **S** | T45 |
| T47 | Password template | T01 | — | **S** | T45, T46 |
| T48 | Metafield definitions | — | T14 (product MFs), T39 (collection MFs) | **S** | Any phase |
| T49 | Structured data (JSON-LD) | T14, T39, T41 | — | **M** | T50, T51, T52 |
| T50 | GA4 enhanced ecommerce events | T11 (cart), T14 (PDP) | — | **M** | T49, T51, T52 |
| T51 | Accessibility audit pass | All sections built | — | **M** | T52 |
| T52 | Performance audit (Lighthouse, budget) | All sections built | — | **M** | T51 |
| T53 | Strip review chrome | — | Launch | **S** | T51, T52 |

### Complexity Key

| Size | Estimate | Examples |
|------|----------|---------|
| **S** | 2–4 hours | Tokens, single snippet, simple section, breadcrumb |
| **M** | 4–8 hours | Header, 50/50 split, collection filters, reviews integration |
| **L** | 8–16 hours | Cart drawer, PDP main (gallery + buy box), variant grid |

### Total Estimate

- **S tasks (23):** ~60 hours
- **M tasks (22):** ~130 hours
- **L tasks (3):** ~36 hours
- **Total:** ~226 hours (~5.5 weeks at 40h/week for one developer)
- **With parallelism (2 devs):** ~3.5 weeks for build, +1 week QA/polish = ~4.5 weeks

---

**END OF DEPENDENCY GRAPH**
