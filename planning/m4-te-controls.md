# M4 Theme Editor Controls — Tiers & Schema Organization

**Status:** APPROVED 2026-07-30 (Andrew)  
**Authority companion:** `planning/m4-section-library-CONTRACT.md` §7  
**Type:** Type OS owns typography — **no** per-section `font_picker` sprawl (`planning/m4-type-hierarchy.md`)

---

## Tiers

| Tier | Role | Typical controls |
|------|------|------------------|
| **A — Marketing** | Mid-page / hero marketing blocks | Copy + image and/or video + basic layout (height, reverse, ratio, focal) |
| **B — Text band** | Typographic / CTA bands | Copy + CTA only (no media block) |
| **C — Commerce (custom)** | Domain commerce modules | Product-driven core + TE extras (tabs/products, show/hide buy-box chrome, links) |

### Examples

| Section | Tier | Notes |
|---------|------|-------|
| `fifty-fifty`, `split-hero`, `fullbleed-statement`, `visual-mosaic`, `collab-hero`, `home-ugc` | **A** | Media + copy; detailed framing on 50/50 |
| `statement-band`, `disciplines`, `problem-section`, `guarantee-band`, `studio-trust` | **B** | Copy / CTA; omit Media |
| `variant-grid`, `pdp-buy-box` | **C** | Domain controls under Section headers; gallery/variants stay product-driven on PDP |

---

## Schema organization (EVERY section — same order)

Use Shopify schema `header` settings. Same labels when the block applies. **Omit** fields that don’t apply — do not invent fake ones. **No font pickers.**

### Block 1 — Shared

1. **`Shared — Content`** — eyebrow, heading, body, CTA label, CTA link (omit N/A)
2. **`Shared — Media`** — image, video, poster (omit Tier B)
3. **`Shared — Layout`** — height, reverse, ratio, alignment basics (omit if N/A)

### Block 2 — Section-specific (below Shared)

4. **`Section — …`** — custom controls only for that section  
   Examples: `Section — Fifty-fifty — media fit` · `Section — Variant grid — tabs` · `Section — PDP buy box — quotes & display`

### Rules

- Shared blocks first, same order, consistent labels.
- Section-specific always **below** Shared.
- Multiple `Section —` headers OK when groups are distinct (tabs vs see-all vs links).
- Product Admin owns PDP gallery images and variant SKUs — TE may show/hide chrome and set URLs; do **not** fake a full image picker that fights product media.
- Sticky ATC stays in `pdp-sticky-atc`, not buy-box.

---

## Detail upgrade targets (Tier A/C)

Approved for richer TE (still Type OS for type):

1. **`fifty-fifty`** — height, ratio, focal/scale, contain width, video URL, reverse, colors already present; Shared → Section — media fit
2. **`variant-grid`** — Shared content first; Section — tabs / see-all / PDP mode / links (Open/Closed/One-Offs/Outdoor stay complete)
3. **`pdp-buy-box`** — Shared info + display toggles (trust/rating, size chart, payment line, micro-quotes, thumb count); gallery from product Admin
