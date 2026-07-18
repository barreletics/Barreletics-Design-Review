# Barreletics Blueprint — Master Roadmap

**Status:** 🔵 Ready for Review
**Last Updated:** 2026-07-18

---

## Tier 1: Foundation

**Purpose:** Establish the canonical reference system that governs all downstream work.

| # | Deliverable | Dependencies | Acceptance Criteria | Authority | Status |
|---|-------------|-------------|--------------------|-----------| -------|
| 01 | Brand North Star | None | Vision, mission, values, category creation principle documented. Consistent with 02. | Architect/Owner | 🔵 |
| 02 | Brand System | 01 | Category creation strategy, voice, slogans, power phrases, naming rules. Operating system framing included. | Architect/Owner | 🔵 |
| 03 | Design System | None | Pointer to skill + resolved tokens, ADR resolutions documented, all conflicts resolved per recency rule. | Architect/Owner | 🔵 |
| 04 | Component Library | 03 | All components specified: purpose, inputs, states, variants, responsive, accessibility, Shopify notes. | Architect/Owner | 🔵 |
| 05 | PDP Architecture | 03, 04 | Section-by-section spec matching approved PDP page. Structured data, meta tags, content strategy. | Architect/Owner | 🔵 |
| 06 | Homepage Architecture | 03, 04 | Section-by-section spec matching approved Home page. Narrative arc documented. | Architect/Owner | 🔵 |
| 07 | Product Knowledge Base | 01, 02 | Master Knowledge System: 16 topics, each with canonical answer, quotes, surface map, abbreviated version. Company-wide scope. | Architect/Owner | 🔵 |
| 08 | Copy Guide | 02, 07 | Hard rules, voice, channel-specific patterns, anti-patterns. All copy sources from Knowledge Base. | Architect/Owner | 🔵 |
| 09 | Collection Architecture | 03, 04, 12 | Pillar page strategy, section architecture, dual shopping/SEO role. | Architect/Owner | 🔵 |
| 10 | Decision Log | All ADRs | All 7 ADRs resolved. Numbered decisions with rationale and impact. | Architect/Owner | 🔵 |
| 11 | Navigation Architecture | 09, 12 | Primary nav, sub-nav, mobile, footer, announcement strip, future scaling. | Architect/Owner | 🔵 |
| 12 | SEO & GEO Standards | 07, 09 | Keyword targets, pillar strategy, structured data, GEO content, AI search optimization. | Architect/Owner | 🔵 |
| 13 | Knowledge Architecture | 07 | Flow diagram, downstream system requirements, governance, update cascade, conflict resolution. | Architect/Owner | 🔵 |
| — | Decision Framework | All | Builder autonomy rules, escalation triggers. | Architect/Owner | 🔵 |
| — | Infrastructure Recommendations | All | Skills, templates, standards, repo structure. | Builder | 🔵 |

---

## Tier 2: Core Experience

**Purpose:** Build the primary customer journey pages in Shopify.

| # | Deliverable | Dependencies | Acceptance Criteria | Authority | Status |
|---|-------------|-------------|--------------------|-----------| -------|
| 2.1 | Shopify Token File | 03 approved | All design tokens as CSS custom properties. Zero hardcoded values. | Builder | ⚪ |
| 2.2 | Global Header | 04, 11 approved | Announcement ticker, nav, logo, cart, mobile hamburger, sticky behavior. All breakpoints. | Builder | ⚪ |
| 2.3 | Global Footer | 04, 11 approved | Link columns, newsletter, social, copyright. All breakpoints. | Builder | ⚪ |
| 2.4 | Homepage Build | 06, 2.1–2.3 | All sections per doc 06. Pixel-match approved HTML. Performance: LCP <2.5s. | Builder → Architect review | ⚪ |
| 2.5 | PDP Build | 05, 2.1–2.3 | Gallery, buy box, variants, ATC, accordion, reviews, sock math, FAQ, newsletter, sticky ATC. | Builder → Architect review | ⚪ |
| 2.6 | Collection / Pillar Build | 09, 12, 2.1–2.3 | Pillar content + product grid + filters + GEO sections. SEO requirements met. | Builder → Architect review | ⚪ |
| 2.7 | Compare Page | 07, 09 | Open Sole vs Closed Sole comparison. Structured data. Internal linking. | Builder | ⚪ |

---

## Tier 3: Supporting Experience

**Purpose:** Build secondary pages and integrate external systems.

| # | Deliverable | Dependencies | Acceptance Criteria | Authority | Status |
|---|-------------|-------------|--------------------|-----------| -------|
| 3.1 | FAQ Page | 07 approved | Full Q&A from Knowledge Base. Category-grouped. Search/filter. FAQ schema. | Builder | ⚪ |
| 3.2 | About Us Page | 01, 02 | Founder story, brand values, manifesto. | Builder | ⚪ |
| 3.3 | Journal Template | 08, 12 | Article template (6 variants). Blog index. Category filtering. | Builder | ⚪ |
| 3.4 | Sub-Collection Pages | 09, 11 | Open Sole, Closed Sole, Outdoor. Filtered grids + pillar content. | Builder | ⚪ |
| 3.5 | Help Scout Setup | 07, 13 | Saved replies, macros, templates sourced from Knowledge Base. Category creation in all replies. | Builder → Architect review | ⚪ |
| 3.6 | Tidio AI Setup | 07, 13 | Q&A pairs from Knowledge Base. Intent routing. Human handoff rules. | Builder → Architect review | ⚪ |
| 3.7 | Static Pages | 07 | Contact, Shipping & Returns, Warranty, Privacy, Terms. | Builder | ⚪ |
| 3.8 | 404 + Cart + Search | 04 | Branded 404, cart page (fallback), predictive search. | Builder | ⚪ |

---

## Tier 4: Systems

**Purpose:** Implementation infrastructure, dev handoff, and launch preparation.

| # | Deliverable | Dependencies | Acceptance Criteria | Authority | Status |
|---|-------------|-------------|--------------------|-----------| -------|
| 4.1 | Updated Shopify Build Spec | All Tier 1 | Build spec updated to reflect all foundation decisions. Section map, snippet map, template map current. | Builder | ⚪ |
| 4.2 | Component Library (Liquid) | 04, 2.1 | Reusable Liquid sections and snippets for all 26 components. | Builder | ⚪ |
| 4.3 | Analytics Implementation | — | GA4 events, enhanced ecommerce, UTM tracking. Property 300437005. | Builder | ⚪ |
| 4.4 | Integration Setup | — | Judge.me, Klaviyo, Shop Pay, Juicer configured and styled. | Builder | ⚪ |
| 4.5 | Performance Optimization | 2.4–2.7 | LCP <2.5s, CLS <0.1, INP <200ms. Image optimization, critical CSS, JS budget <30KB. | Builder | ⚪ |
| 4.6 | Accessibility Audit | 2.4–2.7 | WCAG 2.1 AA. Zero critical violations. Keyboard nav. Screen reader tested. | Builder | ⚪ |
| 4.7 | Migration Plan | All | Content migration checklist, URL redirect map, rollback plan. | Builder → Architect review | ⚪ |
| 4.8 | Dev Handoff Package | All | Complete package for any developer to pick up the build. | Builder | ⚪ |
| 4.9 | Launch Checklist | All | DNS, SSL, theme publish, app activation, analytics verification, stakeholder sign-off. | Architect/Owner | ⚪ |

---

## Critical Path

```
Tier 1 (Foundation docs approved)
  → Tier 2.1 (Tokens)
    → Tier 2.2–2.3 (Global components)
      → Tier 2.4–2.6 (Core pages) [parallel]
        → Tier 3 (Supporting pages) [parallel with late Tier 2]
          → Tier 4 (Systems + launch)
```

Tier 1 approval is the gate. Nothing in Tier 2+ should begin until critical-path foundation docs (03, 04, 05, 06, 07) are approved.

---

**Cross-references:**
- Foundation docs → `planning/01-*.md` through `planning/13-*.md`
- Engineering backlog (128 tasks) → `planning/engineering-backlog.md`
- Shopify build spec → `planning/shopify-build-specification.md`
- Decision framework → `planning/DECISION_FRAMEWORK.md`
