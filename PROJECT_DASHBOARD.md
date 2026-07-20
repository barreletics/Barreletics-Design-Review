# Barreletics Blueprint — Project Dashboard

**Last Updated:** 2026-07-19
**Current Milestone:** 4C — Validation (Planning)

---

## Status Key
- ⚪ Not Started
- 🟡 In Progress
- 🔵 Ready for Review
- ✅ Approved
- 🔒 Locked

---

## Milestone 1: Foundation — 🔒 Locked

> **Foundation approved and locked — 2026-07-18.** Architectural changes require Decision Log approval.

### Completed & Locked

| # | Document | Status | Notes |
|---|----------|--------|-------|
| — | PDP Approved Page | 🔒 Locked | `Barreletics PDP - APPROVED July 17.html` |
| — | Home Approved Page | 🔒 Locked | `Barreletics Home - APPROVED July 17.html` |
| — | Collection v4 Page | 🔒 Locked | `Barreletics Collection - Definitive-v4.html` |
| — | Design System Skill | 🔒 Locked | `~/.cursor/skills/barreletics-design-system/SKILL.md` |
| — | Brand Copy Skill | 🔒 Locked | `~/.cursor/skills/barreletics-brand-copy/SKILL.md` |
| — | Slogan Engine Skill | 🔒 Locked | `~/.cursor/skills/barreletics-slogan-engine/SKILL.md` |

### Foundation Documents (Locked)

| # | Document | Status | File |
|---|----------|--------|------|
| 01 | Brand North Star | 🔒 | `planning/01-brand-north-star.md` |
| 02 | Brand System | 🔒 | `planning/02-brand-system.md` |
| 03 | Design System | 🔒 | `planning/03-design-system.md` |
| 04 | Component Library | 🔒 | `planning/04-component-library.md` |
| 05 | PDP Architecture | 🔒 | `planning/05-pdp-architecture.md` |
| 06 | Homepage Architecture | 🔒 | `planning/06-homepage-architecture.md` |
| 07 | Product Knowledge Base (Master) | 🔒 | `planning/07-product-knowledge-base.md` |
| 08 | Copy Guide | 🔒 | `planning/08-copy-guide.md` |
| 09 | Collection / Pillar Architecture | 🔒 | `planning/09-collection-architecture.md` |
| 10 | Decision Log | 🔒 | `planning/10-decision-log.md` |
| 11 | Navigation Architecture | 🔒 | `planning/11-navigation-architecture.md` |
| 12 | SEO & GEO Standards | 🔒 | `planning/12-seo-geo-standards.md` |
| 13 | Knowledge Architecture | 🔒 | `planning/13-knowledge-architecture.md` |

### Supporting Documents

| Document | Status | File |
|----------|--------|------|
| Master Roadmap | 🔒 | `planning/MASTER_ROADMAP.md` |
| Decision Framework | 🔒 | `planning/DECISION_FRAMEWORK.md` |
| Infrastructure Recommendations | 🔒 | `planning/INFRASTRUCTURE_RECOMMENDATIONS.md` |

### Archived (Superseded by Foundation Docs)

| Original File | Archived To | Superseded By |
|----------------|------------|---------------|
| `QA-01-BRAND-NORTH-STAR.md` | `planning/archive/` | Doc 01 |
| `QA-02-BRAND-SYSTEM.md` | `planning/archive/` | Doc 02 |
| `QA-03-DESIGN-SYSTEM.md` | `planning/archive/` | Doc 03 |
| `QA-07-COPY-GUIDE.md` | `planning/archive/` | Doc 08 |
| `QA-09-PRODUCT-KNOWLEDGE.md` | `planning/archive/` | Doc 07 |
| `component-inventory.md` | `planning/archive/` | Doc 04 |
| `executive-master-roadmap.md` | `planning/archive/` | `MASTER_ROADMAP.md` |

### Preserved (Still Referenced)

| File | Reason |
|------|--------|
| `ADR-01` through `ADR-07` | Historical reference — resolved in Doc 10 |
| `engineering-backlog.md` | 128 implementation tasks — active backlog |
| `shopify-build-specification.md` | Build spec — active reference for Tier 4 |

---

## Milestone 2: Core Experience — 🔒 Locked

> **Milestone 2: Core Experience approved and locked — 2026-07-18.** Shopify build system, core pages, variant selection, cart flow, Judge.me integration, GEO sections complete.

### Phase 1: Build System — ✅ Complete

| Deliverable | Status | File |
|-------------|--------|------|
| Build Specification v2 | ✅ | `planning/shopify-build-spec-v2.md` |
| Design Tokens CSS | ✅ | `shopify-build/assets/design-tokens.css` |
| Base Styles CSS | ✅ | `shopify-build/assets/barreletics-base.css` |
| Announcement Strip | ✅ | `shopify-build/snippets/announcement-strip.liquid` |
| Header / Navigation | ✅ | `shopify-build/snippets/header-nav.liquid` |
| Footer | ✅ | `shopify-build/snippets/footer.liquid` |
| Product Card | ✅ | `shopify-build/snippets/product-card.liquid` |
| FAQ Accordion | ✅ | `shopify-build/snippets/faq-accordion.liquid` |
| Section Wrapper | ✅ | `shopify-build/snippets/section-wrapper.liquid` |
| Trust Strip | ✅ | `shopify-build/snippets/trust-strip.liquid` |
| Button | ✅ | `shopify-build/snippets/button.liquid` |

### Phase 2: Page Builds — ✅ Complete

| Deliverable | Status | File |
|-------------|--------|------|
| **Snippets (D-022–D-025)** | | |
| Sticky ATC (D-023) | ✅ | `shopify-build/snippets/sticky-atc.liquid` |
| Cart Drawer (D-024) | ✅ | `shopify-build/snippets/cart-drawer.liquid` |
| Review Card (D-025) | ✅ | `shopify-build/snippets/review-card.liquid` |
| GEO Section (D-022) | ✅ | `shopify-build/snippets/geo-section.liquid` |
| **Homepage Sections** | | |
| Hero (50/50) | ✅ | `shopify-build/sections/hero.liquid` |
| Value Strip | ✅ | `shopify-build/sections/value-strip.liquid` |
| Variant Grid (tabbed) | ✅ | `shopify-build/sections/variant-grid.liquid` |
| Disciplines | ✅ | `shopify-build/sections/disciplines.liquid` |
| 50/50 Split (reusable) | ✅ | `shopify-build/sections/fifty-fifty.liquid` |
| Social Proof (reviews) | ✅ | `shopify-build/sections/social-proof.liquid` |
| Newsletter | ✅ | `shopify-build/sections/newsletter.liquid` |
| **Collection Sections** | | |
| Collection Hero | ✅ | `shopify-build/sections/collection-hero.liquid` |
| (reuses variant-grid, disciplines, fifty-fifty, newsletter) | | |
| **PDP Sections** | | |
| PDP Buy Box | ✅ | `shopify-build/sections/pdp-buy-box.liquid` |
| PDP Features | ✅ | `shopify-build/sections/pdp-features.liquid` |
| PDP Sock Math | ✅ | `shopify-build/sections/pdp-sock-math.liquid` |
| PDP Reviews (Judge.me custom) | ✅ | `shopify-build/sections/pdp-reviews.liquid` |
| PDP Sticky ATC wrapper | ✅ | `shopify-build/sections/pdp-sticky-atc.liquid` |
| **Templates** | | |
| Homepage (index.json) | ✅ | `shopify-build/templates/index.json` |
| Collection (collection.json) | ✅ | `shopify-build/templates/collection.json` |
| Product (product.json) | ✅ | `shopify-build/templates/product.json` |
| **Layout** | | |
| theme.liquid | ✅ | `shopify-build/layout/theme.liquid` |
| **Remaining** | | |
| Compare Page | ⚪ | Phase 3 |

### Phase 3: Quality Assurance — ✅ Complete

| Deliverable | Status | File |
|-------------|--------|------|
| QA Report | ✅ | `planning/milestone-2-qa-report.md` |
| Critical Fixes (13/13) | ✅ | Token, accessibility, markup, copy fixes |
| Minor Fixes (7/10) | ✅ | Hover, ARIA, color compliance fixes |
| Deferred (3 minor) | 📋 | Title tags (M-05/M-09), 50/50 dimensions (M-08) |

## Milestone 3: Supporting Experience — 🔒 Locked

> **Milestone 3: Supporting Experience approved and locked — 2026-07-18.** All supporting pages, collection templates, site experience features, GEO/SEO, and production hardening approved. Milestones 1-3 now constitute the canonical Barreletics architecture.

### Phase 1: Page Builds — ✅ Complete

| Deliverable | Status | File |
|-------------|--------|------|
| **Layout** | | |
| Theme (extended metadata, OG, schemas) | ✅ | `shopify-build/layout/theme.liquid` |
| **Supporting Pages** | | |
| FAQ Page | ✅ | `shopify-build/sections/page-faq.liquid` / `templates/page.faq.json` |
| About Page | ✅ | `shopify-build/sections/page-about.liquid` / `templates/page.about.json` |
| Contact Page | ✅ | `shopify-build/sections/page-contact.liquid` / `templates/page.contact.json` |
| **Blog / Journal** | | |
| Blog Listing | ✅ | `shopify-build/sections/blog-listing.liquid` / `templates/blog.json` |
| Article Content | ✅ | `shopify-build/sections/article-content.liquid` / `templates/article.json` |
| **Search** | | |
| Search Results | ✅ | `shopify-build/sections/search-results.liquid` / `templates/search.json` |
| **PDP Enhancements** | | |
| Recently Viewed (localStorage) | ✅ | `shopify-build/sections/recently-viewed.liquid` |
| Product Recommendations | ✅ | `shopify-build/sections/recommendations.liquid` |
| **Sub-Collection Pages** | | |
| New Arrivals | ✅ | `shopify-build/templates/collection.new-arrivals.json` |
| Limited Editions | ✅ | `shopify-build/templates/collection.limited-editions.json` |
| One-Offs | ✅ | `shopify-build/templates/collection.one-offs.json` |
| Gift Cards | ✅ | `shopify-build/templates/collection.gift-cards.json` |
| Sale | ✅ | `shopify-build/templates/collection.sale.json` |
| **Navigation** | | |
| Breadcrumb (all page types) | ✅ | `shopify-build/snippets/breadcrumb.liquid` |

### Phase 2: Structured Data & SEO — ✅ Complete

| Deliverable | Status | File |
|-------------|--------|------|
| Collection Schema (CollectionPage) | ✅ | `shopify-build/snippets/collection-schema.liquid` |
| Article Schema (BlogPosting) | ✅ | `shopify-build/snippets/article-schema.liquid` |
| Organization Schema (enhanced) | ✅ | `shopify-build/snippets/organization-schema.liquid` |
| Related Links snippet | ✅ | `shopify-build/snippets/related-links.liquid` |
| WebSite + SearchAction (homepage) | ✅ | In `layout/theme.liquid` |
| Open Graph tags (all pages) | ✅ | In `layout/theme.liquid` |
| Twitter Card (summary_large_image) | ✅ | In `layout/theme.liquid` |
| BreadcrumbList JSON-LD | ✅ | `snippets/breadcrumb.liquid` (canonical location) |

### Phase 3: Quality Assurance — ✅ Complete

| Deliverable | Status | File |
|-------------|--------|------|
| QA Report | ✅ | `planning/milestone-3-qa-report.md` |
| Critical Fixes (12/12) | ✅ | Token, accessibility, color compliance fixes |
| Decision Log entries D-028 through D-032 | ✅ | `planning/10-decision-log.md` |

### Architectural Decisions (M3)
| Decision | Summary |
|----------|---------|
| D-028 | Shipping/Returns as separate pages |
| D-029 | Grip Comparison as category disruption asset |
| D-030 | Header/Footer V2 pattern for non-breaking updates |
| D-031 | Recently Viewed via localStorage |
| D-032 | Collection templates reuse existing M2 sections |

### Deferred to Milestone 4
| Item | Status | Notes |
|------|--------|-------|
| Help Scout Integration | ⚪ | Docs 07, 13 approved — M4 scope |
| Tidio AI Setup | ⚪ | Docs 07, 13 approved — M4 scope |

## Milestone 4: Production Readiness — 🟡 In Progress

> Divided into 5 sequential gates per D-036. See `planning/MILESTONES-4-5-6-ROADMAP.md` for full scope.

| Gate | Name | Status | Entry Criterion |
|------|------|--------|----------------|
| M4A | Production Assembly | 🔒 Locked | M1-3 locked + Pre-Deployment Truth Set |
| M4B | Integrations | 🔒 Locked | M4A complete |
| M4C | Validation | ⚪ Planning | M4B complete + Policy Freeze Gate (D-040) |
| M4D | Launch | ⚪ | M4C complete + Pre-Deployment Truth Set verified |
| M4E | Stabilization | ⚪ | M4D complete (theme live) |

> **M4B locked** — all integration code in place with graceful degradation. D-045 documents production tracking strategy (Shopify native preferred, theme-level as fallback). Credential-dependent activation deferred to M4D Launch.

### M4B Deliverables

| Deliverable | Status | File |
|-------------|--------|------|
| **Tracking Snippets** | | |
| GA4 (gtag.js + enhanced ecommerce) | ✅ | `snippets/analytics-head.liquid`, `snippets/analytics-events.liquid` |
| Meta Pixel (base + events + dedup) | ✅ | `snippets/meta-pixel.liquid` |
| Pinterest Tag (base + events + enhanced match) | ✅ | `snippets/pinterest-tag.liquid` |
| Microsoft Clarity (session recording) | ✅ | `snippets/clarity.liquid` |
| Help Scout Beacon (chat widget) | ✅ | `snippets/helpscout-beacon.liquid` |
| Tidio AI Chat (support widget) | ✅ | `snippets/tidio-widget.liquid` |
| **Theme Configuration** | | |
| Settings Schema (Tracking & Integrations) | ✅ | `config/settings_schema.json` |
| Search Console verification meta tag | ✅ | `layout/theme.liquid` |
| Theme.liquid integration includes | ✅ | `layout/theme.liquid` |
| Graceful degradation (all snippets) | ✅ | All snippets use `{% if settings.* != blank %}` |
| Duplicate prevention (GA4/Meta warnings) | ✅ | Settings schema info text + snippet comments |
| **Judge.me** | | |
| Custom review rendering (D-025) | ✅ | `sections/pdp-reviews.liquid`, `snippets/review-card.liquid` |
| Metafield reads + API hydration | ✅ | `sections/pdp-reviews.liquid` |
| **Planning Documents** | | |
| Environment Config | ✅ | `planning/m4b-environment-config.md` |
| Verification Checklist | ✅ | `planning/m4b-verification-checklist.md` |
| Help Scout Alignment | ✅ | `planning/m4b-helpscout-alignment.md` |
| Tidio Knowledge Base | ✅ | `planning/m4b-tidio-knowledge-base.md` |
| Integration Plan | ✅ | `planning/m4b-integration-plan.md` |
| Implementation Checklist | ✅ | `planning/m4b-implementation-checklist.md` |
| Blockers Log | ✅ | `planning/m4b-blockers.md` |
| **Owner Actions Remaining** | | |
| Paste 5 tracking IDs into Theme Settings | ⚪ | GA4, Meta, Pinterest, Clarity, Search Console |
| Paste 2 widget keys into Theme Settings | ⚪ | Help Scout Beacon, Tidio |
| Configure Judge.me app (metafields + widget) | ⚪ | Judge.me admin |
| Configure CAPI (Meta & Instagram channel) | ⚪ | Shopify admin |
| Configure Google Merchant Center | ⚪ | Shopify admin |
| Create Help Scout saved replies | ⚪ | Help Scout admin |
| Import Tidio knowledge base | ⚪ | Tidio admin |

### M4A Deliverables

| Deliverable | Status | File |
|-------------|--------|------|
| Theme consolidation (v2 → canonical) | ✅ | `shopify-build/snippets/header-nav.liquid`, `footer.liquid` |
| Settings schema | ✅ | `shopify-build/config/settings_schema.json` |
| Settings data | ✅ | `shopify-build/config/settings_data.json` |
| Locale strings | ✅ | `shopify-build/locales/en.default.json` |
| Missing templates (cart, 404, page, customers/) | ✅ | `shopify-build/templates/` |
| Content Inventory | ✅ | `planning/m4a-content-inventory.md` |
| Navigation Config | ✅ | `planning/m4a-navigation-config.md` |
| Metafield Spec | ✅ | `planning/m4a-metafield-spec.md` |
| Asset Inventory | ✅ | `planning/m4a-asset-inventory.md` |
| Redirect Map (+ verification audit) | ✅ | `planning/m4a-redirect-map.md` |
| Pre-Deployment Baseline | ✅ | `planning/m4a-pre-deployment-baseline.md` |
| Hero Alt Concept (D-041) | ✅ | `shopify-build/sections/hero-alt.liquid` |
| Consolidated Partners Page (D-042) | ✅ | `shopify-build/sections/page-partners.liquid` / `templates/page.partners.json` |

### Key Decisions (M4-6 Roadmap)
| Decision | Summary |
|----------|---------|
| D-036 | Milestone 4 divided into 5 gates (M4A-M4E) with entry/exit criteria |
| D-037 | GEO expansion is data-gated, not volume-driven |
| D-038 | Milestone 5 scoped as finite v1, ongoing work → post-v1 operations |
| D-039 | All M4 tasks assigned Builder/Owner/Joint responsibility |
| D-040 | Policy Freeze Gate required before production QA |
| D-041 | Homepage hero — two concepts built for side-by-side comparison |
| D-042 | Partner Programs consolidated into single page |
| D-043 | Collections created only when products/merchandising require them |
| D-044 | M4A Production Assembly locked |
| D-045 | Production tracking strategy — Shopify native preferred, theme-level fallback only |
| D-046 | M4B Integrations locked — credential activation deferred to M4D |

## Milestone 5: Growth Platform (v1) — ⚪ Planning

> Finite v1 scope per D-038. Post-v1 operations defined separately.

## Milestone 6: Platform Completion — ⚪ Planning

> Deliverables include `GOVERNANCE-GUIDE.md`, `MAINTENANCE-GUIDE.md`, `DEPLOYMENT-GUIDE.md`, `CHANGELOG.md`, Git tag `v1.0.0`.

---

## Risks / Decisions Needed

| Risk | Impact | Mitigation |
|------|--------|------------|
| Foundation docs need Architect/Owner review before Milestone 2 starts | Blocks implementation | Prioritize review of docs 01–13 |
| Help Scout content migration scope TBD | May delay Milestone 3 | Define scope in Knowledge Architecture review |
| Photography assets are placeholders in approved pages | Blocks final launch | Set hard deadline for brand photography |

---

## Next Actions

1. **Owner:** Paste production IDs into Theme Settings → Tracking & Integrations (GA4, Meta, Pinterest, Clarity, Search Console, Help Scout, Tidio) — see `planning/m4b-environment-config.md`
2. **Owner:** Configure Judge.me app — enable metafield sync, disable default widget
3. **Owner:** Create Help Scout saved replies from `planning/m4b-helpscout-alignment.md`
4. **Owner:** Import Tidio knowledge base from `planning/m4b-tidio-knowledge-base.md`
5. **Owner:** Configure CAPI via Shopify Meta & Instagram channel
6. **Owner:** Install Google & YouTube channel for Merchant Center product feed
7. **Owner+Builder:** Run verification checklist (`planning/m4b-verification-checklist.md`)
8. **Builder:** Address deferred M2 minor issues (M-05, M-08, M-09) during deployment
