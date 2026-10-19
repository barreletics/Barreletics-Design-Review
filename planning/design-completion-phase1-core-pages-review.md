# Design Completion Phase 1 — Core Pages Lock Review

> **Superseded for active work** by [`planning/design-completion-core-pages-system.md`](design-completion-core-pages-system.md) (v2 — conversion system + Decision Packet). Keep this file as historical inventory; do not open new blockers from §1/§8 here.

---
document: Design Completion Phase 1 — Home / Collections / PDP Lock Review
version: 1.0
status: ⚪ Historical — superseded by design-completion-core-pages-system.md
created: 2026-07-20
branch: design-completion-phase1-core-review
scope: Homepage · Collections (`/collections/grippy-shoes` pillar) · PDP only
depends_on:
  - planning/01–13 (Foundation)
  - planning/04-component-library.md
  - planning/05-pdp-architecture.md
  - planning/06-homepage-architecture.md
  - planning/09-collection-architecture.md
  - planning/10-decision-log.md (esp. D-022, D-041)
  - planning/11-navigation-architecture.md
  - planning/12-seo-geo-standards.md
  - Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html
  - origin/cro-phase-1 → planning/cro-phase-1-roadmap.md (PR parallel)
  - origin/component-system → docs/component-system.md (PR parallel)
---

**Explicit constraint:** No implementation until Owner approves this review’s decisions. Docs PRs #10–#16 are parallel/non-blocking; this review does not merge them.

---

## 1. Executive Verdict

### **Not yet ready to lock** — lockable after Owner resolves the conditions below.

The July 17 approved HTML pages and Collection Definitive-v4 are strong conversion compositions and largely match the live Liquid templates. They are **not** yet lock-ready because:

1. **Authority conflict** — Locked architecture docs (`planning/05`, `06`, `09`) describe different section stacks than the HTML files they cite as “Approved Source.”
2. **Hero not locked (D-041)** — Two homepage hero concepts remain open; foundation explicitly says do not lock until Owner picks.
3. **PDP dual lineage** — Design-system skill / ADRs treat **v49** as token/component truth; page architecture cites **PDP APPROVED July 17**; Liquid `product.json` follows the July 17 / Definitive path, not the fuller v49 Enhanced stack (justifier, dedicated motion, 6-pillar strip).
4. **Policy gaps vs Decision Log** — D-022 requires GEO on Homepage; Home APPROVED HTML has no GEO section (Liquid `index.json` does). Collection Definitive-v4 lacks customer testimonials required by pillar SEO (`planning/09`, `planning/12`).
5. **High-value orphans** — Founder Letter, Manifesto, full Sock Math, justifier feed, and several Decision Matrix sections exist in the repo but are absent from the three lock candidates — each needs a deliberate Keep / Defer / Skip.

**Conditions to lock (minimum):**

| # | Condition | Owner action |
|---|-----------|--------------|
| C1 | Pick canonical mockup per page (see §6) | Approve authority table |
| C2 | Resolve D-041 hero concept A vs B | Pick one headline system |
| C3 | Reconcile `planning/05/06/09` section lists to match chosen mockups (doc-only) | Approve rewrite scope |
| C4 | Decide GEO on Home (D-022 vs APPROVED HTML) | Keep Liquid GEO or amend D-022 |
| C5 | Decide Must-list in §5 (≤8 items) | Approve Must / defer rest |

Until C1–C5 are answered, treat pages as **freeze-candidates**, not locked.

---

## 2. Inventory — What Was Reviewed

### Lock-candidate mockups (primary)

| Page | Canonical candidate | Path | Notes |
|------|---------------------|------|-------|
| Home | **APPROVED July 17** | `barreletics-design-review/design_handoff_barreletics 2/pages/Barreletics Home - APPROVED July 17.html` | Matches Definitive-v8 structure; cited by `planning/06` |
| Collection | **Definitive-v4** | `…/Barreletics Collection - Definitive-v4.html` | Cited by `planning/09`; newest collection artifact |
| PDP | **APPROVED July 17** | `…/Barreletics PDP - APPROVED July 17.html` | Cited by `planning/05`; Definitive-v8 ≈ same stack |

### Parallel / competing artifacts (not ignored)

| Artifact | Path | Role in this review |
|----------|------|---------------------|
| Home Matured | `…/Barreletics Home - Matured.html` | Source of Founder / Manifesto / rotating eyebrow / fuller narrative |
| Home v24 | `files/Barreletics_Home_v24.html` | Audit lineage; asset inventory; not lock source |
| PDP v49 Final / Enhanced | `…/Barreletics PDP - v49 Final.html`, `… v49 Enhanced.html` | Token/component authority; justifier + motion + pillars |
| PDP Complete v49 | `archive/pdp-history/PDP Complete v49.html` | Design-system skill source of truth |
| Section Decision Matrix | `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` + `sections/*-section.html` | Orphan section library |
| Liquid templates | `shopify-build/templates/{index,collection,product}.json` | What is actually assembled today |
| Component library | `planning/04-component-library.md` | Declared reusable components |
| Component system (branch) | `origin/component-system:docs/component-system.md` | Permanent UI library draft |
| CRO Phase 1 (branch) | `origin/cro-phase-1:planning/cro-phase-1-roadmap.md` | Friction + experiment backlog (post-lock tests, not redesign) |
| Brand / SEO / Nav | `planning/01`, `02`, `11`, `12`, `07`, `13` | Messaging + SEO obligations |

---

## 3. Per-Page Review

### 3.1 Homepage

#### Current section stack (APPROVED July 17)

1. Announcement strip  
2. Hero — “The Pilates Sock Era Is Over” + Shop Now / See Why  
3. Problem — “Yoga Socks Are Useless”  
4. Disciplines proof  
5. Lineup (full color strip)  
6. Variants grid (Closed/Open + size + quick-add)  
7. Value strip (inside / after lineup area — trust props, not 6 brand pillars)  
8. Editorial quote (Mia Evans)  
9. 50/50 — “Upgrade Your Grip…”  
10. Coperni collab  
11. Full-bleed statement  
12. Reviews  
13. 50/50 Sock Math lite — “One Pair. Done.” ($74 vs $112–$144/yr)  
14. Instagram / UGC  
15. Guarantee — “Zero risk. All grip.”  
16. Newsletter  

**Absent vs `planning/06` architecture:** dedicated 6-item Pillar Strip; full Sock Math (dark, 6-cell); Founder Letter; Manifesto; Closing Statement as standalone; rotating 5-message eyebrow; FAQ; GEO.

**Present in Liquid `index.json` but not in APPROVED HTML:** `geo-section`.  
**Present in APPROVED HTML but missing/weak in Liquid:** Problem, Lineup, Coperni, Instagram, Guarantee (Liquid collapses narrative to hero → value-strip → disciplines → grid → two 50/50s → social-proof → GEO → newsletter).

#### Architecture comparison

| Arch § (`planning/06`) | In APPROVED HTML? | In Liquid? | Assessment |
|------------------------|-------------------|------------|------------|
| Hero + rotating eyebrow | Hero yes; rotation **no** | Hero yes; rotation **no** | Align docs to static eyebrow **or** restore rotation from Matured |
| Pillar Strip (6) | **No** (value-strip ≠ pillars) | value-strip only | Owner: keep value-strip as intentional simplification |
| Product grid + quick-add | Yes | Yes | Lock-ready |
| Full Sock Math | Lite 50/50 only | Lite 50/50 | Full module orphaned in `sections/sock-math.html` |
| Founder / Manifesto / Closing | No | No | Strong brand orphans — see table |
| Reviews | Yes | social-proof | Lock-ready |
| Newsletter | Yes | Yes | Lock-ready |
| GEO (D-022) | **No** | **Yes** | Must resolve before lock |

#### Messaging hierarchy & conversion flow

**Strengths:** Category disruption early (Problem → Disciplines → Shop). Price + grid mid-page. Sock Math lite after social proof. Guarantee before email. Clear path: declare → prove → shop → validate → close.

**Friction (from CRO roadmap — flag for post-lock tests, not redesign):** generic “Shop Now”; mobile product image below fold; Performance Skins vs Grippy Shoes label split; no video above fold.

#### Desktop / mobile

- Desktop composition is coherent (one narrative spine).  
- Mobile: hero stacks copy-first (CRO H-09). Touch targets on primary CTAs OK; watch swatch/quick-add density on grid.  
- Sticky ATC appears in mockup CSS patterns — confirm Home doesn’t surface product sticky incorrectly (PDP-only intent).

#### Simplify / improve (purpose-tagged)

| Rec | Purpose | Note |
|-----|---------|------|
| Pick hero concept (D-041) | brand / conversion | Blocker |
| Add GEO accordion (match Liquid + D-022) **or** amend D-022 | SEO | Blocker |
| Decide Coperni permanence (seasonal vs evergreen) | brand | Owner |
| Decide IG feed vs Juicer vs static UGC | trust / conversion | Owner |
| Do **not** add Founder+Manifesto+full Sock Math without cutting elsewhere | UX | Avoid page bloat |

#### Owner-approval needed (Home)

- D-041 hero A vs B  
- GEO on / off for Home  
- Canonical stack = APPROVED HTML vs Liquid vs Matured hybrid  
- Coperni + IG keep/seasonalize  

---

### 3.2 Collections — Grippy Shoes pillar

#### Current section stack (Definitive-v4)

1. Announcement strip  
2. Collection hero — “Shop All Styles & Colors” + Open/Closed education  
3. Sole explain cards (chooser)  
4. Mid-value trust strip  
5. Variants grid (All / Closed / Open / One-Offs / Outdoor + size + Compare)  
6. Disciplines proof  
7. 50/50 — “Never Loses Grip.”  
8. 50/50 — “Commit to the Gear.”  
9. Trust FAQ (+ repeated trust row)  
10. GEO accordion  
11. Newsletter  

#### Architecture comparison (`planning/09`)

| Arch § | In Definitive-v4? | In Liquid `collection.json`? | Assessment |
|--------|-------------------|------------------------------|------------|
| Category-creation hero | Partial — shopping H1, less “socks era” framing | Same | Consider stronger SEO H1 (doc 12) without killing shop clarity |
| Pillar Strip (6) | **No** (mid-value trust strip) | value-strip | Intentional simplification OK if documented |
| Sole Type Chooser | Yes (`sole-explain`) | `show_sole_cards: true` | Lock-ready |
| Product grid + facets | Yes (tabs; limited facets) | Yes | Color facet / sort — Should |
| Benefit grid (3 cards) | Absorbed into mid-value / disciplines | No dedicated | Optional |
| Category-creation 50/50 | Yes (×2) | Yes (×2) | Lock-ready |
| FAQ + schema | Yes | **Missing from collection.json** | Must — Liquid gap |
| GEO | Yes | Yes | Lock-ready |
| Newsletter | Yes | **Missing from collection.json order** | Should |
| Testimonials on pillar | **No** | No | Must for SEO pillar requirements |

#### Messaging hierarchy & conversion flow

**Strengths:** Decision support before grid (Open vs Closed). Compare link in toolbar. Disciplines after products = education without blocking shop. FAQ + GEO for SEO/AI.

**Gaps:** No reviews/UGC on pillar (trust + SEO). Hero leans merchandising (“Shop All Styles”) over category creation (“grip socks → Performance Skins”). CRO C-04 / C-02: discipline labels + value framing on cards.

#### Desktop / mobile

- Filter chips horizontal — good.  
- Grid density OK for SKU count.  
- Sole cards: ensure mobile stack order keeps “pick this if…” readable above fold after short scroll.

#### Simplify / improve

| Rec | Purpose | Note |
|-----|---------|------|
| Add 3–6 curated reviews or editorial proof band | trust / SEO | Pillar requirement |
| Align collection.json with Definitive-v4 (FAQ + newsletter) | UX / SEO | Implementation after approval |
| Stronger category H1/subhead (keep shop CTA) | SEO / education | Copy approval |
| Discipline “Best for…” on sole cards | conversion / education | CRO C-04 — can be post-lock test |
| Do not add Sock Math + Founder here | UX | Keep pillar shop-first |

#### Owner-approval needed (Collection)

- Hero: shop-first vs category-creation-first  
- Reviews/UGC on pillar Y/N  
- FAQ presence in Liquid (sync to mockup)  

---

### 3.3 PDP

#### Current section stack (APPROVED July 17)

1. Gallery + buy box (badge, title, stars, price, installments, size, swatches, ATC, trust cues)  
2. 50/50 grip / obsession editorial  
3. 50/50 problem (“Yoga Socks Are Useless”)  
4. Variant grid (shop all colors)  
5. Full-bleed  
6. Sock Math (comparison cards, $144 strike)  
7. 50/50 lifestyle / quote  
8. Reviews  
9. Guarantee-style split  
10. Juicer / UGC  
11. FAQ  
12. Newsletter  
13. Sticky ATC  

**v49 Enhanced adds / changes:** dedicated pillar/value treatment, justifier testimonials, “See how it works” motion, dual review treatments, stronger feature grid — **not** 1:1 with July 17.

#### Architecture comparison (`planning/05` vs v49 vs Liquid)

| Arch § | July 17 APPROVED | v49 Enhanced | Liquid `product.json` |
|--------|------------------|--------------|------------------------|
| Gallery + buy box | Yes | Yes | pdp-buy-box |
| Brand Pillars strip | **No** | Yes | value-strip (trust, not 6 pillars) |
| Variant grid | Yes | Yes | Yes |
| Reviews | Yes | Yes (+ Judge.me style) | pdp-reviews |
| Sock Math | Yes | Yes | pdp-sock-math |
| Motion | Embedded / weak | Dedicated | fifty-fifty video |
| Justifier testimonials | **No** | **Yes** | **No** |
| FAQ | Yes | Yes | (check template — FAQ may be in buy-box accordion / separate) |
| Newsletter | Yes | Yes | present |
| Sticky ATC | Yes | Yes | pdp-sticky-atc |
| GEO | Yes (in APPROVED) | Weak / absent in Enhanced | Yes |
| UGC / Juicer | Yes | No | No dedicated |

#### Messaging hierarchy & conversion flow

**Strengths:** Buy box first; category disruption close to ATC; Sock Math for price anchoring; sticky ATC; FAQ for objections.

**Friction (CRO — post-lock tests unless Owner pulls into Must):** price before sock math in buy box; size anxiety (M/L only); reviews far below fold; size chart navigation-away; no gallery video; swatch touch size borderline.

#### Desktop / mobile

- Desktop two-column buy box matches system.  
- Mobile: gallery → buy box → long scroll; sticky ATC critical.  
- Prefer swipe gallery (CRO P-07) as Should after lock.

#### Simplify / improve

| Rec | Purpose | Note |
|-----|---------|------|
| Declare single PDP authority: July 17 **or** v49 Enhanced hybrid | brand / UX | Blocker |
| If July 17: document pillars/justifier/motion as deferred orphans | trust / education | Avoid silent loss |
| If hybrid: import justifier + motion only (highest trust/education ROI) | trust / education | Prefer over full v49 rewrite |
| Buy-box micro-quotes (CRO P-02) | conversion / trust | Should — low effort |
| Size guide modal + free exchange line | conversion / UX | Should |
| Keep Juicer/UGC if July 17 wins | trust | Don’t drop without replacement |

#### Owner-approval needed (PDP)

- Lock source = APPROVED July 17 vs v49 Enhanced vs hybrid  
- Justifier + motion Keep / Defer  
- UGC module Keep / Defer  

---

## 4. Cross-Page Consistency

| Element | Home | Collection | PDP | Verdict |
|---------|------|------------|-----|---------|
| Announcement strip | Yes | Yes | Often absent in mockup | PDP should inherit global strip |
| Value / trust strip | Yes | Yes | Yes (Liquid) | Consistent; **not** 6-pillar strip |
| Disciplines proof | Yes | Yes | Via features | Shared — good |
| Variant grid | Yes | Yes | Yes | Shared component — good |
| Sock Math | Lite | No | Full | Intentional; document |
| Reviews | Yes | **No** | Yes | Collection gap |
| FAQ | No | Yes | Yes | Home OK without if D-022 GEO exists |
| GEO | Mockup no / Liquid yes | Yes | Yes | Home inconsistency |
| Guarantee | Yes | Via trust/FAQ | Yes | Good |
| UGC / IG | Yes | No | Juicer | Decide shared UGC pattern |
| Coperni | Yes | In grid SKU | Swatch | Seasonal policy needed |
| Nav label “Grippy Shoes” vs body “Performance Skins” | All pages | All | All | By design (`planning/11`) — keep |
| Tokens (v49 charcoal/rust/cream) | Yes | Yes | Yes | Consistent |

**Cross-page recommendation:** One shared **Trust strip** + one shared **Disciplines** + one shared **Variant grid** is already the right system. Do not force identical mid-page narratives (Home = brand story, Collection = decide+shop, PDP = convert).

---

## 5. Orphan Ideas Table

Ideas, sections, or components that exist in the project but are **not** fully incorporated into the three lock-candidate pages.

| Idea | Source path | Page(s) | Incorporate? | Why |
|------|-------------|---------|--------------|-----|
| Founder Letter | `sections/founder-letter.html`, Home Matured, `planning/04` #15, `planning/06` §9 | Home | **N** (defer) | High brand value but long page already; better About first, Home later |
| Manifesto (+ rotation) | `sections/manifesto.html`, Home Matured, `planning/04` #16, `planning/06` §10 | Home | **N** (defer) | Brand theater; conversion ROI unclear; About/brand pages |
| Closing Statement (standalone) | `sections/closing-statement.html`, `planning/06` §11 | Home | **N** | Guarantee + newsletter already close; duplicate CTA risk |
| Rotating hero eyebrow (5 msgs) | Home Matured / v24, `planning/06` §1 | Home | **Y** if motion budget OK else **N** | Education density; respect `prefers-reduced-motion`; Owner call with D-041 |
| Full Sock Math (dark, 6-cell) | `sections/sock-math.html`, matrix §19, `planning/04` #8 | Home | **Y** (replace lite) **or** keep lite | Conversion/education; lite already present — upgrade only if Owner wants parity with PDP |
| 6-item Pillar Strip | `planning/04` #4, `planning/05/06/09`, v49 | All three | **N** for lock | Value-strip covers trust; pillars duplicate disciplines — avoid clutter |
| Justifier testimonials | v49 Enhanced/Final, `planning/05` §7 | PDP | **Y** (Should→Must if v49 hybrid) | Trust at mid-funnel; unique vs Judge.me grid |
| Dedicated Motion “See how it works” | v49, `planning/05` §6 | PDP (Home secondary CTA) | **Y** (Should) | Education for new category; video > more copy |
| Promo tiles / limited edition band | matrix §18, `sections/18-section.html` | Home | **N** | Merchandising noise unless drop calendar exists |
| Credibility / “As seen in” | `sections/credibility.html`, CRO trust gaps | Home | **Should** | Trust; only if real press logos available |
| Association strip | `sections/assoc.html`, `planning/04` #25 | Home | **N** | Overlaps credibility |
| Decision Matrix splits 20/21/23/24/26 | `sections/20–26-section.html` | Home/PDP | **N** | Superseded by APPROVED splits; archive |
| Coperni full video split | matrix §25, Home APPROVED Coperni | Home | **Keep as-is** | Already in Home APPROVED; seasonalize later |
| Instagram / Juicer UGC | Home APPROVED, PDP APPROVED | Home/PDP; Collection optional | **Y** keep on Home+PDP | Trust; Collection Should |
| GEO on Homepage | D-022, Liquid `index.json`, `planning/12` | Home | **Y** | Policy already requires it; mockup lag |
| Collection testimonials | `planning/09`, `planning/12` pillar reqs | Collection | **Y** | SEO + trust gap |
| Collection FAQ in Liquid | Definitive-v4 vs `collection.json` | Collection | **Y** | Mockup has it; template incomplete |
| Buy-box micro-quotes | CRO P-02 / trust §7 | PDP | **Y** (Should) | Conversion at decision point |
| Size guide modal + exchange reassurance | CRO P-05/P-06 | PDP | **Y** (Should) | UX / conversion |
| Price anchoring near $74 | CRO P-01 | PDP | **Y** (Should) | Conversion; copy-only |
| Open vs Closed “Best for…” labels | CRO C-04 | Collection | **Y** (Should) | Education / conversion |
| Card value subtitle (“replaces 6–8 socks”) | CRO C-02 | Collection/Home grid | **Y** (Nice→Should) | Conversion; test if contested |
| Discipline shop tabs | CRO C-10 | Collection | **N** for lock | Nav already has Open/Closed; post-lock test |
| Hero video above fold | CRO H-03 | Home | **Nice** | Education; asset + perf cost |
| Mobile image-first hero | CRO H-09 | Home | **Should** | UX / conversion mobile |
| Press logo bar | CRO H-07 | Home | **Nice** | Trust iff assets real |
| Compare Styles inline on Collection | CRO C-05, nav `planning/11` | Collection | **Should** | Decision support |
| Cross-sell Open↔Closed | CRO P-14, `recommendations.liquid` | PDP | **Nice** | AOV; after lock |
| Sticky ATC variant preview | CRO P-11 | PDP | **Nice** | UX |
| Component System formalization | `docs/component-system.md` (branch) | All | **N** for page lock | Parallel docs PR; non-blocking |
| Hero-alt “Think Outside the Sock” | `shopify-build/sections/hero-alt.liquid`, D-041 | Home | **Owner pick** | Cannot lock Home until chosen |

---

## 6. Recommended Canonical Authority (for Owner approval)

| Page | Proposed lock source | Secondary reference | Do not use as lock source |
|------|----------------------|---------------------|---------------------------|
| Home | APPROVED July 17 HTML **+** Liquid GEO (D-022) | Home Matured for deferred brand sections | Home v24 audit; Decision Matrix full 23-stack |
| Collection | Definitive-v4 HTML | `planning/12` for SEO copy depth | Collection Matured (superseded) |
| PDP | APPROVED July 17 HTML for **page composition** | v49 for **tokens/components** + optional justifier/motion | PDP Matured; v36 alone |

Architecture docs `planning/05/06/09` should be **doc-patched** after Owner approves this table so “Approved Source” and section lists match reality.

---

## 7. Prioritized Recommendations

### Must (before lock)

1. **Resolve D-041** — pick Home hero concept A or B. *(brand / conversion)*  
2. **Approve canonical authority table (§6)** — end July 17 vs v49 vs Matured ambiguity. *(brand / UX)*  
3. **Home GEO** — keep Liquid GEO and add to Home lock mockup, or formally amend D-022. *(SEO)*  
4. **Collection FAQ + newsletter parity** — Definitive-v4 → `collection.json`. *(SEO / conversion)*  
5. **Collection social proof band** — 3–6 reviews or instructor quotes. *(trust / SEO)*  
6. **PDP lineage decision** — July 17 pure vs hybrid (justifier + motion from v49). *(trust / education)*  
7. **Doc reconciliation** — update `planning/05/06/09` section lists to match chosen mockups (documentation only). *(UX / governance)*  
8. **Global announcement strip on PDP** — match Home/Collection. *(conversion / trust)*

### Should (immediately after lock / same sprint if Owner wants)

1. Buy-box micro-quotes + light price anchoring. *(conversion / trust)*  
2. Size guide modal + “free size exchange” near size pills. *(UX / conversion)*  
3. Sole cards “Best for…” discipline labels. *(education / conversion)*  
4. Mobile hero image-first test design (don’t ship both permanently). *(UX / conversion)*  
5. Compare Styles prominence on Collection grid. *(education / conversion)*  
6. Gallery swipe + optional demo clip in PDP media. *(UX / education)*  
7. Align Liquid Home closer to APPROVED (Problem, Guarantee, UGC) **or** explicitly retire those sections from the lock mockup. *(brand / trust)*  

### Nice (backlog / CRO Phase 1)

1. Full Sock Math upgrade on Home. *(education / conversion)*  
2. Founder Letter + Manifesto on About, then consider Home. *(brand)*  
3. Press / “As seen in” bar. *(trust)*  
4. Cross-sell + cart SAVE15 framing (CRO cart experiments). *(conversion)*  
5. Hero video, discipline tabs, promo tiles. *(education / merchandising)*  

---

## 8. Owner-Approval Required List

Decisions that **must not** be implemented by builders without an explicit Owner yes/no:

1. Homepage hero concept (D-041 A vs B)  
2. Canonical lock files per page (§6)  
3. Whether Home includes GEO (uphold D-022 vs APPROVED HTML)  
4. Whether Collection hero stays shop-first or shifts to category-creation SEO H1  
5. Whether Collection gains a reviews/UGC band  
6. PDP = July 17 only vs v49 hybrid (justifier / motion / pillars)  
7. Coperni block: evergreen vs campaign-only  
8. Instagram/Juicer: keep, replace with Judge.me UGC, or drop  
9. Any Must-list item that adds section length (Founder, Manifesto, full Sock Math, press bar)  
10. Permission to patch locked foundation docs `planning/05/06/09` to match reality  

---

## 9. What Is Already Strong (do not redesign)

- Category-creation narrative on Home (Problem → Disciplines → Shop).  
- Shared variant grid + quick-add pattern across pages.  
- Collection sole chooser before grid.  
- PDP Sock Math + sticky ATC + FAQ.  
- v49 token system (charcoal / rust / cream / 6px CTA / gold stars).  
- Nav strategy: “Grippy Shoes” wayfinding + “Performance Skins” education (`planning/11`).  
- Collection + PDP GEO accordions for AI/SEO.

---

## 10. Explicit Non-Actions

- **No implementation** of Must/Should/Nice items until Owner approves.  
- **No merges** of parallel docs PRs (#10–#16) as part of this work.  
- **No redesign** of locked visual tokens (ADR-01–07 / v49).  
- **No expansion** to Cart, About, Compare, or Apparel in this phase.  
- CRO experiments remain a **post-lock testing roadmap**, not a reason to reopen composition casually.

---

## 11. Suggested Owner Meeting Agenda (15 min)

1. Hero A vs B (2 min)  
2. Approve §6 authority table (3 min)  
3. Yes/No on Must #3–#6 (GEO, Collection FAQ/reviews, PDP hybrid) (5 min)  
4. Coperni + UGC seasonal policy (2 min)  
5. Authorize doc patch PR for `planning/05/06/09` (3 min)  

---

## 12. Sign-off

| Role | Status |
|------|--------|
| Review author | Complete — 2026-07-20 |
| Owner | ☐ Approve conditions C1–C5 / Must list |
| Architect | ☐ Confirm doc patch scope for 05/06/09 |
| Builder | ☐ No build until Owner sign-off |

**Lock status until sign-off:** `NOT READY TO LOCK`
