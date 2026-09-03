# Page ↔ Template Registry — SINGLE SOURCE

**Status:** ACTIVE · seeded 2026-08-09  
**Purpose:** Stop agents shipping the wrong page by binding **live handle → repo template → hub Locked mock → Admin theme-template suffix → QA preview path**.  
**Companion skill:** `.cursor/skills/barreletics-page-qa/SKILL.md` (also `~/.cursor/skills/barreletics-page-qa/`)  
**Freeze:** `planning/m4-section-freeze.md` · **Anti-revert:** `barreletics-anti-revert`  
**QA theme (default):** `187144929571` (M4 Visual QA) — push only when Andrew names this ID in-message.

> **Law:** If this registry conflicts with Andrew’s **CURRENT message** → CURRENT MESSAGE WINS. Update this file **forward**. Never invent handles. Never link dead URLs below.

### How to read a row

| Column | Meaning |
|--------|---------|
| **Handle / URL** | Canonical customer URL (use this in nav, CTAs, QA) |
| **Repo template** | File under `shopify-build/templates/` |
| **Hub Locked mock** | Authority in `docs/index.html` (or “live Admin / spine” when no Locked mock) |
| **Admin suffix** | Shopify Admin → resource → **Theme template** dropdown value (filename after `type.`) |
| **QA preview** | Path on storefront + `?preview_theme_id=187144929571` (or named disposable ID) |

**Team review index (one page for Andrew + team):** `docs/team-review.html`

Preview base: `https://barreletics.com{path}?preview_theme_id=187144929571`  
Theme Editor: `https://admin.shopify.com/store/barreletics/themes/187144929571/editor`

---

## Collections

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Shop All (grippy shoes)** | `/collections/barre-pilates-yoga-shoe-sock-footwear` | `collection.json` | Hub mock still **Collection v18 Locked** → `docs/Barreletics Collection - Definitive-v18.html` (do not overwrite). **M4 runtime SIGNED 2026-09-02 night:** Upgrade + tags → Studio → grid → No socks → Never slip on fullbleed → mosaic after Never loses — `templates/collection.json` | *(default / none)* | `/collections/barre-pilates-yoga-shoe-sock-footwear` |
| **Apparel** | `/collections/apparel` | `collection.apparel.json` | Structure follows **Collection v18 Locked** (apparel copy; no sole education). Live content: `https://barreletics.com/collections/apparel` | **`apparel`** (Admin set 2026-08-09 via `collectionUpdate`; was `apparel-page`) | `/collections/apparel` |
| **Optional sock kit** | `/collections/hot-kits` | `collection.hot-kits.json` | Coming-soon. Copy LOCKED J 2026-08-27. Handle stays `hot-kits`. Nav: **Socks** under Apparel (`m4-menu` only). **No page newsletter**. | **`hot-kits`** | `/collections/hot-kits` — **404 until collection is published to Online Store** |

**Do not treat Apparel as Shop All.** Wrong page = Apparel still on default collection template.

---

## Product (PDP)

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Closed Sole** | `/products/best-reformer-pilates-legree-workout-shoes` | `product.json` | **SIGNED 2026-08-16** · living spine = current `product.json` (v19 mock lineage). **No extra wow.** Wow = `fullbleed-lifestyle` 80/60. Prior fingerprint: v16 @ `691f03b` — never overwrite v16/v19 HTML. **Studio FAQ** = Theme settings → Studio FAQ (`use_studio_bank`). | *(default / none)* | `/products/best-reformer-pilates-legree-workout-shoes` |
| **Open Sole** | `/products/studio-performance-skin-footwear` | `product.open-sole.json` | Same **PDP v19 Locked** mock + Open spine | Live Admin **`in-studio-template`** (renders `product.in-studio-template.json` — keep byte-identical to `product.open-sole.json`). Do not flip Admin to `open-sole` without a letter — live Impulse uses this suffix. | `/products/studio-performance-skin-footwear` |
| **Outdoor / water shoes** | `/products/aquatic-performance-skins` | `product.outdoor.json` | Same **PDP v19 Locked** mock + Outdoor spine | **`outdoor`** | `/products/aquatic-performance-skins` |
| **Coperni collab** | `/products/barreletics-x-coperni-closed-sole` | `product.coperni.json` | **Product first** (2026-08-21): buy-box → strip → crosslink images → runway story. Not a Locked Closed PDP. | **`coperni`** | `/products/barreletics-x-coperni-closed-sole` |
| **One-off Closed** | `/products/one-off-colors-closed-sole` | `product.one-off-closed.json` | Closed Sole quality twin; One-Offs tab only; FAQ = Closed + 3 one-off Qs; P-011/D-051 | **`one-off-closed`** | `/products/one-off-colors-closed-sole` |
| **One-off Open** | `/products/one-off-colors-open-sole` | `product.one-off-open.json` | Same + Open deltas (rust badge · Open copy · handle) | **`one-off-open`** | `/products/one-off-colors-open-sole` |

**Deleted / do not recreate:** `product.closed-sole.json` — Closed Sole **is** the default `product.json`.

---

## Help & info pages

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Help hub** | `/pages/help` | `page.help.json` + `sections/page-help.liquid` | Pre-push: `docs/HELP-PREPUSH-PREVIEW.html` (= Help v8). **Push only after Andrew yes.** | **`help`** (create Admin page if 404) | `/pages/help?preview_theme_id=187144929571` |
| **FAQ** | `/pages/faq` | `page.faq.json` | **FAQ v7 quiet** → `docs/Barreletics FAQ - Definitive-v7.html` (Andrew 2026-08-12: rebuild target). **v4 Locked** = prior fingerprint — never overwrite | **`faq`** ✅ verified | `/pages/faq` |
| **Size chart** | `/pages/performance-skins-size-chart` | **`page.size-chart.json`** *(the file Admin actually renders)* · identical aliases `page.performance-skins-size-chart.json`, `page.size-guide.json` — **push all three or the page goes stale** | Calm system: `docs/Barreletics Size Chart - Definitive-v1.html`. Chart shows **M / L only** — no "S coming soon" | **`size-chart`** ✅ verified | `/pages/performance-skins-size-chart` |
| **Returns (policy)** | `/pages/returns` | **`page.shipping-retruns.json`** *(live Admin typo — this is the file that renders)* · identical alias `page.returns.json` | Hub **Current:** `docs/REVIEW-2026-08-08.html#returns` (canonical). Mock v3 = superseded concept | **`shipping-retruns`** ✅ verified — do not re-point Admin until letter; alias ready for **`returns`** | `/pages/returns` |
| **About / Our story** | `/pages/our-story` | `page.our-story.json` and/or `page.about.json` (confirm Admin assignment before edit) | Brand story mock for review: `docs/Barreletics Brand - Definitive-v1.html` (not Locked until letter). Help hub: **Help v3 Locked** | Confirm in Admin (`our-story` / `about` / default) | `/pages/our-story` |
| **Contact** | `/pages/contact-us-form` | **`page.contact.json`** *(Admin suffix is `contact`, not the handle)* · alias `page.contact-us-form.json` | Contact v1 (hub, not Locked) · live form page. **GOOD — do not thrash** | **`contact`** ✅ verified | `/pages/contact-us-form` |
| **Reviews (all Judge.me)** | `/pages/reviews` | `page.reviews.json` · live Admin often **`page.judgeme_all_reviews.json`** — keep both on full store widget | Shared Open+Closed page. 3 photo cards = Leslie S. / B P. / Tracie (Judge.me photo reviews). Full Judge.me list + native Write a Review. Review counts hidden (stars stay). Not a PDP. No sole-specific review pages. | Live **`judgeme_all_reviews`**; also `reviews` | `/pages/reviews` |

Help menu authority: About → `/pages/our-story` · FAQ → `/pages/faq` · Contact → `/pages/contact-us-form` · Returns → `/pages/returns`. Header Help fallback = **`/pages/help`** (hub exists 2026-08-14 — do **not** restore `/pages/faq`).

### Admin suffixes verified against Shopify 2026-08-12 (read this before editing a Help page)

Several Help pages render a template whose **name does not match the handle**. Editing the sibling file silently does nothing, and pushing only one name of a pair leaves the live page on a stale copy — that is what emptied the Fit Tips off the size chart.

| Live handle | Admin suffix | File that actually renders |
|---|---|---|
| `/pages/help` | `help` | `page.help.json` |
| `/pages/faq` | `faq` | `page.faq.json` |
| `/pages/performance-skins-size-chart` | `size-chart` | `page.size-chart.json` |
| `/pages/returns` | `shipping-retruns` | `page.shipping-retruns.json` |
| `/pages/returns-portal` | `start-a-retrun` | `page.start-a-retrun.json` |
| `/pages/contact-us-form` | `contact` | `page.contact.json` |

Re-query any time with `shopify store execute -s barreletics.myshopify.com -q 'query { pages(first: 100) { nodes { handle templateSuffix } } }'`. Keep alias files byte-identical and push every alias in the pair.

**Returns URL roles (2026-08-09):** announcement banner → `/pages/returns#returns` · Help/footer → `/pages/returns` · portal → `/pages/returns-portal` (separate).

---

## Journal (blog)

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Journal index** | `/blogs/news` | `blog.json` | **Journal v5 Locked** → `docs/Barreletics Journal - Definitive-v5.html` | Blog uses `blog.json` (no page suffix) | `/blogs/news` |
| **Article** | `/blogs/news/{article}` | `article.json` | Follow Journal Locked type/chrome | — | `/blogs/news/{handle}` |

---

## Partner / portal pages

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Collaborations** | `/pages/collaborations` | `page.collaborations.json` | Help-style tiles → Coperni + Free People. Footer + header parent. Never link the parent at a single product or `/`. | **`collaborations`** | `/pages/collaborations` |
| **Free People** | `/pages/free-people` | `page.free-people.json` | Live page + repo teaser→hero→grid. Exclusive sold only at Free People — **say it, don’t outbound.** CTA stays on-site (`#variants`). Hub has no Locked card. | **`free-people`** | `/pages/free-people` |
| **Partner programs** | `/pages/partners` | `page.partners.json` | Hub for wholesale / studio / ambassador. Footer Learn link only — not on Help page (Andrew 2026-08-21). | **`partners`** | `/pages/partners` |
| **Returns portal** | `/pages/returns-portal` | Live Admin often **`page.start-a-retrun.json`** *(typo)* · clean alias `page.returns-portal.json` | ReturnZap embed (live). Mock portal v1 = superseded bespoke form | Live **`start-a-retrun`**; clean-up → **`returns-portal`** when Andrew letters Admin change | `/pages/returns-portal` |

---

## Dead handles — NEVER ship / NEVER link

| Dead URL | Why | Use instead |
|----------|-----|-------------|
| `/blogs/journal` | Not the live blog handle | `/blogs/news` |
| `/pages/help` | Was 404 — template now in repo; Admin page + push after Andrew yes | `/pages/help` + template `help` |
| `/collections/open-sole` | Collection handle **does not exist** in Admin (404) | Shop All + sole tabs / PDP Open |
| `/collections/closed-sole` | Same — 404 | Shop All + sole tabs / PDP Closed |
| `/collections/outdoor` | Same — 404 | PDP Outdoor `/products/aquatic-performance-skins` |
| `/collections/collaborations` | Collection does not exist (404) | `/pages/collaborations` |
| `/pages/contact` | 404 | `/pages/contact-us-form` |
| `/pages/about` | 404 | `/pages/our-story` |

Repo may still contain `collection.open-sole.json` / `collection.closed-sole.json` / `collection.outdoor.json` for future mapping — **do not link those handles until Admin collections exist and this registry is updated.**

---

## Agent checklist (before any page work)

1. Find the row in **this file** for the page Andrew named.  
2. Open the **hub Locked mock** (if any) — do not invent a layout.  
3. Edit only the listed **repo template** (+ shared sections if required) — **one page per turn**.  
4. Confirm **Admin suffix** matches (or note Admin still required — e.g. Apparel → `apparel`).  
5. Push **only** if Andrew named a theme ID in **this** message.  
6. Verify the **QA preview path** for *that* handle — not a sibling page.  
7. If the change hits nav URLs, sole copy, or >1 surface → update freeze + this registry (see `.cursor/rules/os-sync-on-global-change.mdc`).

---

## Orphaned templates — no Admin page, render nowhere *(verified 2026-08-12 against all 45 Admin pages)*

| Repo template | Expected handle | Reality |
|---|---|---|
| `page.shipping.json` | `/pages/shipping` | **404 — no Admin page exists.** Shipping policy actually lives inside `/pages/returns` ("SHIPPING, RETURNS & FAQ") |
| `page.warranty.json` | `/pages/warranty` | **404 — no Admin page exists.** Warranty terms actually render on `/pages/returns` and `/pages/faq` |

Both files are maintained and correct in the repo — edits to them just aren't visible to any customer. Before trusting a preview of either, confirm the Admin page exists. **Do not create these pages without a letter**; the store deliberately consolidates shipping + returns + FAQ onto one handle, and adding thin duplicates would split the policy and the SEO.

Also note: contact is `/pages/contact-us-form` with suffix **`contact`**, not `/pages/contact`. `/pages/size-guide` does not exist either — the size chart is `/pages/performance-skins-size-chart` (suffix `size-chart`).

**Help hub tiles audited 2026-08-12 — all five return 200:** `/pages/contact-us-form` · `/pages/faq` · `/pages/performance-skins-size-chart` · `/pages/returns` · `/pages/returns-portal`. The hub correctly avoids the two orphans.

---

## Maintenance

Update this registry **forward** when Andrew locks a new mock, renames a handle, or changes an Admin suffix. Do not “fix” by restoring older collection/PDP URLs from `planning/m4a-*` archives.
