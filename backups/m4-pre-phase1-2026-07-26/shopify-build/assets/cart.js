/**
 * Barreletics AJAX Cart Controller (D-024)
 *
 * Handles add-to-cart, quantity changes, item removal,
 * cart drawer rendering, and free-shipping progress bar.
 */
(function () {
  'use strict';

  var FREE_SHIPPING_THRESHOLD = 15000; // $150 in cents
  var liveRegion;

  function init() {
    liveRegion = document.createElement('div');
    liveRegion.setAttribute('aria-live', 'polite');
    liveRegion.setAttribute('aria-atomic', 'true');
    liveRegion.className = 'visually-hidden';
    liveRegion.id = 'cart-live-region';
    document.body.appendChild(liveRegion);

    bindAddToCartForms();
    bindDrawerControls();
  }

  /* ── Public API ── */

  function addToCart(variantId, quantity) {
    quantity = quantity || 1;
    return fetch('/cart/add.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: variantId, quantity: quantity })
    })
    .then(function (res) {
      if (!res.ok) throw new Error('add-to-cart-failed');
      return res.json();
    })
    .then(function () {
      return fetchCart();
    })
    .then(function (cart) {
      renderDrawer(cart);
      updateCartCount(cart.item_count);
      announce('Item added to cart');
      openDrawer();
      return cart;
    });
  }

  function fetchCart() {
    return fetch('/cart.js', {
      headers: { 'Accept': 'application/json' }
    }).then(function (res) { return res.json(); });
  }

  function changeItem(lineKey, quantity) {
    return fetch('/cart/change.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: lineKey, quantity: quantity })
    })
    .then(function (res) { return res.json(); })
    .then(function (cart) {
      renderDrawer(cart);
      updateCartCount(cart.item_count);
      if (quantity === 0) {
        announce('Item removed from cart');
      } else {
        announce('Cart updated');
      }
      return cart;
    });
  }

  /* ── Drawer open / close ── */

  var triggerEl = null;

  function openDrawer() {
    var drawer = document.getElementById('cart-drawer');
    if (!drawer) return;
    triggerEl = document.activeElement;
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    var first = drawer.querySelector('button, [href], input');
    if (first) first.focus();
  }

  function closeDrawer() {
    var drawer = document.getElementById('cart-drawer');
    if (!drawer) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (triggerEl && triggerEl.focus) triggerEl.focus();
  }

  /* ── Rendering ── */

  function renderDrawer(cart) {
    var itemsContainer = document.getElementById('cart-drawer-items');
    var subtotalEl = document.getElementById('cart-subtotal');
    var footer = document.querySelector('.cart-drawer__footer');

    if (!itemsContainer) return;

    if (cart.item_count === 0) {
      itemsContainer.innerHTML =
        '<div class="cart-drawer__empty">' +
          '<p>Your cart is empty</p>' +
          '<a href="/collections/grippy-shoes" class="btn btn--primary">Shop Grippy Shoes</a>' +
        '</div>';
      if (footer) footer.style.display = 'none';
    } else {
      var html = '';
      cart.items.forEach(function (item) {
        html +=
          '<div class="cart-drawer__item" data-line-key="' + item.key + '">' +
            '<a href="' + item.url + '" class="cart-drawer__item-img">' +
              '<img src="' + getSizedUrl(item.image, 160) + '" alt="' + escapeHtml(item.title) + '" width="80" height="80" loading="lazy">' +
            '</a>' +
            '<div class="cart-drawer__item-details">' +
              '<a href="' + item.url + '" class="cart-drawer__item-title">' + escapeHtml(item.product_title) + '</a>' +
              '<p class="cart-drawer__item-variant">' + escapeHtml(item.variant_title || '') + '</p>' +
              '<div class="cart-drawer__item-qty">' +
                '<button type="button" data-qty-change="-1" aria-label="Decrease quantity">−</button>' +
                '<span>' + item.quantity + '</span>' +
                '<button type="button" data-qty-change="1" aria-label="Increase quantity">+</button>' +
              '</div>' +
            '</div>' +
            '<div class="cart-drawer__item-right">' +
              '<span class="cart-drawer__item-price">' + formatMoney(item.final_line_price) + '</span>' +
              '<button type="button" class="cart-drawer__item-remove" data-remove-item aria-label="Remove ' + escapeHtml(item.title) + '">Remove</button>' +
            '</div>' +
          '</div>';
      });
      itemsContainer.innerHTML = html;
      if (footer) footer.style.display = '';
    }

    if (subtotalEl) {
      subtotalEl.textContent = formatMoney(cart.total_price);
    }

    updateShippingBar(cart.total_price);
    bindDrawerControls();
  }

  function updateShippingBar(totalCents) {
    var fill = document.getElementById('shipping-fill');
    var text = document.getElementById('shipping-text');
    if (!fill || !text) return;

    var pct = Math.min((totalCents / FREE_SHIPPING_THRESHOLD) * 100, 100);
    fill.style.width = pct + '%';

    if (totalCents >= FREE_SHIPPING_THRESHOLD) {
      text.textContent = 'You qualify for free shipping!';
    } else {
      var remaining = formatMoney(FREE_SHIPPING_THRESHOLD - totalCents);
      text.textContent = remaining + ' away from free shipping';
    }
  }

  function updateCartCount(count) {
    document.querySelectorAll('[data-cart-count]').forEach(function (el) {
      el.textContent = count;
      el.style.display = count > 0 ? '' : 'none';
    });
  }

  /* ── Event Binding ── */

  function bindAddToCartForms() {
    var form = document.getElementById('pdp-form');
    if (form && !form.dataset.ajaxBound) {
      form.dataset.ajaxBound = 'true';
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var idInput = form.querySelector('input[name="id"]');
        if (!idInput) return;
        var btn = form.querySelector('.pdp-buy__cta');
        if (btn) {
          btn.disabled = true;
          btn.textContent = 'Adding\u2026';
        }
        addToCart(parseInt(idInput.value, 10), 1)
          .catch(function () {
            showError(form, 'This item is currently unavailable');
          })
          .finally(function () {
            if (btn) {
              var price = btn.getAttribute('data-price') || '';
              btn.disabled = false;
              btn.textContent = price ? 'Add to Cart \u2014 ' + price : 'Add to Cart';
            }
          });
      });
    }
  }

  function bindDrawerControls() {
    var drawer = document.getElementById('cart-drawer');
    if (!drawer) return;

    drawer.querySelectorAll('[data-qty-change]').forEach(function (btn) {
      if (btn.dataset.bound) return;
      btn.dataset.bound = 'true';
      btn.addEventListener('click', function () {
        var item = btn.closest('[data-line-key]');
        if (!item) return;
        var key = item.getAttribute('data-line-key');
        var qtySpan = item.querySelector('.cart-drawer__item-qty span');
        var currentQty = parseInt(qtySpan.textContent, 10) || 1;
        var delta = parseInt(btn.getAttribute('data-qty-change'), 10);
        var newQty = Math.max(0, currentQty + delta);
        changeItem(key, newQty);
      });
    });

    drawer.querySelectorAll('[data-remove-item]').forEach(function (btn) {
      if (btn.dataset.bound) return;
      btn.dataset.bound = 'true';
      btn.addEventListener('click', function () {
        var item = btn.closest('[data-line-key]');
        if (!item) return;
        changeItem(item.getAttribute('data-line-key'), 0);
      });
    });

    drawer.querySelectorAll('[data-cart-close]').forEach(function (el) {
      if (el.dataset.bound) return;
      el.dataset.bound = 'true';
      el.addEventListener('click', closeDrawer);
    });
  }

  function showError(form, message) {
    var existing = form.querySelector('.pdp-buy__error');
    if (existing) existing.remove();
    var el = document.createElement('p');
    el.className = 'pdp-buy__error';
    el.setAttribute('role', 'alert');
    el.textContent = message;
    form.appendChild(el);
    setTimeout(function () { el.remove(); }, 5000);
  }

  function announce(message) {
    if (liveRegion) liveRegion.textContent = message;
  }

  /* ── Helpers ── */

  function formatMoney(cents) {
    return '$' + (cents / 100).toFixed(2).replace(/\.00$/, '');
  }

  function getSizedUrl(src, width) {
    if (!src) return '';
    if (src.indexOf('_') > -1 && src.match(/_\d+x\./)) {
      return src.replace(/_\d+x\./, '_' + width + 'x.');
    }
    return src.replace(/(\.[a-z]+)(\?|$)/, '_' + width + 'x$1$2');
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  /* ── Expose global API ── */

  window.BarreleticsCart = {
    add: addToCart,
    fetch: fetchCart,
    change: changeItem,
    open: openDrawer,
    close: closeDrawer
  };

  /* ── Keyboard handling + focus trap for drawer ── */
  document.addEventListener('keydown', function (e) {
    var drawer = document.getElementById('cart-drawer');
    if (!drawer) return;
    if (!drawer.classList.contains('is-open')) return;

    if (e.key === 'Escape') {
      closeDrawer();
      return;
    }

    if (e.key === 'Tab') {
      var panel = drawer.querySelector('.cart-drawer__panel');
      if (!panel) return;
      var focusable = panel.querySelectorAll(
        'button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
      );
      if (focusable.length === 0) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];

      if (e.shiftKey) {
        if (document.activeElement === first) {
          e.preventDefault();
          last.focus();
        }
      } else {
        if (document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
