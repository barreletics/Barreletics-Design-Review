# Knowledge Graph — Barreletics Repository

**Date:** 2026-07-13  
**Status:** PLANNING  
**Purpose:** Map relationships, dependencies, and data flow between all knowledge domains

---

## MASTER DEPENDENCY DIAGRAM

```
                    ┌─────────────────────────────────────────────────────────────────┐
                    │                    SOURCE LAYER (Raw Inputs)                      │
                    │                                                                   │
                    │  Barreletics_Research_Bible.md    barreletics-decisions-2026-07-09.json
                    │  sections/*.html                  files/Barreletics_Home_v24.html │
                    │  Barreletics-PDP-v36-Jul2026.html IMPLEMENTATION-ROADMAP-Jul2026.md
                    │  barreletics-design-review/       manychat-kb/                    │
                    │  docs/08-LIVE-SITE-COPY-AUDIT.md  WORKFLOW.md                     │
                    └──────────────────────────────┬────────────────────────────────────┘
                                                   │
                                                   ▼
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                           KNOWLEDGE BASE LAYER (docs/)                                    │
│                                                                                          │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌──────────────┐   │
│  │ 01-BRAND     │     │ 02-BRAND     │     │ 03-DESIGN        │     │ 09-PRODUCT   │   │
│  │ NORTH STAR   │     │ SYSTEM       │     │ SYSTEM           │     │ KNOWLEDGE    │   │
│  │ (WHY)        │     │ (VOICE/MSG)  │     │ (TOKENS/RULES)   │     │ (FACTS)      │   │
│  └──────┬───────┘     └──────┬───────┘     └────────┬─────────┘     └──────┬───────┘   │
│         │                    │                       │                       │           │
│         ▼                    ▼                       ▼                       ▼           │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌──────────────┐   │
│  │              │     │ 07-COPY      │     │ 04-COMPONENT     │     │ 10-DECISIONS │   │
│  │  (terminal)  │     │ GUIDE        │     │ LIBRARY          │     │ (LOG)        │   │
│  │              │     │              │     │                  │     │              │   │
│  └──────────────┘     └──────┬───────┘     └────────┬─────────┘     └──────┬───────┘   │
│                              │                       │                       │           │
│                              ▼                       ▼                       │           │
│                       ┌──────────────┐     ┌──────────────────┐              │           │
│                       │ 08-CREATIVE  │     │ 05-PDP           │◄─────────────┘           │
│                       │ PLAYBOOK     │     │ ARCHITECTURE     │                          │
│                       │ (STUB)       │     └────────┬─────────┘                          │
│                       └──────────────┘              │                                    │
│                                                     │                                    │
│                              ┌───────────────┐      │      ┌────────────────┐            │
│                              │ 06-HOMEPAGE   │◄─────┼──────│ (shared deps)  │            │
│                              │ ARCHITECTURE  │      │      └────────────────┘            │
│                              └───────────────┘      │                                    │
└─────────────────────────────────────────────────────┼────────────────────────────────────┘
                                                      │
                                                      ▼
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                           IMPLEMENTATION LAYER                                            │
│                                                                                          │
│  planning/11-shopify-implementation-roadmap-inventory.md                                  │
│  Shopify Theme (Liquid sections, snippets, templates, assets)                            │
│  ManyChat KB (customer-facing automation)                                                 │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## DOMAIN DEPENDENCY MAP

### docs/01 — Brand North Star (WHY)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `Barreletics_Research_Bible.md` (Sections 1, 4, 6) | Founder story, positioning, category ownership |
| **Inputs** | `docs/08-LIVE-SITE-COPY-AUDIT.md` | Live Shopify product descriptions |
| **Inputs** | `manychat-kb/` | Customer-facing founder narrative |
| **Outputs** | `docs/02-BRAND-SYSTEM.md` | Voice/tone inherit from North Star values |
| **Outputs** | `docs/07-COPY-GUIDE.md` | Copy must reflect brand positioning |
| **Outputs** | `docs/09-PRODUCT-KNOWLEDGE.md` | Product framing draws from positioning |
| **Cross-ref** | `docs/10-DECISIONS.md` | Cites North Star for decision rationale |

---

### docs/02 — Brand System (VOICE / MESSAGING)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/01-BRAND-NORTH-STAR.md` | Inherits values, mission, positioning |
| **Inputs** | `Barreletics_Research_Bible.md` (Sections 1, 4, 6) | Slogan mapping, voice guidelines |
| **Inputs** | `manychat-kb/12-brand-voice-and-taglines.md` | Taglines, tone rules |
| **Outputs** | `docs/07-COPY-GUIDE.md` | Voice rules govern all copy |
| **Outputs** | `docs/04-COMPONENT-LIBRARY.md` | Components use brand slogans |
| **Outputs** | `docs/05-PDP-ARCHITECTURE.md` | PDP copy follows voice system |
| **Outputs** | `docs/06-HOMEPAGE-ARCHITECTURE.md` | Section headlines from slogan map |
| **Outputs** | `manychat-kb/` | ManyChat voice matches brand system |
| **Cross-ref** | `docs/10-DECISIONS.md` | Copy decisions cite brand system |

---

### docs/03 — Design System (TOKENS / RULES)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `barreletics-design-review/Barreletics Design Review/audit-styles.css` | PRIMARY token stylesheet |
| **Inputs** | `barreletics-design-review/Barreletics Design Review/maturation-styles.css` | Matured tokens |
| **Inputs** | `Barreletics_Research_Bible.md` (Section 7) | Design system rules |
| **Inputs** | `barreletics-design-review/design_handoff_barreletics 2/README.md` | Handoff instructions |
| **Outputs** | `docs/04-COMPONENT-LIBRARY.md` | Components built from tokens |
| **Outputs** | `docs/05-PDP-ARCHITECTURE.md` | PDP uses design tokens |
| **Outputs** | `docs/06-HOMEPAGE-ARCHITECTURE.md` | Homepage uses design tokens |
| **Outputs** | `docs/10-DECISIONS.md` | Design decisions logged |
| **Outputs** | Shopify theme (implementation target) | CSS variables, typography, spacing |
| **Cross-ref** | `planning/ADR-01` through `ADR-07` | Architecture Decision Records |

---

### docs/04 — Component Library (PATTERNS)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/03-DESIGN-SYSTEM.md` | Tokens define component styling |
| **Inputs** | `sections/*.html` | Source HTML for each component |
| **Inputs** | `docs/02-BRAND-SYSTEM.md` | Slogans populate components |
| **Inputs** | `docs/09-PRODUCT-KNOWLEDGE.md` | Product data fills components |
| **Outputs** | `docs/05-PDP-ARCHITECTURE.md` | PDP assembled from components |
| **Outputs** | `docs/06-HOMEPAGE-ARCHITECTURE.md` | Homepage assembled from components |
| **Outputs** | Shopify sections/snippets | Each component → Liquid section |
| **Cross-ref** | `docs/10-DECISIONS.md` | Component decisions (splits, grids, etc.) |

---

### docs/05 — PDP Architecture (PRODUCT PAGE)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/03-DESIGN-SYSTEM.md` | Design tokens |
| **Inputs** | `docs/04-COMPONENT-LIBRARY.md` | Reusable components |
| **Inputs** | `docs/09-PRODUCT-KNOWLEDGE.md` | Product data, variants, benefits |
| **Inputs** | `docs/02-BRAND-SYSTEM.md` | Copy and voice |
| **Inputs** | `Barreletics-PDP-v36-Jul2026.html` | Canonical PDP mock |
| **Inputs** | `docs/10-DECISIONS.md` | Constraining decisions (D-003, D-004, etc.) |
| **Outputs** | Shopify `templates/product.json` | Implementation target |
| **Outputs** | `docs/07-COPY-GUIDE.md` | PDP copy cataloged in copy guide |
| **Cross-ref** | `manychat-kb/10-faq-general.md` | FAQ content on PDP |
| **Cross-ref** | JudgeMe reviews integration | Review display section |

---

### docs/06 — Homepage Architecture (HOME PAGE)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/03-DESIGN-SYSTEM.md` | Design tokens, CSS variables |
| **Inputs** | `docs/04-COMPONENT-LIBRARY.md` | All section components |
| **Inputs** | `docs/02-BRAND-SYSTEM.md` | Slogan-to-section mapping |
| **Inputs** | `docs/09-PRODUCT-KNOWLEDGE.md` | Product cards, pricing |
| **Inputs** | `files/Barreletics_Home_v24.html` | Latest homepage mock |
| **Inputs** | `barreletics-design-review/.../Barreletics Home - Matured.html` | Canonical matured design |
| **Inputs** | `docs/10-DECISIONS.md` | Constraining decisions |
| **Outputs** | Shopify `templates/index.json` | Implementation target |
| **Outputs** | `docs/07-COPY-GUIDE.md` | Homepage copy cataloged |
| **Cross-ref** | `docs/05-PDP-ARCHITECTURE.md` | Shared components (ticker, reviews, newsletter) |

---

### docs/07 — Copy Guide (ALL APPROVED COPY)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/02-BRAND-SYSTEM.md` | Voice, tone, slogan rules |
| **Inputs** | `docs/01-BRAND-NORTH-STAR.md` | Brand positioning language |
| **Inputs** | `docs/05-PDP-ARCHITECTURE.md` | PDP copy extracted |
| **Inputs** | `docs/06-HOMEPAGE-ARCHITECTURE.md` | Homepage copy extracted |
| **Inputs** | `Section-26-NotesFromStudio.html`, `Section-27-FAQ.html`, `Section-28-Newsletter.html` | Section copy |
| **Inputs** | `docs/08-LIVE-SITE-COPY-AUDIT.md` | Current production copy |
| **Outputs** | Shopify theme (metafields, section content) | Final copy for implementation |
| **Outputs** | `manychat-kb/` | CS/automation copy consistency |
| **Cross-ref** | `docs/09-PRODUCT-KNOWLEDGE.md` | Product descriptions |

---

### docs/08 — Creative Playbook (STUB)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/02-BRAND-SYSTEM.md` | Brand voice for campaigns |
| **Inputs** | `docs/03-DESIGN-SYSTEM.md` | Visual guidelines for assets |
| **Status** | STUB — not yet built | |

---

### docs/09 — Product Knowledge (ALL FACTS)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `Barreletics_Research_Bible.md` (40+ citations) | Technology, reviews, competitive |
| **Inputs** | `manychat-kb/02–11` | Sizing, pricing, care, FAQ, objections |
| **Inputs** | `docs/08-LIVE-SITE-COPY-AUDIT.md` | Live product data, variants, pricing |
| **Inputs** | Shopify catalog (live) | Variant inventory, GIDs |
| **Outputs** | `docs/05-PDP-ARCHITECTURE.md` | PDP product data |
| **Outputs** | `docs/06-HOMEPAGE-ARCHITECTURE.md` | Product cards, pricing display |
| **Outputs** | `docs/04-COMPONENT-LIBRARY.md` | Benefit grid content, sock math data |
| **Outputs** | `docs/10-DECISIONS.md` | Product-level decisions |
| **Outputs** | `manychat-kb/` | CS answers sourced from product facts |
| **Outputs** | Shopify metafields | Product data for implementation |
| **Cross-ref** | `docs/07-COPY-GUIDE.md` | Product descriptions |

---

### docs/10 — Decisions (CONSTRAINT LOG)

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `Barreletics_Research_Bible.md` (12+ citations) | Design rules from Section 7 |
| **Inputs** | `barreletics-decisions-2026-07-09.json` | CEO per-section notes |
| **Inputs** | `IMPLEMENTATION-ROADMAP-Jul2026.md` | Timeline decisions |
| **Inputs** | `WORKFLOW.md` | Workflow decisions (D-WF-01–09) |
| **Inputs** | `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` | Section approval matrix |
| **Inputs** | `docs/03-DESIGN-SYSTEM.md` | Design token decisions |
| **Inputs** | `docs/04-COMPONENT-LIBRARY.md` | Component decisions |
| **Inputs** | `docs/05-PDP-ARCHITECTURE.md` | PDP architecture decisions |
| **Outputs** | ALL docs (constraining) | Decisions constrain every other doc |
| **Outputs** | `planning/ADR-*` | Formal ADR records |
| **Outputs** | Shopify implementation | Must-follow constraints |

---

### planning/11 — Shopify Implementation Roadmap

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | ALL docs/ (01–10) | Knowledge base feeds implementation |
| **Inputs** | All HTML prototypes (canonical set) | Build targets |
| **Inputs** | `sections/*.html` | Named section source HTML |
| **Inputs** | `files/Barreletics_Home_v24.html` | Homepage canonical |
| **Inputs** | `Barreletics-PDP-v36-Jul2026.html` | PDP canonical |
| **Outputs** | Shopify theme build | Final deliverable |
| **Cross-ref** | `docs/10-DECISIONS.md` | Constraints on implementation |
| **Cross-ref** | `IMPLEMENTATION-ROADMAP-Jul2026.md` | Timeline/phasing |

---

### manychat-kb/ — ManyChat Knowledge Base

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Inputs** | `docs/01-BRAND-NORTH-STAR.md` | Brand positioning |
| **Inputs** | `docs/02-BRAND-SYSTEM.md` | Voice and tone |
| **Inputs** | `docs/09-PRODUCT-KNOWLEDGE.md` | Product facts |
| **Outputs** | `docs/09-PRODUCT-KNOWLEDGE.md` | Sizing, care, FAQ data |
| **Outputs** | `docs/01-BRAND-NORTH-STAR.md` | Founder narrative |
| **Bidirectional** | `docs/07-COPY-GUIDE.md` | Copy consistency both ways |
| **Files** | 02-open-vs-closed-sole, 03-sizing-chart, 04-pricing, 05-why-better-than-socks, 06-care-and-cleaning, 07-returns-and-exchanges, 08-shipping, 09-faq-fit-sizing, 10-faq-general, 11-sensitive-and-medical, 12-brand-voice-and-taglines, 13-direct-links, 14-escalation-and-handoff, 15-objection-handling, 16-comment-snippets |

---

### Barreletics_Research_Bible.md — Primary Source

| Direction | Connected To | Relationship |
|-----------|-------------|--------------|
| **Outputs** | `docs/01` | Founder story, brand positioning (17+ citations) |
| **Outputs** | `docs/02` | Voice guidelines, slogans (8+ citations) |
| **Outputs** | `docs/03` | Design system rules (Section 7) |
| **Outputs** | `docs/09` | Product technology, reviews, competitive (40+ citations) |
| **Outputs** | `docs/10` | Decision rationale (12+ citations) |
| **Status** | ~70% extracted into docs/, raw detail remains | Critical primary source |

---

## READING ORDER (Prerequisite Chain)

```
LEVEL 0 (No prerequisites — read first):
  docs/01-BRAND-NORTH-STAR.md
  docs/03-DESIGN-SYSTEM.md
  docs/09-PRODUCT-KNOWLEDGE.md

LEVEL 1 (Requires Level 0):
  docs/02-BRAND-SYSTEM.md          ← requires 01
  docs/10-DECISIONS.md             ← requires 03, 09

LEVEL 2 (Requires Level 1):
  docs/04-COMPONENT-LIBRARY.md     ← requires 03, 02
  docs/07-COPY-GUIDE.md            ← requires 02, 01

LEVEL 3 (Requires Level 2):
  docs/05-PDP-ARCHITECTURE.md      ← requires 04, 09, 10
  docs/06-HOMEPAGE-ARCHITECTURE.md ← requires 04, 02, 09, 10

LEVEL 4 (Requires all above):
  planning/11-shopify-implementation-roadmap-inventory.md ← requires ALL
```

---

## SOURCE → KNOWLEDGE BASE FLOW

```
Barreletics_Research_Bible.md ──────┬──► docs/01 (brand positioning)
                                    ├──► docs/02 (voice, slogans)
                                    ├──► docs/03 (design rules)
                                    ├──► docs/09 (product tech, reviews)
                                    └──► docs/10 (decision rationale)

manychat-kb/ ───────────────────────┬──► docs/09 (sizing, care, FAQ, objections)
                                    ├──► docs/01 (founder narrative)
                                    └──► docs/02 (taglines, voice)

docs/08-LIVE-SITE-COPY-AUDIT.md ───┬──► docs/09 (live variants, pricing)
                                    ├──► docs/07 (production copy)
                                    └──► docs/01 (product descriptions)

sections/*.html ────────────────────────► docs/04 (component specs extracted)

files/Barreletics_Home_v24.html ────────► docs/06 (homepage architecture)

Barreletics-PDP-v36-Jul2026.html ──────► docs/05 (PDP architecture)

barreletics-decisions-2026-07-09.json ──► docs/10 (CEO notes)

WORKFLOW.md ────────────────────────────► docs/10 (workflow decisions)

IMPLEMENTATION-ROADMAP-Jul2026.md ─────► docs/10 (timeline decisions)
                                   ────► planning/11 (roadmap phases)
```

---

## DECISION FLOW (Constraining Relationships)

```
docs/10-DECISIONS.md
  │
  ├──► D-001 (Roboto only)           ──► docs/03, 04, 05, 06 (typography)
  ├──► D-003 (Buttons: 0px radius)   ──► docs/04, 05, 06 (button rendering)
  ├──► D-004 (Coral: cart badge ONLY) ──► docs/03, 04, 05, 06 (color usage)
  ├──► D-006 (50/50 split sizing)    ──► docs/04, 06 (section layout)
  ├──► D-007 (Color palette values)  ──► docs/03, 04, 05, 06 (all styling)
  ├──► D-013 (Product naming)        ──► docs/09, 07 (product references)
  ├──► D-WF-* (Workflow rules)       ──► ALL docs (editing constraints)
  │
  └──► planning/ADR-01 through ADR-07 (formal architecture decision records)
       └──► Shopify theme (implementation must comply)
```

---

## IMPLEMENTATION FLOW (What's Needed to Build Shopify)

```
PHASE 1: Foundation
  docs/03 (tokens) ──► Shopify CSS variables, settings_schema.json
  docs/10 (decisions) ──► Constraints checklist

PHASE 2: Components
  docs/04 (component library) ──► Liquid sections + snippets
  sections/*.html (named files) ──► Reference HTML for each section

PHASE 3: Page Templates
  docs/05 + Barreletics-PDP-v36 ──► templates/product.json + PDP sections
  docs/06 + files/Home_v24 ──► templates/index.json + homepage sections

PHASE 4: Content & Data
  docs/09 (products) ──► Shopify product metafields, variant data
  docs/07 (copy) ──► Section content, metafields
  docs/02 (brand) ──► Theme settings, header/footer copy

PHASE 5: Integrations
  manychat-kb/ ──► ManyChat flow content (external)
  JudgeMe ──► Review display sections
  Juicer ──► Social feed embed
  Shop Pay ──► Payment installment display

BUILD DEPENDENCY CHAIN:
  03 → 04 → [05, 06] → Shopify theme
  09 → metafields → [05, 06] data bindings
  02 → 07 → section content population
  10 → ADRs → build constraint validation
```

---

## CROSS-REFERENCE DENSITY MAP

| Doc | Cited By (count) | Cites (count) | Hub Score |
|-----|------------------|---------------|-----------|
| docs/09-PRODUCT-KNOWLEDGE | 5 docs | 6 sources | **HIGH** (data hub) |
| docs/10-DECISIONS | 6 docs | 8 sources | **HIGH** (constraint hub) |
| docs/03-DESIGN-SYSTEM | 4 docs | 4 sources | **HIGH** (token hub) |
| docs/04-COMPONENT-LIBRARY | 3 docs | 4 docs | MEDIUM (assembly layer) |
| docs/02-BRAND-SYSTEM | 4 docs | 3 sources | MEDIUM (voice authority) |
| docs/01-BRAND-NORTH-STAR | 3 docs | 3 sources | MEDIUM (foundation) |
| docs/07-COPY-GUIDE | 1 doc | 5 docs | LOW (terminal consumer) |
| docs/05-PDP-ARCHITECTURE | 1 doc | 5 docs | LOW (terminal consumer) |
| docs/06-HOMEPAGE-ARCHITECTURE | 1 doc | 5 docs | LOW (terminal consumer) |
| Barreletics_Research_Bible.md | 5 docs | 0 (primary source) | **CRITICAL** (root source) |
