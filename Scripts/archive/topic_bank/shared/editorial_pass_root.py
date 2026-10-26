from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Authored second-pass proposals and explicit scope review for 001 and 281 only."""
import copy
import json
from pathlib import Path
import manage_all_topic_banks as allbanks
import manage_ai_topics as ai

ROOT=Path(__file__).resolve().parents[4]


def topic(question,coverage):
    return {'question':question,'coverage':coverage}


def group(parent,title,level,profile,items):
    return {'parent':parent,'title':title,'level':level,'research_profile':profile,
            'topics':[topic(q,s) for q,s in items]}


AI_GROUPS=[
    group('Learning, representations and causal questions','Learning with scarce feedback','intermediate','technical',[
        ('What does principal-component analysis preserve when it reduces a dataset to fewer dimensions?',
         'Follow centered synthetic features, variance directions, projection and reconstruction loss; distinguish a visually separated projection from validated classes or causal factors.'),
        ('How can active learning choose which examples a person should label next?',
         'Compare uncertainty sampling, diversity and a random-label baseline at a fixed annotation budget; examine biased sampling and an independent test set.'),
        ('Why does a contextual bandit need to explore options that currently look worse?',
         'Trace actions, partial feedback, exploration cost and regret in a fictional recommendation task; distinguish one-step feedback from multi-step reinforcement learning.'),
        ('What does knowledge distillation transfer from a teacher model to a smaller student?',
         'Compare training targets, student capacity, matched-task outcomes and inherited errors; distinguish learning from teacher outputs from reducing the bit width of unchanged weights.'),
        ('How can a low-rank adapter change a model without updating every stored weight?',
         'Illustrate a weight update as a product of smaller matrices; separate trainable parameters, retained base weights and task evaluation from a tutorial or universal memory promise.'),
    ]),
    group('Data provenance, language and access','Scripts and cross-language retrieval','intermediate','technical',[
        ('Why can visually identical text have different character sequences in an AI dataset?',
         'Compare composed and combining-character forms, normalization and span offsets with a declared Unicode sample; inspect matching and annotation errors rather than infer meaning from byte equality.'),
        ('How can transliterated names prevent a document search from finding the right source?',
         'Compare native-script, Romanized and variant-spelling queries for a consented or fictional entity; distinguish entity resolution and retrieval recall from the quality of a generated translation.'),
        ('How can a tokenizer comparison separate morphological structure from the length of a written word?',
         'Use qualified annotations for a declared language pair with different word-formation patterns; inspect segmentation, length-normalized task errors and vocabulary coverage without ranking languages as intrinsically harder.'),
    ]),
    group('Retrieval, tools and deployed systems','Search selection and lifecycle controls','advanced','technical',[
        ('What does a reranker decide after a document retriever has already selected candidates?',
         'Trace candidate generation, relevance scores, ordering and missing-candidate limits in a small controlled collection; evaluate retrieval recall separately from reranking precision and final answer support.'),
        ('What must an application retire when a model endpoint is withdrawn?',
         'Map versioned prompts, evaluation baselines, dependent tools, stored embeddings and fallback behavior in a hypothetical migration; separate replacing a service from disposing of physical hardware.'),
        ('How does abstaining change the relationship between model accuracy and the number of requests answered?',
         'Plot a risk-coverage tradeoff on labeled synthetic predictions as a declared threshold varies; include subgroup coverage and decision costs rather than equating fewer answers with a safer system.'),
    ]),
    group('Applied AI, robotics and scientific systems','Longitudinal deployment and changing users','advanced','synthesis',[
        ('How can an AI evaluation distinguish initial novelty from a lasting change in how people perform a task?',
         'Plan repeated baseline and follow-up observations, learning effects, participant attrition and task substitution in a hypothetical low-stakes deployment; distinguish a longitudinal outcome from a one-session productivity comparison.'),
        ('Why can a personalized assistant become less useful when a household or team changes?',
         'Trace shared versus individual preferences, consent to stored history, stale assumptions and re-evaluation after membership changes using fictional records; distinguish application memory governance from retraining model weights.'),
    ]),
]


AYUR_GROUPS=[
    group('Classical frameworks and textual interpretation','Missing foundational distinctions','foundation','tradition',[
        ('What role do the five mahabhutas play in an attributed Ayurvedic explanation?',
         'Read one source classification and its stated explanatory purpose; distinguish the five-element vocabulary from chemical elements, measurable substances or a modern periodic table.'),
        ('What are the three malas classifying in a named Ayurvedic text?',
         'Compare the attributed categories, examples and translation choices; separate textual descriptions of waste from a modern diagnostic test or a detoxification prescription.'),
        ('How does a classical definition of swasthya connect bodily function, experience and social ideals?',
         'Compare one attributed passage with its translation and intended context; distinguish a normative definition of wellbeing from a measured population-health outcome.'),
        ('What does prabhava add when a text classifies a substance using rasa, guna, virya and vipaka?',
         'Read a bounded example in a named edition and expose the explanatory role assigned to exceptional action; do not turn a textual explanation into a proven pharmacological mechanism.'),
        ('How does rasayana function as a traditional category rather than a measurable promise to reverse ageing?',
         'Compare attributed aims, intended audiences and textual contexts with the endpoints a later longevity claim would need; no rejuvenation regimen or efficacy conclusion.'),
        ('What can a short dosha questionnaire omit about how a practitioner records a case?',
         'Compare questionnaire items, self-report, classification agreement and contextual assessment using a fictional example; distinguish an educational quiz from validated diagnosis or prediction.'),
    ]),
    group('Botanical identity and material quality','Named materials beyond generic herb profiles','intermediate','health',[
        ('How can a Tulsi documentary separate sacred household relationships from a commercial ingredient identity?',
         'Compare an attributed household account, a botanist-authenticated specimen and a product declaration; retain regional naming differences and distinguish cultural significance from clinical evidence.'),
        ('What changes when Amla is discussed as a fresh fruit, a dried ingredient and a sweetened preparation?',
         'Compare material, carrier ingredients, processing and the denominator used for composition claims; do not transfer a nutrition measurement or trial outcome across unlike products.'),
        ('What evidence links a Shatavari product to the root material named in its study?',
         'Trace a voucher, reported plant part, microscopic description and batch identity; distinguish raw-material authentication from a reproductive-health or lactation claim.'),
        ('What do Haritaki market grades describe, and how can they be distinguished from species identity?',
         'Compare attributed trade classifications, specimen descriptions and the terms used in a chosen source; do not assume that a named grade establishes chemical potency or clinical superiority.'),
        ('How can a red dye obtained from a Manjistha material tell a different story from a blood-purification claim?',
         'Trace an attributed material-and-craft history, botanical authentication and the evidence required for a separate physiological claim; no extraction recipe or unverified therapeutic conclusion.'),
        ('What must a Bhringraj hair-oil study separate about the plant extract and the carrier oil?',
         'Compare ingredient declaration, carrier-only comparison, hair-shaft versus scalp endpoints and follow-up; distinguish a cosmetic observation from evidence of treating a cause of hair loss.'),
        ('Why should an Aloe gel, leaf latex and whole-leaf product not be treated as one study material?',
         'Compare the named fractions, processing, constituent reporting and route of exposure in identified records; provide no ingestion instructions or product safety assurance.'),
        ('What information is lost when a compounded hing product is described simply as a resin?',
         'Compare a declared resin source with carriers, mixture labels, sampling and analytical identity; distinguish a household spice mixture from a purified research material.'),
        ('How can a piperine bioavailability claim be separated from ordinary black-pepper use?',
         'Read exact formulation, co-administered material, exposure measure and study population as identification fields; exclude advice to combine supplements or alter medicines.'),
        ('What makes an essential oil a different exposure from a herb-infused oil?',
         'Compare stated extraction, carrier, constituent concentration and route in hypothetical labels; distinguish both from eating the original culinary ingredient without giving application or dilution instructions.'),
    ]),
    group('Preparations and formulations','Food, carriers and preparation categories','foundation','tradition',[
        ('How do manda, peya and yavagu name distinct rice preparations in an attributed source?',
         'Compare the described consistency, preparation category and intended textual context; keep a historical food explanation separate from a therapeutic diet or recipe prescription.'),
        ('What changes when curd is processed into the preparation called takra in a chosen account?',
         'Compare source terminology, ingredient and process descriptions with a clearly identified household food; do not assume every modern buttermilk product matches the historical material.'),
        ('How are phanta and hima distinguished from kwatha in a preparation classification?',
         'Compare attributed solvent, temperature category and source purpose without giving quantities, preparation instructions or claims that one method treats a condition better.'),
        ('What does an avaleha base contribute to the identity of a Chyawanprash product?',
         'Compare a named textual formulation, disclosed carriers and ingredient variation on two hypothetical labels; distinguish food-like presentation, formulation identity and demonstrated clinical benefit.'),
        ('How do a three-ingredient group such as Trikatu and a group such as Dashamoola organize different kinds of material?',
         'Use attributed ingredient lists to compare grouping logic, botanical parts and naming uncertainty; no assertion that shared group membership establishes interchangeable products or effects.'),
        ('Why does a claim about an Ayurvedic food combination need to identify what viruddha means in its source?',
         'Compare the source context, classification and exact modern outcome claimed; distinguish a textual incompatibility category from measured food allergy, contamination or clinical causation.'),
        ('What can a turmeric-milk recipe establish without proving a claim about immunity?',
         'Compare culinary variation, ingredient quantities as historical description, the meaning of an advertised outcome and the need for matched human evidence; no benefit promise or medicinal recipe.'),
        ('How can seasonal recipe adaptations preserve a food tradition without claiming a universal therapeutic menu?',
         'Compare two attributed regional khichdi or leaf-dish accounts, local ingredients, labor and adaptation for a workday; keep culinary choices distinct from condition-specific nutrition guidance.'),
    ]),
    group('Practice frameworks','Daily life, supervision and patient experience','intermediate','tradition',[
        ('How is nidra situated alongside food and daily conduct in an attributed Ayurvedic source?',
         'Read a bounded passage and its intended audience; distinguish a traditional account of sleep from a modern diagnosis of insomnia or evidence for a supplement.'),
        ('What can a text mean by individual capacity when it discusses exercise?',
         'Compare attributed context, audience and seasonal assumptions with questions a later exercise evaluation would ask; provide no exercise dose, medical clearance or universal capacity test.'),
        ('How can an oil-pulling claim distinguish a mouth-health endpoint from a whole-body detoxification claim?',
         'Identify the practice named, material and comparison in a proposed study review; separate measured local endpoints, subjective experience and unsupported systemic extrapolation without technique instructions.'),
        ('What does a description of shirodhara need to separate about ritual setting, participant experience and clinical outcomes?',
         'Compare attributed practitioner accounts, contextual factors, comparison conditions and follow-up in a future study review; no procedural instructions or therapeutic endorsement.'),
        ('How are vamana, virechana, basti, nasya and raktamokshana distinguished as source categories?',
         'Use one named source and qualified historical review to compare the categories, attributed purposes and supervision context; no operational steps, substances, quantities or self-treatment instructions.'),
        ('What should an account of treatment consent reveal beyond a signed form?',
         'Map disclosed uncertainty, alternatives, ability to decline, hygiene accountability, follow-up and qualified responsibilities in a fictional traditional-care service; select a jurisdiction before making legal claims.'),
        ('How do descriptions of ritusandhi frame change between seasons rather than six isolated routine lists?',
         'Read an attributed transition passage alongside a declared local calendar; distinguish historical adaptation language from a demonstrated disease-prevention rule.'),
    ]),
    group('Research literacy and comparative evidence','Population, measurement and preparation matching','advanced','health',[
        ('What would show that a translated symptom questionnaire measures the same outcome in two trial populations?',
         'Compare item meaning, translation process, measurement equivalence, participant interpretation and prespecified meaningful-change criteria in a hypothetical herbal trial; distinguish valid measurement from a statistically significant average.'),
        ('Why can an adult herbal trial leave a pregnancy, breastfeeding or childhood claim unanswered?',
         'Inspect inclusion criteria, the exact preparation, exposure route and outcomes studied; define the missing population evidence without extrapolating safety or recommending personal use.'),
        ('How can a fertility advertisement move from a laboratory marker to a claim about having a child?',
         'Separate measured hormones or other surrogate outcomes, conception, live birth, follow-up and co-interventions in hypothetical study descriptions; no inference that one supplement treats infertility.'),
        ('What must a PCOS or menopause supplement claim specify before trials can be compared?',
         'Require a defined population, the particular symptom or clinical endpoint, comparator, preparation and follow-up; keep distinct conditions and outcomes separate rather than promising a whole-condition cure.'),
        ('How can a microbiome change be reported without proving relief of a digestive disorder?',
         'Distinguish assay, microbial endpoint, symptom measure, comparator and causal interpretation in a hypothetical herbal study; do not infer that any microbiome change is beneficial.'),
        ('What does standardization to one marker leave unknown about a multi-component extract?',
         'Compare the marker specification, full composition reporting, batch sampling and clinical material match; separate analytical consistency from proof that the marker produces the claimed outcome.'),
        ('Why can a longevity study of an organism fail to establish longer healthy lives for people?',
         'Compare species, exposure, lifespan versus healthspan endpoints and human applicability; use later identified primary studies and avoid turning a laboratory observation into an anti-ageing promise.'),
    ]),
    group('Safety, surveillance and product accountability','Claims, reporting and vulnerable contexts','intermediate','health',[
        ('What information would help a qualified safety service evaluate a suspected reaction to a multi-ingredient product?',
         'Map a fictional report with product/batch identity, exposure timeline, concurrent medicines and available records; distinguish public reporting from diagnosis, causality assessment or an estimated reaction rate.'),
        ('Why does a polypharmacy review need the full supplement list rather than one advertised herb?',
         'Compare ingredient disclosure, multiple concurrent products, timing and uncertain interaction evidence in fictional documentation for a qualified reviewer; no advice to start, stop or combine medicines.'),
        ('How can an immunity-booster or permanent-cure advertisement be made specific enough to assess?',
         'Require a defined condition or endpoint, population, time horizon, exact product and comparison; separate an undefined promotional phrase from a claim with testable criteria.'),
        ("What must a copper-vessel water claim distinguish about antimicrobial testing and a person's actual exposure?",
         'Separate laboratory conditions, released material, storage context and measured human outcomes as future evidence questions; no home test, safe limit or health-use recommendation.'),
        ('What does a castor-oil pack or navel-oiling claim need to demonstrate beyond absorption imagery?',
         'Trace the claimed route, measured exposure, outcome and comparison in a proposed evidence review; distinguish an illustration or tradition account from a demonstrated mechanism or benefit.'),
        ('How can an autophagy claim in fasting marketing be separated from evidence about an Ayurvedic regimen?',
         'Compare the source term langhana, the exact intervention, biomarker measurement and claimed human outcome; avoid treating shared vocabulary as proof or supplying a fasting plan.'),
    ]),
    group('History, institutions and respectful communication','Texts, institutions and material fieldwork','intermediate','history',[
        ('How do Ashtanga Sangraha and Ashtanga Hridaya organize comparable material in selected editions?',
         'Compare a bounded pair of passages, arrangement and commentary apparatus; record attribution and dating uncertainty without claiming a simple author-to-author progression.'),
        ('How does an organizing passage in Madhava Nidana differ in purpose from one in Sharangadhara Samhita?',
         'Compare the selected texts structure and intended knowledge tasks in named editions; avoid reconstructing treatment instructions or assuming one universal curriculum.'),
        ('What can a Bhavaprakasha entry reveal about the history of materia-medica classification?',
         'Trace a chosen entry through attributed names, grouping, commentary and later identification; separate textual history from authentication of a modern jar.'),
        ('How has the figure of Dhanvantari been represented in a particular temple, image or institutional setting?',
         'Choose attributed visual and textual records and distinguish religious meaning, institutional symbolism and historical claims; no universal chronology or claim that iconography proves medical efficacy.'),
        ('How did a particular colonial-period educational policy change the teaching of Ayurveda?',
         'Select a dated institution and compare policy text, curricula, language and practitioner responses; preserve regional disagreement and distinguish official policy from lived implementation.'),
        ('What can a filmed herb-drying facility reveal that a finished-product label cannot?',
         'Trace batch identity, storage records, measured process conditions and sampling limits in a permissioned observational case; distinguish recorded practice from certification or proof of uncontaminated output.'),
        ('How can cultivation and wild collection create different questions of tenure and benefit sharing?',
         'Compare a named supply-chain case through land access, labor, consent, harvest records and conservation evidence; do not treat cultivated as automatically sustainable or provide collection instructions.'),
    ]),
]


def update_ai():
    b=ai.load(ai.HOME/'IN_DEPTH_TOPIC_BANK.json');s=ai.load(ai.HOME/'topics_status.json')
    original_ids=[t['id'] for c,t in ai.topics(b)]
    parents={p['title']:p['id'] for p in b['parent_categories']}
    next_id=max(int(t['id'].split('-')[-1]) for c,t in ai.topics(b))+1
    cats={c['title']:c for c in b['categories']}
    for g in AI_GROUPS:
        if g['title'] not in cats:
            used={c['id'] for c in b['categories']};number=1
            while f'CATALOG-001-E{number:02d}' in used:number+=1
            profile=g['research_profile'] if g['research_profile'] in b['research_profiles'] else 'technical'
            c={'id':f'CATALOG-001-E{number:02d}','title':g['title'],'level':g['level'],
               'research_profile':profile,'parent_id':parents[g['parent']],'prerequisites':[], 'topics':[]}
            b['categories'].append(c);cats[g['title']]=c;b['reading_paths'][g['level']].append(c['id'])
        c=cats[g['title']]
        for t in g['topics']:
            if any(ai.normalize(t['question'])==ai.normalize(old['question']) for _,old in ai.topics(b)):continue
            c['topics'].append(dict(t,id=f'BANK-001-{next_id:03d}',angle=None,status='proposed',verified_sources=[],origin='editorial_second_pass'));next_id+=1
    mappings=[[13,14],[136,18,20],[157,17,28],[23,24,27],[33,34,125],[29,154],[26,36,123],[92,111,35],[38,39,44],[19,22,52],[15,173,169],[49,203,204,206]]
    b['starter_concept_crosswalk']={f'BANK-001-{i:03d}':[f'BANK-001-{n:03d}' for n in refs] for i,refs in enumerate(mappings,1)}
    b['editorial_review']={'summary':'Reviewed all existing questions and scopes, all twelve starter subjects and every prior gap. Added scarce-feedback learning, script handling, retrieval selection and longitudinal lifecycle questions; retained existing explanatory boundaries and separated case/source selection from missing subject branches.', 'audit_file':'Scripts/editorial_review_root.json'}
    byid={t['id']:t for c,t in ai.topics(b)}
    byid['BANK-001-193']['additional_scope']='This is a machine-translation explainer: compare model outputs and context sensitivity under a declared model version. The human translator purpose/register problem has its primary home in niche 529; neither episode should repeat the other as a general idiom list.'
    b['open_coverage']=[
        {'area':'Language and script cases','next_step':'The added normalization, transliteration and morphology questions cover distinct missing mechanisms. Select qualified language reviewers and declared datasets; dialect speech and accessibility remain in 068, 103 and 133 rather than cloned language-name episodes.'},
        {'area':'Versioned cases and regional institutions','next_step':'Select systems, dates, facilities, jurisdictions and participant groups within the existing energy, rights and deployment questions. Add a new proposal only when the case changes the mechanism, decision or outcome question.'},
        {'area':'Frontier and longitudinal evidence','next_step':'Memory, adaptation, reasoning and physical learning already have active questions. Evaluate newly documented mechanisms and longer-term deployment outcomes as evidence becomes available; a product launch alone does not warrant another episode.'},
        {'area':'Research and production readiness','next_step':'All questions remain proposals requiring actual source discovery, case selection, registered-angle review and claim work. Existing registry IDEA readiness remains unchanged.'},
    ]
    b['counts']=ai.totals(b)
    s['catalog_summary']={'active_proposals':b['counts']['proposed_topics'],'categories':len(b['parent_categories']),'subcategories':len(b['categories']),'archived_starters':12,'legacy_references':27}
    errors,_=ai.validate(b,s,check_views=False)
    assert not errors,errors
    allbanks.write(ai.HOME/'IN_DEPTH_TOPIC_BANK.json',b);allbanks.write(ai.HOME/'topics_status.json',s)
    for p,content in ai.reading_views(b,s).items():allbanks.save_bytes(p,content.encode('utf-8'))
    return b,original_ids


if __name__=='__main__':
    audit=ROOT/'Scripts/editorial_review_root.json'
    if not audit.exists():
        allbanks.write(audit,{'status':'in_progress','owned_niches':['001','281'],'source_verification':'not_performed'})
    allbanks.write(ROOT/'Scripts/editorial_pass_001.json',{'001':AI_GROUPS})
    allbanks.write(ROOT/'Scripts/editorial_pass_281.json',{'281':AYUR_GROUPS})
    b,original_ids=update_ai()
    allbanks.apply(ROOT/'Scripts/editorial_pass_281.json')
    print(f'001 now {b["counts"]["proposed_topics"]} proposals; {len(original_ids)} original active records retained.')
