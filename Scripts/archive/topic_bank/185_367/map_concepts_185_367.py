import json
from pathlib import Path
root=Path(__file__).resolve().parents[4]
p=root/'Scripts/expansion_185_367.json';r=json.loads(p.read_text(encoding='utf-8'))
reviewed={}
for line in (root/'Scripts/reviewed_concepts_185_367.txt').read_text(encoding='utf-8-sig').splitlines():
 if not line or line.startswith('#'):continue
 nid,indices=line.split(':');reviewed[nid]=indices.split(',')
for nid,ids in reviewed.items():
 d=next((root/'topics').glob(nid+'_*'));b=json.loads((d/'IN_DEPTH_TOPIC_BANK.json').read_text(encoding='utf-8'))
 old={t['id']:t for c in b['prior_initial_map']['categories'] for t in c['topics']}
 for index in ids:
  oid=f'BANK-{nid}-{index}';phrase=old[oid].get('title',old[oid]['question']).lower()
  matches=[t for g in r[nid] for t in g['topics'] if phrase in (g['title']+' '+t['question']+' '+t['coverage']).lower()]
  assert len(matches)==1,(oid,matches)
  matches[0].setdefault('covers_starter_ids',[]).append(oid)
# Explicit reviewed mappings may override the earlier broad candidate.
errors=[]
for line in (root/'Scripts/manual_concepts_185_367.txt').read_text(encoding='utf-8-sig').splitlines():
 if not line:continue
 nid,ind,fragment=line.split('|');oid=f'BANK-{nid}-{ind}'
 for g in r[nid]:
  for t in g['topics']:
   t['covers_starter_ids']=[x for x in t.get('covers_starter_ids',[]) if x!=oid]
 matches=[t for g in r[nid] for t in g['topics'] if fragment.lower() in t['question'].lower()]
 if len(matches)!=1:errors.append((oid,fragment,len(matches)));continue
 matches[0].setdefault('covers_starter_ids',[]).append(oid)
if errors:print(errors);raise SystemExit(1)
for nid,gs in r.items():
 for g in gs:
  for t in g['topics']:
   if t.get('covers_starter_ids'):t['covers_starter_ids']=sorted(set(t['covers_starter_ids']))
   else:t.pop('covers_starter_ids',None)
p.write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Reviewed concept mappings',sum(len(t.get('covers_starter_ids',[])) for gs in r.values() for g in gs for t in g['topics']))

