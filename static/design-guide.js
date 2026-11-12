(() => {
  const button = document.getElementById('copy-design-prompt');
  const prompt = document.getElementById('design-review-prompt');
  const status = document.getElementById('design-copy-status');
  if (!button || !prompt || !status) return;
  button.hidden = false;
  button.addEventListener('click', async () => {
    button.disabled = true;
    try {
      await navigator.clipboard.writeText(prompt.textContent.trim());
      status.textContent = 'Prompt copied. Paste it into your AI assistant and add your interface.';
    } catch {
      status.textContent = 'Copy was unavailable. Select the prompt above and copy it manually.';
    } finally {
      button.disabled = false;
    }
  });
})();
