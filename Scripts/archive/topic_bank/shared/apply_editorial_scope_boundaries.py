from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Add reviewed neighboring-topic boundaries and correct compound starter routes.

Run after duplicate consolidation, so every target resolves to a live proposal.
"""
import manage_all_topic_banks as m


ROOT = m.ROOT


def main():
    data = m.read(ROOT / 'Scripts/editorial_duplicate_decisions_final.json')
    banks = {}
    changed = set()
    for item in data['additional_scope_boundaries']:
        nid = item['topic_id'].split('-')[1]
        b = banks.setdefault(nid, m.read(m.home(nid) / 'IN_DEPTH_TOPIC_BANK.json'))
        refs = b.setdefault('editorial_cross_references', [])
        if not any(r['topic_id'] == item['topic_id'] and r['related_id'] == item['related_id'] for r in refs):
            refs.append(item)
            changed.add(nid)
    nid = '532'
    b = banks.setdefault(nid, m.read(m.home(nid) / 'IN_DEPTH_TOPIC_BANK.json'))
    crosswalk = b['starter_concept_crosswalk']
    expected = {
        'BANK-532-002': ['BANK-001-028', 'BANK-001-030'],
        'BANK-532-004': ['BANK-001-034'],
        'BANK-532-005': ['BANK-001-025'],
        'BANK-532-006': ['BANK-001-036'],
    }
    for old, targets in expected.items():
        if crosswalk.get(old) != targets:
            crosswalk[old] = targets
            changed.add(nid)
    # The range reviewer recorded revised gap wording without mutating banks
    # owned concurrently by the starter auditors. Apply it centrally now.
    audit = m.read(ROOT / 'Scripts' / 'editorial_review_002_184.json')
    for nid, review in audit['banks'].items():
        if 'recommended_open_coverage' not in review:
            continue
        b = banks.setdefault(nid, m.read(m.home(nid) / 'IN_DEPTH_TOPIC_BANK.json'))
        revised = review['recommended_open_coverage']
        if b.get('open_coverage') != revised:
            b['open_coverage'] = revised
            changed.add(nid)
    for nid in sorted(changed):
        p = m.home(nid) / 'IN_DEPTH_TOPIC_BANK.json'
        errors = m.check_bank(banks[nid], p.parent)
        assert not errors, (nid, errors)
        m.write(p, banks[nid])
        m.render(banks[nid], p.parent)
    print('Updated scope boundaries and starter routes in', ', '.join(sorted(changed)))


if __name__ == '__main__':
    main()
