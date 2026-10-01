# 09 — Collection Template Reference

All collection templates live in `templates/`. Each is a JSON template that composes existing sections — no new sections were created for sub-collections (D-032).

---

## Template Inventory

| Template File | Assigned To | Section Count |
|---------------|-------------|---------------|
| `collection.json` | Base / Shop All (grippy shoes) | 8 |
| `collection.apparel.json` | Apparel | 8 |
| `collection.closed-sole.json` | Closed Sole | 5 |
| `collection.gift-cards.json` | Gift Cards | 3 |
| `collection.limited-editions.json` | Limited Editions | 4 |
| `collection.new-arrivals.json` | New Arrivals | 4 |
| `collection.one-offs.json` | One-Offs | 4 |
| `collection.open-sole.json` | Open Sole | 5 |
| `collection.outdoor.json` | Outdoor | 5 |
| `collection.sale.json` | Sale | 4 |

---

## Template Selection Logic

Shopify assigns a template to a collection via the template suffix in **Shopify Admin → Collections → [Collection] → Theme template**. The suffix maps to the filename:

```
collection.json               ← suffix: (none / default)
collection.closed-sole.json   ← suffix: closed-sole
collection.gift-cards.json    ← suffix: gift-cards
collection.limited-editions.json ← suffix: limited-editions
...
```

---

## Section Composition per Template

### `collection.json` (Base / Shop All — grippy shoes)

```
collection-hero      ← "Two Versions. One Performance." + sole comparison cards
value-strip
variant-grid         ← show_all_tab: true, products_per_page: 16
disciplines
fifty-fifty-grip     ← "Never Loses Grip." on cream bg
fifty-fifty-commit   ← "Commit to the Gear." reversed layout
geo-section          ← "Built for every studio discipline" (barre, reformer, pilates, yoga)
newsletter
```

This is the only template with `show_sole_cards: true` in the collection-hero, rendering the Open Sole / Closed Sole comparison cards with descriptions. It is also the only template with `show_all_tab: true` in variant-grid and the only one that includes the `disciplines` and dual `fifty-fifty` sections.

### `collection.apparel.json` (Apparel — `/collections/apparel`)

```
collection-hero      ← "Performance Apparel Engineered to Move!" · no sole cards
value-strip
variant-grid         ← Yoga Pants + T-Shirts tabs · no M/L filter · no Compare · apparel size chart
fullbleed-workout    ← "BRING YOUR WORKOUT TO LIFE"
fifty-fifty-tees     ← Performance Fabric V-Neck & Tank
fifty-fifty-think-outside ← Think Outside the Sock → grippy shoes
reviews              ← pdp-reviews · store scope
collection-faq       ← Apparel FAQ (sizing / care / returns)
```

Live content authority: `https://barreletics.com/collections/apparel`. Structure follows Collection v18 shop-first spine (hero → value → grid → mid proof → reviews → FAQ) without grippy-shoe sole education. Assign theme template suffix **`apparel`** on the Apparel collection in Admin after push.

### `collection.closed-sole.json`

```
collection-hero      ← eyebrow "Closed Sole", show_sole_cards: false
value-strip
variant-grid         ← collection: "closed-sole", show_all_tab: false
geo-section          ← "Why studios choose Closed Sole" (reformer, barre, lagree, sizing)
newsletter
```

### `collection.open-sole.json`

```
collection-hero      ← eyebrow "Open Sole", show_sole_cards: false
value-strip
variant-grid         ← collection: "open-sole", show_all_tab: false
geo-section          ← "Why studios choose Open Sole" (barefoot, yoga, mat, sizing)
newsletter
```

### `collection.outdoor.json`

```
collection-hero      ← "From Beach to Boat Deck"
value-strip
variant-grid         ← collection: "outdoor", show_all_tab: false
geo-section          ← "Where Outdoor grippy shoes perform" (beach, boat, travel, care)
newsletter
```

### `collection.new-arrivals.json`

```
collection-hero      ← "Just Dropped"
value-strip
variant-grid         ← collection: "new-arrivals", show_all_tab: false
newsletter           ← "Never miss a drop" / "New arrivals, direct to your inbox."
```

### `collection.limited-editions.json`

```
collection-hero      ← "Limited Runs. Unlimited Grip."
value-strip
variant-grid         ← collection: "limited-editions", show_all_tab: false
newsletter           ← "First access" / "Be the first to know."
```

### `collection.one-offs.json`

```
collection-hero      ← "One of a Kind"
value-strip
variant-grid         ← collection: "one-offs", show_all_tab: false
newsletter
```

### `collection.sale.json`

```
collection-hero      ← "Performance on Sale"
value-strip
variant-grid         ← collection: "sale", show_all_tab: false
newsletter           ← "Sale alerts" / "Know before it sells out."
```

### `collection.gift-cards.json`

```
collection-hero      ← "Give the Gift of Grip"
variant-grid         ← collection: "gift-cards", products_per_page: 8, show_all_tab: false
newsletter
```

This is the only template that omits `value-strip`.

---

## Section Reuse Matrix

| Section | Base | Closed | Open | Outdoor | New | Limited | One-Offs | Sale | Gift Cards |
|---------|------|--------|------|---------|-----|---------|----------|------|------------|
| `collection-hero` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `value-strip` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `variant-grid` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `disciplines` | ✓ | — | — | — | — | — | — | — | — |
| `fifty-fifty` | ✓ (×2) | — | — | — | — | — | — | — | — |
| `geo-section` | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — |
| `newsletter` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Filtering: `variant-grid` Section

The `variant-grid` section renders a tab-based product grid. Key settings per template:

| Setting | Type | Description |
|---------|------|-------------|
| `show_all_tab` | boolean | When `true`, shows an "All" tab alongside category tabs. Only enabled on the base `collection.json` |
| `products_per_page` | integer | Number of products displayed. 16 for most; 8 for gift cards and the PDP cross-sell grid |
| `collection` | string | Collection handle to pull products from. Absent in base template (uses the page's own collection) |
| `eyebrow` | text | Small text above the grid title |
| `title` | text | Grid heading |
| `body` | text | Description below heading |
| `view_all_url` | url | Optional "View all" link |

---

## Collection Hero Differences

The `collection-hero` section is shared across all templates but configured differently per collection:

| Template | Eyebrow | Title | Sole Cards |
|----------|---------|-------|------------|
| Base | "Two Versions. One Performance." | "Shop All Styles & Colors" | **Yes** (with Open/Closed descriptions) |
| Closed Sole | "Closed Sole" | *(empty — uses collection title)* | No |
| Open Sole | "Open Sole" | *(empty)* | No |
| Outdoor | "Outdoor" | "From Beach to Boat Deck" | No |
| New Arrivals | "New Arrivals" | "Just Dropped" | No |
| Limited Editions | "Limited Edition" | "Limited Runs. Unlimited Grip." | No |
| One-Offs | "One-Offs" | "One of a Kind" | No |
| Sale | "Sale" | "Performance on Sale" | No |
| Gift Cards | "Gift Cards" | "Give the Gift of Grip" | No |

---

## GEO Section Variations

Four templates include `geo-section` with collection-specific Q&A blocks:

| Template | Heading | Q&A Topics |
|----------|---------|------------|
| Base | "Built for every studio discipline" | Barre, Reformer, Pilates, Yoga |
| Closed Sole | "Why studios choose Closed Sole" | Reformer, Barre, Lagree, Sizing |
| Open Sole | "Why studios choose Open Sole" | Barefoot diff, Yoga, Mat Pilates, Sizing |
| Outdoor | "Where Outdoor grippy shoes perform" | Beach, Boat/paddleboard, Travel, Care |

Each GEO block uses `type: "geo_item"` with `question` and `answer` (HTML) settings, rendered as accordion Q&A pairs.

---

## Newsletter Variations

Most templates use the default newsletter copy. Three templates customize it:

| Template | Eyebrow | Title |
|----------|---------|-------|
| New Arrivals | "Never miss a drop" | "New arrivals, direct to your inbox." |
| Limited Editions | "First access" | "Be the first to know." |
| Sale | "Sale alerts" | "Know before it sells out." |

---

## Cross-References

- `variant-grid` section implementation → section source files
- GEO section accordion pattern → [06-javascript-architecture.md](06-javascript-architecture.md)
- Collection-hero styling → [07-css-architecture.md](07-css-architecture.md) (inline styles per section)
- D-032: all sub-collection templates reuse existing sections → decision log
