# SEO Platform — Long-Term Authority Architecture

---
document: SEO Platform
version: 1.0
status: 🔵 Ready for Review
last_modified: 2026-07-19
depends_on: [02-brand-system, 07-product-knowledge-base, 09-collection-architecture, 11-navigation-architecture, 12-seo-geo-standards]
technical_ref: docs/20-seo-architecture.md
---

## Strategic Premise

Barreletics is **replacing the grip sock category** with Performance Skins.

**Search strategy:** Target **sock queries to disrupt**, not shoe queries to compete. Rank where demand already lives (“grip socks,” “Pilates socks”), then convert visitors to grippy shoes / Performance Skins.

**North Star (search):** Move SERPs and AI answers from “best grip socks” → “grip sock alternatives” → “performance skins / grip shoes.”

All facts and claims must come from Doc 07. No retired claims (`RETIRED_CLAIMS.md`). GEO expansion remains **data-gated** (D-037).

---

## 1. Complete Keyword Map

### Intent legend
- **I** Informational · **C** Commercial · **T** Transactional · **N** Navigational

### Primary category terms (head) — P1

| Keyword | Intent | Target page | Priority |
|---------|--------|-------------|----------|
| grip shoes | C | `/collections/grippy-shoes` | P1 |
| grippy shoes | C | `/collections/grippy-shoes` | P1 |
| pilates shoes | C | `/collections/grippy-shoes` | P1 |
| barre shoes | C | `/collections/grippy-shoes` | P1 |
| yoga shoes | C | `/collections/grippy-shoes` | P2 |
| lagree shoes | C | `/collections/grippy-shoes` | P1 |
| studio shoes | C | `/collections/grippy-shoes` | P2 |
| reformer shoes | C | `/collections/closed-sole` | P1 |

### Category disruption terms (sock queries) — P1 strategic

| Keyword | Intent | Target page | Priority |
|---------|--------|-------------|----------|
| grip socks | C/I | `/collections/grippy-shoes` + `/pages/grip-comparison` | P1 |
| grippy socks | C | `/collections/grippy-shoes` | P1 |
| pilates socks | C | `/collections/grippy-shoes` | P1 |
| barre socks | C | `/collections/grippy-shoes` | P1 |
| yoga socks | C | `/collections/grippy-shoes` | P2 |
| best pilates socks | C | `/collections/grippy-shoes` | P1 |
| best barre socks | C | `/collections/grippy-shoes` | P1 |
| best yoga socks | C | `/pages/grip-comparison` | P2 |
| grip socks for pilates | C | `/collections/grippy-shoes` | P1 |
| grip socks for barre | C | `/collections/grippy-shoes` | P1 |
| non slip socks for pilates | C | `/collections/grippy-shoes` | P1 |
| toeless grip socks | C | `/collections/open-sole` | P2 |
| studio socks | C | `/collections/grippy-shoes` | P2 |

### Long-tail / problem-aware — P1–P2

| Keyword | Intent | Target page | Priority |
|---------|--------|-------------|----------|
| best shoes for reformer pilates | C | `/collections/closed-sole` | P1 |
| shoes for lagree megaformer | C | `/collections/grippy-shoes` | P1 |
| grip shoes for barre class | C | `/collections/grippy-shoes` | P1 |
| non slip shoes for pilates | C | `/collections/grippy-shoes` | P1 |
| shoes that grip on reformer | C | `/collections/closed-sole` | P1 |
| alternative to grip socks | C | `/pages/grip-comparison` | P1 |
| better than grip socks | C | `/pages/grip-comparison` | P1 |
| why grip socks don't work | I | Journal + grip-comparison | P1 |
| grip socks vs grip shoes | C | `/pages/grip-comparison` | P1 |
| do grip socks actually work | I | Journal / FAQ | P2 |
| grip socks keep slipping | I | Journal → PDP | P1 |
| feet sliding in pilates | I | Journal → collection | P1 |
| slipping during barre class | I | Journal → collection | P1 |
| best footwear for pilates reformer | C | `/collections/closed-sole` | P1 |
| shoes for megaformer | C | `/collections/grippy-shoes` | P1 |
| cadillac pilates footwear | C | `/collections/closed-sole` | P2 |

### Comparison / decision — P1

| Keyword | Intent | Target page | Priority |
|---------|--------|-------------|----------|
| grip socks vs barreletics | C | `/pages/grip-comparison` | P1 |
| best grip shoes for pilates [year] | C | `/collections/grippy-shoes` | P1 |
| open sole vs closed sole grip shoes | C | `/pages/compare-open-closed-sole` | P1 |
| are grip shoes better than grip socks | C | `/pages/grip-comparison` | P1 |
| pilates shoes review | C | PDP / Journal | P2 |
| barreletics review | N/C | Homepage / PDP | P1 |
| barreletics vs grip socks | C | `/pages/grip-comparison` | P1 |

### GEO-modified — P2–P3 (create only when D-037 criteria met)

| Pattern | Intent | Target | Priority |
|---------|--------|--------|----------|
| best pilates shoes [city] | C | Future GEO hub | P3 |
| grip shoes for barre [city] | C | Future GEO hub | P3 |
| pilates studio shoes [state] | C | State hub | P2 |
| where to buy grip shoes near me | T | Shipping/FAQ + GEO | P3 |

### Informational / educational — P1–P2

| Keyword | Intent | Target | Priority |
|---------|--------|--------|----------|
| what to wear to pilates class | I | Journal | P1 |
| what to wear to barre class | I | Journal | P1 |
| do you need special shoes for pilates | I | Journal → collection | P1 |
| what shoes for reformer pilates | I | Journal → closed-sole | P1 |
| can you wear socks on reformer | I | Journal / FAQ | P2 |
| pilates footwear guide | I | Journal pillar | P1 |
| barre class dress code | I | Journal | P2 |
| lagree class what to wear | I | Journal | P1 |

**Cluster count:** ~70 mapped terms across 6 intent groups.

---

## 2. Collection Keyword Strategy

| Collection | URL | Primary | Secondary | Intent |
|------------|-----|---------|-----------|--------|
| Shop All Grippy Shoes | `/collections/grippy-shoes` | grip shoes, grippy shoes | pilates shoes, barre shoes, lagree shoes, studio shoes | Commercial |
| Open Sole | `/collections/open-sole` | open sole grip shoes | barefoot pilates shoes, open heel grip shoes | Commercial |
| Closed Sole | `/collections/closed-sole` | closed sole grip shoes | reformer shoes, full coverage pilates shoes | Commercial |
| Outdoor | `/collections/outdoor` | outdoor grip shoes | water shoes, beach grip shoes (secondary only) | Commercial |
| New Arrivals | `/collections/new-arrivals` | new grip shoes | new barreletics colors | Commercial |
| Limited Editions | `/collections/limited-editions` | limited edition grip shoes | barreletics limited edition | Commercial |
| Sale | `/collections/sale` | barreletics sale | grip shoes sale | Transactional |

### Per-collection SEO templates

**Title tag:** `{Primary Keyword} | Barreletics` (≤60 chars when possible)  
Example: `Grippy Shoes for Pilates & Barre | Barreletics`

**Meta description:** Problem → category shift → proof → CTA. Include $74 and Made in USA when natural.  
Example: `Replace grip socks with Performance Skins — 360° grip, rinse-clean, Made in USA. Shop Open Sole & Closed Sole from $74.`

**H1:** Category/customer language, not stuffed. Pillar H1 can lead with grippy shoes / studio performance framing per Doc 08.

**Description body:** Educational intro + buying guidance + sock-vs-skin framing (no competitor names). Natural keyword integration only.

**Internal links TO collection:** Homepage, journal CTAs, FAQ, grip-comparison, related PDPs, footer Shop links.  
**Internal links FROM collection:** Sub-collections, compare page, size guide, FAQ, top PDPs.

---

## 3. PDP Keyword Strategy

| Product type | URL pattern | Primary | Secondary / long-tail |
|--------------|-------------|---------|------------------------|
| Open Sole [Color] | `/products/[handle]` | [color] open sole grip shoes | [color] pilates shoes, [color] barre shoes |
| Closed Sole [Color] | `/products/[handle]` | [color] closed sole grip shoes | [color] reformer shoes, full coverage [discipline] |

### PDP on-page rules

| Element | Guidance |
|---------|----------|
| Title | Style + color + “Grippy Shoes” / Performance Skin framing |
| Meta | Keyword + Open/Closed differentiator + $74 + trust signal |
| Image alt | Descriptive: style, color, context (e.g. “Closed Sole Dark Grey grippy shoes on reformer”) — no stuffing |
| Description | Doc 07 facts; weave primary keyword once in first 100 words |
| FAQ schema | Size, Open vs Closed, care, returns, vs grip socks |
| Reviews | AggregateRating from Judge.me (never hardcoded) |

---

## 4. GEO Content Strategy (D-037)

**Do not mass-produce city pages.** Qualify first.

### Qualification criteria (all preferred)

1. Material Shopify order concentration  
2. Studio density / partner presence  
3. Distinct local content possible (not boilerplate)  
4. Clear conversion path to collection/PDP  
5. Search demand signal (GSC / keyword tools)

### Tier 1 — State hubs (when data supports)

Priority candidates (validate with Shopify geo): Florida, Texas, California, New York, then next revenue states.

| Item | Spec |
|------|------|
| URL | `/pages/grip-shoes-[state]` or journal hub (choose one pattern and stick) |
| Title | `Grip Shoes for Pilates & Barre in [State] \| Barreletics` |
| Content | Why studios choose Performance Skins, shipping note, 2–3 local studio mentions only if real, FAQ, CTA to pillar |
| Schema | FAQPage + Organization; avoid fake LocalBusiness NAP |

### Tier 2 — City pages

Only with genuine local value (partner studio, event, measurable demand). Template: intro · studio context · what to wear · product CTA · FAQ. Anti-thin: unique paragraphs, real names, no spun clones.

### Tier 3 — International

Canada / UK / Australia when order data justifies. Trust signal: ships internationally (FedEx / 195 countries per Doc 07) — do not invent local inventory.

---

## 5. Internal Linking Architecture

```
Homepage (authority hub)
├── /collections/grippy-shoes (primary pillar)
│   ├── /collections/open-sole
│   ├── /collections/closed-sole
│   ├── /collections/outdoor
│   └── /pages/compare-open-closed-sole
├── /pages/grip-comparison (disruption pillar)
├── /pages/faq (knowledge hub)
├── /pages/about (brand)
├── /blogs/journal (content hub)
│   └── discipline + disruption articles → pillar + PDPs
└── Policy/support pages (size, shipping, returns, warranty)
```

| From | Link to | Anchor direction |
|------|---------|------------------|
| Journal discipline guides | Pillar + relevant sub-collection | “shop grippy shoes for [discipline]” |
| Grip comparison | Open/Closed collections + PDPs | “see Open Sole” / “shop Closed Sole” |
| PDP | Pillar + compare + size guide | breadcrumb + body links |
| FAQ | Collections + policies | topical anchors |
| Footer | Pillar, FAQ, Journal, key policies | brand + utility |

**Rules:** Every PDP links up to pillar. Every article has 3–5 contextual internal links. Prefer descriptive anchors over “click here.”

---

## 6. Blog / Journal Architecture

**Hub URL:** `/blogs/journal` (not `/blogs/blog`)

### Content pillars

1. **Discipline guides** — Barre, Pilates, Reformer, Lagree, Megaformer, Cadillac, Yoga  
2. **Product education** — Open vs Closed, care, sizing, materials  
3. **Category disruption** — Why grip socks fail, socks vs shoes, sock math  
4. **Studio life** — Spotlights, instructors (rights-cleared)  
5. **GEO** — Only when D-037 qualified  

### Article templates

| Type | Keyword pattern | Words | Internal links | CTA |
|------|-----------------|-------|----------------|-----|
| Discipline guide | what to wear to [discipline] | 1500–2500 | 3–5 | Shop collection |
| Product education | [feature] explained | 800–1200 | 2–3 | Compare styles |
| Category disruption | grip socks vs … | 1200–2000 | 3–5 | Grip comparison / shop |
| Studio spotlight | [studio] [city] | 600–1000 | 1–2 | Find your grip |

### Calendar framework

- Cadence target: 2–4 evergreen pieces / month once staffing allows  
- ~80% evergreen / 20% timely (launches, seasons)  
- Refresh top GSC pages quarterly (titles, FAQs, internals)  
- Move names only from Doc 07 Appendix (verified)

---

## 7. Pillar Pages

### Primary — Shop All Grippy Shoes

**URL:** `/collections/grippy-shoes`  
**Must compete for:** grip shoes, grippy shoes, pilates shoes, barre shoes, sock head terms (via educational blocks)  
**Required modules:** educational intro · buying guide · product grid · Open vs Closed · FAQ + schema · social proof · optional GEO (data-gated)

### Secondary — Grip Comparison

**URL:** `/pages/grip-comparison`  
**Must compete for:** grip socks vs grip shoes, alternative to grip socks  
**Required modules:** Double Failure framing · Sock Math · materials · longevity range language · CTAs to collections

### Tertiary

- Sub-collections (Open/Closed/Outdoor)  
- FAQ hub  
- Compare Open vs Closed page  

---

## 8. FAQ Expansion

| FAQ question | Target query | Volume (est.) | Current | Expansion |
|--------------|--------------|---------------|---------|-----------|
| Open vs Closed Sole? | open sole vs closed sole | Low–Med | PDP, Compare | Keep + reinforce Compare |
| How long do they last? | how long do grip shoes last | Low | PDP FAQ | Journal with testimonials (range language only) |
| Better than grip socks? | grip socks vs grip shoes | Med–High | Grip Comparison | Pillar depth + FAQ schema |
| What size should I get? | barreletics sizing | Med | Size guide | Featured-snippet answer block |
| Free shipping? | barreletics free shipping | Low | Shipping | Exact: **$150** |
| Return policy? | barreletics returns | Med | Returns | Exact: 30-day, sellable condition — **not a trial** |
| Warranty? | grip shoes warranty | Low | Warranty | Manufacturing defects only, 90-day |

**New FAQ candidates from search demand:** slipping on reformer, socks underneath, outdoor use (secondary), washing, latex/silicone-free.

---

## 9. Structured Data Opportunities

| Already in theme (target) | Next opportunities |
|---------------------------|-------------------|
| Product, AggregateRating, FAQPage, BreadcrumbList, CollectionPage, Organization, WebSite+SearchAction, Article | HowTo (care, sizing) |
| | VideoObject when videos ship |
| | Richer Product attributes (material, audience) |
| | FAQ coverage on more commercial pages |
| | Review snippet hygiene (Judge.me sync) |

**Rules:** One BreadcrumbList canonical location. No duplicate conflicting Product schemas. Stars only from real Judge.me data.

---

## 10. AI Search Optimization (GEO / AI Overviews)

AI systems cite **clear, attributable, structured facts**.

**Barreletics advantages:** patented/injection-molded grip story, Made in USA, named testimonials, discipline-specific expertise, Doc 07 as single source of truth.

**Playbook:**
1. Lead sections with direct answer sentences  
2. Use comparison tables (socks vs Performance Skins)  
3. FAQ schema on high-intent pages  
4. Cite evidence levels; avoid absolute durability claims  
5. Keep category-creation framing without shaming sock users  
6. Unique pages beat thin spun GEO  

---

## 11. Local Authority Strategy

| Lever | Action |
|-------|--------|
| Studio partners | Earn site mentions/links; spotlight content with permission |
| Reviews | Encourage Judge.me + relevant profile reviews |
| Events | Trade-show / studio event pages only when real |
| GBP | Only if a real physical presence exists — do not fake local SEO |
| Press | Pitch innovation / Made in USA / category story |

---

## 12. Link Building Roadmap

| Tier | Targets | Approach | Timeline |
|------|---------|----------|----------|
| 1 Product/review | Fitness pubs, “best of” lists | Product seeding + honest reviews | 0–6 mo |
| 2 Content | Guest posts, studio blogs | Discipline guides, education | 3–9 mo |
| 3 Brand/authority | Patent, manufacturing, founder story | PR kit from Knowledge Base | 6–12 mo |
| 4 Community | Partner studios, instructors | Relationship-first, no PBNs | Ongoing |

**Quality bar:** Editorial, relevant, no paid link schemes. Prefer links that also drive studio-aware traffic.

---

## Authority Scorecard

| Target term | Current (qualitative) | Target | Key actions | Timeline |
|-------------|----------------------|--------|-------------|----------|
| grip shoes | Emerging | Top 3 → #1 | Pillar + links + journal | 6–12 mo |
| pilates shoes | Emerging | Top 3 | Closed/Open SEO + guide | 6–12 mo |
| barre shoes | Emerging | Top 3 | Pillar + barre guide | 6–12 mo |
| lagree shoes | Low competition opportunity | Top 3 | Discipline page + PDP FAQs | 3–9 mo |
| grip socks (disrupt) | Contested | Page-one + convert | Comparison pillar + ads/landing alignment | 3–9 mo |
| grip socks alternative | Underserved | #1 | Grip Comparison + series | 3–6 mo |
| open sole vs closed sole | Controllable | #1 | Compare page dominance | 3–6 mo |
| barreletics | Brand | Own all page-one brand SERP | Consistency + reviews | Ongoing |

---

## Operating Cadence

| Cadence | Work |
|---------|------|
| Weekly | GSC queries, index coverage, top landing CVR |
| Monthly | Rank/ movement on P1 terms, content shipped, internal link audit |
| Quarterly | Refresh pillars, retire thin pages, GEO qualification review, scorecard update |

---

## Cross-References

- SEO/GEO Foundation → `planning/12-seo-geo-standards.md`  
- Navigation/URLs → `planning/11-navigation-architecture.md`  
- Collections → `planning/09-collection-architecture.md`  
- Technical SEO → `docs/20-seo-architecture.md`  
- Copy rules → `planning/08-copy-guide.md`  
- Knowledge cascade → `planning/13-knowledge-architecture.md`  
