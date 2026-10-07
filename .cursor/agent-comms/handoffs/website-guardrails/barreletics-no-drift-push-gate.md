---
name: Barreletics no-drift push gate
description: >-
  use this before every Barreletics draft push or before saying fixed/matched —
  ruler, lock-scan, pull-verify, measure vs ruler; never trust TE checkboxes
  alone; one axis one proof
---
# Barreletics no-drift push gate

## When
Before every Barreletics draft theme push, before telling Andrew a visual is “matched/fixed/done,” and after any section move.

## Why
Drift burns finite human minutes. Rulers exist — copy them. Prove before speaking.

## Autopsy gates (from 2026-09-12 pad drift)
Never repeat:
1. Push without lock-scan
2. Trust TE checkbox alone (Shopify strips it)
3. Say “fixed/matched” without measure vs ruler
4. Measure the wrong surface (old theme / no draft chrome)
5. Invent values instead of copying the ruler
6. Wrong editor link or wrong vocab (PDP ≠ collection)
7. Multiple false “dones” on one axis

Full table: `planning/NO-DRIFT-PROCESS-LOCKED.md`

## Steps
1. **Name the ruler** — Shop All / type-os / page `*.lock.json` / earmark doc.
2. **Lock-scan** — `python3 scripts/lock-scan.py . templates/<file>.json`. Fix FAILs. Never weaken locks.
3. **Code gate** — tokens + Liquid (`section.index`, suffix, `!important`). TE checkbox optional mirror only.
4. **Push** — named files only → draft `187144929571`.
5. **Pull-verify** — pull the same files back; confirm the change exists on remote.
6. **Prove** — measure vs ruler (computed CSS + screenshot). Confirm redesign is showing before measuring.
7. **Link** — Theme Editor `previewPath` for the page you changed only.
8. **One axis** — one proof, then one “done.” Coffee blurts.

## Say-done checklist
Ruler · scan clean · pull-verify · measured · correct link.

## Grid page-open (locked)
Shop All: `--pad-grid-page-open` 72 / mobile 56.

## Output
`ruler: …` · `lock-scan: OK|FAIL` · `pull-verify: OK` · `measured: …` · `preview: <url>`
