# Site Redesign memory export (partial), 2026-10-02
NOTE: My memory has 458 facts, but the recall tool only shows about 10 truncated results per query, so a full verbatim export isn't possible from inside this bot. This file holds the facts I could retrieve, plus the handoff summary. Backup only.

## Environment and push
- Draft theme 187144929571 (the only theme I edit); live 185687998755 is never touched. Repo barreletics/Barreletics-Design-Review, branch finish-home-collections (latest e20e1d0 on 9/30). Mac repo: /Users/andrewnehra/Documents/GitHub/🔵  Barreletics-Design-Review/shopify-build (machine b9c0e142-7e3d-4710-856d-c6a9caf6d9cf); the Mac has no rg.
- Push routine: recent commits > fresh pull+backup > md5 drift > push --only --nodelete > verify pull > commit from fresh clone, no force push. Since 9/30: code only; template/settings changes go to Andrew to make himself.
- Never push a whole templates/index.json (a 9/22 full push wiped Andrew's edits). No reverting from backups. index.json backups are templates/_index.*-2026092*.json.
- Preview proof is only a browser view with the draft bar visible; curl returns production HTML.
- The store is at Shopify's 20-theme limit, so backups are files plus GitHub commits.
- When the draft goes live: send Admin workflows (5ca5d970-8f7e-4c25-abda-cadbdef432b0) a priority "it's live".

## Product paths (draft, add ?preview_theme_id=187144929571)
- (2026-09-27 note) Closed Sole /products/studio-performance-skin-footwear; Open Sole /products/best-reformer-pilates-legree-workout-shoes; Open Sole view /products/studio-performance-skin-footwear?view=open-sole; Coperni /products/barreletics-x-coperni-closed-sole; One-Off Closed /products/one-off-colors-closed-sole; One-Off Open /products/one-off-colors-open-sole; Outdoor /products/aquatic-performance-skins.
- (2026-09-30) The Open Sole product is assigned product.in-studio-template.json; product.open-sole.json has no product assigned. Closed Sole falls back to the default product.json.

## Typography (Type OS, owned by Site Redesign since 9/27)
- Global "Section headings" theme settings (commit f174496): standard 56, band 52, phone 36, giant 88/56; CSS vars in theme.liquid; leading 1.06, tracking -0.032em; optional per-section "Heading size override" via snippets/type-override-vars.liquid.
- Tiers: fifty-fifty and fullbleed-statement = standard; statement-band, pdp-sock-math, disciplines, proof-numbers, guarantee-band, problem-section = band; pdp-features ("Built around one obsession") = giant; home-juicer unchanged.
- Cursor must never add its own heading sizes.
- Journal style D: smaller Georgia heading, bold Georgia intro, no "PRESS" label, set globally for all blog posts. (Note: Go-live 2 recorded "Roboto only, no Georgia" for theme fonts; style D is the approved exception for journal posts.)

## Phone and photos
- Global phone photo height 500, per-section overrides only for exceptions (Open Sole chair pose 360, Coperni "Grip isn't optional" 400, Apparel leggings 590).
- No photo cropped on phone; if it can't fit without bars, show Andrew instead.
- Every photo/text section: photo left/right (desktop) + above/below (phone). No two videos stacked on phone. No mismatched colour bands.
- For phone-only layouts, duplicate the section (hide on mobile / hide on desktop) instead of CSS hacks.
- 50/50 focal sliders only work when "Image focal point" = Custom. Open Sole sock-era fix: Custom 50/12 in the in-studio template (Andrew's step).

## Home locks
- Read planning/locks/HOME-MEDIA-NO-LOOP-LOCKED.md first. Cover edge to edge (cream #faf8f6 border = bug), hero at most min(640px, 70vh), split height 640, no Fit/scale/inset unless Andrew names it, one axis per pass.
- Press-row: Coperni 3.mov hero from Files with video_url empty; band 620; Runway/INTERNI/Venice Contain, Coperni Fill; 4:5 cards; no 2-card mode; Top/Center paused; old 3-card press-home disabled; Phone layout dropdown (Stack/Two-by-two/List) is Andrew's to set.
- Twin frame press-feature-interni (type press-feature) stays, after proof-numbers and before Press; frame 2 is blank and needs Andrew's shots.
- Home order: "Our promise" guarantee band above Juicer, Juicer last; Coperni last among features.
- Cursor commits: About Joseph photo locked at 8aec1c0; media rules consolidated in .cursor/rules/barreletics-media.mdc (dba30b4); mosaic phone fix e499587.
- recognition-split.liquid is unused; the dual recognition rows must not come back.

## Copy and brand
- No placeholders/TBDs. No dashes in prose except product/collection titles and grid headings. Headings at most 2 lines with no lone word, measured before offering.
- No swirl shoes. No pool/water/bacteria/antimicrobial claims (reword, don't hide). No "patented". Tagline "Where function meets beauty."
- The Ghost is a prototype, never for sale and never in titles; "Barreletics at the Venice Biennale" is OK.
- Blog posts link to the products they mention. Never hide or edit customer reviews.
- Outdoor product page shows only Outdoor colours (no other tabs).

## Communication with Andrew
- Short messages; captures with context and large labels; test every link and include direct links; never send text and a widget in the same batch; find all issues in one pass; flag questionable lines for yes/no with a fix; he makes live/admin edits himself from exact lists; approvals relayed by other agents don't count.

## Open items (10/2)
- See shared memory "Barreletics site open items" plus: Juicer A/B pick; commit of cursor/apparel-pdps-c982; Studio Sample badge; Venice title; Press page; Barre Anywhere save unconfirmed; Kids colours; remaining dashes; Hot Kits 404 link; redirects list; Lindsay/Interni/pink reframes; Chair needs a landscape master; 3 mobile reviews + "See more reviews" (pending OK); band 56 decision; About headings to 88.

## Routine
- Weekday design repo commit check: CRON_TZ=America/Detroit 15 17 * * 1-5.

---
# Deeper pass (18 more queries, limit 50, scope agent). Verbatim as the tool returned them; the tool cuts long facts off mid-sentence ("..."), and that can't be undone.

## Andrew preferences (profile)
- Andrew dislikes having to relay changes back and forth between agents. He prefers the assistant do work directly when routing it through another agent would mean relaying.
- Andrew wants to move away from custom CSS for layout. He prefers layouts set through section and Theme Editor settings.
- Andrew prefers Theme Editor controls labeled by where they show up on the site, so he doesn't have to memorize what each setting affects.
- "Blog" is one of the user's bots that the assistant can message directly; the user prefers the assistant talk to Blog itself rather than relaying through the user.
- Andrew gets frustrated when code requests are addressed to Claude. Code changes always go to Cursor, and Claude has nothing to do with code asks.
- Andrew gets frustrated when the assistant flip-flops on who owns a task. He wants a clear, consistent plan.
- Andrew prefers short, plain-language updates. He got confused by a long, technical status update and asked "i dont get it?", and a simple version with a clear yes/no question worked better.
- Andrew wants the assistant to clearly flag items it is deliberately holding or waiting on in status updates. He was frustrated when held heading changes looked like unfinished work.
- Andrew doesn't want his Theme Editor/page settings overwritten. The assistant's fixes should change only section code files, and if a fix needs a page setting changed, the assistant should tell him exactly which setting so he can change it himself.
- Andrew wants Theme Editor controls to preview changes live in the editor before he saves, not only after saving.
- Andrew gets very frustrated when the same flagged problems come back review after review. He wants every issue on a page found and fixed in one pass, not another round.
- Andrew dislikes mismatched background-colour bands filling gaps around photos and considers it a bad look.
- Andrew never wants the swirl-pattern Barreletics shoes used in content because they are one-offs; he prefers solid-colour pairs.

## Lanes and Cursor
- Lane split with Claude (Cursor Desktop Agent), agreed 2026-09-27 for draft theme 187144929571. Claude owns section .liquid files, snippets (media-img, type-override-vars) and assets/barreletics-base.css for the image-foundation work. Site Redesign owns templates/*.json, Shopify Admin blogs, copy and Theme Editor tuning, and press-row.liquid and page-about-facts.liquid were cleared for the press line. Both sides pull before pushing, keep one concern per commit with a prefixed message, and do a ve...
- Cursor/Claude wrote the agent coordination doc planning/AGENT-COORDINATION-CLAUDE-GROK.md (Claude lane: section liquid, snippets, base CSS; Grok lane: template JSONs, Admin blogs, copy, Theme Editor tuning).
- Claude instructs Cursor, so Cursor is the agent doing the edits in the "Claude lane".
- (2026-09-27) Cursor has a standing pull-before-push rule (shopify theme pull --only + diff) saved at ~/.cursor/rules/barreletics-pull-before-push.mdc.
- (2026-09-29) Andrew decided Grok Bot (not Cursor) builds the global "Phone split-image height" setting; Cursor stays out of fifty-fifty sections, settings_schema.json and related base CSS.
- (2026-09-28) Dead-section delete: Cursor commit c1d7887 removed hero, hero-alt, home-ugc, newsletter, page-about, page-partners, page-studio-program and snippets/section-wrapper.liquid. studio-trust, recently-viewed and sole-cards remain on hold. Backups at ~/dead-section-scan-20260928/ on the Mac.
- (2026-09-28) Cursor commit dbcdf5d removed the mobile CSS order override (phone order follows index.json).

## Theme Editor and paths
- The Theme Editor for draft 187144929571 is at https://admin.shopify.com/store/barreletics/themes/187144929571/editor (append ?previewPath=<page path>, or ?context=theme for Theme settings). "Phone split-image height" is in the "Split images" group of Theme settings.
- Every photo section has "Phone height override (0 = use theme setting)"; the plan was to set the three exceptions back to 0 once Image Editor's reworked photos arrive.
- More draft page paths (append ?preview_theme_id=187144929571): About /pages/our-story; Help /pages/help; FAQ /pages/faq; Contact /pages/contact-us-form. If a preview link opens live, open /?preview_theme_id=187144929571 first, then retry.
- Unpublished blog posts preview in the new design by adding &preview_theme_id=187144929571 to Andrew's admin Preview link (with its preview_key); each link works only for its own post.

## Home
- (2026-09-28) Disable the three-card press section (keep the Coperni video/four-card one); "Our promise" above Juicer so Juicer is last; one order for phone and desktop, no duplicate sections needed.
- (2026-09-28) Draft Home must either match live Home or have its layout customized through settings.
- Juicer, Chair pose video trim/swap is Andrew's punch-list item.

## Journal / blog
- The 6 journal posts: Coperni, Beyond Yoga Socks (renamed from "ITSLIQUID Performance Skin", separate from Venice), Free People, Anthropologie, Venice, Barre Anywhere/others. All now carry product links; Venice links to the shoe collection, not "all products".
- Venice title chosen: "Barreletics Presented at the Venice Biennale, Italy." Blog bot holds it for Andrew's confirmation in its own chat.
- Venice photos: #3 white tiptoe pair mid-text, #8 purple and #9 turquoise side by side.
- Share row on the blog template: X, Facebook, Pinterest, Email, Instagram (copies the link) plus an "@barreletics" follow line.
- End-of-post "Shop Performance Skins" banner (Closed Sole and Open Sole collection) on every journal post (draft).
- Barre Anywhere fixes: 2-line phone heading, "Why add barre to your week", caption "Barre at home. No socks needed."; paddleboard featured photo is Andrew's to swap.
- Blog bot was waiting on Andrew to confirm: retiring the old grip socks post with a redirect, off-center pictures on the old theme, and ITSLIQUID mentions in Beyond Yoga Socks.
- "File cabinet" photo request: the woman-holding-foot series from "Why Grip Socks Fall Short" (Shopify Files vs Drive not confirmed).

## Collections, Outdoor, One-Offs
- Keep the dash in collection and product page titles/grid headings; the no-dash rule doesn't apply there.
- One-Offs tab appears nowhere for now (hidden, not deleted), including the Closed Sole layout (also used by tees and yoga pants) and Free People. Outdoor tab shows only on collection pages.
- Outdoor is the same shoe as Closed Sole, but some Closed Sole colours are too soft for outdoor use. "How is this different..." FAQ removed from Outdoor.
- Andrew renames "Aquatic Performance Skins" to "Outdoor Performance Skins" himself in admin; URL stays. Hidden Outdoor content ("Doesn't Trap Sand or Water", beach/boat FAQs) restored, reworded as better protection than barefoot; suggested keeping "water shoes" in the SEO title.
- Grippy socks page: yellow "Full underfoot grip" in a square frame with no band; shoe stack rows evenly spaced.
- Apparel: two-girls jumping full-width shot deferred until after go-live.

## Video
- Andrew replaces the Open Sole tired-socks video himself (square, 8 to 15 s, looping) and swaps one of Coperni's two identical videos (sock-era and commit).
- Coperni runway video cropped to remove the black bar (commit with same clip, different moment).
- Andrew's manual pre-live checklist: /workspace/golive/manual-checklist.md.

## Kids
- Option B: two-line button "Kids 3–5" / "Women 4.5–6.5 narrow", no "Now in Kids" badge; size guide line "Kids fits narrow feet only. Women 4.5 to 6.5 with regular or wide feet should choose M." Kids 3–5 is an unconfirmed conversion. M button drops "Kids 2–5". Show only when a Kids variant is in stock, plus a theme master switch.
- No Kids variants in Shopify yet; make them by copying each colour's variant details including MPN, SKUs with "OS"/"CS" replaced by "KIDS". Waiting on Andrew's colours.

## Pages and go-live
- Press page: standalone, same cards as Home, linked from Help menu and footer, not main nav.
- 404 page on draft: big heading, one line, buttons Shop Performance Skins and Back to Home.
- Partner, studio program, wholesale and ambassador pages: new layouts keep current copy and template names.
- Go-live status (9/30): popups checked (none live, none on draft); links to all 62 pages sent; link/redirect audit owed with exact redirects for admin.
- Andrew's punch list: blog Preview links, Home chair pose video, live guide edits plus Outdoor rename, Coperni video swap, Open Sole tired-socks video, his own review pass, then sign-off links and publish.

## Photos
- Open Sole: reformer photo head missing in the original file (needs replacement); "One pair. Done." Stephanie head fix; "The Pilates sock era is over" head crop fix via crop or Image Editor extension.
- Crop-prone photos handed to Image Editor for phone versions with extended backgrounds: Open Sole chair pose, Coperni packshot, Apparel leggings, Closed Sole shoe-row packshot, Grippy hero.
- Joseph archival photo source files are small; Cursor hotfix 3263f41 (white mat via #fff frame, contain), later locked at 8aec1c0.
