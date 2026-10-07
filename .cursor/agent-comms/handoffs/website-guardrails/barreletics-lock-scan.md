---
name: Barreletics lock scan
description: >-
  use this on any Barreletics page before push — sitewide lock scan; pair with
  no-drift push gate; Shop All ruler for grid-open 72/56
---
# Barreletics lock scan (sitewide)

## When
On any page refine, before every draft push, or “does this match the lock?”

**Always pair with** [Barreletics no-drift push gate](sand-workflow:barreletics-no-drift-push-gate) before claiming a visual match.

## Ruler: Shop All
Grid-open under-nav: `--pad-grid-page-open` **72** / mobile **56**. Copy — never invent.

## Catalog
`planning/locks/` · `planning/NO-DRIFT-PROCESS-LOCKED.md` (includes drift autopsy)

Scanner: `python3 scripts/lock-scan.py`

## Steps
1. Run scanner on the template.
2. Report FAIL only.
3. Fix without weakening locks.
4. Pull-verify after push.
5. For pad/media/type: measure vs ruler before “OK.”

## Output
`FAIL: …` or `OK — matches lock`.
