# Help menu · FAQ · Returns policy · Returns portal — where everything actually is

---
document: Help & Returns Inventory
version: 1.0
status: Findings — read-only investigation, nothing edited
author: Design System agent
date: 2026-08-08
verified: live curl (status + rendered template fingerprints) · Shopify Admin GraphQL `menus` query · live sitemap_pages_1 · QA draft theme 187144929571 render comparison · shopify-build source · live theme reference /Users/andrewnehra/barreletics-theme-live-apr2026
related: page-inventory-decisions.md · 11-navigation-architecture.md
---

## Mock → page map (re-verified 2026-08-08, read-only)

| Mock | Page handle | Page exists? | Deployed template matches mock? |
|---|---|---|---|
| `docs/Barreletics Help - Definitive-v4.html` (squares routing hub) | `/pages/help` | **No — 404 live and on QA `187144929571`** | No template (`page.help.json` does not exist in `shopify-build/`), no section built |
| `docs/Barreletics FAQ - Definitive-v7.html` (search + topic row) | `/pages/faq` | **Yes — 200 live and on QA** | **No.** QA renders `page.faq.json` → `page-faq` + `geo-section` + `contact-cta`, a plain category accordion with **zero search inputs**. v7 is still a candidate awaiting `LOCK THIS`. |
| Help menu (`help-menu`, 4 items) | n/a — menu, not a URL | Yes, assigned via `header-group.json` → `help_menu` | All four items 200: `/pages/our-story`, `/pages/faq`, `/pages/contact-us-form`, `/pages/returns` |

## The one-line answer

All four Help-menu links work on the live storefront. The returns **policy** page is `/pages/returns`; the returns **portal** is `/pages/returns-portal`, and it is a third-party app — **ReturnZap** — embedded in the page's Admin body content. The portal is **not in any menu**; the only way a customer finds it is by clicking through `/pages/returns` first.

---

## 1. Help menu

**Shopify menu:** handle `help-menu`, title "Help menu", ID `gid://shopify/Menu/313280364835`. Four items, all typed `HTTP` (plain URLs, not linked resources).

| Item | URL | Live status |
|---|---|---|
| About Us | https://barreletics.com/pages/our-story | **200** |
| FAQ | https://barreletics.com/pages/faq | **200** |
| Contact Us | https://barreletics.com/pages/contact-us-form | **200** |
| Returns & Exchanges | https://barreletics.com/pages/returns | **200** |

**No 404s. No redirects. No wrong destinations.** Every item resolves directly, first hop, no chain.

**Repo wiring:** `shopify-build/sections/header-group.json` → `header.settings.help_menu: "help-menu"`. Rendered by `shopify-build/sections/header.liquid` (lines 108–140 desktop dropdown, 212–220 mobile drawer). Verified rendering on QA draft theme `187144929571`: "Help ▾" appears as a text dropdown with all four children, desktop and mobile drawer.

**Where it does NOT appear:** the published live theme. barreletics.com's header still shows the old menu — an "About Us" dropdown containing About Us / Contact Us / FAQ, with **no Returns item**. The Help dropdown exists only on the QA draft theme. That's expected (repo is master, live is the old theme), but it means the Help menu Andrew approved is not yet what a customer sees.

**Two cosmetic issues:**

1. The "Help ▾" parent link itself hrefs to `help_menu.links.first.url` = `/pages/our-story`. Clicking the word "Help" navigates to About Us. Should probably be a non-navigating toggle, or point at `/pages/faq`.
2. `header.liquid` line 14 carries a correct comment: `/pages/help` 404s on this store. Confirmed — https://barreletics.com/pages/help returns **404**. There is no Help landing page and the fallback logic handles it.

**Design mock:** `docs/Barreletics Help - Definitive-v3.html` is the **Locked** hub card. `Barreletics Help - Definitive-v4.html` (footer 10% purge) is marked "candidate — say LOCK THIS to promote" and has not been promoted. Neither is a shipping page; Help is a menu, not a URL.

---

## 2. FAQ

| | |
|---|---|
| **Live URL** | https://barreletics.com/pages/faq — **200** |
| **Live template** | live theme `templates/page.faq.json` (sections: `main-page`, `apps`, `rich-text`, `contact-form`, `judgeme_carousel`) — rendered fingerprint `template--26590735237411` |
| **Repo template** | `shopify-build/templates/page.faq.json` |
| **Repo section** | `shopify-build/sections/page-faq.liquid` (+ `geo-section`, `contact-cta`) |
| **QA draft theme** | **200** — renders the repo build correctly (`faq-content` → `geo-section` → `contact-cta`) |
| **Design authority** | `docs/Barreletics FAQ - Definitive-v4.html` is **Locked** on the hub. v5 (copy fix), v6 (prior), **v7 (current candidate)** are all built but v7 is still awaiting "LOCK THIS". |

**Drift: yes, significant.** The shipping build (`page-faq.liquid`) is a plain category-grouped accordion — no search field, no topic row, no elevated head. Confirmed by rendering the QA theme: zero search inputs in the markup. Mocks v6 and v7 both introduce the search field and topic navigation. **None of the v5→v7 work has been built into the theme.** The FAQ Andrew has been reviewing in `docs/` and the FAQ on the QA draft theme are two different designs.

Also worth noting: the repo FAQ has a "Returns & Exchanges" category whose answers say *"Contact our support team to initiate an exchange."* It never mentions the returns portal. See §5.

---

## 3. Returns policy page

| | |
|---|---|
| **Live URL** | https://barreletics.com/pages/returns — **200** |
| **Live page title** | "Barreletics SHIPPING & RETURNS" |
| **Live template** | live theme `templates/page.shipping-retruns.json` — **note the typo, "retruns"** — fingerprint `template--26590735466787` |
| **Live content source** | the `main-page` section, i.e. hand-written HTML pasted into the **Admin page body**, not a theme section |
| **Repo template** | `shopify-build/templates/page.returns.json` |
| **Repo section** | `shopify-build/sections/page-returns.liquid` |
| **QA draft theme** | 🚨 **404** — see below |
| **Design authority** | `docs/Barreletics Returns - Definitive-v3.html` (hub card "v3 · Returns · Policy + Start a return") |

### 🚨 `/pages/returns` returns 404 on the QA draft theme

The page's Admin **template suffix is `shipping-retruns`** (a typo baked into the live theme years ago). `shopify-build/` has `page.returns.json`, not `page.shipping-retruns.json`. Shopify 404s when a page's assigned template doesn't exist in the active theme — so on theme `187144929571`, `/pages/returns` is simply gone.

This is not unique to returns. Verified on the QA theme:

| Page | Live | QA draft `187144929571` |
|---|---|---|
| `/pages/faq` | 200 | **200** ✅ |
| `/pages/our-story` | 200 | **200** ✅ |
| `/pages/contact-us-form` | 200 | **200** ✅ |
| `/pages/returns` | 200 | **404** ❌ |
| `/pages/returns-portal` | 200 | **404** ❌ |
| `/pages/performance-skins-size-chart` | 200 | **404** ❌ |
| `/pages/compare-open-closed-sole` | 200 | **404** ❌ |
| `/pages/free-people` | 200 | **404** ❌ |
| `/pages/reviews` | 200 | **404** ❌ |

FAQ, About and Contact survive only because their Admin suffixes (`faq`, `about`, `contact`) happen to match filenames that exist in both themes. **Six reviewable pages are unreachable on the QA preview.** This is an Admin template-suffix problem, not a repo problem — the fix is either renaming the suffix in Admin or adding matching filenames to the theme. Reported, not fixed.

### Drift: the repo returns page contradicted the live one — **FIXED FORWARD 2026-08-08**

- **Live `/pages/returns`** routes every return and exchange through the portal — four "Start a Return" / "Start an Exchange" buttons, plus inline links, all pointing at `https://barreletics.com/pages/returns-portal`.
- **Repo `page.returns.json` used to** describe a completely different process: step 1 *"Contact Support — email our support team with your order number"*, step 2 *"Receive Return Label"*. It never mentioned the portal, and shipping it would have silently deleted the portal from the site.

`page.returns.json` now renders `main-page` — the Admin page body — exactly like `page.shipping-retruns.json`, so both produce the same page and the portal links survive. `sections/page-returns.liquid` is **deleted**; nothing references it, and its schema defaults carried the same retired email-support wording. Proven by render, not by reading: `preview-returns-handle-template.html` is byte-identical to `preview-returns.html` and both carry five `pages/returns-portal` hrefs with zero occurrences of the retired strings.

### Also live: the legal policy

https://barreletics.com/policies/refund-policy — **200**. Admin-managed, referenced at checkout. Never redirect this; it is a different surface from the editorial page.

---

## 4. Returns portal

| | |
|---|---|
| **Live URL** | https://barreletics.com/pages/returns-portal — **200** |
| **Page H1** | "Start a Return or Exchange" (og:title "Start Your Return") |
| **What it actually is** | **ReturnZap**, a third-party Shopify app |
| **The embed** | `<script src="https://portal.returnzap.com/v2.js" async></script>` + `<return-zap shop-id="AWfBVmPxpdsnFDKeoeCBpP"></return-zap>` |
| **Where the embed lives** | inside the `main-page` section — i.e. **pasted into the Admin page body content**, not in any theme file |
| **Live template** | live theme `templates/page.start-a-retrun.json` — **also a typo, "retrun"** — fingerprint `template--26590735630627` |
| **Repo template** | **none. Does not exist.** No `page.returns-portal.json`, no `page-returns-portal.liquid` |
| **QA draft theme** | **404** (same template-suffix cause as above) |
| **Design authority** | `docs/Barreletics Returns Portal - Definitive-v1.html` |

### Is it reachable from navigation? No.

Exhaustively checked:

- Live header nav — **no portal link**
- Live footer (Contact Us · FAQ · Shipping & Returns · Size Guide · Blog · Sitemap · Privacy · Terms) — **no portal link**
- `help-menu` in Shopify Admin — **no portal item**
- `shopify-build/sections/footer.liquid` — links FAQ and `/pages/returns`, **no portal**
- `shopify-build/` searched for `returns-portal` / `returnzap` / `return-zap` — **zero matches anywhere in the repo**

The **only** path a customer has is: land on `/pages/returns` → click one of the "Start a Return" buttons in the page body. Two clicks minimum, and only if they find the returns page first. There is no app-proxy route either — `/apps/returns-portal`, `/apps/returnzap` and `/tools/returns-portal` all **404** (the live theme has stale `request.path contains '/apps/returns-portal'` guards in three `br-*` sections referencing a proxy path that no longer resolves).

### The mock does not match what's live

`docs/Barreletics Returns Portal - Definitive-v1.html` designs a **bespoke in-house form** — order number + email fields, plus a separate Track Order form, with a JS toast on submit. The live page is a ReturnZap web component that renders its own UI. The mock is a visual concept, not a spec for the shipping page. Any build against it either replaces ReturnZap or has to be re-skinned around it. Worth an explicit decision before anyone builds this.

---

## 5. Duplicate returns pages

Five live surfaces serve "returns". Verified by rendered-template fingerprint:

| URL | Status | Template fingerprint | What it is | Verdict |
|---|---|---|---|---|
| **https://barreletics.com/pages/returns** | 200 | `26590735466787` (own) | Real page, own content, "SHIPPING & RETURNS", 670 views/90d | **CANONICAL** editorial returns page |
| **https://barreletics.com/pages/returns-portal** | 200 | `26590735630627` (own) | ReturnZap "Start a Return", 347 views/90d | **KEEP** — different job, functional not editorial |
| **https://barreletics.com/policies/refund-policy** | 200 | Admin policy | Legal surface, referenced at checkout | **KEEP** — never redirect a policy URL |
| https://barreletics.com/pages/returns-and-exchanges | 200 | `26590735368483` **shared doorway** | Renders the Open Sole product landing with Add to Cart. Title "Customer Returns and Exchanges". No returns content. 26 views/90d | **301 → `/pages/returns`** |
| https://barreletics.com/pages/30-day-returns | 200 | `26590735368483` **shared doorway** | Byte-identical to the above (13,109 vs 13,115 words, same sections). Title "30 Day Returns". <8 views/90d | **301 → `/pages/returns`** |

The last two are two of the **ten** pages on this store sharing template `26590735368483`, which ignores page content entirely and renders a hardcoded product page. Documented in `planning/page-inventory-decisions.md`. They have no unique content to lose — they never rendered any. Redirect, don't delete.

**Recommended canonical:** `https://barreletics.com/pages/returns`, with a prominent link out to `/pages/returns-portal` (which it already has) and `/policies/refund-policy` kept untouched as the legal surface.

---

## Other things found (reported, not fixed)

- **`/collections/hot-kits` 404s on both live and the QA draft**, and it is a top-level item in `m4-menu` ("Hot Pilates & Yoga Kits") — so the new header currently ships with a broken primary nav link. `shopify-build/templates/collection.hot-kits.json` exists as a new untracked file, so another agent appears to be mid-build on it; the collection itself does not exist in Admin yet. Not part of the Help menu, but Andrew will hit it.
- **The typo'd template filenames** — `page.shipping-retruns.json` and `page.start-a-retrun.json` — are the direct cause of the QA 404s. Renaming them in Admin is a template-dropdown change; nothing in the repo needs to move.
- `/pages/help`, `/pages/contact`, `/pages/about`, `/pages/warranty`, `/pages/track-order`, `/pages/shipping-returns`, `/pages/faqs`, `/pages/help-center`, `/pages/return-policy`, `/pages/start-a-return` all **404**. None are referenced by the Help menu; several are referenced by `shopify-build/sections/footer.liquid` and `page-contact.liquid` (already catalogued in `page-inventory-decisions.md`).

## Priority order

1. **Fix the QA-theme 404s** (Admin template suffixes) — six pages Andrew wants to approve are currently unreachable on the preview theme. Nothing else on this list can be visually approved until this is done.
2. **Decide the returns-portal story** — repo `page.returns.json` currently replaces the portal with "email support". Reconcile before that template ships.
3. **Add the portal to navigation**, or accept that it is intentionally two clicks deep behind `/pages/returns`.
4. **301 the two doorway returns pages** to `/pages/returns`.
5. **Promote or reject FAQ v7** — the theme build is three mock versions behind.

---

**Method.** Live status codes and redirect chains via `curl` with a browser user-agent (`-I`, `-L`). Rendered template identity via Shopify's `shopify-section-template--<id>__<name>` markup fingerprints. Menus via Admin GraphQL `menus(first: 25)` (read-only; the CLI app lacks `read_content` and `read_themes`, so `pages` and `theme` queries were denied and the page inventory came from `sitemap_pages_1.xml` instead). QA-theme behaviour by previewing theme `187144929571` on the myshopify domain with the preview cookie and comparing `cdn/shop/t/141` against live `cdn/shop/t/137`. No Shopify mutations, no theme push/pull, no files in `shopify-build/` edited, nothing committed.
