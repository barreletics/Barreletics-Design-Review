# Help page section headings LOCKED

**Andrew 2026-10-07:** Same exhaustive 56/36 heading pass as Open Sole — every visual section heading on `/pages/help`.

**Draft only:** `187144929571` · never live `185687998755`  
**Template:** `templates/page.help.json` (`page-returns` section)  
**Preview:** `/pages/help?preview_theme_id=187144929571`

## Standard

| Width | font-size | line-height | weight | letter-spacing |
|------|-----------|-------------|--------|----------------|
| 1440 | **56px** | 59.36px (1.06) | 400 | -0.032em (-1.792px) |
| 390 | **36px** | 38.16px (1.06) | 400 | -0.032em (-1.152px) |

`COVERED` / `NOT COVERED` are 12px / 700 labels, not section headings.

## Lock

`layout/theme.liquid` scoped `template.suffix == 'help'` → `#help-heading-unify`.

Targets `.page-returns-head__title` and card/FAQ/CTA `h2.h2-standard` only on `body.template-page-help`.

## Never

- Do not change Home / Closed / collections / Open Sole / yoga-pants by editing shared type tokens
- Do not push stale local `theme.liquid` over draft
- Do not force h3 labels to 56/36
