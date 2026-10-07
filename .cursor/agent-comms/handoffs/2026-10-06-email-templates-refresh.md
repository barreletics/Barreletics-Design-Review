# Email Templates refresh — 2026-10-06 (old bot 60505f59-6766-4da6-b461-7d81d9de1fb7)

## Role
Barreletics lifecycle / welcome / campaign / abandoned-cart emails (Marketing lane). Owns Shopify Messaging templates + Flow email workflows only. Writes paste-ready copy/HTML (Messaging has no API). Sibling One-off Emails owns one-off vendor/partner/prospect mail — not this bot.

## Sidebar
Section: **Marketing** (id `section-mu3yyrzg-4`). Name: Email Templates. Keep same description as old profile (lifecycle, welcome, campaign, abandoned-cart; start from shared memory + this handoff).

## Access
- Store: `barreletics.myshopify.com` admin in box Chrome (Sidekick + Flow UI). No Shopify Admin API token on box for discounts.
- **No Mac control** for Shopify (token-saving). Prefer Sidekick / paste-ready HTML; browser only when needed.
- Prior handoff (Oct 2): repo `barreletics/Barreletics-Design-Review` branch `grok/handoff-email-templates`, `.cursor/agent-comms/handoffs/2026-10-02-email-templates-refresh.md` — superseded by this file for refresh.

## Guardrails (standing)
- Touch **only** email workflows / automations / campaigns. **Never** eFulfillment/returns flows or the theme.
- Built/edited names get `[GROK]` prefix; retire = rename `OLD – not used …`, never delete.
- **Nothing on/off / publish without Andrew’s yes** in the same conversation.
- Email locks: logo header; white footer `255 East Brown Street, ste 310, Birmingham MI 48009`; name/address 10px `#8A8A8A`, other footer 12px `#8A8A8A`, Unsubscribe 12px `#666666` underlined; rust `#C45C3F` buttons; no “Barreletics” in subjects; say “barre and Pilates”.
- Run skill `email-go-live-checklist` before any go-live paste.
- Wholesale shipping terms are **PRIVATE** (Help Scout wholesale template only) — never site, FAQ, ManyChat, or marketing emails.
- Sidekick cannot reliably read Flow; use screenshots for waits/conditions. Flow draft → live needs **Apply changes** (not just Sidekick “save”).
- Usage: pause big work at 70%, hard stop at 80% (20% reserved for automations). Prefer Cursor for heavy HTML; keep replies short.

## Live status (as of 2026-10-05)
- **`[GROK] Abandoned Checkout – All customers (3-email)`** — Active, firing. Waits **4h / 20h / 24h**. Creates `SAVE10-…` codes (verified: usage limit 1, once per customer, no combining with shipping/product/order discounts).
- **`[GROK] Welcome Series`** — Active. **Fixed 2026-10-05 12:09 PM ET:** first condition is now **Default email address marketing state is equal to SUBSCRIBED** (old tag gate newsletter / shopify-forms-769328 / POWR / Save 10 Welcome removed). Trigger + 3 emails + 2×24h waits + 0-order checks unchanged. New site Subscribe signups should get the series; optional: watch next run to confirm send.
- Also Active (leave alone unless asked): `[GROK] Abandoned Cart 4 Hours` (filters CART abandonment so it doesn’t double-send with checkout series), `[GROK] Abandoned product browse`, and historically `[GROK] Customer Winback – SAVE2`, `[GROK] First-purchase upsell`.

## Open items
1. Confirm a post-fix Welcome Series run actually sends (Andrew was offered; no yes yet).
2. **10% OFF banner** on all-customers cart emails — asked Oct 5; never inspected live HTML; unanswered (skip unless he asks).
3. Optional tidy: inactive leftovers without full OLD rename (`[GROK] TEMP – copy of 3-email…`, `[TEST-6415]…`, Unique 10% variants, Messaging templates GROK AC Email 1/2/3).
4. Still unverified from earlier audit (not blocking): automatic discount `0-Wholesale-Shipping` restricted to wholesale customers only (can stack with SAVE10 if not). Partner Codes / discounts bot territory if pursued.
5. October campaign calendar (Oct 1/8/15 etc.) — was pending; don’t invent without Andrew.

## Routines
None. (Oct 5 cart-banner reminder was one-off and deleted.)

## Group chats
None known.

## Do not
- Rescan / re-audit all Flows on first turn.
- Turn workflows on/off or Apply changes without Andrew’s yes.
- Put wholesale shipping in any marketing email.
- Touch eFulfillment/returns or theme.
- Re-open the 10% banner question unless he asks.

## First message for new bot
Read your handoff at `/workspace/handoffs/2026-10-06-email-templates-refresh.md` and STATUS.md if present. Do not rescan or re-audit. Wait for one task.
