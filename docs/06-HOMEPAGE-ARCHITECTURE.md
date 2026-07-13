# Homepage Architecture — Lossless Complete Specification

**CRITICAL:** This document is a lossless migration of EVERY specification, measurement, code, class name, color value, font size, animation, interaction, and decision from the approved Barreletics Homepage design system. NO SUMMARIZATION. NO SIMPLIFICATION. ALL DECISIONS PRESERVED EXACTLY.

Last Updated: 2026-07-12  
Source Authority: Barreletics Home - Matured.html, home-matured.css, home-tweaks.jsx  
Status: APPROVED

---

## MATURED HOMEPAGE SPECIFICATION (Primary Source)

### Complete HTML from Barreletics Home - Matured.html

<!DOCTYPE html>
<!-- saved from url=(0058)file:///Users/andrewnehra/Downloads/Barreletics_v28_1.html -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Barreletics performance skins — the grip shoe that outperforms grip socks in barre, reformer Pilates, Lagree and Megaformer. 360° grip, no latex, no silicone. Trusted by 1,000+ instructors. Made in USA.">
<title>Barreletics — Home · Matured Direction</title>
<link href="maturation-styles.css" rel="stylesheet">
<link href="home-matured.css" rel="stylesheet">
<link rel="icon" type="image/png" href="barreletics-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com/">
<link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ============================================================
   Barreletics Design Audit — Stylesheet
   Pulls tokens directly from /config/settings_data.json
   ============================================================ */

:root {
  /* Brand color tokens — calibrated to the LIVE site, not the unused settings.
     The header & footer render --colorNav from --colorBody (#fff) per
     snippets/css-variables.liquid, so the cream + plum in settings_data.json
     is dead code. The real palette is: white, ink, light-grey, coral accent. */
  --br-bg:           #ffffff;
  --br-alt-bg:       #f9f9f9;
  --br-alt-bg-2:     #f3f3f3;   /* the slightly deeper grey used in br-media-text-split */
  --br-text:         #050505;
  --br-text-soft:    #4a4a4a;
  --br-text-mute:    #8a8a8a;
  --br-line:         #e6e6e6;
  --br-line-soft:    #efefef;

  /* WARM ACCENT — restrained to cart badge ONLY (matches live site).
     Stars use gold. Sale uses ink. CTAs are black-on-white.
     The earlier f93820 was too aggressive — live site uses coral on cart only. */
  --br-accent:       #f97250;   /* cart badge ONLY — restraint is the point */
  --br-accent-hover: #e85e3c;
  --br-coral:        var(--br-accent);   /* alias */
  --br-sale:         var(--br-text);     /* sale price is just ink-bold, not red */
  --br-star:         #fbc02d;             /* gold star color */
  --br-info:         #3a8de8;             /* sale banner blue + LE chip */
  --br-le:           #3a8de8;
  --br-le-bg:        #eaf3fc;

  --br-button:       #050505;
  --br-button-text:  #ffffff;

  /* Audit accents (only used in audit chrome, NOT in mock components) */
  --au-bg:           #fafaf7;
  --au-card:         #ffffff;
  --au-flag:         #c43d2a;
  --au-flag-bg:      #fdf0ec;
  --au-ok:           #1f6f4a;
  --au-ok-bg:        #ecf6f0;
  --au-note:         #6b5b3a;
  --au-note-bg:      #fbf5e6;

  /* Typography system — PROPOSED (one family, one ramp) */
  --t-font: 'Roboto', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;

  --t-eyebrow:      12px;   /* uppercase, 0.08em, 600 */
  --t-body-sm:      14px;
  --t-body:         16px;
  --t-body-lg:      18px;
  --t-h6:           18px;
  --t-h5:           22px;
  --t-h4:           28px;
  --t-h3:           36px;
  --t-h2:           44px;
  --t-h1:           56px;
  --t-display:      72px;

  /* Mobile clamps applied via clamp() on hero/display only */
  --t-h1-mobile:    36px;
  --t-display-mobile: 44px;

  /* Spacing scale */
  --sp-1: 4px;
  --sp-2: 8px;
  --sp-3: 12px;
  --sp-4: 16px;
  --sp-5: 24px;
  --sp-6: 32px;
  --sp-7: 48px;
  --sp-8: 64px;
  --sp-9: 96px;
  --sp-10: 128px;

  /* Buttons — ONE primary, ONE secondary, ONE tertiary, no more */
  --btn-text-size:   14px;
  --btn-pad-y:       14px;
  --btn-pad-x:       28px;
  --btn-radius:      0px;       /* matches "button_style":"square" */
  --btn-letter:      0.06em;
  --btn-weight:      600;
}

/* ============================================================ */

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  font-family: var(--t-font);
  font-size: var(--t-body);
  line-height: 1.55;
  color: var(--br-text);
  background: var(--au-bg);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-wrap: pretty;
}

img, video { max-width: 100%; display: block; }

/* ---------- Audit chrome ---------- */

.au-nav {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(250, 250, 247, 0.92);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--br-line);
}

.au-nav__inner {
  max-width: 1320px;
  margin: 0 auto;
  padding: 14px 28px;
  display: flex;
  align-items: center;
  gap: 32px;
}

.au-nav__brand {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-accent);
  white-space: nowrap;
}

.au-nav__brand span {
  font-weight: 400;
  letter-spacing: 0.1em;
  color: var(--br-text-soft);
  margin-left: 10px;
}

.au-nav__links {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.au-nav__links a {
  color: var(--br-text-soft);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  padding-bottom: 2px;
  transition: color 0.15s, border-color 0.15s;
}

.au-nav__links a:hover { color: var(--br-text); border-color: var(--br-text); }

.au-nav__meta {
  margin-left: auto;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  white-space: nowrap;
}

/* ---------- Document wrapper ---------- */

.au-doc {
  max-width: 1320px;
  margin: 0 auto;
  padding: 64px 28px 160px;
}

.au-section {
  padding-top: 80px;
  margin-top: -1px;
}

.au-section + .au-section {
  border-top: 1px solid var(--br-line);
  padding-top: 80px;
  margin-top: 80px;
}

.au-kicker {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--br-accent);
  margin: 0 0 14px;
}

.au-h1 {
  font-size: clamp(40px, 5vw, 64px);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: -0.02em;
  margin: 0 0 24px;
  max-width: 18ch;
}

.au-h2 {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 500;
  line-height: 1.15;
  letter-spacing: -0.01em;
  margin: 0 0 16px;
  max-width: 22ch;
}

.au-h3 {
  font-size: 22px;
  font-weight: 600;
  line-height: 1.25;
  margin: 0 0 12px;
}

.au-lede {
  font-size: 19px;
  line-height: 1.55;
  color: var(--br-text-soft);
  max-width: 62ch;
  margin: 0 0 16px;
}

.au-body {
  font-size: 16px;
  line-height: 1.6;
  color: var(--br-text-soft);
  max-width: 62ch;
}

.au-body + .au-body { margin-top: 12px; }

.au-rule {
  height: 1px;
  background: var(--br-line);
  border: 0;
  margin: 48px 0;
}

/* ---------- Cover ---------- */

.au-cover {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 64px;
  align-items: end;
  padding: 80px 0 64px;
  border-bottom: 1px solid var(--br-line);
}

.au-cover__meta {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-bottom: 6px;
}

.au-cover__stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 16px 18px;
  background: var(--au-card);
  border: 1px solid var(--br-line);
}

.au-cover__stat b {
  font-size: 32px;
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  color: var(--br-text);
}

.au-cover__stat span {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
}

.au-cover__stat--flag b { color: var(--au-flag); }

@media (max-width: 900px) {
  .au-cover { grid-template-columns: 1fr; gap: 40px; }
}

/* ---------- Findings cards ---------- */

.au-findings {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

@media (max-width: 800px) {
  .au-findings { grid-template-columns: 1fr; }
}

.au-finding {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.au-finding__head {
  display: flex;
  align-items: center;
  gap: 10px;
}

.au-finding__num {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--br-text-mute);
  text-transform: uppercase;
}

.au-finding__tag {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  padding: 4px 8px;
  background: var(--au-flag-bg);
  color: var(--au-flag);
}

.au-finding__tag--note { background: var(--au-note-bg); color: var(--au-note); }
.au-finding__tag--ok   { background: var(--au-ok-bg);   color: var(--au-ok); }

.au-finding h3 {
  font-size: 20px;
  font-weight: 500;
  margin: 0;
  line-height: 1.3;
}

.au-finding p {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
}

.au-finding__evidence {
  font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 11.5px;
  line-height: 1.6;
  background: #f5f4ee;
  border-left: 2px solid var(--au-flag);
  padding: 12px 14px;
  color: #2a2a2a;
  overflow-x: auto;
  white-space: pre-wrap;
}

/* ---------- Tokens table ---------- */

.au-tokens {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
}

.au-token {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-height: 130px;
}

.au-token__swatch {
  width: 100%;
  height: 56px;
  border: 1px solid rgba(0,0,0,0.06);
}

.au-token__name {
  font-size: 13px;
  font-weight: 600;
  color: var(--br-text);
}

.au-token__hex {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 11px;
  color: var(--br-text-mute);
  letter-spacing: 0.05em;
}

.au-token__usage {
  font-size: 11px;
  color: var(--br-text-soft);
  line-height: 1.4;
}

/* ---------- Type ramp ---------- */

.au-typeramp {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.au-typeramp__row {
  display: grid;
  grid-template-columns: 110px 80px 1fr;
  align-items: baseline;
  gap: 24px;
  padding-bottom: 14px;
  border-bottom: 1px dashed var(--br-line);
}

.au-typeramp__row:last-child { border-bottom: 0; padding-bottom: 0; }

.au-typeramp__label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  font-weight: 600;
}

.au-typeramp__meta {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  color: var(--br-text-mute);
}

.au-typeramp__sample { color: var(--br-text); }

/* ---------- Section catalog (the 8 sections) ---------- */

.au-catalog {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

@media (max-width: 1000px) { .au-catalog { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px)  { .au-catalog { grid-template-columns: 1fr; } }

.au-catalog__item {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-height: 220px;
}

.au-catalog__num {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--br-accent);
}

.au-catalog__item h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  line-height: 1.25;
}

.au-catalog__item p {
  margin: 0;
  font-size: 13px;
  line-height: 1.5;
  color: var(--br-text-soft);
}

.au-catalog__diagram {
  margin-top: auto;
  height: 60px;
  background: var(--au-bg);
  border: 1px solid var(--br-line-soft);
  display: grid;
  gap: 4px;
  padding: 4px;
}

/* ---------- Section mock wrapper ---------- */

.au-mock {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  margin-top: 24px;
  overflow: hidden;
}

.au-mock__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 18px 24px;
  border-bottom: 1px solid var(--br-line);
  background: #fbfaf6;
}

.au-mock__title {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.au-mock__title b {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--br-accent);
}

.au-mock__title h3 {
  font-size: 22px;
  font-weight: 500;
  margin: 0;
  letter-spacing: -0.01em;
}

.au-mock__tabs {
  display: flex;
  gap: 0;
  border: 1px solid var(--br-line);
}

.au-mock__tab {
  appearance: none;
  background: transparent;
  border: 0;
  padding: 8px 16px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text-soft);
  cursor: pointer;
  border-right: 1px solid var(--br-line);
  font-family: var(--t-font);
}

.au-mock__tab:last-child { border-right: 0; }

.au-mock__tab[aria-selected="true"] {
  background: var(--br-text);
  color: #fff;
}

.au-mock__stage {
  background: var(--br-bg);
  padding: 0;
  position: relative;
}

.au-mock__panel { display: none; }
.au-mock__panel[data-active="true"] { display: block; }

.au-mock__notes {
  padding: 18px 24px;
  background: #fbfaf6;
  border-top: 1px solid var(--br-line);
  font-size: 13px;
  line-height: 1.55;
  color: var(--br-text-soft);
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
}

.au-mock__notes b { color: var(--br-text); font-weight: 600; }

.au-mock__note-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.au-mock__note-item::before {
  content: "";
  width: 6px;
  height: 6px;
  background: var(--br-coral);
  border-radius: 50%;
  flex-shrink: 0;
}

/* ============================================================
   COMPONENT TOKENS (used inside section mocks — must look like
   the LIVE site after normalization)
   ============================================================ */

.br {
  font-family: var(--t-font);
  color: var(--br-text);
  background: var(--br-bg);
}

.br * { box-sizing: border-box; }

.br-eyebrow {
  font-size: var(--t-eyebrow);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-accent);
  margin: 0 0 12px;
  line-height: 1.3;
}

.br-display {
  font-size: clamp(var(--t-display-mobile), 5.4vw, var(--t-display));
  line-height: 1;
  font-weight: 400;
  letter-spacing: -0.02em;
  margin: 0;
}

.br-h1 {
  font-size: clamp(var(--t-h1-mobile), 4vw, var(--t-h1));
  line-height: 1.05;
  font-weight: 400;
  letter-spacing: -0.015em;
  margin: 0;
}

.br-h2 {
  font-size: clamp(28px, 2.6vw, var(--t-h2));
  line-height: 1.1;
  font-weight: 500;
  letter-spacing: -0.01em;
  margin: 0;
}

.br-h3 {
  font-size: var(--t-h3);
  line-height: 1.15;
  font-weight: 500;
  letter-spacing: -0.005em;
  margin: 0;
}

.br-h4 {
  font-size: var(--t-h4);
  line-height: 1.2;
  font-weight: 500;
  margin: 0;
}

.br-h5 {
  font-size: var(--t-h5);
  line-height: 1.3;
  font-weight: 500;
  margin: 0;
}

.br-body {
  font-size: var(--t-body);
  line-height: 1.6;
  margin: 0;
  color: var(--br-text);
}

.br-body-lg {
  font-size: var(--t-body-lg);
  line-height: 1.55;
  margin: 0;
  color: var(--br-text);
}

.br-body-sm {
  font-size: var(--t-body-sm);
  line-height: 1.5;
  margin: 0;
}

/* Buttons */
.br-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: var(--t-font);
  font-size: var(--btn-text-size);
  font-weight: var(--btn-weight);
  letter-spacing: var(--btn-letter);
  text-transform: uppercase;
  padding: var(--btn-pad-y) var(--btn-pad-x);
  border-radius: var(--btn-radius);
  text-decoration: none;
  border: 1px solid transparent;
  cursor: pointer;
  transition: opacity 0.15s, background-color 0.15s, color 0.15s;
  line-height: 1;
}

.br-btn:hover { opacity: 0.88; }

.br-btn--primary {
  background: var(--br-button);
  color: var(--br-button-text);
  border-color: var(--br-button);
}

.br-btn--secondary {
  background: transparent;
  color: var(--br-text);
  border-color: var(--br-text);
}

.br-btn--tertiary {
  background: transparent;
  color: var(--br-text);
  border-color: transparent;
  padding-left: 0;
  padding-right: 0;
  border-bottom: 1px solid var(--br-text);
  border-radius: 0;
}

.br-btn--invert {
  background: #ffffff;
  color: var(--br-text);
  border-color: #ffffff;
}

.br-btn--on-image {
  background: transparent;
  color: #ffffff;
  border-color: #ffffff;
}

.br-btn--lg { font-size: 15px; padding: 16px 32px; }
.br-btn--sm { font-size: 12px; padding: 10px 20px; }

/* Section helpers */
.br-section {
  padding: var(--sp-9) var(--sp-5);
}
.br-section--tight { padding: var(--sp-7) var(--sp-5); }

.br-container { max-width: 1280px; margin: 0 auto; }
.br-container--narrow { max-width: 880px; margin: 0 auto; }

.br-grid { display: grid; }
.br-flex { display: flex; }

/* Image placeholder */
.br-img {
  background:
    repeating-linear-gradient(
      135deg,
      #efece2 0 16px,
      #e8e4d6 16px 32px
    );
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.05em;
  text-align: center;
  padding: 12px;
  text-transform: lowercase;
}

.br-img--dark {
  background:
    repeating-linear-gradient(
      135deg,
      #2c2c2c 0 16px,
      #232323 16px 32px
    );
  color: #b5b0a1;
}

.br-img--blush {
  background:
    repeating-linear-gradient(
      135deg,
      #f3e3dc 0 16px,
      #efdcd2 16px 32px
    );
  color: #9c7464;
}

.br-img--ink {
  background:
    repeating-linear-gradient(
      135deg,
      #1f1f1f 0 16px,
      #161616 16px 32px
    );
  color: #888;
}

/* Why-it-works strip (canonical) */
.br-why-strip {
  background: var(--br-alt-bg);
  display: flex;
  align-items: stretch;
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
  width: 100%;
  -webkit-font-smoothing: antialiased;
}
.br-why-strip__label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--br-text);
  white-space: nowrap;
  padding: 14px 22px;
  background: #ffffff;
  border-right: 1px solid var(--br-line);
}
.br-why-strip__pts {
  display: flex;
  flex: 1;
  justify-content: space-between;
  align-items: center;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
  padding: 14px 22px;
  gap: 10px;
}
.br-why-strip__div {
  width: 1px;
  height: 12px;
  background: var(--br-line);
  flex-shrink: 0;
}

/* ============================================================
   Section: Header (chrome)
   ============================================================ */

.br-header {
  background: var(--br-bg);
  color: var(--br-text);
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 18px 32px;
  border-bottom: 1px solid var(--br-line);
}

.br-header__nav {
  display: flex;
  gap: 28px;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-weight: 500;
}

.br-header__logo {
  font-size: 22px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 400;
}

.br-header__util {
  justify-self: end;
  display: flex;
  gap: 18px;
  align-items: center;
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.br-header__cart {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  position: relative;
}

.br-header__cart-dot {
  width: 8px; height: 8px;
  background: var(--br-coral);
  border-radius: 50%;
}

/* Announcement strip */
.br-announce {
  background: var(--br-text);
  color: #fff;
  text-align: center;
  font-size: 11.5px;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  padding: 9px 16px;
  font-weight: 500;
}

/* ============================================================
   Footer
   ============================================================ */

.br-footer {
  background: var(--br-bg);
  color: var(--br-text);
  padding: 80px 32px 32px;
  border-top: 1px solid var(--br-line);
}

.br-footer__grid {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.4fr repeat(4, 1fr);
  gap: 48px;
  padding-bottom: 64px;
  border-bottom: 1px solid var(--br-line);
}

@media (max-width: 800px) {
  .br-footer__grid { grid-template-columns: 1fr 1fr; gap: 32px; }
}

.br-footer__col h6 {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-weight: 600;
  margin: 0 0 18px;
  opacity: 0.7;
}

.br-footer__col ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.br-footer__col a {
  color: var(--br-text);
  text-decoration: none;
  font-size: 14px;
  border-bottom: 1px solid transparent;
}

.br-footer__col a:hover { border-color: currentColor; }

.br-footer__brand .br-header__logo { color: var(--br-text); }

.br-footer__bottom {
  max-width: 1280px;
  margin: 0 auto;
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  opacity: 0.7;
  flex-wrap: wrap;
  gap: 16px;
}
/* ============================================================
   PDP pixel-final stylesheet
   Inherits all tokens from audit-styles.css
   ============================================================ */

html, body { background: #ffffff; }

/* ---------- Announcement + header ---------- */

/* ============================================================
   ROTATING TICKER — single strip, messages cross-fade
   ============================================================ */
.pdp-ticker {
  background: var(--br-text);
  color: #fff;
  height: 36px;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.pdp-ticker__slide {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0 16px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.55s ease, transform 0.55s ease;
  white-space: nowrap;
}
.pdp-ticker__slide.is-active {
  opacity: 1;
  transform: translateY(0);
}
.pdp-ticker__slide b { font-weight: 700; }
.pdp-ticker__slide a {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.6);
  padding-bottom: 1px;
  margin-left: 6px;
}
.pdp-ticker__slide a:hover { color: #fff; border-color: #fff; }

@media (max-width: 600px) {
  .pdp-ticker__slide { font-size: 11px; letter-spacing: 0.08em; }
}

.pdp-announce {
  background: var(--br-text);
  color: #fff;
  text-align: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 11px 16px;
}

.pdp-announce--sale {
  background: var(--br-info);
  color: #fff;
  letter-spacing: 0.12em;
  font-weight: 600;
}
.pdp-announce--sale b { font-weight: 700; }

.pdp-announce--info {
  background: #fafafa;
  color: var(--br-text);
  font-weight: 500;
  font-size: 11.5px;
  border-bottom: 1px solid var(--br-line);
}
.pdp-announce--info a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  margin-left: 6px;
  font-weight: 500;
}
.pdp-announce--info a:hover { opacity: 0.7; }

.pdp-header {
  position: sticky;
  top: 0;
  z-index: 30;
  background: #ffffff;
  border-bottom: 1px solid var(--br-line);
}

.pdp-header__inner {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 18px 32px;
  gap: 24px;
}

.pdp-header__nav {
  display: flex;
  gap: 30px;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.01em;
}
.pdp-header__nav a {
  color: var(--br-text);
  text-decoration: none;
  padding: 4px 0;
  border-bottom: 1px solid transparent;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.pdp-header__nav a:hover { border-color: var(--br-text); }
.pdp-header__chev {
  font-size: 12px;
  line-height: 1;
  display: inline-block;
  margin-top: -1px;
  opacity: 0.7;
}

.pdp-header__logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 200px;
  height: 38px;
  padding: 0 8px;
  text-decoration: none;
}
.pdp-header__logo img {
  display: block;
  height: 100%;
  width: auto;
}
.pdp-header__logo--placeholder {
  border: 1px dashed var(--br-line);
  background: rgba(0,0,0,0.015);
  padding: 0 16px;
}
.pdp-header__logo span {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 10.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-mute);
  text-transform: lowercase;
}

.pdp-header__util {
  display: flex;
  gap: 24px;
  justify-content: flex-end;
  align-items: center;
  font-size: 13px;
  font-weight: 500;
}
.pdp-header__util a {
  color: var(--br-text);
  text-decoration: none;
  position: relative;
}
.pdp-header__cart {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.pdp-header__cart-dot {
  width: 24px; height: 24px;
  background: var(--br-accent);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0;
}
.pdp-header__cart-dot::before {
  content: "0";
}

/* ---------- Crumb ---------- */
.pdp-crumb {
  max-width: 1440px;
  margin: 0 auto;
  padding: 18px 32px 0;
  font-size: 11.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text-mute);
}
.pdp-crumb a { color: inherit; text-decoration: none; }
.pdp-crumb a:hover { color: var(--br-text); }

/* ============================================================
   PDP MAIN — gallery + buy box
   ============================================================ */

.pdp-main {
  max-width: 1440px;
  margin: 0 auto;
  padding: 32px 32px 80px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: flex-start;
}

@media (max-width: 1000px) {
  .pdp-main { grid-template-columns: 1fr; gap: 32px; }
}

/* Gallery */
.pdp-gallery {
  display: grid;
  grid-template-columns: 88px 1fr;
  gap: 12px;
  position: sticky;
  top: 88px;
}
@media (max-width: 700px) {
  .pdp-gallery { grid-template-columns: 1fr; position: static; }
  .pdp-gallery__thumbs { display: flex; flex-direction: row; }
}

.pdp-gallery__thumbs {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pdp-gallery__thumb {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 10px, #e8e4d6 10px 20px);
  border: 1px solid transparent;
  cursor: pointer;
  position: relative;
}
.pdp-gallery__thumb[aria-selected="true"] { border-color: var(--br-text); }
.pdp-gallery__thumb--blush {
  background:
    repeating-linear-gradient(135deg, #f3e3dc 0 10px, #efdcd2 10px 20px);
}
.pdp-gallery__thumb--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 10px, #232323 10px 20px);
}
.pdp-gallery__thumb--video::after {
  content: "▶";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 16px;
  color: rgba(255,255,255,0.8);
}

.pdp-gallery__hero {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  color: #8a7e63;
  position: relative;
}
.pdp-gallery__zoom {
  position: absolute;
  bottom: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  background: rgba(255,255,255,0.9);
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 16px;
  color: var(--br-text);
}

/* Buy box */
.pdp-buy {
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding-top: 6px;
}

.pdp-buy__judge {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--br-text-soft);
}
.pdp-buy__stars {
  color: var(--br-accent);
  letter-spacing: 0.16em;
}
.pdp-buy__judge a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  font-weight: 500;
}

.pdp-buy__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  margin: 0;
}

.pdp-buy__name {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 400;
  margin: 0;
  letter-spacing: -0.015em;
  line-height: 1.1;
}

/* v2 — Brand-line dominant hierarchy */
.pdp-buy__seo-label {
  font-size: 16px;
  font-weight: 500;
  letter-spacing: -0.005em;
  color: var(--br-text);
  margin: 6px 0 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--br-line);
  line-height: 1.3;
}

.pdp-buy__name--brand {
  font-size: clamp(34px, 3.8vw, 52px);
  font-weight: 400;
  line-height: 1;
  letter-spacing: -0.02em;
}
.pdp-buy__seo {
  font-size: 15px;
  line-height: 1.4;
  color: var(--br-text-soft);
  margin: 14px 0 0;
  max-width: 50ch;
  font-weight: 400;
}

.pdp-buy__tagline {
  font-size: clamp(17px, 1.6vw, 20px);
  font-weight: 500;
  color: var(--br-text);
  margin: 10px 0 0;
  letter-spacing: -0.005em;
  line-height: 1.3;
}

.pdp-buy__sub {
  font-size: 15px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
  max-width: 50ch;
}

.pdp-buy__price {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-top: 4px;
}
.pdp-buy__price-now {
  font-size: 22px;
  font-weight: 500;
}
.pdp-buy__price-meta {
  font-size: 12.5px;
  color: var(--br-text-soft);
  letter-spacing: 0.04em;
}

.pdp-buy__row { display: flex; flex-direction: column; gap: 10px; }
.pdp-buy__row-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
}
.pdp-buy__row-head a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  font-weight: 500;
}

.pdp-buy__swatches {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.pdp-buy__swatch {
  width: 36px;
  height: 36px;
  border: 1px solid var(--br-line);
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  transition: border-color 0.12s, transform 0.12s;
}
.pdp-buy__swatch:hover { transform: scale(1.06); }
.pdp-buy__swatch[aria-selected="true"] {
  border-color: var(--br-text);
  box-shadow: inset 0 0 0 2px #fff;
}
.pdp-buy__swatch[data-le]::after {
  content: "LE";
  position: absolute;
  top: -8px; right: -8px;
  background: var(--br-le);
  color: #fff;
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 2px 5px 1px;
  border-radius: 2px;
}

.pdp-buy__sizes {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 6px;
}
.pdp-buy__sizes--two {
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.pdp-buy__size {
  border: 1px solid var(--br-text);
  background: #fff;
  padding: 12px 4px;
  text-align: center;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.12s, color 0.12s;
}
.pdp-buy__size--wide {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 16px 12px;
}
.pdp-buy__size-letter {
  font-size: 22px;
  font-weight: 500;
  letter-spacing: 0.04em;
  line-height: 1;
}
.pdp-buy__size-meta {
  font-size: 11px;
  letter-spacing: 0.04em;
  color: var(--br-text-soft);
  text-transform: none;
}
.pdp-buy__size--wide[aria-selected="true"] .pdp-buy__size-meta {
  color: rgba(255,255,255,0.78);
}
.pdp-buy__size:hover { background: var(--br-text); color: #fff; }
.pdp-buy__size[aria-selected="true"] { background: var(--br-text); color: #fff; }
.pdp-buy__size[disabled] {
  opacity: 0.34;
  color: var(--br-text-mute);
  border-color: var(--br-line);
  text-decoration: line-through;
  cursor: not-allowed;
}
.pdp-buy__size[disabled]:hover { background: transparent; color: var(--br-text-mute); }

.pdp-buy__cta-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-buy__cta {
  background: var(--br-text);
  color: #fff;
  border: 0;
  padding: 18px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: opacity 0.15s;
  text-align: center;
}
.pdp-buy__cta:hover { opacity: 0.88; }

.pdp-buy__shipnote {
  display: flex;
  gap: 16px;
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  flex-wrap: wrap;
}
.pdp-buy__shipnote span::before {
  content: "✓ ";
  color: var(--br-accent);
  margin-right: 2px;
  font-weight: 700;
}

.pdp-buy__tabs {
  border-top: 1px solid var(--br-line);
  margin-top: 4px;
}
.pdp-buy__tab {
  border-bottom: 1px solid var(--br-line);
}
.pdp-buy__tab summary {
  list-style: none;
  cursor: pointer;
  padding: 16px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.06em;
}
.pdp-buy__tab summary::-webkit-details-marker { display: none; }
.pdp-buy__tab summary::after {
  content: "+";
  font-weight: 300;
  font-size: 22px;
  color: var(--br-text-mute);
  transition: transform 0.15s;
}
.pdp-buy__tab[open] summary::after {
  content: "−";
}
.pdp-buy__tab-body {
  padding: 0 0 18px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--br-text-soft);
}
.pdp-buy__tab-body p { margin: 0 0 10px; }
.pdp-buy__tab-body p:last-child { margin-bottom: 0; }

/* ============================================================
   PILLAR STRIP
   ============================================================ */

.pdp-pillars {
  background: var(--br-alt-bg);
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
}
.pdp-pillars__inner {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  align-items: stretch;
}
.pdp-pillars__label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-text);
  white-space: nowrap;
  padding: 18px 28px;
  background: #fff;
  border-right: 1px solid var(--br-line);
  display: flex;
  align-items: center;
}
.pdp-pillars__pts {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 32px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  gap: 20px;
}
.pdp-pillars__div {
  width: 1px;
  height: 14px;
  background: var(--br-line);
}

@media (max-width: 800px) {
  .pdp-pillars__label { display: none; }
  .pdp-pillars__pts {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    font-size: 10.5px;
    text-align: center;
  }
  .pdp-pillars__div { display: none; }
}

/* ============================================================
   SECTION HELPERS
   ============================================================ */

.pdp-section {
  max-width: 1440px;
  margin: 0 auto;
  padding: 96px 32px;
}
.pdp-section--tight { padding: 64px 32px; }
.pdp-section--alt { background: var(--br-alt-bg); max-width: none; }
.pdp-section--alt > * {
  max-width: 1440px;
  margin-left: auto;
  margin-right: auto;
}

.pdp-eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  margin: 0 0 14px;
}

.pdp-h2 {
  font-size: clamp(28px, 3.2vw, 44px);
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.1;
  margin: 0;
  text-wrap: balance;
}

.pdp-h3 {
  font-size: clamp(20px, 1.6vw, 24px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.2;
  margin: 0;
}

.pdp-lede {
  font-size: 18px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 16px 0 0;
  max-width: 60ch;
}

/* ============================================================
   PREMIUM / VALUE BLOCK — addresses the "expensive" objection
   ============================================================ */

.pdp-value {
  background: var(--br-text);
  color: #fff;
}
.pdp-value__inner {
  max-width: 1440px;
  margin: 0 auto;
  padding: 96px 32px;
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 64px;
  align-items: center;
}
@media (max-width: 900px) {
  .pdp-value__inner { grid-template-columns: 1fr; padding: 64px 24px; gap: 32px; }
}

.pdp-value__copy .pdp-eyebrow { color: rgba(255,255,255,0.7); }
.pdp-value__copy .pdp-h2 { color: #fff; }
.pdp-value__copy .pdp-lede { color: rgba(255,255,255,0.78); }

.pdp-value__compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.12);
}
.pdp-value__col {
  padding: 26px 24px;
  background: var(--br-text);
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-value__col--ours { background: #1a1a1a; }
.pdp-value__tag {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.6);
}
.pdp-value__col--ours .pdp-value__tag { color: var(--br-accent); }
.pdp-value__amount {
  font-size: clamp(28px, 3vw, 38px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1;
  color: #fff;
  margin: 4px 0 12px;
}
.pdp-value__amount-unit {
  font-size: 13px;
  font-weight: 400;
  color: rgba(255,255,255,0.55);
  letter-spacing: 0;
  margin-left: 4px;
}
.pdp-value__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 13.5px;
  color: rgba(255,255,255,0.78);
}
.pdp-value__list li {
  position: relative;
  padding-left: 16px;
}
.pdp-value__list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 1px;
  background: rgba(255,255,255,0.4);
}
.pdp-value__col--ours .pdp-value__list li::before {
  background: var(--br-accent);
}

/* ============================================================
   BENEFIT GRID — PDP variant
   ============================================================ */

.pdp-benefits {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 48px;
}
@media (max-width: 800px) {
  .pdp-benefits { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 520px) {
  .pdp-benefits { grid-template-columns: 1fr; }
}

.pdp-benefit {
  background: #fff;
  border-top: 2px solid var(--br-text);
  padding: 22px 22px 26px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pdp-benefit__num {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  margin-bottom: 8px;
}
.pdp-benefit__title {
  font-size: 17px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.005em;
}
.pdp-benefit__sub {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
}

/* ============================================================
   MEDIA SPLIT (story block)
   ============================================================ */

.pdp-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  min-height: 580px;
}
@media (max-width: 900px) {
  .pdp-split { grid-template-columns: 1fr; min-height: 0; }
}

.pdp-split__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  min-height: 100%;
  position: relative;
}
.pdp-split__media--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 18px, #232323 18px 36px);
  color: #a39a83;
}
.pdp-split__media-tag {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(0,0,0,0.5);
  color: #fff;
  padding: 5px 9px;
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 0;
}

.pdp-split__copy {
  padding: 80px 64px;
  background: var(--br-alt-bg);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
@media (max-width: 900px) {
  .pdp-split__copy { padding: 48px 24px; }
  .pdp-split__media { aspect-ratio: 4/5; }
}
.pdp-split__copy .pdp-h2 { margin-bottom: 16px; }

.pdp-split__list {
  list-style: none;
  margin: 28px 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 15px;
}
.pdp-split__list li {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.pdp-split__list li::before {
  content: "→";
  color: var(--br-accent);
  font-weight: 700;
  flex-shrink: 0;
}

/* ============================================================
   TESTIMONIAL
   ============================================================ */

.pdp-quote {
  text-align: center;
  max-width: 760px;
  margin: 0 auto;
}
.pdp-quote__stars {
  color: var(--br-accent);
  letter-spacing: 0.2em;
  font-size: 18px;
  margin-bottom: 22px;
}
.pdp-quote__body {
  font-size: clamp(22px, 2.4vw, 32px);
  font-weight: 400;
  line-height: 1.35;
  margin: 0 0 24px;
  text-wrap: balance;
  letter-spacing: -0.005em;
  color: var(--br-text);
}
.pdp-quote__attr {
  font-size: 11.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pdp-quote__attr b {
  color: var(--br-text);
  font-weight: 700;
  margin-right: 8px;
}

/* ============================================================
   VARIANT GRID — "Shop all colors & sizes"
   ============================================================ */

.pdp-variants__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}
.pdp-variants__head-meta { display: flex; flex-direction: column; gap: 4px; }
.pdp-variants__head-link {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
}

.pdp-variants__tabs {
  display: flex;
  gap: 0;
  margin-bottom: 28px;
}
.pdp-variant-tab {
  font-family: inherit;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.04em;
  padding: 12px 22px;
  border: 1px solid var(--br-text);
  background: #fff;
  color: var(--br-text);
  cursor: pointer;
  margin: 0 -1px 0 0;
  position: relative;
  transition: background 0.12s, color 0.12s;
}
.pdp-variant-tab[aria-selected="true"] {
  background: var(--br-text);
  color: #fff;
  z-index: 2;
}
.pdp-variant-tab:hover:not([aria-selected="true"]) {
  background: var(--br-alt-bg);
}

.pdp-variants__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 1000px) { .pdp-variants__grid { grid-template-columns: repeat(2, 1fr); } }

.pdp-vcard {
  background: #fff;
  display: flex;
  flex-direction: column;
  position: relative;
  cursor: pointer;
}
.pdp-vcard__media {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  margin-bottom: 14px;
  position: relative;
  overflow: hidden;
}
.pdp-vcard__media--blush {
  background: repeating-linear-gradient(135deg, #f3e3dc 0 14px, #efdcd2 14px 28px);
}
.pdp-vcard__media--stone {
  background: repeating-linear-gradient(135deg, #d4d0c4 0 14px, #c9c5b8 14px 28px);
}
.pdp-vcard__media--dark {
  background: repeating-linear-gradient(135deg, #2c2c2c 0 14px, #232323 14px 28px);
}
.pdp-vcard__le {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--br-le);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 4px 8px 3px;
}
.pdp-vcard__quick {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  background: rgba(255,255,255,0.96);
  color: var(--br-text);
  padding: 10px;
  text-align: center;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  opacity: 0;
  transition: opacity 0.15s;
}
.pdp-vcard:hover .pdp-vcard__quick { opacity: 1; }

.pdp-vcard__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
  line-height: 1.35;
}
.pdp-vcard__meta {
  font-size: 12px;
  color: var(--br-text-soft);
  letter-spacing: 0.02em;
}
.pdp-vcard__price {
  font-size: 13px;
  font-weight: 500;
  margin-top: 2px;
}
.pdp-vcard__sale {
  color: var(--br-accent);
  font-weight: 500;
}
.pdp-vcard__sale s {
  color: var(--br-text-mute);
  text-decoration: line-through;
  font-weight: 400;
  margin-right: 4px;
}

/* ============================================================
   REVIEWS (Judge.me restyled)
   ============================================================ */

.pdp-reviews__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: 32px;
  gap: 24px;
  flex-wrap: wrap;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
}
.pdp-reviews__head-bigstars {
  font-size: 32px;
  color: var(--br-accent);
  letter-spacing: 0.18em;
  line-height: 1;
}
.pdp-reviews__head-summary {
  font-size: 14px;
  color: var(--br-text-soft);
  margin-top: 4px;
}
.pdp-reviews__head-summary b { color: var(--br-text); font-weight: 600; }

.pdp-reviews__grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0;
  border-top: 1px solid var(--br-line);
}
.pdp-review {
  padding: 24px 32px;
  border-bottom: 1px solid var(--br-line);
  border-right: 1px solid var(--br-line);
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.pdp-review:nth-child(2n) { border-right: 0; }
.pdp-review__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pdp-review__stars { color: var(--br-accent); letter-spacing: 0.16em; font-size: 13px; }
.pdp-review__verified {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.pdp-review__verified::before {
  content: "✓";
  color: var(--br-accent);
  font-weight: 700;
}
.pdp-review__title {
  font-size: 15px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.005em;
}
.pdp-review__body {
  font-size: 14px;
  line-height: 1.6;
  color: var(--br-text);
  margin: 0;
}
.pdp-review__attr {
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  margin: 0;
}
.pdp-review__attr b { color: var(--br-text); font-weight: 600; }

@media (max-width: 720px) {
  .pdp-reviews__grid { grid-template-columns: 1fr; }
  .pdp-review { border-right: 0; }
}

.pdp-reviews__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pdp-reviews__more {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 500;
}
.pdp-reviews__write {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  background: var(--br-text);
  color: #fff;
  padding: 12px 20px;
  font-weight: 700;
}
.pdp-reviews__write:hover { opacity: 0.88; }

/* ============================================================
   FAQ
   ============================================================ */

.pdp-faq {
  max-width: 880px;
  margin: 0 auto;
}
.pdp-faq__list {
  margin-top: 32px;
  border-top: 1px solid var(--br-line);
}
.pdp-faq__item {
  border-bottom: 1px solid var(--br-line);
}
.pdp-faq__item summary {
  list-style: none;
  cursor: pointer;
  padding: 22px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  font-size: 17px;
  font-weight: 500;
  letter-spacing: -0.005em;
}
.pdp-faq__item summary::-webkit-details-marker { display: none; }
.pdp-faq__item summary::after {
  content: "+";
  font-size: 24px;
  font-weight: 300;
  color: var(--br-text-mute);
  flex-shrink: 0;
}
.pdp-faq__item[open] summary::after { content: "−"; }
.pdp-faq__body {
  padding: 0 0 22px;
  font-size: 15px;
  line-height: 1.65;
  color: var(--br-text-soft);
  max-width: 64ch;
}
.pdp-faq__body p { margin: 0 0 12px; }
.pdp-faq__body p:last-child { margin-bottom: 0; }
.pdp-faq__body a {
  color: var(--br-text);
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  text-decoration: none;
}

/* ============================================================
   PRODUCT RAIL — pairs with your kit
   ============================================================ */

.pdp-rail__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: 32px;
  gap: 24px;
}
.pdp-rail__list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 900px) { .pdp-rail__list { grid-template-columns: 1fr 1fr; } }

.pdp-rail-card {
  background: #fff;
  display: flex;
  flex-direction: column;
}
.pdp-rail-card__media {
  aspect-ratio: 4/5;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  margin-bottom: 14px;
}
.pdp-rail-card__media--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 14px, #efdcd2 14px 28px); }
.pdp-rail-card__media--stone { background: repeating-linear-gradient(135deg, #d4d0c4 0 14px, #c9c5b8 14px 28px); }
.pdp-rail-card__media--dark  { background: repeating-linear-gradient(135deg, #2c2c2c 0 14px, #232323 14px 28px); }
.pdp-rail-card__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
}
.pdp-rail-card__price {
  font-size: 13px;
  color: var(--br-text-soft);
  margin: 0;
}

/* ============================================================
   Tweaks-controlled variants
   ============================================================ */

/* Quick Add legacy hover button kept for tweaks-panel testing only;
   the production default is the text-link .pdp-vcard__addlink */
.pdp-vcard__add {
  display: none !important;
}

/* Card style — bordered variant */
[data-card-style="bordered"] .pdp-vcard {
  border: 1px solid var(--br-line);
  padding: 12px;
  background: #fff;
  transition: border-color 0.15s;
}
[data-card-style="bordered"] .pdp-vcard:hover { border-color: var(--br-text); }
[data-card-style="bordered"] .pdp-vcard__media { margin-bottom: 12px; }

/* Verified badge toggle */
[data-verified="off"] .pdp-review__verified { display: none; }

/* CTA size variants */
[data-cta-size="compact"] .pdp-buy__cta { padding: 14px; font-size: 13px; }
[data-cta-size="bold"]    .pdp-buy__cta { padding: 22px; font-size: 15px; letter-spacing: 0.14em; }

/* ============================================================ */

.pdp-footer {
  background: #fff;
  border-top: 1px solid var(--br-line);
  padding: 80px 32px 32px;
}
.pdp-footer__grid {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.4fr repeat(4, 1fr);
  gap: 48px;
  padding-bottom: 56px;
  border-bottom: 1px solid var(--br-line);
}
@media (max-width: 900px) {
  .pdp-footer__grid { grid-template-columns: 1fr 1fr; gap: 32px; }
}
.pdp-footer__brand .pdp-header__logo {
  margin-bottom: 16px;
}
.pdp-footer__brand p {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  max-width: 32ch;
  margin: 0 0 20px;
}
.pdp-footer__newsletter {
  display: flex;
  gap: 0;
  border: 1px solid var(--br-text);
}
.pdp-footer__newsletter input {
  flex: 1;
  padding: 12px 14px;
  font-family: inherit;
  font-size: 13px;
  border: 0;
  background: transparent;
  color: var(--br-text);
}
.pdp-footer__newsletter input::placeholder { color: var(--br-text-mute); }
.pdp-footer__newsletter button {
  background: var(--br-text);
  color: #fff;
  border: 0;
  padding: 12px 16px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

.pdp-footer__col h6 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 18px;
  color: var(--br-text);
}
.pdp-footer__col ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-footer__col a {
  color: var(--br-text-soft);
  text-decoration: none;
  font-size: 14px;
}
.pdp-footer__col a:hover { color: var(--br-text); }

.pdp-footer__bottom {
  max-width: 1440px;
  margin: 0 auto;
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 12px;
  color: var(--br-text-mute);
  letter-spacing: 0.02em;
}
/* ============================================================
   pages-extras.css — components used on Home / Collection / Article / Blog
   that aren't already in pdp-styles.css
   ============================================================ */

/* ============== MEDIA SPLIT HERO (Home + Collection short hero) ============== */

.pg-hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 640px;
  background: var(--br-alt-bg);
  border-bottom: 1px solid var(--br-line);
}
.pg-hero-split--short { min-height: 380px; }
.pg-hero-split--reverse .pg-hero-split__media { order: 2; }

.pg-hero-split__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  min-height: 100%;
  position: relative;
}
.pg-hero-split__media--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 18px, #232323 18px 36px);
  color: #a39a83;
}
.pg-hero-split__media--blush {
  background:
    repeating-linear-gradient(135deg, #f3e3dc 0 18px, #efdcd2 18px 36px);
  color: #9c7464;
}
.pg-hero-split__media-tag {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(0,0,0,0.5);
  color: #fff;
  padding: 5px 10px;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.pg-hero-split__copy {
  padding: 96px 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: #ffffff;
}
.pg-hero-split--short .pg-hero-split__copy { padding: 56px 64px; }

.pg-hero-split__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-accent);
  margin: 0 0 14px;
}
.pg-hero-split__title {
  font-size: clamp(36px, 4.4vw, 60px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.02;
  margin: 0;
  max-width: 16ch;
  text-wrap: balance;
}
.pg-hero-split--short .pg-hero-split__title {
  font-size: clamp(28px, 3.2vw, 44px);
  max-width: 22ch;
}
.pg-hero-split__body {
  font-size: 17px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 18px 0 0;
  max-width: 48ch;
}
.pg-hero-split__ctas {
  display: flex;
  gap: 12px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pg-hero-split__cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
  border: 1px solid var(--br-text);
  background: var(--br-text);
  color: #fff;
  cursor: pointer;
  transition: opacity 0.15s, background 0.15s, color 0.15s;
}
.pg-hero-split__cta:hover { opacity: 0.88; }
.pg-hero-split__cta--secondary {
  background: transparent;
  color: var(--br-text);
  border-color: var(--br-text);
}

@media (max-width: 900px) {
  .pg-hero-split { grid-template-columns: 1fr; min-height: 0; }
  .pg-hero-split__media { aspect-ratio: 4/5; }
  .pg-hero-split__copy { padding: 48px 24px; }
  .pg-hero-split--short .pg-hero-split__copy { padding: 32px 24px; }
}

/* ============== COLLAB HERO (Home + Collection feature) ============== */

.pg-collab {
  position: relative;
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 20px, #232323 20px 40px);
  min-height: 560px;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}
.pg-collab__overlay {
  position: relative;
  z-index: 2;
  padding: 80px 64px;
  width: 100%;
  background:
    linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.55) 100%);
  color: #fff;
}
.pg-collab__overlay-inner { max-width: 1440px; margin: 0 auto; }
.pg-collab__le {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.14);
  color: #cfe1ff;
  padding: 8px 14px 7px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  border-radius: 999px;
  margin-bottom: 18px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.pg-collab__le::before {
  content: "";
  display: inline-block;
  width: 6px;
  height: 6px;
  background: var(--br-le);
  border-radius: 50%;
}
.pg-collab__title {
  font-size: clamp(40px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 0.98;
  margin: 0;
  text-wrap: balance;
  max-width: 18ch;
}
.pg-collab__sub {
  font-size: clamp(16px, 1.6vw, 19px);
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.92;
  max-width: 56ch;
}
.pg-collab__ctas {
  display: flex;
  gap: 12px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pg-collab__cta {
  display: inline-block;
  background: #ffffff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-collab__cta--ghost {
  background: transparent;
  color: #fff;
  border: 1px solid rgba(255,255,255,0.6);
}

@media (max-width: 700px) {
  .pg-collab__overlay { padding: 48px 24px; }
}

/* ============================================================
   HERO VIDEO MOMENT · short film between hero and content
   ============================================================ */
.pg-video-moment {
  position: relative;
  aspect-ratio: 21/9;
  min-height: 380px;
  max-height: 640px;
  overflow: hidden;
  background: #050505;
}
.pg-video-moment__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-video-moment__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 48px 32px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.45) 100%);
  color: #fff;
}
.pg-video-moment__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 14px;
  opacity: 0.88;
}
.pg-video-moment__title {
  font-size: clamp(32px, 4vw, 56px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1.05;
  margin: 0;
  max-width: 22ch;
  text-wrap: balance;
}

/* ============================================================
   COPERNI v2 · runway-first collab layout
   ============================================================ */
.pg-collab-v2 {
  background: #050505;
  color: #fff;
}
.pg-collab-v2__hero {
  position: relative;
  aspect-ratio: 16/8;
  min-height: 520px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
}
.pg-collab-v2__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-collab-v2__overlay {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 64px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.6) 100%);
  max-width: 1600px;
  margin: 0 auto;
}
.pg-collab-v2__title {
  font-size: clamp(36px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 12px 0 0;
  text-wrap: balance;
}
.pg-collab-v2__sub {
  font-size: clamp(15px, 1.5vw, 18px);
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.92;
  max-width: 60ch;
}
.pg-collab-v2__ctas { margin-top: 28px; }
.pg-collab-v2__gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2px;
  background: #050505;
}
.pg-collab-v2__tile {
  margin: 0;
  aspect-ratio: 3/4;
  overflow: hidden;
  background: #1a1a1a;
}
.pg-collab-v2__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-collab-v2__tile--copy {
  background: #f9f9f9;
  color: var(--br-text);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 32px;
}
@media (max-width: 900px) {
  .pg-collab-v2__gallery { grid-template-columns: 1fr 1fr; }
  .pg-collab-v2__overlay { padding: 32px 24px; }
}

/* ============================================================
   COPERNI GRID · 1 feature + 3 tiles (v5a)
   ============================================================ */
.pg-coperni-grid {
  background: #050505;
  color: #fff;
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 2px;
  min-height: 560px;
}
.pg-coperni-grid__feature {
  position: relative;
  overflow: hidden;
  background: #1a1a1a;
  display: flex;
  align-items: flex-end;
  min-height: 560px;
}
.pg-coperni-grid__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-coperni-grid__overlay {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 40px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.6) 100%);
  color: #fff;
}
.pg-coperni-grid__title {
  font-size: clamp(32px, 3.6vw, 52px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 12px 0 14px;
}
.pg-coperni-grid__sub {
  font-size: 16px;
  line-height: 1.5;
  margin: 0 0 22px;
  opacity: 0.92;
  max-width: 44ch;
}
.pg-coperni-grid__cta {
  font-size: 12px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #fff;
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.6);
  padding-bottom: 2px;
  font-weight: 700;
}
.pg-coperni-grid__tiles {
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  gap: 2px;
  background: #050505;
}
.pg-coperni-grid__tile {
  margin: 0;
  overflow: hidden;
  background: #1a1a1a;
}
.pg-coperni-grid__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
@media (max-width: 900px) {
  .pg-coperni-grid { grid-template-columns: 1fr; }
  .pg-coperni-grid__feature { min-height: 420px; }
  .pg-coperni-grid__tiles { grid-template-rows: none; grid-template-columns: repeat(3, 1fr); }
}

/* ============================================================
   FEATURED STRIP · 2-tile (v5b)
   ============================================================ */
.pg-feat-strip {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 32px;
}
.pg-feat-tile {
  display: flex;
  flex-direction: column;
  background: var(--br-alt-bg);
  text-decoration: none;
  color: var(--br-text);
  overflow: hidden;
  transition: opacity 0.15s;
}
.pg-feat-tile:hover { opacity: 0.92; }
.pg-feat-tile__media {
  aspect-ratio: 4/3;
  overflow: hidden;
  background: #f3f3f3;
}
.pg-feat-tile__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-feat-tile__copy {
  padding: 24px 28px 28px;
}
.pg-feat-tile__title {
  font-size: clamp(20px, 2vw, 28px);
  font-weight: 500;
  letter-spacing: -0.005em;
  margin: 4px 0 12px;
}
.pg-feat-tile__cta {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 700;
}
@media (max-width: 700px) {
  .pg-feat-strip { grid-template-columns: 1fr; padding: 0 16px; }
}

/* ============================================================
   VARIANT-CTA TWEAK MODES (Home tweaks panel)
   ============================================================ */
[data-variant-cta="off"] .pdp-vcard__addlink { display: none; }
[data-variant-cta="hover"] .pdp-vcard__addlink { display: none; }
[data-variant-cta="hover"] .pdp-vcard:hover .pdp-vcard__addlink { display: inline-block; }
[data-variant-cta="always"] .pdp-vcard__addlink {
  display: block;
  background: var(--br-text);
  color: #fff;
  text-align: center;
  padding: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  border: 0;
  margin-top: 12px;
}

/* ============================================================
   "Worn through every transition" media split placeholder slot
   ============================================================ */
.pg-text-with-media {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  min-height: 480px;
  background: var(--br-alt-bg);
}
.pg-text-with-media__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  color: #7a6f5b;
}
.pg-text-with-media__copy {
  padding: 64px 56px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
@media (max-width: 800px) {
  .pg-text-with-media { grid-template-columns: 1fr; }
  .pg-text-with-media__media { aspect-ratio: 4/5; }
  .pg-text-with-media__copy { padding: 40px 24px; }
}
.pg-hero-image {
  position: relative;
  height: 88vh;
  min-height: 580px;
  max-height: 820px;
  overflow: hidden;
  background: #0a0a0a;
}
.pg-hero-image__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-hero-image__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: 64px;
  background:
    linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%);
  color: #fff;
}
.pg-hero-image__copy { max-width: 780px; }
.pg-hero-image__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 16px;
  opacity: 0.88;
}
.pg-hero-image__title {
  font-size: clamp(40px, 5.4vw, 80px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-hero-image__body {
  font-size: 18px;
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.9;
  max-width: 50ch;
}
.pg-hero-image__ctas {
  display: flex;
  gap: 12px;
  margin-top: 28px;
  flex-wrap: wrap;
}
.pg-hero-image__cta {
  display: inline-block;
  background: #fff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-hero-image__cta--ghost {
  background: transparent;
  color: #fff;
  border: 1px solid #fff;
}
@media (max-width: 700px) {
  .pg-hero-image__overlay { padding: 32px 24px; }
  .pg-hero-image { height: 78vh; }
}

/* ============================================================
   THE SHOE IN MOTION · 3-up video grid
   ============================================================ */
.pg-motion-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.pg-motion {
  margin: 0;
  display: flex;
  flex-direction: column;
  background: var(--br-alt-bg);
  overflow: hidden;
}
.pg-motion__video {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  display: block;
  background: #f3f3f3;
}
.pg-motion__cap {
  padding: 18px 20px 22px;
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--br-text-soft);
}
.pg-motion__cap b {
  display: block;
  color: var(--br-text);
  font-weight: 600;
  letter-spacing: -0.005em;
  font-size: 15px;
  margin-bottom: 4px;
}
@media (max-width: 900px) {
  .pg-motion-grid { grid-template-columns: 1fr; gap: 24px; }
  .pg-motion__video { aspect-ratio: 16/9; }
}

/* ============================================================
   HOME v2 · FULL-BLEED VIDEO HERO
   ============================================================ */
.pg-hero-video {
  position: relative;
  height: 90vh;
  min-height: 580px;
  max-height: 820px;
  overflow: hidden;
  background: #050505;
}
.pg-hero-video__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-hero-video__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: 64px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%);
  color: #fff;
}
.pg-hero-video__copy { max-width: 780px; }
.pg-hero-video__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 16px;
  opacity: 0.88;
}
.pg-hero-video__title {
  font-size: clamp(40px, 5.4vw, 80px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-hero-video__body {
  font-size: 18px;
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.9;
  max-width: 50ch;
}
.pg-hero-video__ctas {
  display: flex;
  gap: 12px;
  margin-top: 28px;
  flex-wrap: wrap;
}
.pg-hero-video__cta {
  display: inline-block;
  background: #fff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-hero-video__cta--ghost {
  background: transparent;
  color: #fff;
  border: 1px solid #fff;
}
@media (max-width: 700px) {
  .pg-hero-video__overlay { padding: 32px 24px; }
  .pg-hero-video { height: 80vh; }
}

/* ============================================================
   HOME v3 · MULTI-TILE HERO
   ============================================================ */
.pg-hero-tiles {
  padding: 16px;
  background: #fff;
}
.pg-hero-tiles__grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: repeat(2, minmax(280px, 1fr));
  gap: 12px;
  max-width: 1600px;
  margin: 0 auto;
}
.pg-hero-tiles__feature {
  grid-column: 1;
  grid-row: 1 / 3;
  position: relative;
  overflow: hidden;
  background: #050505;
  min-height: 580px;
  display: flex;
  align-items: flex-end;
}
.pg-hero-tiles__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-hero-tiles__feature-copy {
  position: relative;
  z-index: 2;
  padding: 36px;
  color: #fff;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.6) 100%);
  width: 100%;
}
.pg-hero-tiles__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin: 0 0 14px;
  opacity: 0.9;
}
.pg-hero-tiles__title {
  font-size: clamp(28px, 3.4vw, 48px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.05;
  margin: 0 0 22px;
  max-width: 18ch;
  text-wrap: balance;
}
.pg-hero-tiles__cta {
  display: inline-block;
  background: #fff;
  color: var(--br-text);
  padding: 12px 24px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-hero-tile {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  padding: 22px;
  text-decoration: none;
  color: var(--br-text);
  min-height: 280px;
  background: var(--br-alt-bg);
}
.pg-hero-tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}
.pg-hero-tile span {
  position: relative;
  z-index: 2;
  font-size: clamp(20px, 2vw, 28px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.15;
  max-width: 16ch;
  color: var(--br-text);
  background: rgba(255,255,255,0.92);
  padding: 8px 14px;
  display: inline-block;
}
.pg-hero-tile--pink span, .pg-hero-tile--lilac span, .pg-hero-tile--yellow span {
  background: rgba(255,255,255,0.92);
}
@media (max-width: 900px) {
  .pg-hero-tiles__grid {
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto;
  }
  .pg-hero-tiles__feature { grid-column: span 2; grid-row: auto; min-height: 420px; }
}

/* ============================================================
   EQUAL-HEIGHT JOURNAL / EDITORIAL CARDS · fix
   ============================================================ */
.pg-edit {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.pg-edit__dek { flex: 1; }
.pg-editorial-grid, .pg-editorial-grid--six { align-items: stretch; }

/* ============================================================
   VARIANT CARD · "Add to cart →" text link (replaces overlay button)
   ============================================================ */
.pdp-vcard__addlink {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  margin-top: 8px;
  align-self: flex-start;
  display: inline-block;
}
.pdp-vcard__addlink:hover { opacity: 0.7; }

.pg-editorial__head {
  text-align: center;
  margin: 0 auto 48px;
  max-width: 56ch;
}
.pg-editorial__head .pdp-h2 { margin-bottom: 12px; }

.pg-editorial-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}
.pg-editorial-grid--six { grid-template-columns: repeat(3, 1fr); gap: 56px 32px; }
@media (max-width: 900px) {
  .pg-editorial-grid, .pg-editorial-grid--six { grid-template-columns: 1fr; gap: 32px; }
}

.pg-edit {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
}
.pg-edit__media {
  aspect-ratio: 4/3;
  background:
    repeating-linear-gradient(135deg, #efece2 0 16px, #e8e4d6 16px 32px);
  margin-bottom: 16px;
  transition: opacity 0.2s;
}
.pg-edit__media--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 16px, #efdcd2 16px 32px); }
.pg-edit__media--dark  { background: repeating-linear-gradient(135deg, #2c2c2c 0 16px, #232323 16px 32px); }
.pg-edit__media--stone { background: repeating-linear-gradient(135deg, #d4d0c4 0 16px, #c9c5b8 16px 32px); }
.pg-edit:hover .pg-edit__media { opacity: 0.92; }

.pg-edit__meta {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
  margin: 4px 0 8px;
}
.pg-edit__title {
  font-size: 22px;
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.2;
  margin: 0 0 8px;
  color: var(--br-text);
}
.pg-edit__dek {
  font-size: 14.5px;
  color: var(--br-text-soft);
  line-height: 1.55;
  margin: 0;
  max-width: 38ch;
}

/* Blog index uses a featured + grid layout */
.pg-feature {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 48px;
  align-items: center;
  margin-bottom: 64px;
  padding-bottom: 56px;
  border-bottom: 1px solid var(--br-line);
}
.pg-feature__media {
  aspect-ratio: 4/3;
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 20px, #232323 20px 40px);
}
.pg-feature__meta {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-accent);
  margin: 0 0 12px;
}
.pg-feature__title {
  font-size: clamp(32px, 3.6vw, 48px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1.05;
  margin: 0 0 18px;
  text-wrap: balance;
}
.pg-feature__dek {
  font-size: 17px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0 0 24px;
  max-width: 48ch;
}
.pg-feature__cta {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 700;
}
@media (max-width: 900px) {
  .pg-feature { grid-template-columns: 1fr; gap: 24px; }
}

/* ============== ARTICLE HERO + BODY ============== */

.pg-article-hero {
  position: relative;
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 22px, #232323 22px 44px);
  color: #fff;
  min-height: 64vh;
  display: flex;
  align-items: flex-end;
}
.pg-article-hero__inner {
  position: relative;
  z-index: 2;
  max-width: 1440px;
  margin: 0 auto;
  padding: 80px 32px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.55) 100%);
  width: 100%;
}
.pg-article-hero__meta {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin: 0 0 16px;
  color: var(--br-accent);
}
.pg-article-hero__meta-sep { color: rgba(255,255,255,0.4); }
.pg-article-hero__meta-time { color: rgba(255,255,255,0.78); font-weight: 600; }

.pg-article-hero__title {
  font-size: clamp(40px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  max-width: 22ch;
  text-wrap: balance;
}
.pg-article-hero__dek {
  font-size: clamp(18px, 1.8vw, 22px);
  line-height: 1.45;
  color: rgba(255,255,255,0.88);
  margin: 24px 0 0;
  max-width: 52ch;
  text-wrap: pretty;
}
.pg-article-hero__byline {
  display: flex;
  gap: 24px;
  align-items: center;
  margin-top: 36px;
  font-size: 13px;
  letter-spacing: 0.04em;
  color: rgba(255,255,255,0.88);
}
.pg-article-hero__avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  border: 1px solid rgba(255,255,255,0.3);
}
.pg-article-hero__byline b { color: #fff; font-weight: 600; margin-right: 4px; }

@media (max-width: 700px) {
  .pg-article-hero__inner { padding: 48px 24px; }
}

/* Article body */
.pg-article-body {
  max-width: 720px;
  margin: 0 auto;
  padding: 80px 24px 96px;
  font-size: 18px;
  line-height: 1.7;
  color: var(--br-text);
}
.pg-article-body__lede {
  font-size: 22px;
  line-height: 1.55;
  color: var(--br-text);
  font-weight: 400;
  letter-spacing: -0.005em;
  margin: 0 0 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
}
.pg-article-body p {
  margin: 0 0 20px;
  text-wrap: pretty;
}
.pg-article-body h2 {
  font-size: clamp(24px, 2.4vw, 32px);
  font-weight: 500;
  letter-spacing: -0.005em;
  margin: 48px 0 14px;
  line-height: 1.2;
}
.pg-article-body h3 {
  font-size: 22px;
  font-weight: 500;
  margin: 36px 0 10px;
  line-height: 1.25;
}
.pg-article-body ul {
  margin: 0 0 24px;
  padding-left: 0;
  list-style: none;
}
.pg-article-body ul li {
  position: relative;
  padding-left: 22px;
  margin-bottom: 8px;
}
.pg-article-body ul li::before {
  content: "→";
  color: var(--br-accent);
  font-weight: 700;
  position: absolute;
  left: 0;
}
.pg-article-body blockquote {
  margin: 32px -16px;
  padding: 24px 32px;
  background: var(--br-alt-bg);
  border-left: 3px solid var(--br-accent);
  font-size: 22px;
  line-height: 1.4;
  font-weight: 400;
  letter-spacing: -0.005em;
}
.pg-article-body figure {
  margin: 40px -32px;
}
.pg-article-body figcaption {
  font-size: 13px;
  color: var(--br-text-mute);
  letter-spacing: 0.02em;
  margin-top: 12px;
  font-style: italic;
  text-align: center;
}
.pg-article-body__figure {
  aspect-ratio: 16/9;
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
}

/* ============== HOME — MULTI-PROMO TILES (alt to media-split) ============== */

.pg-promos {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 32px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
.pg-promo {
  position: relative;
  aspect-ratio: 4/3;
  background:
    repeating-linear-gradient(135deg, #efece2 0 16px, #e8e4d6 16px 32px);
  display: flex;
  align-items: flex-end;
  padding: 32px;
  text-decoration: none;
  color: var(--br-text);
  overflow: hidden;
}
.pg-promo--dark {
  background: repeating-linear-gradient(135deg, #2c2c2c 0 16px, #232323 16px 32px);
  color: #fff;
}
.pg-promo--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 16px, #efdcd2 16px 32px); }
.pg-promo__inner {
  position: relative;
  z-index: 2;
  background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.35) 100%);
  width: 100%;
  padding: 20px;
  margin: -32px;
  margin-top: 0;
  padding-top: 32px;
}
.pg-promo__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin: 0 0 8px;
  opacity: 0.78;
}
.pg-promo__title {
  font-size: clamp(24px, 2.4vw, 32px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.1;
  margin: 0 0 4px;
}
.pg-promo__more {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-top: 12px;
  display: inline-block;
  border-bottom: 1px solid currentColor;
  padding-bottom: 2px;
  font-weight: 700;
}
@media (max-width: 700px) {
  .pg-promos { grid-template-columns: 1fr; }
  .pg-promo { aspect-ratio: 16/10; }
}

/* ============== NEWSLETTER MID-PAGE BLOCK ============== */

.pg-newsletter {
  background: var(--br-text);
  color: #fff;
  padding: 80px 32px;
}
.pg-newsletter__inner {
  max-width: 880px;
  margin: 0 auto;
  text-align: center;
}
.pg-newsletter__inner h2 {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 400;
  margin: 0 0 12px;
  letter-spacing: -0.015em;
  line-height: 1.1;
}
.pg-newsletter__inner p {
  font-size: 16px;
  color: rgba(255,255,255,0.78);
  margin: 0 0 28px;
  line-height: 1.55;
}
.pg-newsletter__form {
  display: flex;
  max-width: 480px;
  margin: 0 auto;
  border: 1px solid rgba(255,255,255,0.3);
}
.pg-newsletter__form input {
  flex: 1;
  padding: 16px 18px;
  border: 0;
  background: transparent;
  color: #fff;
  font-family: inherit;
  font-size: 14px;
}
.pg-newsletter__form input::placeholder { color: rgba(255,255,255,0.5); }
.pg-newsletter__form button {
  background: var(--br-accent);
  color: #fff;
  border: 0;
  padding: 16px 24px;
  font-family: inherit;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

/* ============== PAGE NAV STRIP (cross-link between mocks) ============== */

.pg-tab-strip {
  background: var(--br-alt-bg);
  border-bottom: 1px solid var(--br-line);
}
.pg-tab-strip__inner {
  max-width: 1440px;
  margin: 0 auto;
  padding: 10px 32px;
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  align-items: center;
}
.pg-tab-strip__label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-text-mute);
  margin-right: 10px;
}
.pg-tab-strip a {
  display: inline-block;
  padding: 6px 14px;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  text-decoration: none;
  border: 1px solid transparent;
  border-radius: 0;
}
.pg-tab-strip a:hover { color: var(--br-text); border-color: var(--br-line); background: #fff; }
.pg-tab-strip a[aria-current="page"] {
  background: var(--br-text);
  color: #fff;
  border-color: var(--br-text);
}

/* ============== COLLECTION VARIANT GRID (full, expanded) ============== */

.pg-coll-variants {
  max-width: 1440px;
  margin: 0 auto;
  padding: 56px 32px 96px;
}
.pg-coll-variants__head {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 24px;
  margin-bottom: 28px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
  flex-wrap: wrap;
}
.pg-coll-variants__count {
  font-size: 13px;
  color: var(--br-text-soft);
  letter-spacing: 0.04em;
}
.pg-coll-variants__count b { color: var(--br-text); font-weight: 600; }
.pg-coll-variants__sort {
  display: flex;
  gap: 16px;
  align-items: center;
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pg-coll-variants__sort select {
  font-family: inherit;
  font-size: 13px;
  padding: 8px 12px;
  border: 1px solid var(--br-text);
  background: #fff;
  text-transform: none;
  letter-spacing: 0;
}

.pg-coll-variants__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px 24px;
}
@media (max-width: 1000px) { .pg-coll-variants__grid { grid-template-columns: repeat(2, 1fr); } }


/* ============================================================
   BELIEF BANDS · oversized type, no image (editorial pause)
   ============================================================ */
.pg-belief {
  background: #fff;
  padding: 80px 32px;
  text-align: center;
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
}
.pg-belief--dark {
  background: var(--br-text);
  color: #fff;
  border-color: var(--br-text);
}
.pg-belief__inner { max-width: 1200px; margin: 0 auto; }
.pg-belief__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 18px;
  opacity: 0.75;
}
.pg-belief__line {
  font-size: clamp(36px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-belief__hashtag {
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--br-accent);
  font-weight: 700;
  margin: 22px 0 0;
}

/* ============================================================
   FULL-BLEED LIFESTYLE BAND (Join the Movement)
   ============================================================ */
.pg-fullbleed {
  position: relative;
  min-height: 580px;
  overflow: hidden;
  background: #1a1a1a;
  display: flex;
  align-items: center;
}
.pg-fullbleed__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-fullbleed__overlay {
  position: relative;
  z-index: 2;
  padding: 80px 64px;
  max-width: 720px;
  color: #fff;
}
.pg-fullbleed__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 16px;
  opacity: 0.9;
}
.pg-fullbleed__title {
  font-size: clamp(40px, 5.4vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-fullbleed__body {
  font-size: 18px;
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.92;
  max-width: 46ch;
}
.pg-fullbleed__cta {
  display: inline-block;
  margin-top: 28px;
  background: #fff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
@media (max-width: 700px) {
  .pg-fullbleed__overlay { padding: 48px 24px; }
}


/* ============================================================
   v11 ADDITIONS — new sections not in base CSS
   ============================================================ */

/* HERO */
.pg-hero-image { position: relative; width: 100%; min-height: 85vh; display: flex; align-items: flex-end; overflow: hidden; }
.pg-hero-image__media { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 30%; }
.pg-hero-image__overlay { position: relative; z-index: 2; width: 100%; padding: 80px 64px; background: linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.2) 60%, transparent 100%); }
.pg-hero-image__eyebrow { font-size: 12px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.72); margin: 0 0 16px; transition: opacity 0.3s ease; }
.pg-hero-image__title { font-size: clamp(40px, 5.5vw, 72px); font-weight: 400; letter-spacing: -0.025em; line-height: 1.02; color: #fff; margin: 0; max-width: 18ch; text-wrap: balance; }
.pg-hero-image__body { font-size: 18px; line-height: 1.55; color: rgba(255,255,255,0.82); margin: 20px 0 0; max-width: 52ch; }
.pg-hero-image__ctas { display: flex; gap: 14px; margin-top: 36px; flex-wrap: wrap; }
.pg-hero-image__cta { display: inline-flex; align-items: center; padding: 16px 36px; font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; background: #fff; color: #050505; }
.pg-hero-image__cta--ghost { background: transparent; color: #fff; border: 1.5px solid rgba(255,255,255,0.6); }
.pg-hero-image__cta--ghost:hover { background: rgba(255,255,255,0.1); }

/* MEDIA SPLIT 50/50 */
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CANONICAL 50/50 SPLIT SIZE — DO NOT CHANGE
   Approved: v18 "Never slip in chair pose" section
   height: 420px FIXED | overflow: hidden | padding: 56px 64px
   Fixed height = all splits locked at same size regardless of content
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.v11-split { display: grid; grid-template-columns: 1fr 1fr; min-height: 420px; border-top: 1px solid var(--br-line); border-bottom: 1px solid var(--br-line); }
.v11-split__media { position: relative; overflow: hidden; background: #111; }
.v11-split__media img, .v11-split__media video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
.v11-split__copy { background: #f9f7f2; display: flex; flex-direction: column; justify-content: center; padding: 80px 72px; }
.v11-split__stars { font-size: 18px; color: var(--br-star); letter-spacing: 2px; margin-bottom: 6px; }
.v11-split__trusted { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--br-text-soft); margin-bottom: 16px; }
.v11-split__slogan { font-size: clamp(38px, 4.6vw, 66px); font-weight: 300; letter-spacing: -0.03em; line-height: 1.0; color: var(--br-text); margin-bottom: 28px; min-height: 0; max-width: 15ch; text-wrap: balance; transition: opacity 0.4s ease; }
.v11-split__slogan strong { font-weight: 600; }
.v11-split__cta { display: inline-flex; align-items: center; gap: 8px; padding: 16px 32px; background: var(--br-button); color: var(--br-button-text); font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; align-self: flex-start; }

/* SOCK COMPARISON */
.v11-compare { padding: 80px 64px; background: var(--br-bg); }
.v11-compare__inner { max-width: 1200px; margin: 0 auto; }
.v11-compare__head { text-align: center; margin-bottom: 64px; }
.v11-compare__eyebrow { font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--br-accent); margin: 0 0 14px; }
.v11-compare__title { font-size: clamp(28px, 3.5vw, 48px); font-weight: 400; letter-spacing: -0.02em; margin: 0; }
.v11-compare__sub { font-size: 17px; color: var(--br-text-soft); margin: 16px auto 0; max-width: 56ch; }
.v11-compare__grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; background: var(--br-line); }
.v11-compare__col { background: var(--br-bg); padding: 48px; }
.v11-compare__col--them { background: var(--br-alt-bg); }
.v11-compare__col-head { font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 32px; padding-bottom: 16px; border-bottom: 2px solid var(--br-line); }
.v11-compare__col-head--us { border-bottom-color: var(--br-text); }
.v11-compare__row { display: flex; justify-content: space-between; align-items: baseline; padding: 14px 0; border-bottom: 1px solid var(--br-line-soft); font-size: 15px; }
.v11-compare__row:last-child { border-bottom: none; }
.v11-compare__row-label { color: var(--br-text-soft); }
.v11-compare__row-val { font-weight: 600; }
.v11-compare__row-val--bad { color: #c43d2a; }
.v11-compare__row-val--good { color: #1f6f4a; }
.v11-compare__math { margin-top: 48px; padding: 32px; background: var(--br-text); color: #fff; text-align: center; }
.v11-compare__math-line { font-size: 15px; line-height: 1.7; opacity: 0.82; }
.v11-compare__math-big { font-size: clamp(22px, 2.5vw, 32px); font-weight: 500; letter-spacing: -0.01em; margin-top: 12px; opacity: 1; }

/* 3 DISCIPLINES */
.v11-disciplines { background: var(--br-alt-bg); padding: 96px 64px; }
.v11-disciplines__inner { max-width: 1280px; margin: 0 auto; }
.v11-disciplines__head { text-align: center; margin-bottom: 64px; }
.v11-disciplines__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; }
.v11-disc { position: relative; overflow: hidden; min-height: 520px; }
.v11-disc__img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s ease; }
.v11-disc:hover .v11-disc__img { transform: scale(1.03); }
.v11-disc__overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.1) 55%, transparent 100%); display: flex; flex-direction: column; justify-content: flex-end; padding: 40px 36px; }
.v11-disc__eyebrow { font-size: 11px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.7); } .v11-disc__eyebrow--UNUSED { color: var(--br-accent); margin-bottom: 10px; }
.v11-disc__title { font-size: clamp(22px, 2.2vw, 30px); font-weight: 400; color: #fff; line-height: 1.15; margin: 0 0 12px; letter-spacing: -0.01em; }
.v11-disc__body { font-size: 14px; line-height: 1.55; color: rgba(255,255,255,0.78); margin: 0; }

/* VIDEO SECTION */
.v11-videos { padding: 80px 64px; background: var(--br-bg); }
.v11-videos__inner { max-width: 1280px; margin: 0 auto; }
.v11-videos__head { text-align: center; margin-bottom: 64px; }
.v11-videos__layout { display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; align-items: start; }
.v11-video-large { position: relative; }
.v11-video-large video { width: 100%; display: block; aspect-ratio: 16/10; object-fit: cover; background: #111; }
.v11-video-large__cap { padding: 20px 0 0; }
.v11-video-large__title { font-size: 17px; font-weight: 500; margin: 0 0 6px; }
.v11-video-large__sub { font-size: 14px; color: var(--br-text-soft); margin: 0; }
.v11-videos-small { display: flex; flex-direction: column; gap: 16px; }
.v11-video-small { display: grid; grid-template-columns: auto 1fr; gap: 16px; align-items: start; }
.v11-video-small video { width: 160px; aspect-ratio: 4/3; object-fit: cover; background: #111; display: block; }
.v11-video-small__cap { padding-top: 4px; }
.v11-video-small__title { font-size: 15px; font-weight: 500; margin: 0 0 4px; }
.v11-video-small__sub { font-size: 13px; color: var(--br-text-soft); margin: 0; line-height: 1.5; }

/* REVIEWS UPGRADED */
.v11-reviews { padding: 80px 64px; background: var(--br-alt-bg); }
.v11-reviews__inner { max-width: 1280px; margin: 0 auto; }
.v11-reviews__head { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 56px; }
.v11-reviews__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; }
.v11-review { background: var(--br-bg); padding: 40px; }
.v11-review__stars { font-size: 16px; color: var(--br-star); letter-spacing: 1px; margin-bottom: 16px; }
.v11-review__title { font-size: 17px; font-weight: 500; margin: 0 0 12px; }
.v11-review__body { font-size: 15px; line-height: 1.65; color: var(--br-text-soft); margin: 0 0 20px; }
.v11-review__attr { font-size: 12px; color: var(--br-text-mute); font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; }
.v11-review__badge { display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; padding: 2px 8px; background: var(--br-le-bg); color: var(--br-le); margin-bottom: 12px; }

/* GUARANTEE */
.v11-guarantee { padding: 72px 64px; background: var(--br-text); color: #fff; }
.v11-guarantee__inner { max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1px 1fr 1px 1fr; gap: 48px; }
.v11-guarantee__eyebrow { font-size: 11px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 12px; }
.v11-guarantee__title { font-size: 22px; font-weight: 400; letter-spacing: -0.01em; margin: 0 0 14px; }
.v11-guarantee__body { font-size: 14px; line-height: 1.65; color: rgba(255,255,255,0.72); margin: 0; }
.v11-guarantee__divider { width: 1px; background: rgba(255,255,255,0.12); }
.v11-guarantee__head { max-width: 1000px; margin: 0 auto 40px; text-align: center; }
.v11-guarantee__main-title { font-size: clamp(28px, 3vw, 44px); font-weight: 400; letter-spacing: -0.02em; color: #fff; margin: 0 0 16px; }
.v11-guarantee__main-sub { font-size: 16px; color: rgba(255,255,255,0.65); line-height: 1.6; max-width: 54ch; margin: 0 auto; }

/* BELIEF BAND */
.v11-belief { padding: 64px; background: var(--br-bg); border-top: 1px solid var(--br-line); border-bottom: 1px solid var(--br-line); text-align: center; }
.v11-belief__line { font-size: clamp(36px, 5vw, 72px); font-weight: 400; letter-spacing: -0.01em; color: var(--br-text); margin: 0; }
.v11-belief--dark { background: var(--br-text); }
.v11-belief--dark .v11-belief__line { color: #fff; }

/* NEWSLETTER */
.v11-newsletter { padding: 96px 64px; background: var(--br-alt-bg-2); text-align: center; }
.v11-newsletter h2 { font-size: clamp(24px, 2.8vw, 40px); font-weight: 400; letter-spacing: -0.02em; margin: 0 0 14px; }
.v11-newsletter p { font-size: 16px; color: var(--br-text-soft); max-width: 48ch; margin: 0 auto 32px; }
.v11-newsletter__form { display: flex; gap: 0; max-width: 480px; margin: 0 auto; }
.v11-newsletter__form input { flex: 1; padding: 16px 20px; font-size: 15px; border: 1px solid var(--br-line); background: #fff; outline: none; }
.v11-newsletter__form button { padding: 16px 28px; background: var(--br-button); color: var(--br-button-text); font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; border: none; cursor: pointer; }

/* COLLAB HERO */
.v11-collab { position: relative; min-height: 600px; display: flex; align-items: center; overflow: hidden; }
.v11-collab__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.v11-collab__video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.v11-collab__overlay { position: relative; z-index: 2; padding: 80px 80px; background: linear-gradient(to right, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.2) 65%, transparent 100%); width: 100%; }
.v11-collab__le { font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(255,255,255,0.6); margin-bottom: 16px; display: block; }
.v11-collab__title { font-size: clamp(32px, 4vw, 56px); font-weight: 400; letter-spacing: -0.02em; color: #fff; margin: 0 0 20px; max-width: 14ch; }
.v11-collab__sub { font-size: 16px; line-height: 1.6; color: rgba(255,255,255,0.78); max-width: 44ch; margin: 0 0 36px; }
.v11-collab__cta { display: inline-flex; align-items: center; padding: 16px 36px; background: #fff; color: #050505; font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; }

/* JOURNAL */
.v11-journal { padding: 80px 64px; background: var(--br-bg); }
.v11-journal__inner { max-width: 1280px; margin: 0 auto; }
.v11-journal__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 56px; }
.v11-article { text-decoration: none; color: inherit; display: block; }
.v11-article__img { width: 100%; aspect-ratio: 3/2; object-fit: cover; display: block; background: var(--br-alt-bg); margin-bottom: 20px; }
.v11-article__meta { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--br-accent); margin-bottom: 10px; }
.v11-article__title { font-size: 19px; font-weight: 500; line-height: 1.3; margin: 0 0 10px; letter-spacing: -0.01em; }
.v11-article__dek { font-size: 14px; line-height: 1.6; color: var(--br-text-soft); margin: 0; }
.v11-article:hover .v11-article__title { text-decoration: underline; }

/* SECTION HEADER SHARED */
.v11-section-head { text-align: center; }
.v11-eyebrow { font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--br-accent); margin: 0 0 14px; }
.v11-h2 { font-size: clamp(28px, 3.2vw, 44px); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin: 0; }
.v11-lede { font-size: 17px; line-height: 1.6; color: var(--br-text-soft); max-width: 56ch; margin: 16px auto 0; }

@media (max-width: 900px) {
  .v11-split, .v11-compare__grid, .v11-disciplines__grid, .v11-reviews__grid, .v11-journal__grid, .v11-guarantee__inner { grid-template-columns: 1fr; }
  .v11-videos__layout { grid-template-columns: 1fr; }
  .v11-video-small { grid-template-columns: 1fr; }
  .v11-video-small video { width: 100%; }
  .v11-compare { padding: 64px 24px; }
  .v11-disciplines { padding: 64px 24px; }
  .v11-reviews { padding: 64px 24px; }
  .v11-guarantee { padding: 64px 24px; }
  .v11-videos { padding: 64px 24px; }
  .v11-journal { padding: 64px 24px; }
  .pg-hero-image__overlay { padding: 48px 24px; }
  .v11-split__copy { padding: 56px 36px; }
}

/* ============================================================
   MOBILE FIRST — v13
   ============================================================ */
@media (max-width: 768px) {

  /* Header */
  .pdp-header__nav { display: none; }
  .pdp-header__inner { padding: 0 20px; }

  /* Hero */
  .pg-hero-image { min-height: 75vh; }
  .pg-hero-image__overlay { padding: 32px 24px 48px; }
  .pg-hero-image__title { font-size: clamp(30px, 9vw, 48px); max-width: 100%; }
  .pg-hero-image__body { font-size: 16px; margin-top: 14px; }
  .pg-hero-image__ctas { flex-direction: column; gap: 10px; margin-top: 28px; }
  .pg-hero-image__cta { width: 100%; justify-content: center; min-height: 52px; font-size: 14px; }

  /* Pillar strip */
  .pdp-pillars__pts { flex-direction: column; gap: 8px; text-align: center; }
  .pdp-pillars__div { display: none; }

  /* 50/50 splits */

  /* Tighter splits on mobile */
  .v11-split { height: auto !important; overflow: visible !important; }
  .v11-split__media { min-height: 260px !important; }
  .v11-split__copy { padding: 36px 24px !important; }
  .v11-split__slogan { font-size: clamp(20px, 5.5vw, 28px) !important; }
  .v11-split__cta { width: 100%; justify-content: center; }

  .v11-split { grid-template-columns: 1fr; height: auto !important; }
  .v11-split__media { min-height: 280px; order: 0 !important; }
  .v11-split__copy { padding: 40px 24px; order: 1 !important; }
  .v11-split__slogan { font-size: clamp(20px, 6vw, 28px); min-height: auto; }

  /* Price strip */
  .v11-price-strip { padding: 36px 24px; }
  .v11-price-strip p:first-child { font-size: 20px; }

  /* Product grid */
  .pdp-variants__grid { grid-template-columns: 1fr 1fr; gap: 16px; }
  .pdp-variants__head { flex-direction: column; gap: 16px; }

  /* Disciplines */
  .v11-disciplines { padding: 48px 24px; }
  .v11-disciplines__grid { grid-template-columns: 1fr; }
  .v11-disc { min-height: 360px; }

  /* Videos */
  .v11-videos { padding: 48px 24px; }
  .v11-videos__layout { grid-template-columns: 1fr; }
  .v11-video-small { grid-template-columns: 1fr; }
  .v11-video-small video, .v11-video-small img { width: 100%; aspect-ratio: 16/9; }

  /* Reviews */
  .v11-reviews { padding: 48px 24px; }
  .v11-reviews__grid { grid-template-columns: 1fr; }
  .v11-reviews__head { flex-direction: column; gap: 16px; }

  /* Collab */
  .v11-collab__overlay { padding: 40px 24px; }
  .v11-collab__title { font-size: clamp(26px, 7vw, 40px); }

  /* Journal */
  .v11-journal { padding: 48px 24px; }
  .pg-editorial-grid { grid-template-columns: 1fr; gap: 32px; }

  /* Guarantee */
  .v11-guarantee { padding: 48px 24px; }
  .v11-guarantee__inner { grid-template-columns: 1fr; gap: 32px; }
  .v11-guarantee__divider { display: none; }
  .v11-guarantee__main-title { font-size: clamp(26px, 7vw, 40px); }

  /* Belief bands */
  .v11-belief { padding: 48px 24px; }
  .v11-belief__line { font-size: clamp(26px, 7vw, 44px); }

  /* Newsletter */
  .v11-newsletter { padding: 56px 24px; }
  .v11-newsletter__form { flex-direction: column; }
  .v11-newsletter__form input, .v11-newsletter__form button { width: 100%; min-height: 52px; }

  /* Footer */
  .pdp-footer__grid { grid-template-columns: 1fr; gap: 32px; }
  .pdp-footer__bottom { flex-direction: column; gap: 12px; text-align: center; }

  /* FAQ */
  .pdp-faq__list { padding: 0 !important; }

  /* General sections */
  .pdp-section { padding: 56px 24px; }
  .v11-compare { padding: 48px 24px; }
  .v11-compare__grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {



  /* Value v20 mobile */
  section[style*="background:#f5f2ec;padding:52px"] > div > div {
    grid-template-columns: 1fr !important;
  }
  section[style*="background:#f5f2ec;padding:52px"] > div > div > div[style*="background:#ddd8d0;margin:0 28px"] {
    display: none !important;
  }
  section[style*="background:#f5f2ec;padding:52px"] > div > div > div {
    padding: 20px 0 !important;
    border-bottom: 1px solid #ddd8d0;
  }
  section[style*="background:#f5f2ec;padding:52px"] { padding: 40px 24px !important; }

  /* Value section condensed — mobile */
  section[style*="background:#f5f2ec;padding:56px"] > div {
    grid-template-columns: 1fr !important;
  }
  section[style*="background:#f5f2ec;padding:56px"] > div > div[style*="background:#ddd8d0"] {
    display: none !important;
  }
  section[style*="background:#f5f2ec;padding:56px"] > div > div:not([style*="background"]) {
    padding: 24px 0 !important;
    border-bottom: 1px solid #ddd8d0;
  }
  section[style*="background:#f5f2ec;padding:56px"] { padding: 40px 24px !important; }


  /* Collab split — mobile stack */
  section[style*="grid-template-columns:1fr 1fr;min-height:560px"] {
    grid-template-columns: 1fr !important;
  }
  section[style*="grid-template-columns:1fr 1fr;min-height:560px"] > div:first-child {
    min-height: 280px;
  }
}
@media (max-width: 480px) {
  .pg-hero-image__title { font-size: clamp(28px, 8vw, 38px); }
  .v11-h2 { font-size: clamp(24px, 7vw, 32px); }
  .pdp-h2 { font-size: clamp(22px, 7vw, 30px); }
  .pdp-variants__grid { grid-template-columns: 1fr; }
}


/* Alternate light value section */
.pdp-value--light {
  background: #f5f3ee;
}
.pdp-value--light .pdp-value__col {
  background: #fff;
}
.pdp-value--light .pdp-value__col--ours {
  background: var(--br-text);
}
.pdp-value--light .pdp-value__copy .pdp-eyebrow { color: var(--br-accent); }
.pdp-value--light .pdp-value__copy .pdp-h2 { color: var(--br-text); }
.pdp-value--light .pdp-value__copy .pdp-lede { color: var(--br-text-soft); }
.pdp-value--light .pdp-value__compare { background: var(--br-line); }
.pdp-value--light .pdp-value__col .pdp-value__tag { color: var(--br-text-soft); }
.pdp-value--light .pdp-value__col .pdp-value__amount { color: var(--br-text); }
.pdp-value--light .pdp-value__col .pdp-value__list { color: var(--br-text-soft); }
.pdp-value--light blockquote { background: rgba(0,0,0,0.04); border-left-color: var(--br-accent); }
.pdp-value--light blockquote p { color: var(--br-text); }
.pdp-value--light blockquote cite { color: var(--br-text-mute); }
.pdp-value--light a[style] { background: var(--br-text) !important; color: #fff !important; }

</style>

<style>
/* ============================================================
   MATURED DIRECTION — warm palette override
   Applied on top of v10 base. Toggle via Tweaks panel.
   ============================================================ */
[data-matured="on"] {
  --br-bg: #f1ede4;
  --br-alt-bg: #faf8f3;
  --br-alt-bg-2: #f0ece3;
  --br-text: #1c1916;
  --br-text-soft: #6b645a;
  --br-text-mute: #9a9182;
  --br-line: #e2dccf;
  --br-line-soft: #ede8dd;
  --br-accent: #c45c3f;
  --br-accent-hover: #a84d35;
  --br-coral: #c45c3f;
  --br-button: #1c1916;
  --br-button-text: #ffffff;
  --au-bg: #eae5da;
}

[data-matured="on"] .pdp-ticker {
  background: #24201b;
}
[data-matured="on"] .pdp-header {
  background: rgba(241,237,228,0.96);
  border-bottom-color: #e2dccf;
}
[data-matured="on"] .pdp-footer {
  background: #24201b;
}
[data-matured="on"] .v11-guarantee {
  background: #24201b;
}
[data-matured="on"] .sm {
  background: #24201b;
}
[data-matured="on"] .v11-newsletter {
  background: #24201b;
}
[data-matured="on"] .m-manifesto {
  background: #24201b;
}
[data-matured="on"] .v11-disciplines {
  background: #24201b;
}

/* Ground toggle */
[data-ground="white"][data-matured="on"] {
  --br-bg: #ffffff;
  --br-alt-bg: #ffffff;
  --br-alt-bg-2: #f9f9f9;
  --au-bg: #ffffff;
}
[data-ground="white"][data-matured="on"] .pdp-header {
  background: rgba(255,255,255,0.96);
}

/* Eyebrow toggle — soft */
[data-eyebrow="soft"][data-matured="on"] .v11-eyebrow,
[data-eyebrow="soft"][data-matured="on"] .pdp-eyebrow,
[data-eyebrow="soft"][data-matured="on"] .sm__eyebrow,
[data-eyebrow="soft"][data-matured="on"] .v11-rev2__eyebrow {
  font-weight: 500;
  letter-spacing: 0.02em;
  text-transform: none;
  color: var(--br-text-soft);
}

/* Matured-only sections */
.matured-section { display: none; }
[data-matured="on"] .matured-section { display: block; }
</style>
</head>
<body data-matured="on" data-ground="warm" data-eyebrow="soft" data-density="editorial">

<!-- SCHEMA MARKUP for GEO/SEO -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Barreletics Performance Skin — Grippy Shoe for Barre, Pilates & Yoga",
  "description": "The premium grip shoe for barre, reformer Pilates, Lagree, Megaformer, and yoga. Replaces grip socks. 360-degree grip, no latex, no silicone. Made in USA.",
  "brand": { "@type": "Brand", "name": "Barreletics" },
  "offers": { "@type": "Offer", "price": "74.00", "priceCurrency": "USD", "availability": "https://schema.org/InStock" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "294" }
}
</script>

<!-- TICKER -->
<div class="pdp-ticker" aria-live="polite">
  <span class="pdp-ticker__slide">Buy 2 Save 15% · use code <b>SAVE15</b></span>
  <span class="pdp-ticker__slide is-active">🇺🇸 Made in USA · Free shipping over $150 · 30-day returns &nbsp;<a href="#">details →</a></span>
  <span class="pdp-ticker__slide">★ Trusted by 1,000’s of instructors · studios · athletes</span>
</div>

<!-- HEADER -->
<header class="pdp-header">
  <div class="pdp-header__inner">
    <nav class="pdp-header__nav">
      <a href="Barreletics Collection.html">Grippy Footwear <span class="pdp-header__chev">⌄</span></a>
      <a href="#">Apparel <span class="pdp-header__chev">⌄</span></a>
      <a href="#">Collaborations <span class="pdp-header__chev">⌄</span></a>
      <a href="Barreletics Blog.html">Journal</a>
      <a href="#">About Us <span class="pdp-header__chev">⌄</span></a>
    </nav>
    <a href="#" class="pdp-header__logo" aria-label="Barreletics home">
      <img src="barreletics-logo.png" alt="Barreletics">
    </a>
    <div class="pdp-header__util">
      <a href="#">Account</a>
      <a href="#" class="pdp-header__cart">Cart <span class="pdp-header__cart-dot"></span></a>
    </div>
  </div>
</header>

<!-- HERO -->
<section class="pg-hero-image" aria-label="Secure in every hold">
  <img class="pg-hero-image__media" src="https://barreletics.com/cdn/shop/files/IMG_2917.jpg" alt="Barreletics performance skin on foot — secure grip for barre and Pilates">
  <div class="pg-hero-image__overlay">
    <div style="max-width: 1280px; margin: 0 auto; width: 100%;">
      <p class="pg-hero-image__eyebrow" id="hero-eyebrow" style="opacity: 1;">The Pilates sock era is over.</p>
      <h1 class="pg-hero-image__title">Secure in every hold.<br>No sliding. No resets.</h1>
      <p class="pg-hero-image__body">The performance skin engineered for barre, reformer Pilates, Lagree and Megaformer. 360° grip. No latex, no silicone. Trusted by 1,000’s of instructors.</p>
      <div class="pg-hero-image__ctas">
        <a href="Barreletics Collection.html" class="pg-hero-image__cta">Shop the collection</a>
        <a href="#how-it-works" class="pg-hero-image__cta pg-hero-image__cta--ghost">See it in action ↓</a>
      </div>
    </div>
  </div>
</section>

<!-- PILLAR STRIP -->
<section class="pdp-pillars" aria-label="Why it works">
  <div class="pdp-pillars__inner">
    <span class="pdp-pillars__label">#letusknockyoursocksoff</span>
    <div class="pdp-pillars__pts">
      <span>360° Grip</span><span class="pdp-pillars__div"></span>
      <span>Two Surfaces. Zero Slip.</span><span class="pdp-pillars__div"></span>
      <span>No Mid-Class Adjustments</span><span class="pdp-pillars__div"></span>
      <span>Rinse &amp; Reuse</span><span class="pdp-pillars__div"></span>
      <span>No Latex / No Silicone</span><span class="pdp-pillars__div"></span>
      <span>Made in USA</span>
    </div>
  </div>
</section>

<!-- MEDIA SPLIT 50/50 — rotating slogans -->
<section class="v11-split">
  <div class="v11-split__media">
    <img src="https://barreletics.com/cdn/shop/files/Multi_Image.jpg" alt="Barreletics performance skin — grip from heel to toe">
  </div>
  <div class="v11-split__copy">
    <div class="v11-split__stars">★★★★★</div>
    <p class="v11-split__trusted">Trusted by 1,000’s of instructors &amp; studios</p>
    <h2 class="v11-split__slogan">Never slip in<br><strong>chair pose.</strong></h2>
    <p style="font-size:16px;line-height:1.6;color:var(--br-text-soft);margin:0 0 20px;max-width:38ch">Or side plank. Or reformer bridges. Any held position where your sock has been quietly failing you.</p>
    <a href="Barreletics Collection.html" class="v11-split__cta">Shop the collection →</a>
  </div>
</section>

<!-- PRODUCT GRID -->
<section class="pdp-section" id="shop">
  <header class="pdp-variants__head">
    <div class="pdp-variants__head-meta">
      <p class="pdp-eyebrow" style="color:var(--br-accent);margin:0">The studio collection</p>
      <h2 class="pdp-h2">Shop all colors &amp; styles.</h2>
      <p class="pdp-lede" style="margin-top:12px">Closed sole for barre &amp; reformer. Open sole for yoga &amp; mat Pilates. Same 360° grip — two builds, your call.</p>
    </div>
    <a href="Barreletics Collection.html" class="pdp-variants__head-link">See all 24 styles →</a>
  </header>
  <div class="pdp-variants__tabs" role="tablist">
    <button class="pdp-variant-tab" aria-selected="true">Closed sole</button>
    <button class="pdp-variant-tab">Open sole</button>
  </div>
  <div class="pdp-variants__grid">
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg" alt="Closed Sole Black" style="width:100%;height:100%;object-fit:cover;display:block"><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Closed Sole · Black</h3>
      <span class="pdp-vcard__meta">★★★★★ 24 verified reviews</span>
      <span class="pdp-vcard__price">$74</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png" alt="Closed Sole Dusty Rose" style="width:100%;height:100%;object-fit:cover;display:block"><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Closed Sole · Dusty Rose</h3>
      <span class="pdp-vcard__meta">18 verified reviews</span>
      <span class="pdp-vcard__price">$74</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg" alt="Closed Sole Light Grey" style="width:100%;height:100%;object-fit:cover;display:block"><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Closed Sole · Light Grey</h3>
      <span class="pdp-vcard__meta">14 verified reviews</span>
      <span class="pdp-vcard__price">$74</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png" alt="Coperni x Barreletics Limited Edition" style="width:100%;height:100%;object-fit:cover;display:block"><span class="pdp-vcard__le">Limited Edition</span><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Coperni × Closed</h3>
      <span class="pdp-vcard__meta">Limited drop · one run</span>
      <span class="pdp-vcard__price">$115</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
  </div>
  <div style="text-align:center;margin-top:48px;padding-top:32px;border-top:1px solid var(--br-line)">
    <a href="Barreletics Collection.html" class="pg-hero-split__cta">View all 12 colors &amp; styles</a>
    <p style="font-size:12px;color:var(--br-text-mute);letter-spacing:0.06em;margin:14px 0 0">Closed Sole · Open Sole · 6 colors each · M / L sizing</p>
  </div>
</section>

<!-- PROMO TILES — 2-box feature -->
<section style="padding:0 64px 64px;background:#fff">
  <div class="pg-promos">
    <!-- Tile 1: Limited edition color -->
    <a href="Barreletics Collection.html" class="pg-promo" style="background:#f5f0eb">
      <img style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center" src="https://barreletics.com/cdn/shop/files/Yellow.jpg" alt="Limited edition color — Rivian Green">
      <div class="pg-promo__inner">
        <p class="pg-promo__eyebrow" style="color:rgba(255,255,255,0.75)">Limited edition</p>
        <h3 class="pg-promo__title" style="color:#fff">New color.<br>Rivian Green.</h3>
        <span class="pg-promo__more" style="color:#fff">Shop now →</span>
      </div>
    </a>
    <!-- Tile 2: Yoga pants / apparel -->
    <a href="#" class="pg-promo pg-promo--dark">
      <img style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top" src="https://barreletics.com/cdn/shop/files/barrletixx_blue_pants_FINAL_d820a140-d75f-49bb-9035-77fc4dde3551.jpg" alt="Barreletics performance apparel">
      <div class="pg-promo__inner">
        <p class="pg-promo__eyebrow" style="color:rgba(255,255,255,0.65)">Now in studio</p>
        <h3 class="pg-promo__title" style="color:#fff">Performance<br>apparel.</h3>
        <span class="pg-promo__more" style="color:#fff">Shop leggings →</span>
      </div>
    </a>
  </div>
</section>

<!-- SOCK MATH -->
<style>
.sm{background:#141414;color:#fff;padding:clamp(56px,7vw,104px) clamp(24px,5vw,64px)}
.sm__inner{max-width:1280px;margin:0 auto}
.sm__head{display:flex;justify-content:space-between;align-items:flex-end;gap:28px;flex-wrap:wrap;margin-bottom:8px}
.sm__eyebrow{font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.7);margin:0 0 18px}
.sm__title{font-size:clamp(34px,4.6vw,60px);font-weight:300;letter-spacing:-0.025em;line-height:1.02;margin:0;max-width:18ch}
.sm__title strong{font-weight:600}
.sm__sub{font-size:17px;line-height:1.6;color:rgba(255,255,255,0.72);margin:20px 0 0;max-width:60ch}
.sm__toggle{display:inline-flex;border:1px solid rgba(255,255,255,0.25);flex-shrink:0}
.sm__toggle button{font-family:inherit;font-size:11.5px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:12px 22px;background:transparent;color:rgba(255,255,255,0.6);border:0;cursor:pointer;transition:.15s}
.sm__toggle button.is-on{background:#fff;color:#141414}
.sm-variant{display:none}
.sm[data-sm="a"] .sm-a{display:block}
.sm[data-sm="b"] .sm-b{display:block}
/* Design A — comparison */
.sm__cards{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.12);margin:44px 0 0}
.sm__card{background:#141414;padding:34px 32px;display:flex;flex-direction:column}
.sm__card--ours{background:#1d1d1d}
.sm__label{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin:0}
.sm__label--ours,.sm__card--ours .sm__label{color:var(--br-accent)}
.sm__price{font-size:clamp(40px,5vw,64px);font-weight:300;letter-spacing:-0.03em;line-height:1;margin:14px 0 4px}
.sm__price s{color:rgba(255,255,255,0.4);text-decoration-thickness:2px}
.sm__meta{font-size:12.5px;color:rgba(255,255,255,0.55);letter-spacing:0.03em;margin:0 0 22px}
.sm__rows{list-style:none;margin:0;padding:18px 0 0;border-top:1px solid rgba(255,255,255,0.12);display:flex;flex-direction:column;gap:13px}
.sm__row{display:flex;justify-content:space-between;align-items:baseline;gap:16px;font-size:13.5px}
.sm__row-k{color:rgba(255,255,255,0.6)}
.sm__row-v{color:rgba(255,255,255,0.85);font-weight:500;text-align:right}
.sm__card--ours .sm__row-v{color:#fff;font-weight:600}
/* slogan nest (replaces numbered grid) */
.sm__slogans{display:grid;grid-template-columns:1fr 1fr;gap:0 56px;margin:0 0 44px;border-top:1px solid rgba(255,255,255,0.14)}
.sm__slogans p{font-size:clamp(21px,2.1vw,30px);font-weight:300;letter-spacing:-0.018em;line-height:1.12;color:rgba(255,255,255,0.5);margin:0;padding:24px 0;border-bottom:1px solid rgba(255,255,255,0.1)}
.sm__slogans strong{font-weight:600;color:#fff}
.sm__slogans em{font-style:normal;font-weight:600;color:var(--br-accent)}
/* Design B — statement */
.sm-b__row{display:flex;align-items:center;justify-content:center;gap:clamp(24px,5vw,80px);margin:48px 0 0;flex-wrap:wrap}
.sm-b__col{text-align:center}
.sm-b__big{font-size:clamp(60px,9vw,132px);font-weight:200;letter-spacing:-0.045em;line-height:0.85}
.sm-b__big s{color:rgba(255,255,255,0.3);text-decoration-thickness:3px}
.sm-b__big--ours{color:var(--br-accent)}
.sm-b__cap{font-size:13px;color:rgba(255,255,255,0.6);margin:16px auto 0;letter-spacing:0.02em;max-width:24ch}
.sm-b__arrow{font-size:clamp(34px,4vw,60px);color:rgba(255,255,255,0.28);font-weight:200}
.sm-b__statement{text-align:center;font-size:clamp(44px,6.5vw,92px);font-weight:300;letter-spacing:-0.035em;margin:52px 0 0;line-height:0.95}
.sm-b__statement strong{font-weight:600}
.sm-b__stats{display:flex;justify-content:center;gap:clamp(22px,4vw,60px);margin:40px 0 44px;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,0.14);padding-top:30px}
.sm-b__stats span{font-size:12.5px;color:rgba(255,255,255,0.6);letter-spacing:0.05em;text-transform:uppercase}
.sm-b__stats b{display:block;font-size:clamp(26px,2.8vw,38px);font-weight:500;color:#fff;letter-spacing:-0.015em;margin-bottom:4px}
.sm__cta{display:inline-flex;align-items:center;gap:8px;background:#fff;color:#141414;padding:16px 30px;font-size:13px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none}
.sm__cta:hover{opacity:0.88}
@media(max-width:760px){.sm__cards,.sm__slogans{grid-template-columns:1fr}}
</style>
<section class="sm" id="sockmath" data-sm="a" aria-label="The Sock Math">
  <div class="sm__inner">
    <div class="sm__head">
      <div class="sm__headcopy">
        <p class="sm__eyebrow">The Sock Math</p>
        <h2 class="sm__title">Stop replacing.<br><strong>Start performing.</strong></h2>
      </div>
      <div class="sm__toggle" role="tablist" aria-label="Switch layout">
        <button data-v="a" class="is-on" type="button">Comparison</button>
        <button data-v="b" type="button">Statement</button>
      </div>
    </div>
    <p class="sm__sub">Grip socks have two failure points — your foot moves inside the sock, and the sock moves on the floor. Barreletics eliminates both.</p>

    <!-- DESIGN A: comparison + slogan nest -->
    <div class="sm-a sm-variant">
      <div class="sm__cards">
        <div class="sm__card">
          <p class="sm__label">Grip socks</p>
          <div class="sm__price"><s>$336</s></div>
          <p class="sm__meta">per year · 8–12 pairs at $18–28 each</p>
          <ul class="sm__rows">
            <li class="sm__row"><span class="sm__row-k">Grip lifespan</span><span class="sm__row-v">6–8 washes</span></li>
            <li class="sm__row"><span class="sm__row-k">Pairs per year</span><span class="sm__row-v">8–12</span></li>
            <li class="sm__row"><span class="sm__row-k">Foot slips inside?</span><span class="sm__row-v">Yes</span></li>
            <li class="sm__row"><span class="sm__row-k">Grip after 6 months</span><span class="sm__row-v">Cracked &amp; peeling</span></li>
          </ul>
        </div>
        <div class="sm__card sm__card--ours">
          <p class="sm__label">Barreletics</p>
          <div class="sm__price">$74</div>
          <p class="sm__meta">once · same grip from class 1 to class 1,000</p>
          <ul class="sm__rows">
            <li class="sm__row"><span class="sm__row-k">Grip lifespan</span><span class="sm__row-v">1,000+ classes</span></li>
            <li class="sm__row"><span class="sm__row-k">Pairs needed</span><span class="sm__row-v">1</span></li>
            <li class="sm__row"><span class="sm__row-k">Foot slips inside?</span><span class="sm__row-v">Impossible</span></li>
            <li class="sm__row"><span class="sm__row-k">Grip after 6 months</span><span class="sm__row-v">Identical to day 1</span></li>
          </ul>
        </div>
      </div>
      <div class="sm__slogans" style="margin-top:48px">
        <p>Socks fail. <strong>This doesn't.</strong></p>
        <p>360° grip — <em>not dots</em> that wash off.</p>
        <p>Your foot <strong>can't move inside it.</strong></p>
        <p>Same grip, <strong>class 1 to class 1,000.</strong></p>
        <p>Rinse. Dry. <strong>Reuse. Forever.</strong></p>
        <p>No latex. No silicone. <em>Made in USA.</em></p>
      </div>
      <a href="Barreletics Collection.html" class="sm__cta">Shop the collection →</a>
    </div>

    <!-- DESIGN B: statement -->
    <div class="sm-b sm-variant">
      <div class="sm-b__row">
        <div class="sm-b__col">
          <p class="sm__label">Grip socks</p>
          <div class="sm-b__big"><s>$336</s></div>
          <p class="sm-b__cap">every year — 8–12 pairs, grip cracked in 6–8 washes</p>
        </div>
        <div class="sm-b__arrow" aria-hidden="true">→</div>
        <div class="sm-b__col">
          <p class="sm__label sm__label--ours">Barreletics</p>
          <div class="sm-b__big sm-b__big--ours">$74</div>
          <p class="sm-b__cap">once — same grip on class 1 as class 1,000</p>
        </div>
      </div>
      <p class="sm-b__statement">One pair. <strong>Done.</strong></p>
      <div class="sm-b__stats">
        <span><b>1,000+</b>classes, one pair</span>
        <span><b>1</b>pair, ever</span>
        <span><b>0</b>mid-class resets</span>
        <span><b>360°</b>full-contact traction</span>
      </div>
      <div style="text-align:center"><a href="Barreletics Collection.html" class="sm__cta">Shop the collection →</a></div>
    </div>
  </div>
</section>
<script>
(function(){
  var s=document.getElementById('sockmath'); if(!s) return;
  var btns=s.querySelectorAll('.sm__toggle button');
  function set(v){ s.dataset.sm=v; try{localStorage.setItem('br_sockmath',v);}catch(e){}
    btns.forEach(function(b){var on=b.dataset.v===v;b.classList.toggle('is-on',on);b.setAttribute('aria-selected',on);}); }
  btns.forEach(function(b){ b.addEventListener('click',function(){set(b.dataset.v);}); });
  var saved='a'; try{saved=localStorage.getItem('br_sockmath')||'a';}catch(e){}
  set(saved);
})();
</script>

<!-- PHOTO SPLIT — pink group -->
<section class="v11-split" style="border-top:none;border-bottom:1px solid var(--br-line)">
  <div class="v11-split__copy" style="order:-1">
    <div class="v11-split__stars">★★★★★</div>
    <p class="v11-split__trusted">For yoga, Pilates, and barre</p>
    <h2 class="v11-split__slogan">Progress, built from<br><strong>the ground up.</strong></h2>
    <p style="font-size:16px;line-height:1.6;color:var(--br-text-soft);margin:0 0 20px;max-width:38ch">From first class to your hundredth. The grip to hold longer, push harder, and focus on form — not your feet.</p>
    <a href="Barreletics Collection.html" class="v11-split__cta">Shop the collection →</a>
  </div>
  <div class="v11-split__media">
    <img src="https://barreletics.com/cdn/shop/files/IMG_5051.jpg" alt="Barreletics performance skins — in the studio">
  </div>
</section>

<!-- 3 DISCIPLINES -->
<section class="v11-disciplines" id="disciplines">
  <div class="v11-disciplines__inner">
    <div class="v11-disciplines__head">
      <p class="v11-eyebrow">Three disciplines. One shoe.</p>
      <h2 class="v11-h2">Barre. Reformer. Megaformer. One shoe.</h2>
      <p class="v11-lede">For yoga, Pilates, and barre — on the mat or off it — the same 360° grip holds through every transition, every pose, every class.</p>
    </div>
    <div class="v11-disciplines__grid">
      <div class="v11-disc">
        <img class="v11-disc__img" src="https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=1200" alt="Barre class — Barreletics grip shoes">
        <div class="v11-disc__overlay">
          <p class="v11-disc__eyebrow">Barre</p>
          <h3 class="v11-disc__title">In the plié. In the relevé. In everything.</h3>
          <p class="v11-disc__body">Through every plié, relevé, and arabesque — heel-to-toe grip that holds. No adjusting at the barre between sets.</p>
        </div>
      </div>
      <div class="v11-disc">
        <img class="v11-disc__img" src="https://barreletics.com/cdn/shop/files/View_recent_photos.png" alt="Pilates reformer — Barreletics grip shoes">
        <div class="v11-disc__overlay">
          <p class="v11-disc__eyebrow">Reformer Pilates</p>
          <h3 class="v11-disc__title">The carriage moves. Your feet don’t.</h3>
          <p class="v11-disc__body">From footbar to carriage, footwork to bridging — the carriage moves. Your feet don’t.</p>
        </div>
      </div>
      <div class="v11-disc">
        <img class="v11-disc__img" src="https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A7000_blue_background_2.jpg" alt="Lagree Megaformer — Barreletics grip shoes">
        <div class="v11-disc__overlay">
          <p class="v11-disc__eyebrow">Lagree &amp; Megaformer</p>
          <h3 class="v11-disc__title">50 minutes. Every transition. Zero adjustments.</h3>
          <p class="v11-disc__body">Slow reps, fast transitions, 50 minutes of time under tension. Earn the shake. Not the slip.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PINK VIDEO SPLIT -->
<section class="v11-split" style="border-bottom:none">
  <div class="v11-split__media">
    <video autoplay="" loop="" muted="" playsinline="" preload="metadata" src="https://cdn.shopify.com/videos/c/o/v/d11716a75dc64da7ba1a5521e39d942b.mov" poster="https://barreletics.com/cdn/shop/files/IMG_2917.jpg?v=1741040637&amp;width=1200">
    </video>
  </div>
  <div class="v11-split__copy">
    <div class="v11-split__stars">★★★★★</div>
    <p class="v11-split__trusted">Barefoot-inspired feel — second-skin fit</p>
    <h2 class="v11-split__slogan">Never<br><strong>loses grip.</strong></h2>
    <p style="font-size:16px;line-height:1.6;color:var(--br-text-soft);margin:0 0 20px;max-width:38ch">Same grip on class 1 as class 1,000. No adjustments. No resets. Just movement.</p>
    <a href="Barreletics Collection.html" class="v11-split__cta">Shop the collection →</a>
  </div>
</section>

<!-- REVIEWS -->
<style>
.v11-rev2{padding:clamp(56px,7vw,96px) clamp(24px,5vw,64px);background:var(--br-alt-bg)}
.v11-rev2__inner{max-width:1320px;margin:0 auto}
.v11-rev2__head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:40px;padding-bottom:26px;border-bottom:1px solid var(--br-line)}
.v11-rev2__eyebrow{font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--br-accent);margin:0 0 10px}
.v11-rev2__title{font-size:clamp(26px,3vw,40px);font-weight:500;letter-spacing:-0.015em;margin:0;line-height:1.05}
.v11-rev2__summary{font-size:14px;color:var(--br-text-soft);margin:10px 0 0}
.v11-rev2__summary b{color:var(--br-text);font-weight:600}
.v11-rev2__link{font-size:12px;letter-spacing:0.1em;text-transform:uppercase;color:var(--br-text);text-decoration:none;border-bottom:1px solid var(--br-text);padding-bottom:2px;font-weight:600;white-space:nowrap}
.v11-rev2__grid{column-count:4;column-gap:16px}
@media(max-width:1100px){.v11-rev2__grid{column-count:3}}
@media(max-width:760px){.v11-rev2__grid{column-count:2}}
@media(max-width:480px){.v11-rev2__grid{column-count:1}}
.v11-rc{break-inside:avoid;margin:0 0 16px;background:#fff;border:1px solid var(--br-line);display:flex;flex-direction:column}
.v11-rc__media{overflow:hidden;position:relative}
.v11-rc__media img{width:100%;height:100%;object-fit:cover;display:block}
.v11-rc__tag{position:absolute;left:12px;bottom:12px;background:rgba(0,0,0,0.55);color:#fff;font-size:10px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;padding:5px 9px;backdrop-filter:blur(4px)}
.v11-rc__body{padding:22px 22px 24px}
.v11-rc__stars{color:var(--br-star);font-size:14px;letter-spacing:1.5px;margin-bottom:11px}
.v11-rc__badge{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:3px 8px;background:var(--br-le-bg);color:var(--br-le);margin-bottom:11px}
.v11-rc__quote{font-size:15px;line-height:1.55;color:var(--br-text);margin:0 0 15px;letter-spacing:-0.005em}
.v11-rc--media .v11-rc__quote{font-size:14px}
.v11-rc__attr{font-size:11px;font-weight:600;letter-spacing:0.07em;text-transform:uppercase;color:var(--br-text-mute)}
.v11-rev2__foot{margin-top:36px;text-align:center}
</style>
<section class="v11-rev2" id="reviews">
  <div class="v11-rev2__inner">
    <div class="v11-rev2__head">
      <div>
        <p class="v11-rev2__eyebrow">Confidence, from the ground up</p>
        <h2 class="v11-rev2__title">1,000+ reviews. 4.9 stars.</h2>
        <p class="v11-rev2__summary"><b>294 verified</b> · instructors, reformer devotees & 4-year customers</p>
      </div>
      <a href="#" class="v11-rev2__link">Read all reviews →</a>
    </div>
    <div class="v11-rev2__grid">

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:4/5"><img src="https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=900" alt="Customer in barre class wearing Barreletics" loading="lazy"><span class="v11-rc__tag">Barre · in class</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"My love-hate relationship with the sock has come to a ceremonial end. The improvement in the first minute of barre class is beyond words."</p>
          <p class="v11-rc__attr">Mia Evans · Closed Sole</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <span class="v11-rc__badge">80 helpful votes</span>
          <p class="v11-rc__quote">"I looked at these for over a year thinking 'way too expensive.' I can't tell you how much I spent on Pilates socks that ruined and stretched out. Then I got these. Game changer."</p>
          <p class="v11-rc__attr">Gwen M. · Queens, US</p>
        </div>
      </article>

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:1/1"><img src="https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A7000_blue_background_2.jpg" alt="Instructor on the reformer wearing Barreletics" loading="lazy"><span class="v11-rc__tag">Reformer · studio</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <span class="v11-rc__badge">Barre instructor</span>
          <p class="v11-rc__quote">"I teach on a variety of surfaces — these provide the perfect level of grip and support and fit like a glove. Finally a good durable barre shoe!"</p>
          <p class="v11-rc__attr">Laura P. · Sacramento, US</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"After almost a year off the foot bar due to my neuropathy, I am confidently back to the footwork series in Pilates."</p>
          <p class="v11-rc__attr">JenB · Millville, US</p>
        </div>
      </article>

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:4/5"><img src="https://barreletics.com/cdn/shop/files/Multi_Image.jpg?v=1768346625&width=900" alt="Barreletics performance skin — heel to toe grip" loading="lazy"><span class="v11-rc__tag">4-year customer</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"This is my second pair — my first purchased almost 4 years ago. The security is unmatched. I refuse to wear anything else."</p>
          <p class="v11-rc__attr">Kimberly · Knoxville, US</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"Genius concept. Simple, effective, stylish — I can improve my workout 10 fold without the nagging sock slippage and constant adjustment."</p>
          <p class="v11-rc__attr">Jess · Ashburn, US</p>
        </div>
      </article>

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:1/1"><img src="https://cdn.shopify.com/s/files/1/0045/0612/4391/files/IMG_5051.jpg" alt="Barreletics in the studio" loading="lazy"><span class="v11-rc__tag">Cadillac · age 70</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"The best invention known to Pilates devotees. At 70 I can accomplish advanced moves on the Cadillac — your foot has to grip the bar without fail."</p>
          <p class="v11-rc__attr">Dvorah S. · Fairfield, US</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <span class="v11-rc__badge">18 months use</span>
          <p class="v11-rc__quote">"I was dreading Pilates after a spinal fusion — grip socks would slip on bridges. I started looking for something that would help, and found it."</p>
          <p class="v11-rc__attr">Samantha B. · Castle Rock, US</p>
        </div>
      </article>

    </div>
    <div class="v11-rev2__foot"><a href="#" class="v11-rev2__link">Read all 294 reviews →</a></div>
  </div>
</section>

<!-- BELIEF DARK -->
<!-- COPERNI COLLAB -->
<section style="display:grid;grid-template-columns:1fr 1fr;min-height:480px">
  <!-- Left: video -->
  <div style="position:relative;overflow:hidden;background:#0a0a0a">
    <video style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" autoplay="" loop="" muted="" playsinline="" preload="metadata" src="https://cdn.shopify.com/videos/c/o/v/d7ca87eac5034642851089c63af6a2d8.mov">
    </video>
  </div>
  <!-- Right: runway model still + copy -->
  <div style="position:relative;overflow:hidden;background:#111;display:flex;flex-direction:column;justify-content:flex-end">
    <img style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;opacity:0.85" src="https://barreletics.com/cdn/shop/files/Screenshot_2026-03-20_at_6.53.30_PM.png" alt="Coperni x Barreletics — Paris runway SS26">
    <div style="position:relative;z-index:2;padding:48px 48px;background:linear-gradient(to top,rgba(0,0,0,0.88) 0%,rgba(0,0,0,0.3) 60%,transparent 100%)">
      <span style="font-size:clamp(20px,2.5vw,32px);font-weight:400;letter-spacing:-0.01em;color:rgba(255,255,255,0.9);display:block;margin-bottom:20px;font-style:normal">The Pilates sock era is over.</span>
      <span style="font-size:11px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.45);display:block;margin-bottom:14px">Limited Edition · Paris SS26</span>
      <h2 style="font-size:clamp(26px,3vw,42px);font-weight:400;letter-spacing:-0.02em;color:#fff;margin:0 0 14px;line-height:1.1">Barreletics ×<br>Coperni.</h2>
      <p style="font-size:15px;line-height:1.6;color:rgba(255,255,255,0.75);margin:0 0 28px;max-width:36ch">A Pilates shoe on the Coperni runway, Spring–Summer 2026. Closed sole. One run.</p>
      <a href="#" style="display:inline-flex;align-items:center;padding:14px 28px;background:#fff;color:#050505;font-size:13px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none">Shop the collab →</a>
    </div>
  </div>
</section>

<!-- JOURNAL PREVIEW -->
<section class="v11-journal">
  <div class="v11-journal__inner">
    <div class="v11-section-head">
      <p class="v11-eyebrow">The journal</p>
      <h2 class="v11-h2">Notes from the studio.</h2>
      <p class="v11-lede">Care guides, founder notes, and stories from the people who put performance skins to the test.</p>
    </div>
    <div class="pg-editorial-grid" style="margin-top:56px">
    <a href="Barreletics Article.html" class="pg-edit">
      <div class="pg-edit__media"><img src="https://barreletics.com/cdn/shop/files/Multi_Image.jpg" alt="How to wash your performance skins" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <p class="pg-edit__meta">Care · 3 min read</p>
      <h3 class="pg-edit__title">How to wash your performance skins.</h3>
      <p class="pg-edit__dek">The only three steps you need. Plus the one thing that quietly kills grip skins faster than anything else.</p>
    </a>
    <a href="Barreletics Article 02 Founder.html" class="pg-edit">
      <div class="pg-edit__media"><img src="https://barreletics.com/cdn/shop/products/barreletixxjumpingtogether.jpg" alt="Why we built a grip sock replacement" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <p class="pg-edit__meta">Founder · 5 min read</p>
      <h3 class="pg-edit__title">Why we built a grip-sock replacement.</h3>
      <p class="pg-edit__dek">The moment in class that made it obvious the grip sock needed to be retired. And what it took to build the replacement.</p>
    </a>
    <a href="Barreletics Article 03 Coperni.html" class="pg-edit">
      <div class="pg-edit__media"><img src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png" alt="Coperni x Barreletics in Paris" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <p class="pg-edit__meta">Story · 4 min read</p>
      <h3 class="pg-edit__title">Coperni × Barreletics, in Paris.</h3>
      <p class="pg-edit__dek">How a performance skin built for studio floors ended up closing Coperni’s Paris show.</p>
    </a>
  </div>
    <div style="text-align:center;margin-top:48px">
      <a href="Barreletics Blog.html" class="pdp-variants__head-link">Read the journal →</a>
    </div>
  </div>
</section>

<!-- GUARANTEE -->
<section class="v11-guarantee" id="guarantee">
  <div class="v11-guarantee__head">
    <h2 class="v11-guarantee__main-title" style="font-size:clamp(32px,4vw,56px);font-weight:300;letter-spacing:-0.02em">Zero risk.<br><strong style="font-weight:600">All grip.</strong></h2>
    <p style="font-size:20px;font-weight:500;color:rgba(255,255,255,0.85);margin:20px 0 0;letter-spacing:-0.01em">Try it for 30 days.</p>
    <p class="v11-guarantee__main-sub">Wear it to every class. If it’s not the best footwear decision you’ve made, return it. No questions. The product doesn’t fail — that’s why we can offer this.</p>
  </div>
  <div class="v11-guarantee__inner">
    <div>
      <p class="v11-guarantee__eyebrow">30-day confidence</p>
      <h3 class="v11-guarantee__title">30 days. Your call.</h3>
      <p class="v11-guarantee__body">Wear it to every class for 30 days. Not the best footwear decision you’ve made? Return it. No questions, no hassle.</p>
    </div>
    <div class="v11-guarantee__divider"></div>
    <div>
      <p class="v11-guarantee__eyebrow">90-day product warranty</p>
      <h3 class="v11-guarantee__title">Built to last. Backed to prove it.</h3>
      <p class="v11-guarantee__body">If the material tears or the seams fail, we replace it. No receipts, no runaround. That’s the 90-day product guarantee.</p>
    </div>
    <div class="v11-guarantee__divider"></div>
    <div>
      <p class="v11-guarantee__eyebrow">The long game</p>
      <h3 class="v11-guarantee__title">One pair. Four years. Still gripping.</h3>
      <p class="v11-guarantee__body">$74 once versus $144–$336 in socks every year. Kimberly bought her first pair 4 years ago. She’s on her second — for the color.</p>
    </div>
  </div>
</section>

<!-- NEWSLETTER -->
<section class="v11-newsletter">
  <h2>10% off your first pair.</h2>
  <p>New drops, studio stories, care tips. Once or twice a quarter. Never spam.</p>
  <form class="v11-newsletter__form" onsubmit="return false">
    <input type="email" placeholder="Email address" aria-label="Email address">
    <button type="submit">Get 10% off</button>
  </form>
</section>

<!-- FAQ (GEO-optimized) -->
<section class="pdp-section pdp-faq" id="faq" style="background:var(--br-alt-bg)">
  <p class="pdp-eyebrow" style="color:var(--br-accent);text-align:center">Common questions</p>
  <h2 class="pdp-h2" style="text-align:center">Everything you need to know.</h2>
  <div class="pdp-faq__list" style="margin-top:48px;max-width:800px;margin-left:auto;margin-right:auto">
    <details class="pdp-faq__item" open="">
      <summary class="pdp-faq__q">What makes Barreletics different from grip socks?</summary>
      <p class="pdp-faq__a">Grip socks have two failure points: the sock slips on the floor, and your foot slips inside the sock. Barreletics is a performance skin — it wraps your foot like a second skin, so interior movement is impossible. The exterior grip covers 360 degrees from heel to toe. No latex, no silicone dots, no fabric to stretch out.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">Are Barreletics good for reformer Pilates?</summary>
      <p class="pdp-faq__a">Yes — they were specifically engineered for reformer Pilates, barre, Lagree and Megaformer. The closed sole grips the footbar and carriage through every transition. Over 294 verified reviews, with Pilates instructors, reformer practitioners, and Lagree devotees all citing the reformer as their primary use case.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">How long do Barreletics last compared to grip socks?</summary>
      <p class="pdp-faq__a">Grip socks typically lose their grip after 6–8 washes. Barreletics customers report using the same pair for 1–4+ years with no grip degradation. At $74 vs $144–$336 in annual sock spending, the math strongly favors one pair of Barreletics.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">How do you clean Barreletics?</summary>
      <p class="pdp-faq__a">Warm soapy water and air dry. Never the washing machine — machine washing accelerates material breakdown. A quick rinse after class keeps them studio-fresh indefinitely.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">What size should I order?</summary>
      <p class="pdp-faq__a">Barreletics come in M (Women’s 5.5–7.5) and L (Women’s 8–11). For a more forgiving fit, size up. For men up to size 10.5, choose Large. The performance skin should sit where the ball of your foot meets your toes.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">What is the return policy?</summary>
      <p class="pdp-faq__a">30-day returns. 90-day product warranty — if anything fails structurally, we replace it, no questions asked. We’ve never worried about making this offer because the product doesn’t fail.</p>
    </details>
  </div>
</section>

<!-- INSTAGRAM FEED -->
<section style="padding:80px 64px;background:#fff;border-top:1px solid var(--br-line)">
  <div style="max-width:1280px;margin:0 auto;text-align:center">
    <p style="font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--br-accent);margin:0 0 12px">Follow along</p>
    <h2 style="font-size:clamp(24px,3vw,36px);font-weight:400;letter-spacing:-0.02em;margin:0 0 8px">@barreletics</h2>
    <p style="font-size:15px;color:var(--br-text-soft);margin:0 0 48px">#letusknockyoursocksoff</p>
    <!-- Juicer embed -->
    <div class="juicer-feed j-initialized" data-feed-id="barreletics" data-per="9" data-truncate="300"><div class="j-loading-wrapper"><div class="j-loading">Loading...</div></div></div>
  </div>
</section>



<!-- FOOTER -->
<footer class="pdp-footer">
  <div class="pdp-footer__grid">
    <div class="pdp-footer__col pdp-footer__brand">
      <a href="#" class="pdp-header__logo" aria-label="Barreletics home">
        <img src="barreletics-logo.png" alt="Barreletics">
      </a>
      <p>The premium performance alternative to grip socks. Superior grip from heel to toe, on the floor and on your foot. Made in USA.</p>
      <p style="margin-top:14px;font-size:13px;letter-spacing:0.12em;text-transform:uppercase;color:var(--br-accent);font-weight:700">#letusknockyoursocksoff</p>
    </div>
    <div class="pdp-footer__col"><h6>Shop</h6><ul>
      <li><a href="Barreletics Collection.html">Studio collection</a></li>
      <li><a href="#">Outdoor &amp; aquatic</a></li>
      <li><a href="#">Closed vs open sole</a></li>
      <li><a href="#">Studio bundles</a></li>
      <li><a href="#">Coperni × Barreletics</a></li>
      <li><a href="#">Gift cards</a></li>
    </ul></div>
    <div class="pdp-footer__col"><h6>Support</h6><ul>
      <li><a href="#">Size chart</a></li>
      <li><a href="#">Care guide</a></li>
      <li><a href="#">Shipping &amp; returns</a></li>
      <li><a href="#">30-day confidence guarantee</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Contact</a></li>
    </ul></div>
    <div class="pdp-footer__col"><h6>Journal</h6><ul>
      <li><a href="Barreletics Blog.html">All articles</a></li>
      <li><a href="#">How to wash your skins</a></li>
      <li><a href="#">Founder story</a></li>
      <li><a href="#">Coperni × Barreletics</a></li>
      <li><a href="#">About Barreletics</a></li>
      <li><a href="#">Become an affiliate</a></li>
    </ul></div>
    <div class="pdp-footer__col"><h6>Follow</h6><ul>
      <li><a href="#">Instagram</a></li>
      <li><a href="#">TikTok</a></li>
      <li><a href="#">YouTube</a></li>
      <li><a href="#">Pinterest</a></li>
    </ul></div>
  </div>
  <div class="pdp-footer__bottom">
    <span>© 2026 Barreletics. All rights reserved. Made in USA.</span>
    <span><a href="#" style="color:inherit;text-decoration:none">Privacy</a> · <a href="#" style="color:inherit;text-decoration:none">Terms</a> · <a href="#" style="color:inherit;text-decoration:none">Accessibility</a></span>
  </div>
</footer>

<script>
// Rotating ticker — cross-fades messages every 5s
(function () {
  const ticker = document.querySelector('.pdp-ticker');
  if (!ticker) return;
  const slides = ticker.querySelectorAll('.pdp-ticker__slide');
  if (slides.length < 2) return;
  let i = 0;
  setInterval(() => {
    slides[i].classList.remove('is-active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('is-active');
  }, 5000);
})();

</script>

<script>
// Rotating slogans on media split
const slogans = [
  "Socks fail. This doesn’t.",
  "Secure in every hold. No sliding. No resets.",
  "Your foot moves in the sock. The sock moves on the floor. Now neither does.",
  "Stop adjusting. Move.",
  "Built for the move, not the pose.",
  "Earn the shake. Not the slip.",
  "For people who call it their practice.",
  "Five days a week. Zero compromises."
];
let idx = 0;
const el = document.getElementById('rotating-slogan');
if (el) {
  setInterval(() => {
    el.style.opacity = '0';
    setTimeout(() => {
      idx = (idx + 1) % slogans.length;
      el.textContent = slogans[idx];
      el.style.opacity = '1';
    }, 400);
  }, 4000);
}
</script>

<script>

// Hero eyebrow rotation
const eyebrows = [
  "The Pilates sock era is over.",
  "A new kind of grip shoe.",
  "Trusted by 1,000’s of instructors.",
  "Made in USA. Built for the carriage.",
  "Barre. Reformer. Megaformer. One shoe."
];
let eidx = 0;
const eyebrowEl = document.getElementById('hero-eyebrow');
if (eyebrowEl) {
  setInterval(() => {
    eyebrowEl.style.opacity = '0';
    setTimeout(() => {
      eidx = (eidx + 1) % eyebrows.length;
      eyebrowEl.textContent = eyebrows[eidx];
      eyebrowEl.style.opacity = '1';
    }, 300);
  }, 3500);
}

// Second rotating slogan — video split
const slogans2 = [
  "Your foot moves in the sock. The sock moves on the floor. Now neither does.",
  "The Pilates sock era is over.",
  "50 minutes. Every transition. Zero adjustments.",
  "Built for the move, not the pose.",
  "Stop adjusting. Start moving.",
  "For people who call it their practice."
];
let idx2 = 0;
const el2 = document.getElementById('rotating-slogan-2');
if (el2) {
  setInterval(() => {
    el2.style.opacity = '0';
    setTimeout(() => {
      idx2 = (idx2 + 1) % slogans2.length;
      el2.textContent = slogans2[idx2];
      el2.style.opacity = '1';
    }, 400);
  }, 5000);
}
</script>


<!-- ═══════ MATURED: THE FOUNDER ═══════ -->
<section class="matured-section" style="border-top:1px solid var(--br-line)">
  <div class="m-founder">
    <div class="m-founder__media">
      <div class="ph ph--dark" data-ph="Founder portrait — Stefanie Miller"></div>
    </div>
    <div class="m-founder__copy">
      <p class="m-eyebrow">Why we built it</p>
      <p class="m-founder__quote">She was literally unable to <strong>"get a grip"</strong> — so she engineered one.</p>
      <p class="m-founder__body">After years modeling for the world's best fashion houses, our founder fell in love with textiles. When no grip sock could keep up with her barre practice, she applied what she'd learned — and made an injection-molded performance skin instead.</p>
      <div class="m-founder__sign"><b>Stefanie Miller</b><span>Founder · Made in USA</span></div>
      <ul class="m-founder__extra m-extra m-extra--flex">
        <li><b>A textile background</b>, not a sock company</li>
        <li><b>Molded, not printed</b> — no latex, no silicone</li>
      </ul>
    </div>
  </div>
</section>

<!-- ═══════ MATURED: THE PROBLEM ═══════ -->
<section class="matured-section" style="border-top:1px solid var(--br-line)">
  <div class="m-prob">
    <div>
      <p class="m-eyebrow">The problem with grip socks</p>
      <h2 class="m-display m-prob__display">Socks were never<br><strong>built to grip.</strong></h2>
      <p class="m-prob__body">Printed dots wear flat. Toes stay bound. You replace them every few months. <b>A molded performance skin solves all of it at once</b> — 360° traction that doesn't fade.</p>
    </div>
    <ul class="m-prob__old m-extra m-extra--flex">
      <p class="m-prob__old-h">What you're replacing</p>
      <li><s>Slipping on the reformer</s></li>
      <li><s>Loss of stability mid-move</s></li>
      <li><s>Worn-out grip</s></li>
      <li><s>Constant sock replacement</s></li>
    </ul>
  </div>
</section>

<!-- ═══════ MATURED: BRAND LINE ═══════ -->
<section class="matured-section">
  <div class="m-manifesto">
    <p class="m-eyebrow" style="color:rgba(255,255,255,0.7);justify-content:center;">The brand line</p>
    <div class="m-manifesto__rotator" id="sloganRotator">
      <div class="m-manifesto__line is-active">Grip Isn't <strong>Optional.</strong></div>
      <div class="m-manifesto__line">No Socks. <strong>Just Grip.</strong></div>
      <div class="m-manifesto__line">Pilates <strong>Evolved.</strong></div>
      <div class="m-manifesto__line">Built For <strong>Movement.</strong></div>
      <div class="m-manifesto__line">The End Of <strong>Grip Socks.</strong></div>
      <div class="m-manifesto__line">Move Without <strong>Limits.</strong></div>
    </div>
    <p class="m-manifesto__sub">Where barefoot meets performance. The future of grip — molded, not printed.</p>
  </div>
</section>

<script>
// Brand line rotator
(function() {
  const rotator = document.getElementById('sloganRotator');
  if (!rotator) return;
  const lines = Array.from(rotator.querySelectorAll('.m-manifesto__line'));
  let i = 0;
  setInterval(function() {
    lines[i].classList.remove('is-active');
    i = (i + 1) % lines.length;
    lines[i].classList.add('is-active');
  }, 2600);
})();
</script>

<!-- Tweaks -->
<div id="tweaks-root"></div>
<script src="https://unpkg.com/react@18.3.1/umd/react.development.js" integrity="sha384-hD6/rw4ppMLGNu3tX5cjIb+uRZ7UkRJ6BPkLpg4hAu/6onKUg4lLsHAs9EBPT82L" crossorigin="anonymous"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" integrity="sha384-u6aeetuaXnQ38mYT8rp6sbXaQe3NL9t+IBXmnYxwkUI2Hw4bsp2Wvmx4yRQF1uAm" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" integrity="sha384-m08KidiNqLdpJqLq95G/LEi8Qvjl/xUYll3QILypMoQ65QorJ9Lvtp2RXYGBFj1y" crossorigin="anonymous"></script>
<script type="text/babel" src="tweaks-panel.jsx"></script>
<script type="text/babel">
const HOME_MAT_DEFAULTS = {
  "matured": "on",
  "ground": "warm",
  "eyebrow": "soft",
  "density": "editorial"
};

function HomeMatTweaks() {
  const [t, setTweak] = useTweaks(HOME_MAT_DEFAULTS);

  React.useEffect(() => {
    document.body.dataset.matured = t.matured;
    document.body.dataset.ground = t.ground;
    document.body.dataset.eyebrow = t.eyebrow;
    document.body.dataset.density = t.density;
  }, [t.matured, t.ground, t.eyebrow, t.density]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Direction" />
      <TweakRadio label="Palette" value={t.matured}
        options={['on', 'off']}
        onChange={(v) => setTweak('matured', v)} />
      <TweakRadio label="Ground" value={t.ground}
        options={['warm', 'white']}
        onChange={(v) => setTweak('ground', v)} />
      <TweakRadio label="Eyebrows" value={t.eyebrow}
        options={['soft', 'technical']}
        onChange={(v) => setTweak('eyebrow', v)} />
      <TweakRadio label="Density" value={t.density}
        options={['editorial', 'informative']}
        onChange={(v) => setTweak('density', v)} />
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('tweaks-root')).render(<HomeMatTweaks />);
</script>

</body></html>
---

## CSS Specifications (from home-matured.css)

/* ============================================================
   Barreletics Home — Matured
   Page chrome: ticker, header, footer, product grid, structure
   Component styles come from maturation-styles.css
   ============================================================ */

/* ---------- Page body ---------- */
html, body {
  margin: 0; padding: 0;
  font-family: var(--font);
  background: var(--m-bg);
  color: var(--m-ink);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-wrap: pretty;
}
img, video { max-width: 100%; display: block; }
[data-ground="white"] { --m-bg: #ffffff; --m-surface: #ffffff; }

.page-wrap { overflow: hidden; }

/* ---------- Ticker ---------- */
.hm-ticker {
  background: var(--m-dark);
  color: #fff;
  position: relative;
  height: 40px;
  overflow: hidden;
  z-index: 100;
}
.hm-ticker__slide {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.06em;
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 0.5s ease, transform 0.5s ease;
  text-align: center;
  white-space: nowrap;
}
.hm-ticker__slide.is-active {
  opacity: 1;
  transform: translateY(0);
}
.hm-ticker__slide b { font-weight: 700; }
.hm-ticker__slide a {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  margin-left: 6px;
}
.hm-ticker__slide a:hover { color: #fff; border-color: #fff; }

/* ---------- Header ---------- */
.hm-header {
  position: sticky;
  top: 0;
  z-index: 90;
  background: rgba(255,255,255,0.96);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--m-line);
}
.hm-header__inner {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 40px;
  height: 60px;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
}
.hm-header__nav {
  display: flex;
  gap: 28px;
  font-size: 14px;
  font-weight: 400;
  letter-spacing: 0.01em;
}
.hm-header__nav a {
  color: var(--m-ink);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: color 0.15s;
}
.hm-header__nav a:hover { color: var(--m-accent); }
.hm-header__chev {
  font-size: 12px;
  line-height: 1;
  opacity: 0.5;
  transform: translateY(1px);
}
.hm-header__logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 24px;
  text-decoration: none;
}
.hm-header__logo img {
  display: block;
  height: 100%;
  width: auto;
}
.hm-header__util {
  display: flex;
  gap: 24px;
  justify-self: end;
  align-items: center;
  font-size: 14px;
  font-weight: 400;
}
.hm-header__util a {
  color: var(--m-ink);
  text-decoration: none;
}
.hm-header__cart {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.hm-header__cart-dot {
  width: 20px; height: 20px;
  background: var(--m-accent);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  color: #fff;
}
.hm-header__cart-dot::before { content: "0"; }

/* ---------- Section spacing ---------- */
.hm-section {
  border-top: 1px solid var(--m-line);
}
.hm-section:first-child { border-top: 0; }

/* ---------- Product grid (v28 adaptation) ---------- */
.hm-grid {
  background: #fff;
  padding: 64px 56px;
}
.hm-grid__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
.hm-grid__tabs {
  display: flex;
  gap: 0;
  margin-bottom: 28px;
}
.hm-grid__tab {
  padding: 12px 24px;
  font-family: var(--font);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  cursor: pointer;
  border: 1px solid var(--m-line);
  background: transparent;
  color: var(--m-mute);
}
.hm-grid__tab:first-child { border-right: 0; }
.hm-grid__tab.is-active {
  background: var(--m-ink);
  color: #fff;
  border-color: var(--m-ink);
}
.hm-grid__products {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
.hm-grid__card {
  display: flex;
  flex-direction: column;
  gap: 6px;
  text-decoration: none;
  color: inherit;
}
.hm-grid__card-img {
  aspect-ratio: 1;
  background: #f5f5f5;
  overflow: hidden;
  position: relative;
}
.hm-grid__card-img img {
  width: 100%; height: 100%;
  object-fit: cover; display: block;
}
.hm-grid__card-le {
  position: absolute; top: 10px; left: 10px;
  font-size: 9px; font-weight: 700;
  letter-spacing: 0.1em; text-transform: uppercase;
  background: var(--m-accent); color: #fff;
  padding: 4px 8px;
}
.hm-grid__card h4 { font-size: 14px; font-weight: 500; margin: 4px 0 0; }
.hm-grid__card .meta { font-size: 12px; color: var(--m-soft); margin: 0; }
.hm-grid__card .price { font-size: 13px; font-weight: 500; margin: 0; }
.hm-grid__card .shop { font-size: 12px; font-weight: 600; letter-spacing: 0.06em; color: var(--m-ink); margin-top: 2px; }
.hm-grid__foot {
  text-align: center;
  margin-top: 48px;
  padding-top: 32px;
  border-top: 1px solid var(--m-line);
}
.hm-grid__foot a {
  display: inline-block;
  padding: 16px 48px;
  background: var(--m-ink);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-decoration: none;
}
.hm-grid__foot p {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--m-mute);
  letter-spacing: 0.1em;
  margin: 14px 0 0;
}

/* ---------- Footer ---------- */
.hm-footer {
  background: var(--m-dark);
  color: #fff;
  padding: 80px 40px 32px;
  border-top: 1px solid rgba(255,255,255,0.1);
}
.hm-footer__grid {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.3fr 1fr 1fr 1fr;
  gap: 48px;
}
.hm-footer__brand p {
  font-size: 14px;
  line-height: 1.55;
  color: rgba(255,255,255,0.6);
  margin: 16px 0 20px;
  max-width: 32ch;
}
.hm-footer__newsletter {
  display: flex;
  gap: 0;
  border: 1px solid rgba(255,255,255,0.3);
}
.hm-footer__newsletter input {
  flex: 1;
  padding: 12px 14px;
  background: transparent;
  border: 0;
  font-family: var(--font);
  font-size: 13px;
  color: #fff;
  outline: none;
}
.hm-footer__newsletter input::placeholder { color: rgba(255,255,255,0.4); }
.hm-footer__newsletter button {
  background: #fff;
  color: var(--m-dark);
  border: 0;
  padding: 0 18px;
  font-family: var(--font);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
}
.hm-footer__col h6 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.5);
  margin: 0 0 18px;
}
.hm-footer__col ul {
  list-style: none;
  margin: 0; padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.hm-footer__col a {
  color: rgba(255,255,255,0.7);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.15s;
}
.hm-footer__col a:hover { color: #fff; }
.hm-footer__bottom {
  max-width: 1280px;
  margin: 0 auto;
  padding-top: 32px;
  margin-top: 56px;
  border-top: 1px solid rgba(255,255,255,0.12);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: rgba(255,255,255,0.4);
}
.hm-footer__bottom a { color: rgba(255,255,255,0.5); text-decoration: none; }
.hm-footer__bottom a:hover { color: #fff; }
.hm-footer__legal {
  display: flex;
  gap: 16px;
}

/* ---------- Mobile ---------- */
@media (max-width: 900px) {
  .hm-header__nav { display: none; }
  .hm-header__inner { padding: 0 20px; }
  .hm-grid { padding: 48px 24px; }
  .hm-grid__products { grid-template-columns: 1fr 1fr; }
  .hm-footer__grid { grid-template-columns: 1fr 1fr; gap: 32px; }
  .hm-footer__bottom { flex-direction: column; gap: 12px; text-align: center; }
}
@media (max-width: 600px) {
  .hm-grid__products { grid-template-columns: 1fr; }
  .hm-footer__grid { grid-template-columns: 1fr; }
  .hm-ticker__slide { font-size: 11px; letter-spacing: 0.04em; }
}

---

## JavaScript Configuration (from home-tweaks.jsx)

/* global React, ReactDOM */
const { useEffect } = React;

const HOME_TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "variantCta": "always",
  "featuredTiles": "compare-color",
  "articleHero": "image-overlay"
}/*EDITMODE-END*/;

function HomeTweaks() {
  const [t, setTweak] = useTweaks(HOME_TWEAK_DEFAULTS);

  useEffect(() => {
    const root = document.documentElement;
    root.dataset.variantCta = t.variantCta;
    root.dataset.featuredTiles = t.featuredTiles;
    root.dataset.articleHero = t.articleHero;
  }, [t]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Variant cards · CTA">
        <TweakRadio
          label="Add to cart"
          value={t.variantCta}
          onChange={v => setTweak('variantCta', v)}
          options={[
            { value: 'off',    label: 'Off' },
            { value: 'link',   label: 'Text link' },
            { value: 'hover',  label: 'On hover' },
            { value: 'always', label: 'Always' },
          ]}
        />
      </TweakSection>

      <TweakSection label="Featured tile strip">
        <TweakSelect
          label="Combo"
          value={t.featuredTiles}
          onChange={v => setTweak('featuredTiles', v)}
          options={[
            { value: 'compare-color', label: 'Compare open/closed + Featured color' },
            { value: 'yoga-color',    label: 'Yoga pant + Featured color' },
            { value: 'le-color',      label: 'Limited edition + Featured color' },
            { value: 'compare-yoga',  label: 'Compare + Yoga pant' },
          ]}
        />
      </TweakSection>

      <TweakSection label="Article hero">
        <TweakRadio
          label="Style"
          value={t.articleHero}
          onChange={v => setTweak('articleHero', v)}
          options={[
            { value: 'image-overlay', label: 'A · Image' },
            { value: 'centered',      label: 'B · Centered' },
          ]}
        />
      </TweakSection>
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('home-tweaks-root')).render(<HomeTweaks />);

---

## VERSION HISTORY & SUPERSEDED SPECIFICATIONS

The following versions represent the design evolution. Earlier versions are superseded by Matured specification above.

### Version 10 (Penultimate Release)

<!DOCTYPE html>
<!-- saved from url=(0058)file:///Users/andrewnehra/Downloads/Barreletics_v28_1.html -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Barreletics performance skins — the grip shoe that outperforms grip socks in barre, reformer Pilates, Lagree and Megaformer. 360° grip, no latex, no silicone. Trusted by 1,000+ instructors. Made in USA.">
<title>Barreletics — Home v10 · A New Kind of Grip Shoe</title>
<link rel="icon" type="image/png" href="barreletics-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com/">
<link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ============================================================
   Barreletics Design Audit — Stylesheet
   Pulls tokens directly from /config/settings_data.json
   ============================================================ */

:root {
  /* Brand color tokens — calibrated to the LIVE site, not the unused settings.
     The header & footer render --colorNav from --colorBody (#fff) per
     snippets/css-variables.liquid, so the cream + plum in settings_data.json
     is dead code. The real palette is: white, ink, light-grey, coral accent. */
  --br-bg:           #ffffff;
  --br-alt-bg:       #f9f9f9;
  --br-alt-bg-2:     #f3f3f3;   /* the slightly deeper grey used in br-media-text-split */
  --br-text:         #050505;
  --br-text-soft:    #4a4a4a;
  --br-text-mute:    #8a8a8a;
  --br-line:         #e6e6e6;
  --br-line-soft:    #efefef;

  /* WARM ACCENT — restrained to cart badge ONLY (matches live site).
     Stars use gold. Sale uses ink. CTAs are black-on-white.
     The earlier f93820 was too aggressive — live site uses coral on cart only. */
  --br-accent:       #f97250;   /* cart badge ONLY — restraint is the point */
  --br-accent-hover: #e85e3c;
  --br-coral:        var(--br-accent);   /* alias */
  --br-sale:         var(--br-text);     /* sale price is just ink-bold, not red */
  --br-star:         #fbc02d;             /* gold star color */
  --br-info:         #3a8de8;             /* sale banner blue + LE chip */
  --br-le:           #3a8de8;
  --br-le-bg:        #eaf3fc;

  --br-button:       #050505;
  --br-button-text:  #ffffff;

  /* Audit accents (only used in audit chrome, NOT in mock components) */
  --au-bg:           #fafaf7;
  --au-card:         #ffffff;
  --au-flag:         #c43d2a;
  --au-flag-bg:      #fdf0ec;
  --au-ok:           #1f6f4a;
  --au-ok-bg:        #ecf6f0;
  --au-note:         #6b5b3a;
  --au-note-bg:      #fbf5e6;

  /* Typography system — PROPOSED (one family, one ramp) */
  --t-font: 'Roboto', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;

  --t-eyebrow:      12px;   /* uppercase, 0.08em, 600 */
  --t-body-sm:      14px;
  --t-body:         16px;
  --t-body-lg:      18px;
  --t-h6:           18px;
  --t-h5:           22px;
  --t-h4:           28px;
  --t-h3:           36px;
  --t-h2:           44px;
  --t-h1:           56px;
  --t-display:      72px;

  /* Mobile clamps applied via clamp() on hero/display only */
  --t-h1-mobile:    36px;
  --t-display-mobile: 44px;

  /* Spacing scale */
  --sp-1: 4px;
  --sp-2: 8px;
  --sp-3: 12px;
  --sp-4: 16px;
  --sp-5: 24px;
  --sp-6: 32px;
  --sp-7: 48px;
  --sp-8: 64px;
  --sp-9: 96px;
  --sp-10: 128px;

  /* Buttons — ONE primary, ONE secondary, ONE tertiary, no more */
  --btn-text-size:   14px;
  --btn-pad-y:       14px;
  --btn-pad-x:       28px;
  --btn-radius:      0px;       /* matches "button_style":"square" */
  --btn-letter:      0.06em;
  --btn-weight:      600;
}

/* ============================================================ */

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  font-family: var(--t-font);
  font-size: var(--t-body);
  line-height: 1.55;
  color: var(--br-text);
  background: var(--au-bg);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-wrap: pretty;
}

img, video { max-width: 100%; display: block; }

/* ---------- Audit chrome ---------- */

.au-nav {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(250, 250, 247, 0.92);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--br-line);
}

.au-nav__inner {
  max-width: 1320px;
  margin: 0 auto;
  padding: 14px 28px;
  display: flex;
  align-items: center;
  gap: 32px;
}

.au-nav__brand {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-accent);
  white-space: nowrap;
}

.au-nav__brand span {
  font-weight: 400;
  letter-spacing: 0.1em;
  color: var(--br-text-soft);
  margin-left: 10px;
}

.au-nav__links {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.au-nav__links a {
  color: var(--br-text-soft);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  padding-bottom: 2px;
  transition: color 0.15s, border-color 0.15s;
}

.au-nav__links a:hover { color: var(--br-text); border-color: var(--br-text); }

.au-nav__meta {
  margin-left: auto;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  white-space: nowrap;
}

/* ---------- Document wrapper ---------- */

.au-doc {
  max-width: 1320px;
  margin: 0 auto;
  padding: 64px 28px 160px;
}

.au-section {
  padding-top: 80px;
  margin-top: -1px;
}

.au-section + .au-section {
  border-top: 1px solid var(--br-line);
  padding-top: 80px;
  margin-top: 80px;
}

.au-kicker {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--br-accent);
  margin: 0 0 14px;
}

.au-h1 {
  font-size: clamp(40px, 5vw, 64px);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: -0.02em;
  margin: 0 0 24px;
  max-width: 18ch;
}

.au-h2 {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 500;
  line-height: 1.15;
  letter-spacing: -0.01em;
  margin: 0 0 16px;
  max-width: 22ch;
}

.au-h3 {
  font-size: 22px;
  font-weight: 600;
  line-height: 1.25;
  margin: 0 0 12px;
}

.au-lede {
  font-size: 19px;
  line-height: 1.55;
  color: var(--br-text-soft);
  max-width: 62ch;
  margin: 0 0 16px;
}

.au-body {
  font-size: 16px;
  line-height: 1.6;
  color: var(--br-text-soft);
  max-width: 62ch;
}

.au-body + .au-body { margin-top: 12px; }

.au-rule {
  height: 1px;
  background: var(--br-line);
  border: 0;
  margin: 48px 0;
}

/* ---------- Cover ---------- */

.au-cover {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 64px;
  align-items: end;
  padding: 80px 0 64px;
  border-bottom: 1px solid var(--br-line);
}

.au-cover__meta {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-bottom: 6px;
}

.au-cover__stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 16px 18px;
  background: var(--au-card);
  border: 1px solid var(--br-line);
}

.au-cover__stat b {
  font-size: 32px;
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  color: var(--br-text);
}

.au-cover__stat span {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
}

.au-cover__stat--flag b { color: var(--au-flag); }

@media (max-width: 900px) {
  .au-cover { grid-template-columns: 1fr; gap: 40px; }
}

/* ---------- Findings cards ---------- */

.au-findings {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

@media (max-width: 800px) {
  .au-findings { grid-template-columns: 1fr; }
}

.au-finding {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.au-finding__head {
  display: flex;
  align-items: center;
  gap: 10px;
}

.au-finding__num {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--br-text-mute);
  text-transform: uppercase;
}

.au-finding__tag {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  padding: 4px 8px;
  background: var(--au-flag-bg);
  color: var(--au-flag);
}

.au-finding__tag--note { background: var(--au-note-bg); color: var(--au-note); }
.au-finding__tag--ok   { background: var(--au-ok-bg);   color: var(--au-ok); }

.au-finding h3 {
  font-size: 20px;
  font-weight: 500;
  margin: 0;
  line-height: 1.3;
}

.au-finding p {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
}

.au-finding__evidence {
  font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 11.5px;
  line-height: 1.6;
  background: #f5f4ee;
  border-left: 2px solid var(--au-flag);
  padding: 12px 14px;
  color: #2a2a2a;
  overflow-x: auto;
  white-space: pre-wrap;
}

/* ---------- Tokens table ---------- */

.au-tokens {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
}

.au-token {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-height: 130px;
}

.au-token__swatch {
  width: 100%;
  height: 56px;
  border: 1px solid rgba(0,0,0,0.06);
}

.au-token__name {
  font-size: 13px;
  font-weight: 600;
  color: var(--br-text);
}

.au-token__hex {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 11px;
  color: var(--br-text-mute);
  letter-spacing: 0.05em;
}

.au-token__usage {
  font-size: 11px;
  color: var(--br-text-soft);
  line-height: 1.4;
}

/* ---------- Type ramp ---------- */

.au-typeramp {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.au-typeramp__row {
  display: grid;
  grid-template-columns: 110px 80px 1fr;
  align-items: baseline;
  gap: 24px;
  padding-bottom: 14px;
  border-bottom: 1px dashed var(--br-line);
}

.au-typeramp__row:last-child { border-bottom: 0; padding-bottom: 0; }

.au-typeramp__label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  font-weight: 600;
}

.au-typeramp__meta {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  color: var(--br-text-mute);
}

.au-typeramp__sample { color: var(--br-text); }

/* ---------- Section catalog (the 8 sections) ---------- */

.au-catalog {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

@media (max-width: 1000px) { .au-catalog { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px)  { .au-catalog { grid-template-columns: 1fr; } }

.au-catalog__item {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-height: 220px;
}

.au-catalog__num {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--br-accent);
}

.au-catalog__item h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  line-height: 1.25;
}

.au-catalog__item p {
  margin: 0;
  font-size: 13px;
  line-height: 1.5;
  color: var(--br-text-soft);
}

.au-catalog__diagram {
  margin-top: auto;
  height: 60px;
  background: var(--au-bg);
  border: 1px solid var(--br-line-soft);
  display: grid;
  gap: 4px;
  padding: 4px;
}

/* ---------- Section mock wrapper ---------- */

.au-mock {
  background: var(--au-card);
  border: 1px solid var(--br-line);
  margin-top: 24px;
  overflow: hidden;
}

.au-mock__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 18px 24px;
  border-bottom: 1px solid var(--br-line);
  background: #fbfaf6;
}

.au-mock__title {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.au-mock__title b {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--br-accent);
}

.au-mock__title h3 {
  font-size: 22px;
  font-weight: 500;
  margin: 0;
  letter-spacing: -0.01em;
}

.au-mock__tabs {
  display: flex;
  gap: 0;
  border: 1px solid var(--br-line);
}

.au-mock__tab {
  appearance: none;
  background: transparent;
  border: 0;
  padding: 8px 16px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text-soft);
  cursor: pointer;
  border-right: 1px solid var(--br-line);
  font-family: var(--t-font);
}

.au-mock__tab:last-child { border-right: 0; }

.au-mock__tab[aria-selected="true"] {
  background: var(--br-text);
  color: #fff;
}

.au-mock__stage {
  background: var(--br-bg);
  padding: 0;
  position: relative;
}

.au-mock__panel { display: none; }
.au-mock__panel[data-active="true"] { display: block; }

.au-mock__notes {
  padding: 18px 24px;
  background: #fbfaf6;
  border-top: 1px solid var(--br-line);
  font-size: 13px;
  line-height: 1.55;
  color: var(--br-text-soft);
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
}

.au-mock__notes b { color: var(--br-text); font-weight: 600; }

.au-mock__note-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.au-mock__note-item::before {
  content: "";
  width: 6px;
  height: 6px;
  background: var(--br-coral);
  border-radius: 50%;
  flex-shrink: 0;
}

/* ============================================================
   COMPONENT TOKENS (used inside section mocks — must look like
   the LIVE site after normalization)
   ============================================================ */

.br {
  font-family: var(--t-font);
  color: var(--br-text);
  background: var(--br-bg);
}

.br * { box-sizing: border-box; }

.br-eyebrow {
  font-size: var(--t-eyebrow);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--br-accent);
  margin: 0 0 12px;
  line-height: 1.3;
}

.br-display {
  font-size: clamp(var(--t-display-mobile), 5.4vw, var(--t-display));
  line-height: 1;
  font-weight: 400;
  letter-spacing: -0.02em;
  margin: 0;
}

.br-h1 {
  font-size: clamp(var(--t-h1-mobile), 4vw, var(--t-h1));
  line-height: 1.05;
  font-weight: 400;
  letter-spacing: -0.015em;
  margin: 0;
}

.br-h2 {
  font-size: clamp(28px, 2.6vw, var(--t-h2));
  line-height: 1.1;
  font-weight: 500;
  letter-spacing: -0.01em;
  margin: 0;
}

.br-h3 {
  font-size: var(--t-h3);
  line-height: 1.15;
  font-weight: 500;
  letter-spacing: -0.005em;
  margin: 0;
}

.br-h4 {
  font-size: var(--t-h4);
  line-height: 1.2;
  font-weight: 500;
  margin: 0;
}

.br-h5 {
  font-size: var(--t-h5);
  line-height: 1.3;
  font-weight: 500;
  margin: 0;
}

.br-body {
  font-size: var(--t-body);
  line-height: 1.6;
  margin: 0;
  color: var(--br-text);
}

.br-body-lg {
  font-size: var(--t-body-lg);
  line-height: 1.55;
  margin: 0;
  color: var(--br-text);
}

.br-body-sm {
  font-size: var(--t-body-sm);
  line-height: 1.5;
  margin: 0;
}

/* Buttons */
.br-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: var(--t-font);
  font-size: var(--btn-text-size);
  font-weight: var(--btn-weight);
  letter-spacing: var(--btn-letter);
  text-transform: uppercase;
  padding: var(--btn-pad-y) var(--btn-pad-x);
  border-radius: var(--btn-radius);
  text-decoration: none;
  border: 1px solid transparent;
  cursor: pointer;
  transition: opacity 0.15s, background-color 0.15s, color 0.15s;
  line-height: 1;
}

.br-btn:hover { opacity: 0.88; }

.br-btn--primary {
  background: var(--br-button);
  color: var(--br-button-text);
  border-color: var(--br-button);
}

.br-btn--secondary {
  background: transparent;
  color: var(--br-text);
  border-color: var(--br-text);
}

.br-btn--tertiary {
  background: transparent;
  color: var(--br-text);
  border-color: transparent;
  padding-left: 0;
  padding-right: 0;
  border-bottom: 1px solid var(--br-text);
  border-radius: 0;
}

.br-btn--invert {
  background: #ffffff;
  color: var(--br-text);
  border-color: #ffffff;
}

.br-btn--on-image {
  background: transparent;
  color: #ffffff;
  border-color: #ffffff;
}

.br-btn--lg { font-size: 15px; padding: 16px 32px; }
.br-btn--sm { font-size: 12px; padding: 10px 20px; }

/* Section helpers */
.br-section {
  padding: var(--sp-9) var(--sp-5);
}
.br-section--tight { padding: var(--sp-7) var(--sp-5); }

.br-container { max-width: 1280px; margin: 0 auto; }
.br-container--narrow { max-width: 880px; margin: 0 auto; }

.br-grid { display: grid; }
.br-flex { display: flex; }

/* Image placeholder */
.br-img {
  background:
    repeating-linear-gradient(
      135deg,
      #efece2 0 16px,
      #e8e4d6 16px 32px
    );
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.05em;
  text-align: center;
  padding: 12px;
  text-transform: lowercase;
}

.br-img--dark {
  background:
    repeating-linear-gradient(
      135deg,
      #2c2c2c 0 16px,
      #232323 16px 32px
    );
  color: #b5b0a1;
}

.br-img--blush {
  background:
    repeating-linear-gradient(
      135deg,
      #f3e3dc 0 16px,
      #efdcd2 16px 32px
    );
  color: #9c7464;
}

.br-img--ink {
  background:
    repeating-linear-gradient(
      135deg,
      #1f1f1f 0 16px,
      #161616 16px 32px
    );
  color: #888;
}

/* Why-it-works strip (canonical) */
.br-why-strip {
  background: var(--br-alt-bg);
  display: flex;
  align-items: stretch;
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
  width: 100%;
  -webkit-font-smoothing: antialiased;
}
.br-why-strip__label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--br-text);
  white-space: nowrap;
  padding: 14px 22px;
  background: #ffffff;
  border-right: 1px solid var(--br-line);
}
.br-why-strip__pts {
  display: flex;
  flex: 1;
  justify-content: space-between;
  align-items: center;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
  padding: 14px 22px;
  gap: 10px;
}
.br-why-strip__div {
  width: 1px;
  height: 12px;
  background: var(--br-line);
  flex-shrink: 0;
}

/* ============================================================
   Section: Header (chrome)
   ============================================================ */

.br-header {
  background: var(--br-bg);
  color: var(--br-text);
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 18px 32px;
  border-bottom: 1px solid var(--br-line);
}

.br-header__nav {
  display: flex;
  gap: 28px;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-weight: 500;
}

.br-header__logo {
  font-size: 22px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 400;
}

.br-header__util {
  justify-self: end;
  display: flex;
  gap: 18px;
  align-items: center;
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.br-header__cart {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  position: relative;
}

.br-header__cart-dot {
  width: 8px; height: 8px;
  background: var(--br-coral);
  border-radius: 50%;
}

/* Announcement strip */
.br-announce {
  background: var(--br-text);
  color: #fff;
  text-align: center;
  font-size: 11.5px;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  padding: 9px 16px;
  font-weight: 500;
}

/* ============================================================
   Footer
   ============================================================ */

.br-footer {
  background: var(--br-bg);
  color: var(--br-text);
  padding: 80px 32px 32px;
  border-top: 1px solid var(--br-line);
}

.br-footer__grid {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.4fr repeat(4, 1fr);
  gap: 48px;
  padding-bottom: 64px;
  border-bottom: 1px solid var(--br-line);
}

@media (max-width: 800px) {
  .br-footer__grid { grid-template-columns: 1fr 1fr; gap: 32px; }
}

.br-footer__col h6 {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-weight: 600;
  margin: 0 0 18px;
  opacity: 0.7;
}

.br-footer__col ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.br-footer__col a {
  color: var(--br-text);
  text-decoration: none;
  font-size: 14px;
  border-bottom: 1px solid transparent;
}

.br-footer__col a:hover { border-color: currentColor; }

.br-footer__brand .br-header__logo { color: var(--br-text); }

.br-footer__bottom {
  max-width: 1280px;
  margin: 0 auto;
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  opacity: 0.7;
  flex-wrap: wrap;
  gap: 16px;
}
/* ============================================================
   PDP pixel-final stylesheet
   Inherits all tokens from audit-styles.css
   ============================================================ */

html, body { background: #ffffff; }

/* ---------- Announcement + header ---------- */

/* ============================================================
   ROTATING TICKER — single strip, messages cross-fade
   ============================================================ */
.pdp-ticker {
  background: var(--br-text);
  color: #fff;
  height: 36px;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.pdp-ticker__slide {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0 16px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.55s ease, transform 0.55s ease;
  white-space: nowrap;
}
.pdp-ticker__slide.is-active {
  opacity: 1;
  transform: translateY(0);
}
.pdp-ticker__slide b { font-weight: 700; }
.pdp-ticker__slide a {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.6);
  padding-bottom: 1px;
  margin-left: 6px;
}
.pdp-ticker__slide a:hover { color: #fff; border-color: #fff; }

@media (max-width: 600px) {
  .pdp-ticker__slide { font-size: 11px; letter-spacing: 0.08em; }
}

.pdp-announce {
  background: var(--br-text);
  color: #fff;
  text-align: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 11px 16px;
}

.pdp-announce--sale {
  background: var(--br-info);
  color: #fff;
  letter-spacing: 0.12em;
  font-weight: 600;
}
.pdp-announce--sale b { font-weight: 700; }

.pdp-announce--info {
  background: #fafafa;
  color: var(--br-text);
  font-weight: 500;
  font-size: 11.5px;
  border-bottom: 1px solid var(--br-line);
}
.pdp-announce--info a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  margin-left: 6px;
  font-weight: 500;
}
.pdp-announce--info a:hover { opacity: 0.7; }

.pdp-header {
  position: sticky;
  top: 0;
  z-index: 30;
  background: #ffffff;
  border-bottom: 1px solid var(--br-line);
}

.pdp-header__inner {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 18px 32px;
  gap: 24px;
}

.pdp-header__nav {
  display: flex;
  gap: 30px;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.01em;
}
.pdp-header__nav a {
  color: var(--br-text);
  text-decoration: none;
  padding: 4px 0;
  border-bottom: 1px solid transparent;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.pdp-header__nav a:hover { border-color: var(--br-text); }
.pdp-header__chev {
  font-size: 12px;
  line-height: 1;
  display: inline-block;
  margin-top: -1px;
  opacity: 0.7;
}

.pdp-header__logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 200px;
  height: 38px;
  padding: 0 8px;
  text-decoration: none;
}
.pdp-header__logo img {
  display: block;
  height: 100%;
  width: auto;
}
.pdp-header__logo--placeholder {
  border: 1px dashed var(--br-line);
  background: rgba(0,0,0,0.015);
  padding: 0 16px;
}
.pdp-header__logo span {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 10.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-mute);
  text-transform: lowercase;
}

.pdp-header__util {
  display: flex;
  gap: 24px;
  justify-content: flex-end;
  align-items: center;
  font-size: 13px;
  font-weight: 500;
}
.pdp-header__util a {
  color: var(--br-text);
  text-decoration: none;
  position: relative;
}
.pdp-header__cart {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.pdp-header__cart-dot {
  width: 24px; height: 24px;
  background: var(--br-accent);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0;
}
.pdp-header__cart-dot::before {
  content: "0";
}

/* ---------- Crumb ---------- */
.pdp-crumb {
  max-width: 1440px;
  margin: 0 auto;
  padding: 18px 32px 0;
  font-size: 11.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text-mute);
}
.pdp-crumb a { color: inherit; text-decoration: none; }
.pdp-crumb a:hover { color: var(--br-text); }

/* ============================================================
   PDP MAIN — gallery + buy box
   ============================================================ */

.pdp-main {
  max-width: 1440px;
  margin: 0 auto;
  padding: 32px 32px 80px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: flex-start;
}

@media (max-width: 1000px) {
  .pdp-main { grid-template-columns: 1fr; gap: 32px; }
}

/* Gallery */
.pdp-gallery {
  display: grid;
  grid-template-columns: 88px 1fr;
  gap: 12px;
  position: sticky;
  top: 88px;
}
@media (max-width: 700px) {
  .pdp-gallery { grid-template-columns: 1fr; position: static; }
  .pdp-gallery__thumbs { display: flex; flex-direction: row; }
}

.pdp-gallery__thumbs {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pdp-gallery__thumb {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 10px, #e8e4d6 10px 20px);
  border: 1px solid transparent;
  cursor: pointer;
  position: relative;
}
.pdp-gallery__thumb[aria-selected="true"] { border-color: var(--br-text); }
.pdp-gallery__thumb--blush {
  background:
    repeating-linear-gradient(135deg, #f3e3dc 0 10px, #efdcd2 10px 20px);
}
.pdp-gallery__thumb--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 10px, #232323 10px 20px);
}
.pdp-gallery__thumb--video::after {
  content: "▶";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 16px;
  color: rgba(255,255,255,0.8);
}

.pdp-gallery__hero {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  color: #8a7e63;
  position: relative;
}
.pdp-gallery__zoom {
  position: absolute;
  bottom: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  background: rgba(255,255,255,0.9);
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 16px;
  color: var(--br-text);
}

/* Buy box */
.pdp-buy {
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding-top: 6px;
}

.pdp-buy__judge {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--br-text-soft);
}
.pdp-buy__stars {
  color: var(--br-accent);
  letter-spacing: 0.16em;
}
.pdp-buy__judge a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  font-weight: 500;
}

.pdp-buy__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  margin: 0;
}

.pdp-buy__name {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 400;
  margin: 0;
  letter-spacing: -0.015em;
  line-height: 1.1;
}

/* v2 — Brand-line dominant hierarchy */
.pdp-buy__seo-label {
  font-size: 16px;
  font-weight: 500;
  letter-spacing: -0.005em;
  color: var(--br-text);
  margin: 6px 0 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--br-line);
  line-height: 1.3;
}

.pdp-buy__name--brand {
  font-size: clamp(34px, 3.8vw, 52px);
  font-weight: 400;
  line-height: 1;
  letter-spacing: -0.02em;
}
.pdp-buy__seo {
  font-size: 15px;
  line-height: 1.4;
  color: var(--br-text-soft);
  margin: 14px 0 0;
  max-width: 50ch;
  font-weight: 400;
}

.pdp-buy__tagline {
  font-size: clamp(17px, 1.6vw, 20px);
  font-weight: 500;
  color: var(--br-text);
  margin: 10px 0 0;
  letter-spacing: -0.005em;
  line-height: 1.3;
}

.pdp-buy__sub {
  font-size: 15px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
  max-width: 50ch;
}

.pdp-buy__price {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-top: 4px;
}
.pdp-buy__price-now {
  font-size: 22px;
  font-weight: 500;
}
.pdp-buy__price-meta {
  font-size: 12.5px;
  color: var(--br-text-soft);
  letter-spacing: 0.04em;
}

.pdp-buy__row { display: flex; flex-direction: column; gap: 10px; }
.pdp-buy__row-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
}
.pdp-buy__row-head a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  font-weight: 500;
}

.pdp-buy__swatches {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.pdp-buy__swatch {
  width: 36px;
  height: 36px;
  border: 1px solid var(--br-line);
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  transition: border-color 0.12s, transform 0.12s;
}
.pdp-buy__swatch:hover { transform: scale(1.06); }
.pdp-buy__swatch[aria-selected="true"] {
  border-color: var(--br-text);
  box-shadow: inset 0 0 0 2px #fff;
}
.pdp-buy__swatch[data-le]::after {
  content: "LE";
  position: absolute;
  top: -8px; right: -8px;
  background: var(--br-le);
  color: #fff;
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 2px 5px 1px;
  border-radius: 2px;
}

.pdp-buy__sizes {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 6px;
}
.pdp-buy__sizes--two {
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.pdp-buy__size {
  border: 1px solid var(--br-text);
  background: #fff;
  padding: 12px 4px;
  text-align: center;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.12s, color 0.12s;
}
.pdp-buy__size--wide {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 16px 12px;
}
.pdp-buy__size-letter {
  font-size: 22px;
  font-weight: 500;
  letter-spacing: 0.04em;
  line-height: 1;
}
.pdp-buy__size-meta {
  font-size: 11px;
  letter-spacing: 0.04em;
  color: var(--br-text-soft);
  text-transform: none;
}
.pdp-buy__size--wide[aria-selected="true"] .pdp-buy__size-meta {
  color: rgba(255,255,255,0.78);
}
.pdp-buy__size:hover { background: var(--br-text); color: #fff; }
.pdp-buy__size[aria-selected="true"] { background: var(--br-text); color: #fff; }
.pdp-buy__size[disabled] {
  opacity: 0.34;
  color: var(--br-text-mute);
  border-color: var(--br-line);
  text-decoration: line-through;
  cursor: not-allowed;
}
.pdp-buy__size[disabled]:hover { background: transparent; color: var(--br-text-mute); }

.pdp-buy__cta-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-buy__cta {
  background: var(--br-text);
  color: #fff;
  border: 0;
  padding: 18px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: opacity 0.15s;
  text-align: center;
}
.pdp-buy__cta:hover { opacity: 0.88; }

.pdp-buy__shipnote {
  display: flex;
  gap: 16px;
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  flex-wrap: wrap;
}
.pdp-buy__shipnote span::before {
  content: "✓ ";
  color: var(--br-accent);
  margin-right: 2px;
  font-weight: 700;
}

.pdp-buy__tabs {
  border-top: 1px solid var(--br-line);
  margin-top: 4px;
}
.pdp-buy__tab {
  border-bottom: 1px solid var(--br-line);
}
.pdp-buy__tab summary {
  list-style: none;
  cursor: pointer;
  padding: 16px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.06em;
}
.pdp-buy__tab summary::-webkit-details-marker { display: none; }
.pdp-buy__tab summary::after {
  content: "+";
  font-weight: 300;
  font-size: 22px;
  color: var(--br-text-mute);
  transition: transform 0.15s;
}
.pdp-buy__tab[open] summary::after {
  content: "−";
}
.pdp-buy__tab-body {
  padding: 0 0 18px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--br-text-soft);
}
.pdp-buy__tab-body p { margin: 0 0 10px; }
.pdp-buy__tab-body p:last-child { margin-bottom: 0; }

/* ============================================================
   PILLAR STRIP
   ============================================================ */

.pdp-pillars {
  background: var(--br-alt-bg);
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
}
.pdp-pillars__inner {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  align-items: stretch;
}
.pdp-pillars__label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-text);
  white-space: nowrap;
  padding: 18px 28px;
  background: #fff;
  border-right: 1px solid var(--br-line);
  display: flex;
  align-items: center;
}
.pdp-pillars__pts {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 32px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  gap: 20px;
}
.pdp-pillars__div {
  width: 1px;
  height: 14px;
  background: var(--br-line);
}

@media (max-width: 800px) {
  .pdp-pillars__label { display: none; }
  .pdp-pillars__pts {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    font-size: 10.5px;
    text-align: center;
  }
  .pdp-pillars__div { display: none; }
}

/* ============================================================
   SECTION HELPERS
   ============================================================ */

.pdp-section {
  max-width: 1440px;
  margin: 0 auto;
  padding: 96px 32px;
}
.pdp-section--tight { padding: 64px 32px; }
.pdp-section--alt { background: var(--br-alt-bg); max-width: none; }
.pdp-section--alt > * {
  max-width: 1440px;
  margin-left: auto;
  margin-right: auto;
}

.pdp-eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  margin: 0 0 14px;
}

.pdp-h2 {
  font-size: clamp(28px, 3.2vw, 44px);
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.1;
  margin: 0;
  text-wrap: balance;
}

.pdp-h3 {
  font-size: clamp(20px, 1.6vw, 24px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.2;
  margin: 0;
}

.pdp-lede {
  font-size: 18px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 16px 0 0;
  max-width: 60ch;
}

/* ============================================================
   PREMIUM / VALUE BLOCK — addresses the "expensive" objection
   ============================================================ */

.pdp-value {
  background: var(--br-text);
  color: #fff;
}
.pdp-value__inner {
  max-width: 1440px;
  margin: 0 auto;
  padding: 96px 32px;
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 64px;
  align-items: center;
}
@media (max-width: 900px) {
  .pdp-value__inner { grid-template-columns: 1fr; padding: 64px 24px; gap: 32px; }
}

.pdp-value__copy .pdp-eyebrow { color: rgba(255,255,255,0.7); }
.pdp-value__copy .pdp-h2 { color: #fff; }
.pdp-value__copy .pdp-lede { color: rgba(255,255,255,0.78); }

.pdp-value__compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.12);
}
.pdp-value__col {
  padding: 26px 24px;
  background: var(--br-text);
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-value__col--ours { background: #1a1a1a; }
.pdp-value__tag {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.6);
}
.pdp-value__col--ours .pdp-value__tag { color: var(--br-accent); }
.pdp-value__amount {
  font-size: clamp(28px, 3vw, 38px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1;
  color: #fff;
  margin: 4px 0 12px;
}
.pdp-value__amount-unit {
  font-size: 13px;
  font-weight: 400;
  color: rgba(255,255,255,0.55);
  letter-spacing: 0;
  margin-left: 4px;
}
.pdp-value__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 13.5px;
  color: rgba(255,255,255,0.78);
}
.pdp-value__list li {
  position: relative;
  padding-left: 16px;
}
.pdp-value__list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 1px;
  background: rgba(255,255,255,0.4);
}
.pdp-value__col--ours .pdp-value__list li::before {
  background: var(--br-accent);
}

/* ============================================================
   BENEFIT GRID — PDP variant
   ============================================================ */

.pdp-benefits {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 48px;
}
@media (max-width: 800px) {
  .pdp-benefits { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 520px) {
  .pdp-benefits { grid-template-columns: 1fr; }
}

.pdp-benefit {
  background: #fff;
  border-top: 2px solid var(--br-text);
  padding: 22px 22px 26px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pdp-benefit__num {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  margin-bottom: 8px;
}
.pdp-benefit__title {
  font-size: 17px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.005em;
}
.pdp-benefit__sub {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
}

/* ============================================================
   MEDIA SPLIT (story block)
   ============================================================ */

.pdp-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  min-height: 580px;
}
@media (max-width: 900px) {
  .pdp-split { grid-template-columns: 1fr; min-height: 0; }
}

.pdp-split__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  min-height: 100%;
  position: relative;
}
.pdp-split__media--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 18px, #232323 18px 36px);
  color: #a39a83;
}
.pdp-split__media-tag {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(0,0,0,0.5);
  color: #fff;
  padding: 5px 9px;
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 0;
}

.pdp-split__copy {
  padding: 80px 64px;
  background: var(--br-alt-bg);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
@media (max-width: 900px) {
  .pdp-split__copy { padding: 48px 24px; }
  .pdp-split__media { aspect-ratio: 4/5; }
}
.pdp-split__copy .pdp-h2 { margin-bottom: 16px; }

.pdp-split__list {
  list-style: none;
  margin: 28px 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 15px;
}
.pdp-split__list li {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.pdp-split__list li::before {
  content: "→";
  color: var(--br-accent);
  font-weight: 700;
  flex-shrink: 0;
}

/* ============================================================
   TESTIMONIAL
   ============================================================ */

.pdp-quote {
  text-align: center;
  max-width: 760px;
  margin: 0 auto;
}
.pdp-quote__stars {
  color: var(--br-accent);
  letter-spacing: 0.2em;
  font-size: 18px;
  margin-bottom: 22px;
}
.pdp-quote__body {
  font-size: clamp(22px, 2.4vw, 32px);
  font-weight: 400;
  line-height: 1.35;
  margin: 0 0 24px;
  text-wrap: balance;
  letter-spacing: -0.005em;
  color: var(--br-text);
}
.pdp-quote__attr {
  font-size: 11.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pdp-quote__attr b {
  color: var(--br-text);
  font-weight: 700;
  margin-right: 8px;
}

/* ============================================================
   VARIANT GRID — "Shop all colors & sizes"
   ============================================================ */

.pdp-variants__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}
.pdp-variants__head-meta { display: flex; flex-direction: column; gap: 4px; }
.pdp-variants__head-link {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
}

.pdp-variants__tabs {
  display: flex;
  gap: 0;
  margin-bottom: 28px;
}
.pdp-variant-tab {
  font-family: inherit;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.04em;
  padding: 12px 22px;
  border: 1px solid var(--br-text);
  background: #fff;
  color: var(--br-text);
  cursor: pointer;
  margin: 0 -1px 0 0;
  position: relative;
  transition: background 0.12s, color 0.12s;
}
.pdp-variant-tab[aria-selected="true"] {
  background: var(--br-text);
  color: #fff;
  z-index: 2;
}
.pdp-variant-tab:hover:not([aria-selected="true"]) {
  background: var(--br-alt-bg);
}

.pdp-variants__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 1000px) { .pdp-variants__grid { grid-template-columns: repeat(2, 1fr); } }

.pdp-vcard {
  background: #fff;
  display: flex;
  flex-direction: column;
  position: relative;
  cursor: pointer;
}
.pdp-vcard__media {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  margin-bottom: 14px;
  position: relative;
  overflow: hidden;
}
.pdp-vcard__media--blush {
  background: repeating-linear-gradient(135deg, #f3e3dc 0 14px, #efdcd2 14px 28px);
}
.pdp-vcard__media--stone {
  background: repeating-linear-gradient(135deg, #d4d0c4 0 14px, #c9c5b8 14px 28px);
}
.pdp-vcard__media--dark {
  background: repeating-linear-gradient(135deg, #2c2c2c 0 14px, #232323 14px 28px);
}
.pdp-vcard__le {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--br-le);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 4px 8px 3px;
}
.pdp-vcard__quick {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  background: rgba(255,255,255,0.96);
  color: var(--br-text);
  padding: 10px;
  text-align: center;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  opacity: 0;
  transition: opacity 0.15s;
}
.pdp-vcard:hover .pdp-vcard__quick { opacity: 1; }

.pdp-vcard__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
  line-height: 1.35;
}
.pdp-vcard__meta {
  font-size: 12px;
  color: var(--br-text-soft);
  letter-spacing: 0.02em;
}
.pdp-vcard__price {
  font-size: 13px;
  font-weight: 500;
  margin-top: 2px;
}
.pdp-vcard__sale {
  color: var(--br-accent);
  font-weight: 500;
}
.pdp-vcard__sale s {
  color: var(--br-text-mute);
  text-decoration: line-through;
  font-weight: 400;
  margin-right: 4px;
}

/* ============================================================
   REVIEWS (Judge.me restyled)
   ============================================================ */

.pdp-reviews__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: 32px;
  gap: 24px;
  flex-wrap: wrap;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
}
.pdp-reviews__head-bigstars {
  font-size: 32px;
  color: var(--br-accent);
  letter-spacing: 0.18em;
  line-height: 1;
}
.pdp-reviews__head-summary {
  font-size: 14px;
  color: var(--br-text-soft);
  margin-top: 4px;
}
.pdp-reviews__head-summary b { color: var(--br-text); font-weight: 600; }

.pdp-reviews__grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0;
  border-top: 1px solid var(--br-line);
}
.pdp-review {
  padding: 24px 32px;
  border-bottom: 1px solid var(--br-line);
  border-right: 1px solid var(--br-line);
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.pdp-review:nth-child(2n) { border-right: 0; }
.pdp-review__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pdp-review__stars { color: var(--br-accent); letter-spacing: 0.16em; font-size: 13px; }
.pdp-review__verified {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.pdp-review__verified::before {
  content: "✓";
  color: var(--br-accent);
  font-weight: 700;
}
.pdp-review__title {
  font-size: 15px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.005em;
}
.pdp-review__body {
  font-size: 14px;
  line-height: 1.6;
  color: var(--br-text);
  margin: 0;
}
.pdp-review__attr {
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  margin: 0;
}
.pdp-review__attr b { color: var(--br-text); font-weight: 600; }

@media (max-width: 720px) {
  .pdp-reviews__grid { grid-template-columns: 1fr; }
  .pdp-review { border-right: 0; }
}

.pdp-reviews__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pdp-reviews__more {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 500;
}
.pdp-reviews__write {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  background: var(--br-text);
  color: #fff;
  padding: 12px 20px;
  font-weight: 700;
}
.pdp-reviews__write:hover { opacity: 0.88; }

/* ============================================================
   FAQ
   ============================================================ */

.pdp-faq {
  max-width: 880px;
  margin: 0 auto;
}
.pdp-faq__list {
  margin-top: 32px;
  border-top: 1px solid var(--br-line);
}
.pdp-faq__item {
  border-bottom: 1px solid var(--br-line);
}
.pdp-faq__item summary {
  list-style: none;
  cursor: pointer;
  padding: 22px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  font-size: 17px;
  font-weight: 500;
  letter-spacing: -0.005em;
}
.pdp-faq__item summary::-webkit-details-marker { display: none; }
.pdp-faq__item summary::after {
  content: "+";
  font-size: 24px;
  font-weight: 300;
  color: var(--br-text-mute);
  flex-shrink: 0;
}
.pdp-faq__item[open] summary::after { content: "−"; }
.pdp-faq__body {
  padding: 0 0 22px;
  font-size: 15px;
  line-height: 1.65;
  color: var(--br-text-soft);
  max-width: 64ch;
}
.pdp-faq__body p { margin: 0 0 12px; }
.pdp-faq__body p:last-child { margin-bottom: 0; }
.pdp-faq__body a {
  color: var(--br-text);
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  text-decoration: none;
}

/* ============================================================
   PRODUCT RAIL — pairs with your kit
   ============================================================ */

.pdp-rail__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: 32px;
  gap: 24px;
}
.pdp-rail__list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 900px) { .pdp-rail__list { grid-template-columns: 1fr 1fr; } }

.pdp-rail-card {
  background: #fff;
  display: flex;
  flex-direction: column;
}
.pdp-rail-card__media {
  aspect-ratio: 4/5;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  margin-bottom: 14px;
}
.pdp-rail-card__media--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 14px, #efdcd2 14px 28px); }
.pdp-rail-card__media--stone { background: repeating-linear-gradient(135deg, #d4d0c4 0 14px, #c9c5b8 14px 28px); }
.pdp-rail-card__media--dark  { background: repeating-linear-gradient(135deg, #2c2c2c 0 14px, #232323 14px 28px); }
.pdp-rail-card__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
}
.pdp-rail-card__price {
  font-size: 13px;
  color: var(--br-text-soft);
  margin: 0;
}

/* ============================================================
   Tweaks-controlled variants
   ============================================================ */

/* Quick Add legacy hover button kept for tweaks-panel testing only;
   the production default is the text-link .pdp-vcard__addlink */
.pdp-vcard__add {
  display: none !important;
}

/* Card style — bordered variant */
[data-card-style="bordered"] .pdp-vcard {
  border: 1px solid var(--br-line);
  padding: 12px;
  background: #fff;
  transition: border-color 0.15s;
}
[data-card-style="bordered"] .pdp-vcard:hover { border-color: var(--br-text); }
[data-card-style="bordered"] .pdp-vcard__media { margin-bottom: 12px; }

/* Verified badge toggle */
[data-verified="off"] .pdp-review__verified { display: none; }

/* CTA size variants */
[data-cta-size="compact"] .pdp-buy__cta { padding: 14px; font-size: 13px; }
[data-cta-size="bold"]    .pdp-buy__cta { padding: 22px; font-size: 15px; letter-spacing: 0.14em; }

/* ============================================================ */

.pdp-footer {
  background: #fff;
  border-top: 1px solid var(--br-line);
  padding: 80px 32px 32px;
}
.pdp-footer__grid {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.4fr repeat(4, 1fr);
  gap: 48px;
  padding-bottom: 56px;
  border-bottom: 1px solid var(--br-line);
}
@media (max-width: 900px) {
  .pdp-footer__grid { grid-template-columns: 1fr 1fr; gap: 32px; }
}
.pdp-footer__brand .pdp-header__logo {
  margin-bottom: 16px;
}
.pdp-footer__brand p {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  max-width: 32ch;
  margin: 0 0 20px;
}
.pdp-footer__newsletter {
  display: flex;
  gap: 0;
  border: 1px solid var(--br-text);
}
.pdp-footer__newsletter input {
  flex: 1;
  padding: 12px 14px;
  font-family: inherit;
  font-size: 13px;
  border: 0;
  background: transparent;
  color: var(--br-text);
}
.pdp-footer__newsletter input::placeholder { color: var(--br-text-mute); }
.pdp-footer__newsletter button {
  background: var(--br-text);
  color: #fff;
  border: 0;
  padding: 12px 16px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

.pdp-footer__col h6 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 18px;
  color: var(--br-text);
}
.pdp-footer__col ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-footer__col a {
  color: var(--br-text-soft);
  text-decoration: none;
  font-size: 14px;
}
.pdp-footer__col a:hover { color: var(--br-text); }

.pdp-footer__bottom {
  max-width: 1440px;
  margin: 0 auto;
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 12px;
  color: var(--br-text-mute);
  letter-spacing: 0.02em;
}
/* ============================================================
   pages-extras.css — components used on Home / Collection / Article / Blog
   that aren't already in pdp-styles.css
   ============================================================ */

/* ============== MEDIA SPLIT HERO (Home + Collection short hero) ============== */

.pg-hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 640px;
  background: var(--br-alt-bg);
  border-bottom: 1px solid var(--br-line);
}
.pg-hero-split--short { min-height: 380px; }
.pg-hero-split--reverse .pg-hero-split__media { order: 2; }

.pg-hero-split__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  min-height: 100%;
  position: relative;
}
.pg-hero-split__media--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 18px, #232323 18px 36px);
  color: #a39a83;
}
.pg-hero-split__media--blush {
  background:
    repeating-linear-gradient(135deg, #f3e3dc 0 18px, #efdcd2 18px 36px);
  color: #9c7464;
}
.pg-hero-split__media-tag {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(0,0,0,0.5);
  color: #fff;
  padding: 5px 10px;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.pg-hero-split__copy {
  padding: 96px 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: #ffffff;
}
.pg-hero-split--short .pg-hero-split__copy { padding: 56px 64px; }

.pg-hero-split__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-accent);
  margin: 0 0 14px;
}
.pg-hero-split__title {
  font-size: clamp(36px, 4.4vw, 60px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.02;
  margin: 0;
  max-width: 16ch;
  text-wrap: balance;
}
.pg-hero-split--short .pg-hero-split__title {
  font-size: clamp(28px, 3.2vw, 44px);
  max-width: 22ch;
}
.pg-hero-split__body {
  font-size: 17px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 18px 0 0;
  max-width: 48ch;
}
.pg-hero-split__ctas {
  display: flex;
  gap: 12px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pg-hero-split__cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
  border: 1px solid var(--br-text);
  background: var(--br-text);
  color: #fff;
  cursor: pointer;
  transition: opacity 0.15s, background 0.15s, color 0.15s;
}
.pg-hero-split__cta:hover { opacity: 0.88; }
.pg-hero-split__cta--secondary {
  background: transparent;
  color: var(--br-text);
  border-color: var(--br-text);
}

@media (max-width: 900px) {
  .pg-hero-split { grid-template-columns: 1fr; min-height: 0; }
  .pg-hero-split__media { aspect-ratio: 4/5; }
  .pg-hero-split__copy { padding: 48px 24px; }
  .pg-hero-split--short .pg-hero-split__copy { padding: 32px 24px; }
}

/* ============== COLLAB HERO (Home + Collection feature) ============== */

.pg-collab {
  position: relative;
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 20px, #232323 20px 40px);
  min-height: 560px;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}
.pg-collab__overlay {
  position: relative;
  z-index: 2;
  padding: 80px 64px;
  width: 100%;
  background:
    linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.55) 100%);
  color: #fff;
}
.pg-collab__overlay-inner { max-width: 1440px; margin: 0 auto; }
.pg-collab__le {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.14);
  color: #cfe1ff;
  padding: 8px 14px 7px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  border-radius: 999px;
  margin-bottom: 18px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.pg-collab__le::before {
  content: "";
  display: inline-block;
  width: 6px;
  height: 6px;
  background: var(--br-le);
  border-radius: 50%;
}
.pg-collab__title {
  font-size: clamp(40px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 0.98;
  margin: 0;
  text-wrap: balance;
  max-width: 18ch;
}
.pg-collab__sub {
  font-size: clamp(16px, 1.6vw, 19px);
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.92;
  max-width: 56ch;
}
.pg-collab__ctas {
  display: flex;
  gap: 12px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pg-collab__cta {
  display: inline-block;
  background: #ffffff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-collab__cta--ghost {
  background: transparent;
  color: #fff;
  border: 1px solid rgba(255,255,255,0.6);
}

@media (max-width: 700px) {
  .pg-collab__overlay { padding: 48px 24px; }
}

/* ============================================================
   HERO VIDEO MOMENT · short film between hero and content
   ============================================================ */
.pg-video-moment {
  position: relative;
  aspect-ratio: 21/9;
  min-height: 380px;
  max-height: 640px;
  overflow: hidden;
  background: #050505;
}
.pg-video-moment__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-video-moment__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 48px 32px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.45) 100%);
  color: #fff;
}
.pg-video-moment__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 14px;
  opacity: 0.88;
}
.pg-video-moment__title {
  font-size: clamp(32px, 4vw, 56px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1.05;
  margin: 0;
  max-width: 22ch;
  text-wrap: balance;
}

/* ============================================================
   COPERNI v2 · runway-first collab layout
   ============================================================ */
.pg-collab-v2 {
  background: #050505;
  color: #fff;
}
.pg-collab-v2__hero {
  position: relative;
  aspect-ratio: 16/8;
  min-height: 520px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
}
.pg-collab-v2__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-collab-v2__overlay {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 64px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.6) 100%);
  max-width: 1600px;
  margin: 0 auto;
}
.pg-collab-v2__title {
  font-size: clamp(36px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 12px 0 0;
  text-wrap: balance;
}
.pg-collab-v2__sub {
  font-size: clamp(15px, 1.5vw, 18px);
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.92;
  max-width: 60ch;
}
.pg-collab-v2__ctas { margin-top: 28px; }
.pg-collab-v2__gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2px;
  background: #050505;
}
.pg-collab-v2__tile {
  margin: 0;
  aspect-ratio: 3/4;
  overflow: hidden;
  background: #1a1a1a;
}
.pg-collab-v2__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-collab-v2__tile--copy {
  background: #f9f9f9;
  color: var(--br-text);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 32px;
}
@media (max-width: 900px) {
  .pg-collab-v2__gallery { grid-template-columns: 1fr 1fr; }
  .pg-collab-v2__overlay { padding: 32px 24px; }
}

/* ============================================================
   COPERNI GRID · 1 feature + 3 tiles (v5a)
   ============================================================ */
.pg-coperni-grid {
  background: #050505;
  color: #fff;
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 2px;
  min-height: 560px;
}
.pg-coperni-grid__feature {
  position: relative;
  overflow: hidden;
  background: #1a1a1a;
  display: flex;
  align-items: flex-end;
  min-height: 560px;
}
.pg-coperni-grid__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-coperni-grid__overlay {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 40px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.6) 100%);
  color: #fff;
}
.pg-coperni-grid__title {
  font-size: clamp(32px, 3.6vw, 52px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 12px 0 14px;
}
.pg-coperni-grid__sub {
  font-size: 16px;
  line-height: 1.5;
  margin: 0 0 22px;
  opacity: 0.92;
  max-width: 44ch;
}
.pg-coperni-grid__cta {
  font-size: 12px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #fff;
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.6);
  padding-bottom: 2px;
  font-weight: 700;
}
.pg-coperni-grid__tiles {
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  gap: 2px;
  background: #050505;
}
.pg-coperni-grid__tile {
  margin: 0;
  overflow: hidden;
  background: #1a1a1a;
}
.pg-coperni-grid__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
@media (max-width: 900px) {
  .pg-coperni-grid { grid-template-columns: 1fr; }
  .pg-coperni-grid__feature { min-height: 420px; }
  .pg-coperni-grid__tiles { grid-template-rows: none; grid-template-columns: repeat(3, 1fr); }
}

/* ============================================================
   FEATURED STRIP · 2-tile (v5b)
   ============================================================ */
.pg-feat-strip {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 32px;
}
.pg-feat-tile {
  display: flex;
  flex-direction: column;
  background: var(--br-alt-bg);
  text-decoration: none;
  color: var(--br-text);
  overflow: hidden;
  transition: opacity 0.15s;
}
.pg-feat-tile:hover { opacity: 0.92; }
.pg-feat-tile__media {
  aspect-ratio: 4/3;
  overflow: hidden;
  background: #f3f3f3;
}
.pg-feat-tile__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-feat-tile__copy {
  padding: 24px 28px 28px;
}
.pg-feat-tile__title {
  font-size: clamp(20px, 2vw, 28px);
  font-weight: 500;
  letter-spacing: -0.005em;
  margin: 4px 0 12px;
}
.pg-feat-tile__cta {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 700;
}
@media (max-width: 700px) {
  .pg-feat-strip { grid-template-columns: 1fr; padding: 0 16px; }
}

/* ============================================================
   VARIANT-CTA TWEAK MODES (Home tweaks panel)
   ============================================================ */
[data-variant-cta="off"] .pdp-vcard__addlink { display: none; }
[data-variant-cta="hover"] .pdp-vcard__addlink { display: none; }
[data-variant-cta="hover"] .pdp-vcard:hover .pdp-vcard__addlink { display: inline-block; }
[data-variant-cta="always"] .pdp-vcard__addlink {
  display: block;
  background: var(--br-text);
  color: #fff;
  text-align: center;
  padding: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  border: 0;
  margin-top: 12px;
}

/* ============================================================
   "Worn through every transition" media split placeholder slot
   ============================================================ */
.pg-text-with-media {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  min-height: 480px;
  background: var(--br-alt-bg);
}
.pg-text-with-media__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  color: #7a6f5b;
}
.pg-text-with-media__copy {
  padding: 64px 56px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
@media (max-width: 800px) {
  .pg-text-with-media { grid-template-columns: 1fr; }
  .pg-text-with-media__media { aspect-ratio: 4/5; }
  .pg-text-with-media__copy { padding: 40px 24px; }
}
.pg-hero-image {
  position: relative;
  height: 88vh;
  min-height: 580px;
  max-height: 820px;
  overflow: hidden;
  background: #0a0a0a;
}
.pg-hero-image__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-hero-image__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: 64px;
  background:
    linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%);
  color: #fff;
}
.pg-hero-image__copy { max-width: 780px; }
.pg-hero-image__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 16px;
  opacity: 0.88;
}
.pg-hero-image__title {
  font-size: clamp(40px, 5.4vw, 80px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-hero-image__body {
  font-size: 18px;
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.9;
  max-width: 50ch;
}
.pg-hero-image__ctas {
  display: flex;
  gap: 12px;
  margin-top: 28px;
  flex-wrap: wrap;
}
.pg-hero-image__cta {
  display: inline-block;
  background: #fff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-hero-image__cta--ghost {
  background: transparent;
  color: #fff;
  border: 1px solid #fff;
}
@media (max-width: 700px) {
  .pg-hero-image__overlay { padding: 32px 24px; }
  .pg-hero-image { height: 78vh; }
}

/* ============================================================
   THE SHOE IN MOTION · 3-up video grid
   ============================================================ */
.pg-motion-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.pg-motion {
  margin: 0;
  display: flex;
  flex-direction: column;
  background: var(--br-alt-bg);
  overflow: hidden;
}
.pg-motion__video {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  display: block;
  background: #f3f3f3;
}
.pg-motion__cap {
  padding: 18px 20px 22px;
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--br-text-soft);
}
.pg-motion__cap b {
  display: block;
  color: var(--br-text);
  font-weight: 600;
  letter-spacing: -0.005em;
  font-size: 15px;
  margin-bottom: 4px;
}
@media (max-width: 900px) {
  .pg-motion-grid { grid-template-columns: 1fr; gap: 24px; }
  .pg-motion__video { aspect-ratio: 16/9; }
}

/* ============================================================
   HOME v2 · FULL-BLEED VIDEO HERO
   ============================================================ */
.pg-hero-video {
  position: relative;
  height: 90vh;
  min-height: 580px;
  max-height: 820px;
  overflow: hidden;
  background: #050505;
}
.pg-hero-video__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-hero-video__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: 64px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%);
  color: #fff;
}
.pg-hero-video__copy { max-width: 780px; }
.pg-hero-video__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 16px;
  opacity: 0.88;
}
.pg-hero-video__title {
  font-size: clamp(40px, 5.4vw, 80px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-hero-video__body {
  font-size: 18px;
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.9;
  max-width: 50ch;
}
.pg-hero-video__ctas {
  display: flex;
  gap: 12px;
  margin-top: 28px;
  flex-wrap: wrap;
}
.pg-hero-video__cta {
  display: inline-block;
  background: #fff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-hero-video__cta--ghost {
  background: transparent;
  color: #fff;
  border: 1px solid #fff;
}
@media (max-width: 700px) {
  .pg-hero-video__overlay { padding: 32px 24px; }
  .pg-hero-video { height: 80vh; }
}

/* ============================================================
   HOME v3 · MULTI-TILE HERO
   ============================================================ */
.pg-hero-tiles {
  padding: 16px;
  background: #fff;
}
.pg-hero-tiles__grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: repeat(2, minmax(280px, 1fr));
  gap: 12px;
  max-width: 1600px;
  margin: 0 auto;
}
.pg-hero-tiles__feature {
  grid-column: 1;
  grid-row: 1 / 3;
  position: relative;
  overflow: hidden;
  background: #050505;
  min-height: 580px;
  display: flex;
  align-items: flex-end;
}
.pg-hero-tiles__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.pg-hero-tiles__feature-copy {
  position: relative;
  z-index: 2;
  padding: 36px;
  color: #fff;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.6) 100%);
  width: 100%;
}
.pg-hero-tiles__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin: 0 0 14px;
  opacity: 0.9;
}
.pg-hero-tiles__title {
  font-size: clamp(28px, 3.4vw, 48px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.05;
  margin: 0 0 22px;
  max-width: 18ch;
  text-wrap: balance;
}
.pg-hero-tiles__cta {
  display: inline-block;
  background: #fff;
  color: var(--br-text);
  padding: 12px 24px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
.pg-hero-tile {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  padding: 22px;
  text-decoration: none;
  color: var(--br-text);
  min-height: 280px;
  background: var(--br-alt-bg);
}
.pg-hero-tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}
.pg-hero-tile span {
  position: relative;
  z-index: 2;
  font-size: clamp(20px, 2vw, 28px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.15;
  max-width: 16ch;
  color: var(--br-text);
  background: rgba(255,255,255,0.92);
  padding: 8px 14px;
  display: inline-block;
}
.pg-hero-tile--pink span, .pg-hero-tile--lilac span, .pg-hero-tile--yellow span {
  background: rgba(255,255,255,0.92);
}
@media (max-width: 900px) {
  .pg-hero-tiles__grid {
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto;
  }
  .pg-hero-tiles__feature { grid-column: span 2; grid-row: auto; min-height: 420px; }
}

/* ============================================================
   EQUAL-HEIGHT JOURNAL / EDITORIAL CARDS · fix
   ============================================================ */
.pg-edit {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.pg-edit__dek { flex: 1; }
.pg-editorial-grid, .pg-editorial-grid--six { align-items: stretch; }

/* ============================================================
   VARIANT CARD · "Add to cart →" text link (replaces overlay button)
   ============================================================ */
.pdp-vcard__addlink {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  margin-top: 8px;
  align-self: flex-start;
  display: inline-block;
}
.pdp-vcard__addlink:hover { opacity: 0.7; }

.pg-editorial__head {
  text-align: center;
  margin: 0 auto 48px;
  max-width: 56ch;
}
.pg-editorial__head .pdp-h2 { margin-bottom: 12px; }

.pg-editorial-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}
.pg-editorial-grid--six { grid-template-columns: repeat(3, 1fr); gap: 56px 32px; }
@media (max-width: 900px) {
  .pg-editorial-grid, .pg-editorial-grid--six { grid-template-columns: 1fr; gap: 32px; }
}

.pg-edit {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
}
.pg-edit__media {
  aspect-ratio: 4/3;
  background:
    repeating-linear-gradient(135deg, #efece2 0 16px, #e8e4d6 16px 32px);
  margin-bottom: 16px;
  transition: opacity 0.2s;
}
.pg-edit__media--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 16px, #efdcd2 16px 32px); }
.pg-edit__media--dark  { background: repeating-linear-gradient(135deg, #2c2c2c 0 16px, #232323 16px 32px); }
.pg-edit__media--stone { background: repeating-linear-gradient(135deg, #d4d0c4 0 16px, #c9c5b8 16px 32px); }
.pg-edit:hover .pg-edit__media { opacity: 0.92; }

.pg-edit__meta {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
  margin: 4px 0 8px;
}
.pg-edit__title {
  font-size: 22px;
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.2;
  margin: 0 0 8px;
  color: var(--br-text);
}
.pg-edit__dek {
  font-size: 14.5px;
  color: var(--br-text-soft);
  line-height: 1.55;
  margin: 0;
  max-width: 38ch;
}

/* Blog index uses a featured + grid layout */
.pg-feature {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 48px;
  align-items: center;
  margin-bottom: 64px;
  padding-bottom: 56px;
  border-bottom: 1px solid var(--br-line);
}
.pg-feature__media {
  aspect-ratio: 4/3;
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 20px, #232323 20px 40px);
}
.pg-feature__meta {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-accent);
  margin: 0 0 12px;
}
.pg-feature__title {
  font-size: clamp(32px, 3.6vw, 48px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1.05;
  margin: 0 0 18px;
  text-wrap: balance;
}
.pg-feature__dek {
  font-size: 17px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0 0 24px;
  max-width: 48ch;
}
.pg-feature__cta {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 700;
}
@media (max-width: 900px) {
  .pg-feature { grid-template-columns: 1fr; gap: 24px; }
}

/* ============== ARTICLE HERO + BODY ============== */

.pg-article-hero {
  position: relative;
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 22px, #232323 22px 44px);
  color: #fff;
  min-height: 64vh;
  display: flex;
  align-items: flex-end;
}
.pg-article-hero__inner {
  position: relative;
  z-index: 2;
  max-width: 1440px;
  margin: 0 auto;
  padding: 80px 32px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.55) 100%);
  width: 100%;
}
.pg-article-hero__meta {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin: 0 0 16px;
  color: var(--br-accent);
}
.pg-article-hero__meta-sep { color: rgba(255,255,255,0.4); }
.pg-article-hero__meta-time { color: rgba(255,255,255,0.78); font-weight: 600; }

.pg-article-hero__title {
  font-size: clamp(40px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  max-width: 22ch;
  text-wrap: balance;
}
.pg-article-hero__dek {
  font-size: clamp(18px, 1.8vw, 22px);
  line-height: 1.45;
  color: rgba(255,255,255,0.88);
  margin: 24px 0 0;
  max-width: 52ch;
  text-wrap: pretty;
}
.pg-article-hero__byline {
  display: flex;
  gap: 24px;
  align-items: center;
  margin-top: 36px;
  font-size: 13px;
  letter-spacing: 0.04em;
  color: rgba(255,255,255,0.88);
}
.pg-article-hero__avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  border: 1px solid rgba(255,255,255,0.3);
}
.pg-article-hero__byline b { color: #fff; font-weight: 600; margin-right: 4px; }

@media (max-width: 700px) {
  .pg-article-hero__inner { padding: 48px 24px; }
}

/* Article body */
.pg-article-body {
  max-width: 720px;
  margin: 0 auto;
  padding: 80px 24px 96px;
  font-size: 18px;
  line-height: 1.7;
  color: var(--br-text);
}
.pg-article-body__lede {
  font-size: 22px;
  line-height: 1.55;
  color: var(--br-text);
  font-weight: 400;
  letter-spacing: -0.005em;
  margin: 0 0 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
}
.pg-article-body p {
  margin: 0 0 20px;
  text-wrap: pretty;
}
.pg-article-body h2 {
  font-size: clamp(24px, 2.4vw, 32px);
  font-weight: 500;
  letter-spacing: -0.005em;
  margin: 48px 0 14px;
  line-height: 1.2;
}
.pg-article-body h3 {
  font-size: 22px;
  font-weight: 500;
  margin: 36px 0 10px;
  line-height: 1.25;
}
.pg-article-body ul {
  margin: 0 0 24px;
  padding-left: 0;
  list-style: none;
}
.pg-article-body ul li {
  position: relative;
  padding-left: 22px;
  margin-bottom: 8px;
}
.pg-article-body ul li::before {
  content: "→";
  color: var(--br-accent);
  font-weight: 700;
  position: absolute;
  left: 0;
}
.pg-article-body blockquote {
  margin: 32px -16px;
  padding: 24px 32px;
  background: var(--br-alt-bg);
  border-left: 3px solid var(--br-accent);
  font-size: 22px;
  line-height: 1.4;
  font-weight: 400;
  letter-spacing: -0.005em;
}
.pg-article-body figure {
  margin: 40px -32px;
}
.pg-article-body figcaption {
  font-size: 13px;
  color: var(--br-text-mute);
  letter-spacing: 0.02em;
  margin-top: 12px;
  font-style: italic;
  text-align: center;
}
.pg-article-body__figure {
  aspect-ratio: 16/9;
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
}

/* ============== HOME — MULTI-PROMO TILES (alt to media-split) ============== */

.pg-promos {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 32px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
.pg-promo {
  position: relative;
  aspect-ratio: 4/3;
  background:
    repeating-linear-gradient(135deg, #efece2 0 16px, #e8e4d6 16px 32px);
  display: flex;
  align-items: flex-end;
  padding: 32px;
  text-decoration: none;
  color: var(--br-text);
  overflow: hidden;
}
.pg-promo--dark {
  background: repeating-linear-gradient(135deg, #2c2c2c 0 16px, #232323 16px 32px);
  color: #fff;
}
.pg-promo--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 16px, #efdcd2 16px 32px); }
.pg-promo__inner {
  position: relative;
  z-index: 2;
  background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.35) 100%);
  width: 100%;
  padding: 20px;
  margin: -32px;
  margin-top: 0;
  padding-top: 32px;
}
.pg-promo__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin: 0 0 8px;
  opacity: 0.78;
}
.pg-promo__title {
  font-size: clamp(24px, 2.4vw, 32px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.1;
  margin: 0 0 4px;
}
.pg-promo__more {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-top: 12px;
  display: inline-block;
  border-bottom: 1px solid currentColor;
  padding-bottom: 2px;
  font-weight: 700;
}
@media (max-width: 700px) {
  .pg-promos { grid-template-columns: 1fr; }
  .pg-promo { aspect-ratio: 16/10; }
}

/* ============== NEWSLETTER MID-PAGE BLOCK ============== */

.pg-newsletter {
  background: var(--br-text);
  color: #fff;
  padding: 80px 32px;
}
.pg-newsletter__inner {
  max-width: 880px;
  margin: 0 auto;
  text-align: center;
}
.pg-newsletter__inner h2 {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 400;
  margin: 0 0 12px;
  letter-spacing: -0.015em;
  line-height: 1.1;
}
.pg-newsletter__inner p {
  font-size: 16px;
  color: rgba(255,255,255,0.78);
  margin: 0 0 28px;
  line-height: 1.55;
}
.pg-newsletter__form {
  display: flex;
  max-width: 480px;
  margin: 0 auto;
  border: 1px solid rgba(255,255,255,0.3);
}
.pg-newsletter__form input {
  flex: 1;
  padding: 16px 18px;
  border: 0;
  background: transparent;
  color: #fff;
  font-family: inherit;
  font-size: 14px;
}
.pg-newsletter__form input::placeholder { color: rgba(255,255,255,0.5); }
.pg-newsletter__form button {
  background: var(--br-accent);
  color: #fff;
  border: 0;
  padding: 16px 24px;
  font-family: inherit;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

/* ============== PAGE NAV STRIP (cross-link between mocks) ============== */

.pg-tab-strip {
  background: var(--br-alt-bg);
  border-bottom: 1px solid var(--br-line);
}
.pg-tab-strip__inner {
  max-width: 1440px;
  margin: 0 auto;
  padding: 10px 32px;
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  align-items: center;
}
.pg-tab-strip__label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-text-mute);
  margin-right: 10px;
}
.pg-tab-strip a {
  display: inline-block;
  padding: 6px 14px;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  text-decoration: none;
  border: 1px solid transparent;
  border-radius: 0;
}
.pg-tab-strip a:hover { color: var(--br-text); border-color: var(--br-line); background: #fff; }
.pg-tab-strip a[aria-current="page"] {
  background: var(--br-text);
  color: #fff;
  border-color: var(--br-text);
}

/* ============== COLLECTION VARIANT GRID (full, expanded) ============== */

.pg-coll-variants {
  max-width: 1440px;
  margin: 0 auto;
  padding: 56px 32px 96px;
}
.pg-coll-variants__head {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 24px;
  margin-bottom: 28px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
  flex-wrap: wrap;
}
.pg-coll-variants__count {
  font-size: 13px;
  color: var(--br-text-soft);
  letter-spacing: 0.04em;
}
.pg-coll-variants__count b { color: var(--br-text); font-weight: 600; }
.pg-coll-variants__sort {
  display: flex;
  gap: 16px;
  align-items: center;
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pg-coll-variants__sort select {
  font-family: inherit;
  font-size: 13px;
  padding: 8px 12px;
  border: 1px solid var(--br-text);
  background: #fff;
  text-transform: none;
  letter-spacing: 0;
}

.pg-coll-variants__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px 24px;
}
@media (max-width: 1000px) { .pg-coll-variants__grid { grid-template-columns: repeat(2, 1fr); } }


/* ============================================================
   BELIEF BANDS · oversized type, no image (editorial pause)
   ============================================================ */
.pg-belief {
  background: #fff;
  padding: 80px 32px;
  text-align: center;
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
}
.pg-belief--dark {
  background: var(--br-text);
  color: #fff;
  border-color: var(--br-text);
}
.pg-belief__inner { max-width: 1200px; margin: 0 auto; }
.pg-belief__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 18px;
  opacity: 0.75;
}
.pg-belief__line {
  font-size: clamp(36px, 5vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-belief__hashtag {
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--br-accent);
  font-weight: 700;
  margin: 22px 0 0;
}

/* ============================================================
   FULL-BLEED LIFESTYLE BAND (Join the Movement)
   ============================================================ */
.pg-fullbleed {
  position: relative;
  min-height: 580px;
  overflow: hidden;
  background: #1a1a1a;
  display: flex;
  align-items: center;
}
.pg-fullbleed__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.pg-fullbleed__overlay {
  position: relative;
  z-index: 2;
  padding: 80px 64px;
  max-width: 720px;
  color: #fff;
}
.pg-fullbleed__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 16px;
  opacity: 0.9;
}
.pg-fullbleed__title {
  font-size: clamp(40px, 5.4vw, 72px);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1;
  margin: 0;
  text-wrap: balance;
}
.pg-fullbleed__body {
  font-size: 18px;
  line-height: 1.5;
  margin: 18px 0 0;
  opacity: 0.92;
  max-width: 46ch;
}
.pg-fullbleed__cta {
  display: inline-block;
  margin-top: 28px;
  background: #fff;
  color: var(--br-text);
  padding: 14px 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
}
@media (max-width: 700px) {
  .pg-fullbleed__overlay { padding: 48px 24px; }
}


/* ============================================================
   v11 ADDITIONS — new sections not in base CSS
   ============================================================ */

/* HERO */
.pg-hero-image { position: relative; width: 100%; min-height: 85vh; display: flex; align-items: flex-end; overflow: hidden; }
.pg-hero-image__media { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 30%; }
.pg-hero-image__overlay { position: relative; z-index: 2; width: 100%; padding: 80px 64px; background: linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.2) 60%, transparent 100%); }
.pg-hero-image__eyebrow { font-size: 12px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.72); margin: 0 0 16px; transition: opacity 0.3s ease; }
.pg-hero-image__title { font-size: clamp(40px, 5.5vw, 72px); font-weight: 400; letter-spacing: -0.025em; line-height: 1.02; color: #fff; margin: 0; max-width: 18ch; text-wrap: balance; }
.pg-hero-image__body { font-size: 18px; line-height: 1.55; color: rgba(255,255,255,0.82); margin: 20px 0 0; max-width: 52ch; }
.pg-hero-image__ctas { display: flex; gap: 14px; margin-top: 36px; flex-wrap: wrap; }
.pg-hero-image__cta { display: inline-flex; align-items: center; padding: 16px 36px; font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; background: #fff; color: #050505; }
.pg-hero-image__cta--ghost { background: transparent; color: #fff; border: 1.5px solid rgba(255,255,255,0.6); }
.pg-hero-image__cta--ghost:hover { background: rgba(255,255,255,0.1); }

/* MEDIA SPLIT 50/50 */
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CANONICAL 50/50 SPLIT SIZE — DO NOT CHANGE
   Approved: v18 "Never slip in chair pose" section
   height: 420px FIXED | overflow: hidden | padding: 56px 64px
   Fixed height = all splits locked at same size regardless of content
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.v11-split { display: grid; grid-template-columns: 1fr 1fr; min-height: 420px; border-top: 1px solid var(--br-line); border-bottom: 1px solid var(--br-line); }
.v11-split__media { position: relative; overflow: hidden; background: #111; }
.v11-split__media img, .v11-split__media video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
.v11-split__copy { background: #f9f7f2; display: flex; flex-direction: column; justify-content: center; padding: 80px 72px; }
.v11-split__stars { font-size: 18px; color: var(--br-star); letter-spacing: 2px; margin-bottom: 6px; }
.v11-split__trusted { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--br-text-soft); margin-bottom: 16px; }
.v11-split__slogan { font-size: clamp(38px, 4.6vw, 66px); font-weight: 300; letter-spacing: -0.03em; line-height: 1.0; color: var(--br-text); margin-bottom: 28px; min-height: 0; max-width: 15ch; text-wrap: balance; transition: opacity 0.4s ease; }
.v11-split__slogan strong { font-weight: 600; }
.v11-split__cta { display: inline-flex; align-items: center; gap: 8px; padding: 16px 32px; background: var(--br-button); color: var(--br-button-text); font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; align-self: flex-start; }

/* SOCK COMPARISON */
.v11-compare { padding: 80px 64px; background: var(--br-bg); }
.v11-compare__inner { max-width: 1200px; margin: 0 auto; }
.v11-compare__head { text-align: center; margin-bottom: 64px; }
.v11-compare__eyebrow { font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--br-accent); margin: 0 0 14px; }
.v11-compare__title { font-size: clamp(28px, 3.5vw, 48px); font-weight: 400; letter-spacing: -0.02em; margin: 0; }
.v11-compare__sub { font-size: 17px; color: var(--br-text-soft); margin: 16px auto 0; max-width: 56ch; }
.v11-compare__grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; background: var(--br-line); }
.v11-compare__col { background: var(--br-bg); padding: 48px; }
.v11-compare__col--them { background: var(--br-alt-bg); }
.v11-compare__col-head { font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 32px; padding-bottom: 16px; border-bottom: 2px solid var(--br-line); }
.v11-compare__col-head--us { border-bottom-color: var(--br-text); }
.v11-compare__row { display: flex; justify-content: space-between; align-items: baseline; padding: 14px 0; border-bottom: 1px solid var(--br-line-soft); font-size: 15px; }
.v11-compare__row:last-child { border-bottom: none; }
.v11-compare__row-label { color: var(--br-text-soft); }
.v11-compare__row-val { font-weight: 600; }
.v11-compare__row-val--bad { color: #c43d2a; }
.v11-compare__row-val--good { color: #1f6f4a; }
.v11-compare__math { margin-top: 48px; padding: 32px; background: var(--br-text); color: #fff; text-align: center; }
.v11-compare__math-line { font-size: 15px; line-height: 1.7; opacity: 0.82; }
.v11-compare__math-big { font-size: clamp(22px, 2.5vw, 32px); font-weight: 500; letter-spacing: -0.01em; margin-top: 12px; opacity: 1; }

/* 3 DISCIPLINES */
.v11-disciplines { background: var(--br-alt-bg); padding: 96px 64px; }
.v11-disciplines__inner { max-width: 1280px; margin: 0 auto; }
.v11-disciplines__head { text-align: center; margin-bottom: 64px; }
.v11-disciplines__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; }
.v11-disc { position: relative; overflow: hidden; min-height: 520px; }
.v11-disc__img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s ease; }
.v11-disc:hover .v11-disc__img { transform: scale(1.03); }
.v11-disc__overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.1) 55%, transparent 100%); display: flex; flex-direction: column; justify-content: flex-end; padding: 40px 36px; }
.v11-disc__eyebrow { font-size: 11px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.7); } .v11-disc__eyebrow--UNUSED { color: var(--br-accent); margin-bottom: 10px; }
.v11-disc__title { font-size: clamp(22px, 2.2vw, 30px); font-weight: 400; color: #fff; line-height: 1.15; margin: 0 0 12px; letter-spacing: -0.01em; }
.v11-disc__body { font-size: 14px; line-height: 1.55; color: rgba(255,255,255,0.78); margin: 0; }

/* VIDEO SECTION */
.v11-videos { padding: 80px 64px; background: var(--br-bg); }
.v11-videos__inner { max-width: 1280px; margin: 0 auto; }
.v11-videos__head { text-align: center; margin-bottom: 64px; }
.v11-videos__layout { display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; align-items: start; }
.v11-video-large { position: relative; }
.v11-video-large video { width: 100%; display: block; aspect-ratio: 16/10; object-fit: cover; background: #111; }
.v11-video-large__cap { padding: 20px 0 0; }
.v11-video-large__title { font-size: 17px; font-weight: 500; margin: 0 0 6px; }
.v11-video-large__sub { font-size: 14px; color: var(--br-text-soft); margin: 0; }
.v11-videos-small { display: flex; flex-direction: column; gap: 16px; }
.v11-video-small { display: grid; grid-template-columns: auto 1fr; gap: 16px; align-items: start; }
.v11-video-small video { width: 160px; aspect-ratio: 4/3; object-fit: cover; background: #111; display: block; }
.v11-video-small__cap { padding-top: 4px; }
.v11-video-small__title { font-size: 15px; font-weight: 500; margin: 0 0 4px; }
.v11-video-small__sub { font-size: 13px; color: var(--br-text-soft); margin: 0; line-height: 1.5; }

/* REVIEWS UPGRADED */
.v11-reviews { padding: 80px 64px; background: var(--br-alt-bg); }
.v11-reviews__inner { max-width: 1280px; margin: 0 auto; }
.v11-reviews__head { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 56px; }
.v11-reviews__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; }
.v11-review { background: var(--br-bg); padding: 40px; }
.v11-review__stars { font-size: 16px; color: var(--br-star); letter-spacing: 1px; margin-bottom: 16px; }
.v11-review__title { font-size: 17px; font-weight: 500; margin: 0 0 12px; }
.v11-review__body { font-size: 15px; line-height: 1.65; color: var(--br-text-soft); margin: 0 0 20px; }
.v11-review__attr { font-size: 12px; color: var(--br-text-mute); font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; }
.v11-review__badge { display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; padding: 2px 8px; background: var(--br-le-bg); color: var(--br-le); margin-bottom: 12px; }

/* GUARANTEE */
.v11-guarantee { padding: 72px 64px; background: var(--br-text); color: #fff; }
.v11-guarantee__inner { max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1px 1fr 1px 1fr; gap: 48px; }
.v11-guarantee__eyebrow { font-size: 11px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 12px; }
.v11-guarantee__title { font-size: 22px; font-weight: 400; letter-spacing: -0.01em; margin: 0 0 14px; }
.v11-guarantee__body { font-size: 14px; line-height: 1.65; color: rgba(255,255,255,0.72); margin: 0; }
.v11-guarantee__divider { width: 1px; background: rgba(255,255,255,0.12); }
.v11-guarantee__head { max-width: 1000px; margin: 0 auto 40px; text-align: center; }
.v11-guarantee__main-title { font-size: clamp(28px, 3vw, 44px); font-weight: 400; letter-spacing: -0.02em; color: #fff; margin: 0 0 16px; }
.v11-guarantee__main-sub { font-size: 16px; color: rgba(255,255,255,0.65); line-height: 1.6; max-width: 54ch; margin: 0 auto; }

/* BELIEF BAND */
.v11-belief { padding: 64px; background: var(--br-bg); border-top: 1px solid var(--br-line); border-bottom: 1px solid var(--br-line); text-align: center; }
.v11-belief__line { font-size: clamp(36px, 5vw, 72px); font-weight: 400; letter-spacing: -0.01em; color: var(--br-text); margin: 0; }
.v11-belief--dark { background: var(--br-text); }
.v11-belief--dark .v11-belief__line { color: #fff; }

/* NEWSLETTER */
.v11-newsletter { padding: 96px 64px; background: var(--br-alt-bg-2); text-align: center; }
.v11-newsletter h2 { font-size: clamp(24px, 2.8vw, 40px); font-weight: 400; letter-spacing: -0.02em; margin: 0 0 14px; }
.v11-newsletter p { font-size: 16px; color: var(--br-text-soft); max-width: 48ch; margin: 0 auto 32px; }
.v11-newsletter__form { display: flex; gap: 0; max-width: 480px; margin: 0 auto; }
.v11-newsletter__form input { flex: 1; padding: 16px 20px; font-size: 15px; border: 1px solid var(--br-line); background: #fff; outline: none; }
.v11-newsletter__form button { padding: 16px 28px; background: var(--br-button); color: var(--br-button-text); font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; border: none; cursor: pointer; }

/* COLLAB HERO */
.v11-collab { position: relative; min-height: 600px; display: flex; align-items: center; overflow: hidden; }
.v11-collab__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.v11-collab__video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.v11-collab__overlay { position: relative; z-index: 2; padding: 80px 80px; background: linear-gradient(to right, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.2) 65%, transparent 100%); width: 100%; }
.v11-collab__le { font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(255,255,255,0.6); margin-bottom: 16px; display: block; }
.v11-collab__title { font-size: clamp(32px, 4vw, 56px); font-weight: 400; letter-spacing: -0.02em; color: #fff; margin: 0 0 20px; max-width: 14ch; }
.v11-collab__sub { font-size: 16px; line-height: 1.6; color: rgba(255,255,255,0.78); max-width: 44ch; margin: 0 0 36px; }
.v11-collab__cta { display: inline-flex; align-items: center; padding: 16px 36px; background: #fff; color: #050505; font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; }

/* JOURNAL */
.v11-journal { padding: 80px 64px; background: var(--br-bg); }
.v11-journal__inner { max-width: 1280px; margin: 0 auto; }
.v11-journal__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 56px; }
.v11-article { text-decoration: none; color: inherit; display: block; }
.v11-article__img { width: 100%; aspect-ratio: 3/2; object-fit: cover; display: block; background: var(--br-alt-bg); margin-bottom: 20px; }
.v11-article__meta { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--br-accent); margin-bottom: 10px; }
.v11-article__title { font-size: 19px; font-weight: 500; line-height: 1.3; margin: 0 0 10px; letter-spacing: -0.01em; }
.v11-article__dek { font-size: 14px; line-height: 1.6; color: var(--br-text-soft); margin: 0; }
.v11-article:hover .v11-article__title { text-decoration: underline; }

/* SECTION HEADER SHARED */
.v11-section-head { text-align: center; }
.v11-eyebrow { font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--br-accent); margin: 0 0 14px; }
.v11-h2 { font-size: clamp(28px, 3.2vw, 44px); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin: 0; }
.v11-lede { font-size: 17px; line-height: 1.6; color: var(--br-text-soft); max-width: 56ch; margin: 16px auto 0; }

@media (max-width: 900px) {
  .v11-split, .v11-compare__grid, .v11-disciplines__grid, .v11-reviews__grid, .v11-journal__grid, .v11-guarantee__inner { grid-template-columns: 1fr; }
  .v11-videos__layout { grid-template-columns: 1fr; }
  .v11-video-small { grid-template-columns: 1fr; }
  .v11-video-small video { width: 100%; }
  .v11-compare { padding: 64px 24px; }
  .v11-disciplines { padding: 64px 24px; }
  .v11-reviews { padding: 64px 24px; }
  .v11-guarantee { padding: 64px 24px; }
  .v11-videos { padding: 64px 24px; }
  .v11-journal { padding: 64px 24px; }
  .pg-hero-image__overlay { padding: 48px 24px; }
  .v11-split__copy { padding: 56px 36px; }
}

/* ============================================================
   MOBILE FIRST — v13
   ============================================================ */
@media (max-width: 768px) {

  /* Header */
  .pdp-header__nav { display: none; }
  .pdp-header__inner { padding: 0 20px; }

  /* Hero */
  .pg-hero-image { min-height: 75vh; }
  .pg-hero-image__overlay { padding: 32px 24px 48px; }
  .pg-hero-image__title { font-size: clamp(30px, 9vw, 48px); max-width: 100%; }
  .pg-hero-image__body { font-size: 16px; margin-top: 14px; }
  .pg-hero-image__ctas { flex-direction: column; gap: 10px; margin-top: 28px; }
  .pg-hero-image__cta { width: 100%; justify-content: center; min-height: 52px; font-size: 14px; }

  /* Pillar strip */
  .pdp-pillars__pts { flex-direction: column; gap: 8px; text-align: center; }
  .pdp-pillars__div { display: none; }

  /* 50/50 splits */

  /* Tighter splits on mobile */
  .v11-split { height: auto !important; overflow: visible !important; }
  .v11-split__media { min-height: 260px !important; }
  .v11-split__copy { padding: 36px 24px !important; }
  .v11-split__slogan { font-size: clamp(20px, 5.5vw, 28px) !important; }
  .v11-split__cta { width: 100%; justify-content: center; }

  .v11-split { grid-template-columns: 1fr; height: auto !important; }
  .v11-split__media { min-height: 280px; order: 0 !important; }
  .v11-split__copy { padding: 40px 24px; order: 1 !important; }
  .v11-split__slogan { font-size: clamp(20px, 6vw, 28px); min-height: auto; }

  /* Price strip */
  .v11-price-strip { padding: 36px 24px; }
  .v11-price-strip p:first-child { font-size: 20px; }

  /* Product grid */
  .pdp-variants__grid { grid-template-columns: 1fr 1fr; gap: 16px; }
  .pdp-variants__head { flex-direction: column; gap: 16px; }

  /* Disciplines */
  .v11-disciplines { padding: 48px 24px; }
  .v11-disciplines__grid { grid-template-columns: 1fr; }
  .v11-disc { min-height: 360px; }

  /* Videos */
  .v11-videos { padding: 48px 24px; }
  .v11-videos__layout { grid-template-columns: 1fr; }
  .v11-video-small { grid-template-columns: 1fr; }
  .v11-video-small video, .v11-video-small img { width: 100%; aspect-ratio: 16/9; }

  /* Reviews */
  .v11-reviews { padding: 48px 24px; }
  .v11-reviews__grid { grid-template-columns: 1fr; }
  .v11-reviews__head { flex-direction: column; gap: 16px; }

  /* Collab */
  .v11-collab__overlay { padding: 40px 24px; }
  .v11-collab__title { font-size: clamp(26px, 7vw, 40px); }

  /* Journal */
  .v11-journal { padding: 48px 24px; }
  .pg-editorial-grid { grid-template-columns: 1fr; gap: 32px; }

  /* Guarantee */
  .v11-guarantee { padding: 48px 24px; }
  .v11-guarantee__inner { grid-template-columns: 1fr; gap: 32px; }
  .v11-guarantee__divider { display: none; }
  .v11-guarantee__main-title { font-size: clamp(26px, 7vw, 40px); }

  /* Belief bands */
  .v11-belief { padding: 48px 24px; }
  .v11-belief__line { font-size: clamp(26px, 7vw, 44px); }

  /* Newsletter */
  .v11-newsletter { padding: 56px 24px; }
  .v11-newsletter__form { flex-direction: column; }
  .v11-newsletter__form input, .v11-newsletter__form button { width: 100%; min-height: 52px; }

  /* Footer */
  .pdp-footer__grid { grid-template-columns: 1fr; gap: 32px; }
  .pdp-footer__bottom { flex-direction: column; gap: 12px; text-align: center; }

  /* FAQ */
  .pdp-faq__list { padding: 0 !important; }

  /* General sections */
  .pdp-section { padding: 56px 24px; }
  .v11-compare { padding: 48px 24px; }
  .v11-compare__grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {



  /* Value v20 mobile */
  section[style*="background:#f5f2ec;padding:52px"] > div > div {
    grid-template-columns: 1fr !important;
  }
  section[style*="background:#f5f2ec;padding:52px"] > div > div > div[style*="background:#ddd8d0;margin:0 28px"] {
    display: none !important;
  }
  section[style*="background:#f5f2ec;padding:52px"] > div > div > div {
    padding: 20px 0 !important;
    border-bottom: 1px solid #ddd8d0;
  }
  section[style*="background:#f5f2ec;padding:52px"] { padding: 40px 24px !important; }

  /* Value section condensed — mobile */
  section[style*="background:#f5f2ec;padding:56px"] > div {
    grid-template-columns: 1fr !important;
  }
  section[style*="background:#f5f2ec;padding:56px"] > div > div[style*="background:#ddd8d0"] {
    display: none !important;
  }
  section[style*="background:#f5f2ec;padding:56px"] > div > div:not([style*="background"]) {
    padding: 24px 0 !important;
    border-bottom: 1px solid #ddd8d0;
  }
  section[style*="background:#f5f2ec;padding:56px"] { padding: 40px 24px !important; }


  /* Collab split — mobile stack */
  section[style*="grid-template-columns:1fr 1fr;min-height:560px"] {
    grid-template-columns: 1fr !important;
  }
  section[style*="grid-template-columns:1fr 1fr;min-height:560px"] > div:first-child {
    min-height: 280px;
  }
}
@media (max-width: 480px) {
  .pg-hero-image__title { font-size: clamp(28px, 8vw, 38px); }
  .v11-h2 { font-size: clamp(24px, 7vw, 32px); }
  .pdp-h2 { font-size: clamp(22px, 7vw, 30px); }
  .pdp-variants__grid { grid-template-columns: 1fr; }
}


/* Alternate light value section */
.pdp-value--light {
  background: #f5f3ee;
}
.pdp-value--light .pdp-value__col {
  background: #fff;
}
.pdp-value--light .pdp-value__col--ours {
  background: var(--br-text);
}
.pdp-value--light .pdp-value__copy .pdp-eyebrow { color: var(--br-accent); }
.pdp-value--light .pdp-value__copy .pdp-h2 { color: var(--br-text); }
.pdp-value--light .pdp-value__copy .pdp-lede { color: var(--br-text-soft); }
.pdp-value--light .pdp-value__compare { background: var(--br-line); }
.pdp-value--light .pdp-value__col .pdp-value__tag { color: var(--br-text-soft); }
.pdp-value--light .pdp-value__col .pdp-value__amount { color: var(--br-text); }
.pdp-value--light .pdp-value__col .pdp-value__list { color: var(--br-text-soft); }
.pdp-value--light blockquote { background: rgba(0,0,0,0.04); border-left-color: var(--br-accent); }
.pdp-value--light blockquote p { color: var(--br-text); }
.pdp-value--light blockquote cite { color: var(--br-text-mute); }
.pdp-value--light a[style] { background: var(--br-text) !important; color: #fff !important; }

</style>
</head>
<body>

<!-- SCHEMA MARKUP for GEO/SEO -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Barreletics Performance Skin — Grippy Shoe for Barre, Pilates & Yoga",
  "description": "The premium grip shoe for barre, reformer Pilates, Lagree, Megaformer, and yoga. Replaces grip socks. 360-degree grip, no latex, no silicone. Made in USA.",
  "brand": { "@type": "Brand", "name": "Barreletics" },
  "offers": { "@type": "Offer", "price": "74.00", "priceCurrency": "USD", "availability": "https://schema.org/InStock" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "294" }
}
</script>

<!-- TICKER -->
<div class="pdp-ticker" aria-live="polite">
  <span class="pdp-ticker__slide">Buy 2 Save 15% · use code <b>SAVE15</b></span>
  <span class="pdp-ticker__slide is-active">🇺🇸 Made in USA · Free shipping over $150 · 30-day returns &nbsp;<a href="#">details →</a></span>
  <span class="pdp-ticker__slide">★ Trusted by 1,000’s of instructors · studios · athletes</span>
</div>

<!-- HEADER -->
<header class="pdp-header">
  <div class="pdp-header__inner">
    <nav class="pdp-header__nav">
      <a href="Barreletics Collection.html">Grippy Footwear <span class="pdp-header__chev">⌄</span></a>
      <a href="#">Apparel <span class="pdp-header__chev">⌄</span></a>
      <a href="#">Collaborations <span class="pdp-header__chev">⌄</span></a>
      <a href="Barreletics Blog.html">Journal</a>
      <a href="#">About Us <span class="pdp-header__chev">⌄</span></a>
    </nav>
    <a href="#" class="pdp-header__logo" aria-label="Barreletics home">
      <img src="barreletics-logo.png" alt="Barreletics">
    </a>
    <div class="pdp-header__util">
      <a href="#">Account</a>
      <a href="#" class="pdp-header__cart">Cart <span class="pdp-header__cart-dot"></span></a>
    </div>
  </div>
</header>

<!-- HERO -->
<section class="pg-hero-image" aria-label="Secure in every hold">
  <img class="pg-hero-image__media" src="https://barreletics.com/cdn/shop/files/IMG_2917.jpg" alt="Barreletics performance skin on foot — secure grip for barre and Pilates">
  <div class="pg-hero-image__overlay">
    <div style="max-width: 1280px; margin: 0 auto; width: 100%;">
      <p class="pg-hero-image__eyebrow" id="hero-eyebrow" style="opacity: 1;">The Pilates sock era is over.</p>
      <h1 class="pg-hero-image__title">Secure in every hold.<br>No sliding. No resets.</h1>
      <p class="pg-hero-image__body">The performance skin engineered for barre, reformer Pilates, Lagree and Megaformer. 360° grip. No latex, no silicone. Trusted by 1,000’s of instructors.</p>
      <div class="pg-hero-image__ctas">
        <a href="Barreletics Collection.html" class="pg-hero-image__cta">Shop the collection</a>
        <a href="#how-it-works" class="pg-hero-image__cta pg-hero-image__cta--ghost">See it in action ↓</a>
      </div>
    </div>
  </div>
</section>

<!-- PILLAR STRIP -->
<section class="pdp-pillars" aria-label="Why it works">
  <div class="pdp-pillars__inner">
    <span class="pdp-pillars__label">#letusknockyoursocksoff</span>
    <div class="pdp-pillars__pts">
      <span>360° Grip</span><span class="pdp-pillars__div"></span>
      <span>Two Surfaces. Zero Slip.</span><span class="pdp-pillars__div"></span>
      <span>No Mid-Class Adjustments</span><span class="pdp-pillars__div"></span>
      <span>Rinse &amp; Reuse</span><span class="pdp-pillars__div"></span>
      <span>No Latex / No Silicone</span><span class="pdp-pillars__div"></span>
      <span>Made in USA</span>
    </div>
  </div>
</section>

<!-- MEDIA SPLIT 50/50 — rotating slogans -->
<section class="v11-split">
  <div class="v11-split__media">
    <img src="https://barreletics.com/cdn/shop/files/Multi_Image.jpg" alt="Barreletics performance skin — grip from heel to toe">
  </div>
  <div class="v11-split__copy">
    <div class="v11-split__stars">★★★★★</div>
    <p class="v11-split__trusted">Trusted by 1,000’s of instructors &amp; studios</p>
    <h2 class="v11-split__slogan">Never slip in<br><strong>chair pose.</strong></h2>
    <p style="font-size:16px;line-height:1.6;color:var(--br-text-soft);margin:0 0 20px;max-width:38ch">Or side plank. Or reformer bridges. Any held position where your sock has been quietly failing you.</p>
    <a href="Barreletics Collection.html" class="v11-split__cta">Shop the collection →</a>
  </div>
</section>

<!-- PRODUCT GRID -->
<section class="pdp-section" id="shop">
  <header class="pdp-variants__head">
    <div class="pdp-variants__head-meta">
      <p class="pdp-eyebrow" style="color:var(--br-accent);margin:0">The studio collection</p>
      <h2 class="pdp-h2">Shop all colors &amp; styles.</h2>
      <p class="pdp-lede" style="margin-top:12px">Closed sole for barre &amp; reformer. Open sole for yoga &amp; mat Pilates. Same 360° grip — two builds, your call.</p>
    </div>
    <a href="Barreletics Collection.html" class="pdp-variants__head-link">See all 24 styles →</a>
  </header>
  <div class="pdp-variants__tabs" role="tablist">
    <button class="pdp-variant-tab" aria-selected="true">Closed sole</button>
    <button class="pdp-variant-tab">Open sole</button>
  </div>
  <div class="pdp-variants__grid">
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg" alt="Closed Sole Black" style="width:100%;height:100%;object-fit:cover;display:block"><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Closed Sole · Black</h3>
      <span class="pdp-vcard__meta">★★★★★ 24 verified reviews</span>
      <span class="pdp-vcard__price">$74</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png" alt="Closed Sole Dusty Rose" style="width:100%;height:100%;object-fit:cover;display:block"><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Closed Sole · Dusty Rose</h3>
      <span class="pdp-vcard__meta">18 verified reviews</span>
      <span class="pdp-vcard__price">$74</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg" alt="Closed Sole Light Grey" style="width:100%;height:100%;object-fit:cover;display:block"><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Closed Sole · Light Grey</h3>
      <span class="pdp-vcard__meta">14 verified reviews</span>
      <span class="pdp-vcard__price">$74</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
    <a href="Barreletics PDP v2.html" class="pdp-vcard" style="text-decoration:none;color:inherit">
      <div class="pdp-vcard__media" style="background:#f5f5f5"><img src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png" alt="Coperni x Barreletics Limited Edition" style="width:100%;height:100%;object-fit:cover;display:block"><span class="pdp-vcard__le">Limited Edition</span><div class="pdp-vcard__quick">Quick view</div></div>
      <h3 class="pdp-vcard__title">Coperni × Closed</h3>
      <span class="pdp-vcard__meta">Limited drop · one run</span>
      <span class="pdp-vcard__price">$115</span>
      <span class="pdp-vcard__addlink">Add to cart →</span>
    </a>
  </div>
  <div style="text-align:center;margin-top:48px;padding-top:32px;border-top:1px solid var(--br-line)">
    <a href="Barreletics Collection.html" class="pg-hero-split__cta">View all 12 colors &amp; styles</a>
    <p style="font-size:12px;color:var(--br-text-mute);letter-spacing:0.06em;margin:14px 0 0">Closed Sole · Open Sole · 6 colors each · M / L sizing</p>
  </div>
</section>

<!-- PROMO TILES — 2-box feature -->
<section style="padding:0 64px 64px;background:#fff">
  <div class="pg-promos">
    <!-- Tile 1: Limited edition color -->
    <a href="Barreletics Collection.html" class="pg-promo" style="background:#f5f0eb">
      <img style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center" src="https://barreletics.com/cdn/shop/files/Yellow.jpg" alt="Limited edition color — Rivian Green">
      <div class="pg-promo__inner">
        <p class="pg-promo__eyebrow" style="color:rgba(255,255,255,0.75)">Limited edition</p>
        <h3 class="pg-promo__title" style="color:#fff">New color.<br>Rivian Green.</h3>
        <span class="pg-promo__more" style="color:#fff">Shop now →</span>
      </div>
    </a>
    <!-- Tile 2: Yoga pants / apparel -->
    <a href="#" class="pg-promo pg-promo--dark">
      <img style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top" src="https://barreletics.com/cdn/shop/files/barrletixx_blue_pants_FINAL_d820a140-d75f-49bb-9035-77fc4dde3551.jpg" alt="Barreletics performance apparel">
      <div class="pg-promo__inner">
        <p class="pg-promo__eyebrow" style="color:rgba(255,255,255,0.65)">Now in studio</p>
        <h3 class="pg-promo__title" style="color:#fff">Performance<br>apparel.</h3>
        <span class="pg-promo__more" style="color:#fff">Shop leggings →</span>
      </div>
    </a>
  </div>
</section>

<!-- SOCK MATH -->
<style>
.sm{background:#141414;color:#fff;padding:clamp(56px,7vw,104px) clamp(24px,5vw,64px)}
.sm__inner{max-width:1280px;margin:0 auto}
.sm__head{display:flex;justify-content:space-between;align-items:flex-end;gap:28px;flex-wrap:wrap;margin-bottom:8px}
.sm__eyebrow{font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.7);margin:0 0 18px}
.sm__title{font-size:clamp(34px,4.6vw,60px);font-weight:300;letter-spacing:-0.025em;line-height:1.02;margin:0;max-width:18ch}
.sm__title strong{font-weight:600}
.sm__sub{font-size:17px;line-height:1.6;color:rgba(255,255,255,0.72);margin:20px 0 0;max-width:60ch}
.sm__toggle{display:inline-flex;border:1px solid rgba(255,255,255,0.25);flex-shrink:0}
.sm__toggle button{font-family:inherit;font-size:11.5px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:12px 22px;background:transparent;color:rgba(255,255,255,0.6);border:0;cursor:pointer;transition:.15s}
.sm__toggle button.is-on{background:#fff;color:#141414}
.sm-variant{display:none}
.sm[data-sm="a"] .sm-a{display:block}
.sm[data-sm="b"] .sm-b{display:block}
/* Design A — comparison */
.sm__cards{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.12);margin:44px 0 0}
.sm__card{background:#141414;padding:34px 32px;display:flex;flex-direction:column}
.sm__card--ours{background:#1d1d1d}
.sm__label{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin:0}
.sm__label--ours,.sm__card--ours .sm__label{color:var(--br-accent)}
.sm__price{font-size:clamp(40px,5vw,64px);font-weight:300;letter-spacing:-0.03em;line-height:1;margin:14px 0 4px}
.sm__price s{color:rgba(255,255,255,0.4);text-decoration-thickness:2px}
.sm__meta{font-size:12.5px;color:rgba(255,255,255,0.55);letter-spacing:0.03em;margin:0 0 22px}
.sm__rows{list-style:none;margin:0;padding:18px 0 0;border-top:1px solid rgba(255,255,255,0.12);display:flex;flex-direction:column;gap:13px}
.sm__row{display:flex;justify-content:space-between;align-items:baseline;gap:16px;font-size:13.5px}
.sm__row-k{color:rgba(255,255,255,0.6)}
.sm__row-v{color:rgba(255,255,255,0.85);font-weight:500;text-align:right}
.sm__card--ours .sm__row-v{color:#fff;font-weight:600}
/* slogan nest (replaces numbered grid) */
.sm__slogans{display:grid;grid-template-columns:1fr 1fr;gap:0 56px;margin:0 0 44px;border-top:1px solid rgba(255,255,255,0.14)}
.sm__slogans p{font-size:clamp(21px,2.1vw,30px);font-weight:300;letter-spacing:-0.018em;line-height:1.12;color:rgba(255,255,255,0.5);margin:0;padding:24px 0;border-bottom:1px solid rgba(255,255,255,0.1)}
.sm__slogans strong{font-weight:600;color:#fff}
.sm__slogans em{font-style:normal;font-weight:600;color:var(--br-accent)}
/* Design B — statement */
.sm-b__row{display:flex;align-items:center;justify-content:center;gap:clamp(24px,5vw,80px);margin:48px 0 0;flex-wrap:wrap}
.sm-b__col{text-align:center}
.sm-b__big{font-size:clamp(60px,9vw,132px);font-weight:200;letter-spacing:-0.045em;line-height:0.85}
.sm-b__big s{color:rgba(255,255,255,0.3);text-decoration-thickness:3px}
.sm-b__big--ours{color:var(--br-accent)}
.sm-b__cap{font-size:13px;color:rgba(255,255,255,0.6);margin:16px auto 0;letter-spacing:0.02em;max-width:24ch}
.sm-b__arrow{font-size:clamp(34px,4vw,60px);color:rgba(255,255,255,0.28);font-weight:200}
.sm-b__statement{text-align:center;font-size:clamp(44px,6.5vw,92px);font-weight:300;letter-spacing:-0.035em;margin:52px 0 0;line-height:0.95}
.sm-b__statement strong{font-weight:600}
.sm-b__stats{display:flex;justify-content:center;gap:clamp(22px,4vw,60px);margin:40px 0 44px;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,0.14);padding-top:30px}
.sm-b__stats span{font-size:12.5px;color:rgba(255,255,255,0.6);letter-spacing:0.05em;text-transform:uppercase}
.sm-b__stats b{display:block;font-size:clamp(26px,2.8vw,38px);font-weight:500;color:#fff;letter-spacing:-0.015em;margin-bottom:4px}
.sm__cta{display:inline-flex;align-items:center;gap:8px;background:#fff;color:#141414;padding:16px 30px;font-size:13px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none}
.sm__cta:hover{opacity:0.88}
@media(max-width:760px){.sm__cards,.sm__slogans{grid-template-columns:1fr}}
</style>
<section class="sm" id="sockmath" data-sm="a" aria-label="The Sock Math">
  <div class="sm__inner">
    <div class="sm__head">
      <div class="sm__headcopy">
        <p class="sm__eyebrow">The Sock Math</p>
        <h2 class="sm__title">Stop replacing.<br><strong>Start performing.</strong></h2>
      </div>
      <div class="sm__toggle" role="tablist" aria-label="Switch layout">
        <button data-v="a" class="is-on" type="button">Comparison</button>
        <button data-v="b" type="button">Statement</button>
      </div>
    </div>
    <p class="sm__sub">Grip socks have two failure points — your foot moves inside the sock, and the sock moves on the floor. Barreletics eliminates both.</p>

    <!-- DESIGN A: comparison + slogan nest -->
    <div class="sm-a sm-variant">
      <div class="sm__cards">
        <div class="sm__card">
          <p class="sm__label">Grip socks</p>
          <div class="sm__price"><s>$336</s></div>
          <p class="sm__meta">per year · 8–12 pairs at $18–28 each</p>
          <ul class="sm__rows">
            <li class="sm__row"><span class="sm__row-k">Grip lifespan</span><span class="sm__row-v">6–8 washes</span></li>
            <li class="sm__row"><span class="sm__row-k">Pairs per year</span><span class="sm__row-v">8–12</span></li>
            <li class="sm__row"><span class="sm__row-k">Foot slips inside?</span><span class="sm__row-v">Yes</span></li>
            <li class="sm__row"><span class="sm__row-k">Grip after 6 months</span><span class="sm__row-v">Cracked &amp; peeling</span></li>
          </ul>
        </div>
        <div class="sm__card sm__card--ours">
          <p class="sm__label">Barreletics</p>
          <div class="sm__price">$74</div>
          <p class="sm__meta">once · same grip from class 1 to class 1,000</p>
          <ul class="sm__rows">
            <li class="sm__row"><span class="sm__row-k">Grip lifespan</span><span class="sm__row-v">1,000+ classes</span></li>
            <li class="sm__row"><span class="sm__row-k">Pairs needed</span><span class="sm__row-v">1</span></li>
            <li class="sm__row"><span class="sm__row-k">Foot slips inside?</span><span class="sm__row-v">Impossible</span></li>
            <li class="sm__row"><span class="sm__row-k">Grip after 6 months</span><span class="sm__row-v">Identical to day 1</span></li>
          </ul>
        </div>
      </div>
      <div class="sm__slogans" style="margin-top:48px">
        <p>Socks fail. <strong>This doesn't.</strong></p>
        <p>360° grip — <em>not dots</em> that wash off.</p>
        <p>Your foot <strong>can't move inside it.</strong></p>
        <p>Same grip, <strong>class 1 to class 1,000.</strong></p>
        <p>Rinse. Dry. <strong>Reuse. Forever.</strong></p>
        <p>No latex. No silicone. <em>Made in USA.</em></p>
      </div>
      <a href="Barreletics Collection.html" class="sm__cta">Shop the collection →</a>
    </div>

    <!-- DESIGN B: statement -->
    <div class="sm-b sm-variant">
      <div class="sm-b__row">
        <div class="sm-b__col">
          <p class="sm__label">Grip socks</p>
          <div class="sm-b__big"><s>$336</s></div>
          <p class="sm-b__cap">every year — 8–12 pairs, grip cracked in 6–8 washes</p>
        </div>
        <div class="sm-b__arrow" aria-hidden="true">→</div>
        <div class="sm-b__col">
          <p class="sm__label sm__label--ours">Barreletics</p>
          <div class="sm-b__big sm-b__big--ours">$74</div>
          <p class="sm-b__cap">once — same grip on class 1 as class 1,000</p>
        </div>
      </div>
      <p class="sm-b__statement">One pair. <strong>Done.</strong></p>
      <div class="sm-b__stats">
        <span><b>1,000+</b>classes, one pair</span>
        <span><b>1</b>pair, ever</span>
        <span><b>0</b>mid-class resets</span>
        <span><b>360°</b>full-contact traction</span>
      </div>
      <div style="text-align:center"><a href="Barreletics Collection.html" class="sm__cta">Shop the collection →</a></div>
    </div>
  </div>
</section>
<script>
(function(){
  var s=document.getElementById('sockmath'); if(!s) return;
  var btns=s.querySelectorAll('.sm__toggle button');
  function set(v){ s.dataset.sm=v; try{localStorage.setItem('br_sockmath',v);}catch(e){}
    btns.forEach(function(b){var on=b.dataset.v===v;b.classList.toggle('is-on',on);b.setAttribute('aria-selected',on);}); }
  btns.forEach(function(b){ b.addEventListener('click',function(){set(b.dataset.v);}); });
  var saved='a'; try{saved=localStorage.getItem('br_sockmath')||'a';}catch(e){}
  set(saved);
})();
</script>

<!-- PHOTO SPLIT — pink group -->
<section class="v11-split" style="border-top:none;border-bottom:1px solid var(--br-line)">
  <div class="v11-split__copy" style="order:-1">
    <div class="v11-split__stars">★★★★★</div>
    <p class="v11-split__trusted">For yoga, Pilates, and barre</p>
    <h2 class="v11-split__slogan">Progress, built from<br><strong>the ground up.</strong></h2>
    <p style="font-size:16px;line-height:1.6;color:var(--br-text-soft);margin:0 0 20px;max-width:38ch">From first class to your hundredth. The grip to hold longer, push harder, and focus on form — not your feet.</p>
    <a href="Barreletics Collection.html" class="v11-split__cta">Shop the collection →</a>
  </div>
  <div class="v11-split__media">
    <img src="https://barreletics.com/cdn/shop/files/IMG_5051.jpg" alt="Barreletics performance skins — in the studio">
  </div>
</section>

<!-- 3 DISCIPLINES -->
<section class="v11-disciplines" id="disciplines">
  <div class="v11-disciplines__inner">
    <div class="v11-disciplines__head">
      <p class="v11-eyebrow">Three disciplines. One shoe.</p>
      <h2 class="v11-h2">Barre. Reformer. Megaformer. One shoe.</h2>
      <p class="v11-lede">For yoga, Pilates, and barre — on the mat or off it — the same 360° grip holds through every transition, every pose, every class.</p>
    </div>
    <div class="v11-disciplines__grid">
      <div class="v11-disc">
        <img class="v11-disc__img" src="https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=1200" alt="Barre class — Barreletics grip shoes">
        <div class="v11-disc__overlay">
          <p class="v11-disc__eyebrow">Barre</p>
          <h3 class="v11-disc__title">In the plié. In the relevé. In everything.</h3>
          <p class="v11-disc__body">Through every plié, relevé, and arabesque — heel-to-toe grip that holds. No adjusting at the barre between sets.</p>
        </div>
      </div>
      <div class="v11-disc">
        <img class="v11-disc__img" src="https://barreletics.com/cdn/shop/files/View_recent_photos.png" alt="Pilates reformer — Barreletics grip shoes">
        <div class="v11-disc__overlay">
          <p class="v11-disc__eyebrow">Reformer Pilates</p>
          <h3 class="v11-disc__title">The carriage moves. Your feet don’t.</h3>
          <p class="v11-disc__body">From footbar to carriage, footwork to bridging — the carriage moves. Your feet don’t.</p>
        </div>
      </div>
      <div class="v11-disc">
        <img class="v11-disc__img" src="https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A7000_blue_background_2.jpg" alt="Lagree Megaformer — Barreletics grip shoes">
        <div class="v11-disc__overlay">
          <p class="v11-disc__eyebrow">Lagree &amp; Megaformer</p>
          <h3 class="v11-disc__title">50 minutes. Every transition. Zero adjustments.</h3>
          <p class="v11-disc__body">Slow reps, fast transitions, 50 minutes of time under tension. Earn the shake. Not the slip.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PINK VIDEO SPLIT -->
<section class="v11-split" style="border-bottom:none">
  <div class="v11-split__media">
    <video autoplay="" loop="" muted="" playsinline="" preload="metadata" src="https://cdn.shopify.com/videos/c/o/v/d11716a75dc64da7ba1a5521e39d942b.mov" poster="https://barreletics.com/cdn/shop/files/IMG_2917.jpg?v=1741040637&amp;width=1200">
    </video>
  </div>
  <div class="v11-split__copy">
    <div class="v11-split__stars">★★★★★</div>
    <p class="v11-split__trusted">Barefoot-inspired feel — second-skin fit</p>
    <h2 class="v11-split__slogan">Never<br><strong>loses grip.</strong></h2>
    <p style="font-size:16px;line-height:1.6;color:var(--br-text-soft);margin:0 0 20px;max-width:38ch">Same grip on class 1 as class 1,000. No adjustments. No resets. Just movement.</p>
    <a href="Barreletics Collection.html" class="v11-split__cta">Shop the collection →</a>
  </div>
</section>

<!-- REVIEWS -->
<style>
.v11-rev2{padding:clamp(56px,7vw,96px) clamp(24px,5vw,64px);background:var(--br-alt-bg)}
.v11-rev2__inner{max-width:1320px;margin:0 auto}
.v11-rev2__head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:40px;padding-bottom:26px;border-bottom:1px solid var(--br-line)}
.v11-rev2__eyebrow{font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--br-accent);margin:0 0 10px}
.v11-rev2__title{font-size:clamp(26px,3vw,40px);font-weight:500;letter-spacing:-0.015em;margin:0;line-height:1.05}
.v11-rev2__summary{font-size:14px;color:var(--br-text-soft);margin:10px 0 0}
.v11-rev2__summary b{color:var(--br-text);font-weight:600}
.v11-rev2__link{font-size:12px;letter-spacing:0.1em;text-transform:uppercase;color:var(--br-text);text-decoration:none;border-bottom:1px solid var(--br-text);padding-bottom:2px;font-weight:600;white-space:nowrap}
.v11-rev2__grid{column-count:4;column-gap:16px}
@media(max-width:1100px){.v11-rev2__grid{column-count:3}}
@media(max-width:760px){.v11-rev2__grid{column-count:2}}
@media(max-width:480px){.v11-rev2__grid{column-count:1}}
.v11-rc{break-inside:avoid;margin:0 0 16px;background:#fff;border:1px solid var(--br-line);display:flex;flex-direction:column}
.v11-rc__media{overflow:hidden;position:relative}
.v11-rc__media img{width:100%;height:100%;object-fit:cover;display:block}
.v11-rc__tag{position:absolute;left:12px;bottom:12px;background:rgba(0,0,0,0.55);color:#fff;font-size:10px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;padding:5px 9px;backdrop-filter:blur(4px)}
.v11-rc__body{padding:22px 22px 24px}
.v11-rc__stars{color:var(--br-star);font-size:14px;letter-spacing:1.5px;margin-bottom:11px}
.v11-rc__badge{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:3px 8px;background:var(--br-le-bg);color:var(--br-le);margin-bottom:11px}
.v11-rc__quote{font-size:15px;line-height:1.55;color:var(--br-text);margin:0 0 15px;letter-spacing:-0.005em}
.v11-rc--media .v11-rc__quote{font-size:14px}
.v11-rc__attr{font-size:11px;font-weight:600;letter-spacing:0.07em;text-transform:uppercase;color:var(--br-text-mute)}
.v11-rev2__foot{margin-top:36px;text-align:center}
</style>
<section class="v11-rev2" id="reviews">
  <div class="v11-rev2__inner">
    <div class="v11-rev2__head">
      <div>
        <p class="v11-rev2__eyebrow">Confidence, from the ground up</p>
        <h2 class="v11-rev2__title">1,000+ reviews. 4.9 stars.</h2>
        <p class="v11-rev2__summary"><b>294 verified</b> · instructors, reformer devotees & 4-year customers</p>
      </div>
      <a href="#" class="v11-rev2__link">Read all reviews →</a>
    </div>
    <div class="v11-rev2__grid">

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:4/5"><img src="https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=900" alt="Customer in barre class wearing Barreletics" loading="lazy"><span class="v11-rc__tag">Barre · in class</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"My love-hate relationship with the sock has come to a ceremonial end. The improvement in the first minute of barre class is beyond words."</p>
          <p class="v11-rc__attr">Mia Evans · Closed Sole</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <span class="v11-rc__badge">80 helpful votes</span>
          <p class="v11-rc__quote">"I looked at these for over a year thinking 'way too expensive.' I can't tell you how much I spent on Pilates socks that ruined and stretched out. Then I got these. Game changer."</p>
          <p class="v11-rc__attr">Gwen M. · Queens, US</p>
        </div>
      </article>

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:1/1"><img src="https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A7000_blue_background_2.jpg" alt="Instructor on the reformer wearing Barreletics" loading="lazy"><span class="v11-rc__tag">Reformer · studio</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <span class="v11-rc__badge">Barre instructor</span>
          <p class="v11-rc__quote">"I teach on a variety of surfaces — these provide the perfect level of grip and support and fit like a glove. Finally a good durable barre shoe!"</p>
          <p class="v11-rc__attr">Laura P. · Sacramento, US</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"After almost a year off the foot bar due to my neuropathy, I am confidently back to the footwork series in Pilates."</p>
          <p class="v11-rc__attr">JenB · Millville, US</p>
        </div>
      </article>

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:4/5"><img src="https://barreletics.com/cdn/shop/files/Multi_Image.jpg?v=1768346625&width=900" alt="Barreletics performance skin — heel to toe grip" loading="lazy"><span class="v11-rc__tag">4-year customer</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"This is my second pair — my first purchased almost 4 years ago. The security is unmatched. I refuse to wear anything else."</p>
          <p class="v11-rc__attr">Kimberly · Knoxville, US</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"Genius concept. Simple, effective, stylish — I can improve my workout 10 fold without the nagging sock slippage and constant adjustment."</p>
          <p class="v11-rc__attr">Jess · Ashburn, US</p>
        </div>
      </article>

      <article class="v11-rc v11-rc--media">
        <div class="v11-rc__media" style="aspect-ratio:1/1"><img src="https://cdn.shopify.com/s/files/1/0045/0612/4391/files/IMG_5051.jpg" alt="Barreletics in the studio" loading="lazy"><span class="v11-rc__tag">Cadillac · age 70</span></div>
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <p class="v11-rc__quote">"The best invention known to Pilates devotees. At 70 I can accomplish advanced moves on the Cadillac — your foot has to grip the bar without fail."</p>
          <p class="v11-rc__attr">Dvorah S. · Fairfield, US</p>
        </div>
      </article>

      <article class="v11-rc">
        <div class="v11-rc__body">
          <div class="v11-rc__stars">★★★★★</div>
          <span class="v11-rc__badge">18 months use</span>
          <p class="v11-rc__quote">"I was dreading Pilates after a spinal fusion — grip socks would slip on bridges. I started looking for something that would help, and found it."</p>
          <p class="v11-rc__attr">Samantha B. · Castle Rock, US</p>
        </div>
      </article>

    </div>
    <div class="v11-rev2__foot"><a href="#" class="v11-rev2__link">Read all 294 reviews →</a></div>
  </div>
</section>

<!-- BELIEF DARK -->
<!-- COPERNI COLLAB -->
<section style="display:grid;grid-template-columns:1fr 1fr;min-height:480px">
  <!-- Left: video -->
  <div style="position:relative;overflow:hidden;background:#0a0a0a">
    <video style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" autoplay="" loop="" muted="" playsinline="" preload="metadata" src="https://cdn.shopify.com/videos/c/o/v/d7ca87eac5034642851089c63af6a2d8.mov">
    </video>
  </div>
  <!-- Right: runway model still + copy -->
  <div style="position:relative;overflow:hidden;background:#111;display:flex;flex-direction:column;justify-content:flex-end">
    <img style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;opacity:0.85" src="https://barreletics.com/cdn/shop/files/Screenshot_2026-03-20_at_6.53.30_PM.png" alt="Coperni x Barreletics — Paris runway SS26">
    <div style="position:relative;z-index:2;padding:48px 48px;background:linear-gradient(to top,rgba(0,0,0,0.88) 0%,rgba(0,0,0,0.3) 60%,transparent 100%)">
      <span style="font-size:clamp(20px,2.5vw,32px);font-weight:400;letter-spacing:-0.01em;color:rgba(255,255,255,0.9);display:block;margin-bottom:20px;font-style:normal">The Pilates sock era is over.</span>
      <span style="font-size:11px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.45);display:block;margin-bottom:14px">Limited Edition · Paris SS26</span>
      <h2 style="font-size:clamp(26px,3vw,42px);font-weight:400;letter-spacing:-0.02em;color:#fff;margin:0 0 14px;line-height:1.1">Barreletics ×<br>Coperni.</h2>
      <p style="font-size:15px;line-height:1.6;color:rgba(255,255,255,0.75);margin:0 0 28px;max-width:36ch">A Pilates shoe on the Coperni runway, Spring–Summer 2026. Closed sole. One run.</p>
      <a href="#" style="display:inline-flex;align-items:center;padding:14px 28px;background:#fff;color:#050505;font-size:13px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none">Shop the collab →</a>
    </div>
  </div>
</section>

<!-- JOURNAL PREVIEW -->
<section class="v11-journal">
  <div class="v11-journal__inner">
    <div class="v11-section-head">
      <p class="v11-eyebrow">The journal</p>
      <h2 class="v11-h2">Notes from the studio.</h2>
      <p class="v11-lede">Care guides, founder notes, and stories from the people who put performance skins to the test.</p>
    </div>
    <div class="pg-editorial-grid" style="margin-top:56px">
    <a href="Barreletics Article.html" class="pg-edit">
      <div class="pg-edit__media"><img src="https://barreletics.com/cdn/shop/files/Multi_Image.jpg" alt="How to wash your performance skins" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <p class="pg-edit__meta">Care · 3 min read</p>
      <h3 class="pg-edit__title">How to wash your performance skins.</h3>
      <p class="pg-edit__dek">The only three steps you need. Plus the one thing that quietly kills grip skins faster than anything else.</p>
    </a>
    <a href="Barreletics Article 02 Founder.html" class="pg-edit">
      <div class="pg-edit__media"><img src="https://barreletics.com/cdn/shop/products/barreletixxjumpingtogether.jpg" alt="Why we built a grip sock replacement" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <p class="pg-edit__meta">Founder · 5 min read</p>
      <h3 class="pg-edit__title">Why we built a grip-sock replacement.</h3>
      <p class="pg-edit__dek">The moment in class that made it obvious the grip sock needed to be retired. And what it took to build the replacement.</p>
    </a>
    <a href="Barreletics Article 03 Coperni.html" class="pg-edit">
      <div class="pg-edit__media"><img src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png" alt="Coperni x Barreletics in Paris" style="width:100%;height:100%;object-fit:cover;display:block"></div>
      <p class="pg-edit__meta">Story · 4 min read</p>
      <h3 class="pg-edit__title">Coperni × Barreletics, in Paris.</h3>
      <p class="pg-edit__dek">How a performance skin built for studio floors ended up closing Coperni’s Paris show.</p>
    </a>
  </div>
    <div style="text-align:center;margin-top:48px">
      <a href="Barreletics Blog.html" class="pdp-variants__head-link">Read the journal →</a>
    </div>
  </div>
</section>

<!-- GUARANTEE -->
<section class="v11-guarantee" id="guarantee">
  <div class="v11-guarantee__head">
    <h2 class="v11-guarantee__main-title" style="font-size:clamp(32px,4vw,56px);font-weight:300;letter-spacing:-0.02em">Zero risk.<br><strong style="font-weight:600">All grip.</strong></h2>
    <p style="font-size:20px;font-weight:500;color:rgba(255,255,255,0.85);margin:20px 0 0;letter-spacing:-0.01em">Try it for 30 days.</p>
    <p class="v11-guarantee__main-sub">Wear it to every class. If it’s not the best footwear decision you’ve made, return it. No questions. The product doesn’t fail — that’s why we can offer this.</p>
  </div>
  <div class="v11-guarantee__inner">
    <div>
      <p class="v11-guarantee__eyebrow">30-day confidence</p>
      <h3 class="v11-guarantee__title">30 days. Your call.</h3>
      <p class="v11-guarantee__body">Wear it to every class for 30 days. Not the best footwear decision you’ve made? Return it. No questions, no hassle.</p>
    </div>
    <div class="v11-guarantee__divider"></div>
    <div>
      <p class="v11-guarantee__eyebrow">90-day product warranty</p>
      <h3 class="v11-guarantee__title">Built to last. Backed to prove it.</h3>
      <p class="v11-guarantee__body">If the material tears or the seams fail, we replace it. No receipts, no runaround. That’s the 90-day product guarantee.</p>
    </div>
    <div class="v11-guarantee__divider"></div>
    <div>
      <p class="v11-guarantee__eyebrow">The long game</p>
      <h3 class="v11-guarantee__title">One pair. Four years. Still gripping.</h3>
      <p class="v11-guarantee__body">$74 once versus $144–$336 in socks every year. Kimberly bought her first pair 4 years ago. She’s on her second — for the color.</p>
    </div>
  </div>
</section>

<!-- NEWSLETTER -->
<section class="v11-newsletter">
  <h2>10% off your first pair.</h2>
  <p>New drops, studio stories, care tips. Once or twice a quarter. Never spam.</p>
  <form class="v11-newsletter__form" onsubmit="return false">
    <input type="email" placeholder="Email address" aria-label="Email address">
    <button type="submit">Get 10% off</button>
  </form>
</section>

<!-- FAQ (GEO-optimized) -->
<section class="pdp-section pdp-faq" id="faq" style="background:var(--br-alt-bg)">
  <p class="pdp-eyebrow" style="color:var(--br-accent);text-align:center">Common questions</p>
  <h2 class="pdp-h2" style="text-align:center">Everything you need to know.</h2>
  <div class="pdp-faq__list" style="margin-top:48px;max-width:800px;margin-left:auto;margin-right:auto">
    <details class="pdp-faq__item" open="">
      <summary class="pdp-faq__q">What makes Barreletics different from grip socks?</summary>
      <p class="pdp-faq__a">Grip socks have two failure points: the sock slips on the floor, and your foot slips inside the sock. Barreletics is a performance skin — it wraps your foot like a second skin, so interior movement is impossible. The exterior grip covers 360 degrees from heel to toe. No latex, no silicone dots, no fabric to stretch out.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">Are Barreletics good for reformer Pilates?</summary>
      <p class="pdp-faq__a">Yes — they were specifically engineered for reformer Pilates, barre, Lagree and Megaformer. The closed sole grips the footbar and carriage through every transition. Over 294 verified reviews, with Pilates instructors, reformer practitioners, and Lagree devotees all citing the reformer as their primary use case.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">How long do Barreletics last compared to grip socks?</summary>
      <p class="pdp-faq__a">Grip socks typically lose their grip after 6–8 washes. Barreletics customers report using the same pair for 1–4+ years with no grip degradation. At $74 vs $144–$336 in annual sock spending, the math strongly favors one pair of Barreletics.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">How do you clean Barreletics?</summary>
      <p class="pdp-faq__a">Warm soapy water and air dry. Never the washing machine — machine washing accelerates material breakdown. A quick rinse after class keeps them studio-fresh indefinitely.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">What size should I order?</summary>
      <p class="pdp-faq__a">Barreletics come in M (Women’s 5.5–7.5) and L (Women’s 8–11). For a more forgiving fit, size up. For men up to size 10.5, choose Large. The performance skin should sit where the ball of your foot meets your toes.</p>
    </details>
    <details class="pdp-faq__item">
      <summary class="pdp-faq__q">What is the return policy?</summary>
      <p class="pdp-faq__a">30-day returns. 90-day product warranty — if anything fails structurally, we replace it, no questions asked. We’ve never worried about making this offer because the product doesn’t fail.</p>
    </details>
  </div>
</section>

<!-- INSTAGRAM FEED -->
<section style="padding:80px 64px;background:#fff;border-top:1px solid var(--br-line)">
  <div style="max-width:1280px;margin:0 auto;text-align:center">
    <p style="font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--br-accent);margin:0 0 12px">Follow along</p>
    <h2 style="font-size:clamp(24px,3vw,36px);font-weight:400;letter-spacing:-0.02em;margin:0 0 8px">@barreletics</h2>
    <p style="font-size:15px;color:var(--br-text-soft);margin:0 0 48px">#letusknockyoursocksoff</p>
    <!-- Juicer embed -->
    <div class="juicer-feed j-initialized" data-feed-id="barreletics" data-per="9" data-truncate="300"><div class="j-loading-wrapper"><div class="j-loading">Loading...</div></div></div>
  </div>
</section>



<!-- FOOTER -->
<footer class="pdp-footer">
  <div class="pdp-footer__grid">
    <div class="pdp-footer__col pdp-footer__brand">
      <a href="#" class="pdp-header__logo" aria-label="Barreletics home">
        <img src="barreletics-logo.png" alt="Barreletics">
      </a>
      <p>The premium performance alternative to grip socks. Superior grip from heel to toe, on the floor and on your foot. Made in USA.</p>
      <p style="margin-top:14px;font-size:13px;letter-spacing:0.12em;text-transform:uppercase;color:var(--br-accent);font-weight:700">#letusknockyoursocksoff</p>
    </div>
    <div class="pdp-footer__col"><h6>Shop</h6><ul>
      <li><a href="Barreletics Collection.html">Studio collection</a></li>
      <li><a href="#">Outdoor &amp; aquatic</a></li>
      <li><a href="#">Closed vs open sole</a></li>
      <li><a href="#">Studio bundles</a></li>
      <li><a href="#">Coperni × Barreletics</a></li>
      <li><a href="#">Gift cards</a></li>
    </ul></div>
    <div class="pdp-footer__col"><h6>Support</h6><ul>
      <li><a href="#">Size chart</a></li>
      <li><a href="#">Care guide</a></li>
      <li><a href="#">Shipping &amp; returns</a></li>
      <li><a href="#">30-day confidence guarantee</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Contact</a></li>
    </ul></div>
    <div class="pdp-footer__col"><h6>Journal</h6><ul>
      <li><a href="Barreletics Blog.html">All articles</a></li>
      <li><a href="#">How to wash your skins</a></li>
      <li><a href="#">Founder story</a></li>
      <li><a href="#">Coperni × Barreletics</a></li>
      <li><a href="#">About Barreletics</a></li>
      <li><a href="#">Become an affiliate</a></li>
    </ul></div>
    <div class="pdp-footer__col"><h6>Follow</h6><ul>
      <li><a href="#">Instagram</a></li>
      <li><a href="#">TikTok</a></li>
      <li><a href="#">YouTube</a></li>
      <li><a href="#">Pinterest</a></li>
    </ul></div>
  </div>
  <div class="pdp-footer__bottom">
    <span>© 2026 Barreletics. All rights reserved. Made in USA.</span>
    <span><a href="#" style="color:inherit;text-decoration:none">Privacy</a> · <a href="#" style="color:inherit;text-decoration:none">Terms</a> · <a href="#" style="color:inherit;text-decoration:none">Accessibility</a></span>
  </div>
</footer>

<script>
// Rotating ticker — cross-fades messages every 5s
(function () {
  const ticker = document.querySelector('.pdp-ticker');
  if (!ticker) return;
  const slides = ticker.querySelectorAll('.pdp-ticker__slide');
  if (slides.length < 2) return;
  let i = 0;
  setInterval(() => {
    slides[i].classList.remove('is-active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('is-active');
  }, 5000);
})();

</script>

<script>
// Rotating slogans on media split
const slogans = [
  "Socks fail. This doesn’t.",
  "Secure in every hold. No sliding. No resets.",
  "Your foot moves in the sock. The sock moves on the floor. Now neither does.",
  "Stop adjusting. Move.",
  "Built for the move, not the pose.",
  "Earn the shake. Not the slip.",
  "For people who call it their practice.",
  "Five days a week. Zero compromises."
];
let idx = 0;
const el = document.getElementById('rotating-slogan');
if (el) {
  setInterval(() => {
    el.style.opacity = '0';
    setTimeout(() => {
      idx = (idx + 1) % slogans.length;
      el.textContent = slogans[idx];
      el.style.opacity = '1';
    }, 400);
  }, 4000);
}
</script>

<script>

// Hero eyebrow rotation
const eyebrows = [
  "The Pilates sock era is over.",
  "A new kind of grip shoe.",
  "Trusted by 1,000’s of instructors.",
  "Made in USA. Built for the carriage.",
  "Barre. Reformer. Megaformer. One shoe."
];
let eidx = 0;
const eyebrowEl = document.getElementById('hero-eyebrow');
if (eyebrowEl) {
  setInterval(() => {
    eyebrowEl.style.opacity = '0';
    setTimeout(() => {
      eidx = (eidx + 1) % eyebrows.length;
      eyebrowEl.textContent = eyebrows[eidx];
      eyebrowEl.style.opacity = '1';
    }, 300);
  }, 3500);
}

// Second rotating slogan — video split
const slogans2 = [
  "Your foot moves in the sock. The sock moves on the floor. Now neither does.",
  "The Pilates sock era is over.",
  "50 minutes. Every transition. Zero adjustments.",
  "Built for the move, not the pose.",
  "Stop adjusting. Start moving.",
  "For people who call it their practice."
];
let idx2 = 0;
const el2 = document.getElementById('rotating-slogan-2');
if (el2) {
  setInterval(() => {
    el2.style.opacity = '0';
    setTimeout(() => {
      idx2 = (idx2 + 1) % slogans2.length;
      el2.textContent = slogans2[idx2];
      el2.style.opacity = '1';
    }, 400);
  }, 5000);
}
</script>


</body></html>