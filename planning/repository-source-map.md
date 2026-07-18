# Repository Source Map

**Date:** 2026-07-13  
**Status:** PLANNING — do not commit  
**Scope:** Every major source file/group mapped to knowledge-base role

**Legend:**  
- **Status:** Current (active/production-relevant) · Historical (superseded by newer version) · Duplicate (byte-identical copy exists elsewhere) · Superseded (replaced by a docs/ equivalent) · Unknown (role unclear)  
- **Feeds:** Which docs/ file(s) this source feeds into  
- **Referenced By:** Which docs/ file(s) mention this file by name  
- **Unique Content:** Does this file contain information NOT captured in docs/?  
- **Preserve:** Must this file be kept?

---

## 1. Root-Level Files

| File | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `WORKFLOW.md` | Current | docs/10-DECISIONS.md (workflow decisions D-WF-01–D-WF-09) | 10-DECISIONS.md (9 citations) | No — fully extracted into 10-DECISIONS.md | Yes — operating model, authority doc |
| `IMPLEMENTATION-ROADMAP-Jul2026.md` | Current | docs/10-DECISIONS.md (implementation timeline, color mandate) | 10-DECISIONS.md (3 citations) | No — key decisions extracted | Yes — roadmap phases, section assignments |
| `barreletics-decisions-2026-07-09.json` | Current | docs/10-DECISIONS.md (per-section CEO notes) | 10-DECISIONS.md (6 citations) | Yes — raw CEO notes with typos/nuance not in docs | Yes — primary decision record |
| `Barreletics-DesignSystem-v1_0-Jul2026.html` | Current | None directly | None | Yes — standalone design system HTML, not referenced by docs/ | Review — may duplicate docs/03 content |
| `Barreletics-PDP-v36-Jul2026.html` | Current | docs/05-PDP-ARCHITECTURE.md (HTML structure source) | 05-PDP-ARCHITECTURE.md, 09-PRODUCT-KNOWLEDGE.md | No — fully extracted into docs/05 | Yes — canonical PDP mock |
| `Barreletics-Everything-Index.html` | Historical | None | None | Yes — 406KB master index not referenced anywhere | Review — large file, unclear current role |
| `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` | Current | docs/10-DECISIONS.md (cited as source) | 10-DECISIONS.md (1 citation) | Partial — interactive matrix UI not in docs | Yes — decision reference |
| `matrix-20260707.html` | Historical | None | None (but index.html redirects to it) | Yes — earlier matrix version | No — superseded by SectionDecisionMatrix-v1_0 |
| `index.html` | Current | None | None | No — just a redirect to matrix-20260707.html | No — trivial redirect |
| `Section-26-NotesFromStudio.html` | Current | docs/07-COPY-GUIDE.md (copy extracted) | 07-COPY-GUIDE.md | No — copy fully extracted | Yes — source HTML for section 26 |
| `Section-27-FAQ.html` | Current | docs/07-COPY-GUIDE.md (copy extracted) | 07-COPY-GUIDE.md | No — copy fully extracted | Yes — source HTML for section 27 |
| `Section-28-Newsletter.html` | Current | docs/07-COPY-GUIDE.md (copy extracted) | 07-COPY-GUIDE.md | No — copy fully extracted | Yes — source HTML for section 28 |
| `Makefile` | Current | None | None | Yes — PR automation workflow, not documented in docs/ | Yes — tooling |
| `Manychat Content.zip` | Historical | None | None | No — extracted contents in `Manychat Content/` dir | No — archive of extracted content |

---

## 2. `/sections/` Directory (38 HTML Files)

| File/Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `hero.html` | Current | docs/04-COMPONENT-LIBRARY.md (Header/Hero) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `founder-letter.html` | Current | docs/04-COMPONENT-LIBRARY.md (Founder Letter) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `founder2.html` | Current | docs/04-COMPONENT-LIBRARY.md (Founder V2) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `manifesto.html`, `manifesto2.html` | Current | docs/04-COMPONENT-LIBRARY.md (Manifesto) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `problem.html`, `problem2.html` | Current | docs/04-COMPONENT-LIBRARY.md (Problem Statement) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `closing-statement.html` | Current | docs/04-COMPONENT-LIBRARY.md (Closing Statement) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `credibility.html` | Current | docs/04-COMPONENT-LIBRARY.md (Credibility) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `variants.html` | Current | docs/04-COMPONENT-LIBRARY.md (Variant Grid) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `range.html` | Current | docs/04-COMPONENT-LIBRARY.md (Range + Promo) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `assoc.html` | Current | docs/04-COMPONENT-LIBRARY.md (Association) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `sock-math.html` | Current | docs/04 (implicit) | None directly | No — extracted into component library | Yes — reference HTML |
| `split-section.html`, `split-section2.html`, `split-section3.html` | Current | docs/04-COMPONENT-LIBRARY.md (50/50 splits) | 04-COMPONENT-LIBRARY.md | No — component spec extracted | Yes — reference HTML |
| `testimonial.html` | Current | docs/04 (implicit) | None directly | No — extracted into component library | Yes — reference HTML |
| `disciplines.html` | Current | docs/04 (implicit) | None directly | No — extracted into component library | Yes — reference HTML |
| `01-section.html` – `29-section.html` (19 files) | Historical | None | 10-DECISIONS.md ("Do NOT use for production builds; use named sections") | No — design study variations, superseded by named section files | No — explicitly deprecated |

---

## 3. `/files/` Directory (16 Files — Homepage Versions)

| File/Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `Barreletics_Home_v24.html` | Current | docs/06-HOMEPAGE-ARCHITECTURE.md (latest version) | None directly | No — architecture extracted into docs/06 | Yes — latest homepage mock |
| `Barreletics_Home_v10.html` – `v23.html` (14 files) | Historical | None | None | No — superseded by v24 | No — version history, also duplicated in barreletics-design-review/ |
| `index.html` | Current | None | None | No — navigation file for /files/ directory | No — trivial |

---

## 4. `/barreletics-design-review/` Directory (Design Handoff Bundle)

### 4A. Top-Level Files

| File | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `README.md` | Current | None | None | Yes — coding agent instructions for handoff bundle | Yes — meta-documentation |
| `Barreletics_Handoff.md` | Historical | None | 04-COMPONENT-LIBRARY.md (1 citation) | Partial — handoff context (dated May 29) now partially stale | Yes — decision history |
| `Barreletics_Research_Bible.md` | Current | docs/01, 02, 03, 09, 10 (heavily cited) | 01-BRAND-NORTH-STAR.md (17+), 02-BRAND-SYSTEM.md (8+), 03-DESIGN-SYSTEM.md (2), 09-PRODUCT-KNOWLEDGE.md (40+), 10-DECISIONS.md (12+) | Yes — primary source for brand positioning, customer research, competitive analysis; ~70% extracted but raw detail remains | **Yes — critical primary source** |
| `Barreletics_Home_v10.html` | Duplicate | None | None | No — identical to files/Barreletics_Home_v10.html | No |
| `Barreletics_Home_v23.html` | Duplicate | None | None | No — identical to files/Barreletics_Home_v23.html | No |
| `Barreletics_All_Versions.zip` | Historical | None | None | No — archive of version history | No |
| `files.zip` | Historical | None | None | No — archive of files/ directory | No |

### 4B. `Barreletics Design Review/` (Canonical Design Pages)

| File/Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `Barreletics Home - Matured.html` | **Current ★** | docs/03, 06, 07 (canonical home) | 03-DESIGN-SYSTEM.md (marked ★ CANONICAL) | No — fully documented in docs/03, 06, 07 | **Yes — canonical design artifact** |
| `Barreletics PDP - Matured.html` | **Current ★** | docs/03, 05 (canonical PDP) | 03-DESIGN-SYSTEM.md (marked ★ CANONICAL) | No — fully documented in docs/03, 05 | **Yes — canonical design artifact** |
| `Barreletics Collection - Matured.html` | **Current ★** | docs/03 (canonical collection) | 03-DESIGN-SYSTEM.md (marked ★ CANONICAL) | No — fully documented in docs/03 | **Yes — canonical design artifact** |
| `Barreletics Maturation Study.html` | Current | docs/03 (rationale reference) | 03-DESIGN-SYSTEM.md | Yes — current-vs-matured comparison not in docs | Yes — decision rationale |
| `Barreletics Audit.html` | Current | docs/03 (audit rationale) | 03-DESIGN-SYSTEM.md | Yes — original audit reasoning | Yes — decision rationale |
| `Barreletics Wireframes.html` | Current | docs/03 (IA reference) | 03-DESIGN-SYSTEM.md | Yes — lo-fi IA exploration | Yes — IA reference |
| `Barreletics Article*.html` (6 files) | Current | docs/03 (article templates) | 03-DESIGN-SYSTEM.md | No — documented in docs/03 | Yes — article template designs |
| `Barreletics Blog.html` | Current | docs/03 (blog template) | 03-DESIGN-SYSTEM.md | No — documented in docs/03 | Yes — blog template design |
| `Barreletics Home v2…v11.html` (10 files) | Historical | None | 03-DESIGN-SYSTEM.md ("Exploration history, reference only") | No — superseded by Matured version | No — history only |
| `Barreletics PDP v2.html` | Historical | None | 03-DESIGN-SYSTEM.md ("Earlier PDP exploration") | No — superseded | No |
| `Barreletics Collection.html` | Historical | None | 03-DESIGN-SYSTEM.md ("Earlier Collection exploration") | No — superseded | No |
| `Section 15 - Variant Grid v28.html` | Current | docs/03 (variant grid study) | 03-DESIGN-SYSTEM.md | Yes — standalone variant grid study | Yes |
| `audit-styles.css` | **Current ★** | docs/03 (PRIMARY token stylesheet) | 03-DESIGN-SYSTEM.md (marked PRIMARY) | Yes — canonical design tokens as CSS | **Yes — token source of truth** |
| `maturation-styles.css` | Current | docs/03 | 03-DESIGN-SYSTEM.md | Yes — matured-direction tokens | Yes |
| `home-matured.css` | Current | docs/03 | 03-DESIGN-SYSTEM.md | No — documented | Yes |
| `pdp-styles.css` | Current | docs/03, 05 | 03-DESIGN-SYSTEM.md, 05-PDP-ARCHITECTURE.md | No — documented | Yes |
| `pages-extras.css` | Current | docs/03 | 03-DESIGN-SYSTEM.md | No — documented | Yes |
| `wireframes-styles.css` | Current | docs/03 | 03-DESIGN-SYSTEM.md | No — documented | Yes |
| `section-mocks.css` + `section-mocks.html` | Current | docs/03 | 03-DESIGN-SYSTEM.md | No — documented | Yes |
| `*.js`, `*.jsx` (5 files) | Current | None | None | Yes — audit/tweak behavior not in docs | Yes |

### 4C. `Barreletics_All_Versions/` and `Barreletics_All_Versions 2/`

| Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|---------|--------|-------|---------------|----------------|----------|
| All contents | Duplicate | None | None | No — mirrors of `Barreletics Design Review/` | No — per repository-audit.md |

### 4D. `design_handoff_barreletics 2/` and `design_handoff_barreletics 3/`

| Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|---------|--------|-------|---------------|----------------|----------|
| `design_handoff_barreletics 2/README.md` | **Current** | docs/03-DESIGN-SYSTEM.md (Primary Source — verbatim) | 03-DESIGN-SYSTEM.md | No — copied verbatim into docs/03 | **Yes — original handoff README** |
| `design_handoff_barreletics 2/pages/` | Duplicate | None | None | No — mirrors `Barreletics Design Review/` | No |
| `design_handoff_barreletics 3/` | Duplicate | None | None | No — likely older copy | No |

### 4E. `project/`

| Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|---------|--------|-------|---------------|----------------|----------|
| All contents | Duplicate | None | README.md references it | No — byte-identical to `Barreletics Design Review/` | No |

---

## 5. `/manychat-kb/` Directory (15 .md Files + 1 .zip)

| File | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `02-open-vs-closed-sole.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (2), 09-PRODUCT-KNOWLEDGE.md (1) | No — fully extracted | Yes — source record |
| `03-sizing-chart.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (1), 09-PRODUCT-KNOWLEDGE.md (2) | No — fully extracted | Yes — source record |
| `04-pricing.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (3), 09-PRODUCT-KNOWLEDGE.md (2) | No — fully extracted | Yes — source record |
| `05-why-better-than-socks.md` | Superseded | docs/01-BRAND-NORTH-STAR.md, 09-PRODUCT-KNOWLEDGE.md | 01-BRAND-NORTH-STAR.md (4), 09-PRODUCT-KNOWLEDGE.md (2) | No — fully extracted | Yes — source record |
| `06-care-and-cleaning.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (1), 09-PRODUCT-KNOWLEDGE.md (1) | No — fully extracted | Yes — source record |
| `07-returns-and-exchanges.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (3), 09-PRODUCT-KNOWLEDGE.md (1) | No — fully extracted | Yes — source record |
| `08-shipping.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (2), 09-PRODUCT-KNOWLEDGE.md (1) | No — fully extracted | Yes — source record |
| `09-faq-fit-sizing.md` | Superseded | docs/09 (implicit via FAQ sections) | None directly | Possibly — check for FAQ content not in docs/09 | Yes — source record |
| `10-faq-general.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md | 09-PRODUCT-KNOWLEDGE.md (2) | No — fully extracted | Yes — source record |
| `11-sensitive-and-medical.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md, 10-DECISIONS.md | 10-DECISIONS.md (1), 09-PRODUCT-KNOWLEDGE.md (1) | No — fully extracted | Yes — source record |
| `12-brand-voice-and-taglines.md` | Superseded | docs/02-BRAND-SYSTEM.md, 10-DECISIONS.md | 02-BRAND-SYSTEM.md (6), 10-DECISIONS.md (3) | No — fully extracted | Yes — source record |
| `13-direct-links.md` | Current | None | None | Yes — direct links for ManyChat flows, not in docs/ | Yes — operational content |
| `14-escalation-and-handoff.md` | Superseded | docs/10-DECISIONS.md | 10-DECISIONS.md (2) | No — fully extracted | Yes — source record |
| `15-objection-handling.md` | Superseded | docs/09-PRODUCT-KNOWLEDGE.md | 09-PRODUCT-KNOWLEDGE.md (1) | No — fully extracted | Yes — source record |
| `16-comment-snippets.md` | Current | None | None | Yes — social media comment snippets not in docs/ | Yes — operational content |
| `manychat-kb-all-16.zip` | Historical | None | None | No — archive of the above files | No |

---

## 6. `/docs/` Directory (13 Files — Knowledge Base)

| File | Status | Lines | Sources From | Unique Content | Preserve |
|------|--------|-------|--------------|----------------|----------|
| `00-README.md` | Stub | 4 | None | No | Yes — placeholder |
| `01-BRAND-NORTH-STAR.md` | Current (APPROVED implied) | 248 | Research Bible, manychat-kb/05, Shopify product descriptions, 08-LIVE-SITE-COPY-AUDIT | Yes — synthesized brand positioning | **Yes** |
| `02-BRAND-SYSTEM.md` | Current | 175 | Research Bible Sections 1/4/6, manychat-kb/12 | Yes — synthesized brand system | **Yes** |
| `03-DESIGN-SYSTEM.md` | Current | 411 | design_handoff README (verbatim), Research Bible Section 7 | Yes — canonical design system spec | **Yes** |
| `04-COMPONENT-LIBRARY.md` | Current | 1,122 | /sections/ HTML files, Research Bible | Yes — full component catalog | **Yes** |
| `05-PDP-ARCHITECTURE.md` | Current | 2,814 | Barreletics-PDP-v36, PDP - Matured.html, pdp-styles.css | Yes — complete PDP spec | **Yes** |
| `06-HOMEPAGE-ARCHITECTURE.md` | Current | 10,511 | Barreletics Home - Matured.html, CSS files | Yes — full homepage arch with embedded HTML/CSS | **Yes** |
| `07-COPY-GUIDE.md` | Current | 217,636 | All Matured.html files, Section-26/27/28 HTML | Partial — 217K lines includes full embedded HTML (likely needs cleanup) | **Yes** (but bloated) |
| `08-CREATIVE-PLAYBOOK.md` | Stub | 4 | None | No | Yes — placeholder |
| `08-LIVE-SITE-COPY-AUDIT.md` | Current (APPROVED) | 2,257 | Live site crawl (barreletics.com) | Yes — site-wide copy audit | **Yes** |
| `09-PRODUCT-KNOWLEDGE.md` | Current | 1,227 | Research Bible, manychat-kb/*, 08-LIVE-SITE-COPY-AUDIT, Shopify store | Yes — comprehensive product data | **Yes** |
| `10-DECISIONS.md` | Current | 1,092 | All sources (Research Bible, JSON, roadmap, matrix, WORKFLOW, manychat-kb, other docs/) | Yes — master decision registry | **Yes** |
| `INDEX.md` | Current (Stub) | 27 | None (navigation only) | No | Yes — navigation |

---

## 7. `/planning/` Directory (13 Files)

| File | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `repository-audit.md` | Current | None | None | Yes — duplication analysis, cleanup plan | Yes — planning |
| `repository-source-map.md` | Current | None | None | Yes — this file | Yes — planning |
| `knowledge-base-consistency-audit.md` | Current | None | None | Yes — cross-doc consistency findings | Yes — planning |
| `consistency-remediation-plan.md` | Current | None | None | Yes — fix plan for consistency issues | Yes — planning |
| `ADR-01-color-palette-values.md` | Current | None | None | Yes — architecture decision record | Yes — planning |
| `QA-01-BRAND-NORTH-STAR.md` | Current | None | None | Yes — QA results for docs/01 | Yes — planning |
| `QA-02-BRAND-SYSTEM.md` | Current | None | None | Yes — QA results for docs/02 | Yes — planning |
| `QA-03-DESIGN-SYSTEM.md` | Current | None | None | Yes — QA results for docs/03 | Yes — planning |
| `QA-07-COPY-GUIDE.md` | Current | None | None | Yes — QA results for docs/07 | Yes — planning |
| `QA-09-PRODUCT-KNOWLEDGE.md` | Current | None | None | Yes — QA results for docs/09 | Yes — planning |
| `08-creative-playbook-inventory.md` | Current | None | None | Yes — inventory for docs/08 build | Yes — planning |
| `10-decisions-inventory.md` | Current | None | None | Yes — inventory for docs/10 build | Yes — planning |
| `11-shopify-implementation-roadmap-inventory.md` | Current | None | None | Yes — Shopify implementation planning | Yes — planning |
| `INDEX-inventory.md` | Current | None | None | Yes — inventory for INDEX build | Yes — planning |

---

## 8. `/scripts/` Directory (2 Files)

| File | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `create_pr.py` | Current | None | None (called by Makefile) | Yes — PR automation logic | Yes — tooling |
| `pr.sh` | Current | None | None (called by Makefile) | Yes — PR automation fallback | Yes — tooling |

---

## 9. `/.github/` Directory

| File | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `workflows/ai-review-pr.yml` | Current | None | None | Yes — CI workflow for AI PR review | Yes — tooling |
| `PR-AUTOMATION.md` | Current | None | None | Yes — PR automation docs | Yes — tooling docs |
| `QUICK-REFERENCE.md` | Current | None | None | Yes — quick reference for contributors | Yes — tooling docs |
| `SETUP.md` | Current | None | None | Yes — setup instructions | Yes — tooling docs |
| `SYSTEM-OVERVIEW.md` | Current | None | None | Yes — system architecture docs | Yes — tooling docs |

---

## 10. Other

| File/Pattern | Status | Feeds | Referenced By | Unique Content | Preserve |
|------|--------|-------|---------------|----------------|----------|
| `Manychat Content/` (directory) | Historical | None | None | No — empty (zip was extracted but content went to manychat-kb/) | No |
| `Manychat Content.zip` | Historical | None | None | No — archive | No |

---

## Summary: Files Safe to Remove

| Category | Count | Examples |
|----------|-------|---------|
| Duplicate directory trees | ~300 files | `project/`, `Barreletics_All_Versions 2/`, `design_handoff_barreletics 2/pages/`, `design_handoff_barreletics 3/` |
| Historical homepage versions | ~24 files | `files/v10–v23`, `Barreletics Home v2–v11` in design review |
| Deprecated numbered sections | 19 files | `sections/01-section.html` – `29-section.html` |
| Archive zips | 4 files | `Manychat Content.zip`, `manychat-kb-all-16.zip`, `files.zip`, `Barreletics_All_Versions.zip` |
| Superseded files | 2 files | `matrix-20260707.html`, `index.html` (redirect) |
| **Estimated removable** | **~350 files** | |

## Summary: Files That Must Be Preserved

| Category | Key Files |
|----------|-----------|
| Primary sources | `Barreletics_Research_Bible.md`, `barreletics-decisions-2026-07-09.json`, `WORKFLOW.md` |
| Canonical design artifacts | 3 `*-Matured.html` files, `audit-styles.css`, `Barreletics-PDP-v36-Jul2026.html` |
| Named section HTML | 19 files in `/sections/` (hero, founder-letter, variants, etc.) |
| ManyChat KB (source record) | 15 .md files in `/manychat-kb/` |
| Full docs/ knowledge base | 13 files in `/docs/` |
| Planning artifacts | 13 files in `/planning/` |
| Tooling | Makefile, scripts/, .github/ |
| Handoff docs | `barreletics-design-review/README.md`, `Barreletics_Handoff.md`, `design_handoff_barreletics 2/README.md` |

## Unresolved Items

1. **`Barreletics-DesignSystem-v1_0-Jul2026.html`** — 57KB standalone design system HTML at root. Not referenced by any docs/ file. May contain content that overlaps with or supplements `docs/03-DESIGN-SYSTEM.md`. Needs manual review.
2. **`Barreletics-Everything-Index.html`** — 406KB master index at root. Not referenced anywhere. Unclear whether it has ongoing value or is a one-time artifact.
3. **`manychat-kb/09-faq-fit-sizing.md`** — Not directly cited by any docs/ file (unlike all other manychat-kb files). May contain uncaptured FAQ content.
4. **`manychat-kb/13-direct-links.md`** and **`16-comment-snippets.md`** — Operational ManyChat content not extracted into any docs/ file. Unique but outside the design knowledge base scope.
5. **`docs/07-COPY-GUIDE.md`** — At 217,636 lines, this file is abnormally large. It appears to contain full embedded HTML from multiple design files rather than distilled copy guidance. Likely needs restructuring.
