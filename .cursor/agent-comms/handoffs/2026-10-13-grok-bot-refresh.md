# Grok Bot (front desk/director) refresh — 2026-10-13 ~9:50 AM ET
Old bot: aa3b203e-439b-4c78-b271-222e1cbb46ba (Grok section). Andrew calls this role "Papa Grok"; name stays Grok Bot.
Read also: repo barreletics/Barreletics-Design-Review branch grok/handoff-grok-director, .cursor/agent-comms/handoffs/2026-10-03-grok-director-refresh-2.md (commit 4bc9d1d3, Oct 13 eFS section + old 3PL history), /workspace/handoffs/2026-10-13-efs-testing-handoff.md, /workspace/fulfillment-handoffs/EFS-MASTER-KNOWLEDGE.md, /workspace/efs-golive-check/TEST-PLAN-v2.md, EFS-FULL-RATE-MATRIX.md. Shared user memory has standing rules.
## FIRST TASK (Andrew approved)
One Shopify DRAFT order (not a website checkout) on the TEST item (SKUs "TEST CS-..."), domestic address. Check routing (eFS app location 114571313443 first, Barreletics 31315624039 second) and shipping rates vs matrix (Std $9.95 free $150+, Ground Econ $17.95, Priority $18.95, 2Day/Overnight FedEx +120%, AK/HI/PR $18.95). eFS flows aren't live; don't expect them. Item may be active but NOT shown on storefront. Change NO store settings (no Managed Markets, no locations). Don't complete/pay unless needed to see routing; report and wait for Andrew before more. Use a computerUse subagent in the box browser Shopify admin.
## Open
- Waiting on Eric's reply/call time (sent 9:26 AM; tests 11-12, meet 12+).
- EFS Go-Live bot 69cd9920: hide vs retire is Grok Bot's call; Andrew leaned hide.
- Shopify Processing 6993e6c7 owns order transfers (one test order first).
## Routines to recreate (then old bot deletes its own)
- Bot chat-size refresh and GitHub backup: 24 18 * * 1-5 ET.
- Midday bot chat-size check: 18 12 * * 1-5 ET.
- Sales + ads dashboard health check: 32 7 * * 1-5 ET.
These three routines stay on the old bot for now; Andrew will say when to move them.
