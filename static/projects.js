(() => {
  const root = document.querySelector('[data-projects]');
  if (!root) return;
  const entries = [...root.querySelectorAll('.project-entry')];
  const filters = [...root.querySelectorAll('[data-filter]')];
  const search = root.querySelector('input[type="search"]');
  const count = root.querySelector('.project-count');
  const empty = root.querySelector('.projects-empty');
  let category = 'All';
  const update = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    entries.forEach(entry => {
      entry.hidden = !(category === 'All' || entry.dataset.category === category) || !entry.textContent.toLocaleLowerCase().includes(query);
      if (!entry.hidden) visible++;
    });
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === category)));
    count.textContent = `${visible} of ${entries.length} projects`;
    empty.hidden = visible !== 0;
  };
  filters.forEach(button => button.addEventListener('click', () => { category = button.dataset.filter; update(); }));
  search.addEventListener('input', update);
  root.querySelector('[data-clear]').addEventListener('click', () => { category = 'All'; search.value = ''; update(); search.focus(); });
  root.querySelector('.projects-tools').hidden = false;
  update();
  const dialog = root.querySelector('dialog');
  if (typeof dialog.showModal !== 'function') return;
  let opener;
  let previewImage;
  let playing = false;
  const motion = document.createElement('button');
  motion.type = 'button'; motion.className = 'preview-motion'; motion.hidden = true;
  dialog.querySelector('.preview-close').before(motion);
  const updatePlayback = () => {
    if (!previewImage?.dataset.gif) return;
    dialog.querySelector('img').src = playing ? previewImage.dataset.gif : previewImage.dataset.still;
    motion.textContent = playing ? 'Pause animation' : 'Play animation';
    motion.setAttribute('aria-pressed', String(playing));
  };
  motion.addEventListener('click', () => { playing = !playing; updatePlayback(); });
  root.querySelectorAll('[data-preview]').forEach(link => link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault(); opener = link;
    let img = dialog.querySelector('img');
    if (!img) { img = document.createElement('img'); dialog.querySelector('figure').prepend(img); }
    previewImage = link.querySelector('img');
    img.alt = previewImage.alt;
    motion.hidden = !previewImage.dataset.gif;
    if (previewImage.dataset.gif) {
      playing = previewImage.src === new URL(previewImage.dataset.gif, location.href).href;
      updatePlayback();
    } else { img.src = link.href; }
    dialog.querySelector('figcaption').textContent = link.dataset.caption;
    dialog.showModal();
  }));
  const closePreview = () => { dialog.close(); opener?.focus(); };
  dialog.querySelector('.preview-close').addEventListener('click', closePreview);
  dialog.addEventListener('cancel', event => { event.preventDefault(); closePreview(); });
  dialog.addEventListener('click', event => { if (event.target === dialog) { const box = dialog.getBoundingClientRect(); if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) closePreview(); } });
  dialog.addEventListener('close', () => opener?.focus());
})();
