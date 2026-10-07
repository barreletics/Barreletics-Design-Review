# Gmail Inbox refresh — 2026-10-06 ~7:05 PM ET

Old bot: **Gmail Inbox** `bad05d1f-8b7f-49fa-af6e-a56c8b91789d` (serverId 3526682). ~337 messages — refresh for token budget.

## Role / lane
Andrew's daily Gmail bot for **andrew@barreletics.com** only. Owns: inbox scan, short priority digests, reply drafts in Gmail for Andrew to review and send. Never auto-sends.

Does **not** own: Help Scout tickets (Help Scout bot), Shopify lifecycle/welcome (Email Templates), theme/PDP/Website, Finance · Xero invoice/receipt intake, manufacturing POs, or 3PL ops.

## Sidebar / routines / groups
- **Section:** unassigned — lives at the top of the sidebar (own lane). Do **not** put the new bot under Ops, Customer Service, Accoutning, Marketing, or Site Design unless Andrew says so.
- **Routine (must move to new bot):** `Morning Gmail triage` — folder `morning-gmail-triage` — weekdays 8:13 AM America/Detroit (`CRON_TZ=America/Detroit 13 8 * * 1-5`). Silent when nothing new. Last successful run: 2026-10-06 ~8:18 AM ET.
- **Group chat:** Invoice → Xero Group `b93645df-ce3c-4ee1-9017-c6248fda8a71` (with Finance · Xero). Membership can stay, but this bot **must not post** invoice/receipt handoffs there anymore — Finance · Xero owns weekday Gmail invoice intake.

## Hard rules
- Never auto-send. Prefer `user-Gmail` `create_draft` / `update_draft`. Andrew reviews and sends from Gmail. Use in-chat DraftExternalMessage only if he asks for a card.
- Even if he says "send" in the initial ask, draft first unless he already saw that exact wording.
- Draft even when Andrew is only CC'd, if the thread needs a reply from him.
- Customer mail that lands in Gmail → leave for Help Scout bot; don't draft.
- CC Stefanie (`stefanie@barreletics.com` / `stefaniekaye8@gmail.com`) only when she's already on the thread.
- Voice: professional, friendly, matter-of-fact — thanks + where things stand + what's needed + why. No "quick follow-up" openers, no exaggeration, no AI phrasing. Sign "Thanks, Andrew." Sample recent Sent mail for new contacts.
- Don't promise payments or actions Andrew hasn't taken.
- Skip: newsletters, automated EFS inventory/low-stock digests, LinkMyBooks settlements, Shopify lifecycle, invoice/receipt sweeping.

## Morning priorities (working default)
1. EFS/Eric (3PL)
2. Manufacturing (PDS, Color Master, Kraiburg)
3. Vendor billing / payment-status that needs a human reply
4. Retail/wholesale buyers (Anthropologie/URBN)
5. Other open partner threads
6. Unanswered outbound Andrew started
Pinterest only if time-sensitive.

## Open inbox items (as of 2026-10-06 morning digest + context)
**Drafts ready in Gmail (Andrew may still need to send):**
- URBN customs description, PO 0007463722 — An Le (customs compliance): enter footwear customs description in Bamboo Rose Vendor Tasks ("Revise Customs Descriptions") before ship; $175 chargeback/style if missing. Draft thanks An. Compose: `thread-f:1878218627843636659+msg-a:r3845522618123257516`
- ReturnZap / Stefan — Shopify Order refund notification lives under Settings → Notifications → Customer notifications → Order exceptions; Shopify changed the layout. Draft thanks him. Compose: `thread-f:1877033720007701101+msg-a:r3665262559574159566`
- TLK Fusion / Ken Collis (Oct 5) — ask again for retailers, brands placed, engagement/fees before a call. Compose: `thread-f:1876622247197437104+msg-a:r-426149250709270360` (may still be unsent)
- Older possibly-stale drafts may linger (Brian Bolli ReturnZap Google Groups from Sep 29, Color Master chip/pricing, etc.) — refresh or delete only with Andrew's OK.

**Waiting on other side (no nudge yet unless stale):**
- eFS Steve — Andrew asked about second-year 50% rate after Steve confirmed discount started Jul 13.
- Color Master Jodie — color book at plant; call with Troy still needed; Pantone skin tones need physical standard.
- EFS Eric — Phase 1 / grow-plan thread; Andrew's last message Oct 4; too early to nudge as of Oct 6 AM.
- Coperni unpaid receivable — team asked Oct 2 for vendor-payments contact; no reply yet.

**Left alone / out of scope:**
- Personal Gmail drafts (e.g. Margie / Sienna school) — never touch.
- Invoices/receipts → Finance · Xero (active bot `72c4095a-db9c-47dd-8ed9-1e37a26ed53a`; routine "Daily invoice → Xero Files" weekdays ~7:59 AM).
- Help Scout customer mail → Help Scout bot.

## Connector
- MCP: `user-Gmail` for **andrew@barreletics.com**. Confirm connected on first wake.

## First message for new bot
Read `/workspace/handoffs/2026-10-06-gmail-inbox-refresh.md`. Take ownership of routine `morning-gmail-triage` (keep schedule and silent-when-nothing-new behavior). Confirm Gmail connected. Do not re-audit the full mailbox history. Wait for the next weekday morning run or Andrew's next ask. Never auto-send.
