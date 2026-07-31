# M4 Theme Editor Controls — Tiers & Schema Organization

**Status:** APPROVED 2026-07-30 (Andrew) · **Shared patterns + TE Q&A 2026-07-30**  
**Authority companion:** `planning/m4-section-library-CONTRACT.md` §7 · freeze rules §8  
**Type:** Type OS owns typography — **SETTLED** — **no** per-section `font_picker` sprawl (`planning/m4-type-hierarchy.md`)  
**Freeze registry:** `planning/m4-section-freeze.md` — **Footer A+ APPROVED / SETTLED** (sitewide; no brand blurb). Do not change frozen section structure without Andrew letter in-message.

---

## Font family policy (HARD)

| Control | Allowed? | Notes |
|---------|----------|-------|
| **Font family** (`font_picker`) | **NO** | Brand Type OS / theme font stays. Do **not** add per-section family pickers. |
| **Title size / Body size** | **YES** | Select with numeric px steps (see below). |
| **Title weight / Body weight** | **YES** | `default` · `400` · `500` · `600` · `700`. |
| **Heading level** (`h1`–`h6`) | **YES** | Must output the **real HTML tag**. Visual size is Title size — not heading level. |

**Schema info (copy):** “Family is brand Type OS — use Title size/weight to adjust.”

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
| `title_size` | select | `default` (= **Default / Type OS**) · `12` · `13` · `14` · `15` · `16` · `17` · `18` · `20` · `22` · `24` · `26` · `28` · `30` · `32` · `36` · `40` · `44` · `48` · `56` (+ `64` · `72` on hero/collab) |
| `body_size` | select | same mid-page list (through `56`) |
| `title_weight` / `body_weight` | select | `default` · `400` · `500` · `600` · `700` (optional) |
| `heading_level` | select | `h1`–`h6` — wire to real tags via `{% case %}` |

**Wire:** when value ≠ `default`, set a CSS custom property (e.g. `--ff-title-size: 32px`). When `default`, omit the var so Type OS / section baseline CSS wins.  
**Never** add `font_picker` (family).

Apply on: `fifty-fifty`, `split-hero`, `statement-band`, `fullbleed-statement`, `collab-hero`, `variant-grid` (content sizes only).  
Skip on `pdp-buy-box` — product title is Admin-owned; Type OS owns the H1.

---

## Shared pattern — section anchor dropdown (CTA / trust / tag links)

Shopify’s native `url` setting often **drops hash-only** values (`#variants`). Use a **select** of known homepage anchors + **Custom URL…** text field.

| Setting | Role |
|---------|------|
| `cta_link_target` (select) | Known anchors **or** `custom` |
| `cta_url` (text) | Used only when target = `custom` — full URL, relative path, or any `#hash` |
| Same pattern | `trust_link_target` + `trust_url` · `tag_link_target` + `tag_url` |

**Known homepage anchors (keep in sync with `templates/index.json` / section Anchor IDs):**

| Value | Section |
|-------|---------|
| `#variants` | `variant-grid` (Anchor ID default `variants`) |
| `#knock-socks` | `statement-band` |
| `#reviews` | `social-proof` (hardcoded `id="reviews"`) |
| `#guarantee` | `guarantee-band` |
| `#never-loses-grip` | fifty-fifty grip |
| `#one-pair` | fifty-fifty one-pair |
| `#coperni` | `collab-hero` |
| `#problem` | `problem-section` |

**Liquid resolve:** if target ≠ blank and ≠ `custom` → use target; else use text field; blank custom → section default (usually all-products).

**Schema info:** “Homepage section anchors jump on the same page. Choose Custom URL… for a full URL or any other #hash.”

---

## Shared pattern — CTA chrome (where CTAs are styled)

| Setting | Type | Notes |
|---------|------|-------|
| `cta_size` | select | Default / Type OS + small px list |
| `cta_style` | select | `solid` · `outline` |
| `cta_bg_color` | color | Solid fill |
| `cta_border_color` | color | Outline / border |

Wire via CSS vars on the section root.

---

## Shared pattern — media field meanings

Use the same labels + `info` copy wherever media applies. Fields are **not** redundant — keep Shopify video + URL pattern:

| Field | When to use |
|-------|-------------|
| **Shopify video** (`type: video`) | Preferred when the file lives in **Shopify Files**. Wins if both video fields are set. |
| **Video URL (mp4)** | External/CDN mp4 when **not** using Shopify Video. Ignored if Shopify video is set. Leave blank if unused. |
| **Image / poster (Shopify)** (`image_picker`) | Still image for image mode, **or** poster frame when using Video URL. Prefer over URL fields when the asset is in Shopify. |
| **Poster URL fallback** | Poster for Video URL **only** when Image / poster (Shopify) is empty. Not used for still-image mode. |
| **Image URL fallback** | Still image when **Shopify image picker is empty** and there is no video — CDN/external. **Leave blank** if Shopify image is set. **Not** a video poster. |

---

## Shared pattern — layout

| Control | Notes |
|---------|-------|
| **Media column %** | Range **35–65**; text = 100 − media. Default **50** on fifty-fifty; hero may default higher (e.g. 62 media-dominant). Desktop only. |
| **Media / section corner radius** | **One** range **0–24px** (step 2). Applies **equally to all four corners** (L/R linked). |
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
| **Gap below trust row** | range px | Space between trust row and heading |
| **Trust link** | anchor select + custom text | Same convention as CTA |

Wire via CSS vars on the section root (e.g. `--sh-star-color`, `--sh-star-size`, `--sh-trust-gap`, `--sh-trust-below`, `--sh-trust-size`).

`statement-band` (“Let us knock your socks off”) is **title-size**, not trust stars.

---

## Tag text (split-hero)

**Tag text** is a decorative line under the CTA (campaign hashtag look, e.g. `#letusknockyoursocksoff`).  
It is **not** this section’s Anchor ID. It only links if Tag link / custom URL is set (usually `#knock-socks`).

---

## Section aria-label

Accessibility name for **screen readers** — **not visible** on the page.  
Leave blank to fall back to the Heading (or a sensible section default).

---

## Detail upgrade targets

1. **`fifty-fifty`** — shared type + media clarity + media column % + radii + media fit + CTA chrome + anchors + heading level
2. **`split-hero`** — shared type/media/layout + **Section — trust** + CTA chrome + tag/trust anchors + heading h1–h6
3. **`statement-band`** — title size (statement line) + CTA anchors
4. **`variant-grid`** — Shared content sizes; Anchor ID `variants`; Section — tabs / see-all / links
5. **`pdp-buy-box`** — Shared content toggles; no title-size override (Admin title)
