# One-off colors — surfaces (OS how-to)

**OS homes:** `docs/10-DECISIONS.md` **P-011** · `planning/10-decision-log.md` **D-051** · `docs/08-theme-settings-reference.md` · `docs/09-PRODUCT-KNOWLEDGE.md` · `planning/page-template-registry.md` · PDP **05** note below.

## Gate (Theme settings)

**Theme settings → One-off colors → product picker**

| Picker | Surfaces |
|---|---|
| Set | Nav under Grippy · quiet PDP link under ATC · All Variants One-Offs tab |
| Empty | All three hide |

Theme setting **wins** over section `product_oneoffs` when set. Do **not** add One-off colors in Online Store → Navigation.

## Products + templates

| Product | Handle | Admin theme template | Repo |
|---|---|---|---|
| One Off Colors (Closed Sole) | `one-off-colors-closed-sole` | `one-off-closed` | `product.one-off-closed.json` |
| One Off Colors (Open Sole) | `one-off-colors-open-sole` | `one-off-open` | `product.one-off-open.json` |

## Buy box (one-off PDPs)

- Color pickers = **shoe photos** (variant media), not File-cabinet circles  
- **Hide sold-out** colors/sizes  
- Option 1 may be misnamed (e.g. “Grey Swirl”); code treats position 1 as color on one-offs  
- Quiet link hidden on the one-off PDP itself  

## All Variants → One-Offs tab

- **Available now** then **Earlier one-offs** (sold out)  
- Starts at **2 rows**; **See more** adds one row at a time  

## Lean PDP spine (cold traffic)

Keep brand for strangers; drop Closed Sole sock-era stack:

`pdp-buy-box` → `value-strip` → `pdp-features` → `variant-grid` → `reviews` → `guarantee-band` → `home-juicer` → `collection-faq` → `pdp-sticky-atc`

## QA (M4 only)

Theme Editor: `187144929571` · previewPath product handles above. Live stays untouched until Brian pulls + Theme settings set on live.
