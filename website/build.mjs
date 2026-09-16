import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import MarkdownIt from 'markdown-it';
import {mathjax} from 'mathjax-full/js/mathjax.js';
import {TeX} from 'mathjax-full/js/input/tex.js';
import {SVG} from 'mathjax-full/js/output/svg.js';
import {liteAdaptor} from 'mathjax-full/js/adaptors/liteAdaptor.js';
import {RegisterHTMLHandler} from 'mathjax-full/js/handlers/html.js';
import {AllPackages} from 'mathjax-full/js/input/tex/AllPackages.js';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out=path.join(root,'_site');
const base='/algebra-number-theory-drafts';
const origin='https://hwzw.github.io';
const repo='https://github.com/Hwzw/algebra-number-theory-drafts';
const sha=execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim();
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const plain=s=>s.replace(/\$`([^`]+)`\$/g,'$1').replace(/\$+/g,'').replace(/[*`#]/g,'').replace(/\[([^\]]+)\]\([^)]*\)/g,'$1').replace(/\s+/g,' ').trim();
const adaptor=liteAdaptor(); RegisterHTMLHandler(adaptor);
const doc=mathjax.document('',{InputJax:new TeX({packages:AllPackages.filter(p=>!['autoload','require'].includes(p)),tags:'none'}),OutputJax:new SVG({fontCache:'none'})});
const errors=[];let mathCount=0;let currentFile='';
function math(source,display){
  mathCount++;
  const node=doc.convert(source,{display});
  const html=adaptor.outerHTML(node);
  if(html.includes('data-mjx-error')) errors.push({file:currentFile,source,error:html.match(/data-mjx-error="([^"]*)"/)?.[1]});
  return `<span class="${display?'display-math':'inline-math'}" role="math" aria-label="${esc(source)}">${html}</span>`;
}
const md=new MarkdownIt({html:false,linkify:true,typographer:false});
md.renderer.rules.heading_open=(tokens,idx,opts,env,self)=>{
 const text=tokens[idx+1]?.content||'';
 tokens[idx].attrSet('id',plain(text).toLowerCase().replace(/[^\w\s-]/g,'').replace(/\s/g,'-'));
 return self.renderToken(tokens,idx,opts);
};
const defaultLink=md.renderer.rules.link_open||((tokens,idx,opts,env,self)=>self.renderToken(tokens,idx,opts));
md.renderer.rules.link_open=(tokens,idx,opts,env,self)=>{
  const token=tokens[idx];const href=token.attrGet('href');
  if(href&&!/^(?:[a-z]+:|#|\/)/i.test(href)){
    const parsed=new URL(href,'https://source.invalid/'+env.source);
    const rel=decodeURIComponent(parsed.pathname.slice(1));
    const target=path.join(root,rel);
    let url;
    if(fs.existsSync(target)&&fs.statSync(target).isFile()&&rel.endsWith('.md')) url=base+'/'+(rel==='README.md'?'collection.html':rel.replace(/README\.md$/,'index.html').replace(/\.md$/,'.html'));
    else if(rel.endsWith('/')) url=repo+'/tree/main/'+rel;
    else if(fs.existsSync(target)&&rel.endsWith('.pdf'))url=base+'/'+rel;
    else url=repo+'/blob/main/'+rel;
    token.attrSet('href',url+parsed.hash);
  }
  return defaultLink(tokens,idx,opts,env,self);
};
function render(text,source){
  currentFile=source;const stash=[];
  const save=(s,display)=>{const n=stash.length;stash.push(math(s,display));return `MATHPLACEHOLDER${n}END`;};
  // Preserve math before Markdown can reinterpret underscores, backslashes, or pipes.
  text=text.replace(/```math\s*\n([\s\S]*?)```/g,(_,s)=>'\n\n'+save(s.trim(),true)+'\n\n');
  text=text.replace(/\$\$([\s\S]*?)\$\$/g,(_,s)=>'\n\n'+save(s.trim(),true)+'\n\n');
  text=text.replace(/\$`([^`]*?)`\$/g,(_,s)=>save(s,false));
  text=text.replace(/(?<!\\)\$(?!\s)([^\n$]+?)(?<!\s)(?<!\\)\$/g,(_,s)=>save(s,false));
  const anchors=[];
  text=text.replace(/<a id="([\w:-]+)"><\/a>/g,(_,id)=>{anchors.push(`<a id="${esc(id)}"></a>`);return `ANCHORPLACEHOLDER${anchors.length-1}END`;});
  text=text.replace(/<!--[\s\S]*?-->/g,'');
  return md.render(text,{source}).replace(/MATHPLACEHOLDER(\d+)END/g,(_,n)=>stash[+n]).replace(/ANCHORPLACEHOLDER(\d+)END/g,(_,n)=>anchors[+n]);
}
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.name.startsWith('.')?[]:e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);}
const files=['README.md','CITATIONS.md','REPRODUCIBILITY.md','SCOPE.md',...['papers','selected_papers','reassessment'].flatMap(d=>walk(path.join(root,d)).map(f=>path.relative(root,f)))];
const markdown=files.filter(f=>f.endsWith('.md'));
const paperFiles=markdown.filter(f=>/^(papers|selected_papers)\/P\d+[^/]*\/manuscript\.md$/.test(f));
function info(file){
  const text=fs.readFileSync(path.join(root,file),'utf8');
  const title=plain(text.match(/^# (.+)$/m)?.[1]||path.basename(file));
  const abstract=text.match(/^## Abstract\s*\n([\s\S]*?)(?=^## |$(?![\s\S]))/m)?.[1]?.trim()||'';
  const dateString=text.slice(0,600).match(/(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}/)?.[0];
  const texFile=path.join(root,path.dirname(file),'manuscript.tex');
  const tex=fs.existsSync(texFile)?fs.readFileSync(texFile,'utf8'):'';
  const year=(text.slice(0,200).match(/\b(20\d{2})\b/)||tex.match(/\\date\{[^}]*?(20\d{2})/))?.[1]||execFileSync('git',['log','--diff-filter=A','--format=%aI','--',file],{cwd:root,encoding:'utf8'}).trim().split('\n').at(-1).slice(0,4);
  if(!/^20\d{2}$/.test(year))throw new Error('No publication year: '+file);
  const date=dateString?new Date(dateString+' 12:00:00 UTC').toISOString().slice(0,10):year;
  const folder=path.dirname(file);const id=folder.split('/').at(-1).split('-')[0];
  return {file,text,title,abstract,date,dateString,folder,id,selected:file.startsWith('selected_papers/'),url:base+'/'+folder+'/manuscript.html'};
}
const papers=paperFiles.map(info).sort((a,b)=>Number(b.id.slice(1))-Number(a.id.slice(1))||Number(b.selected)-Number(a.selected));
const distinct=new Set(papers.map(p=>p.id)).size;
function shell({title,description,content,url,meta='',bodyClass=''}){
return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="google-site-verification" content="CI4xkTu6GNijZ08gdr0l2779WoAxMwGxkB2jNNXivRE"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${esc(title)}${title==='Henry Zweiman'?' — Mathematical research':' | Henry Zweiman'}</title><meta name="description" content="${esc(description)}"><meta name="author" content="Henry Zweiman"><meta name="robots" content="index,follow"><link rel="canonical" href="${origin}${url}"><meta property="og:type" content="article"><meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(description)}"><meta property="og:url" content="${origin}${url}"><link rel="icon" href="${base}/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="${base}/assets/site.css">${meta}</head><body class="${bodyClass}"><a class="skip" href="#main">Skip to content</a><header class="site-header"><a class="wordmark" href="${base}/"><span class="monogram">HZ</span> Henry Zweiman</a><nav aria-label="Main navigation"><a href="${base}/#papers">Manuscripts</a><a href="${repo}">GitHub <span aria-hidden="true">↗</span></a></nav></header>${content}<footer><span>Henry Zweiman · Mathematical research</span><a href="${repo}/commit/${sha}">Source version ${sha.slice(0,7)}</a></footer></body></html>`;
}
fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(path.join(out,'assets'),{recursive:true});
fs.copyFileSync(path.join(root,'website/site.css'),path.join(out,'assets/site.css'));
fs.writeFileSync(path.join(out,'assets/favicon.svg'),'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="10" fill="#182c48"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-size="33" fill="white">H</text></svg>');
const routes=[];
function write(rel,html){fs.mkdirSync(path.dirname(path.join(out,rel)),{recursive:true});fs.writeFileSync(path.join(out,rel),html);routes.push(base+'/'+rel);}
const featured=papers.find(p=>!p.selected);
const rows=papers.filter(p=>!p.selected).map(p=>{
  const revised=papers.find(r=>r.selected&&r.id===p.id);const primary=revised||p;
  return `<li class="paper-row"><div class="paper-number">${p.id}</div><div><h3><a href="${primary.url}">${esc(primary.title)}</a></h3><p class="summary">${esc(plain(primary.abstract).slice(0,245))}${plain(primary.abstract).length>245?'…':''}</p><div class="paper-meta"><span>${esc(primary.dateString||'Research manuscript')}</span>${revised?'<span class="edition">Revised edition</span>':''}</div></div><div class="row-links"><a href="${primary.url}">Read paper</a><a href="${base}/${primary.folder}/manuscript.pdf">PDF</a>${revised?`<a href="${p.url}">Original</a>`:''}</div></li>`;
}).join('');
write('index.html',shell({title:'Henry Zweiman',description:`Mathematical research by Henry Zweiman. Read ${distinct} manuscripts, full proofs, revisions, and typeset PDFs.`,url:base+'/',content:`<main id="main"><section class="intro"><div><p class="eyebrow">Mathematical research</p><h1>Henry Zweiman</h1><p class="intro-copy">Manuscripts in algebra, number theory,<br class="desktop-break"> and analysis.</p></div><div class="collection-count"><strong>${distinct}</strong><span>distinct manuscripts</span><a href="${base}/#papers">Browse the collection ↓</a></div></section><aside class="notice"><strong>Research drafts.</strong> Prepared with OpenAI Codex and AI collaborators. Not peer reviewed or independently verified by human experts. See each paper’s assessment for scope and prior work.</aside><section class="latest" aria-labelledby="latest-title"><div><p class="eyebrow">Latest manuscript · ${featured.id}</p><h2 id="latest-title"><a href="${featured.url}">${esc(featured.title)}</a></h2></div><div><p>${esc(plain(featured.abstract).slice(0,360))}…</p><a class="text-link" href="${featured.url}">Read the full paper <span aria-hidden="true">→</span></a></div></section><section id="papers" class="catalog"><div class="section-heading"><h2>The manuscripts</h2><span>${distinct} papers · ${papers.filter(p=>p.selected).length} revised editions</span></div><ol class="paper-list">${rows}</ol></section></main>`}));
for(const file of markdown){
  const text=fs.readFileSync(path.join(root,file),'utf8');
  const p=papers.find(p=>p.file===file);
  const rel=file==='README.md'?'collection.html':file.replace(/README\.md$/,'index.html').replace(/\.md$/,'.html');
  const title=p?.title||plain(text.match(/^# (.+)$/m)?.[1]||path.basename(file));
  const description=p?plain(p.abstract).slice(0,300):`${title}. Supporting material for Henry Zweiman's mathematical research.`;
  const alternate=p&&papers.find(q=>q.id===p.id&&q.selected!==p.selected);
  let meta='';let contents='';
  if(p){
    const pdf=`${origin}${base}/${p.folder}/manuscript.pdf`;
    meta=`<meta name="citation_title" content="${esc(p.title)}"><meta name="citation_author" content="Henry Zweiman">${p.date?`<meta name="citation_publication_date" content="${p.date.replaceAll('-','/')}">`:''}<meta name="citation_pdf_url" content="${pdf}"><script type="application/ld+json">${JSON.stringify({'@context':'https://schema.org','@type':'ScholarlyArticle',headline:p.title,author:{'@type':'Person',name:'Henry Zweiman'},...(p.date?{datePublished:p.date}:{}),description:plain(p.abstract),url:origin+p.url,encoding:{'@type':'MediaObject',contentUrl:pdf,encodingFormat:'application/pdf'},creativeWorkStatus:'Research preprint',isBasedOn:repo+'/blob/'+sha+'/'+file}).replace(/</g,'\\u003c')}</script>`;
    const sections=[...text.matchAll(/^## (.+)$/gm)].map((m,i)=>({title:plain(m[1]),id:`section-${i}`}));
    let i=0;const body=render(text.replace(/^# .+\n/,'').replace(/^## (.+)$/gm,(_,t)=>`<a id="section-${i++}"></a>\n\n## ${t}`),file);
    const resources=['README.md','ASSESSMENT.md','REVIEW.md'].filter(f=>fs.existsSync(path.join(root,p.folder,f))).map(f=>`<a href="${base}/${p.folder}/${f==='README.md'?'index.html':f.replace('.md','.html')}">${({ 'README.md':'Overview','ASSESSMENT.md':'Assessment','REVIEW.md':'Review record'})[f]}</a>`).join('');
    contents=`<main id="main" class="paper-layout"><aside class="paper-sidebar"><a class="back-link" href="${base}/#papers">← All manuscripts</a><p class="eyebrow">${p.id} ${p.selected?'· Revised edition':''}</p><a class="pdf-button" href="${base}/${p.folder}/manuscript.pdf">Read the PDF</a><nav class="contents" aria-label="On this page"><p>Contents</p>${sections.map(s=>`<a href="#${s.id}">${esc(s.title)}</a>`).join('')}</nav><nav class="resources" aria-label="Paper resources">${resources}<a href="${repo}/blob/main/${file}">Markdown on GitHub ↗</a><a href="${repo}/blob/main/${p.folder}/manuscript.tex">LaTeX source ↗</a>${alternate?`<a href="${alternate.url}">${p.selected?'Original':'Revised'} edition</a>`:''}</nav></aside><article class="manuscript"><header class="paper-heading"><p class="eyebrow">Research preprint</p><h1>${esc(p.title)}</h1></header><aside class="paper-notice">AI-assisted research draft. Not peer reviewed or independently human-verified.</aside><div class="prose">${body}</div></article></main>`;
  }else contents=`<main id="main" class="support-page"><a class="back-link" href="${base}/#papers">← All manuscripts</a><div class="prose">${render(text,file)}</div><p class="source-link"><a href="${repo}/blob/main/${file}">View this document on GitHub ↗</a></p></main>`;
  write(rel,shell({title,description,url:base+'/'+rel,meta,content:contents,bodyClass:p?'paper-page':'support'}));
}
for(const file of files.filter(f=>f.endsWith('.pdf'))){fs.mkdirSync(path.dirname(path.join(out,file)),{recursive:true});fs.copyFileSync(path.join(root,file),path.join(out,file));}
write('404.html',shell({title:'Page not found',description:'This research page could not be found.',url:base+'/404.html',content:`<main id="main" class="support-page"><p class="eyebrow">404</p><h1>Page not found</h1><p>The manuscript may have moved.</p><a href="${base}/">Return to the manuscript collection</a></main>`}));
fs.writeFileSync(path.join(out,'sitemap.xml'),`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${routes.filter(r=>!r.endsWith('404.html')).map(r=>`<url><loc>${origin}${r.endsWith('/index.html')?r.replace(/index.html$/,''):r}</loc></url>`).join('')}</urlset>`);
fs.writeFileSync(path.join(out,'.nojekyll'),'');
fs.writeFileSync(path.join(out,'build-report.json'),JSON.stringify({commit:sha,distinctManuscripts:distinct,editions:papers.length,pages:routes.length,mathExpressions:mathCount,mathErrors:errors},null,2));
console.log(JSON.stringify({distinctManuscripts:distinct,editions:papers.length,pages:routes.length,mathExpressions:mathCount,mathErrors:errors.length}));
if(errors.length){console.error(JSON.stringify(errors.slice(0,20),null,2));process.exitCode=1;}
