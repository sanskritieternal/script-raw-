from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Record reviewed scope decisions for root-owned topic banks; preserve source records."""
import copy
from collections import Counter
from pathlib import Path
import manage_all_topic_banks as m
import manage_ai_topics as ai

ROOT=Path(__file__).resolve().parents[4]

# Explicit playlist entry order, reviewed against original titles and active scopes.
# These are referrals/narrowing decisions, not claims every broad old title is a new episode.
PLAYLIST_REFS={
 0:[18,18,84,51,51,51,13,89,52,14,53,85,54,57,56,55,87,18],
 1:[31,33,90,91,65,19,19,92,42,67,93,29,22,72,19,94,95,71,19,117,21,107,95,96],
 2:[25,98,104,107,21,107,21,82,69,21,21,49,70,97,107,99],
 3:[20,25,90,19,21,20,20,19,21,133,20,23],
 4:[63,56,55,107,63,62,62,107,105,63,28,30,101,49,49,107],
 5:[107,107,100,100,101,91,25,106,107,99,107,107,56,107],
 6:[62,62,108,113,110,79,99,62,109,109,62,108,62,113],
 7:[61,61,61,61,61,61,61,61,114,61,61,107],
 8:[52,119,119,119,119,107,119,28,107,63,124,48],
 9:[108,108,108,31,19,82,82,108,108,48,111,48],
10:[49,65,33,96,95,91,95,95,48,48,99,38],
11:[118,92,118,118,48,116,116,82,117,48,108,48],
12:[31,124,117,117,88,121,109,48,48,123,48,121],
13:[29,104,103,104,26,26,102,103,30,79,28,27],
14:[78,78,80,80,80,112,112,112,112,112,111,113,113,14],
15:[75,76,64,128,129,129,130,16,75,83,83,45,19,131,132,77],
16:[50,33,31,31,39,26,115,124,49,44,81,74,120,122,116,48],
17:[81,62,89,55,33,33,90,29,124,124,49,60,107,27,47,124],
18:[134,134,91,20,23,41,133,24,134,22,71,20,77,82,75,19],
19:[87,20,20,19,21,25,29,49,115,50,61,19,74,33,83,46],
}
PLAYLIST_BOUNDARIES={
 0:'The broad foundational title is narrowed to an attributed term/framework question; linked scopes do not diagnose viewers or validate the framework as modern physiology.',
 1:'A named monograph is a possible case, not automatically a distinct episode. The link supplies a material, identity, cultural or evidence question; a complete plant biography is not claimed.',
 2:'Preserve the spice title as a culinary/material case. Where the link is a general material or food method, select a case only if it changes the question; no copied spice-by-angle series is counted.',
 3:'Identification demonstrations use authenticated specimens and a bounded material question. A photograph or guessing format is not evidence of product authenticity or safe use.',
 4:'Traditional food descriptions are separated from nutrition or clinical conclusions. The link defines the interpretive/material boundary; individualized diet advice is outside this catalog.',
 5:'Recipe and regional variants are culinary case/format choices within a scoped food proposal, not automatically additional therapeutic episodes. No recipe is asserted to treat a condition.',
 6:'Routine adaptations are case choices within source-context, experience or supervision questions. General sleep, exercise and hygiene guidance belongs in the specialist health banks.',
 7:'Individual seasons remain selectable source passages within the calendar/transition questions. Renaming the season alone does not create another distinct episode.',
 8:'The legacy symptom wording is retained but not promoted to diagnosis or self-treatment. Its Ayurveda-specific contribution is a claim, material or study-design question; general clinical explanation belongs in niche 353/015.',
 9:'Separate textual sleep/context questions and preparation-specific study review from generic sleep, meditation or mental-health instruction, whose primary homes are 538/280/537.',
10:'A product/plant example is narrowed to material identity, carrier effects or evidence boundaries. Diagnosing hair loss, scalp disease or skin reactions is outside these proposals.',
11:'These broad health titles are narrowed to preparation matching, population evidence or claim-endpoint questions. General reproductive and maternal care belongs in 504/353; no treatment choices are supplied.',
12:'Separate ageing and performance marketing from exact endpoints and populations. General ageing, nutrition, exercise and clinical care remain neighboring topics, not promised herbal protocols.',
13:'Preparation/group names are compared as material classifications and formula identities. Descriptions do not provide medicinal manufacturing instructions or establish efficacy.',
14:'The linked topics describe attributed categories and consent/supervision questions. Individual procedures remain historical/source cases; operational instructions are deliberately outside scope.',
15:'Named text and institution titles are bounded by selected passages/editions or a dated policy case. The link does not claim all contents, authorship or chronology are already researched.',
16:'The link identifies a particular evidence or public-claim question. Any named trial, standard, reporting route or clinical statement needs later primary-source and qualified review.',
17:'An internet myth is narrowed to a defined classification or testable claim. A yes/no title is not retained as an unsupported factual conclusion or an extra episode duplicating the linked question.',
18:'Visits, interviews and cultivation stories are possible evidence-gathering formats for these scopes; access, permission, named location and source records remain to be selected.',
19:'Shorts, quizzes and viewer Q&A are packaging variants of the linked substantive questions. They are not additional active BANK proposals merely because their runtime or wording differs.',
}


def finalize_281():
    p=m.home('281')/'IN_DEPTH_TOPIC_BANK.json';b=m.read(p)
    for c in b['categories']:
        old=next((t for t in c['topics'] if t['id']=='BANK-281-032'),None)
        if old:
            retired=copy.deepcopy(old);retired.update(duplicate_of='BANK-009-107',retirement_reason='The practical significance versus statistical significance question already has a protected primary proposal in psychology. Use one common explanation; translated patient-outcome measurement is separately scoped in BANK-281-115.')
            b.setdefault('retired_duplicate_proposals',[]).append(retired)
            c['topics'].remove(old)
        consent=next((t for t in c['topics'] if t['id']=='BANK-281-113'),None)
        if consent:
            retired=copy.deepcopy(consent);retired.update(duplicate_of='BANK-026-037',retirement_reason='The common informed-consent question is already scoped in ethics; a traditional-care example alone does not justify a second counted explanation.')
            b.setdefault('retired_duplicate_proposals',[]).append(retired);c['topics'].remove(consent)
        for tid,primary,reason in [
            ('BANK-281-092','BANK-281-020','The new Shatavari example repeats voucher/plant-part/batch authentication already in020 and031; a plant-name substitution alone is not a separate subject.'),
            ('BANK-281-118','BANK-281-047','The broad condition-claim comparison repeats defining population, intervention and outcomes already in047/031; naming PCOS or menopause does not add a distinct evidence mechanism.')]:
            repeated=next((t for t in c['topics'] if t['id']==tid),None)
            if repeated:
                archived=copy.deepcopy(repeated);archived.update(duplicate_of=primary,retirement_reason=reason)
                b.setdefault('retired_duplicate_proposals',[]).append(archived);c['topics'].remove(repeated)
    for c,t in m.records(b):
        if 'related_ids' in t:t['related_ids']=['BANK-281-115' if ref=='BANK-281-032' else ref for ref in t['related_ids']]
    for old,refs in b.get('starter_concept_crosswalk',{}).items():
        b['starter_concept_crosswalk'][old]=list(dict.fromkeys('BANK-009-107' if ref=='BANK-281-032' else ref for ref in refs))
    b.setdefault('editorial_cross_references',[])
    cross={'topic_id':'BANK-281-115','related_id':'BANK-009-107','boundary':'The neighboring topic explains statistical versus practical size generally. This topic tests whether translated patient-reported measurements mean the same thing before a trial result is interpreted.'}
    if cross not in b['editorial_cross_references']:b['editorial_cross_references'].append(cross)
    legacy={}
    done=[18,89,86,14,62,61,56,105,108,31,29,33,78,79,59,60,81,37,119,49]
    queue=[18,31,33,51,90,91,52,25,29,62,19,30,92,110,65,89,103,78,49,74]
    trends=[68,106,126,127,125,31]
    decisions=[]
    for route,t in m.legacy_records(b['local_reconciliation']['local_status_original']):
        parts=route.split('/');index=int(parts[-1]);title=t.get('title',t.get('concept',''))
        if parts[0]=='playlists':
            pi=int(parts[1]);n=PLAYLIST_REFS[pi][index];reason=PLAYLIST_BOUNDARIES[pi]
            decision='format/case selection' if pi in (5,7,18,19) else 'narrowed to a scoped question'
        elif parts[0]=='completed_topics':n=done[index];reason='Original completion status and title are retained without certification. The current proposal supplies a bounded inquiry rather than endorsing the historical title or repeating its broad survey.';decision='preserved execution reference with scope referral'
        elif parts[0]=='first_20_uploads_queue':n=queue[index];reason='Original upload-queue metadata stays unchanged. The linked scope defines the proposed question; this is not an additional counted episode or production approval.';decision='queue reference to scoped proposal'
        else:n=trends[index];reason='Historical trend language is preserved without a claim of current popularity or proven benefit. Narrow to the linked evidence/material question before selecting a case.';decision='unverified historical trend narrowed'
        legacy[route]={'decision':decision,'reason':reason,'bank_ids':[f'BANK-281-{n:03d}']}
        if n==113:legacy[route]['bank_ids']=['BANK-026-037']
        if n==92:legacy[route]['bank_ids']=['BANK-281-020','BANK-281-031']
        if n==118:legacy[route]['bank_ids']=['BANK-281-047','BANK-281-031']
        decisions.append({'route':route,'title':title,**legacy[route]})
    b['legacy_topic_crosswalk']=legacy
    b['open_coverage']=[
        {'area':'Legacy cases and formats','next_step':'Every preserved playlist, queue and trend reference now has an editorial disposition and scope referral. Named plant/recipe/season variants and field visits still need a distinct case, permission and sources before becoming episodes; short-form packaging alone is not new subject coverage.'},
        {'area':'Regional and textual case selection','next_step':'Foundational terms, named-text comparisons, colonial institutions and household transmission now have explicit questions. Choose exact passages, editions, language assistance, regions and practitioner accounts rather than imply a single tradition-wide answer.'},
        {'area':'Evidence and qualified review','next_step':'Preparation, population, translated outcomes, reporting and public-claim questions are scoped. Actual trial records, official dated standards, laboratory data and qualified clinical interpretation remain research work; no clinical protocol or product certification is supplied.'},
    ]
    b['editorial_review']={'summary':'Reviewed every active question and scope, all twelve starter subjects and all preserved legacy reference routes. Added missing foundational, food/preparation, practice, population-evidence, claim and text/institution branches; reserved overlapping statistical-significance wording under its primary question and kept recipe/season/short variants as cases rather than filler.','audit_file':'Scripts/editorial_review_root.json'}
    b['counts']={'categories':len(b['categories']),'proposed_topics':len(m.records(b))}
    assert not m.check_bank(b,p.parent),m.check_bank(b,p.parent)
    m.write(p,b);m.render(b,p.parent)
    return b,decisions


if __name__=='__main__':
    before=m.read(ROOT/'Scripts/editorial_review_inputs/before_editorial_pass.json')['banks']
    b281,legacy=finalize_281();b001=ai.load(ai.HOME/'IN_DEPTH_TOPIC_BANK.json')
    results={}
    for nid,b in [('001',b001),('281',b281)]:
        now={t['id']:t for c in b['categories'] for t in c['topics']};old={t['id']:t for t in before[nid]['topics']}
        results[nid]={'reviewed_before_ids':list(old),'reviewed_active_ids':list(now),'source_questions_scopes_read':True,
            'added_ids':[tid for tid in now if tid not in old], 'retired_ids':[tid for tid in old if tid not in now],
            'starter_decisions':[{'starter_id':tid,'target_ids':refs,'scope_evidence':[now[t]['coverage'] if t in now else 'Primary neighboring proposal; see cross-niche referral.' for t in refs]} for tid,refs in b['starter_concept_crosswalk'].items()],
            'previous_gaps_read':before[nid]['open_coverage'], 'remaining_specific_work':b['open_coverage']}
    results['001']['gap_decisions']=[
        {'area':'Language and regional depth','decision':'added','ids':[f'BANK-001-{n:03d}' for n in [216,217,218]],'reason':'Normalization, transliterated retrieval and morphology pose distinct mechanisms; dialect transcription remains in 068/103/133.'},
        {'area':'Architecture and research frontiers','decision':'added concrete missing branches','ids':[f'BANK-001-{n:03d}' for n in [211,212,213,214,215,219,220,221]],'reason':'Dimensionality reduction, label acquisition, partial-feedback learning, teacher/student transfer, adapter structure, reranking and endpoint lifecycle/abstention questions differ from the existing training and inference explanations.'},
        {'area':'Deployment outcomes and affected users','decision':'added','ids':['BANK-001-222','BANK-001-223'],'reason':'Longitudinal evaluation and changing shared-user memory add temporal and consent questions beyond the initial productivity baseline.'},
        {'area':'Energy, water and hardware lifecycle','decision':'existing scoped coverage; case selection remains','ids':[f'BANK-001-{n:03d}' for n in [49,203,204,205,206,207]],'reason':'Operational boundaries, water, embodied material, supply contracts, heat transfer and retirement are already distinct questions. Another regional example needs measured records rather than a cloned topic.'},
        {'area':'Legal and institutional variation; named historical cases; readiness','decision':'research/case selection','ids':[f'BANK-001-{n:03d}' for n in [140,144,186,188,189]],'reason':'The missing items are chosen versions, jurisdictions, dates and primary records, not an absent general branch; no current-law or historical finding was invented.'},
    ]
    results['001']['semantic_decisions']=[
        {'ids':['BANK-001-020','BANK-001-152'],'decision':'distinct','boundary':'020 follows a complete optimizer update;152 derives credit assignment through local derivatives before any update.'},
        {'ids':['BANK-001-034','BANK-001-126'],'decision':'distinct','boundary':'034 compares compressed weight representations and quality;126 tests numerical tolerances/accumulation/runtime reproducibility.'},
        {'ids':['BANK-001-193','BANK-529-030'],'decision':'distinct with explicit boundary','boundary':'001 studies a versioned machine-translation output/context test;529 addresses human communicative purpose and translation judgment.'},
        {'ids':['BANK-001-081','BANK-531-031'],'decision':'same core question; retain source001 primary','boundary':'531 should refer to checkpoints/state recovery here and use specialist operating-system questions instead.'},
        {'ids':['BANK-001-109','BANK-128-031'],'decision':'same core tracking question; retain source001 primary','boundary':'Reported to owning agent for retirement/referral of redundant new128 proposal.'},
        {'ids':['BANK-001-108','BANK-333-030'],'decision':'distinct','boundary':'108 evaluates what a communication demo proves;333 identifies the signal, recording location and decoding assumptions.'},
    ]
    results['281']['gap_decisions']=[
        {'area':'Existing playlist titles','decision':'reviewed every route; explicit narrowing/case/format/neighbor decisions','added_ids':results['281']['added_ids'],'legacy_dispositions':legacy},
        {'area':'Regional/textual variation','decision':'added concrete text/institution questions','ids':[f'BANK-281-{n:03d}' for n in range(128,135)],'reason':'Named text comparison, materia-medica history, iconography, colonial teaching, facility observation and tenure/benefit sharing cover distinct gaps; editions and locations remain case choices.'},
        {'area':'Preparation-specific evidence','decision':'added','ids':[f'BANK-281-{n:03d}' for n in range(90,108)]+[f'BANK-281-{n:03d}' for n in range(115,122)],'reason':'Material fractions/carriers, extraction categories, named food/formula identity, measurement equivalence, population transfer and surrogate outcomes now have bounded inquiries.'},
        {'area':'Safety/public claims','decision':'added','ids':[f'BANK-281-{n:03d}' for n in range(122,128)],'reason':'Reporting, polypharmacy documentation, undefined marketing endpoints, copper exposure, pack absorption and autophagy extrapolation have distinct evidence questions, without advice.'},
    ]
    results['281']['semantic_decisions']=[
        {'ids':['BANK-281-032','BANK-009-107'],'decision':'retired new281 overlap; source009 primary','boundary':'Keep one practical-versus-statistical-significance explanation.'},
        {'ids':['BANK-281-113','BANK-026-037'],'decision':'retired new281 overlap; source026 primary','boundary':'Consent beyond a signature is the same core question; a clinical example does not warrant another active explanation.'},
        {'ids':['BANK-281-092','BANK-281-020'],'decision':'retired case-only overlap','boundary':'A plant-name substitution does not add a new material-authentication mechanism; keep the Shatavari title as a possible case.'},
        {'ids':['BANK-281-118','BANK-281-047'],'decision':'retired broad claim-framework overlap','boundary':'The proposed population/material/comparator/endpoint checklist already exists; condition examples need a distinct clinical-research question before another BANK proposal.'},
        {'ids':['BANK-281-021','BANK-281-065'],'decision':'general method versus bounded named-material case','boundary':'021 compares plant parts as study identities;065 limits its inquiry to neem leaf versus seed-oil exposures and reporting.'},
        {'ids':['BANK-281-017','BANK-281-075'],'decision':'method versus manuscript transmission case','boundary':'017 addresses edition/translation differences;075 follows Charaka manuscript witnesses and editorial apparatus.'},
        {'ids':['BANK-281-038','BANK-281-122'],'decision':'distinct roles','boundary':'038 concerns qualified causal investigation of a signal;122 concerns what a lay report must document before that investigation.'},
        {'ids':['BANK-281-027','BANK-281-103'],'decision':'general material identity versus carrier/formulation case','boundary':'027 compares the same formula name across recipes;103 isolates the avaleha base and food-like marketing of Chyawanprash.'},
    ]
    audit={'date':'2026-10-23','status':'owned_scope_review_complete','source_verification':'not_performed',
        'exhaustive_claim':False,'method':'Direct review of before-pass questions/scopes, original starter subjects, gap notes and legacy titles; authored decisions are saved below. Lexical candidates are triage only.', 'banks':results}
    m.write(ROOT/'Scripts/editorial_review_root.json',audit)
    print({nid:{'active':len(v['reviewed_active_ids']),'added':len(v['added_ids']),'retired':len(v['retired_ids'])} for nid,v in results.items()})
