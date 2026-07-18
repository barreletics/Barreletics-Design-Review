# 10 — Decision Log

---
document: 10 – Decision Log
version: 1.0
status: 🔒 Locked
approved_by: Owner / Architect
approval_date: 2026-07-18
last_modified: 2026-07-18
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

## ADR Archive

The original ADR documents (ADR-01 through ADR-07) are preserved in `planning/` for historical reference. Their UNRESOLVED status is now superseded by the decisions above.

---

**Cross-references:**
- Design system tokens → `03-design-system.md`
- Knowledge architecture → `13-knowledge-architecture.md`
- Navigation rationale → `11-navigation-architecture.md`
- Copy rules → `08-copy-guide.md`
