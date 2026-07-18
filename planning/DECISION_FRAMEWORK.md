# Decision Framework

**Status:** 🔵 Ready for Review
**Last Updated:** 2026-07-18

---

## Purpose

Documents when the Builder proceeds autonomously vs escalates to the Architect/Owner. Clear boundaries prevent bottlenecks while protecting strategic decisions.

## Builder Proceeds Autonomously When:

- **Follows an approved foundation doc** — Implementing what's already documented in docs 01–13
- **Applies the Design System** — Using tokens, components, and patterns from doc 03 and the Design System skill
- **Follows Navigation Architecture** — Building nav, footer, breadcrumbs per doc 11
- **Follows SEO/GEO Standards** — Implementing structured data, meta tags, GEO content per doc 12
- **Expands approved Knowledge Base copy** — Using doc 07 content in downstream systems (Help Scout, Tidio, website) per doc 13's adaptation rules
- **Improves implementation without changing strategy** — Performance optimization, accessibility fixes, responsive refinements, code quality
- **Resolves technical implementation details** — CSS specifics, Liquid template structure, JS architecture, Shopify section schema
- **Creates content from approved patterns** — GEO sections using verified move names, FAQ answers from Knowledge Base, journal articles using Copy Guide voice
- **Fixes bugs or inconsistencies** — Correcting something that doesn't match an approved doc

## Builder Escalates When:

- **Brand positioning changes** — Any shift in the category creation strategy, brand voice, or competitive framing
- **Strategic business decision required** — Pricing changes, policy changes, new product launches, partnership decisions
- **Meaningful tradeoff between conversion/SEO/UX/branding** — When optimizing one dimension meaningfully compromises another
- **Page architecture fundamentally changes** — Adding/removing/reordering sections in an approved page architecture
- **New messaging needed not in approved docs** — Claims, taglines, or product descriptions that don't exist in docs 02, 07, or 08
- **Conflicts between approved docs** — When two foundation documents give contradictory guidance
- **Milestone complete for review** — Every milestone gate requires Architect/Owner review before proceeding
- **Knowledge Base policy update** — Changes to returns, warranty, shipping, pricing, or any policy in doc 07
- **New channel integration** — Adding a downstream system to the Knowledge Architecture (doc 13)
- **Navigation structure changes** — Adding/removing/renaming primary or secondary nav items

## Decision Record Requirements

All escalated decisions must be logged in `10-decision-log.md` with:
- Decision ID (D-###)
- Date resolved
- Decision statement
- Rationale (why this choice, not alternatives)
- Impact (which documents/systems are affected)

## Recency Rule

When conflicts exist between earlier documents and later strategic decisions:
1. Later decision wins
2. Preserve what's still accurate in the earlier document
3. Remove what's outdated
4. Log the resolution in `10-decision-log.md`

The Knowledge Base (doc 07) is the canonical source for product facts. If a downstream system contradicts the Knowledge Base, the Knowledge Base is correct and the downstream system must be updated.

## Review Gates

| Gate | Trigger | Reviewer |
|------|---------|----------|
| Foundation complete | All 13 docs at 🔵 | Architect/Owner |
| Page build complete | Each Tier 2 page built | Architect/Owner |
| Integration complete | Help Scout / Tidio configured | Architect/Owner |
| Pre-launch | All tiers complete | Architect/Owner |
| Post-launch (48h) | Launch monitoring period | Architect/Owner |

---

## Canonical Ownership

Each Foundation document is the single authoritative source for its domain. If two documents ever disagree, the owner document listed here is authoritative for that domain.

| Domain | Owner Document |
|--------|---------------|
| Brand | 01 – Brand North Star |
| Brand System & Guardrails | 02 – Brand System |
| Design Tokens & Visual System | 03 – Design System |
| Components | 04 – Component Library |
| PDP | 05 – PDP Architecture |
| Homepage | 06 – Homepage Architecture |
| Product Knowledge & Facts | 07 – Product Knowledge Base |
| Copy & Messaging | 08 – Copy Guide |
| Collection Pages | 09 – Collection Architecture |
| Decisions | 10 – Decision Log |
| Navigation | 11 – Navigation Architecture |
| SEO & GEO | 12 – SEO & GEO Standards |
| Knowledge Flow & AI Governance | 13 – Knowledge Architecture |

---

**Cross-references:**
- Foundation docs → `planning/01-*.md` through `planning/13-*.md`
- Decision log → `planning/10-decision-log.md`
- Knowledge governance → `planning/13-knowledge-architecture.md`
- Master roadmap → `planning/MASTER_ROADMAP.md`
