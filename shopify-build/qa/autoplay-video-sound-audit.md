# Autoplay video sound audit

Sections checked: `shopify-build/**/*.liquid` (excluding backups).

**Policy:** Background/autoplay videos must always be muted (HTML + JS).

**Risk findings:** 0 — no autoplay video markup without `muted` in theme liquid.

fifty-fifty + split-hero also use `snippets/bg-video-autoplay-script.liquid` to force `v.muted = true` and `play()` on load and `shopify:section:load`.
