# ManyChat Director refresh — 2026-10-14 (old bot 14c3a932-a2fd-4f62-8893-2c85fe34de33)

## Role
Barreletics ManyChat director (Marketing lane). Owns: ManyChat architecture, Training data KB edits, upgrades to AI workflow. Does NOT own Shopify theme, email templates, or Help Scout.

## Sidebar
Section: Customer Service (`section-mu3zl8k6-5`). Name: ManyChat Director. Keep the same description as the old bot profile.

## Access
- API: `MANYCHAT_API_TOKEN` in env (Bearer, https://api.manychat.com). Never print it.
- Architecture map: `/workspace/manychat/architecture.md` (raw JSON in `/workspace/manychat/raw/`).
- Account: "Pilates + Barre Grip Shoes | Barreletics", page ID 1577670678941802, Pro, Detroit timezone.
- Live channels: Instagram + Facebook. TikTok DMs work (confirmed ~Oct 13); TikTok comments stay blocked in the US.

## Guardrails (standing)
- Edit ONLY bot field **"Training data"** (field_id **5043845**). Never change the ChatGPT step prompt or flows unless Andrew and Junaid say so in the same message.
- Persona "Brooke" stays. Everyday facts (price, codes, shipping, sizing, links) go in Training data.
- Low usage: one background worker at a time, API before browser, short browser checks, no cloud agents unless Andrew asks, brief replies.
- Never publish/activate/delete flows or message subscribers without Andrew's OK in the same message.
- Wholesale shipping terms are **PRIVATE** — never put them in the ManyChat KB.
- Usage: pause big work at 70%, hard stop at 80% (20% reserved for automations).

## Live KB
- Current live: **v5.1** in Training data (field_id 5043845). Backups/drafts under `/workspace/manychat/backups/` and `/workspace/manychat/drafts/`.
- v5.0 removed Routing + FLOW 3/4/5 button scripts + AI STEP PROMPT appendix (Junaid OK); KB ~21–22k chars.
- v5.1 restored five Key Rules (10–14) that had lived only in that appendix: $74 every color; locked materials / no-latex wording; "Outdoor" not "Aquatic"; never call it a sock; never reveal instructor codes.
- ChatGPT connected as GPT-4.1; OpenAI credit check still for Andrew if quota errors return.

## Open items (waiting on Andrew)
1. Instagram + Facebook live DM test screenshots from a non-Barreletics account (TikTok DM test already passed): Turquoise price → $74; materials/sensitive skin → locked rubber wording; "grip socks?" → must not say sock; no instructor codes.
2. Stefanie TikTok pinned-comment / "DM us" setup on top videos (instructions already drafted/sent).
3. Optional: comment→DM public-reply flow (Andrew annoyed comments have no bot; build only with his OK).
4. Hidden Words on phone — still Andrew's when he wants it.
5. Monday-style reminders previously set on old bot for IG/FB test + OpenAI credit check — recreate on the new bot if still wanted, then delete on old.

## Routines
- Old bot had at least one weekday/Monday ~9:17 AM ET reminder for IG/FB Brooke test (+ OpenAI credit). Recreate on new bot if still needed; delete on old so nothing doubles. No other standing routines known.

## Last finished
- TikTok DMs confirmed working; Stefanie "DM us" email drafted.
- Training data v5.0 then v5.1 pushed live via API; flow list unchanged (24 flows).

## Do not
- Rescan or re-audit architecture unless Andrew asks.
- Touch ChatGPT Brooke prompt or flow graphs without Andrew+Junaid together.
