(function () {
  'use strict';

  function normalise(str) {
    return (str || '').replace(/\s*\([^)]*\)/g, '').trim().toLowerCase();
  }

  function initBrVariantsFilter(filterEl) {
    var buttons = filterEl.querySelectorAll('[data-size]');
    var grid = document.querySelector('.br-variants-grid');
    if (!grid) return;

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var size = btn.getAttribute('data-size');
        var wasActive = btn.classList.contains('is-active');

        buttons.forEach(function (b) { b.classList.remove('is-active'); });

        if (wasActive) {
          size = 'all';
        } else {
          btn.classList.add('is-active');
        }

        var allGroups = grid.querySelectorAll('.br-product-group');
        var targets = allGroups.length ? Array.from(allGroups) : [grid];

        targets.forEach(function (group) {
          group.querySelectorAll('.br-variant-card[data-br-size]').forEach(function (card) {
            if (size === 'all') {
              card.style.display = '';
            } else {
              card.style.display =
                normalise(card.getAttribute('data-br-size')) === normalise(size) ? 'flex' : 'none';
            }
          });
        });
      });
    });
  }

  function init() {
    var filters = document.querySelectorAll('[data-br-size-filter]');
    if (!filters.length) return;
    filters.forEach(function (filterEl) {
      if (document.querySelector('.br-variants-grid')) {
        initBrVariantsFilter(filterEl);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
