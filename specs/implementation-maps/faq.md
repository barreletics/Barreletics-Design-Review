# Implementation Map — FAQ

## Reuse
- `sections/page-faq.liquid`, `templates/page.faq.json`, geo

## Modify
| File | Change |
|------|--------|
| `templates/page.faq.json` | Replace terminal newsletter with contact CTA section |

## New
| File | Role |
|------|------|
| `sections/contact-cta.liquid` | “Still have questions?” → Contact |

## Dependencies
- `/pages/contact`

## Technical risks
- Low

## Recommended order
1. Add contact-cta section
2. Swap FAQ template order
