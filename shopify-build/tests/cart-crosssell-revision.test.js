'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const bundle = require('../assets/cart-bundle-promo.js');

function skinItem(qty, priceCents) {
  return {
    quantity: qty,
    final_line_price: priceCents * qty,
    product_title: 'Performance Skins — Closed Sole',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M',
    url: '/products/studio-performance-skin-closed-sole'
  };
}

const LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
const FUTURE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'future_tiers' });
const VARIANT = { offerArm: 'variant' };

function htmlAt(items, cfg, total) {
  const r = bundle.computeBundlePromo(items, cfg, total);
  return { r, html: bundle.renderPromoHtml(r) };
}

test('0 Closed Sole pairs: panel hidden', () => {
  const r = bundle.computeBundlePromo([], LIVE, 0);
  assert.equal(r.showPanel, false);
});

test('live control 1 pair: preview notice, pants photo, no picker', () => {
  const { r, html } = htmlAt([skinItem(1, 7400)], LIVE, 7400);
  assert.equal(r.offerArm, 'control');
  assert.equal(r.footwearOfferLine, 'Buy 2+ Closed Sole pairs. Save 15%.');
  assert.equal(r.pantsPickerVisible, false);
  assert.match(html, /Preview only—offers aren't applied at checkout/);
  assert.match(html, /cart-bundle-promo__pants-img/);
  assert.ok(!html.includes('data-bundle-add-pair'));
});

test('live variant 1 pair: add-pair flow only', () => {
  const items = [skinItem(1, 7400)];
  const r = bundle.computeBundlePromo(items, LIVE, 7400, VARIANT);
  const html = bundle.renderPromoHtml(r);
  assert.equal(r.showAddPairStage, true);
  assert.match(html, /Buy 2 or more pairs\. Get 15% off\./);
  assert.match(html, /data-open-add-pair-picker/);
  assert.ok(!html.includes('cart-bundle-promo__pants-img'));
});

test('live control 2 pairs: picker allowed, closed-sole footwear line', () => {
  const { r, html } = htmlAt([skinItem(2, 7400)], LIVE, 14800);
  assert.equal(r.pantsPickerVisible, true);
  assert.equal(r.footwearOfferLine, 'Buy 2+ Closed Sole pairs. Save 15%.');
  assert.match(html, /data-bundle-pants-picker/);
  assert.equal(r.nudge, '');
});

test('pant already in cart: no pants cross-sell block', () => {
  const pant = {
    quantity: 1,
    final_line_price: 8900,
    product_title: 'Yoga Pant',
    url: '/products/lightly-padded-knee-yoga-pant-black'
  };
  const r = bundle.computeBundlePromo([skinItem(2, 7400), pant], LIVE, 23700);
  assert.equal(r.showPantsOffer, false);
});

test('future control: footwear line at 1+ closed pairs', () => {
  const r1 = bundle.computeBundlePromo([skinItem(1, 7400)], FUTURE, 7400);
  assert.equal(r1.footwearOfferLine, 'Buy 2+ Closed Sole pairs. Save 10%.');
  const r2 = bundle.computeBundlePromo([skinItem(2, 7400)], FUTURE, 14800);
  assert.equal(r2.footwearOfferLine, 'Buy 2+ Closed Sole pairs. Save 10%.');
});

test('visual preview HTML has no discount auto-apply links', () => {
  const { html } = htmlAt([skinItem(2, 7400)], LIVE, 14800);
  assert.ok(!html.includes('/discount/'));
});

test('source does not hardcode SAVE2 2FOR15 or pants promo codes', () => {
  const fs = require('fs');
  const path = require('path');
  const js = fs.readFileSync(path.join(__dirname, '../assets/cart-bundle-promo.js'), 'utf8');
  assert.ok(!js.includes('SAVE2'));
  assert.ok(!js.includes('2FOR15'));
});

test('config percent edits sync footwear and pants copy', () => {
  const cfg = bundle.mergeConfig({
    enabled: true,
    livePairPercent: 20,
    pantsPercent: 40
  });
  const r = bundle.computeBundlePromo([skinItem(2, 7400)], cfg, 14800);
  assert.equal(r.footwearOfferLine, 'Buy 2+ Closed Sole pairs. Save 20%.');
  assert.equal(
    r.pantsOfferLine,
    'Save 40% on one pair of yoga pants with 2+ Closed Sole pairs.'
  );
});
