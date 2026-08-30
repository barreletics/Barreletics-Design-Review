# M4 Section Freeze Registry — APPROVED / SETTLED

> ## ⛔ ANTI-REVERT (HARD)
> **Agents must not silently restore older compositions.**  
> **Law:** `.cursor/rules/anti-revert-fail-closed.mdc` (+ `.cursor/rules/section-freeze-no-drift.mdc`)  
> **If this freeze file conflicts with Andrew’s CURRENT message → CURRENT MESSAGE WINS.**  
> Update this registry to match his ask — do **not** `git checkout` / restore freeze over his ask.  
> Before editing footer, `product.json`, `index.json`, or any file listed below: (a) read this file, (b) state what will change, (c) never restore prior composition unless Andrew says **“restore X”**.

**Status:** ACTIVE  
**Authority:** Companion to `planning/m4-section-library-CONTRACT.md` §8  
**Guardrails:** `.cursor/rules/anti-revert-fail-closed.mdc` · `.cursor/rules/section-freeze-no-drift.mdc`  
**Rule:** Frozen sections must not drift, revert, or be replaced without **explicit Andrew approval in the CURRENT message**.

> **Page ↔ template registry (2026-08-09 forward):** Canonical handle → repo template → hub Locked mock → Admin suffix → QA preview path lives in **`planning/page-template-registry.md`**. Page work: auto-invoke **`barreletics-page-qa`**. Multi-surface edits: `.cursor/rules/os-sync-on-global-change.mdc` (update this freeze + the registry forward).

> **Studio FAQ bank 2026-08-26:** Theme settings → **Studio FAQ** is the one list for Closed / Open / One-Offs / Coperni (`use_studio_bank`). Outdoor + Shop All + `/pages/faq` stay local. No 18+ months. Open vs Closed = P-003. Extra One-Off blocks stay on those two PDPs only.

> **Sock kit LOCKED 2026-08-27 (J):** Theme settings → **Sock kit**. Label `Complete the kit` · one link `Optional sock kit →` → `/collections/hot-kits` · small type `A sock made for Performance Skins with grip around the toes.` + `Does your studio require a sock? Need help with sweat, warmth, or comfort?` Buy-box checkbox only shows/hides. Layout / fold untouched. Nav: **Socks** under Apparel on `m4-menu` (not live Main menu). Collection page copy reframed — no heat sell. Handle stays `hot-kits`. Still 404 until Andrew publishes the collection to Online Store.

---

## What “APPROVED / FROZEN” means

1. Andrew visually approved the composition (Shopify draft preview and/or named letter).
2. Structure is locked in `shopify-build/` (repo = master).
3. Agents may fix bugs / TE copy / schema labels **only if** they do not change layout structure, visual system, or swap to an alternate design.
4. Agents must **not**:
   - `git checkout` older section files without current-message approval
   - Replace with live / Impulse / dark Phase 1 / gallery pick without a letter
   - Invent alternate footers, heroes, or chrome “improvements”
   - Silently restore removed elements (brand blurb, value checklist / ✓ list, 10% offer)

---

## Owner visual sign-off — 2026-08-11 (M4 `187144929571`)

**SIGNED — do not thrash without CURRENT MESSAGE letter:**

| Item | Sign-off |
|---|---|
| **Header nav #2** | 13px / 500 / sentence case · gap 26 · actions 13px · logo TE 45 |
| **Closed badge default rust** | TE black/charcoal/blue honored |
| **Buy-box fold / ATC** | Above fold · chart-only Size · no qty · no Coming soon S |
| **v20d fold chrome** | Hub judge-fold authority |
| **TRANSFORM contrast** | Title readable (stacking fix) |
| **Description accordion** | TE `description_accordion_body` (v19 Closed seeded). **NEVER** Admin `product.description`. Fallback = `short_description` only |
| **Value-strip + features** | 4-up: USA · Free shipping over $150 · **30-day returns** · **90-day warranty** (must say the words — not “30-day · 90-day”). No latex/silicone on the strip (Andrew 2026-08-15 — that lives in Description accordion + FAQ). Accordion label = **Returns & warranty**. |

**NOT signed yet:** Open / one-off · dual nav

---

## Closed Sole PDP — SIGNED 2026-08-16

**Andrew:** “Great I think we are good” · “lock in the page” · “lock it.”  
**No extra wow.** Do not add a third full-bleed. Do not enlarge existing bleeds.

| Item | Locked |
|---|---|
| Handle | `/products/best-reformer-pilates-legree-workout-shoes` |
| Template | `shopify-build/templates/product.json` |
| QA | `187144929571` · [Closed preview](https://barreletics.com/products/best-reformer-pilates-legree-workout-shoes?preview_theme_id=187144929571) |
| Spine | buy-box → value-strip → features → disciplines → sock-era → variant-grid → Kimberly quote → TRANSFORM → sock-math → **wow** → commit → reviews → numbers → guarantee → juicer → FAQ → sticky |
| Wow | `fullbleed-lifestyle` · `show_text: false` · video · **80vh / 60vh** · after Sock Math / before Commit. Swap media in this slot only — never add another. |
| TRANSFORM | `fullbleed-statement` · type-on-media · Multi_Image · 80 / 60 |
| Sock Math | Editorial L · copy from `docs/pdp-sock-math-directions.html` (v8) · photo Juicer **5986441** (Q outdoor) · 480 frame · cover |
| Kimberly | Juicer **5986429** · `focal_y: 85` · quote + stars. **Never** barefoot reformer (`src-3`). |
| Videos | Sock-era / Commit / Numbers = `image_position: center` |
| Badge | Closed Sole · rust |
| 50/50 TE | Global schema order LOCKED (every 50/50): **1 Photo/video → 2 Focus+height → 3 Heading/body/CTA → 4 Trust strip → 5 Quote/stats → 6 Layout extras → 7 Insets** |
| Trust strip | SIGNED 2026-08-16 · off by default · *Trusted by 1,000+ Instructors* or stars only |

Do **not** thrash `product.json` spine or `fifty-fifty.liquid` TE order without a letter. Open / Outdoor not included.

**Forward 2026-08-21 — Closed reviews text only.** Andrew: Outdoor no-photo looks better → Closed match. `show_photo_cards: false` · `show_live_text: false` · 6 text cards stay · More stories → `/pages/reviews`. Photo blocks kept in JSON, hidden. Buy-box / spine untouched.

**Forward 2026-08-21 — all PDPs + Shop All + Apparel + Home match.** Andrew: reviews page is great → same treatment everywhere else. Flags only: `show_photo_cards: false` · `show_live_text: false` · text cards stay · More stories → `/pages/reviews`. `/pages/reviews` keeps the full Judge.me list. Buy-box / spine / TE photos untouched.

**SIGNED 2026-08-21 — review cards.** Andrew: “the judge me cards are great… much better.” Text-card row on Shop All / PDPs / Home / Apparel is **LOCKED**. Photos + full list stay on `/pages/reviews` only. Do not put photo cards or live JM back on those pages without a letter.

**Forward 2026-08-21 — Coperni product first.** Andrew: product, then other images, then full runway. Spine: buy-box → value-strip → coperni-crosslink → coperni-pdp-story → rest. Firefox mute/autoplay **earmarked** — not this turn.

**Forward 2026-08-21 — Coperni title = Display.** Banner title was custom 28–50 / Georgia italic — off Type OS. Now `--type-h2-display-*` (same as 50/50s). Story quote stays quote-size. Buy-box lede untouched.

**Forward 2026-08-21 — `/pages/reviews` full Judge.me list.** Andrew: all reviews + scroll / load more. Mount official `judgeme_all_reviews` (`all_reviews_header` + `all_reviews_N`) + `judgeme_core` in theme. Compact PDP reviews unchanged. Photos stay on this page. **No Product / Shop tabs** (hide `.jdgm-subtab`).

### LOCKED 2026-08-21 — reviews + Coperni (Andrew: commit and lock every page)

| Page | Locked |
|---|---|
| `/pages/reviews` | Full Judge.me list + Load more · no Product/Shop tabs · photos live here |
| Shop All · Apparel · Home | Text cards + More stories → `/pages/reviews` · no photo cards · no live JM |
| Closed · Open · Outdoor | Same text-card reviews (Closed/Outdoor already signed/locked as pages) |
| One-off Closed · One-off Open | Same text-card reviews |
| Coperni | **Product first** → images → runway · banner title = Type OS Display |

**Do not** put photo cards or live JM back on PDPs / Shop All / Home / Apparel.  
**Earmarked, not locked:** Firefox mute / autoplay.

### Forward 2026-08-30 — review counts hidden + shared photo set + Write a Review

> **Andrew CURRENT MESSAGE:** Hide review COUNTS sitewide until thousands (stars stay; do not invent counts). First 3 review cards = the photo reviews from `/pages/reviews`. One reviews page for Open and Closed. Judge.me Write a Review on `/pages/reviews` only.

| Surface | Forward |
|---|---|
| Counts | Stars stay. Hide `N reviews`, Judge.me badge counts, histogram, “Based on X reviews”. `Trusted by 1,000+ Instructors` stays. |
| Photo set | Same 3 Judge.me photo reviews on Home + `/pages/reviews`: Leslie S. (Katy), B P. (Philadelphia), Tracie. Verbatim quotes + Judge.me images. |
| Home | Hybrid stays (3 photo + 6 text). Photo cards ON so the first 3 cards match the reviews-page photo set. 6 text cards unchanged. |
| `/pages/reviews` | Shared page (page.reviews + page.judgeme_all_reviews). Full Judge.me list + native `jdgm-write-rev-link` Write a Review. No sole-specific review pages. |
| PDPs / Shop All / Apparel | Text cards stay; photo cards remain off. No Write a Review. |


---

## Help family — LOCKED 2026-08-15 (Andrew: "lock help")

**Owner lock.** Help menu is done. Do not reopen without a letter.

| Surface | Handle | Status |
|---|---|---|
| Help hub | `/pages/help` | LOCKED |
| FAQ | `/pages/faq` | LOCKED |
| Returns | `/pages/returns` | LOCKED 2026-08-14 |
| Size guide | `/pages/performance-skins-size-chart` | SIGNED 2026-08-12 |
| Contact | `/pages/contact-us-form` | LOCKED — do not thrash |
| Returns portal | `/pages/returns-portal` | LOCKED |

Header Help fallback = `/pages/help`. Do **not** restore `/pages/faq`.

---

## Closed Sole copy — forward 2026-08-15 (content micro-check)

Layout already approved ("closed sole looks good"). Copy-only in `product.json`. **No** buy-box layout / CSS / spine change.

- **Banned 18+ months** stripped. **Grip never degrades stays** (Andrew 2026-08-15: the shoe may wear; the grip does not). Longevity anecdotes = 1,000 classes · year four.
- **Size buttons** (shared `pdp-buy-box.liquid` labels only — no layout/CSS): M **Women 5.5–7.5 · Kids 2–5** · L **Women 7.5–11 · Men to 10.5**. Matches CA-05. Do not restore Women 8–10 / Men 8.5–11.
- Sock math annual cost = **$144–$336** / 8–12 pairs (was $112–144 / 6–8).
- Size FAQ = CA-05/CA-06 (M 5.5–7.5 + kids 2–5 · L 7.5–11 · width at 7.5). No "conforms" · no "between sizes, go larger."
- Shipping accordion + FAQ = process **24–48 hours**, typically ship next business day (was "ship within 1–2 business days").
- Admin SEO on the live product still says **"cushioned"** — that is Shopify Admin, not this template. Fix in Admin when Andrew wants it.
- **Trust split forward 2026-08-15 (Andrew walk-back):** strip back to USA · Free shipping over $150 · **30-day returns** · **90-day warranty**. Do not put latex/silicone on the strip or the guarantee band. Skin-safe / no latex / no silicone already lives in Description accordion and FAQ “Are they latex-free…”. Accordion title stays **Returns & warranty** (the fine print). Guarantee band titles back to **30-Day Returns · 90-Day Warranty · Built to Last**. No “Defects covered.” No “Try on at home.”

---

## Returns — LOCKED 2026-08-14 (Andrew: "returns is locked")

**Owner lock** on M4 `187144929571` → `/pages/returns` (`page.shipping-retruns.json` + alias `page.returns.json`). Do not thrash without a letter.

**Composition (forward):** head → Start a return (one portal button) → policy cards → Need a hand? (Start a return + Contact + 72-hour refund note). **No** numbered how-to band. **No** studio-trial line. **No** 24-hour defect clock. Jump row = Start a return / Returns / Warranty / Shipping. Anchors use `scroll-margin-top` 130px so the sticky header does not cover card headings.

**Card interiors (signed same day, "looks great"):** rich-text `p` / `ul` / `li` restored on `.page-returns-card > .type-body` only. Do **not** widen to `.page-returns-card ul` — that breaks warranty Covered / Not covered.

**Copy law on this page:** "Try them on for size — indoors only." International ends with a size-chart link, not "Size carefully before ordering."

### Antimicrobial purge — 2026-08-14 (same lock turn)

P-015 / CA-02. Live runtime cleaned: `page.technology.json` · `page.grip-comparison.json` · `collection.apparel.json`. Say wipe-clean / non-porous. Never restore "antimicrobial" or "resists bacterial growth." Frozen backups and evidence snapshots left alone.

---

## Returns card interiors — SIGNED 2026-08-14 ("looks great") — subsumed by the lock above

**Owner sign-off** on M4 `187144929571` → `/pages/returns`. Returns v3 composition unchanged — this was a missing-CSS repair inside the existing policy cards, not a redesign.

- **Root cause:** `barreletics-base.css` resets all margins to 0 and sets `ul, ol { list-style: none; }`. `page-returns.liquid` never restored either for its rich-text card bodies, so multi-paragraph copy and the labeled lists rendered as one unbroken block. Same repair pattern already in `article-content.liquid`.
- **Shipped:** `.page-returns-card > .type-body` gets `p` margin `--space-4` · `ul/ol` `list-style: revert` + `padding-left: --space-6` · `li` margin `--space-2` · last child margin 0.
- **Scoped on purpose:** the `> .type-body` child selector keeps `.page-returns-coverage__col` lists on their own bordered-row / ✓✕ treatment. Do **not** widen to `.page-returns-card ul` — that breaks the warranty Covered / Not covered columns.
- **Also signed 2026-08-14:** `.page-returns-cta__inner .page-returns-cta__alt` top margin `--space-8`. The `__inner .type-body` rule was outranking the unscoped `__alt` rule and zeroing it, pinning "Looking for product FAQ?" against the Contact button.
- **Applies to any section with rich-text output:** the global reset means every new rich-text wrapper needs `p` / `ul` / `li` rules or it ships as a text blob. Check this before calling a card section done.

---

## Size guide — SIGNED 2026-08-12 ("the size page looks great")

**Owner sign-off** on M4 `187144929571` → `/pages/performance-skins-size-chart`.

**FORWARD UPDATE — same day, second Andrew letter 2026-08-12.** Large starts at **7.5, not 8**, and the chart publishes **four** columns. The 8–11 version below was signed earlier that afternoon and is superseded. Do **not** restore it.

**Canonical chart (matches the live site):**

| Size | Women's (US) | Men's (US) | Kids' (US) |
|---|---|---|---|
| **M** | 5.5–7.5 | — | **2–5** |
| **L** | **7.5–11** | up to 10.5 | — |

Kids' 2–5 has always been on the live site; the M4 build had dropped it. It stays.

**Width decides at the 7.5 overlap** — 7.5 sits in both rows on purpose:

| Case | Take |
|---|---|
| Below 7 | M |
| Wide foot at 7 or 7.5 | **L** |
| Narrow foot at 7.5 or 8 | **M** |
| 8.5 and above | **L always** — length governs, regardless of width |

No small size.

**Table columns are now Size · Women's · Men's · Kids'.** `foot_length` and `best_for` are removed from the schema, replaced by `mens_size` and `kids_size` with the rule in TE help text.

⚠️ **Push order matters on this section.** Shopify validates JSON template block settings against the schema already on the theme, so pushing `page-size-guide.liquid` and the three templates in one command silently strips `mens_size` / `kids_size`. Push the section first, then the templates — or push twice and verify the Men's and Kids' cells aren't showing the dash fallback.

**RETIRED — never reintroduce:** M 5–8 / L 8.5–11 · **L 8–11** (shipped briefly 2026-08-12 afternoon) · "Between Sizes? Size Up." · "conforms slightly over the first few wears" · "conforms to your foot shape over the first few sessions" · snug-colors note telling people to size up · the **Foot Length** column (8.5"–9.5" / 9.5"–10.5" — repo-only, never on the live site, no source; Andrew: "we only give shoe size").

**Also locked here:** Black credited alongside Light Grey as most forgiving · GEO block removed from this page (duplicated the fit tips above it).

**Files:** `templates/page.size-chart.json` + aliases `page.performance-skins-size-chart.json`, `page.size-guide.json` (push all three — Admin renders the alias) · `sections/page-size-guide.liquid` (fallback rows + schema defaults corrected so a cleared block list can't resurrect old numbers).

**Single source for all of this:** `docs/11-CANONICAL-ANSWERS.md` → CA-05 through CA-09. Change it there first, then propagate.

**Still carrying wrong sizing (await letter):** `templates/product.json` PDP accordion — publishes M W 5–7.5 / Men 6–8, L W 8–10 / Men 8.5–11 and "go larger" if between sizes.

**FAQ page:** rebuilt from the canonical source the same day and carries the same rule — **not yet signed.**

---

## Frozen registry

| ID | Surface | Status | Fingerprint (lineage) | Locked composition | Files |
|----|---------|--------|------------------------|--------------------|-------|
| **Footer** | Sitewide footer (all pages via `footer-group`) | **SIGNED 2026-08-12** (Join the list A) · LOCKED Jul 31 2026 | WORKING layout + Join the list · Light/Dark TE | Trusted by (toggle) · Join the list **split** (headline left, form right, **checks OFF**) · columns · Light/Dark per band · size TE · SEO Learn link · **NO brand blurb** · **NO 10%** · **NO cadence / never-spam / nothing-else** · Andrew approved 2026-08-12 | `sections/footer.liquid`, `footer-group.json`, `assets/chrome.css` · `specs/frozen/footer.md` |
| **PDP** | Product templates + buy-box | **Closed PDP SIGNED 2026-08-16** · **LOCKED Aug 1 2026** · **proportions LOCKED 2026-08-08 night** · **Closed badge rust LOCKED 2026-08-11** · v16 prior · Closed=`product.json` · Open=`product.open-sole.json` · Outdoor=`product.outdoor.json` | Mock **`Definitive-v19.html`** + current Closed `product.json` (QA **`187144929571`**) | **Closed SIGNED 2026-08-16** (see block above). **No extra wow.** Wow = `fullbleed-lifestyle` 80/60 video. **Proportions (PDP only):** fifty-fifty **560**/pad **80**/mobile **320** · fullbleed **80vh/60vh** · gallery 1:1 · thumbs 72 · **Closed + Open + Outdoor badges = rust** `#c45c3f` · city FAQ last · `pdp-reviews`. Home fifty-fifty stays **640**. v16 @ `691f03b` prior (NEVER overwrite). | `docs/…Definitive-v19.html` · `templates/product.json` · `product.open-sole.json` · `product.outdoor.json` · `pdp-buy-box.liquid` · `specs/frozen/pdp.md` |
| **PDP purchase stack** | Buy-box commercial stack (`#buy`) | **LOCKED Aug 1 2026** · **Description accordion SIGNED 2026-08-11** · badge default rust + TE honor | Option A stack + kit Option A · on spine | price → muted `or 4 × $18.50` → color/size → qty+CTA → **empty under ATC** → quiet Complete the kit → accordion · **Description accordion = TE `description_accordion_body` (v19 Closed seeded) · NEVER Admin `product.description` · fallback `short_description` only** · sole badge TE default rust · `show_trust_row: false` | visual: `Definitive-v19.html` `#buy` · live: `product.json` `pdp-buy-box` · `specs/frozen/pdp.md` |
| **PDP trust split** | Value strip + accordion policy | **LOCKED Aug 1 2026** (4-up strip refinement) · **band height forward 2026-08-10** | Scan strip · accordion detail · no under-ATC repeat | **Value strip (4-up, no links by default):** Made in USA · **Free shipping over $150** · 30-day returns · 90-day warranty · **Band height TE:** `padding_y` default **28** / mobile **24** (was 16/`--gap-a`) — type stays 12px · **Under ATC:** nothing · **Accordion:** Shipping + 30/90 · **no page `studio-trust`** · (Non-toxic / No latex / No silicone **removed** from strip) | `product.json` `value-strip` · `sections/value-strip.liquid` · `Definitive-v19.html` (mock prior) · `specs/frozen/pdp.md` |
| **PDP variants 4×** | Shop-all / variants cards | **LOCKED Jul 31 2026** | Option A under Quick Add · on draft `variant-grid` | Name → meta pill → $74 → Quick Add → quiet `or 4 × $18.50` · **no dual pills** · **LE / Sold Out image badges REQUIRED** · Draft Home chrome | `product.json` `variant-grid` · `Definitive-v19.html` `#variants` · `specs/frozen/pdp.md` |
| **Type OS** | Typography system | **SETTLED** | See `planning/m4-type-hierarchy.md` | Family/size/weight/tracking; no per-section `font_picker` | Type tokens + TE policy |
| **Home WORKING** | Homepage layout authority | **WORKING** (layout authority — not a free redesign surface) | Home WORKING mocks / draft match commits | Agents must not invent alternate homepage composition; match WORKING unless Andrew approves change in-message. **Exception locked 2026-08-01:** `proof-numbers` after social-proof (see row below). | `templates/index.json` + home sections |
| **Proof numbers** | Reusable stats band (Home; optional elsewhere) | **LOCKED Aug 1 2026** · White tone | Draft QA `187144929571` · Andrew visual approve | White default · cream/charcoal TE · 3-up: 1,000's instructors · 1,000+ classes (attribution TBD) · USA · Show toggle · after reviews / before One pair | `sections/proof-numbers.liquid` · `index.json` · `specs/frozen/proof-numbers.md` |
| **Header nav type** | Sitewide header chrome (`header-group`) | **LOCKED 2026-08-11** · nav font **#2** (supersedes Aug 8 18px) · **Help fallback `/pages/help` 2026-08-14** | v20d fold chrome + M4 `187144929571` | Nav **13px / 500 / 0.01em / sentence case** (no `text-transform`) · gap **26px** · utility actions **Help ▾ · Account · Cart** **13px / 500** · logo height TE (currently 45 — do not thrash to 42 without letter) · Help fallback **`/pages/help`** (hub exists — do **not** restore `/pages/faq`) | `assets/design-tokens.css` (`--type-nav-*`), `assets/chrome.css`, `sections/header.liquid`, `sections/header-group.json` · `docs/pdp-fold-v20d-chrome.html` |
| **PDP fold chrome** | Fold-judgment mock + sitewide nav sync | **LOCKED 2026-08-11** · nav font **#2** | Hub `docs/index.html` · `pdp-fold-v20d-chrome.html` | Logo **42px** on mock · nav **13px / 500 / sentence case** · sitewide header now matches nav #2 (logo TE 45 left alone). **Judge ATC above fold here.** Never thrash without chrome letter. | `docs/pdp-fold-v20d-chrome.html` · `docs/Barreletics PDP - Definitive-v20d-fold-with-chrome.html` · `.cursor/rules/pdp-fold-preview-from-m4.mdc` · hub Shop card |
| **Juicer / Instagram** | Reusable library section (any page) | **LOCKED Jul 31 2026** · on PDP draft | v19 Juicer · PDP `product.json` includes `home-juicer` | Eyebrow / @barreletics / body · live Juicer (`barreletics`) · **max_height 0** · See more · Follow · TE add/omit · **on PDP after guarantee, before FAQ** | `sections/home-juicer.liquid` · `product.json` · `specs/frozen/juicer.md` · `Definitive-v19.html` `#instagram` |
| **Brand / About** | `/pages/our-story` · `page.our-story.json` | **LOCKED 2026-08-13** · mock v25 | `docs/Barreletics Brand - Definitive-v25.html` | Hero → intro + pull → founder split → prototype split → 2-col values → Joseph cream mat → USA facts → letter close → GEO → dark close · **TE mobile stack** on splits + Joseph · v24 black museum prior | `page-about-*.liquid` · `page.our-story.json` · `specs/frozen/about.md` |

Update the **Fingerprint** column with the freeze commit SHA after each freeze ship.

---

## Footer — SIGNED 2026-08-12 (Join the list A) · LOCKED Jul 31 2026

- **Sitewide:** `layout/theme.liquid` → `{% sections 'footer-group' %}` (every page). One edit, every page. Do **not** paste Join the list into page templates.
- **Authority:** `specs/frozen/footer.md`
- **Stack:** Trusted by (toggle) → Join the list (toggle, NO 10%) → Shop/Learn/Support/Connect → Made in USA
- **TE:** Light/Dark per band (text follows); size overrides; show/hide Trusted + Join; checkmarks toggle **default off**. Dark Join = text-colored checks (no rust) if ever re-enabled.
- **Join the list A — SIGNED Andrew 2026-08-12:** headline left, form right. No rust checks. Body = **"New colorways and studio stories."** — no send-frequency claim, no "never spam", no "nothing else". Checklist TE stays, default off; do not turn on without a letter.
- **Hot Kits (Andrew 2026-08-12):** pulled the standalone `newsletter` from `collection.hot-kits.json`. Kits now uses the same footer Join the list as every other page. Hero / fifty-fifty / value-strip untouched.

- **Sitewide:** `layout/theme.liquid` → `{% sections 'footer-group' %}` (every page).
- **Authority:** `specs/frozen/footer.md`
- **Stack:** Trusted by (toggle) → Join the list (toggle, NO 10%) → Shop/Learn/Support/Connect → Made in USA
- **TE:** Light/Dark per band (text follows); size overrides; show/hide Trusted + Join; checkmarks toggle **default off**. Dark Join = text-colored checks (no rust) if ever re-enabled.
- **Join the list A (Andrew 2026-08-12):** headline left, form right. No rust checks. Body = **"New colorways and studio stories."** — no send-frequency claim (not twice a quarter), no "never spam", no "nothing else". Checklist TE stays, default off; do not turn on without a letter.
- **Learn includes:** Best Grippy Socks → `/pages/best-barre-pilates-yoga-grippy-socks`
- **Draft:** `187144929571` — never live.
- **Do not** add page-level duplicate newsletter sections.

### 10% purge sweep — 2026-08-08 (secondary pages)

Owner ask: "Make sure the footers and email 10% is up to date on the secondary pages also."

- `shopify-build/**` was already clean — `newsletter.liquid` / `footer.liquid` defaults are Join the list · Subscribe; no 10% in locales, templates, or snippets.
- **Fixed in place** (not hub-Locked): Contact v1 · Returns v3 · Size Chart v1 · Returns Portal v1 · Track Order v1 · Home Type OS Preview.
- **Hub-Locked mocks were NOT edited in place.** Purged copies exist as new versions awaiting an Andrew letter: **Collection v19** · **SEO v37** · **Journal v6** · **Help v4**. Say `LOCK THIS` + the version to promote. Locked v18 / v36 / v5 / v3 still carry the retired 10% footer by design.
- **Still stale by design:** PDP v16 (hard lock) · FAQ v4 (superseded by clean v5/v7) · all `Prior` / `Archive` / `Superseded` lineage mocks · `docs/footer-version-gallery.html` + `footer-gallery-assets/**` (historical record) · lossless archives (`07-COPY-GUIDE.md`, `05-PDP-ARCHITECTURE.md`, `06-HOMEPAGE-ARCHITECTURE.md`, `08-LIVE-SITE-COPY-AUDIT.md`).
- KB / decision records updated forward: BZ-007 marked **RETIRED**; ManyChat pricing, Tidio, Help Scout offers reply, product-knowledge, content inventories.
- QA: `planning/footer-sweep-qa/` — 1440px + 390px footer crops, harness `footer_shot.py`.

### Navigation wiring — forward update 2026-08-08

Owner ask: finish M4 navigation end to end. Composition unchanged; **link targets only**.

- **Header** (`assets/chrome.css`, no type values touched): nav/hamburger/Help breakpoint
  moved 768px → **900px** because the approved 18px title-case row needs ~873px and was
  forcing horizontal page scroll at 769–865px. Subnav `min-width` 180 → 220px (the longest
  label wrapped). Last drawer item's bottom border removed (doubled hairline).
- **Footer** (`sections/footer.liquid`): the hardcoded fallback columns pointed at ten
  handles that 404. They now carry the §3 link set from
  `planning/navigation-menu-spec.md` — same four columns, same headings, same order, no
  discount copy, `Better Than Grippy Socks` still under Learn. `footer-group.json`
  pre-selects `footer-shop` / `footer-learn` / `footer-support` and its `email_url` moved
  off the dead `/pages/contact`.
- **Size chart link** (`sections/pdp-buy-box.liquid`, `sections/variant-grid.liquid`):
  default was `/pages/size-chart` (404) → `/pages/performance-skins-size-chart` (200).
  One href each; the locked v19 buy-box composition is untouched.
- Evidence + reproducible checks: `planning/nav-qa/` (`audit.py`, `link-check.py`,
  screenshots at 390 / 768 / 1024 / 1440). Nothing was pushed to Shopify.

---

## PDP — product identity swap, 2026-08-08 (Andrew CURRENT MESSAGE — forward update)

> **Andrew, 2026-08-08:** *"no make the existing pdp page the closed sole and change the open sole. we probably want to keep secure in every hold on both for the title?"*
>
> Current message wins over the dated wording below, which is preserved as history. **The v19 spine
> is not reordered** — this is a product-identity change only. All 17 sections and their order are
> byte-verified unchanged.

| Item | Before 2026-08-08 | After 2026-08-08 |
|---|---|---|
| `templates/product.json` (v19 spine) | served **Open Sole** (`studio-performance-skin-footwear`) | serves **Closed Sole** (`best-reformer-pilates-legree-workout-shoes`) |
| Open Sole page | — | `templates/product.open-sole.json` (renamed from `product.closed-sole.json`) |
| `templates/product.closed-sole.json` | Closed Sole variant template | **deleted** — Closed Sole is the default template now |
| `templates/product.outdoor.json` | Grippy Water Shoes | unchanged, out of scope |
| Buy-box lede, **both** sole pages | Open: *Secure in every hold. / No sliding. No resets.* · Closed: *Heel and foot fully covered. / Same grip, same stability.* | **both pages:** *Secure in every hold. / No sliding. No resets.* (approved inventory, Problem/Solution) |
| Sole badge on `product.json` | charcoal (retired) | **`sole_badge: "Closed Sole"`, `sole_badge_color: "rust"`** — OWNER 2026-08-11 (NEVER black/charcoal) |
| Sole badge on `product.open-sole.json` | (varied) | **`sole_badge_color: "rust"`** (`#c45c3f`) |
| FAQ city GEO blocks | mixed mid-list | **NYC / LA / London·Melbourne (/ Toronto on Closed) last** under “Everything you need to know.” Discipline GEO + compare stay above cities. |

### Outdoor PDP — LOCKED 2026-08-20

**Andrew:** “ok lets lock in outdoor.”
**Handle:** `/products/aquatic-performance-skins` · template `product.outdoor.json` · Admin suffix **`outdoor`**
**Beat:** features → disciplines → Better than barefoot 50/50 → Shop all → Denise → sand video → dress them up → text reviews (no photo cards) → second skin → juicer.
**Type:** 50/50 titles = dress-them-up Display size.
**Photos:** he picks in TE (`te-pick-` Files). Do not reshuffle the spine without a letter.
**Out of this lock:** Open, Shop All, Home, Coperni, one-offs. Help family already LOCKED — do not reopen.

### Forward update — Open sock-math pad 80 (2026-08-20)

> **Andrew CURRENT MESSAGE:** 72 vs site. Open One pair pad = **80** (matches PDP 50/50). His TE photos kept. Closed stays 0. Real IG stills in Files as `te-pick-ig-real-`.

### Forward update — Sock math pad + no dark strip (2026-08-20)

> **Andrew CURRENT MESSAGE:** One pair / Done needs TE padding top/bottom. Kill darker strip under “Yoga socks are useless.” Leave his TE photos — do not push Open/Closed JSON. IG stills → Files as `te-pick-`.

### Forward update — Open media swap (2026-08-20)

> **Andrew CURRENT MESSAGE:** bad pics for video and images. Open only. TRANSFORM = Barre short studio video. Wow = studio clip `cf4ac9` (not mat). Sock-math = putting-on `65797`. Commit = blue studio (not court). Numbers = jumping. Closed untouched. Not signed.

### Forward update — Open TRANSFORM video + sock-math unframed (2026-08-20)

> **Andrew CURRENT MESSAGE:** Open only. Frame gone on One pair / Done (`image_unframed`). TRANSFORM video + unframed sock-math. Closed sock-math stays 480 framed. Keep `product.open-sole.json` = `product.in-studio-template.json`. Not signed.

### Forward update — Outdoor copies Closed beat (2026-08-20)

> **Andrew CURRENT MESSAGE:** Outdoor only. Same beat as Closed: Better than barefoot 50/50 → Shop all → Denise → sand video → dress them up → text reviews (no photo cards) → second skin. Juicer stays. 3 real water quotes only — do not invent 3 more. Closed / Open / buy-box / Liquid untouched.

### Forward update — Outdoor titles match dress them up (2026-08-20)

> **Andrew CURRENT MESSAGE:** Outdoor only. Dress them up is the locked title size. Better than barefoot + Feels like a second skin → same Display size (not Statement). Sand line bumped to 48/500. Slogans stay. Closed / Open / buy-box / Liquid untouched.

### Forward update — Outdoor home-run layout (2026-08-20)

> **Andrew CURRENT MESSAGE:** Outdoor only. Layout home run — he adds photos in TE. Sand wow → Denise 50/50 → Better than barefoot 50/50 → text reviews (no photos, no compact Judge.me) → dress-them-up → numbers. Alternate L/R + cream/white. Closed / Open / buy-box / Liquid untouched.

### Forward update — Outdoor: one wow + text reviews (2026-08-20)

> **Andrew CURRENT MESSAGE:** Outdoor only. Sand-kick is the only wow. Dock wow → 50/50 **Better than barefoot.** + lake paddle lady. Water-shoes 50/50 dropped. Reviews = heading + text cards only; photos live on `/pages/reviews`. Closed / Open / buy-box / 560 untouched.

### Forward update — Outdoor flow: Denise after sand (2026-08-20)

> **Andrew CURRENT MESSAGE:** Outdoor only. Shop → sand-kick hero → Denise quote. Then water-shoes 50/50 → dock wow. Closed / Open / buy-box / 560 untouched.

### Forward update — Outdoor second wow: dock water (2026-08-18)

> **Andrew CURRENT MESSAGE:** Lake-lady contain doesn’t work with the design / doesn’t look like a customer shot. Second wow = `outdoor-dock-adventures.jpg` Cover 80/70 (marina, coral on dock). Not Judge.me. Closed / sand-kick / 560 untouched.

### Forward update — Outdoor lake wow: whole photo (2026-08-18)

> **Andrew CURRENT MESSAGE:** Second wow must show the lady’s face **and** the paddleboard. Tall photo + Cover was cropping both. This instance only: `media_fit: contain` · 100vh/80vh. Closed / sand-kick stay Cover. Shared `fullbleed-statement` default remains Cover.

### Forward update — Outdoor paddle shots (2026-08-18)

> **Andrew CURRENT MESSAGE:** Water-shoes 50/50 = blue-graded paddle POV (`outdoor-water-50-50-blue.jpg`). Second wow = lady on the lake (`outdoor-paddle-caribbean.jpg`). Sand-kick hero + 560 Cover stay. Closed / Open / buy-box untouched.

### Forward update — PDP 50/50 Cover uniform (2026-08-18)

> **Andrew CURRENT MESSAGE:** keep 50/50 uniform site-wide. Open + Outdoor match Closed: **Cover** · **560** · pad **80** · mobile **320**. No Fit. No Square. Closed JSON untouched. Home fifty-fifty stays 640.

### Forward update — Outdoor wow break + beach-walk hero (2026-08-18)

> **Andrew CURRENT MESSAGE:** Sock Math between the two Outdoor wows. First wow = live beach-walk video `18588a6a` at **100vh / 80vh**. Closed / Open / buy-box untouched. No pool copy.

### Forward update — Open 50/50s: no Judge.me + Fit mode (2026-08-17)

> **Andrew CURRENT MESSAGE:** Judge.me review photos stay on the 3 review cards only — never in 50/50s. 50/50 media uses Shopify Files / studio on-foot. `fifty-fifty` **Fit** = natural photo (column width, height follows the file). No 560 crop. No letterbox. Closed `product.json` untouched. Cover stays Closed/Home default.

### Forward update — Outdoor rust badge + Open Sole PDP pass (2026-08-09)

> **Andrew CURRENT MESSAGE:** do all of the above — Outdoor/water + Open Sole. Outdoor badge **rust** `#c45c3f` (`sole_badge_color: rust`). Open H1 strips Admin sole dash (badge carries sole). Open sock-era = **The Pilates sock era is over.** Love-hate testimonial **Open only**. Featured photo sets unique Open ≠ Closed ≠ Outdoor ≠ Coperni (2026-08-09: Outdoor water-only Denise/Lisa K./Sienna H.; Coperni Kathia/Victoria/Sheryl — no Mia on Coperni). TRANSFORM scrim lightened on Open (`overlay_opacity: 35`). FAQ `bg_class: white` on Open/Outdoor/Closed to separate from cream footer “Trusted by…”. One pair. Done. = compact comparison **without** review quote (Closed/Open/Coperni cleared 2026-08-09). Cover-crop: Outdoor water-shoes/commit/numbers `focal_y 43` + mobile **360**.

### Forward update — Outdoor barefoot / slip / image dedupe (2026-08-09)

> **Andrew CURRENT MESSAGE:** tackle all new Outdoor items. Disciplines = **Anywhere you'd go barefoot — but better.** Secondary slogan **Better than barefoot.** on fullbleed lifestyle only. Image dedupe (beach / boat dock each once). Slip copy = general liability (won't create grip where surface has none) in buy-box, feature, FAQ, numbers. Reviews = 3 curated photos + compact live Judge.me (`show_live_text: true`, `show_text_cards: false`).

### Forward update — Outdoor Judge.me + IG lifestyle (2026-08-09)

> **Andrew CURRENT MESSAGE:** Judge.me text row must work — never hide photo-bearing reviews in compact mode; `show_live_text` always mounts widget. Replace Outdoor packshots with live/IG water lifestyle (paddleboard, dock, beach, resort). Real people body = **Paddleboarding. Beach. Boat. Resortwear.** Commit = dress-them-up resortwear. No pool positioning images.

### Forward update — Open Sole badge + FAQ city order (2026-08-08 night)

> **Andrew CURRENT MESSAGE:** Open Sole badge = rust orange (not charcoal). City FAQ items at the bottom of Everything you need to know.

### Forward update — PDP section/image scale back to v19 (2026-08-08 night)

> **Andrew CURRENT MESSAGE:** prior agent drifted scale. Match Definitive-v19: **fifty-fifty `min_height: 560`** (not Home WORKING 640), text `vertical_padding: 80`, mobile media **320**; **fullbleed-statement / lifestyle wow `height_desktop: 80` / `height_mobile: 60`** (was 90/100 + 70). Applied on `product.json`, `product.open-sole.json`, `product.outdoor.json` only — Home fifty-fifty default stays 640.

`product.json` SHA-256 after the swap: `9097409f46f4ef7e80a675b50d1072ca072e2a70ff2854fe97c78eee0b9e5b2b`
(prior lock fingerprint `00a209a5abf9bf9c258d7cb422cb055f7d95da7a0f11f7f7cb0294afa0b847a5`).
`product.open-sole.json` SHA-256: `d10e5e1e889c6c06f258b79e2a8d461ed0bab077d1ad7026f11f08408b430150`.

Template assignment is **per-product in Shopify Admin** and cannot be set from the repo — see
`planning/PDP-WORKING-ENTRY.md`. Decision record: `planning/10-decision-log.md` → **D-049**.
QA harness + previews: `planning/pdp-variants-qa/`.

Everything below this block still describes the locked v19 composition and remains in force.

### Section rhythm + cover-crop forward update, 2026-08-08 (Andrew CURRENT MESSAGE)

> **Andrew, 2026-08-08:** *"you have some spacing issues with breathers… on one of the 50-50s. From
> one section to the other, it looks like it needs some space. Take a look and it needs to be
> standardized."* · *"I think the 'great alternative to water shoes' — the top of the photo might get
> clipped."* · *"Shipping really needs to be in the accordion."*

**Spacing — standardised, no composition change.** Every hardcoded vertical section padding on the
PDP spine was replaced with design tokens under a three-tier rule now written into
`docs/23-design-token-reference.md` → *Section rhythm — three tiers*: content sections own
`--section-padding-y`, `value-strip` owns `--gap-a`, `fullbleed-statement` owns `0`, and
`pdp-buy-box` is the hero exception. Boundary gaps went from fifteen different values spread 0–162px
to **128 / 64 / 0** desktop and **96 / 48 / 0** mobile.

`fifty-fifty` gained a section-level `padding-block` rhythm band. The **full-bleed media law of
2026-08-08 is intact** — `.split-media` still has zero padding, zero margin and fills 100% × 100% of
its column. The band sits on the section box so a fifty-fifty can no longer weld itself to the next
breather at a literal 0px gap, and the text column subtracts it with `calc()` so the Theme Editor
*Inner vertical padding* control keeps its meaning and its 88px effect.

Sections edited: `fifty-fifty`, `pdp-features`, `disciplines`, `variant-grid`, `pdp-sock-math`,
`social-proof`, `guarantee-band`, `value-strip`. **These are shared library sections, so the rhythm
also lands on `index.json`, every `collection.*.json` and `page.about.json`** — intended, but those
pages have not been re-reviewed visually.

**Cover crop — fixed forward per slot, not by reverting to `contain`.** `A14_TopBottom_Yellow-600x600`
in the Outdoor *"A great alternative to water shoes"* slot was genuinely clipping: the shoe leaves
only 6.7% white above it, and `cover` was taking 9% at 390px — the toes were cut, with 6px of air
left at 1440px. Same failure on Outdoor commit/numbers and both Open Sole pack-shot slots.
**50/50 trust strip SIGNED 2026-08-16** (Andrew: “trusted update worked”). TE: **Show stars + trust line** + **Trust line** on every `fifty-fifty`. Off by default. Quote/Kimberly stars unchanged. Never invent review counts — use *Trusted by 1,000+ Instructors* or stars only.

**50/50 Theme Editor order SIGNED 2026-08-16** (Andrew: “Great I think we are good” · lock). Schema order only — same IDs, same Liquid. Every 50/50: **1 Photo / video → 2 Focus + height → 3 Heading / body / CTA → 4 Trust strip → 5 Quote / stats → 6 Layout extras → 7 Insets**. Do not reorder Features / Full-bleed / buy-box without a letter.

`fifty-fifty` gained a **Custom (%) focal point** Theme Editor control (`focal_x` / `focal_y`
ranges) because the old nine-value select can only snap to an edge. Fixes are per-slot settings:
Outdoor water-shoes/commit/numbers `focal_y 43` + `mobile_media_height 360`, Open second-skin
`focal_y 41`, Open lifestyle `focal_y 55`, Closed+Open lifestyle/numbers `focal_y 85` (keeps all four
shoes in `barreletixxjumpingtogether` instead of grazing them). Defaults unchanged, so no other page
moved. Evidence: `planning/pdp-variants-qa/crop-audit/`.

Still open, not changed: `Multi_Image.jpg` (1400×484) in the Closed and Open *commit* slots loses
30.6% off **each side** in a near-square box and slices the outer shoes — horizontal, so no focal
value fixes it. Needs a different image or Andrew's call.

**Shipping — nothing to consolidate.** All three PDPs already carried the identical four-accordion
set (Description · Care & how to wear · Shipping · 30-day returns + 90-day warranty) with identical
`shipping_accordion` / `returns_accordion` bodies, and no loose shipping copy anywhere outside them.
The approved trust split is intact: under-ATC empty, strip scan = Made in USA · Free shipping over
$150 · 30-day returns · 90-day warranty, accordion carries the detail. **`pdp-buy-box.liquid` was not
modified.** What looked wrong was the QA harness force-opening every accordion; it now renders them
closed as the theme does.

Spine order byte-verified unchanged on all three templates (17 / 17 / 16 keys, same sequence).
`product.json` SHA-256 `2fab77b44466fb011500d7a274b86dd82e3340bfe88ff26ae3a23a3823cebf6b`
→ **`05e84980c86e2fed2f8d404f09750c800d5f9ba17777d97f0491ac2108d7c564`**.

### Copy law forward update — "fully enclosed" RETIRED, 2026-08-08 (Andrew CURRENT MESSAGE)

> **Andrew, 2026-08-08:** *"quit saying fully enclosed heel - dont make shit up"*

Banned everywhere in customer-facing copy: **fully enclosed · fully-enclosed · fully enclosed heel ·
fully enclosed feel**. The surviving approved P-003 line is **"Heel and foot fully covered. Same
grip, same stability."** The older approved sentence *"Sleek, fully enclosed feel."* is superseded —
kept as a dated RETIRED record in `docs/09-PRODUCT-KNOWLEDGE.md` and
`manychat-kb/02-open-vs-closed-sole.md`, and recorded as **P-013** in `docs/10-DECISIONS.md`.

Copy-only edit, no composition change. `product.json` spine order byte-verified unchanged (17
sections, same order). SHA-256 `9097409f46f4ef7e80a675b50d1072ca072e2a70ff2854fe97c78eee0b9e5b2b`
→ **`f9fd7673893f09fb56fab566cecf62d7cb7232ef424bbfe41a16c5a6c56f4629`**.

Also fixed forward in `collection.closed-sole.json`, which carried the **retired discipline split**
(*"built for reformer footwork, barre, and Lagree where full-foot lockdown matters"*) — replaced with
P-003 feel-and-coverage wording.

Still outstanding (owned by another agent this turn, not edited here):
`templates/page.wholesale.json` and `sections/page-wholesale.liquid`.

---

## Apparel collection — forward update 2026-08-09 (Andrew CURRENT MESSAGE)

> **Andrew:** *"Apparel is not the correct landing page for the collections page. Update that.
> Please look at the live version. We already made this version so go back to the approved pages
> and update it."*

**Why it was wrong:** `/collections/apparel` had no dedicated template, so QA fell through to
default `collection.json` (grippy-shoes Shop All — sole cards, Closed/Open grid, grip FAQ).

**Fix-forward (no restore):**
- New `templates/collection.apparel.json` — live Apparel copy + Collection v18 shop-first spine
  (hero → value → grid → fullbleed → tees 50/50 → Think Outside the Sock → reviews → apparel FAQ)
- `variant-grid`: tab labels drive card meta; `show_size_filter` / `show_compare_link` for Apparel
  (Yoga Pants / T-Shirts · no M/L shoe filter · no Open/Closed Compare)

**Authority:** live `https://barreletics.com/collections/apparel` + hub **Collection v18 Locked**
structure. After push: Admin → Apparel collection → Theme template suffix **`apparel`**.

**QA push 2026-08-09 (this turn):** `collection.apparel.json` + `collection.json` (v18 Secure hero,
`show_sole_cards: false`) + Free People + Coperni sections/templates pushed to **`187144929571`**.
Verified: Shop All / Collection = v18 · Free People = teaser (badge **Only at Free People**) → hero → grid · exclusive on badge · shop copy = Barreletics.com · no outbound (Andrew 2026-08-21) · Coperni product = collab spine.
**Still Admin:** Apparel collection → Theme template → **`apparel`** (until then Apparel falls through to
default Collection v18 shoes stack). Open/Closed/Outdoor **collection handles do not exist** in Admin
(`/collections/open-sole` etc. 404) — templates exist; create/map handles or stop linking them.

---

## Grippy Shoes collection landing — forward update 2026-08-09 (Andrew CURRENT MESSAGE)

> **Andrew:** *"Fix the grippy shoe landing page now"*

**Why it was wrong:** Default `collection.json` still carried the pre-v18 stack (sole cards on,
"Shop All Styles" hero, missing pose / Commit fullbleed / Knock Socks, separate GEO, default tab
Closed). Hub authority is **Collection v18 Locked**.

**Fix-forward (no restore):**
- `sections/collection-hero.liquid` → v18 split hero (trust + Secure in Every Hold + CTAs + media
  with `media_fill` inset|column · sole cards off by default)
- `templates/collection.json` → v18 spine (hero → value → grid All-default → pose → Commit
  fullbleed → disciplines → Never Loses → Knock Socks → reviews → unified FAQ). Apparel stays on
  `collection.apparel.json`.

**Authority:** `docs/Barreletics Collection - Definitive-v18.html` · live handle
`/collections/barre-pilates-yoga-shoe-sock-footwear`. QA theme **`187144929571`**.
FAQ sole answers use P-003 wording (no discipline split; no “fully enclosed”).

---

## Reviews — LIVE Judge.me everywhere, 2026-08-08 (Andrew CURRENT MESSAGE — forward update)

> **Andrew, 2026-08-08:** *"Live for everything. But you would have to force the first cards to be
> ones with images and the text cards thereafter — unless we might need to manually add the photo
> cards?"*
>
> Current message wins. Reviews were curated static blocks; they are now live Judge.me on every
> surface. This is a **fix-forward** change — nothing was restored. The rest of the v19 spine is
> untouched: only the review slot changed, and it changed **in place**, at the same index.

### Hybrid reviews — 2026-08-08 evening (Andrew CURRENT MESSAGE)

> **Andrew:** curated top 3 photo cards + text cards underneath; live/dynamic under; different
> best-3 per page; Add image placeholders OK until real customer photos are dropped in TE.

**Forward update — not a restore of `social-proof`.** Slot stays `pdp-reviews` at the same spine
index. Composition is now:

1. **Top — up to 3 curated `photo_review` blocks** (Theme Editor image picker + verbatim quote).
   Blank image → “Add image” placeholder. Quotes only from `docs/09-PRODUCT-KNOWLEDGE.md`
   PRODUCTION-READY REVIEWS. **No author repeats across** product / open / outdoor / home /
   collection / reviews / judgeme-all templates.
2. **Under — live Judge.me** in `compact` mode (PDP / home / collection): histogram, media, and
   write-review chrome hidden; text-card grid, max 6. `full` mode on `/pages/reviews` pages.
3. Juicer remains the visual wall. “More stories →” still goes to `/pages/reviews`.

**Answer to the trailing question: photo-first is not manual.** Judge.me ships "Pictures First" as a
default sorting method (Judge.me Admin → Settings → Widgets → Review Widget → Search and pagination
→ Default sorting method). The store is currently on `most-recent` — verified in the live
`jdgmSettings` payload on `barreletics.com`. `pdp-reviews` also promotes photo reviews client-side,
so photo cards lead even before that dropdown is changed. No pinning or hand-curation required;
pinning stays available in the Judge.me admin as a deliberate override and the theme leaves pinned
reviews where Judge.me put them.

### Surfaces switched (same slot, same index, no reorder)

| Template | Slot | Was | Now |
|---|---|---|---|
| `templates/product.json` | 11 / 17 | `social-proof` (9 image + 6 text blocks) | `pdp-reviews` · scope **product** |
| `templates/product.open-sole.json` | 11 / 17 | `social-proof` | `pdp-reviews` · scope **product** |
| `templates/product.outdoor.json` | 10 / 16 | `social-proof` | `pdp-reviews` · scope **product** |
| `templates/index.json` | 8 / 14 | `social-proof` | `pdp-reviews` · scope **store** · cream `#f5f2ec` |
| `templates/collection.json` | 6 / 9 | `social-proof` + **hardcoded `4.9` / `294`** | `pdp-reviews` · scope **store** · live aggregate |
| `templates/page.reviews.json` | 1 / 2 | `social-proof` | `pdp-reviews` · scope **store** |
| `templates/page.judgeme_all_reviews.json` | 1 / 2 | `social-proof` | `pdp-reviews` · scope **store** |

JSON key renamed `social-proof` → `reviews` so the spine is self-describing. **v19 spine order after
the swap** (index 11 only):
`pdp-buy-box → value-strip → pdp-features → disciplines → fifty-fifty-sock-era → variant-grid →
fifty-fifty-lifestyle → fullbleed-statement → pdp-sock-math → fullbleed-lifestyle →
fifty-fifty-commit → **reviews** → fifty-fifty-numbers → guarantee-band → home-juicer →
collection-faq → pdp-sticky-atc`

SHA-256 after: `product.json` **`68a51a48daf41b69ea1e3239178eb75534695f284791b4ef004ce9902087b3be`**
(was `f9fd7673893f09fb56fab566cecf62d7cb7232ef424bbfe41a16c5a6c56f4629`) ·
`product.open-sole.json` `fb2644f1640e795732d45c9791c72dbfe9a0bd1236796e8b574721acdb552b4a` ·
`product.outdoor.json` `39b5ff607741d34592392b09d21fd8d78b34117001e89bf44514507a1e893007` ·
`index.json` `7ec3b87d6f6f65f3f71ab03b3b7aa290b5697a441c7a6494bc6845c197425290` ·
`collection.json` `c42e001181a08c1bbc787a834db1d45a1d41c9ba3581be68f7011df297efdb11`.

### `sections/pdp-reviews.liquid` — rewritten forward

- **Was broken.** It fetched `judge.me/api/v1/reviews` with no `api_token`; that endpoint 401s
  (verified against the live store), so the community grid only ever rendered "Reviews are
  temporarily unavailable." Do not reintroduce that call.
- **Now tokenless and server-rendered** from the metafields the Judge.me app installs:
  `product.metafields.judgeme.widget` (product scope) and
  `shop.metafields.judgeme.all_reviews_page` (store scope). The Judge.me script hydrates the same
  container for pagination, sort, voting and the write-review form.
- Curated `featured_review` blocks **removed** — there is no hand-authored review copy left in this
  section, which retires the misattributed-testimonial risk on every surface it covered.
- Judge.me markup is skinned to Barreletics tokens (`jdgm-*` → stars, type, borders, radius).
- Empty state is a **labelled** stand-in, never a silent blank region.

### Homepage + fabricated-content sweep — 2026-08-08 (Andrew CURRENT MESSAGE, second letter)

> **Andrew, 2026-08-08:** *"probably use the live review, however we may want to control them"* ·
> remove the *"Attribution TBD — verify named review before publishing claim"* note.

`index.json` is a radioactive surface, so it moved only on his word. Both changes are **forward
edits** — nothing was restored.

1. **Homepage reviews are live Judge.me.** `index.json` slot 8 / 14, `pdp-reviews` scope **store**,
   cream `#f5f2ec`. Order otherwise byte-identical.
2. **Internal QA note deleted.** `index.json` → `proof-numbers` → `n2` → `detail` was rendering
   *"Attribution TBD — verify named review before publishing claim"* to customers. Now empty; the
   Liquid guards `detail != blank`, so nothing renders in its place. **Nothing else in
   `proof-numbers` changed** — tone `white`, blocks `n1`/`n2`/`n3`, stat `1,000+`, label `Classes`,
   and the `n1`/`n3` details are all asserted unchanged by the edit script.

#### Fabricated review content — removed

A parallel audit found the curated blocks contained invented reviews. The Judge.me swap deleted the
`social-proof` blocks wholesale, which removed all of them from every template. Two fragments
survived outside those blocks and are now gone:

| Where | Was | Now |
|---|---|---|
| `index.json` → `proof-numbers` → `n2.detail` | "Attribution TBD — verify named review before publishing claim" | *(empty)* |
| `product.json` → `fifty-fifty-lifestyle` | `quote_author: "Sarah M."` · `quote_meta: "Barre Instructor · New York, NY"` — an **invented name over another customer's words** | *(both blank)* |

`fifty-fifty-lifestyle` keeps its quote text, image, stars and position on the spine — only the
fabricated attribution was removed, and `fifty-fifty.liquid` guards both fields on `!= blank`, so
the author and role lines simply do not render. **Open for Andrew:** the quote itself
("My love-hate relationship with the sock…") is not in the live Judge.me feed's first pages, so it
could not be verified. He should either supply the real reviewer or drop the quote. No name was
substituted, because substituting an unverified one repeats the original mistake.

Verified zero remaining across `shopify-build/`: `Lauren T.` · `Hannah R.` · `Priya K.` ·
`Jordan P.` · `Elena V.` · `Chris N.` · `Sarah M.` · `Attribution TBD` · `I will never go back`.
The `proof-numbers.liquid` **schema preset default** still carries "One athlete's achievement — swap
name in TE when locked"; it is a preset default, not rendered by `index.json`, and Andrew's letter
said to change nothing else in `proof-numbers` — left alone, flagged.

#### What was actually on each surface before the swap (curation record)

| Surface | Reviews shown | Authors |
|---|---|---|
| PDP Closed (`product.json`) | 15 | Mia Evans, Gwen M., Dvorah S., **Lauren T., Hannah R., Priya K., Jordan P., Elena V., Chris N.**, Kimberly, Dvorah S., Myrna C., Barbara, Wendy B., Amy S. |
| Homepage (`index.json`) | 9 | **exactly the first 9 of the Closed PDP set, same order** — 6 of them fabricated |
| Collection (`collection.json`) | 3 | Gwen M., Lauren T., Dvorah S. — all from the same pool |
| `/pages/reviews` | 3 | Mia Evans, Gwen M., Dvorah S. — the same three again |
| PDP Open / Outdoor | 12 / 7 | genuinely different sets |

Dvorah S. appeared on 5 of 6 surfaces, Gwen M. on 4. The homepage, collection and reviews page were
the same handful repeated. Post-swap the three PDPs show their own product's reviews (genuinely
different per product) and the four store-scope surfaces show the same store-wide pool in the same
sort order — see the control note below.

#### Control — what Judge.me gives Andrew

| Want | Where | Notes |
|---|---|---|
| Photo reviews first | Judge.me Admin → Settings → Widgets → Review Widget → Search and pagination → **Default sorting method → "Pictures First"** | Awesome plan. Also governs All Reviews page + floating tab. Theme already promotes photo reviews regardless. |
| Pin a review to the top | Judge.me Admin → Reviews → pin | Review Widget only; pins across a product group/bundle |
| Hand-pick a set | Judge.me Admin → Reviews → **Add tags → "Feature review"** | Free plan. Powers Cards/Reviews/Videos/Testimonials Carousel + Reviews Grid |
| A **different** curated set per page | Tag reviews with custom tags, then **Filter by tags** per Cards Carousel block | Free plan; per-block setting in the Shopify Theme Editor |
| Hide a review from home but keep it on the PDP | Cards Carousel set to **Featured / tag-filtered** on home, review widget on the PDP | Unpublishing hides it *everywhere* — not per page |

**Boundary:** per-page curation requires the Judge.me **Cards Carousel** app block, whose settings
live in the Theme Editor per block. App blocks cannot be fully wired from repo template JSON, so
switching the store-scope surfaces to curated carousels is Theme Editor work on Andrew's word, not a
repo change. The current `pdp-reviews` store scope renders the all-reviews widget — complete and
live, but uncurated.

### Visual change — Andrew must approve

He authorised live data, **not** a layout change, and the swap is not neutral: the curated
carousel (featured quote → 3 image cards → prev/next → text-card row) is replaced by the Judge.me
widget (rating summary + histogram + review list with customer photos). Before/after:
`planning/reviews-live-qa/REVIEWS-BEFORE-AFTER-1440px.png` and `-390px.png`. Pre-swap previews
preserved in `planning/reviews-live-qa/before/`. If he rejects the widget look, the fix-forward is
to re-skin `pdp-reviews` — **not** to restore `social-proof`.

- `sections/social-proof.liquid` is **retained** as a library section (preset intact, still
  addable in Theme Editor) but is no longer referenced by any template.
- `/pages/reviews` keep-or-retire: now resolved in favour of **keep** — it hosts the live
  all-reviews widget, which is real content rather than a duplicate of curated quotes.
- **Still hand-authored on the PDP, out of scope for this letter:** the `fifty-fifty-lifestyle`
  pull-quote at spine index 6 ("My love-hate relationship with the sock…", attributed to Mia
  Evans). It is a frozen lifestyle section, not a review section. Flag for Andrew.
- Buy-box `rating_text` ("Trusted by 1,000+ Instructors") is a trust claim, not a review
  aggregate — left untouched. Buy-box JSON-LD `aggregateRating` already reads the live
  Judge.me metafields.
- Nothing was pushed to Shopify — no theme ID was named in the message.

---

## PDP — LOCKED Aug 1 2026 (v19 mock + current product.json spine)

> ### ⛔ NEVER OVERWRITE
> Rule: `.cursor/rules/pdp-hub-lock.mdc`  
> File: `docs/Barreletics PDP - Definitive-v16.html` = content from **`691f03b`** only.  
> File: `docs/Barreletics PDP - Definitive-v19.html` = mock authority — do not overwrite without Andrew letter.  
> Template: `shopify-build/templates/product.json` = **locked spine as of 2026-08-01** (draft QA theme **`187144929571`**).  
> No Definitive-v20 for this lock — refinements (4-up Free shipping strip + lifestyle wow) live in `product.json`. New versions only for future experiments. July 17 / v17 / TypeOS-236a001 are **not** hub current.

- **Hub cards:** `v16 · Locked / APPROVED` (prior fingerprint) · **`v19 · Locked`** (current mock + Aug 1 spine refinements) · `v18 · Prior`
- **Current authority:** mock `Definitive-v19.html` **PLUS** `templates/product.json` composition locked **2026-08-01**
- **QA match note:** Draft `187144929571` (M4 Visual QA) is the Shopify QA match — do not thrash spine without Andrew letter. Push only when Andrew names this ID in-message. Never publish.

### Locked spine order (`product.json` `order`)

`pdp-buy-box` → `value-strip` → `pdp-features` → `disciplines` → `fifty-fifty-sock-era` → `variant-grid` → `fifty-fifty-lifestyle` (quote) → `fullbleed-statement` (**TRANSFORM YOUR PRACTICE** type-on-media) → `pdp-sock-math` (compact) → `fullbleed-lifestyle` (**media-only wow** · Stef running CDN · after sock-math / before commit) → `fifty-fifty-commit` → `reviews` (**`pdp-reviews`, live Judge.me — forward update 2026-08-08**; was `social-proof`, same index) → `fifty-fifty-numbers` (**Think outside the sock!**) → `guarantee-band` (centered 3-up) → `home-juicer` → `collection-faq` (FAQ+GEO) → `pdp-sticky-atc`

### Locked deltas (`product.json` = source of truth for spine)

| Zone | Locked state |
|------|----------------|
| Under ATC | **empty** (`show_trust_row: false`) |
| Value strip | **4-up scan (no strip links by default):** Made in USA · **Free shipping over $150** · 30-day returns · 90-day warranty |
| Trust architecture | Strip = scan · accordion = policy detail · empty under ATC |
| Fullbleed TRANSFORM | `fullbleed-statement` · show_text · title **TRANSFORM YOUR PRACTICE** · CTA Shop now → `#buy` |
| Lifestyle wow | `fullbleed-lifestyle` · `show_text: false` · **video** · 80vh / 60vh · after sock-math / before commit. **SIGNED 2026-08-16: this is the wow. No third full-bleed. Do not enlarge.** Swap media in-slot only. |
| Reviews | ~~`social-proof` · featured quote + image carousel + optional text-card ★ row~~ — **SUPERSEDED 2026-08-08:** slot is **`pdp-reviews` on live Judge.me**, same index 11. See "Reviews — LIVE Judge.me everywhere" above. CTA **More stories →** retained. |
| Sock math | **SIGNED 2026-08-16 on Closed:** editorial L (`layout: editorial`) · `docs/pdp-sock-math-directions.html` **v8** — One pair. / Done. / 3-pack / This ends that. / Cycle $144–$336 · $74 once · Silicone never grips… / 360° grip · Secure in every hold. / Foot: Yoga socks are useless. Photo Juicer **5986441** · **480** frame · lifestyle `cover`. Compact layout left for Coperni. Do not grow the frame. |
| Lifestyle quote | `fifty-fifty` · `content_style: quote` |
| Think outside | `fifty-fifty` · `content_style: statement` — eyebrow **Grip, Support, Comfort** · title **Think outside the sock!** · CTA Shop now → `#buy` |
| Guarantee | Centered **3-up** (`guarantee-band` · 30 / 90 / Built to Last) |
| FAQ + GEO | Merged in **`collection-faq`** — **no page `studio-trust`** |
| Juicer | **`home-juicer`** on PDP (after guarantee, before FAQ) |
| Newsletter | **No page newsletter** — footer Join the list only (NO 10%) |

- **Buy box:** lede calm 34–44 / 400 · quiet Complete the kit · Coming soon (S) · empty under ATC · `#buy` anchor · **title sole badge** (v16 quiet pill, TE optional)
- **Purchase stack:** price → muted `or 4 × $18.50` → color/size → qty+CTA → kit → accordion. **Title sole badge:** TE show on/off + color select — Black/charcoal `#1c1916` · Rust `#c45c3f` · Blue (live strip) `#458CD9` (Open default rust · Closed default black); label from override → `sole_type` metafield → handle/title fallback.
- **Variants 4×:** quiet `or 4 × $18.50` under Quick Add · LE/Sold Out badges REQUIRED · no sole image pills
- **Gallery thumbs:** 4 visible · touch-scroll · **no arrow buttons**
- **Archived:** `Definitive-v16-TypeOS-236a001.html` · backups in `docs/pdp-signed-backups/`

---

## PDP purchase stack — LOCKED Aug 1 2026 (carries Jul 31)

- **Surface:** Buy-box commercial composition on `Definitive-v19.html` `#buy` + `product.json` `pdp-buy-box`.
- **Authority:** `docs/Barreletics PDP - Definitive-v19.html` `#buy` · `specs/frozen/pdp.md` · lineage `pdp-purchase-stack-options.html` A (stack) + kit Option A
- **Order:** reviews trust → title + **optional sole badge** / lede → **PRICE** → muted `or 4 × $18.50` → [color + size] → [qty | CTA] → **empty under ATC** → quiet Complete the kit → accordion
- **Hard:** no Affirm purple · no payment chips · no bordered widget panels · **title sole badge TE optional** (CURRENT MESSAGE Aug 2 — show default ON, color select, metafield/handle label) · **no trust repeat under ATC** (strip + accordion own guarantees)
- **Do not** strip this stack from buy-box / `#buy` without Andrew letter.

---

## PDP trust split — LOCKED Aug 1 2026 (4-up Free shipping strip)

- **Authority:** `shopify-build/templates/product.json` `value-strip` + buy-box accordion (mock v19 remains visual prior; strip labels follow spine)
- **Value strip (scan, 4-up):** Made in USA · **Free shipping over $150** · 30-day returns · 90-day warranty · **no strip links by default**
- **Band height (2026-08-10 forward):** TE `padding_y` default **28px** desktop / **24px** mobile (was 16/`--gap-a`). Type stays 12px. Tune in Theme Editor — not a type-size change.
- **Under ATC:** nothing — CTA flows directly to kit
- **Accordion (detail):** Description · Care · Shipping (Complimentary shipping on orders over $150 · fulfill 1–2 business days · delivery windows) · 30-day returns + 90-day warranty
- **Do not** reintroduce ✓ ships/30/90 under ATC, or restore Non-toxic / No latex / No silicone strip labels, without Andrew letter.

---

## PDP variants 4× payments — LOCKED Jul 31 2026

- **Surface:** Shop all colors & styles cards on `Definitive-v19.html` `#variants`
- **Authority:** `docs/pdp-4x-payments-options.html` Option A · Under Quick Add · `specs/frozen/pdp.md`
- **Order:** Name → meta pill → $74 → Quick Add → quiet `or 4 × $18.50`
- **Hard:** meta pill owns chip zone — Pay in 4 never a second pill; no install under price next to Closed Sole meta · **no Closed/Open Sole image pills**
- **Status badges REQUIRED:** Limited Edition (blue) + Sold Out (charcoal) on variant images whenever status applies — do not strip
- **Chrome:** Draft Home Option A (tabs · Size · LE/Sold Out · meta pill · solid Quick Add · Sold Out = grey disabled button same shape as Quick Add)

---

## Header nav type — LOCKED 2026-08-11 nav #2 (supersedes Aug 8 18px)

**CURRENT MESSAGE 2026-08-11:** Ship v20d LOCKED nav **#2** — **13px / 500 / 0.01em / sentence case** · gap **26px** · actions **13px / 500**. Tokens + `header-group` `nav_link_size: "13"`. Logo TE left at **45** (do not force 42 without letter). Aug 8 18px row below is **history only**.

## Header nav type — UPDATED Aug 8 2026 (history — superseded by nav #2)

Owner: *“The font in the header is not good or right. Look at the live site, it’s much better.”*
Recorded **forward** at the time — **superseded 2026-08-11** by nav #2 lock above.

**Measured** on the published storefront, not from a theme copy on disk. Published theme =
`185687998755` **“Live Barreletics - Brian Go Live”** (Streamline 7.0). Probe + JSON:
`planning/header-type-qa/`.

| Surface | Live (measured) | Ours before | Ours after |
|---|---|---|---|
| Desktop nav link | 21.96px at rest / 18.96px sticky · 400 · 0.45em-equiv `0.025em` · **none** · 1.6 | 13px · 600 · 0.14em · **uppercase** | **18px · 400 · 0.025em · none · 1.6** |
| Between labels | 30px (7.5px 15px padding) | 32px | **30px** |
| Mobile drawer link | 22px · 400 · normal · none | 15px · 600 | **18px · 400 · normal** |
| Utility actions | icons only (no text equivalent) | 11px · 500 · 0.12em uppercase | **14px · 400 · 0.025em title case** |

- **The capitals were ours.** Live computes `text-transform: none` and its menu titles are
  authored in title case — so uppercase nav must **not** be reintroduced in CSS.
- **`/Users/andrewnehra/barreletics-theme-live-apr2026` is a different theme** from what is
  published. Do not derive live values from it; measure the storefront.
- Size lands at live's **sticky** value because our header is permanently sticky and its bar
  is shorter than Streamline's.
- `--type-nav-*` are **header-only** tokens (sole consumers: `chrome.css` header rules).
- **Size APPROVED by owner 2026-08-08: 18px · title case · weight 400 — “approved as built.”**
  Do not resize. 22px was evaluated and rejected; it survives only as a harness preview
  (`?size=22`). Side-by-side kept for the record:
  `planning/header-type-qa/COMPARE-desktop-1440px.png`.
- **Help renders as a LABEL, not a bare icon (owner 2026-08-08 — “where is help”).** Both
  `help_menu` branches now respect `show_action_labels`: label + caret when on, question-mark
  icon when off. Help · Account · Cart share 14px / 400 / 0.025em title case. Do not revert the
  assigned-menu branch to icon-only.
- **Help fallback URL = `/pages/help`** (`help_fallback_url` in `header.liquid`). Forward
  2026-08-14 — the Help hub exists. **Do not restore `/pages/faq`.** The Aug 8 note that
  `/pages/help` 404s is **history only**. Mobile drawer uses the same URL when no help menu
  is assigned, gated on `show_help`.
- **Forward fix 2026-08-08 (“which FAQ or help are we using”):** the desktop “Help ▾” parent
  used to href `help_menu.links.first.url` = `/pages/our-story` (About). It hrefs
  `help_fallback_url` in both branches. That URL is now **`/pages/help`**. Dropdown children,
  labels, and layout unchanged. Do not revert it to `links.first.url`.
- Headroom at 1440px, last nav item → utility actions: **167.7px** at 18px (133.7px at 22px).
  Both sizes crowd only in the 768–960px tablet band.
- **Bug fixed in passing:** inline cart count was painting on top of the "Cart" label
  (`.site-header__cart-badge--inline` lost to the later base rule on order). Now specificity-
  bumped. Pre-existing, not a type change.
- Untouched: `--type-brand-*` (wordmark), announcement strip, footer, and the unused
  `snippets/header-nav.liquid`.

---

## Juicer / Instagram — LOCKED Jul 31 2026

- **Reusable:** `sections/home-juicer.liquid` (TE name **Juicer Instagram**). Preset + complete schema — add/remove on Home, PDP, or any template in Theme Editor. **Not** homepage-only; **not** auto-wired onto every `product.json` / page JSON.
- **Authority:** `docs/Barreletics PDP - Definitive-v19.html` `#instagram` · `specs/frozen/juicer.md`
- **Composition:** Follow the movement · @barreletics · Real practitioners… · live Juicer feed · bigger tiles · no max-height / no inner sidebar scroll · See more · Follow on Instagram →
- **Locked TE defaults:** `max_height` **0** · `posts_per_page` **12** · `max_pages` **1** · `enable_see_more` **true** · feed `barreletics`. Instance overrides OK per page.
- **Home:** `templates/index.json` → `home-juicer` matches these defaults (no clamp).
- **Do not** reintroduce max-height clamp as the default or couple this section to homepage-only logic.

---

## How to add a freeze

1. Visual QA on disposable draft (`187144929571` unless Andrew names another ID).
2. Andrew says approve / freeze / settle / lock (or equivalent letter).
3. Add/update row in this registry + CONTRACT §8.
4. Add `APPROVED / FROZEN` banner comment at top of the section Liquid if useful.
5. Commit + push; deploy draft only if code changed and ID named.
