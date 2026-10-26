"""Audit review coverage and preservation against the saved editorial-pass baseline.

This validates recorded evidence and references, not the truth or completeness of
editorial judgments. Never converts a similarity score into a duplicate verdict.
"""
from collections import Counter
from pathlib import Path
import re
import manage_all_topic_banks as m

ROOT=Path(__file__).resolve().parents[1]
AUDITS=['Scripts/editorial_review_root.json','Scripts/editorial_review_002_184.json',
        'Scripts/editorial_review_185_367.json','Scripts/editorial_review_368_550.json']


def main():
    baseline=m.read(ROOT/'Scripts/editorial_review_inputs/before_editorial_pass.json')['banks']
    audit_entries={};errors=[]
    for name in AUDITS:
        p=ROOT/name
        if not p.exists():errors.append('Missing audit: '+name);continue
        a=m.read(p);banks=a.get('banks',{})
        if isinstance(banks,list):banks={b['niche_id']:b for b in banks}
        for nid,entry in banks.items():
            nid=str(nid).zfill(3)
            if nid in audit_entries:errors.append('Duplicate audit owner '+nid)
            audit_entries[nid]={'file':name,'entry':entry}
    changes=[];totals=Counter();target_id_cache={}
    for nid,old in baseline.items():
        b=m.read(m.home(nid)/'IN_DEPTH_TOPIC_BANK.json')
        now={t['id']:t for c,t in m.records(b)}
        retired={t['id']:t for t in b.get('retired_duplicate_proposals',[])}
        original={t['id']:t for t in old['topics']}
        for tid,t in original.items():
            actual=now.get(tid,retired.get(tid))
            if actual is None:errors.append(f'{nid}: lost original active ID {tid}');continue
            for key in ('question','coverage'):
                if t[key]!=actual[key]:errors.append(f'{nid}: original {key} rewritten {tid}')
        entry=audit_entries.get(nid)
        if not entry:errors.append('No per-bank editorial audit '+nid)
        elif not entry['entry']:errors.append('Empty per-bank audit '+nid)
        else:
            e=entry['entry']
            read_ids=e.get('reviewed_before_ids',e.get('reviewed_ids',e.get('active_ids_reviewed')))
            if read_ids is not None and set(read_ids)!=set(original):
                errors.append(f'{nid}: recorded before-review IDs do not match saved baseline')
        additions=[tid for tid in now if tid not in original]
        removed=[tid for tid in original if tid not in now]
        totals['active_before']+=len(original);totals['active_after']+=len(now)
        totals['new_active']+=len(additions);totals['retired_previous']+=len(removed)
        starters=[t for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']]
        missing=[t['id'] for t in starters if not b.get('starter_concept_crosswalk',{}).get(t['id'])]
        if missing:errors.append(f'{nid}: {len(missing)} archived starter subjects have no explicit active coverage route')
        if entry:
            decisions=entry['entry'].get('starter_decisions',[])
            by_starter={d.get('starter_id'):d for d in decisions}
            if len(decisions)!=len(by_starter) or set(by_starter)!={t['id'] for t in starters}:
                errors.append(f'{nid}: starter review inventory does not match archived starter IDs')
            for old in starters:
                decision=by_starter.get(old['id'])
                if not decision:continue
                targets=decision.get('target_ids',[])
                evidence=(decision.get('scope_evidence') or decision.get('coverage_evidence')
                          or decision.get('target_evidence'))
                if not targets or not evidence:
                    errors.append(f"{nid}: missing mapped scope evidence for {old['id']}")
                for tid in targets:
                    if tid not in now and tid not in retired:
                        other=tid.split('-')[1] if re.fullmatch(r'BANK-\d{3}-\d{3,}',tid) else None
                        if not other or other not in baseline:
                            errors.append(f'{nid}: invalid starter audit target {tid}')
                        else:
                            if other not in target_id_cache:
                                linked=m.read(m.home(other)/'IN_DEPTH_TOPIC_BANK.json')
                                target_id_cache[other]={t['id'] for c,t in m.records(linked)}|{
                                    t['id'] for t in linked.get('retired_duplicate_proposals',[])}
                            if tid not in target_id_cache[other]:
                                errors.append(f'{nid}: missing starter audit target {tid}')
        totals['starter_subjects']+=len(starters);totals['unmapped_starters']+=len(missing)
        changes.append({'niche_id':nid,'before':len(original),'after':len(now),
            'added_active_ids':additions,'retired_before_ids':removed,
            'unmapped_starter_ids':missing,'audit_file':entry['file'] if entry else None})
    if len(audit_entries)!=len(baseline):errors.append('Editorial bank inventory is incomplete or contains extra bank IDs')
    result={'date':'2026-10-24','banks_in_baseline':len(baseline),'banks_with_audit':len(audit_entries),
        'totals':dict(totals),'errors':errors,'banks':changes,
        'limit':'Checks recorded review coverage, preserved questions/scopes, identity and mapping presence; not semantic uniqueness, exhaustive subject coverage or factual verification.'}
    m.write(ROOT/'topics/TOPIC_BANK_EDITORIAL_VALIDATION.json',result)
    print({k:v for k,v in result.items() if k not in ('banks','errors')})
    if errors:print('\n'.join(errors[:30]))
    return not errors


if __name__=='__main__':raise SystemExit(0 if main() else 1)
