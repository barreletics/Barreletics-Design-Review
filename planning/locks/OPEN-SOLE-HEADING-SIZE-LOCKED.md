# Open Sole section headings LOCKED

**Andrew 2026-10-07:** Every section heading on the Open Sole PDP must be the same size. Raised many times — lock it.

**Draft only:** `187144929571` · never live `185687998755`  
**Template:** `templates/product.in-studio-template.json`  
**Page:** `/products/studio-performance-skin-footwear?preview_theme_id=187144929571`

## Standard (Home / Closed editorial Display)

| Width | font-size | line-height | weight | letter-spacing |
|------|-----------|-------------|--------|----------------|
| 1440 | **56px** | 59.36px (1.06) | 400 | -0.032em (-1.792px) |
| 390 | **36px** | 38.16px (1.06) | 400 | -0.032em (-1.152px) |

Product **h1** stays 18 / 600. Eyebrows, cards, buy box, footer stay out.

## What was wrong

- fifty-fifty used standard 56 / 1.06 / -0.032em
- statement-band / guarantee used band 52 / 1.1 / -0.028em (looked smaller than Never loses / Tired)
- pdp-features used giant 88 / 56 phone
- FAQ / reviews / juicer / Shop all used h2-standard 32 / 24
- `fullbleed-statement` **Hold every pose.** had `heading_size_override: 0` (TE empty number) → 36px on desktop
- **Redefine movement** is a 56px fifty-fifty title; **Redefine movement** on Think is a type-label eyebrow (not a heading)

## Lock

`layout/theme.liquid` scoped `template.suffix == 'in-studio-template'`:

- band + giant tokens = standard 56 / 36
- `#open-sole-heading-unify` forces every `#main-content` section heading to the standard
- JSON: Hold every pose `heading_size_override` **56** (never 0)

Home / Closed Sole / `/collections/all` must not move.

## Never

- Do not “fix” this by changing Home / Closed / collections heading CSS
- Do not push `theme.liquid` from the stale local tree over draft
- Do not clear `heading_size_override` back to 0 on Hold every pose
- Do not change copy, images, media heights, mobile text pads 96/96, buy box, or the product h1
