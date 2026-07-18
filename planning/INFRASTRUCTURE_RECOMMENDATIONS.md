# Infrastructure Recommendations

**Status:** 🔵 Ready for Review
**Last Updated:** 2026-07-18

---

## Purpose

Recommendations for skills, templates, standards, and tooling that improve quality, consistency, and autonomy across the Barreletics Blueprint.

---

## 1. New Skills Recommended

### Category Disruption Skill
**Priority:** High
**Purpose:** Auto-invoke on any content creation to ensure category creation messaging is embedded. Checks that copy moves from "which grip sock" to "why grip socks at all" and flags anti-patterns.
**Trigger:** Any Barreletics copywriting, messaging, or content task.

### QA Checklist Skill
**Priority:** High
**Purpose:** Automated quality checks before any page or document is marked Ready for Review. Validates: design token compliance, copy accuracy against Knowledge Base, SEO requirements, accessibility basics.
**Trigger:** Any Barreletics page build completion or doc review.

### SEO/GEO Content Skill
**Priority:** Medium
**Purpose:** Auto-invoke when creating GEO sections, pillar page content, or structured data. Contains keyword targets, GEO templates, schema markup patterns, and verified discipline terminology.
**Trigger:** Any SEO, GEO, structured data, or pillar page content task.

### Help Scout Adaptation Skill
**Priority:** Medium (Milestone 3)
**Purpose:** Transforms Knowledge Base topics into Help Scout-formatted saved replies, macros, and email templates. Ensures category creation messaging in all customer communication.
**Trigger:** Help Scout content creation or update.

### Tidio AI Adaptation Skill
**Priority:** Medium (Milestone 3)
**Purpose:** Transforms Knowledge Base topics into Tidio Q&A pairs with intent routing and human handoff rules.
**Trigger:** Tidio chatbot configuration or update.

---

## 2. Templates Recommended

### ADR Template
For future architectural decisions. Structure:
- Problem statement
- Options with pros/cons
- Decision + rationale
- Impact on affected documents
- Files to update

### Page Architecture Template
For new pages (landing pages, campaign pages, sub-collections). Structure:
- Page purpose
- Section architecture (numbered)
- Structured data requirements
- Meta tag specification
- Content strategy
- Mobile behavior
- Cross-references

### Knowledge Base Topic Template
For adding new topics to doc 07. Structure:
- Canonical answer
- Key customer quotes (name, city)
- Surface map (where this appears)
- Abbreviated version
- Help Scout adaptation
- Tidio Q&A pair

---

## 3. Documentation Standards

### Naming Convention
- Foundation docs: `##-kebab-case-name.md` (e.g., `07-product-knowledge-base.md`)
- Supporting docs: `UPPER_SNAKE_CASE.md` (e.g., `DECISION_FRAMEWORK.md`)
- Archive: `planning/archive/original-name.md`

### Status Badges
Every document header must include:
- Status: ⚪ / 🟡 / 🔵 / ✅ / 🔒
- Last Updated date
- Source reference (if applicable)

### Cross-Reference Rule
Every document must end with a cross-references section linking to related foundation docs. No orphan documents.

### Recency Rule
When conflicts exist: later decision wins. Log resolution in `10-decision-log.md`.

---

## 4. Repository Structure Improvements

### Current Structure (Post-Foundation)
```
Barreletics-Design-Review/
├── PROJECT_DASHBOARD.md           ← Project status hub
├── barreletics-design-review/     ← Design handoff files (locked)
│   └── design_handoff_barreletics 2/
│       └── pages/                 ← Approved + historical HTML mockups
├── planning/                      ← Foundation docs + planning
│   ├── 01-brand-north-star.md     ← Numbered foundation system
│   ├── ...
│   ├── 13-knowledge-architecture.md
│   ├── MASTER_ROADMAP.md
│   ├── DECISION_FRAMEWORK.md
│   ├── INFRASTRUCTURE_RECOMMENDATIONS.md
│   ├── engineering-backlog.md     ← Active backlog
│   ├── shopify-build-specification.md
│   ├── ADR-01-*.md through ADR-07-*.md  ← Historical (resolved)
│   └── archive/                   ← Superseded documents
└── docs/                          ← Legacy (if exists)
```

### Recommended Future Additions
- `planning/templates/` — ADR, page architecture, KB topic templates
- `planning/checklists/` — QA, launch, migration checklists (extracted from backlog)

---

## 5. Tooling Recommendations

### Knowledge Base Sync Tool
**Priority:** High (Milestone 3)
**Purpose:** Script or automation that validates downstream systems (Help Scout, Tidio, website) against Knowledge Base. Flags drift — content that doesn't match the canonical source.

### Design Token Linter
**Priority:** Medium (Milestone 2)
**Purpose:** CI check that flags hardcoded hex values, black (#000), orange, or $75 in any Shopify theme file. Enforces token system compliance.

### Content Freshness Monitor
**Priority:** Low (Post-launch)
**Purpose:** Alerts when Knowledge Base topics haven't been reviewed in 90+ days. Ensures governance cadence from doc 13 is maintained.

---

## 6. Process Recommendations

### Foundation Review Process
1. Builder marks docs 🔵 Ready for Review
2. Architect/Owner reviews each document for accuracy, completeness, consistency
3. Feedback → Builder incorporates → re-review
4. Architect/Owner marks ✅ Approved
5. Builder proceeds with dependent Tier 2 work

### Change Cascade Process (from doc 13)
1. Update made in Knowledge Base (doc 07)
2. Builder identifies affected downstream systems from surface map
3. Each system updated per its format requirements
4. Changes logged if they involve policy (doc 10)
5. Downstream systems validated against Knowledge Base

### Milestone Gate Process
1. Builder completes all deliverables in milestone
2. Builder marks milestone 🔵 in Dashboard
3. Architect/Owner reviews all deliverables
4. Architect/Owner approves gate → next milestone unlocked
5. Dashboard updated to ✅

---

**Cross-references:**
- Project Dashboard → `PROJECT_DASHBOARD.md`
- Master Roadmap → `planning/MASTER_ROADMAP.md`
- Decision Framework → `planning/DECISION_FRAMEWORK.md`
- Knowledge Architecture → `planning/13-knowledge-architecture.md`
