(() => {
  const root = document.querySelector('[data-writing]');
  if (!root) return;
  const entries = [...root.querySelectorAll('.essay-entry')];
  const topic = root.querySelector('select');
  const search = root.querySelector('input');
  const update = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    entries.forEach(entry => {
      entry.hidden = (topic.value !== 'all' && entry.dataset.topic !== topic.value) || !entry.textContent.toLocaleLowerCase().includes(query);
      if (!entry.hidden) visible++;
    });
    root.querySelectorAll('.reading-series').forEach(series => { series.hidden = !entries.some(entry => !entry.hidden && entry.dataset.topic === 'Regression'); });
    root.querySelectorAll('.writing-group').forEach(group => { group.hidden = ![...group.querySelectorAll('.essay-entry')].some(entry => !entry.hidden); });
    root.querySelector('.writing-count').textContent = `${visible} of ${entries.length} articles`;
    root.querySelector('.writing-empty').hidden = visible > 0;
  };
  topic.addEventListener('change', update);
  search.addEventListener('input', update);
  root.querySelector('[data-reset]').addEventListener('click', () => { topic.value = 'all'; search.value = ''; update(); search.focus(); });
  root.querySelector('.writing-controls').hidden = false;
  update();
})();
