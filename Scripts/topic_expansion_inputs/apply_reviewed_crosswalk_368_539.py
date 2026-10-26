import json
from pathlib import Path
p=Path('Scripts/expansion_368_550.json'); data=json.loads(p.read_text(encoding='utf-8'))
flat={}
for line in Path('Scripts/topic_expansion_inputs/368_550_authored.txt').read_text(encoding='utf-8-sig').splitlines():
    if line.strip():
        nid,title,level,q,scope=line.split('|');flat.setdefault(nid,[]).append(q)
fixes={
'411':{2:4},'419':{7:4},'460':{8:11},'465':{6:5},'467':{4:1},'468':{7:7},
'471':{9:5},'476':{8:10},'479':{1:10},'480':{9:6},'484':{1:10},'490':{1:2,2:2},'492':{7:10},'496':{1:10},'509':{6:2},'513':{3:2},'530':{6:1}}
review=[]
for line in Path('Scripts/topic_expansion_inputs/368_539_manual_crosswalk.txt').read_text(encoding='utf-8-sig').splitlines():
    nid,nums=line.split('|');indices=[int(x) for x in nums.split(',')]
    for oldindex,newindex in fixes.get(nid,{}).items():indices[oldindex-1]=newindex
    bank=json.loads(next(Path('topics').glob(nid+'_*/IN_DEPTH_TOPIC_BANK.json')).read_text(encoding='utf-8'))
    originals=[t for c in bank['prior_initial_map']['categories'] for t in c['topics']]
    assert len(indices)==len(originals),(nid,len(indices),len(originals))
    lookup={t['question']:t for g in data[nid]['groups'] for t in g['topics']}
    for old,newindex in zip(originals,indices):
        assert newindex>0
        target=lookup[flat[nid][newindex-1]]
        for t in lookup.values():
            if old['id'] in t.get('covers_starter_ids',[]):t['covers_starter_ids'].remove(old['id'])
        target.setdefault('covers_starter_ids',[]).append(old['id'])
        review.append({'niche_id':nid,'original_id':old['id'],'original_concept':old['title'],'active_question':target['question'],'active_scope':target['coverage'],'review':'subject scope reviewed; introductory or comparative treatment, not exhaustive depth'})
    # The prior queue tracked lexical matches, which this explicit editorial pass supersedes.
    data[nid]['open_coverage']=[]
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
Path('Scripts/topic_expansion_inputs/368_539_reviewed_crosswalk.json').write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Manually reviewed and assigned',len(review),'starter concepts across',len({r['niche_id'] for r in review}),'niches; old IDs/questions remain archived.')
