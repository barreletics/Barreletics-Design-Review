// Rotating ticker — cross-fades messages every 5s
(function () {
  const ticker = document.querySelector('.pdp-ticker');
  if (!ticker) return;
  const slides = ticker.querySelectorAll('.pdp-ticker__slide');
  if (slides.length < 2) return;
  let i = 0;
  setInterval(() => {
    slides[i].classList.remove('is-active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('is-active');
  }, 5000);
})();
