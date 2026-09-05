# Reviews → live Judge.me — QA evidence, 2026-08-08

Andrew, 2026-08-08: *"Live for everything. But you would have to force the first cards to be ones
with images and the text cards thereafter — unless we might need to manually add the photo cards?"*

Registry entry: `planning/m4-section-freeze.md` → **Reviews — LIVE Judge.me everywhere, 2026-08-08**.

## The photo-first answer

**Not manual.** Judge.me ships photo-first as a default sorting method, and the theme also enforces
it. Two layers:

1. **Judge.me admin (the one thing Andrew has to click).**
   Judge.me Admin → **Settings → Widgets → Review Widget → Search and pagination → Default sorting
   method → "Pictures First"**. This also governs the All Reviews page and the Floating Reviews Tab.
   Judge.me documents it as an Awesome-plan feature.
   The store is on `most-recent` today — read directly out of the `jdgmSettings` payload served on
   `barreletics.com`, which also carries `widget_sorting_pictures_first_text: "Pictures First"`, so
   the option is present in this install.
2. **Theme-side promotion (already on).** `pdp-reviews` moves reviews carrying photos to the top of
   whichever page Judge.me returned, so photo cards lead regardless of the admin setting or plan.
   TE toggle: **Photo reviews first**, default on. Pinned reviews are left where Judge.me put them,
   because pinning is a deliberate merchandising choice made in the admin.

Manual pinning therefore is **not** required. It stays available in the Judge.me admin if Andrew
ever wants a specific review nailed to the top.

## What the live store actually does — measured, not assumed

Captured from `https://barreletics.com/products/best-reformer-pilates-legree-workout-shoes`:

| Fact | Value |
|---|---|
| Judge.me installed | yes — Shopify app block, `<div id="judgeme_product_reviews" class="jdgm-widget jdgm-review-widget">` |
| Rendering | **server-side HTML**, review bodies present in the document (SEO-indexable) |
| Widget version | `3.0`, theme `leex` |
| Current sort | `default_sort_method: "most-recent"` |
| Pinning | supported — `jdgm-rev__pinned` present in the widget markup |
| Reviews with photos | present — `jdgm-rev__pics` |
| `judge.me/api/v1/reviews` without a token | **HTTP 401** `"Failed to authenticate"` |

That last row is why the old `pdp-reviews.liquid` never worked: it fetched the v1 API with no
`api_token`, so every load fell into the catch branch and printed "Reviews are temporarily
unavailable." The rewrite uses the tokenless metafields instead
(`product.metafields.judgeme.widget`, `shop.metafields.judgeme.all_reviews_page`).

## Curation — who picked the reviews, and were they the same everywhere

**Before: hand-picked by an agent, and largely the same handful repeated.**

| Surface | Shown | Authors |
|---|---|---|
| PDP Closed | 15 | Mia Evans, Gwen M., Dvorah S., **Lauren T., Hannah R., Priya K., Jordan P., Elena V., Chris N.**, Kimberly, Dvorah S., Myrna C., Barbara, Wendy B., Amy S. |
| Homepage | 9 | **the first 9 of the Closed PDP set, same order** — 6 fabricated |
| Collection | 3 | Gwen M., Lauren T., Dvorah S. |
| `/pages/reviews` | 3 | Mia Evans, Gwen M., Dvorah S. |
| PDP Open / Outdoor | 12 / 7 | genuinely different sets |

Dvorah S. appeared on 5 of 6 surfaces, Gwen M. on 4. Bolded names are the fabricated ones.

**After: nobody picks them — Judge.me serves them in its configured sort order.** The three PDPs
use product scope, so each shows its own product's reviews and they genuinely differ. Homepage,
collection, `/pages/reviews` and the Judge.me all-reviews page all use store scope, so they draw the
same store-wide pool in the same order — different from before, but still the same set as each
other until a curated carousel is added.

## Control available to Andrew

| Want | Where | Plan |
|---|---|---|
| Photo reviews first | Settings → Widgets → Review Widget → Search and pagination → Default sorting method → **Pictures First** | Awesome |
| Pin a review to the top | Reviews → pin (Review Widget only) | — |
| Hand-pick a set | Reviews → **Add tags → "Feature review"** | Free |
| A **different** curated set per page | custom tags + **Filter by tags** per Cards Carousel block, in the Shopify Theme Editor | Free |
| Hide from home, keep on PDP | Featured/tag-filtered carousel on home + review widget on PDP | Free |

Unpublishing a review removes it from **every** surface — there is no per-page hide. Per-page
curation needs the Judge.me **Cards Carousel** app block, configured per block in the Theme Editor;
app blocks cannot be wired from repo template JSON, so that step is Theme Editor work on Andrew's
word.

## Before / after

The swap is **not** visually neutral, so it is shown rather than assumed:

- `REVIEWS-BEFORE-AFTER-1440px.png` — PDP reviews slot
- `REVIEWS-BEFORE-AFTER-390px.png` — PDP reviews slot, mobile
- `HOME-REVIEWS-BEFORE-AFTER-1440px.png` — homepage reviews slot (`index.json`, store scope)

Left = curated `social-proof` (featured quote → 3 image cards → prev/next → text-card row, all
hand-authored in `product.json`). Right = `pdp-reviews` on live Judge.me; in a static file the
widget cannot fetch, so the labelled stand-in shows where it lands.

Pre-swap previews are preserved untouched in `before/` — they are a record, not a restore target.

## Rebuild

```
python3 planning/pdp-variants-qa/build.py     # full PDP previews (all three templates)
python3 planning/reviews-live-qa/compare.py   # PDP reviews-slot before/after
python3 planning/reviews-live-qa/home.py      # homepage reviews-slot before/after
```

## Fabricated content — removed, and proven gone

```
rg -c "Lauren T\.|Hannah R\.|Priya K\.|Jordan P\.|Elena V\.|Chris N\.|Sarah M\.|Attribution TBD|I will never go back" \
   shopify-build/ planning/pdp-variants-qa/preview-*.html
# ZERO matches
```

The Judge.me swap deleted the `social-proof` blocks wholesale, taking every fabricated review with
them. Two fragments lived outside those blocks and were removed separately on Andrew's 2026-08-08
letter: the `index.json` → `proof-numbers` → `n2` internal QA note, and the invented
`quote_author: "Sarah M."` on `product.json` → `fifty-fifty-lifestyle`. That quote's text could not
be found in the live Judge.me feed, so it now runs unattributed rather than under a substituted
name — Andrew should supply the real reviewer or drop it.

## Static previews and the third-party embed

Judge.me is a third-party embed, exactly like the Juicer feed, and cannot render inside a file on
disk. Both the section itself and the preview harness therefore draw a dashed, labelled stand-in
reading **"Placeholder — live Judge.me widget renders here"**, naming the metafield that fills it.
There are deliberately **no fake review cards** in the preview — inventing cards is precisely what
going live was meant to end. Verify with:

```
rg -c "Placeholder — live Judge.me widget renders here" planning/pdp-variants-qa/preview-*.html
```
