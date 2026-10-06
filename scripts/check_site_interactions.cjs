// Run with jsdom available through NODE_PATH or node_modules.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.resolve(__dirname, '..');
const source = name => fs.readFileSync(path.join(root, 'static', name), 'utf8');

function analytics(url) {
  const dom = new JSDOM(`<a id="email" href="mailto:private@example.com?subject=Private">Contact</a>
    <a id="pdf" href="/cv/jien-weng-lai-public-cv.pdf">PDF</a>
    <a id="text" href="/cv/profile.txt">Text</a>
    <a id="project" href="/projects/videoflow/?private=secret">Project</a>
    <a id="other" href="/notes/">Writing</a><video controls></video>`, {url, runScripts:'outside-only'});
  const events = [];
  dom.window.goatcounter = {count: event => events.push(event)};
  dom.window.document.addEventListener('click', event => event.preventDefault());
  dom.window.eval(source('site.js'));
  for (const id of ['email','pdf','text','project','other']) dom.window.document.getElementById(id).click();
  const video = dom.window.document.querySelector('video');
  video.dispatchEvent(new dom.window.Event('play'));
  video.dispatchEvent(new dom.window.Event('play'));
  return events;
}

async function motion(reduced) {
  const dom = new JSDOM('<figure><video data-preview-video data-src="/demo.mp4"></video><button class="motion-toggle" hidden></button></figure>', {url:'https://example.com',runScripts:'outside-only',pretendToBeVisual:true});
  const {window} = dom;
  let preference, observer, paused = true, starts = 0;
  const media = {matches:reduced,addEventListener:(_, callback) => {preference=callback}};
  window.matchMedia = () => media;
  window.IntersectionObserver = class {constructor(callback) {observer=callback} observe() {}};
  const video = window.document.querySelector('video');
  const button = window.document.querySelector('button');
  video.play = () => {paused=false;starts++;return Promise.resolve()};
  video.pause = () => {paused=true};
  window.eval(source('portfolio.js'));
  assert.equal(video.getAttribute('src'), null, 'Offscreen previews must not fetch video');
  observer([{isIntersecting:true}]);
  if (reduced) {
    assert.equal(video.getAttribute('src'), null, 'Reduced motion must preserve the poster until requested');
    assert.equal(button.textContent,'Play animation');
    button.click();
  }
  assert.equal(paused,false);
  assert.equal(video.getAttribute('src'),'/demo.mp4');
  observer([{isIntersecting:false}]);
  assert.equal(paused,true,'Offscreen playback must stop');
  observer([{isIntersecting:true}]);
  assert.equal(paused,false,'Requested playback resumes when visible');
  button.click();
  assert.equal(paused,true);
  assert.equal(button.getAttribute('aria-pressed'),'false');
  media.matches = true;
  preference({matches:true});
  assert.equal(paused,true);
  assert.ok(starts >= 2);
}

function gifMotion() {
  const dom = new JSDOM('<figure><img data-animated data-gif="/demo.gif" data-still="/still.webp"><button class="motion-toggle" hidden></button></figure>', {url:'https://example.com',runScripts:'outside-only'});
  dom.window.matchMedia = () => ({matches:true,addEventListener() {}});
  dom.window.eval(source('portfolio.js'));
  const image = dom.window.document.querySelector('img');
  const button = dom.window.document.querySelector('button');
  assert.equal(image.getAttribute('src'),'/still.webp');
  button.click();
  assert.equal(image.getAttribute('src'),'/demo.gif');
  button.click();
  assert.equal(image.getAttribute('src'),'/still.webp');
}

(async () => {
  const events = analytics('https://jienweng.github.io/projects/videoflow/');
  assert.deepEqual(events.map(e=>e.path), ['contact-email','cv-download-pdf','cv-read-text','project-open-videoflow','project-demo-play']);
  assert.equal(events.some(e=>JSON.stringify(e).includes('secret')||JSON.stringify(e).includes('private@example.com')),false);
  assert.equal(analytics('http://localhost:8766/').length,0);
  assert.equal(analytics('https://jienweng.github.io/pr-preview/pr-15/').length,0);
  gifMotion();
  await motion(false);
  await motion(true);
  console.log('Interaction checks passed: event whitelist, preview isolation, one-time demo event, reduced motion, and visible-only playback.');
})().catch(error => {console.error(error);process.exitCode=1});
