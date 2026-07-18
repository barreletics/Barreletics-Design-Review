# M4A Navigation Configuration

---
document: M4A Navigation Configuration
status: 🔵 Ready for Review
created: 2026-07-18
depends_on: [11-navigation-architecture, 09-collection-architecture]
---

## Purpose

Exact Shopify navigation menu configuration mapping Doc 11 (Navigation Architecture) to Shopify admin menu structure. Ready for direct implementation in Shopify admin > Online Store > Navigation.

---

## Main Menu (`main-menu`)

```
Grippy Shoes                        → /collections/grippy-shoes
├── Shop All                        → /collections/grippy-shoes
├── Open Sole                       → /collections/open-sole
├── Closed Sole                     → /collections/closed-sole
├── Outdoor                         → /collections/outdoor
└── Compare Styles                  → /pages/compare-open-closed-sole

Apparel                             → /collections/apparel
├── Shop All Apparel                → /collections/apparel
├── Tops                            → /collections/tops
└── Bottoms                         → /collections/bottoms

Collaborations                      → /collections/collaborations

Journal                             → /blogs/journal
```

## Footer Menu (`footer`)

```
Shop
├── All Grippy Shoes                → /collections/grippy-shoes
├── Open Sole                       → /collections/open-sole
├── Closed Sole                     → /collections/closed-sole
├── Outdoor                         → /collections/outdoor
└── Apparel                         → /collections/apparel

Support
├── FAQ                             → /pages/faq
├── Shipping                        → /pages/shipping
├── Returns                         → /pages/returns
├── Warranty                        → /pages/warranty
└── Contact Us                      → /pages/contact

Company
├── About Us                        → /pages/about
├── Journal                         → /blogs/journal
├── Collaborations                  → /collections/collaborations
└── Compare Styles                  → /pages/compare-open-closed-sole
```

## Collection Handle Map

| Collection | Handle | URL | Type |
|-----------|--------|-----|------|
| All Grippy Shoes (pillar) | `grippy-shoes` | `/collections/grippy-shoes` | Manual + Automated |
| Open Sole | `open-sole` | `/collections/open-sole` | Automated (tag: open-sole) |
| Closed Sole | `closed-sole` | `/collections/closed-sole` | Automated (tag: closed-sole) |
| Outdoor | `outdoor` | `/collections/outdoor` | Automated (tag: outdoor) |
| New Arrivals | `new-arrivals` | `/collections/new-arrivals` | Automated (date-based) |
| Limited Editions | `limited-editions` | `/collections/limited-editions` | Automated (tag: limited-edition) |
| One-Offs | `one-offs` | `/collections/one-offs` | Automated (tag: one-off) |
| Gift Cards | `gift-cards` | `/collections/gift-cards` | Automated (product type: Gift Card) |
| Sale | `sale` | `/collections/sale` | Automated (compare_at_price > price) |
| All Apparel | `apparel` | `/collections/apparel` | Automated (product type: Apparel) |
| Tops | `tops` | `/collections/tops` | Automated (tag: tops) |
| Bottoms | `bottoms` | `/collections/bottoms` | Automated (tag: bottoms) |
| Collaborations | `collaborations` | `/collections/collaborations` | Manual |

## Page Handle Map

| Page | Handle | URL |
|------|--------|-----|
| FAQ | `faq` | `/pages/faq` |
| About | `about` | `/pages/about` |
| Contact | `contact` | `/pages/contact` |
| Shipping | `shipping` | `/pages/shipping` |
| Returns | `returns` | `/pages/returns` |
| Warranty | `warranty` | `/pages/warranty` |
| Size Guide | `size-guide` | `/pages/size-guide` |
| Compare Open vs Closed Sole | `compare-open-closed-sole` | `/pages/compare-open-closed-sole` |
| Grip Comparison | `grip-comparison` | `/pages/grip-comparison` |
| Technology | `technology` | `/pages/technology` |
| Partner Programs | `partners` | `/pages/partners` |
| ~~Wholesale~~ | ~~`wholesale`~~ | ~~`/pages/wholesale`~~ → redirects to `/pages/partners` (D-042) |
| ~~Ambassador~~ | ~~`ambassador`~~ | ~~`/pages/ambassador`~~ → redirects to `/pages/partners` (D-042) |
| ~~Studio Program~~ | ~~`studio-program`~~ | ~~`/pages/studio-program`~~ → redirects to `/pages/partners` (D-042) |

## Blog Handle

| Blog | Handle | URL |
|------|--------|-----|
| Journal | `journal` | `/blogs/journal` |

## Shopify Admin Implementation Notes

1. **Main menu** — Create in Navigation > Add menu > Handle: `main-menu`
2. **Footer menu** — Not used as a Shopify menu; footer is hardcoded in `snippets/footer.liquid` per Doc 11 structure (4-column grid doesn't map to Shopify's flat menu model)
3. **Collection creation** — D-043: Create collections ONLY when products/merchandising require them. Templates are ready (from M3). Do NOT batch-create all 13 collections immediately — create each collection in Shopify admin only when there are actual products to populate it.
4. **Page creation** — All pages above must exist with correct handles before navigation links work
5. **Blog creation** — Blog named "Journal" with handle `journal` must exist
6. **Partner page consolidation** — D-042: `/pages/wholesale`, `/pages/ambassador`, and `/pages/studio-program` are superseded by unified `/pages/partners`. Old handles redirect to partners page.

## Current Live Site → New Mapping

> **D-043:** Collections are created ONLY when products/merchandising require them. Templates exist and are ready. Do not batch-create all collections.

| Current Live Handle | New Handle | Action |
|--------------------|------------|--------|
| `barre-pilates-yoga-shoe-sock-footwear` | `grippy-shoes` | Create when ready, redirect old |
| (none — single collection template) | `open-sole` | Create only when products/merchandising require it |
| (none) | `closed-sole` | Create only when products/merchandising require it |
| (none) | `outdoor` | Create only when products/merchandising require it |
| (none) | `apparel` | Create only when products/merchandising require it |
| (none) | `tops` | Create only when products/merchandising require it |
| (none) | `bottoms` | Create only when products/merchandising require it |
| `compare-open-vs-closed` | `compare-open-closed-sole` | Create new page, redirect old |
