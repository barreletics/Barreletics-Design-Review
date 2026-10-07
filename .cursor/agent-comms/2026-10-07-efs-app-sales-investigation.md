# eFS app & sales investigation — Oct 7, 2026

Handoff for Cursor. Sources: `/workspace/efs-golive-check/` (app-impact.md, NOTES.md, previous-connection-timeline.md) and `/workspace/checkout-tests/` (log.csv T1–T19, http_sweep.md). Read-only Shopify work unless noted. Times ET.

## Verdict

About **90% that the eFS app is NOT hurting sales.** The drop is in traffic (social plus a fading international ad test), not checkout. International sessions went from **113 → 50/day** starting Sep 28. US checkout completion without Michigan test traffic was **63% before vs 61% after**.

The open **10%**: the app location's settings can't be viewed, and the timing coincides with the Sep 28 reinstall. The only definitive test is to uninstall for a few days and watch sales.

## Checkout tests (T1–T19) & HTTP sweep

- Regular carts (US + CA/GB/AU/DE/ES/AE) get rates and reach payment. Global-e handles international inside Shopify checkout.
- **One Off Colors** (both products) caused the international "not available for delivery" / empty shipping-rates block (T11; HTTP sweep isolation). Andrew set them to **Draft**; they **404 as of 10:55 AM ET**.
- **Coperni L → Canada** also fails (T14). Likely in shipping profile **"New Test Profile"** (24 products, ships from Barreletics only); that profile's International zone has **no rates**.
- Gift-card test orders, all Closed Sole M Black, all went through; Global-e accepts Shopify gift cards. Being cancelled, restocked, refunded to the cards:
  - #5867 US $88.39
  - #5868 CA CAD 163.17
  - #5869 DE EUR 118.88
  - #5870 AE AED 426.30

## Admin read-only check

- **2 markets:** International (Managed/Global-e; 59 regions, 136 rates, 46 regions shipping) and United States.
- **13 regions with no rates** (months, per Andrew): Aruba, Bahamas, Barbados, Bermuda, BVI, Costa Rica, Dominica, Dominican Republic, Greenland, Honduras, Martinique, Panama, St. Barthélemy.
- **Product eligibility 7/8.** Unsupported: "SAMPLE ITEMS - NOT FOR SALE".
- **General** profile ships from Barreletics and eFulfillment Center. App location **"Efulfillment Service - 2015"** is not in any shipping profile ("Start shipping", not enabled), not in any market, and has no Locations detail page.
- #5869 and #5870 assigned to Barreletics, not on hold.
- **No order has ever been assigned** to app location `114571313443` (created when the app was reinstalled Sep 28 2026).

## Sales / funnel (PRE Sep 14–27 vs POST Sep 29–Oct 6)

- Drop is upstream of checkout; US paid regular orders were already down the week before install vs the Sep 14–20 spike.
- US checkout→order excl. Michigan: **63% (108/171) PRE vs 61% (45/74) POST**.
- Intl sessions/day **113 → 50**; intl paid regular orders **16 → 3**. Sample too small to call checkout.
- Fulfillment normal: all POST regular orders FULFILLED manually from eFulfillment Center or Barreletics; none at the app location; none ON_HOLD (except known ReturnZap/test cases).
- Prior Apr 2026 blackouts were routing + Managed Markets conflicts, not a documented connector-only failure.

## Open items

- Fix Coperni international, or Draft it.
- New Test Profile's international zone has no rates.
- App Shopify scopes missing: `write_products`, `write_orders`, `read_markets`, `read_shipping`.
