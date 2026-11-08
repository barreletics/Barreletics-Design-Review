'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var bundle = require('../assets/cart-bundle-promo.js');

test('recoverAddPairSubmitState clears pending and re-runs syncSubmit after failed add', function () {
  var state = { pending: true, syncSubmit: null };
  var btn = {
    disabled: true,
    textContent: 'Adding…',
    setAttribute: function () {},
    removeAttribute: function () {}
  };
  var syncRuns = 0;
  function syncSubmit() {
    syncRuns += 1;
    btn.disabled = false;
    btn.setAttribute('data-variant-id', '101');
  }
  state.syncSubmit = syncSubmit;

  bundle.recoverAddPairSubmitState(state, btn, 'Add pair', syncSubmit);

  assert.equal(state.pending, false);
  assert.equal(btn.textContent, 'Add pair');
  assert.equal(syncRuns, 1);
  assert.equal(btn.disabled, false);
});

test('recoverAddPairSubmitState uses state.syncSubmit when argument omitted', function () {
  var state = { pending: true };
  var btn = { textContent: 'Adding…' };
  var called = false;
  state.syncSubmit = function () {
    called = true;
    btn.disabled = false;
  };
  bundle.recoverAddPairSubmitState(state, btn, 'Add pair');
  assert.equal(called, true);
  assert.equal(btn.disabled, false);
});

test('failed native add simulation: second attempt allowed without selection change', function () {
  var state = { pending: false, selected: { color: 'Purple', size: 'M' } };
  var btn = {
    disabled: false,
    textContent: 'Add pair',
    _vid: '202',
    getAttribute: function (k) {
      return k === 'data-variant-id' ? this._vid : null;
    },
    setAttribute: function (k, v) {
      if (k === 'data-variant-id') this._vid = v;
    },
    removeAttribute: function () {
      this._vid = '';
    }
  };
  var attempts = 0;
  var addFn = function () {
    attempts += 1;
    if (attempts === 1) return Promise.reject(new Error('cart-add-failed'));
    return Promise.resolve();
  };
  var syncSubmit = function () {
    if (state.selected.color && state.selected.size) {
      btn.disabled = false;
      btn.setAttribute('data-variant-id', '202');
    }
  };

  state.pending = true;
  btn.disabled = true;
  var prev = btn.textContent;
  btn.textContent = 'Adding…';
  return addFn(202)
    .catch(function () {})
    .finally(function () {
      bundle.recoverAddPairSubmitState(state, btn, prev, syncSubmit);
    })
  .then(function () {
    assert.equal(attempts, 1);
    assert.equal(state.pending, false);
    assert.equal(btn.disabled, false);
    assert.equal(btn.textContent, 'Add pair');
    assert.ok(!state.pending);
    state.pending = true;
    btn.disabled = true;
    return addFn(202).finally(function () {
      bundle.recoverAddPairSubmitState(state, btn, prev, syncSubmit);
    });
  })
  .then(function () {
    assert.equal(attempts, 2);
    assert.equal(btn.disabled, false);
  });
});
