# Design Completion — Core Pages as One Conversion System

---
document: Design Completion — Home / Collections / PDP System Review
version: 2.0
status: 🔵 Active — decisions batched; proceed on Recommended defaults below
created: 2026-07-20
updated: 2026-07-20
branch: design-completion-phase1-core-review
supersedes: planning/design-completion-phase1-core-pages-review.md (v1 lock-gate style)
scope: Homepage · Collections (`/collections/grippy-shoes`) · PDP — treated as one funnel
depends_on:
  - planning/01–13 (Foundation)
  - planning/05-pdp-architecture.md
  - planning/06-homepage-architecture.md
  - planning/09-collection-architecture.md
  - planning/10-decision-log.md (esp. D-022, D-041)
  - planning/12-seo-geo-standards.md
  - origin/cro-phase-1 → planning/cro-phase-1-roadmap.md
  - origin/component-system → docs/component-system.md
---

**Constraint:** Documentation / design-completion only. No Shopify implementation in this PR. No lock declaration.

**Working rule:** Continue on the Recommended choices in the Decision Packet unless Owner overrides. Do not open separate blocker threads.

**Canonical mockups (composition authority):**
| Page | Mockup | Tokens |
|------|--------|--------|
| Home | `Barreletics Home - APPROVED July 17.html` | v49 / design tokens |
| Collection | `Barreletics Collection - Definitive-v4.html` | v49 / design tokens |
| PDP | `Barreletics PDP - APPROVED July 17.html` | v49 / design tokens (not v49 Enhanced page stack) |

---

## 0. Funnel Model (how the three pages work together)

```
Awareness / paid / organic
        ↓
   HOME — declare category, prove, shop (grid ATC or → Collection/PDP)
        ↓
   COLLECTION — decide Open vs Closed, browse, quick-add or → PDP
        ↓
   PDP — size/color, objections, ATC (sticky), FAQ/GEO for SEO
```

| Funnel job | Home | Collection | PDP |
|------------|------|------------|-----|
| Category creation | Primary | Secondary (SEO depth) | Reinforce near buy box |
| Decision support | Light (Closed/Open in grid) | Primary (sole chooser) | Size/color + fit |
| Direct convert | Quick-add grid | Quick-add grid | Primary ATC |
| Trust | Reviews + Guarantee + UGC | FAQ (+ reviews gap) | Reviews + FAQ + Sock Math |
| SEO / AI | GEO (policy) | GEO + FAQ + testimonials | GEO + FAQ + Product JSON-LD |

**System principle:** Share announcement strip, value/trust strip, disciplines proof, and variant grid. Do **not** clone mid-page narratives — Home = brand story, Collection = decide+shop, PDP = convert.

---

## 1. Homepage

### 1.1 Current section inventory

**APPROVED July 17 (design authority)**
1. Announcement strip + nav  
2. Hero — “The Pilates Sock Era Is Over” + Shop Now / See Why  
3. Problem — “Yoga Socks Are Useless”  
4. Disciplines + in-class proof  
5. Lineup (full color strip)  
6. Variants grid (Closed/Open + size + quick-add)  
7. Value / trust strip  
8. Editorial quote  
9. 50/50 — Upgrade / grip  
10. Coperni collab  
11. Full-bleed statement  
12. Reviews  
13. Sock Math lite — “One Pair. Done.”  
14. Instagram / UGC  
15. Guarantee  
16. Newsletter  

**Liquid `index.json` today:** Hero → value-strip → disciplines → variant-grid → fifty-fifty → social-proof → sock-math fifty-fifty → **GEO** → newsletter  
*(Shorter than APPROVED; has GEO that mockup lacks.)*

### 1.2 Missing vs architecture / concepts / CRO

| Gap | Source | Severity class |
|-----|--------|----------------|
| Rotating 5-message hero eyebrow | `planning/06` | Optional |
| Dedicated 6-pillar strip | `planning/05/06/09` | Optional (value-strip covers) |
| Full dark Sock Math (6-cell) | `planning/06`, matrix | Optional (lite present) |
| Founder Letter / Manifesto / Closing | `planning/06`, Matured | Optional → About first |
| GEO accordion | D-022, Liquid, `planning/12` | **Critical** |
| Hero concept lock (A vs B) | D-041 | **Critical** (copy only) |
| Problem / Guarantee / IG / Coperni vs Liquid | APPROVED vs `index.json` | Recommended (parity later) |
| Mobile image-first hero | CRO H-09 | Recommended |
| Specific hero CTA copy | CRO H-01 | Recommended |
| Hero video above fold | CRO H-03 | Optional |

### 1.3 Improvements

| ID | Improvement | Purpose | Priority |
|----|-------------|---------|----------|
| H-C1 | Resolve D-041: ship Concept A (APPROVED “Sock Era” system) as default | brand, conversion | **Critical** |
| H-C2 | Add GEO section to Home mockup/stack to match D-022 + Liquid | SEO | **Critical** |
| H-R1 | Align Liquid toward APPROVED narrative (Problem, Guarantee, UGC) without bloating above grid | brand, trust | **Recommended** |
| H-R2 | Test hero primary CTA specificity (“Shop Grippy Shoes — $74” / “Replace Your Grip Socks”) | conversion | **Recommended** |
| H-R3 | Mobile: product/lifestyle image in first viewport (image-first or tighter stack) | UX, conversion | **Recommended** |
| H-R4 | Keep Coperni as seasonal module (swap out when campaign ends) | brand | **Recommended** |
| H-O1 | Upgrade Sock Math lite → full dark module | education, conversion | **Optional** |
| H-O2 | Restore rotating eyebrow (respect `prefers-reduced-motion`) | education | **Optional** |
| H-O3 | Founder / Manifesto on About, not Home for launch | brand | **Optional** |
| H-O4 | Press / “As seen in” only with real logos | trust | **Optional** |

---

## 2. Collections (Grippy Shoes pillar)

### 2.1 Current section inventory

**Definitive-v4 (design authority)**
1. Announcement strip + nav  
2. Collection hero — shop-first H1 + Open/Closed education  
3. Sole explain / chooser cards  
4. Mid-value trust strip  
5. Variants grid (All / Closed / Open / One-Offs / Outdoor + size + Compare)  
6. Disciplines proof  
7. 50/50 — “Never Loses Grip.”  
8. 50/50 — “Commit to the Gear.”  
9. Trust FAQ (+ trust row)  
10. GEO accordion  
11. Newsletter  

**Liquid `collection.json` today:** collection-hero → value-strip → variant-grid → disciplines → two fifty-fifties → GEO → newsletter  
*(Missing FAQ present in Definitive-v4; no testimonials.)*

### 2.2 Missing vs architecture / concepts / CRO

| Gap | Source | Severity class |
|-----|--------|----------------|
| Customer testimonials (name/city) | `planning/09`, `planning/12` pillar reqs | **Critical** |
| FAQ (+ schema) in Liquid parity | Definitive-v4 vs `collection.json` | **Critical** |
| Dedicated 6-pillar strip | `planning/09` | Optional |
| Benefit grid (3 cards) | `planning/09` | Optional (absorbed) |
| Category-creation-first H1 | SEO ideal vs shop clarity | Recommended (subhead, not H1 flip) |
| “Best for…” on sole cards | CRO C-04 | Recommended |
| Card value subtitle / price context | CRO C-02 | Recommended |
| Inline Compare Styles | CRO C-05 | Recommended |
| Discipline filter tabs | CRO C-10 | Optional |
| Sock Math / Founder on collection | orphans | Optional — skip |

### 2.3 Improvements

| ID | Improvement | Purpose | Priority |
|----|-------------|---------|----------|
| C-C1 | Add compact social-proof band (3–6 reviews or instructor quotes w/ name/city) above or below FAQ | trust, SEO | **Critical** |
| C-C2 | Keep FAQ + GEO + newsletter in collection stack (mockup authority); Liquid gap is build follow-up | SEO, UX | **Critical** |
| C-R1 | Keep shop-first H1; strengthen SEO/category subhead + intro (Performance Skins vs grip socks) | SEO, education | **Recommended** |
| C-R2 | Sole cards: “Pick this if…” / Best-for discipline labels | conversion, education | **Recommended** |
| C-R3 | Surface Compare Styles near grid/chooser | education, conversion | **Recommended** |
| C-R4 | Product card value line (“replaces 6–8 socks”) near $74 | conversion | **Recommended** |
| C-O1 | Color facet + richer sort | UX | **Optional** |
| C-O2 | Discipline shop tabs | conversion | **Optional** |
| C-O3 | Dedicated 3-card benefit grid | education | **Optional** |

---

## 3. PDP

### 3.1 Current section inventory

**APPROVED July 17 (composition authority)**
1. Gallery + buy box (badge, title, stars, price, installments, size, swatches, ATC, trust)  
2. 50/50 grip / editorial  
3. 50/50 problem (“Yoga Socks Are Useless”)  
4. Variant grid (shop all colors)  
5. Full-bleed  
6. Sock Math  
7. 50/50 lifestyle / quote  
8. Reviews  
9. Guarantee-style split  
10. Juicer / UGC  
11. FAQ  
12. GEO  
13. Newsletter  
14. Sticky ATC  

**Liquid `product.json` today:** pdp-buy-box → value-strip → pdp-features → fifty-fifty-video → variant-grid → fifty-fifty-lifestyle → pdp-sock-math → pdp-reviews → GEO → newsletter → sticky ATC  

**v49 Enhanced (not composition authority):** adds dedicated 6-pillars, justifier testimonials, stronger motion — use as **component/token** reference and optional module source only.

### 3.2 Missing vs architecture / concepts / CRO

| Gap | Source | Severity class |
|-----|--------|----------------|
| Global announcement strip | Home/Collection parity | **Critical** |
| Justifier testimonials | `planning/05` §7, v49 | Recommended |
| Dedicated motion module | `planning/05` §6 | Recommended (Liquid has video fifty-fifty) |
| 6-pillar strip | `planning/05` | Optional (value-strip OK) |
| Buy-box micro-quotes | CRO P-02 | Recommended |
| Size guide modal + exchange line | CRO P-05/P-06 | Recommended |
| Price anchoring near $74 | CRO P-01 | Recommended |
| Gallery swipe + demo clip | CRO P-07 | Recommended |
| Swatch touch target ≥44px | CRO | Recommended |
| Cross-sell Open↔Closed | CRO P-14 | Optional |

### 3.3 Improvements

| ID | Improvement | Purpose | Priority |
|----|-------------|---------|----------|
| P-C1 | Declare PDP composition = July 17 APPROVED; tokens = v49 (no full v49 Enhanced rewrite) | brand, UX | **Critical** |
| P-C2 | Include global announcement strip on PDP | conversion, trust | **Critical** |
| P-R1 | Keep / restore UGC (Juicer or Judge.me photos) if July 17 stack wins | trust | **Recommended** |
| P-R2 | Import justifier strip from v49 **or** elevate 2–3 micro-quotes into buy box (pick one pattern) | trust, conversion | **Recommended** |
| P-R3 | Size guide as modal + free size-exchange line at size pills | UX, conversion | **Recommended** |
| P-R4 | Light price anchoring near buy-box price (cost-per-class / replaces socks) | conversion | **Recommended** |
| P-R5 | Mobile gallery swipe; optional demo clip in media | UX, education | **Recommended** |
| P-O1 | Full 6-pillar strip | education | **Optional** |
| P-O2 | Cross-sell + sticky color preview | conversion, UX | **Optional** |

---

## 4. Cross-page consistency

| Element | Home | Collection | PDP | System note |
|---------|------|------------|-----|-------------|
| Announcement strip | Yes | Yes | Add | Global — Critical on PDP |
| Value / trust strip | Yes | Yes | Yes | Shared; **not** 6-pillar strip at launch |
| Disciplines proof | Yes | Yes | Via features | Shared component family |
| Variant grid + quick-add | Yes | Yes | Yes | Shared — keep API consistent |
| Sock Math | Lite | No | Full | Intentional funnel depth |
| Reviews | Yes | **Add** | Yes | Collection Critical gap |
| FAQ | No | Yes | Yes | Home OK without if GEO present |
| GEO | Add to mockup | Yes | Yes | Uphold D-022 everywhere |
| Guarantee | Yes | Via FAQ/trust | Yes | Keep Home/PDP emphasis |
| UGC | Instagram | Via reviews band | Juicer/Judge.me | One proof language, three densities |
| Coperni | Seasonal Home | SKU/tab | Swatch/badge | Campaign policy |
| Nav “Grippy Shoes” vs body “Performance Skins” | All | All | All | Keep (`planning/11`) |
| Tokens (charcoal / rust / cream / gold stars) | Yes | Yes | Yes | v49 ADRs — do not redesign |

**Do not force identical mid-pages.** Force identical: strip, value props, grid behavior, GEO presence, review voice, CTA button system (`docs/component-system.md` patterns).

---

## 5. Decision Packet

All true product decisions needing Owner input live here. Work proceeds on **Recommended** defaults. Override by Decision ID only.

### STOP-level (materially changes architecture / composition)

These two choices change what “the page is.” Everything else is additive.

| ID | Decision | Options | **Recommended** | Why | Impact if wrong |
|----|----------|---------|-----------------|-----|-----------------|
| **DP-01** | Homepage hero messaging (D-041) | A: “Pilates Sock Era Is Over” (APPROVED / `hero.liquid`) · B: “Think Outside the Sock” (`hero-alt.liquid`) | **A** | Matches APPROVED mockup, category-creation North Star, and existing paid creative language; B is softer and less category-clear for cold traffic | Wrong hero = rebuild creative + confuse Meta/landing continuity; recoverable but expensive |
| **DP-02** | Canonical composition authority | July 17 / Definitive-v4 as above · Matured hybrid · Full v49 Enhanced PDP rewrite | **July 17 Home+PDP + Definitive-v4 Collection; v49 = tokens/components only** | Ends dual-lineage thrash; Liquid already closer to July 17 path than Enhanced | Picking Enhanced as page authority forces large PDP rebuild and orphan July 17 assets |

---

### Standard decisions (batch — proceed on Recommended)

| ID | Decision | Options | **Recommended** | Why | Impact if wrong |
|----|----------|---------|-----------------|-----|-----------------|
| **DP-03** | Home GEO (D-022 vs APPROVED HTML) | Keep GEO · Amend D-022 to exclude Home | **Keep GEO** (add to Home mockup) | Policy already decided High; Liquid already ships it; SEO/AI cost of removing is high | Amending D-022 weakens AI retrieval; keeping GEO is low visual cost if accordion |
| **DP-04** | Collection hero framing | Shop-first H1 · Category-creation H1 | **Shop-first H1 + stronger category/SEO subhead** | Pillar is dual-purpose; shoppers need “shop all” clarity; SEO can live in subhead + body + FAQ | Pure SEO H1 may hurt shop clarity; pure shop H1 without subhead leaves SEO soft |
| **DP-05** | Collection social proof | Add reviews band · Skip for launch | **Add 3–6 curated reviews/instructor quotes** | Explicit pillar requirement in `planning/09` + `12` | Skipping fails SEO/trust checklist; adding wrong quotes is easy to swap |
| **DP-06** | Collection FAQ in stack | Keep (Definitive-v4) · Drop | **Keep FAQ + schema** | Decision support + SEO; mockup already has it | Dropping hurts long-tail and AI answers |
| **DP-07** | PDP lineage extras | July 17 pure · Hybrid (justifier and/or motion from v49) · Full Enhanced | **July 17 + buy-box micro-quotes (or justifier if assets ready); keep Liquid video fifty-fifty as motion** | Highest trust ROI without rewrite; motion already partially in Liquid | Full Enhanced delays launch; pure July 17 without any mid-funnel quotes leaves trust lower |
| **DP-08** | Coperni on Home | Evergreen · Seasonal/campaign | **Seasonal** | Limited-edition energy dies if left forever | Evergreen feels stale; seasonal needs a swap plan |
| **DP-09** | UGC pattern | Keep IG + Juicer · Judge.me only · Drop | **Keep Home IG + PDP UGC; Collection uses review band (DP-05)** | Trust density matches funnel stage | Dropping UGC removes social proof; triple UGC widgets = clutter |
| **DP-10** | 6-pillar strip vs value-strip | Force pillars on all 3 · Keep value-strip | **Keep value-strip**; pillars Optional later | Avoid duplicate disciplines + pillars; value-strip already shared | Pillars add length; low incremental clarity |
| **DP-11** | Founder / Manifesto / full Sock Math on Home | Add now · Defer | **Defer** Founder/Manifesto to About; keep Sock Math lite; full Sock Math Optional | Protect conversion spine length | Adding all three bloats Home and dilutes ATC |
| **DP-12** | Patch locked docs `planning/05/06/09` to match chosen stacks | Patch after this packet · Leave docs divergent | **Patch (doc-only) after Owner ack of DP-01–DP-02** | Authority conflict is the #1 design-system debt | Leaving docs wrong guarantees builder thrash |

---

## 6. Critical checklist (before launch — design-complete bar)

Count: **8 Critical** items across pages/system.

1. **DP-01 / H-C1** — Hero Concept A (default)  
2. **DP-02 / P-C1** — Composition authority locked as table in §0  
3. **DP-03 / H-C2** — Home GEO present  
4. **DP-05 / C-C1** — Collection testimonials/reviews band  
5. **DP-06 / C-C2** — Collection FAQ in stack  
6. **P-C2** — PDP announcement strip  
7. **DP-12** — Doc reconciliation of `05/06/09` (documentation follow-up)  
8. **Cross-page** — Shared value-strip + variant-grid + GEO presence on all three  

*(Implementation of Liquid gaps is out of scope for this PR; the design-complete bar is the approved system above.)*

---

## 7. Recommended defaults summary (for Owner skim)

| ID | Recommended choice |
|----|--------------------|
| DP-01 | Hero **A** — Sock Era |
| DP-02 | July 17 Home/PDP + Definitive-v4 Collection; v49 tokens only |
| DP-03 | **Keep** Home GEO |
| DP-04 | Shop-first H1 + stronger SEO subhead |
| DP-05 | **Add** Collection reviews band |
| DP-06 | **Keep** Collection FAQ |
| DP-07 | July 17 + micro-quotes/justifier; keep video fifty-fifty |
| DP-08 | Coperni **seasonal** |
| DP-09 | Home IG + PDP UGC; Collection via reviews |
| DP-10 | **Keep** value-strip (no forced 6-pillars) |
| DP-11 | **Defer** Founder/Manifesto/full Sock Math |
| DP-12 | **Patch** `05/06/09` after DP-01/02 ack |

---

## 8. Explicit non-actions

- No Shopify theme edits in this workstream deliverable.  
- No “LOCKED” declaration on pages.  
- No Cart / About / Compare / Apparel scope.  
- No redesign of ADR tokens (palette, radii, stars).  
- CRO Phase 1 experiments remain post-design-complete tests, not composition reopeners.  
- Parallel `component-system` / `cro-phase-1` branches inform this review; not merged here.

---

## 9. Relation to prior Phase 1 review

`planning/design-completion-phase1-core-pages-review.md` remains as historical inventory. **This document supersedes it for active work:** blockers are collapsed into the Decision Packet; Recommended defaults are the forward path; Critical items are the launch bar — not a freeze.

---

## 10. Sign-off (lightweight)

| Role | Action |
|------|--------|
| Review author | System review complete — 2026-07-20 |
| Owner | Override any DP-* Recommended choice by ID; silence = proceed on Recommended |
| Architect | Schedule doc patch for `05/06/09` after DP-01/02 |
| Builder | Wait for design-complete Critical bar; no impl in this PR |
