(function () {
  const giscusContainer = document.getElementById("giscus-container");
  if (giscusContainer && window.giscusConfig) {
    const script = document.createElement("script");
    script.src = "https://giscus.app/client.js";
    script.async = true;
    script.crossOrigin = "anonymous";
    script.setAttribute("data-repo", window.giscusConfig.repo);
    script.setAttribute("data-repo-id", window.giscusConfig.repoId);
    script.setAttribute("data-category", window.giscusConfig.category);
    script.setAttribute("data-category-id", window.giscusConfig.categoryId);
    script.setAttribute("data-mapping", window.giscusConfig.mapping);
    script.setAttribute("data-strict", window.giscusConfig.strict);
    script.setAttribute("data-reactions-enabled", window.giscusConfig.reactionsEnabled);
    script.setAttribute("data-emit-metadata", window.giscusConfig.emitMetadata);
    script.setAttribute("data-input-position", window.giscusConfig.inputPosition);
    script.setAttribute("data-lang", window.giscusConfig.lang);
    script.setAttribute("data-theme", "light");
    giscusContainer.appendChild(script);
  }
})();

// Count useful actions without collecting email addresses, search terms, or link queries.
(() => {
  if (location.hostname !== 'jienweng.github.io' || location.pathname.startsWith('/pr-preview/')) return;
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link || !window.goatcounter?.count) return;
    const url = new URL(link.href, location.href);
    let action;
    if (url.protocol === 'mailto:') action = 'contact-email';
    else if (url.origin === location.origin) {
      if (url.pathname === '/cv/jien-weng-lai-public-cv.pdf') action = 'cv-download-pdf';
      else if (url.pathname === '/cv/profile.txt') action = 'cv-read-text';
      else if (url.pathname === '/cv/') action = 'cv-open';
      else if (/^\/projects\/[^/]+\/$/.test(url.pathname)) action = 'project-open-' + url.pathname.split('/')[2];
      else if (url.pathname === '/blog/quandatics-crm-business-transformation/') action = 'project-open-crm';
    } else if (link.closest('.project-detail-actions')) {
      const project = location.pathname.split('/').filter(Boolean).pop();
      action = 'project-resource-' + project;
    }
    if (action) window.goatcounter.count({path: action, title: action.replaceAll('-', ' '), event: true});
  });
  const watched = new WeakSet();
  document.addEventListener('play', event => {
    const video = event.target;
    if (!(video instanceof HTMLVideoElement) || !video.controls || watched.has(video) || !window.goatcounter?.count) return;
    watched.add(video);
    window.goatcounter.count({path: 'project-demo-play', title: 'Play recorded project workflow', event: true});
  }, true);
})();
