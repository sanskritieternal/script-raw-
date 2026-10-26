import json
from pathlib import Path
from editorial_authoring_002_184 import parse
p=Path('Scripts/editorial_pass_002_184.json'); payload=json.loads(p.read_text(encoding='utf-8'))
new=parse(r'''
[113]
@Grid planning|Availability and dispatch|intermediate
Why is a dispatchable generator not the same thing as a generator that is always available?|Compare operator control, fuel, maintenance, ramp limits, variable output and demand uncertainty in a hypothetical grid; distinguish capacity from energy delivered.|2
[114]
@Water institutions|Tariffs and affordability|advanced
How can a water tariff recover network costs while leaving some households unable to access a reliable supply?|Compare fixed charges, metered use, connection fees, subsidies, informal vendors and service quality in one dated jurisdiction; give no personal billing or legal advice.|7
[115]
@Forest landscapes|Degradation and farm mosaics|intermediate
What distinguishes forest degradation from clearing when a satellite still sees tree cover?|Compare canopy, species, biomass, disturbance, land use and measurement thresholds in a fictional mapped landscape; distinguish a chosen indicator from the whole ecosystem.|7
How does an agroforestry mosaic connect tree management with crops, livestock and household needs?|Compare shade, water, tenure, labor, seasonality, production and landscape connectivity in one identified farming region; avoid equating tree planting with a universal benefit.|5
[117]
@Adventure institutions|Mountaineering and expedition labor|advanced
How did mountaineering clubs, guides and transport networks change who could climb in the nineteenth century?|Compare dated club records, access, equipment, class, gender and local expertise through a bounded Alpine history; avoid reducing modern mountaineering to a sequence of summit records.|7
How are responsibility, credit and risk divided between commercial expedition clients, guides and local workers?|Trace permits, contracts, load carrying, rescue obligations, insurance and consented worker accounts in a dated expedition context; exclude route instruction and assumptions that all workers share one identity.|9
[122]
@News institutions|Cheap print and radio production|intermediate
How did the penny press change who paid for news and which readers publishers sought?|Compare price, advertising, circulation, reporting costs, urban literacy and editorial choices through one dated newspaper case; distinguish business-model change from a claim of universal democratization.|1
How did a radio newsroom verify and assemble a bulletin before it reached a live microphone?|Trace assignment, wire copy, timing, editing, recorded sound, corrections and local judgment in a defined historical newsroom; separate production practice from the history of radio hardware.|3
[124]
@Audio production|Room sound and recording continuity|intermediate
Why can the same voice recording sound intelligible nearby but unclear after a room's reflections are added?|Compare direct sound, early reflections, reverberation, microphone distance and speech intelligibility using a labeled audio simulation; distinguish acoustic treatment from soundproofing.|2
What should an interview-recording backup preserve if the primary recorder fails halfway through a conversation?|Compare independent recording paths, power, storage, synchronization, monitoring, permissions and recovery in a benign planned workflow; distinguish redundancy from two files sharing one failure point.|7
[127]
@VFX production|Bidding and changing scope|advanced
What must a VFX shot bid specify before a studio can compare two quoted prices?|Map plates, assets, frame range, complexity, versions, approvals, revisions, dependencies and delivery requirements through a fictional bid; distinguish a scoped estimate from a guaranteed final cost.|8
[138]
@Cycling institutions|Electric assistance classifications|advanced
Why can two similar-looking e-bikes fall under different legal classifications?|Compare assistance mode, rated power, speed rules, vehicle labels, rider obligations and the date of one jurisdiction's official definitions; exclude modification instructions or personal legal conclusions.|6
[140]
@Boat ownership|Survey evidence and exclusions|advanced
What can a pre-purchase marine survey establish when some parts of a vessel cannot be inspected?|Compare access, haul-out limits, equipment tests, documentation, exclusions and specialist follow-up in a fictional survey; avoid certifying a boat or replacing a qualified surveyor.|6
[145]
@University institutions|Rankings and internal choices|advanced
How can a university's response to a ranking change where it spends money and whom it admits?|Trace a named ranking's dated indicators, measurement incentives, institutional decisions, affected students and unintended effects; distinguish an observed policy response from an unsupported claim of motive.|7
[146]
@Life histories|Contradictory chronologies|advanced
How can a public figure's chronology be reconstructed when letters, official records and later memoirs give different dates?|Compare event proximity, calendars, document purpose, independence, inferred intervals and unresolved contradictions; do not silently choose the most dramatic sequence.|5
[147]
@Biographical interpretation|Posthumous reputation|advanced
How did a person's reputation change after death when archives, commemorations or political priorities changed?|Compare dated obituaries, new documents, biographies, monuments and attributed criticism; distinguish a new interpretation from proof of a newly alleged act.|8
[148]
@Humanitarian institutions|Origins and refugee mandates|intermediate
How did the early Red Cross movement connect battlefield relief, national societies and international agreements?|Trace dated founding documents, neutrality claims, volunteer organization, access and exclusions; distinguish the movement's branches rather than treating every Red Cross institution as one organization.|1
How do refugee-assistance institutions divide responsibility when legal protection, shelter and longer-term services fall to different bodies?|Map mandates, eligibility, host authorities, funding, local partners and affected people's accounts in one dated setting; avoid individual immigration advice.|3
[149]
@Cultural organization|Kinship vocabulary|intermediate
What can kinship terms reveal about social obligations beyond a biological family tree?|Compare terms of address and reference, household practice, descent, marriage, adoption and translation in one attributed community context; avoid treating terminology as a complete account of actual relationships.|2
[150]
@Pastoral networks|Specific landscapes and trade|intermediate
How do seasonal movements in a Mongolian pastoral landscape connect grazing, weather and household decisions?|Trace one documented region's seasonal camps, water, herd composition, tenure, markets and changing access; avoid treating all Mongol communities as historically or presently identical.|1
How have Kazakh pastoral landscapes changed as mobility, borders and land institutions changed?|Compare named routes, pasture access, herd composition, settlement records and community accounts across a bounded period; distinguish adaptation from a simple disappearance narrative.|2
How did a named Bedouin trade network connect pastoral mobility with towns and markets?|Compare goods, routes, credit, intermediaries, seasonal access and changing political authority through attributed historical accounts; avoid portraying all Bedouin societies as one network.|3
[153]
@Polar systems|Permafrost carbon and research governance|advanced
How can thawing permafrost release different greenhouse gases under wet and dry conditions?|Compare microbial decomposition, oxygen, substrate, hydrology, time horizon and measurement uncertainty; distinguish site measurements from a global forecast.|3
What does the Antarctic Treaty system regulate about research and environmental access, and what remains outside a simple no-ownership summary?|Compare dated treaty instruments, claims, inspection, environmental obligations and national authorization; distinguish institutional explanation from permission to travel or conduct research.|7
[154]
@Microbial systems|Metabolic diversity|intermediate
Why can two microbes living side by side obtain energy from entirely different chemical processes?|Compare electron donors and acceptors, carbon sources, oxygen conditions and metabolic cooperation conceptually; exclude culturing or manipulating organisms.|3
[155]
@Biotechnology manufacturing|Industrial enzymes|intermediate
What changes when an enzyme becomes a manufactured ingredient rather than a laboratory observation?|Trace host choice, production consistency, separation, formulation, activity measurement and product requirements through a benign industrial example; exclude experimental or organism-engineering procedures.|5
[156]
@Everyday materials|Deposits and curing|intermediate
Why can hard water leave a mineral deposit even after the water itself has evaporated?|Compare dissolved ions, heating, evaporation, saturation and surface conditions conceptually; exclude chemical mixing or descaling prescriptions.|2
Why can an adhesive feel dry while its bond is still developing?|Compare evaporation, chemical curing, moisture, substrate, time and manufacturer-defined conditions using nonprocedural diagrams; distinguish curing from a universal strong-bond claim.|6
[157]
@Materials under load|Fatigue and microstructure|intermediate
Why can repeated loads damage a metal even when each load is below the strength measured in a single pull test?|Compare cyclic loading, crack initiation, surface condition, environment, stress range and specimen variability; exclude design life calculations or diagnosing actual components.|6
[158]
@Electrochemical systems|Flow batteries|intermediate
How does a redox flow battery separate stored energy from the equipment that delivers power?|Compare electrolyte tanks, cell stack, circulation, membrane, scale and losses using a conceptual schematic; exclude construction, chemical handling or performance guarantees.|6
[162]
@Failure investigation|Network cascade records|advanced
What did the 2003 Northeast blackout investigation establish about how local events became a regional cascade?|Compare the official chronology, monitoring, vegetation management, protection, communication and institutional recommendations; distinguish established findings from a unique simulated reconstruction.|6
[163]
@Comparing extremes|River measurement conventions|advanced
Why can claims about the world's longest river disagree without either team making an arithmetic error?|Compare source selection, tributary conventions, channel migration, map resolution, coastline endpoints and uncertainty; distinguish a measurement definition from an uncontested geographical title.|2
[167]
@Historical counterfactuals|Chokepoint alternatives|advanced
How could closing a historical trade chokepoint change routes without simply moving the same trade to the nearest passage?|State a dated hypothetical closure, vessel technology, alternative costs, ports, institutions, demand and actor knowledge; separate a bounded network scenario from a prediction of all later history.|6
[169]
@Shared institutions|Volunteer libraries|advanced
How does a volunteer-run library maintain reliable access when donations and staff time fluctuate?|Trace governance, opening hours, collection decisions, safeguarding, accessibility, repairs and handover in a consented institution; distinguish a functioning service from a one-day book donation.|3
''')
for nid,v in new.items():payload.setdefault(nid,{'groups':[]})['groups'].extend(v['groups'])
p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Additional gap payloads saved',sum(len(g['topics']) for v in new.values() for g in v['groups']))
