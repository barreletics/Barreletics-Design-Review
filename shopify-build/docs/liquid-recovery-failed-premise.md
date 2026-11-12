# Failed premise (Liquid recovery)

**Claimed:** Static regex / unit tests on placeholder patterns adequately prove valid **Shopify upload** Liquid for `cart-bundle-promo-config.liquid`.

**Falsified:** Shopify CLI rejected upload with `'raw' tag was never closed` on line 1. Cause: prose inside `{% comment %}` contained literal text `{% raw %}` (lexer opens `raw`, never closed). Regex tests never parsed the file with Shopify Liquid.

**Remediation:** Parser-backed CI (`shopify theme check` + Ruby `Liquid::Template.parse`) on exact artifact bytes before handoff.
