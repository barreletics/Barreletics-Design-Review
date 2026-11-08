'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

var BASE = bundle.mergeConfig({ enabled: true });

function skinItem(qty, priceCents) {
  return {
    quantity: qty,
    final_line_price: priceCents * qty,
    product_title: 'Studio Performance Skin — Closed Sole',
    product_type: 'Grippy Shoes',
    variant_title: 'Onyx / M',
    url: '/products/studio-performance-skin-closed-sole'
  };
}

function pantItem(qty, priceCents) {
  return {
    quantity: qty,
    final_line_price: priceCents * qty,
    product_title: 'High-Waist Yoga Pant',
    product_type: 'Apparel',
    variant_title: 'Black / S',
    url: '/products/high-waist-yoga-pant'
  };
}

test('flag off hides panel', function () {
  var result = bundle.computeBundlePromo([skinItem(2, 7400)], { enabled: false });
  assert.equal(result.showPanel, false);
  assert.equal(result.totalSavingsCents, 0);
});

test('0 pairs — no pair savings line with message', function () {
  var result = bundle.computeBundlePromo([], BASE);
  assert.equal(result.pairCount, 0);
  assert.equal(result.totalSavingsCents, 0);
});

test('1 pair — nudge Add 1 pair Save 15% in live mode', function () {
  var result = bundle.computeBundlePromo([skinItem(1, 7400)], BASE);
  var nudge = result.lines.find(function (l) {
    return l.variant === 'nudge';
  });
  assert.ok(nudge);
  assert.equal(nudge.message, 'Add 1 pair. Save 15%.');
  assert.equal(result.totalSavingsCents, 0);
});

test('2 pairs — live 15% on pair subtotal', function () {
  var result = bundle.computeBundlePromo([skinItem(2, 7400)], BASE);
  assert.equal(result.pairCount, 2);
  assert.equal(result.totalSavingsCents, Math.round(14800 * 0.15));
});

test('3+ pairs — future tier uses 15% not a fourth tier', function () {
  var cfg = bundle.mergeConfig({
    enabled: true,
    pairPromoMode: 'future_tiers',
    tierTwoPercent: 10,
    tierThreePlusPercent: 15
  });
  var two = bundle.computeBundlePromo([skinItem(2, 7400)], cfg);
  assert.equal(two.totalSavingsCents, Math.round(14800 * 0.1));

  var three = bundle.computeBundlePromo([skinItem(3, 7400)], cfg);
  assert.equal(three.totalSavingsCents, Math.round(22200 * 0.15));

  var four = bundle.computeBundlePromo([skinItem(4, 7400)], cfg);
  assert.equal(four.totalSavingsCents, Math.round(29600 * 0.15));
});

test('pants promo requires 2+ pairs and caps at one pant unit savings', function () {
  var items = [skinItem(2, 7400), pantItem(1, 8900)];
  var result = bundle.computeBundlePromo(items, BASE);
  var pantsLine = result.lines.find(function (l) {
    return l.type === 'pants';
  });
  assert.ok(pantsLine);
  assert.equal(pantsLine.previewUnitPriceCents, 6370);
  assert.equal(pantsLine.savingsCents, Math.round(9800 * 0.35));
  assert.ok(result.lines.some(function (l) {
    return l.message.indexOf('You save $') === 0;
  }));
});

test('two pants — only one unit of 35% proposed savings', function () {
  var items = [skinItem(2, 7400), pantItem(2, 8900)];
  var result = bundle.computeBundlePromo(items, BASE);
  var pantsSave = Math.round(9800 * 0.35);
  assert.equal(result.totalSavingsCents, Math.round(14800 * 0.15) + pantsSave);
});

test('pants ignored below pair threshold', function () {
  var items = [skinItem(1, 7400), pantItem(1, 8900)];
  var result = bundle.computeBundlePromo(items, BASE);
  assert.ok(!result.lines.some(function (l) {
    return l.type === 'pants';
  }));
});

test('custom percent edits propagate', function () {
  var cfg = bundle.mergeConfig({
    enabled: true,
    pantsPercent: 30,
    pantsProposedPriceCents: 10000,
    livePairPercent: 20
  });
  var items = [skinItem(2, 5000), pantItem(1, 8900)];
  var result = bundle.computeBundlePromo(items, cfg);
  assert.equal(result.totalSavingsCents, Math.round(10000 * 0.2) + Math.round(10000 * 0.3));
});

test('open sole does not count toward closed sole pairs', function () {
  var openSole = {
    quantity: 2,
    final_line_price: 14800,
    product_title: 'Studio Performance Skin — Open Sole',
    url: '/products/studio-performance-skin-open-sole'
  };
  var result = bundle.computeBundlePromo([openSole], BASE);
  assert.equal(result.pairCount, 0);
});
