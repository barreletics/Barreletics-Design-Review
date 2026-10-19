# Design Completion — Remaining Pages Review

---
document: Design Completion — Navigation through Support page review
version: 1.0
status: 🔴 Review — Owner approval of Decision Packet before implementation
created: 2026-07-20
branch: design-completion-remaining-pages
scope: Navigation · Footer · Cart · About · FAQ · Wholesale · Ambassador · Studio · Support
depends_on:
  - planning/01–04, 07, 11, 12, 13 (Foundation)
  - planning/10-decision-log.md (esp. D-024, D-042, D-002)
  - planning/m4a-navigation-config.md
  - planning/m4a-content-inventory.md
  - planning/m4a-redirect-map.md
  - docs/14-cart-flow.md
  - origin/component-system → docs/component-system.md (PR parallel)
  - planning/design-completion-phase1-core-pages-review.md (parallel core-three track)
---

**Explicit constraint:** No implementation in this PR. Docs-only readiness review so these surfaces can ship when Home / Collections / PDP finalize. Does not merge parallel PRs.

**Architecture note (locked):** D-042 already consolidated Wholesale + Studio Program + Ambassador into `/pages/partners`. This review covers the three program intents as named in the assignment, then maps them to Partners as the canonical surface.

---

## 1. Executive Verdict

### **Ready to design-finalize after Decision Packet** — not architecture-blocked.

Unlike the core-three lock review, these surfaces already have **Liquid implementations** aligned to Doc 11 / M4A. There are **no competing APPROVED HTML page mockups** for About / FAQ / Partners / Cart (header/footer patterns live inside Home/PDP HTML only).

Gaps are mostly: (1) Cart full-page + drawer SSR/JS contract, (2) desktop Help vs Doc 11, (3) About founder content/assets, (4) orphan partner page templates vs D-042, (5) Support policy polish + Contact operational details.

**STOP-level only if Owner reverses D-042** (un-consolidate partner pages). Recommended choice: uphold D-042.

---

## 2. Inventory — Artifacts Reviewed

| Surface | Planning / Docs | Liquid / Theme | HTML mockups |
|---------|-----------------|----------------|--------------|
| Navigation | `planning/11`, `m4a-navigation-config`, `04` §2 | `snippets/header-nav.liquid`, `announcement-strip.liquid` | Embedded in Home/PDP HTML (non-canonical) |
| Footer | `planning/11`, `04` §14 | `snippets/footer.liquid` | Embedded in Home/PDP HTML (legacy columns) |
| Cart | `docs/14-cart-flow.md`, D-024 | `snippets/cart-drawer.liquid`, `assets/cart.js`, `templates/cart.json` | None dedicated |
| About | `m4a-content-inventory`, brand docs 01–02, `04` Founder/Manifesto | `templates/page.about.json`, `sections/page-about.liquid` | Founder article HTML exists; no About page mockup |
| FAQ | Doc 07 §1–16, `04` §26 | `page.faq.json`, `page-faq.liquid`, `faq-accordion.liquid` | `Section-27-FAQ.html` (PDP/section pattern only) |
| Wholesale | D-042, redirect map | `page-partners.liquid` `#wholesale` + orphan `page-wholesale.liquid` | None |
| Ambassador | D-042 | Partners `#ambassadors` + orphan `page-ambassador.liquid` | None |
| Studio | D-042 | Partners `#studio-partners` + orphan `page-studio-program.liquid`; `Section-26-NotesFromStudio.html` is UGC/editorial, not the program page | None for program |
| Support | Doc 11 Help/Support, Doc 07 §13–15 | `page-contact`, `page-shipping`, `page-returns`, `page-warranty` | None |

**Component system (parallel):** Header, footer, FAQ accordion, buttons documented on `origin/component-system`. Treat as implementation reference after merge — not a competing IA.

---

## 3. Per-Surface Review

### 3.1 Navigation

#### Current state
- **Doc 11 (locked):** flat primary `Grippy Shoes | Apparel | Collaborations | Journal` + utility `[Help] [Account] [Cart]`; Grippy/Apparel subnav; mobile hamburger + accordion; sticky header transparent → white + hairline; coral cart badge; Help utility = About / FAQ / Contact / Returns.
- **Liquid:** Matches primary + subnav + mobile utility list. Announcement strip rendered in `theme.liquid`. Scrolled state CSS present.
- **Gaps vs Doc 11:** Desktop Help is a single icon → `/pages/faq` only (no dropdown). Cart badge shows **count numeral** on coral (Doc 11 says coral **dot**). Logo is text `BARRELETICS` (acceptable until SVG asset lock).

#### Missing vs architecture / knowledge
| Item | Severity |
|------|----------|
| Desktop Help dropdown (About, FAQ, Contact, Returns) | **Critical** |
| Partners not in primary nav (correct — footer/Company or campaign only) | — OK |
| Apparel Tops/Bottoms may 404 until collections exist (D-043) | **Recommended** (merch gate, not redesign) |

#### Improvements (purpose-tagged)

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Add desktop Help menu matching Doc 11 + mobile utility | UX / trust | **Critical** | Desktop first; mobile already lists links |
| Keep coral badge; prefer small count over pure dot | conversion | **Recommended** | Both (amend Doc 11 note if kept) |
| Confirm Outdoor / Apparel sub-links only live when collections exist | UX | **Recommended** | Both |
| Wordmark SVG when asset ready | brand | **Optional** | Both |

#### Mobile / desktop
- Mobile drawer + accordion matches Doc 11; touch targets ≥44px in CSS.
- Desktop dropdowns for Grippy/Apparel exist; Help is the incomplete utility.

---

### 3.2 Footer

#### Current state
- **Liquid** matches M4A footer config: Shop / Support / Company / Newsletter; dark `#1c1916`; IG / TikTok / Facebook; copyright.
- **Doc 11** Support column lists “Shipping & Returns” as one link; Liquid correctly splits Shipping + Returns + Warranty (M4A + content inventory). Prefer Liquid/M4A.

#### Missing
| Item | Severity |
|------|----------|
| Partners link absent from Company column | **Recommended** |
| Legal links (Privacy / Terms) not in Doc 11 or Liquid | **Optional** (ops/compliance) |
| Legacy HTML footers still say “Studio collection / Wholesale” | Ignore — non-canonical |

#### Improvements

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Add `Partner Programs` → `/pages/partners` under Company | conversion / B2B | **Recommended** | Both |
| Keep split Support links; patch Doc 11 wording to match M4A | governance | **Recommended** | — |
| Single-column stack already in footer CSS ≤768 | UX | — OK | Mobile |

---

### 3.3 Cart

#### Current state
- **Drawer (primary):** Implemented per D-024 — shipping progress ($150), line items, qty, remove, subtotal, View Full Cart, Checkout. Documented in `docs/14-cart-flow.md`.
- **Full page:** `templates/cart.json` references `main-cart` + `recommendations` — **`sections/main-cart.liquid` is missing** from the theme (no matching section file).
- **SSR vs JS contract bug:** Server-rendered drawer uses `data-line` + `data-qty-minus` / `data-qty-plus`; `cart.js` re-render expects `data-line-key` + `data-qty-change`. First paint qty controls likely non-functional until an AJAX re-render.

#### Missing vs architecture
| Item | Severity |
|------|----------|
| `main-cart` section implementation for `/cart` | **Critical** |
| Align drawer SSR markup with `cart.js` selectors | **Critical** |
| Trust row / SAVE15 framing near checkout (CRO nice-to-have from core review) | **Optional** |
| Cross-sell / recommendations section wiring | **Recommended** |

#### Improvements

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Build `main-cart` parity with drawer (items, shipping bar, checkout) | conversion | **Critical** | Desktop (full page more used); mobile still drawer-first |
| Fix SSR attribute contract to match `cart.js` | conversion / UX | **Critical** | Both |
| Empty state → Grippy Shoes (already) | conversion | — OK | Both |
| Optional upsell band below drawer footer / on full cart | conversion | **Optional** | Both |
| Drawer 420px / 90vw — verify thumb reach on qty ± | UX | **Recommended** | Mobile |

---

### 3.4 About

#### Current state (Liquid stack)
1. Fifty-fifty hero — category creation (“The Grip Sock Era Is Over”)  
2. `page-about` — story, manifesto quote, values grid, Made in USA  
3. Fifty-fifty founder — placeholder image / thin narrative  
4. GEO accordion  
5. Newsletter  

Content inventory: **⚠️ Needs Review** (founder story & mission). Component library lists Founder Letter / Manifesto / Closing as About-capable; full Founder Letter from Home Matured is **not** on this page.

#### Missing
| Item | Severity |
|------|----------|
| Owner-approved founder copy + real portrait asset | **Critical** (content lock) |
| Closing statement / fuller manifesto module | **Optional** (brand) |
| Dedicated HTML About mockup | **Optional** — Liquid is sufficient if visual QA against v49 tokens |

#### Improvements

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Approve founder fifty-fifty copy + image before go-live | brand / trust | **Critical** | Both |
| Keep values as non-card-feeling text blocks if redesigning (avoid generic card grid polish pass) | brand | **Recommended** | Desktop |
| CTA “Shop Performance Skins” → `/collections/grippy-shoes` OK; keep Grippy Shoes in nav, Performance Skins in content | brand / IA | — OK | Both |
| Manifesto stays short one-liner (matches brand north star) | brand | **Recommended** | Both |

---

### 3.5 FAQ

#### Current state
- Strong Liquid hub: categorized accordion from Doc 07 themes (Fit, Durability, Care, Sole, Socks, Studio, Surfaces, Returns, Warranty, Shipping, Materials) + FAQPage schema + GEO + closing section.
- Accordion pattern reusable (`faq-accordion` / details).

#### Missing vs Doc 07
| Item | Severity |
|------|----------|
| Pricing & installments (Doc 07 §16) Q&A sparse/absent | **Recommended** |
| Outdoor / water-use dedicated Q (partially under surfaces) | **Optional** |
| Terminal section is newsletter “Subscribe” while copy says “Get in touch” | **Critical** (UX honesty) |
| Jump links / sticky category TOC | **Recommended** | Mobile especially |

#### Improvements

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Replace FAQ footer newsletter with Contact CTA (or dual: Contact primary + email optional) | UX / trust | **Critical** | Both |
| Add 1–2 pricing/installment FAQs from Doc 07 §16 | education / conversion | **Recommended** | Both |
| Category anchor nav at top | UX | **Recommended** | Mobile |
| Keep schema; audit answers against RETIRED_CLAIMS + Doc 07 on each content edit | governance | **Recommended** | — |

---

### 3.6 Wholesale · 3.7 Ambassador · 3.8 Studio

**Canonical surface (locked D-042):** `/pages/partners` via `page-partners.liquid` / `page.partners.json`

| Program | Anchor | Content pattern |
|---------|--------|-----------------|
| Wholesale | `#wholesale` | Eyebrow, title, body, benefits, CTA → `#partner-inquiry` |
| Studio | `#studio-partners` | Same |
| Ambassador | `#ambassadors` | Same + affiliate widget placeholder comment |

Unified form: Name, Email, Program Interest (Wholesale / Studio Partner / Ambassador), Message. **No public pricing/terms** (correct).

**Orphans still in repo:** `page-wholesale`, `page-ambassador`, `page-studio-program` (+ JSON templates). Redirect map includes 301s to `/pages/partners`. Risk: if Shopify pages still assigned old templates, users see superseded UX.

`Section-26-NotesFromStudio.html` = editorial/UGC pattern for Home/PDP — **not** the Studio Program page. Do not confuse tracks.

#### Missing
| Item | Severity |
|------|----------|
| Uphold D-042; do not rebuild three separate marketing pages | STOP if reversed |
| Retire or clearly deprecate orphan Liquid templates | **Critical** (governance) |
| Owner-approved public benefit copy (no internal pricing) | **Recommended** |
| Affiliate platform embed (placeholder only) | **Optional** |
| Studio testimonials (exist on orphan studio template, not on Partners) | **Optional** |
| Footer / Contact subject routing to Partners | **Recommended** |

#### Improvements

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Confirm live Shopify pages use `page.partners` + 301s active | conversion / SEO | **Critical** | — |
| Add Partners to footer Company | conversion | **Recommended** | Both |
| Contact subject “Wholesale Inquiry” → also link/suggest Partners page | UX | **Recommended** | Both |
| Deep-link CTAs (`/pages/partners#wholesale` etc.) from emails/ads | conversion | **Recommended** | Both |
| Stack programs single-column on mobile (already section-stacked) | UX | — OK | Mobile |

---

### 3.9 Support

**Definition for this track:** Help/Support cluster — Contact hub + Shipping + Returns + Warranty (+ FAQ as primary self-serve). There is **no** `/pages/support` handle; Doc 11 uses Support as footer column label.

#### Current state
- Contact: form + quick links to FAQ / Returns / Shipping / Warranty; subject dropdown includes Wholesale.
- Shipping / Returns / Warranty: dedicated Liquid sections sourced from Doc 07.
- Content inventory: Contact **⚠️ Needs Review** (hours/email).

#### Missing
| Item | Severity |
|------|----------|
| Published support email + hours on Contact | **Critical** (ops) |
| Help Scout / Tidio routing verified (M4B) — integration, not visual design | **Recommended** |
| Doc 11 Help “Returns & Exchanges” URL vs `/pages/returns` naming | **Optional** (label only) |
| Single combined “Shipping & Returns” page | **Not recommended** — split pages match M4A |

#### Improvements

| Rec | Purpose | Severity | Device |
|-----|---------|----------|--------|
| Lock Contact info card (email, SLA, hours) | trust | **Critical** | Both |
| Two-column → stack form above info on mobile (verify CSS) | UX | **Recommended** | Mobile |
| Add Partners quick link on Contact for B2B subjects | UX | **Recommended** | Both |
| Keep policy pages claim-synced to Doc 07 | governance | **Recommended** | — |

---

## 4. Cross-Cutting Gaps

| Gap | Surfaces | Severity |
|-----|----------|----------|
| No dedicated design-handoff HTML for these pages — Liquid is de facto mockup | All | **Recommended** (visual QA pass against v49 tokens, not new page designs) |
| Doc 11 Support column wording ≠ M4A/Liquid split links | Nav/Footer docs | **Recommended** (doc patch) |
| Core-three not locked yet — shared header/footer/cart must stay token-stable | Nav/Footer/Cart | **Critical** for sequencing (finalize chrome after or with core lock) |
| Component-system PR parallel — consume after merge, don’t fork styles | All | **Optional** |

---

## 5. Decision Packet (this track only)

Batched **recommended choices**. No separate blocker list. **STOP** only if marked.

| ID | Decision | Recommended choice | Severity if ignored |
|----|----------|--------------------|---------------------|
| R-01 | Partner programs IA | **Uphold D-042.** Canonical = `/pages/partners` with `#wholesale` / `#studio-partners` / `#ambassadors`. Keep 301s. Do not ship three separate public pages. | **STOP** if Owner reverses |
| R-02 | Orphan partner templates | **Deprecate** `page-wholesale` / `page-ambassador` / `page-studio-program` (remove from assignment or archive comment). Live pages must use `page.partners`. | Critical |
| R-03 | Desktop Help | **Add dropdown** matching Doc 11: About, FAQ, Contact, Returns & Exchanges. Keep icon affordance. | Critical |
| R-04 | Cart badge | **Keep coral badge with count** (superset of Doc 11 “dot”). Patch Doc 11 note later. | Recommended |
| R-05 | Footer Support links | **Keep Liquid/M4A split** (FAQ, Shipping, Returns, Warranty, Contact). Add Partners under Company. | Recommended |
| R-06 | Cart surfaces | **Drawer = primary**; **implement `main-cart`** for `/cart`; **fix SSR ↔ `cart.js` selectors** before polish. | Critical |
| R-07 | About composition | **Keep current Liquid stack**; Owner supplies founder copy + image; no new HTML page mockup required. | Critical (content) |
| R-08 | FAQ terminal CTA | **Contact-primary** (“Still have questions? → Contact”) not newsletter Subscribe with contact copy. | Critical |
| R-09 | Support IA | **No `/pages/support`.** Support = Contact + policy pages + FAQ. | Recommended |
| R-10 | Public partner terms | **Never show** wholesale pricing, minimums, or commission rates on Partners (already). | Critical (policy) |
| R-11 | Affiliate | **Defer** embed; keep placeholder until platform chosen. | Optional |
| R-12 | Sequencing | **Design-finalize chrome (Nav/Footer/Cart) with or immediately after core-three lock** so Home/PDP don’t drift. Content pages (About/FAQ/Partners/Support) can content-lock in parallel. | Recommended |

---

## 6. Critical Items Checklist

1. **Desktop Help dropdown** incomplete vs Doc 11.  
2. **`main-cart` section missing** while `cart.json` references it.  
3. **Cart drawer SSR/JS attribute mismatch** (`data-line` / `qty-minus` vs `data-line-key` / `qty-change`).  
4. **About founder** copy + asset Owner approval.  
5. **FAQ closing CTA** copy/action mismatch (contact vs subscribe).  
6. **D-042 enforcement:** orphan templates + live redirects/templates must not resurrect three partner pages.  
7. **Contact** support email / hours / SLA published.  
8. **Shared chrome sequencing** with core-three lock (avoid dual header/footer redesigns).

---

## 7. Recommended / Optional (summary)

**Recommended:** Footer → Partners; FAQ category TOC + pricing FAQs; Contact → Partners quick link; deep links to partner anchors; Doc 11 wording patch for Support column + cart badge; visual QA Liquid pages against v49 tokens; wire cart recommendations.

**Optional:** Legal footer links; About closing statement; studio testimonials on Partners; affiliate widget; cart upsell/SAVE15 framing; wordmark SVG; pure-dot cart badge.

---

## 8. Explicit Non-Actions

- No implementation in this branch.  
- No merge of core-three, component-system, or CRO PRs as part of this work.  
- No redesign of v49 tokens / ADR-01–07.  
- No un-consolidation of Partners unless Owner issues a new Decision Log entry (STOP).  
- No new full-page HTML mockups required before content lock (Liquid + Decision Packet sufficient).

---

## 9. Sign-off

| Role | Status |
|------|--------|
| Review author | Complete — 2026-07-20 |
| Owner | ☐ Approve Decision Packet R-01–R-12 |
| Architect | ☐ Confirm Doc 11 minor wording patches (Support column, cart badge) after approval |
| Builder | ☐ No build until Owner sign-off on Critical list |

**Track status until sign-off:** `READY FOR DECISION PACKET` (not architecture-blocked)
