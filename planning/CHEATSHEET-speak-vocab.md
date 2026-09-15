# Barreletics — speak vocab cheat sheet

How Andrew talks to Grok / Cursor about the theme. Updated 2026-09-12.

## Sections

| You say | Means |
| --- | --- |
| **50/50** | Split section: half media, half text (`fifty-fifty`) |
| **Fullbleed** | Full-width media band with optional title on top (`fullbleed-statement`) |
| **Features / Obsession** | Bullet/feature grid (`pdp-features`) — e.g. Grip, support, and freedom |
| **Shop all / variants** | Color/style grid (`variant-grid`) |
| **Buy box** | Top PDP: price, sizes, ATC (`pdp-buy-box`) |
| **Guarantee band** | Our promise columns |
| **Value strip** | Thin trust/value row under buy box (often off) |

## Locked type

| You say | Means |
| --- | --- |
| **Type OS Display** | Big 50/50 title — ~38–52px, weight **400** |
| **Display + strong punch** | Same Display, plus `<strong>` on the turn (→ ~700). **Size unchanged** |
| **Statement** | Fullbleed role — smaller (~28–36). Prefer **Display** on Outdoor fullbleed |
| **Supporting** | Features heading (~40/400) — not a 50/50 |

## Example asks

- “Nudge the barefoot **50/50** focal down.”
- “Set that title to **Display + strong punch**.”
- “Move **Outdoor works** 50/50 below Denise.”
- “Turn **value strip** off.”

## Related OS

- Type OS: `planning/type-os-LOCKED.md`
- 50/50 mobile: `planning/fifty-fifty-pdp-mobile-LOCKED.md`
- Parked next: `planning/PARKED-NEXT.md`

## Whole-system copy updates

When Andrew says **whole system** / **everywhere** / **sitewide** for policy or FAQ lines, update **all surfaces that carry that line**:

| Surface | Where |
| --- | --- |
| FAQ master | `/pages/faq` → `templates/page.faq.json` |
| Help Quick answers | `/pages/help` (+ returns/shipping templates using it) → `sections/page-returns.liquid` |
| PDP on-page FAQ | e.g. Outdoor `collection-faq` in product template JSON |
| Good to know | PDP buy-box note accordion (per template, e.g. Outdoor) |
| Buy-box Shipping & returns / warranty | Locked in `sections/pdp-buy-box.liquid` (all PDPs) |

Say: **“Sync whole system”** or **“Update FAQ master + Help + Outdoor”**.

