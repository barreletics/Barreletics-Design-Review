'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

var LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

function app15() {
  return { value_type: 'percentage', value: '15.0', target_type: 'line_item', title: 'Footwear 15%' };
}

function app10() {
  return { value_type: 'percentage', value: '10.0', target_type: 'line_item', title: 'Other offer 10%' };
}

function appFixed() {
  return { value_type: 'fixed_amount', value: '20.0', target_type: 'line_item', title: 'Fixed $20' };
}

function skinLine(qty, originalEach, finalEach, allocs) {
  return {
    quantity: qty,
    original_line_price: originalEach * qty,
    final_line_price: finalEach * qty,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes',
    line_level_discount_allocations: allocs || []
  };
}

test('confirmed 15%: linked allocation $22.20 on 148→125.80 is Applied', function () {
  var items = [
    skinLine(2, 7400, 6290, [{ amount: 2220, discount_application: app15() }])
  ];
  var r = bundle.computeBundlePromo(items, LIVE, 12580, VARIANT);
  assert.equal(r.pairSavingsCents, 2220);
  assert.equal(r.savingsTag, 'Applied');
  assert.equal(r.estimatedTotalCents, 12580);
});

test('10% other offer on skins: never Applied 15%; preview remains $22.20', function () {
  var items = [
    skinLine(2, 7400, 6660, [{ amount: 1480, discount_application: app10() }])
  ];
  var r = bundle.computeBundlePromo(items, LIVE, 13320, VARIANT);
  assert.equal(r.pairSavingsMode, 'preview');
  assert.equal(r.savingsTag, 'Preview');
  assert.equal(r.pairSavingsCents, 2220);
  assert.notEqual(r.savingsLine, 'You save $14.80.');
});

test('fixed amount discount: never Applied 15%', function () {
  var items = [skinLine(2, 7400, 7000, [{ amount: 1800, discount_application: appFixed() }])];
  var r = bundle.computeBundlePromo(items, LIVE, 14000, VARIANT);
  assert.equal(r.pairSavingsMode, 'preview');
  assert.equal(r.savingsTag, 'Preview');
});

test('unlinked allocation metadata: never Applied', function () {
  var items = [skinLine(2, 7400, 6660, [{ amount: 1480 }])];
  var r = bundle.computeBundlePromo(items, LIVE, 13320, VARIANT);
  assert.equal(r.pairSavingsMode, 'preview');
  assert.equal(r.pairSavingsCents, 2220);
});

test('discount_application_index requires matching cart application', function () {
  var items = [
    skinLine(2, 7400, 6290, [{ amount: 2220, discount_application_index: 0 }])
  ];
  var opts = Object.assign({}, VARIANT, {
    discountApplications: [app15()]
  });
  var r = bundle.computeBundlePromo(items, LIVE, 12580, opts);
  assert.equal(r.savingsTag, 'Applied');
  assert.equal(r.pairSavingsCents, 2220);
});

test('index without applications array: preview only', function () {
  var items = [
    skinLine(2, 7400, 6290, [{ amount: 2220, discount_application_index: 0 }])
  ];
  var r = bundle.computeBundlePromo(items, LIVE, 12580, VARIANT);
  assert.equal(r.pairSavingsMode, 'preview');
});

test('pants-only allocation does not count toward footwear Applied', function () {
  var items = [
    skinLine(2, 7400, 7400, []),
    {
      quantity: 1,
      original_line_price: 8900,
      final_line_price: 8010,
      product_title: 'Yoga Pant',
      url: '/products/lightly-padded-knee-yoga-pant-black',
      line_level_discount_allocations: [{ amount: 890, discount_application: app10() }]
    }
  ];
  var r = bundle.computeBundlePromo(items, LIVE, 22810, VARIANT);
  assert.equal(r.pairSavingsMode, 'preview');
  assert.equal(r.pairSavingsCents, 2220);
});

test('preview undiscounted 2×$74 shows $22.20', function () {
  var items = [skinLine(2, 7400, 7400, [])];
  var r = bundle.computeBundlePromo(items, LIVE, 14800, VARIANT);
  assert.equal(r.pairSavingsCents, 2220);
  assert.equal(r.pairSavingsMode, 'preview');
  assert.equal(r.estimatedTotalCents, 12580);
});
