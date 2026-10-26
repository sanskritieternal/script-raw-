import json
from pathlib import Path
p=Path('topics')
for d in sorted(p.iterdir()):
 if d.is_dir() and 185<=int(d.name[:3])<=190:
  b=json.loads((d/'IN_DEPTH_TOPIC_BANK.json').read_text(encoding='utf-8'))
  print('\n'+d.name)
  print('GAPS',json.dumps(b.get('open_coverage',[]),ensure_ascii=False))
  print('STARTERS',[(t['id'],t.get('title',t['question'])) for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']])
  for c in b['categories']:
   for t in c['topics']:print(t['id'],t['question'],'SCOPE:',t['coverage'])
