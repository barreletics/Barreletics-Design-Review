# M4A Pre-Deployment Baseline

---
document: M4A Pre-Deployment Baseline
status: 🔵 Ready for Review
created: 2026-07-18
depends_on: [MILESTONES-4-5-6-ROADMAP §9]
---

## Purpose

Documents the current production state for comparison after theme switch. This is the "before" snapshot that validates no regressions occur during deployment (§9 of the Roadmap).

---

## Current Product Inventory

| Handle | Title | Type | Status |
|--------|-------|------|--------|
| `studio-performance-skin-footwear` | Studio Performance Skin (Open Sole) | Performance Skin | Active |
| `best-reformer-pilates-legree-workout-shoes` | Studio Performance Skin (Closed Sole) | Performance Skin | Active |
| `aquatic-performance-skins` | Aquatic Performance Skins (Outdoor) | Performance Skin | Active |
| `barreletics-x-coperni-closed-sole` | Barreletics × Coperni (Closed Sole) | Performance Skin | Active |
| `lightly-padded-knee-yoga-pant-black` | High-Rise Reinforced-Knee Yoga Pant | Apparel | Active |

**Total active products:** 5
**Product handles verified:** Unchanged between old and new theme

---

## Current Collection Inventory (Live Site)

| Handle | Products | Template |
|--------|----------|----------|
| `barre-pilates-yoga-shoe-sock-footwear` | All Performance Skins | `collection.json` |

**Note:** Live site uses a single collection with product-level filtering via the `br-variants` section. The new theme introduces sub-collections (open-sole, closed-sole, outdoor, etc.) per Doc 09.

---

## Current Page Inventory (Live Site)

| Handle | Title | Template |
|--------|-------|----------|
| `compare-open-vs-closed` | Compare Open vs Closed | `page.compare-open-vs-closed.json` |
| `free-people` | Free People | `page.free-people.json` |
| `faq` | FAQ | (from snapshots) |
| `contact` | Contact | (from snapshots) |
| `about` | About | (from snapshots) |
| `shipping-retruns` | Shipping & Returns | (from snapshots) |
| `start-a-retrun` | Start a Return | (from snapshots) |
| `outdoor` | Outdoor | (from snapshots) |
| `aquatic-footwear` | Aquatic Footwear | (from snapshots) |
| `become-an-affiliate` | Become an Affiliate | (from snapshots) |
| `wholesale-calculator` | Wholesale Calculator | (from snapshots) |
| `size-chart` | Size Chart | (from snapshots) |
| `shop-bundles` | Shop Bundles | (from snapshots) |
| `blank-page` | Blank Page | (from snapshots) |
| `bogo-template` | BOGO Template | (from snapshots) |

---

## Current Blog/Article Inventory

| Blog Handle | Blog Title | Article Count |
|-------------|-----------|---------------|
| Unknown (likely `blog`) | Blog/Journal | Unknown — requires Shopify admin verification |

---

## Current URL Structure Summary

### Indexed URLs (from theme templates)

| Pattern | Example | Count |
|---------|---------|-------|
| Homepage | `/` | 1 |
| Products | `/products/studio-performance-skin-footwear` | 5 |
| Collections | `/collections/barre-pilates-yoga-shoe-sock-footwear` | ~5 |
| Pages | `/pages/faq`, `/pages/about`, etc. | ~15 |
| Blog | `/blogs/blog` | 1 |
| Blog articles | `/blogs/blog/[article-handle]` | Unknown |

**Estimated total indexed URLs:** 30–50

---

## Current Theme Information

| Item | Value |
|------|-------|
| Theme name | Custom (likely Stiletto or modified base) |
| Theme ID | Requires Shopify admin access |
| Last modified | Active as of July 2026 |
| Backup status | ☐ Full .zip backup needed before M4D |

---

## Analytics Baseline

| Metric | Source | Status |
|--------|--------|--------|
| Monthly sessions | GA4 (Property 300437005) | ☐ Owner to pull 30-day report pre-launch |
| Conversion rate | GA4 | ☐ Owner to pull |
| Revenue by channel | GA4 | ☐ Owner to pull |
| Top landing pages | GA4 | ☐ Owner to pull |
| Core Web Vitals (CrUX) | Chrome UX Report | ☐ Check pre-launch |
| Search Console impressions | GSC | ☐ Owner to pull |
| Search Console indexed pages | GSC | ☐ Owner to pull |

**Note:** Builder can pull GA4 data via the `user-google-analytics` MCP during M4B, but the baseline should be frozen before any changes begin. Recommend Owner exports this data before M4D.

---

## Review Baseline

| Metric | Source | Status |
|--------|--------|--------|
| Total reviews (all products) | Judge.me | ☐ Pull from Judge.me dashboard |
| Average rating | Judge.me | ☐ Pull from Judge.me dashboard |
| Reviews per product | Judge.me | ☐ Pull per-product breakdown |

---

## Verification Checklist (Pre-Deployment)

This checklist must be verified AGAIN immediately before M4D (Launch):

- [ ] All product handles confirmed unchanged
- [ ] All redirects entered in Shopify admin
- [ ] Full theme backup (.zip) downloaded
- [ ] GA4 baseline frozen (30-day snapshot)
- [ ] Search Console baseline frozen (indexed pages, impressions)
- [ ] Judge.me review count baseline recorded
- [ ] Rollback plan tested (can unpublish new theme and revert)
- [ ] DNS configuration verified
- [ ] Payment gateway tested (test mode)

---

## Items Requiring Owner Action

| Item | Why | When |
|------|-----|------|
| GA4 30-day export | Baseline comparison post-launch | Before M4D |
| Search Console export | Indexed pages baseline | Before M4D |
| Judge.me dashboard export | Review count baseline | Before M4D |
| Full theme .zip backup | Rollback capability | Before M4D |
| DNS verification | Domain routing confirmation | Before M4D |
