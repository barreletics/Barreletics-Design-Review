# HOME MEDIA — NO-LOOP LOCK (Andrew 2026-09-20)

Read this BEFORE any Home hero / 50/50 / press media edit. Do not re-diagnose from scratch.

## What “done” means
1. **No cream border / inset / letterbox** around media. Photo/video fills the media column edge-to-edge.
2. **Cover only** on desk for hero + fifty-fifty + press media (unless Andrew names Fit).
3. **Hero not too tall.** Desk hero height = `min(640px, 70vh)` — never raw `100vh`, never uncapped square-on-62vw.
4. **Theme Editor with sidebar ≠ proof.** Always verify on **full-page** preview: `?preview_theme_id=187144929571`. Editor iframe lies.
5. **One axis per push.** Measure / screenshot full page before say-done.

## Do / Don’t
- DO: `object-fit: cover` + absolute fill; media column `padding:0`; wrapper `background: transparent`; cream only on text panel if needed.
- DO: Push liquid/CSS from Mac CLI; draft theme `187144929571` only.
- DON’T: Use `transform: scale()` or `inset %` to “un-zoom.”
- DON’T: Trust TE section chrome; trust full-page storefront preview.
- DON’T: Push `index.json` for media fills unless Andrew named a setting change (height/gap). Prefer liquid.
- DON’T: Re-open Cover vs Fit vs crop philosophy mid-axis.

## Hero
- File: `assets/split-hero.css` + `sections/split-hero.liquid`
- Height: `min(640px, 70vh)` desk. Full page must match.
- New hero art: export to frame ratio, upload Files, pick in TE.

## Fifty-fifty
- File: `sections/fifty-fifty.liquid`
- Home Grip + One Pair: Cover, min_height 640, scale 100, section_gap 0, no cream media_bg.
- Cream around photo = BUG. Fix fill, don’t discuss.

## Press (Interni)
- No cream media tray. Cover fill on desk.

## Self-check before reply
- [ ] Full-page preview checked (not only TE sidebar)
- [ ] Media left edge = column left (no cream gutter)
- [ ] Hero ≤ 640px / 70vh desk
- [ ] No scale()/inset “fake uncrop”
