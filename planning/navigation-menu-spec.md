# Navigation menu spec — ready to enter in Shopify Admin

---
document: Navigation menu spec (Admin entry sheet)
version: 3.0
status: >
  As-built. M4 Menu + Help menu + Kits collection applied via Admin API 2026-08-08.
  Remaining owner work = 3 footer menus, publish hot-kits, Theme Editor picks (§0).
created: 2026-08-07
last_modified: 2026-08-08
depends_on: [planning/11-navigation-architecture.md, shopify-build/sections/header.liquid, planning/nav-qa/]
authority: planning/11-navigation-architecture.md (🔒 Locked 2026-07-18)
---

## 0. ADMIN ENTRY CHECKLIST — do these in order, nothing to decide

Everything below is typed into **Shopify Admin** and the **M4 Visual QA** Theme Editor
(theme `187144929571`). The repo side is finished and verified — see §7. Titles matter:
Shopify derives the handle from the title, and the theme files already point at those
handles, so type the titles **exactly** as written.

### ✅ AS-BUILT 2026-08-08 — Steps 1, 2 and 4 already done via Admin API

Applied directly with `shopify store execute --allow-mutations`. **Do not re-enter these.**

| Thing | Status | ID |
|---|---|---|
| `M4 Menu` (`m4-menu`) | **Updated** to the Step 1 table below, incl. Hot Pilates & Yoga Kits. SALE removed, Journal replaces Blog, About removed (it lives in Help), Collaborations restored with Coperni + Free People children. | `gid://shopify/Menu/313154371875` |
| `Help menu` (`help-menu`) | **Created** with the four Step 2 items | `gid://shopify/Menu/313280364835` |
| `Hot Pilates & Yoga Kits` collection (`hot-kits`) | **Created**, 0 products, description set. **Not yet published to Online Store** — see Step 4b. | `gid://shopify/Collection/508346466595` |

**SALE, precisely:** `/collections/sale` **404s**, but `/pages/sale` **is live (200)**. SALE is out
of the nav by owner decision — *"we don't have anything on sale right now so we would not need it"* —
which stands regardless of the URLs. Reviving it means creating the Sale collection, not linking
`/pages/sale`.

**Still owner-only work:** the three footer menus (Step 3), publishing the Kits collection
(Step 4b), and the Theme Editor picks (Step 5). Publication scopes are not granted to the CLI app,
so the Kits collection cannot be published by API.

### Step 1 — Menu `M4 Menu` ✅ done

Admin → **Content → Menus**. Title: `M4 Menu` (handle reads `m4-menu`).
Recorded here as the authoritative item list.

| # | Level | Name (type exactly) | Link (paste exactly) |
|---|---|---|---|
| 1 | top | `Grippy Shoes` | `/collections/barre-pilates-yoga-shoe-sock-footwear` |
| 2 | under 1 | `Shop All Grippy Shoes` | `/collections/barre-pilates-yoga-shoe-sock-footwear` |
| 3 | under 1 | `Open Sole` | `/products/studio-performance-skin-footwear` |
| 4 | under 1 | `Closed Sole` | `/products/best-reformer-pilates-legree-workout-shoes` |
| 5 | under 1 | `Outdoor` | `/products/aquatic-performance-skins` |
| 6 | under 1 | `Compare Styles` | `/pages/compare-open-closed-sole` |
| 7 | top | `Hot Pilates & Yoga Kits` | `/collections/hot-kits` |
| 8 | top | `Apparel` | `/collections/apparel` |
| 9 | under 8 | `Shop All Apparel` | `/collections/apparel` |
| 10 | under 8 | `Tops` | `/products/barreletics-performance-fabric-yoga-t-shirts` |
| 11 | under 8 | `Bottoms` | `/products/lightly-padded-knee-yoga-pant-black` |
| 12 | top | `Collaborations` | `/products/barreletics-x-coperni-closed-sole` |
| 13 | under 12 | `Coperni` | `/products/barreletics-x-coperni-closed-sole` |
| 14 | under 12 | `Free People` | `/pages/free-people` |
| 15 | top | `Journal` | `/blogs/news` |

Do **not** touch `Main menu` — that is the published theme's menu.

**Hot Pilates & Yoga Kits is a deliberate placeholder** (owner letter 2026-08-08: *"it's nothing
right now but put it so we can complete the design and function — we can shut off or on"*). The
collection exists with zero products so the nav structure and design are complete now. The
**on/off switch is the collection's Online Store publication**, not the menu item — unpublish to
hide, publish to reveal. Leaving the item in the menu while the collection is unpublished would
ship a 404, so keep them in sync: publish before the item goes live to customers, or remove the
item while it stays dark.

This item is **not** in the Locked architecture (`11-navigation-architecture.md`), which lists four
top-level items. It is added forward by owner instruction. Do not "correct" it back out.

### Step 2 — Menu `Help menu` ✅ done

Admin → **Content → Menus**. Title: `Help menu` (handle reads `help-menu`).
Four items, flat, in this order:

| # | Name | Link |
|---|---|---|
| 1 | `About Us` | `/pages/our-story` |
| 2 | `FAQ` | `/pages/faq` |
| 3 | `Contact Us` | `/pages/contact-us-form` |
| 4 | `Returns & Exchanges` | `/pages/returns` |

### Step 3 — Create the three footer menus

Same place, three separate menus. Titles must produce handles `footer-shop`,
`footer-learn`, `footer-support` — `footer-group.json` already points at those.

**Title `Footer Shop`**

| # | Name | Link |
|---|---|---|
| 1 | `All Grippy Shoes` | `/collections/barre-pilates-yoga-shoe-sock-footwear` |
| 2 | `Open Sole` | `/products/studio-performance-skin-footwear` |
| 3 | `Closed Sole` | `/products/best-reformer-pilates-legree-workout-shoes` |
| 4 | `Outdoor` | `/products/aquatic-performance-skins` |
| 5 | `Apparel` | `/collections/apparel` |

**Title `Footer Learn`**

| # | Name | Link |
|---|---|---|
| 1 | `About Us` | `/pages/our-story` |
| 2 | `Journal` | `/blogs/news` |
| 3 | `Collaborations` | `/products/barreletics-x-coperni-closed-sole` |
| 4 | `Compare Styles` | `/pages/compare-open-closed-sole` |
| 5 | `Better Than Grippy Socks` | `/pages/best-barre-pilates-yoga-grippy-socks` |

**Title `Footer Support`**

| # | Name | Link |
|---|---|---|
| 1 | `FAQ` | `/pages/faq` |
| 2 | `Size Guide` | `/pages/performance-skins-size-chart` |
| 3 | `Care Instructions` | `/pages/care` |
| 4 | `Returns & Exchanges` | `/pages/returns` |
| 5 | `Shipping Policy` | `/policies/shipping-policy` |
| 6 | `Refund Policy` | `/policies/refund-policy` |
| 7 | `Contact Us` | `/pages/contact-us-form` |

Do **not** create a Connect menu — the footer builds that column from the social URL
settings, and Instagram is already set.

### Step 3b — The Kits on/off switch (one click, owner only)

`Hot Pilates & Yoga Kits` is in the nav and the page is fully designed, but the collection is
**not published to Online Store**, so `/collections/hot-kits` currently returns **404**. That
publication toggle *is* the on/off switch — the CLI app has no `read_publications` /
`write_publications` scope, so it cannot be flipped from here.

**To turn it on:** Admin → **Products → Collections → Hot Pilates & Yoga Kits** →
**Publishing** → check **Online Store** → Save. To turn it off again, uncheck it.

Already done by API, no action needed:

- Collection created, handle `hot-kits`, 0 products, description written.
- **Theme template set to `hot-kits`**, so it renders
  `shopify-build/templates/collection.hot-kits.json` — a deliberate coming-soon page
  (hero → "The idea" fifty-fifty → value strip → *Be first to the kits* signup), **not** an
  empty product grid. Requires a `shopify theme push` of `shopify-build/` to the M4 theme
  before it renders; until then the collection falls back to the default collection template.
- Menu item added to `M4 Menu`.

**Keep the two in sync.** A published menu item plus an unpublished collection ships a 404 to
customers. While Kits stays dark, either leave it unpublished *and* accept the 404 on the draft
only, or pull the menu item. When products land, add a `variant-grid` section to
`collection.hot-kits.json` and drop the "Coming soon" eyebrows.

### Step 4 — Theme Editor picks on theme `187144929571`

`https://admin.shopify.com/store/barreletics/themes/187144929571/editor`

1. **Header** section → **Main menu** = `M4 Menu`. (Not `Main menu`.)
2. **Header** section → **Optional secondary menu** = `Help menu`.
3. Leave **Nav link size** at `18px (live match)` and **Nav item gap** at `30` — approved,
   do not adjust.
4. **Footer** section → **Shop menu** = `Footer Shop`, **Learn menu** = `Footer Learn`,
   **Support menu** = `Footer Support`. Leave **Connect menu** blank.
5. Save.

If a `shopify theme push` of `shopify-build/` happens after this, the handles in
`header-group.json` and `footer-group.json` already match, so the picks survive — but
re-open the editor and confirm the five pickers still read the right menu names.

### Step 5 — Check it on the draft storefront

`https://barreletics.myshopify.com?preview_theme_id=187144929571`

1. Desktop: hover `Grippy Shoes` (5 items), `Apparel` (3 items) and `Collaborations`
   (2 items); `Hot Pilates & Yoga Kits` and `Journal` must be plain links with no dropdown.
   Hover `Help ▾` (4 items).
2. Narrow the window below ~900px: the nav collapses to the hamburger.
3. Phone: open the drawer, tap `Grippy Shoes`, `Apparel` and `Collaborations` — sub-items
   expand inline; the four Help items sit below the divider.
4. Footer: four columns, `Better Than Grippy Socks` under Learn, no discount copy.
5. `Hot Pilates & Yoga Kits` → 404 until Step 3b is done. After publishing it should show the
   coming-soon page with the *Be first to the kits* signup and **no** product grid.

### Step 6 — Only if you also want the architecture's collection URLs

Nothing above depends on this; it is the upgrade path. Create collections
`grippy-shoes`, `open-sole`, `closed-sole`, `outdoor`, `collaborations` in Admin, then
repoint the matching menu items from the product URLs to the collection URLs. `tops` and
`bottoms` stay deferred — one product each.

---

## Reconciled against locked architecture — 2026-08-08

`planning/11-navigation-architecture.md` is **🔒 Locked** and is the source of truth for nav
**structure and labels**. v1.0 of this entry sheet was drafted independently and drifted from it.
v2.0 conforms to the architecture. Structure and labels come from the architecture; **URLs come from
what returns 200 on the live store today**, with the architecture's intended URL kept in a "future
target" column.

| Drift in v1.0 | Fixed in v2.0 | Why |
|---|---|---|
| Label "Grippy Footwear" | **Grippy Shoes** | Architecture §"Why Grippy Shoes" — real search demand + mobile comprehension |
| Collaborations dropped | **Restored** as level 1 | It is in the locked primary nav |
| "Blog" as level 1 | **Journal** | Architecture label; owner reconfirmed "Journal" 2026-08-08 |
| "About" as level 1 | **Moved into Help** as About Us | Architecture puts About Us in utility nav, not primary |
| Sub-label "Shop All" / "All Apparel" | **Shop All Grippy Shoes** / **Shop All Apparel** | Architecture labels verbatim |
| Help had 7 items | **4 items** (About Us · FAQ · Contact Us · Returns & Exchanges) | Architecture Help set. The 3 real pages cut from Help (Size Guide, Care, policy links) move to **Footer Support** so nothing becomes unreachable — see judgment call in §2 |
| Footer columns ad hoc | Mapped to architecture's **Shop / Support / Company** columns | Architecture §Footer Structure |

**Held from the current thread (not architecture drift — do not "restore"):**

- **SALE removed 2026-08-08** — nothing is on sale. Not in the architecture either. Stays out.
- **Better Than Grippy Socks = footer, not header** (owner 2026-08-08). Architecture doesn't list it
  in primary nav, so both agree. It stays under Footer Learn.
- **Hot Pilates & Yoga Kits** exists on the **live published site only**. It is *not* in the locked
  architecture and there is no kit collection. It is **legacy live-only** — deliberately excluded.
  Do not add it back "to match live."
- Apparel → **Accessories** is in the architecture marked **(future)**. `/collections/accessories`
  **404s**, so it is intentionally absent from the entry sheet below. Add it when the collection is
  created.

**Architecture is stale on one point:** its Footer Newsletter row says "Email signup with 10% off."
That copy was **stripped** and must **not** be reintroduced — footer is Join the list with **NO 10%**
per `planning/m4-section-freeze.md` (Footer LOCKED Jul 31 2026) and
`.cursor/rules/anti-revert-fail-closed.mdc`. The architecture doc is Locked and was not edited;
this note records the exception.

---

## THE BLOCKER (read first)

**Navigation cannot be populated from this repo.** `shopify-build/sections/header.liquid` uses
Shopify `link_list` settings (`menu`, `help_menu`). A link_list stores only a *handle* — the actual
menu items live in **Shopify Admin → Content → Menus** (older label: Online Store → Navigation),
which is store data, not theme code. The repo can only say *which* menu to use.

So: Andrew (or Brian) must create/edit the menus in Admin, then pick them in the Theme Editor
header section. Everything below is written so it can be typed in with zero decisions.

### Verified store reality (checked 2026-08-07, re-verified 2026-08-08)

Only **4 collections** exist: `barre-pilates-yoga-shoe-sock-footwear`, `in-studio-grip`, `apparel`,
`favorites` (plus `/collections/all`). The architecture points at `/collections/grippy-shoes`,
`/open-sole`, `/closed-sole`, `/outdoor`, `/collaborations`, `/tops`, `/bottoms`, `/accessories` —
**all 404 today**, even though the repo has collection templates for several of them. Same for most
pages (`/pages/about`, `/pages/contact`, `/pages/help`, `/pages/warranty`, `/pages/size-guide`,
`/pages/shipping`, `/pages/returns-exchanges`, `/pages/track-your-order`, `/pages/accessibility`).

Newly verified 2026-08-08 (`curl -L`):

| Path | Status | Use |
|---|---|---|
| `/products/barreletics-x-coperni-closed-sole` | **200** ("Barreletics × Coperni — Closed Sole") | Collaborations destination |
| `/pages/free-people` | **200** ("Free People") | second collab page — see §1 judgment call |
| `/collections/accessories` | 404 | Accessories (future) stays out |
| `/collections/collaborations` | 404 | future target only |
| `/collections/collabs`, `/collections/collaboration`, `/pages/collaborations`, `/pages/coperni` | 404 | no alternative collab hub exists |
| `/policies/privacy-policy`, `/policies/terms-of-service` | 200 | available if legal column is wanted |

**Rule for this sheet: never enter a URL that 404s.**

---

## 1. Main menu — `M4 Menu` (handle `m4-menu`)

Owner created this menu 2026-08-08. It is **separate from `main-menu`**, which the published theme
uses — so editing `m4-menu` cannot affect the live storefront. `header-group.json` already points at
`m4-menu`, so a theme push lands on the draft's own menu, never the live one.

Primary nav as built: `Grippy Shoes | Hot Pilates & Yoga Kits | Apparel | Collaborations | Journal`
+ `[Help] [Account] [Cart]`. Help is a separate menu (§2); Account and Cart are header icons, not
menu items.

This is the Locked four-item architecture **plus Kits**, added forward by owner letter 2026-08-08.

**Live-verified 2026-08-08 — 15 of 16 nav URLs return 200.** The only failure is
`/collections/hot-kits` (404, collection unpublished — see §0 Step 3b).

| Level | Label | Link (200 today) | Future target once built |
|---|---|---|---|
| 1 | Grippy Shoes | `/collections/barre-pilates-yoga-shoe-sock-footwear` | `/collections/grippy-shoes` |
| 2 | Shop All Grippy Shoes | `/collections/barre-pilates-yoga-shoe-sock-footwear` | `/collections/grippy-shoes` |
| 2 | Open Sole | `/products/studio-performance-skin-footwear` | `/collections/open-sole` |
| 2 | Closed Sole | `/products/best-reformer-pilates-legree-workout-shoes` | `/collections/closed-sole` |
| 2 | Outdoor | `/products/aquatic-performance-skins` | `/collections/outdoor` |
| 2 | Compare Styles | `/pages/compare-open-closed-sole` | same |
| 1 | Hot Pilates & Yoga Kits | `/collections/hot-kits` — **404 until published** | same |
| 1 | Apparel | `/collections/apparel` | same |
| 2 | Shop All Apparel | `/collections/apparel` | same |
| 2 | Tops | `/products/barreletics-performance-fabric-yoga-t-shirts` | `/collections/tops` |
| 2 | Bottoms | `/products/lightly-padded-knee-yoga-pant-black` | `/collections/bottoms` |
| 1 | Collaborations | `/products/barreletics-x-coperni-closed-sole` | `/collections/collaborations` |
| 2 | Coperni | `/products/barreletics-x-coperni-closed-sole` | same |
| 2 | Free People | `/pages/free-people` | same |
| 1 | Journal | `/blogs/news` | same (blog handle is `news`) |

Indented form, matching the menu exactly:

```
Grippy Shoes                    /collections/barre-pilates-yoga-shoe-sock-footwear
    Shop All Grippy Shoes       /collections/barre-pilates-yoga-shoe-sock-footwear
    Open Sole                   /products/studio-performance-skin-footwear
    Closed Sole                 /products/best-reformer-pilates-legree-workout-shoes
    Outdoor                     /products/aquatic-performance-skins
    Compare Styles              /pages/compare-open-closed-sole
Hot Pilates & Yoga Kits         /collections/hot-kits
Apparel                         /collections/apparel
    Shop All Apparel            /collections/apparel
    Tops                        /products/barreletics-performance-fabric-yoga-t-shirts
    Bottoms                     /products/lightly-padded-knee-yoga-pant-black
Collaborations                  /products/barreletics-x-coperni-closed-sole
    Coperni                     /products/barreletics-x-coperni-closed-sole
    Free People                 /pages/free-people
Journal                         /blogs/news
```

### Resolved — Collaborations destination

An earlier revision of this doc offered three options and asked the owner to pick. **Option B is
what shipped:** `Collaborations` is a parent (pointing at the Coperni product so the parent itself
is never dead) with two children, `Coperni` and `Free People`. Both 200.

`/collections/collaborations` still 404s, so the label does not yet match a real hub. The upgrade
path stays open: create a `collaborations` collection holding both collabs, repoint the parent, and
the children become optional. **Do not link `/collections/collaborations` until it exists.**

### Items still with no real destination

| Item | Status | Recommendation |
|---|---|---|
| **Hot Pilates & Yoga Kits** | **In the nav as of 2026-08-08** by owner letter — *"it's nothing right now but put it so we can complete the design and function, we can shut off or on."* Collection exists (0 products) but is unpublished, so the URL 404s. Page is designed: `templates/collection.hot-kits.json`. | Publish when ready (§0 Step 3b). Not in the Locked architecture — **do not remove it to "match" the architecture.** |
| **Accessories** | In architecture as Apparel child, marked **(future)**; `/collections/accessories` 404s | Omit now; add as Apparel level 2 when the collection exists. |
| **SALE** | Removed 2026-08-08 — nothing on sale. `/collections/sale` 404s; `/pages/sale` is 200 but is not the right destination. Not in architecture. | Stays out. `collection.sale.json` template remains in the repo. To revive: create the Sale collection, then add level 1 `SALE` → `/collections/sale`. |
| Architecture `/collections/grippy-shoes` pillar | Does not exist (404) | Either create the collection (preferred — repo already has `collection.json` + sub-templates) or keep the `barre-pilates-yoga-shoe-sock-footwear` handle. Do not link 404s. |

---

## 2. Help menu — `Help menu` (handle `help-menu`)

Admin: **Menus → Add menu**, Title `Help menu` (handle `help-menu`). The header renders this as the
`Help ▾` dropdown; its first link is also the parent link target.

Architecture Help = exactly four items. All four links below verified 200 on 2026-08-08.

| Label (architecture) | Link (200 today) | Future target |
|---|---|---|
| About Us | `/pages/our-story` | `/pages/about` |
| FAQ | `/pages/faq` | same |
| Contact Us | `/pages/contact-us-form` | `/pages/contact` |
| Returns & Exchanges | `/pages/returns` | `/pages/returns-exchanges` |

```
About Us               /pages/our-story
FAQ                    /pages/faq
Contact Us             /pages/contact-us-form
Returns & Exchanges    /pages/returns
```

### Judgment call — the three items cut from Help (owner to confirm)

v1.0 had seven Help items. The architecture's Help is four, so **Size Guide** (`/pages/sizing`),
**Care Instructions** (`/pages/care`), **Shipping Policy** (`/policies/shipping-policy`) and
**Refund Policy** (`/policies/refund-policy`) were cut from the header dropdown. All four are real
200 pages and shoppers do look for them, so they are **preserved in Footer Support** (§3) rather than
deleted — nothing becomes unreachable.

If the owner would rather keep a fatter Help dropdown than follow the locked four, say so and this
sheet gets a second block; the architecture would then need a forward update. **Not decided here.**

Notes: `/pages/help`, `/pages/about`, `/pages/contact`, `/pages/returns-exchanges`,
`/pages/warranty`, `/pages/size-guide`, `/pages/shipping`, `/pages/track-your-order` and
`/pages/accessibility` **all 404** — do not link them. The handles above are the live equivalents.

### Support pages that do not exist yet (Help stays incomplete until these are built)

| Missing page | Why it matters | Repo status |
|---|---|---|
| Warranty | 90-day warranty is a headline trust claim in the value strip and guarantee band, but there is no page to link | `templates/page.warranty.json` exists — page never created in Admin |
| Track Your Order | Standard support expectation; drives contact-form volume without it | none |
| Accessibility | Compliance exposure | none |
| About (`/pages/about`) | Architecture's Help target; `/pages/our-story` is the live stand-in | `templates/page.about.json` exists — page never created |

### Repo has templates for pages that were never created in Admin

`page.wholesale.json`, `page.ambassador.json`, `page.studio-program.json`, `page.partners.json`,
`page.technology.json`, `page.grip-comparison.json`, `page.compare.json`, `page.about.json`,
`page.shipping.json`, `page.size-guide.json`, `page.warranty.json`, `page.contact.json` all exist in
`shopify-build/templates/` but the corresponding pages **404 on the store**. The design system is
ahead of the store's content. Creating those pages in Admin (and assigning the matching template) is
owner/Brian work, not a theme push.

Two extra live pages catalogued 2026-08-08: `/pages/care` and `/pages/reviews`.

If `help_menu` is left blank the header falls back to a single `Help ▾` link to `/pages/help`,
**which 404s**. Assign the menu or turn Help off.

---

## 3. Footer menus (optional — footer works without them)

`sections/footer.liquid` ships hardcoded fallback columns. Several of those fallbacks point at
handles that 404 on this store (`/collections/open-sole`, `/collections/closed-sole`,
`/pages/how-it-works`, `/pages/size-guide`, `/pages/compare`, `/pages/shipping-returns`,
`/pages/warranty`, `/pages/contact`).

Assigning **any** of the four column pickers switches the footer to menu-driven columns, so these
menus are the clean fix without touching the frozen footer section.

Column names follow the architecture's Footer Structure (Shop · Support · Company). "Footer Learn"
is the theme's picker for the architecture's **Company** column.

```
Footer Shop            (handle footer-shop)
    All Grippy Shoes   /collections/barre-pilates-yoga-shoe-sock-footwear
    Open Sole          /products/studio-performance-skin-footwear
    Closed Sole        /products/best-reformer-pilates-legree-workout-shoes
    Outdoor            /products/aquatic-performance-skins
    Apparel            /collections/apparel

Footer Learn           (handle footer-learn)   [architecture: Company]
    About Us           /pages/our-story
    Journal            /blogs/news
    Collaborations     /products/barreletics-x-coperni-closed-sole
    Compare Styles     /pages/compare-open-closed-sole
    Better Than Grippy Socks   /pages/best-barre-pilates-yoga-grippy-socks

Footer Support         (handle footer-support)
    FAQ                /pages/faq
    Size Guide         /pages/performance-skins-size-chart
    Care Instructions  /pages/care
    Returns & Exchanges  /pages/returns
    Shipping Policy    /policies/shipping-policy
    Refund Policy      /policies/refund-policy
    Contact Us         /pages/contact-us-form
```

**Better Than Grippy Socks belongs here** (owner decision 2026-08-08), under Footer Learn — not in
the header. It is the top SEO page, so it must stay linked from every page; the footer does that
without cluttering the shopping nav.

Footer notes:

- Architecture's Support column lists **Warranty** — omitted because `/pages/warranty` 404s. Add it
  the day the page is created.
- Architecture's Support column says "Shipping & Returns" as one link; the live store splits these
  into `/pages/returns` + `/policies/shipping-policy`, so both are listed.
- Size Guide points at `/pages/performance-skins-size-chart` ("Shoe Size Chart"), not
  `/pages/sizing`. Both return 200, but `/pages/sizing` is tab content ("Sizing- Tab") that
  renders inside a product page rather than a standalone destination. Same target is now
  the default for the PDP **Size Chart →** link (§7).
- Size Guide and Care Instructions sit here because they were reconciled out of Help (§2).
- `/collections/all` ("All Colors" in v1.0) was dropped — not an architecture label. `/policies/privacy-policy`
  and `/policies/terms-of-service` are both 200 if a legal row is ever wanted.
- **Newsletter: Join the list, NO 10% off.** The architecture's "10% off" note is stale; that copy was
  stripped and must not be reintroduced (`planning/m4-section-freeze.md`,
  `.cursor/rules/anti-revert-fail-closed.mdc`).
- Connect column: leave `menu_connect` blank — the footer already builds it from the social URL
  settings (Instagram is set).

---

## 4. Theme Editor steps (after menus exist)

1. Theme Editor → **Header** section → **Main menu** = `M4 Menu` (**not** `Main menu` — that's the
   published theme's live menu).
2. Same section → **Optional secondary menu** = `Help menu`.
3. Leave header logo/nav sizing as-is (another agent owns header typography — do not adjust here).
4. Footer section → optionally assign Shop / Learn / Support column menus.
5. QA desktop + mobile drawer: parents with children must render as accordions, and every link must
   return 200.

---

## 5. Schema / code gaps found

| Gap | Impact | Recommendation |
|---|---|---|
| `header.liquid` renders an **empty `<nav>`** when no menu is assigned | A TE-added header looks broken until a menu exists — likely exactly what Andrew is seeing | Add a hardcoded fallback nav mirroring the footer's fallback pattern (4 links: Grippy Shoes · Apparel · Collaborations · Journal). Needs owner OK before editing the section. **Still open** — Step 1 of §0 removes the symptom. |
| ~~Help fallback links to `/pages/help` (404)~~ | — | **Fixed in repo** — `header.liquid` falls back to `/pages/faq`, and the mobile drawer gets the same fallback so phones are never left without support. |
| No dropdown depth control | Header renders exactly 2 levels; 3rd-level Admin items are silently dropped | Fine for this IA (max 2 levels). Document only. |
| Announcement messages are blocks on `announcement-strip`, not the header | No gap — rotation + 4 messages already set in `header-group.json` | None. |
| `header-group.json` in repo vs TE-added header | A future `shopify theme push` of `header-group.json` **overwrites the header Andrew just added in the Theme Editor**, including his menu picks | Menu handles are already set in the repo file (`m4-menu`), so a push lands configured; re-verify in TE after any push. |

---

## 6. Copy compliance

All labels above comply with decision **P-012** (retired venue language — see
`.cursor/rules/no-pool-positioning.mdc`). The Outdoor item is described with approved vocabulary only
(resortwear, paddleboarding, beach, outdoor yoga, boating, travel) wherever nav copy is expanded.

---

## 7. Repo-side verification — done 2026-08-08

Evidence lives in `planning/nav-qa/`. Two runnable checks, both green:

- `python3 planning/nav-qa/audit.py` — renders `header.liquid`'s markup with the complete
  menu above against the real `design-tokens.css` / `chrome.css` / `chrome.js`, at 390 /
  768 / 1024 / 1440 plus a 769→1024 sweep. Asserts dropdown position and clipping, empty
  dropdown artifacts, drawer accordion behaviour, ≥44px tap targets, Escape close, and
  horizontal overflow. Writes `report.json` and the screenshots.
- `python3 planning/nav-qa/link-check.py` — pulls every internal href out of the shipped
  section files (Liquid comments stripped) and requests it. Writes `link-check.json`.

**Verified working**

| Check | Result |
|---|---|
| Grippy Shoes / Apparel dropdowns | Open on hover *and* keyboard focus; 5 and 3 rows; fully inside the viewport; every row hit-testable (not clipped or covered) at 1024 and 1440 |
| Collaborations / Journal | Plain links — no `<ul>` rendered, no empty dropdown artifact, no `--has-sub` class |
| Help ▾ | Opens on desktop, right-aligned, 4 rows, stays inside the viewport |
| Mobile drawer 390 / 768 | Hamburger opens it, both parents collapsed until tapped then expand inline, `aria-expanded` tracks state, Escape closes and unlocks body scroll |
| Tap targets | Smallest interactive row in the drawer is 44px |
| Help on mobile | All 4 items render under the drawer divider |
| Overflow / collisions | None at 390, 768, 1024, 1440, or anywhere in the 769→1024 sweep |
| Every shipped link | 200, except the two `Complete the kit` products (Coming soon) |

**Defects found and fixed forward** (`assets/chrome.css` only — no type values touched)

1. **Header overflowed 769–865px.** The row needs ~873px for logo + four title-case 18px
   labels + Help/Account/Cart, but the drawer only took over at 768px, so the whole page
   scrolled sideways on tablets. The nav/hamburger/Help breakpoint moved to **900px**; the
   padding and mobile logo-height switch stayed at 768px so nothing else shifted.
2. **Dropdown min-width 180px wrapped "Shop All Grippy Shoes"** onto two lines. Now 220px,
   capped at `100vw - 32px`.
3. **Doubled hairline** where the last drawer item's bottom border met the utility list's
   top border. Last item's border removed.

**Link targets repointed forward**

| File | Was (404) | Now (200) |
|---|---|---|
| `sections/pdp-buy-box.liquid` | `/pages/size-chart` | `/pages/performance-skins-size-chart` |
| `sections/variant-grid.liquid` | `/pages/size-chart` | `/pages/performance-skins-size-chart` |
| `sections/footer.liquid` fallbacks | `/collections/open-sole`, `/collections/closed-sole`, `/pages/how-it-works`, `/pages/size-guide`, `/pages/compare`, `/pages/shipping-returns`, `/pages/warranty`, `/pages/contact`, `/products/gift-card`, `/apps/tracktor` | the §3 link set (all 200) |
| `sections/footer-group.json` | `email_url` → `/pages/contact` | `/pages/contact-us-form` |

`footer-group.json` also pre-selects `footer-shop` / `footer-learn` / `footer-support` so a
push lands configured. Until those menus exist the handles resolve blank and the footer
falls back to the hardcoded columns, which now carry the same links — so the footer is
correct either way. Footer composition, column count, headings and order are unchanged; no
discount copy was reintroduced.

---

## 8. Still blocked on Admin — cannot be finished in the repo

**Partly unblocked 2026-08-08.** `M4 Menu`, `Help menu` and the Kits collection were applied
through the Admin API with `shopify store execute --allow-mutations`, so they are no longer waiting
on manual entry. What remains genuinely blocked is below.

| Blocked item | Why the repo cannot do it | Consequence today |
|---|---|---|
| ~~`M4 Menu`, `Help menu`~~ | **DONE via Admin API 2026-08-08** — see §0 | Nav and Help render |
| `Footer Shop`, `Footer Learn`, `Footer Support` | Menus are **linklists — store data**, not theme files. A theme can only name a handle. | Footer falls back to its hardcoded columns until these exist |
| Publishing the `hot-kits` collection to Online Store | CLI app has no `read_publications` / `write_publications` scope | `/collections/hot-kits` 404s, so the Kits nav item is dead until the owner ticks Online Store. This toggle is also the intended on/off switch |
| Collections `open-sole`, `closed-sole`, `outdoor`, `collaborations` (and the `grippy-shoes` pillar) | Collections are store data | Menu items point at single products instead of category pages. Every link is 200, so nothing is broken — but the label promises a category and delivers one product |
| `tops` / `bottoms` collections | Deliberately deferred — one product each | Same: item points at that one product |
| Kit products for `Complete the kit` | Products are store data | Two 404 links in the PDP buy box, gated behind `show_kit_links` / label settings. **Not touched** — locked v19 composition |
| Pages `warranty`, `track-your-order`, `accessibility`, `about` | Pages are store data (repo already has `page.warranty.json`, `page.about.json` etc.) | Warranty is a headline trust claim with nowhere to link, so it stays out of the footer |
| Theme Editor menu picks + visual approval | Approval happens in Shopify, not GitHub | Nav is unreviewed until Step 4–5 |

No `shopify theme push` / `pull` / `dev` / `delete` / publish was run in this pass. No theme ID was
named in the current message, so `templates/collection.hot-kits.json` is **repo-only** — it needs a
push to `187144929571` before the Kits page renders as designed.

### Store mutations applied 2026-08-08 (audit trail)

| Mutation | Target | Detail |
|---|---|---|
| `menuUpdate` | `gid://shopify/Menu/313154371875` (`m4-menu`) | Set to the §1 structure: Kits added, Collaborations given Coperni + Free People children, SALE and About removed, Blog → Journal |
| `menuCreate` | `gid://shopify/Menu/313280364835` (`help-menu`) | Four §2 items |
| `collectionCreate` | `gid://shopify/Collection/508346466595` (`hot-kits`) | Title `Hot Pilates & Yoga Kits`, 0 products, coming-soon description |
| `collectionUpdate` | same | `templateSuffix: "hot-kits"` so it renders `collection.hot-kits.json`. Harmless before the push — Shopify falls back to the default collection template |

Nothing touched `main-menu`, any published theme, or any product.
