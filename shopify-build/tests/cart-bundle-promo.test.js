'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

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

function pantItem(qty) {
  return {
    quantity: qty,
    final_line_price: 8900 * qty,
    product_title: 'Lightly Padded Knee Yoga Pant',
    product_type: 'Apparel',
    variant_title: 'Black · M',
    url: '/products/high-waist-yoga-pant'
  };
}

var FUTURE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'future_tiers' });
var LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

test('flag off hides panel', function () {
  var r = bundle.computeBundlePromo([skinItem(2, 7400)], { enabled: false }, 14800);
  assert.equal(r.showPanel, false);
});

test('future: 2 pairs — 10% savings $14.80 and tier-3 nudge', function () {
  var items = [skinItem(1, 7400), skinItem(1, 7400)];
  var r = bundle.computeBundlePromo(items, FUTURE, 14800);
  assert.equal(r.pairSavingsCents, 1480);
  assert.equal(r.nudge, 'Add 1 pair. Save 15%.');
  assert.equal(r.savingsLine, 'You save $14.80.');
  assert.equal(r.estimatedTotalCents, 13320);
  assert.equal(r.shippingGapCents, 1680);
});

test('live control: 1 pair footwear line, pants qual-only (default arm)', function () {
  var r = bundle.computeBundlePromo([skinItem(1, 7400)], LIVE, 7400);
  assert.equal(r.offerArm, 'control');
  assert.equal(r.nudge, '');
  assert.equal(r.footwearOfferLine, 'Buy 2+ Closed Sole pairs. Save 15%.');
  assert.equal(r.showPantsOffer, true);
  assert.equal(r.pantsQualOnly, true);
  assert.equal(r.totalSavingsCents, 0);
});

test('live variant: 1 pair add-pair stage only', function () {
  var r = bundle.computeBundlePromo([skinItem(1, 7400)], LIVE, 7400, VARIANT);
  assert.equal(r.offerArm, 'variant');
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, false);
});

test('live: 2 pairs — 15% savings, no nudge', function () {
  var r = bundle.computeBundlePromo([skinItem(2, 7400)], LIVE, 14800);
  assert.equal(r.pairSavingsCents, 2220);
  assert.equal(r.nudge, '');
});

test('variant: pants offer hidden at 1 pair (progressive stage)', function () {
  var r = bundle.computeBundlePromo([skinItem(1, 7400)], FUTURE, 7400, VARIANT);
  assert.equal(r.showPantsOffer, false);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.pantsPickerVisible, false);
});

test('pants picker at 2+ pairs with proposed $98 / 35%', function () {
  var r = bundle.computeBundlePromo([skinItem(2, 7400)], FUTURE, 14800, VARIANT);
  assert.equal(r.pantsPickerVisible, true);
  assert.equal(r.pantsSaleCents, 6370);
  assert.equal(
    r.pantsOfferLine,
    'Save 35% on one pair of yoga pants with 2+ Performance Skin pairs.'
  );
});

test('one pant in cart — one unit savings only', function () {
  var items = [skinItem(2, 7400), pantItem(2)];
  var r = bundle.computeBundlePromo(items, FUTURE, 14800 + 17800);
  assert.equal(r.pantsSavingsCents, 3430);
  assert.equal(r.totalSavingsCents, 1480 + 3430);
});

test('percent edit updates headline and sale price (variant arm)', function () {
  var cfg = bundle.mergeConfig({ enabled: true, pantsPercent: 30, pantsProposedPriceCents: 10000 });
  var r = bundle.computeBundlePromo([skinItem(2, 7400)], cfg, 14800, VARIANT);
  assert.equal(
    r.pantsOfferLine,
    'Save 30% on one pair of yoga pants with 2+ Performance Skin pairs.'
  );
  assert.equal(bundle.pantsSaleCents(cfg), 7000);
});

test('variant: open sole counts toward pair stages', function () {
  var openSole = {
    quantity: 2,
    final_line_price: 14800,
    product_title: 'Performance Skins — Open Sole',
    url: '/products/studio-performance-skin-footwear'
  };
  var r = bundle.computeBundlePromo([openSole], FUTURE, 14800, VARIANT);
  assert.equal(r.pairCount, 2);
  assert.equal(r.showPanel, true);
  assert.equal(r.showPantsOffer, true);
});

test('control: open sole excluded from pair count', function () {
  var openSole = {
    quantity: 2,
    final_line_price: 14800,
    product_title: 'Performance Skins — Open Sole',
    url: '/products/studio-performance-skin-footwear'
  };
  var r = bundle.computeBundlePromo([openSole], FUTURE, 14800);
  assert.equal(r.pairCount, 0);
  assert.equal(r.showPanel, false);
});

test('resolveVariantFromOptions matches size and color', function () {
  var variants = [
    { id: 1, option1: 'Small (2-4)', option2: 'Black' },
    { id: 2, option1: 'Medium (6-8)', option2: 'Black' }
  ];
  var v = bundle.resolveVariantFromOptions(variants, { option1: 'Medium (6-8)', option2: 'Black' });
  assert.equal(v.id, 2);
});

test('HTML render includes progress, savings, pants prices', function () {
  var r = bundle.computeBundlePromo([skinItem(2, 7400)], FUTURE, 14800);
  var html = bundle.renderPromoHtml(r);
  assert.match(html, /cart-bundle-promo__progress/);
  assert.match(html, /You save \$14\.80/);
  assert.match(html, /\$98\.00/);
  assert.match(html, /\$63\.70/);
});
