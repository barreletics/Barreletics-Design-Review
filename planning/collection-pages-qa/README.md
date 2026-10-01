# Collection pages QA harness

Built 2026-08-08. The ten collection templates had no preview anywhere under `planning/`,
which is why the broken video source on `collection.json` and the two grey "Media placeholder"
panels were never seen on screen — they were only ever reported from source JSON.

```
python3 planning/collection-pages-qa/build.py
```

Renders every `shopify-build/templates/collection*.json` for real through the section Liquid,
reusing the Liquid environment and tag stripping from `planning/returns-pages-qa/build.py`.

## What is real and what is not

**Real:** every setting-driven string — headings, body copy, FAQ and GEO answers, review blocks,
CTA hrefs, and all `image_url` / `video_url` / `poster_url` media.

**Not real:** anything that needs a storefront `collection` or `product` object. Variant cards
render empty, and a `collection-hero` with `title: ""` shows an empty H1 here because the live
`{{ section.settings.title | default: collection.title }}` fallback has no Admin collection
title to fall back to. On the storefront those H1s resolve to the Shopify collection title.

Unset settings resolve to `""` (see `Settings.__missing__`) so the `!= blank` fallback chains
in `fifty-fifty.liquid` branch the way Shopify branches them. Without that, python-liquid
reports them Undefined and the media column renders empty rather than picking the image.

No screenshots — this harness is for reading and grepping the rendered HTML.
