from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Apply reviewed duplicate decisions while retaining full records and reserved IDs.

Run only after all range owners declare SAFE. Input: list of
{retire_id, primary_id, reason}; no similarity score can trigger retirement.
"""
import argparse
import copy
from pathlib import Path
import manage_all_topic_banks as m

ROOT=Path(__file__).resolve().parents[4]


def consolidate(input_path):
    decisions=m.read(input_path)
    if isinstance(decisions,dict):decisions=decisions['decisions']
    banks={nid:m.read(m.home(nid)/'IN_DEPTH_TOPIC_BANK.json') for nid in m.rows()}
    active={t['id']:(nid,c,t) for nid,b in banks.items() for c,t in m.records(b)}
    retired={t['id']:t for b in banks.values() for t in b.get('retired_duplicate_proposals',[])}
    aliases={tid:t['duplicate_of'] for tid,t in retired.items()}
    for decision in decisions:
        tid,primary=decision['retire_id'],decision['primary_id']
        assert tid!=primary and tid in active|retired,decision
        assert decision['reason'].strip(),decision
        aliases[tid]=primary
    def primary(tid):
        seen=set()
        while tid in aliases:
            assert tid not in seen,('alias cycle',tid)
            seen.add(tid);tid=aliases[tid]
        assert tid in active,('missing active primary',tid)
        return tid
    for tid in aliases:primary(tid)
    changed=set();applied=[]
    for decision in decisions:
        tid=decision['retire_id'];target=primary(tid)
        if tid in retired:continue
        nid,c,t=active[tid]
        assert nid!='001','001 retirements need its dedicated legacy crosswalk handling'
        saved=copy.deepcopy(t)
        saved.update(duplicate_of=target, retirement_reason=decision['reason'],
                     editorial_retirement_pass='second_scope_review_2026_10_23',original_subcategory_id=c['id'])
        banks[nid].setdefault('retired_duplicate_proposals',[]).append(saved)
        c['topics'].remove(t);changed.add(nid)
        applied.append({'retired_id':tid,'primary_id':target,'reason':decision['reason'],
                        'original_fields_sha256':m.fingerprint(t)})
    for nid,b in banks.items():
        old=m.fingerprint(b)
        for t in b.get('retired_duplicate_proposals',[]):t['duplicate_of']=primary(t['id'])
        for r in b.get('duplicate_referrals',[]):
            r['primary_topic_id']=primary(r['primary_topic_id']);r['primary_directory']=m.home(r['primary_topic_id'].split('-')[1]).name
        for old_id,refs in b.get('starter_concept_crosswalk',{}).items():
            b['starter_concept_crosswalk'][old_id]=list(dict.fromkeys(primary(tid) for tid in refs))
        for review in b.get('legacy_topic_crosswalk',{}).values():
            review['bank_ids']=list(dict.fromkeys(primary(tid) for tid in review.get('bank_ids',[])))
        if 'editorial_cross_references' in b:
            b['editorial_cross_references']=[dict(ref,related_id=primary(ref['related_id'])) for ref in b['editorial_cross_references']
                if ref['topic_id'] not in aliases and ref['topic_id']!=primary(ref['related_id'])]
        b['counts']={'categories':len(b['categories']),'proposed_topics':len(m.records(b))}
        # Preserve metadata for source subcategories, including any now-empty one.
        if m.fingerprint(b)!=old:changed.add(nid)
    # Write all changed JSON first, so cross-bank validation sees a consistent graph.
    for nid in changed:
        if nid=='001':
            # No active001 retirement; only optional cross-reference canonicalization.
            import manage_ai_topics as ai
            m.write(ai.HOME/'IN_DEPTH_TOPIC_BANK.json',banks[nid])
        else:m.write(m.home(nid)/'IN_DEPTH_TOPIC_BANK.json',banks[nid])
    for nid in changed:
        if nid=='001':
            import manage_ai_topics as ai
            b=banks[nid];status=ai.load(ai.HOME/'topics_status.json')
            for p,content in ai.reading_views(b,status).items():m.save_bytes(p,content.encode('utf-8'))
        else:
            errors=m.check_bank(banks[nid],m.home(nid));assert not errors,errors
            m.render(banks[nid],m.home(nid))
    report_path=ROOT/'Scripts/editorial_duplicate_consolidation.json'
    earlier=m.read(report_path) if report_path.exists() else {'decisions':[],'applied':[],'changed_niches':[]}
    combined_decisions={d['retire_id']:d for d in earlier['decisions']}
    combined_decisions.update({d['retire_id']:d for d in decisions})
    combined_applied={d['retired_id']:d for d in earlier['applied']}
    combined_applied.update({d['retired_id']:d for d in applied})
    m.write(report_path,{'decisions':list(combined_decisions.values()),'applied':list(combined_applied.values()),
         'changed_niches':sorted(set(earlier['changed_niches'])|changed),
         'preservation':'Full original records and IDs retained; active counts exclude retired overlaps.'})
    print(f'Applied {len(applied)} explicit retirements; refreshed {len(changed)} banks.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path,required=True)
    consolidate(parser.parse_args().input)
