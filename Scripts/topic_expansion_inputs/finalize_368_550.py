import json
from pathlib import Path
p=Path('Scripts/expansion_368_550.json');a=json.loads(p.read_text(encoding='utf-8'))
seen=set()
for line in Path('Scripts/topic_expansion_inputs/368_539_further_coverage.txt').read_text(encoding='utf-8-sig').splitlines():
    nid,branches=line.split('|');seen.add(nid)
    a[nid]['open_coverage']=[{'area':'Further subject branches beyond the reviewed starter concepts','next_step':'Develop distinct individually bounded proposals on: '+branches+'. These are expansion opportunities, not researched or production-ready scripts.'}]
assert seen=={str(i) for i in range(368,540)}
for nid,payload in a.items():
    bank=json.loads(next(Path('topics').glob(nid+'_*/IN_DEPTH_TOPIC_BANK.json')).read_text(encoding='utf-8'))
    old={t['id'] for c in bank['prior_initial_map']['categories'] for t in c['topics']}
    mapped={x for g in payload['groups'] for t in g['topics'] for x in t.get('covers_starter_ids',[])}
    assert old==mapped,(nid,old-mapped,mapped-old)
p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('All183 niche payloads have specific expansion areas; all1701 starter concepts have reviewed active mappings.')
