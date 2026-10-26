from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Display actual starter headings alongside ranked active scope candidates for review."""
import argparse
from collections import Counter
import math
import re
import manage_all_topic_banks as m
from editorial_review_tools import tokens


def show(start,end):
    for n in range(start,end+1):
        nid=f'{n:03d}';b=m.read(m.home(nid)/'IN_DEPTH_TOPIC_BANK.json');rs=m.records(b)
        starters=[t for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']]
        bags=[set(tokens(t['question']+' '+t['coverage'])) for c,t in rs]
        df=Counter(w for bag in bags for w in bag)
        print('\n###',nid,b['name'])
        for old in starters:
            title=old.get('title',old['question']);terms=set(tokens(title))
            ranked=sorted(((sum(math.log((len(rs)+1)/(df[w]+.5)) for w in terms&bag),i) for i,bag in enumerate(bags)),reverse=True)
            best=[rs[i][1] for score,i in ranked[:2]]
            print(old['id'].split('-')[-1],title)
            for t in best:print(' ->',t['id'].split('-')[-1],t['question'],'|',t['coverage'])


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('start',type=int);ap.add_argument('end',type=int);ap.add_argument('--prepared',action='store_true');ap.add_argument('--questions',action='store_true');ap.add_argument('--filter',default='');ap.add_argument('--ordinal-start',type=int,default=1);args=ap.parse_args()
    if args.questions:
        for n in range(args.start,args.end+1):
            b=m.read(m.home(f'{n:03d}')/'IN_DEPTH_TOPIC_BANK.json');print('\n###',n,b['name'])
            for c,t in m.records(b):
                if not args.filter or re.search(args.filter,t['question']+' '+t['coverage'],re.I):print(t['id'].split('-')[-1],t['question'],'|',t['coverage'])
    elif args.prepared:
        prepared=m.read(m.ROOT/'Scripts/editorial_review_inputs/starter_candidates_002_110.json')
        for n in range(args.start,args.end+1):
            b=prepared[f'{n:03d}'];print('\n###',n,b['name'])
            for s in b['starters'][args.ordinal_start-1:]:
                print(s['starter_id'].split('-')[-1],s['title'])
                for c in s['candidates'][:2]:print(' ->',c['id'].split('-')[-1],c['question'],'|',c['coverage'])
    else:show(args.start,args.end)
