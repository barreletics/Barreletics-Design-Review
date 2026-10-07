# Image Editor refresh handoff (2026-10-06, ~6:35 PM ET)

**Old bot:** Image Editor `fddf56a3-9934-435e-8c66-904f6469b9ab` (serverId 4813221). Keep visible until Grok Bot says hide.
**Name:** Image Editor (no title).
**Section:** Site Design (`section-mu3yeesr-1`).
**Routines:** none.
**Group chats:** none.
**Notify:** `notifyOnAgentUpdates: true` in settings.json.

## Role / persona (copy into new profile description)

Barreletics media reframer — Site Design family, sibling to Site Redesign · QC (and Website / Site Redesign for wire).

OWNS: Andrew pastes image/video CDN or Files links → reframe ONE asset at a time to the locked export size → hand the finished file back (path + preview). No Shopify wire. No Theme Editor. No full-page QC claims.

LOCKED SIZES (desk masters):
- Home 50/50 stills: **1400×1260** (≈10:9 / 11:10, matches desk box 712.5×640 @1440). Cover-ready. Subject centered with margin. Fill with real scene — **no letterbox/pads/cream bars**. Crop/reframe from source; never stretch.
- Full-bleed pink: **1425×900** (or 2× 2850×1800).
- Stef hero: already done — do not redo unless Andrew names it.
- Chair / portrait video: portrait cannot fill landscape without pads; only accept landscape masters Andrew provides, or wait for reshoot. Do not letterbox.
- Phone frame target (when asked): **390×500** display → export **780×1000** (2×) and **1170×1500** (3×) when source allows. Aspect 0.78 portrait. Extend backgrounds; never stretch; never cut subject.

RULES:
1. One asset per turn when possible. Name the target size before editing.
2. Prefer box ImageMagick / OpenCV / PIL. Show before/after dims. Naming: `{W}x{H}__slug.ext`.
3. Mobile can share the same desk master (center safe zone) OR get a dedicated phone master when Site Redesign / Website asks for 390×500.
4. Never touch live theme. Never push theme JSON. Never upload to Shopify Files unless Andrew explicitly asks. Hand file to Website / Site Redesign / QC for wire + full-page proof on the **real** draft URL.
5. If source aspect cannot fill target without pads or killing the subject → STOP and tell Andrew (A better crop window, B new shoot / outpaint master, C different target, D approved Fit exception). Subject integrity > hitting pixel size. No fake Cover crops.
6. Cream lock: soft **`#faf8f6`** only (sock-era / sitewide). Forbidden darker `#f5f2ec`. White `#ffffff` OK for white studio.
7. Short updates. Prefer fixing over philosophy. Screenshots only when Andrew needs to look (token budget tight).

## Guardrails (hard)

- Draft theme id for context only: `187144929571`. Image Editor does **not** edit liquid/schema/templates.
- Never invent Fit/scale/inset workarounds to "uncrop" Cover media.
- Never use swirl/marbled one-off shoes as packshots.
- Outpaint / background extend: original subject pixels must stay byte-identical on top of any new background. Prefer exact color fill for studio; GenerateImage only for background rings if needed, never redraw people/products.
- Before Open Sole Never-slip chair pose yellow theme height thrash: read `barreletics-chair-pose-yellow` skill (theme lock at 360 Cover — phone masters are separate files).
- Cover vs Fit physics: read `shopify-media-cover-gate` skill before advising TE media_fit.
- Andrew review guardrail (shared): before handing him a link/page, check the real URL at 390 and 1440; Image Editor hands **files**, not live page claims.

## Key Mac / box paths

**Mac (machine `b9c0e142-7e3d-4710-856d-c6a9caf6d9cf`):**
- `/Users/andrewnehra/Documents/GitHub/🔵  Barreletics-Design-Review/shopify-upload/` (`stills/`, `videos/`, OPERATING-PLAN.md)
- Lindsay trials: `…/shopify-upload-test/`
- Desktop zips historically: `barreletics-shopify-upload-for-chat.zip`, Chat Edited Images / Lindsay Chat.png

**Box:**
- `/workspace/image-editor/` — exports, chatgpt-9-originals.zip, sources
- `/workspace/image-editor/exports/shopify-upload/`, `m4-home/`, `lindsay-test/`
- `/workspace/phone-reframes-2026-09-29/` — phone masters + before/after sheets + NOTES.md + src/ + work/
- Drive zip (historical): `https://drive.google.com/file/d/1h_V1NQA1_CVS_gZ1ijHRpa1LScxaWI-m/view?usp=drivesdk` (public share may still need Andrew)

## Done (recent / still relevant)

### Phone reframes (2026-09-29) — delivered to Site Redesign; Andrew loved Multi_Image restack
Folder: `/workspace/phone-reframes-2026-09-29/`
| # | Source file | Outputs | Method / notes |
|---|-------------|---------|----------------|
| 1 | `P5A4949.jpg` 2100×1400 | `780x1000__` + `1170x1500__open-sole-never-slip-chair-yellow.jpg` | Floor extended ~703px; bottom third is new floor; legs still cut at top (source). Open: keep vs 360 landscape exception. |
| 2 | `Purple_45b2348c-….jpg` 600×600 | `780x1000__coperni-grip-isnt-optional-purple.jpg` only | White pad; 1.3× soft. Needs larger original. Solid purple OK. |
| 3 | `Black_on_Black_Yoga_Pant.jpg` 1000×1500 | `1170x1500__` + `780x1000__apparel-super-high-rise-leggings.jpg` | Pink sides +85px; waistband+feet in at 500. Best of set. |
| 4 | `Multi_Image.jpg` 1937×670 | `1170x1500__` + `780x1000__multi-image-shoe-restack.jpg` | 7 shoes restacked 2/1/calm/2/2; Andrew loved layout. |
| 5a | `Yellow_Image-Blue_Shoe_1200x1200_….jpg` 1200×1200 | blue shoe commit | Yellow extended above toes. |
| 5b | `barreletixxstefrunningpinkbackground.jpg` 2128×2436 | Coperni running | Pink wall above head; full body. |

Sheets: `sheet-1-…` through `sheet-5b-….jpg`. Nothing uploaded to Shopify; wire still Site Redesign / Website.

### Desk 1400×1260 batch (earlier)
~33 stills + 6 videos cover-cropped into shopify-upload / m4-home. Portrait videos Red until landscape masters. Operating plan: Green/Yellow/Red triage → visual pass → upload folder only if subject survives.

### Lindsay Reformer (Cover 50/50 worked example)
CDN `Lindsay_Reformer_2.png` 1086×1448 AR 0.75. Chat outpaint master `Lindsay Chat.png` 1322×1190 (Mac Desktop Chat Edited Images; box copy `/workspace/image-editor/exports/Lindsay-Chat.png`) is preferred path to clean 1400×1260 Cover without killing subject.

### ChatGPT originals ZIP (2026-09-22)
`/workspace/image-editor/chatgpt-9-originals.zip` — 9 CDN originals unmodified (dims as CDN served; some small e.g. 50072453 = 862×960).

### Venice Biennale Postcard bot
Created by this bot for Andrew: `d9df3764-c5d0-49d1-81be-55e9467aeb46` in Marketing. Bilingual EN+IT noted. Not Image Editor work going forward.

### TE controls (Not Image Editor)
Never-slip / 50/50 TE knobs (frame shape desk+mobile, text bg, pad bg, labeled white + cream `#faf8f6`) owned by Website / Site Redesign family — Image Editor stays on media files.

## Open items for new bot

1. **Chair pose phone master:** Andrew OK overall; decide extended floor vs keep 360 landscape. Confirm on real draft @390 before wire.
2. **Coperni purple:** soft 600px source — find larger master if exists, or leave.
3. **Phone set wire:** Site Redesign / Website still to swap files into draft 187144929571 after real-URL check (Andrew guardrail).
4. **Lindsay Chat → 1400×1260:** optional clean resize/stage if asked.
5. **Portrait lifestyle masters:** still need landscape shoots or outpaint for Cover 50/50s that can't keep full subject.
6. Do not claim phone/desk QC on live pages — file delivery only.

## Skills to open first when relevant

- `/home/box/agent-data/workflows/barreletics-chair-pose-yellow/SKILL.md`
- `/home/box/agent-data/workflows/shopify-media-cover-gate/SKILL.md`
- `/home/box/agent-data/workflows/barreletics-cream-band/SKILL.md`
- `/home/box/agent-data/workflows/barreletics-media-fill-50-50/SKILL.md`

## Handoff contacts

- Wire / TE / Home: Website (`c26abd74-aac4-4412-bb15-5d308182c631` or current Site Design Website) and/or Site Redesign (`0b84b5bd-8846-478f-bca4-9faedc5de6a7`)
- Full-page QC: Site Redesign · QC (`dd04cb88-be09-4dec-b886-fff74d75584e`)
- Front desk: Grok Bot (`aa3b203e-439b-4c78-b271-222e1cbb46ba`)

## After new bot exists

Old bot waits for Grok Bot instruction to hide. Do not delete. Point Andrew to the new Image Editor for new reframes.
