# What Cursor changed on draft M4 QA (187144929571)

**Not Grok’s 50/50 sections.** Those are `sections/fifty-fifty*.liquid` + Theme settings → Split images. Cursor did **not** change global 50/50 phone height.

**Preview rule:** Use `barreletics.myshopify.com` + `?preview_theme_id=187144929571` while logged into Shopify Admin (barreletics.com often strips the param).

**Theme editor (draft):** https://admin.shopify.com/store/barreletics/themes/187144929571/editor

---

## PDP — “Gallery” + “Thumbnails” (P7 + P8) ← overlaps file with Grok, not same code

**What you see:** Product page left column — **big square hero image** + **row of small square images** under it.

**File:** `shopify-build/sections/pdp-buy-box.liquid` (only `.pdp-gallery__hero` + `.pdp-gallery__thumb` markup/CSS)

**What Cursor changed:** `<img>` → `{% render 'media-img' %}` (same layout; Grok’s sizes/kit/copy/swatches untouched)

| Preview link |
|--------------|
| [Closed Sole PDP](https://barreletics.myshopify.com/products/best-reformer-pilates-legree-workout-shoes?preview_theme_id=187144929571) |
| [Open Sole PDP](https://barreletics.myshopify.com/products/best-reformer-pilates-legree-workout-shoes-open-sole?preview_theme_id=187144929571) |

**Mockup label on page:**

```
┌─────────────────────┐  │  Title, price, swatches  │
│   BIG HERO IMAGE    │  │  (Grok’s PDP work)       │
│   (P8 Cursor)       │  │                          │
├─ thumb thumb thumb ─┤  │  Add to cart             │
   (P7 Cursor)         │                          │
```

---

## Reviews — “Photo cards” (P6)

**What you see:** In **Reviews** section — hand-picked blocks with **customer photo on top**, quote underneath (Theme Editor `photo_review` blocks). **Not** the text-only “Real people” row. **Not** 50/50.

**File:** `shopify-build/sections/pdp-reviews.liquid` (photo grid only)

| Preview link |
|--------------|
| [PDP → #reviews](https://barreletics.myshopify.com/products/best-reformer-pilates-legree-workout-shoes?preview_theme_id=187144929571#reviews) |
| [Home → reviews band](https://barreletics.myshopify.com/?preview_theme_id=187144929571#reviews) (photo cards only if section has `photo_review` blocks enabled) |

---

## Home — variant grid (P2)

**What you see:** “Shop all colors & styles” — color cards with Quick Add.

**File:** `shopify-build/snippets/variant-card.liquid`

| Preview link |
|--------------|
| [Home — scroll to Shop all colors](https://barreletics.myshopify.com/?preview_theme_id=187144929571) |

---

## Search / collection product cards (P1)

**File:** `shopify-build/snippets/product-card.liquid`

| Preview link |
|--------------|
| [Search “grip”](https://barreletics.myshopify.com/search?q=grip&preview_theme_id=187144929571) |

---

## Other Cursor work (same draft, not PDP gallery)

| Area | File | Link |
|------|------|------|
| Mosaic phone scroll | `sections/visual-mosaic.liquid` | [Home](https://barreletics.myshopify.com/?preview_theme_id=187144929571) |
| Blog INTERNI contain | `sections/blog-listing.liquid` | [Journal](https://barreletics.myshopify.com/blogs/journal?preview_theme_id=187144929571) |
| Sock math phone | `sections/pdp-sock-math.liquid` | PDPs that include section |
| Cart / sticky bar | **No code change** — named exceptions in `.cursor/rules/barreletics-media.mdc` only |

---

## Grok lane (Cursor did NOT edit for 50/50 global height)

- `sections/fifty-fifty*.liquid`, `config/settings_schema.json` (split media height)
- `templates/*.json` (Theme Editor JSON)
- Most of `pdp-buy-box.liquid` **except** gallery block above

---

## Revert?

If PDP gallery + review photo cards should be Grok-only again: say **revert P6 P7 P8 on draft** — restores those two section files to pre–media-img commits; Grok PDP logic stays.
