# Implementation Map — Homepage

## Reuse
| File | Role |
|------|------|
| `sections/hero.liquid` | Hero A (Sock Era) |
| `sections/value-strip.liquid` | Shared trust strip |
| `sections/disciplines.liquid` | Discipline proof |
| `sections/variant-grid.liquid` | Shop grid ATC |
| `sections/fifty-fifty.liquid` | Problem/grip, Sock Math lite, Coperni seasonal |
| `sections/social-proof.liquid` | Reviews |
| `sections/geo-section.liquid` | GEO (DP-03) |
| `sections/newsletter.liquid` | Email |
| `snippets/header-nav.liquid`, `announcement-strip`, `footer` | Chrome |

## Modify
| File | Change |
|------|--------|
| `templates/index.json` | Order toward frozen stack; Coperni seasonal settings; add UGC + guarantee blocks |
| `sections/hero.liquid` | Keep Concept A; optional CTA specificity later |

## New
| File | Role |
|------|------|
| `sections/home-ugc.liquid` | Instagram / UGC band (DP-09) |
| `sections/guarantee-band.liquid` | Guarantee trust band |

## Dependencies
- v49 CSS variables in theme assets
- Collection `grippy-shoes` for CTAs
- Coperni media assets (seasonal)

## Technical risks
- Section bloat vs July 17 parity — keep Sock Math lite; defer Founder
- UGC widget (Juicer) may need app embed; ship static grid fallback

## Recommended order
1. Freeze `index.json` order + hero settings
2. Add guarantee + UGC sections
3. Wire Coperni as fifty-fifty seasonal
4. Visual QA vs July 17
