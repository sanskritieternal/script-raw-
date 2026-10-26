import json,sys
from pathlib import Path
sys.path.insert(0,str(Path('Scripts').resolve()))
import manage_all_topic_banks as m
errors=[];summary=[]
for p in sorted(Path('topics').glob('*/IN_DEPTH_TOPIC_BANK.json')):
    nid=int(p.parent.name[:3])
    if 368<=nid<=550:
        b=m.read(p);errors.extend(m.check_bank(b,p.parent))
        count=sum(len(c['topics']) for c in b['categories'])
        starters=sum(len(c['topics']) for c in b.get('prior_initial_map',{}).get('categories',[]))
        mapped=len(b.get('starter_concept_crosswalk',{}))
        summary.append({'niche_id':b['niche_id'],'active_proposals':count,'starter_concepts':starters,'mapped_starter_concepts':mapped,'open_starter_mappings':starters-mapped})
report={'range':'368–550','niches':len(summary),'active_proposals':sum(x['active_proposals'] for x in summary),'mapped_starter_concepts':sum(x['mapped_starter_concepts'] for x in summary),'starter_concepts':sum(x['starter_concepts'] for x in summary),'errors':errors,'coverage_exhaustive':False,'source_verification':'not_performed','banks':summary}
Path('Scripts/topic_expansion_inputs/368_550_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='banks'},indent=2,ensure_ascii=False))
