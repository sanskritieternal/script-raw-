"""Record manual scope decisions on all fresh post-addition lexical candidates.

The numbered pair file is an immutable review input produced after the first
duplicate consolidation. Similarity scores never decide the verdict.
"""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
INPUT = ROOT / 'Scripts/editorial_review_inputs/final_new_semantic_candidates.json'

RETIRE = {
    1: ('BANK-354-040', 'BANK-006-125', 'Both trace microbial horizontal gene transfer, gene trees and the failure of a single organism tree; retain the established mechanism scope.'),
    2: ('BANK-470-041', 'BANK-470-038', 'Both ask who consents to enhancement affecting future generations and compare reversibility and intergenerational consequences.'),
    4: ('BANK-541-039', 'BANK-004-162', 'Both map Mahabharata telling occasions and narrator knowledge in an edition; keep the newly bounded frame-structure proposal.'),
    5: ('BANK-056-053', 'BANK-002-076', 'Both examine Beale paper editions, provenance and cipher claims before accepting the treasure narrative.'),
    18: ('BANK-471-042', 'BANK-470-032', 'Workplace incentives, refusal costs and nominally optional enhancement are the same episode; retain the general ethics primary.'),
    19: ('BANK-425-036', 'BANK-425-045', 'Both cover train stopping and station coordination for platform doors; the newer scope also bounds evacuation responsibilities.'),
    27: ('BANK-470-043', 'BANK-470-032', 'Formally optional hiring enhancement under unequal bargaining power repeats the workplace-compulsion question.'),
    32: ('BANK-411-044', 'BANK-411-039', 'Oversized material texture in a miniature is already the concrete scale-cue and surface-detail problem in the primary scope.'),
    35: ('BANK-396-030', 'BANK-064-046', 'Both compare household appliance power, running time and measured energy; the existing scope has explicit cycles and service denominators.'),
    38: ('BANK-526-042', 'BANK-096-042', 'Both ask about museum and source-community care, authority and responsibilities after repatriation, beyond the handover ceremony.'),
    39: ('BANK-056-030', 'BANK-002-024', 'Both test claimed Voynich decipherment by reproducibility, broad corpus coverage and independent validation.'),
    45: ('BANK-140-044', 'BANK-021-022', 'Both bound what a pre-purchase marine survey can establish when access and testing exclude systems.'),
    53: ('BANK-430-041', 'BANK-430-035', 'The generic tower conversion scope repeats floor plate, services and egress barriers already bounded to housing conversion.'),
    55: ('BANK-324-043', 'BANK-061-026', 'Both explain why asynchronous operations do not imply parallel CPU computation using scheduling and I/O examples.'),
    56: ('BANK-550-046', 'BANK-124-042', 'Both use pickup pattern, distance and room response to explain a microphone recording; the primary states the controlled comparison.'),
}

DISTINCT = {
    0: 'Airport noise, land and surface transport distribution differ from theme-park housing and services impact.',
    3: 'Campaign coordination and data submission differ from uncertainty in one amateur occultation timing.',
    6: 'Memoir reshaping of early letters differs from constructing a chronology across conflicting record classes.',
    7: 'National largest-city/capital contrast differs from the administrative role of a provincial capital.',
    8: 'Resident authority in travel documentary framing differs from accountable health-program needs assessment.',
    9: 'Multiplayer synchronization differs from preservation when a virtual-world server closes.',
    10: 'General oral-performance adaptation differs from the named Terukkuttu staging and local musical roles; case binding is still required.',
    11: 'Whole theatre-production preservation differs from contextual metadata for a folk-theatre recording.',
    12: 'Clinical patient-footage reconstruction differs from synthetic imagery mistaken for archival footage.',
    13: 'A black-hole horizon model differs from comparison with the cosmological particle horizon.',
    14: 'Circus publicity about race/nationality differs from labor bargaining over pay and working conditions.',
    15: 'Audience tracking of a selected card differs from measured differences between remembered and actual routine conditions.',
    16: 'Drivetrain operating-point efficiency and percentage-point arithmetic have different objects.',
    17: 'General longitudinal versus cross-sectional age design differs from the measurement of children’s sleep.',
    20: 'Reviewing experimental live performance differs from analyzing attention in an experimental film.',
    21: 'Pipeline gas composition and specification differ from liquefaction, storage and receiving systems.',
    22: 'Landing-impact and mass design tradeoffs differ from seals, actuation and repeated-service reliability.',
    23: 'Household currency mismatch management differs from economy-wide foreign-currency functions.',
    24: 'Protected-land access, sampling and data release differ from commercial image publication rights.',
    25: 'Character appearance continuity differs from downstream editing and sound revisions after a changed shot.',
    26: 'Emotion regulation versus suppression is a human measurement question; recognition versus experience concerns AI consciousness.',
    28: 'Food-web dependencies and supply-chain food loss are unrelated despite shared food wording.',
    29: 'Participle translation and finite tense/aspect translation are different grammatical objects.',
    30: 'Staging/payload performance design differs from integration interface test failures.',
    31: 'Macro employment/ownership futures differ from training apprentices when entry tasks change.',
    33: 'General product service shutdown differs from memorial-data custody and deletion after provider closure.',
    34: 'Mahabharata dialogue close reading differs from planning a visual adaptation of that dialogue.',
    36: 'Updating current-event analysis differs from correcting dated trivia answers in an archive.',
    37: 'Wildlife camera disturbance differs from drone footage permissions and aviation rules.',
    40: 'Road/track brake behavior differs from regulatory approval of a road-legal vehicle.',
    41: 'Detector signals and noise rejection differ from multimessenger evidence compared with telescope images.',
    42: 'Garuda narrative roles differ from regional Vaishnava emphasis among forms of Vishnu.',
    43: 'Forest system structure differs from the specific ecological roles of dead trees.',
    44: 'Definitions of consciousness differ from clinical assessment as a limit on philosophical inference.',
    46: 'Service access due to distance differs from historical administrative transfer of a territory.',
    47: 'Why headset motion causes discomfort differs from measuring discomfort without a universal latency threshold.',
    48: 'Classical stages of a quantum workload differ from classical control-hardware scaling constraints.',
    49: 'General theory-measurement disagreement differs from discriminating AI-specific consciousness predictions.',
    50: 'Meaning of unofficial flag use differs from historical adoption and changing legal status.',
    51: 'One verse with its traditional commentary differs from a landscape-imagery and speaker reading; select passages to preserve this boundary.',
    52: 'General household labor archaeology differs from Egyptian craft-workshop debris as a bounded case.',
    54: 'Linear versus parallel clue paths differ from remote-participant clue fairness.',
    57: 'Pitch accent in recitation differs from editorial choices among manuscripts, accent notation and recitation.',
    58: 'Defining an alternate-nostril intervention differs from choosing an active comparator in its trial.',
    59: 'General auction provenance and restriction checks differ from a restitution claim despite legal sale.',
}


def main():
    pairs = json.loads(INPUT.read_text(encoding='utf-8'))['pairs']
    assert len(pairs) == 60 and set(RETIRE) | set(DISTINCT) == set(range(60))
    assert not set(RETIRE) & set(DISTINCT)
    verdicts = []
    decisions = []
    for i, pair in enumerate(pairs):
        ids = {pair['left']['id'], pair['right']['id']}
        if i in RETIRE:
            old, primary, why = RETIRE[i]
            assert ids == {old, primary}, (i, ids, old, primary)
            verdicts.append({'pair_index': i, 'ids': sorted(ids), 'decision': 'consolidate_same_episode',
                             'reason': why, 'scope_evidence': [pair['left']['coverage'], pair['right']['coverage']]})
            decisions.append({'retire_id': old, 'primary_id': primary, 'reason': why})
        else:
            verdicts.append({'pair_index': i, 'ids': sorted(ids), 'decision': 'retain_distinct_scope',
                             'reason': DISTINCT[i], 'scope_evidence': [pair['left']['coverage'], pair['right']['coverage']]})
    (ROOT / 'Scripts/editorial_final_semantic_decisions.json').write_text(
        json.dumps({'input': INPUT.relative_to(ROOT).as_posix(), 'pairs_reviewed': len(verdicts),
                    'method': 'Manual reading of both full questions and coverage scopes; similarity is only triage.',
                    'candidate_decisions': verdicts, 'duplicate_recommendations': decisions},
                   ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'Scripts/editorial_final_duplicate_additions.json').write_text(
        json.dumps({'decisions': decisions}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    final_path = ROOT / 'Scripts/editorial_duplicate_decisions_final.json'
    final = json.loads(final_path.read_text(encoding='utf-8'))
    combined = {row['retire_id']: row for row in final['decisions']}
    for row in decisions:
        assert row['retire_id'] not in combined or combined[row['retire_id']] == row
        combined[row['retire_id']] = row
    final['decisions'] = list(combined.values())
    final['additional_candidate_review'] = 'Scripts/editorial_final_semantic_decisions.json'
    final_path.write_text(json.dumps(final, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Reviewed {len(verdicts)} new lexical pairs: {len(decisions)} duplicate recommendations, {len(DISTINCT)} retained distinctions.')


if __name__ == '__main__':
    main()
