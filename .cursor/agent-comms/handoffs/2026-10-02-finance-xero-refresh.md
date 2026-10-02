# Finance · Xero handoff (2026-10-02)

- Role: Barreletics day-to-day Xero (bills, bank, Documents) and sole owner of Gmail invoice/receipt intake. Draft first; confirm before money moves.
- Xero API: Custom Connection via curl, creds /home/box/.xero_creds (line1 id, line2 secret), client_credentials; tenant e22b5378-9953-4c8c-a4b4-d28217bf4272. Never use XERO_CLIENT_SECRET env. API can't reconcile.
- Accounts: Chase Ink 4473 = 1204 (default for emailed charges); Checking 5003 = 1201 (EFS, Retrofit, Melio); Visa 7072 not in Xero (file only, flag).
- Paid receipts = AUTHORISED Spend Money with receipt attached, total incl tax, card checked, dup check (same vendor ±7d, ±10%), GET-verify, then forward to xero.inbox.odvh5w.i9lfpm55iqjd5ugu@xerofiles.com + green "In Xero Documents" label + star. Never ACCPAY for paid charges; ACCPAY only for unpaid AP (Melio; Andrew pays).
- Documents copy of an API-booked entry: archive it (Create transaction would duplicate). Andrew reconciles 4473; tell him when entries are ready.
- 9/30 audit: 46 labeled threads checked; 8 bad entries deleted, Jukebox -> $159, Amazon 9098124 -> $131.30. 10/2 catch-up booked Manychat $39 (86f2bf40).
- Waiting on Andrew: Hilliards $39.69 + Post Tavern $119.57 (Visa 7072); Melio fee $1.44 (1201?); EFS 581862/583396/581090; PDS 16712 $1,660 + 16713 $942.02 (PO-2001, charge unconfirmed); old duplicate DRAFT bills to delete; Upwork $183.30 date (7/31?).
- 10/2 scheduled run failed (cause unconfirmed; likely creds file timing). Watch Monday's run.

## Routine (move to new bot)
Name: Daily invoice → Xero Files
Schedule: CRON_TZ=America/Detroit 59 7 * * 1-5 (weekdays 7:59 AM ET)
Prompt:
```
Daily Barreletics invoice/receipt sweep. I am the sole owner of Gmail invoice/receipt intake (Daily Gmail no longer does this). Goal: every paid invoice/receipt emailed to Andrew is filed in Xero Documents AND booked correctly as Spend Money on the paying account — filing alone is not done.

Scope: only messages received since the previous successful run (if the last run failed, go back to the last successful one; on Monday include the weekend). Do not re-review older mail or recap old chats.

Access: Gmail connector (discover tools each run). Xero via Custom Connection API with curl: creds in /home/box/.xero_creds (line1 client id, line2 secret), client_credentials token from identity.xero.com, tenant e22b5378-9953-4c8c-a4b4-d28217bf4272. Never use the XERO_CLIENT_SECRET env var. Xero Documents filing address: xero.inbox.odvh5w.i9lfpm55iqjd5ugu@xerofiles.com.

Steps:
1. Find in-scope invoice/receipt emails (incl. Trash/archived, since Andrew deletes/archives) without the green "In Xero Documents" label. Skip noise (ops reports, shipping notices, settlements, remittances/incoming money).
2. Extract vendor, date, TOTAL INCLUDING TAX (never the pre-tax subtotal), reference/order/invoice number, and card last-4 on the receipt.
3. Card check: default paying account Chase Ink ···4473 (code 1204). If the receipt clearly shows a different card (e.g. Visa ···7072, not in Xero), do NOT book — file only and flag. EFS/Retrofit/Melio are paid from Checking ···5003 (1201); if the paying account is unclear, flag instead of guessing.
4. Duplicate check before booking: search non-deleted Xero BankTransactions and ACCPAY bills for the same vendor within ±7 days and within 10% of the total, or same reference. If any possible match exists, don't create — flag with IDs.
5. Book: AUTHORISED SPEND BankTransaction on the paying account, Total exactly equal to receipt total incl. tax, reference = invoice/order number, receipt attached. Never create ACCPAY for already-paid charges; for genuinely unpaid invoices, check for an existing bill, else create a DRAFT ACCPAY.
6. Verify via GET that Total, account, date, reference, attachment match. Only then forward the receipt to the Xero Documents address and apply the green "In Xero Documents" label + star. If verification fails, fix or flag; don't label.
7. Never reconcile, never delete, never email anyone else.

Report to Andrew only if something was booked or needs him, in at most 5 short bullets (what was booked: vendor, amount, account; what's flagged and why). Stay silent if nothing new. If a step fails (auth, connector), say exactly what failed in one line.
```
