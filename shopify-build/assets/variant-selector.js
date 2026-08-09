/**
 * Barreletics PDP Variant Selection Controller
 *
 * Resolves option combinations to Shopify variant IDs and keeps
 * the buy box, sticky ATC, and URL in sync.
 *
 * Expects a global `window.__pdpProduct` JSON object set by Liquid.
 */
(function () {
  'use strict';

  var product = window.__pdpProduct;
  if (!product || !product.variants) return;

  var state = {
    options: {}
  };

  var els = {
    form: document.getElementById('pdp-form'),
    variantInput: document.querySelector('#pdp-form input[name="id"]'),
    priceNow: document.querySelector('.pdp-buy__price-now'),
    ctaBtn: document.querySelector('.pdp-buy__cta'),
    mainImg: document.getElementById('pdp-main-img'),
    selectedColor: document.getElementById('selected-color'),
    swatches: document.querySelectorAll('.pdp-buy__swatch'),
    sizeBtns: document.querySelectorAll('.pdp-buy__size-btn')
  };

  function init() {
    product.options.forEach(function (name, i) {
      var position = i + 1;
      var container = document.querySelector('[data-option-position="' + position + '"]');
      if (!container) return;

      if (name === 'Color') {
        state.options[position] = getActiveValue(container, '.pdp-buy__swatch', 'data-color');
        container.querySelectorAll('.pdp-buy__swatch').forEach(function (btn) {
          btn.addEventListener('click', function () {
            selectOption(position, btn.getAttribute('data-color'), container, '.pdp-buy__swatch', 'data-color');
          });
        });
      } else if (name === 'Size') {
        state.options[position] = getActiveValue(container, '.pdp-buy__size-btn:not(.is-soon)', 'data-size');
        container.querySelectorAll('.pdp-buy__size-btn:not(.is-soon)').forEach(function (btn) {
          btn.addEventListener('click', function () {
            selectOption(position, btn.getAttribute('data-size'), container, '.pdp-buy__size-btn:not(.is-soon)', 'data-size');
          });
        });
      }
    });

    updateVariant();
    updateAvailability();
  }

  function getActiveValue(container, selector, attr) {
    var active = container.querySelector(selector + '.is-active');
    return active ? active.getAttribute(attr) : null;
  }

  function selectOption(position, value, container, selector, attr) {
    container.querySelectorAll(selector).forEach(function (el) {
      var match = el.getAttribute(attr) === value;
      el.classList.toggle('is-active', match);
      if (el.hasAttribute('aria-selected')) {
        el.setAttribute('aria-selected', match ? 'true' : 'false');
      }
    });

    state.options[position] = value;

    if (els.selectedColor && position === getColorPosition()) {
      els.selectedColor.textContent = value;
    }

    updateVariant();
    updateAvailability();
  }

  function getColorPosition() {
    for (var i = 0; i < product.options.length; i++) {
      if (product.options[i] === 'Color') return i + 1;
    }
    return -1;
  }

  function resolveVariant() {
    var selected = [];
    for (var i = 1; i <= product.options.length; i++) {
      selected.push(state.options[i]);
    }

    for (var v = 0; v < product.variants.length; v++) {
      var variant = product.variants[v];
      var match = true;
      for (var j = 0; j < selected.length; j++) {
        if (variant.options[j] !== selected[j]) {
          match = false;
          break;
        }
      }
      if (match) return variant;
    }
    return null;
  }

  function updateVariant() {
    var variant = resolveVariant();
    if (!variant) return;

    if (els.variantInput) {
      els.variantInput.value = variant.id;
    }

    if (els.priceNow) {
      els.priceNow.textContent = formatMoney(variant.price);
    }

    if (els.ctaBtn) {
      if (variant.available) {
        els.ctaBtn.disabled = false;
        els.ctaBtn.textContent = 'Add to Cart \u2014 ' + formatMoney(variant.price);
        els.ctaBtn.classList.remove('btn--disabled');
      } else {
        els.ctaBtn.disabled = true;
        els.ctaBtn.textContent = 'Sold Out';
        els.ctaBtn.classList.add('btn--disabled');
      }
    }

    if (els.mainImg && variant.featured_image) {
      els.mainImg.src = variant.featured_image.src;
      els.mainImg.srcset =
        getSizedUrl(variant.featured_image.src, 400) + ' 400w, ' +
        getSizedUrl(variant.featured_image.src, 600) + ' 600w, ' +
        getSizedUrl(variant.featured_image.src, 800) + ' 800w';
    }

    updateUrl(variant.id);

    document.dispatchEvent(new CustomEvent('variant:changed', {
      detail: { variant: variant, product: product }
    }));
  }

  function updateAvailability() {
    var colorPos = getColorPosition();
    var sizePos = -1;
    for (var i = 0; i < product.options.length; i++) {
      if (product.options[i] === 'Size') { sizePos = i + 1; break; }
    }

    if (sizePos < 0) return;

    els.sizeBtns.forEach(function (btn) {
      var size = btn.getAttribute('data-size');
      var available = product.variants.some(function (v) {
        var colorMatch = colorPos < 0 || v.options[colorPos - 1] === state.options[colorPos];
        var sizeMatch = v.options[sizePos - 1] === size;
        return colorMatch && sizeMatch && v.available;
      });
      btn.classList.toggle('is-unavailable', !available);
      btn.disabled = !available;
      btn.setAttribute('aria-disabled', !available ? 'true' : 'false');
    });
  }

  function updateUrl(variantId) {
    if (!window.history || !window.history.replaceState) return;
    var url = new URL(window.location.href);
    url.searchParams.set('variant', variantId);
    window.history.replaceState({}, '', url.toString());
  }

  function formatMoney(cents) {
    return '$' + (cents / 100).toFixed(2).replace(/\.00$/, '');
  }

  function getSizedUrl(src, width) {
    if (!src) return '';
    return src.replace(/(\.[a-z]+)(\?|$)/, '_' + width + 'x$1$2');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
