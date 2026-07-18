# INDEX Inventory — Complete Repository Navigation Map

**Generated:** 2026-07-13  
**Purpose:** Background preparation for final INDEX.md — maps every file, its category, purpose, status, and dependencies  
**DO NOT COMMIT** — planning artifact only

---

## Summary Statistics

| Category | File Count | Notes |
|----------|-----------|-------|
| docs/ (Knowledge Base) | 13 files | 4 APPROVED, 5 PENDING REVIEW, 3 STUB, 1 no-status |
| manychat-kb/ | 16 files + 1 zip | ManyChat chatbot knowledge base |
| sections/ | 31 files | Individual HTML section prototypes |
| files/ | 16 files | Homepage version progression (v10–v24 + index) |
| barreletics-design-review/ | ~250+ files | Full Claude Design project archive (versions, uploads, handoffs) |
| .github/ | 5 files | PR automation workflow + docs |
| scripts/ | 2 files | PR automation scripts |
| Root-level | 10 files | HTML prototypes, config, data, workflow |
| planning/ | This file | Background prep (no commits) |

---

## 1. docs/ — Knowledge Base (CANONICAL)

These are the authoritative operating documents. Status per WORKFLOW.md rules.

| File | Status | Purpose | Dependencies |
|------|--------|---------|-------------|
| `docs/INDEX.md` | STUB | Navigation guide for all docs | References all docs/0x files |
| `docs/00-README.md` | STUB | Getting started and overview | — |
| `docs/01-BRAND-NORTH-STAR.md` | PENDING REVIEW | Brand vision, mission, core values | Source: Research Bible, uploads |
| `docs/02-BRAND-SYSTEM.md` | PENDING REVIEW | Brand identity, voice, tone, messaging guidelines | Refs: 01-BRAND-NORTH-STAR |
| `docs/03-DESIGN-SYSTEM.md` | PENDING REVIEW | Design tokens, principles, system architecture | Refs: 02-BRAND-SYSTEM; feeds 04, 05, 06 |
| `docs/04-COMPONENT-LIBRARY.md` | APPROVED | Reusable components, page sections, layout patterns | Refs: 03-DESIGN-SYSTEM; feeds 05, 06 |
| `docs/05-PDP-ARCHITECTURE.md` | APPROVED | Lossless PDP specification (every measurement, class, color, decision) | Refs: 03, 04; source: PDP HTML prototypes |
| `docs/06-HOMEPAGE-ARCHITECTURE.md` | APPROVED | Lossless Homepage specification (all sections, animations, interactions) | Refs: 03, 04; source: Homepage HTML versions |
| `docs/07-COPY-GUIDE.md` | PENDING REVIEW | Lossless copy asset catalog (every headline, CTA, label, microcopy) | Source: all HTML prototypes, live site audit |
| `docs/08-CREATIVE-PLAYBOOK.md` | STUB | Creative direction, campaigns, asset specifications | Refs: 01, 02, 07 |
| `docs/08-LIVE-SITE-COPY-AUDIT.md` | APPROVED | Systematic page-by-page crawl of barreletics.com copy | Source: live site; feeds 07-COPY-GUIDE |
| `docs/09-PRODUCT-KNOWLEDGE.md` | PENDING REVIEW | Every product fact, spec, variant, claim — sourced and cited | Source: Shopify catalog, Research Bible, uploads |
| `docs/10-DECISIONS.md` | STUB | Architectural decisions, rationale, changelog | Source: barreletics-decisions JSON, section matrix |

**Note:** Two files share the `08-` prefix (CREATIVE-PLAYBOOK and LIVE-SITE-COPY-AUDIT). INDEX.md should clarify this numbering.

---

## 2. manychat-kb/ — ManyChat Chatbot Knowledge Base

All files are standalone KB articles for the ManyChat AI chatbot integration.

| File | Purpose | Dependencies |
|------|---------|-------------|
| `manychat-kb/02-open-vs-closed-sole.md` | Open vs closed sole product comparison | Product knowledge (09) |
| `manychat-kb/03-sizing-chart.md` | Sizing chart and fit guidance | Product knowledge (09) |
| `manychat-kb/04-pricing.md` | Pricing information | Shopify catalog |
| `manychat-kb/05-why-better-than-socks.md` | Competitive positioning vs grip socks | Product knowledge (09), brand messaging (02) |
| `manychat-kb/06-care-and-cleaning.md` | Care and cleaning instructions | Product knowledge (09) |
| `manychat-kb/07-returns-and-exchanges.md` | Return/exchange policy | Store policies |
| `manychat-kb/08-shipping.md` | Shipping information | Store policies |
| `manychat-kb/09-faq-fit-sizing.md` | FAQ: fit and sizing questions | 03-sizing-chart |
| `manychat-kb/10-faq-general.md` | FAQ: general product questions | Multiple KB articles |
| `manychat-kb/11-sensitive-and-medical.md` | Sensitive/medical use disclaimers | Product knowledge (09) |
| `manychat-kb/12-brand-voice-and-taglines.md` | Brand voice guidelines for chatbot | 02-BRAND-SYSTEM, 07-COPY-GUIDE |
| `manychat-kb/13-direct-links.md` | Direct links to key pages | Shopify store URLs |
| `manychat-kb/14-escalation-and-handoff.md` | When to escalate to human support | — |
| `manychat-kb/15-objection-handling.md` | Objection handling scripts | Brand messaging, product knowledge |
| `manychat-kb/16-comment-snippets.md` | Social media comment reply snippets | Brand voice (12) |
| `manychat-kb/manychat-kb-all-16.zip` | Archive of all 16 KB files | All above |

**Note:** Numbering starts at 02 (no 01 file present). This may be intentional (01 = system prompt configured in ManyChat directly).

---

## 3. sections/ — HTML Section Prototypes

Individual homepage section builds. Each is a standalone HTML file for one section of the redesigned homepage.

| File | Section | Purpose |
|------|---------|---------|
| `sections/hero.html` | Hero | Hero banner section |
| `sections/01-section.html` | §01 | Hero (numbered version) |
| `sections/problem.html` | Problem | Problem/pain point section |
| `sections/problem2.html` | Problem v2 | Alternative problem section |
| `sections/03-section.html` | §03 | 50/50 Progress section |
| `sections/04-section.html` | §04 | TBD (undecided section) |
| `sections/06-section.html` | §06 | Refactor target |
| `sections/07-section.html` | §07 | Refactor target |
| `sections/08-section.html` | §08 | Refactor target |
| `sections/09-section.html` | §09 | The Problem (keep — matured) |
| `sections/10-section.html` | §10 | Brand & conversion |
| `sections/12-section.html` | §12 | Variants |
| `sections/13-section.html` | §13 | Conversion |
| `sections/14-section.html` | §14 | Variant grid v2 |
| `sections/15-section.html` | §15 | v28 original variant grid |
| `sections/18-section.html` | §18 | Promo tiles |
| `sections/19-section.html` | §19 | Sock math |
| `sections/20-section.html` | §20 | Never loses grip (50/50) |
| `sections/21-section.html` | §21 | Push harder (50/50) |
| `sections/23-section.html` | §23 | Video & content |
| `sections/24-section.html` | §24 | Content 2 |
| `sections/25-section.html` | §25 | Coperni collab |
| `sections/26-section.html` | §26 | Content 3 / blog |
| `sections/29-section.html` | §29 | Final CTA |
| `sections/assoc.html` | — | Association/trust badges |
| `sections/closing-statement.html` | — | Closing statement section |
| `sections/credibility.html` | — | Credibility/social proof |
| `sections/disciplines.html` | — | Disciplines showcase |
| `sections/founder-letter.html` | — | Founder letter section |
| `sections/founder2.html` | — | Founder letter v2 |
| `sections/manifesto.html` | — | Brand manifesto |
| `sections/manifesto2.html` | — | Brand manifesto v2 |
| `sections/range.html` | — | Product range showcase |
| `sections/sock-math.html` | — | Sock math (named version) |
| `sections/split-section.html` | — | Split/50-50 layout |
| `sections/split-section2.html` | — | Split/50-50 layout v2 |
| `sections/split-section3.html` | — | Split/50-50 layout v3 |
| `sections/testimonial.html` | — | Testimonials section |
| `sections/variants.html` | — | Variant display section |

**Missing numbered sections:** 02, 05, 11, 16, 17, 22, 27, 28 (some may be covered by named files or not yet built)

---

## 4. files/ — Homepage Version Progression

Linear version history of complete homepage prototypes.

| File | Purpose |
|------|---------|
| `files/index.html` | Version index/directory page |
| `files/Barreletics_Home_v10.html` | Homepage v10 |
| `files/Barreletics_Home_v11.html` | Homepage v11 |
| `files/Barreletics_Home_v12.html` | Homepage v12 |
| `files/Barreletics_Home_v13.html` | Homepage v13 |
| `files/Barreletics_Home_v14.html` | Homepage v14 |
| `files/Barreletics_Home_v15.html` | Homepage v15 |
| `files/Barreletics_Home_v16.html` | Homepage v16 |
| `files/Barreletics_Home_v17.html` | Homepage v17 |
| `files/Barreletics_Home_v18.html` | Homepage v18 |
| `files/Barreletics_Home_v19.html` | Homepage v19 |
| `files/Barreletics_Home_v20.html` | Homepage v20 |
| `files/Barreletics_Home_v21.html` | Homepage v21 |
| `files/Barreletics_Home_v22.html` | Homepage v22 |
| `files/Barreletics_Home_v23.html` | Homepage v23 |
| `files/Barreletics_Home_v24.html` | Homepage v24 (latest in this set) |

**Relationship:** These are the output of the Barreletics_All_Versions archive, progressing from v10 to v24. Earlier versions (v1–v9) live in `barreletics-design-review/Barreletics Design Review/` and its versions subdirectories.

---

## 5. Root-Level Files

| File | Category | Purpose | Dependencies |
|------|----------|---------|-------------|
| `index.html` | Prototype | Root-level homepage (likely latest or redirect) | — |
| `Barreletics-DesignSystem-v1_0-Jul2026.html` | Prototype | Design system reference (standalone HTML) | Source for docs/03 |
| `Barreletics-Everything-Index.html` | Prototype | Master index of all prototypes | References all HTML files |
| `Barreletics-PDP-v36-Jul2026.html` | Prototype | PDP prototype v36 (latest) | Source for docs/05 |
| `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` | Prototype | Section decision matrix viewer | Source for IMPLEMENTATION-ROADMAP |
| `Section-26-NotesFromStudio.html` | Prototype | Section 26 — Notes from Studio standalone | feeds sections/26-section |
| `Section-27-FAQ.html` | Prototype | Section 27 — FAQ standalone | feeds docs/07-COPY-GUIDE |
| `Section-28-Newsletter.html` | Prototype | Section 28 — Newsletter signup standalone | feeds sections/ |
| `matrix-20260707.html` | Prototype | Section decision matrix (July 7 snapshot) | Superseded by SectionDecisionMatrix-v1_0 |
| `IMPLEMENTATION-ROADMAP-Jul2026.md` | Planning | Implementation roadmap from section matrix (23 sections) | Source: decision matrix, decisions JSON |
| `WORKFLOW.md` | Operations | Permanent operating model (roles, statuses, rules) | APPROVED — governs all docs |
| `Makefile` | Tooling | PR automation convenience commands | Refs: scripts/create_pr.py, scripts/pr.sh |
| `barreletics-decisions-2026-07-09.json` | Data | CEO section-by-section decisions (raw JSON) | Source for docs/10-DECISIONS, IMPLEMENTATION-ROADMAP |
| `Manychat Content.zip` | Archive | Zipped ManyChat content export | Source for manychat-kb/ |
| `Manychat Content/` | Archive | Unzipped ManyChat content (appears empty of files) | Superseded by manychat-kb/ |

---

## 6. .github/ — PR Automation System

| File | Purpose | Dependencies |
|------|---------|-------------|
| `.github/workflows/ai-review-pr.yml` | GitHub Actions workflow for auto PR creation | Triggered by scripts |
| `.github/PR-AUTOMATION.md` | Complete PR automation reference guide (500+ lines) | — |
| `.github/QUICK-REFERENCE.md` | One-page PR cheat sheet | Summary of PR-AUTOMATION |
| `.github/SETUP.md` | Onboarding and verification guide | — |
| `.github/SYSTEM-OVERVIEW.md` | PR system architecture overview | References all .github and scripts files |

---

## 7. scripts/ — Automation Scripts

| File | Purpose | Dependencies |
|------|---------|-------------|
| `scripts/create_pr.py` | Python PR automation script (recommended) | Called by Makefile |
| `scripts/pr.sh` | Bash PR automation fallback | Called by Makefile |

---

## 8. barreletics-design-review/ — Full Design Archive

This is the complete Claude Design project export with multiple sub-archives. Contains the original design review work, all version history, uploads, screenshots, and handoff materials.

### 8a. Top-level design files

| File | Purpose |
|------|---------|
| `barreletics-design-review/README.md` | Design review project readme |
| `barreletics-design-review/Barreletics_Handoff.md` | Design handoff document |
| `barreletics-design-review/Barreletics_Research_Bible.md` | Research Bible (product research, competitive analysis) |
| `barreletics-design-review/Barreletics_Home_v10.html` | Homepage v10 prototype |
| `barreletics-design-review/Barreletics_Home_v23.html` | Homepage v23 prototype |
| `barreletics-design-review/files.zip` | Archive of homepage versions |

### 8b. Barreletics Design Review/ (Claude project — current files)

Primary working directory from Claude Design sessions. Contains:

**HTML Prototypes (Page Types):**
- Home: v1 (base), v2–v10, Matured
- PDP: v1, v2, Matured
- Collection: v1, Matured
- Blog, Article (6 articles: base, Founder, Coperni, Teacher, Retire, Barefoot)
- Audit, Wireframes, Maturation Study
- Section 15 — Variant Grid v28
- Section Mocks

**CSS Stylesheets:**
- `audit-styles.css` — Audit page styles
- `home-matured.css` — Matured home styles
- `maturation-styles.css` — Maturation study styles
- `pages-extras.css` — Additional page styles
- `pdp-styles.css` — PDP-specific styles
- `section-mocks.css` — Section mock styles
- `wireframes-styles.css` — Wireframe styles

**JavaScript:**
- `audit-behavior.js` — Audit page interactions
- `ticker.js` — Ticker/marquee animation

**JSX (React-style tweaks panels):**
- `audit-tweaks.jsx` — Audit page tweaks panel
- `home-tweaks.jsx` — Home page tweaks panel
- `pdp-tweaks.jsx` — PDP tweaks panel
- `tweaks-panel.jsx` — Shared tweaks panel component

**Images:**
- `barreletics-logo.png` — Full logo
- `barreletics-mark.png` — Logo mark only

### 8c. Barreletics Design Review/uploads/

Source materials uploaded to Claude Design:

| File | Purpose |
|------|---------|
| `Barreletics_Complete_Handoff_for_ClaudeDesign.md` | Complete design handoff brief |
| `Barreletics_Content_From_website` | Scraped website content |
| `Barreletics_ManyChat_Knowledge.md` | ManyChat KB consolidated |
| `Barreletics_Research_Bible.md` | Full research bible |
| `Barreletics_v28_1_BASE.html` | v28.1 base prototype |
| `Copy of Barreletics-Dragonfly-Logo-Black.pdf/png` | Dragonfly logo (black) |
| `Dragonly-Logo-Black.pdf/png` | Dragonfly logo alternate |
| `More content.pdf` | Additional content materials |
| `barreletics-pdp-live.pdf` | Live PDP page capture |
| `screencapture-*.pdf` (×3) | Full-page captures of live collection/PDP pages |
| `Screenshot 2026-05-24 *.png` (×22) | Design review screenshots |
| `Screenshot 2026-05-30 *.png` (×1) | Later design screenshot |
| `pasted-*.png` (×1) | Pasted clipboard image |
| `Claude Design Files/` | Duplicate uploads with hash suffixes |

### 8d. Barreletics Design Review/screenshots/

Design comparison screenshots:

| File | Purpose |
|------|---------|
| `01-teal-sections.png`, `02-teal-sections.png` | Teal section comparison |
| `01-v10-check.png`, `02-v10-check.png` | v10 verification |
| `01-v10b.png` through `04-v10b.png` | v10b progression |
| `after-50-50.png`, `review-50-50.png`, `v2-50-50.png` | 50/50 section review |
| `after-sockmath.png`, `review-sockmath.png`, `v2-sockmath.png`, `v10-sockmath.png` | Sock math section review |
| `colorway-lab.png` | Colorway experimentation |
| `study-check.png`, `study-overview.png` | Maturation study check |
| `v10-hero.png` | v10 hero screenshot |

### 8e. Barreletics Design Review/versions/

Date-stamped version snapshots preserving state at each design iteration:

| Directory | Contents |
|-----------|----------|
| `versions/2026-05-24/` | Initial: Articles, Blog, Collection, Home, PDP v2, PDP + CSS (13 files) |
| `versions/2026-05-25/` | Day 2: Added ticker.js, pdp-tweaks.jsx (15 files) |
| `versions/2026-05-25-batch/` | Batch update: Home v2–v5b, home-tweaks.jsx (12 files) |
| `versions/2026-05-25-v4-prebuild/` | Pre-v4 build checkpoint (11 files) |
| `versions/2026-05-25-v4-video/` | v4 video integration (1 file) |
| `versions/2026-05-25-v5/` | v5 full set: all 6 articles + 5 pages + CSS/JSX (18 files) |
| `versions/2026-05-25-coperni-vid/` | Coperni video integration (1 file) |
| `versions/2026-05-26-v6/` | v6: Home v4, v5a, v5b + CSS (5 files) |
| `versions/2026-05-26-v7v8/` | v7/v8: Home v4, v6 (2 files) |
| `versions/2026-05-26-v9/` | v9: Home v6 (1 file) |
| `versions/2026-05-31/` | Maturation study + Section 15 v28 + CSS (3 files) |

### 8f. Barreletics Design Review/export/

| File | Purpose |
|------|---------|
| `Barreletics Maturation Study - Bundled.html` | Self-contained maturation study export |

### 8g. Barreletics Design Review/mocks/

| File | Purpose |
|------|---------|
| `index.html` | Section mocks directory page |

### 8h. Barreletics_All_Versions/

Consolidated archive of homepage v10–v24 progression:

| File | Purpose |
|------|---------|
| `Barreletics_Handoff.md` | Handoff notes for version set |
| `Barreletics_Research_Bible.md` | Research bible copy |
| `Barreletics_Home_v10.html` – `v24.html` | 15 homepage versions |
| `index.html` | Version directory page |

### 8i. design_handoff_barreletics 2/

Complete design handoff package (most comprehensive version):

| Directory | Contents |
|-----------|----------|
| `pages/` | All page prototypes: Home (v1–v11 + Matured + Final + Patched), PDP (v1, v2 + Matured + Final), Collection (v1, Matured, Final), Articles (6), Blog, Audit, Wireframes, Maturation Study, Section 15, Section Mocks |
| `pages/` (CSS) | audit-styles, home-matured, maturation-styles, pages-extras, pdp-styles, section-mocks, wireframes-styles |
| `pages/` (JS/JSX) | audit-behavior.js, ticker.js, audit-tweaks.jsx, home-tweaks.jsx, pdp-tweaks.jsx, tweaks-panel.jsx |
| `pages/` (images) | barreletics-logo.png, barreletics-mark.png |
| `README.md` | Handoff readme |

### 8j. project/

Working project directory (mirrors Barreletics Design Review/ structure):
- Same set of HTML prototypes (Home v1–v9, PDP, Collection, Articles, Blog, Audit, Wireframes)
- Same CSS, JS, JSX files
- Same uploads/ and versions/ subdirectories
- Appears to be a parallel/backup copy

### 8k. Barreletics Design Review 2/ & design_handoff_barreletics 3/

Empty or minimal directories (likely incomplete copies).

---

## 9. Duplicate/Redundant File Mapping

The repository has significant duplication across archives. Canonical locations:

| Content | Canonical Location | Also Found In |
|---------|--------------------|---------------|
| Homepage v10–v24 | `files/` | `barreletics-design-review/Barreletics_All_Versions/` |
| Homepage v1–v9 | `barreletics-design-review/Barreletics Design Review/` | `project/`, `design_handoff_barreletics 2/pages/` |
| Research Bible | `barreletics-design-review/Barreletics_Research_Bible.md` | `uploads/`, `Barreletics_All_Versions/`, `Claude Design Files/` |
| Handoff | `barreletics-design-review/Barreletics_Handoff.md` | `Barreletics_All_Versions/` |
| CSS/JS assets | `barreletics-design-review/Barreletics Design Review/` | `project/`, `design_handoff_barreletics 2/pages/`, version dirs |
| Logo assets | `barreletics-design-review/Barreletics Design Review/` | `project/uploads/`, `design_handoff_barreletics 2/pages/` |
| PDP/Collection protos | `barreletics-design-review/Barreletics Design Review/` | `project/`, `design_handoff_barreletics 2/pages/` |

---

## 10. Proposed INDEX.md Navigation Structure

```markdown
# Barreletics Design Review — Master Index

## Quick Start
- WORKFLOW.md — Operating model, roles, status system
- IMPLEMENTATION-ROADMAP-Jul2026.md — 6-week build plan

## Knowledge Base (docs/)
### Core Brand
- 01-BRAND-NORTH-STAR.md [PENDING REVIEW]
- 02-BRAND-SYSTEM.md [PENDING REVIEW]

### Design & Build
- 03-DESIGN-SYSTEM.md [PENDING REVIEW]
- 04-COMPONENT-LIBRARY.md [APPROVED]
- 05-PDP-ARCHITECTURE.md [APPROVED]
- 06-HOMEPAGE-ARCHITECTURE.md [APPROVED]

### Content & Copy
- 07-COPY-GUIDE.md [PENDING REVIEW]
- 08-CREATIVE-PLAYBOOK.md [STUB]
- 08-LIVE-SITE-COPY-AUDIT.md [APPROVED]

### Product & Decisions
- 09-PRODUCT-KNOWLEDGE.md [PENDING REVIEW]
- 10-DECISIONS.md [STUB]

## ManyChat Knowledge Base (manychat-kb/)
- 16 articles covering product info, sizing, pricing, FAQ, policies,
  brand voice, objection handling, comment snippets

## HTML Prototypes
### Section Builds (sections/)
- 31 individual section prototypes (hero, problem, variants, sock-math, etc.)

### Homepage Versions (files/)
- v10–v24 linear progression

### Standalone Prototypes (root)
- Design System v1.0, PDP v36, Section Decision Matrix v1.0
- Section 26 (Notes from Studio), Section 27 (FAQ), Section 28 (Newsletter)

## Design Archive (barreletics-design-review/)
### Source Material
- Research Bible, Handoff docs, uploaded references

### Version History
- Claude Design Review sessions (v1–v10, matured variants)
- Date-stamped snapshots (2026-05-24 through 2026-05-31)
- All Versions archive (v10–v24)

### Design Assets
- CSS: audit, home-matured, maturation, pages-extras, pdp, section-mocks, wireframes
- JS: audit-behavior, ticker
- JSX: audit-tweaks, home-tweaks, pdp-tweaks, tweaks-panel
- Images: logo, mark, dragonfly logo, screenshots

## Data & Config
- barreletics-decisions-2026-07-09.json — CEO section decisions
- Makefile — PR automation commands

## PR Automation (.github/ + scripts/)
- Workflow, Python/Bash scripts, setup docs, quick reference

## Planning (planning/)
- Background preparation files — not committed
```

---

## 11. Open Questions for INDEX.md Finalization

1. **08- numbering conflict:** CREATIVE-PLAYBOOK and LIVE-SITE-COPY-AUDIT both use `08-`. Should one be renumbered?
2. **Archive cleanup:** `barreletics-design-review/` contains 3+ redundant copies (project/, design_handoff 2/, Barreletics Design Review/). Should INDEX link only canonical locations?
3. **Section coverage gaps:** Sections 02, 05, 11, 16, 17, 22, 27, 28 have no numbered file in `sections/`. Some are covered by named files (27→FAQ, 28→Newsletter at root). Document which are intentionally absent vs pending build.
4. **Manychat KB numbering:** Starts at 02 — is 01 configured in ManyChat directly (system prompt)?
5. **Empty directories:** `Barreletics Design Review 2/`, `design_handoff_barreletics 3/`, `Manychat Content/` appear empty. Flag for cleanup?
6. **files/ vs barreletics-design-review/Barreletics_All_Versions/:** Both contain v10–v24. Which is canonical for INDEX links?
