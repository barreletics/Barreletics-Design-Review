/**
 * Barreletics PDP Variant Selection Controller
 *
 * Resolves option combinations to Shopify variant IDs and keeps
 * the buy box, sticky ATC, and URL in sync.
 *
 * Expects a global `window.__pdpProduct` JSON object set by Liquid.
 *
 * 2026-09-30: works for ANY option name. Each option row is
 * `[data-option-position]` (optionally `data-option-kind="color|size|other"`);
 * a button's value is data-option-value, else data-color, else data-size.
 * Previously only options named exactly "Color"/"Size" were wired, so the
 * T-shirt "Style" option and the One-Off "Grey Swirl" colour row did nothing.
 */
(function () {
  'use strict';

  var product = window.__pdpProduct;
  if (!product || !product.variants) return;

  var BTN_SELECTOR = '[data-option-value], .pdp-buy__swatch, .pdp-buy__size-btn:not(.is-soon)';

  var state = {
    options: {}
  };

  var rows = {}; // position -> { el, kind }

  var els = {
    form: document.getElementById('pdp-form'),
    variantInput: document.querySelector('#pdp-form input[name="id"]'),
    priceNow: document.querySelector('.pdp-buy__price-now'),
    ctaBtn: document.querySelector('.pdp-buy__cta'),
    mainImg: document.getElementById('pdp-main-img'),
    selectedColor: document.getElementById('selected-color')
  };

  function valueOf(btn) {
    if (btn.hasAttribute('data-option-value')) return btn.getAttribute('data-option-value');
    if (btn.hasAttribute('data-color')) return btn.getAttribute('data-color');
    return btn.getAttribute('data-size');
  }

  function buttonsIn(container) {
    return Array.prototype.slice.call(container.querySelectorAll(BTN_SELECTOR));
  }

  function kindFor(container, name) {
    var k = container.getAttribute('data-option-kind');
    if (k) return k;
    var n = (name || '').toLowerCase();
    if (n.indexOf('size') > -1) return 'size';
    if (n.indexOf('color') > -1 || n.indexOf('colour') > -1) return 'color';
    return 'other';
  }

  function init() {
    var current = product.variants.filter(function (v) {
      return els.variantInput && String(v.id) === String(els.variantInput.value);
    })[0];

    product.options.forEach(function (name, i) {
      var position = i + 1;
      var container = document.querySelector('[data-option-position="' + position + '"]');
      if (!container) {
        // Option not rendered (e.g. hidden): keep the current variant's value so resolution still works.
        state.options[position] = current ? current.options[i] : null;
        return;
      }
      rows[position] = { el: container, kind: kindFor(container, name) };

      var btns = buttonsIn(container);
      var active = btns.filter(function (b) { return b.classList.contains('is-active'); })[0];
      state.options[position] = active ? valueOf(active) : (current ? current.options[i] : null);

      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          if (btn.disabled) return;
          selectOption(position, valueOf(btn));
        });
      });
    });

    updateVariant();
    updateAvailability();
  }

  function selectOption(position, value) {
    var row = rows[position];
    if (row) {
      buttonsIn(row.el).forEach(function (el) {
        var match = valueOf(el) === value;
        el.classList.toggle('is-active', match);
        if (el.hasAttribute('aria-selected')) el.setAttribute('aria-selected', match ? 'true' : 'false');
        if (el.hasAttribute('aria-pressed')) el.setAttribute('aria-pressed', match ? 'true' : 'false');
      });
    }

    state.options[position] = value;
    userPicked = true;

    if (els.selectedColor && row && row.kind === 'color') {
      els.selectedColor.textContent = value;
    }

    updateVariant();
    updateAvailability();
  }

  function resolveVariant() {
    for (var v = 0; v < product.variants.length; v++) {
      var variant = product.variants[v];
      var match = true;
      for (var j = 0; j < product.options.length; j++) {
        if (variant.options[j] !== state.options[j + 1]) {
          match = false;
          break;
        }
      }
      if (match) return variant;
    }
    return null;
  }

  function setCta(enabled, label) {
    if (!els.ctaBtn) return;
    els.ctaBtn.disabled = !enabled;
    els.ctaBtn.textContent = label;
    els.ctaBtn.classList.toggle('btn--disabled', !enabled);
  }

  function updateVariant() {
    var variant = resolveVariant();
    if (!variant) {
      // Combination does not exist: never leave a stale variant id that would add the wrong item.
      if (els.variantInput) els.variantInput.value = '';
      setCta(false, 'Unavailable');
      document.dispatchEvent(new CustomEvent('variant:changed', {
        detail: { variant: { id: '', available: false, price: product.price, title: 'Unavailable', featured_image: null }, product: product }
      }));
      return;
    }

    if (els.variantInput) {
      var changed = String(els.variantInput.value) !== String(variant.id);
      els.variantInput.value = variant.id;
      /* Shop Pay installments (shopify-payment-terms, rendered by {{ form | payment_terms }})
         only re-reads the form's name="id" input on a change event; setting .value alone
         left the old variant's split (e.g. $19.50 for $39 after picking the $34 Tank Top). */
      if (changed) {
        els.variantInput.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }

    if (els.priceNow) {
      els.priceNow.textContent = formatMoney(variant.price);
    }

    if (variant.available) {
      setCta(true, 'Add to Cart');
    } else {
      setCta(false, 'Sold Out');
    }

    if (els.mainImg && variant.featured_image) {
      var imgBase = variant.featured_image.src;
      /* Sized src avoids full-res flash in the hero frame (media-img + absolute fill). */
      els.mainImg.src = getSizedUrl(imgBase, 800);
      els.mainImg.srcset =
        getSizedUrl(imgBase, 400) + ' 400w, ' +
        getSizedUrl(imgBase, 600) + ' 600w, ' +
        getSizedUrl(imgBase, 800) + ' 800w, ' +
        getSizedUrl(imgBase, 1200) + ' 1200w';
    }

    updateUrl(variant.id);

    document.dispatchEvent(new CustomEvent('variant:changed', {
      detail: { variant: variant, product: product }
    }));
  }

  /* Size buttons are crossed out when no available variant has that size together with
     every other currently selected option (colour, style, ...). Colour/style rows are not
     crossed out (unchanged behaviour: shoppers can always switch colour). */
  function updateAvailability() {
    Object.keys(rows).forEach(function (key) {
      var position = parseInt(key, 10);
      var row = rows[position];
      if (row.kind !== 'size') return;

      buttonsIn(row.el).forEach(function (btn) {
        var val = valueOf(btn);
        var available = product.variants.some(function (v) {
          if (!v.available) return false;
          for (var j = 0; j < product.options.length; j++) {
            var want = (j + 1 === position) ? val : state.options[j + 1];
            if (want != null && v.options[j] !== want) return false;
          }
          return true;
        });
        btn.classList.toggle('is-unavailable', !available);
        btn.disabled = !available;
        btn.setAttribute('aria-disabled', !available ? 'true' : 'false');
      });
    });
  }

  var userPicked = false;
  function updateUrl(variantId) {
    /* Theme editor: never rewrite the preview URL. The editor tracks the iframe URL; an
       unexpected ?variant= rewrite on load made Save jump the preview back to Home (2026-09-30). */
    if (window.Shopify && window.Shopify.designMode) return;
    /* Only after a shopper picks a swatch/size, not on page load. */
    if (!userPicked) return;
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
