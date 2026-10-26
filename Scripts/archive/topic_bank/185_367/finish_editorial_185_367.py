from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json,sys
from pathlib import Path
import manage_all_topic_banks as m

def dump(start,end):
 for n in range(start,end+1):
  if n==281:continue
  b=m.read(m.home(f'{n:03d}')/'IN_DEPTH_TOPIC_BANK.json')
  print('\n@'+b['niche_id']+' '+b['name'])
  print('GAPS',json.dumps(b.get('open_coverage',[]),ensure_ascii=False))
  old={t['id']:t for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']}
  active={t['id']:t for _,t in m.records(b)}
  print('MAPS', '; '.join(k+' '+v.get('title',v['question'])+' -> '+','.join(b.get('starter_concept_crosswalk',{}).get(k,[])) for k,v in old.items()))
  for c,t in m.records(b):
   print(t['id'].split('-')[-1],t['question'],'[',t['coverage'],']')

if __name__=='__main__':dump(int(sys.argv[1]),int(sys.argv[2]))
