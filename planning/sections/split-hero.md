# Split hero

**Status:** In revision — **not frozen**  
**Filename:** `shopify-build/sections/split-hero.liquid`  
**CSS:** `shopify-build/assets/split-hero.css`  
**QA theme:** `187144929571` (M4 Visual QA)

---

## Theme Editor (summary)

| Group | Controls |
|-------|----------|
| **Media** | Type image\|video · image/poster · Shopify video · external MP4 URL · controls · reverse layout |
| **Trust** | Show row · show stars · **star color** (default gold `#d4af37` = production) · richtext trust · trust URL |
| **Copy** | Headline · heading level · **richtext body** · CTA · tag |
| **Typography** | Heading font · body font · desktop/mobile headline size · body size |
| **Colors** | Copy bg · headline · body/trust · CTA bg/text |

Stars sit in the trust row **above** the headline (Home WORKING order).

---

## Notes vs production / mock

- Star default is **gold** (design token / production), not mock rust — change in TE if you want rust `#c45c3f`.
- Video prefers Shopify Files video; external URL + poster as fallback (stronger than fifty-fifty placeholder).
