# Journal / blog hero gallery

**Date:** 2026-08-08 · **Purpose:** every Journal, blog-index and article hero that has
existed in this M4 repo, rendered and laid out side by side so the owner can point at
the one he remembers.

**Main deliverable:** `GALLERY-journal-heroes-1440.png` 
Mobile companion: `GALLERY-journal-heroes-390.png` 
Individual crops: `crops/` · render manifest: `manifest.json`

Read-and-render only. No mock file was edited, locked or otherwise. Nothing was
restored from an older commit into the working tree.

---

## The nine heroes, oldest to newest

| # | Version | Hero structure | Headline | What distinguishes it |
|---|---|---|---|---|
| 1 | **Legacy `Barreletics Blog.html`** — May 2026 handoff | Type-only centred masthead, then a horizontal **image-left / copy-right** featured card | "Notes from the studio." · **44 / 500** · lede 18/1.55 | The original blog index. Calm, small headline; the featured card carries the visual weight. Eyebrow "The journal" in accent. |
| 2 | **Legacy `Barreletics Article.html`** — May 2026 handoff | **Full-bleed background image**, ~700px tall, dark gradient bottom-up, all text **overlaid bottom-left**: category / read time / date, headline, dek, avatar byline | "How to wash your performance skins." · **72 / 400** · dek 22/1.45 | The only true full-bleed image hero in the whole set. Editorial, magazine-cover feel. Very likely the "nice hero section" being remembered. |
| 3 | **Journal Definitive-v1** | Centred masthead + **topic filter row** (All · Care · Founder · Movement · Story · Wellness) + hairline rule + featured card | "From the studio" · **46 / 400** (clamp 34–46) · lede 17/1.45 | First Journal proper. Adds the topic nav and the hairline that separates masthead from feed. Lighter, more restrained than the legacy blog. |
| 4 | **Journal Definitive-v2 / v3** | Identical to v1 | "From the studio" · **46 / 400** | Hero renders **pixel-identical between v2 and v3** — only the lede copy changed from v1. v3's additions (GEO block, FAQ) are all below the fold. |
| 5 | **Journal Definitive-v4** | Identical structure to v2/v3 | "From the studio" · **46 / 400** | Unified FAQ (machines + hot thin sock) merged below the fold. Hero untouched. First Journal published to `docs/`. |
| 6 | **Journal Definitive-v5** — hub **Locked** | Same structure, much bigger type | "From the **S**tudio" · **72 / 700**, lh 1.06, ls −0.028em · lede 17/1.60 | The Type OS pass (SETTLED 2026-07-29). Headline jumps 46→72 and 400→700, and the title switches to title case. This is the current hub authority. |
| 7 | **Journal Definitive-v6** | Hero unchanged from v5 | "From the Studio" · **72 / 700** | Footer copy fix only (light Join the list). Listed on the hub as a promotion candidate; the hero is byte-for-byte v5. |
| 8 | **`blog-listing.liquid`** — shipping | Centred **type-only** masthead, no featured card, straight into a 3-up card grid | "The Barreletics Journal" · **72 / 700** · subtitle 17/1.60 | What actually ships. No hero image, no topic filter, no featured post — the masthead is pure type sitting on white above the grid. |
| 9 | **`article-content.liquid`** — shipping | Centred **type-only** title + byline, hero image below as a **contained, rounded block** | "Why grip socks stop gripping" · **72 / 700** | The image is demoted from full-bleed backdrop (v2 above) to a boxed illustration under the title. This is the biggest regression from the May mocks. |

---

## Reading the gallery

- **Only two of the nine use an image as the hero itself**: #2 (full-bleed, text
  overlaid) and, loosely, #9 (contained block below the title). Everything else is a
  type masthead with the imagery starting underneath.
- **The Journal line (v1 → v6) never changed structure** — masthead, topic filter,
  hairline, featured card. The only thing that moved across five versions is the
  headline: 46/400 → 72/700 at the Type OS pass.
- **The shipping implementation dropped two things** the mocks all had: the topic
  filter row and the featured-post card. `blog-listing.liquid` goes masthead →
  3-up grid with nothing in between.

## Recommendation

**#2 — the legacy `Barreletics Article.html` full-bleed hero — is the strongest**, and
it is almost certainly the one being remembered. It is the only treatment that gets
the product imagery working as the page's opening statement instead of as an
illustration below a heading, and the 72/400 headline over a gradient reads far more
like a brand than 72/700 on white does. It also solves the article template's real
problem: right now a reader lands on centred black text with no image above the fold.

Two caveats if it gets rebuilt:

1. **Contrast.** In the render, "How to wash your performance skins." sits over the
   pale mid-section of the product shot and the white text nearly disappears. The
   gradient starts at 30% and only reaches 0.55 opacity — it needs to be stronger, or
   the copy needs a scrim behind it.
2. **Type OS.** The mock's 72/**400** predates the settled hero token (72/**700**).
   Rebuilding at 700 will read heavier than the screenshot; worth showing both.

The realistic best outcome is a **merge, not a swap**: keep the current layout he
already approved, and give the Journal index back its **featured card** (#1/#3–#7) and
the article template a **full-bleed hero** (#2).

---

## Method

`shoot.py` drives headless Chrome over CDP: `Emulation.setDeviceMetricsOverride` for a
real viewport at any width (headless Chrome on macOS clamps windows to 500px, so
`--window-size=390` silently renders at 500), then `Page.captureScreenshot` with a clip
from the top of the page to the bottom of the hero element plus 28px. `compose.py`
stacks the crops with Pillow.

```
python3 planning/journal-hero-gallery/shoot.py      # crops/ + manifest.json
python3 planning/journal-hero-gallery/compose.py    # GALLERY-*.png
```

### Notes on the renders

- **No broken images.** Every crop loaded all of its remote CDN artwork —
  `manifest.json` records `brokenImages: []` for all sixteen renders. Nothing blank in
  these images is a loading failure.
- **Mock scaffolding hidden.** The May 2026 handoff files carry a `.pg-tab-strip`
  version switcher and the Journal mocks carry a `.mock-banner` note, both above the
  design. Both are hidden with injected CSS at render time so the crops start on real
  page chrome. The target files are never written to.
- **#8 and #9 have no site header** and use flat placeholder blocks where photography
  goes. They are rendered from `planning/blog-about-type-qa/preview-{blog,article}.html`,
  a harness that lifts the real `<style>` block out of each `.liquid` section — the
  sections cannot be opened in a browser directly. Type and layout are accurate; the
  grey rectangles are the harness, not a design choice.
- **Journal v1, v2, v3 were deleted from the working tree.** They survive only in git at
  `8719617` under `barreletics-design-review/design_handoff_barreletics 2/pages/`. They
  are extracted read-only into `sources/` for rendering — nothing was restored over a
  working-tree file.
- **Legacy `Barreletics Blog.html` exists in six copies** across
  `barreletics-design-review/{project,Barreletics Design Review}/versions/*`. The heroes
  are identical; the only difference is that the 2026-05-24 copy lacks the breadcrumb
  above the masthead. The final handoff copy is the one rendered.
- **`Barreletics Journal - Compare-Blog-v2.html`** (also git-only) is a two-pane iframe
  comparison harness, not a design. Extracted to `sources/` for the record, not rendered.
- **Mobile at 390px** is rendered only where the hero differs meaningfully: #1, #2, #6,
  #7, #8, #9. v1–v4 mobile is the same layout as v5 with a 32px headline instead of the
  Type OS clamp.

### Files

```
GALLERY-journal-heroes-1440.png   main deliverable
GALLERY-journal-heroes-390.png    mobile companion
crops/                            individual hero crops, 1440 + 390
sources/                          git-only Journal v1/v2/v3 + compare harness (read-only)
manifest.json                     per-render source path, crop height, broken-image check
shoot.py / compose.py             regenerate
```
