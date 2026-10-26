import json,hashlib
from pathlib import Path
snapshot={}
for p in sorted(Path('topics').glob('*/IN_DEPTH_TOPIC_BANK.json')):
    nid=int(p.parent.name[:3])
    if 368<=nid<=550:
        b=json.loads(p.read_text(encoding='utf-8'));snapshot[b['niche_id']]={'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'active':[{'subcategory':c['title'],'level':c['level'],**t} for c in b['categories'] for t in c['topics']],'starter_concepts':[t for c in b['prior_initial_map']['categories'] for t in c['topics']],'starter_concept_crosswalk':b.get('starter_concept_crosswalk',{}),'open_coverage':b.get('open_coverage',[])}
Path('Scripts/editorial_read_368_550.json').write_text(json.dumps(snapshot,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Read/saved',len(snapshot),'banks;',sum(len(x['active']) for x in snapshot.values()),'active question/scope records;',sum(len(x['starter_concepts']) for x in snapshot.values()),'starter concepts.')
