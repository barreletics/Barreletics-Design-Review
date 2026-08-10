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

Preview base: `https://barreletics.myshopify.com{path}?preview_theme_id=187144929571`  
Theme Editor: `https://admin.shopify.com/store/barreletics/themes/187144929571/editor`

---

## Collections

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Shop All (grippy shoes)** | `/collections/barre-pilates-yoga-shoe-sock-footwear` | `collection.json` | **Collection v18 Locked** → `docs/Barreletics Collection - Definitive-v18.html` | *(default / none)* | `/collections/barre-pilates-yoga-shoe-sock-footwear` |
| **Apparel** | `/collections/apparel` | `collection.apparel.json` | Structure follows **Collection v18 Locked** (apparel copy; no sole education). Live content: `https://barreletics.com/collections/apparel` | **`apparel`** (Admin set 2026-08-09 via `collectionUpdate`; was `apparel-page`) | `/collections/apparel` |

**Do not treat Apparel as Shop All.** Wrong page = Apparel still on default collection template.

---

## Product (PDP)

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **Closed Sole** | `/products/best-reformer-pilates-legree-workout-shoes` | `product.json` | **PDP v19 Locked** → `docs/Barreletics PDP - Definitive-v19.html` (+ current spine). Prior fingerprint: v16 @ `691f03b` — never overwrite | *(default / none)* | `/products/best-reformer-pilates-legree-workout-shoes` |
| **Open Sole** | `/products/studio-performance-skin-footwear` | `product.open-sole.json` | Same **PDP v19 Locked** mock + Open spine | **`open-sole`** | `/products/studio-performance-skin-footwear` |
| **Outdoor / water shoes** | `/products/aquatic-performance-skins` | `product.outdoor.json` | Same **PDP v19 Locked** mock + Outdoor spine | **`outdoor`** | `/products/aquatic-performance-skins` |
| **Coperni collab** | `/products/barreletics-x-coperni-closed-sole` | `product.coperni.json` | Collab spine (crosslink + story); not a separate hub Locked PDP card — match repo + live | **`coperni`** | `/products/barreletics-x-coperni-closed-sole` |
| **One-off Closed** | `/products/one-off-colors-closed-sole` | `product.one-off-closed.json` | Lean spine (no sock-era); photo pickers; hide OOS; P-011/D-051 | **`one-off-closed`** | `/products/one-off-colors-closed-sole` |
| **One-off Open** | `/products/one-off-colors-open-sole` | `product.one-off-open.json` | Same lean one-off spine | **`one-off-open`** | `/products/one-off-colors-open-sole` |

**Deleted / do not recreate:** `product.closed-sole.json` — Closed Sole **is** the default `product.json`.

---

## Help & info pages

| Surface | Handle / URL | Repo template | Hub Locked mock | Admin suffix | QA preview path |
|---------|--------------|---------------|-----------------|--------------|-----------------|
| **FAQ** | `/pages/faq` | `page.faq.json` | **FAQ v4 Locked** → `docs/Barreletics FAQ - Definitive-v4.html` (v5+ = copy/layout experiments; promote only with `LOCK THIS`) | **`faq`** | `/pages/faq` |
| **Returns (policy)** | `/pages/returns` | `page.shipping-retruns.json` *(live Admin typo)* · clean alias `page.returns.json` | Hub **Current:** `docs/REVIEW-2026-08-08.html#returns` (canonical). Mock v3 = superseded concept | Live often **`shipping-retruns`** — do not re-point Admin until letter; alias ready for **`returns`** | `/pages/returns` |
| **About / Our story** | `/pages/our-story` | `page.our-story.json` and/or `page.about.json` (confirm Admin assignment before edit) | Brand story mock for review: `docs/Barreletics Brand - Definitive-v1.html` (not Locked until letter). Help hub: **Help v3 Locked** | Confirm in Admin (`our-story` / `about` / default) | `/pages/our-story` |
| **Contact** | `/pages/contact-us-form` | `page.contact-us-form.json` | Contact v1 (hub, not Locked) · live form page | **`contact-us-form`** | `/pages/contact-us-form` |

Help menu authority: About → `/pages/our-story` · FAQ → `/pages/faq` · Contact → `/pages/contact-us-form` · Returns → `/pages/returns`. Header Help fallback = **`/pages/faq`**.

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
| **Free People** | `/pages/free-people` | `page.free-people.json` | Live page + repo teaser→hero→grid spine (hub has no Locked Free People card) | **`free-people`** | `/pages/free-people` |
| **Returns portal** | `/pages/returns-portal` | Live Admin often **`page.start-a-retrun.json`** *(typo)* · clean alias `page.returns-portal.json` | ReturnZap embed (live). Mock portal v1 = superseded bespoke form | Live **`start-a-retrun`**; clean-up → **`returns-portal`** when Andrew letters Admin change | `/pages/returns-portal` |

---

## Dead handles — NEVER ship / NEVER link

| Dead URL | Why | Use instead |
|----------|-----|-------------|
| `/blogs/journal` | Not the live blog handle | `/blogs/news` |
| `/pages/help` | 404 · no `page.help.json` | Help menu + `/pages/faq` fallback |
| `/collections/open-sole` | Collection handle **does not exist** in Admin (404) | Shop All + sole tabs / PDP Open |
| `/collections/closed-sole` | Same — 404 | Shop All + sole tabs / PDP Closed |
| `/collections/outdoor` | Same — 404 | PDP Outdoor `/products/aquatic-performance-skins` |
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

## Maintenance

Update this registry **forward** when Andrew locks a new mock, renames a handle, or changes an Admin suffix. Do not “fix” by restoring older collection/PDP URLs from `planning/m4a-*` archives.
