import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const out=path.join(root,'_site');
const base='/algebra-number-theory-drafts';
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);}
const files=walk(out),issues=[];let checkedLinks=0,pdfs=0,papers=0;
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
for(const f of files){
 const rel=path.relative(out,f);
 if(f.endsWith('.pdf')){if(hash(f)!==hash(path.join(root,rel)))issues.push(rel+': PDF differs from source');pdfs++;}
 if(!f.endsWith('.html'))continue;
 const html=fs.readFileSync(f,'utf8');
 if(/(?:MATH|ANCHOR)PLACEHOLDER\d+END|data-mjx-error/.test(html))issues.push(rel+': render error');
 if(!html.includes('rel="canonical"'))issues.push(rel+': missing canonical');
 if(/\/manuscript.html$/.test(rel)){
  papers++;
  for(const name of ['citation_title','citation_author','citation_publication_date','citation_pdf_url'])if(!html.includes(`name="${name}"`))issues.push(rel+': missing '+name);
  if(!html.includes('References')&&!html.includes('Bibliography'))issues.push(rel+': no references');
 }
 for(const m of html.matchAll(/(?:href|src)="([^"<>]+)"/g)){
  const href=m[1].replaceAll('&amp;','&');
  if(/^(?:https?:|mailto:|data:)/i.test(href))continue;
  const url=new URL(href,'https://hwzw.github.io'+base+'/'+rel);
  if(!url.pathname.startsWith(base+'/'))continue;
  let target=path.join(out,decodeURIComponent(url.pathname.slice(base.length+1)));
  if(url.pathname.endsWith('/'))target=path.join(target,'index.html');
  checkedLinks++;
  if(!fs.existsSync(target)){issues.push(`${rel}: missing ${href}`);continue;}
  if(url.hash&&target.endsWith('.html')){
   const content=fs.readFileSync(target,'utf8');const id=decodeURIComponent(url.hash.slice(1));
   if(!content.includes(`id="${id}"`))issues.push(`${rel}: missing anchor ${href}`);
  }
 }
}
console.log(JSON.stringify({htmlPages:files.filter(f=>f.endsWith('.html')).length,paperEditions:papers,identicalPDFs:pdfs,checkedLinks,issues:issues.length},null,2));
if(issues.length){console.error(issues.join('\n'));process.exitCode=1;}
