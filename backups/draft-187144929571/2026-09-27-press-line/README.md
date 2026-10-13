# Draft theme 187144929571 — press-line snapshots (2026-09-27)

These folders are **read-only backups** of four theme files from Shopify draft theme **187144929571**. They are **not** wired into `shopify-build/`; nothing here is loaded by the theme build.

| Folder | Meaning |
|--------|---------|
| `pristine-1137ET/` | Pulled from the draft at **11:37 AM ET** on 2026-09-27, **before** the press-line change. |
| `pushed-1207ET/` | Same paths as live on the draft since **12:07 PM ET** on 2026-09-27 (press-line push). |

Paths mirror the theme layout: `sections/press-row.liquid`, `sections/page-about-facts.liquid`, `templates/index.json`, `templates/page.about.json`.

**What changed between pristine and pushed:** “Also featured in” mentions line (`show_mentions` / `mentions_*` settings) in the two liquid sections and JSON; Venice press card image (`IMG_2917.jpg`) and copy/block order on home `press-row`; About facts section settings aligned with the mentions feature.

## `shopify-build/` vs this draft (finish-home-collections @ `1c8a235`)

Reconcile git and the draft separately before replacing anything under `shopify-build/`:

- **`templates/index.json`:** Repo has newer home hero tuning (e.g. `image_pos_y` / mobile **22** vs draft **50**, `media_column_pct` **62** vs **50**, taller tiles/min heights, different mobile aspect modes) and different block imagery (e.g. Lindsay reformer vs chat asset) than the draft snapshots here.
- **`templates/page.about.json`:** Repo reflects About v25 work (stripped auto-generated header, `media_max_vh` caps on value blocks); draft exports include the Shopify auto-generated comment block and extra theme-editor default fields.
- **`sections/press-row.liquid`:** Draft snapshots include eyebrow heading, `media-img`, and hide-on-mobile/desktop controls; repo copy at `1c8a235` is an older/simpler section file (mentions line exists only in `pushed-1207ET/` here).
- **`sections/page-about-facts.liquid`:** Pristine backup matches repo at `1c8a235`; mentions markup appears only in `pushed-1207ET/`.
