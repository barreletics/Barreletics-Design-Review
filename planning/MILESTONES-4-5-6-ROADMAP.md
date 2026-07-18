# Milestones 4, 5, 6 — Barreletics Endgame Roadmap

---
document: Milestones 4-5-6 Roadmap
status: ⚪ Planning
created: 2026-07-18
revised: 2026-07-18
revision_note: 12 architectural corrections per owner review (D-036 through D-040)
depends_on: Milestones 1-3 (locked)
---

## Overview

Milestones 1-3 established the canonical Barreletics architecture: brand system, design tokens, component library, all page templates, structured data, and site experience. **No architectural redesign is permitted** — all future work extends the approved systems.

This document defines the complete endgame: from production deployment through growth platform to platform v1.0 handoff.

---

## Milestone 4 — Production Readiness

**Objective:** Transform the completed architecture into a production-ready Shopify theme.

**Dependencies:** Milestones 1-3 locked, Shopify admin access, Judge.me account access, Help Scout access, Tidio access, GA4 access, Meta Business Manager access
**Estimated effort:** Large
**Success criteria:** See [Milestone 4 Success Criteria](#milestone-4-complete-when) at end of document

Milestone 4 is divided into five sequential gates. Each gate has explicit entry criteria, deliverables, and exit criteria. No gate may begin until the previous gate's exit criteria are satisfied.

| Gate | Name | Owner(s) |
|------|------|----------|
| M4A | Production Assembly | Builder + Owner |
| M4B | Integrations | Builder + Owner |
| M4C | Validation | Builder + Owner |
| M4D | Launch | Builder + Owner |
| M4E | Stabilization | Builder + Owner |

---

### M4A — Production Assembly

**Entry criteria:** Milestones 1-3 locked (D-035). Pre-Deployment Truth Set complete (see §9).
**Exit criteria:** Theme renders correctly in Shopify preview with all production content, navigation, and assets. Owner approves content and policy freeze (see §8).

#### M4A.1 Canonical Theme Consolidation

> **NOTE:** Some consolidation may have been completed during the M3 lock (D-030, D-035). Verify status before duplicating work.

| Task | Responsibility | Notes |
|------|---------------|-------|
| Consolidate `theme-m3.liquid` into canonical `theme.liquid` | Builder | Single layout file in production |
| Header v2 → canonical header | Builder | No parallel versioned header files |
| Footer v2 → canonical footer | Builder | No parallel versioned footer files |
| Single canonical BreadcrumbList (in `snippets/breadcrumb.liquid` only) | Builder | No duplicate BreadcrumbList in layout |
| Remove all parallel versioned files | Builder | Git history provides version control |
| Verify consolidation is complete | Builder | If already done in M3, note and confirm |

#### M4A.2 Shopify Preview Deployment

| Task | Responsibility |
|------|---------------|
| Upload theme to Shopify preview environment | Builder |
| Verify all sections render in preview | Builder |
| DNS and domain configuration verification | Owner |

#### M4A.3 Production Content Population

| Task | Responsibility |
|------|---------------|
| Theme settings population (settings_data.json — colors, typography, content) | Builder |
| Page creation for all supporting pages (FAQ, About, Contact, Shipping, Returns, Size Guide, Warranty, Wholesale, Ambassador, Studio Program, Grip Comparison, Technology) | Builder |
| Production copy approval | **Owner** |
| Pricing approval | **Owner** |

#### M4A.4 Navigation and Collection Configuration

| Task | Responsibility |
|------|---------------|
| Collection creation and product assignment (matching Doc 09) | Builder |
| Navigation menu configuration (matching Doc 11 — flat primary nav + footer) | Builder |
| Navigation link verification (no 404s) | Builder |

#### M4A.5 Metafields Setup

| Task | Responsibility |
|------|---------------|
| Judge.me review metafields | Builder |
| GEO content metafields | Builder |
| Product specification metafields | Builder |

#### M4A.6 Forms Configuration

| Task | Responsibility |
|------|---------------|
| Contact form routing verification | Builder |
| Newsletter signup form | Builder |
| Ambassador application form | Builder |
| Wholesale inquiry form | Builder |

#### M4A.7 Asset Upload

| Task | Responsibility |
|------|---------------|
| Logo upload | Builder (asset: **Owner**) |
| OG default image (`og-default.jpg`) | Builder (asset: **Owner**) |
| Favicons and touch icons | Builder (asset: **Owner**) |

#### M4A.8 Redirect Map (301s)

| Task | Responsibility |
|------|---------------|
| Existing URL crawl (all indexed pages) | Builder |
| New URL inventory | Builder |
| 301 redirect map (old → new) | Builder |
| Redirect implementation | Builder |
| Redirect verification (no 404s on previously indexed URLs) | Builder |

---

### M4B — Integrations

**Entry criteria:** M4A exit criteria satisfied.
**Exit criteria:** All required integrations configured and individually verified. Conditional integrations deferred unless owner confirms.

#### Required Integrations

**Judge.me** — Responsibility: Builder (access: **Owner**)
- Production validation and metafield sync
- Review import from existing store data (if applicable)
- Widget configuration (headless rendering via metafields, per D-025)
- Star rating display verification across PDP, collection cards, social proof section

**Help Scout** — Responsibility: Joint
- Saved replies aligned with Product Knowledge Base (Doc 07)
- Macro templates for common inquiries (sizing, shipping, returns, warranty)
- Contact form integration with page-contact.liquid
- Team assignment rules
- Customer-service workflow approval — **Owner**

**Tidio AI** — Responsibility: Builder (access: **Owner**)
- Knowledge base training from Doc 07 (Product Knowledge Base)
- Conversation flows: sizing help, shipping questions, returns process
- Handoff rules (when to escalate to human via Help Scout)
- Widget placement and styling (matching brand tokens)

**GA4 (Property 300437005)** — Responsibility: Builder (access: **Owner**)
- Enhanced ecommerce events: view_item, add_to_cart, begin_checkout, purchase
- Custom events: size_selector_click, sticky_atc_click, cart_drawer_open
- Conversion tracking configuration
- Cross-domain tracking (if applicable)
- Data stream verification

**Meta Pixel + CAPI** — Responsibility: Builder (access: **Owner**)
- Purchase, AddToCart, InitiateCheckout standard events
- ViewContent on PDP
- Conversions API (CAPI) server-side event verification
- Event deduplication (browser pixel + CAPI)
- Custom audience pixel fires

**Pinterest Tag** — Responsibility: Builder (access: **Owner**)
- Conversion tracking setup (purchase, add_to_cart, page_visit)
- Enhanced match parameters

**Microsoft Clarity** — Responsibility: Builder (access: **Owner**)
- Heatmap and session recording setup
- Smart events for key interactions

#### Conditional Integrations — Implement Only After Owner Confirmation

> Do not build or configure any paid application merely because it appears in this roadmap. Conditional integrations require explicit owner confirmation of active subscription and intended use before any implementation work begins.

**Klaviyo** — Status: ⚪ Unconfirmed
- Owner credentials required: Yes
- Builder can prepare: Email signup form markup (already in newsletter section)
- Builder cannot complete without access: Klaviyo account, API keys, flow configuration
- If confirmed:
  - Email signup forms (newsletter section integration)
  - Welcome flow, abandoned cart flow, post-purchase flow
  - Segment creation (by discipline, by purchase history)

---

### M4C — Validation

**Entry criteria:** M4B exit criteria satisfied. **Policy Freeze Gate** cleared (see §8 — owner sign-off on all business policies and content required before QA begins).
**Exit criteria:** All validation categories pass. No critical defects remain.

#### M4C.1 Functional QA (Purchase Flow End-to-End)

| Task | Responsibility |
|------|---------------|
| Cart flow: browse → add → drawer → checkout | Builder |
| Payment gateway tested (test mode) | Builder + Owner |
| Payment/tax verification | **Owner + accountant** |
| Shipping rates configured and calculating correctly | **Owner** |
| Tax settings verified by jurisdiction | **Owner + accountant** |
| Email notifications customized (order confirmation, shipping, etc.) | Builder |
| Gift card purchase and redemption | Builder |
| Discount code and automatic discount verification | Builder |

#### M4C.2 Accessibility Audit (WCAG 2.1 AA)

- Screen reader testing (VoiceOver on macOS/iOS, NVDA on Windows) — Builder
- Keyboard-only navigation testing (all interactive elements reachable) — Builder
- Color contrast verification (all text meets 4.5:1 minimum) — Builder
- Focus management audit (visible focus indicators, logical tab order) — Builder
- ARIA implementation validation (roles, labels, live regions) — Builder
- Form accessibility (labels, error messages, required indicators) — Builder
- Media accessibility (alt text, video captions if applicable) — Builder

#### M4C.3 Responsive/Device Testing

| Browser | Versions | Priority |
|---------|----------|----------|
| Chrome (Desktop) | Latest 2 | Critical |
| Safari (Desktop) | Latest 2 | Critical |
| Firefox (Desktop) | Latest 2 | High |
| Edge (Desktop) | Latest 2 | Medium |
| iOS Safari | Latest 2 | Critical |
| Chrome Mobile (iOS) | Latest | High |
| Chrome Mobile (Android) | Latest | High |

**Viewport testing:**
- 375px (iPhone SE — minimum supported)
- 390px (iPhone 14)
- 428px (iPhone 14 Pro Max)
- 768px (iPad portrait)
- 1024px (iPad landscape / small laptop)
- 1280px (standard laptop)
- 1440px (large desktop)
- 1920px (full HD)

#### M4C.4 Cross-Browser Testing

All pages render correctly across browser matrix above. Forms, cart, variant selection, sticky ATC, cart drawer all functional.

#### M4C.5 Structured Data Validation

- Google Rich Results Test for all page types — Builder
- Schema.org validator for all JSON-LD outputs — Builder
- Product schema with offers, aggregate rating (Judge.me)
- FAQ schema on FAQ page
- BreadcrumbList on all non-homepage pages
- Organization schema (homepage)
- BlogPosting schema (articles)
- CollectionPage schema (collections)
- WebSite + SearchAction (homepage)
- Test with Google Search Console after deployment

#### M4C.6 Performance (Lighthouse Lab Testing)

**Lighthouse Targets:**
- Performance ≥ 90
- Accessibility ≥ 95
- Best Practices ≥ 95
- SEO ≥ 95

**Core Web Vitals (Lab Testing — Pre-Launch):**
- LCP ≤ 2.5s
- INP ≤ 200ms
- CLS ≤ 0.1

> **Note:** FID is deprecated and replaced by INP (Interaction to Next Paint) as of March 2024. All Core Web Vitals targets use the current Google metric set.

> **Note:** Core Web Vitals field data cannot be fully validated before the new theme receives real production traffic. Lab testing (Lighthouse, Chrome DevTools) provides pre-launch estimates. True field data validation occurs during M4E Stabilization using Chrome User Experience Report (CrUX) data and GA4 Web Vitals.

**Performance optimization tasks:**
- Image optimization pipeline (WebP/AVIF conversion, responsive srcset, lazy loading) — Builder
- Critical CSS extraction for above-the-fold content — Builder
- JavaScript bundle analysis (variant-selector.js, cart-drawer.js, recently-viewed) — Builder
- Font loading optimization (preload key weights, font-display: swap) — Builder
- CDN and browser caching headers (Shopify CDN configuration) — Builder
- Reduce render-blocking resources — Builder
- Preconnect to critical third-party origins (Judge.me, GA4, Meta) — Builder

#### M4C.7 Analytics Event Validation

- GA4 events firing correctly (view_item, add_to_cart, begin_checkout, purchase) — Builder
- Meta Pixel events firing correctly — Builder
- CAPI events matching and deduplicating — Builder
- Pinterest Tag events — Builder
- Custom events (size_selector_click, sticky_atc_click, cart_drawer_open) — Builder

---

### M4D — Launch

**Entry criteria:** M4C exit criteria satisfied. Pre-Deployment Truth Set verified (see §9). Rollback strategy tested.
**Exit criteria:** Theme live in production. Real transaction completed. Immediate monitoring clean.

| Task | Responsibility |
|------|---------------|
| Full theme backup (current live theme .zip) | Builder |
| Rollback test (verify can revert to previous theme) | Builder |
| Theme publish | Builder + **Owner** approval |
| DNS propagation verification | Builder |
| Real transaction test (live purchase) | **Joint** |
| Verify GA4 events firing in production | Builder |
| Verify Meta Pixel events firing in production | Builder |
| Verify CAPI events matching in production | Builder |
| Immediate monitoring (0–4 hours): real-time GA4, error log review, order verification | Builder |
| 404 monitoring on previously indexed URLs | Builder |

---

### M4E — Stabilization

**Entry criteria:** M4D exit criteria satisfied. Theme live, real transaction confirmed.
**Exit criteria:** 30-day review complete with no unresolved critical issues.

| Review | Timing | Responsibility |
|--------|--------|---------------|
| 24-hour review | Launch +24h | Builder |
| 48-hour review | Launch +48h | Builder + Owner |
| 7-day review | Launch +7d | Builder + Owner |
| 30-day SEO and analytics review | Launch +30d | Builder + Owner |

**24-hour review includes:**
- Full GA4 comparison to previous day
- Conversion rate check
- Page speed check
- Error log review
- Order verification

**48-hour review includes:**
- Search Console coverage report
- Core Web Vitals field data (initial — may take time to accumulate in CrUX)
- Customer feedback review

**7-day review includes:**
- Full analytics comparison (week-over-week)
- SEO ranking check
- Customer feedback review
- Integration health (Judge.me, GA4, Meta, CAPI)

**30-day review includes:**
- Full analytics comparison (month-over-month)
- SEO ranking stability
- Core Web Vitals field data (CrUX — sufficient sample size by 30 days)
- Search Console index coverage
- Redirect verification (all 301s working)
- Customer support patterns

---

### M4 Risk Assessment

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| SEO ranking disruption during switch | Medium | High | 301 redirects mapped, keep old URLs valid, monitor Search Console daily | Builder + Owner |
| Judge.me metafield sync delay | Low | Medium | Test in preview; have manual fallback display | Builder |
| Performance below targets on mobile | Medium | Medium | Audit before launch; defer non-critical JS; lazy-load below fold | Builder |
| Payment/checkout issues | Low | Critical | Test mode verification + live small-amount test purchase | Owner + Builder |
| Customer confusion during transition | Low | Medium | Communication plan; keep old theme as instant rollback | Owner |
| Data integrity during migration (products, metafields, reviews) | Low | Critical | Full backup before migration; verify counts post-migration | Builder + Owner |

---

## §8 — Policy Freeze Gate

**This gate is an entry criterion for M4C (Validation).** Builder must not treat draft business rules as production-approved.

Before final production QA begins, the **Owner** must sign off on all of the following:

| Policy / Content | Owner Sign-Off |
|-----------------|---------------|
| Shipping terms | ☐ |
| Return terms | ☐ |
| Warranty language | ☐ |
| Pricing (all products) | ☐ |
| Discounts and promo codes | ☐ |
| Free-shipping threshold ($150) | ☐ |
| Size guidance | ☐ |
| Product claims | ☐ |
| Wholesale terms | ☐ |
| Studio Program terms | ☐ |
| Ambassador terms | ☐ |

Builder may not proceed to M4C until all items are signed off. Any post-freeze changes require a new Decision Log entry.

---

## §9 — Pre-Deployment Truth Set

**This inventory is an entry criterion for M4A (Production Assembly) and must be verified again before M4D (Launch).**

| Item | Status | Responsibility |
|------|--------|---------------|
| Existing URL crawl (all indexed pages) | ☐ | Builder |
| New URL inventory | ☐ | Builder |
| 301 redirect map (old → new) | ☐ | Builder |
| Product handle comparison (old vs new) | ☐ | Builder |
| Collection handle comparison (old vs new) | ☐ | Builder |
| Page handle comparison (old vs new) | ☐ | Builder |
| Existing metadata export (titles, descriptions) | ☐ | Builder |
| Existing analytics baseline (traffic, conversion rate) | ☐ | Builder |
| Existing review-count baseline (Judge.me) | ☐ | Builder |
| Existing theme backup (full .zip) | ☐ | Builder |

---

## Milestone 5 — Growth Platform (v1 Scope)

**Objective:** Build everything that increases traffic, conversion, and merchandising without changing the architecture.

**Dependencies:** Milestone 4 complete (production site live, M4E stabilization passed), analytics data flowing, customer data available
**Estimated effort:** Medium (finite v1 scope — see deliverables below)
**Success criteria:** See [Milestone 5 Success Criteria](#milestone-5-complete-when) at end of document

### Milestone 5 v1 Completion Definition

Milestone 5 v1 is complete when ALL of the following are operational:

1. Reusable landing-page framework operational
2. One live campaign implemented and measured
3. One complete One-Offs drop workflow documented and tested
4. Initial Journal taxonomy and publishing process established
5. Initial studio and wholesale resource structures created
6. CRO baseline recorded and prioritized experiment backlog created
7. GEO qualification framework operational

Continued campaigns, content publishing, experimentation, and market expansion move to **Post-v1 Operations** (see bottom of this section).

---

### 5.1 Landing Page Framework

- Reusable landing page template system using existing sections (hero, fifty-fifty, value-strip, social-proof, newsletter)
- Campaign-specific page builder patterns (compose from section library)
- Seasonal promotion templates (holiday, back-to-studio, new year)
- UTM-specific landing experiences (match ad creative to page content)

### 5.2 Campaign Architecture

- UTM tracking standards (reference existing UTM guide at `/Users/andrewnehra/Documents/Claude/Projects/Barreletics social/utm-tracking/UTM-GUIDE.md`)
- Campaign landing page → collection → PDP conversion flow
- Email campaign templates (aligned with brand design system)
- Social media campaign landing pages (Meta, Pinterest creative → dedicated pages)
- Paid media landing page optimization (match message to ad promise)
- Retargeting audience strategy (site visitors, cart abandoners, purchasers)

### 5.3 Seasonal & Collection Framework

- Seasonal collection system (Spring/Summer, Fall/Winter releases)
- New Arrivals automation (date-based, auto-rotating)
- Limited Edition drop workflow (announce → countdown → release → sold out)
- One-Offs release process (single-item drops, scarcity messaging per brand guardrails)
- Color launch playbook (new colorway → collection update → email → social)

### 5.4 Editorial / Journal Expansion

- Content calendar framework (cadence, categories, SEO targets)
- Article templates by type:
  - Education (discipline guides, performance skin care explainers)
  - Studio Spotlight (partner studio features)
  - Product Story (design decisions, material innovations)
  - Discipline Guide (barre, Pilates, Lagree, reformer, yoga)
- SEO article optimization checklist (target keywords, internal links, schema)
- Internal linking strategy (articles → products/collections, bidirectional)
- Author and category taxonomy

### 5.5 Studio Resource Center

- Studio partnership portal/page (info, application, benefits)
- Instructor resources (class recommendations, student sizing guidance)
- Studio ordering process documentation
- Marketing materials for studios (digital assets, print templates)
- Case studies / success stories (partner studio testimonials)

### 5.6 Wholesale Resource Library

- Wholesale catalog (product line, pricing tiers, minimums)
- Volume pricing and discount structure documentation
- Order process documentation (how to place, reorder, handle returns)
- Brand guidelines for retail partners (display, messaging, restrictions)
- Marketing assets for retail environments

### 5.7 Ambassador Expansion

- Application and approval workflow (form → review → onboard)
- Ambassador dashboard or portal page (links, assets, performance)
- Commission/referral tracking integration (discount codes or affiliate platform)
- Content creation guidelines (brand voice, approved claims, visual standards)
- Ambassador spotlight features (journal articles, social features)

### 5.8 Data-Gated GEO Expansion Program

> Location pages are authorized ONLY when supported by verifiable data. Do not create thin, repetitive location pages for SEO volume.

**GEO page qualification criteria — ALL must be met before creating a location page:**

1. **Verified search demand** — keyword research shows meaningful search volume for the location + product/service terms
2. **Customer/order concentration data** — Shopify order data confirms customer presence in the target location
3. **Studio density or active partners** — at least one active studio partner or verifiable studio density in the area
4. **Unique local content available** — real, differentiated content exists for the location (not templated filler)
5. **Clear conversion path** — the page has a specific next action (studio finder, product recommendation, local event)

**Process:**
- Builder proposes location pages with supporting data
- Owner approves each location page individually
- Builder creates page only after approval
- No batch-creation of city/state/international pages without individual justification

### 5.9 CRO Opportunities

- Cart abandonment recovery (email flow, exit intent, retargeting)
- Exit intent strategy (email capture, not discounting — per brand positioning)
- Social proof optimization (review placement, count visibility, UGC)
- Urgency/scarcity (authentic only — "X left in this size" from real inventory, seasonal deadlines)
- Multi-pair Performance Skin recommendations (Open Sole + Closed Sole pairing, Studio + Outdoor pairing)
- Product recommendation engine refinement (by discipline, by purchase history)
- Mobile checkout optimization (reduce steps, Apple Pay/Google Pay prominence)
- Size confidence (size guide prominence, fit guarantee messaging)
- Accessories or future owner-approved product category cross-sell

> **Note:** Do not introduce future product assumptions (socks, bundles, kits) unless owner explicitly approves the product category.

### 5.10 Future Personalization

- Returning visitor experience (welcome back, recently viewed prominence)
- Discipline-based product recommendations (yoga → specific models)
- Size memory / preferences (localStorage or account-based)
- Wishlist functionality (save for later, back-in-stock notifications)

---

### Post-v1 Operations (Not Part of Milestone 5 Completion)

The following are ongoing operational activities that continue after Milestone 5 v1 is declared complete. They do not block v1.0 declaration.

- Continued campaign creation and measurement
- Continued Journal article publishing
- Continued CRO experimentation (A/B tests, iteration)
- GEO page expansion (per qualification framework)
- Ambassador program growth
- Studio and wholesale partnership expansion
- Seasonal collection refreshes
- New product category launches (only when owner-approved)

---

## Milestone 6 — Platform Completion

**Objective:** Finish Barreletics Version 1.0 — the complete operating system for the brand.

**Dependencies:** Milestones 4-5 complete, production site stable, initial customer data
**Estimated effort:** Medium
**Success criteria:** See [Milestone 6 Success Criteria](#milestone-6-complete-when) at end of document

---

### 6.1 Final Documentation Audit

- All 13 Foundation documents reviewed for accuracy post-launch
- Implementation learnings incorporated (what changed from plan to reality)
- Gap analysis between planned architecture and actual implementation
- Any new decisions logged (D-036+)

### 6.2 Knowledge Base Reconciliation

- Doc 07 updated with new Q&A from post-launch customer interactions
- Help Scout saved replies verified against Knowledge Base (no drift)
- Tidio AI responses verified against Knowledge Base (no contradictions)
- All channels delivering consistent answers (website, email, chat, social)
- Retired claims list reviewed and enforced

### 6.3 Design System v1.0 Lock

**Deliverables:**
- `planning/03-design-system.md` — canonical design system document (updated with any implementation refinements)
- `/Users/andrewnehra/.cursor/skills/barreletics-design-system/SKILL.md` — design system skill (updated)
- Token values finalized (any adjustments from production testing)
- Component specifications updated to reflect actual Shopify implementation
- Design System versioned as v1.0 (semantic version lock)
- Change process documented (how to propose token/component changes)

### 6.4 Component Catalog

**Deliverables:**
- `planning/04-component-library.md` — canonical component library document
- `shopify-build/snippets/` — complete inventory of all Liquid snippets
- `shopify-build/sections/` — complete inventory of all Liquid sections
- Usage documentation for each component (props/settings, variants, examples)
- Configuration options documented (JSON template settings)
- Visual examples / screenshots of each component in production
- Dependency map (which components render which snippets)

### 6.5 Governance Documentation

**Deliverables:**
- `planning/GOVERNANCE-GUIDE.md` — new deliverable
  - Content update process (who can edit what, approval flow)
  - Theme update process (branch → PR → review → deploy)
  - New page creation process (template selection, section composition)
  - New collection creation process (template, nav update, announcements)
  - Product launch checklist (photography, copy, metafields, collection assignment)
  - Seasonal update checklist (hero swap, collection refresh, promotion pages)
  - Emergency rollback procedure (unpublish theme, verify, communicate)

### 6.6 Maintenance Guide

**Deliverables:**
- `planning/MAINTENANCE-GUIDE.md` — new deliverable
  - Routine maintenance tasks (weekly, monthly, quarterly)
  - Monitoring checklist:
    - Performance: Lighthouse CI, Core Web Vitals field data
    - Accessibility: automated scans + quarterly manual audit
    - SEO: Search Console, ranking tracking, crawl errors
    - Integration health: Judge.me sync, GA4 events, Meta Pixel, CAPI
  - Shopify platform updates (how to handle theme API changes)
  - Third-party app updates (Judge.me, Tidio, Help Scout version changes)

### 6.7 Deployment Guide

**Deliverables:**
- `planning/DEPLOYMENT-GUIDE.md` — new deliverable
  - Shopify CLI usage (theme push, preview, publish)
  - Pre-deployment checklist
  - Post-deployment verification
  - Rollback procedure
  - Environment management (preview vs production)

### 6.8 Technical Debt Review

- Known limitations documented (what the architecture can't do yet)
- Improvement opportunities cataloged (performance gains, UX refinements)
- Prioritized backlog for v1.1 (quick wins vs. larger efforts)
- Browser support sunset plan (when to drop older versions)

### 6.9 Future Roadmap

- Additional product category framework (how to add new categories)
- Internationalization considerations (multi-currency, language, regional shipping)
- Multi-language preparation (if applicable — translation workflow, hreflang)
- Platform evolution path (Shopify Online Store 2.0 features, new APIs)

### 6.10 AI Governance

- AI content generation rules finalized (what AI can/cannot write)
- Knowledge Base training documentation (how to update AI systems)
- Approved prompt templates for AI systems (Tidio, internal tools)
- Quality assurance process for AI-generated content (human review gates)
- Brand guardrails for AI (claims it must never make, tone boundaries)

### 6.11 Versioning Strategy

**Deliverables:**
- `CHANGELOG.md` — at repo root
- Git tags (e.g., `v1.0.0`) — version record
- Semantic versioning for the platform: v1.0 (launch), v1.x (growth additions), v2.0 (major redesign)
- Change log format and maintenance process
- Release process (tag, changelog, deploy, verify)
- Breaking change policy (what constitutes a breaking change, communication)
- Theme version tracking in Shopify (naming convention, notes)

### 6.12 Platform Handoff Documentation

- Complete technical documentation for any future developer
- Architecture overview (how Milestones 1-3 compose into the full system)
- Repository guide (directory structure, file naming, build process)
- Deployment guide (reference `planning/DEPLOYMENT-GUIDE.md`)
- "Day 1" developer onboarding document (get productive in < 1 day)
- Decision Log orientation (how to read, how to add entries)

> **No governance artifact should exist only in an AI tool or undocumented external context.** Every operational document must have a concrete file path in this repository.

---

## Cross-Milestone Risk Register

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|------|-----------|--------|------------|-------|
| R-01 | SEO ranking disruption during theme switch | Medium | High | Map all existing URLs to new; 301 redirects for any changes; monitor Search Console daily for 30 days; keep old theme as rollback | Builder + Owner |
| R-02 | Third-party integration failures (Judge.me, Tidio, CAPI) | Low | High | Test all integrations in preview/staging; have manual fallback for each; stagger integration activation post-launch | Builder |
| R-03 | Performance regression on production data volume | Medium | Medium | Test with full product catalog; lazy-load non-critical sections; monitor CWV field data daily post-launch | Builder |
| R-04 | Customer experience disruption during migration | Low | High | Launch during low-traffic window; "pardon our dust" banner if needed; customer service team briefed; instant rollback available | Owner |
| R-05 | Data integrity during migration (products, metafields, reviews) | Low | Critical | Full backup before migration; verify product count, metafield data, review count post-migration; test orders in both themes | Builder + Owner |
| R-06 | Team capacity / knowledge transfer | Medium | Medium | Document everything in M6; ensure no single-point-of-failure knowledge; governance docs enable anyone to maintain | Owner |
| R-07 | Timeline pressure vs quality | Medium | High | Milestones are sequential — do not skip M4 validation for speed; launch readiness is binary (ready or not); no partial launches | Owner |
| R-08 | Photography assets remain placeholder at launch | High | Medium | Define hard deadline for brand photography; identify which pages can launch with lifestyle stock; prioritize hero and PDP imagery | Owner |
| R-09 | Shopify platform changes during development | Low | Medium | Pin to current API version; monitor Shopify changelog; test in preview before adopting new features | Builder |
| R-10 | Meta Pixel / CAPI overclaim post-launch | Medium | Medium | Establish Shopify-as-truth baseline (per existing diagnostic skills); monitor Meta claimed vs Shopify attributed weekly | Owner + Builder |

---

## Milestone Dependency Chain

```
M1 (Foundation) → M2 (Core Experience) → M3 (Supporting Experience)
                                                      ↓
                                              M4A (Production Assembly)
                                                      ↓
                                              M4B (Integrations)
                                                      ↓
                                           [Policy Freeze Gate]
                                                      ↓
                                              M4C (Validation)
                                                      ↓
                                        [Pre-Deployment Truth Set]
                                                      ↓
                                              M4D (Launch)
                                                      ↓
                                              M4E (Stabilization)
                                                      ↓
                                              M5 (Growth Platform v1)
                                                      ↓
                                              M6 (Platform Completion) → v1.0 🎯
```

---

## Final Success Criteria

### Milestone 4 Complete When:

- Canonical theme deployed to production (no parallel versioned files)
- Purchase path works end-to-end (real transaction completed)
- All required integrations verified (Judge.me, GA4, Meta Pixel, CAPI, Pinterest Tag, Clarity)
- No critical accessibility defects remain (WCAG 2.1 AA)
- No critical schema errors remain (Google Rich Results Test passes)
- Redirects verified (no 404s on previously indexed URLs)
- Analytics events validated (purchase, add_to_cart, begin_checkout, view_item, pageview)
- Rollback tested and documented
- Owner approves all production policies and content (Policy Freeze Gate cleared)
- 30-day stabilization review complete (M4E)

### Milestone 5 Complete When:

- Growth framework is reusable (landing page template system operational)
- At least one real campaign deployed and measured
- One-Offs operating workflow documented and tested
- Editorial system ready for repeated publishing (Journal taxonomy + process)
- CRO baseline and experiment backlog recorded
- GEO expansion is data-gated (qualification framework operational)

### Milestone 6 Complete When:

- Repository documentation matches production exactly
- Design System v1.0 locked (`planning/03-design-system.md` + design system skill updated)
- Component catalog complete with usage documentation (`planning/04-component-library.md` + snippet/section inventory)
- Governance and maintenance procedures documented (`planning/GOVERNANCE-GUIDE.md`, `planning/MAINTENANCE-GUIDE.md`, `planning/DEPLOYMENT-GUIDE.md`)
- Knowledge Base reconciled (`planning/07-product-knowledge-base.md`)
- Technical debt recorded and prioritized
- Handoff package complete (onboarding doc, architecture overview, repo guide)
- Platform v1.0 tagged in Git (`v1.0.0`) and formally declared
- `CHANGELOG.md` at repo root reflects full history

---

## Document Status

This is a **planning document only** — no code, no implementation. It must be reviewed and approved by the Owner before any Milestone 4 work begins.
