# One-off colors — surfaces (OS how-to)

**OS homes:** `docs/10-DECISIONS.md` **P-011** · **P-014** · `planning/10-decision-log.md` **D-051** · **D-052** · `docs/08-theme-settings-reference.md` · `planning/page-template-registry.md`

## Strategy lock (P-014 / D-052) — 2026-08-10

**Feature ONE one-off at a time** via Theme settings. Keep it simple and special.

| Rule | Detail |
|---|---|
| Featured | Single picker `one_off_product` → nav + quiet ATC link + core PDP One-Offs tab |
| Both products in Admin | OK — Closed + Open one-off can both exist / be Active |
| Nav | Only the **featured** product appears under Grippy |
| Flip drop | Change Theme settings picker (Open **or** Closed) |
| Not now | Mixed Open+Closed in one product · third-level nav · dual nav Liquid |
| Future (if both menu-live) | Two **sibling** links under Grippy — no nested layer. Needs Andrew confirm before build |

**Why not one mixed product:** sole badge, Admin theme template (`one-off-open` vs `one-off-closed`), inventory, and ATC all assume one sole per product. Mixing soles in one SKU creates wrong badges and template fights.

**Why Theme settings (not page controls / Navigation):** sitewide gate in one place; page TE is for that PDP’s layout; do not also add One-off in Online Store → Navigation.

## Gate (Theme settings)

**Theme settings → One-off colors → product picker**

| Picker | Surfaces |
|---|---|
| Set | Nav under Grippy · quiet PDP link under ATC · All Variants One-Offs tab (core PDPs) |
| Empty | All three hide |

Theme setting **wins** over section `product_oneoffs` on Home / Collection / **core** PDPs. On one-off PDPs, Liquid uses **this page’s product** for the One-Offs tab.

## Admin checklist (featured drop)

1. **Products** — ensure the drop product is **Active** + **Online Store** channel on.  
2. **Theme template** (Admin → product → Theme template):  
   - Closed one-off → **`one-off-closed`**  
   - Open one-off → **`one-off-open`**  
3. **Theme settings** (Theme Editor → Theme settings → **One-off colors**):  
   - **One-off product** = the featured product (the one that should win nav + quiet link).  
   - Optional: Nav label / quiet link label / parent match (`grippy`).  
4. **Clear picker** → hides nav + quiet link (use when no featured drop).  
5. **Do not** add “One-off colors” in Online Store → Navigation.  
6. **QA** — Theme Editor preview on M4 (`187144929571`) for that product handle.

| Product | Handle | Admin theme template | Repo |
|---|---|---|---|
| One Off Colors (Closed Sole) | `one-off-colors-closed-sole` | `one-off-closed` | `product.one-off-closed.json` |
| One Off Colors (Open Sole) | `one-off-colors-open-sole` | `one-off-open` | `product.one-off-open.json` |

## Authority

**Closed Sole matured PDP** (`product.json` + shared sections) is visual/quality authority. One-off twins match that quality. Open deltas only: rust One-Off badge · Open sole copy · handle `one-off-colors-open-sole`.

**Do not edit** approved `product.json` / Open / Outdoor when fixing one-offs.

## Buy box (LOCKED FOLD — HARD)

**Rule:** `.cursor/rules/one-off-buy-box-lock.mdc` · anti-revert radioactive.

Buy column = **Closed Sole locked fold** (`pdp-buy-box.liquid` + v20c). **Fold judgment with chrome** = hub **v20d · LOCKED chrome** (`docs/pdp-fold-v20d-chrome.html`) — logo 42px · nav **#2** 13px mid Roboto. Agents doing one-off FAQ / 50/50 / reviews must **not** edit buy-box layout/CSS or wholesale-rebuild buy-box from `product.json`.

| Allowed JSON deltas | Forbidden |
|---|---|
| lede · short_description · One-Off badge · badge color · `show_kit_links: false` | Condensed stub · hide sold-out **sizes** · add “Size” label (v20c = chart-only) · qty / Coming soon S · thumb ≠ 7 |

- Photo swatches for colors · **hide sold-out colors only** (sizes stay M/L like Closed)  
- `show_size_chart_link: true` · `show_soon_size: false` · `thumb_count: 7`  
- Badge **One-Off** (never rewritten to Open Sole because handle contains `open-sole`). Core Closed Sole **default** badge = rust (TE may pick black/charcoal/blue). Distinct from Closed one-off black One-Off badge. Never dump Admin description into `short_description`.

## Variant grid (one-off PDPs)

Same shop-all tabs as Closed Sole (**Closed · Open · One-Offs · Outdoor**). Default tab = **One-Offs**. One-Offs panel = **this** one-off product (not theme picker; no misroute to core Open Sole).

**One-Offs tab cards (2026-08-10):** single 4-up grid — **available first, then sold-out**. No “Available now” / “Earlier one-offs” band headings. See more still expands one row at a time. Buy-box still hides sold-out options (unchanged).

## Spine (both one-offs)

No page-top hero. No sock-era / TRANSFORM / sock-math.

`pdp-buy-box` → `value-strip` → `pdp-features` → `fifty-fifty-lifestyle` → `variant-grid` → `fifty-fifty-commit` → `reviews` → `fifty-fifty-numbers` → `guarantee-band` → `home-juicer` → `collection-faq` → `pdp-sticky-atc`

Features: Closed eyebrow **Why Barreletics** · title **Same grip system. Limited color.**

**Fifty-fifty copy (2026-08-10):** One-off voice (limited color / when gone it’s gone) — not core Closed/Open slogans. Open vs Closed differ only on sole feel lines. No rust eyebrows.

**Open one-off hero + reviews (2026-08-11):** After lifestyle quote → media-only `fullbleed-lifestyle` (studio workout video + people-in-motion poster). Reviews hybrid: 3 TE photo cards (manual, per template) · text row = live Judge.me compact · curated text blocks off. `pictures_first` = soft prefer JM reviews with media in the cardify row — not full catalog reorder.

**Prompt 4 reviews variation (2026-08-11):** One-off review cards are **not** the Closed Sole Kimberly/Dvorah/Dorothy set. Closed one-off = 3 photo + 6 text (limited-color / second-pair voice). Open one-off = 3 distinct photo cards + live JM text (`show_text_cards: false`). Titles: “Limited color. Real grip.” Core `product.json` / open / outdoor reviews untouched.

FAQ: Closed full stack **plus** 3 One-Off limited-run questions.

Juicer: settings match Closed `product.json`. Renders on M4 — not in static HTML mocks.

## QA

Push only when Andrew says **push to 187144929571**. Preview path: `/products/one-off-colors-open-sole` or `…-closed-sole` with Admin template suffix set.

---

## STOP — dual nav

**Do not build** dual Theme pickers / two nav items unless Andrew confirms both drops must be menu-live. Pattern reserved: sibling links under Grippy (P-014).
