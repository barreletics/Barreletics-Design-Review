# M4 Theme Editor Controls — Tiers & Schema Organization

**Status:** APPROVED 2026-07-30 (Andrew) · **Shared patterns extended 2026-07-30**  
**Authority companion:** `planning/m4-section-library-CONTRACT.md` §7  
**Type:** Type OS owns typography — **no** per-section `font_picker` sprawl (`planning/m4-type-hierarchy.md`)

---

## Tiers

| Tier | Role | Typical controls |
|------|------|------------------|
| **A — Marketing** | Mid-page / hero marketing blocks | Copy + image and/or video + basic layout (height, reverse, column %, focal, radius) |
| **B — Text band** | Typographic / CTA bands | Copy + CTA + title size override (no media block) |
| **C — Commerce (custom)** | Domain commerce modules | Product-driven core + TE extras (tabs/products, show/hide buy-box chrome, links) |

### Examples

| Section | Tier | Notes |
|---------|------|-------|
| `fifty-fifty`, `split-hero`, `fullbleed-statement`, `visual-mosaic`, `collab-hero`, `home-ugc` | **A** | Media + copy; shared type/media/layout blocks |
| `statement-band`, `disciplines`, `problem-section`, `guarantee-band`, `studio-trust` | **B** | Copy / CTA; omit Media; title size override when heading exists |
| `variant-grid`, `pdp-buy-box` | **C** | Domain controls under Section headers; variant-grid gets shared content sizes only |

---

## Schema organization (EVERY section — same order)

Use Shopify schema `header` settings. Same labels when the block applies. **Omit** fields that don’t apply — do not invent fake ones. **No font pickers.**

### Block 1 — Shared

1. **`Shared — Content`** — eyebrow, heading, body, CTA label, CTA link + **type overrides** (omit N/A)
2. **`Shared — Media`** — Shopify video / URL / image / poster (omit Tier B)
3. **`Shared — Layout`** — height, reverse, media column %, radius (omit if N/A)

### Block 2 — Section-specific (below Shared)

4. **`Section — …`** — custom controls only for that section  
   Examples: `Section — Fifty-fifty — media fit` · `Section — Split hero — trust` · `Section — Variant grid — tabs`

### Rules

- Shared blocks first, same order, consistent labels.
- Section-specific always **below** Shared.
- Multiple `Section —` headers OK when groups are distinct (tabs vs see-all vs links).
- Product Admin owns PDP gallery images and variant SKUs — TE may show/hide chrome and set URLs; do **not** fake a full image picker that fights product media.
- Sticky ATC stays in `pdp-sticky-atc`, not buy-box.

---

## Shared pattern — type size / weight overrides

**Keep heading register** (display / standard / hero class) from Type OS. Add optional numeric overrides only.

| Setting | Type | Values |
|---------|------|--------|
| `title_size` | select | `default` (= **Default / Type OS**) · `15` · `16` · `18` · `20` · `24` · `28` · `32` · `36` · `40` (+ larger steps on hero/statement: `44`–`72` as needed) |
| `body_size` | select | same mid-page list |
| `title_weight` / `body_weight` | select | `default` · `400` · `500` · `600` · `700` (optional) |

**Wire:** when value ≠ `default`, set a CSS custom property (e.g. `--ff-title-size: 32px`). When `default`, omit the var so Type OS / section baseline CSS wins.  
**Never** add `font_picker` (family).

Apply on: `fifty-fifty`, `split-hero`, `statement-band`, `fullbleed-statement`, `collab-hero`, `variant-grid` (content sizes only).  
Skip on `pdp-buy-box` — product title is Admin-owned; Type OS owns the H1.

---

## Shared pattern — media field meanings

Use the same labels + `info` copy wherever media applies. Fields are **not** redundant:

| Field | When to use |
|-------|-------------|
| **Shopify video** (`type: video`) | Preferred when the file lives in **Shopify Files**. Wins if both video fields are set. |
| **Video URL (mp4)** | External/CDN mp4 when **not** using Shopify Video. Ignored if Shopify video is set. |
| **Image / poster (Shopify)** (`image_picker`) | Still image for image mode, **or** poster frame when using Video URL. Prefer over URL fields when the asset is in Shopify. |
| **Poster URL fallback** | Poster for Video URL **only** when Image / poster (Shopify) is empty. Not used for still-image mode. |
| **Image URL fallback** | Still image when no Shopify image is set and there is no video. **Not** a video poster. |

---

## Shared pattern — CTA link

| Kind | Use |
|------|-----|
| Collection / product / page URL | Normal navigation |
| `#anchor` | Same-page jump to a section that has that **Anchor ID** (e.g. `#variants`, `#knock-socks`) |
| Blank | Section default — usually all-products collection (do **not** hard-default unexplained anchors in Liquid) |

Put intentional homepage anchors in `templates/index.json`, not as silent Liquid defaults.

---

## Shared pattern — layout

| Control | Notes |
|---------|-------|
| **Media column %** | Range **35–65**; text = 100 − media. Default **50** on fifty-fifty; hero may default higher (e.g. 62 media-dominant). Desktop only. |
| **Media / section corner radius** | Range **0–24px** (step 2). Apply via CSS vars. |
| Height / reverse / focal | Keep as today; section-specific framing stays under `Section — …` |

---

## Shared pattern — trust row (sections that show stars)

Only on sections that render stars / trust UI (today: **`split-hero`**; PDP rating row is product chrome, not this pattern).

| Control | Type | Notes |
|---------|------|-------|
| Show trust row / Show stars | checkbox | Existing |
| **Star color** | color | Default gold token `#d4af37` |
| **Star size** | range px | ~10–28 |
| **Trust text size** | select | Default / Type OS + small px list |
| **Trust row gap** | range px | Space between stars and text |

Wire via CSS vars on the section root (e.g. `--sh-star-color`, `--sh-star-size`, `--sh-trust-gap`, `--sh-trust-size`).

`statement-band` (“Let us knock your socks off”) is **title-size**, not trust stars.

---

## Detail upgrade targets

1. **`fifty-fifty`** — shared type + media clarity + media column % + radii + media fit (Section)
2. **`split-hero`** — shared type/media/layout + **Section — trust** (stars)
3. **`statement-band`** — title size (statement line)
4. **`variant-grid`** — Shared content sizes; Section — tabs / see-all / links
5. **`pdp-buy-box`** — Shared content toggles; no title-size override (Admin title)
