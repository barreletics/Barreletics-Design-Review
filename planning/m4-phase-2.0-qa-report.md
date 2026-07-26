# M4 Phase 2.0 QA Report — Draft `187143618851`

**Date:** 2026-07-26  
**Scope:** Post–`theme.liquid` swap functional gate  
**Verdict:** **FAIL — do not start section construction**

Preview: https://barreletics.myshopify.com?preview_theme_id=187143618851

---

## Pass / fail by function

| Function | Result | Evidence |
|----------|--------|----------|
| Page renders (home) | **FAIL** | Visible Liquid errors at top of every page |
| Announcement strip | **PASS** | Renders; rotates messages |
| Desktop main nav (`main-menu`) | **PASS** | 5 top items; dropdowns present |
| Mobile nav open/close | **PASS** | Drawer toggles `is-open` |
| Header account link | **PASS** | `/account` link present |
| Header search / predictive search | **FAIL** | No search control in new header; Impulse `search-modal` / predictive UI not wired |
| Localization / markets selector | **FAIL** | Not in new layout/header |
| Cart icon | **PARTIAL** | Link + badge present |
| Cart drawer (slide-over) | **FAIL** | Impulse `#CartDrawer` in DOM but `position:static`, no `theme.js` — dumps inline at page bottom; not a drawer |
| `/cart` page | **FAIL** | Broken layout (“Quantity/Total” orphaned); empty-state inconsistency with badge |
| Search results page `/search` | **PASS** | Returns results (e.g. “grippy” → 6) |
| Predictive search (header) | **FAIL** | Not exposed in chrome |
| Product form / size+color / ATC button | **PARTIAL** | Forms + ATC visible on product templates; drawer path broken so ATC UX fails |
| Judge.me | **PASS** | App embed + floating reviews tab + stars |
| Tidio | **PASS** | App embed loads chat widget |
| Help Scout Beacon | **FAIL** | Layout renders missing snippet; Beacon not present |
| Popups (POWR) | **PASS** | POWR script present (app embed) |
| `popup-group` (theme newsletter/age) | **FAIL** | File exists on theme; **not** included in new `theme.liquid` |
| Analytics snippets (layout) | **FAIL** | Missing files → Liquid errors |
| App blocks host | **PASS** | Judge.me / Forms / etc. still inject via `settings_data` embeds |
| Footer structure | **PARTIAL** | Headings render; **0 menu links** in Shop/Support/Company |
| Footer newsletter form | **PASS** | Email + SIGN UP present |
| Impulse CSS/JS theme runtime | **FAIL** | `theme.css` / `theme.js` not loaded by new layout (assets may still exist on theme) |

---

## Confirmed regressions (from layout swap)

1. **Missing snippets referenced by new layout** (Liquid errors on every page):  
   `analytics-head`, `meta-pixel`, `pinterest-tag`, `clarity`, `analytics-events`, `helpscout-beacon`, `tidio-widget` (+ schema snippets if those templates hit).
2. **Cart drawer non-functional** — Impulse drawer markup kept; Impulse `theme.js` / drawer CSS not loaded → static block at page bottom.
3. **Search removed from header** — store search page still works if navigated directly.
4. **Localization UI removed**.
5. **`popup-group` not rendered** (Impulse newsletter/age verification sections orphaned).
6. **Footer menus empty** — footer expects handles that do not exist (see menus).
7. **No `theme.css`** in document — Impulse section styling partially degraded; only tokens + base + chrome.

---

## Required restoration (minimal — not Impulse architecture)

| # | Restore | How (recommended) |
|---|---------|-------------------|
| 1 | Stop Liquid errors | Edit draft `theme.liquid`: remove renders of missing shopify-build snippets **or** push stub/no-op snippets. Prefer remove/guard — app embeds already cover Judge.me/Tidio/pixels partially. |
| 2 | Working cart UX | **Either** (A) wire thin Barreletics `cart-drawer` + `cart.js` from `shopify-build` and point header trigger at it, **or** (B) temporarily re-load Impulse `theme.js` + required cart CSS only until thin drawer ships. Do not restore full Impulse header. |
| 3 | Search entry point | Add header search control that opens existing Impulse `search-modal` / predictive-search **or** links to `/search` (temporary). |
| 4 | Footer menus | Create Admin menus `footer-shop`, `footer-support`, `footer-company` **or** remappoint footer settings to existing `footer` handle with nested items. |
| 5 | Help menu (optional) | Create `help-menu` or leave unset (header already tolerates blank). |
| 6 | `popup-group` | Re-add `{% sections 'popup-group' %}` to layout **if** age/newsletter popup still required; else leave out and rely on POWR/app (document choice). |
| 7 | Help Scout | Only if still required: push `helpscout-beacon` snippet **or** drop render (Tidio is active). |

---

## Duplicate scripts / apps

| Source | Status |
|--------|--------|
| **Tidio app embed** | Enabled — widget loads (**keep**) |
| **Tidio layout snippet** | Missing file → Liquid error (would double if pushed while embed on) — **do not push tidio-widget while embed enabled** |
| **Judge.me app embed** | Enabled — OK |
| **Meta Pixel / Clarity / Pinterest layout snippets** | Missing — errors only; FB/GTM still appear via Shopify/customer events / other apps (**audit before re-adding snippets**) |
| **Help Scout** | Not in app embeds; snippet missing — currently off |
| **POWR Popup embed** | Enabled + script present |
| **Shopify Inbox** | Disabled — OK |
| **Markivo / Forms / sitemap SEO embeds** | Enabled |

**Rule:** Prefer **one** owner per concern (app embed XOR theme snippet).

---

## Admin menus (confirmed) — portability correction

**Do not create new Navigation handles.** Theme uses Theme Editor pickers only.

| Handle | Exists | Theme use |
|--------|--------|-----------|
| `main-menu` | YES | Soft-assigned in header-group (existing store menu; reassignable) |
| `footer` | YES | Soft-assigned as **primary footer menu** (nested→columns / flat→list) |
| `footer-shop` / `footer-support` / `footer-company` / `help-menu` | NO | **Not required — removed from architecture** |
| Others | various | Optional merchant picks only |

See `planning/m4-store-portability-rules.md`.

---

## Blockers before section construction

1. **Liquid errors must be cleared** (layout snippet references).  
2. **Cart drawer must work** (no static footer dump).  
3. **Footer menus** must resolve (create handles or remappoint).  
4. **Decide search + popup-group + Help Scout** (restore thin vs drop).  
5. **Re-QA ATC → drawer → checkout path** on a real PDP after fixes.  
6. Stay on draft `187143618851` only; `--nodelete`; no publish.

**Gate status:** Phase 2.0 **not passed**. Heroes / ports / JSON wiring **blocked** until restorations above land and this checklist re-runs green.
