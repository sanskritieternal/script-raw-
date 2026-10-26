import json
from pathlib import Path
p=(Path(__file__).resolve().parents[3] / 'expansion_185_367.txt')
r={}; current=None
for line in p.read_text(encoding='utf-8-sig').splitlines():
 if not line.strip(): continue
 if line.startswith('@'): current=line[1:];r.setdefault(current,[]);continue
 route,level,q,scope=line.split('|');parent,title=route.split(' / ',1)
 r[current].append({'parent':parent,'title':title,'level':level,'topics':[{'question':q,'coverage':scope}]})
p.with_suffix('.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(r),'niches',sum(len(s['topics']) for ss in r.values() for s in ss),'proposals')
