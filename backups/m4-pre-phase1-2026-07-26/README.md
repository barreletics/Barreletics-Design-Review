# M4 pre–Phase 1 backup (2026-07-26)

Created before any push to draft theme `187143618851`.

| Path | What |
|------|------|
| `shopify-build/` | Snapshot of Design-Review shell at backup time |
| `donor-chrome/` | Read-only copy of live local chrome + 3 br-* sections from `barreletics-theme-live-apr2026` |
| `draft-theme-pull/` | (added after Shopify auth) Pull of unpublished draft `187143618851` before overwrite |

**Do not push these folders to Shopify.** Restore reference only.

## draft-theme-pull/
Full pre-push pull of unpublished draft `#187143618851` (2026-07-26).
Assets folder omitted from git (large binaries); Liquid/JSON/config retained.
Re-pull assets anytime: `shopify theme pull --theme 187143618851 --path backups/m4-pre-phase1-2026-07-26/draft-theme-pull`
