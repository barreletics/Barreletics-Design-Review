'use strict';

var assert = require('node:assert/strict');
var test = require('node:test');
var path = require('path');
var { parseHTML } = require('linkedom');

var FIXTURE_PRODUCT = {
  options: [
    { name: 'Size', position: 1, values: ['M (W 5.5-7.5)'] },
    { name: 'Color', position: 2, values: ['Purple'] }
  ],
  variants: [{ id: 101, option1: 'M (W 5.5-7.5)', option2: 'Purple', available: true }]
};

function installDom() {
  var parsed = parseHTML('<!DOCTYPE html><html><body></body></html>');
  globalThis.window = parsed.window;
  globalThis.document = parsed.document;
  globalThis.Node = parsed.window.Node;
  globalThis.HTMLElement = parsed.window.HTMLElement;
  globalThis.Element = parsed.window.Element;
  delete require.cache[path.join(__dirname, '../assets/cart-bundle-promo.js')];
  return require('../assets/cart-bundle-promo.js');
}

function closedSkin() {
  return {
    quantity: 1,
    final_line_price: 7400,
    product_title: 'Closed Sole Performance Skin',
    product_type: 'Grippy Shoes',
    variant_title: 'Purple · M (W 5.5-7.5)',
    url: '/products/best-reformer-pilates-legree-workout-shoes'
  };
}

function waitMicrotask() {
  return new Promise(function (resolve) {
    setImmediate(resolve);
  });
}

test('DOM: failed native add keeps error visible and allows same-selection retry', function () {
  var bundle = installDom();
  var container = document.createElement('div');
  document.body.appendChild(container);

  var addAttempts = 0;
  var config = bundle.mergeConfig({
    enabled: true,
    pairPromoMode: 'live_2for15',
    fetchProductJson: function () {
      return Promise.resolve({ product: FIXTURE_PRODUCT });
    },
    addToCartFn: function () {
      addAttempts += 1;
      if (addAttempts === 1) return Promise.reject(new Error('native-cart-reject'));
      return Promise.resolve({ ok: true });
    }
  });

  bundle.mountPromo(container, [closedSkin()], config, 7400, { offerArm: 'variant' });

  assert.ok(container.querySelector('[data-sole-choice="closed"]'), 'sole pills visible immediately');
  assert.match(container.textContent, /Buy 2 or more pairs\. Save 15%\./);
  assert.match(container.textContent, /Choose your second pair below\./);
  assert.equal(container.querySelector('[data-open-add-pair-picker]'), null);

  var closedSole = container.querySelector('[data-sole-choice="closed"]');
  assert.ok(closedSole);
  closedSole.click();

  return waitMicrotask()
    .then(function () {
      return waitMicrotask();
    })
    .then(function () {
      var swatch = container.querySelector('[data-swatch-color="Purple"]');
      assert.ok(swatch, 'purple swatch rendered');
      assert.equal(swatch.getAttribute('data-swatch-kind'), 'text');
      assert.equal(swatch.textContent, 'Purple');
      swatch.click();
      var sizeSel = container.querySelector('[data-size-select]');
      assert.ok(sizeSel);
      var sizeOpt = Array.prototype.find.call(sizeSel.options, function (o) {
        return o.value === 'M (W 5.5-7.5)';
      });
      assert.ok(sizeOpt);
      sizeOpt.selected = true;
      sizeSel.dispatchEvent(new window.Event('change', { bubbles: true }));
      var submit = container.querySelector('[data-bundle-add-skin-pair]');
      assert.ok(submit);
      assert.equal(submit.disabled, false);
      assert.equal(submit.getAttribute('data-variant-id'), '101');
      submit.click();
      return waitMicrotask();
    })
    .then(function () {
      var status = container.querySelector('[data-add-pair-status]');
      assert.ok(status);
      assert.equal(status.hidden, false);
      assert.match(status.textContent, /Try again/i);
      assert.equal(status.classList.contains('is-error'), true);
      var submit = container.querySelector('[data-bundle-add-skin-pair]');
      assert.equal(submit.disabled, false, 'submit re-enabled for same selection');
      assert.equal(submit.getAttribute('data-variant-id'), '101');
      assert.equal(submit.textContent, 'Add pair');
      assert.equal(addAttempts, 1);
      submit.click();
      return waitMicrotask();
    })
    .then(function () {
      assert.equal(addAttempts, 2, 'second attempt without changing selection');
      var submit = container.querySelector('[data-bundle-add-skin-pair]');
      assert.equal(submit.disabled, false);
    });
});
