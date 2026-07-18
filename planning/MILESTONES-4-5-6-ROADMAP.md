# Milestones 4, 5, 6 — Barreletics Endgame Roadmap

---
document: Milestones 4-5-6 Roadmap
status: ⚪ Planning
created: 2026-07-18
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
**Success criteria:** Theme passes all Lighthouse targets, all integrations functional, launch checklist 100% complete, rollback tested

---

### 4.1 Production Deployment Strategy

- Theme migration plan (current live theme → new theme)
- Staging/preview environment setup via Shopify theme preview
- Data migration considerations (existing products, collections, pages, metafields)
- DNS and domain configuration verification
- Rollback strategy (keep current live theme unpublished; one-click revert)
- Launch window and communication plan (low-traffic window, team alerts)

### 4.2 Shopify Production Configuration

- Theme settings population (settings_data.json — colors, typography, content)
- Collection creation and product assignment (matching Doc 09 architecture)
- Page creation for all supporting pages (FAQ, About, Contact, Shipping, Returns, Size Guide, Warranty, Wholesale, Ambassador, Studio Program, Grip Comparison, Technology)
- Navigation menu configuration (matching Doc 11 — flat primary nav + footer)
- Metafield setup for Judge.me reviews, GEO content, product specifications
- Payment, shipping, and tax configuration verification
- Gift card product setup
- Discount code and automatic discount configuration

### 4.3 Third-Party Integrations

**Judge.me**
- Production validation and metafield sync
- Review import from existing store data (if applicable)
- Widget configuration (headless rendering via metafields, per D-025)
- Star rating display verification across PDP, collection cards, social proof section

**Help Scout**
- Saved replies aligned with Product Knowledge Base (Doc 07)
- Macro templates for common inquiries (sizing, shipping, returns, warranty)
- Contact form integration with page-contact.liquid
- Team assignment rules

**Tidio AI**
- Knowledge base training from Doc 07 (Product Knowledge Base)
- Conversation flows: sizing help, shipping questions, returns process
- Handoff rules (when to escalate to human via Help Scout)
- Widget placement and styling (matching brand tokens)

**GA4 (Property 300437005)**
- Enhanced ecommerce events: view_item, add_to_cart, begin_checkout, purchase
- Custom events: size_selector_click, sticky_atc_click, cart_drawer_open
- Conversion tracking configuration
- Cross-domain tracking (if applicable)
- Data stream verification

**Meta Pixel + CAPI**
- Purchase, AddToCart, InitiateCheckout standard events
- ViewContent on PDP
- Conversions API (CAPI) server-side event verification
- Event deduplication (browser pixel + CAPI)
- Custom audience pixel fires

**Pinterest Tag**
- Conversion tracking setup (purchase, add_to_cart, page_visit)
- Enhanced match parameters

**Microsoft Clarity**
- Heatmap and session recording setup
- Smart events for key interactions

**Klaviyo (if applicable)**
- Email signup forms (newsletter section integration)
- Welcome flow, abandoned cart flow, post-purchase flow
- Segment creation (by discipline, by purchase history)

### 4.4 Performance Optimization

**Targets:**
- Lighthouse Performance ≥ 90
- Lighthouse Accessibility ≥ 95
- Lighthouse Best Practices ≥ 95
- Lighthouse SEO ≥ 95

**Core Web Vitals:**
- LCP < 2.5s
- FID < 100ms (INP < 200ms)
- CLS < 0.1

**Optimization tasks:**
- Image optimization pipeline (WebP/AVIF conversion, responsive srcset, lazy loading)
- Critical CSS extraction for above-the-fold content
- JavaScript bundle analysis (variant-selector.js, cart-drawer.js, recently-viewed)
- Font loading optimization (preload key weights, font-display: swap)
- CDN and browser caching headers (Shopify CDN configuration)
- Reduce render-blocking resources
- Preconnect to critical third-party origins (Judge.me, GA4, Meta)

### 4.5 Accessibility Certification

**WCAG 2.1 AA full audit:**
- Screen reader testing (VoiceOver on macOS/iOS, NVDA on Windows)
- Keyboard-only navigation testing (all interactive elements reachable)
- Color contrast verification (all text meets 4.5:1 minimum)
- Focus management audit (visible focus indicators, logical tab order)
- ARIA implementation validation (roles, labels, live regions)
- Form accessibility (labels, error messages, required indicators)
- Media accessibility (alt text, video captions if applicable)

### 4.6 Cross-Browser/Device Testing

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

### 4.7 Structured Data Validation

- Google Rich Results Test for all page types
- Schema.org validator for all JSON-LD outputs
- Product schema with offers, aggregate rating (Judge.me)
- FAQ schema on FAQ page
- BreadcrumbList on all non-homepage pages
- Organization schema (homepage)
- BlogPosting schema (articles)
- CollectionPage schema (collections)
- WebSite + SearchAction (homepage)
- Test with Google Search Console after deployment

### 4.8 Launch Checklist

**Pre-launch:**
- [ ] All pages render correctly in Shopify preview
- [ ] All forms submit and route to correct destinations
- [ ] Cart flow: browse → add → drawer → checkout functional
- [ ] All navigation links resolve (no 404s)
- [ ] Favicon and touch icons configured
- [ ] robots.txt and sitemap.xml correct
- [ ] Canonical URLs set on all pages
- [ ] Meta tags (title, description) populated for every page
- [ ] OG and Twitter Card images uploaded and rendering
- [ ] SSL certificate valid
- [ ] Payment gateway tested (test mode + live verification)
- [ ] Shipping rates configured and calculating correctly
- [ ] Tax settings verified by jurisdiction
- [ ] Email notifications customized (order confirmation, shipping, etc.)
- [ ] Judge.me reviews displaying with correct styling

**Launch:**
- [ ] Publish new theme
- [ ] Verify DNS propagation
- [ ] Test purchase flow end-to-end (real transaction)
- [ ] Verify GA4 events firing
- [ ] Verify Meta Pixel events firing
- [ ] Verify CAPI events matching

**Post-launch monitoring:**
- 0-4 hours: Real-time GA4 monitoring, error log review, order verification
- 24 hours: Full GA4 comparison to previous day, conversion rate check, page speed check
- 48 hours: Search Console coverage report, Core Web Vitals field data
- 1 week: Full analytics comparison, SEO ranking check, customer feedback review

### 4.9 Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| SEO ranking disruption during switch | Medium | High | 301 redirects mapped, keep old URLs valid, monitor Search Console daily |
| Judge.me metafield sync delay | Low | Medium | Test in preview; have manual fallback display |
| Performance below targets on mobile | Medium | Medium | Audit before launch; defer non-critical JS; lazy-load below fold |
| Payment/checkout issues | Low | Critical | Test mode verification + live small-amount test purchase |
| Customer confusion during transition | Low | Medium | Communication plan; keep old theme as instant rollback |

---

## Milestone 5 — Growth Platform

**Objective:** Build everything that increases traffic, conversion, and merchandising without changing the architecture.

**Dependencies:** Milestone 4 complete (production site live), analytics data flowing, customer data available  
**Estimated effort:** Large (ongoing)  
**Success criteria:** Landing page system operational, first campaign deployed, journal publishing, CRO baseline established, geo content expanding

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
  - Education (discipline guides, sock math explainers)
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

### 5.8 GEO Content Roadmap

- City-level landing pages (top 20 markets by studio density)
- State-level content hubs (California, New York, Texas, Florida priorities)
- International market pages (Canada, UK, Australia if applicable)
- Studio directory (curated partner list by city/region)
- Local SEO optimization (Google Business Profile, local schema, NAP consistency)

### 5.9 CRO Opportunities

- Cart abandonment recovery (email flow, exit intent, retargeting)
- Exit intent strategy (email capture, not discounting — per brand positioning)
- Social proof optimization (review placement, count visibility, UGC)
- Urgency/scarcity (authentic only — "X left in this size" from real inventory, seasonal deadlines)
- Cross-sell and upsell optimization (Performance Skins + future socks bundle)
- Product recommendation engine refinement (by discipline, by purchase history)
- Mobile checkout optimization (reduce steps, Apple Pay/Google Pay prominence)
- Size confidence (size guide prominence, fit guarantee messaging)

### 5.10 Future Personalization

- Returning visitor experience (welcome back, recently viewed prominence)
- Discipline-based product recommendations (yoga → specific models)
- Size memory / preferences (localStorage or account-based)
- Wishlist functionality (save for later, back-in-stock notifications)
- "Build Your Perfect Fit" kit builder (Performance Skins + future socks pairing)

---

## Milestone 6 — Platform Completion

**Objective:** Finish Barreletics Version 1.0 — the complete operating system for the brand.

**Dependencies:** Milestones 4-5 complete, production site stable, initial customer data  
**Estimated effort:** Medium  
**Success criteria:** All documentation complete, governance processes established, v1.0 formally declared, handoff package ready

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

- Design System skill updated with any implementation refinements
- Token values finalized (any adjustments from production testing)
- Component specifications updated to reflect actual Shopify implementation
- Design System versioned as v1.0 (semantic version lock)
- Change process documented (how to propose token/component changes)

### 6.4 Component Catalog

- Complete catalog of all Liquid sections and snippets
- Usage documentation for each component (props/settings, variants, examples)
- Configuration options documented (JSON template settings)
- Visual examples / screenshots of each component in production
- Dependency map (which components render which snippets)

### 6.5 Governance Documentation

- Content update process (who can edit what, approval flow)
- Theme update process (branch → PR → review → deploy)
- New page creation process (template selection, section composition)
- New collection creation process (template, nav update, announcements)
- Product launch checklist (photography, copy, metafields, collection assignment)
- Seasonal update checklist (hero swap, collection refresh, promotion pages)
- Emergency rollback procedure (unpublish theme, verify, communicate)

### 6.6 Maintenance Guide

- Routine maintenance tasks (weekly, monthly, quarterly)
- Monitoring checklist:
  - Performance: Lighthouse CI, Core Web Vitals field data
  - Accessibility: automated scans + quarterly manual audit
  - SEO: Search Console, ranking tracking, crawl errors
  - Integration health: Judge.me sync, GA4 events, Meta Pixel, CAPI
- Shopify platform updates (how to handle theme API changes)
- Third-party app updates (Judge.me, Tidio, Help Scout version changes)

### 6.7 Technical Debt Review

- Known limitations documented (what the architecture can't do yet)
- Improvement opportunities cataloged (performance gains, UX refinements)
- Prioritized backlog for v1.1 (quick wins vs. larger efforts)
- Browser support sunset plan (when to drop older versions)

### 6.8 Future Roadmap

- Barreletics Socks launch preparation (new product type, PDP variant, collection)
- Additional product category framework (how to add new categories)
- Internationalization considerations (multi-currency, language, regional shipping)
- Multi-language preparation (if applicable — translation workflow, hreflang)
- Platform evolution path (Shopify Online Store 2.0 features, new APIs)

### 6.9 AI Governance

- AI content generation rules finalized (what AI can/cannot write)
- Knowledge Base training documentation (how to update AI systems)
- Approved prompt templates for AI systems (Tidio, internal tools)
- Quality assurance process for AI-generated content (human review gates)
- Brand guardrails for AI (claims it must never make, tone boundaries)

### 6.10 Versioning Strategy

- Semantic versioning for the platform: v1.0 (launch), v1.x (growth additions), v2.0 (major redesign)
- Change log format and maintenance process
- Release process (tag, changelog, deploy, verify)
- Breaking change policy (what constitutes a breaking change, communication)
- Theme version tracking in Shopify (naming convention, notes)

### 6.11 Platform Handoff Documentation

- Complete technical documentation for any future developer
- Architecture overview (how Milestones 1-3 compose into the full system)
- Repository guide (directory structure, file naming, build process)
- Deployment guide (Shopify CLI, theme push, preview, publish)
- "Day 1" developer onboarding document (get productive in < 1 day)
- Decision Log orientation (how to read, how to add entries)

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
                                              M4 (Production Readiness)
                                                      ↓
                                              M5 (Growth Platform)
                                                      ↓
                                              M6 (Platform Completion) → v1.0 🎯
```

---

## Document Status

This is a **planning document only** — no code, no implementation. It must be reviewed and approved by the Owner before any Milestone 4 work begins.
