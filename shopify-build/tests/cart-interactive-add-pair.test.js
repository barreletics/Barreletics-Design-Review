'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

var LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });

function closedSkin(qty, color) {
  return {
    quantity: qty,
    final_line_price: 7400 * qty,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: (color || 'Purple') + ' · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes'
  };
}

function openSkin(qty, color) {
  return {
    quantity: qty,
    final_line_price: 7400 * qty,
    product_title: 'Open Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: 'M (W 5.5-7.5) / ' + (color || 'Black'),
    url: '/products/studio-performance-skin-footwear'
  };
}

function pantItem() {
  return {
    quantity: 1,
    final_line_price: 8900,
    product_title: 'Yoga Pant',
    url: '/products/lightly-padded-knee-yoga-pant-black'
  };
}

var FIXTURE_PRODUCT = {
  options: [
    { name: 'Size', position: 1, values: ['M (W 5.5-7.5)', 'L (W 8-11)'] },
    { name: 'Color', position: 2, values: ['Purple', 'Black', 'White'] }
  ],
  variants: [
    { id: 101, option1: 'M (W 5.5-7.5)', option2: 'Purple', available: true },
    { id: 102, option1: 'M (W 5.5-7.5)', option2: 'Black', available: true },
    { id: 103, option1: 'M (W 5.5-7.5)', option2: 'White', available: false },
    { id: 104, option1: 'L (W 8-11)', option2: 'Black', available: true }
  ]
};

test('at 1 pair: add-pair stage on, pants offer off', function () {
  var r = bundle.computeBundlePromo([closedSkin(1, 'Purple')], LIVE, 7400);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, false);
  assert.equal(r.footwearOfferLine, '');
});

test('at 2+ pairs: pants stage on, add-pair off', function () {
  var mixed = [closedSkin(1, 'Purple'), openSkin(1, 'Black')];
  var r = bundle.computeBundlePromo(mixed, LIVE, 14800);
  assert.equal(r.showAddPairStage, false);
  assert.equal(r.showPantsOffer, true);
  assert.equal(r.pantsPickerVisible, true);
  assert.match(r.footwearOfferLine, /Save 15%/);
});

test('pants not counted as footwear pairs', function () {
  var r = bundle.computeBundlePromo([pantItem()], LIVE, 8900);
  assert.equal(r.showPanel, false);
});

test('1 pant in cart suppresses second pants offer at 2 pairs', function () {
  var items = [closedSkin(2, 'Purple'), pantItem()];
  var r = bundle.computeBundlePromo(items, LIVE, 23700);
  assert.equal(r.showPantsOffer, false);
});

test('normalizeColorLabel treats LightGrey as light grey', function () {
  assert.equal(bundle.normalizeColorLabel('LightGrey'), 'light grey');
  assert.equal(bundle.normalizeColorLabel('light grey'), 'light grey');
});

test('colorsUsedInCart excludes duplicate color offers', function () {
  var used = bundle.colorsUsedInCart([closedSkin(1, 'Purple'), openSkin(1, 'Black')], LIVE);
  assert.equal(used['purple'], true);
  assert.equal(used['black'], true);
  var meta = bundle.colorValuesForProduct(FIXTURE_PRODUCT, used);
  assert.deepEqual(meta.colors, ['White']);
});

test('render at 1 pair: exact headline, no pants image', function () {
  var r = bundle.computeBundlePromo([closedSkin(1)], LIVE, 7400);
  var html = bundle.renderPromoHtml(r);
  assert.match(html, /Add one more pair of Performance Skins/);
  assert.match(html, /data-bundle-add-pair/);
  assert.match(html, /Preview only—offers aren't applied at checkout/);
  assert.ok(!html.includes('cart-bundle-promo__pants-img'));
  assert.ok(!html.includes('unlock'));
});

test('render at 2 pairs includes pants block and preview savings', function () {
  var r = bundle.computeBundlePromo([closedSkin(2)], LIVE, 14800);
  var html = bundle.renderPromoHtml(r);
  assert.match(html, /cart-bundle-promo__pants-img/);
  assert.match(html, /data-bundle-pants-picker/);
  assert.match(html, /You save/);
});

test('sizesForColor respects availability flag', function () {
  var rows = bundle.sizesForColor(FIXTURE_PRODUCT.variants, 'option2', 'White', 'option1');
  assert.equal(rows.length, 1);
  assert.equal(rows[0].available, false);
  var blackRows = bundle.sizesForColor(FIXTURE_PRODUCT.variants, 'option2', 'Black', 'option1');
  assert.equal(blackRows.length, 2);
  assert.equal(blackRows[0].available, true);
});

test('no discount redirect links in rendered html', function () {
  var r = bundle.computeBundlePromo([closedSkin(2)], LIVE, 14800);
  var html = bundle.renderPromoHtml(r);
  assert.ok(!html.includes('/discount/'));
});
