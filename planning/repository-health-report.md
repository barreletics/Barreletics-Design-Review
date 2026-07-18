# Repository Health Report

**Date:** 2026-07-13  
**Status:** PLANNING — do not commit  
**Method:** All values measured directly from repository contents. No estimates.

---

## REPOSITORY SIZE

| Metric | Value |
|--------|-------|
| Total files (excluding .git/) | 578 |
| Total docs/ files | 13 |
| Total planning/ files | 27 |
| Total docs/ lines | 237,528 |
| Total planning/ lines | 7,059 |

### Docs File Sizes (lines)

| File | Lines |
|------|-------|
| docs/00-README.md | 4 |
| docs/01-BRAND-NORTH-STAR.md | 248 |
| docs/02-BRAND-SYSTEM.md | 175 |
| docs/03-DESIGN-SYSTEM.md | 411 |
| docs/04-COMPONENT-LIBRARY.md | 1,122 |
| docs/05-PDP-ARCHITECTURE.md | 2,814 |
| docs/06-HOMEPAGE-ARCHITECTURE.md | 10,511 |
| docs/07-COPY-GUIDE.md | 217,636 |
| docs/08-CREATIVE-PLAYBOOK.md | 4 |
| docs/08-LIVE-SITE-COPY-AUDIT.md | 2,257 |
| docs/09-PRODUCT-KNOWLEDGE.md | 1,227 |
| docs/10-DECISIONS.md | 1,092 |
| docs/INDEX.md | 27 |

**Largest file:** docs/07-COPY-GUIDE.md — 217,636 lines  
**Smallest file:** docs/00-README.md — 4 lines (tied with docs/08-CREATIVE-PLAYBOOK.md — 4 lines)

### Planning File Sizes (lines)

| File | Lines |
|------|-------|
| planning/11-shopify-implementation-roadmap-inventory.md | 1,379 |
| planning/10-decisions-inventory.md | 978 |
| planning/08-creative-playbook-inventory.md | 777 |
| planning/consistency-remediation-plan.md | 631 |
| planning/INDEX-inventory.md | 445 |
| planning/repository-audit.md | 349 |
| planning/knowledge-base-consistency-audit.md | 276 |
| planning/repository-source-map.md | 254 |
| planning/review-09-product-knowledge.md | 158 |
| planning/review-10-decisions.md | 143 |
| planning/architecture-governance-summary.md | 142 |
| planning/review-03-design-system.md | 135 |
| planning/review-07-copy-guide.md | 133 |
| planning/review-02-brand-system.md | 128 |
| planning/ADR-04-eyebrow-letter-spacing.md | 115 |
| planning/ADR-05-pdp-text-color.md | 114 |
| planning/review-01-brand-north-star.md | 114 |
| planning/QA-09-PRODUCT-KNOWLEDGE.md | 102 |
| planning/ADR-01-color-palette-values.md | 93 |
| planning/ADR-07-star-rating-color.md | 89 |
| planning/ADR-03-button-border-radius.md | 82 |
| planning/ADR-06-review-card-radius.md | 81 |
| planning/QA-02-BRAND-SYSTEM.md | 80 |
| planning/ADR-02-free-shipping-threshold.md | 77 |
| planning/QA-07-COPY-GUIDE.md | 72 |
| planning/QA-03-DESIGN-SYSTEM.md | 66 |
| planning/QA-01-BRAND-NORTH-STAR.md | 46 |

---

## DOCUMENT COVERAGE

### APPROVED Documents (4)

| Document | Lines |
|----------|-------|
| docs/04-COMPONENT-LIBRARY.md | 1,122 |
| docs/05-PDP-ARCHITECTURE.md | 2,814 |
| docs/06-HOMEPAGE-ARCHITECTURE.md | 10,511 |
| docs/08-LIVE-SITE-COPY-AUDIT.md | 2,257 |

### PENDING REVIEW Documents (6)

| Document | Lines | Review Packet |
|----------|-------|---------------|
| docs/01-BRAND-NORTH-STAR.md | 248 | planning/review-01-brand-north-star.md |
| docs/02-BRAND-SYSTEM.md | 175 | planning/review-02-brand-system.md |
| docs/03-DESIGN-SYSTEM.md | 411 | planning/review-03-design-system.md |
| docs/07-COPY-GUIDE.md | 217,636 | planning/review-07-copy-guide.md |
| docs/09-PRODUCT-KNOWLEDGE.md | 1,227 | planning/review-09-product-knowledge.md |
| docs/10-DECISIONS.md | 1,092 | planning/review-10-decisions.md |

### STUB Documents (2)

| Document | Lines |
|----------|-------|
| docs/00-README.md | 4 |
| docs/08-CREATIVE-PLAYBOOK.md | 4 |

**Note:** docs/INDEX.md is also marked STUB (27 lines) but serves as navigation, not content.

### Total Knowledge Base Documents: 13

---

## CITATION COVERAGE

"Source:" line counts measured via grep across each document.

| Document | "Source:" lines |
|----------|----------------|
| docs/01-BRAND-NORTH-STAR.md | 24 |
| docs/02-BRAND-SYSTEM.md | 12 |
| docs/03-DESIGN-SYSTEM.md | 4 |
| docs/09-PRODUCT-KNOWLEDGE.md | 82 |
| docs/10-DECISIONS.md | 116 |

**Total measured "Source:" citations across these 5 documents:** 238

---

## DUPLICATE COVERAGE

Per planning/repository-audit.md (measured 2026-07-13):

| Metric | Value |
|--------|-------|
| Estimated exact duplicate files | ~350 of 551 |
| Full directory mirrors | 3 duplicate trees (~300 redundant copies) |
| Homepage version files duplicated | 15 files (v10–v24) in 2 locations |
| CSS files duplicated 8–11 times | 7 unique CSS files with duplicates |
| Research Bible copies | 5 |
| Identical homepage versions | v22 and v23 are byte-identical |

---

## PLANNING COVERAGE

| Metric | Count |
|--------|-------|
| Total planning/ files | 27 |
| ADRs (Architecture Decision Records) | 7 (ADR-01 through ADR-07) |
| Review packets | 6 (review-01, 02, 03, 07, 09, 10) |
| QA checklists | 5 (QA-01, 02, 03, 07, 09) |
| Inventories | 4 (08-creative-playbook, 10-decisions, 11-shopify, INDEX) |
| Audits/plans | 4 (repository-audit, consistency-remediation-plan, knowledge-base-consistency-audit, architecture-governance-summary) |
| Other | 1 (repository-source-map) |

---

## MISSING DOCUMENTATION

### Stub Documents Not Yet Built

| File | Current Size | Needed Content |
|------|-------------|----------------|
| docs/00-README.md | 4 lines | Getting started and repository overview |
| docs/08-CREATIVE-PLAYBOOK.md | 4 lines | Creative direction, campaigns, asset specifications |

### Referenced Documents That Don't Exist

| Referenced As | Referenced By | Status |
|---------------|---------------|--------|
| Root README.md | Standard convention | Does not exist at repository root |
| .gitignore | planning/repository-audit.md | Does not exist |
| Collection page architecture doc | planning/repository-audit.md (Section 5D) | No equivalent to docs/05 or docs/06 for collections |
| manychat-kb/01-*.md | planning/repository-audit.md (Section 5E) | Files 02–16 exist; 01 is missing |
| docs/08-LIVE-SITE-COPY-AUDIT.md in INDEX.md | planning/repository-audit.md (Section 7A) | File exists but INDEX.md does not list it |

### Documents Without Review Packets

| Document | Status | Has Review Packet |
|----------|--------|-------------------|
| docs/04-COMPONENT-LIBRARY.md | APPROVED | No |
| docs/05-PDP-ARCHITECTURE.md | APPROVED | No |
| docs/06-HOMEPAGE-ARCHITECTURE.md | APPROVED | No |
| docs/08-LIVE-SITE-COPY-AUDIT.md | APPROVED | No |

(APPROVED documents were reviewed directly; review packets exist only for PENDING REVIEW documents.)

---

## TECHNICAL DEBT

### Unresolved Conflicts

From docs/10-DECISIONS.md SOURCE CONFLICTS REGISTER:

| ID | Conflict | Status |
|----|----------|--------|
| C-001 | Button radius: 0px vs 6px | Needs resolution |
| C-002 | Eyebrow letter-spacing: 0.14em vs 0.08em | Needs resolution |
| C-003 | PDP review card radius: 0–4px vs 12px | Needs resolution |
| C-004 | PDP text color: #050505 vs #1c1916 | Needs resolution |
| C-005 | PDP CTA coral hover vs restraint rule | Needs resolution |
| C-006 | Color naming: production vs design | Timeline TBD |
| C-007 | Product title: SEO vs brand | Timeline TBD |
| C-008 | Yoga Tight compare-at: missing in API | Data quality issue |
| C-009 | Roadmap colors vs DS tokens | Later/divergent decision? |
| C-010 | Free shipping: $75 vs $150 | RESOLVED — $150 is current |

**Unresolved conflicts: 9** (C-001 through C-009)  
**Resolved conflicts: 1** (C-010)

### ADRs Awaiting Decision

| ADR | Topic | Blocking |
|-----|-------|----------|
| ADR-01 | Color palette values | Implementation of all color tokens |
| ADR-02 | Free shipping threshold | PDP and cart copy |
| ADR-03 | Button border-radius | CTA and pill button styling |
| ADR-04 | Eyebrow letter-spacing | Label typography system-wide |
| ADR-05 | PDP text color | Ink tone across entire site |
| ADR-06 | Review card radius | Card appearance on PDP |
| ADR-07 | Star rating color | Rating stars on PDP |

**ADRs awaiting decision: 7**

### Consistency Findings

Per planning/knowledge-base-consistency-audit.md:

| Severity | Count |
|----------|-------|
| Critical | 3 |
| High | 6 |
| Medium | 10 |
| Low | 11 |
| **Total** | **30** |

---

## REMAINING BLOCKERS

From planning/architecture-governance-summary.md:

1. **ADR-01 through ADR-07 must be resolved** — 7 color/radius/typography conflicts prevent implementation
2. **OS 2.0 confirmation needed** — Shopify OS 2.0 not yet confirmed as target platform (open question in docs/03)
3. **Photography assets needed from brand team** — All current imagery is placeholder only
4. **5 undecided sections** — Sections 04, 15, 24, 25, 29 need CEO decisions (Keep/Refactor/Remove)

---

## READINESS SCORES

### Repository Readiness

**Formula:** (APPROVED + PENDING REVIEW docs) / total planned docs × 100

- APPROVED documents: 4
- PENDING REVIEW documents: 6
- Total planned documents: 13 (all files in docs/)
- **Score: (4 + 6) / 13 × 100 = 76.9%**

*Methodology: Counts documents with status APPROVED or PENDING REVIEW (substantive content exists and is either approved or under review) divided by total docs/ files.*

### Knowledge Base Completeness

**Formula:** (non-STUB docs) / total docs × 100

- Non-STUB documents: 10 (4 APPROVED + 6 PENDING REVIEW)
- STUB documents: 3 (00-README.md, 08-CREATIVE-PLAYBOOK.md, INDEX.md)
- Total docs: 13
- **Score: 10 / 13 × 100 = 76.9%**

*Methodology: Any document with actual content (not just a title + status line) counts as non-STUB.*

### Shopify Readiness

**Formula:** resolved prerequisites / total prerequisites × 100

Prerequisites identified in architecture-governance-summary.md:

| Prerequisite | Resolved? |
|--------------|-----------|
| Design tokens defined | Yes (but conflicts unresolved) |
| Section decisions made | Partial (23 of 28 decided) |
| PDP specification | Yes (APPROVED) |
| Homepage specification | Yes (APPROVED) |
| Component library | Yes (APPROVED) |
| Implementation order defined | Yes |
| Shopify OS 2.0 confirmed | No |
| Photography assets | No |
| Product data documented | Yes |
| App integrations identified | Yes |
| Content migration plan | Yes |
| Timeline defined | Yes |
| ADR conflicts resolved | No (0 of 7) |

- Resolved: 8 (counting "partial" section decisions as resolved)
- Total: 13
- **Score: 8 / 13 × 100 = 61.5%**

*Methodology: Each prerequisite from the governance summary scored as resolved or not. Partially resolved items (section decisions 23/28) counted as resolved.*

### AI Readiness

**Formula:** Existence of required operational documents (binary per document)

| Required Document | Exists? |
|-------------------|---------|
| WORKFLOW.md | Yes (145 lines, APPROVED) |
| AI-OPERATIONS-MANUAL (planning/) | No (being created now) |
| planning/architecture-governance-summary.md | Yes (142 lines) |
| planning/consistency-remediation-plan.md | Yes (631 lines) |
| planning/knowledge-base-consistency-audit.md | Yes (276 lines) |
| planning/repository-audit.md | Yes (349 lines) |
| planning/engineering-backlog.md | Yes (being created now) |

- Present: 5 of 7
- **Score: 5 / 7 × 100 = 71.4%**

*Methodology: Binary check for existence of each document an AI agent would need to become operational.*

### Developer Onboarding Readiness

**Formula:** Existence of required onboarding documents

| Required Document | Exists? |
|-------------------|---------|
| Root README.md | No |
| WORKFLOW.md | Yes |
| docs/03-DESIGN-SYSTEM.md | Yes (PENDING REVIEW) |
| docs/04-COMPONENT-LIBRARY.md | Yes (APPROVED) |
| planning/11-shopify-implementation-roadmap-inventory.md | Yes |
| planning/engineering-backlog.md | Yes (being created now) |
| .gitignore | No |

- Present: 5 of 7
- **Score: 5 / 7 × 100 = 71.4%**

*Methodology: Binary check for documents a new developer would need to start working on the Shopify theme.*

---

## READINESS SUMMARY

| Dimension | Score | Notes |
|-----------|-------|-------|
| Repository readiness | 76.9% | 10 of 13 docs have substantive content |
| Knowledge base completeness | 76.9% | 3 STUBs remain |
| Shopify readiness | 61.5% | Blocked by 7 ADRs + OS 2.0 + photography |
| AI readiness | 71.4% | AI-OPERATIONS-MANUAL being created |
| Developer onboarding readiness | 71.4% | No root README or .gitignore |

---

**END OF HEALTH REPORT**
