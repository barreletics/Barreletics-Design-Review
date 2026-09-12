# Implementation Map — Collections

## Reuse
| File | Role |
|------|------|
| `sections/collection-hero.liquid` | Shop-first H1 + sole cards |
| `sections/value-strip.liquid` | Trust |
| `sections/variant-grid.liquid` | Grid |
| `sections/disciplines.liquid` | Proof |
| `sections/fifty-fifty.liquid` | Education |
| `sections/social-proof.liquid` | Reviews band (DP-05) |
| `sections/geo-section.liquid` | GEO |
| `snippets/faq-accordion.liquid` | FAQ pattern |

## Modify
| File | Change |
|------|--------|
| `templates/collection.json` | Reviews + FAQ + GEO; shop-first copy; FAQ = Product FAQ |
| `sections/collection-hero.liquid` | Shop-first H1 setting; Pick-this-if; clickable sole cards |
| `snippets/product-card.liquid` | Value line + Quick Add — $74 |

## New
| File | Role |
|------|------|
| `sections/collection-faq.liquid` | Collection FAQ + schema (DP-06) |

## Dependencies
- Grippy-shoes collection products
- Compare page URL for chooser links

## Technical risks
- `collection.description` may override JSON body — set Admin description or force settings
- FAQ schema duplication if also on PDP — keep collection FAQ abbreviated

## Recommended order
1. Hero copy/settings (DP-04)
2. Add reviews band to JSON
3. Build `collection-faq`
4. QA sole cards + grid
