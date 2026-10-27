# Barreletics: product changes on Oct 22, 2026 and how they relate to checkout (read-only audit)
Pulled 5:25 PM ET Oct 22 via Admin GraphQL 2025-07. Nothing was modified. Raw data: /workspace/pc/*.json

## Bottom line
- Only **2 products** have an updatedAt on Oct 22 (ET). In both cases the cause is routine, not a shipping change:
  1. **Super-High Rise Reinforced Knee Yoga Tight**, updated 12:47:57 PM ET. The only thing changed today is the `judgeme.widget` metafield (Judge.me review widget refresh, 12:47:56 PM ET). No variant or inventory item on this product changed today.
  2. **Best Grippy Shoes, Open Sole**, updated 12:47:57 PM ET (same Judge.me widget refresh) and again at 3:55:07 PM ET. The 3:55 PM update matches order #6017 (OS-LG-Yellow, paid 3:54 PM ET): variant OS-LG-Yellow updatedAt 3:55:08 PM ET, inventory decrement. Variant OS-LG-RG updatedAt 11:40:59 AM ET matches order #6016.
- **No weight, requiresShipping, HS code, origin, price or status changes today.** Every inventoryItem updatedAt is Oct 15 or earlier (Open Sole: Jun 12 / Jul 15; Yoga Tight: Oct 12–15).
- **No calcurates, shipping or dimension metafields exist** on either product or any of their variants.
- **Shipping rates were still being quoted today.** Each of today's 4 US abandoned checkouts has total = subtotal + $9.95, the "Standard Shipping" flat rate (the MI one also includes tax). US buyers were getting a rate and then not paying. So for US checkouts, the evidence goes against "rates broke because of product fields."
- Confidence that today's product edits caused the drop: **low (~10%)**.

## Per-variant snapshot (current)
**Open Sole** (ACTIVE, published 2019): 18 variants, all priced $74.00. All have weight 3.0 POUNDS, requiresShipping=true, tracked=true, origin US, HS 640299, province null, countryHarmonizedSystemCodes empty, taxable=true, inventoryPolicy DENY. compareAt is $74.00 (equal to price) on most and null on OS-MED-White, OS-LG-White and OS-LG-Blue. Barcode is null on OS-MED-RG, OS-MED-DB, OS-LG-RG and OS-LG-DB. Locations are Barreletics, eFulfillment Center and Old Stock. Odd but old: OS-MED-White shows Barreletics available = -1; Old Stock has 46 on_hand for LG-DGY.
**Yoga Tight** (ACTIVE): 8 variants at $89.00, compareAt $129.00, weight 2.5 POUNDS, requiresShipping=true, tracked, US, HS 610463. Policy is CONTINUE, except YP-LG-Black (DENY, 0 stock).
Metafields: global SEO, mm-google-shopping, mc-facebook, judgeme, reviews, custom, pbc_wholesale, spofSteps, quick; variant-level mpn / harmonized_system_code / hide_from_storefront / stock_label. The only one updated today is judgeme.widget on both products, at 12:47 PM ET.

## Flags (none are new today)
- Weights look high: 3 lb for a pair of grip shoes, 2.5 lb for leggings. If Calcurates rates by weight or uses dimensional/box rules, these values (plus **no dimension metafields**) could inflate or block its quotes once it is put into a zone. Not a change from before today.
- compareAt equals price ($74/$74) on Open Sole, so there's no real "sale" shown. Cosmetic.
- No product has compare-at lower than price. No status or publish changes.
- Comparison with past orders: SKUs sold Oct 15–22 (OS-*, CS-*, YP-*) carry the same weights now, and inventoryItem updatedAt dates are older than those orders, so the weights were the same before today.

## Carrier services and delivery profiles
- carrierServices: **Calcurates (via app)** is active, callbackUrl hidden. **Flat rates by Shopify Managed Markets** is also active.
- **Calcurates is not attached to any zone method** in either delivery profile, so it is not producing rates at checkout right now.
- General profile (96 variants):
  - US zone: Standard $9.95, Free Shipping 3-9 Day $0 (conditional), USPS Priority $16.95, FedEx Ground Economy $14.95, fedex calculated (+90%).
  - AK/HI/PR: USPS Ground Advantage $16.95 and usps calculated.
  - Intl (45 countries): fedex, ups, dhl (calculated).
  - MX: dhl_ecommerce.
- "New Test Profile" (24 variants): only the "TEST CS-*" Closed Sole Test Item.

## Shipping lines on orders, Oct 15–22 (ET)
- US: almost every order used **Standard Shipping $9.95** (source shopify). Exceptions: Free Shipping 3-9 Day $0 on #5945, #5991 and #6010, plus custom $0 lines on #5947, #5999 and #6016.
- #5957 (CA, Oct 15): "Standard" $5.21, source Managed Markets (managed-markets-fedex).
- #5948–5955 (Oct 15, 12:53–1:00 PM ET): 8 refunded TEST orders to CA/MX/GB/AE/SA/ES/IT/BR, FedEx International Connect Plus $31–58.
- No Calcurates-sourced shipping titles on any order. No change in rate titles or prices through #6017 (3:54 PM ET today).
- #6015 (11:21 AM ET today, US): VOIDED with no shipping line.

## Abandoned checkouts, Oct 22 (ET)
| Created (ET) | Ship to | Subtotal | Total | Implied shipping |
|---|---|---|---|---|
| 12:55 AM | CA-AB | 76.94 | 112.14 | intl rate + duties/tax |
| 9:53 AM | FR | 91.82 | 128.29 | intl (Managed Markets) |
| 1:45 PM | US-DE | 152.00 | 161.95 | $9.95 Standard |
| 1:50 PM | US-DE | 74.00 | 83.95 | $9.95 Standard |
| 3:14 PM | US-NY | 74.00 | 83.95 | $9.95 Standard |
| 4:21 PM | US-MI | 89.00 | 104.29 | $9.95 + tax |
Shipping-line detail isn't available on abandonedCheckouts, so these amounts are inferred from totals. The two DE checkouts are probably the same shopper.

## What could break rates at checkout
- None of today's product changes. They are review-widget metafields and inventory decrements from sales.
- Possible risk, not yet active: a Calcurates rollout that changes zone methods, or the app using the heavy weights and missing dimensions.
- Next things to check, not visible via this API scope: the Shopify admin activity log for shipping/checkout settings changes at the 12:56 PM ET shop update, checkout extensions, payment method issues (the US buyers saw a rate, so the failure may be at payment), and Managed Markets duties for intl.
