import json
from pathlib import Path
r={};n=None
for line in (Path(__file__).resolve().parents[3] / 'editorial_pass_185_367.txt').read_text(encoding='utf-8-sig').splitlines():
 if not line:continue
 if line.startswith('@'):n=line[1:];r.setdefault(n,[]);continue
 route,level,q,scope=line.split('|');parent,title=route.split(' / ',1)
 r[n].append({'parent':parent,'title':title,'level':level,'topics':[{'question':q,'coverage':scope}]})
(Path(__file__).resolve().parents[3] / 'editorial_pass_185_367.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(r),'niches with substantive additions;',sum(len(g['topics']) for gs in r.values() for g in gs),'new proposals')
