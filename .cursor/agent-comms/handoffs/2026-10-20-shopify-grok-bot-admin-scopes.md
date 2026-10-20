# Grok Bot Admin: Shopify scopes (2026-10-20)

The app lives in the Shopify **Dev Dashboard** (dev.shopify.com), not the Partner Dashboard. It uses the client_credentials grant (env SHOPIFY_GROK_ADMIN_CLIENT_ID/SECRET).

## Released 2026-10-20 ~8:43 AM ET (Andrew)
Full scope list on the new version (a new version REPLACES the old scopes, so always keep the full list):
read_markets,write_markets,read_shipping,write_shipping,read_orders,write_orders,read_products,write_products,read_inventory,write_inventory,read_publications,write_publications,read_locations,read_all_orders,read_reports,read_customers,read_analytics

Added this time: read_all_orders, read_reports, read_customers, read_analytics.

## Status at 8:43 AM ET
The token still only returns the old scopes (write_markets,write_shipping,write_orders,write_products,write_inventory,write_publications,read_locations). The new version isn't active until the store approves it.

## Remaining step
In Shopify admin (barreletics.myshopify.com/admin) go to Settings, then Apps, then Grok Bot Admin, and approve the updated permissions. Then re-check the token scopes. If read_all_orders is refused, it needs Shopify's approval for full order history, and protected customer data (name, email, phone, address) may need its own request in the app's settings.

## Why
Without read_all_orders the app only sees the last 60 days of orders, so Shopify can't verify Meta's Feb–Apr 2026 results.
