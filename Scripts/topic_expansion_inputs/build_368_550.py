import json
from pathlib import Path
from collections import defaultdict
p=Path('Scripts/topic_expansion_inputs/368_550_authored.txt')
out={}
for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
    if not line.strip(): continue
    parts=line.split('|')
    if len(parts)!=5: raise ValueError((n,line))
    nid,title,level,question,coverage=parts
    bank=out.setdefault(nid,[])
    group=next((g for g in bank if g['title']==title and g['level']==level),None)
    if group is None:
        group={'parent':{'foundation':'Foundations','intermediate':'Methods and applications','advanced':'Systems and interpretation'}[level],'title':title,'level':level,'topics':[]}
        bank.append(group)
    if not question.endswith('?'): raise ValueError((n,question))
    group['topics'].append({'question':question,'coverage':coverage})
assert set(out)=={str(i) for i in range(368,551)}
Path('Scripts/expansion_368_550.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('niches',len(out),'proposals',sum(len(g['topics']) for b in out.values() for g in b))
