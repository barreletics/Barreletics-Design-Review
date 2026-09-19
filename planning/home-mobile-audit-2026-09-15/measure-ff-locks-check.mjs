import { chromium } from 'playwright';
import fs from 'fs';
const URL = 'https://barreletics.myshopify.com/?preview_theme_id=187144929571';
const outDir = '/Users/andrewnehra/Documents/GitHub/🔵  Barreletics-Design-Review/planning/home-mobile-audit-2026-09-15';
const browser = await chromium.launch({ headless: true, channel: 'chrome' });
const page = await browser.newPage();
await page.setViewportSize({ width: 390, height: 844 });
await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);
for (let i=0;i<3;i++){
  const c=await page.evaluate(()=>{for(const b of document.querySelectorAll('button,[role=button]')){const t=(b.innerText||'').toLowerCase();if(t.includes('accept')||t==='got it'||t==='decline'){b.click();return t}}return null});
  if(c) await page.waitForTimeout(300); else break;
}
await page.addStyleTag({content:`#PreviewBarContainer,.preview-bar,#shopify-preview-bar,iframe#preview-bar-iframe,.shopify-pc__banner,#shopify-pc__banner,[id*=shopify-pc]{display:none!important}`});

const data = await page.evaluate(()=>{
  const by=s=>[...document.querySelectorAll('[id^=shopify-section]')].find(e=>e.id.endsWith(s));
  const m=(name,suf)=>{
    const root=by(suf);
    if(!root) return {name, missing:true};
    const frame=root.querySelector('.split-section, .section-frame, .press-feature');
    const media=root.querySelector('.split-media, .press-feature__media');
    const text=root.querySelector('.split-text, .press-feature__copy');
    const img=media?.querySelector('img');
    const vars={
      ffMob: frame ? getComputedStyle(frame).getPropertyValue('--ff-mobile-media-height').trim() : null,
      ffText: frame ? getComputedStyle(frame).getPropertyValue('--ff-mobile-text-height').trim() : null,
      pfMob: frame ? getComputedStyle(frame).getPropertyValue('--pf-mobile-media-height').trim() : null,
      pfText: frame ? getComputedStyle(frame).getPropertyValue('--pf-mobile-text-height').trim() : null,
    };
    const mr=media?.getBoundingClientRect();
    const tr=text?.getBoundingClientRect();
    const ir=img?.getBoundingClientRect();
    const ics=img?getComputedStyle(img):null;
    const mcs=media?getComputedStyle(media):null;
    const tcs=text?getComputedStyle(text):null;
    return {
      name,
      vars,
      mediaH: Math.round(mr?.height||0),
      mediaMinH: mcs?.minHeight||null,
      mediaMaxH: mcs?.maxHeight||null,
      textH: Math.round(tr?.height||0),
      textMinH: tcs?.minHeight||null,
      objectFit: ics?.objectFit||null,
      objectPosition: ics?.objectPosition||null,
      imgH: Math.round(ir?.height||0),
      imgW: Math.round(ir?.width||0),
      overflowX: Math.max(0, Math.round((mr?.right||0)-innerWidth)),
      src: (img?.currentSrc||img?.src||'').split('?')[0].split('/').pop()||null,
    };
  };
  return {
    Grip: m('Grip','__fifty-fifty-grip'),
    OnePair: m('One Pair','__fifty-fifty-one-pair'),
    Interni: m('Interni','__press-feature-interni'),
  };
});
fs.writeFileSync(`${outDir}/ff-locks-after-interni-chatgpt.json`, JSON.stringify(data, null, 2));
console.log(JSON.stringify(data, null, 2));
await browser.close();
