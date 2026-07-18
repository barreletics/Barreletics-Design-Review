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
| Wholesale | `wholesale` | `/pages/wholesale` |
| Ambassador | `ambassador` | `/pages/ambassador` |
| Studio Program | `studio-program` | `/pages/studio-program` |

## Blog Handle

| Blog | Handle | URL |
|------|--------|-----|
| Journal | `journal` | `/blogs/journal` |

## Shopify Admin Implementation Notes

1. **Main menu** — Create in Navigation > Add menu > Handle: `main-menu`
2. **Footer menu** — Not used as a Shopify menu; footer is hardcoded in `snippets/footer.liquid` per Doc 11 structure (4-column grid doesn't map to Shopify's flat menu model)
3. **Collection creation** — All collections above must exist in Shopify admin before theme deployment
4. **Page creation** — All pages above must exist with correct handles before navigation links work
5. **Blog creation** — Blog named "Journal" with handle `journal` must exist

## Current Live Site → New Mapping

| Current Live Handle | New Handle | Action |
|--------------------|------------|--------|
| `barre-pilates-yoga-shoe-sock-footwear` | `grippy-shoes` | Create new, redirect old |
| (none — single collection template) | `open-sole` | Create new |
| (none) | `closed-sole` | Create new |
| (none) | `outdoor` | Create new |
| (none) | `apparel` | Create new |
| (none) | `tops` | Create new |
| (none) | `bottoms` | Create new |
| `compare-open-vs-closed` | `compare-open-closed-sole` | Create new, redirect old |
