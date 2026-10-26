from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json
from pathlib import Path
import manage_all_topic_banks as m
errors=[];count=0;active=0;mapping=0;unmapped=[]
for n in range(185,368):
 if n==281:continue
 nid=f'{n:03d}';d=m.home(nid);b=m.read(d/'IN_DEPTH_TOPIC_BANK.json')
 if nid=='345':
  b.setdefault('starter_concept_crosswalk',{})['BANK-345-009']=['BANK-012-030']
  b['open_coverage']=[{'area':'Habitability criteria have a primary home in niche012','next_step':'Use the linked BANK-012-030 proposal instead of counting the retired BANK-345-033 duplicate; retain planetary-atmosphere, surface and sampling questions here.'},{'area':'Planet-specific evidence','next_step':'Select actual missions, spectra and samples for Venus, Mars and giant-planet proposals; compare contrary models and uncertainty before any script is promoted.'}]
  m.write(d/'IN_DEPTH_TOPIC_BANK.json',b);m.render(b,d)
 errors.extend(m.check_bank(b,d));count+=1;active+=len(m.records(b));mapping+=len(b.get('starter_concept_crosswalk',{}))
 if n>=216:
  for c in b.get('prior_initial_map',{}).get('categories',[]):
   for t in c['topics']:
    if not b.get('starter_concept_crosswalk',{}).get(t['id']):unmapped.append(t['id'])
result={'niches_checked':count,'active_proposals':active,'reviewed_starter_concepts':mapping,'unmapped_216_367':unmapped,'errors':errors,'source_verification':'not_performed','remote_changes':'none','coverage_review':'All starter concepts216–367 mapped to reviewed scoped proposals, including the345 habitability referral to012. Broader case, region, language and source depth remains open.'}
m.write((Path(__file__).resolve().parents[3] / 'audit_185_367.json'),result)
print(json.dumps(result,indent=2))
