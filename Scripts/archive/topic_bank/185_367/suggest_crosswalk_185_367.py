import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[4]
r=json.loads((root/'Scripts/expansion_185_367.json').read_text(encoding='utf-8-sig'))
for nid,gs in r.items():
 d=next((root/'topics').glob(nid+'_*'));b=json.loads((d/'IN_DEPTH_TOPIC_BANK.json').read_text(encoding='utf-8-sig'))
 old=b.get('prior_initial_map',{})
 for c in old.get('categories',[]):
  for t in c['topics']:
   title=t.get('title',t['question']);phrase=title.lower()
   matches=[x for g in gs for x in g['topics'] if phrase in (g['title']+' '+x['question']+' '+x['coverage']).lower()]
   if len(matches)==1:print(nid,t['id'],title,'=>',matches[0]['question'])

