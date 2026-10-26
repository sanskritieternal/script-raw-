import json,re
from pathlib import Path
p=Path('Scripts/expansion_368_550.json')
a=json.loads(p.read_text(encoding='utf-8'))
stop=set('a an the and or of in on for to with versus vs through by from as using under into one why how what which can do does different differences claims evidence requirements principles constraints limitations assumptions standards conditions forms effects'.split())
def tok(s):
    return {w.rstrip('s') for w in re.findall(r'[a-z0-9]+',s.lower()) if w not in stop and len(w)>2}
review=[];missing=[]; total=0
for nid,groups in a.items():
    bankp=next(Path('topics').glob(nid+'_*/IN_DEPTH_TOPIC_BANK.json'))
    b=json.loads(bankp.read_text(encoding='utf-8'))
    old=[t for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']]
    ts=[t for g in groups for t in g['topics']]
    gap=[]
    for o in old:
        title=o.get('title',o['question']); words=tok(title)
        candidates=[t for t in ts if words and words<=tok(t['question']+' '+t['coverage'])]
        if candidates:
            chosen=min(candidates,key=lambda t:len(tok(t['question']+' '+t['coverage'])-words))
            chosen.setdefault('covers_starter_ids',[]).append(o['id'])
            review.append(nid+'|'+o['id']+'|'+title+'|'+chosen['question'])
            total+=1
        else:
            gap.append(title)
            missing.append(nid+'|'+o['id']+'|'+title)
    a[nid]={'groups':groups,'open_coverage':[{'area':'Starter concepts requiring an individual coverage crosswalk','next_step':'Review dedicated proposal depth for: '+ '; '.join(gap)+'. Existing scopes may introduce related concepts; an explicit match is not yet certified.'}] if gap else [{'area':'Coverage beyond the imported starter map','next_step':'Add selected local cases, region/language variations and deeper methods after choosing a distinct audience question; no exhaustive coverage is claimed.'}]}
p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
Path('Scripts/topic_expansion_inputs/368_550_mapping_candidates.txt').write_text('\n'.join(review)+'\n',encoding='utf-8')
Path('Scripts/topic_expansion_inputs/368_550_mapping_open.txt').write_text('\n'.join(missing)+'\n',encoding='utf-8')
print('exact meaningful-token mapping candidates',total,'unmapped concepts',len(missing))
