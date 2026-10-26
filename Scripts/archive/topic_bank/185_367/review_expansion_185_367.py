from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

from pathlib import Path
import json
import manage_all_topic_banks as shared
p=(Path(__file__).resolve().parents[3] / 'expansion_185_367.txt')
lines=p.read_text(encoding='utf-8-sig').splitlines()
p.write_text('\n'.join(x for x in lines if '|Why is a planet in a habitable zone not necessarily habitable?|' not in x)+'\n',encoding='utf-8')
d=shared.home('345');b=shared.read(d/'IN_DEPTH_TOPIC_BANK.json')
for c in b['categories']:
 for t in list(c['topics']):
  if t['id']=='BANK-345-033':
   c['topics'].remove(t);t['duplicate_of']='BANK-012-030';b.setdefault('retired_duplicate_proposals',[]).append(t)
b['categories']=[c for c in b['categories'] if c['topics']]
b.setdefault('duplicate_referrals',[]).append({'topic_id':'BANK-345-033','primary_topic_id':'BANK-012-030','primary_directory':'012_space_universe','reason':'Same question and scope; keep one primary home.'})
b['counts']={'categories':len(b['categories']),'proposed_topics':len(shared.records(b))}
shared.write(d/'IN_DEPTH_TOPIC_BANK.json',b);shared.render(b,d)
