# Page Inventory — Consolidation & Decision Sheet

---
document: Page Inventory Decisions
version: 2.0
status: Proposed — awaiting owner sign-off
author: Design System agent
date: 2026-08-08
supersedes: v1.0 (reframed after authoritative sitemap pull)
verified: Live sitemaps · full-page content fetch of all 21 pages · rendered-template fingerprinting · GA4 property 300437005 (90 days ending 2026-08-07) · live products.json
depends_on: [09-collection-architecture.md, 11-navigation-architecture.md, 12-seo-geo-standards.md]
---

## Headline finding

**Ten of the store's twenty-one pages are the same page.**

They share one page template (`template--26590735368483`) that renders a hardcoded product landing — the Open Sole product, with variant pickers and an Add to Cart button — and **ignores each page's own content entirely.** Their rendered bodies are byte-identical: 3,846 words each, similarity 1.000 on a 6-gram Jaccard comparison, down to identical section instance IDs. Each has its own title and meta description; none has its own body. Measured page-specific content: **1 word.**

The affected pages:

`/pages/privacy-policy` · `/pages/data-sharing-opt-out` · `/pages/care` · `/pages/sizing` · `/pages/t-shirts-and-tank-top-sizing` · `/pages/yoga-pants-size-guide` · `/pages/yoga-pants-t-shirt-size-guide` · `/pages/30-day-returns` · `/pages/returns-and-exchanges` · `/pages/best-barre-pilates-yoga-grippy-socks`

This is a textbook doorway-page pattern and Google treats it as such: ten URLs competing on one body of content, diluting the crawl budget and the authority of the pages that do have real content. **This is more urgent than building anything new**, and it explains most of what looked like "duplication" from the handle list alone.

It also means two things nobody intended:

- **`/pages/data-sharing-opt-out` — the "Your Privacy Choices" page — has no opt-out control on it.** The only forms rendered are the locale selector, the newsletter signup, and an Add to Cart. That page exists to satisfy CCPA/CPRA. It currently sells a shoe. **Fix this first.**
- **`/pages/care`, titled "Care & How to Wear", contains no care instructions.** Same for the three apparel sizing pages, which contain no apparel measurements.

Pages that are genuinely healthy — own template, own content — are `/pages/returns`, `/pages/faq`, `/pages/our-story`, `/pages/contact-us-form`, `/pages/compare-open-closed-sole`, `/pages/performance-skins-size-chart`, `/pages/free-people`, `/pages/returns-portal`, `/pages/reviews`, `/pages/shop-performance-skins`, `/pages/sale`.

> **Root cause, one line:** a single bad template assignment repeated across ten pages. Most of the fix is a template dropdown in Admin, not a rewrite.

---

# Part 1 — Consolidation plan for existing duplicates

**Principle applied throughout: redirect, never delete.** A 301 preserves whatever equity and inbound links a URL has accumulated; deletion throws it away and produces a 404. Every recommendation below is a redirect or a repair. Nothing is deleted.

Traffic figures are GA4 `screenPageViews`, 90 days ending 2026-08-07. "<8" means the page fell below the top-160 paths, so its traffic is negligible but non-zero.

## Cluster A — Returns: five surfaces, one answer

| URL | What it really is | Views/90d | Verdict |
|---|---|---|---|
| **`/policies/refund-policy`** | Legal policy, Admin-managed, referenced at checkout | 12 | **KEEP — legally load-bearing.** Never redirect a policy URL. |
| **`/pages/returns`** | Real page, own template, real content, titled "SHIPPING & RETURNS" | **670** | **CANONICAL editorial returns page.** Assign `page.returns` template. |
| **`/pages/returns-portal`** | Real page, own template, "Start Your Return" — the returns-app landing | **347** | **KEEP — genuinely different job.** Functional, not editorial. Link it prominently from `/pages/returns`. |
| `/pages/returns-and-exchanges` | Doorway duplicate — renders the product landing | 26 | **301 → `/pages/returns`** |
| `/pages/30-day-returns` | Doorway duplicate | <8 | **301 → `/pages/returns`** |

Five surfaces → three, each with a distinct job: the legal policy, the editorial explainer, the functional portal. The two redirected pages have no unique content to lose — they never rendered any.

## Cluster B — Sizing: five pages, and only one of them works

This cluster needs the most care, because footwear sizing and apparel sizing are legitimately different content and should both survive.

| URL | What it really is | Views/90d | Verdict |
|---|---|---|---|
| **`/pages/performance-skins-size-chart`** | Real page, own template, real shoe size table. Already the 301 target of the retired `/pages/size-guides` handle | **237** | **CANONICAL footwear sizing.** Assign `page.size-guide` template. |
| **`/pages/yoga-pants-size-guide`** | Doorway duplicate — but see the warning below | <8 | **KEEP THE HANDLE — repair, don't redirect.** Make this the single apparel size guide covering pants *and* tops. |
| `/pages/sizing` | Doorway duplicate | <8 default locale, but **228 on `/de/pages/sizing`** | **301 → `/pages/performance-skins-size-chart`.** Redirect rather than delete — there is a live German-market traffic path into this handle. |
| `/pages/yoga-pants-t-shirt-size-guide` | Doorway duplicate. Byte-identical body, *and identical title and meta description*, to `/pages/yoga-pants-size-guide` | <8 | **301 → `/pages/yoga-pants-size-guide`** |
| `/pages/t-shirts-and-tank-top-sizing` | Doorway duplicate | <8 | **301 → `/pages/yoga-pants-size-guide`** |

> ⚠️ **Do not redirect `/pages/yoga-pants-size-guide` away, despite the ugly handle.** The product `lightly-padded-knee-yoga-pant-black` carries the tag `meta-size-chart-yoga-pants-size-guide`. That `meta-size-chart-<page-handle>` pattern is the convention size-chart apps use to bind a size-chart page to a product. Redirecting or renaming this handle would very likely break the size chart on the yoga pant PDP. Keep the handle, fix the content, and revisit the handle only after confirming which app owns that tag.

Five pages → two: one footwear size guide, one apparel size guide. Note this gives `page.size-guide.json` two jobs — it's a section with settings, so one template can serve both pages as separate instances.

## Cluster C — Privacy: one redirect, one urgent repair

| URL | What it really is | Views/90d | Verdict |
|---|---|---|---|
| **`/policies/privacy-policy`** | The real policy | 59 | **KEEP — canonical.** |
| `/pages/privacy-policy` | Doorway duplicate masquerading as a policy | 34 | **301 → `/policies/privacy-policy`** |
| **`/pages/data-sharing-opt-out`** | "Your Privacy Choices" — **renders a product page with an Add to Cart and no opt-out control** | 19 | **🚨 REPAIR IMMEDIATELY. Do not redirect.** Restore Shopify's default page template so the opt-out mechanism renders. |

The opt-out page is the one item on this sheet I'd treat as urgent regardless of everything else. It is a compliance surface that is currently non-functional, and the fix is a template dropdown.

## Cluster D — Sale: a stale orphan

| URL | What it really is | Views/90d | Verdict |
|---|---|---|---|
| `/pages/sale` | Own template, zero page-specific content. Owner confirms nothing is on sale | 78 | **301 → the pillar collection** while nothing is on sale. **Owner decision** — see below. |

78 views per 90 days are currently landing on a page with nothing on it. Sending them to the pillar collection recovers that intent. The tradeoff: when a real sale runs, you must remove the redirect first, and the right home for a sale is `/collections/sale` (an automated collection on the `sale` tag), not a page. If you'd rather not manage that toggle, the alternative is to leave `/pages/sale` alone — it's low-stakes either way.

## Cluster E — `/pages/shop-performance-skins`: a page trying to be a collection

Investigated as asked. It has its own template and **three words** of page-specific content, pulling 149 views/90d. It is a thin shop-landing page, **not** the pillar the architecture wants.

The real pillar already exists: **`/collections/barre-pilates-yoga-shoe-sock-footwear`, at 16,847 views/90d** — more than every content page on the site combined, and the top organic landing page.

**Verdict: 301 `/pages/shop-performance-skins` → the pillar collection** (after the rename in Part 3). It is a weaker second entrance to a door that already exists, and consolidating it feeds the pillar rather than competing with it.

## Cluster F — the doorway template itself

The single highest-leverage repair. For pages being redirected, the template no longer matters. For these four, it does:

| Page | Views/90d | Why it must keep its URL | Fix |
|---|---|---|---|
| `/pages/best-barre-pilates-yoga-grippy-socks` | **333** | Real SEO equity on a keyword handle, and it's the "Learn" nav destination in `planning/m4-section-freeze.md` | Assign `page-grip-comparison` — see Part 2 |
| `/pages/data-sharing-opt-out` | 19 | Compliance surface | Restore Shopify's default page template |
| `/pages/care` | 9 | Live URL with inbound links; care and how-to-wear are top support questions | Rebuild with real care content |
| `/pages/yoga-pants-size-guide` | <8 | Bound to the yoga pant PDP by app tag | Rebuild as the apparel size guide |

### Consolidation summary

| Action | Count |
|---|---|
| 301 redirects to a canonical URL | **7** |
| Pages repaired in place (template reassignment) | **4** |
| Pages deleted | **0** |
| Live pages after consolidation | 21 → **14**, all with distinct jobs |

---

# Part 2 — Verdicts on the twelve unbuilt templates

| Verdict | Meaning in Admin |
|---|---|
| **CREATE** | No live equivalent. Create the page, assign the template. |
| **FOLD INTO X** | The job is already done by live page X. Assign this template to **X**, keeping X's handle and equity. No new handle. Add a 301 from the handle the repo assumes. |
| **DROP** | No real job. Delete the template from the repo. |

| Template | Verdict | Reason |
|---|---|---|
| `page.about.json` | **FOLD INTO** `/pages/our-story` | Real page with its own template and content, 605 views/90d. The repo template is the better build — retarget it; keep the handle for its founder-name search intent. |
| `page.contact.json` | **FOLD INTO** `/pages/contact-us-form` | Real, healthy page, 669 views/90d. Ten links in `shopify-build/` point at `/pages/contact` — fix with a 301, not a second form. |
| `page.size-guide.json` | **FOLD INTO** `/pages/performance-skins-size-chart` **(and a second instance on** `/pages/yoga-pants-size-guide`**)** | The canonical footwear size chart is real and already live. Use a second instance of the same template to repair the apparel guide — one template, two pages, the sizing cluster solved. |
| `page.compare.json` | **FOLD INTO** `/pages/compare-open-closed-sole` | Its Product A / Product B settings *are* Open Sole vs Closed Sole. The live page is healthy and is the site's #1 content page at 1,027 views/90d. Never create `/pages/compare` against it. |
| `page.grip-comparison.json` | **FOLD INTO** `/pages/best-barre-pilates-yoga-grippy-socks` | **The best single fix on this sheet.** A 333-view page with real keyword equity is currently serving doorway content; this 656-line template is the strongest build in the repo and is written for exactly that topic. Equity kept, doorway eliminated, template used. |
| `page.technology.json` | **CREATE** `/pages/technology` | The only genuine content gap. Nothing on-site explains how the grip works, the materials, or Made in USA manufacturing — the proof behind a $74 price and the best available asset for AI answers to "how do grippy shoes work". |
| `page.warranty.json` | **DROP** | Verified covered in four live places (see below). A fifth copy is a fifth place to drift. Lift its "What's NOT covered" list into the FAQ first. |
| `page.shipping.json` | **DROP** | `/policies/shipping-policy` is the legal surface and `/pages/returns` is literally titled "SHIPPING & RETURNS". A third copy guarantees drift. |
| `page.partners.json` | **CREATE** `/pages/partners` — routing hub — *program agent owns* | Three cards routing to the dedicated program pages, plus a general-inquiry fallback form. Updated 2026-08-08 (D-048): it is the hub, not the single surface. |
| `page.wholesale.json` | **CREATE** `/pages/wholesale` — *program agent owns* | Updated 2026-08-08 (D-048), was FOLD INTO `/pages/partners`. B2B buyers qualify on order volume and resale terms — questions no shared form can carry. |
| `page.studio-program.json` | **CREATE** `/pages/studio-program` — *program agent owns* | Updated 2026-08-08 (D-048), was FOLD INTO `/pages/partners`. Studios qualify on class volume and location. |
| `page.ambassador.json` | **CREATE** `/pages/ambassador` — *program agent owns* | Updated 2026-08-08 (D-048), was FOLD INTO `/pages/partners`. Creators qualify on audience and content channels. |

> **Updated 2026-08-08 — the four program rows above.** Owner direction on 2026-08-08 reversed the fold: three dedicated program pages **plus** `/pages/partners` as a routing hub. Recorded as **D-048** in `planning/10-decision-log.md`, superseding D-042. All four templates are built and mobile-QA'd (`planning/partner-programs.md` §5, `planning/partner-pages-qa/`). The three folding 301s were retired in `planning/m4a-redirect-map.md` — they would have made the new pages unreachable.

Two templates already match live handles and need no action: `page.faq.json` → `/pages/faq` (451 views), `page.returns.json` → `/pages/returns` (670 views). Listed so they aren't mistaken for gaps.

**Net: create 5 pages, retarget 5 templates onto existing pages, delete 2 templates.**

> **Scope:** the four program templates are owned by another agent this cycle. Verdicts only — those files were not edited.

---

# Part 3 — Collections to create

The locked navigation needs seven collections. **Only four collections exist, and none of the seven is among them.**

Live today: `/collections/barre-pilates-yoga-shoe-sock-footwear` (16,847 views/90d) · `/collections/apparel` (884) · `/collections/in-studio-grip` (9) · `/collections/favorites`.

### The catalog constraint — six live products

| Product | `product_type` |
|---|---|
| `best-reformer-pilates-legree-workout-shoes` | `Grippy Shoe Closed Sole` |
| `studio-performance-skin-footwear` | `Grippy Shoe Open Sole` |
| `aquatic-performance-skins` | `Aquatic Footwear` |
| `barreletics-x-coperni-closed-sole` | *(empty — untyped, untagged)* |
| `barreletics-performance-fabric-yoga-t-shirts` | `V-Neck T-Shirt` |
| `lightly-padded-knee-yoga-pant-black` | `Yoga Pants` |

Product types are already clean enough to drive automated collections with zero manual curation. Every shoe also carries the `Grippy Shoes` tag.

| Collection | Verdict | How |
|---|---|---|
| `/collections/grippy-shoes` | **RENAME the existing pillar — do not create new** | See the warning below. Highest-stakes action on this sheet. |
| `/collections/open-sole` | **CREATE — automated** | `product_type = Grippy Shoe Open Sole`. Template ready. |
| `/collections/closed-sole` | **CREATE — automated** | `product_type = Grippy Shoe Closed Sole`. Template ready. Picks up the Coperni collab once typed. |
| `/collections/outdoor` | **CREATE — automated** | `product_type = Aquatic Footwear`. **Read the tag warning below before writing its copy.** |
| `/collections/collaborations` | **CREATE — manual** | Top-level nav item with no home. One product today (Coperni), and `/pages/free-people` already pulls 574 views/90d. |
| `/collections/tops` | **HOLD** | One product. A collection page for one t-shirt is an empty shelf that reads as a broken store. `/collections/apparel` covers it. Create at ≥3 products. |
| `/collections/bottoms` | **HOLD** | One product. Same. |

Also drop the templates for collections that can never fill: `collection.new-arrivals.json`, `collection.limited-editions.json`, `collection.one-offs.json`, `collection.gift-cards.json` (one gift-card product, 9 views). Hold `collection.sale.json` until a real sale runs — that's the proper home for the `/pages/sale` traffic.

**So the nav unlock is four collections plus one rename.** Three of the four are automated and need no ongoing maintenance.

### ⚠️ The pillar rename — and where `/pages/shop-performance-skins` goes

`/collections/barre-pilates-yoga-shoe-sock-footwear` carries **16,847 views in 90 days** and is the top organic landing page. The locked nav calls it `/collections/grippy-shoes`.

**Recommended:** rename the handle to `grippy-shoes` in Admin **with Shopify's "create a URL redirect" checkbox ticked**, so the old URL 301s and equity transfers. Then 301 `/pages/shop-performance-skins` into it, consolidating that page's 149 views/90d into the pillar rather than against it.

**Do not build a new `grippy-shoes` collection alongside the old one.** Two pillars on the same keyword set would cannibalise the store's single best-ranking asset — the exact problem this document exists to end.

This is worth a deliberate decision, not a drive-by. Confirm the redirect checkbox, then watch Search Console impressions for that URL for two weeks. If you'd rather not touch it, the alternative is keeping the existing handle and accepting a documented deviation from the locked nav doc — cheaper than a ranking loss. **Your call.**

---

# Warranty and order tracking

## Warranty — you're right. Already covered. `page.warranty.json` should be dropped.

The 90-day claim runs sitewide in the value strip and guarantee band, so it needed verification. It is stated in **four live places**:

| Location | Wording found |
|---|---|
| `/pages/faq` | "Is there a warranty on my purchase? — Yes, all purchases are covered by our 90-day warranty against manufacturing defects." |
| `/pages/returns` | Dedicated block: "90-Day Warranty Included… Return of the defective item is not required." |
| `/policies/refund-policy` | "90-Day Warranty — All purchases are covered against manufacturing defects." |
| `/policies/shipping-policy` | Same 90-day clause, plus warranty-replacement shipping terms |

All four cover the international case (photo proof within 90 days; customer pays replacement shipping and duties) and the 24-hour defective-on-arrival rule. **The sitewide claim is fully substantiated without a standalone page.**

One gap worth closing cheaply: none of the four states what is *not* covered. `page-warranty.liquid` has a well-built "What's NOT covered" block — lift that list into the FAQ answer and the refund policy, then delete the template.

## Order tracking — confirmed. Don't build a page. And `/pages/returns-portal` does not cover it.

Checked as asked: **`/pages/returns-portal` is a returns portal, not order tracking.** Its content is "Start Your Return" with an order-number lookup for initiating a return. It does not surface shipment status. So it neither solves tracking nor conflicts with the recommendation.

Order tracking is already handled three ways:

- **`/account` returns 200 and redirects to `account.barreletics.com/authentication/login`** — the store runs Shopify's new customer accounts, with passwordless email-code login. There is no password page to design.
- **Customers are already tracking successfully.** GA4 shows `/orders` at 305 views and roughly **60 distinct `/orders/<token>` order-status pages** in the top 160 paths over 90 days, at 8–22 views each. That token URL is the order-status page Shopify links from confirmation and shipping emails.
- `/profile` shows 163 views — customers reach the account area unprompted.

A `/pages/track-order` page could only duplicate Shopify's own lookup, and would need maintaining forever. **Verdict: DROP the idea. Add "Track your order" as a nav/footer link pointing at `/account`** — a menu link, not a page.

---

# Admin fixes found along the way

### Copy-law violation live on the store

`aquatic-performance-skins` carries a product tag naming the retired venue positioning that `.cursor/rules/no-pool-positioning.mdc` bans explicitly as an SEO tag, plus two adjacent tags in the same retired family ("Aqua Shoes", "Aquatic Water Shoes"). Search the product's tag list in Admin for the banned venue term and delete it.

This matters beyond hygiene: **that product is the entire basis of the Outdoor collection.** Clean the tags before creating it, and keep its copy to the approved framing — resortwear, paddleboarding, beach, outdoor yoga; boating, boat deck, hot sand, travel and surf also remain approved.

### The Coperni collab is invisible to automation

`barreletics-x-coperni-closed-sole` has an empty `product_type` and **no tags at all**. It will not appear in any automated collection, including `grippy-shoes` and `closed-sole`. Set `product_type = Grippy Shoe Closed Sole` and add the `Grippy Shoes` tag plus a collab tag **before** building the collections, or it will be missing from the new nav.

### Broken internal links in `shopify-build/`

The theme links to handles that 404 today. Flagged, not fixed — several of these files are owned by other agents or guarded by `.cursor/rules/anti-revert-fail-closed.mdc`. Nothing here was edited.

| File | Line | Broken link | Should point to |
|---|---|---|---|
| `sections/pdp-buy-box.liquid` | 9 | `/pages/size-chart` | `/pages/performance-skins-size-chart` — **this is the size-guide link in the buy box** |
| `sections/variant-grid.liquid` | 170 | `/pages/size-chart` | Same |
| `sections/footer.liquid` | 203, 246 | `/pages/how-it-works` | `/pages/technology` once created |
| `sections/footer.liquid` | 206, 249 | `/pages/size-guide` | `/pages/performance-skins-size-chart` |
| `sections/footer.liquid` | 207, 250 | `/pages/compare` | `/pages/compare-open-closed-sole` |
| `sections/footer.liquid` | 214, 257 | `/pages/shipping-returns` | `/pages/returns` |
| `sections/footer.liquid` | 215, 258 | `/pages/warranty` | `/pages/returns` |
| `sections/footer.liquid` · `snippets/footer.liquid` · `snippets/header-nav.liquid` | various | `/pages/contact`, `/pages/about`, `/pages/shipping` | Per Part 2 verdicts |
| `sections/header.liquid` | 123 | `/pages/help` | Make Help a dropdown; remove the page link |
| `sections/page-contact.liquid` | 100–102 | `/pages/shipping`, `/pages/size-guide`, `/pages/warranty` | Per Part 2 verdicts |

**Shortcut:** the redirects in step 2 below make most of these resolve without touching a single guarded file.

---

# What the owner needs to decide

1. **The pillar rename.** Rename to `grippy-shoes` with a 301, or keep the handle and accept a documented deviation from the locked nav doc? 16,847 views/90d is on the table. *(Recommend: rename with the redirect checkbox, then watch Search Console for two weeks.)*
2. **`/pages/sale`.** Redirect to the pillar while nothing is on sale, or leave the stale page up? *(Recommend: redirect, and use a `sale` collection when a real sale runs.)*
3. **Tops and bottoms in the nav.** Ship the Apparel dropdown with only "Shop All Apparel" until there are ≥3 products per bucket? *(Recommend: yes.)*
4. **The four program pages.** Confirm the one-hub approach with the agent who owns them?
5. **`/pages/yoga-pants-size-guide`.** Confirm which app owns the `meta-size-chart-yoga-pants-size-guide` tag before anyone touches that handle.

---

# Admin action checklist, in order

**Urgent — compliance:**

1. Reassign `/pages/data-sharing-opt-out` to Shopify's default page template so the opt-out control renders. It currently shows a product page with Add to Cart.

**Zero risk, unblocks the most:**

2. Add 301 redirects: `/pages/returns-and-exchanges` → `/pages/returns` · `/pages/30-day-returns` → `/pages/returns` · `/pages/sizing` → `/pages/performance-skins-size-chart` · `/pages/yoga-pants-t-shirt-size-guide` → `/pages/yoga-pants-size-guide` · `/pages/t-shirts-and-tank-top-sizing` → `/pages/yoga-pants-size-guide` · `/pages/privacy-policy` → `/policies/privacy-policy` · plus the repo-link fixes `/pages/about` → `/pages/our-story` · `/pages/contact` → `/pages/contact-us-form` · `/pages/size-chart` → `/pages/performance-skins-size-chart` · `/pages/warranty` → `/pages/returns` · `/pages/shipping` → `/policies/shipping-policy`
3. Delete the banned venue tag from `aquatic-performance-skins`; review its two sibling retired-positioning tags
4. Set `product_type` and tags on `barreletics-x-coperni-closed-sole`

**Repair the doorway pages that keep their URLs:**

5. `/pages/best-barre-pilates-yoga-grippy-socks` → assign the `grip-comparison` template
6. `/pages/care` → rebuild with real care and how-to-wear content
7. `/pages/yoga-pants-size-guide` → rebuild as the apparel size guide (pants + tops)

**Collections — the nav unlock:**

8. Create automated `open-sole` (`product_type = Grippy Shoe Open Sole`)
9. Create automated `closed-sole` (`product_type = Grippy Shoe Closed Sole`)
10. Create automated `outdoor` (`product_type = Aquatic Footwear`) — check copy law on its description
11. Create manual `collaborations`; add Coperni
12. **Decide, then act on** the pillar rename → `grippy-shoes`; then 301 `/pages/shop-performance-skins` into it

**Pages:**

13. Create `/pages/technology`, assign the `technology` template
14. Assign existing templates to live pages: `our-story` → about · `contact-us-form` → contact · `performance-skins-size-chart` → size-guide · `compare-open-closed-sole` → compare

**Repo cleanup (agent work, after sign-off):**

15. Lift "What's NOT covered" from `page-warranty.liquid` into the FAQ, then delete `page.warranty.json` and `page.shipping.json`
16. Delete `collection.new-arrivals.json`, `collection.limited-editions.json`, `collection.one-offs.json`, `collection.gift-cards.json`
17. Fix the broken internal links, coordinating with the footer, header and PDP owners

---

**Verification method.** Page and collection inventories came from the live sitemaps. All 21 pages were fetched in full; duplication was measured by 6-gram Jaccard similarity on extracted body text and independently corroborated by rendered Shopify section instance IDs, which revealed the shared template. Page-specific content was isolated from theme boilerplate to produce the "own content" word counts. Product types and tags came from live `products.json`. Traffic is GA4 property 300437005, `screenPageViews`, 90 days ending 2026-08-07. Status codes were checked with `curl -L`, using a browser user-agent where Shopify's bot mitigation required it. No Shopify mutations were performed, no guarded files were edited, and nothing was committed.
