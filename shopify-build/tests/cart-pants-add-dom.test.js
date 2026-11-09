'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var path = require('path');
var { parseHTML } = require('linkedom');

var PANTS_PRODUCT = {
  options: [
    { name: 'Size', position: 1, values: ['S', 'M'] },
    { name: 'Color', position: 2, values: ['Black', 'Grey'] }
  ],
  variants: [
    { id: 501, option1: 'S', option2: 'Black', available: true },
    { id: 502, option1: 'M', option2: 'Black', available: true },
    { id: 503, option1: 'M', option2: 'Grey', available: false }
  ]
};

function installDom() {
  var parsed = parseHTML('<!DOCTYPE html><html><body></body></html>');
  globalThis.window = parsed.window;
  globalThis.document = parsed.document;
  delete require.cache[path.join(__dirname, '../assets/cart-bundle-promo.js')];
  return require('../assets/cart-bundle-promo.js');
}

function closedSkin2() {
  return {
    quantity: 2,
    final_line_price: 14800,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes'
  };
}

function waitMicro() {
  return new Promise(function (resolve) {
    setImmediate(function () {
      setImmediate(resolve);
    });
  });
}

function pickSelectOption(selectEl, value) {
  var opt = Array.prototype.find.call(selectEl.options, function (o) {
    return o.value === value;
  });
  if (!opt) throw new Error('option not found: ' + value);
  opt.selected = true;
  selectEl.dispatchEvent(new window.Event('change', { bubbles: true }));
}

test('pants add: partial selection keeps Add disabled (no variant id)', function () {
  var bundle = installDom();
  var calls = [];
  var cfg = bundle.mergeConfig({
    enabled: true,
    pantsProductHandle: 'lightly-padded-knee-yoga-pant-black',
    fetchProductJson: function () {
      return Promise.resolve({ product: PANTS_PRODUCT });
    },
    addToCartFn: function (vid) {
      calls.push(vid);
      return Promise.resolve({});
    }
  });
  var container = document.createElement('div');
  document.body.appendChild(container);
  bundle.mountPromo(container, [closedSkin2()], cfg, 14800, { offerArm: 'variant' });

  return waitMicro().then(function () {
    var btn = container.querySelector('[data-bundle-add-pant]');
    assert.ok(btn);
    var selects = container.querySelectorAll('.cart-bundle-promo__pants-select');
    pickSelectOption(selects[0], 'M');
    assert.equal(btn.disabled, true);
    assert.equal(btn.getAttribute('data-variant-id'), null);
    assert.equal(calls.length, 0);
  });
});

test('pants add: success calls native add with resolved variant id', function () {
  var bundle = installDom();
  var calls = [];
  var cfg = bundle.mergeConfig({
    enabled: true,
    pantsProductHandle: 'lightly-padded-knee-yoga-pant-black',
    fetchProductJson: function () {
      return Promise.resolve({ product: PANTS_PRODUCT });
    },
    addToCartFn: function (vid) {
      calls.push(vid);
      return Promise.resolve({});
    }
  });
  var container = document.createElement('div');
  document.body.appendChild(container);
  bundle.mountPromo(container, [closedSkin2()], cfg, 14800, { offerArm: 'variant' });

  return waitMicro()
    .then(function () {
      var selects = container.querySelectorAll('.cart-bundle-promo__pants-select');
      assert.equal(selects.length, 2);
      pickSelectOption(selects[0], 'M');
      pickSelectOption(selects[1], 'Black');
      var btn = container.querySelector('[data-bundle-add-pant]');
      assert.equal(btn.getAttribute('data-variant-id'), '502');
      assert.equal(btn.disabled, false);
      btn.click();
      return waitMicro().then(waitMicro);
    })
    .then(function () {
      assert.deepEqual(calls, [502]);
    });
});

test('pants add: failure then retry with same selection', function () {
  var bundle = installDom();
  var attempts = 0;
  var cfg = bundle.mergeConfig({
    enabled: true,
    pantsProductHandle: 'lightly-padded-knee-yoga-pant-black',
    fetchProductJson: function () {
      return Promise.resolve({ product: PANTS_PRODUCT });
    },
    addToCartFn: function () {
      attempts += 1;
      if (attempts === 1) return Promise.reject(new Error('cart-add-failed'));
      return Promise.resolve({});
    }
  });
  var container = document.createElement('div');
  document.body.appendChild(container);
  bundle.mountPromo(container, [closedSkin2()], cfg, 14800, { offerArm: 'variant' });

  return waitMicro()
    .then(function () {
      var selects = container.querySelectorAll('.cart-bundle-promo__pants-select');
      pickSelectOption(selects[0], 'S');
      pickSelectOption(selects[1], 'Black');
      var btn = container.querySelector('[data-bundle-add-pant]');
      btn.click();
      return waitMicro().then(waitMicro);
    })
    .then(function () {
      assert.equal(attempts, 1);
      var status = container.querySelector('[data-pants-add-status]');
      assert.match(status.textContent, /Could not add yoga pants/);
      var btn = container.querySelector('[data-bundle-add-pant]');
      assert.equal(btn.disabled, false);
      btn.click();
      return waitMicro().then(waitMicro);
    })
    .then(function () {
      assert.equal(attempts, 2);
    });
});

test('pants add: sold-out combo keeps button disabled', function () {
  var bundle = installDom();
  var cfg = bundle.mergeConfig({
    enabled: true,
    pantsProductHandle: 'lightly-padded-knee-yoga-pant-black',
    fetchProductJson: function () {
      return Promise.resolve({ product: PANTS_PRODUCT });
    }
  });
  var container = document.createElement('div');
  document.body.appendChild(container);
  bundle.mountPromo(container, [closedSkin2()], cfg, 14800, { offerArm: 'variant' });

  return waitMicro().then(function () {
    var selects = container.querySelectorAll('.cart-bundle-promo__pants-select');
    pickSelectOption(selects[0], 'M');
    pickSelectOption(selects[1], 'Grey');
    var btn = container.querySelector('[data-bundle-add-pant]');
    assert.equal(btn.disabled, true);
    assert.equal(btn.getAttribute('data-variant-id'), null);
  });
});
