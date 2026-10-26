"""Save editorial baselines and lexical candidates for human/agent scope review.

Similarity is a triage aid, never an automatic duplicate verdict.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[4]
DEST = ROOT / 'Scripts/editorial_review_inputs'
STOP = set('the a an and or for with from into through within about does do how why what when where which can could would should is are was were be been being of to in on at by as than that this these those it its their they you your one two same different compare distinguish separate explain examine identify use using chosen named selected specific case study versus without rather between across change changes affect affects make makes mean means tell us question evidence source sources claims claim'.split())


def save(name, data):
    DEST.mkdir(exist_ok=True)
    (DEST/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def records():
    result=[]
    for p in sorted((ROOT/'topics').glob('*/IN_DEPTH_TOPIC_BANK.json')):
        bank=json.loads(p.read_text(encoding='utf-8'))
        nid=bank['niche_id']
        for cat in bank['categories']:
            for topic in cat['topics']:
                result.append({'niche_id':nid, 'niche':bank.get('name',bank.get('title',p.parent.name)),
                    'id':topic['id'],'subcategory':cat['title'],'question':topic['question'],
                    'coverage':topic['coverage'], 'additional_scope':topic.get('additional_scope','')})
    return result


def tokens(text):
    return [t for t in re.findall(r'\w+',unicodedata.normalize('NFKC',text).casefold()) if len(t)>2 and t not in STOP and not t.isdigit()]


def snapshot():
    files={}
    for p in (ROOT/'topics').glob('*/IN_DEPTH_TOPIC_BANK.json'):
        b=json.loads(p.read_text(encoding='utf-8'))
        files[b['niche_id']]={'path':p.relative_to(ROOT).as_posix(), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'topics':[{**t,'category_id':c['id']} for c in b['categories'] for t in c['topics']],
            'open_coverage':b.get('open_coverage',[]), 'starter_concept_crosswalk':b.get('starter_concept_crosswalk',{})}
    save('before_editorial_pass.json',{'date':'2026-10-23','banks':files})
    print(f'Saved {len(files)} banks and {sum(len(b["topics"]) for b in files.values())} active records.')


def candidates(question_only=False,tag=''):
    rows=records(); n=len(rows)
    bags=[Counter(tokens(r['question']) if question_only else tokens(r['question'])*2+tokens(r['coverage'])) for r in rows]
    df=Counter(t for bag in bags for t in bag)
    vectors=[]; postings=defaultdict(list)
    for i,bag in enumerate(bags):
        vec={t:(1+math.log(v))*math.log((n+1)/(df[t]+1)) for t,v in bag.items() if df[t]<n*.035}
        length=math.sqrt(sum(v*v for v in vec.values())) or 1
        vec={t:v/length for t,v in vec.items()}
        vectors.append(vec)
        for t,v in vec.items():postings[t].append((i,v))
    pairs={}
    for i,vec in enumerate(vectors):
        scores=defaultdict(float)
        for token,weight in vec.items():
            for j,v in postings[token]:
                if j>i:scores[j]+=weight*v
        ranked=sorted(((score,j) for j,score in scores.items() if score>=(.48 if question_only else .43)),reverse=True)
        for score,j in ranked[:(4 if question_only else 6)]:
            pairs[(i,j)]={'score':round(score,4),'left':rows[i],'right':rows[j]}
    values=sorted(pairs.values(),key=lambda p:p['score'],reverse=True)
    prefix='semantic_question_candidates_' if question_only else 'semantic_candidates_'
    if tag:prefix=tag+'_'+prefix
    save(prefix+'all.json',{'method':'TF-IDF lexical question similarity; needs scope review.' if question_only else 'TF-IDF lexical similarity of question and individual scope; requires editorial decision; not semantic proof.', 'records':n,'pairs':values})
    for label,start,end in [('002_184',2,184),('185_367',185,367),('368_550',368,550),('root',1,1)]:
        owned=lambda nid: start<=int(nid)<=end and not (label=='185_367' and nid=='281')
        selected=[p for p in values if owned(p['left']['niche_id']) or owned(p['right']['niche_id']) or (label=='root' and '281' in (p['left']['niche_id'],p['right']['niche_id']))]
        save(prefix+label+'.json',{'pairs':selected,'note':'Review actual question and scope; high lexical similarity is often a useful comparison, not a duplicate.'})
    print(f'{n} records; {len(values)} candidate pairs; {sum(p["score"]>=.65 for p in values)} score >= .65.')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['snapshot','candidates','question-candidates']);ap.add_argument('--tag',default='');args=ap.parse_args()
    if args.command=='snapshot':snapshot()
    else:candidates(question_only=args.command=='question-candidates',tag=args.tag)
