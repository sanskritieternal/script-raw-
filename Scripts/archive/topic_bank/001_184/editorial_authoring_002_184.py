import json
from pathlib import Path

def parse(data):
 banks={};nid=None;group=None
 for line in data.strip().splitlines():
  line=line.strip()
  if not line:continue
  if line.startswith('['):nid=line[1:-1];banks[nid]={'groups':[]};continue
  if line.startswith('@'):
   parent,title,level=line[1:].split('|');group={'parent':parent,'title':title,'level':level,'topics':[]};banks[nid]['groups'].append(group);continue
  p=line.split('|');assert len(p) in (2,3),line
  t={'question':p[0],'coverage':p[1]}
  if len(p)==3:t['covers_starter_ids']=[f'BANK-{nid}-{int(i):03d}' for i in p[2].split(',')]
  group['topics'].append(t)
 return banks

def append(data):
 path=Path('Scripts/editorial_pass_002_184.json');banks=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {};banks.update(parse(data));path.write_text(json.dumps(banks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Saved',len(banks),'second-pass authored bank payloads')
if __name__=='__main__':raise SystemExit('Import append() from owned batch authoring scripts.')
