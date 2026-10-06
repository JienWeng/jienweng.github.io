(() => {
  const menu = document.querySelector('.portfolio-menu');
  if (!menu) return;
  menu.addEventListener('click', (event) => {
    if (event.target.closest('a')) menu.open = false;
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.open) {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!menu.contains(event.target)) menu.open = false;
  });
})();

(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-animated]').forEach(image => {
    const button = image.closest('figure').querySelector('.motion-toggle');
    if (!button) return;
    const disclosure = image.closest('.more-work');
    let playing = !preference.matches;
    const update = () => { image.src = playing && (!disclosure || disclosure.open) ? image.dataset.gif : image.dataset.still; button.textContent = playing ? 'Pause animation' : 'Play animation'; button.setAttribute('aria-pressed', String(playing)); };
    disclosure?.addEventListener('toggle', update);
    button.hidden = false;
    button.addEventListener('click', () => { playing = !playing; update(); });
    preference.addEventListener('change', () => { playing = !preference.matches; update(); });
    update();
  });
})();

(() => {
  const disclosure = document.querySelector('.more-work');
  if (!disclosure) return;
  const collapse = disclosure.querySelector('.more-work-collapse');
  disclosure.classList.add('is-enhanced');
  collapse.hidden = false;
  collapse.addEventListener('click', () => { disclosure.open = false; disclosure.querySelector('summary').focus(); });
})();

(() => {
  const links = [...document.querySelectorAll('.crm-artifact a[href$=".svg"], .payment-artifact a[href$=".svg"]')];
  if (!links.length || typeof HTMLDialogElement === 'undefined' || typeof HTMLDialogElement.prototype.showModal !== 'function') return;
  const dialog = document.createElement('dialog');
  dialog.className = 'diagram-viewer';
  dialog.setAttribute('aria-label', 'Full-size diagram');
  dialog.innerHTML = '<div class="diagram-viewer-controls"><button type="button" class="diagram-zoom" aria-pressed="false">Actual size</button><button type="button" class="diagram-close">Close diagram</button></div><figure><div class="diagram-canvas"><img alt=""></div><figcaption></figcaption></figure>';
  document.body.append(dialog);
  const image = dialog.querySelector('img');
  const zoom = dialog.querySelector('.diagram-zoom');
  let opener;
  const resetZoom = () => { dialog.classList.remove('is-zoomed'); zoom.setAttribute('aria-pressed', 'false'); zoom.textContent = 'Actual size'; };
  const close = () => { dialog.close(); document.body.classList.remove('diagram-viewing'); opener?.focus(); };
  links.forEach(link => link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = link;
    const figure = link.closest('figure');
    image.src = link.href;
    image.alt = figure.querySelector('img').alt;
    dialog.querySelector('figcaption').textContent = image.alt;
    resetZoom();
    dialog.showModal();
    document.body.classList.add('diagram-viewing');
    dialog.querySelector('.diagram-close').focus();
  }));
  zoom.addEventListener('click', () => {
    const zoomed = dialog.classList.toggle('is-zoomed');
    zoom.setAttribute('aria-pressed', String(zoomed));
    zoom.textContent = zoomed ? 'Fit diagram' : 'Actual size';
  });
  dialog.querySelector('.diagram-close').addEventListener('click', close);
  dialog.addEventListener('cancel', event => { event.preventDefault(); close(); });
  dialog.addEventListener('close', () => { document.body.classList.remove('diagram-viewing'); opener?.focus(); });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) close();
  });
})();

(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-preview-video]').forEach(video => {
    const button = video.closest('figure').querySelector('.motion-toggle');
    if (!button) return;
    let requested = !preference.matches;
    let visible = false;
    const update = () => {
      const shouldPlay = requested && visible && !document.hidden;
      button.textContent = requested ? 'Pause animation' : 'Play animation';
      button.setAttribute('aria-pressed', String(requested));
      if (shouldPlay) {
        if (!video.getAttribute('src')) video.src = video.dataset.src;
        video.play().catch(error => {
          if (error.name !== 'AbortError') { requested = false; update(); }
        });
      } else video.pause();
    };
    button.hidden = false;
    button.addEventListener('click', () => { requested = !requested; update(); });
    preference.addEventListener('change', () => { requested = !preference.matches; update(); });
    document.addEventListener('visibilitychange', update);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(entries => {
        visible = entries[0].isIntersecting;
        update();
      }, {threshold: 0.1}).observe(video);
    } else visible = true;
    update();
  });
})();
