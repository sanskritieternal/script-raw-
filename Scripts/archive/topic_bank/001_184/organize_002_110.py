import json
from pathlib import Path
DATA=r'''
002|Evidence and historical method:1,6,7,8,16,18,22|People, expeditions and political mysteries:2,10,11,12,21|Places, texts and material identifications:3,4,9,13,15,19,20|Environment, abandonment and community memory:5,14,17
003|Sources, methods and transmission:1,12,20,23,25,26,27,28|Regional worlds and chronological change:2,3,4,5,6,7,8,9,13,14,15,22,24|Institutions, households and exchange:10,11,16,17,18,19,21
004|Sources and interpretive methods:1,7,9,17,19,20|Cosmology, deities and divine relationships:2,3,4,5,6,12,13,14,15,16,21|Epic narrative worlds:10,11,22,23|Living retellings, images and observance:8,18,24,25
005|Development, questions and research:1,2,9,10,18|Fieldwork, contributors and recording:3,4,11,12,16,21|Archive, form and editing:5,6,7,13,14,15,19,22|Release, rights and accountability:8,17,20,23
006|Scientific reasoning and limits:1,16,18,20,23|Physical laws and cosmic questions:2,3,4,9,10,11,19|Living systems and cognition:5,6,7,14,17,22|Earth, materials and planetary systems:8,12,13,15,21
007|Tool choice, local setup and maintenance:1,8,9,10,16,17,20|Documents, data and retrieval:2,7,11,12,18|Creative media workflows:3,4,5,13,19|Code, automation and inclusive validation:6,14,15,21
008|Household cash flow and life transitions:1,2,13,15,16,18,19,23|Banking, consumer protection and taxes:3,8,9,10,17,20,21,22|Saving, investments and retirement:4,5,7,11,12|Insurance and risk transfer:6,14
009|Cognition, learning and decisions:1,2,3,4,10,13,21|Social worlds and applied behavior:5,6,11,12,15,16,23|Emotion, development and clinical literacy:7,9,14,17,22|Measurement, theory and responsible explanation:8,18,19,20,24
010|Records, testimony and evidence interpretation:1,2,3,4,5,6,13,14,20|Case dossiers and justice institutions:9,10,11,12,18,19,21|Contributors, representation and accountability:7,8,15,16,17,22,23
011|Characters, rules and original premises:1,2,3|Clues, atmosphere and story structure:4,5,7|Traditions, audiences and responsible adaptation:6,8
012|Observation and inference:1,8|Stars, galaxies and planetary systems:2,3,4,5|Cosmic history and unseen components:6,7
013|Evidence, experiments and historical claims:1,7,8|Materials, mechanisms and infrastructure:2,3,4|Knowledge systems and transmission:5,6
014|States, territory and historical context:1,2,6|Infrastructure, commerce and environments:3,4,5|Evidence and public explanation:7,8
015|Health evidence and public communication:1,7,8|Prevention and everyday health contexts:2,3,4,5,6
016|Achievement, setbacks and human choices:1,2,3,4|Attribution, storytelling and audience effects:5,6,7,8
017|Characters, problems and social life:1,2,3|Structure, visuals and language:4,5,6|Learning claims and series stewardship:7,8
018|Sources, narrative and visual identity:1,2,3|Performance, assets and sound:4,5,6|Audience care and editorial review:7,8
019|Story, shots and visual worlds:1,2,3,4|Generation, sound and finishing:5,6,7|Rights and production documentation:8
020|Place questions and field research:1,2,3|Communities, access and conservation:4,6,7|Visual reporting and story updates:5,8
021|Meaning, craft and high-cost goods:1,4,5|Assets, services and recurring obligations:2,3,6|Markets and cultural interpretation:7,8
022|Automotive evidence and histories:1,6,8|Powertrains, dynamics and packaging:2,3,4|Safety, ownership and repair:5,7
023|Practices, traditions and experience:1,3,4,7|Authority, community and commerce:2,5,6|Documentary interpretation and responsibility:8
024|History, exchange and household knowledge:1,2,3|Ritual, ingredients and public food:4,5,6|Representation and production methods:7,8
025|Canon, worlds and player agency:1,3,4,5|Environmental and audiovisual storytelling:2,6|Communities and responsible episodes:7,8
026|Medical evidence and care institutions:1,6,7,8|Physiological systems and repair:2,3,4,5
027|Inheritance, regulation and genomic methods:1,2,7|Evolutionary processes and evidence:3,4,6|Complex traits and public interpretation:5,8
028|Deep-ocean habitats and life:1,2,3|Vehicles, sampling and observation:4,5,7|Human disturbance and explanation:6,8
029|Fossil evidence and reconstruction:1,2,3|Ecology, behavior and changing worlds:4,5,6|Extinction and public interpretation:7,8
030|Investigation and extraordinary claims:1,6,7,8|Land, water and atmospheric processes:2,3,4,5
031|Structures and engineering constraints:1,2,3,4,5|Construction, institutions and lifecycle:6,7,8
032|Mission design, journeys and surface work:1,2,3,4|Operations, history and protected environments:5,6,7|Economics and public interpretation:8
033|Observation, testimony and claim quality:1,2,3,4|Astrobiology and technosignatures:5,6|Institutions and documentary standards:7,8
034|Expedition questions and historical records:1,2,3|Logistics, environments and local knowledge:4,5,6|Outcomes and modern interpretation:7,8
035|Military sources and changing technologies:1,2,3|Command, logistics and civilian worlds:4,5,6|Memory, representation and method:7,8
036|Sources, comparative institutions and queenship:1,16,17|Early imperial and regional formations:2,3,4,5,6,7,8,9|Sultanates, imperial courts and later powers:10,11,12,13,14,15
037|Sites, fortifications and royal spaces:1,2,3,4|Households, conservation and living use:5,6|Tourism and reconstruction:7,8
038|Maps, borders and historical models:1,2,5|Oceans, rivers and remote observation:3,4,6|Records, claims and visual explanation:7,8
039|Questions, excavation and dating:1,2,3|Survey, materials and social inference:4,5,6|Stewardship and public interpretation:7,8
040|Manuscript materials, production and reading:1,2,3|Textual criticism and recovered writing:4,5|Digital access, ownership and interpretation:6,7,8
041|Language evidence and linguistic structure:1,2,3,4|Histories, multilingual lives and revitalization:5,6,7|Myths and digital tools:8
042|Art objects, materials and institutions:1,3,4|Regional arts, exchange and everyday making:2,5,6|Conservation, ownership and interpretation:7,8
043|Musical evidence, instruments and listening:1,3,8|Traditions, labor and cultural exchange:2,4,5|Industries, preservation and attribution:6,7
044|Historical sources and sporting institutions:1,2,3|Access, equipment and performance:4,5|Business, integrity and public memory:6,7,8
045|Disciplines, vehicles and powertrains:1,2,3|Strategies, participants and safety:4,5,6|Business, data and contested narratives:7,8
046|Risk and disaster mechanisms:1,2,3,4|Warning, response and survivor accounts:5,6|Recovery, evidence and public memory:7,8
047|Flight, design and navigation:1,2,3|Safety, human work and airline systems:4,5,6|Wider histories and environmental claims:7,8
048|Evidence, routes and maritime technology:1,2,3|Work, ports, trade and coercion:4,5,6|Wrecks, heritage and ocean change:7,8
049|Sources, piracy and named lives:1,2,3,4|Land outlaws, policing and punishment:5,6|Memory and responsible comparison:7,8
050|Claims, archives and material contexts:1,2,3,4|Legends, hoaxes and incentives:5,6|Heritage, permissions and conclusions:7,8
051|Products, materials and precision processes:1,2,3,4|Assembly, quality and supply chains:5,6,7|Environmental and historical legacies:8
052|Buildings, histories and construction:1,2,3|Climate, housing and public institutions:4,5,6|Reuse, conservation and criticism:7,8
053|Scenarios, resources and settlements:1,2,3,6|Institutions, culture and work:4,5|Resilience and critical evaluation:7,8
054|Concepts, mind theories and experience:1,2,3,4|Philosophical traditions and knowledge:5,6|Other minds and ethical interpretation:7,8
055|Time measurement and physical theories:1,2,3,4|Cosmology, philosophy and causality:5,6,7|Perception and public claims:8
056|Puzzle structure, logic and probability:1,2,3|Mathematics, decipherment and unresolved questions:4,5,6|Solving tools and fair presentation:7,8
057|Secrecy, organizations and historical networks:1,2,3,4,5|Symbols, hidden-power claims and documentary ethics:6,7,8
058|Living traditions and narrative comparison:1,2,3,4|Places, archives and modern circulation:5,6,7|Adaptation and interpretive responsibility:8
059|Creature sources, bodies and environments:1,2,3,4|Material culture, social boundaries and new lore:5,6,7|Evidence and visual reconstruction:8
060|Context, sacred imagery and material meanings:1,2,3|Writing, heraldry and architecture:4,5,6|Digital symbols and responsible interpretation:7,8
061|Execution, design and computational structures:1,2,3|State, services and test evidence:4,5,6|Security, delivery and learning paths:7,8,9
062|Computer systems, compute and storage:1,2,3|Power, operating systems and connections:4,5,6|Workloads, access and lifecycle:7,8
063|Connected devices, media and energy:1,2,3,4|Accounts, support and practical ownership:5,6|Reviews, access and environmental claims:7,8
064|Household space, cleaning and domestic work:1,2,3|Comfort, transitions and accessibility:4,5,6|Maintenance and consumption narratives:7,8
065|Plant observation, soils and establishment:1,2,3|Food growing, pests and perennial design:4,5,6|Containers, climate and accessible practice:7,8,9
066|Animal observation, bodies and ecology:1,2,3|Development, communication and movement:4,5,6|Conservation, welfare and wildlife media:7,8
067|Questions, fieldwork and ecosystems:1,2,3|Capture, evidence and human relationships:4,5,6|Rights, audiences and editorial comparison:7,8
068|Choosing animals and daily welfare:1,2,3|Learning, handling and health literacy:4,5,6|Aging, ownership and public life:7,8
069|Learning, memory and curriculum:1,2,3|Teaching, assessment and core skills:4,5,6|Inclusion, technology and policy evidence:7,8
070|Occupations, skills and applications:1,2,3|Hiring, work arrangements and development:4,5,6|Transitions, access and long-term choices:7,8
071|Capacity, attention and habits:1,2,3|Motivation, tools and reflective practice:4,5,6|Rest, values and evaluation:7,8
072|Context, communication and autonomy:1,2,3|Conflict, social life and transitions:4,5,6|Harm, support and endings:7,8
073|Development, infancy and early learning:1,2,3|Routines, school and adolescence:4,5,6|Disability, resources and family-media ethics:7,8
074|Trip design, bookings and routes:1,2,3|Logistics, traveler needs and contingencies:4,5,6|Local relationships and reflective records:7,8
075|Sacred geographies and journey traditions:1,2,3,5,6|Shrine practice, accessibility and conservation:4,7,8|Media and environmental responsibility:9
076|Studying religion and regional traditions:1,2,3,4,5|Institutions, encounter and pluralism:6,7,8|Comparison and public claims:9
077|Scope, informed choice and participation:1,2,3|Movement access, evidence and clinical limits:4,5,6|Settings, evaluation and wellness media:7,8
078|Literary form, poetry and drama:1,2,3|Regional prose, world literature and genres:4,5,6|Translation, institutions and interpretation:7,8
079|Visual decisions and material practices:1,2,3,4,5|Digital work and reflective practice:6,7|Exhibiting, livelihoods and cultural responsibility:8
080|Screen evidence, image, edit and sound:1,2,3,4|Performance, narrative and adaptation:5,6|Industry, audiences and criticism:7,8
081|Live relationships, text and rehearsal:1,2,3|Movement, design and performance traditions:4,5,6|Audiences, institutions and economics:7,8
082|Clothing design, materials and fit:1,2,3|Dress histories, care and labor:4,5,6|Sustainability, identity and rights:7,8
083|Materials, manufacture and gem reports:1,2,3,4|Design, conservation and cultural histories:5,6|Valuation, sourcing and rights:7,8
084|Object evidence and collecting categories:1,2,3,4,5|Condition and collection care:6|Markets, cultural property and attribution:7,8
085|Project design, measurements and materials:1,2,3,4|Tools, reuse and project economics:5,6|Documentation, rights and sharing:7,8
086|Assessment, diagnosis and treatment purposes:1,2,7|Material-specific restoration and heritage:3,4,5,6|Honest media and handover:8
087|Mechanisms, fluids and electrical sensing:1,2,3|Household, mobility and information systems:4,5,6|Materials, failure and explanatory integrity:7,8
088|Production chains and major materials:1,2,3,4,5|Food, craft and scale comparisons:6,7|Environmental claims and transparency:8
089|Historical credit and technological domains:1,2,3,4,5|Adoption, failure and unintended effects:6,7|Rights and responsible invention stories:8
090|Physical and living-world explanations:1,2,3|Designed systems, institutions and numbers:4,5,6|Question design and explanatory evidence:7,8
091|Ingredients, heat and culinary structures:1,2,3,4,5|Workflow, safety and food histories:6,7|Recipe development and honest media:8
092|Sensory language, tea and coffee:1,2,3|Other drinks and health-claim literacy:4,5|Service, environmental evidence and comparisons:6,7
093|Farm context, resources and crops:1,2,3|Pests, livestock and harvest systems:4,5,6|Economics, land, labor and sustainability:7,8
094|Residents, livelihoods and infrastructure:1,2,3|Services, migration and public culture:4,5,6|Governance and responsible representation:7,8
095|Makers, materials and craft traditions:1,2,3,4,5|Markets, knowledge transmission and design exchange:6,7|Rights and responsible craft media:8
096|Collections, provenance and interpretation:1,2,3|Conservation, living heritage and sites:4,5,6|Digital access, restitution and accountability:7,8
097|Institutions, budgets and service journeys:1,2,3|Procurement, data and oversight:4,5,6|Participation and comparative outcomes:7,8
098|Legal sources, courts and transactions:1,2,3|Public rights, everyday law and creative rights:4,5,6|Criminal safeguards and legal interpretation:7,8
099|Institutions, archives and historical cases:1,2,3|Assessment, oversight and technology:4,5,6|Counterintelligence, diplomacy and open sources:7,8,9
100|Evidence integrity and forensic methods:1,2,3,4|Reconstruction and digital records:5,6|Testimony, miscarriages and ethical interpretation:7,8
101|Memory systems, encoding and forgetting:1,2,3|Retrieval, skills and bodily contexts:4,5,6|Methods, myths and external records:7,8
102|Meaning, listening and explanation:1,2,3|Writing, speaking and language access:4,5,6|Disagreement, digital channels and accountability:7,8
103|Authority, goals and development:1,2,3|Teams, decisions and ethical power:4,5,6|Organizational change and leadership evidence:7,8
104|Organizations, hiring and workflow:1,2,3|Pay, access and digital work:4,5,6|Change, worker voice and storytelling evidence:7,8
105|Decision evidence, prices and framing:1,2,3|Social influence, digital choice and satisfaction:4,5,6|Research quality and consumer protection:7,8
106|Audience, offer, creative and channels:1,2,3|Journeys, measurement and economics:4,5,6|Advertising rules and responsible cases:7,8
107|Transactions, catalogs and payments:1,2,3|Fulfillment, service and store operations:4,5,6|Economics, regulation and privacy:7,8
108|Networks, inventory and warehouse records:1,2,3|Transport, cold chains and resilience:4,5,6|Labor, environmental claims and measurement:7,8
109|Railway systems, vehicles and control:1,2,3|Stations, freight and railway histories:4,5|Maintenance, economics and responsible media:6,7,8
110|Access, active travel and public transport:1,2,3|Roads, freight and unequal burdens:4,5,6|Energy, safety and planning choices:7,8
'''

def main():
 import manage_all_topic_banks as helper
 for line in DATA.strip().splitlines():
  nid,*parts=line.split('|'); directory=helper.home(nid); p=directory/'IN_DEPTH_TOPIC_BANK.json'; b=helper.read(p)
  source_ids=set(b['local_reconciliation']['source_categories'])
  source_cs=[c for c in b['categories'] if c['id'] in source_ids]
  assigned=set(); parents=[]
  for index,part in enumerate(parts,1):
   title,indices=part.rsplit(':',1); pid=f'DOMAIN-{nid}-G{index:02d}'
   parents.append(dict(id=pid,title=title,scope='Read the subcategories from foundations through mechanisms, cases and interpretation; each video retains its individual scope.'))
   for number in map(int,indices.split(',')):
    assert number<=len(source_cs),(nid,number,len(source_cs));c=source_cs[number-1];assert c['id'] not in assigned; assigned.add(c['id']); c['parent_id']=pid;c['reading_subcategory']=c['title']
  assert assigned==source_ids,(nid,'missing hierarchy assignment',source_ids-assigned)
  # Retain distinct authored branches already introduced by the append-only helper.
  extra_parent_ids={c['parent_id'] for c in b['categories'] if c['id'] not in source_ids}
  parents += [p for p in b['parent_categories'] if p['id'] in extra_parent_ids]
  b['parent_categories']=parents
  b['organization_review']={'date':'2026-10-23','source_categories_preserved':len(source_cs),'method':'Manually assigned subject groupings. Source questions, scopes, category titles, IDs and prerequisites remain unchanged.'}
  if int(nid)<=10:
   b['integration_stage']='detailed_import_reconciled_hierarchy_reviewed_coverage_open'
  helper.write(p,b); errors=helper.check_bank(b,directory);assert not errors,errors;helper.render(b,directory)
 print('Reviewed and regrouped109 detailed banks; source metadata and proposals intact.')
if __name__=='__main__':main()
