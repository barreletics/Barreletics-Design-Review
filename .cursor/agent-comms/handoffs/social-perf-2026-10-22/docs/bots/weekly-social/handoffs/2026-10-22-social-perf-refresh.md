# Social Perf refresh handoff, 2026-10-22

- **Role:** paid social for Barreletics: Meta, Google PMax, Pinterest (TikTok later). Dashboard `barreletics/br-paid-dashboard`; Blend account `bps-2c81`. Bot `f7a36d04-6eb4-4233-a21c-91c1e01793c5`.
- **Meta is strictly look-only.** Never create, edit or pause anything without Andrew's approved plan plus his creative.
- Never touch Upgrade Your Grip, PMax or Pinterest beyond the approved routines below.
- Judge every ad on Shopify last-touch, with date range and pull time; platform numbers are claims.
- Show full content before anything is sent. Zaki messages are drafts Andrew sends himself.
- Short, plain replies. OS/GitHub writes go via Papa Grok. Store settings belong to Website bot `f1b1afce`.
- Settled items Oct 21–22: [../DECISIONS-2026-10-21-22.md](../DECISIONS-2026-10-21-22.md).
- **OPEN:** Oct 23 Meta recheck by ad/ad set; if still ~0 purchases, recommend shifting spend back to "Hear The Grip | Sep 2026"; Andrew asks Zaki about overnight changes.
- **OPEN:** Zaki's WhatsApp reply pending (Andrew sends the drafted note himself).
- **OPEN:** Zaki email draft card t29s1 still mentions Yellow Shoes; update it to Andrew's own creative.
- **OPEN:** unanswered whether to resend the fake-order protection task to Website bot `f1b1afce`.
- **OPEN:** PayPal off (Website bot / Andrew). Andrew's new creative pending.
- Managed Markets is ON and must stay on (Andrew, 2026-10-22).

## Appendix: routines (full prompts, verbatim)

## A) Daily Pinterest spend from Blend
Schedule: `CRON_TZ=America/Detroit 17 6 * * *`, flexible ±15 min.

Keep Pinterest live on the Barreletics paid ads dashboard (barreletics/br-paid-dashboard) using Blend, since the Pinterest API token is dead. Pull yesterday's (and any missing days') Pinterest spend, checkouts and checkout value via Blend blendmcp_smart_query_pinterest, account_id bps-2c81 only, ad account 549756523361. In config.json → pinterest_blend_manual, add the days to the `daily` map (and daily_checkouts/daily_checkout_value when nonzero; these are platform claims), update spend, spend_end, note and blend_window. Commit only config.json with "Pinterest spend via Blend through <date>" using $GITHUB_WRITE_TOKEN, then fire repository_dispatch event_type refresh-dashboard. Verify https://barreletics.github.io/br-paid-dashboard/data/latest.json shows Pinterest spend through yesterday. Stay quiet if it worked; message Andrew only if it failed or Blend returned incomplete data.

## B) Grok Restore Winner budget review
Schedule: exact one-offs `CRON_TZ=America/Detroit 0 9 24 10 *` and `0 9 31 10 *`.

Pinterest campaign "Grok Restore Winner" (626760082398), ad account 549756523361, Blend account bps-2c81. On Oct 17, 2026, Andrew approved setting it to $25/day, the level the old Feb 2025 winner held for months; it is the only live Barreletics Pinterest sales campaign. Pinterest guidance: leave it unchanged 7–14 days, then raise 20–30% only if results hold. Each run: read the campaign's status and budget, the last 7 days of Pinterest spend, checkouts and value, and Shopify orders with UTM campaign 626760082398 (Shopify Admin API via client_credentials with env SHOPIFY_GROK_ADMIN_CLIENT_ID/SECRET; never print or save secrets). Oct 24 run: report only, change nothing. Oct 31 run: if both the Oct 17–23 and Oct 24–30 windows show Shopify ROAS of about 2.0 or higher, and the budget is still $25 and the campaign ACTIVE, raise the daily budget to $31 and re-read to verify; otherwise hold and say why with exact numbers. Never touch any other campaign, never touch Meta. Report to Andrew in this chat in 1–2 short sentences with exact numbers. Delete this routine after the Oct 31 run.

## C) Oct 30 budget check-in email to Andrew and Zaki
Schedule: exact `CRON_TZ=America/Detroit 0 9 30 10 *`. Draft card only, never send.

On Oct 30, 2026, Andrew asked for a check-in email to himself (andrew@barreletics.com) and Zaki (zak.ghouri@gmail.com) about raising the Pinterest budget. First, look at the actual numbers for Pinterest campaign "Grok Restore Winner" (626760082398, ad account 549756523361, Blend account bps-2c81) and "Pinterest | US | Sales | Winners | Oct 2026" (626760011313): status, budget, spend, and Pinterest-reported checkouts and ROAS since Oct 17, 2026. Read only; change nothing. Then prepare the email as a draft card for Andrew to review and send himself (do not send it). Subject: "Pinterest budget check-in". Body, warm and plain, no dashes, signed Grok: open with "Hey guys, checking in. This is Grok." Then say you might want to raise the budget to $30 a day if it's performing, but look at it first. Then say "I looked at it. Here's what's happening:" with the real verified numbers, then "Based on this, ..." and state honestly whether the numbers support increasing the budget. Exact numbers only, no guesses. Deliver the draft card to Andrew in this chat.
