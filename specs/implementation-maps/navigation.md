# Implementation Map — Navigation

## Reuse
- `snippets/header-nav.liquid`
- `snippets/announcement-strip.liquid`
- Mobile utility list (already has Help links)

## Modify
| File | Change |
|------|--------|
| `snippets/header-nav.liquid` | Desktop Help dropdown (About/FAQ/Contact/Returns); keep coral count badge |

## New
- None

## Dependencies
- Live pages: about, faq, contact, returns
- Apparel collections may 404 until merchandised (D-043)

## Technical risks
- Dropdown hover vs touch; z-index under sticky header

## Recommended order
1. Help dropdown markup + CSS
2. Verify badge count with cart.js
3. Mobile parity smoke test
