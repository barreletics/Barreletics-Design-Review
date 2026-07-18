# M4A Redirect Map

---
document: M4A Redirect Map
status: 🔵 Ready for Review
created: 2026-07-18
depends_on: [09-collection-architecture, 11-navigation-architecture, 12-seo-geo-standards]
---

## Purpose

301 redirect map from current live site URLs to new theme URLs. Ensures no indexed URLs return 404 after theme switch. All redirects are permanent (301) to preserve SEO equity.

---

## Methodology

- Current URLs derived from live theme template files and Shopify admin structure
- New URLs derived from Doc 09, Doc 11, and Doc 12 specifications
- Product URLs are expected to remain unchanged (same handles in Shopify admin)
- Collection and page URLs change where handles differ

---

## Collection Redirects

| Old URL | New URL | Type | Notes |
|---------|---------|------|-------|
| `/collections/barre-pilates-yoga-shoe-sock-footwear` | `/collections/grippy-shoes` | 301 | Primary collection — main pillar page |
| `/collections/shop-all-products` | `/collections/grippy-shoes` | 301 | Legacy all-products page |
| `/collections/shop-favorites` | `/collections/grippy-shoes` | 301 | Legacy favorites |
| `/collections/collection-landing` | `/collections/grippy-shoes` | 301 | Legacy landing |
| `/collections/apparel-page` | `/collections/apparel` | 301 | Legacy apparel handle |

## Page Redirects

| Old URL | New URL | Type | Notes |
|---------|---------|------|-------|
| `/pages/compare-open-vs-closed` | `/pages/compare-open-closed-sole` | 301 | Handle change |
| `/pages/shipping-retruns` | `/pages/shipping` | 301 | Typo in old handle + split |
| `/pages/start-a-retrun` | `/pages/returns` | 301 | Typo in old handle |
| `/pages/outdoor` | `/collections/outdoor` | 301 | Page → Collection |
| `/pages/aquatic-footwear` | `/collections/outdoor` | 301 | Page → Collection |
| `/pages/shop-bundles` | `/collections/grippy-shoes` | 301 | Removed page |
| `/pages/become-an-affiliate` | `/pages/ambassador` | 301 | Renamed program |
| `/pages/wholesale-calculator` | `/pages/wholesale` | 301 | Consolidated |
| `/pages/bogo-template` | `/collections/sale` | 301 | Promo → Sale collection |
| `/pages/size-chart` | `/pages/size-guide` | 301 | Handle change |
| `/pages/blank-page` | `/` | 301 | Remove placeholder |
| `/pages/free-people` | `/collections/collaborations` | 301 | Collab → collection |

## Blog Redirects

| Old URL | New URL | Type | Notes |
|---------|---------|------|-------|
| `/blogs/blog` | `/blogs/journal` | 301 | D-009: Blog → Journal rename |
| `/blogs/blog/*` | `/blogs/journal/*` | 301 | All articles under old blog |

## Product Redirects

| Old URL | New URL | Type | Notes |
|---------|---------|------|-------|
| (none expected) | — | — | Product handles remain unchanged in Shopify admin |

**Current product handles (unchanged):**
- `studio-performance-skin-footwear` (Open Sole)
- `best-reformer-pilates-legree-workout-shoes` (Closed Sole)
- `aquatic-performance-skins` (Outdoor)
- `barreletics-x-coperni-closed-sole` (Coperni collab)
- `lightly-padded-knee-yoga-pant-black` (Apparel)

---

## Product Template Redirects

Old theme used multiple product templates; new theme uses a single canonical `product.json`. No URL changes needed — Shopify routes by handle regardless of template assignment.

**Templates being retired (no redirect needed — same URL, different template):**
- `product.in-studio-template.json`
- `product.in-studio-reformer-pilate.json`
- `product.coperni.json`
- `product.one-off.json` / `product.one-off-open.json` / `product.one-off-closed.json`
- `product.aquatic-template.json`
- `product.brand-story.json`
- `product.yoga-pants.json`
- `product.v-neck-tops.json`
- `product.preorder.json`
- `product.gift-card.json`
- `product.product-landing.json`

---

## Implementation

Redirects are implemented in Shopify Admin > Online Store > Navigation > URL Redirects.

**Bulk import format (CSV):**
```
Redirect from,Redirect to
/collections/barre-pilates-yoga-shoe-sock-footwear,/collections/grippy-shoes
/collections/shop-all-products,/collections/grippy-shoes
/collections/shop-favorites,/collections/grippy-shoes
/collections/collection-landing,/collections/grippy-shoes
/collections/apparel-page,/collections/apparel
/pages/compare-open-vs-closed,/pages/compare-open-closed-sole
/pages/shipping-retruns,/pages/shipping
/pages/start-a-retrun,/pages/returns
/pages/outdoor,/collections/outdoor
/pages/aquatic-footwear,/collections/outdoor
/pages/shop-bundles,/collections/grippy-shoes
/pages/become-an-affiliate,/pages/partners
/pages/wholesale-calculator,/pages/partners
/pages/wholesale,/pages/partners
/pages/ambassador,/pages/partners
/pages/studio-program,/pages/partners
/pages/bogo-template,/collections/sale
/pages/size-chart,/pages/size-guide
/pages/blank-page,/
/pages/free-people,/collections/collaborations
/blogs/blog,/blogs/journal
```

---

## Redirect Verification Audit

> **Final redirect implementation requires Owner sign-off. Items flagged for Brian review must be resolved before M4D Launch.**

### Collection Redirects

| Source URL | Destination URL | Still Necessary? | Redirect Chains? | Redirect Loops? | SEO Concerns | Requires Owner/Brian Review? |
|-----------|----------------|-------------------|-------------------|-----------------|--------------|------------------------------|
| `/collections/barre-pilates-yoga-shoe-sock-footwear` | `/collections/grippy-shoes` | Yes | No | No | High-equity URL — must 301 | No |
| `/collections/shop-all-products` | `/collections/grippy-shoes` | Yes | No | No | None | No |
| `/collections/shop-favorites` | `/collections/grippy-shoes` | Yes | No | No | None | No |
| `/collections/collection-landing` | `/collections/grippy-shoes` | Yes | No | No | None | No |
| `/collections/apparel-page` | `/collections/apparel` | Yes | No | No | None | No |

### Page Redirects

| Source URL | Destination URL | Still Necessary? | Redirect Chains? | Redirect Loops? | SEO Concerns | Requires Owner/Brian Review? |
|-----------|----------------|-------------------|-------------------|-----------------|--------------|------------------------------|
| `/pages/compare-open-vs-closed` | `/pages/compare-open-closed-sole` | Yes | No | No | None | No |
| `/pages/shipping-retruns` | `/pages/shipping` | Yes | No | No | Typo correction — SEO positive | No |
| `/pages/start-a-retrun` | `/pages/returns` | Yes | No | No | Typo correction — SEO positive | No |
| `/pages/outdoor` | `/collections/outdoor` | Yes | No | No | Page→Collection type change | **Yes** — verify outdoor collection exists with products |
| `/pages/aquatic-footwear` | `/collections/outdoor` | Yes | No | No | Page→Collection type change | **Yes** — verify outdoor collection exists with products |
| `/pages/shop-bundles` | `/collections/grippy-shoes` | Yes | No | No | Bundle concept removed | No |
| `/pages/become-an-affiliate` | `/pages/partners` | Yes | No | No | Updated: now routes to consolidated partners page | No |
| `/pages/wholesale-calculator` | `/pages/partners` | Yes | No | No | Updated: now routes to consolidated partners page | No |
| `/pages/bogo-template` | `/collections/sale` | Unknown | No | No | Promo page — may no longer exist | **Yes** — confirm sale collection exists |
| `/pages/size-chart` | `/pages/size-guide` | Yes | No | No | None | No |
| `/pages/blank-page` | `/` | Yes | No | No | Remove placeholder | No |
| `/pages/free-people` | `/collections/collaborations` | Unknown | No | No | Collab may be inactive | **Yes** — confirm collaboration status |
| `/pages/wholesale` | `/pages/partners` | Yes | No | No | D-042: consolidated partners page | No |
| `/pages/ambassador` | `/pages/partners` | Yes | No | No | D-042: consolidated partners page | No |
| `/pages/studio-program` | `/pages/partners` | Yes | No | No | D-042: consolidated partners page | No |

### Blog Redirects

| Source URL | Destination URL | Still Necessary? | Redirect Chains? | Redirect Loops? | SEO Concerns | Requires Owner/Brian Review? |
|-----------|----------------|-------------------|-------------------|-----------------|--------------|------------------------------|
| `/blogs/blog` | `/blogs/journal` | Yes | No | No | Blog equity preservation | No |
| `/blogs/blog/*` | `/blogs/journal/*` | Yes | No | No | Individual articles need per-entry redirects (no wildcard support) | **Yes** — article inventory needed |

### Product Redirects

| Source URL | Destination URL | Still Necessary? | Redirect Chains? | Redirect Loops? | SEO Concerns | Requires Owner/Brian Review? |
|-----------|----------------|-------------------|-------------------|-----------------|--------------|------------------------------|
| (none expected) | — | — | — | — | Product handles unchanged | No |

### Flagged for Owner/Brian Review

1. **Outdoor collection redirect** — `/pages/outdoor` and `/pages/aquatic-footwear` redirect to `/collections/outdoor`, but collection must exist with products before redirect goes live
2. **Sale collection** — `/pages/bogo-template` → `/collections/sale` requires sale collection to exist
3. **Collaborations** — `/pages/free-people` → `/collections/collaborations` requires confirmation collaboration is still active/relevant
4. **Blog articles** — Each article under `/blogs/blog/` needs individual redirect entry; Shopify has no wildcard support. Full article inventory required before implementation.
5. **Partner page consolidation** — Old `/pages/wholesale`, `/pages/ambassador`, `/pages/studio-program` all redirect to `/pages/partners` per D-042

---

## Post-Publish Verification Plan

After theme publish:
1. Test each redirect with `curl -I` to confirm 301 status
2. Monitor Google Search Console for 404 errors (daily for 7 days)
3. Check Google Search Console Coverage report for crawl errors
4. Verify no redirect chains (A → B → C should be A → C)

---

## Risk Notes

- Blog article redirects (`/blogs/blog/*` → `/blogs/journal/*`) require wildcard or individual entries per article
- Shopify does not support wildcard redirects natively — each blog article needs its own redirect entry
- Articles must be moved to the new "Journal" blog in Shopify admin, which changes their URL automatically
- If articles are simply moved to the `journal` blog, Shopify handles the redirect automatically
