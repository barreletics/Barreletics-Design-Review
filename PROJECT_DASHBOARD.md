# Barreletics Blueprint — Project Dashboard

**Last Updated:** 2026-07-18
**Current Milestone:** 2 — Core Experience (QA Complete, Ready for Review)

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

## Milestone 2: Core Experience — 🔵 Ready for Review

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

## Milestone 3: Supporting Experience — ⚪ Not Started

| Deliverable | Status | Dependencies |
|-------------|--------|-------------|
| FAQ Page | ⚪ | Doc 07 approved |
| About Us Page | ⚪ | Docs 01, 02 approved |
| Journal (Blog) Template | ⚪ | Docs 08, 12 approved |
| Sub-Collection Pages | ⚪ | Docs 09, 11 approved |
| Help Scout Integration | ⚪ | Docs 07, 13 approved |
| Tidio AI Setup | ⚪ | Docs 07, 13 approved |

## Milestone 4: Systems — ⚪ Not Started

| Deliverable | Status | Dependencies |
|-------------|--------|-------------|
| Shopify Build Spec (updated) | ⚪ | All foundation docs approved |
| Component Library (Liquid) | ⚪ | Docs 03, 04 approved |
| Dev Handoff Package | ⚪ | All milestones 1–3 complete |
| Analytics / Tracking | ⚪ | Shopify build in progress |

---

## Risks / Decisions Needed

| Risk | Impact | Mitigation |
|------|--------|------------|
| Foundation docs need Architect/Owner review before Milestone 2 starts | Blocks implementation | Prioritize review of docs 01–13 |
| Help Scout content migration scope TBD | May delay Milestone 3 | Define scope in Knowledge Architecture review |
| Photography assets are placeholders in approved pages | Blocks final launch | Set hard deadline for brand photography |

---

## Next Actions

1. **Architect/Owner:** Review PR #2 (`milestone-2-core-experience` → `main`) — QA complete, all critical issues fixed
2. **Builder:** Address deferred minor issues (M-05, M-08, M-09) during deployment
3. **Builder:** Begin Milestone 3 — Supporting Experience (FAQ, About, Journal, sub-collections)
4. **Builder:** Implement variant grid JavaScript filtering when Shopify collection API is connected
