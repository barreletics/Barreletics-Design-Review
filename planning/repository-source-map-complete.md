# Complete Repository Source Map

**Date:** 2026-07-13  
**Status:** PLANNING  
**Scope:** Every file and folder in the repository, mapped with purpose, status, and preservation requirements

**Legend:**  
- **Status:** CURRENT (actively used) · HISTORICAL (superseded, keep for reference) · DUPLICATE (same content elsewhere) · UNKNOWN (needs investigation) · ARCHIVE-SAFE (can be archived without loss)  
- **Feeds:** Which docs/ file(s) this source feeds into  
- **Referenced By:** Which docs/ file(s) mention this file  
- **Unique:** Contains information not captured elsewhere  
- **Preserve:** Must be kept for the build

---

## ROOT DIRECTORY

| File | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|---------|--------|-------|---------------|--------|----------|
| `WORKFLOW.md` | Operating model — roles, status system, sprint ticket format, commit rules | CURRENT | docs/10-DECISIONS.md (workflow decisions D-WF-01–09) | docs/10 (9 citations) | No — fully extracted | Yes — authority doc |
| `IMPLEMENTATION-ROADMAP-Jul2026.md` | 6-week build timeline, phase plan, section assignments | CURRENT | docs/10-DECISIONS.md | docs/10 (3 citations) | No — key decisions extracted | Yes — active roadmap |
| `barreletics-decisions-2026-07-09.json` | Raw CEO decision notes per section (JSON) | CURRENT | docs/10-DECISIONS.md (per-section notes) | docs/10 (6 citations) | Yes — raw notes with nuance not in docs | Yes — primary decision record |
| `Barreletics-DesignSystem-v1_0-Jul2026.html` | Standalone design system HTML spec (57KB) | CURRENT | None directly | None | Yes — interactive HTML format | Review — may duplicate docs/03 |
| `Barreletics-PDP-v36-Jul2026.html` | Canonical PDP mock v36 (52KB) | CURRENT | docs/05-PDP-ARCHITECTURE.md | docs/05, docs/09 | No — fully extracted into docs/05 | Yes — canonical source |
| `Barreletics-Everything-Index.html` | Master index of all content (406KB) | HISTORICAL | None | None | Yes — comprehensive index not captured elsewhere | No — superseded by docs/INDEX.md |
| `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` | Interactive section decision matrix (14KB) | CURRENT | docs/10-DECISIONS.md | docs/10 (1 citation) | Partial — interactive UI | Yes — decision reference |
| `matrix-20260707.html` | Earlier matrix version (11KB) | HISTORICAL | None | None (index.html redirects here) | No — superseded by SectionDecisionMatrix v1_0 | No — superseded |
| `index.html` | Redirect page → matrix-20260707.html | ARCHIVE-SAFE | None | None | No — trivial redirect | No |
| `Section-26-NotesFromStudio.html` | Section 26 source HTML (4.4KB) | CURRENT | docs/07-COPY-GUIDE.md | docs/07 | No — copy extracted | Yes — source HTML |
| `Section-27-FAQ.html` | Section 27 source HTML (4.6KB) | CURRENT | docs/07-COPY-GUIDE.md | docs/07 | No — copy extracted | Yes — source HTML |
| `Section-28-Newsletter.html` | Section 28 source HTML (4.4KB) | CURRENT | docs/07-COPY-GUIDE.md | docs/07 | No — copy extracted | Yes — source HTML |
| `Makefile` | PR automation, build commands, workflow shortcuts (3.2KB) | CURRENT | None | None | Yes — tooling not documented elsewhere | Yes — tooling |
| `Manychat Content.zip` | Archive of extracted ManyChat KB files (22KB) | ARCHIVE-SAFE | None | None | No — contents extracted to `Manychat Content/` | No — redundant archive |
| `Manychat Content/` | Directory — contains only .DS_Store | ARCHIVE-SAFE | None | None | No — empty | No |

---

## /docs/ DIRECTORY (13 files)

The canonical knowledge base. All implementation references come from here.

| File | Lines | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|-------|---------|--------|-------|---------------|--------|----------|
| `00-README.md` | 4 | Directory readme / stub | CURRENT | None | None | No | Yes — structural |
| `01-BRAND-NORTH-STAR.md` | 248 | Brand WHY, origin story, positioning, audience | PENDING REVIEW | Implementation (voice/tone for all copy) | planning/review-01, QA-01 | Yes — canonical brand foundation | Yes |
| `02-BRAND-SYSTEM.md` | 175 | Voice, tone, messaging framework | PENDING REVIEW | Implementation (copy guidelines) | planning/review-02, QA-02 | Yes — canonical voice guide | Yes |
| `03-DESIGN-SYSTEM.md` | 411 | Design tokens, principles, architecture rules | PENDING REVIEW | Sprint 16 (token file generation) | planning/review-03, QA-03, ADR-01–07 | Yes — canonical tokens | Yes |
| `04-COMPONENT-LIBRARY.md` | 1,122 | Reusable component specs, layout patterns | APPROVED | All Shopify section builds | planning/consistency-remediation-plan (multiple) | Yes — implementation blueprint | Yes |
| `05-PDP-ARCHITECTURE.md` | 2,814 | Complete PDP HTML/CSS specification | APPROVED | Sprints 21–30 (PDP build) | planning/consistency-remediation-plan, ADR-03, ADR-05 | Yes — PDP source of truth | Yes |
| `06-HOMEPAGE-ARCHITECTURE.md` | 10,511 | Complete homepage HTML/CSS specification | APPROVED | Sprints 31–40 (homepage build) | planning/consistency-remediation-plan, ADR-01 | Yes — homepage source of truth | Yes |
| `07-COPY-GUIDE.md` | 217,636 | Lossless copy archive — all approved HTML copy | PENDING REVIEW | All builds (copy source) | planning/review-07, QA-07 | Yes — canonical copy | Yes |
| `08-CREATIVE-PLAYBOOK.md` | 4 | Stub — not yet built | STUB | None | None | No | Yes — placeholder |
| `08-LIVE-SITE-COPY-AUDIT.md` | 2,257 | Evidence-based audit of 46 live site URLs | APPROVED | docs/09, docs/10 (evidence) | planning/08-creative-playbook-inventory | Yes — live site snapshot | Yes |
| `09-PRODUCT-KNOWLEDGE.md` | 1,227 | Product facts, specs, variants, materials | PENDING REVIEW | PDP build (product content) | planning/review-09, QA-09 | Yes — canonical product data | Yes |
| `10-DECISIONS.md` | 1,092 | Complete decision log (all D- and C- items) | PENDING REVIEW | ADR resolution, remediation | planning/review-10, all ADRs | Yes — decision authority | Yes |
| `INDEX.md` | 27 | Index/table of contents for docs/ | CURRENT | None | None | No — structural | Yes |

---

## /planning/ DIRECTORY (27 files)

Planning artifacts — not committed to main. Working documents for build coordination.

| File | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `08-creative-playbook-inventory.md` | Inventory/gap analysis for creative playbook doc | CURRENT | Yes — active planning |
| `10-decisions-inventory.md` | Full inventory of decisions document content | CURRENT | Yes — active planning |
| `11-shopify-implementation-roadmap-inventory.md` | Detailed Shopify implementation planning | CURRENT | Yes — active planning |
| `ADR-01-color-palette-values.md` | Architecture Decision Record — color palette conflict | CURRENT | Yes — pending resolution |
| `ADR-02-free-shipping-threshold.md` | ADR — shipping threshold ($75 vs $150) | CURRENT | Yes — pending resolution |
| `ADR-03-button-border-radius.md` | ADR — button radius (0px vs 6px) | CURRENT | Yes — pending resolution |
| `ADR-04-eyebrow-letter-spacing.md` | ADR — eyebrow letter-spacing value | CURRENT | Yes — pending resolution |
| `ADR-05-pdp-text-color.md` | ADR — text color (#1c1916 vs #050505) | CURRENT | Yes — pending resolution |
| `ADR-06-review-card-radius.md` | ADR — review card border-radius | CURRENT | Yes — pending resolution |
| `ADR-07-star-rating-color.md` | ADR — star rating fill color | CURRENT | Yes — pending resolution |
| `INDEX-inventory.md` | Inventory analysis of docs/INDEX.md | CURRENT | Yes — active planning |
| `QA-01-BRAND-NORTH-STAR.md` | QA checklist for docs/01 review | CURRENT | Yes — review support |
| `QA-02-BRAND-SYSTEM.md` | QA checklist for docs/02 review | CURRENT | Yes — review support |
| `QA-03-DESIGN-SYSTEM.md` | QA checklist for docs/03 review | CURRENT | Yes — review support |
| `QA-07-COPY-GUIDE.md` | QA checklist for docs/07 review | CURRENT | Yes — review support |
| `QA-09-PRODUCT-KNOWLEDGE.md` | QA checklist for docs/09 review | CURRENT | Yes — review support |
| `architecture-governance-summary.md` | Current state summary — metrics, status, conflicts | CURRENT | Yes — reference |
| `consistency-remediation-plan.md` | 30 remediation tickets for all findings | CURRENT | Yes — implementation queue |
| `knowledge-base-consistency-audit.md` | Audit report — 30 findings across docs/ | CURRENT | Yes — source for remediation |
| `repository-audit.md` | Repository structure audit | CURRENT | Yes — reference |
| `repository-source-map.md` | Source map (predecessor to this file) | CURRENT | Superseded by this file |
| `review-01-brand-north-star.md` | Review packet for docs/01 (ChatGPT) | CURRENT | Yes — review support |
| `review-02-brand-system.md` | Review packet for docs/02 | CURRENT | Yes — review support |
| `review-03-design-system.md` | Review packet for docs/03 | CURRENT | Yes — review support |
| `review-07-copy-guide.md` | Review packet for docs/07 | CURRENT | Yes — review support |
| `review-09-product-knowledge.md` | Review packet for docs/09 | CURRENT | Yes — review support |
| `review-10-decisions.md` | Review packet for docs/10 | CURRENT | Yes — review support |

---

## /manychat-kb/ DIRECTORY (16 .md files + 1 zip)

ManyChat customer service knowledge base articles. Used by automated chat responses.

| File | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|---------|--------|-------|---------------|--------|----------|
| `02-open-vs-closed-sole.md` | Product explanation: sole design | CURRENT | docs/09 (product facts) | None | Partial — some detail not in docs/09 | Yes — active chatbot |
| `03-sizing-chart.md` | Size chart and fit guide | CURRENT | docs/09 (sizing) | None | Partial — chatbot-specific formatting | Yes — active chatbot |
| `04-pricing.md` | Pricing information | CURRENT | docs/09 (pricing) | None | No — pricing in docs/09 | Yes — active chatbot |
| `05-why-better-than-socks.md` | Competitive positioning vs socks | CURRENT | docs/01 (positioning) | None | Partial — chatbot-specific arguments | Yes — active chatbot |
| `06-care-and-cleaning.md` | Care instructions | CURRENT | docs/09 (care) | None | No — care info in docs/09 | Yes — active chatbot |
| `07-returns-and-exchanges.md` | Return policy | CURRENT | docs/09 (policies) | None | No — policy in docs/09 | Yes — active chatbot |
| `08-shipping.md` | Shipping information + $150 threshold | CURRENT | docs/09 (shipping) | None | No — shipping in docs/09 | Yes — active chatbot |
| `09-faq-fit-sizing.md` | FAQ: fit and sizing questions | CURRENT | docs/09 (FAQ content) | None | Partial — Q&A format unique | Yes — active chatbot |
| `10-faq-general.md` | FAQ: general questions | CURRENT | docs/09 (FAQ content) | None | Partial — Q&A format unique | Yes — active chatbot |
| `11-sensitive-and-medical.md` | Medical/sensitivity disclaimers | CURRENT | None | None | Yes — not in docs/ | Yes — active chatbot |
| `12-brand-voice-and-taglines.md` | Brand voice for chatbot responses | CURRENT | docs/01, docs/02 (voice) | None | Partial — chatbot-specific tone | Yes — active chatbot |
| `13-direct-links.md` | Key URLs for chatbot responses | CURRENT | None | None | Yes — URL directory unique | Yes — active chatbot |
| `14-escalation-and-handoff.md` | Escalation protocols | CURRENT | None | None | Yes — not documented elsewhere | Yes — active chatbot |
| `15-objection-handling.md` | Objection handling scripts | CURRENT | docs/01 (positioning) | None | Yes — sales scripts unique | Yes — active chatbot |
| `16-comment-snippets.md` | Social media comment response templates | CURRENT | None | None | Yes — unique content | Yes — active chatbot |
| `manychat-kb-all-16.zip` | Archive of all 16 KB files | ARCHIVE-SAFE | None | None | No — contents are the .md files above | No — redundant |

---

## /sections/ DIRECTORY (39 HTML files)

Homepage section HTML mocks — used as reference for Shopify implementation.

### Named Sections (Current — reference HTML for builds)

| File | Size | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|------|---------|--------|-------|---------------|--------|----------|
| `hero.html` | 175KB | Hero section mock | CURRENT | docs/04 (Header/Hero component) | docs/04 | No — spec extracted | Yes — reference |
| `founder-letter.html` | 175KB | Founder letter section | CURRENT | docs/04 (Founder Letter) | docs/04 | No — spec extracted | Yes — reference |
| `founder2.html` | 176KB | Founder section v2 | CURRENT | docs/04 (Founder V2) | docs/04 | No — spec extracted | Yes — reference |
| `manifesto.html` | 175KB | Manifesto section | CURRENT | docs/04 (Manifesto) | docs/04 | No — spec extracted | Yes — reference |
| `manifesto2.html` | 175KB | Manifesto section v2 | CURRENT | docs/04 (Manifesto) | docs/04 | No — spec extracted | Yes — reference |
| `problem.html` | 175KB | Problem statement section | CURRENT | docs/04 (Problem Statement) | docs/04 | No — spec extracted | Yes — reference |
| `problem2.html` | 175KB | Problem statement v2 | CURRENT | docs/04 (Problem Statement) | docs/04 | No — spec extracted | Yes — reference |
| `closing-statement.html` | 3KB | Closing CTA section | CURRENT | docs/04 (Closing Statement) | docs/04 | No — spec extracted | Yes — reference |
| `credibility.html` | 176KB | Credibility/trust section | CURRENT | docs/04 (Credibility) | docs/04 | No — spec extracted | Yes — reference |
| `variants.html` | 177KB | Variant grid section | CURRENT | docs/04 (Variant Grid) | docs/04 | No — spec extracted | Yes — reference |
| `range.html` | 178KB | Range + promo section | CURRENT | docs/04 (Range + Promo) | docs/04 | No — spec extracted | Yes — reference |
| `assoc.html` | 174KB | Association section | CURRENT | docs/04 (Association) | docs/04 | No — spec extracted | Yes — reference |
| `sock-math.html` | 175KB | Sock math comparison | CURRENT | docs/04 (implicit) | None directly | No — extracted | Yes — reference |
| `split-section.html` | 175KB | 50/50 split layout | CURRENT | docs/04 (50/50 splits) | docs/04 | No — spec extracted | Yes — reference |
| `split-section2.html` | 175KB | 50/50 split v2 | CURRENT | docs/04 (50/50 splits) | docs/04 | No — spec extracted | Yes — reference |
| `split-section3.html` | 174KB | 50/50 split v3 | CURRENT | docs/04 (50/50 splits) | docs/04 | No — spec extracted | Yes — reference |
| `testimonial.html` | 175KB | Testimonial section | CURRENT | docs/04 (implicit) | None directly | No — extracted | Yes — reference |
| `disciplines.html` | 175KB | Disciplines/activities section | CURRENT | docs/04 (implicit) | None directly | No — extracted | Yes — reference |

### Numbered Sections (Historical — deprecated design study variations)

| File | Size | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|------|---------|--------|-------|---------------|--------|----------|
| `01-section.html` | 174KB | Study variation — Section 01 | HISTORICAL | None | docs/10 (deprecated note) | No | No — explicitly deprecated |
| `03-section.html` | 174KB | Study variation — Section 03 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `04-section.html` | 174KB | Study variation — Section 04 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `06-section.html` | 174KB | Study variation — Section 06 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `07-section.html` | 174KB | Study variation — Section 07 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `08-section.html` | 174KB | Study variation — Section 08 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `09-section.html` | 174KB | Study variation — Section 09 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `10-section.html` | 174KB | Study variation — Section 10 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `12-section.html` | 174KB | Study variation — Section 12 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `13-section.html` | 174KB | Study variation — Section 13 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `14-section.html` | 174KB | Study variation — Section 14 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `15-section.html` | 174KB | Study variation — Section 15 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `18-section.html` | 174KB | Study variation — Section 18 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `19-section.html` | 174KB | Study variation — Section 19 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `20-section.html` | 174KB | Study variation — Section 20 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `21-section.html` | 174KB | Study variation — Section 21 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `23-section.html` | 174KB | Study variation — Section 23 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `24-section.html` | 174KB | Study variation — Section 24 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `25-section.html` | 174KB | Study variation — Section 25 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `26-section.html` | 174KB | Study variation — Section 26 | HISTORICAL | None | docs/10 | No | No — deprecated |
| `29-section.html` | 174KB | Study variation — Section 29 | HISTORICAL | None | docs/10 | No | No — deprecated |

---

## /files/ DIRECTORY (16 HTML files + 1 index)

Homepage version history — sequential design iterations (v10–v24).

| File | Size | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|------|---------|--------|-------|---------------|--------|----------|
| `Barreletics_Home_v10.html` | 113KB | Homepage version 10 | HISTORICAL | docs/06 (early reference) | None | No — superseded by v24 | No — historical |
| `Barreletics_Home_v11.html` | 131KB | Homepage version 11 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v12.html` | 130KB | Homepage version 12 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v13.html` | 134KB | Homepage version 13 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v14.html` | 135KB | Homepage version 14 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v15.html` | 136KB | Homepage version 15 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v16.html` | 137KB | Homepage version 16 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v17.html` | 139KB | Homepage version 17 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v18.html` | 143KB | Homepage version 18 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v19.html` | 143KB | Homepage version 19 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v20.html` | 146KB | Homepage version 20 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v21.html` | 151KB | Homepage version 21 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v22.html` | 152KB | Homepage version 22 | HISTORICAL | None | None | No | No — historical |
| `Barreletics_Home_v23.html` | 152KB | Homepage version 23 | HISTORICAL | docs/06 (matured reference) | None | No — same as v22 (identical size) | No — duplicate |
| `Barreletics_Home_v24.html` | 153KB | Homepage version 24 (latest) | CURRENT | docs/06-HOMEPAGE-ARCHITECTURE.md | docs/06 | No — extracted into docs/06 | Yes — canonical latest |
| `index.html` | 253B | Directory index / redirect | ARCHIVE-SAFE | None | None | No | No |

---

## /barreletics-design-review/ DIRECTORY

Original design handoff package from Claude Design project. Contains the full project history.

### Root Level

| File | Size | Purpose | Status | Feeds | Referenced By | Unique | Preserve |
|------|------|---------|--------|-------|---------------|--------|----------|
| `Barreletics_Handoff.md` | 569B | Brief handoff notes | HISTORICAL | None | None | No — minimal content | No |
| `Barreletics_Home_v10.html` | 113KB | Homepage v10 (duplicate of files/) | DUPLICATE | None | None | No | No — duplicate |
| `Barreletics_Home_v23.html` | 152KB | Homepage v23 (duplicate of files/) | DUPLICATE | None | None | No | No — duplicate |
| `Barreletics_Research_Bible.md` | 18KB | Research Bible — original source material | CURRENT | docs/01, docs/02, docs/09 | docs/01, docs/02 (sourced from) | Partial — some raw research not in docs | Yes — source material |
| `README.md` | 1.5KB | Project readme | HISTORICAL | None | None | No | No |
| `Barreletics_All_Versions.zip` | 397KB | Zip of all versions directory | ARCHIVE-SAFE | None | None | No — contents extracted | No |
| `files.zip` | 386KB | Zip of files | ARCHIVE-SAFE | None | None | No — contents extracted | No |

### /barreletics-design-review/Barreletics Design Review/ (Main Project Directory)

#### HTML Design Files

| File | Purpose | Status | Feeds | Unique | Preserve |
|------|---------|--------|-------|--------|----------|
| `Barreletics Article.html` | Article page template (original) | CURRENT | docs/04 (article component) | Yes — article layout | Yes |
| `Barreletics Article 02 Founder.html` | Article: Founder story | CURRENT | docs/07 (copy source) | Yes — article content | Yes |
| `Barreletics Article 03 Coperni.html` | Article: Coperni collaboration | CURRENT | docs/07 (copy source) | Yes — article content | Yes |
| `Barreletics Article 04 Teacher.html` | Article: Teacher story | CURRENT | docs/07 (copy source) | Yes — article content | Yes |
| `Barreletics Article 05 Retire.html` | Article: Retirement story | CURRENT | docs/07 (copy source) | Yes — article content | Yes |
| `Barreletics Article 06 Barefoot.html` | Article: Barefoot story | CURRENT | docs/07 (copy source) | Yes — article content | Yes |
| `Barreletics Audit.html` | Design audit document (33KB) | HISTORICAL | None | Yes — audit findings | No — superseded by docs/08-LIVE-SITE-COPY-AUDIT |
| `Barreletics Blog.html` | Blog index page design | CURRENT | None | Yes — blog layout | Yes |
| `Barreletics Collection - Matured.html` | Collection page — matured direction | CURRENT | None | Yes — collection design | Yes — latest collection |
| `Barreletics Collection.html` | Collection page — original | HISTORICAL | None | No — superseded by matured | No |
| `Barreletics Home - Matured.html` | Homepage — matured direction (158KB) | CURRENT | docs/06 (primary source) | No — extracted into docs/06 | Yes — source HTML |
| `Barreletics Home v10.html` | Homepage v10 | HISTORICAL | None | No | No |
| `Barreletics Home v2.html` through `v9.html` | Homepage iterations v2–v9 | HISTORICAL | None | No | No — historical |
| `Barreletics Home.html` | Homepage original | HISTORICAL | None | No | No — v1 |
| `Barreletics Maturation Study.html` | Full maturation study (102KB) | CURRENT | docs/06 (design rationale) | Yes — design evolution reasoning | Yes — unique context |
| `Barreletics PDP - Matured.html` | PDP — matured direction | CURRENT | docs/05-PDP-ARCHITECTURE.md | No — extracted into docs/05 | Yes — source |
| `Barreletics PDP v2.html` | PDP version 2 | HISTORICAL | None | No | No |
| `Barreletics PDP.html` | PDP original | HISTORICAL | None | No | No |
| `Barreletics Wireframes.html` | Wireframe layouts (64KB) | HISTORICAL | None | Yes — early layout thinking | No — superseded by mocks |
| `Section 15 - Variant Grid v28.html` | Variant grid section (8KB) | CURRENT | docs/04 (variant grid) | Partial | Yes — specific variant reference |

#### CSS Files

| File | Size | Purpose | Status | Unique | Preserve |
|------|------|---------|--------|--------|----------|
| `audit-styles.css` | 20KB | Audit page styling | HISTORICAL | No | No |
| `home-matured.css` | 8KB | Matured homepage CSS | CURRENT | No — extracted into docs/06 | Yes — CSS reference |
| `maturation-styles.css` | 44KB | Maturation study styling | CURRENT | Partial — design token values | Yes — reference |
| `pages-extras.css` | 33KB | Extra page styles (collection, blog, article) | CURRENT | Yes — collection/blog styles not in docs | Yes |
| `pdp-styles.css` | 31KB | PDP CSS | CURRENT | No — extracted into docs/05 | Yes — CSS reference |
| `section-mocks.css` | 21KB | Section mock styling | CURRENT | No — extracted into docs/04 | Yes — reference |
| `wireframes-styles.css` | 21KB | Wireframe styling | HISTORICAL | No | No |

#### JavaScript/JSX Files

| File | Size | Purpose | Status | Unique | Preserve |
|------|------|---------|--------|--------|----------|
| `audit-behavior.js` | 1KB | Audit page interactions | HISTORICAL | No | No |
| `audit-tweaks.jsx` | 4KB | Audit UI tweaks | HISTORICAL | No | No |
| `home-tweaks.jsx` | 2KB | Homepage interaction tweaks | CURRENT | Yes — behavior logic | Yes |
| `pdp-tweaks.jsx` | 2KB | PDP interaction tweaks | CURRENT | Yes — behavior logic | Yes |
| `ticker.js` | 417B | Scrolling ticker animation | CURRENT | Yes — animation code | Yes |
| `tweaks-panel.jsx` | 25KB | Interactive tweaks panel | CURRENT | Yes — development tool | Yes |

#### Assets

| File | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `barreletics-logo.png` | Logo image (10KB) | CURRENT | Yes |
| `barreletics-mark.png` | Brand mark image (9KB) | CURRENT | Yes |
| `section-mocks.html` | All section mocks combined (61KB) | CURRENT | Yes — master reference |

#### /screenshots/ (19 PNG files)

Design review screenshots documenting visual progress.

| Files | Purpose | Status | Preserve |
|-------|---------|--------|----------|
| `01-teal-sections.png`, `02-teal-sections.png` | Color study screenshots | HISTORICAL | No — reference only |
| `01-v10-check.png`, `02-v10-check.png` | V10 review screenshots | HISTORICAL | No |
| `01-v10b.png` through `04-v10b.png` | V10b iteration screenshots | HISTORICAL | No |
| `after-50-50.png`, `after-sockmath.png` | Before/after comparisons | CURRENT | Yes — design evidence |
| `colorway-lab.png` | Color exploration screenshot | HISTORICAL | No |
| `review-50-50.png`, `review-sockmath.png` | Review round screenshots | CURRENT | Yes — design evidence |
| `study-check.png`, `study-overview.png` | Study documentation | CURRENT | Yes |
| `v10-hero.png`, `v10-sockmath.png` | V10 specific screenshots | HISTORICAL | No |
| `v2-50-50.png`, `v2-sockmath.png` | V2 comparison screenshots | HISTORICAL | No |

#### /versions/ (11 date-stamped subdirectories)

Build version snapshots by date.

| Directory | Purpose | Status | Preserve |
|-----------|---------|--------|----------|
| `2026-05-24` | First build date | HISTORICAL | No — superseded |
| `2026-05-25` | Second build | HISTORICAL | No |
| `2026-05-25-batch` | Batch update | HISTORICAL | No |
| `2026-05-25-coperni-vid` | Coperni video version | HISTORICAL | No |
| `2026-05-25-v4-prebuild` | V4 pre-build | HISTORICAL | No |
| `2026-05-25-v4-video` | V4 with video | HISTORICAL | No |
| `2026-05-25-v5` | V5 build | HISTORICAL | No |
| `2026-05-26-v6` | V6 build | HISTORICAL | No |
| `2026-05-26-v7v8` | V7/V8 builds | HISTORICAL | No |
| `2026-05-26-v9` | V9 build | HISTORICAL | No |
| `2026-05-31` | Final May build | HISTORICAL | No |

#### /uploads/ (49 files)

Original source uploads — design handoff materials, screenshots, PDFs.

| File/Group | Purpose | Status | Unique | Preserve |
|------------|---------|--------|--------|----------|
| `Barreletics_Complete_Handoff_for_ClaudeDesign.md` | Full design handoff document | CURRENT | Yes — complete handoff brief | Yes — source material |
| `Barreletics_Content_From_website/` | Directory of live site content captures | CURRENT | Yes — raw site content | Yes |
| `Barreletics_ManyChat_Knowledge.md` | ManyChat KB master document | CURRENT | No — extracted to manychat-kb/ | No — duplicate |
| `Barreletics_Research_Bible.md` | Research Bible (duplicate) | DUPLICATE | No | No — exists at parent level |
| `Barreletics_v28_1_BASE.html` | V28.1 base HTML | CURRENT | Partial — early PDP reference | Yes |
| `Claude Design Files/` | Subdirectory with Claude design files | CURRENT | Yes — original AI design assets | Yes |
| `Copy of Barreletics-Dragonfly-Logo-Black.pdf` | Logo PDF | CURRENT | No — same as .png | Yes — print format |
| `Copy of Barreletics-Dragonfly-Logo-Black.png` | Logo PNG | DUPLICATE | No | No — duplicate of barreletics-logo.png |
| `Dragonly-Logo-Black.pdf`, `.png` | Logo variations | CURRENT | No — same logo | Yes — originals |
| `More content.pdf` | Additional content document | UNKNOWN | Unknown — needs investigation | Review |
| `Screenshot 2026-05-24 *.png` (28 files) | Design review screenshots from May 24 | HISTORICAL | No — documented in screenshots/ | No |
| `Screenshot 2026-05-30 *.png` | May 30 screenshot | HISTORICAL | No | No |
| `barreletics-pdp-live.pdf` | Live PDP screenshot/export | CURRENT | Yes — live site reference | Yes |
| `pasted-*.png` | Pasted image | UNKNOWN | Unknown | Review |
| `screencapture-barreletics-collections-*.pdf` | Collection page capture | CURRENT | Yes — live collection reference | Yes |
| `screencapture-barreletics-products-*.pdf` (2 files) | PDP page captures | CURRENT | Yes — live PDP reference | Yes |

#### /export/

| File | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `Barreletics Maturation Study - Bundled.html` | Bundled export of maturation study | DUPLICATE | No — same as parent `Barreletics Maturation Study.html` |

#### /mocks/

| File | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `index.html` | Mocks index page | UNKNOWN | Review |

### /barreletics-design-review/Barreletics_All_Versions/ (18 HTML + 1 .md + 1 index)

Extracted version archive. Contains homepage iterations v10–v24 + Research Bible.

| File | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `Barreletics_Home_v10.html` – `v24.html` | 15 homepage versions | HISTORICAL (except v24) | No — duplicates of /files/ |
| `Barreletics_Handoff.md` | Handoff document (5KB version) | HISTORICAL | No — duplicate |
| `Barreletics_Research_Bible.md` | Research Bible | DUPLICATE | No — exists elsewhere |
| `index.html` | Directory index | ARCHIVE-SAFE | No |

### /barreletics-design-review/Barreletics Design Review 2/ (empty)

| Purpose | Status | Preserve |
|---------|--------|----------|
| Empty directory (permissions restricted) | ARCHIVE-SAFE | No |

### /barreletics-design-review/Barreletics_All_Versions 2/ (empty)

| Purpose | Status | Preserve |
|---------|--------|----------|
| Empty directory (permissions restricted) | ARCHIVE-SAFE | No |

### /barreletics-design-review/design_handoff_barreletics 2/

| File | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `README.md` | Handoff readme | HISTORICAL | No |
| `pages/` | Directory with page HTML files | HISTORICAL | Review — may contain unique variations |

### /barreletics-design-review/design_handoff_barreletics 3/ (empty)

| Purpose | Status | Preserve |
|---------|--------|----------|
| Empty directory (permissions restricted) | ARCHIVE-SAFE | No |

### /barreletics-design-review/project/ (Main Working Project — 39 HTML + CSS/JS + assets)

Mirror of the `Barreletics Design Review/` directory with additional "Final" versions.

| Notable Differences from Parent | Purpose | Status | Preserve |
|------|---------|--------|----------|
| `Barreletics Collection - Final.html` | Final collection design | CURRENT | Yes — latest collection |
| `Barreletics Collection - Matured.html` | Matured collection (also in parent) | DUPLICATE | No |
| `Barreletics Home - Final.html` | Final homepage design | CURRENT | Yes — may differ from Matured |
| `Barreletics Home - Patched.html` | Patched homepage | CURRENT | Yes — hotfix version |
| `Barreletics Home v11.html` | V11 (not in parent) | HISTORICAL | No |
| `Barreletics PDP - Final.html` | Final PDP design | CURRENT | Yes — latest PDP |
| `Barreletics PDP - Matured.html` | Matured PDP (also in parent) | DUPLICATE | No |
| All other files | Same as parent directory | DUPLICATE | No |
| `/uploads/` (41 files) | Similar to parent uploads | DUPLICATE | No — mostly same |
| `/versions/` (10 dirs) | Same date directories | DUPLICATE | No |

---

## /.github/ DIRECTORY

CI/CD and automation configuration.

| File | Purpose | Status | Feeds | Unique | Preserve |
|------|---------|--------|-------|--------|----------|
| `PR-AUTOMATION.md` | PR automation documentation (13KB) | CURRENT | None | Yes — workflow docs | Yes |
| `QUICK-REFERENCE.md` | Quick reference for PR workflow (2.5KB) | CURRENT | None | Yes | Yes |
| `SETUP.md` | Setup instructions (7KB) | CURRENT | None | Yes | Yes |
| `SYSTEM-OVERVIEW.md` | System overview documentation (11KB) | CURRENT | None | Yes | Yes |
| `workflows/ai-review-pr.yml` | GitHub Actions: AI PR review | CURRENT | None | Yes | Yes |

---

## /scripts/ DIRECTORY

Build/automation scripts.

| File | Size | Purpose | Status | Unique | Preserve |
|------|------|---------|--------|--------|----------|
| `create_pr.py` | 9KB | Python script for PR creation | CURRENT | Yes — automation code | Yes |
| `pr.sh` | 4KB | Shell script for PR workflow | CURRENT | Yes — automation code | Yes |

---

## SUMMARY STATISTICS

| Category | Files | CURRENT | HISTORICAL | DUPLICATE | ARCHIVE-SAFE |
|----------|-------|---------|------------|-----------|--------------|
| Root | 15 | 10 | 2 | 0 | 3 |
| /docs/ | 13 | 13 | 0 | 0 | 0 |
| /planning/ | 27 | 27 | 0 | 0 | 0 |
| /manychat-kb/ | 17 | 16 | 0 | 0 | 1 |
| /sections/ | 39 | 18 | 21 | 0 | 0 |
| /files/ | 17 | 1 | 15 | 0 | 1 |
| /barreletics-design-review/ | ~150+ | ~30 | ~80 | ~30 | ~10 |
| /.github/ | 5 | 5 | 0 | 0 | 0 |
| /scripts/ | 2 | 2 | 0 | 0 | 0 |

### Archive Candidates (safe to move to `/archive/` without build impact)

1. All numbered `NN-section.html` files in /sections/ (21 files, ~3.6MB)
2. All /files/ versions except v24 (14 files, ~2MB)
3. All zips: `Manychat Content.zip`, `Barreletics_All_Versions.zip`, `files.zip`, `manychat-kb-all-16.zip`
4. Empty directories: `Barreletics Design Review 2/`, `Barreletics_All_Versions 2/`, `design_handoff_barreletics 3/`
5. Duplicate files across `barreletics-design-review/project/` and `barreletics-design-review/Barreletics Design Review/`
6. `matrix-20260707.html` and root `index.html`

### Must Preserve for Build

1. All `/docs/` files (canonical knowledge base)
2. All `/planning/` files (active planning)
3. Named sections in `/sections/` (18 reference HTMLs)
4. `/files/Barreletics_Home_v24.html` (latest homepage)
5. Root decision files: `WORKFLOW.md`, `IMPLEMENTATION-ROADMAP-Jul2026.md`, `barreletics-decisions-2026-07-09.json`
6. Root HTML mocks: `Barreletics-PDP-v36-Jul2026.html`, `Barreletics-DesignSystem-v1_0-Jul2026.html`, `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html`
7. All `/manychat-kb/` .md files (active chatbot)
8. `/.github/` and `/scripts/` (automation)
9. `Makefile` (tooling)
10. `barreletics-design-review/Barreletics Design Review/` — key "Final" and "Matured" versions, CSS files, JSX files, logo assets
