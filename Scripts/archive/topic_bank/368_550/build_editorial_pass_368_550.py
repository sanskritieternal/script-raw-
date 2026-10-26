"""Recover saved authorship, append explicit scope repairs, and build repeatable input."""
import json
from pathlib import Path
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[4]
READ=json.loads((ROOT/'Scripts/editorial_read_368_550.json').read_text(encoding='utf-8'))
groups=defaultdict(list)
repairs={}
for name in ['editorial_authored_368_550.txt','editorial_finish_519_550.txt','editorial_mapping_repairs_368_550.txt','editorial_mapping_repairs_more_368_550.txt']:
    for line in (ROOT/'Scripts'/name).read_text(encoding='utf-8-sig').splitlines():
        if not line.strip():continue
        fields=line.split('|')
        assert len(fields) in (6,7),(name,line)
        nid,title,parent,level,question,coverage=fields[:6]
        proposal={'question':question,'coverage':coverage}
        if len(fields)==7:
            starter=next(t for t in READ[nid]['starter_concepts'] if t['title']==fields[6])
            proposal['covers_starter_ids']=[starter['id']]
            repairs[starter['id']]=question
        groups[nid].append({'parent':parent,'title':title,'level':level,'topics':[proposal]})

# These previously authored questions directly repair misleading starter referrals.
for nid,title,question in [
 ('375','Avoiding mental-illness villain stereotypes','How can horror depict unreliable perception without making mental illness the explanation for evil?'),
]:
    starter=next(t for t in READ[nid]['starter_concepts'] if t['title']==title)
    topic=next(t for g in groups[nid] for t in g['topics'] if t['question']==question)
    topic['covers_starter_ids']=[starter['id']];repairs[starter['id']]=question

payload={}
for nid,gs in sorted(groups.items()):
    branches=list(dict.fromkeys(g['title'] for g in gs))
    # These are concrete later editorial decisions, not invented uncovered subject labels.
    remaining=[{'area':'Concrete case selection for '+title,
                'next_step':next(g['topics'][0]['coverage'] for g in gs if g['title']==title)+' Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.'}
               for title in branches]
    payload[nid]={'groups':gs,'open_coverage':remaining}

assert set(payload)=={f'{i:03d}' for i in range(368,551)}
(ROOT/'Scripts/editorial_pass_368_550.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'Scripts/editorial_mapping_repairs_368_550.json').write_text(json.dumps(repairs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(payload),'banks;',sum(len(g['topics']) for p in payload.values() for g in p['groups']),'authored proposals;',len(repairs),'explicit mapping repairs')
