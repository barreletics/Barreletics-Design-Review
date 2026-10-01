# Earmark: Shopify Admin via box / Cloudflare (2026-09-13)

## Problem
Box browser Shopify Admin repeatedly hits Cloudflare “Verify you are human” and loops. Handing the box to Andrew does not reliably clear it for agent-driven Admin work (discounts, etc.).

## Do instead
- **Discount / Admin mutations:** Andrew creates in his Mac/phone Admin browser, OR Mac `shopify store auth` + `shopify store execute` with the right scopes (`write_discounts`, etc.).
- **Theme push / nav menus / pages:** keep using CLI paths that already work (theme push, menuUpdate, pageUpdate) — those do not need box Admin UI.
- **Do not** retry box Admin captcha loops for the same task.

## Related
Andrea code `0-ANDREAMINSKI` — create inactive in Andrew’s Admin; own in **Barreletics Andrea** chat.
