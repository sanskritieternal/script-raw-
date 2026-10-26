from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Explicit editorial decisions on the two candidate sets involving 001/281."""
from pathlib import Path
import manage_all_topic_banks as m
ROOT=Path(__file__).resolve().parents[4]
VERDICTS={
 '001-034|532-032':('duplicate','001 quantization and batching scopes already explain the same tradeoff; specialist introductions should refer to them.'),
 '001-193|529-030':('distinct','A versioned machine-model output/context test differs from human translation purpose, audience and register. 001 now states that boundary.'),
 '001-108|333-030':('distinct','Evidence of communication outcomes versus signals, recording location and decoding assumptions.'),
 '009-107|281-032':('retired','One practical-versus-statistical-significance explanation, primary009107. Translated measurement equivalence is separately scoped in281115.'),
 '001-109|128-031':('duplicate','Same sensor/world mapping and tracking-failure question; source001109 primary.'),
 '001-081|531-031':('duplicate','Same durable task state and checkpoint recovery; source001081 primary.'),
 '026-037|281-113':('retired','Same consent-beyond-signature explanation, primary026037.'),
 '001-201|481-035':('duplicate','Both require theory-dependent testable criteria and evidence for AI-consciousness claims; source001201 primary.'),
 '281-015|281-087':('distinct','015 explains three substance-classification axes;087 explains the exceptional-action term when those axes do not account for a textual attribution.'),
 '001-051|093-044':('distinct','Shared question grammar, different subjects: component licensing versus measured agricultural outcomes.'),
 '001-082|338-033':('duplicate','Same task-scoped read/write/action privilege mapping; a coding example alone does not create a new threat model.'),
 '001-090|128-040':('duplicate','Same live-state, calibration and use-validation distinction from visual3D geometry; source001090 primary.'),
 '001-031|100-013':('distinct','Answer entailment from documents and forensic proposition levels require different evidence, roles and decisions.'),
 '001-044|532-035':('duplicate','Existence, passage support and attribution checks already belong in001044/031.'),
 '001-101|104-038':('distinct','Deployment supplier accountability differs from sponsor/source independence in a documentary.'),
 '001-052|007-048':('distinct','Controlled model-comparison reproducibility differs from maintaining version-dependent interface tutorial steps.'),
 '001-108|333-031':('distinct','Communication-demo outcome evidence differs from user-specific signal calibration and adaptation.'),
}
if __name__=='__main__':
    result={}
    for file in ('semantic_candidates_root.json','semantic_question_candidates_root.json'):
        for p in m.read(ROOT/'Scripts/editorial_review_inputs'/file)['pairs']:
            ids=sorted([p['left']['id'],p['right']['id']]);key='|'.join(i.removeprefix('BANK-') for i in ids)
            verdict,reason=VERDICTS[key]
            result[key]={'ids':ids,'decision':verdict,'reason':reason,'reviewed_question_and_scope':[p['left'],p['right']]}
    audit=m.read(ROOT/'Scripts/editorial_review_root.json');audit['candidate_decisions']=list(result.values())
    m.write(ROOT/'Scripts/editorial_review_root.json',audit)
    m.write(ROOT/'Scripts/editorial_duplicate_recommendations_root.json',{'decisions':[
      {'retire_id':'BANK-278-002','primary_id':'BANK-278-024','reason':'Both source records close-read the same dharana/dhyana/samadhi sequence in Yoga Sutra3; keep one episode, full original record inactive.'},
      {'retire_id':'BANK-280-035','primary_id':'BANK-278-024','reason':'Same textual relationship among the same three terms; a shorter overview format is not a distinct question.'},
      {'retire_id':'BANK-279-091','primary_id':'BANK-279-005','reason':'Both source scopes request the same intervention protocol checklist; paper-reading vocabulary versus checklist presentation is not a distinct subject.'},
      {'retire_id':'BANK-280-008','primary_id':'BANK-278-030','reason':'Both source scopes examine the same Shvetashvatara body/breath/contemplation passage; retain one bounded close reading.'},
    ]})
    print(f'Saved {len(result)} direct root candidate decisions and four protected-source overlap recommendations.')
