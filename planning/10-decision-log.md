# 10 — Decision Log

---
document: 10 – Decision Log
version: 1.0
status: 🔒 Locked
approved_by: Owner / Architect
approval_date: 2026-07-18
last_modified: 2026-08-08
depends_on: [01, 02, 03, 04, 05, 06, 07, 08, 09]
supersedes: [ADR-01 through ADR-07]
---

## Purpose

Canonical record of all design, brand, and implementation decisions. When a conflict exists between earlier documents and this log, this log reflects the resolved state.

## Resolution Methodology

All ADRs from the prior planning phase (ADR-01 through ADR-07) are resolved per the **recency rule**: the v49 approved design system and July 17 approved pages represent the latest strategic decisions and supersede earlier document values.

---

## Resolved Decisions

### D-001: Color Palette Values
**Resolved:** 2026-07-18 | **Severity:** Critical | **Source ADR:** ADR-01

**Decision:** Adopt v49 palette as canonical. Warm charcoal `#1c1916` for primary text. Warm cream `#f5f2ec` for alternating backgrounds. Body text `#4a4a4a`. Muted `#8a8a8a`.

**Rationale:** The v49 PDP and matured homepage both use the warmer values. Three approved pages (PDP, Home, Collection) all use this palette. The earlier `#050505` / `#f9f9f9` values from the base design system are superseded.

**Impact:** `03-design-system.md` updated. Design System skill already uses v49 values.

---

### D-002: Free Shipping Threshold
**Resolved:** 2026-07-18 | **Severity:** Critical | **Source ADR:** ADR-02

**Decision:** $150. All references to $75 are obsolete and must not appear in any customer-facing content.

**Rationale:** Live site already uses $150. All approved docs confirm $150. The $75 references in older PDP spec drafts were stale copy from a previous threshold.

**Impact:** All docs updated. Knowledge Base (doc 07) and Copy Guide (doc 08) document $150 as canonical.

---

### D-003: Button Border-Radius
**Resolved:** 2026-07-18 | **Severity:** Critical | **Source ADR:** ADR-03

**Decision:** CTA buttons use `6px` border-radius. The earlier system rule of `0px` for all buttons is superseded by v49 approved design.

**Rationale:** v49 PDP uses 6px on CTA and size selector buttons. All three approved pages use this value. The "all buttons square" rule predates v49 and was not carried forward.

**Impact:** `03-design-system.md` documents 6px as canonical CTA radius.

---

### D-004: Eyebrow Letter-Spacing
**Resolved:** 2026-07-18 | **Severity:** High | **Source ADR:** ADR-04

**Decision:** System default is `0.08em / 700 weight`. Component-specific exceptions permitted:
- Manifesto section: `0.18em` (approved exception — larger display context)
- Closing CTA section: `0.06em` (approved exception — compact context)

**Rationale:** v49 PDP and matured homepage CSS tokens both use `0.08em`. The earlier `0.14em` from the Research Bible predates v49. The two component exceptions are documented in their section specs.

**Impact:** `03-design-system.md` updated. Design System skill already uses `0.08em`.

---

### D-005: PDP Text Color
**Resolved:** 2026-07-18 | **Severity:** High | **Source ADR:** ADR-05

**Decision:** Primary text color is `#1c1916` (warm charcoal) everywhere. The earlier `#050505` (cool near-black) is retired.

**Rationale:** v49 PDP uses `#1c1916` in 8+ declarations. Matured homepage overrides to `#1c1916`. Both approved pages use this value. The warmer ink suits the athletic/lifestyle brand positioning. Both pass WCAG AA by wide margin (15.3:1 vs 19.5:1 — both well above 4.5:1 minimum).

**Impact:** `03-design-system.md` updated. The `[data-matured="on"]` override mechanism becomes the default; no toggle needed.

---

### D-006: Review Card Radius
**Resolved:** 2026-07-18 | **Severity:** High | **Source ADR:** ADR-06

**Decision:** Review and justifier cards use `12px` border-radius. The system's earlier "never 12–16px" prohibition is superseded by v49 approved design.

**Rationale:** v49 PDP uses 12px on both review cards and justifier cards. This is the approved design. The contextual radius system in v49 uses: 3px (badges), 6px (buttons), 8px (gallery/video), 12px (content cards), 50% (swatches).

**Impact:** `03-design-system.md` documents the full radius system. `04-component-library.md` specifies 12px for review cards.

---

### D-007: Star Rating Color
**Resolved:** 2026-07-18 | **Severity:** High | **Source ADR:** ADR-07

**Decision:** Star/rating color is `#d4af37` (antique gold) everywhere. The earlier `#fbc02d` (Material Design amber) is retired.

**Rationale:** v49 PDP uses `#d4af37` in star ratings. The darker antique gold is more premium, pairs better with the warm `#1c1916` text, and provides better contrast on white backgrounds (3.0:1 vs 2.1:1). Stars are decorative/iconic; numeric ratings provide accessible value.

**Impact:** `03-design-system.md` updated. Design System skill already uses `#d4af37`.

---

### D-008: Navigation Structure
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Flat primary nav: `Grippy Shoes | Apparel | Collaborations | Journal` + utility `[Help] [Account] [Cart]`. No mega-menu. "Grippy Shoes" (not "Performance Skins") in nav — SEO and mobile conversion priority.

**Rationale:** See `11-navigation-architecture.md` for full rationale.

---

### D-009: Blog → Journal Rename
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** All references to "Blog" become "Journal" in navigation, URLs (`/blogs/journal`), and copy. 301 redirects for any existing `/blogs/blog/` URLs.

---

### D-010: Studio-First Positioning
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Studio use (barre, Pilates, Lagree, Reformer, yoga) is the primary positioning in hero, collection opening, and PDP lead messaging. Outdoor and water use appear ONLY in Outdoor tab and Compare page. Never in primary/hero messaging.

---

### D-011: Sock-Underneath Guidance
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** "Designed to be worn barefoot" is the lead message. Three approved reasons for thin sock underneath: perspiration, hygiene preference, narrow feet/fit customization. This is intentional guidance, not a workaround.

---

### D-012: Longevity Claims
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** Use "from months to years, from dozens of classes to over 1,000" — varies person to person. No specific class count or month guarantees. Customer reports of 3–4 years are cited as examples, not promises.

---

### D-013: Knowledge System Architecture
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** The Product Knowledge Base (doc 07) is the company's Master Knowledge System — not a website-only resource. It feeds all channels: website, Help Scout, Tidio AI, wholesale, studio education, SEO/GEO, and future AI agents. Updates are made once and cascade everywhere.

**Rationale:** See `13-knowledge-architecture.md` for full architecture.

---

### D-014: Product Knowledge Base — Single Source of Truth
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** The Product Knowledge Base (doc 07) is the single source of truth for all factual product claims across all channels. Any factual claim that appears on the website, in Help Scout, Tidio, wholesale materials, or any other channel must originate from doc 07.

---

### D-015: Foundation Documents Supersede Legacy QA Documents
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Foundation documents (01–13) supersede all legacy QA documents. The QA-* files in `planning/archive/` are historical reference only and must not be treated as authoritative for any domain.

---

### D-016: Component Library Is Fully Self-Contained
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** The Component Library (doc 04) contains complete specifications for all 26 components plus additional components. No Foundation document depends on archived documentation for specifications.

---

### D-017: Evidence Classifications Adopted
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** All factual claims carry evidence-level metadata using five canonical types: Engineering Verified, Manufacturing Specification, Customer Testimonial, Brand Positioning, Internal Guidance. See doc 07 Evidence Classification section.

---

### D-018: "Never Degrades" Retired
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** The claim "never degrades" is retired and replaced with specific manufacturing language: "Injection-molded grip won't peel or flake like silicone dots" or "Injection-molded grip maintains full-contact traction throughout the life of the product." Added to `RETIRED_CLAIMS.md`.

---

### D-019: "No Allergic Reaction Risk" Retired
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** The claim "No allergic reaction risk" is retired and replaced with "Skin-safe, non-toxic material." Added to `RETIRED_CLAIMS.md`.

---

### D-020: Foundation Approved for Lock
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** All 13 Foundation documents are complete and internally consistent. Final revision applied (claims governance, materials language, component library completion, evidence classifications, canonical ownership). Priority shifts from planning to implementation pending Architect/Owner approval.

---

### D-021: Milestone 1 Foundation Locked
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** All 13 Foundation documents (01–13) are locked as of 2026-07-18. Architectural changes to any locked document require a new Decision Log entry with Owner/Architect approval before implementation.

**Context:**
- Owner reviewed and approved all 13 Foundation documents
- Priority shifts from planning to implementation
- Milestone 2 (Core Experience) is authorized to begin
- Locked documents serve as canonical specs for all builds

**Impact:** All Foundation docs status changed from 🔵 Ready for Review to 🔒 Locked. Dashboard updated. Milestone 2 authorized.

---
### D-022: GEO Content Sections — Required on All Major Pages
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Every major indexable page includes a GEO section (Homepage, Collection, PDPs, key educational pages). Purpose: AI discoverability, semantic relevance, long-tail search, LLM retrieval. Must be designed as premium editorial content — not keyword blocks or SEO filler.

**Rationale:** Doc 12 requires GEO/SEO content for AI retrieval and long-tail capture. Approved PDP and Collection prototypes both include GEO accordion sections with regional content.

**Impact:** GEO section added to section architecture for all major page types.

---

### D-023: Sticky Add-to-Cart Behavior
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Desktop & Mobile: hidden when native Add to Cart is visible, appears only when purchase module scrolls completely out of view, disappears immediately when it returns. Mobile: compact bar with product thumbnail, price, selected size, Add to Cart button. Must never compete with the primary purchase module.

**Rationale:** Standard PDP UX pattern. Ensures purchase access at all scroll depths without visual noise when native CTA is visible.

**Impact:** `snippets/sticky-atc.liquid` created. Section wrapper `sections/pdp-sticky-atc.liquid` added to PDP template.

---

### D-024: Cart Experience — Drawer + Full Page
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Primary: AJAX Cart Drawer (default on Add to Cart). Secondary: Full Cart Page (for editing quantities, discount codes, large orders, familiarity). Flow: Add to Cart → Cart Drawer → Checkout (with option to go to full cart page).

**Rationale:** Drawer minimizes friction for single-product purchases (dominant use case). Full cart page preserves familiarity for multi-item orders and discount code entry.

**Impact:** `snippets/cart-drawer.liquid` created. Cart drawer integrated into `layout/theme.liquid`. Full cart page remains as `templates/cart.json`.

---

### D-025: Judge.me Reviews — Custom Styled
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Judge.me as data source only — not for rendering. All reviews rendered using Barreletics design tokens (typography, colors, spacing, border radius, icons, card styling, mobile behavior). Review experience must feel native to the Barreletics design system.

**Rationale:** Approved PDP prototype renders reviews with custom typography, gold stars (D-007), 12px card radius (D-006), and Barreletics spacing. Judge.me app blocks would override this styling. Custom rendering ensures brand coherence.

**Impact:** `snippets/review-card.liquid` created. Reviews sections use Judge.me API/metafields for data, custom templates for rendering.

---

### D-026: 50/50 Split Section — Flexible Height for Liquid
**Decided:** 2026-07-18 | **Severity:** Low | **Source:** M-08 (QA Report)

**Decision:** The 50/50 split section uses `min-height: 580px` (not a fixed `height: 420px`) and token-based padding `var(--space-14) var(--space-12)` (not hardcoded `80px 72px`). This is an intentional deviation from Doc 04 Component 5 static prototype specs.

**Rationale:** The Liquid section is reused 6× across three page types with varying content lengths (short eyebrow+title on Homepage, long paragraph on Collection, video placeholder on PDP). A fixed 420px height with overflow:hidden would clip content on mobile and in longer-copy instances. Using `min-height` with token-based padding ensures the section adapts to content while maintaining visual consistency. The static prototype's fixed dimensions were designed for a single content scenario.

**Impact:** No changes needed. The visual result is proportionally consistent with the approved prototype at desktop widths; mobile responsiveness is improved.

---

### D-027: Milestone 2 Core Experience Locked
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** All Shopify build system components, core page sections, variant selection JS, AJAX cart flow, Judge.me integration, GEO sections, and QA fixes approved and locked. Milestone 2 is complete.

**Context:**
- Architect reviewed and approved PR #2 (`milestone-2-core-experience` → `main`)
- 39 files: build spec, design tokens, base CSS, layout, 14 sections, 12 snippets, 3 templates, 2 JS modules
- QA report: 13/13 critical fixes resolved, 7/10 minor fixes resolved, 3 deferred to deployment
- Remaining work is implementation polish and deployment (Milestone 3+)

**Impact:** All Milestone 2 deliverables status changed to 🔒 Locked. Dashboard updated. Milestone 3 (Supporting Experience) authorized to begin.

---

### D-028: Shipping and Returns Split Into Separate Pages
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** Shipping and Returns are separate pages (page.shipping.json, page.returns.json) rather than a combined page. This provides clearer navigation, better SEO targeting, and easier content updates.

**Rationale:** Shipping and returns serve different user intents — pre-purchase confidence vs. post-purchase support. Separate pages allow targeted title tags, meta descriptions, and structured data. Easier to link contextually (FAQ → Returns, PDP → Shipping).

**Impact:** Two page templates planned instead of one combined page. Contact page support links reference separate `/pages/returns` and `/pages/shipping` URLs.

---

### D-029: Grip Comparison as Category Disruption Asset
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Dedicated grip-comparison page designed as a conversion asset. Positions "Barreletics vs Grip Socks" comparison as the primary category-creation landing page for consideration-stage traffic.

**Rationale:** Core brand strategy is category creation — replacing grip socks, not competing within the category. A comparison page captures high-intent search queries ("grip socks vs grippy shoes," "best grip for reformer") and converts them with direct feature/value comparison. Serves as SEO and paid landing page.

**Impact:** Grip comparison page planned as standalone template. Will include structured data for competitive comparison content.

---

### D-030: Header/Footer V2 Pattern for Non-Breaking Updates
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** Navigation and footer updates created as v2 files (header-nav-v2.liquid, footer-v2.liquid) rather than modifying locked M2 components. Theme layout swap during deployment.

**Rationale:** M2 components are locked (D-027). Creating v2 files allows M3 navigation additions (FAQ, About, Journal, Contact in nav/footer) without risking M2 regressions. During deployment, theme-m3.liquid renders the v2 snippets.

**Impact:** No M2 files modified. V2 snippets created when navigation changes are finalized. Theme-m3.liquid will swap render calls during deployment.

---

### D-031: Recently Viewed via localStorage
**Decided:** 2026-07-18 | **Severity:** Medium

**Decision:** Recently viewed products tracked via localStorage (client-side) rather than Shopify customer metafields or cookies. Simpler, no server-side dependency, GDPR-friendly (no PII).

**Rationale:** localStorage persists across sessions without authentication, works for anonymous users (majority of traffic), requires no API calls, and stores no personally identifiable information. Max 8 items tracked, 4 displayed. Client-side rendering from stored JSON avoids additional Liquid/API complexity.

**Impact:** `sections/recently-viewed.liquid` created with full localStorage tracking and client-side rendering. No server-side dependencies. Can be added to any template via JSON.

---

### D-032: Collection Templates Reuse Existing Sections
**Decided:** 2026-07-18 | **Severity:** Low

**Decision:** All sub-collection templates (open-sole, closed-sole, outdoor, new-arrivals, limited-editions, one-offs, gift-cards, sale) reuse existing collection-hero, variant-grid, value-strip, and newsletter sections with different settings. No new sections created for collection pages.

**Rationale:** Section architecture from M2 was designed for reuse. Collection-hero, variant-grid, and newsletter sections accept settings that customize copy, layout, and behavior per collection. Creating duplicate sections would violate DRY and increase maintenance burden.

**Impact:** 5 new sub-collection templates added (collection.new-arrivals.json, collection.limited-editions.json, collection.one-offs.json, collection.gift-cards.json, collection.sale.json) — all JSON-only, referencing existing section types.

---

### D-033: Architecture Consistency Audit — No Foreign Colors
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Form success/error states and comparison highlighting must use brand palette colors, not Material Design green/red (`#e8f5e9`, `#2e7d32`, `#fbe9e7`, `#c62828`). Success states use `var(--bg-alternate)` with `var(--text-primary)`. Error states use `rgba(196, 92, 63, 0.08)` (rust-tinted) with `var(--accent-primary)`. Warranty covered/not-covered uses charcoal/rust distinction. Comparison sock-math uses brand warm cream vs rust-tinted backgrounds.

**Rationale:** The brand palette is warm neutrals + rust accent. Introducing Material Design green/red creates visual dissonance and violates the "no new visual language" principle. The charcoal/rust pairing provides sufficient visual distinction for positive/negative states while maintaining brand coherence.

**Impact:** Fixed in page-ambassador, page-studio-program, page-wholesale, page-warranty, page-grip-comparison, and page-size-guide sections. All 6 files updated.

---

### D-034: JS-Rendered Product Cards Must Match Snippet Classes
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** When rendering product cards client-side via JavaScript (recommendations, recently-viewed), CSS class names must match `product-card.liquid` snippet exactly: `product-card__content` (not `__info`), `product-card__name` (not `__title`). This ensures JS-rendered cards inherit the same styling as Liquid-rendered cards.

**Rationale:** The recommendations section initially used `product-card__info` and `product-card__title` classes which don't exist in `product-card.liquid`'s `<style>` block, causing broken styling for dynamically loaded cards.

**Impact:** `sections/recommendations.liquid` updated to use correct class names.

---

### D-035: Milestone 3 Supporting Experience Locked
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** All supporting pages, collection templates, site experience features, GEO/SEO, and production hardening approved. Milestones 1-3 now constitute the canonical Barreletics architecture. All future work extends without redesigning approved systems.

**Context:**
- All supporting pages built and QA'd (FAQ, About, Contact, Shipping, Returns, Size Guide, Warranty, Wholesale, Ambassador, Studio Program, Grip Comparison, Technology)
- Blog/Journal system complete (listing + article templates)
- Search results page complete
- All sub-collection templates finalized
- Header/Footer V2, breadcrumb, structured data infrastructure complete
- 12/12 critical QA fixes resolved (D-033, D-034)
- BreadcrumbList JSON-LD consolidated to `snippets/breadcrumb.liquid` (single canonical location)
- `theme-m3.liquid` promoted to `theme.liquid` (canonical layout)

**Impact:** Milestones 1-3 locked as canonical architecture. Milestone 4 (Production Readiness) authorized to begin planning. No architectural redesign permitted without new Decision Log entry.

---

### D-036: Milestone 4 Divided into Five Gates (M4A–M4E)
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** Milestone 4 (Production Readiness) is divided into five sequential gates with explicit entry and exit criteria: M4A (Production Assembly), M4B (Integrations), M4C (Validation), M4D (Launch), M4E (Stabilization). No gate may begin until the previous gate's exit criteria are satisfied.

**Rationale:** A single monolithic "Production Readiness" milestone obscured dependencies, blocked parallel planning, and made it impossible to verify progress. Sequential gates with defined criteria ensure each phase is complete before the next begins and create natural review checkpoints for Owner and Builder.

**Impact:** `MILESTONES-4-5-6-ROADMAP.md` restructured. `PROJECT_DASHBOARD.md` updated to reflect sub-gates.

---

### D-037: GEO Expansion Is Data-Gated, Not Volume-Driven
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Location pages (city, state, international) are authorized ONLY when supported by verified search demand, customer/order concentration data, studio density or active partners, unique local content, and a clear conversion path. No batch-creation of location pages for SEO volume. Each page requires individual Owner approval with supporting data.

**Rationale:** Thin, repetitive location pages provide no user value, risk Google thin-content penalties, and waste build effort. Data-gated expansion ensures every location page has genuine demand and differentiated content.

**Impact:** Milestone 5 §5.8 restructured as "Data-Gated GEO Expansion Program." Automatic 20-city, state-hub, and international page plans removed.

---

### D-038: Milestone 5 Scoped as Finite v1
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Milestone 5 is scoped as a finite v1 deliverable, not an ongoing effort. v1 completion requires: reusable landing-page framework, one live campaign, one One-Offs drop workflow, initial Journal taxonomy, initial studio/wholesale resources, CRO baseline with experiment backlog, and GEO qualification framework. Continued campaigns, content publishing, experimentation, and market expansion move to "Post-v1 Operations."

**Rationale:** An open-ended milestone with "Large (ongoing)" effort cannot be declared complete, which blocks Milestone 6 and v1.0 declaration. Finite scope defines a clear finish line while preserving ongoing operational work as a separate concern.

**Impact:** Milestone 5 estimated effort changed from "Large (ongoing)" to "Medium (finite v1 scope)." Post-v1 Operations section added.

---

### D-039: All M4 Tasks Assigned Builder/Owner/Joint Responsibility
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Every Milestone 4 task carries an explicit responsibility label: Builder, Owner, Joint, or External Provider. Builder cannot independently complete payment, tax, account-access, or business-policy decisions. Access-dependent work is marked with "Owner credentials required," "Builder can prepare," or "Builder cannot complete without access."

**Rationale:** Previous roadmap implied Builder could independently complete all tasks, including business decisions (payment/tax configuration, policy approvals, pricing) that require Owner authority. Clear labels prevent blocked work, wasted effort, and unauthorized decisions.

**Impact:** All M4 task tables include Responsibility column. Conditional integrations section created for unconfirmed tools.

---

### D-040: Policy Freeze Gate Required Before Production QA
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** A Policy Freeze Gate is an entry criterion for M4C (Validation). Owner must sign off on: shipping terms, return terms, warranty language, pricing, discounts/promo codes, free-shipping threshold ($150), size guidance, product claims, wholesale terms, Studio Program terms, and Ambassador terms before QA begins. Builder must not treat draft business rules as production-approved. Post-freeze changes require a new Decision Log entry.

**Rationale:** QA against draft policies wastes cycles — any policy change after QA invalidates test results and requires re-testing. Freezing policies before QA ensures the validated state matches what ships to production.

**Impact:** Policy Freeze Gate added as M4C entry criterion in `MILESTONES-4-5-6-ROADMAP.md` §8.

---

### D-041: Homepage Hero — Two Concepts for Side-by-Side Comparison
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Homepage hero is NOT locked. Two concepts built for Owner side-by-side comparison before final lock. Current concept ("The Pilates Sock Era Is Over" / "Studio Workouts & Footwear Will Never Be The Same") preserved in `hero.liquid`. Alternative concept ("Think Outside the Sock." / "No Socks. Just Grip." / "Meet the Performance Skin.") built in `hero-alt.liquid`. Same layout, design tokens, and structure — only copy/messaging differs.

**Rationale:** Hero headline is the highest-impact brand decision. Owner requested two directions to compare before committing. Building both as functional sections enables real preview in the Theme Customizer rather than abstract copy review.

**Impact:** `hero-alt.liquid` created. Content inventory updated to flag hero as "TWO concepts pending Owner comparison — do not lock." Neither concept is finalized until Owner makes selection.

---

### D-042: Partner Programs Consolidated Into Single Page — SUPERSEDED 2026-08-08 (see D-048)
**Decided:** 2026-07-18 | **Severity:** High

**Status:** Superseded by **D-048** (Owner direction 2026-08-08). Original text preserved below as history — do not implement. Three dedicated partner pages plus a `/pages/partners` routing hub is the current state.

**Decision:** Three separate partner pages (Wholesale, Studio Program, Ambassador) consolidated into a single `/pages/partners` page with three sections and a unified inquiry form. Individual page templates (`page.wholesale.json`, `page.studio-program.json`, `page.ambassador.json`) are superseded. Wholesale/Studio/Ambassador terms (pricing, minimums, commission structures) remain internal — never displayed publicly. Ambassador section is architected with a clear integration point for a future affiliate platform. No affiliate/commission functionality built.

**Rationale:** Three separate pages with overlapping structure and minimal content created unnecessary navigation complexity and maintenance burden. A single page with anchor-linked sections provides a cleaner user experience and simplifies the inquiry flow. Internal pricing (50% off MSRP, 10-pair minimum) must never appear on public pages.

**Impact:** `page-partners.liquid` and `page.partners.json` created. Redirect map updated: old `/pages/wholesale`, `/pages/ambassador`, `/pages/studio-program` all 301 to `/pages/partners`. Content inventory and forms inventory updated. Navigation config updated.

---

### D-043: Collections Created Only When Products Require Them
**Decided:** 2026-07-18 | **Severity:** High

**Decision:** Shopify collections are created in admin ONLY when products/merchandising require them. Collection TEMPLATES exist (from M3) and are ready to use, but the actual Shopify collections should not be batch-created until there are products to populate them. No unnecessary collection proliferation.

**Rationale:** Creating empty collections degrades the storefront experience (empty pages) and creates false navigation expectations. Templates are the reusable asset; the Shopify admin collections are the content decision. Content follows merchandising readiness, not template availability.

**Impact:** Navigation config updated to mark planned collections as "Create only when products/merchandising require it." Instruction to batch-create all 13 collections removed.

---

### D-044: M4A Production Assembly Locked
**Decided:** 2026-07-18 | **Severity:** Critical

**Decision:** M4A Production Assembly gate is complete and locked. All deliverables verified: theme consolidation, settings schema/data, locale strings, missing templates, planning documentation (content inventory, navigation config, metafield spec, asset inventory, redirect map, pre-deployment baseline), hero alt concept (D-041), consolidated partners page (D-042). QA passed all 11 validation categories. PR #4 merged to main.

**Context:**
- 29 files: 19 added, 3 modified, 2 deleted (v2 consolidation)
- 16/16 JSON files validated
- 4/4 Liquid files verified (syntax, schema, references)
- 1 defect found and fixed (redirect map stale targets)
- No M1-M3 architecture conflicts
- No unauthorized business-policy decisions

**Impact:** M4A status changed to 🔒 Locked. M4B (Integrations) authorized to begin. Dashboard updated.

---

### D-045: Production Tracking Strategy
**Decided:** 2026-07-19 | **Severity:** Critical

**Decision:** Shopify native channel integrations are the preferred production implementation for GA4 and Meta tracking:
- **GA4:** Shopify Google & YouTube channel is the preferred production implementation
- **Meta Pixel + CAPI:** Shopify Meta & Instagram channel is the preferred production implementation
- Theme-level GA4 and Meta snippets (`snippets/analytics-head.liquid`, `snippets/meta-pixel.liquid`) exist as fallback/custom implementation ONLY
- Theme-level GA4 and Meta tracking MUST remain disabled (IDs left blank in Theme Settings) whenever Shopify native integrations are active
- Enabling both simultaneously creates duplicate tracking and corrupts analytics data
- Integrations NOT natively handled by Shopify remain theme-managed: Microsoft Clarity, Help Scout, Tidio, Pinterest Tag, Google Search Console verification
- This is a permanent architectural decision — future developers must not enable both sources

**Rationale:** Shopify's native channels provide server-side event delivery (CAPI), automatic deduplication, enhanced match quality, and zero-maintenance updates. Theme-level snippets duplicate these events browser-side, causing inflated metrics, broken attribution, and corrupted conversion data. The theme snippets exist for scenarios where native channels are unavailable or insufficient (custom events, non-standard configurations).

**Impact:** `m4b-integration-plan.md`, `m4b-environment-config.md`, and `m4b-verification-checklist.md` updated to reference this decision. All future integration work must verify native channel status before enabling theme-level tracking.

**Status:** Approved

---

### D-046: M4B Integrations Locked
**Decided:** 2026-07-19 | **Severity:** Critical

**Decision:** M4B Integrations gate is complete and locked. All integration snippets, configuration system, Help Scout alignment, Tidio knowledge base, and verification checklist are complete. Credential insertion and platform activation deferred to M4D Launch.

**Context:**
- All tracking snippets built with graceful degradation (GA4, Meta Pixel, Pinterest, Clarity, Help Scout Beacon, Tidio)
- Settings schema extended with Tracking & Integrations section
- Theme.liquid integration includes added
- Duplicate prevention documented (D-045)
- Help Scout saved reply content prepared (`m4b-helpscout-alignment.md`)
- Tidio knowledge base content prepared (`m4b-tidio-knowledge-base.md`)
- Verification checklist ready for post-credential activation (`m4b-verification-checklist.md`)
- Owner actions documented: paste IDs, configure apps, run verification

**Impact:** M4B status changed to 🔒 Locked. M4C (Validation) authorized to begin planning. Dashboard updated.

**Status:** Approved

---

### D-047: M4C Validation Gate Locked
**Decided:** 2026-07-19 | **Severity:** Critical

**Decision:** M4C Validation gate is complete and locked. 130 validations executed: 109 pass, 6 failures fixed and re-verified, 15 N/A (deferred to M4D for runtime evidence on deployed preview). Zero unresolved failures. Evidence-first validation framework established.

**Context:**
- All code-verifiable validations pass
- 6 remediated failures: NAV-004 (mobile utility menu), HOME-003 (value strip), HOME-004/COL-004 (variant grid tabs), HOME-010 (hardcoded hex), CART-010 (focus trap)
- 15 N/A items require deployed Shopify preview or device testing — methods documented for M4D
- No Owner blockers remaining at code level
- Advisory findings (non-blocking): organization schema orphan, fifty-fifty bg_color setting, mobile menu focus trap

**Impact:** M4C status changed to 🔒 Locked. M4D (Launch) authorized to begin. Dashboard updated.

**Status:** Approved

---

### D-048: Three Dedicated Partner Pages Plus a Routing Hub — supersedes D-042
**Decided:** 2026-08-08 | **Severity:** High

**Decision:** Wholesale, Studio Program, and Ambassador each get a dedicated page with its own intake form: `/pages/wholesale`, `/pages/studio-program`, `/pages/ambassador`. `/pages/partners` is retained as a routing hub — three cards linking to the program pages, plus a general-inquiry fallback form. This reverses D-042's consolidation onto a single page. Program terms (commission %, discounts, thresholds) remain Theme Editor settings and internal pricing is never displayed publicly, unchanged from D-042.

**Rationale:** The three audiences ask genuinely different qualification questions — a studio needs class volume and location, a wholesale buyer needs order volume and resale terms, an ambassador needs audience and content channels. One merged form cannot serve all three without either asking every applicant irrelevant questions or collecting too little to qualify anyone. Owner direction 2026-08-08 governs; D-042's maintenance-burden rationale is outweighed by intake quality.

**Impact:** `templates/page.ambassador.json`, `page.studio-program.json`, `page.wholesale.json`, and `page.partners.json` built and mobile-QA'd (see `planning/partner-programs.md` §5, QA output in `planning/partner-pages-qa/`). The three folding 301s (`/pages/wholesale`, `/pages/ambassador`, `/pages/studio-program` → `/pages/partners`) are **retired** in `planning/m4a-redirect-map.md` — they would have made the new pages unreachable. `planning/page-inventory-decisions.md` Part 2 updated from FOLD to CREATE for the three program templates.

**Downstream doc sweep — COMPLETE 2026-08-08.** The files listed here as "still stale and owned by other agents" have since been updated forward, each cross-referencing D-048 and preserving the D-042 wording as struck history: `planning/m4a-content-inventory.md` (page rows, owner-approval row, forms inventory — the "Partner inquiry (unified)" row is now four rows), `planning/m4a-navigation-config.md` (handle map + Admin note 6), `docs/03-section-library.md` (`page-partners.liquid` entry), `specs/frozen/{wholesale,ambassador,studio}.md` (R-01/R-02 HOLD marked superseded, not deleted), `specs/frozen/navigation.md` (authority re-cited to D-048; the "Partners not in primary nav" call itself is unchanged), `specs/implementation-maps/{wholesale,ambassador,studio}.md` (were titled "deprecated standalone"), `planning/m4-section-library-CONTRACT.md` (DELETE-after-decompose rows annotated as a future refactor, not deprecation), `PROJECT_DASHBOARD.md`, `planning/partner-programs.md` (§4.5 item 7 + architecture note), and `planning/m4b-helpscout-alignment.md` §7 (saved reply now links the three program pages).

Deliberately unchanged: the `/pages/become-an-affiliate` and `/pages/wholesale-calculator` → `/pages/partners` 301s (correct — they point at the hub); `specs/frozen/homepage.md` / `collections.md` references to "D-042 partners page" (those concern holding Free People / Coperni collab sprawl, a different sense of "partner"); D-044's M4A gate record above (historical); `backups/**` and `planning/archive/**` snapshots.

**Status:** Approved — Owner letter 2026-08-08

---

### D-049: The Refined v19 PDP Spine Serves Closed Sole; Open Sole Moves to Its Own Template
**Decided:** 2026-08-08 | **Severity:** High

**Decision:** `shopify-build/templates/product.json` — the refined, locked v19 spine — now serves the **Closed Sole** product (`best-reformer-pilates-legree-workout-shoes`). **Open Sole** (`studio-performance-skin-footwear`) moves to a new variant template, `shopify-build/templates/product.open-sole.json`, created by renaming the day-old `product.closed-sole.json` and rewriting its copy from Closed Sole to Open Sole. `product.closed-sole.json` no longer exists. `product.outdoor.json` is untouched. The buy-box lede **"Secure in every hold. / No sliding. No resets."** is now the title line on **both** sole pages.

**Rationale:** Owner direction 2026-08-08: *"no make the existing pdp page the closed sole and change the open sole. we probably want to keep secure in every hold on both for the title?"* Closed Sole is the higher-inventory, higher-colorway SKU and the one the refined page's photography and reformer/Lagree GEO copy already suited. The shared lede is approved inventory (Problem/Solution) and reads correctly for either coverage style, so nothing sole-specific is claimed in the headline.

**Scope guard — this is a product-identity change, not a spine change.** All 17 sections in `product.json` and their order are byte-verified unchanged against the pre-edit capture: `pdp-buy-box` → `value-strip` → `pdp-features` → `disciplines` → `fifty-fifty-sock-era` → `variant-grid` → `fifty-fifty-lifestyle` → `fullbleed-statement` → `pdp-sock-math` → `fullbleed-lifestyle` → `fifty-fifty-commit` → `social-proof` → `fifty-fifty-numbers` → `guarantee-band` → `home-juicer` → `collection-faq` → `pdp-sticky-atc`. Only four fields changed in `product.json`: the sole badge label, the badge colour, and two FAQ answers that named a sole using the discipline split retired by P-003.

**Impact:** `product.json` SHA-256 moves from `00a209a5abf9bf9c258d7cb422cb055f7d95da7a0f11f7f7cb0294afa0b847a5` to `9097409f46f4ef7e80a675b50d1072ca072e2a70ff2854fe97c78eee0b9e5b2b` — authorised by this letter. Registries updated forward, prior wording preserved as dated history: `planning/m4-section-freeze.md`, `planning/PDP-WORKING-ENTRY.md`, `planning/pdp-variants-qa/README.md`. QA harness `planning/pdp-variants-qa/build.py` re-pointed and previews relabelled. `.cursor/rules/pdp-hub-lock.mdc` still describes `product.json` as the PDP spine, which remains true — it names no product, so it needs no edit; flagged for the owner rather than changed.

**Admin follow-up (not a repo change):** theme template assignment is per-product in Shopify Admin → Product → Online store → Theme template. Open Sole must be set to `product.open-sole`; Closed Sole stays on **Default product**. The old `product.closed-sole` template name is gone.

**Copy sourcing:** every replacement line traces to the approved slogan inventory (`barreletics-brand-copy` / `barreletics-slogan-engine`), the P-003 sole letter (`manychat-kb/02-open-vs-closed-sole.md`), `docs/09-PRODUCT-KNOWLEDGE.md` Product 2, or the locked v19 spine. Nothing was invented. Per-line source tables live in `planning/pdp-variants-qa/README.md`.

**Status:** Approved — Owner direction 2026-08-08

---

### D-050: Sole Description Language Fixed as HARD Copy Law — "Fully Enclosed" Banned
**Decided:** 2026-08-08 | **Severity:** High

**Decision:** The Closed Sole is described as **"Heel and foot fully covered."** and nothing else. The phrases **"fully enclosed," "fully-enclosed," "enclosed heel," "sleek, fully enclosed feel,"** and any construction calling the Closed Sole *enclosed* are banned from all customer-facing copy. The sanctioned wording, from the P-003 letter, is the only approved way to describe the sole difference:

- **Closed Sole:** "Heel and foot fully covered."
- **Open Sole:** "Heel exposed, mid-foot breathing hole. More grounded, barefoot feel. Natural toe splay."
- **Both:** "Both perform identically — same grip, same stability."
- **Choosing:** "Choice is preference and feel only."

This entry also re-asserts the **discipline split retired 2026-08-02 under P-003**: never write "Open = barre/yoga, Closed = reformer/Lagree/Megaformer" or any variant assigning a discipline to a sole. Both soles perform identically across all disciplines.

**Rationale:** Owner direction 2026-08-08, the third correction on the same phrase in one day — *"quit saying fully enclosed heel - dont make shit up"* → *"quit fucking saying fully enclosed this is not how we describe it. Fucking make a rule and stop drifting."* The phrase kept reappearing because it was embedded in the approved knowledge base and re-copied by every new agent. This is how the brand describes its own product; drifting invents product claims the Owner has not approved. Cross-references **P-003** (approved sole wording, `manychat-kb/02-open-vs-closed-sole.md`) and **P-013** (`docs/10-DECISIONS.md`, "fully enclosed" retired).

**Impact:** New rule `.cursor/rules/sole-description-language.mdc` (alwaysApply) establishes the ban, the approved wording, the discipline-split prohibition, scope, and exceptions. Cross-referenced from `.cursor/rules/anti-revert-fail-closed.mdc` and `.cursor/rules/section-freeze-no-drift.mdc`. The `barreletics-brand-copy` skill — which auto-invokes on all Barreletics copy work — carries the ban in its anti-patterns list. Scope covers PDP/collection/page templates, section Liquid **and their schema defaults**, mocks in `docs/`, `planning/`, `specs/`, `manychat-kb/`, email, ads, and the ManyChat KB. `docs/09-PRODUCT-KNOWLEDGE.md` and `manychat-kb/02-open-vs-closed-sole.md` are named as the SOURCE documents that must never carry banned phrasing. `backups/**`, `archive/**`, and `planning/archive/**` are frozen snapshots and are excluded.

**Status:** Approved — Owner letter 2026-08-08

---

## ADR Archive

The original ADR documents (ADR-01 through ADR-07) are preserved in `planning/` for historical reference. Their UNRESOLVED status is now superseded by the decisions above.

---

**Cross-references:**
- Design system tokens → `03-design-system.md`
- Knowledge architecture → `13-knowledge-architecture.md`
- Navigation rationale → `11-navigation-architecture.md`
- Copy rules → `08-copy-guide.md`
