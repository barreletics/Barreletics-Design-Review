---
name: barreletics-anti-revert
description: >-
  FAIL-CLOSED anti-revert gate for Barreletics Design-Review. Blocks silent
  rollback, git restore/checkout of shopify-build, fix-drift restores, PDP thrash,
  Instagram/juicer/proof-numbers/footer/value-strip/buy-box reverts, and overwriting
  locked mocks. Auto-invoke BEFORE any edit to shopify-build/sections, templates,
  product.json, product.open-sole, pdp-buy-box, footer, home-juicer, proof-numbers,
  value-strip, index.json, freeze docs, or docs/Barreletics PDP; ALSO when the agent
  thinks "drift", "wrong", "revert", "restore older", "match freeze", "go back",
  "undo prior agent", or "clean up the mess" by rolling files back. Never invent
  review counts or sole-dash H1s while "fixing".
---

# Barreletics Anti-Revert — FAIL CLOSED

Companion rule (always-on): `.cursor/rules/anti-revert-fail-closed.mdc`  
Freeze registry: `planning/m4-section-freeze.md`  
**Page ↔ template registry:** `planning/page-template-registry.md`  
**Page QA skill (auto-invoke on page/template/handle work):** `barreletics-page-qa` → `.cursor/skills/barreletics-page-qa/SKILL.md` · `~/.cursor/skills/barreletics-page-qa/SKILL.md`  
OS sync (>1 surface): `.cursor/rules/os-sync-on-global-change.mdc`  
PDP lock: `.cursor/rules/pdp-hub-lock.mdc`

## Sense it — STOP if any of these thoughts appear

Treat as a **revert attempt** (halt) if you are about to:

- `git restore` / `git checkout` / `git show … > file` / overwrite from an older commit
- “fix drift” by putting an older composition back
- Delete Open Sole / Outdoor / reviews / partner pages “to go back”
- Match an **older** freeze row over the working tree + Andrew’s **current** message
- Flip hub PDP off v19, or overwrite `Definitive-v16` / `Definitive-v19` in place
- Reintroduce stripped copy (e.g. **10% off**)
- “Unify” by stripping signed-off buy-box fields (Complete the kit, Coming soon, trust line)
- Invent “4.9 · 2,000+ reviews” or put `— Open Sole` / `— Closed Sole` in the H1

**Wrong numbers / wrong feed / “looks off” ≠ permission to restore.** Fix forward or **ASK**.

## Supreme law

**Andrew’s CURRENT message wins** over freeze docs, prior agents, and older commits.  
Update freeze **forward**. Never restore an older freeze over his ask.  
Exact restore phrase required in the **CURRENT** message: **`restore X`**.

## Radioactive without `restore X` (CURRENT message)

| Surface | Path |
|---|---|
| Instagram / Juicer | `shopify-build/sections/home-juicer.liquid` |
| Proof numbers | `shopify-build/sections/proof-numbers.liquid` |
| Value strip / under-ATC / badges | `shopify-build/sections/value-strip.liquid` |
| Footer | `shopify-build/sections/footer.liquid` |
| Buy box | `shopify-build/sections/pdp-buy-box.liquid` |
| **One-off buy-box fold** | `product.one-off-*.json` buy-box + shared `pdp-buy-box.liquid` — **copy deltas only**; never rebuild from `product.json` or hide sold-out sizes (see `.cursor/rules/one-off-buy-box-lock.mdc`) |
| Home / PDP spines | `templates/index.json`, `product.json`, `product.open-sole.json`, `product.outdoor.json` |
| Locked mocks | `docs/Barreletics PDP - Definitive-v16.html`, `…-v19.html` |

## Mandatory gate (copy into your turn before editing guarded surfaces)

```
ANTI-REVERT GATE
- [ ] Current message does NOT ask to rollback; if it says “restore X”, restore ONLY X
- [ ] I will NOT run git restore / checkout / show>file on shopify-build or locked mocks
- [ ] I stated 1–3 lines what will change (fix-forward only)
- [ ] PDP: match v19 + current product*.json — no invented ratings; H1 has NO sole dash; **Closed/Open/Outdoor badge = rust** (never roll Closed back to black)
- [ ] If unsure → ASK. Do not thrash.
```

## PDP buy-box ground truth (do not invent)

- Trust: `Trusted by 1,000+ Instructors` (never invent review counts)
- H1: `Best Grippy Shoes for Barre, Pilates & Yoga` — **no** `— Open Sole` / `— Closed Sole`
- Lede: `Secure in every hold.` / `No sliding. No resets.`
- Badge: TE optional; **default rust** for Closed/Open/Outdoor. Explicit TE black/charcoal/rust/blue **honored** — never force over a TE pick. One-Off Closed = black · One-Off Open = rust · label **One-Off**
- Copy split: `short_description` = above price only. Description accordion = TE `description_accordion_body` (SIGNED) · **NEVER** Admin `product.description` · blank → `short_description` only. **Never** blank/unify short_description across product*.json
- Authority: `docs/Barreletics PDP - Definitive-v19.html` + `pdp-buy-box.liquid` + current `product*.json`

## Keep unless Andrew deletes (CURRENT message)

Open Sole template · Outdoor template · hybrid reviews (3 photo + 6 text) · partner/help pages · local QA harness under `planning/pdp-variants-qa/`

## Shopify

No `shopify theme push` unless Andrew names theme ID **`187144929571`** (or another disposable ID) in **that same message**. Never publish.

## Parallel agents

One writer per surface per turn. Do not reclaim another agent’s freeze/section/template by restoring older files.
