# Yoga pants PDP section headings LOCKED

**Andrew 2026-10-07:** Same exhaustive 56/36 heading pass as Open Sole — every visual section heading on `/products/lightly-padded-knee-yoga-pant-black`.

**Draft only:** `187144929571` · never live `185687998755`  
**Template:** `templates/product.yoga-pants.json`  
**Preview:** `/products/lightly-padded-knee-yoga-pant-black?preview_theme_id=187144929571`

## Standard

| Width | font-size | line-height | weight | letter-spacing |
|------|-----------|-------------|--------|----------------|
| 1440 | **56px** | 59.36px (1.06) | 400 | -0.032em (-1.792px) |
| 390 | **36px** | 38.16px (1.06) | 400 | -0.032em (-1.152px) |

Product **h1** stays 18 / 600. Buy-box lede, feature cards, eyebrows, footer stay out.

## Lock

`layout/theme.liquid` scoped `template.suffix == 'yoga-pants'` → `#yoga-pants-heading-unify`.

Do not change Home / Closed / collections / Open Sole by editing shared type tokens.

## Image-only (not a heading)

`fullbleed-workout` title **BRING YOUR WORKOUT TO LIFE** is `show_text: false` — image only. Do not turn text on to “fix” size.

## Never

- Do not push stale local `theme.liquid` over draft
- Do not force buy-box h1 or feature-card titles to 56/36
- Do not edit `product.yoga-pants.json` for this lock
