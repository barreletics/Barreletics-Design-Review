/**
 * Simulated cart offer — no network, no Shopify. Design preview only.
 */
(function (global) {
  'use strict';

  var NOTICE = 'Design preview — simulated cart. Percentages are illustrative only; not applied at checkout.';

  var CATALOG = {
    open: {
      label: 'Add Open Sole',
      colors: ['Black', 'White', 'Coral', 'Rivian Green', 'Dusty Blue'],
      sizes: ['M (W 5.5-7.5)', 'L (W 8-11)']
    },
    closed: {
      label: 'Add Closed Sole',
      colors: ['Purple', 'Black', 'Coral', 'Deep Teal', 'Bright Yellow'],
      sizes: ['M (W 5.5-7.5)', 'L (W 8-11)']
    }
  };

  var PANTS_IMG =
    'https://cdn.shopify.com/s/files/1/0045/0612/4391/files/IMG_2914.jpg?v=1741040643';

  function normColor(c) {
    return String(c || '')
      .toLowerCase()
      .replace(/\s+/g, ' ')
      .trim();
  }

  function initialState() {
    return {
      pairs: [{ sole: 'closed', color: 'Purple', size: 'M (W 5.5-7.5)', label: 'Closed Sole — Purple' }],
      pants: false,
      pick: { sole: null, color: '', size: '' },
      pending: false,
      addPickerOpen: false
    };
  }

  function pairCount(state) {
    return (state.pairs || []).length;
  }

  function colorsInCart(state) {
    var u = {};
    (state.pairs || []).forEach(function (p) {
      if (p.color) u[normColor(p.color)] = true;
    });
    return u;
  }

  function availableColors(state, sole) {
    return (CATALOG[sole].colors || []).slice();
  }

  function stage(state) {
    var n = pairCount(state);
    if (n < 2) return 'add-pair';
    if (!state.pants) return 'pants-offer';
    return 'complete';
  }

  function canAddPair(state) {
    var p = state.pick;
    return p.sole && p.color && p.size && !state.pending;
  }

  function addPair(state) {
    if (!canAddPair(state)) return state;
    var sole = state.pick.sole;
    var next = {
      sole: sole,
      color: state.pick.color,
      size: state.pick.size,
      label: (sole === 'open' ? 'Open' : 'Closed') + ' Sole — ' + state.pick.color
    };
    state = JSON.parse(JSON.stringify(state));
    state.pairs.push(next);
    state.pick = { sole: null, color: '', size: '' };
    state.addPickerOpen = false;
    return state;
  }

  function removeLastPair(state) {
    state = JSON.parse(JSON.stringify(state));
    if (state.pairs.length > 1) state.pairs.pop();
    else state = initialState();
    state.pants = false;
    state.pick = { sole: null, color: '', size: '' };
    state.addPickerOpen = false;
    return state;
  }

  function addPants(state) {
    state = JSON.parse(JSON.stringify(state));
    state.pants = true;
    return state;
  }

  function resetAll() {
    return initialState();
  }

  global.BarreleticsMockCart = {
    NOTICE: NOTICE,
    CATALOG: CATALOG,
    PANTS_IMG: PANTS_IMG,
    initialState: initialState,
    pairCount: pairCount,
    colorsInCart: colorsInCart,
    availableColors: availableColors,
    stage: stage,
    canAddPair: canAddPair,
    addPair: addPair,
    removeLastPair: removeLastPair,
    addPants: addPants,
    resetAll: resetAll,
    normColor: normColor
  };
})(typeof window !== 'undefined' ? window : globalThis);
