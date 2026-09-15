import { chromium } from 'playwright';
import fs from 'fs';

const URL = 'https://barreletics.myshopify.com/?preview_theme_id=187144929571';
const SECTIONS = [
  { suffix: '__split_hero', name: 'split_hero', andrew: 'Hero shot', mediaSel: '.split-hero__media', bodySel: '.split-hero__body' },
  { suffix: '__fifty-fifty-grip', name: 'fifty-fifty-grip', andrew: 'Snack/Never loses (video 50/50)', mediaSel: '.split-media', bodySel: '.split-text__body' },
  { suffix: '__collab-hero', name: 'collab-hero', andrew: 'Coperni video', mediaSel: '.collab-hero__stage, .collab-hero__media-wrap, .collab-hero__video-wrap, .collab-hero video, .collab-hero', bodySel: '.collab-hero__body' },
  { suffix: '__fullbleed-statement', name: 'fullbleed-statement', andrew: 'Full bleed', mediaSel: '.fullbleed-statement, .fullbleed-statement__media, [class*="fullbleed"]', bodySel: null },
  { suffix: '__fifty-fifty-one-pair', name: 'fifty-fifty-one-pair', andrew: 'One Pair (ruler)', mediaSel: '.split-media', bodySel: '.split-text__body' },
  { suffix: '__statement-band', name: 'statement-band', andrew: 'Knock/snack socks off (text band)', mediaSel: '.statement-band, .statement-band__inner', bodySel: '.statement-band__title, .type-statement, h2' },
];

async function measureViewport(page, label, width, height) {
  await page.setViewportSize({ width, height });
  await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(4000);
  const out = {};
  for (const s of SECTIONS) {
    const data = await page.evaluate(({ suffix, mediaSel, bodySel }) => {
      const root = [...document.querySelectorAll('[id^="shopify-section"]')].find(el => el.id.endsWith(suffix));
      if (!root) return { missing: true };
      let media = null;
      for (const sel of mediaSel.split(',').map(x => x.trim())) {
        media = root.querySelector(sel);
        if (media) break;
      }
      media = media || root;
      const body = bodySel ? root.querySelector(bodySel) : null;
      const mr = media.getBoundingClientRect();
      const rr = root.getBoundingClientRect();
      const cs = getComputedStyle(media);
      const bcs = body ? getComputedStyle(body) : null;
      const frame = root.querySelector('.split-section, .split-hero, .collab-hero, .fullbleed-statement, .statement-band');
      const fcs = frame ? getComputedStyle(frame) : null;
      const textEl = root.querySelector('.split-text, .split-hero__copy, .collab-hero__overlay, .collab-hero__editorial-copy, .statement-band__copy');
      const tcs = textEl ? getComputedStyle(textEl) : null;
      const tr = textEl ? textEl.getBoundingClientRect() : null;
      return {
        sectionId: root.id,
        rootH: Math.round(rr.height),
        mediaH: Math.round(mr.height),
        mediaW: Math.round(mr.width),
        textH: tr ? Math.round(tr.height) : null,
        textMinH: tcs ? tcs.minHeight : null,
        minHeight: cs.minHeight,
        frameMinH: fcs ? fcs.minHeight : null,
        bodyFontSize: bcs ? bcs.fontSize : null,
        textPad: tcs ? { padT: tcs.paddingTop, padB: tcs.paddingBottom, padL: tcs.paddingLeft, padR: tcs.paddingRight } : null,
        inlineVars: frame ? {
          ffMin: frame.style.getPropertyValue('--ff-min-height') || null,
          ffMob: frame.style.getPropertyValue('--ff-mobile-media-height') || null,
          ffText: frame.style.getPropertyValue('--ff-mobile-text-height') || null,
          shScale: frame.style.getPropertyValue('--sh-height-scale') || null,
          chDesk: frame.style.getPropertyValue('--ch-height-desktop') || null,
        } : null,
      };
    }, s);
    out[s.name] = { andrew: s.andrew, ...data };
  }
  return { label, width, height, sections: out };
}

const browser = await chromium.launch({ headless: true, channel: 'chrome' });
const page = await browser.newPage();
const desktop = await measureViewport(page, 'desktop_1280', 1280, 900);
const mobile = await measureViewport(page, 'mobile_390', 390, 844);

// pull-verify remote JSON settings via page? skip — use shopify pull instead
await browser.close();

const result = {
  theme: 187144929571,
  url: URL,
  measured_at: new Date().toISOString(),
  before_from_diag: {
    desktop_1280: { grip_mediaH: 720, one_pair_mediaH: 853, hero_note: '92vh locked (~828 @900vh)' },
    mobile_390: { grip_mediaH: 640, one_pair_mediaH: 520 },
  },
  after: { desktop, mobile },
};
fs.writeFileSync('measure.json', JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
