import { chromium } from 'playwright';
import fs from 'fs';
const URL = 'https://barreletics.myshopify.com/?preview_theme_id=187144929571';
const outDir = '/Users/andrewnehra/Documents/GitHub/🔵  Barreletics-Design-Review/planning/home-mobile-audit-2026-09-15';
const browser = await chromium.launch({ headless: true, channel: 'chrome' });
const page = await browser.newPage();
await page.setViewportSize({ width: 390, height: 844 });
await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(5000);
for (let i=0;i<4;i++){
  const c=await page.evaluate(()=>{for(const b of document.querySelectorAll('button,[role=button]')){const t=(b.innerText||'').toLowerCase();if(t.includes('accept')||t==='got it'||t==='decline'){b.click();return t}}return null});
  if(c) await page.waitForTimeout(400); else break;
}
await page.addStyleTag({content:`#PreviewBarContainer,.preview-bar,#shopify-preview-bar,iframe#preview-bar-iframe,.shopify-pc__banner,#shopify-pc__banner,[id*=shopify-pc]{display:none!important}`});

const theme = await page.evaluate(()=>({name:Shopify?.theme?.name,id:Shopify?.theme?.id}));

await page.evaluate(()=>{const el=[...document.querySelectorAll('[id^=shopify-section]')].find(e=>e.id.endsWith('__press-feature-interni'));el?.scrollIntoView({block:'start'})});
await page.waitForTimeout(800);

const data = await page.evaluate(()=>{
  const by=s=>[...document.querySelectorAll('[id^=shopify-section]')].find(e=>e.id.endsWith(s));
  const measure=(label, rootSel, mediaSel, textSel)=>{
    const root=by(rootSel);
    if(!root) return {label, missing:true};
    const media=root.querySelector(mediaSel);
    const text=root.querySelector(textSel);
    const img=media?.querySelector('img');
    const mr=media?.getBoundingClientRect();
    const tr=text?.getBoundingClientRect();
    const ir=img?.getBoundingClientRect();
    const mcs=media?getComputedStyle(media):null;
    const ics=img?getComputedStyle(img):null;
    return {
      label,
      sectionId: root.id,
      mediaH: Math.round(mr?.height||0),
      mediaW: Math.round(mr?.width||0),
      overflowX: Math.max(0, Math.round((mr?.right||0)-innerWidth)),
      docOverflowX: Math.max(0, document.documentElement.scrollWidth - innerWidth),
      textH: Math.round(tr?.height||0),
      objectFit: ics?.objectFit||null,
      objectPosition: ics?.objectPosition||null,
      imgOverflowW: img&&media?Math.round(ir.width-mr.width):null,
      imgOverflowH: img&&media?Math.round(ir.height-mr.height):null,
      naturalW: img?.naturalWidth||null,
      naturalH: img?.naturalHeight||null,
      imgW: Math.round(ir?.width||0),
      imgH: Math.round(ir?.height||0),
      src: img?.currentSrc || img?.src || null,
      mediaBg: mcs?.backgroundColor||null,
    };
  };
  return {
    Interni: measure('Interni','__press-feature-interni','.press-feature__media','.press-feature__copy'),
    Grip: measure('Grip','__fifty-fifty-grip','.split-section__media, .fifty-fifty__media, [class*=media]','.split-section__copy, .fifty-fifty__copy, [class*=copy]'),
    OnePair: measure('One Pair','__fifty-fifty-one-pair','.split-section__media, .fifty-fifty__media, [class*=media]','.split-section__copy, .fifty-fifty__copy, [class*=copy]'),
  };
});

await page.screenshot({ path: `${outDir}/interni-chatgpt-cover-390.png`, fullPage: false });

const masthead = await page.evaluate(()=>{
  const root=[...document.querySelectorAll('[id^=shopify-section]')].find(e=>e.id.endsWith('__press-feature-interni'));
  const img=root?.querySelector('.press-feature__media img');
  if(!img) return null;
  const media=root.querySelector('.press-feature__media');
  const mr=media.getBoundingClientRect();
  const scale = Math.max(mr.width/img.naturalWidth, mr.height/img.naturalHeight);
  const dispW = img.naturalWidth * scale;
  const dispH = img.naturalHeight * scale;
  const cropX = (dispW - mr.width)/2;
  const cropY = (dispH - mr.height)/2;
  return {
    natural: [img.naturalWidth, img.naturalHeight],
    media: [Math.round(mr.width), Math.round(mr.height)],
    scale: +scale.toFixed(4),
    cropX: Math.round(cropX),
    cropY: Math.round(cropY),
    topOfImageVisible: cropY < 1,
    sidesCropped: cropX > 1,
    srcHasChatgpt: (img.currentSrc||img.src||'').includes('chatgpt-editorial-clean'),
    objectFit: getComputedStyle(img).objectFit,
    objectPosition: getComputedStyle(img).objectPosition,
  };
});

const result = { theme, viewport: {w:390,h:844}, ...data, masthead, measuredAt: new Date().toISOString() };
fs.writeFileSync(`${outDir}/interni-chatgpt-cover-measure-390.json`, JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
await browser.close();
