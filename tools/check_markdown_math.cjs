#!/usr/bin/env node
/* Validate every inline/display formula with local MathJax 3.2.2.
 * GitHub's actual renderer/configuration is not exercised.
 * Optional --html writes local SVG previews for visual inspection.
 */
const fs = require('fs');
const path = require('path');
const cp = require('child_process');
const crypto = require('crypto');
const {mathjax} = require('./markdown-math-check/node_modules/mathjax-full/js/mathjax.js');
const {TeX} = require('./markdown-math-check/node_modules/mathjax-full/js/input/tex.js');
const {SVG} = require('./markdown-math-check/node_modules/mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('./markdown-math-check/node_modules/mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('./markdown-math-check/node_modules/mathjax-full/js/handlers/html.js');
const {AllPackages} = require('./markdown-math-check/node_modules/mathjax-full/js/input/tex/AllPackages.js');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const root = path.resolve(__dirname, '..');
const pandoc = process.env.PANDOC || path.join(__dirname, 'pandoc/pandoc');
const args = process.argv.slice(2);
const html = args.includes('--html');
const files = args.filter(x => x !== '--html');
if (!files.length) {
  for (const f of fs.readdirSync(path.join(root, 'papers')).sort()) {
    if (/^P\d\d-/.test(f)) files.push(path.join(root, 'papers', f, 'manuscript.md'));
  }
}
const reports = [];
for (const file of files) {
  const tex = new TeX({
    packages: AllPackages.filter(x => !['noerrors', 'noundefined', 'physics'].includes(x)),
    tags: 'ams',
    formatError: (_jax, err) => { throw err; }
  });
  const document = mathjax.document('', {InputJax: tex, OutputJax: new SVG({fontCache:'none'})});
  const ast = JSON.parse(cp.execFileSync(pandoc, [file, '-f', 'gfm', '-t', 'json'], {encoding:'utf8', maxBuffer:20e6}));
  const errors = [];
  let count = 0;
  function walk(obj) {
    if (Array.isArray(obj)) return obj.map(walk);
    if (!obj || typeof obj !== 'object') return obj;
    let formula, display;
    if (obj.t === 'Math') {
      formula = obj.c[1]; display = obj.c[0].t === 'DisplayMath';
    } else if (obj.t === 'CodeBlock' && obj.c[0][1].includes('math')) {
      formula = obj.c[1]; display = true;
    }
    if (formula !== undefined) {
      count++;
      try {
        const node = document.convert(formula, {display});
        const svg = adaptor.outerHTML(node);
        if (svg.includes('data-mml-node="merror"')) throw new Error('MathJax merror');
        if (html) return {t: obj.t === 'CodeBlock' ? 'RawBlock' : 'RawInline', c:['html', svg]};
      } catch (err) {
        errors.push({index:count, formula, message:String(err.message || err)});
      }
      return obj;
    }
    const next = {};
    for (const [key,value] of Object.entries(obj)) next[key] = walk(value);
    return next;
  }
  const output = walk(ast);
  if (html && !errors.length) {
    const rendered = cp.execFileSync(pandoc, ['-f','json','-t','html5','--standalone',
      '--metadata','pagetitle=Manuscript Markdown preview'], {input:JSON.stringify(output),encoding:'utf8',maxBuffer:50e6});
    const styled = rendered.replace('</head>', '<style>body{max-width:1050px;margin:40px auto;padding:0 24px;font:18px/1.55 Georgia,serif}mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden;padding:8px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #bbb;padding:5px 12px}a{color:#0645ad}h1{line-height:1.2}</style></head>');
    const qa = path.join(path.dirname(file),'markdown-qa');
    fs.mkdirSync(qa,{recursive:true});
    fs.writeFileSync(path.join(qa,'preview.html'),styled);
  }
  const report = {file:path.relative(root,file),mathjax_version:'3.2.2',
    markdown_sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'),
    validator_sha256:crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),
    expressions:count,errors,local_svg_preview_created:html && !errors.length,
    local_visual_inspection:false,github_live_render_inspected:false};
  const outname = path.join(path.dirname(file),'markdown-math-check.json');
  fs.writeFileSync(outname,JSON.stringify(report,null,2)+'\n');
  reports.push(report);
  console.log(path.basename(path.dirname(file)),count,'expressions,',errors.length,'errors');
}
const collections = [...new Set(files.map(file=>path.dirname(path.dirname(path.resolve(file)))))];
const manifestFolder = collections.length === 1 ? collections[0] : root;
fs.writeFileSync(path.join(manifestFolder,'markdown-math-check-manifest.json'),JSON.stringify({
  note:'Local MathJax syntax validation, not a live GitHub rendering test.',reports},null,2)+'\n');
if (reports.some(r=>r.errors.length)) process.exitCode=1;
