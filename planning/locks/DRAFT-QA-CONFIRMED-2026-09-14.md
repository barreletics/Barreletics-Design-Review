# Draft QA CONFIRMED — 2026-09-14

**Andrew:** black closeout kills it; everything checked out; lock it; guardrails on.  
**Branch:** `finish-home-collections`  
**Draft theme only:** `187144929571` (never live `185687998755`)

## Confirmed stack (do not regress)

| Item | Lock letter / machine |
| --- | --- |
| Soft cream `#faf8f6` only (Help Quick Answers + sitewide) | [CREAM-SOFT-LOCKED.md](./CREAM-SOFT-LOCKED.md) |
| Trusted by footer **dark** (black / white) | [TRUSTED-BY-DARK-LOCKED.md](./TRUSTED-BY-DARK-LOCKED.md) |
| FAQ Background default **cream** | [FAQ-BG-LOCKED.md](./FAQ-BG-LOCKED.md) |
| Open Sole Chair Pose P5A4949 COVER · 360 | [OPEN-SOLE-CHAIR-POSE-LOCKED.md](./OPEN-SOLE-CHAIR-POSE-LOCKED.md) |
| Coperni PDP (CTA, Fashion Week, spine) | [COPERNI-PDP-LOCKED.md](./COPERNI-PDP-LOCKED.md) |
| Guarantee columns Type H3 + outline CTA `#1c1916` | `sitewide.lock.json` → `guarantee_band` |
| Collaborations = **Collaborations** (not Brand collaborations) | H1 / footer / URL; Brand collaboration = Wholesale dropdown only |
| Collaborations lede A+B | `page.collaborations.json` |

## Guardrails

- `planning/locks/sitewide.lock.json` + `python3 scripts/lock-scan.py .` before any draft push
- alwaysApply rules under `.cursor/rules/*LOCKED*.mdc`
- Fix-forward only — no thrash restores
- No theme/repo edits without Andrew saying **go**

## Index

See [README.md](./README.md) for the full locks list.
