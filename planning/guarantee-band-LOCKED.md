# Guarantee band LOCKED 2026-09-11

Source of truth for `sections/guarantee-band.liquid` + template settings.
Cursor rule: `.cursor/rules/guarantee-band-LOCKED.mdc`

## Borders
- `.guarantee-section`: `border-top` and `border-bottom` both `1px solid #d6cfc0`
- Bottom border separates the band from Juicer (and anything below) on every page that uses the section
- Do not remove either border

## Type
- Section title: `title_role: display` on PDPs (`h2-display`)
- Column titles (`.guarantee-item h4`): `clamp(20px, 2.2vw, 26px)` / weight `500`
- Home pattern: loud section title + compact columns + short detail lines + one outline **See details →**

## PDP column copy
| Column | Detail |
| --- | --- |
| 30-Day Returns | Returned items must be clean, unworn, and in new, sellable condition. |
| 90-Day Warranty | Defects only — not wear or accidents. |
| Built to Last | Never loses grip. |

- Sub: `30-day returns for indoor try-on. 90-day warranty against manufacturing defects.`
- CTA: `See details →` → `/pages/help#returns` (outline)
- Hard eligibility rules live on Help/FAQ — not restriction-first in the band
- Reject: “try-on for fit”, “Not after…”, per-column See details, ~40px competing titles

## Home
- Keep 4-up trust set (Free Shipping / Made in USA stay)
- Shared Returns / Warranty titles use the same locked detail lines as PDPs

## Scope
Applies wherever `guarantee-band` is included: Home (`index.json`), `product.json`, open-sole, one-offs, Coperni, outdoor, in-studio.
