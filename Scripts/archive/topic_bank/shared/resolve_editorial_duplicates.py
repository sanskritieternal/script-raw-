from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Record scope-reviewed duplicate decisions without inferring them from similarity scores.

The underlying recommendations and full question/scope comparison are retained in
editorial_duplicate_scope_review.json. Run after range audits are final, before
consolidate_editorial_duplicates.py.
"""
from collections import defaultdict

import manage_all_topic_banks as m


ROOT = m.ROOT

# Review of both actual individual scopes found these meaningful distinctions.
REJECTED = {
    'BANK-036-053': ('BANK-003-130', 'The former compares temple and inscription authority across dated sites; the latter tests early Pallava epigraphic claims against later monuments.'),
    'BANK-095-022': ('BANK-013-047', 'Professional stone carving stages are a different production question from the archaeological reconstruction of historic hollow vessels.'),
    'BANK-101-034': ('BANK-009-116', 'General Stroop interference and cross-language reading skill measurement ask different questions.'),
    'BANK-292-038': ('BANK-054-029', 'The comparative dual/nondual Vedanta question extends beyond the Advaita-specific question.'),
    'BANK-546-045': ('BANK-546-044', 'Scheduling, access and role-specific exposure differ from batting eras, venues and opposition.'),
}

# Explicit choices for conflicting recommendations and reciprocal suggestions.
PREFERRED = {
    'BANK-291-040': 'BANK-004-026',
    'BANK-274-042': 'BANK-004-027',
    'BANK-343-038': 'BANK-006-021',
    'BANK-367-031': 'BANK-006-022',
    'BANK-354-034': 'BANK-006-036',
    'BANK-348-034': 'BANK-006-072',
    'BANK-349-033': 'BANK-006-078',
    'BANK-302-031': 'BANK-008-096',
    'BANK-342-035': 'BANK-019-033',
    'BANK-023-038': 'BANK-278-092',
    'BANK-350-037': 'BANK-026-027',
    'BANK-216-032': 'BANK-030-027',
    'BANK-003-149': 'BANK-003-043',
    'BANK-036-045': 'BANK-003-043',
    'BANK-286-036': 'BANK-036-096',
    'BANK-218-054': 'BANK-038-023',
    'BANK-256-032': 'BANK-043-014',
    'BANK-252-037': 'BANK-044-020',
    'BANK-234-032': 'BANK-047-024',
    'BANK-268-050': 'BANK-054-031',
    'BANK-323-032': 'BANK-061-032',
    'BANK-071-021': 'BANK-009-028',
    'BANK-171-031': 'BANK-009-028',
    'BANK-275-035': 'BANK-075-019',
    'BANK-280-092': 'BANK-077-032',
    'BANK-360-033': 'BANK-087-018',
    'BANK-261-034': 'BANK-095-022',
    'BANK-307-032': 'BANK-106-026',
    'BANK-308-032': 'BANK-107-011',
    'BANK-210-020': 'BANK-114-018',
    'BANK-205-015': 'BANK-115-021',
    'BANK-206-026': 'BANK-115-022',
    'BANK-187-016': 'BANK-142-015',
    'BANK-161-010': 'BANK-113-010',
    'BANK-211-023': 'BANK-113-010',
    'BANK-055-030': 'BANK-012-014',
    'BANK-344-030': 'BANK-012-014',
    'BANK-251-031': 'BANK-251-037',
    'BANK-278-086': 'BANK-023-022',
    'BANK-541-047': 'BANK-004-079',
}

# These are useful as distinct topics. The first belongs to a particular Gita
# passage; the second frames a larger philosophical dialogue.
EXTRA_BOUNDARIES = [
    ('BANK-004-079', 'BANK-271-039', 'Arjuna’s state before and during the Gita dialogue versus the larger teaching framework of the Gita.'),
    ('BANK-095-022', 'BANK-013-047', 'Professional carving workflow versus archaeological evidence for hollow-vessel production.'),
    ('BANK-036-053', 'BANK-003-130', 'Temple and inscription authority across sites versus early Pallava epigraphic claims.'),
    ('BANK-101-034', 'BANK-009-116', 'General Stroop interference versus cross-language reading skill as a measurement variable.'),
    ('BANK-292-038', 'BANK-054-029', 'Dual and nondual Vedanta comparison versus Advaita-specific analysis.'),
    ('BANK-546-045', 'BANK-546-044', 'Scheduling and role exposure versus batting eras and venue/opposition adjustment.'),
]


def main():
    recommendations = defaultdict(list)
    for name in ('editorial_duplicate_recommendations_root.json',
                 'editorial_review_002_184.json', 'editorial_review_185_367.json',
                 'editorial_review_368_550.json'):
        obj = m.read(ROOT / 'Scripts' / name)
        for row in obj.get('duplicate_recommendations', obj.get('decisions', [])):
            recommendations[row['retire_id']].append(row)
    decisions = []
    chosen_primaries = set(PREFERRED.values())
    reversed_recommendations = []
    for retire_id, options in sorted(recommendations.items()):
        if retire_id in REJECTED:
            continue
        if retire_id in chosen_primaries:
            reversed_recommendations.append(retire_id)
            continue
        targets = {row['primary_id'] for row in options}
        chosen = PREFERRED.get(retire_id)
        if chosen is None:
            assert len(targets) == 1, (retire_id, targets)
            chosen = next(iter(targets))
        original = next((row for row in options if row['primary_id'] == chosen), options[0])
        assert chosen in targets or retire_id == 'BANK-211-023', (retire_id, chosen, targets)
        decisions.append({'retire_id': retire_id, 'primary_id': chosen,
                          'reason': original['reason'] + (' The reviewed common primary is BANK-113-010.' if retire_id == 'BANK-211-023' else '')})
    # The reciprocal recommendation preferred a later repeated Nasadiya
    # treatment. Keep the original close-reading record as primary instead.
    decisions.append({'retire_id': 'BANK-291-040', 'primary_id': 'BANK-004-026',
                      'reason': 'Both cover the Nasadiya Sukta creation-question passage. Keep the original close reading as primary and preserve the later question and scope in the retired record.'})
    aliases = {row['retire_id']: row['primary_id'] for row in decisions}
    cycles = []
    for source in aliases:
        seen = set()
        target = source
        while target in aliases:
            if target in seen:
                cycles.append((source, tuple(sorted(seen))))
                break
            seen.add(target)
            target = aliases[target]
    assert not cycles, ('alias cycles', cycles)
    m.write(ROOT / 'Scripts' / 'editorial_duplicate_decisions_final.json',
            {'decisions': decisions, 'rejected_as_distinct': [
                {'retire_id': tid, 'compared_id': other, 'boundary': why}
                for tid, (other, why) in sorted(REJECTED.items())],
             'additional_scope_boundaries': [
                 {'topic_id': a, 'related_id': b, 'boundary': why}
                 for a, b, why in EXTRA_BOUNDARIES],
             'reversed_recommendations': reversed_recommendations,
             'review_basis': 'Manual comparison of full question and individual coverage scope; no lexical score retires a topic.'})
    print(f'{len(decisions)} explicit retirements, {len(REJECTED)} distinct-scope rejections, {len(reversed_recommendations)} reversed source choices, no alias cycles.')


if __name__ == '__main__':
    main()
