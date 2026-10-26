from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json
from pathlib import Path
import manage_all_topic_banks as m
# Each row is a reviewed ordered starter001–012 target. '+' combines actual complementary scopes; '-' is a newly authored covers_starter_ids mapping.
rows='''
051 - 33+34 15 27+46 20 - - 25 29+32 - 35 37
052 21 26+27 - 31 17 17 - 25 37+48 28 29+35 47
053 17 - 25+27 - - - - 29 13 21+39 14 44
054 14 17 25 34 21 37 22 42 29 30 31 36
055 17 16 21+23 - 41 24+34 33 19 39 38 20+33 28
056 22 23 - - - 30 - - 27 - 14+40 14+45
057 17 22 23 18 15 16 21 - - 34+38 33 44
058 BANK-059-019 19 - - 45 - 27 33+36 13 28+42 17 21
059 20 18 21+22+23 - - 25 - - 41 47 14+31 16
060 17 - - 30 29 - - 47 35 41 36+39 16+44
061 14 17+49 21+22 23 13 56 27 20+28 35 - 36+37 45
062 - - 18+19 21 26 27 - 13+30 17 38 25 40
063 - 15 22 - 32 33 28 21 25 13 29 41
064 45 25 26 16 31 44 - - 32 14+33 33 40+42
065 13+40 17+18 36 19 21 14 20 31 43 33 42+45 16
066 21 28 - - - - 17 36 16 37 35 39
067 - 20 18 23 - - 26 28 33 34 32 35
068 29 27 38 25 26+28 - 15 17+18 14 - 33 34+36
069 17 30 19 20+29 34 37 42 40 51 32 - -
070 17+23 14 18 25+27 38 19 20 - 29 39 - -
071 17 - 22 38+39 34 30 16 29 42+47 42 38 -
072 16 - 20 25+47 38 24 31+35 28 22 36 13+14+39 40
073 14+23 21 26 - 40 41 49 - 45 46 15 44
074 14 20 16 19 22 25 43 42 28 31 - 38
075 - 31 - 16 - 36+52 - 38 15 - 50 14+41
076 23+24 18+19 - - 40 - - - - BANK-075-014 37 39
077 31 17 36 30 24 18 44 20 14 13 13 13
078 29+30 - 36 - 14 49 16 38 46+50 42 - -
079 13 13+40 46 40 - 30 - - 37 - 40 39+43
080 - 16 20 - 31 - 33 13+26 - 38+48 45 37
'''
missing=[];report={}
baseline=m.read(Path('Scripts/editorial_review_inputs/before_editorial_pass.json'))['banks']
alltopics={t['id']:t for q in Path('topics').glob('*/IN_DEPTH_TOPIC_BANK.json') for bank in [m.read(q)] for c in bank['categories'] for t in c['topics']}
for line in rows.strip().splitlines():
 parts=line.split();nid=parts[0];assert len(parts)==13,(nid,len(parts));p=next(Path('topics').glob(nid+'*/IN_DEPTH_TOPIC_BANK.json'));b=m.read(p)
 for i,target in enumerate(parts[1:],1):
  sid=f'BANK-{nid}-{i:03d}'
  if target!='-':b.setdefault('starter_concept_crosswalk',{})[sid]=[s if s.startswith('BANK-') else f'BANK-{nid}-{int(s):03d}' for s in target.split('+')]
  if sid not in b.get('starter_concept_crosswalk',{}):missing.append(sid)
 m.write(p,b);m.render(b,p.parent)
 oldids={t['id'] for t in baseline[nid]['topics']}
 report[nid]={'reviewed_before_ids':[t['id'] for t in baseline[nid]['topics']],
 'starter_decisions':[{'starter_id':t['id'],'starter_title':t['title'],'target_ids':b['starter_concept_crosswalk'][t['id']],
 'scope_evidence':[alltopics[x]['coverage']+((' Additional scope: '+alltopics[x]['additional_scope']) if alltopics[x].get('additional_scope') else '') for x in b['starter_concept_crosswalk'][t['id']]],
 'decision':'mapped to individually bounded current scope after rejecting weak lexical matches'} for c in b['prior_initial_map']['categories'] for t in c['topics']],
 'new_proposals':[{'id':t['id'],'question':t['question'],'coverage':t['coverage']} for c in b['categories'] for t in c['topics'] if t['id'] not in oldids]}
m.write(Path('Scripts/editorial_starters_051_080.json'),{'banks':report,'validation':{'banks':30,'starters':sum(len(x['starter_decisions']) for x in report.values()),'errors':missing,'verified_sources':'not_performed'}});print('Missing starter IDs',missing)
