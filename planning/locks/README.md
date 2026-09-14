# Barreletics locks (source of truth index)

Machine-readable: `*.lock.json` + `sitewide.lock.json`  
Human letters: `*-LOCKED.md` in this folder  
Scanner: `python3 scripts/lock-scan.py .` from repo root

## Confirmed page / block letters

| Lock | File |
| --- | --- |
| Coperni PDP | [COPERNI-PDP-LOCKED.md](./COPERNI-PDP-LOCKED.md) |
| Open Sole Chair Pose yellow | [OPEN-SOLE-CHAIR-POSE-LOCKED.md](./OPEN-SOLE-CHAIR-POSE-LOCKED.md) |
| Soft cream sitewide | [CREAM-SOFT-LOCKED.md](./CREAM-SOFT-LOCKED.md) |
| Trusted by footer dark | [TRUSTED-BY-DARK-LOCKED.md](./TRUSTED-BY-DARK-LOCKED.md) |
| FAQ Background cream default | [FAQ-BG-LOCKED.md](./FAQ-BG-LOCKED.md) |
| Sitewide tokens / guarantee / cream / chair | [sitewide.lock.json](./sitewide.lock.json) |
| Shop All | [shop-all.lock.json](./shop-all.lock.json) |
| Grid page-open | [grid-page-open.lock.json](./grid-page-open.lock.json) |

Cursor alwaysApply rules under `.cursor/rules/*LOCKED*.mdc` and `chair-pose-yellow-fit.mdc` mirror these. Prefer letter + lock-scan over memory.
