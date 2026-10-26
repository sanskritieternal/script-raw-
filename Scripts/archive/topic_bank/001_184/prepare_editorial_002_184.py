import json,pathlib,re,math,collections
from itertools import combinations
STOP=set('a an the and or of to in for on with without from by as at is are be can could do does did how why what which when who whose should would will this that these those it its their they them one two same different compare comparing distinguish separate trace explain named selected specific chosen actual evidence source sources question questions scope example examples case cases rather than not avoid through before after within between use using include including into beyond based identify identified context'.split())
def toks(s):
 return {w.rstrip('s') for w in re.findall(r'[a-z]{3,}',s.lower()) if w not in STOP}
def candidates(b):
 ts=[t for c in b['categories'] for t in c['topics']];sets={t['id']:toks(t['question']+' '+t['coverage']) for t in ts};freq=collections.Counter(w for s in sets.values() for w in s);idf={w:math.log((len(ts)+1)/(n+1))+1 for w,n in freq.items()}
 def score(a,z):
  aa,zz=sets[a['id']],sets[z['id']];shared=aa&zz
  return sum(idf[w]**2 for w in shared)/math.sqrt(sum(idf[w]**2 for w in aa)*sum(idf[w]**2 for w in zz))
 old=set(b['local_reconciliation']['source_records']);pairs=[]
 for a,z in combinations(ts,2):
  if a['id'] in old and z['id'] in old:continue
  value=score(a,z)
  if value>.27:pairs.append({'score':round(value,3),'a':a,'b':z})
 return sorted(pairs,key=lambda p:-p['score'])[:6]
report={}
for n in range(2,185):
 p=next(pathlib.Path('topics').glob(f'{n:03d}*/IN_DEPTH_TOPIC_BANK.json'));b=json.loads(p.read_text(encoding='utf-8'))
 report[f'{n:03d}']={'name':b['name'],'current_gap_notes':b.get('open_coverage',[]),'semantic_candidates':candidates(b)}
pathlib.Path('Scripts/editorial_candidates_002_184.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared per-bank question+scope lexical candidates for183 banks; candidates require semantic judgment, not automatic retirement.')
