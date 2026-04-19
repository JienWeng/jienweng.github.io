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
