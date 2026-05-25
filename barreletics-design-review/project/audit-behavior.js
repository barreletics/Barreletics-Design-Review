/* Tab switching for section mocks (vanilla, no React) */
document.addEventListener('click', (e) => {
  const tab = e.target.closest('.au-mock__tab');
  if (!tab) return;
  const group = tab.dataset.group;
  const target = tab.dataset.target;
  if (!group || !target) return;

  document.querySelectorAll(`.au-mock__tab[data-group="${group}"]`).forEach(t => {
    t.setAttribute('aria-selected', t === tab ? 'true' : 'false');
  });
  document.querySelectorAll(`[data-panel-group="${group}"]`).forEach(p => {
    p.dataset.active = (p.dataset.panel === target) ? 'true' : 'false';
  });
});

/* Smooth scroll for nav links */
document.addEventListener('click', (e) => {
  const a = e.target.closest('a[href^="#"]');
  if (!a) return;
  const id = a.getAttribute('href').slice(1);
  const target = document.getElementById(id);
  if (!target) return;
  e.preventDefault();
  const y = target.getBoundingClientRect().top + window.pageYOffset - 80;
  window.scrollTo({ top: y, behavior: 'smooth' });
});
