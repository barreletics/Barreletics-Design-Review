'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var fs = require('fs');
var path = require('path');

var ROOT = path.join(__dirname, '..');
var OWNER_BASELINE = path.join(__dirname, 'fixtures/owner-settings_schema-baseline.json');

function sectionByName(schema, name) {
  return schema.find(function (g) {
    return g && g.name === name;
  });
}

function settingIds(group) {
  return (group.settings || []).map(function (s) {
    return s.id;
  }).filter(Boolean);
}

test('settings_schema: 17 non-cart sections match owner baseline byte-for-byte', function () {
  var owner = JSON.parse(fs.readFileSync(OWNER_BASELINE, 'utf8'));
  var current = JSON.parse(fs.readFileSync(path.join(ROOT, 'config/settings_schema.json'), 'utf8'));
  assert.equal(current.length, owner.length);
  assert.equal(current.length, 18);

  for (var i = 0; i < owner.length; i++) {
    if (owner[i].name === 'Cart bundle preview (Nov08)') continue;
    assert.deepEqual(
      current[i],
      owner[i],
      'section mismatch: ' + owner[i].name
    );
  }
});

test('settings_schema: cart bundle section adds only approved toggle setting IDs', function () {
  var owner = JSON.parse(fs.readFileSync(OWNER_BASELINE, 'utf8'));
  var current = JSON.parse(fs.readFileSync(path.join(ROOT, 'config/settings_schema.json'), 'utf8'));
  var ownerCart = sectionByName(owner, 'Cart bundle preview (Nov08)');
  var currentCart = sectionByName(current, 'Cart bundle preview (Nov08)');
  assert.ok(ownerCart && currentCart);

  var ownerIds = new Set(settingIds(ownerCart));
  var currentIds = new Set(settingIds(currentCart));
  var added = [];
  currentIds.forEach(function (id) {
    if (!ownerIds.has(id)) added.push(id);
  });
  assert.deepEqual(added.sort(), [
    'cart_bundle_add_pair_offer_enabled',
    'cart_bundle_pants_offer_enabled'
  ]);

  var preserved = [
    'cart_bundle_pants_headline',
    'cart_bundle_pants_qual_template',
    'cart_bundle_preview_disclaimer'
  ];
  preserved.forEach(function (id) {
    var o = ownerCart.settings.find(function (s) {
      return s.id === id;
    });
    var c = currentCart.settings.find(function (s) {
      return s.id === id;
    });
    assert.deepEqual(c, o, 'owner text/default must be preserved for ' + id);
  });
});
