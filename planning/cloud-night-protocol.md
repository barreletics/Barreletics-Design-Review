# Cloud night protocol — same rules as awake desktop

**Repo:** ★ Barreletics-Design-Review · `shopify-build/`  
**Theme:** M4 Visual QA **`187144929571`** only  
**Queue:** `planning/sprint-queue.md`  
**OS:** anti-revert · freeze · Finish → Approve → Lock → Next · CURRENT MESSAGE WINS  

Cloud agents and desktop agents use **the same queue and the same stop rules**. Overnight ≠ freestyle.

---

## Hard laws (Cloud + desktop)

1. **One writer per surface per turn.** Claim a queue row; do not edit another agent’s files.  
2. **Stop at AWAITING ANDREW** — always leave M4 preview URL (or research artifact path). Never self-approve. Never LOCK without Andrew’s `approved` / `looks good` / equivalent.  
3. **Push only to `187144929571`** and only when the task letter (or queue row) authorizes push. Never publish. Never other theme IDs.  
4. **Never touch LOCKED surfaces** without explicit Andrew letter in the **current** message / queue note.  
5. **Never `git restore` / checkout** guarded `shopify-build` paths to “fix drift.” Fix forward or ASK.  
6. **Copy laws:** no “fully enclosed”; no pool positioning; sole preference/feel only.  
7. **Home (Track D)** starts only when B+C have no open AWAITING rows for PDP globals.  
8. **Help (Track A):** never guess variation — pick list first (`help-pages-variation-index.md`).  
9. **Global PDP changes:** log `planning/pdp-global-changelog.md` → Track C sync sweep.  
10. **Ambassador (Track E):** research doc only until Andrew approves plan — no app install.

---

## Claiming a row (Cloud)

1. Read `planning/sprint-queue.md`  
2. Pick highest-priority **QUEUED** row you are allowed to own (different files from desktop IN PROGRESS)  
3. Set Owner = `cloud` · Status = `IN PROGRESS`  
4. Read anti-revert skill before any `shopify-build/` edit  
5. Execute only that row  
6. Status → `AWAITING ANDREW` + preview/artifact link  
7. Stop. Do not start the next track’s blocked work.

---

## Awake morning handoff

Andrew opens the queue, batch-reviews AWAITING rows on M4, replies `approved` or `fix X` per row. Agents lock forward, then take next QUEUED rows.

---

## Cloud setup notes

- Launch Cloud agents **from this repo** with base branch that exists on remote (e.g. `finish-home-collections` or `main` as configured).  
- Uncommitted local work is **not** on the Cloud VM — commit/push queue docs before overnight if Cloud must see them, or regenerate from letter.  
- Prefer Cloud for: research (E), audits, read/report, isolated page implementations after Andrew picks.  
- Prefer desktop for: live TE eyeball with Andrew, push+immediate visual QA loops.
