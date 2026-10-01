# Full technical integrity audit — 2026-08-08

Scope: `shopify-build/templates/**`, `shopify-build/sections/**`, and every QA preview under
`planning/`. Technical integrity only — **copy and wording are a separate agent's lane**; anything
copy-shaped is parked in the last section for them.

No `git restore` / `git checkout` / revert of any kind was run. No commits. No Shopify commands.
Tooling written for this audit lives in `planning/_audit-2026-08-08/`
(`schema_check.py`, `asset_check.py`, `qa_sweep.py` + their JSON output).

**Live-writer warning.** While this audit ran, another agent was writing to `shopify-build/`:
`templates/product.json` (14:02), `templates/collection.closed-sole.json`,
`templates/collection.outdoor.json`, `templates/page.faq.json`, and `sections/page-compare.liquid`
all changed mid-pass. Every finding below was re-verified against the tree as of **14:05**, but the
collection templates in particular are a moving target. I deliberately did **not** write into any
file that agent was holding.

---

## 1. JSON validity — PASS

All **46** JSON files under `shopify-build/templates/` (including `customers/`) parse cleanly.
Zero syntax errors. Zero `order` / `sections` mismatches, zero `block_order` / `blocks` mismatches
across every template.

## 2. Schema key integrity

Every `type` in every template was resolved against `shopify-build/sections/*.liquid`, and every
setting key and block type checked against that section's `{% schema %}`.

### Invalid setting keys — 15 (all pre-existing, none from today's work)

These fail silently in Shopify: the value is discarded and the section falls back to its schema
default, which is exactly how a section ends up looking blank or wrong for no visible reason.

| Template | Section | Dead keys |
|---|---|---|
| `index.json` | `split_hero` (`split-hero`) | `bg_color`, `text_color`, `body_color` |
| `collection.gift-cards.json` | `variant-grid` | `collection`, `products_per_page`, `view_all_url` |
| `collection.limited-editions.json` | `variant-grid` | same three |
| `collection.new-arrivals.json` | `variant-grid` | same three |
| `collection.sale.json` | `variant-grid` | same three |

The `variant-grid` case is the more serious one: those four collection pages are trying to point the
grid at a specific collection and page size, and **none of it is taking effect**. The grid is
rendering whatever its schema defaults say. All four templates predate today (Jul 31), so this is
old breakage surfacing, not a regression — but it is live breakage.

`split_hero`'s three colour keys are cosmetic; the hero renders, it just ignores those colours.

### Block types and block setting keys — PASS

Zero invalid block types. Zero invalid block setting keys across the entire template set.

### Missing section files — 10 (expected)

`main-404`, `main-account`, `main-activate-account`, `main-addresses`, `main-login`, `main-order`,
`main-register`, `main-reset-password`, `main-list-collections`, `main-password` are referenced by
templates but absent from `shopify-build/sections/`. These are Shopify's built-in account/system
sections supplied by the base theme; `shopify-build/` is an overlay, not a standalone theme. Not a
defect — noted so it isn't rediscovered as one.

### Orphaned schema settings — 271, two of which matter

The bulk are the shared "Section frame" inset controls (`inset_top`, `inset_x_mobile`,
`hide_on_mobile`, …) and Theme-Editor-only type overrides, present on every section by design.
Two orphans are real signals, both covered under Links below:

- `pdp-buy-box.kit_link_1_url` / `kit_link_2_url` — never set by any template, so the kit links fall
  through to hardcoded 404 defaults.
- `collection-hero.closed_url` / `open_url` — never set, so the sole cards fall through to
  `/collections/closed-sole` and `/collections/open-sole`, both 404 on live.

## 3. `product.json` integrity — PASS

Order is exactly the 17-section locked spine, in the required sequence:

```
pdp-buy-box → value-strip → pdp-features → disciplines → fifty-fifty-sock-era → variant-grid →
fifty-fifty-lifestyle → fullbleed-statement → pdp-sock-math → fullbleed-lifestyle →
fifty-fifty-commit → social-proof → fifty-fifty-numbers → guarantee-band → home-juicer →
collection-faq → pdp-sticky-atc
```

**SHA-256 (as of 14:05):** `2fab77b44466fb011500d7a274b86dd82e3340bfe88ff26ae3a23a3823cebf6b`

At 13:55 the same file hashed `61388cef8ad9f92d6f2e6a94a29c6d22037fa50ec36e9f8730e962ab796d5a0a`.
The other agent rewrote it at 14:02 (+479 / −115 lines). The spine order survived that rewrite
intact — I re-checked after. Nothing in this audit touched `product.json`.

Sibling spines, for the record:

- `product.open-sole.json` — 17 sections, identical spine with `fifty-fifty-second-skin` at
  position 5. SHA `9331cff0c04e4e340d57750744bb7af593d58df3f8dd77f31eb0c4786325c39d`.
- `product.outdoor.json` — 16 sections, `pdp-sock-math` deliberately absent as specified. SHA
  `5aa55f77250de04c21d95cb3ef5bd9bebb43aadb87ab2d82233e24c912fef081`.

## 4. Empty / missing content

108 empty-string settings exist. Most are intentional hide switches (`eyebrow: ""` and
`cta_text: ""` suppress their element behind an `!= blank` guard), and I verified each pattern
against the section Liquid. The ones that actually render something visible:

### Sections that will paint a grey "Media placeholder" gradient

`fifty-fifty.liquid` falls back to `.split-media__placeholder` — a grey-to-pink gradient panel
printing the alt text — when no image, `image_url`, video, or `video_url` is set. Four sections hit
this:

| Template | Section | What renders |
|---|---|---|
| `collection.json` | `fifty-fifty-commit` | grey gradient panel, half the section width |
| `collection.hot-kits.json` | `fifty-fifty-kit-idea` | grey gradient panel |
| `page.about.json` | `about-hero` | gradient printing "Barreletics Performance Skins on reformer" |
| `page.about.json` | `about-founder` | gradient printing the literal words "Founder portrait placeholder" |

The About page ones predate today. The two collection ones are from today's work.

### Broken video source

`collection.json` → `fifty-fifty-grip` has `video_url: "#"`. That renders
`<video><source src="#" type="video/mp4"></video>` — an autoplaying element pointed at the page
itself. It never paints. The identical twin section on `index.json` (same id, same heading, same
body) carries the real asset:
`https://cdn.shopify.com/s/files/1/0045/0612/4391/files/Barre_Short_Video_-nosound.mp4?v=1590451878`
plus a `poster_url`. The collection copy looks like it was duplicated with the media stripped.

Not fixed here: `collection.json` was being actively rewritten by the parallel agent, and choosing
media is a content call. The candidate value is above.

### Empty H1 fallbacks — safe

`collection.open-sole.json` and `collection.closed-sole.json` both set `title: ""` on
`collection-hero`. The Liquid is `{{ section.settings.title | default: collection.title }}`, and
Liquid's `default` filter treats an empty string as falsy, so the H1 falls back to the Admin
collection title rather than rendering empty. Worth an eyeball in preview since the Admin titles are
SEO-shaped, but structurally sound.

The empty `closed_desc` / `open_desc` / `closed_image` / `open_image` on those two templates are
inert — `show_sole_cards` is `false`, so the cards that would consume them never render.

## 5. Images — PASS after one fix

35 distinct media URLs across all templates and sections were fetched with `curl`. **34/34 now
return 200.**

**Fixed:** `product.outdoor.json` → `social-proof` block `r3` pointed at
`…/4391/files/A14_TopBottom_Yellow-600x600_15161205-….jpg` (404). The same asset lives under
`…/4391/products/…` and returns 200 — that path is already used correctly by
`fifty-fifty-water-shoes` in the same file. Changed `files/` → `products/`. Confirmed 200, and the
rebuilt preview reports zero broken images.

### Wrong-product check

I pulled each product's real image list from the storefront `.js` endpoints and compared:

- `product.open-sole.json` — all images belong to `studio-performance-skin-footwear` (Open Sole). Correct.
- `product.outdoor.json` — all `A14_*` images are genuinely attached to `aquatic-performance-skins`. Correct.
- `product.json` (Closed Sole) — **one to look at.** `social-proof` block `r7` uses
  `Copreni_Final_More_grey.png`, which is the Coperni collaboration product's only image
  (`/products/barreletics-x-coperni-closed-sole`). A collab hero shot is being used as a customer
  review photo on the main Closed Sole PDP. It loads fine; whether it belongs there is a judgement
  call, so it is reported rather than changed.

## 6. Links

Every internal `href` in the changed templates and sections was tested against the live storefront.
24/41 return 200. Breaking the 17 failures into real problems and noise:

### Real dead links, live today

| Path | Where | Impact |
|---|---|---|
| `/products/hot-pilates-kit` | `pdp-buy-box.liquid` default | "Complete the kit → Hot Pilates Kit" in the buy box on Closed Sole **and** Open Sole PDPs |
| `/products/hot-yoga-kit` | `pdp-buy-box.liquid` default | same, second link |
| `/collections/open-sole` | `page.compare*.json` `product_a_url`, `collection-hero.liquid` default | the "Shop Open Sole" CTA on the comparison page |
| `/collections/closed-sole` | `page.compare*.json` `product_b_url`, `collection-hero.liquid` default | the "Shop Closed Sole" CTA on the comparison page |
| `/collections/grippy-shoes` | `page.size-chart.json` `cta_url`, plus `hero.liquid`, `main-cart.liquid`, `page.about.json`, `page.grip-comparison.json`, `page.technology.json` | primary CTA on the size chart page and several others |

The kit links are the worst of these: `show_kit_links` is `true` on both main PDPs, neither template
sets `kit_link_1_url` / `kit_link_2_url`, so both fall through to the hardcoded 404 defaults. Two
dead links sitting directly under Add to Cart.

The live collection handle that does resolve is
`/collections/barre-pilates-yoga-shoe-sock-footwear` (200) — `collection.hot-kits.json` already
points its CTA there correctly.

None of these were fixed: `pdp-buy-box` is a named radioactive surface, and picking the right
destination (create the collection vs. repoint the link vs. hide the block) is Andrew's call.

### Not-yet-created pages — expected, not defects

`/pages/wholesale`, `/pages/studio-program`, `/pages/ambassador`, `/collections/hot-kits` all 404
because the Shopify page/collection doesn't exist yet. `/collections/hot-kits` matches the known-good
nav baseline (15/16 with only hot-kits failing). The partner hub CTAs in `page-partners.liquid` will
light up the moment Brian creates those three pages.

### Older wrong handles — pre-existing

`/pages/contact` (live is `/pages/contact-us-form`), `/pages/shipping`, `/pages/size-guide`,
`/pages/warranty` — all in `contact-cta.liquid` and `page-contact.liquid`, neither changed today.

### False positives — ignore

`/cart/add` (400, POST-only), `/cart/change.js` (400), `/recommendations/products.json?product_id=`
(422, needs a real id), `/embed-code.js?per=` (a concatenated Juicer URL fragment, not a link).

### Template-suffix typos — cosmetic, Admin-visible

`page.shipping-retruns.json` and `page.start-a-retrun.json` carry misspellings ("retruns",
"retrun"). These are Shopify **template suffixes**, not URLs, so nothing 404s — but the misspelling
shows in the Admin template dropdown. The clean-named aliases exist and are byte-identical:

- `page.start-a-retrun.json` ≡ `page.returns-portal.json`
- `page.compare.json` ≡ `page.compare-open-vs-closed.json`
- `page.reviews.json` ≡ `page.judgeme_all_reviews.json`
- `page.size-chart.json` ≡ `page.size-guide.json` (identical content; differ only in unicode escaping)

## 7. `fifty-fifty.liquid` full-bleed change — no collateral damage

The new rule is scoped defensively:

```css
.split-section:not(.split-section--contain) .split-media { padding: 0; margin: 0; }
```

`contain` mode keeps its own `display:flex` / `object-fit:contain` / `max-width:420px` /
`padding:48px 24px` block untouched. I enumerated all 19 `fifty-fifty` consumers across every
template:

- **`contain`:** exactly one — `index.json` → `fifty-fifty-one-pair`. Unaffected by the change, as
  reported.
- **`cover` or default cover:** the other 18 — collection, hot-kits, About, and all three PDPs.
  These are the intended beneficiaries.

Rendering verified in the rebuilt PDP previews at 1440px and 390px: media fills its column edge to
edge, no inset, no letterboxing. Collection, hot-kits and About have no preview harness (see §9), so
their fifty-fifty sections were verified by settings inspection only — and the two collection ones
hit the placeholder/broken-video problems in §4 regardless of fit mode.

## 8. Mobile + desktop QA

Driven through CDP `Emulation.setDeviceMetricsOverride` at 1440×900 and 390×844, working around the
500px headless clamp. Full data in `planning/_audit-2026-08-08/qa-sweep.json`.

### Horizontal overflow — PASS everywhere

`document.scrollWidth === viewport width` on all 13 pages at both widths. The `variants-tab` hits
that show up in the raw log sit inside `.variants-tabs { overflow-x: auto }`, which is the intended
mobile behaviour, not page overflow.

### Text under 12px — PASS

Every sub-12px string is either the approved 11px uppercase label token or belongs to the QA
harness's own chrome (the black banner, the `/products/…` path footer). No section ships
non-compliant small type.

### Sticky elements — PASS

The one "overlap" flagged on every page is `div.header-section` containing `header.site-header` —
a parent wrapping its child, both `position: sticky`. Not a clash. `pdp-sticky-atc` never collides
with the header.

### Tap targets under 44px

**Fixed** in `variant-grid.liquid`, inside the existing ≤768px block: `.variants-link`
("Size chart →", "Compare →") was 61×21 and `.variants-see-all__btn` ("See all colors & styles") was
138×19. Both are 14px underlined text controls where padding would drag the underline away from the
text, so the hit region is grown with a transparent `::after { inset: -12px -10px }` overlay —
nothing moves visually, the touch area clears 44px. Note that `getBoundingClientRect()` still
reports the small box afterwards, since pseudo-elements don't change an element's box; the probe
cannot see this fix, so don't read the unchanged numbers as a failed fix.

`variant-grid` already handled the rest of mobile correctly: `.variants-tab { min-height: 44px }`
and `.variants-size__btn { min-width: 44px; min-height: 44px }` were already in place.

**Not fixed, reported:**

- `.home-juicer__cta` ("Follow on Instagram →") — 180×22 on mobile. `home-juicer` is a named
  radioactive surface; not touching it without a word from Andrew.
- Variant card colour-name links — 18px tall on mobile. The card image above is the real tap target
  and is full-size, so this is a minor secondary path.
- Desktop `.variants-tab` (36px) and `.variants-size__btn` (39×28) — desktop pointer targets; the
  44px rule is a touch guideline and mobile already complies.
- `page.returns.json` — **19** sub-44px targets at both widths, including the primary
  "Start a Return" (92×18) and "Start an Exchange" (121×18) portal CTAs. That section
  (`page-returns.liquid`) wasn't part of today's changes, but it is on the review list and these are
  the page's main actions.

## 9. Preview fidelity

**`qa-stub` is gone from every PDP preview.** The only surviving mentions are a historical note in
`planning/pdp-variants-qa/README.md` and a stale `__pycache__/build.cpython-314.pyc`. The upgraded
`build.py` renders `variant-grid`, the buy-box accordions, `home-juicer` and `pdp-sticky-atc` for
real from `product-data.json`.

**Stale previews found and regenerated:**

| Preview | Was | Source was | Now |
|---|---|---|---|
| `partner-pages-qa/preview-wholesale.html` | 13:21 | 13:26 | rebuilt |
| `partner-pages-qa/preview-studio-program.html` | 13:21 | 13:26 | rebuilt |
| `partner-pages-qa/preview-ambassador.html` | 13:21 | 13:26 | rebuilt |
| `partner-pages-qa/preview-partners.html` | 13:22 | 13:26 | rebuilt |
| `returns-pages-qa/preview-compare-open-vs-closed.html` | 13:22 | 13:26 | rebuilt |
| all three `pdp-variants-qa/preview-*.html` | were current | — | rebuilt anyway, to pick up the image fix |

All previews and screenshots are now newer than every template and section they render.

**Gap: the collection templates have no preview harness at all.** `collection.json`,
`collection.open-sole.json`, `collection.closed-sole.json`, `collection.hot-kits.json` and
`collection.outdoor.json` all changed today and there is nothing under `planning/` that renders
them. That is also exactly where the broken video source and the two placeholder panels live, so
those defects have never been seen on screen. Building that harness is a real piece of work and the
parallel agent is currently holding two of those files, so it is flagged rather than attempted.

## 10. Type OS compliance

The four new partner sections are **clean** — `page-wholesale`, `page-studio-program`,
`page-ambassador`, `page-partners` each have zero hardcoded `font-size`, zero hardcoded
`font-weight`, zero `!important`. Same for `main-page.liquid`, `collection-faq.liquid` and
`fullbleed-statement.liquid`. That is the newest work and it is on-system.

The single `!important` in `fifty-fifty.liquid` is `max-width: none` on `.split-text__title` — a
layout reset, not a type override. Benign.

Hardcoded values that remain are all pre-existing and predate today's edits: `pdp-buy-box` (21 sizes
/ 11 weights), `variant-grid` (19 / 10, plus 6 `!important` on grid-column rules), `social-proof`
(17 / 6), `pdp-sock-math` (6 / 6), `collection-hero` (4 / 1). None of it is drift introduced today,
and converting it is a deliberate Type OS migration, not an audit fix — so it is reported, not
touched.

---

## Fixed in this pass

1. `shopify-build/templates/product.outdoor.json` — `social-proof` block `r3` image URL
   `files/` → `products/`. Was a 404, now 200.
2. `shopify-build/sections/variant-grid.liquid` — mobile-only transparent `::after` hit-area on
   `.variants-link` and `.variants-see-all__btn`, bringing both over 44px. No visual change, no
   logic change.
3. Regenerated five stale previews (four partner, one compare) and rebuilt all three PDP previews
   plus their 1440/390 screenshots and side-by-sides.

Nothing was restored, reverted, checked out, committed, or pushed.

## Preview URLs (static server, port 8787)

All verified 200:

- http://localhost:8787/planning/pdp-variants-qa/preview-closed.html
- http://localhost:8787/planning/pdp-variants-qa/preview-open.html
- http://localhost:8787/planning/pdp-variants-qa/preview-outdoor.html
- http://localhost:8787/planning/pdp-variants-qa/SIDE-BY-SIDE-1440px.png
- http://localhost:8787/planning/pdp-variants-qa/SIDE-BY-SIDE-390px.png
- http://localhost:8787/planning/partner-pages-qa/preview-partners.html
- http://localhost:8787/planning/partner-pages-qa/preview-wholesale.html
- http://localhost:8787/planning/partner-pages-qa/preview-studio-program.html
- http://localhost:8787/planning/partner-pages-qa/preview-ambassador.html
- http://localhost:8787/planning/returns-pages-qa/preview-returns.html
- http://localhost:8787/planning/returns-pages-qa/preview-returns-portal.html
- http://localhost:8787/planning/returns-pages-qa/preview-size-chart.html
- http://localhost:8787/planning/returns-pages-qa/preview-compare-open-vs-closed.html
- http://localhost:8787/planning/returns-pages-qa/preview-reviews.html
- http://localhost:8787/planning/returns-pages-qa/preview-free-people.html

No URL exists for the five collection templates — see §9.

---

## For the copy auditor

Not edited, not judged — handing these over:

1. **`collection.closed-sole.json`, `geo-section` blocks** use "Full enclosure means nothing shifts"
   (`geo-barre`) and "the full enclosure should hug your foot" (`geo-sizing`). The sole-description
   rule bans any construction calling the Closed Sole enclosed.
2. **`collection.closed-sole.json` geo blocks assign disciplines to a sole** — "Best grippy shoes for
   reformer footwork", "Closed Sole grippy shoes for barre classes", "Grippy shoes for Lagree and
   Megaformer" are all framed as Closed-Sole-specific. Same pattern in `collection.open-sole.json`
   (`geo-yoga`, `geo-mat`). The discipline split was retired.
3. **`product.outdoor.json` → `pdp-buy-box.short_description`** opens "The closed sole provides grip,
   stability, and protection from hot sand" — on the Outdoor product, which is a different product
   from the Closed Sole.
4. **`collection.json` → `collection-hero.body`** reads "Closed Sole wraps your entire foot. Open Sole
   frees your heel…", which drifts from the sanctioned wording used everywhere else in the same file
   (`closed_desc` / `open_desc` are correct).
5. `collection.outdoor.json` and its geo blocks read clean on the no-pool rule — beach,
   paddleboarding, boat decks, resortwear, hot sand only. No pool language found anywhere in
   `shopify-build/templates/`.
