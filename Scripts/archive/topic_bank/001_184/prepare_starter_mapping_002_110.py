import json,re,math,collections
from pathlib import Path
STOP=set('the a an and or of to in for on with without from by as at is are be can could do does did how why what which when who whose should would will this that these those it its their they them one two same different compare comparing distinguish separate trace explain named selected specific chosen actual evidence source sources question questions scope example examples case cases rather than not avoid through before after within between use using include including into beyond based identify identified context'.split())
def tok(s):return {w.rstrip('s') for w in re.findall(r'[a-z]{3,}',s.lower()) if w not in STOP}
out={}
for n in range(2,111):
 p=next(Path('topics').glob(f'{n:03d}*/IN_DEPTH_TOPIC_BANK.json'));b=json.loads(p.read_text(encoding='utf-8'));ts=[t for c in b['categories'] for t in c['topics']];df=collections.Counter(w for t in ts for w in tok(t['question']+' '+t['coverage']))
 rows=[]
 for c in b['prior_initial_map']['categories']:
  for t in c['topics']:
   words=tok(t['title']); score=lambda z:sum(1+math.log((len(ts)+1)/(df[w]+1)) for w in words&tok(z['question']+' '+z['coverage']))/max(len(words),1)
   best=sorted(ts,key=score,reverse=True)[:3]
   rows.append({'starter_id':t['id'],'title':t['title'],'candidates':[{'id':z['id'],'score':round(score(z),2),'question':z['question'],'coverage':z['coverage']} for z in best]})
 out[f'{n:03d}']={'name':b['name'],'starters':rows}
Path('Scripts/editorial_review_inputs/starter_candidates_002_110.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
