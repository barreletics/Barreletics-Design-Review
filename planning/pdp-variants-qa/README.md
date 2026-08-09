# PDP variants — Closed Sole / Open Sole / Outdoor

## READ FIRST — what these preview files are, and what they are not

**Every section on all three pages now renders for real. There are no stubs left.**

Earlier builds of `build.py` replaced `variant-grid`, `home-juicer` and `pdp-sticky-atc` with grey
`qa-stub` placeholder strips, and rendered only two of the buy box's four accordions. That is why
the previews read as *"the accordion section is missing the descriptions"* and *"where is the all
variants"* — **the templates were never missing that content; the harness was not drawing it.**
Fixed 2026-08-08.

| Section | How the harness renders it |
|---|---|
| `pdp-buy-box` | Real. All **four** accordions — Description · Care & how to wear · Shipping · 30-day returns + 90-day warranty — rendered **closed**, exactly as the theme ships them. Click to open in the live preview |
| `variant-grid` | **Real.** Full tab set, M/L size filter, See all, and one card per colour×size from live product data. Section CSS + JS lifted from `sections/variant-grid.liquid` |
| `value-strip` | Real. Both lines — the full `·` list for desktop and the `show_on_mobile` subset that takes over below 768px |
| `pdp-features`, `disciplines`, `fifty-fifty`, `fullbleed-statement`, `pdp-sock-math`, `social-proof`, `guarantee-band`, `collection-faq` | Real markup + real section `<style>`. `fifty-fifty` layout variables are read from the template with the same defaults the Liquid uses |
| `home-juicer` | Real chrome, real tile count, real grid — but the pictures are **filler**, drawn in the same labelled placeholder mosaic the v19 mock uses for a blocked feed. juicer.io only serves tiles at runtime |
| `pdp-sticky-atc` | Real bar, pinned open. In Shopify it slides in when the buy box scrolls away — a static capture can never show that |

Variant, colour, price and sold-out data comes from `product-data.json`, read from the live store on
2026-08-08 via the read-only Shopify MCP. Nothing in it is invented. Where the store has no
colour-specific photograph, the product's featured image is used.

**This is still a local harness, not an approval surface.** Per the design-system rules, visual
approval happens on a Shopify draft preview. Nothing has been pushed.

---

**Date:** 2026-08-08 (revised same day — see the swap below)

**Original ask:** *"Did you make the secondary PDP differences between open and closed sole page with
slogan variables and images? Keep the PDP we already refined and make another with the variation,
then we need to do the outdoor page."*

**Revision — Andrew, 2026-08-08, governing:** *"no make the existing pdp page the closed sole and
change the open sole. we probably want to keep secure in every hold on both for the title?"*

Three product pages, differentiated by slogan, copy and imagery — not one template serving all
products.

| Page | Template | Product | Handle |
|---|---|---|---|
| **Closed Sole** | `templates/product.json` — **the refined v19 spine** | Studio Performance Skin — Closed Sole | `best-reformer-pilates-legree-workout-shoes` |
| **Open Sole** | `templates/product.open-sole.json` | Studio Performance Skin — Open Sole | `studio-performance-skin-footwear` |
| Outdoor | `templates/product.outdoor.json` | Grippy Water Shoes | `aquatic-performance-skins` |

`templates/product.closed-sole.json` was **renamed** into `product.open-sole.json` — not copied — and
its copy rewritten from Closed Sole to Open Sole. Closed Sole no longer needs a variant template
because it is served by the default one.

Assignment is per-product in Shopify Admin → Product → Online store → Theme template. Andrew or
Brian makes that selection; nothing about it is automatic. **Open Sole must be re-pointed to
`product.open-sole`** — the old `product.closed-sole` name is gone.

---

## The 2026-08-08 swap — what moved in `product.json`

The v19 **spine order is unchanged**. All 17 sections and their sequence were captured before the
first edit and diffed after the last one: identical. This was a product-identity change, not a
composition change, so only four fields moved.

| Field | Old | New | Approved source |
|---|---|---|---|
| `pdp-buy-box.sole_badge` | *(absent — auto-derived)* | `Closed Sole` | Product naming (`barreletics-brand-copy`), Shopify product title |
| `pdp-buy-box.sole_badge_color` | `rust` | `charcoal` | Established badge convention: rust = Open, charcoal = Closed |
| `collection-faq` → `f2` answer, final sentence | *"Closed Sole for full lockdown; Open Sole when you want heel freedom."* | *"Both perform identically with the same grip and stability."* | P-003 (`manychat-kb/02-open-vs-closed-sole.md`), verbatim |
| `collection-faq` → `f6` question + answer | *"Open Sole vs Closed Sole — which one?"* / reformer-vs-barre discipline split | *"Closed Sole or Open Sole — which one?"* / the full P-003 feel-and-coverage answer | P-003, verbatim |

The two FAQ edits were required regardless of the swap: both carried the **retired discipline split**
that P-003/P-004 killed on 2026-08-02, listed as copy anti-pattern #9 in `barreletics-brand-copy`.

```
SHA-256 before  00a209a5abf9bf9c258d7cb422cb055f7d95da7a0f11f7f7cb0294afa0b847a5
SHA-256 after   9097409f46f4ef7e80a675b50d1072ca072e2a70ff2854fe97c78eee0b9e5b2b
```

The hash change is authorised by Andrew's current message and recorded forward in
`planning/m4-section-freeze.md`, `planning/PDP-WORKING-ENTRY.md` and `planning/10-decision-log.md`
(**D-049**). The v19 and v16 mock HTML files were read only — neither was touched.

### Deliberately left alone in `product.json`

| Field | Why |
|---|---|
| `short_description` | Product-general and identical to the section's Liquid default. Names no sole. |
| `size_soon_note` / `show_soon_size` | The Small-coming-soon roadmap applies to both soles, not just Open. |
| Size-chart link | Not set — inherits `/pages/performance-skins-size-chart`, which is product-general. |
| All image URLs | Every image on the v19 spine is brand lifestyle (`Multi_Image`, `barreletixxjumpingtogether`, `barreletixxstefrunningpinkbackground`, `IMG_2917`) or already Closed-Sole family (Dusty Rose, Coperni grey). **No Open-Sole-exclusive product photography was on the page**, so nothing needed swapping. |
| `variant-grid.default_tab: "closed"` | Was already `closed` — now correct for the page rather than accidental. |
| `fullbleed-statement` title *TRANSFORM YOUR PRACTICE* | Breaks the sentence-case law but is a named element of the v19 lock (`.cursor/rules/pdp-hub-lock.mdc`). Not sole-specific. Flagged, not changed. |
| `social-proof` → `r9` | *"Open Sole for mat, Closed for machines — same grip system, zero sock drawer."* Names both soles and asserts the retired split, on what is now the Closed Sole page. Rewriting it would mean inventing a review. Flagged for Andrew. |
| `collection-faq` → `geo-hot` | *"The patented grip surface performs better when warm"* is on the slogan-engine banned list ("heat makes grip better — not approved"). Product-general and part of the v19 lock. Flagged, not changed. |

---

## Structural changes vs settings changes

**Structural: none of consequence.** No section files were edited, no schema settings were added,
no new section types were invented. Every setting used already existed in the approved library.

Both variant templates keep the v19 spine's 17-section order. Two section *keys* were renamed inside
the new files so the Theme Editor labels read honestly — nothing about the rendered composition
changes:

| v19 key | Open Sole | Outdoor |
|---|---|---|
| `fifty-fifty-sock-era` | `fifty-fifty-second-skin` | `fifty-fifty-water-shoes` |

Two settings differences on Outdoor turn things **off** rather than restyling anything:

- `show_kit_links: false` — the Hot Pilates / Hot Yoga kit cross-sells are studio offers.
- `show_soon_size: false` — the "Small coming soon" note describes the studio SKU roadmap.

Everything else is copy and image URLs.

---

## Copy set — Closed Sole (`product.json`, the v19 spine)

Unchanged from the locked v19 composition apart from the four identity fields in the table above.

| Slot | Copy | Source |
|---|---|---|
| Buy-box lede | Secure in every hold. / No sliding. No resets. | Approved inventory (Problem/Solution) — Andrew 2026-08-08: keep on both soles |
| Badge | Closed Sole (charcoal) | Approved product naming |
| Features head | Built around one obsession: *Grip.* | v19 spine |
| Disciplines | Upgrade your grip. Upgrade your workout. | Approved inventory |
| Split 1 | The sock era is over. | Approved inventory |
| Full-bleed | TRANSFORM YOUR PRACTICE | v19 lock (casing exception — flagged) |
| Sock math | One pair. Done. | Approved inventory |
| Commit | You commit to the class. Commit to the gear. | Approved inventory |
| Reviews | Real people. Real results. | Approved inventory |
| Statement | Think outside the sock! | Approved inventory |
| Sole FAQ | Closed Sole or Open Sole — which one? *(P-003 feel-and-coverage answer)* | P-003, verbatim |

## Copy set — Open Sole (`product.open-sole.json`)

**Owner letter 2026-08-08: no new slogans.** Every line below traces to the approved inventory in
`barreletics-brand-copy` / `barreletics-slogan-engine`, to `docs/09-PRODUCT-KNOWLEDGE.md` Product 2,
to the P-003 sole letter, or to the approved v19 spine. Nothing is invented.

| Slot | Copy | Source |
|---|---|---|
| Buy-box lede | Secure in every hold. / No sliding. No resets. | Approved inventory (Problem/Solution) — Andrew 2026-08-08: same lede on both soles |
| Buy-box body | Grippy shoes designed for Barre, Pilates, Reformer, Megaformer, Lagree, and Yoga. Built for breathability, natural toe splay, and secure grip with excellent stability. | 09-PK Product 2 description, verbatim fragment |
| Badge | Open Sole (rust) | Approved product naming + established badge convention |
| Features head | Built around one obsession: *Grip.* | v19 spine (product-general) |
| Features | Natural Toe Splay / Open-toe for natural balance and control · 360° Grip / Maximum control · Secure in Every Hold / No slipping. No resets. · Performs Under Sweat / Latex- & silicone-free. | Approved inventory (Performance, Open Sole) + 09-PK Product 2 bullet points + v19 |
| Disciplines | Upgrade your grip. Upgrade your workout. | Approved inventory |
| Split 1 | Feels like a *second skin.* / Ultra-light, flexible feel—more control than socks. The open-toe design mimics barefoot freedom while ensuring total control. | Approved inventory (Performance) — three verbatim lines |
| Variant grid | Shop all colors & styles *(default tab: open)* | Approved Home clarity keeper |
| Quote | "I am a full-time Barre instructor and teach on a variety of surfaces and mats — these provide the perfect level of grip and support and fit like a glove." — Laura P., Sacramento | Verbatim review, 09-PK Hero Quotes |
| Full-bleed | Finally secure. Stay focused. | Approved inventory (sentence-cased per casing law) |
| Sock math | One pair. No more socks. · ours = Barreletics Open Sole · 18+ month lifespan | Approved inventory (Value) + v19 |
| Commit | The cost of two classes. For every class after. | Approved inventory |
| Reviews | Real people. Real results. — Amy S. · Alexis G. · Jane R. · Jennifer K. · Dvorah S. · Dorothy | Approved inventory head; every review verbatim from 09-PK |
| Statement | Smarter than grip socks. | Approved inventory (Performance) |
| Sole FAQ | Open Sole or Closed Sole — which one? *(P-003 feel-and-coverage answer, Open listed first)* | P-003, verbatim |
| GEO Lagree | Super Lunges, Catfish, and Bear on the Megaformer — locked-in grip through holds, transitions, and balance. | Brand-copy cross-format phrases + approved inventory |
| GEO reformer | Elephant, knee stretches, and pikes — the long stretch series demands 360° grip. Locked-in through reformer footwork — no adjusting between sets. Barefoot feel with natural toe splay. | Brand-copy cross-format phrases + approved inventory |

### Open Sole imagery — all verified HTTP 200, all from the Open Sole product

| Slot | Asset |
|---|---|
| Split "second skin" | `Studio_TopBottom_Pink-1000x1000.jpg` — top and bottom, heel exposed |
| Lifestyle quote | `Blue__1_2490f04b….jpg` — exposed bottom and mid-foot breathing hole |
| Review rail | `Studio_TopBottom_Pink` · `studio-performance-skin-footwear.jpg` (yellow pair) · `Blue__1_` · `black_desktop_3.jpg` · `IMG_2917.jpg` (brand hero) · `barreletixxstefrunningpinkbackground.jpg` |
| Full-bleeds | `barreletixxjumpingtogether.jpg` (statement) · `Multi_Image.jpg` (media-only wow) |

**Admin issue found:** the Open Sole product in Shopify has
`Performance-Skin-Footwear-White_a7103efd….jpg` attached — and that photo is a **Closed Sole**
silhouette (heel and foot fully covered). It is excluded from every Open Sole slot here and from
the harness gallery, but it is still live on the product and should be removed or re-assigned in
Admin.

## Copy set — Outdoor

Source of record for this page is `docs/09-PRODUCT-KNOWLEDGE.md` → Product 3, plus the revised
2026-08-07 water-shoe description. No wet-surface grip promise appears anywhere on the page; the
approved caution ("Always check wet surfaces for slippage") does.

| Slot | Copy | Source |
|---|---|---|
| Buy-box lede | Perfect for / outdoor adventures. | Revised 2026-08-07 live description |
| Buy-box body | The closed sole provides grip, stability, and protection from hot sand. Ideal for paddleboarding, boating, beach, and resortwear. Always check wet surfaces for slippage. | Revised 2026-08-07 description, verbatim |
| Features head | Grip, support, and freedom—perfected for *every surface.* | Approved inventory (Performance) |
| Features | Grip, Stability, Protection · A Barrier Where It Matters · Doesn't Trap Sand or Water · Travel-Friendly | 09-PK Product 3 description + customer themes, verbatim fragments |
| Disciplines | Anywhere you'd go barefoot — but better. | 09-PK Product 3 "Great for" list, verbatim |
| Split 1 | A great alternative to *water shoes.* | 09-PK Product 3, verbatim |
| Variant grid | Shop all colors & styles / Ideal for paddleboarding, boating, beach, and resortwear. | Clarity keeper + revised description |
| Quote | "The Barreletics footwear is a genius product. It combines minimalist aesthetics, vibrant colors and functionality." — Luis D. | Verbatim review, 09-PK |
| Full-bleed | Perfect for outdoor adventures. | Revised 2026-08-07 description |
| Commit | Travel-friendly, zero maintenance — *rinse and go.* | 09-PK customer themes, verbatim |
| Reviews | Real people. Real results. | Approved inventory |
| Statement | Feels like a *second skin.* | Approved inventory |
| Guarantee 3rd point | Built to Last | v19 spine |
| Badge | Outdoor (blue) | 09-PK Product 3 collection tab |

### Slots deleted rather than invented

| Page | Slot | Why |
|---|---|---|
| Outdoor | whole `pdp-sock-math` section | The only approved cost/lifespan figures ($112–144/yr, 6–8 weeks, 18+ months) describe grip socks. No approved price or lifespan data exists for water shoes or flip flops, so every comparison figure in the previous version was invented. |
| Open Sole | FAQ "Why does full-bottom coverage matter?" | Removed earlier the same day: the answer rested on an invented "dead zone" mechanism claim. Coverage is already answered by the P-003 sole-choice FAQ directly above it. |

Section keys were renamed so the Theme Editor labels read honestly:
`fifty-fifty-one-pair` → `fifty-fifty-second-skin` (Open Sole), `fifty-fifty-barefoot` →
`fifty-fifty-water-shoes` (Outdoor). Rendered composition is unchanged; `build.py` dispatches on
section `type`, not key.

FAQ sets are per page: Open Sole leads with sole choice (P-003 wording, Open listed first), care,
sizing and reformer/Lagree GEO; Outdoor leads with what it's for, the water-shoe comparison, the
wet-surface caution and beach/boat/travel/outdoor-yoga GEO.

---

## Copy law compliance

Scanned clean for the banned pool vocabulary, invented scenery, retired offers and retired policy
framing across both new templates:

> pool · poolside · pool deck · water park · tidal pool · tidepool · spa visits · aqua barre ·
> water aerobics · rocky coves · shell-covered beaches · pebbly · 10% off · studio trial · over $75

The wet-surface caution is kept on the Outdoor page and names the **surface, not the venue**:

> "Certain wet tile and stone areas are inherently slippery for any footwear, as are wet polished
> marble and oiled or waxed floors."

---

## ⚠️ Things that need Andrew's call

**1. Both soles differentiate on feel + coverage, not a discipline split.**

The original brief described Open Sole as "barre, Pilates, yoga; the classic" and Closed Sole as
"reformer, Lagree, Megaformer." That is the exact split the 2026-08-02 letter retired —
`barreletics-brand-copy` records it as P-003/P-004 and lists "Open = yoga / Closed = reformer" as
copy anti-pattern #9, and `docs/09-PRODUCT-KNOWLEDGE.md` states both soles perform identically with
the same studio uses.

So each page differentiates on **coverage and feel** — the approved axis — and both keep the full
barre/Pilates/reformer/Lagree/Megaformer/yoga discipline set. If the discipline split has been
reinstated since August 2nd, say so and it is a fast edit to either template.

**2. The retired split is now fixed forward in `product.json` — as authorised.**

`collection-faq` blocks `f2` and `f6` carried *"Closed Sole: ideal for reformer and Megaformer…
Open Sole: preferred for barre and yoga."* Both now carry the P-003 wording verbatim. This was
inside the scope of Andrew's 2026-08-08 message (FAQ answers that name a sole) and is recorded in
**D-049**; nothing was rolled back to an older composition.

**2b. Two v19 items left alone that arguably want a letter.**

- `social-proof` → `r9` still reads *"Open Sole for mat, Closed for machines — same grip system,
  zero sock drawer"* on what is now the Closed Sole page. That is the retired split inside a review
  card; rewriting it would mean inventing a testimonial, so it was left and flagged.
- `collection-faq` → `geo-hot` still claims *"The patented grip surface performs better when warm."*
  The slogan engine lists heat-performance claims as never-generate. Product-general, part of the
  v19 lock, flagged not changed.

**3. Related, not fixed here:** the Outdoor product's **live Shopify** description and SEO tags still
contain banned pool language ("poolside activities", tags `grippy shoes for pools`, and the alt text
on two product images). That is an Admin fix, not a repo fix — flagged in the no-pool rule as still
outstanding.

**4. Sizing numbers conflict three ways.** `docs/09-PRODUCT-KNOWLEDGE.md` (sourced from
`manychat-kb/03-sizing-chart.md`) gives M = Women 5.5–7.5 and L = Women 7.5–11 / Men up to 10.5. The
locked v19 FAQ gives M = Women 5–7.5, Men 6–8 and L = Women 8–10, Men 8.5–11. **Live Shopify variant
labels** on both sole products read `M (W 5.5-7.5)` and `L (W 8-11)`. The variant templates use the
09-PK numbers; `product.json` keeps the v19 numbers untouched. Confirm which is right — one line
per page either way.

**4b. "Small coming soon" contradicts the product knowledge doc.** Both pages show S as *Coming
soon*, which comes from the v19 lock, the size-chart mock and the FAQ mocks. But
`docs/09-PRODUCT-KNOWLEDGE.md` Fit Notes and `docs/10-DECISIONS.md` both state *"No small size — the
material stretches and conforms to your foot."* This is not sole-specific either way, so it was left
as the v19 lock has it. Worth resolving in one place.

**5. Returns policy tension on Outdoor.** The internal returns note in
`docs/09-PRODUCT-KNOWLEDGE.md` requires returns be "clean, like new, **no outdoor wear**, no sole
damage." That reads oddly on a product sold for beach and boat use. The page uses the approved
public wording ("new, sellable condition") and does not repeat the outdoor-wear clause, but the
underlying policy may want a rewrite for this SKU.

---

## Imagery — what exists, what's still needed

Every image URL used is a real, live, verified-200 Shopify CDN asset.

**Outdoor product photography that exists** (all product-on-white, pulled from the live product):

- `A14_TopBottom_Yellow-600x600_15161205-…jpg`
- `A14_Front_3QT_Blue-600x600_1e8fd664-…jpg`
- `A14_TopBottom_LightGray-1000x1000.jpg`
- `A14_TopBottom_Blue-1000x1000.jpg`
- `A14_TopBottom_White-1000x1000_b72b34db-…jpg`

**Closed Sole photography that exists:** `Purple_45b2348c-…jpg`, `Outside_Black-600x600…jpg`,
`A14_TopBottom_Yellow-600x600.jpg`, `Rear_3QT_Blue-600x600.jpg`, `A14_TopBottom_Gray-1000x1000.jpg`.

**Open Sole photography that exists:** `Studio_TopBottom_Pink-1000x1000.jpg` (pink pair, top and
bottom), `black_desktop_3.jpg`, `Blue__1_2490f04b-…jpg`, `studio-performance-skin-footwear.jpg`
(yellow pair). A fifth image on the product, `Performance-Skin-Footwear-White_a7103efd-…jpg`, is a
**Closed Sole** silhouette mis-filed on the Open Sole product — excluded here, needs an Admin fix.

### Owner needs to supply — Outdoor lifestyle

There is **no outdoor lifestyle photography anywhere in the repo or on the product**. Rather than
put a barre-studio photo on a beach page, the two full-bleed slots are pointed at neutral existing
assets and marked in the Theme Editor `image_alt` field:

| Section | Setting | Current placeholder | What's needed |
|---|---|---|---|
| `fullbleed-statement` ("GRIP DOESN'T STOP AT THE DOOR") | `image_url` | `yellow_tone_mix.png` | Wide outdoor hero — beach, boat deck or paddleboard, feet in frame |
| `fullbleed-lifestyle` (media-only wow) | `image_url` | `A14_TopBottom_LightGray` | Full-bleed outdoor lifestyle — paddleboarding, beach or travel |

Both are exposed as normal Theme Editor image settings, so replacing them is a drag-and-drop with no
code change. Nice-to-have beyond that: a hot-sand detail shot and a wet-boat-deck grip shot for the
`fifty-fifty` slots, which currently use product-on-white.

**Neither sole page needs new photography** — full product photography exists for both, and the
studio lifestyle and video assets are shared. The Closed Sole page (the v19 spine) keeps its
existing brand-lifestyle imagery untouched.

### Reviews

There are **no verified outdoor testimonials**. Nothing was invented. The Outdoor review rail reuses
verified durability and grip reviews from the research bible and is framed as brand proof ("Four
years in. Same grip.") rather than as outdoor proof. Real beach/boat reviews would be a meaningful
upgrade to that section.

---

## Verification

`build.py` reads the three real templates, lifts the real `<style>` blocks from the matching
`sections/*.liquid`, and wraps them around static markup mirroring each section's Liquid output.
Stylesheets link live from `shopify-build/assets`, so a re-run always reflects the working tree.

```
python3 planning/pdp-variants-qa/build.py
```

Headless Chrome on macOS clamps windows to 500px, so true 390px comes from an iframe inside a wider
window — same technique as `planning/mobile-qa/mqa.py` and `planning/blog-about-type-qa/build.py`.

| File | What it is |
|---|---|
| `SIDE-BY-SIDE-1440px.png` | All three pages, desktop, side by side (Closed · Open · Outdoor) |
| `SIDE-BY-SIDE-390px.png` | All three pages, mobile, side by side |
| `closed-1440.png` / `open-1440.png` / `outdoor-1440.png` | Individual desktop captures |
| `closed-390.png` / `open-390.png` / `outdoor-390.png` | Individual mobile captures |
| `preview-*.html` | Live previews — open in a browser, re-render on reload |

Every preview carries a banner naming the sole **and** the template file it was built from, so
there is no ambiguity about which page is which after the 2026-08-08 swap:
`preview-closed.html` → `templates/product.json`, `preview-open.html` →
`templates/product.open-sole.json`.

A static server is running on port 8787 from the repo root:

- http://127.0.0.1:8787/planning/pdp-variants-qa/preview-closed.html
- http://127.0.0.1:8787/planning/pdp-variants-qa/preview-open.html
- http://127.0.0.1:8787/planning/pdp-variants-qa/preview-outdoor.html
- http://127.0.0.1:8787/planning/pdp-variants-qa/SIDE-BY-SIDE-1440px.png
- http://127.0.0.1:8787/planning/pdp-variants-qa/SIDE-BY-SIDE-390px.png

Every section renders for real — see the fidelity table at the top of this file. `qa-stub` no longer
appears in any generated preview.

**This is a local harness, not an approval surface.** Per the design-system rules, visual approval
happens on a Shopify draft preview. Nothing was pushed — say the word with theme ID `187144929571`
and these can go up for real review.

---

## 2026-08-08 — Small size retired, fifty-fifty media full-bleed

**Small removed** (Andrew: *"get rid of the small and small option for now we dont need it"*).
`show_soon_size` off and `size_soon_note` emptied on all three templates; the *"Small is coming
soon (planned ~Women 4–5 / Men 5–6)"* sentence deleted from the Closed and Open sizing FAQ answers,
leaving the rest of each answer untouched; and the `pdp-buy-box.liquid` **schema defaults** changed
to `false` / `""` plus the inline Liquid fallback removed, so it cannot reappear when the section is
added fresh. Outdoor already had it off. Sizing answers now describe only M and L.

**Fifty-fifty media** (Andrew: *"i dont want images inside the 50 50 section within the section full
50 images"*). Six slots were set to `media_fit: contain`, which insets the image to 72% width with
48px padding on a background — an image floating inside the column rather than filling it. All six
flipped to `cover`: Open Sole `fifty-fifty-lifestyle` + `fifty-fifty-second-skin`, Outdoor
`fifty-fifty-lifestyle` + `commit` + `numbers` + `water-shoes`. Closed Sole was already `cover`
throughout. `fifty-fifty.liquid` also gained an explicit rule stating that outside contain mode the
media has zero padding, zero margin and fills 100% × 100% of its column, so this cannot drift back.

Measured after the change, desktop and mobile: media column = exactly half the section, image =
exactly the media column, padding 0, radius 0, at 1440px and at a true 390px viewport.

**Not changed:** `index.json` → `fifty-fifty-one-pair` is the only other `contain` user in the repo
(homepage). It was left alone — the fix was applied as per-page template settings, not by changing
what `contain` means, so no other page is affected. `collection.json`, `collection.hot-kits.json`
and `page.about.json` all use `cover` already.

---

## Diagnosis — "the Open Sole page is underwhelming"

**It is photography, not copy or structure.** Both pages carry the same 17-section spine, the same
section types in the same order, zero empty settings and zero orphaned setting keys. Nothing was
hollowed out by the approved-sources copy rewrite. Two concrete gaps:

**1. The two slots that carry Open Sole's identity use catalogue shots, not lifestyle frames.**

| Slot | Closed Sole (v19 spine) | Open Sole |
|---|---|---|
| First editorial split | `barreletixxstefrunningpinkbackground.jpg` — real scene | `Studio_TopBottom_Pink` — product on white |
| Lifestyle split | `barreletixxjumpingtogether.jpg` — real scene | `Blue__1_…` — product on white |

Closed Sole uses brand lifestyle photography in every differentiating slot. Open Sole uses flat
top-and-bottom product shots in both. Now that the media is full-bleed this reads *worse*, not
better: a 1000×1000 product-on-white cropped into a tall half-column is mostly empty white with a
cropped shoe in it. Full-bleed was the right call — it just exposes the real problem.

**2. Social proof is thinner.** Closed Sole runs 9 photo review cards; Open Sole runs 6. Text
reviews match at 6 each. The FAQ count (13 vs 14) is *correct* — the removed row was the
"Why does full-bottom coverage matter?" answer, which rested on an invented mechanism claim.

**Root cause, and why it is not fixable from the repo:** the Open Sole product in Shopify has five
photographs and only four usable ones — all product-on-white. The fifth,
`Performance-Skin-Footwear-White_a7103efd…`, is a **Closed Sole** silhouette mis-filed on the Open
Sole product. **There is no Open-Sole lifestyle photography anywhere in the repo or on the product.**

**Recommendation — needs Andrew's call, nothing changed:**

1. **Shoot or supply two Open Sole lifestyle frames** for the two splits above. This is the only fix
   that actually closes the gap. Everything else is a workaround.
2. **Interim, sourceable today:** `barreletixxstefrunningpinkbackground.jpg`, `barreletixxjumpingtogether.jpg`
   and `Multi_Image.jpg` are product-general brand frames, not Closed-Sole-specific, and are already
   licensed and in use. One could be moved into the Open Sole editorial split. **Not done** — it
   would make the two pages look near-identical, which defeats the point of separate PDPs. Say the
   word if you want it anyway as a stopgap.
3. **Three more photo reviews** would bring Open to parity with Closed. The verified reviews exist in
   `docs/09-PRODUCT-KNOWLEDGE.md`, but they are the same reviews Closed already uses — duplicating
   them across both pages is a judgement call, not a copy fix. **Not done.**
4. **Admin fix, unrelated to the repo:** remove or re-assign the mis-filed Closed Sole photo on the
   Open Sole product.

## Also worth knowing — Outdoor is effectively out of stock

Live inventory shows **every Outdoor colour sold out except L / LightGrey**. The variant grid renders
that honestly now, so the Outdoor preview is a wall of "Sold Out" badges. That is real data, not a
harness artefact.

## Still unresolved — sizing ranges conflict (reported again, not touched)

`docs/09-PRODUCT-KNOWLEDGE.md` says **M = Women 5.5–7.5** and **L = Women 7.5–11 / Men up to 10.5**.
The locked v19 FAQ says **M = Women 5–7.5 / Men 6–8** and **L = Women 8–10 / Men 8.5–11**. Live
Shopify variant labels read `M (W 5.5-7.5)` and `L (W 8-11)` — a third answer. Each page still says
whatever it said before; only the Small sentence was deleted. **One line per page fixes it once you
say which is right.**

---

## 2026-08-08 (later) — Juicer verdict, section rhythm, cover-crop audit, shipping accordion

### 1. Juicer / Instagram — the templates are fine, the harness was lying

`home-juicer` is present on **all three** PDPs and the settings blocks are **byte-identical**:

```
eyebrow "Follow the movement" · title "@barreletics" · body "Real practitioners. Real studios.
Real grip." · feed_id barreletics · posts_per_page 12 · max_pages 1 · enable_see_more true ·
max_height 0 · cta "Follow on Instagram →" · profile_url instagram.com/barreletics · anchor instagram
```

Every value matches the frozen defaults in `specs/frozen/juicer.md`, and every key validates against
the `home-juicer` schema. **Nothing was wrong with the template, and nothing was changed in it.**

What Andrew saw was the harness. juicer.io injects the tiles at runtime, so a static file has none.
The previous stand-in was a 6-across grid of square product photos, which reads as a broken or
mis-configured feed rather than as a placeholder. It now draws the same **3-column mixed-ratio
mosaic** the v19 mock falls back to when the Juicer CDN is blocked, at the real `posts_per_page`
count, inside a dashed amber frame captioned *"Placeholder tiles — not the live Instagram feed"*,
with a note naming the feed, page count and See-more state. Judge the chrome and density; ignore the
pictures.

### 2. Section rhythm — standardised, and written into the design system

The full rule now lives in `docs/23-design-token-reference.md` → **Section rhythm — three tiers**.
Short version: content sections own `--section-padding-y`, the value strip owns `--gap-a`,
full-bleed statements own `0`, and `pdp-buy-box` is the hero exception. Every hardcoded vertical
section padding on the spine was replaced with a token.

Measured boundary-to-boundary ink gaps, 1440px (Closed Sole; Open and Outdoor identical apart from
the sections they omit):

| Boundary | Before | After |
|---|---|---|
| buy box → value strip | 82 | 72 |
| value strip → features | 116 | 84 |
| features → disciplines | **162** | 130 |
| disciplines → fifty-fifty | 81 | 129 |
| fifty-fifty → variant grid | 88 | 128 |
| variant grid → fifty-fifty | 91 | 128 |
| fifty-fifty → full-bleed TRANSFORM | **0** | **64** |
| full-bleed → sock math | 80 | 64 |
| sock math → full-bleed lifestyle | 121 | 64 |
| full-bleed lifestyle → fifty-fifty commit | **0** | **64** |
| fifty-fifty commit → reviews | 73 | 129 |
| reviews → Think outside the sock | 89 | 128 |
| fifty-fifty → guarantee band | 65 | 129 |
| guarantee → Juicer | 132 | 128 |
| Juicer → FAQ | 129 | 129 |

Before: sixteen boundaries, fifteen different values, spread 0–162. After: **128 / 64 / 0** plus the
buy-box hero pair, ±1–3px of border rounding. Mobile 390px collapses to **96 / 48 / 0** the same way.
The two 0px boundaries on Outdoor (`fullbleed-statement` → `fullbleed-lifestyle`) are band↔band and
are **left at 0 on purpose** — that is a deliberate photographic diptych, not a bug.

**Files touched:** `fifty-fifty` (rhythm band + text-column `calc()`), `pdp-features`, `disciplines`,
`variant-grid`, `pdp-sock-math`, `social-proof`, `guarantee-band`, `value-strip`. Not touched:
`home-juicer` and `faq-accordion` (already on tokens), `pdp-buy-box`, `fullbleed-statement`.

**Cross-page impact — reported, not separately reviewed.** These are shared library sections, so the
same rhythm now applies on `index.json` (homepage), every `collection.*.json`, and `page.about.json`.
That is the intent of a standard, but the homepage and collections have **not** been visually
re-reviewed here.

### 3. Cover-crop audit — every `cover` fifty-fifty on all three pages

`media_fit: cover` scales to fill and throws away the overflow, so a studio pack-shot with a thin
white margin loses its toes. Each image below was measured for real: natural size, the subject's own
margin to the frame, the rendered box, and the source pixels lost per edge.

| Page · slot | Image | Natural | Subject margin T/B | Crop @1440 | Crop @390 | Verdict | Fix |
|---|---|---|---|---|---|---|---|
| Outdoor · **water shoes** | `A14_TopBottom_Yellow-600x600` | 600×600 | 6.7% / 8.8% | 5.6% / 5.6% | **9% / 9% — CLIPPED** | Toes cut on mobile, 6px of air on desktop | focal 43%, mobile media 360 |
| Outdoor · commit | `A14_TopBottom_Blue-1000x1000` | 1000×1000 | 6.6% / 8.8% | 5.6% / 5.6% | **9% / 9% — CLIPPED** | Same failure | focal 43%, mobile media 360 |
| Outdoor · numbers | `A14_TopBottom_LightGray-1000x1000` | 1000×1000 | 6.6% / 8.8% | 5.6% / 5.6% | **9% / 9% — CLIPPED** | Same failure | focal 43%, mobile media 360 |
| Outdoor · lifestyle quote | `A14_Front_3QT_Blue-600x600` | 600×600 | 28% / 24% | 5.6% | 9% | Safe — generous margin | none |
| Open · second skin | `Studio_TopBottom_Pink-1000x1000` | 1000×1000 | 6.7% / 9.5% | 11.1% | **CLIPPED** | Toes cut | focal 41%, mobile media 360 |
| Open · lifestyle quote | `Blue__1_2490f04b…` | 530×530 | 8.7% / 7.0% | 11.1% | **CLIPPED** | Toes cut | focal 55%, mobile media 360 |
| Closed + Open · lifestyle & numbers | `barreletixxjumpingtogether` | 1400×1878 | photographic | 16.9% | 19.4% | **Shoes grazed the bottom edge** | focal 85% — keeps all four shoes, crops torsos instead |
| Closed · sock era | `barreletixxstefrunningpinkbackground` | 1200×1374 | photographic | 11.2% | 14.2% | Safe — head and shoe both in frame | none |
| Closed + Open · commit | `Multi_Image` | 1400×484 | photographic | 30.6% **each side** | 28.9% each side | **Poor** — a 2.9:1 banner in a near-square box; the outer shoes are sliced in half. Horizontal, so no focal value fixes it | **not changed — needs a different image or Andrew's call** |

The two Outdoor full-bleed slots were checked as asked. `IMG_5253` (dock, 960×951) upscales **1.5×**
into 1440×810 and loses 21.6% top and bottom; `49826062…` (surf, 772×959) upscales **1.87×** into
1440×900 and loses 24.8% top and bottom. In both cases the **product stays in frame and the crop
reads deliberately** — the coral shoe on the boat deck, the yellow pair on wet sand. They are soft at
desktop width because of the upscale. Left as-is; higher-resolution originals would help.

Before/after crops for every changed slot: `crop-audit/*-BEFORE-AFTER-390.png`.

**New Theme Editor control.** `fifty-fifty` had a nine-value *Image focal point* select, which can
only snap to an edge — useless when a crop is a few percent too deep at both top and bottom. It now
also offers **Custom (use the sliders below)** plus `focal_x` / `focal_y` percentage ranges. Default
is unchanged (`center` / 50 / 50), so no existing instance moved. Every fix above is a per-slot
Theme Editor setting, not hardcoded CSS.

### 4. Shipping in the accordion — already correct, on all three pages

| Page | Accordion set | `shipping_accordion` | `returns_accordion` | Shipping copy outside the accordion |
|---|---|---|---|---|
| Closed Sole | Description · Care & how to wear · Shipping · 30-day returns + 90-day warranty | 167 chars, identical | 102 chars, identical | value strip *"Free shipping over $150"* only |
| Open Sole | same four | identical | identical | same |
| Outdoor | same four | identical | identical | same |

There is **no loose shipping copy** in any buy box, and the three pages already matched each other
exactly — nothing needed consolidating. The approved trust model is intact: under-ATC empty
(`show_trust_row: false` on all three), the strip scan reads Made in USA · Free shipping over $150 ·
30-day returns · 90-day warranty, and the policy detail lives in the accordion.

What made it *look* wrong was the harness: it force-opened all four accordions, so the shipping and
returns policy text spilled into the buy box as a wall of loose copy — most obvious on Outdoor, whose
panel is shorter because the kit links are off. They now render closed, as the theme ships them.
**No copy was added, removed or reworded, and `pdp-buy-box.liquid` was not modified at all** — the
"Complete the kit" link fallbacks another agent is working on were left untouched.

### 5. Harness fidelity fixes (`build.py`) — measure the theme, not the harness

Four places where the preview did not match the sections it claims to mirror. Spacing QA off the old
harness would have been measuring the wrong page.

| What | Was | Now |
|---|---|---|
| `fifty-fifty` layout vars | Hardcoded `min-height 520`, `vertical-padding 72`, `contain-width 78%` | Read from the template with the Liquid's own defaults (640 / 88 / 72%) |
| Buy box + reviews padding | Hardcoded `48px 64px` / `72px 40px` | The real sections' tokens |
| `value-strip` | Desktop line only — the strip was **empty at 390px** | Both the full and mobile-subset lines |
| Buy-box accordions | Force-opened | Closed, as the theme renders them |

`measure.py` is new: it drives CDP with a real device-metrics override (macOS clamps headless windows
to 500px) and reports, per page and viewport, the ink gap at every section boundary plus a
cover-crop table for every `object-fit: cover` image. `measure-before.json` / `measure-after.json`
hold the raw numbers behind the tables above.

```
python3 planning/pdp-variants-qa/build.py       # previews + screenshots
python3 planning/pdp-variants-qa/measure.py --tag after
```

### Template hashes — section order proven unchanged

| Template | SHA-256 before | SHA-256 after | Order |
|---|---|---|---|
| `product.json` | `2fab77b4…3cebf6b` | `05e84980…08d7c564` | 17 keys, byte-identical sequence |
| `product.open-sole.json` | `9331cff0…86325c39d` | `cdd2b726…2a564ea04` | 17 keys, unchanged |
| `product.outdoor.json` | `5aa55f77…4c912fef081` | `aa02e89e…3d956c3a409` | 16 keys, unchanged |

Only `image_position` / `focal_x` / `focal_y` / `mobile_media_height` were added, inside existing
section `settings`. No section was added, removed or reordered on any page.
