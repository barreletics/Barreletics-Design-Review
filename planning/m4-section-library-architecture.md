# M4 Section Library Architecture — Inventory + Proposed Final Library

> **SUPERSEDED / LOCKED (2026-07-26):** Architecture decisions are frozen in **`planning/m4-section-library-CONTRACT.md`**. Use the CONTRACT for the final library, classifications, and build order. This file is historical inventory + proposal only.

**Date:** 2026-07-26  
**Status:** **SUPERSEDED** — see CONTRACT (ARCHITECTURE APPROVED)  
**Sources:** `shopify-build/sections/*.liquid` · `planning/m4-production-handoff.txt` · `planning/m4-shell-audit-report.md` · `planning/m4-theme-master-directive-alignment.md` · `.cursor/rules/barreletics-design-system-sections.mdc` · Home/Collection/SEO/PDP entry docs · live donor (read-only)

> **Delivery reset (2026-07-26):** Draft theme abandoned (`187143618851` retired). Deliverable = production-ready sections in **`shopify-build/`** handed to Brian via GitHub. **No agent Shopify push.** Homepage / Theme Editor assembly is Brian’s (or later) job after repo approval.

---

## 1. Reset statement

**Development is paused.** We skipped the architecture phase and started building sections before locking the library.

| Fact | Implication |
|------|-------------|
| Deliverable is the **Barreletics section library**, not the homepage | Homepage is only the first template assembled *after* approved sections exist (Brian / later — not agents on a draft theme) |
| One production-quality section per **capability** | No parallel generations of heroes, no forever-legacy duplicates |
| Workflow | Inventory → Andrew approves final library → build **one** section in repo → QA → approve → freeze in repo → next |
| Reference WIP | `home-split-hero` exists and was audited; it is **not frozen** |
| Blocked until freeze | `hero-fullbleed`, `collection-split-hero`, and every other new marketing section |
| Shopify | Draft abandoned — **no agent theme push/pull/dev** unless Andrew names a **new** theme ID in-message |

**Do not build or wire pages until Andrew checks the decision list in §6.**

---

## 2. Inventory

### 2A. `shopify-build` custom sections (library WIP)

**Count:** 44 `.liquid` files (+ 2 section groups).  
**Disposition key:** Keep as-is · Rebuild · Merge into X · Remove

| Section name (filename) | Purpose | Disposition | Notes |
|-------------------------|---------|-------------|-------|
| `announcement-strip.liquid` | Top trust / promo messages (blocks) | **Keep as-is** | Chrome; polish vs WORKING only. Replaces Impulse `announcement-bar` / `br-sale-banner`. |
| `header.liquid` | Site nav, logo, account, cart, mobile drawer | **Keep as-is** | Shopify `link_list`; presentation polish OK. Not Impulse header. |
| `footer.liquid` | Footer menus + newsletter form | **Keep as-is** | Shopify menus; may keep newsletter here *or* separate section (§6). |
| `home-split-hero.liquid` | 50/50 copy \| media page hero | **Rebuild** | Reference implementation; DS audit open; not frozen. Candidate rename → `split-hero` (§6). |
| `hero.liquid` | Older 50/50 split hero prototype | **Merge into** `home-split-hero` / final split hero | Superseded; docs call it home-split starting point. |
| `hero-alt.liquid` | A/B alt copy of `hero` (D-041) | **Remove** | Duplicate capability; do not ship. |
| `collection-hero.liquid` | Collection intro + open/closed sole cards | **Rebuild** → path to `collection-split-hero` | Sole cards may stay here as companion **or** fold into collection-split (§6). |
| `fifty-fifty.liquid` | Image/video \| copy mid-page split | **Rebuild** | Stub/port target for `br-media-text-split`; preserve schema IDs where templates depend. |
| `variant-grid.liquid` | Product/color grid + Quick Add + tabs | **Rebuild** | Stub for `br-variants`; KEEP logic non-negotiable (handoff). Biggest port. |
| `disciplines.liquid` | Discipline name strip | **Rebuild** | Align to Home WORKING; reusable. |
| `statement-band.liquid` | Large statement / typographic band | **Rebuild** | May absorb “fullbleed-statement / Commit” via surface setting (§6). |
| `value-strip.liquid` | Horizontal value / trust checklist | **Rebuild** | Collection/SEO; removed from Home spine. |
| `guarantee-band.liquid` | Guarantee / risk-reversal band | **Rebuild** | Maps to handoff `guarantee`. |
| `home-ugc.liquid` | Instagram / studio UGC grid | **Rebuild** → `ig-section` | Rename for library reuse; Juicer vs static = content decision. |
| `social-proof.liquid` | Quote-led reviews (marketing) | **Rebuild** → `reviews` | Handoff: quote-led, no aggregate on marketing pages. |
| `contact-cta.liquid` | “Still have questions?” CTA | **Keep as-is** | Thin utility; FAQ/Help. |
| `newsletter.liquid` | Standalone email capture | **Keep as-is** | Or fold into footer only (§6). |
| `collection-faq.liquid` | FAQ accordion (collection) | **Merge into** `faq` | One FAQ section; template presets differ, not separate files. |
| `geo-section.liquid` | GEO Q&A content blocks | **Merge into** `studio-trust` **or Remove** | Home WORKING retired GEO accordion → studio trust line; SEO may still need GEO (§6). |
| `pdp-buy-box.liquid` | PDP gallery + variants + ATC | **Rebuild** | Core commerce; must stay library-grade, not Impulse `main-product`. |
| `pdp-sticky-atc.liquid` | Sticky ATC bar | **Rebuild** | Companion to buy box; keep as own section. |
| `pdp-features.liquid` | PDP feature grid | **Merge into** `fifty-fifty` **or** thin `feature-grid` | Prefer reuse of content primitives over PDP-only clone (§6). |
| `pdp-reviews.liquid` | Judge.me + featured reviews on PDP | **Merge into** `reviews` | One reviews capability; settings for aggregate vs quote-led. |
| `pdp-sock-math.liquid` | Cost comparison (“One pair. Done.”) | **Rebuild** → `sock-math` | Drop `pdp-` prefix; SEO + PDP + Home. |
| `main-cart.liquid` | Cart page | **Rebuild** | Template section; keep Shopify cart APIs. |
| `recommendations.liquid` | Related products | **Keep as-is** | Thin commerce utility; polish later. |
| `recently-viewed.liquid` | Recently viewed products | **Keep as-is** | Thin commerce utility. |
| `search-results.liquid` | Search results grid | **Keep as-is** | Template section. |
| `blog-listing.liquid` | Journal index | **Rebuild** → `journal-index` | Align Journal v5. |
| `article-content.liquid` | Single article body | **Keep as-is** | Journal article template. |
| `page-about.liquid` | Monolithic About page | **Remove** after decompose | Anti-pattern: page = assembly of library sections. |
| `page-ambassador.liquid` | Monolithic Ambassador page | **Remove** after decompose | Same. |
| `page-compare.liquid` | Monolithic Compare page | **Remove** after decompose | Live `br-open-vs-closed-sole` maps to compare content + library. |
| `page-contact.liquid` | Monolithic Contact page | **Remove** after decompose | Use `page-head` / fullbleed + form module. |
| `page-faq.liquid` | Monolithic FAQ page | **Merge into** `faq` + page chrome | Capability is `faq`, not a page section. |
| `page-grip-comparison.liquid` | Monolithic grip comparison | **Remove** after decompose | SEO content → library sections. |
| `page-partners.liquid` | Monolithic partners | **Remove** after decompose | |
| `page-returns.liquid` | Monolithic returns | **Remove** after decompose | Help family → page-head + body modules. |
| `page-shipping.liquid` | Monolithic shipping | **Remove** after decompose | |
| `page-size-guide.liquid` | Monolithic size guide | **Remove** after decompose | |
| `page-studio-program.liquid` | Monolithic studio program | **Remove** after decompose | |
| `page-technology.liquid` | Monolithic technology | **Remove** after decompose | |
| `page-warranty.liquid` | Monolithic warranty | **Remove** after decompose | |
| `page-wholesale.liquid` | Monolithic wholesale | **Remove** after decompose | |

#### Section groups (not sections)

| File | Role | Disposition |
|------|------|-------------|
| `header-group.json` | Announcement + header | **Keep as-is** |
| `footer-group.json` | Footer (+ optional newsletter) | **Keep as-is** |

#### Missing from `shopify-build` (locked capabilities, not built yet)

| Proposed filename | Capability | Source of truth |
|-------------------|------------|-----------------|
| `hero-fullbleed.liquid` | Edge-to-edge hero; align start \| center | Pattern-v2 · `planning/HERO-FULLBLEED.md` · SEO v36 |
| `collection-split-hero.liquid` | Collection split; `media_fill: inset \| column` | Collection v18 |
| `visual-mosaic.liquid` | Multi-tile mosaic (mid-page, not a page hero) | Home WORKING · port `br-multi-box-hero` |
| `lifestyle-break.liquid` | Mid-page full-bleed video (~90vh) | SEO v36 Never Loses |
| `fullbleed-statement.liquid` *or* setting on `statement-band` | Commit / full-bleed typography | Home WORKING |
| `problem-section.liquid` | Problem / “Never Slip in Chair Pose” | Home WORKING |
| `studio-trust.liquid` | Studio / instructor trust band | Home WORKING (replaces GEO accordion) |
| `campaign-stage.liquid` | Campaign runway (optional) | Generalized `br-collab-hero` / Coperni |
| `faq.liquid` | Reusable FAQ blocks | FAQ v4 · Collection · SEO · PDP |
| `page-head.liquid` *or* use `hero-fullbleed` center | Content-page title hero | Help / FAQ / thin pages |
| `help-hub-grid.liquid` | Help hub card grid | Help v3 |

---

### 2B. Legacy / Impulse / `br-*` still on draft or live donor

**Scope note:** Draft `187143618851` still carries Impulse + `br-*` under `--nodelete`. Donor `/Users/andrewnehra/barreletics-theme-live-apr2026` is **read-only**. These are **not** the target library — they are capabilities to absorb, then retire.

#### Custom `br-*` (production-critical)

| Live / draft section | Lines (donor) | Maps to final library | Disposition |
|----------------------|---------------|----------------------|-------------|
| `br-variants` | 4,534 | **`variant-grid`** | Rebuild thin; KEEP Quick Add, Closed/Open/One-Offs/Outdoor tabs, size M/L, LE/Sold Out, product pickers, `use_current_product`, hide-main on one-offs, inventory, Compare + Size chart, 2-row collapse |
| `br-media-text-split` | 1,656 | **`fifty-fifty`** | Rebuild thin; image\|video, reverse, eyebrow, H2, body, CTA; preserve schema IDs |
| `br-multi-box-hero` | 2,597 | **`visual-mosaic`** | Rebuild Home WORKING mosaic only; drop BF grid modes unless proven used |
| `br-collab-hero` | — | **`campaign-stage`** (optional) | HOLD until §6 yes |
| `br-coperni-*` | — | PDP campaign templates / campaign-stage | HOLD |
| `br-hide-kids-size-when-oos` | — | Snippet / PDP behavior (not a marketing section) | Keep logic; snippetize |
| `br-open-vs-closed-sole` | — | Compare page composition | HOLD → compose from library |
| `br-product-highlight` | — | — | Remove after mock sections cover |
| `br-sale-banner` | — | `announcement-strip` | Remove after chrome confirmed |
| `br-seo`, `br-global-styles` | — | — | HOLD → remove after audit |

#### Impulse / SS sprawl (retire via template rewrite — do not “consolidate” into mega-sections)

| Family | Final home (if any) | Disposition |
|--------|---------------------|-------------|
| `ss-hero-14/15/27`, `hero-animated`, `slideshow`, `background-image-text` | `hero-fullbleed` / `split-hero` / `statement-band` | **Remove** after page rewires |
| `text-and-image` | `fifty-fifty` | **Remove** gradually |
| `hero-video` | `lifestyle-break` (pattern only) | HOLD then remove |
| `main-product` / `main-collection` / `main-page*` | `pdp-buy-box`, collection templates, page compositions | Replace when wiring |
| `judgeme_carousel_section` | `reviews` | Keep until reviews strategy ships |
| `apps` | App block host | **Keep** |
| Shogun / PageFly / Weaverse / POWR / LayoutHub | — | HOLD → remove after URL audit |

---

### 2C. Legacy capabilities → final library names (required)

| Live capability | Final section name | Role |
|-----------------|-------------------|------|
| `br-variants` | `variant-grid` | Commerce |
| `br-media-text-split` / Impulse text-and-image | `fifty-fifty` | Content |
| `br-multi-box-hero` | `visual-mosaic` | Content |
| `br-collab-hero` (optional) | `campaign-stage` | Content / campaign |
| Impulse heroes / SS heroes | `hero-fullbleed` + `split-hero` + `collection-split-hero` | Heroes (three max) |

---

## 3. Proposed FINAL section library

**Principle:** one section per capability. Pages assemble approved sections; no monolithic `page-*` sections in the long-term library.

### Chrome

| Filename | Purpose | Source of truth |
|----------|---------|-----------------|
| `announcement-strip` | Promo / trust strip | Keep · Home WORKING |
| `header` | Global navigation | Keep · Shopify menus |
| `footer` | Global footer (+ optional newsletter) | Keep · Shopify menus |

### Heroes (three thin compositions — locked unless §6 changes)

| Filename | Purpose | Source of truth |
|----------|---------|-----------------|
| `split-hero` *(today: `home-split-hero`)* | 50/50 copy \| media first viewport | Mock · rebuild current WIP · **kill** `hero` + `hero-alt` |
| `hero-fullbleed` | Edge-to-edge media; `alignment: start \| center` | Pattern-v2 · SEO · Help |
| `collection-split-hero` | Collection split; `media_fill: inset \| column` | Collection v18 · evolve/replace `collection-hero` |

**Hero challenge (duplicates → single winners):**

| Contender | Verdict |
|-----------|---------|
| `home-split-hero` | **Winner** for split composition (rename to `split-hero` recommended) |
| `hero.liquid` | **Lose** — merge/delete |
| `hero-alt.liquid` | **Lose** — delete |
| `collection-hero.liquid` | **Not** a fourth hero OS — evolve into `collection-split-hero` (± sole-cards companion) |
| Impulse / SS heroes | **Lose** — never port; retire after rewrite |

Do **not** merge full-bleed into split via layout modes (recreates `br-*` Theme Editor hell).

### Commerce

| Filename | Purpose | Source of truth |
|----------|---------|-----------------|
| `variant-grid` | Shop grid / related colors / Quick Add | Port KEEP logic from `br-variants` |
| `pdp-buy-box` | Product purchase UI | Mock PDP v16 · rebuild |
| `pdp-sticky-atc` | Sticky ATC | Mock PDP v16 · rebuild |
| `main-cart` | Cart page | Rebuild · Shopify native |
| `recommendations` | Related products | Keep / polish |
| `recently-viewed` | Recently viewed | Keep / polish |
| `search-results` | Search results | Keep / polish |

### Content

| Filename | Purpose | Source of truth |
|----------|---------|-----------------|
| `fifty-fifty` | Media \| text split | Port `br-media-text-split` · mocks |
| `visual-mosaic` | Multi-tile visual mosaic | Port `br-multi-box-hero` · Home WORKING |
| `disciplines` | Discipline strip | Mock · rebuild |
| `statement-band` | Statement typography band | Mock · rebuild |
| `fullbleed-statement` *or band variant* | Full-bleed commit statement | Home WORKING · §6 |
| `lifestyle-break` | Mid-page video full-bleed | SEO v36 |
| `value-strip` | Value checklist strip | Collection / SEO mocks |
| `sock-math` | Cost / “One pair” math | PDP + SEO + Home · rename from `pdp-sock-math` |
| `problem-section` | Problem / chair-pose beat | Home WORKING |
| `faq` | Accordion FAQ (blocks) | FAQ v4 · merge collection/page FAQs |
| `newsletter` | Email capture (if not footer-only) | Keep |
| `contact-cta` | Support CTA | Keep |
| `page-head` *or* `hero-fullbleed` center | Content page title | Help / FAQ / thin pages · §6 |
| `help-hub-grid` | Help hub links | Help v3 |
| `journal-index` | Blog listing | Journal v5 · rename `blog-listing` |
| `article-content` | Article body | Keep |
| `campaign-stage` *(optional)* | Campaign runway | `br-collab-hero` · §6 |

### Proof

| Filename | Purpose | Source of truth |
|----------|---------|-----------------|
| `reviews` | Quote-led reviews (settings for PDP aggregate) | Merge `social-proof` + `pdp-reviews` |
| `ig-section` | Studio / IG grid | Rename `home-ugc` · Home WORKING |
| `guarantee` | Guarantee band | Rename `guarantee-band` |
| `studio-trust` | Instructor/studio trust | Home WORKING · replaces GEO accordion default |

### Utility / template

| Filename | Purpose | Source of truth |
|----------|---------|-----------------|
| `apps` *(on draft)* | App blocks host | Keep on draft; not a design-system section |
| *(snippets, not sections)* | `product-card`, `button`, `cart-drawer`, trust, sticky helpers | Handoff |

**Approximate final count:** ~3 chrome · ~3 heroes · ~7 commerce · ~16–18 content · ~4 proof · utilities ≈ **~28–32** Shopify sections (matches handoff “~22–28 for full OS” + thin support). Monolithic `page-*` **out** of the final library.

---

## 4. Explicit non-goals / remove list

**Dies after migration (do not rebuild, do not keep forever):**

- Impulse / SS: `ss-hero-*`, `hero-animated`, `slideshow`, `background-image-text`, sprawl `text-and-image`
- Duplicate prototypes: `hero.liquid`, `hero-alt.liquid`
- Overbuilt live: raw `br-variants` / `br-media-text-split` / `br-multi-box-hero` Liquid (logic kept, files retired)
- `br-sale-banner` (→ announcement-strip)
- Monolithic `page-*.liquid` once pages are compositions
- Parallel FAQ files (`collection-faq`, `page-faq`) once `faq` exists
- Homepage-only coupling (hardcoded anchors, forced H1, “Home …” naming that blocks reuse)
- Building multiple new sections in one pass; assembling homepage before library freeze
- Publishing or pushing to any theme other than draft `187143618851`

---

## 5. Build order after approval

One section at a time → QA → Andrew approve → **freeze** → next.

| # | Section | Why this order |
|---|---------|----------------|
| 0 | **Architecture approval** (this doc) | Gate |
| 1 | **`split-hero`** (freeze target; today’s `home-split-hero`) | Reference section; prove library standards (P0 audit gaps) before anything else |
| 2 | `hero-fullbleed` | Second hero composition; SEO/Help depend on it |
| 3 | `collection-split-hero` | Third hero; Collection v18; resolves `collection-hero` / sole-cards decision |
| 4 | `fifty-fifty` | First surgical port; high reuse |
| 5 | `visual-mosaic` | Second port; Home mosaic |
| 6 | `variant-grid` | Third port; largest KEEP-logic job |
| 7 | `disciplines` → `statement-band` → `value-strip` → `sock-math` → `problem-section` | Marketing spine from mocks |
| 8 | `reviews` → `ig-section` → `guarantee` → `studio-trust` | Proof stack |
| 9 | `lifestyle-break` · `faq` · `newsletter`/`contact-cta` · `page-head`/`help-hub-grid` | SEO + Help/FAQ |
| 10 | `pdp-buy-box` → `pdp-sticky-atc` | PDP commerce |
| 11 | `campaign-stage` *(only if §6 yes)* | Optional |
| 12 | Wire templates: Home → Collection → SEO → PDP → Help/FAQ/Journal | Assembly **after** sections frozen |
| 13 | Retire Impulse/`br-*` from draft; Lighthouse / a11y gate | Cleanup |

**Recommendation:** Keep `home-split-hero` as the **first freeze target**, but rename display name (and ideally filename) to **`split-hero`** at freeze so the library is not homepage-branded. Do not start #2 until #1 is frozen.

---

## 6. Decision checklist for Andrew

Check yes/no (or write the choice). **No builds until these are answered.**

### Heroes & naming

- [ ] **H1.** Rename `home-split-hero` → generic **`split-hero`** (filename + Theme Editor name)?
- [ ] **H2.** Confirm **three heroes max**: `split-hero` · `hero-fullbleed` · `collection-split-hero` (no mega-hero)?
- [ ] **H3.** Delete `hero.liquid` + `hero-alt.liquid` after split-hero freeze (no merge of settings beyond copy defaults)?
- [ ] **H4.** Collection sole cards: **(a)** settings/blocks on `collection-split-hero`, or **(b)** thin companion section kept separate?

### Content capabilities

- [ ] **C1.** `fullbleed-statement` as **own section**, or **variant/setting** on `statement-band`?
- [ ] **C2.** Ship **`campaign-stage`** (Coperni generalized) in v1 library, or defer?
- [ ] **C3.** GEO: retire accordion into **`studio-trust`** only, or keep a thin **`geo-section`** for SEO pages?
- [ ] **C4.** Newsletter: **footer-only**, **standalone section**, or both?
- [ ] **C5.** Content pages: **`page-head`** section, or reuse **`hero-fullbleed` (center)** only?
- [ ] **C6.** Monolithic `page-*` sections: approve **remove-after-decompose** (compose from library), not rebuild as page blobs?

### Commerce / proof

- [ ] **P1.** One **`reviews`** section for marketing + PDP (settings toggle aggregate), vs keep PDP reviews separate?
- [ ] **P2.** `pdp-features`: merge into **`fifty-fifty`**, or keep a thin **`feature-grid`**?
- [ ] **P3.** Confirm `variant-grid` KEEP logic list from handoff is still the non-negotiable contract?

### Process

- [ ] **X1.** Approve this inventory + final library list as the architecture freeze gate?
- [ ] **X2.** Approve build order §5 (split-hero first freeze, then fullbleed, then collection-split)?
- [ ] **X3.** Explicit: **no section development / no Shopify push** until X1 + X2 are yes?

---

## Approval stamp

| Field | Value |
|-------|-------|
| Approved by | |
| Date | |
| Notes / deltas | |

Until stamped: **ARCHITECTURE PAUSE** — see `planning/m4-build-progress.md`.
