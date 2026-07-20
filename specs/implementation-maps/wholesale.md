# Implementation Map — Wholesale (deprecated standalone)

## Reuse
- `sections/page-partners.liquid` `#wholesale` — **canonical**

## Modify
| File | Change |
|------|--------|
| `sections/page-wholesale.liquid` | Deprecation banner / comment; do not assign in Admin |
| `templates/page.wholesale.json` | Mark deprecated in comment if possible |

## New
- None

## Dependencies
- Redirects M4A → `/pages/partners`
- R-01 HOLD

## Technical risks
- Live page still assigned orphan template

## Recommended order
1. Confirm Admin uses partners template
2. Deprecate orphan files in comments
3. Verify 301s
