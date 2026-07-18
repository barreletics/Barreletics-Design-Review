# 13 — Knowledge Architecture

**Status:** 🔵 Ready for Review
**Last Updated:** 2026-07-18

---

## Purpose

This document defines how knowledge flows throughout the company. The Master Product Knowledge Base (`07-product-knowledge-base.md`) is the canonical source. Every downstream system consumes and formats that knowledge for its specific context.

**We're not simply building a better website. We're building the operating system for the Barreletics brand.**

## Architecture

```
                Master Product Knowledge Base (07)
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
      Website            Help Scout           Tidio AI
      │                   │                   │
      ├── PDP             ├── Saved Replies    ├── Q&A Pairs
      ├── Collection      ├── Email Templates  ├── Intent Routing
      ├── FAQ Page        ├── Macros           └── Handoff Rules
      ├── Compare Page    ├── Workflows
      ├── Pillar Pages    └── Canned Responses
      └── Journal
          │                   │                   │
      ┌───┴───────────────────┴───────────────────┴───┐
      │                                               │
  SEO / GEO                                    Wholesale / Studio
  │                                            │
  ├── Pillar Content                           ├── Pitch Decks
  ├── Structured Data                          ├── Education Materials
  ├── GEO Sections                             ├── Studio Training
  └── AI Search Optimization                   └── Retail Education
      │                                               │
      └───────────────────┬───────────────────────────┘
                          │
                  Future AI Systems
                  │
                  ├── AI Customer Agents
                  ├── AI Content Generation
                  └── Future Product Launches
```

## The Single Source Rule

A product update should only need to be made **ONCE** in the Knowledge Base. That single update then cascades into every customer-facing and internal system. No drift. No conflicting answers across channels.

**Example flow:** Shipping threshold changes from $150 to $175.
1. Update `07-product-knowledge-base.md` → Topic 15: Shipping
2. Website: PDP trust row, announcement ticker, cart drawer progress bar — all pull from the same truth
3. Help Scout: shipping macro and saved replies reference the Knowledge Base value
4. Tidio AI: shipping Q&A pair updated
5. Wholesale materials: updated at next refresh
6. No one has to remember to update 6 different systems independently

## Downstream System Requirements

### Website
**Format:** HTML-friendly structured content
**Consumes:**
- PDP: accordion content (Description, Size & Fit, Care, Returns), FAQ section, Sock Math data
- Collection: abbreviated answers, pillar page educational content, GEO sections
- FAQ page: full Q&A pairs with schema markup
- Compare page: Open Sole vs Closed Sole canonical comparison
- Journal: educational content, discipline-specific moves

**Update cadence:** Immediate — Knowledge Base changes should be reflected in next deploy or theme update.

### Help Scout
**Format:** Reply-ready copy — warm, efficient, precise. First-person brand voice.
**Consumes:**
- Saved replies: templated responses for common inquiries (sizing, returns, care, shipping)
- Email templates: policy language, product descriptions
- Macros: one-click responses with Knowledge Base facts
- Workflows: automated routing based on inquiry type

**Content adaptation rules:**
- Knowledge Base canonical answers are rewritten for conversational email tone
- Policy language is precise — no hedging, no "I think"
- Category creation embedded naturally: "Performance Skins are designed to..." not "our grip socks..."
- Always link to relevant FAQ/product page for customer self-service

**Update cadence:** Quarterly review, or immediately when policies change.

### Tidio AI (Chatbot)
**Format:** Q&A pairs — question + concise answer + optional expansion
**Consumes:**
- Each Knowledge Base topic maps to one or more chatbot intents
- Abbreviated versions used for initial responses
- Full canonical answers available for "tell me more" follow-up
- Handoff to human support for complex issues (sizing disputes, warranty claims, custom orders)

**Content adaptation rules:**
- Answers under 3 sentences for initial response
- No jargon — plain language that matches how customers actually ask
- Category creation through language: "Performance Skins" not "grip socks" in answers
- Always offer next step: "Would you like to see our size guide?" / "Ready to shop?"

**Update cadence:** Quarterly review, or immediately when policies change.

### Wholesale / Studio / Retail Education
**Format:** Formal but direct. Data-driven. Decision-support focused.
**Consumes:**
- Product specs (materials, construction, pricing)
- Category creation positioning (the pitch for why to stock Performance Skins)
- Sock Math (cost comparison for buyer meetings)
- Discipline-specific content (which studios benefit most)
- Shipping and returns policies (wholesale terms)

**Content adaptation rules:**
- Lead with category creation: "Performance Skins are replacing grip socks"
- Include Sock Math data for financial justification
- Use discipline terminology to demonstrate expertise
- Instructor endorsement data: "Trusted by 1,000's of instructors"

**Update cadence:** Quarterly or with product launches.

### SEO / GEO Content
**Format:** Structured, heading-hierarchical, schema-markup-ready
**Consumes:**
- Discipline-specific moves (Appendix A of Knowledge Base)
- Comparison content (vs grip socks)
- Customer quotes with names/cities
- Product specs and benefits

**Content adaptation rules:**
- Comprehensive coverage optimized for featured snippets and AI citation
- Internal linking to products and collections
- GEO sections use city-specific context with discipline moves
- See `12-seo-geo-standards.md` for full requirements

### Internal Team Training
**Format:** Reference documentation — complete, browsable, searchable
**Consumes:** The full Knowledge Base as-is. No adaptation needed — the Knowledge Base IS the training document.

### Future AI Systems
**Format:** Structured data — topic-based, with canonical answers, abbreviated versions, and surface maps
**Consumes:**
- The Knowledge Base's structure (topic → canonical answer → abbreviated → surface map) is designed for AI consumption
- Each topic is self-contained and can be embedded as context for an AI agent
- The surface map tells an AI agent where each answer should and shouldn't appear

## Governance

### Who Approves Changes

| Change Type | Approver | Process |
|-------------|----------|---------|
| Product facts (specs, pricing, sizing) | Founder / Product | Update Knowledge Base → review → cascade |
| Policy (returns, warranty, shipping) | Founder / Operations | Update Knowledge Base → cascade to Help Scout, Tidio, website |
| Brand positioning (messaging, voice) | Founder / Brand | Update Brand System (02) + Copy Guide (08) → cascade |
| Design (tokens, components, layouts) | Design lead | Update Design System (03) → cascade to build spec |
| Content (copy, SEO, editorial) | Content lead / Builder | Must reference Knowledge Base. New facts require KB update first. |

### Conflict Resolution

When information conflicts between channels:
1. **Knowledge Base wins.** Always. It is the single source of truth.
2. **If the Knowledge Base is wrong**, update the Knowledge Base — don't patch the downstream system.
3. **If a downstream system needs different framing** (e.g., Help Scout needs conversational tone), the facts must match even if the words differ.
4. **Log the conflict** in `10-decision-log.md` if it reveals a policy question.

### Review Cadence

| System | Review Frequency | Trigger |
|--------|-----------------|---------|
| Knowledge Base | Continuous | Any product/policy change |
| Website content | Per deploy | Knowledge Base updates |
| Help Scout | Quarterly | Knowledge Base review + customer feedback patterns |
| Tidio AI | Quarterly | Knowledge Base review + chatbot performance data |
| Wholesale materials | Quarterly | Product launches or positioning changes |
| SEO/GEO content | Monthly | Keyword performance + Knowledge Base updates |

## Category Creation Across All Channels

The category creation strategy applies to EVERY channel — not just the website.

| Channel | Category Creation Expression |
|---------|------------------------------|
| Website | H1s, section copy, comparison content, pillar pages |
| Help Scout | "Performance Skins are designed to..." in every product reply |
| Tidio AI | Reframe "grip sock" questions: "While grip socks use silicone dots, Performance Skins provide 360° grip..." |
| Wholesale | "Performance Skins are replacing grip socks in studios nationwide" |
| Studio education | "Your students are ready to upgrade from grip socks" |
| SEO/GEO | Target sock queries, convert to Performance Skins content |
| Paid ads | Problem/solution framing: sock failure → Performance Skin solution |
| Journal | Educational content positioning Performance Skins as the evolution |

---

**Cross-references:**
- Master Knowledge Base → `07-product-knowledge-base.md`
- Brand positioning → `02-brand-system.md`
- Copy rules per channel → `08-copy-guide.md`
- SEO/GEO standards → `12-seo-geo-standards.md`
- Decision governance → `DECISION_FRAMEWORK.md`
