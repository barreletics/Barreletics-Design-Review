# Journal index QA — 2026-08-08

Bringing the shipping Journal index (`shopify-build/sections/blog-listing.liquid`)
back in line with the approved mock, `docs/Barreletics Journal - Definitive-v6.html`.

The shipping section went masthead → 3-up grid. The mock has two things in
between that had been dropped: a **topic filter row** and a **featured article
card**. Both are now real, merchant-controlled Shopify features.

## Files

| File | What it is |
|---|---|
| `shoot.py` | Builds the previews and shoots every frame below |
| `preview-before.html` / `preview-after.html` | Section CSS lifted live out of `blog-listing.liquid`, wrapped around markup mirroring the Liquid output |
| `before-1440px.png` · `before-390px.png` | What shipped |
| `after-1440px.png` · `after-390px.png` | What ships now |
| `mock-1440px.png` · `mock-390px.png` | The `.journal-index` band of the v6 mock, cropped |
| `COMPARE-1440px.png` · `COMPARE-390px.png` | Mock ǀ after, side by side |
| `manifest.json` | Per-frame crop heights and broken-image report |

Re-run after any edit to the section — the previews link `design-tokens.css` and
`barreletics-base.css` live and re-lift the section's `<style>` block each time:

```
python3 planning/journal-index-qa/shoot.py
```

`--build-only` writes the HTML without shooting. Needs network: the harness uses
the same barreletics.com CDN images as the mock, so the side-by-side compares
design rather than stand-in art.

## Method

The section is Liquid, so it cannot be opened in a browser. `shoot.py` lifts the
real `<style>` block out of `blog-listing.liquid` and wraps it around static
markup that mirrors the Liquid output, using the masthead copy from
`templates/blog.json` and the article set from the v6 mock. Same lift technique
as `planning/blog-about-type-qa/build.py`.

Headless Chrome on macOS clamps windows to a 500px minimum, so 390px comes from
`Emulation.setDeviceMetricsOverride` over CDP rather than `--window-size`
(same as `planning/journal-hero-gallery/shoot.py`). `captureBeyondViewport`
never scrolls, so lazy card images are promoted to eager and decoded before the
clip is taken, otherwise the bottom row shoots as empty boxes.

The mock is read-only. Its review banner is hidden with injected CSS at render
time; the file itself is never written to.

## Known deltas from the mock

Type OS wins wherever it disagrees with the mock's hand-authored CSS
(`planning/m4-type-hierarchy.md` + `assets/design-tokens.css` are settled).

| Element | Mock | Shipping | Why |
|---|---|---|---|
| Topic labels | 11 / 500 / 0.12em | 11 / **600** / **0.08em** | Type OS label role |
| Topic links on mobile | ~18px tall | 44px tap target | WCAG 2.1 §2.5.5; keeps the row a real touch target |
| Featured dek leading | 1.55 | **1.72** | Type OS body leading |
| Featured button | 12 / 700 / 0.1em, 48px | `.btn .btn--primary` — 15 / 500 / 0.12em, 44px | Global CTA token; hover to rust matches |
| Grid cards | Borderless, meta above title, `TAG · N MIN` | Bordered card, tag badge on the image, author + date | Untouched — this is the Type OS pass from earlier today, out of scope here |
| Pagination | Numbered pager `1 2 3 →` | `Page 1 of 2` + Prev/Next | Pre-existing; not part of this work |
| Featured media | Can be `<video>` (`data-media-type`) | Image only | Shopify's `article` object exposes no video field. Would need a metafield or a separate section setting. |
| Masthead lede | Capped at 38ch, wraps to 3 lines | Full container width | The masthead is approved and out of scope — left alone |

Featured meta reads `CARE · FEATURED · 3 MIN` from live article data: first tag,
the merchant's "Featured" label, and a read time derived from the body at 200
wpm (rounded up, floor of 1). No read-time metafield exists on articles —
`article-content.liquid` renders none either.
