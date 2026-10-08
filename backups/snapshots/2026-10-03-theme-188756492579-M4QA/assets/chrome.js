/* Global chrome behaviors — announcement rotation, sticky header, mobile nav */
(function () {
  function initAnnouncement() {
    var strip = document.querySelector('[data-announcement-strip]');
    if (!strip) return;
    var slides = strip.querySelectorAll('[data-slide-index]');
    if (slides.length <= 1) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    var current = 0;
    var paused = false;
    var speed = parseInt(strip.getAttribute('data-rotation-ms') || '4000', 10);

    strip.addEventListener('mouseenter', function () { paused = true; });
    strip.addEventListener('mouseleave', function () { paused = false; });

    setInterval(function () {
      if (paused) return;
      slides[current].classList.remove('is-active');
      current = (current + 1) % slides.length;
      slides[current].classList.add('is-active');
    }, speed);
  }

  function initHeader() {
    var header = document.querySelector('[data-site-header]');
    if (!header) return;

    var menuToggle = header.querySelector('[data-mobile-menu-toggle]');
    var menu = document.querySelector('[data-mobile-menu]');
    var closeButtons = document.querySelectorAll('[data-mobile-menu-close]');
    var parentItems = document.querySelectorAll('.mobile-menu__item--parent');

    function checkScroll() {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    }
    window.addEventListener('scroll', checkScroll, { passive: true });
    checkScroll();

    if (!menu || !menuToggle) return;

    function openMenu() {
      menu.classList.add('is-open');
      menu.setAttribute('aria-hidden', 'false');
      menuToggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }
    function closeMenu() {
      menu.classList.remove('is-open');
      menu.setAttribute('aria-hidden', 'true');
      menuToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    menuToggle.addEventListener('click', openMenu);
    closeButtons.forEach(function (btn) { btn.addEventListener('click', closeMenu); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) closeMenu();
    });

    parentItems.forEach(function (item) {
      var toggle = item.querySelector('.mobile-menu__toggle');
      if (!toggle) return;
      toggle.addEventListener('click', function () {
        var expanded = item.getAttribute('data-expanded') === 'true';
        item.setAttribute('data-expanded', expanded ? 'false' : 'true');
        toggle.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      });
    });
  }


  /* Kick muted autoplay videos so browsers don't sit on the native play button.
     Theme editor: only touch videos inside the section that just loaded.
     Re-scanning the whole Home (hero + problem + press) on every slider tick
     stalled live preview until Save. */
  function initAmbientVideos(scope) {
    var root = scope && scope.querySelectorAll ? scope : document;
    var nodes = root.querySelectorAll('video');
    if (!nodes.length) return;

    function kick(video) {
      if (!video || video.hasAttribute('controls')) return;
      if (video.hasAttribute('data-ambient-kicked') && !video.paused) return;
      video.muted = true;
      video.setAttribute('muted', '');
      video.setAttribute('playsinline', '');
      video.setAttribute('webkit-playsinline', '');
      var playPromise = video.play();
      if (playPromise && typeof playPromise.then === 'function') {
        playPromise
          .then(function () { video.setAttribute('data-ambient-kicked', '1'); })
          .catch(function () { /* autoplay still blocked — overlay CSS hides the button */ });
      } else {
        video.setAttribute('data-ambient-kicked', '1');
      }
    }

    function watch(video) {
      if (video.hasAttribute('controls')) return;
      if (video.getAttribute('data-ambient-bound') === '1') {
        kick(video);
        return;
      }
      video.setAttribute('data-ambient-bound', '1');
      kick(video);
      video.addEventListener('loadeddata', function () { kick(video); });
      video.addEventListener('canplay', function () { kick(video); });
    }

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) kick(entry.target);
        });
      }, { rootMargin: '120px 0px', threshold: 0.01 });
      nodes.forEach(function (video) {
        watch(video);
        io.observe(video);
      });
    } else {
      nodes.forEach(watch);
    }
  }

  document.addEventListener('shopify:section:load', function (event) {
    try {
      initAmbientVideos(event.target);
    } catch (err) { /* never block Theme Editor live preview */ }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initAnnouncement();
      initHeader();
      initAmbientVideos();
    });
  } else {
    initAnnouncement();
    initHeader();
    initAmbientVideos();
  }
})();
