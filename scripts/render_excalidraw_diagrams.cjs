/** Render the editable scenes with Excalidraw's Rough.js stroke style.
 * npm install --prefix /tmp/portfolio-excalidraw-render roughjs jsdom
 * NODE_PATH=/tmp/portfolio-excalidraw-render/node_modules node scripts/render_excalidraw_diagrams.cjs
 * The font is embedded so SVGs remain portable.
 */
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const rough = require('roughjs/bundled/rough.cjs.js');
const root = path.resolve(__dirname, '..');
const font = fs.readFileSync(path.join(root, 'static/fonts/excalifont.woff2')).toString('base64');
const files = ['img/blog/quandatics/deal-to-cash', 'img/blog/quandatics/project-to-cash',
  'img/blog/quandatics/o2c-p2p', 'img/projects/cryptorails-deposit-flow'];
for (const file of files) {
  const source = path.join(root, 'static', file + '.excalidraw');
  const scene = JSON.parse(fs.readFileSync(source));
  const dom = new JSDOM('<!doctype html><html><body></body></html>');
  const doc = dom.window.document;
  const ns = 'http://www.w3.org/2000/svg';
  const svg = doc.createElementNS(ns, 'svg');
  const height = Math.ceil(Math.max(...scene.elements.map(e => e.y+e.height))+40);
  svg.setAttribute('xmlns', ns); svg.setAttribute('width', 1600);
  svg.setAttribute('height', height); svg.setAttribute('viewBox', `0 0 1600 ${height}`);
  svg.setAttribute('role', 'img'); svg.setAttribute('aria-labelledby', 'title');
  const title = doc.createElementNS(ns, 'title'); title.id = 'title';
  title.textContent = scene.elements[0].text; svg.appendChild(title);
  const style = doc.createElementNS(ns, 'style');
  style.textContent = `@font-face{font-family:Excalifont;src:url(data:font/woff2;base64,${font}) format('woff2')}text{font-family:Excalifont,cursive}`;
  svg.appendChild(style);
  const bg = doc.createElementNS(ns, 'rect');
  bg.setAttribute('width', '100%'); bg.setAttribute('height', '100%');
  bg.setAttribute('fill', scene.appState.viewBackgroundColor); svg.appendChild(bg);
  const rc = rough.svg(svg);
  for (const e of scene.elements) {
    const options = { seed:e.seed, roughness:e.roughness, stroke:e.strokeColor,
      strokeWidth:e.strokeWidth, disableMultiStroke:true, fill:e.backgroundColor==='transparent'?undefined:e.backgroundColor, fillStyle:e.fillStyle };
    if(e.type==='rectangle') svg.appendChild(rc.rectangle(e.x,e.y,e.width,e.height,options));
    if(e.type==='arrow') {
      const points=e.points.map(([x,y])=>[e.x+x,e.y+y]);
      svg.appendChild(rc.linearPath(points,options));
      const [a,b]=points.slice(-2); const angle=Math.atan2(b[1]-a[1],b[0]-a[0]);
      const ends=[angle-.5,angle+.5].map(t=>[b[0]-16*Math.cos(t),b[1]-16*Math.sin(t)]);
      svg.appendChild(rc.linearPath([ends[0],b,ends[1]],options));
    }
    if(e.type==='text') {
      const text=doc.createElementNS(ns,'text'); text.setAttribute('fill',e.strokeColor);
      text.setAttribute('font-size',e.fontSize);
      e.text.split('\n').forEach((line,i)=>{
        const span=doc.createElementNS(ns,'tspan'); span.setAttribute('x',e.x);
        span.setAttribute('y',e.y+e.fontSize*.94+i*e.fontSize*e.lineHeight);
        span.textContent=line; text.appendChild(span);
      }); svg.appendChild(text);
    }
  }
  const target = source.replace('.excalidraw','-excalidraw.svg');
  fs.writeFileSync(target,svg.outerHTML+'\n'); console.log(path.relative(root,target));
}
