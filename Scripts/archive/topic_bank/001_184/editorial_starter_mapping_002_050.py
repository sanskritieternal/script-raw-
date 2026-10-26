from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Explicit root decisions on detailed-bank starter archives; not auto similarity mapping."""
import manage_all_topic_banks as m
ROOT=m.ROOT
# Each comma-separated cell refers to that niche's starter in original order.
# '+' combines actual distinct scopes; 'new' is supplied by authored additions below.
MAPS={
 '002':'20,18+19,23,new,43+121,39,18+19,15+90+112,13+96+103,14+17,105,51',
 '003':'19,18,23+26,25+002:25,33+34,38+42,54,45+52,48,49+58,56+155,66',
 '004':'new,66+68+107+140,new,new,45,33,27,39+40+43,23,53+137,19+74,30+51+52,18,43,new,63',
 '005':'13,19+31,14+38,15,23+24+43,28+29,33+34,41,25+88,35,26+46,45',
 '006':'18,new,new,27,33+126,35,36,43+44+47,28+29,30,113,52+99',
 '007':'33+99,101,23+25,28+30+31,15,49+95,44+112,43+45,67+71,38+84,35,16+48+92',
 '008':'13+14,18,28,19+79,29+36,86+118,34,27,43+44,new,50+65,51+100',
 '009':'new,13+15,28+80,23,33,64,37+88,41,48,new,49+90,38+39+102',
 '010':'14,13+69,18,54+92,28+111,29,25,14+37,43+85,58+123,49,48+98+122',
 '011':'13,14,15,16,27,21+22,23,25,33+41,33+35,30+47,38',
 '012':'22,17,25,33,14+24,28+46,29,27,21+37,36,new,30+32',
 '013':'26,17,25,new,new,29+30,34,new,37,38,23,14+40',
 '014':'13,14,new,33,21,25+26,29,23+30+45,37,47,39,38',
 '015':'14,15+18,17,16,21,25+26,29+30,33+34,31,new,13+24+42,39',
 '016':'13,16,15,14,17+22,20,19,18,29,24,22+38,13+14+15+39',
 '017':'13,14,15,16,18,19,17,20,45,29,47,28',
 '018':'13,14+25,15,16,21+24,019:23+29,31+019:28,new,20+42,33+48,37,42',
 '019':'13,14,15,16,21+22,29,19+24,26,37+38,34+41,33+45,42',
 '020':'13,14,15,16,25+28,17+26,37,25+27,32+002:105,19,17+21+31+47,25+005:28',
 '021':'14+38,17+19,21+24,33+34+35,25+26,29+32,30,new,13+15,41+42,37+39,16+44',
 '022':'13+14,15,17,29+46,18,25+26+27,22,new,31,33,39,37',
 '023':'13,17+18,21+23,14+27,23+28,24+45,29,40+43,41+46,30,33+34,44',
 '024':'15,29,17,19,25,30,26,18+33+46,21+41,44+47,18+22,37',
 '025':'26,25,15,21+47,21,21+29,24+45,33,13+37,14+44,38,32+46',
 '026':'25+27,21+22,23,29,13+42,14,33,new,37,38,15+43,new',
 '027':'13,15,14+17+31,30,21,22,23,33,27+38,25,37,41+42+43',
 '028':'17,18,15+22,19,25+28,25+26,23+27,30,32,14,33+34,new',
 '029':'21,19,17,26,33,34,35,16+36,29,41,37,24+42',
 '030':'17,21,30,20,27,26,25,28,37,33,23,13+40',
 '031':'27,18,23,29,15+19,35,34,new,37+38,40,44,24+43',
 '032':'14,21+22+23,15+29+45,new,33,34,25+35,37,41,38,20,42+44',
 '033':'15+46,17,20,21+22,012:31+012:32,33+34+35+45,36,29+32,13+37+48,24,26,42+43+44+47',
 '034':'17,18,19+30,20,27,25,16+22,28,33+46,13+33,new,21+23+31',
 '035':'17,18,19,29,20+21,22,26,30,13,33+48,37,16',
 '036':'40,41,42+43,44,46,47,49+50,51,53,54,55,62,61,58+59,56,66,74,78+79+81,82+84,92,87,89,96,95,100,101,102,103,104,105,37,45+46+50+75,51+88+112,86+106+107,36',
 '037':'15,18,19,20,28,25,26,27,13+31+39,34+41,16+22+23,36+37',
 '038':'13,21,18,22+24,29,30,31,32,26,25,17,15',
 '039':'16,21+47,25,45,23,33,29,new,39,37,14,new',
 '040':'17,18,19+29,20,21+27,22,14,23,29,33,32+35+40,38+39',
 '041':'17,21,21,20,13+15+20,13+32,25+26+27,18+44,37+38+39,33+48,16,45',
 '042':'new,25,new,20,24+29,18+30,new,new,32+39,14+46,16+38,32+43',
 '043':'13+14,15+24,28,30+47,18+25,new,new,33,15+38,new,37,19+42',
 '044':'13+16,17,25,33,new,14+29,33,19+32,24,26,new,new',
 '045':'18,21+48,30,new,13+16,27,19+45,new,new,new,new,14+16+42',
}

ADDITIONS={
 '002':[(4,'What can the Antikythera wreck assemblage reveal beyond the mechanism itself?', 'Compare securely recorded cargo, find locations, recovery phases and dating in a future published excavation case; distinguish the shipwreck assemblage from reconstructing missing gears or assuming a single undocumented voyage.', 'Archaeological context','intermediate')],
 '004':[(1,'How can a Puranic genealogy organize narrative authority without supplying a continuous historical chronology?', 'Read one named lineage list alongside its narrative setting, transmission and attributed dating; distinguish succession within a sacred account from independently anchored reign dates.', 'Narrative frames and source comparison','intermediate'),
 (3,'What changes when the Mahabharata tells a story through several nested narrators?', 'Track the telling settings, reported speakers, audience and knowledge available at each level in a specified public edition; distinguish the frame structure from a chronological summary of the war.', 'Narrative frames and source comparison','intermediate'),
 (4,'How can a Vedic deity in a hymn be compared with the same named figure in a later narrative?', 'Choose a traceable hymn and later public passage, compare addressee, ritual or narrative function and translation context; avoid treating a shared name as proof of unchanged theology across periods.', 'Narrative frames and source comparison','advanced'),
 (15,'How does a classical dance interpretation select a narrative viewpoint from a sacred episode?', 'Compare a publicly authorized performance account with its declared source passage, gesture vocabulary, narrator and omitted action; distinguish an attributed choreographic reading from the only textual meaning.', 'Narrative frames and source comparison','intermediate')],
 '006':[(2,'What does a quantum-field vacuum mean when it is not ordinary empty space?', 'Compare a theory-defined lowest-energy state, fields, measurement and a specified proposed experimental inference; distinguish a physical model from claims that empty space contains a limitless usable energy supply.', 'Quantum concepts and inference','intermediate'),
 (3,'Why is the quantum measurement problem more than an experiment disturbing a particle?', 'Contrast unitary evolution, measurement records and definite observed outcomes in an illustrative setup; compare stated interpretation assumptions without presenting one philosophical resolution as experimentally settled.', 'Quantum concepts and inference','advanced')],
 '008':[(10,'How can two savings goals require different liquidity even when their target dates match?', 'Compare uncertain spending windows, essential versus deferrable outlays, access restrictions and loss tolerance in fictional household scenarios; distinguish goal matching from product recommendations or a universal allocation percentage.', 'Goals and liquidity','intermediate')],
 '009':[(1,'How can seeking confirming evidence differ from refusing to update a belief after contrary evidence appears?', 'Contrast information selection, interpretation and later belief revision using a declared experimental design; control prior knowledge and information cost rather than labeling any disagreement irrational.', 'Evidence seeking and measurement','intermediate'),
 (10,'Why can a survey about a behavior disagree with a direct observation of that behavior?', 'Compare recall window, social desirability, observation setting, reactivity and what the two measures operationalize; use a low-stakes fictional example without equating disagreement with dishonesty.', 'Evidence seeking and measurement','intermediate')],
 '012':[(11,'How does a cosmological particle horizon differ from a black-hole event horizon?', 'Compare the past light signals reachable under a stated expansion model with the causal boundary of a black hole; distinguish observable extent, event horizons and a claim about the size of all space.', 'Cosmological horizons','advanced')],
 '013':[(4,'What can unfinished quarry faces reveal about an Egyptian stone-working sequence?', 'Compare tool traces, abandoned blocks, waste and site records with documented replica assumptions; distinguish extracting a block from transporting it or inferring a lost machine solely from precision.', 'Documented workshops and calculation','intermediate'),
 (5,'How can a Greek and an Arabic astronomical table be compared without assuming a simple copied lineage?', 'Select named editions and compare coordinate conventions, reference epochs, parameters, worked use and manuscript transmission; distinguish a shared mathematical task from proven direct borrowing.', 'Documented workshops and calculation','advanced'),
 (8,'What can a Mesopotamian mathematical tablet reveal about a calculation beyond its final number?', 'Read a published transcription with line order, notation, units and reconstruction limits; compare a worked problem and a tabular aid without treating a modern algebraic rewrite as the original procedure.', 'Documented workshops and calculation','intermediate')],
 '014':[(3,'How did changes in provincial authority alter one Ottoman region before the empire ended?', 'Choose a named province and bounded period, compare fiscal arrangements, appointments, local actors and imperial records; distinguish regional institutional transformation from a generic post-imperial breakup map.', 'Regional imperial transformations','intermediate')],
 '015':[(10,'What can a blinding check establish when participants recognize an intervention?', 'Compare treatment assignment, sensory differences, reported guesses, expectations and measured outcomes in a hypothetical controlled study; separate a plausible comparator from a guarantee that knowledge of assignment caused the result.', 'Controls and expectations','intermediate')],
 '018':[(8,'How can an epic animation signal a return to an earlier telling without changing what characters know?', 'Compare narrator cues, visual transitions, setting and knowledge continuity in an original storyboard based on a specified public passage; distinguish a flashback, a story told within a story and a simultaneous event.', 'Narrative time in adaptation','intermediate')],
 '021':[(8,'What can a leather bag inspection reveal about construction and future repair access?', 'Compare publicly documented seam design, panel joining, lining access, fittings and a repair assessment; distinguish visible finishing from material grade, durability claims or a guarantee of economical repair.', 'Construction and service life','intermediate')],
 '022':[(8,'Why can regenerative braking change its contribution during the same trip?', 'Trace battery acceptance limits, speed, traction, temperature and blending with friction brakes in a documented conceptual system; distinguish recovered energy from a promise of identical pedal feel or stopping distance.', 'Braking control and energy','intermediate')],
 '026':[(8,'How can treatment choice itself confound an observational comparison of patient outcomes?', 'Use a hypothetical clinic record to trace illness severity, prescribing decisions, follow-up and measured outcomes; compare stated adjustment assumptions with randomized assignment without interpreting a real patient or claiming adjustment removes every bias.', 'Study design and public reporting','advanced'),
 (12,'How can a case report identify a person even after their name and photograph are removed?', 'Compare the combined uniqueness of age, location, rare condition, dates and published biography in a fictional case; distinguish consent for clinical care from permission for an identifiable public narrative and avoid publishing real private details.', 'Study design and public reporting','intermediate')],
 '028':[(12,'How can repeated surveys distinguish vent-field succession from a change in where the vehicle looked?', 'Compare fixed locations, repeated imaging, chemical measurements, sampling intervals and detectability before and after a documented field change; distinguish ecological turnover from navigation drift and instrument changes.', 'Time series and sampling','advanced')],
 '031':[(8,'How can a remote construction project plan materials when its access route closes seasonally?', 'Compare delivery windows, storage limits, critical spares, alternate routes and schedule buffers in a fictional logistics plan; distinguish reliable supply from reducing every material choice to its purchase price.', 'Construction logistics','intermediate')],
 '032':[(4,'Why can radiation protection for spacecraft electronics require more than adding shielding?', 'Compare accumulated exposure, individual upset events, component selection, redundancy and error checks in a public documented design; distinguish instrument reliability from crew exposure or a universal safe shielding thickness.', 'Instrument reliability','intermediate')],
 '034':[(11,'Why can permission to enter a protected landscape differ from permission to collect or publish its research materials?', 'Map access, sampling, specimen transfer, community authority, recording and data-release permissions in a hypothetical research expedition; select actual jurisdiction and official rules later rather than supplying a transferable permit checklist.', 'Research access and accountability','intermediate')],
 '042':[(1,'How did a Mauryan pillar combine its physical setting, sculpted capital and inscription as different kinds of public statement?', 'Choose a documented monument and distinguish surviving placement evidence, text, visibility and attributed imagery; avoid assuming all pillars carried identical messages or that every viewer could read the inscription.', 'Objects and intended audiences','intermediate'),
 (3,'How can a Benin court object be read as a record of dynastic memory rather than a freestanding decorative image?', 'Choose an attributed object and compare its reported court setting, commemorative function, materials and oral or written interpretation; distinguish those questions from later collecting and repatriation claims.', 'Objects and intended audiences','intermediate'),
 (7,'What construction rules can organize a geometric ornament without fixing a single symbolic meaning?', 'Use a documented public architectural pattern to compare repeating units, symmetry, joins, surface constraints and workshop interpretation; separate observable geometry from an unsupported universal theological reading.', 'Objects and intended audiences','intermediate'),
 (8,'How can export porcelain show that makers designed an object for more than one cultural audience?', 'Compare a dated vessel group, form, motifs, commissioning records and consumption settings; distinguish demonstrated adaptation from resemblance or an assumed one-way transfer of taste.', 'Objects and intended audiences','intermediate')],
 '043':[(6,'How did segregated performance networks shape the work of jazz musicians in one city?', 'Choose a city and bounded period; compare venue access, bookings, travel, audiences, recording opportunities and attributed performer accounts without treating one musician as representative of every experience.', 'Institutions, audiences and recorded reuse','intermediate'),
 (7,'What changed when an opera institution depended on ticket buyers as well as court or elite patrons?', 'Compare funding, seating access, repertory, management and documented audience practices in a named house across a specified transition; avoid assuming that public tickets meant equal social access.', 'Institutions, audiences and recorded reuse','intermediate'),
 (10,'How did reusing a recorded sample change musical attribution compared with borrowing a tune in a new performance?', 'Trace one later-selected recording pair through credited composition, recorded performance, production and documented permissions; distinguish sonic reuse, musical influence and jurisdiction-specific rights questions without inventing a legal result.', 'Institutions, audiences and recorded reuse','intermediate')],
 '044':[(5,'What changed when an event replaced hand timing with an automatic timing system?', 'Compare the start signal, measured finish, precision, calibration and governing rules in a dated event; distinguish additional decimal places from directly comparable performances.', 'Records and missing populations','intermediate'),
 (12,'What can a formal sporting record omit about competitions held outside the recognized governing body?', 'Compare entry eligibility, local archives, informal contests, reporting practices and the definition of an official result; keep unrecorded performance distinct from a proven record claim.', 'Records and missing populations','intermediate')],
 '045':[(4,'Why can pack racing on a banked oval create different information and coordination demands from a road circuit?', 'Compare track geometry, airflow interaction, traffic, caution procedures and public race records at a documentary level; exclude driving tactics or guidance for hazardous imitation.', 'Racing systems and institutions','intermediate'),
 (8,"How can a development driver's opportunity depend on funding and testing access as well as lap time?", "Trace a named program or fictional career through entry costs, sponsorship, eligibility, seat availability and observed evaluation; do not infer a driver's competence or family wealth from a seat announcement.", 'Racing systems and institutions','intermediate'),
 (10,'How did changes in racing telemetry alter which decisions teams could make from the pit wall?', 'Choose a dated series and compare publicly documented sensors, transmission, logging, regulations and engineering roles; distinguish historical capabilities from private live race data.', 'Racing systems and institutions','intermediate'),
 (11,'How did a particular woman driver navigate an institution that controlled entry, equipment and race licenses?', 'Select a documented career and period with the driver\'s attributed accounts, rules, sponsorship and results; separate institutional barriers from stereotypes about ability or one universal experience.', 'Racing systems and institutions','intermediate')],
}


ADDITIONS['039']=[
 (8,'Why can an isotope match for an archaeological metal fail to identify its trade route?', 'Compare ore-source baselines, overlapping signatures, recycling, mixing and find contexts in a published object study chosen later; distinguish material origin from the places or intermediaries through which an object moved.', 'Provenance and detection limits','advanced'),
 (12,'When can a failure to find an expected artifact challenge an archaeological hypothesis?', 'Compare survey coverage, recovery method, preservation, expected abundance and explicit competing predictions; distinguish an informative nondetection from the absence of systematic investigation.', 'Provenance and detection limits','intermediate')]
ADDITIONS['044'].append((11,"How can a regional champion's career be reconstructed when national databases omit the competition?", "Compare club minutes, local newspapers, dated result sheets, oral accounts and the competition's eligibility rules; distinguish a documented regional achievement from an unverified national or world-record claim.", 'Records and missing populations','intermediate'))
ADDITIONS['045'].append((9,'How can a motorsport barrier manage collision energy differently from a rigid wall?', "Compare a documented design's deformation, loads, tested impact conditions and site constraints at an explanatory level; no construction specification, safety certification or instructions for real-track modification.", 'Racing systems and institutions','intermediate'))


def apply():
    payload={}
    for nid,entries in ADDITIONS.items():
        b=m.read(m.home(nid)/'IN_DEPTH_TOPIC_BANK.json');parent=b['parent_categories'][0]['title']
        groups={}
        for starter,q,scope,title,level in entries:
            key=(title,level)
            g=groups.setdefault(key,{'parent':parent,'title':title,'level':level,'topics':[]})
            g['topics'].append({'question':q,'coverage':scope,'covers_starter_ids':[f'BANK-{nid}-{starter:03d}'],'origin':'editorial_starter_scope_review'})
        payload[nid]=list(groups.values())
    m.write(ROOT/'Scripts/editorial_starter_gap_additions_002_050.json',payload)
    if payload:m.apply(ROOT/'Scripts/editorial_starter_gap_additions_002_050.json')
    audit={}
    for nid,cells in MAPS.items():
        p=m.home(nid)/'IN_DEPTH_TOPIC_BANK.json';b=m.read(p)
        starters=[t for c in b['prior_initial_map']['categories'] for t in c['topics']]
        choices=cells.split(',');assert len(choices)==len(starters),(nid,len(choices),len(starters))
        for old,choice in zip(starters,choices):
            if choice=='new':assert b['starter_concept_crosswalk'].get(old['id']),(nid,old);continue
            refs=[]
            for item in choice.split('+'):
                other,number=item.split(':') if ':' in item else (nid,item)
                refs.append(f'BANK-{other}-{int(number):03d}')
            b.setdefault('starter_concept_crosswalk',{})[old['id']]=refs
        evidence=[]
        for old in starters:
            refs=b['starter_concept_crosswalk'][old['id']];targets=[]
            for ref in refs:
                rb=b if ref.split('-')[1]==nid else m.read(m.home(ref.split('-')[1])/'IN_DEPTH_TOPIC_BANK.json')
                actual=next(t for c,t in m.records(rb) if t['id']==ref)
                targets.append({'id':ref,'question':actual['question'],'coverage':actual['coverage']})
            evidence.append({'starter_id':old['id'],'title':old['title'],'target_ids':refs,'target_evidence':targets,
                'decision':'added_missing_scope' if old['id'] in {f'BANK-{nid}-{e[0]:03d}' for e in ADDITIONS.get(nid,[])} else 'existing_scope_or_combined_subquestions',
                'reason':'Manual subject-and-scope comparison; the linked individual scopes collectively bound this starter subject. Cases, dates, versions, editions and sources still require selection; this is not factual verification.'})
        errors=m.check_bank(b,p.parent);assert not errors,errors
        m.write(p,b)
        audit[nid]={'starter_decisions':evidence,'original_starter_count':len(starters),'read_question_and_scope':True}
    m.write(ROOT/'Scripts/editorial_starters_002_050.json',{'status':'in_progress' if len(audit)<49 else 'review_complete','banks':audit})
    print(f'Saved manual starter evidence for {len(audit)} banks.')


if __name__=='__main__':apply()
