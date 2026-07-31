# M4 Section Library CONTRACT — Frozen Architecture

**Status:** ARCHITECTURE APPROVED  
**Date:** 2026-07-26  
**Approved by:** Andrew  
**Authority:** This file is the frozen contract for the Barreletics Design System theme section library.  
**Supersedes:** `planning/m4-section-library-architecture.md` (proposal — kept for history; decisions locked here)

---

## 1. Status + Andrew decisions (verbatim lock)

| ID | Decision | Verdict |
|----|----------|---------|
| **H1** | Rename `home-split-hero` → `split-hero` | **YES** |
| **H2** | Artificially limit hero count (e.g. three max)? | **NO** — do not artificially limit. Build capabilities. Additional hero types only if genuinely different capability. |
| **H3** | Delete legacy `hero` + `hero-alt` after replacements approved/frozen | **YES** |
| **H4** | Collection sole cards | **(B)** — `sole-cards` = own reusable companion section; not permanently coupled to `collection-split` |
| **C1** | `statement-band` | **Standalone reusable section** (first-class). Full-bleed commit/lifestyle = separate capability (`fullbleed-statement` / `lifestyle-break`) if mocks require — do **not** fold `statement-band` into something else. |
| **C2** | `campaign-stage` in v1 | **DEFER** |
| **C3** | GEO | **YES** — GEO lives in `studio-trust` |
| **C4** | Newsletter | **BOTH** — in footer **and** standalone `newsletter` section |
| **C5** | Content vs marketing entry | `page-head` for informational/content; `hero-fullbleed` for marketing |
| **C6** | Monolithic `page-*` | **YES** — delete after decompose into library sections |
| **P1** | Reviews | **YES** — one `reviews` section |
| **P2** | `pdp-features` | **NO** — keep separate; do **not** merge into `fifty-fifty` |
| **P3** | `variant-grid` KEEP logic | **YES** — non-negotiable (handoff list) |
| **X1** | Freeze architecture | **YES** |
| **X2** | One section at a time | **YES** |
| **X3** | No further implementation until architecture approved; final inventory contract required before more production code | **YES** |

---

## 2. Operating model

### Source of truth (HARD)

**The repository is the Design System.** Every piece of custom code lives in the repo as source of truth. Shopify is **only the runtime** for visual QA — never the master copy.

| Layer | Role |
|-------|------|
| **GitHub / `shopify-build/`** | **Master** — sections, snippets, assets, CSS, JS, documentation. Fully editable + version-controlled. |
| **Disposable draft theme** | Temporary visual-QA runtime only. May be deleted anytime. |
| **Production theme** | Brian integrates from approved repository — not agent-owned. |

**GitHub is NOT a review environment.** Andrew cannot approve sections from source/PR alone. Visual approval happens in Shopify (Theme Editor + storefront preview)—not from the repository.

> I can't review a Shopify section from GitHub source files alone. Every completed section must be deployed to the Shopify development theme and accompanied by a preview URL. I will review the implementation visually in the Theme Editor and on the storefront (desktop + mobile), verify all settings and controls work correctly, then approve or request revisions. GitHub remains the source of truth for code, but visual approval happens in Shopify—not from the repository.

**Do not** treat Theme Editor / remote theme as source of truth. **Do not** develop primarily in Shopify. Fixes discovered during QA are revised **in the repository first**, then re-deployed to a disposable draft if needed.

### QA workflow

1. Build section in repository (`shopify-build/`)
2. Commit it (GitHub master)
3. Deploy to Shopify **development / disposable draft** (push **only** when Andrew names a theme ID in that message; ask if missing; never invent; never live)
4. Send **preview URL** + Theme Editor URL
5. Andrew reviews visually: desktop + mobile, spacing, type, breakpoints, settings/schema, TE controls, image crop, performance
6. Revisions in the repository → redeploy → repeat
7. When approved: freeze in repo → next section
8. Brian pulls approved repository and integrates into production theme

### Rules table

| Rule | Detail |
|------|--------|
| Master | GitHub / **`shopify-build/`** = Design System source of truth |
| Visual approval | Shopify draft **preview URL** + Theme Editor — not GitHub source/PR |
| Handoff | Approved repo → **Brian** → production theme |
| Disposable draft QA | Allowed **only** when Andrew names a theme ID in the current message; ask before any push if no ID |
| Retired draft | `187143618851` — dead; do not use; new disposable ID must be explicit |
| Live / production theme | Forbidden for agent push |
| Remote ≠ master | Never treat Theme Editor or remote theme as source; pull learnings back into repo first |
| Library doctrine | Final theme = **only** this approved production library. Replace legacy — no duplicate generations. |
| Section cadence | One section → commit → deploy draft → preview URL → visual QA → revise in repo → freeze → next |

**Explicit gate:** No production section code until this CONTRACT is acknowledged. After acknowledgment, only **`split-hero`** until that section is frozen via visual QA.

---

## 3. FINAL PRODUCTION SECTION LIBRARY

Approved filenames for the theme. One purpose each. **v1** = build for the OS set. **Deferred** = not in v1.

Rename notes: current repo file → final name where different.

### Chrome (v1) — 3

| Filename | Purpose | Rename / notes |
|----------|---------|----------------|
| `announcement-strip` | Top promo / trust messages | — |
| `header` | Global nav, logo, account, cart, mobile drawer | — |
| `footer` | Global footer menus + newsletter form (C4) | — |

### Heroes & page entry (v1) — 4

No artificial hero cap (H2). Ship distinct capabilities only.

| Filename | Purpose | Rename / notes |
|----------|---------|----------------|
| `split-hero` | 50/50 copy \| media first-viewport hero | **from** `home-split-hero` (H1) |
| `hero-fullbleed` | Edge-to-edge marketing hero; `alignment: start \| center` | New (not in repo yet) |
| `collection-split` | Collection intro split; `media_fill: inset \| column` | **from** `collection-hero` path (was proposed as `collection-split-hero`; final name **`collection-split`**) |
| `page-head` | Informational/content page title entry (Help, FAQ, thin pages) | New — C5; not a marketing hero |

### Companions (v1) — 1

| Filename | Purpose | Rename / notes |
|----------|---------|----------------|
| `sole-cards` | Open/closed sole card pair — reusable companion | New extract from `collection-hero` (H4 B); not permanently coupled to `collection-split` |

### Commerce (v1) — 7

| Filename | Purpose | Rename / notes |
|----------|---------|----------------|
| `variant-grid` | Product/color grid + Quick Add + tabs — KEEP logic non-negotiable (P3) | Rebuild stub |
| `pdp-buy-box` | PDP gallery + variants + ATC | Rebuild |
| `pdp-sticky-atc` | Sticky add-to-cart bar | Rebuild |
| `main-cart` | Cart page | Rebuild |
| `recommendations` | Related products | Keep / polish |
| `recently-viewed` | Recently viewed products | Keep / polish |
| `search-results` | Search results grid | Keep / polish |

### Content (v1) — 17

| Filename | Purpose | Rename / notes |
|----------|---------|----------------|
| `fifty-fifty` | Mid-page media \| copy split | Rebuild from `br-media-text-split` |
| `visual-mosaic` | Multi-tile mosaic (mid-page, not a page hero) | New — from `br-multi-box-hero` / Home WORKING |
| `disciplines` | Discipline name strip | Rebuild |
| `statement-band` | Large typographic statement band | Rebuild — first-class (C1); not a setting on another section |
| `fullbleed-statement` | Full-bleed commit / lifestyle typography plane | New — separate from `statement-band` (C1) |
| `lifestyle-break` | Mid-page full-bleed video (~90vh) | New — SEO Never Loses |
| `value-strip` | Horizontal value / trust checklist | Rebuild |
| `sock-math` | Cost / “One pair. Done.” math | **from** `pdp-sock-math` |
| `comparison` | Sole / grip comparison content (open vs closed, grip tables) | New — maps `page-compare` + `page-grip-comparison` mocks; **not** sock-math |
| `problem-section` | Problem / chair-pose beat | New — Home WORKING |
| `pdp-features` | PDP feature grid | Rebuild — **kept separate** (P2); do not merge into `fifty-fifty` |
| `faq` | Accordion FAQ (blocks) | New — absorbs `collection-faq` + `page-faq` |
| `newsletter` | Standalone email capture | Keep — C4 both with footer |
| `contact-cta` | “Still have questions?” CTA | Keep |
| `help-hub-grid` | Help hub link grid | New — Help v3 |
| `journal-index` | Journal / blog listing | **from** `blog-listing` |
| `article-content` | Single article body | Keep |

### Proof (v1) — 4

| Filename | Purpose | Rename / notes |
|----------|---------|----------------|
| `reviews` | Quote-led reviews; settings for PDP aggregate when needed | Merges `social-proof` + `pdp-reviews` (P1) |
| `ig-section` | Instagram / studio UGC grid | **from** `home-ugc` |
| `guarantee` | Guarantee / risk-reversal band | **from** `guarantee-band` |
| `studio-trust` | Studio / instructor trust; **includes GEO** (C3) | New — absorbs `geo-section` |

### Deferred (not v1)

| Filename | Why deferred |
|----------|--------------|
| `campaign-stage` | **C2 DEFER** — Coperni / collab runway later |
| `featured-products` | Andrew example name — **no distinct locked mock**; product listing = `variant-grid` / `recommendations`. Do not invent. |
| `featured-collections` | Andrew example name — **no distinct locked mock** in Home/Collection/SEO spines. Do not invent. |

### Section groups (not counted as library sections)

| File | Role |
|------|------|
| `header-group.json` | Announcement + header |
| `footer-group.json` | Footer (+ newsletter in footer) |

### Final v1 count

**36** approved production sections (3 chrome + 4 entry + 1 companion + 7 commerce + 17 content + 4 proof).  
Deferred: 3 names (`campaign-stage`, `featured-products`, `featured-collections`).

---

## 4. EXISTING REPO CLASSIFICATION

Every current `shopify-build/sections/*.liquid` → disposition for the final theme.  
Legend: **KEEP** · **REBUILD** · **MERGE→X** · **DELETE**

| Current file | Disposition | Notes |
|--------------|-------------|-------|
| `announcement-strip.liquid` | **KEEP** | Chrome; polish vs WORKING only |
| `header.liquid` | **KEEP** | Chrome; Shopify menus |
| `footer.liquid` | **KEEP** | Chrome; newsletter remains (C4) |
| `home-split-hero.liquid` | **REBUILD** → `split-hero` | First build target after contract acknowledge; H1 rename |
| `hero.liquid` | **MERGE→split-hero** then **DELETE** | Legacy prototype; H3 delete after freeze |
| `hero-alt.liquid` | **DELETE** | Duplicate; H3 after replacements frozen |
| `collection-hero.liquid` | **REBUILD** → `collection-split` + extract `sole-cards` | Sole cards become companion (H4 B) |
| `fifty-fifty.liquid` | **REBUILD** | Port `br-media-text-split`; preserve schema IDs |
| `variant-grid.liquid` | **REBUILD** | KEEP logic non-negotiable (P3) |
| `disciplines.liquid` | **REBUILD** | Align Home WORKING |
| `statement-band.liquid` | **REBUILD** | Standalone first-class (C1) |
| `value-strip.liquid` | **REBUILD** | Collection / SEO |
| `guarantee-band.liquid` | **REBUILD** → `guarantee` | Rename |
| `home-ugc.liquid` | **REBUILD** → `ig-section` | Rename for reuse |
| `social-proof.liquid` | **MERGE→reviews** | One reviews section (P1) |
| `contact-cta.liquid` | **KEEP** | Thin utility |
| `newsletter.liquid` | **KEEP** | Standalone + footer (C4) |
| `collection-faq.liquid` | **MERGE→faq** | One FAQ capability |
| `geo-section.liquid` | **MERGE→studio-trust** | GEO in studio-trust (C3) |
| `pdp-buy-box.liquid` | **REBUILD** | Core commerce |
| `pdp-sticky-atc.liquid` | **REBUILD** | Companion to buy box |
| `pdp-features.liquid` | **REBUILD** | Keep separate (P2); not merge into fifty-fifty |
| `pdp-reviews.liquid` | **MERGE→reviews** | One reviews section (P1) |
| `pdp-sock-math.liquid` | **REBUILD** → `sock-math` | Drop `pdp-` prefix |
| `main-cart.liquid` | **REBUILD** | Cart template |
| `recommendations.liquid` | **KEEP** | Thin commerce utility |
| `recently-viewed.liquid` | **KEEP** | Thin commerce utility |
| `search-results.liquid` | **KEEP** | Template section |
| `blog-listing.liquid` | **REBUILD** → `journal-index` | Journal v5 |
| `article-content.liquid` | **KEEP** | Article template |
| `page-about.liquid` | **DELETE** after decompose | C6 — compose from library |
| `page-ambassador.liquid` | **DELETE** after decompose | C6 |
| `page-compare.liquid` | **DELETE** after decompose | Content → `comparison` + library |
| `page-contact.liquid` | **DELETE** after decompose | `page-head` + form modules |
| `page-faq.liquid` | **MERGE→faq** then **DELETE** | Capability is `faq` |
| `page-grip-comparison.liquid` | **DELETE** after decompose | Content → `comparison` |
| `page-partners.liquid` | **DELETE** after decompose | C6 |
| `page-returns.liquid` | **DELETE** after decompose | C6 |
| `page-shipping.liquid` | **DELETE** after decompose | C6 |
| `page-size-guide.liquid` | **DELETE** after decompose | C6 |
| `page-studio-program.liquid` | **DELETE** after decompose | C6 |
| `page-technology.liquid` | **DELETE** after decompose | C6 |
| `page-warranty.liquid` | **DELETE** after decompose | C6 |
| `page-wholesale.liquid` | **DELETE** after decompose | C6 |

**Missing from repo (approved; build when reach order):**  
`hero-fullbleed`, `collection-split` (as final name), `sole-cards`, `visual-mosaic`, `fullbleed-statement`, `lifestyle-break`, `problem-section`, `comparison`, `faq`, `page-head`, `help-hub-grid`, `studio-trust`, `reviews` (as final merged file), `campaign-stage` (**deferred**).

---

## 5. Build order (one at a time)

| # | Section | Gate |
|---|---------|------|
| 0 | **This CONTRACT acknowledged** | Required before any production code |
| **1** | **`split-hero`** | Rebuild/rename from `home-split-hero` to DS standards → deploy disposable draft → preview URL → visual QA → Andrew approve → **freeze** |
| 2 | `hero-fullbleed` | Only after `split-hero` frozen |
| 3 | `collection-split` | Then `sole-cards` as companion (can follow immediately after, still one-at-a-time) |
| 4 | `fifty-fifty` | First surgical port |
| 5 | `visual-mosaic` | Second port |
| 6 | `variant-grid` | Largest KEEP-logic job |
| 7 | Marketing spine: `disciplines` → `statement-band` → `fullbleed-statement` → `value-strip` → `sock-math` → `comparison` → `problem-section` → `lifestyle-break` | One at a time |
| 8 | Proof: `reviews` → `ig-section` → `guarantee` → `studio-trust` | One at a time |
| 9 | `faq` · `newsletter` polish · `contact-cta` · `page-head` · `help-hub-grid` · `journal-index` | One at a time |
| 10 | `pdp-buy-box` → `pdp-sticky-atc` → `pdp-features` | One at a time |
| 11 | Template assembly | **Brian** (or later) — not agents on Shopify |
| 12 | Delete legacy heroes + monoliths after replacements frozen | H3 / C6 |
| — | `campaign-stage` | **Deferred** (C2) |

**Hard rule after contract acknowledge:** only `split-hero` until frozen. No parallel section builds. Shopify deploy only with Andrew-named disposable draft ID + preview URL for visual approval.

---

## 6. Explicit production-code gate

1. **No production section code** until this CONTRACT is acknowledged.  
2. After acknowledgment: **only `split-hero`** (rebuild/rename from `home-split-hero`) until frozen.  
3. No Shopify CLI theme mutations.  
4. Final theme ships **only** the approved library in §3 — legacy duplicates deleted after replacements are frozen.

---

## 7. Theme Editor control tiers (APPROVED 2026-07-30)

**Full spec:** `planning/m4-te-controls.md`

| Tier | Meaning |
|------|---------|
| **A — Marketing** | Copy + image/video + basic layout |
| **B — Text band** | Copy + CTA only |
| **C — Commerce** | Domain controls (variant tabs/products; PDP product-driven + TE extras) |

**Schema order (every section):** `Shared — Content` → `Shared — Media` → `Shared — Layout` → `Section — …` (custom). Omit N/A blocks; no fake fields; **no font pickers** (Type OS).

**Shared patterns (see `m4-te-controls.md`):** type size/weight overrides (`Default / Type OS` + px list); media field meanings (Shopify video vs URL vs poster vs image fallback); media column % + corner radius; CTA URL vs `#anchor`; trust-row star color/size/gap on sections that show stars. Detail upgrades: `fifty-fifty`, `split-hero`, `statement-band`, `variant-grid`, `pdp-buy-box`.

---

## 8. Section freeze — no drift / no revert (HARD · 2026-07-31)

**Full registry:** `planning/m4-section-freeze.md`  
**Cursor guardrail:** `.cursor/rules/section-freeze-no-drift.mdc`

Once Andrew marks a section **APPROVED / SETTLED / FROZEN**, agents must not silently revert, redesign, or swap it.

| Locked | Status | Notes |
|--------|--------|-------|
| **Footer A+** | **LOCKED / APPROVED / FROZEN** 2026-07-31 | Sitewide default footer. Charcoal/black simplified Join the list · columns → Made in USA (+ Connect). **NO brand blurb. NO checkmark checklist. NO 10%.** Lineage `19b8fe6`. |
| **Type OS** | **SETTLED** | `planning/m4-type-hierarchy.md` |
| **Home WORKING** | Layout authority | Not a free redesign surface |

**Forbidden without explicit Andrew approval in the CURRENT message:** git checkout of frozen section files from old commits; Impulse/live/dark Phase 1 swaps; gallery “picks” as deployable replacements; inventing alternate footers/heroes.

**Allowed:** bugfixes and TE clarity that preserve locked composition; deploy only when Andrew names a disposable theme ID.

---

## Approval stamp

| Field | Value |
|-------|-------|
| Status | **ARCHITECTURE APPROVED** (+ freeze rules §8 · 2026-07-31) |
| Date | **2026-07-26** (architecture) · **2026-07-31** (Footer A+ freeze) |
| Approved by | **Andrew** |
| Contract file | `planning/m4-section-library-CONTRACT.md` |
| Freeze registry | `planning/m4-section-freeze.md` |
| First build target | **`split-hero`** (after contract acknowledge) |
| v1 library count | **36** sections |
