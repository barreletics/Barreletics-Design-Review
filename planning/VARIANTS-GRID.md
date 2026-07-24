# Variants Grid — Universal Rule

**Updated:** 2026-07-24  
**Applies to:** any page with `.variants-section` / `.var-grid`  
**Mocks locked:** SEO `Definitive-v29` · Home `Definitive-WORKING` · Collection `Definitive-v17`

## Page status

| Page | Authority mock | 2-row + See all |
|------|----------------|-----------------|
| Home | `Definitive-WORKING` | **Yes** |
| Collection | `Definitive-v17` | **Yes** |
| SEO Best Grippy Socks | `Definitive-v29` | **Yes** |
| PDP | `Definitive-v15` | **No** — full grid still |
| Journal shop strip | `Definitive-v4` | **No** — full strip still |

Bring PDP + Journal onto this rule before theme build if those grids ship.

## Defaults (all pages)

| Setting | Default | Notes |
|---------|---------|--------|
| `data-initial-rows` | `2` | Visible rows before See all |
| `data-see-all` | `expand` | `expand` = same-page reveal · `link` = go to Collection · `off` = show full grid |
| Columns | 4 desktop / 2 ≤1024px | Visible count = rows × cols (8 / 4) |
| Card chrome | No sole-type image badges | Size / Limited Edition / Sold Out only |
| Tabs | Page-owned | Studio pages: All · Closed · Open (Outdoor separate; One-Offs optional) |

## Markup

```html
<section
  class="variants-section"
  id="shop"
  data-variants-collapse
  data-initial-rows="2"
  data-see-all="expand"
  data-variants-expanded="false"
>
  <!-- head + toolbar + .var-grid(s) -->
  <div class="variants-see-all">
    <button type="button" class="variants-see-all__btn" data-variants-see-all aria-expanded="false">
      See all colors &amp; styles
    </button>
  </div>
</section>
```

Per-page overrides: change `data-initial-rows` / `data-see-all` only — do not fork card CSS.

## Theme (Liquid) mapping

- Section setting `initial_rows` (range 1–6, default 2)
- Section setting `see_all` (expand | link | off)
- `link` → `see_all_url` (default collection URL)

## Conversion note

Default **2 rows + expand** shortens the packshot wall and keeps proof in reach; inventory stays one click away without leaving the page (SEO/Home). Collection may set `initial_rows: 3` or `see_all: off` if browse-depth is the job.
