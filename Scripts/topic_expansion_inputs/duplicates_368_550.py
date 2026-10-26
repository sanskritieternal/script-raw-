import json,re
from pathlib import Path
from collections import defaultdict
items=[]
for p in Path('topics').glob('*/IN_DEPTH_TOPIC_BANK.json'):
    if 368<=int(p.parent.name[:3])<=550:
        b=json.loads(p.read_text(encoding='utf-8'));items.extend((b['niche_id'],t['id'],t['question'],t['coverage']) for c in b['categories'] for t in c['topics'])
stop=set('how why what which when can does do is a an the in of to and or for with from as be rather than one same different'.split())
def words(q):return set(re.findall('[a-z]+',q.lower()))-stop
buckets=defaultdict(list)
for i,row in enumerate(items):
    for w in words(row[2]):buckets[w].append(i)
pairs=set()
for ids in buckets.values():
    if len(ids)>80:continue
    for i in ids:
        for j in ids:
            if i<j:pairs.add((i,j))
out=[]
for i,j in pairs:
    a,b=words(items[i][2]),words(items[j][2]);score=len(a&b)/len(a|b)
    if score>=.50:out.append((score,items[i],items[j]))
for s,a,b in sorted(out,reverse=True)[:35]:print(round(s,2),a[1],a[2],'<>',b[1],b[2])
print('proposals',len(items),'candidate pairs',len(out))
