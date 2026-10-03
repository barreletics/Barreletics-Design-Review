# Autoplay video audit (shopify-build)

Full-theme scan: all `*.liquid` under `sections/` and `snippets/` (no `blocks/` dir).  
Embeds only: `sections/article-content.liquid` styles YouTube/Vimeo **iframes** (not native `<video>`).

**Policy:** Decorative/autoplay videos must be `muted` + `autoplay` + `loop` + `playsinline` (+ `webkit-playsinline` on manual tags).  
**JS:** `snippets/bg-video-autoplay-script.liquid` per section + `assets/chrome.js` `initAmbientVideos` (skips `[controls]`, click-deferred, non-autoplay).

## Sections with native video (Shopify picker and/or URL)

| Section | Autoplay script | Notes |
|---------|-----------------|-------|
| `split-hero.liquid` | yes | |
| `fifty-fifty.liquid` | yes | |
| `problem-section.liquid` | yes | Legacy `video_asset` mp4 same attrs |
| `press-row.liquid` | yes | Locked — script/attrs only |
| `press-cards.liquid` | yes | Autoplay tiles only; `video_mode=click` deferred excluded |
| `press-feature.liquid` | yes | Twin frame — locked |
| `visual-mosaic.liquid` | yes | Per-block tiles |
| `collab-hero.liquid` | yes | Stage + editorial |
| `fullbleed-statement.liquid` | yes | Keeps poster-cover kick script |
| `collection-hero.liquid` | yes | |
| `coperni-pdp-story.liquid` | yes | |

## Snippets

| Snippet | Video output |
|---------|----------------|
| `media-img.liquid` | None (images only) |
| `bg-video-autoplay-script.liquid` | Shared primer (not a `<video>` emitter) |

## User-initiated (no forced autoplay)

- **Press cards** `video_mode=click`: `.press-cards__video--deferred` — `playsinline`, `preload=metadata`, custom play button.
- Any future **`[controls]`** video: skipped by ambient scripts.
