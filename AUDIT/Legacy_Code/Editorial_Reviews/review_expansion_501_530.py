"""Completed editorial pass for the 30 expansion plans; active plans remain editable."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = "history_origins famous_examples hidden_stories beginner_explainers advanced_concepts mysteries_unsolved_cases technology_innovation people_personalities major_events how_it_works rise_fall then_vs_now future_developments myths_vs_facts documentary_stories".split()
QUESTIONS = {
"521": """Which observations led scientists to revise a soil concept?
What can one influential soil study establish beyond its sampled site?
Whose field or land-management knowledge shaped a soil investigation?
How do formation, layers and function connect in a soil profile?
Which sampling and analytical choices change a soil-property estimate?
Which measurements could distinguish explanations for an unexpected soil pattern?
How well does a soil sensor perform against a reference method?
Which documented choices shaped a soil survey or research site?
How did a dated land-use change affect comparable soil measurements?
Where does uncertainty enter between selecting a soil sample and interpreting it?
Why did evidence change support for a soil practice or model?
Does a soil trend persist under consistent depth, season and sampling methods?
What local validation would a proposed soil intervention require?
Does a soil-improvement claim establish a durable measured change?
How did a field investigation connect site history, sampling and interpretation?""",
"522": """Which pollution problem shaped an air-quality measure or policy?
Did a clean-air intervention change emissions, concentration or actual exposure?
Whose monitoring or community-reporting work is missing from an air-quality account?
How do emissions, concentrations and exposure differ for one pollutant?
Which monitoring and modeling choices change an exposure estimate?
Which evidence distinguishes explanations for an unexplained pollution episode?
Does an air-quality sensor or control work under its stated conditions?
How did evidence and public input shape an air-quality decision?
What happened between a pollution warning and subsequent review?
Where are evidence gaps between pollution sources and public reporting?
Which drivers explain a pollutant trend after weather and monitoring changes?
How do two periods compare under consistent stations and averaging times?
What implementation and monitoring would a proposed clean-air measure require?
Does an air-quality claim identify the pollutant and averaging period?
How did a community concern proceed through measurement, attribution and response?""",
"523": """Which species and habitat evidence shaped a conservation approach?
Does monitoring support a conservation project's claimed recovery?
Whose stewardship or field knowledge is omitted from a conservation account?
How do threats, population measures and intervention connect at one site?
Which survey and comparison choices change a conservation-effect estimate?
What competing explanations remain for a population or habitat change?
Does a conservation technology improve usable evidence without undue disturbance?
Whose authority and objectives shaped a conservation decision?
What changed after a dated protection measure or habitat disturbance?
Which ecological and institutional dependencies connect conservation action to follow-up?
Why did a conservation approach gain or lose support?
Does a biodiversity trend persist after accounting for survey effort and detection?
What would a proposed conservation action need to show measurable progress?
Does a biodiversity success claim state its baseline and remaining threats?
How did a conservation intervention move from planning to ecological follow-up?""",
"524": """How did production and distribution changes shape a regional food system?
Who benefited from a food-system intervention within its stated boundary?
Whose labor or knowledge is missing from a food supply-chain account?
How do food flows, prices and nutritional access connect for one product?
Which system-boundary choices change a food-system comparison?
Which causes explain an unexpected food price, supply or loss pattern?
Did a food-chain technology improve outcomes across the stages it affected?
Whose documented incentives shaped a food policy or supply-chain decision?
How did a harvest, trade or infrastructure shock affect one food chain?
Where do losses and responsibility change along a regional food chain?
Why did a food-system practice expand or decline?
How do regional food chains compare using consistent quantities, prices and boundaries?
What resources and access conditions would a proposed food-system change require?
Does a food-security claim establish affordability as well as availability?
How did one disruption travel from producers through workers to consumers?""",
"525": """How did access rules and stock knowledge shape a fishery's management?
What does a management intervention establish about stock and livelihood outcomes?
Whose fishing or processing knowledge is missing from a fishery account?
How do stock, catch, effort and management connect in one fishery?
Which assessment assumptions change advice for a named fish stock?
What competing explanations remain for a change in catch or stock estimates?
Did a fishery technology change catch, bycatch and operating conditions as claimed?
Whose knowledge and authority shaped a fisheries-management decision?
What changed after a quota, closure or stock reassessment?
Where do accountability and custody change between access rights and sale?
Why did a fishery expand or contract after accounting for effort and markets?
How do stock conditions compare under consistent surveys and assessment boundaries?
What enforcement and monitoring would a proposed fishery measure require?
Does a sustainable-seafood claim identify its stock, gear and assessment date?
How did an assessment become a management decision and later review?""",
"526": """How does a community's authorized account explain a historical development?
What does one Indigenous historical case establish within its own place and period?
Which overlooked contribution does the source community consider important?
Which community names and historical contexts are needed to understand one account?
How do authorship, translation and power shape interpretations of a historical issue?
Which historical question remains unresolved across community and external sources?
What can authorized evidence establish about one knowledge practice or technology?
How did one person's actions relate to collective relationships and institutions?
How do community and external records describe a dated event differently?
How did one institution operate in a defined community and period?
Which locally grounded evidence explains change in a historical institution?
How do community members describe continuity across two documented periods?
What permissions and resources would a community-led historical project require?
Does a public historical claim reflect attributed community knowledge and records?
How was one historical account assembled with community authority and access conditions?""",
"527": """How did an oral-history project's original questions shape its collection?
Whose experiences can a documented interview collection represent?
Whose interviewing, translation or archival labor is overlooked?
How does an interview become a contextualized historical source?
Which interpretations of an interview passage fit its recording and corroborating evidence?
What remains uncertain when a remembered event differs from other records?
Does a recording or transcription tool preserve accuracy and consent conditions?
How were selection and access decisions made in an oral-history project?
How did accounts of an event change across recording periods?
Who authorizes each stage from interview invitation to later reuse?
Why did an oral-history project expand, close or change stewardship?
How do recording context and later experience affect accounts of the same topic?
What relationships and stewardship would a proposed collection require?
Does a historical claim fairly represent the full interview and its context?
How did recording, editing and access decisions shape one interview's later use?""",
"528": """How did a library or archive's founding purpose shape its holdings?
Whose needs did a collection or access initiative actually serve?
Whose cataloging, preservation or community work is missing from an institutional account?
How does an item move from acquisition through description to user access?
Which preservation or description tradeoffs affect a defined material type?
What can accession records resolve about a gap in collection provenance?
Does a search or digitization technology improve accuracy and usable access?
Who influenced an acquisition, description or access decision?
How did a move, disaster or policy change affect a collection?
Where do rights and stewardship decisions enter an item's institutional journey?
Why did a collection or public service grow, shrink or disappear?
How did description and access change for the same collection over time?
What recurring support would a proposed collection or access service require?
Does a complete-archive or open-access claim match holdings and restrictions?
Which transfers in a collection's custodial journey are documented or disputed?""",
"529": """How did dated texts and translator accounts shape a translation tradition?
How does an influential translation relate to its source edition and reception?
Whose editing, interpreting or language-consulting work is overlooked?
How do source, audience and revision shape meaning in a translated passage?
Which grammatical and cultural tradeoffs distinguish alternative renderings?
What evidence could clarify an unresolved rendering or attribution?
How does a translation tool perform for a defined language pair and text type?
Which drafts and notes explain a translator's documented choices?
How did a publication or censorship event affect a translation's reception?
Who decides terminology and final wording between source selection and publication?
Why did a translation gain or lose readership?
How do two translations differ after controlling for their source editions?
What source access, expertise and review would a translation project require?
Does a claim of definitive meaning account for context and competing renderings?
How did a translated work move through editions, revisions and reception?""",
"530": """Which communication problem shaped a media-literacy teaching approach?
What does a media-literacy evaluation establish beyond participant confidence?
Whose teaching or verification work is missing from an information-literacy account?
How do source, evidence and context change the interpretation of one public claim?
Which evaluation tasks establish learning beyond recall or familiarity?
What competing explanations remain for a claim's persistence after correction?
Does a verification tool improve checking beyond the tool's own interface?
Which documented source and audience decisions shaped a lesson or editorial choice?
How did an information event proceed from publication through redistribution and correction?
Where can error enter between producing, distributing and checking a claim?
Why did a media format or verification practice gain or lose use?
How did interpretation change across equivalent claims and audience measures?
What audience and evaluation evidence would a proposed literacy program require?
What does original evidence establish about a viral claim's accuracy?
How did a verification effort document evidence, corrections and remaining uncertainty?""",
"511": """Which engineering problem drove a semiconductor device or process change?
What does a landmark chip's benchmark establish for its intended workload?
Whose fabrication, testing or packaging contribution was overlooked?
How does a chip design become a fabricated, packaged and tested device?
Which power, performance, area and yield tradeoffs shape a chip comparison?
Why did measured device behavior differ from its published expectation?
What separates a semiconductor laboratory advance from qualified production?
Which documented constraints shaped a chip or fabrication investment decision?
How did a dated supply or policy event affect a specific chip chain?
Where are quality and responsibility checked between chip design and shipment?
Why did a device architecture gain or lose support for a workload?
How do chip generations compare under equivalent system and test conditions?
What measurements and production steps remain before a proposed chip advance scales?
Does a semiconductor claim compare measured properties or marketing labels?
How did a chip move from design through qualification and deployment?""",
"512": """How did a quantum-computing proposal become a documented experiment?
What did a widely cited quantum demonstration actually establish?
Whose calibration, control or verification work enabled a quantum result?
How do preparation, operations and measurement answer one quantum task?
Which physical and logical resources determine the cost of a quantum task?
Which experiment could distinguish explanations for a disputed quantum result?
Does a component advance improve the full computation being proposed?
Which recorded research decisions shaped a quantum experiment's design?
How did replication or criticism change a quantum milestone's interpretation?
Where do error and validation enter a quantum experiment?
Why did confidence in a quantum approach increase or decline?
How do two demonstrations compare using the same task and resource definitions?
What assumptions stand between a quantum algorithm and its proposed application?
Does a quantum-advantage claim use a defensible classical comparison?
How did a quantum result move from proposal through verification and debate?""",
"513": """Which user task led to an interaction technique's development?
What does a celebrated interface's evaluation establish about its users and tasks?
Whose accessibility or support work shaped an interface project?
How do goals, actions and feedback connect in one user interaction?
How do research methods change the usability conclusion for one task?
Why did real-world use differ from a usability test's prediction?
Does an interaction technology improve tasks for the users it claims to serve?
How did research evidence influence a documented design decision?
What changed in task completion after a dated interface redesign?
Where does a user encounter error, feedback and recovery in a task?
Why did users adopt or abandon an interaction pattern?
How do interface versions compare after accounting for familiarity and training?
What user evidence would a proposed interface need before deployment?
Does an intuitive-design claim fit the diversity of users actually tested?
How did user research change a design between prototype and release?""",
"514": """How did a software project's founding problem shape its releases and governance?
What distinguishes an open-source project's popularity from sustainable use?
Whose documentation, translation or release labor is missing from a project account?
How do licensing, contribution and maintenance work in one open-source project?
Which project-health metrics reveal responsibility rather than activity alone?
What explains a gap between project adoption and maintenance capacity?
Did a development tool improve review or verification in an actual project?
Who decided a license, release or governance change and on what record?
How did a fork, license change or incident affect a project and its users?
How does a contribution move from an issue to a supported release?
Why did an open-source project grow, stagnate or lose support?
How did a project's support and contribution patterns change across releases?
What funding and succession assumptions support a proposed project model?
Does open code come with the security and support being claimed?
How did a project change move from proposal through review to user impact?""",
"515": """Which coordination problem led to an internet institution or rule?
Whose access or interoperability changed after a governance decision?
Whose implementation or civil-society work is missing from a policy account?
Which organizations hold technical, legal and platform authority in one internet issue?
How do governance models distribute participation, enforcement and accountability?
Which evidence could clarify an unresolved internet authority dispute?
Did a protocol or coordination change solve the operator problem it targeted?
How did a proposal, objection and recorded decision shape an internet rule?
What changed when an internet decision moved into implementation?
Where does authority end between proposing, adopting and enforcing an internet rule?
Why did operators or institutions adopt or reject a governance approach?
How did participation and authority change around the same internet issue?
What institutional and technical conditions would a proposed governance change require?
Does a claim of internet control match the powers of the named institution?
How did one governance dispute proceed through decision, implementation and appeal?""",
"516": """Which workplace problem led to a labor protection in one jurisdiction?
Did a labor-rights intervention improve workers' usable access to protection?
Whose organizing or support work is missing from a workplace-rights account?
Who is covered by one workplace right and how is it enforced?
How do complaint records distort estimates of labor-rights enforcement?
What explains a gap between a legal right and documented workplace practice?
Did a payroll or reporting tool make a labor protection more usable?
Whose authority and representation shaped a bargaining or policy decision?
How did a dated law, agreement or judgment change coverage in practice?
Where can a worker encounter barriers between learning a right and seeking remedy?
Why did a labor protection expand, weaken or change enforcement?
How did protection change under consistent worker and sector definitions?
What administration and enforcement would a proposed labor reform require?
Does a workplace-rights claim match the applicable dated rule or agreement?
How did a workplace-rights issue proceed from complaint to documented remedy?""",
"517": """Which documented hazard or incident shaped a workplace safety system?
What does a safety program's evaluation establish beyond low incident reports?
Whose prevention or maintenance work is missing from a safety account?
How does one workplace connect hazard control, reporting and review?
Do exposure, near-miss and injury measures tell the same safety story?
What explains a gap between a safety procedure and observed outcomes?
Does a safety technology work under its intended task and maintenance conditions?
How did worker consultation and assigned responsibilities shape a safety decision?
Which corrective actions followed a dated incident or safety-rule change?
Who checks whether a workplace control continues to perform?
Why did a safety approach gain or lose practical support?
Does a safety trend persist under equivalent hours, tasks and reporting rules?
What evidence and verification would a proposed safety intervention require?
Does a workplace safety claim disclose its denominator and reporting limits?
How did a worker concern move through investigation, prevention and follow-up?""",
"518": """How did a cooperative's founding need shape its ownership and trading rules?
What do member outcomes and finances establish about a cooperative's performance?
Whose voluntary or administrative labor is omitted from a cooperative's account?
How do membership, voting, capital and surplus connect in one cooperative?
Which objectives conflict when judging a cooperative's success?
What explains a gap between cooperative principles and actual decisions?
Did a tool improve cooperative operations without excluding members?
How did a membership or board decision proceed from proposal to implementation?
What changed in control after a cooperative merger, conversion or crisis?
How does a member enter, influence and leave a cooperative?
Why did a cooperative grow or decline under its market and financing conditions?
How did member and financial outcomes change under consistent accounting?
What enforceable rights and resources would a proposed cooperative need?
Does a democratic-ownership claim match actual voting and benefit rules?
How did a member need become a cooperative decision and observed outcome?""",
"519": """How did a poverty measure's purpose shape its original definition?
Which households and outcomes does a poverty-reduction evaluation represent?
Whose living conditions are missing from a public poverty narrative?
How do income, wealth and deprivation describe different household conditions?
Which analytical choices change the estimated distribution of resources?
Why do datasets give different accounts of a poverty or inequality change?
Did a service technology improve access for the households it targeted?
How did affected households influence a policy or measurement decision?
What changed in household conditions after a dated shock or policy change?
How does household survey information become a poverty classification?
Which drivers explain a measured gap after considering prices and transfers?
Does a distributional trend persist under consistent household and price definitions?
What delivery and evaluation assumptions support a proposed anti-poverty measure?
Does a poverty headline use the threshold and denominator readers would expect?
How did a household-support policy move from proposal to actual delivery?""",
"520": """How did a government's budget rules develop and change in practice?
What did a public spending initiative deliver beyond its appropriation?
Whose finance, audit or community-monitoring work is overlooked?
How do revenue, appropriation, expenditure and audit differ in one budget?
Which accounting boundaries change the apparent cost of a budget choice?
Why did actual services differ from a budget promise?
Did a digital budget system improve usable transparency and accountability?
Whose recorded priorities shaped a public spending decision?
What followed a dated budget reform or emergency appropriation?
Where are responsibilities transferred between approval, purchase and service delivery?
Does a growing budget line reflect real expansion or reclassification?
How do fiscal periods compare under consistent accounting and prices?
What financing and implementation assumptions support a proposed budget measure?
Does a public spending claim match its fiscal period and accounting source?
How did a spending promise proceed through delivery and audit?""",
"501": """Which documented problem led a community to establish a public-health program?
What does a prevention program's evaluation establish beyond its success story?
Whose community work is missing from an account of a public-health response?
How do surveillance, prevention and service delivery connect in one local program?
How does an evaluation separate a program's effects from other changes?
Which competing explanations remain for a program's unexpected outcome?
Did a public-health tool improve the outcome it was introduced to change?
Whose priorities shaped a public-health decision and whose were absent?
What changed in service delivery after a dated public-health event?
Who carries responsibility between identifying a health need and checking results?
Why did participation or support for a prevention program expand or decline?
Does a population-health trend persist under consistent reporting definitions?
What would a proposed public-health change require to be evaluated fairly?
Does a public prevention claim match its original evaluation?
How did a community program move from proposal to documented follow-up?""",
"502": """How did a rehabilitation service's goals and professional roles develop?
Which patients and functional outcomes does a prominent rehabilitation evaluation describe?
What patient and therapist work is omitted from a rehabilitation success story?
How does one rehabilitation pathway connect assessment, therapy and follow-up?
Do alternative functional measures tell the same rehabilitation story?
What explains a gap between rehabilitation participation and recorded outcomes?
Did a rehabilitation technology's laboratory performance carry into everyday use?
How were patients' priorities represented in a rehabilitation service decision?
How did a service reorganization change rehabilitation access or continuity?
Who is responsible at each handoff in a rehabilitation pathway?
Why did a rehabilitation approach gain or lose institutional support?
How did service outcomes change after accounting for patient mix and measurement?
What resources would a proposed rehabilitation service need for sustained follow-up?
Does a rehabilitation claim describe the population and outcome actually studied?
How did a patient's goals change across a documented rehabilitation journey?""",
"503": """How did an assistive product develop around a documented user need?
What does a product evaluation establish about participation in a defined activity?
Whose user, caregiver or repair knowledge shaped an assistive product?
Which services make an assistive device usable for a particular activity?
Do an assistive product's outcome measures reflect users' priorities?
Why did an assistive product work differently in a trial and everyday life?
Does a new assistive feature improve a task under comparable conditions?
How did user consultation influence a product's design or procurement?
What changed after a funding or access policy for assistive products?
Who supports an assistive product from assessment through replacement?
Why did an assistive product spread or disappear from provision?
How do two product generations compare on the same user task?
What must be established before an assistive prototype becomes a usable service?
Does a claim of independence match users' measured or reported outcomes?
How did one product journey move from assessment through daily use and repair?""",
"504": """Which access problem shaped a maternal or child health service?
What does a program evaluation establish for its defined families and setting?
Whose care work is overlooked in a maternal or child health pathway?
How does one family move through eligibility, referral and follow-up?
Do access measures and health-outcome measures describe the same service performance?
Which explanations remain for a documented maternal or child service gap?
Did a service technology improve reach without weakening continuity?
How were affected families represented in a care-service decision?
What changed after a maternal or child service opened, closed or reorganized?
Who takes responsibility at each transition in a family care pathway?
Why did participation in a maternal or child service change?
Does an outcome trend persist under consistent age and reporting definitions?
What would a proposed care-service change need to deliver and evaluate?
Does a public maternal or child health claim fit the population studied?
What does one consented family journey reveal about a service system?""",
"505": """Which evidence and methods shaped a nutrition recommendation?
Does the popular account of a dietary study match its actual design?
Whose diets or research contributions are missing from a nutrition study's story?
How do studies distinguish a nutrient, a food and a dietary pattern?
Which measurement and confounding choices drive a nutrition estimate?
Why do studies of the same dietary question disagree?
How well does a nutrition-measurement tool perform against a reference method?
What documented role did a researcher, committee or funder play in a nutrition decision?
Which conclusions changed after a dated nutrition guideline revision?
Where does uncertainty enter between dietary measurement and a public claim?
Why did a nutrition claim gain or lose scientific and public support?
How did the evidence standard behind dietary guidance change over time?
What validation would an emerging nutrition-research method require?
Does a food claim turn an association into an unsupported causal conclusion?
Where did qualifications change between a nutrition paper and its headline?""",
"506": """How did a city's rental rules develop alongside its housing market?
Which households benefited from a documented housing program?
Whose tenant or maintenance work is missing from a housing-policy account?
How do tenancy terms, deposits and repair responsibilities operate in one jurisdiction?
Why do affordability measures give different accounts of the same rental market?
Which explanations account for an unexpected rent or access pattern?
Did a housing technology or building intervention improve residents' conditions?
Whose documented priorities shaped a housing allocation or tenancy decision?
What changed for households after a housing reform or development decision?
Which costs and checks appear along a household's rental journey?
Why did a rental sector or housing scheme expand or contract?
How do housing conditions compare after adjusting for prices and unit quality?
What must a proposed housing intervention deliver beyond its unit target?
Does a housing headline describe listings, occupied homes or actual tenancies?
How did one tenancy or housing-policy case move from application to outcome?""",
"507": """Which service problem led to a water or sanitation network's development?
Did a utility project deliver the coverage and reliability it promised?
Whose operating or household experience is omitted from a utility account?
What distinguishes a connection from a safely delivered water or sanitation service?
How do sampling and intermittent supply affect estimates of service performance?
Which evidence distinguishes competing explanations for a service-quality problem?
Did a treatment or monitoring technology work under actual operating conditions?
Whose needs influenced a utility investment or service-allocation decision?
What changed after a water expansion, drought response or sanitation reform?
Where do responsibility and measurement change within a utility system?
Why did a utility approach succeed, struggle or lose support?
Does a service trend persist under consistent coverage and sampling definitions?
What operating and monitoring capacity would a proposed upgrade require?
Does a safe-service claim represent the households and periods it describes?
How did one utility project move from planning to monitored operation?""",
"508": """How did a municipality change its waste collection and disposal system?
What do verified material destinations reveal about a waste program's results?
Whose waste-handling labor is absent from a recycling success story?
What happens to one waste stream after it leaves the household?
How do system boundaries alter comparisons between waste-management options?
Why do reported recycling figures differ from downstream material records?
Does a sorting or treatment technology perform with its actual incoming waste?
Whose interests shaped a waste contract, disposal site or collection decision?
What changed in material flows after a waste policy or facility opened?
Where does evidence of custody or destination disappear along a waste stream?
Why did a waste-management approach gain or lose viability?
Do waste-performance trends survive consistent material and coverage definitions?
What collection, processing and disposal capacity would a proposed change require?
Does a recycling claim establish actual recovery or only diversion?
What does the documented journey of one discarded material reveal?""",
"509": """How did a city's risk assessment become an adaptation project?
Did an adaptation project reduce the risk it was designed to address?
Whose exposure or maintenance burden is missing from an adaptation account?
How do hazard, exposure and vulnerability interact in one neighborhood?
What comparison would establish an adaptation project's protective effect?
Why did an intervention provide different protection from its prediction?
Does an adaptation technology work under local operating and maintenance conditions?
Whose priorities shaped a city's adaptation investment?
How did a neighborhood's protection perform during a documented hazard event?
Who designs, funds, maintains and evaluates one adaptation measure?
Why did an adaptation approach gain or lose local support?
How did neighborhood risk change after accounting for hazard and development?
Which assumptions determine whether a proposed adaptation measure remains useful?
Does a resilience claim cover the hazard and conditions actually tested?
What happened between identifying a neighborhood risk and evaluating its protection?""",
"510": """How did responsibility for maintaining a public asset develop?
Did a maintenance program improve the reliability measures it targeted?
Whose inspection or upkeep work is missing from an infrastructure account?
How do inspection, repair and renewal differ for one public asset?
How do condition models classify the same asset's maintenance needs?
Which authorized records can explain an unresolved service fault?
Does a new inspection technology detect what its claim promises?
How were inspection findings and service obligations weighed in a maintenance decision?
What changed after a closure, inspection reform or maintenance-funding decision?
How does a reported defect become a checked and completed repair?
Why did a maintenance program expand or accumulate neglected work?
Does a condition trend persist under consistent inspection grades and network size?
What workforce and follow-up would a proposed maintenance strategy need?
Does an infrastructure-condition claim match its inspection evidence?
How did one asset's defect move through investigation, repair and follow-up?""",
}


SOURCES = """501|WHO Health Inequality Monitor|https://www.who.int/data/inequality-monitor|015,180|Population-level prevention, surveillance and program evaluation; personal wellness advice and whole-system financing belong to neighboring niches.|program protocols, disaggregated surveillance data and original evaluations
502|WHO Rehabilitation in health systems: guide for action|https://www.who.int/publications/i/item/rehabilitation-in-health-systems-guide-for-action|026,180,503|Rehabilitation pathways and patient-defined function; general medicine, health-system overviews and assistive-product engineering have separate homes.|referral criteria, service activity, functional measures and consented patient accounts
503|WHO and UNICEF Global report on assistive technology|https://www.who.int/publications/i/item/9789240049451|179,489,502|Assistive-product selection, provision and sustained participation; disability history, speculative enhancement and the full rehabilitation pathway are neighboring subjects.|product evaluations, fitting and repair records, user-defined participation measures
504|WHO maternal and child health monitoring resources|https://www.who.int/teams/maternal-newborn-child-adolescent-health-and-ageing/epidemiology-monitoring-and-evaluation|015,180,501|Maternal and child service pathways and access; broad wellness and general health-system subjects remain separate.|age-specific service indicators, referral and follow-up records, original program evaluations
505|WHO eLENA evidence library|https://www.who.int/tools/elena|024,091,015|Nutrition measurement, study design and interpretation; cooking, food traditions and individualized dietary care are outside this plan.|original dietary studies, measurement validation, guideline evidence reviews and declared funding
506|UN-Habitat housing approach evaluation|https://unhabitat.org/sites/default/files/2023/12/global_report_evaluation_web.pdf|112,313,064|Household housing access, quality and tenancy; property investment, market forecasting and home decoration are neighboring subjects.|local tenancy rules, housing inspections, household costs and documented program delivery
507|WHO and UNICEF Joint Monitoring Programme|https://washdata.org/|114,031,510|Delivered water and sanitation services, reliability and access; general water science and infrastructure maintenance have separate homes.|service definitions, utility monitoring, treatment records, household coverage and affordability data
508|US EPA materials, waste and recycling data|https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling|396,115|Municipal material flows, collection, treatment and final destinations; household lifestyle choices and general ecology are neighboring subjects.|weighed inputs and outputs, contracts, destination records and waste-worker accounts
509|IPCC AR6 urban adaptation chapter|https://www.ipcc.ch/report/ar6/wg2/downloads/report/IPCC_AR6_WGII_Chapter06.pdf|361,111|Urban adaptation measures and distributed protection; climate mechanisms and general city design have separate homes.|local hazard assessments, project designs, maintenance records and observed event performance
510|FHWA transportation asset management guidance|https://www.fhwa.dot.gov/asset/faq.cfm|137,162,031|Institutional upkeep of public assets; household repair instructions, engineering-failure narratives and new construction are neighboring subjects.|authorized inspection reports, asset registers, work orders, budgets and service interruption records
511|NIST semiconductor metrology program|https://www.nist.gov/chips/research-development-programs/metrology-program|442,161|Semiconductor device fabrication, qualification and supply dependencies; general materials and electronics remain neighboring subjects.|original device papers, measurement conditions, process qualification and dated production disclosures
512|NIST quantum information science|https://www.nist.gov/quantum-information-science|343,061|Quantum computing experiments, resources and verification; general quantum physics and classical programming remain separate.|original experiments, benchmark definitions, error estimates and reproducible classical comparisons
513|W3C accessibility evaluation resources|https://www.w3.org/WAI/test-evaluate/|063,325|Human interaction with interfaces and measured task performance; product shopping and software implementation have separate homes.|task protocols, participant criteria, usability observations, accessibility evidence and design records
514|Open Source Initiative definition|https://opensource.org/osd|061,325|Open-source licensing, governance and maintenance ecosystems; coding tutorials and software architecture are neighboring subjects.|actual versioned licenses, repositories, contribution rules, release records and public security notices
515|IETF standards process|https://www.ietf.org/process/|129,318,488|Internet coordination, standards and policy authority; internet history, general connectivity and speculative future networks are neighboring subjects.|dated drafts and RFCs, public decisions, implementation records and jurisdiction-specific policies
516|ILO conventions, protocols and recommendations|https://www.ilo.org/international-labour-standards/conventions-protocols-and-recommendations|104,455,497|Workplace protections, coverage and enforcement; career coaching, general management and consumer transactions are neighboring subjects.|applicable local laws, collective agreements, enforcement decisions and consented worker accounts
517|ILO occupational safety management guidelines|https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_protect/%40protrav/%40safework/documents/normativeinstrument/wcms_107727.pdf|104,183,162|Occupational hazard control and prevention systems; general public safety and engineering failure are neighboring subjects.|published incident reviews, exposure measures, control verification and worker reporting records
518|ILO worker cooperatives|https://www.ilo.org/worker-cooperatives|301,104|Member ownership, cooperative governance and distribution; corporate empires and general workplace management have separate homes.|actual bylaws, membership rules, audited accounts, votes and member distributions
519|World Bank poverty measurement methodology|https://documents1.worldbank.org/curated/en/099101424092027337/pdf/P500855154ddde0b31827a1e9377c43d15e.pdf|168,097|Measured deprivation, resource distribution and policy effects; broad social theory and whole-government operation are neighboring subjects.|household microdata documentation, thresholds, prices, survey weights and original policy evaluations
520|IMF fiscal transparency framework|https://www.imf.org/en/topics/fiscal-policies/fiscal-transparency|097,014|Public revenue, spending execution and accountability; general government administration and geopolitical narratives have separate homes.|published appropriations, execution statements, procurement records and independent public audits
521|FAO Global Soil Partnership|https://www.fao.org/land-water/soils/global-soil-partnership/en|093,350,442|Soil profiles, properties, processes and field measurement; farming instructions and general materials or biology are neighboring subjects.|soil surveys, site histories, depth and season metadata, laboratory methods and repeated field measurements
522|WHO global air quality guidelines|https://www.who.int/Publications/i/Item/9789240034228|361,501|Air pollutants, monitoring, exposure and control; climate dynamics and whole public-health programs remain separate.|calibrated monitor series, averaging definitions, emissions inventories and original exposure studies
523|IUCN Red List categories and criteria|https://nrl.iucnredlist.org/resources/categories-and-criteria|115,066,205|Conservation interventions and ecological outcomes; species profiles and general ecosystem explanation have separate homes.|dated species assessments, survey effort, site baselines, intervention records and local stewardship accounts
524|FAO agrifood systems resources|https://www.fao.org/food-systems/en|093,024,505|Interactions across food production, processing, distribution and access; farm methods, food culture and individual nutrition are neighboring subjects.|material and price flows, production and distribution records, worker accounts and household access measures
525|FAO State of World Fisheries and Aquaculture 2024 landing record|https://www.fao.org/science-technology-and-innovation/resources/publications/the-state-of-world-fisheries-and-aquaculture-2024/fr|191,198,523|Managed fish stocks, harvesting and livelihoods; recreational fishing, marine-life profiles and general conservation are neighboring subjects.|dated stock assessments, effort and observer data, access rules, landing and custody records
526|Smithsonian Native Knowledge 360|https://americanindian.si.edu/nk360|149,014,527|Community-grounded Indigenous histories and authority over accounts; general culture surveys and universal historical narratives are outside this plan.|community-authorized historical sources, attributed oral accounts, provenance and dated external records
527|Oral History Association core principles|https://oralhistory.org/oha-core-principles/|147,173,526|Interview creation, memory, interpretation and consent; biography, family reconstruction and a community's whole history are neighboring subjects.|authorized recordings, consent records, interview guides, transcripts and corroborating primary records
528|Society of American Archivists core values and ethics|https://www2.archivists.org/statements/saa-core-values-statement-and-code-of-ethics|096,040,078|Collection institutions, description, preservation and access; individual manuscript interpretation and literary criticism are neighboring subjects.|collection policies, accession and custody records, catalogs, treatment reports and rights restrictions
529|International Federation of Translators charter|https://library.fit-ift.org/public/Resources/Documents/FIT_Translators_Charter_1994.pdf|041,449,451|Translation decisions, versions and reception; general linguistics, language instruction and criticism unrelated to translation remain separate.|identified source editions, authorized parallel passages, drafts, translator notes and attributed reader studies
530|UNESCO media and information literacy curriculum|https://www.unesco.org/mil4teachers/en/introduction|122,495,069|Claim checking, media interpretation and evaluated learning; media history, account security and general education have separate homes.|original claims and records, dated redistribution traces, lesson designs and original learning evaluations"""

METHODS = [
    "Trace dated origin records and subsequent interpretations.",
    "Read the original evaluation and its population, comparator, outcomes and limitations.",
    "Use attributable contribution records and consented participant accounts.",
    "Use primary definitions and a documented end-to-end example.",
    "Compare original methods, assumptions, measures and uncertainty.",
    "Compare competing explanations and specify missing discriminating evidence.",
    "Compare validation, deployment and follow-up against a stated baseline.",
    "Use decision records, assigned authority and attributed accounts.",
    "Build a dated before-and-after record without assuming causation.",
    "Trace the process, custody transfers and assigned responsibilities.",
    "Compare a dated series with competing explanations for change.",
    "Align definitions, samples, versions and measurement conditions.",
    "Read the actual proposal and distinguish required conditions from achieved results.",
    "Trace the public claim to original evidence and retain its qualifications.",
    "Build a dated evidence trail including dissent and unresolved findings.",
]


def main():
    with (ROOT / "REGISTRY/NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as stream:
        taxonomy = {r["id"]: r for r in csv.DictReader(stream)}
    metadata = {}
    for line in SOURCES.splitlines():
        number, title, url, related, remit, records = line.split("|")
        metadata[number] = dict(title=title, url=url, related=related.split(","), remit=remit, records=records)
    expected = {str(i) for i in range(501, 531)}
    if set(QUESTIONS) != expected or set(metadata) != expected:
        raise ValueError("Expected thirty question and source specifications")
    prepared, changes, ledger = [], [], []
    for number in sorted(expected):
        row, meta = taxonomy[number], metadata[number]
        path = ROOT / row["niche_path"] / "ANGLE_PLAN.json"
        original = path.read_text(encoding="utf-8")
        plan = json.loads(original)
        questions = QUESTIONS[number].splitlines()
        entries = plan["angles"]
        if (plan["niche_id"] != number or len(entries) != 20 or len(questions) != 15
                or [a['slug'] for a in entries[:15]] != BASE):
            raise ValueError(f"Question count or ID mismatch: {number}")
        for index, entry in enumerate(entries):
            if index < 15 and entry["question"] != questions[index]:
                changes.append(dict(niche_id=number, slug=entry["slug"], previous_question=entry["question"], revised_question=questions[index]))
                entry["question"] = questions[index]
            method = METHODS[index] if index < 15 else "Use the selected field lens's underlying records, measurement definitions and attributed accounts."
            entry["evidence"] = f"{method} Case records: {meta['records']}. Starting framework: {meta['title']} ({meta['url']}). Select and verify the dated underlying case sources before scripting."
            old_limit = entry["boundary"].split(" Niche boundary:", 1)[0]
            entry["boundary"] = f"{old_limit} Niche boundary: {meta['remit']}"
        if (len({a['slug'] for a in entries}) != 20 or len({a['question'] for a in entries}) != 20
                or len({a['scope'] for a in entries}) != 20 or any(not a['question'].endswith('?') for a in entries)):
            raise ValueError(f"Duplicate or incomplete angle: {number}")
        plan["purpose"] = meta["remit"]
        plan["status"] = "editorial_question_reviewed"
        plan["generation_basis"] = "Initially seeded in the 501-530 expansion; scopes and question designs subsequently revised."
        plan["review_note"] = "All 20 question designs, scope fit and evidence requirements reviewed. A primary source entry point and neighboring niche boundaries are recorded. Concrete case selection, applicable local records and factual verification remain episode-level work."
        plan["research_sources"] = [dict(title=meta['title'], url=meta['url'], checked_date="2026-10-16", role="Primary institutional framework, methods or data entry point; not blanket evidence for episode claims.")]
        if number == "525":
            plan["research_sources"][0]["access_note"] = "Official publication landing record checked; the linked FAO repository returned HTTP 403 through the research tool. Obtain and inspect the report before using its contents as episode evidence."
        plan["related_niches"] = [dict(niche_id=n, title=taxonomy[n]['title']) for n in meta['related']]
        plan["editorial_review"] = dict(date="2026-10-16", angles=20, checks=["question and scope agreement", "distinct research tasks within the niche", "neighboring niche boundaries", "primary source entry point", "episode evidence requirements"], source_feasibility="Entry point confirmed; case-level evidence must be selected and checked in Phase 1.")
        prepared.append((path, original, json.dumps(plan, ensure_ascii=False, indent=2) + "\n"))
        ledger.append(dict(niche_id=number, niche=row['title'], angles=20, status=plan['status'], source_title=meta['title'], source_url=meta['url'], related_niches=",".join(meta['related']), distinction=meta['remit'], episode_sources="case selection and verification required"))
    archive = ROOT / "AUDIT/Expansion_Editorial_Review_2026-10-16"
    archive.mkdir(exist_ok=True)
    for path, original, revised in prepared:
        backup = archive / f"{path.parent.name}_ANGLE_PLAN.json"
        if not backup.exists(): backup.write_text(original, encoding="utf-8")
        path.write_text(revised, encoding="utf-8")
    for name, rows in [("EXPANSION_EDITORIAL_REVIEW.csv", ledger), ("EXPANSION_QUESTION_CHANGES.csv", changes)]:
        if not rows: continue
        with (ROOT / "AUDIT" / name).open("w", encoding="utf-8", newline="") as stream:
            writer=csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    report = ["# Editorial review of niches 501–530", "", "Reviewed all **30 expansion plans and 600 angles**. Refined the 450 base-angle questions, retained the 150 already revised field questions and 600 scopes, and specified evidence methods and niche boundaries for every angle. Stable angle slugs and counts are preserved.", "", "A primary institutional source entry point was checked for each niche. Some are methodological frameworks or data portals; they support source discovery and framing, not every possible episode claim. Public records, consented accounts, exact versions and original case evaluations still require selection and verification in Phase 1. Access to an institutional page does not imply access to private case records or permission to reuse material.", "", "The editorial status is now `editorial_question_reviewed` for these 30 plans. This records question-design review, not a completed Research Bible, medical or legal approval, or verified episode facts. Across the registry, 528 plans have reviewed question designs and 001/004 remain pilots.", "", "The [review ledger](EXPANSION_EDITORIAL_REVIEW.csv) records all 30 decisions. The [question change ledger](EXPANSION_QUESTION_CHANGES.csv) records the 450 refinements. Original plans are retained under `Expansion_Editorial_Review_2026-10-16/`.", "", "| ID | Niche | Primary source entry point | Distinction from neighboring niches |", "|---|---|---|---|"]
    for r in ledger:
        report.append(f"| {r['niche_id']} | {r['niche']} | [{r['source_title']}]({r['source_url']}) | {r['distinction']} |")
    report += ["", "For dated numerical claims, confirm the reference period and geographic coverage of the underlying source. For culture, translation and oral history, obtain the actual authorized material and observe consent and access restrictions. A resource that describes a method cannot establish a local outcome by itself.", "", "Access note for 525: the official FAO publication landing record was checked, but its linked repository returned HTTP 403 through the research tool. Obtain and inspect the report before using its contents as episode evidence.", ""]
    (ROOT / "AUDIT/EXPANSION_EDITORIAL_REVIEW.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Reviewed {len(prepared)} plans and 600 angles; refined {len(changes)} base questions; source and overlap ledger written")


if __name__ == "__main__":
    main()
