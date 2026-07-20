# 01 — Repository Structure

> Developer reference for the Barreletics Design Review repository.
> Audience: Senior Shopify developer onboarding to the codebase.

---

## Directory Tree

```
Barreletics-Design-Review/
├── shopify-build/              ← Production Shopify theme source
│   ├── layout/
│   │   └── theme.liquid        ← Master layout (orchestrates every page)
│   ├── templates/              ← JSON template files (section composition)
│   │   ├── index.json
│   │   ├── product.json
│   │   ├── collection.json
│   │   ├── collection.{suffix}.json   (8 sub-collection templates)
│   │   ├── page.{suffix}.json         (13 page templates)
│   │   ├── article.json, blog.json, cart.json, search.json
│   │   ├── 404.json, password.json, list-collections.json
│   │   └── customers/          ← Account templates (7 files)
│   ├── sections/               ← Liquid section files (30 files)
│   ├── snippets/               ← Reusable Liquid snippets (23 files)
│   ├── assets/                 ← CSS and JS (4 files)
│   │   ├── design-tokens.css
│   │   ├── barreletics-base.css
│   │   ├── variant-selector.js
│   │   └── cart.js
│   ├── config/
│   │   ├── settings_schema.json    ← Theme settings definitions
│   │   └── settings_data.json      ← Current setting values
│   ├── locales/
│   │   └── en.default.json
│   └── DEPLOYMENT_CHECKLIST.md
│
├── planning/                   ← Foundation docs, ADRs, milestone specs
│   ├── 01-brand-north-star.md through 13-knowledge-architecture.md
│   ├── ADR-01 through ADR-07   (superseded — see 10-decision-log.md)
│   ├── m4a-*, m4b-*, m4c-*, m4d-*   (milestone gate deliverables)
│   ├── MASTER_ROADMAP.md, MILESTONES-4-5-6-ROADMAP.md
│   └── various review, audit, and spec files
│
├── docs/                       ← Documentation (brand docs + technical docs)
│   ├── 00-README.md through 10-DECISIONS.md   (brand/design docs)
│   └── 01-25 technical docs (this series)
│
├── barreletics-design-review/  ← Design mockup history
│   ├── Barreletics Design Review/   ← HTML prototypes, CSS, JS, screenshots
│   ├── Barreletics_All_Versions/    ← Home page version history (v10–v24)
│   ├── design_handoff_barreletics 2/ ← Latest design handoff with approved pages
│   └── project/                     ← Working project files
│
├── archive/pdp-history/        ← PDP version history (v37–v49)
├── sections/                   ← Standalone HTML section prototypes
├── files/                      ← Home page HTML versions (v10–v24)
├── manychat-kb/                ← ManyChat knowledge base articles (16 files)
├── scripts/                    ← Utility scripts (PR creation)
├── .github/                    ← GitHub automation docs
├── index.html                  ← Root index
├── PROJECT_DASHBOARD.md        ← Project status dashboard
├── WORKFLOW.md                 ← Development workflow
└── Makefile                    ← Build automation
```

---

## Purpose of Each Top-Level Directory

| Directory | Purpose |
|-----------|---------|
| `shopify-build/` | **Production theme source.** The only directory that gets deployed to Shopify. Contains all Liquid, CSS, JS, JSON templates, and configuration. |
| `planning/` | **Architecture and planning.** Foundation documents (01–13), ADRs, milestone specs, QA reports, content inventories, metafield specs. These are the specs that `shopify-build/` implements. |
| `docs/` | **Documentation.** Brand/design docs (uppercase names) and technical developer docs (lowercase names, this series). |
| `barreletics-design-review/` | **Design mockup history.** HTML prototypes from the design phase. Multiple version snapshots. The approved designs (v49 PDP, July 17 Home/Collection) are the design source of truth. |
| `archive/pdp-history/` | **PDP evolution.** 13 versions (v37–v49) showing the PDP design evolution. v49 is the approved canonical design. |
| `sections/` | **Section prototypes.** Standalone HTML section mockups used during design. Not deployed. |
| `files/` | **Home page versions.** HTML prototypes of home page iterations (v10–v24). |
| `manychat-kb/` | **ManyChat knowledge base.** 16 markdown files covering product info, sizing, pricing, shipping, returns, brand voice for the ManyChat chatbot. |
| `scripts/` | **Utility scripts.** PR creation helpers. |
| `.github/` | **GitHub config.** PR automation, quick reference, setup guide. |

---

## File Naming Conventions

| Context | Convention | Example |
|---------|-----------|---------|
| Shopify sections | `kebab-case.liquid` | `pdp-buy-box.liquid` |
| Shopify snippets | `kebab-case.liquid` | `header-nav.liquid` |
| Shopify templates | `{type}.{suffix}.json` | `collection.open-sole.json` |
| Planning docs | `{number}-{name}.md` | `10-decision-log.md` |
| ADRs | `ADR-{number}-{name}.md` | `ADR-01-color-palette-values.md` |
| Milestone docs | `m{gate}{letter}-{name}.md` | `m4b-integration-plan.md` |
| Technical docs | `{number}-{name}.md` (lowercase) | `06-javascript-architecture.md` |
| Brand docs | `{number}-{NAME}.md` (uppercase) | `03-DESIGN-SYSTEM.md` |
| Design mockups | `Barreletics {Type} {version}.html` | `Barreletics Home v10.html` |

---

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready. All milestone gates merge here after approval. |
| `technical-documentation` | This documentation effort. |
| Feature branches | Named by milestone or feature (e.g., `milestone-2-core-experience`, `m4a-production-assembly`). |

PRs merge to `main` after architect/owner approval. Locked milestones (D-021, D-027, D-035, D-044, D-046, D-047) cannot be modified without a new Decision Log entry.

---

## How Planning Docs Relate to Implementation

```
planning/01–13 (Foundation)  →  Specs that shopify-build/ implements
planning/10-decision-log.md  →  Overrides everything when conflicts exist
planning/ADR-01–07           →  Superseded by Decision Log (D-001–D-007)
planning/m4a–m4d specs       →  Gate-specific deliverables and checklists
```

Foundation docs define **what** to build. The Decision Log resolves **conflicts** between documents. `shopify-build/` is the **implementation**.

---

## Source of Truth Hierarchy

When any conflict exists between documents, follow this precedence:

1. **`planning/10-decision-log.md`** — Ultimate authority. Resolved decisions supersede all other documents.
2. **Foundation docs (01–13)** — Locked architectural specs. The canonical reference for each domain.
3. **`shopify-build/` source code** — The implementation. Should match Foundation docs; if it doesn't, the Decision Log determines which is correct.
4. **Design System skill** (`~/.cursor/skills/barreletics-design-system/SKILL.md`) — Quick reference for design tokens and component rules. Derived from v49 approved design.
5. **Approved HTML prototypes** — `archive/pdp-history/PDP Complete v49.html` and `barreletics-design-review/design_handoff_barreletics 2/pages/Barreletics PDP - APPROVED July 17.html` are the visual source of truth.
6. **ADR-01 through ADR-07** — Historical. All resolved in Decision Log D-001 through D-007.

---

## Cross-References

- Theme architecture → [Doc 02](02-theme-architecture.md)
- Section inventory → [Doc 03](03-section-library.md)
- Snippet inventory → [Doc 04](04-snippet-library.md)
- Asset inventory → [Doc 05](05-asset-library.md)
- Decision Log → `planning/10-decision-log.md`
