# SEO v37 — Juicer section QA (2026-08-08)

Page: `docs/Barreletics SEO - Best Grippy Socks - Definitive-v37.html` 
Served at `http://localhost:8787/docs/Barreletics%20SEO%20-%20Best%20Grippy%20Socks%20-%20Definitive-v37.html`

## What changed

The Instagram slot on v37 was **not the Juicer section**. It was a one-off
`ig-section` block invented for this page:

- heading `Studio workouts and footwear will never be the same` (a slogan that
  exists nowhere in the production section)
- `@barreletics` demoted to a small grey sub-line under it
- no eyebrow, no body line, no See more control
- a hand-built 4×2 grid of **8 square tiles** filled with Shopify product/CDN
  photography — product shots, not community posts
- cream `#f5f2ec` background with its own border-top, 88px/72px padding

It is now the real section, matching `shopify-build/sections/home-juicer.liquid`
and the way PDP v19 (`docs/Barreletics PDP - Definitive-v19.html`, hub-locked)
renders it:

- eyebrow `Follow the movement`
- h2 `@barreletics`
- body `Real practitioners. Real studios. Real grip.`
- the live `juicer.io/barreletics` embed, `data-per=12` · `data-pages=1`
- `See more` on-page control; `Follow on Instagram →` as the quiet secondary link
- the v19 blocked-feed fallback mosaic (9 real Juicer media tiles, 3 columns,
  mixed aspect ratios) for when the CDN cannot be reached
- white background, `64px 40px` desktop / `48px 16px` mobile per the design
  system spacing spec
- title on the page's own Type OS tokens — `--fs-h2-standard` /
  `--fw-h2-standard`, which resolve to the same 32px/600 v19 hardcodes

Copy is taken verbatim from `home-juicer.liquid` schema defaults and the
`index.json` / `product.json` settings. Nothing new was written.

## Results

| | 1440px | 390px |
|---|---|---|
| Section found | yes | yes |
| Live Juicer feed resolved | yes (`is-juicer-live`) | yes (`is-juicer-live`) |
| Live tiles rendered | 15 | 13 |
| Padding | `64px 40px` | `48px 16px` |
| Heading size / weight | 32px / 600 | 24px / 600 |
| Background | `#ffffff` | `#ffffff` |
| Horizontal overflow | none | none |
| Broken images (of 63) | 0 | 0 |

- `juicer-1440px.png` · `juicer-390px.png` — the section, clipped to its own box
- `audit.json` — full measurement dump for both widths
- Every image URL on the page returns HTTP 200 (verified with curl, including
  the nine juicer.io fallback media and the review-carousel URLs built in JS)
- HTML re-parsed after the edit: no unclosed or stray tags

## How to reproduce

```
python3 planning/seo-v37-qa/shoot.py
```

Headless Chrome on macOS clamps windows to ~500px wide, and this page has
vh-sized sections, so neither `--window-size=390` nor a tall iframe gives an
honest mobile render. `shoot.py` drives Chrome over CDP instead:
`Emulation.setDeviceMetricsOverride` pins a true 390×844 mobile viewport, and
`Page.captureScreenshot` clips to the measured section box with
`captureBeyondViewport`.

## Not touched

The v37 hero, the "ships in one to two days" band and the "One pair. Done."
section are all unchanged — see `planning/seo-v37-hero-earmark.md`.
