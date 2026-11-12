'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');
var baseline = require('./fixtures/cart-bundle-promo-5a01277-baseline.js');

var CTRL_CFG = baseline.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });

function line(overrides) {
  return Object.assign(
    {
      quantity: 1,
      final_line_price: 7400,
      product_title: '',
      product_type: '',
      variant_title: '',
      url: ''
    },
    overrides
  );
}

function panelFor(items, opts) {
  return bundle.computeBundlePromo(items, CTRL_CFG, 7400, opts);
}

function baselinePanel(items) {
  return baseline.computeBundlePromo(items, CTRL_CFG, 7400);
}

test('closed-sole handle + Performance Skins title only: excluded (5a parity)', function () {
  var item = line({
    product_title: 'Performance Skins',
    url: '/products/best-reformer-pilates-legree-workout-shoes',
    variant_title: 'Purple · M'
  });
  var b = baselinePanel([item]);
  var c = panelFor([item]);
  assert.equal(b.showPanel, false);
  assert.equal(c.showPanel, b.showPanel);
  assert.equal(c.offerArm, 'control');
});

test('closed-sole in title + closed-sole handle needle: included', function () {
  var item = line({
    product_title: 'Performance Skins — Closed Sole',
    url: '/products/studio-performance-skin-closed-sole',
    variant_title: 'Purple · M'
  });
  var b = baselinePanel([item]);
  var c = panelFor([item]);
  assert.equal(b.showPanel, true);
  assert.equal(c.showPanel, b.showPanel);
  assert.equal(c.showPantsOffer, b.showPantsOffer);
});

test('open sole on control: excluded', function () {
  var item = line({
    product_title: 'Open Sole',
    url: '/products/studio-performance-skin-footwear',
    variant_title: 'Black / M'
  });
  var b = baselinePanel([item]);
  var c = panelFor([item]);
  assert.equal(b.showPanel, false);
  assert.equal(c.showPanel, b.showPanel);
});

test('pant line only: panel hidden', function () {
  var item = line({
    product_title: 'Yoga Pant',
    url: '/products/lightly-padded-knee-yoga-pant-black'
  });
  var b = baselinePanel([item]);
  var c = panelFor([item]);
  assert.equal(b.showPanel, false);
  assert.equal(c.showPanel, b.showPanel);
});

test('invalid product url: panel hidden', function () {
  var item = line({
    product_title: 'Closed Sole',
    url: '/collections/all'
  });
  var b = baselinePanel([item]);
  var c = panelFor([item]);
  assert.equal(c.showPanel, b.showPanel);
});

test('variant arm: mapped closed handle with generic title counts', function () {
  var item = line({
    product_title: 'Performance Skins',
    url: '/products/best-reformer-pilates-legree-workout-shoes',
    variant_title: 'M / Purple'
  });
  var v = panelFor([item], { offerArm: 'variant' });
  assert.equal(v.offerArm, 'variant');
  assert.equal(v.showPanel, true);
});

test('control 1 pair: pants qual photo stage matches baseline html flags', function () {
  var item = line({
    product_title: 'Closed Sole',
    url: '/products/foo-closed-sole',
    variant_title: 'M'
  });
  var b = baselinePanel([item]);
  var c = panelFor([item]);
  var html = bundle.renderPromoHtml(c);
  assert.equal(c.pantsQualOnly, b.pantsQualOnly);
  if (c.showPanel && c.pantsQualOnly) {
    assert.match(html, /cart-bundle-promo__pants-img/);
  }
});
