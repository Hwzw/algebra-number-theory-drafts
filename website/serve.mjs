import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../_site');
const base='/algebra-number-theory-drafts';
const types={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.svg':'image/svg+xml','.pdf':'application/pdf','.xml':'application/xml','.json':'application/json'};
http.createServer((req,res)=>{
 const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
 if(pathname==='/'){res.writeHead(302,{Location:base+'/'});return res.end();}
 if(!pathname.startsWith(base+'/')){res.writeHead(404);return res.end('Not found');}
 let file=path.resolve(root,pathname.slice(base.length+1)||'index.html');
 if(!file.startsWith(root+path.sep)&&file!==root){res.writeHead(403);return res.end();}
 if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');
 if(!fs.existsSync(file)){res.writeHead(404);return res.end('Not found');}
 res.writeHead(200,{'Content-Type':types[path.extname(file)]||'application/octet-stream'});fs.createReadStream(file).pipe(res);
}).listen(8766,'127.0.0.1',()=>console.log('http://127.0.0.1:8766/algebra-number-theory-drafts/'));
