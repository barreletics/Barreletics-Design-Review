# Finance · Xero refresh handoff — 2026-10-21

Saved on main in barreletics/alternate-projects, commit 07dfc5e:
- docs/bots/accounting/HOME.md: open items, pending sends, routines
- docs/bots/accounting/DECISIONS.md: the 2026-10-20/21 section
- docs/bots/accounting/year-end-2026/: Mike write-offs sheet (xlsx/docx/build_writeoffs.py), mileage log, Stefanie reimbursement draft, PDS 16311/16576/16591 PDFs
- docs/bots/DECISIONS.md: 2026-10-21 Finance line
- Tax strategy (year-end-2026/year-end-tax-strategy-2026.md) was already on main at 694baf6, not in 07dfc5e (the box copy is unchanged)
- Follow-up commit: HOME.md $1,000-note fix item + this handoff at docs/bots/accounting/handoffs/

Xero creds: /home/box/.secrets/xero.env (chmod 600). Use the direct API with client_credentials. Never copy the values.

## Routines (full saved prompts, verbatim)

### Daily invoice → Xero Files (weekdays ~7:59 AM ET, cron 59 7 * * 1-5)
Scan andrew@barreletics.com Gmail for new vendor invoices and payment receipts since the last run (or last 2 days), including Updates, Promotions and trash (skip spam). Skip Melio payment confirmations, marketing, and anything already sent to Xero Documents (xero.inbox.odvh5w.i9lfpm55iqjd5ugu@xerofiles.com). Follow the Invoice email to Xero Documents skill. For each genuine invoice/receipt: if a real vendor PDF or image is attached, send that file to the xerofiles inbox. If the email is HTML-only or link-only (always the case for Upwork receipts and eFulfillment invoice emails), screenshot the real vendor email and send that image to the xerofiles inbox; never skip Upwork or eFulfillment as link-only. Every email sent to Xero Documents gets Gmail labels "In Xero Documents" and "Xero" and is archived (labels stay). Never create bills for already-paid items; match or create a bill only when amount, vendor and bank/card line are a 100% fit, otherwise leave in Review. Tell Andrew briefly what was sent; stay quiet if nothing new. Never pay, approve, reconcile, or delete.

### Weekly 4473 sweep (Mondays ~8:23 AM ET, cron 23 8 * * 1)
Check Stefanie's Barreletics email (user-Gmail--stefanie, including trash, Updates and Promotions; skip spam and her personal Delta card) and her Amazon orders for anything charged to Chase Ink 4473 since the last run that isn't in Xero yet (Xero account 1204). Skip duplicates. Add only items clearly missing, as unreconciled Spend Money with a unique memo "Vendor YYYY-MM-DD $X.XX — note"; send invoices to Xero Documents per the Invoice email to Xero Documents skill and label them "Xero" (plus "In Xero Documents" if sent) and archive. Never reconcile or delete. Message Andrew only when you added something, found a duplicate, or need his decision; otherwise stay quiet.

### Owner reimbursement reminder (1st and 15th ~9:17 AM ET, cron 17 9 1,15 * *)
Remind Andrew to pay down what Barreletics owes him. Using the Xero API (source /home/box/.secrets/xero.env for XERO_CLIENT_ID/XERO_CLIENT_SECRET, client_credentials token, tenant e22b5378-9953-4c8c-a4b4-d28217bf4272), list his unpaid AUTHORISED ACCPAY bills on contact Andrew Nehra (109faa55-2f32-4096-a6e2-7b9f3be4f2bc) with their total, plus Checking 1201 and Chase Ink 1204 balances. Suggest a safe amount to pay this round (keep a cash cushion after the card balance and upcoming bills). Remind him how: transfer from Chase Checking 5003 to his personal account, then match the transfer to those bills in the Xero bank feed. Never move money or reconcile. If no bills are open, stay silent.

### Xero connection check (weekdays ~7:40 AM ET, cron 40 7 * * 1-5)
Check that Xero access works before the daily invoice run. Load XERO_CLIENT_ID/XERO_CLIENT_SECRET from env, or from /home/box/.secrets/xero.env if env is empty, request a client_credentials token, and make one read call (Organisation, tenant e22b5378-9953-4c8c-a4b4-d28217bf4272). If it works, stay silent. If it fails, tell Andrew in one short line that Xero needs the client ID and secret re-entered, and send the secret request.

Rules: draft-first; never pay, reconcile or backdate; deletes only with Andrew's go; cash basis.
