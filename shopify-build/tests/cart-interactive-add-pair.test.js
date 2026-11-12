'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var fs = require('fs');
var path = require('path');
var { parseHTML } = require('linkedom');
var bundle = require('../assets/cart-bundle-promo.js');

var SNIPPET = path.join(__dirname, '../snippets/cart-bundle-promo-config.liquid');

var LIVE = bundle.mergeConfig({ enabled: true, pairPromoMode: 'live_2for15' });
var VARIANT = { offerArm: 'variant' };

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
  var r = bundle.computeBundlePromo([closedSkin(1, 'Purple')], LIVE, 7400, VARIANT);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, false);
  assert.equal(r.footwearOfferLine, '');
});

test('at 2+ pairs: pants stage on, add-pair stays on', function () {
  var mixed = [closedSkin(1, 'Purple'), openSkin(1, 'Black')];
  var r = bundle.computeBundlePromo(mixed, LIVE, 14800, VARIANT);
  assert.equal(r.showAddPairStage, true);
  assert.equal(r.showPantsOffer, true);
  assert.equal(r.pantsPickerVisible, true);
  assert.equal(r.benefitSupportTemplate, 'Add another pair below.');
  assert.equal(r.footwearOfferLine, '');
});

test('pants not counted as footwear pairs', function () {
  var r = bundle.computeBundlePromo([pantItem()], LIVE, 8900);
  assert.equal(r.showPanel, false);
});

test('1 pant in cart suppresses second pants offer at 2 pairs', function () {
  var items = [closedSkin(2, 'Purple'), pantItem()];
  var r = bundle.computeBundlePromo(items, LIVE, 23700, VARIANT);
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

test('colorValuesForAddPair allows repeat colors when cart color is known', function () {
  var cart = [closedSkin(1, 'Purple')];
  var meta = bundle.colorValuesForAddPair(FIXTURE_PRODUCT, cart, LIVE);
  assert.equal(meta.unresolved, false);
  assert.ok(meta.colors.indexOf('Purple') !== -1);
  assert.equal(meta.colors.length, 3);
});

test('render at 1 pair: immediate sole pills and approved copy', function () {
  var r = bundle.computeBundlePromo([closedSkin(1)], LIVE, 7400, VARIANT);
  var html = bundle.renderPromoHtml(r);
  assert.match(html, /Buy 2 or more pairs\. Save 15%\./);
  assert.match(html, /Choose your second pair below\./);
  assert.match(html, /data-sole-choice="closed"/);
  assert.ok(!html.includes('data-open-add-pair-picker'));
  assert.ok(!html.includes('data-add-pair-body hidden'));
  assert.match(html, /data-bundle-add-pair/);
  assert.ok(!html.includes('Performance Skin pairs in cart:'));
  assert.match(html, /Preview only—offers aren't applied at checkout/);
  assert.ok(!html.includes('cart-bundle-promo__pants-img'));
  assert.ok(!html.includes('unlock'));
});

test('render at 2 pairs includes add-pair pills and outfit pants block', function () {
  var r = bundle.computeBundlePromo([closedSkin(2)], LIVE, 14800, VARIANT);
  var html = bundle.renderPromoHtml(r);
  assert.equal(r.showAddPairStage, true);
  assert.match(html, /Add another pair below\./);
  assert.ok(!html.includes('Choose your second pair below.'));
  assert.match(html, /data-sole-choice="closed"/);
  assert.match(html, /Complete your outfit\./);
  assert.match(html, /Get 35% off one pair of yoga pants\./);
  assert.match(html, /cart-bundle-promo__pants-img/);
  assert.match(html, /data-bundle-pants-picker/);
  assert.match(html, /data-bundle-add-pair/);
  assert.equal((html.match(/data-bundle-add-skin-pair/g) || []).length, 1);
});

test('mountPromo at 1→2→3→4→2→1: sole pills and single Add pair persist', function () {
  var counts = [1, 2, 3, 4, 2, 1];
  for (var i = 0; i < counts.length; i++) {
    var n = counts[i];
    var parsed = parseHTML('<!DOCTYPE html><html><body></body></html>');
    globalThis.window = parsed.window;
    globalThis.document = parsed.document;
    delete require.cache[path.join(__dirname, '../assets/cart-bundle-promo.js')];
    var mod = require('../assets/cart-bundle-promo.js');
    var container = document.createElement('div');
    document.body.appendChild(container);
    var items = [closedSkin(n)];
    mod.mountPromo(container, items, LIVE, 7400 * n, VARIANT);
    assert.equal(
      container.querySelectorAll('[data-sole-choice]').length,
      2,
      'pairCount ' + n
    );
    assert.equal(container.querySelectorAll('[data-bundle-add-skin-pair]').length, 1);
    assert.ok(container.querySelector('[data-bundle-add-pair]'));
    if (n >= 2) {
      assert.ok(container.querySelector('[data-bundle-pants-picker]'));
      assert.match(container.textContent, /Add another pair below\./);
    } else {
      assert.ok(!container.querySelector('[data-bundle-pants-picker]'));
      assert.match(container.textContent, /Choose your second pair below\./);
    }
  }
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
  var r = bundle.computeBundlePromo([closedSkin(2)], LIVE, 14800, VARIANT);
  var html = bundle.renderPromoHtml(r);
  assert.ok(!html.includes('/discount/'));
});

test('snippet footwearQualifiedTemplate: assign+json placeholder (Liquid must not strip {{percent}})', function () {
  var liquid = fs.readFileSync(SNIPPET, 'utf8');
  assert.ok(liquid.includes('"footwearQualifiedTemplate": {{ default_footwear_qualified | json }}'));
  assert.ok(!liquid.match(/"footwearQualifiedTemplate":\s*"Save \{\{percent\}\}/));
});

test('at 2 pairs qualified line shows 15% when template retains JS placeholder', function () {
  var cfg = bundle.mergeConfig({
    enabled: true,
    pairPromoMode: 'live_2for15',
    livePairPercent: 15,
    footwearQualifiedTemplate: 'Save {{percent}}% on your Performance Skin pairs.'
  });
  var r = bundle.computeBundlePromo([closedSkin(2)], cfg, 14800, VARIANT);
  assert.equal(r.visualSavingsMode, 'preview');
  assert.match(r.visualSavingsLine, /Your potential savings: \$22\.20/);
  var html = bundle.renderPromoHtml(r);
  assert.match(html, /Your potential savings: \$22\.20/);
  assert.ok(!html.includes('cart-bundle-promo__footwear-qualified'));

  var copperCart = [
    {
      quantity: 2,
      final_line_price: 15600,
      product_title: 'Closed Sole Performance Skin',
      product_type: 'Grippy Shoes',
      variant_title: 'Copper Swirl · L (W 8-11)',
      url: '/products/best-reformer-pilates-legree-workout-shoes'
    }
  ];
  var r156 = bundle.computeBundlePromo(copperCart, cfg, 15600, VARIANT);
  assert.equal(r156.footwearConfirmationLine, 'Save 15% on your Performance Skin pairs.');
  assert.equal(r156.pairSavingsCents, 2340);
});

test('regression: Liquid-stripped template yields bare Save % in DOM', function () {
  var stripped = bundle.mergeConfig({
    enabled: true,
    pairPromoMode: 'live_2for15',
    footwearQualifiedTemplate: 'Save % on your Performance Skin pairs.'
  });
  var r = bundle.computeBundlePromo([closedSkin(2)], stripped, 14800, VARIANT);
  assert.match(r.footwearConfirmationLine, /^Save % on/);

  var parsed = parseHTML('<!DOCTYPE html><html><body></body></html>');
  globalThis.window = parsed.window;
  globalThis.document = parsed.document;
  delete require.cache[path.join(__dirname, '../assets/cart-bundle-promo.js')];
  var mod = require('../assets/cart-bundle-promo.js');
  var fixed = mod.mergeConfig({
    enabled: true,
    pairPromoMode: 'live_2for15',
    livePairPercent: 15,
    footwearQualifiedTemplate: 'Save {{percent}}% on your Performance Skin pairs.'
  });
  var container = document.createElement('div');
  document.body.appendChild(container);
  mod.mountPromo(container, [closedSkin(2)], fixed, 14800, VARIANT);
  var vs = container.querySelector('[data-visual-savings]');
  assert.ok(vs);
  assert.match(vs.textContent, /Your potential savings: \$22\.20/);
  assert.ok(!vs.textContent.match(/Save % on/));
});
