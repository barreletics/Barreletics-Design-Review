/**
 * Barreletics AJAX Cart Controller (D-024)
 *
 * Handles add-to-cart, quantity changes, item removal,
 * cart drawer rendering, and free-shipping progress bar.
 */
(function () {
  'use strict';

  if (window.BarreleticsCart && window.BarreleticsCart.__initialized) {
    return;
  }

  var FREE_SHIPPING_THRESHOLD = 15000; // $150 in cents
  var liveRegion;
  var bundleConfig = null;

  function readBundleConfig() {
    if (bundleConfig) return bundleConfig;
    var el = document.getElementById('cart-bundle-promo-config');
    if (!el || !el.textContent) return null;
    try {
      bundleConfig = JSON.parse(el.textContent);
    } catch (e) {
      bundleConfig = null;
    }
    return bundleConfig;
  }

  function updateBundlePromo(cart) {
    var cfg = readBundleConfig();
    var bundleOn = cfg && cfg.enabled && window.BarreleticsCartBundle;

    var mounts = [
      document.getElementById('cart-bundle-promo-mount'),
      document.getElementById('cart-page-bundle-promo')
    ];

    if (!bundleOn) {
      mounts.forEach(function (mount) {
        if (!mount) return;
        mount.innerHTML = '';
        mount.setAttribute('hidden', 'hidden');
      });
      return;
    }

    mounts.forEach(function (mount) {
      if (!mount) return;
      window.BarreleticsCartBundle.mountPromo(mount, cart.items, cfg, cart.total_price);
    });
  }

  function dispatchCartItemAdded(cart) {
    if (!cart || !cart.items || !cart.items.length) return;
    var last = cart.items[cart.items.length - 1];
    document.dispatchEvent(
      new CustomEvent('cart:item-added', {
        detail: {
          id: last.variant_id,
          sku: last.sku,
          title: last.product_title || last.title,
          variant_title: last.variant_title,
          price: last.price,
          quantity: last.quantity
        }
      })
    );
  }

  function dispatchCartUpdated(cart) {
    document.dispatchEvent(new CustomEvent('cart:updated', { detail: { cart: cart } }));
  }

  function init() {
    liveRegion = document.createElement('div');
    liveRegion.setAttribute('aria-live', 'polite');
    liveRegion.setAttribute('aria-atomic', 'true');
    liveRegion.className = 'visually-hidden';
    liveRegion.id = 'cart-live-region';
    document.body.appendChild(liveRegion);

    var subtotalSsr = document.getElementById('cart-subtotal');
    moneySample = subtotalSsr ? subtotalSsr.textContent : '';
    if (!isUS()) {
      var shipBar = document.querySelector('.cart-drawer__shipping-bar');
      if (shipBar) shipBar.style.display = 'none';
    }

    bindCartTriggers();
    bindAddToCartForms();
    bindDrawerControls();

    /* First load: sync the (closed) drawer meter/note with one /cart.js fetch, only if the cart has items. */
    var drawerEl = document.getElementById('cart-drawer');
    var pageMount = document.getElementById('cart-page-bundle-promo');
  if (drawerEl && parseInt(drawerEl.getAttribute('data-item-count'), 10) > 0) {
      fetchCart()
        .then(function (cart) {
          if (isUS()) updateShippingBar(cart.total_price, cart);
          updateBundlePromo(cart);
          updateCartCount(cart.item_count);
        })
        .catch(function () {});
    } else if (pageMount) {
      fetchCart()
        .then(function (cart) {
          updateBundlePromo(cart);
        })
        .catch(function () {});
    }
  }

  function bindCartTriggers() {
    document.querySelectorAll('[data-cart-trigger]').forEach(function (el) {
      if (el.dataset.cartBound) return;
      el.dataset.cartBound = 'true';
      el.addEventListener('click', function (e) {
        e.preventDefault();
        openDrawer();
      });
    });
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
      dispatchCartItemAdded(cart);
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
      dispatchCartUpdated(cart);
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
    var sb = window.innerWidth - document.documentElement.clientWidth; if (sb > 0) document.body.style.paddingRight = sb + 'px';
    document.body.style.overflow = 'hidden';
    var first = drawer.querySelector('button, [href], input');
    if (first) setTimeout(function(){ try { first.focus({preventScroll:true}); } catch(e){ first.focus(); } }, 320);
  }

  function closeDrawer() {
    var drawer = document.getElementById('cart-drawer');
    if (!drawer) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    document.body.style.paddingRight = '';
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
          '<a href="/collections/all" class="btn btn--primary">Continue shopping</a>' +
        '</div><div id="cart-bundle-promo-mount" class="cart-drawer__bundle-slot" hidden></div>';
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
      html += '<div id="cart-bundle-promo-mount" class="cart-drawer__bundle-slot" hidden></div>';
      itemsContainer.innerHTML = html;
      if (footer) footer.style.display = '';
    }

    if (subtotalEl) {
      subtotalEl.textContent = formatMoney(cart.total_price);
    }

    updateShippingBar(cart.total_price, cart);
    updateBundlePromo(cart);
    bindDrawerControls();
  }

  function updateShippingBar(totalCents, cart) {
    var fill = document.getElementById('shipping-fill');
    var text = document.getElementById('shipping-text');
    if (!fill || !text) return;
    if (!isUS()) return;

    /* total_price is already after discounts. If SAVE2 (10%) isn't applied yet, warn when it would drop the cart under the threshold. */
    var note = document.getElementById('shipping-save2-note');
    if (note) {
      /* Only SAVE2 products get 10% off; handle list comes from snippets/save2-handles.liquid. */
      var dr = document.getElementById('cart-drawer');
      var s2 = ((dr && dr.getAttribute('data-save2-handles')) || '').split(',');
      var qQty = 0, qCents = 0;
      ((cart && cart.items) || []).forEach(function (it) {
        if (s2.indexOf(it.handle) > -1) { qQty += it.quantity; qCents += it.final_line_price; }
      });
      var num = 10 * FREE_SHIPPING_THRESHOLD - 10 * totalCents + qCents; /* 9 x amount still needed after SAVE2, in cents */
      var need = Math.ceil(num / 9);
      if (cart && !cart.total_discount && qQty >= 2 && totalCents >= FREE_SHIPPING_THRESHOLD && num > 0) {
        note.textContent = 'Discounts apply after free shipping is calculated on the next screen.';
        note.hidden = false;
      } else {
        note.hidden = true;
      }
    }

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
      if (count > 0) {
        el.removeAttribute('hidden');
        el.style.display = '';
      } else {
        el.setAttribute('hidden', '');
        el.style.display = 'none';
      }
    });
  }

  /* ── Event Binding ── */

  function bindAddToCartForms() {
    document.querySelectorAll('form[action*="/cart/add"]').forEach(function (form) {
      if (form.dataset.ajaxBound) return;
      form.dataset.ajaxBound = 'true';
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var idInput = form.querySelector('[name="id"]');
        if (!idInput || !idInput.value) return;
        var qtyInput = form.querySelector('[name="quantity"]');
        var qty = qtyInput ? parseInt(qtyInput.value, 10) || 1 : 1;
        var btn = form.querySelector('[type="submit"], button[name="add"]');
        var prev = btn ? btn.textContent : '';
        if (btn) {
          btn.disabled = true;
          btn.textContent = 'Adding\u2026';
        }
        addToCart(parseInt(idInput.value, 10), qty)
          .catch(function () {
            showError(form, 'This item is currently unavailable');
            window.location.href = form.getAttribute('action') || '/cart';
          })
          .finally(function () {
            if (btn) {
              btn.disabled = false;
              btn.textContent = prev || 'Add to cart';
            }
          });
      });
    });
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

    drawer.querySelectorAll('[data-bundle-add-pant]').forEach(function (btn) {
      if (btn.dataset.bound) return;
      btn.dataset.bound = 'true';
      btn.addEventListener('click', function () {
        if (btn.disabled) return;
        var vid = parseInt(btn.getAttribute('data-variant-id'), 10);
        if (!vid) return;
        addToCart(vid, 1);
      });
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

  var moneySample, moneyFmt;
  function formatMoney(cents) {
    var cur = window.Shopify && window.Shopify.currency && window.Shopify.currency.active;
    if (!cur || cur === 'USD') return '$' + (cents / 100).toFixed(2).replace(/\.00$/, '');
    if (moneyFmt === undefined) moneyFmt = parseMoneyFormat(moneySample);
    return formatWith(moneyFmt, cents, cur);
  }

  /* Non-USD (Shopify Markets): format like the store's own `| money` output for the active
     currency. The format (symbol, symbol side, separators, decimals) is read from a price the
     server rendered with `| money`; same trailing ".00" trim as the USD line above. */
  function parseMoneyFormat(sample) {
    sample = (sample || '').trim();
    var m = /\d(?:[\d.,'\u00a0 ]*\d)?/.exec(sample);
    if (!m) return null;
    var run = m[0];
    var dec = /[.,]\d{2}$/.test(run) ? run.charAt(run.length - 3) : '';
    var intPart = dec ? run.slice(0, -3) : run;
    var sep = intPart.replace(/\d/g, '').charAt(0) || (dec === ',' ? '.' : ',');
    return { pre: sample.slice(0, m.index), suf: sample.slice(m.index + run.length), dec: dec, sep: sep };
  }

  function formatWith(f, cents, cur) {
    if (!f) {
      try { return new Intl.NumberFormat(undefined, { style: 'currency', currency: cur }).format(cents / 100); } catch (e) { return (cents / 100).toFixed(2); }
    }
    var n = f.dec ? (cents / 100).toFixed(2) : String(Math.round(cents / 100));
    var p = n.split('.');
    var out = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, f.sep);
    if (p[1] && p[1] !== '00') out += f.dec + p[1];
    return f.pre + out + f.suf;
  }

  /* Free shipping ($150+) is US-only. Unknown country keeps the previous behaviour. */
  function isUS() {
    var c = window.Shopify && window.Shopify.country;
    return !c || c === 'US';
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
    close: closeDrawer,
    __initialized: true
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
