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
    const tcs=text?getComputedStyle(text):null;
    const ics=img?getComputedStyle(img):null;
    const st=root.querySelector('[style]')?.getAttribute('style')||root.querySelector('.press-feature,.split-section')?.getAttribute('style')||'';
    const frame=root.querySelector('.press-feature--split,.split-section,.section-frame') || root.firstElementChild;
    const frameStyle=frame?.getAttribute('style')||'';
    return {
      label,
      sectionId: root.id,
      mediaH: Math.round(mr?.height||0),
      mediaW: Math.round(mr?.width||0),
      overflowX: Math.max(0, Math.round((mr?.right||0)-innerWidth)),
      textH: Math.round(tr?.height||0),
      textMinH: tcs?.minHeight||null,
      justify: tcs?.justifyContent||null,
      padT: tcs?.paddingTop||null,
      padB: tcs?.paddingBottom||null,
      objectFit: ics?.objectFit||null,
      bodyFontSize: (()=>{
        const b=text?.querySelector('.press-feature__body, .split-section__body, p, .type-body');
        return b?getComputedStyle(b).fontSize:null;
      })(),
      imgOverflowW: img&&media?Math.round(ir.width-mr.width):null,
      imgOverflowH: img&&media?Math.round(ir.height-mr.height):null,
      naturalW: img?.naturalWidth||null,
      naturalH: img?.naturalHeight||null,
      imgW: Math.round(ir?.width||0),
      imgH: Math.round(ir?.height||0),
      mediaBg: mcs?.backgroundColor||null,
      fullWidthVisible: img&&media ? (ics?.objectFit==='contain' && Math.abs(ir.width-mr.width)<2) || (ics?.objectFit==='contain' && ir.width<=mr.width+1) : null,
      mediaMaxH: mcs?.maxHeight||null,
      mediaOverflow: mcs?.overflow||null,
      inlineVars: {
        pfMob: getComputedStyle(frame||root).getPropertyValue('--pf-mobile-media-height').trim()||null,
        pfText: getComputedStyle(frame||root).getPropertyValue('--pf-mobile-text-height').trim()||null,
        pfPadT: getComputedStyle(frame||root).getPropertyValue('--pf-text-pad-top-m').trim()||null,
        pfPadB: getComputedStyle(frame||root).getPropertyValue('--pf-text-pad-bottom-m').trim()||null,
        pfBody: getComputedStyle(frame||root).getPropertyValue('--pf-body-size').trim()||null,
        ffMob: getComputedStyle(frame||root).getPropertyValue('--ff-mobile-media-height').trim()||null,
        ffText: getComputedStyle(frame||root).getPropertyValue('--ff-mobile-text-height').trim()||null,
      },
      frameStyleSnippet: (frameStyle||'').slice(0,220)
    };
  };
  return {
    Interni: measure('Interni','__press-feature-interni','.press-feature__media','.press-feature__copy'),
    Grip: measure('Grip','__fifty-fifty-grip','.split-section__media, .fifty-fifty__media, [class*=media]','.split-section__copy, .fifty-fifty__copy, [class*=copy]'),
    OnePair: measure('One Pair','__fifty-fifty-one-pair','.split-section__media, .fifty-fifty__media, [class*=media]','.split-section__copy, .fifty-fifty__copy, [class*=copy]'),
  };
});

await page.evaluate(()=>{const el=[...document.querySelectorAll('[id^=shopify-section]')].find(e=>e.id.endsWith('__press-feature-interni'));el?.scrollIntoView({block:'start'})});
await page.waitForTimeout(500);
await page.locator('[id$="__press-feature-interni"]').screenshot({path:`${outDir}/interni-640-fit-390.png`});

const out={theme, viewport:{w:390,h:844}, data, at:new Date().toISOString()};
fs.writeFileSync(`${outDir}/interni-640-fit-measure-390.json`, JSON.stringify(out,null,2));
console.log(JSON.stringify(out,null,2));
await browser.close();
