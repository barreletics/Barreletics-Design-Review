# Partner codes handoff — 2026-10-06

Written for Grok Bot token-emergency compaction. Agent: Partner codes (`e0045ba0-6ca6-4671-b0f8-94640322191b`). Do **not** hide this chat yet.

## Section / role

- **Chat name:** Partner codes (renamed from Barreletics Andrea)
- **Owner:** Andrew John / Barreletics
- **Scope:** Private `0-` influencer/partner discount codes + manual commission tracking. Not theme QC. Not Admin Cloudflare/auth workflows.
- **Store:** `barreletics.myshopify.com`
- **Tone:** coffee-blurt terse; don’t invent UI paths; don’t retry box Cloudflare loops

### Locked offer rules (Andrea pattern — reuse for future partners)

- Customer **10% off**; matching **10% commission** paid manually on orders that used her code (usually amount **after** discount)
- `appliesOncePerCustomer: true`
- **30-day** window; **reissue** a new `0-` code if continuing
- **Not** new-customers-only
- Create codes **INACTIVE** until Andrew activates
- No paid affiliate apps; Ambassadors footer stays Coming soon / removed
- Naming: prefix `0-` (Shopify has no folders); Flow category in **CAPS** first (e.g. `PARTNER CODES`)

## Live code (verified 2026-10-06 ~19:04 EDT via Mac Shopify CLI)

| Field | Value |
|---|---|
| Code | `0-ANDREAMINSKI` |
| DiscountCodeNode | `gid://shopify/DiscountCodeNode/1631277711651` |
| Status | **ACTIVE** |
| startsAt | `2026-09-13T14:58:10Z` |
| endsAt | `2026-10-14T03:30:58Z` (Oct 13 EOD Eastern) |
| appliesOncePerCustomer | true |
| Admin | https://admin.shopify.com/store/barreletics/discounts/1631277711651 |
| Cart test | https://barreletics.com/discount/0-ANDREAMINSKI |

Auth for CLI: Mac machine, store auth as `stefanie@barreletics.com` (write_discounts / read_discounts). Box Cloudflare blocks Admin — use Mac CLI or Andrew’s browser, never box Admin loops.

## Shopify Flow — PARTNER CODES expiry alert

- **Name pattern:** `PARTNER CODES — Email team when partner code expires` (or similar; category CAPS)
- **Trigger:** Scheduled time daily **9am Eastern**
- **Steps:** Get discount data → Run code (JS filter: endsAt past and ≤24h from scheduledAt) → Send internal email to **support@** + **team@**
- **Subject:** static (list titles in body — do **not** use `{{runCode.expiredCodes.title}}` alone; that broke on lists)
- **Notes/tag:** `grok-partner-codes`
- **Abandoned path:** Discount Expired trigger needed uninstalled third-party connector — do not revive
- **Sidekick:** must not touch/delete other Flows; user deletes bad PARTNER CODES drafts himself
- **Open:** confirm Flow is **ON** while `0-ANDREAMINSKI` is live

## Calendar backup

- **Title:** PARTNER CODES — 0-ANDREAMINSKI expired · pay Andrea commission
- **When:** all-day **Oct 13, 2026**
- **Attendees:** andrew@barreletics.com + stefanie@barreletics.com
- **Event id:** `rp1je07n60lv2mn2flos9ptsgs`
- **Link:** https://www.google.com/calendar/event?eid=cnAxamUwN242MGx2Mm1uMmZsb3M5cHRzZ3MgYW5kcmV3QGJhcnJlbGV0aWNzLmNvbQ
- Google Calendar connector: **connected**

## Partner email (Stefanie sends)

- Draft ready for Stefanie (brand/ops) to send — **do not send until Andrea’s personal email is on file**
- Subject: `Your Barreletics partner code is ready`
- Covers: code live, 10% off + matching commission, once per customer, Sep 13–Oct 13 2026, commission at window end / reissue if continuing
- Optional BCC support@ / team@
- Gmail connectors are now connected (default + stefanie + personal accounts as of handoff write) — still **Stefanie sends**, not this bot, unless Andrew explicitly asks

## Commission process (window end)

1. Filter Shopify orders by discount code `0-ANDREAMINSKI` for the window
2. Commission = **10% of amount after discount** on those orders (manual)
3. Pay Andrea; if continuing, create a **new** inactive `0-` code and activate for next 30 days
4. Optional mid-window tally anytime

## Routines

**None.** This agent has no scheduled/event routines (`automation_status`: You have no routines).

## Groups / rooms

**None** owned by this agent for partner-codes work. Sibling context:
- Admin workflows / Cloudflare: separate chat (do not use this one)
- Primary coordinator: Grok Bot (`aa3b203e-439b-4c78-b271-222e1cbb46ba`)

## Connectors relevant here (status at handoff)

- Shopify-mcp: connected
- Google Calendar: connected
- Gmail (default + stefanie + personal variants): connected
- Google Drive: connected
- Do **not** use box browser for Shopify Admin (Cloudflare)

## Open items

1. **Andrea Minski personal email** — still unknown; blocks Stefanie send
2. **Confirm PARTNER CODES Flow is ON** in Shopify Admin
3. **Oct 13 (or shortly after endsAt) commission tally** — filter orders by code, 10% after discount, pay, decide reissue
4. Optional: mid-window tally before expiry (~7 days left as of 2026-10-06)
5. Future partners: same pattern; create inactive first; Flow naming CAPS

## Do not

- Hide this chat yet (Grok Bot instruction)
- Send Andrea email until email address + Andrew/Stefanie ready
- Retry box Cloudflare Admin auth loops
- Let Sidekick delete/edit unrelated Flows
- Limit codes to new customers only
- Install paid affiliate apps for this

## Success criteria for next owner

- Handoff path known to Grok Bot
- Chat stays visible
- On/after Oct 13: commission paid + reissue decision recorded
- Andrea email sent once address known
