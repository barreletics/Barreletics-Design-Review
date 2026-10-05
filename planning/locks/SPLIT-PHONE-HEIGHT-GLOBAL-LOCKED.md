# Split (50/50) phone media height: GLOBAL, LOCKED 2026-09-29

**Approved:** Andrew, Tue 2026-09-29 12:25 PM ET. One sitewide phone height of **600**, with per-section overrides only where 600 crops badly.
**Draft theme:** `187144929571` only (never live `185687998755`).
**Supersedes:** PDP phone 550 (`fifty-fifty-pdp-mobile-LOCKED.md`, 2026-09-10) and Home/marketing phone 520 (`PAGE-LAYOUT-OS-LOCKED.md`). Desktop heights (PDP 560, Home as set) are unchanged.

## How it works
| Layer | Value |
|---|---|
| Theme setting | Theme settings > **Split images** > **Phone split-image height** (`split_media_height_mobile`), 320 to 700, step 10, default **600** |
| CSS var | `--split-media-h-mobile` on `:root` (layout/theme.liquid `section-gap-os` block) |
| Section setting | `mobile_media_height` = **Phone height override (0 = use global)**, 0 to 700. 0 or blank = global |
| Liquid | `sections/fifty-fifty.liquid` writes `--ff-mobile-media-height` = override px, or `var(--split-media-h-mobile, 600px)`; the CSS fallbacks point to the global var |
| Unchanged | Phone **Square** frame (1:1, ignores height) and phone **Fit/Contain** (auto height) |

## Overrides (the only allowed non-zero values; lock-scan enforces these)
| Template | Section | Phone height | Why |
|---|---|---|---|
| product.in-studio-template.json + product.open-sole.json | fifty-fifty-lifestyle (Never slip in chair pose) | 360 | chair_pose_open hard lock |
| product.coperni.json | fifty-fifty-lifestyle (Grip isn't optional) | 400 FIT | packshot exception |
| product.json (Closed Sole) | fifty-fifty-sock-era (running video) | 500 | 600 cuts the back shoe and fist |
| product.json (Closed Sole) | fifty-fifty-commit (washing video) | 500 | 600 cuts the burned-in caption |
| product.outdoor.json | fifty-fifty-outdoor-works (Practice outside) | 500 | 600 cuts the raised shoe |
| page.best-grippy-socks.json | outgrew (We outgrew grip socks) | 500 | very wide multi-shoe image, shoes cut at any height: **needs a new image** |

## Home Chair Pose (problem-section, not fifty-fifty)
Was a phone Square frame (390x390). Now `media_aspect_mobile: stretch` + `mobile_media_height: 600`. The current media is the video clip01 (810x1080) with black shoes; at Fill 600 the shoes stay in frame on every sampled frame (Square cut more). problem-section has no link to the global var yet, so update this value by hand if the global changes.

## Also in this push
Open Sole `fullbleed-lifestyle` `height_mobile` 60 -> 80 (in-studio + open-sole), approved 2026-09-28.

## Do not
- Put a px value in `mobile_media_height` without adding it to `sitewide.lock.json` -> `fifty_fifty_lifestyle.mobile_media_height_exceptions`
- Re-introduce 550 / 520 per section to "match" old rulers
- Change Chair Pose 360 without Andrew lifting `chair_pose_open`
