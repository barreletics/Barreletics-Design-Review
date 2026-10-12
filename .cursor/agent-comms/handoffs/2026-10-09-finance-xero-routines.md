# Routines to recreate on Finance · Xero e2453a99

## 1. Daily invoice → Xero Files — cron `59 7 * * 1-5` America/Detroit
Scan andrew@ / Barreletics Gmail for new vendor invoices and payment receipts since the last run (or last 2 days). Skip Melio payment confirmations, marketing, and anything already landed in Xero Documents / the xerofiles inbox (xero.inbox.odvh5w.i9lfpm55iqjd5ugu@xerofiles.com).
Follow the Invoice email to Xero Documents skill (screenshot-as-source for HTML-only).
For each genuine invoice/receipt:
- If a real vendor PDF or image is attached: get that file into Accounting → Documents (forward/send to xerofiles when the attach path is reliable; otherwise Upload in the Documents UI). Label with vendor + doc type + amount.
- If the email is HTML-only (e.g. DHL-style payment receipts): do NOT send a compact text PDF and do NOT rely on HTML-only forwards. Capture a screenshot of the real vendor email and Upload that PNG into Accounting → Documents → Inbox. That screenshot is the source of record.
- Link-only portal invoices (e.g. EFS): do not chase the portal unless Andrew asks; note them and skip, or use statement/export if he prefers.
- Match / Create bill only when amount + vendor + bank/card line are a 100% fit; otherwise leave in Review.
Tell Andrew what was uploaded and that the next step is Accounting → Documents (not the old go.xero.com/Docs link). Stay quiet if nothing new. Do not Melio-pay, approve, or post bills unless Andrew asks.

## 2. Owner reimbursement reminder — cron `17 9 1,15 * *` America/Detroit
Remind Andrew to pay down what Barreletics owes him. Using the Xero API (creds /home/box/.xero_creds, tenant e22b5378-9953-4c8c-a4b4-d28217bf4272), list his unpaid AUTHORISED ACCPAY bills on contact Andrew Nehra (109faa55-2f32-4096-a6e2-7b9f3be4f2bc) with their total, plus Checking 1201 and Chase Ink 1204 balances. Suggest a safe amount to pay this round (keep a cash cushion after the card balance and upcoming bills). Remind him how: transfer from Chase Checking 5003 to his personal account, then match the transfer to those bills in the Xero bank feed. Never move money or reconcile. If no bills are open, stay silent.
