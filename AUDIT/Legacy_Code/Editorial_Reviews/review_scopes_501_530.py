"""One-time scope revisions for the 501-530 expansion; plans remain the active source.

This batch resolves the workspace explicitly from its archive location.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = "history_origins famous_examples hidden_stories beginner_explainers advanced_concepts mysteries_unsolved_cases technology_innovation people_personalities major_events how_it_works rise_fall then_vs_now future_developments myths_vs_facts documentary_stories".split()

SCOPES = {
"526": """Trace one community's account of a historical development using community-authorized sources and dated records; avoid imposing a single origin narrative.
Examine one documented Indigenous historical case in its own community, place and period; distinguish its meaning from broad claims about all peoples.
Document an overlooked contribution identified by source-community members; obtain appropriate permission and preserve attribution and restrictions.
Explain the names, institutions and historical context relevant to one community using its preferred terminology and available authorized sources.
Compare interpretations of one historical issue across community accounts and external records; examine authorship, translation, power and evidential limits.
Investigate one unresolved historical question with community involvement and source provenance; distinguish gaps in colonial archives from absence of history.
Examine one technology or knowledge practice through community-authorized accounts and dated evidence; avoid extraction, novelty claims or restricted detail.
Reconstruct one person's documented role using appropriate community sources; situate individual action within collective relationships and historical conditions.
Follow one dated event through community accounts and relevant records; attribute competing narratives and explain the authority behind each source.
Map how one historical institution or process operated in a defined community and period; avoid treating present practice as unchanged evidence of the past.
Explain change in one institution, settlement or historical relationship using locally grounded evidence; avoid decline narratives based only on external records.
Compare two periods within one community using authorized sources and consistent questions; let members describe continuity and change.
Examine one community-led heritage or historical-research proposal through its stated aims, permissions and resources; avoid speaking for future community choices.
Test one public historical claim against attributed community knowledge and relevant primary records; identify uncertainty without dismissing oral evidence.
Build a community-authorized source trail for one event or project; document consent, attribution, context and any limits on public access.
Trace one sovereignty issue through the community's position, treaties or legal records and dated state actions; attribute competing claims precisely.
Examine one place's land records alongside community accounts and changing legal categories; distinguish recorded title from complete historical occupation.
Follow one language-continuity effort through community-defined goals, teaching and archival evidence; honor restrictions on recordings and knowledge.
Read one colonial archival collection against its authorship, purpose and omissions; include relevant community interpretations and avoid treating official description as neutral.
Examine how a community chooses to remember one event through authorized oral, material or written sources; preserve internal differences and access conditions.""",
"527": """Trace one oral-history project from its founding questions through collection and interpretation; distinguish its aims from later uses of the recordings.
Examine one documented interview collection using participant selection, consent and context; assess whose experiences it can and cannot represent.
Document overlooked narrators, interviewers, translators or archive workers in one project; credit their roles and respect permissions.
Explain interview, recording, transcription, interpretation and deposit through one collection; distinguish oral history from an uncontextualized quotation.
Compare approaches to interpreting one interview passage using memory, interview context, corroboration and competing accounts.
Investigate a discrepancy between a remembered event and other records; preserve the narrator's perspective while identifying what remains uncertain.
Evaluate one recording, transcription or access technology in a defined oral-history workflow; examine accuracy, accessibility and consent implications.
Reconstruct one project's selection or access decision through recorded policies and attributed participant accounts; distinguish narrator wishes from institutional rules.
Follow one dated event through interviews recorded at different times; examine how later experiences or questions changed the account.
Map one interview from invitation and consent through recording, editing, review and deposit; identify who can authorize each use.
Explain expansion or closure of one oral-history project using funding, participation, stewardship and access records; avoid judging value by interview count.
Compare accounts of one topic across recording periods using interview context and narrator circumstances; avoid assuming changed memory is deliberate deception.
Assess one proposed oral-history collection through relationships, permissions, recording resources and long-term stewardship; include withdrawal and access questions.
Test one historical claim made from an interview against the full recording, context and other evidence; distinguish recollection from independently established fact.
Build a consent-aware account of one interview's creation and later use; show how editing, transcription and access decisions shape interpretation.
Examine how one interview guide shapes narration through prompts, sequence and interviewer position; compare intended questions with the recorded exchange.
Compare recollections recorded at different intervals after an event; examine context and retrospective meaning without reducing memory to an accuracy score.
Compare a transcript with its recording for one passage; examine omissions, punctuation, translation and accessibility while honoring permissions.
Trace consent for recording, quotation, editing and later access in one project; distinguish initial participation from permission for every reuse.
Examine one collection's deposit, catalog and access conditions; compare narrator restrictions, preservation needs and the experience of intended users.""",
"528": """Trace one library or archive through its founding purpose, collection growth and policy changes; distinguish institutional narratives from documented practice.
Examine one collection or access initiative using holdings, users and stewardship evidence; state whose needs and materials it represents.
Document overlooked cataloging, translation, preservation or community work in one institution; credit contributors and respect privacy or donor conditions.
Explain acquisition, description, preservation and access through one collection; distinguish a catalog description from the contents and provenance of an item.
Compare approaches to describing or preserving one material type; examine context, discoverability, resources and losses introduced by each method.
Investigate a gap in one collection's provenance or description using accession and contextual records; distinguish missing documentation from proof of misconduct.
Evaluate one digitization, search or preservation technology using actual materials and user needs; compare accuracy, access and long-term support.
Reconstruct one acquisition, description or access decision through policies and documented authority; include affected communities' attributed perspectives.
Examine a dated institutional move, disaster or policy change through its effects on holdings, preservation and access.
Map one item from selection and acquisition through description, storage and user access; identify rights and stewardship decisions at each step.
Explain growth or loss of one service or collection using funding, policy, demand and preservation records; avoid equating digitization with improved access.
Compare one collection's description and access across two periods; account for changed terminology, holdings and user interfaces.
Assess one proposed archive or library service through collection rights, staffing, preservation and user access requirements; identify recurring costs.
Test one complete-archive or open-access claim against holdings, catalog coverage, restrictions and available formats.
Build a sourced account of one item or collection's custodial journey; distinguish documented transfers, disputed provenance and unknown gaps.
Examine how one institution selects acquisitions, donations or withdrawals; compare collection policy, resources and groups whose materials are absent.
Audit one set of catalog terms or descriptions with relevant users and source communities; trace inherited language and its effects on discovery.
Examine one documented conservation treatment through condition, method, intervention record and access consequences; avoid offering unsupervised treatment instructions.
Evaluate one digital collection through coverage, image or text quality, accessibility and search; distinguish online availability from usable access.
Trace one item's copyright, donor, privacy and community restrictions; distinguish permission to view from permission to reproduce or publish.""",
"529": """Trace one translation tradition or technique through dated texts and translator accounts; distinguish later reputation from original context.
Compare one influential translation with its identified source edition and reception; state language pair, version and limits of comparison.
Document overlooked translators, interpreters, editors or language consultants in one publication; credit their roles using attributable records.
Explain source text, translation choices, audience and revision through one short authorized passage; distinguish literal correspondence from conveyed meaning.
Compare approaches to one translation problem using grammar, register, context and audience; explain tradeoffs without declaring one universal solution.
Investigate an unresolved rendering or attribution using editions, manuscripts and commentary; distinguish ambiguity in the source from translator error.
Evaluate one translation technology on a defined language pair and text type; examine human review, error categories and excluded contexts.
Reconstruct one translator's documented choices through drafts, notes and correspondence; avoid inferring intent solely from the finished text.
Examine one dated translation, censorship or publication event through editions and reception records; separate immediate response from later interpretation.
Follow one passage from source selection through drafting, review and publication; identify who decides terminology, register and final wording.
Explain why one translation gained or lost readership using publication, distribution and critical evidence; avoid equating sales with accuracy.
Compare two dated translations of the same source passage; control for source edition and explain differences in audience and conventions.
Assess one proposed translation approach through source access, language expertise, review and rights; distinguish demonstration from publishable output.
Test one claim of exact, definitive or untranslatable meaning against context and competing renderings; attribute interpretive disagreements.
Build a documented account of one translated work from source edition through revisions and reception; respect quotation and reproduction permissions.
Compare alternative words for a bounded source passage using grammar, connotation and register; explain what each choice preserves or changes.
Examine one culturally specific term through its uses and possible renderings; distinguish explanation, transliteration and translation without claiming absolute impossibility.
Trace how one publication identifies and compensates translation contributions using credits and available agreements; distinguish documented terms from assumptions.
Compare one text or interface before and after localization for a named audience; examine language, conventions and functional meaning.
Study how a defined readership interprets one translated passage using attributable responses or research; avoid treating one reaction as representative.""",
"530": """Trace one media-literacy approach through the communication problem and teaching context that shaped it; distinguish historical aims from evaluated results.
Examine one documented media-literacy program using participants, learning measures and follow-up; test whether public claims match the evaluation.
Document overlooked teaching, translation or community verification work in one media-literacy effort; credit contributors and protect learner privacy.
Explain source, evidence, context and interpretation through one dated public claim; distinguish checking provenance from agreeing with a conclusion.
Compare evaluation methods for one media-literacy skill using unfamiliar tasks, comparison groups and delayed tests; distinguish knowledge from demonstrated performance.
Investigate why one claim remained persuasive after a correction using available audience and distribution evidence; avoid assuming a single psychological cause.
Evaluate one verification or teaching tool on defined claims and users; compare accuracy, accessibility and transfer beyond the tool itself.
Reconstruct one editorial or teaching decision using source records and attributed accounts; distinguish institutional authority from evidence for a claim.
Follow one dated information event through original publication, redistribution and correction; preserve the sequence and uncertainty at each stage.
Map how one claim is produced, presented, distributed and checked; identify source custody, platform mediation and opportunities for error.
Explain growth or decline of one media format or verification practice using distribution, audience and institutional evidence.
Compare interpretation of one media issue across two periods using equivalent claim types and audience measures; account for platform changes.
Assess a proposed media-literacy intervention through audience needs, teaching design, evaluation and access requirements; frame benefits as testable expectations.
Test one viral or widely repeated claim against the earliest accessible source and supporting evidence; distinguish unsupported, misleading and demonstrably false statements.
Build a sourced account of one verification effort from initial claim through evidence checks, publication and correction; document unresolved uncertainties.
Follow one public claim back through citations, authorship and original records; compare what the source establishes with what later posts assert.
Examine how one platform feature affects the visibility of a defined set of content; distinguish observed ranking from unsupported claims about hidden algorithms.
Trace redistribution of one misleading claim using dated public records; distinguish origin, amplification and audience interpretation without exposing private users.
Check one image against its original date, location, caption and editing history; distinguish authentic pixels from an accurate contextual claim.
Evaluate whether learners apply a taught checking method to unfamiliar claims after a delay; compare demonstrated performance with confidence or recall.""",
"521": """Trace one soil-science concept through field observations, sampling and later revisions; distinguish historical classification from present interpretation.
Examine one influential soil study using site, depth, methods and environmental context; state the limits of transferring its findings.
Document overlooked field, laboratory or local land-management knowledge in one soil investigation; attribute contributions and obtain consent where needed.
Explain soil formation, layers and functions through a defined profile; distinguish measured properties from broad labels such as healthy soil.
Compare soil-analysis or modeling methods for a defined property; examine spatial variability, sampling depth, calibration and uncertainty.
Investigate an unexplained soil pattern using competing physical, biological and management explanations; identify measurements needed to distinguish them.
Evaluate one soil sensor or analytical method against a reference approach; compare site conditions, detection limits and maintenance requirements.
Reconstruct one soil survey or land-management research decision through field records and attributed accounts; separate documented evidence from personal inference.
Examine a dated land-use change or environmental event through soil measurements before and after; account for sampling differences.
Map how one soil sample is selected, collected, analyzed and interpreted; identify uncertainty between field conditions and laboratory results.
Explain changes in a soil practice or scientific model through repeated observations and changing evidence; avoid universal management prescriptions.
Compare one site's soil properties across two periods using consistent depth, season and method; account for land-use and sampling changes.
Assess a proposed soil technology or restoration approach through field validation, timescale and local conditions; distinguish intended from measured effects.
Test one soil-improvement claim against sampling, comparator and follow-up evidence; distinguish short-term measurements from durable change.
Build a source trail for one field investigation from site history through sampling, analysis and interpretation; retain alternative explanations.
Describe one soil profile using observed horizons, parent material and landscape position; distinguish field description from inferred formation history.
Examine a defined soil microbial measurement and its relationship to a stated function; avoid equating diversity counts with universal benefit.
Trace erosion at one site through rainfall, ground cover, slope and measured sediment evidence; distinguish local redistribution from material leaving the system.
Analyze one soil-carbon estimate using depth, bulk density, baseline and repeated measurements; distinguish concentration from total stored carbon.
Compare soil properties under defined land uses using matched sites or repeated observations; examine confounding and the time required for change.""",
"522": """Trace one air-quality measure or policy through the pollution problem and monitoring methods that shaped it; name place and period.
Examine one documented clean-air intervention using pollutant, monitoring coverage and comparison design; separate emissions changes from exposure changes.
Document overlooked monitoring, maintenance or community reporting in one air-quality case; use attributed accounts and protect private health information.
Explain emissions, ambient concentration and personal exposure through one pollutant and location; distinguish short peaks from long-term averages.
Compare methods for estimating one pollution exposure or effect; examine monitor placement, calibration, weather and uncertainty.
Investigate an unexplained pollution episode using monitoring, meteorology and source evidence; distinguish plausible attribution from established cause.
Evaluate one air-quality sensor or control technology under stated conditions; compare validation, maintenance and measured performance.
Reconstruct one air-quality decision using public mandates, monitoring evidence and consultation; distinguish official authority from stakeholder advocacy.
Follow a dated pollution episode or policy change through warnings, measured concentrations and subsequent review in one region.
Map how one pollutant moves from sources through atmospheric conditions to monitoring and public reporting; identify evidence gaps.
Explain growth or decline in one pollutant series using emissions, weather, economic activity and monitoring changes; compare alternative explanations.
Compare two periods using consistent pollutant, station coverage and averaging time; document changes in instruments and weather conditions.
Assess a proposed clean-air measure through source coverage, enforcement, monitoring and expected exposure pathways; label modeled outcomes.
Test one clean-air or unhealthy-air claim against the pollutant, averaging period, location and applicable dated standard.
Build a sourced account of one air-quality investigation from community concern through measurement, attribution and response; include remaining uncertainties.
Compare source-attribution evidence for one pollutant in a defined airshed; distinguish measured contributions from inventory assumptions.
Examine who and where one monitoring network represents; compare station placement, uptime, calibration and populations outside its coverage.
Compare indoor and outdoor measurements for a defined setting and period; examine ventilation, activities and sampling differences without assuming equivalence.
Examine one published health-burden estimate using population, exposure model, baseline risk and uncertainty; distinguish modeled attribution from individual diagnosis.
Evaluate one clean-air policy through its coverage, implementation and monitored outcomes; compare alternative causes and effects on different groups.""",
"523": """Trace one conservation approach through the species, habitat and institutions that shaped it; distinguish dated evidence from later origin narratives.
Examine one conservation project using its target species or habitat, baseline, monitoring and outcomes; test claims of recovery against the data.
Document overlooked community, fieldworker or stewardship contributions to one conservation effort; obtain consent and credit knowledge appropriately.
Explain threats, habitat condition, population measures and conservation action through a named species or site; distinguish designation from effectiveness.
Compare methods for estimating conservation outcomes using detection probability, counterfactuals, timescale and ecological variation.
Investigate an unresolved population or habitat change using competing explanations and monitoring limits; avoid assuming one intervention caused it.
Evaluate one monitoring or conservation technology in a defined deployment; compare detection, disturbance, maintenance and locally usable results.
Reconstruct one conservation decision through scientific evidence, legal powers and community participation; attribute conflicts over objectives.
Examine a dated protection measure, habitat disturbance or species assessment through its implementation and later monitoring.
Map one conservation program from threat assessment through intervention and follow-up; identify ecological and institutional dependencies.
Explain the expansion or withdrawal of one conservation approach using measured outcomes, funding and local effects rather than designation counts alone.
Compare one population or habitat across two periods using consistent survey effort, area and detection methods; state remaining uncertainty.
Assess a proposed conservation action through threat reduction, land access, ecological timescale and monitoring requirements; distinguish forecasts from observed recovery.
Test one biodiversity success claim against the species, site, baseline and monitoring evidence; examine displacement of threats or burdens.
Build a sourced account of one conservation intervention through planning, action and ecological follow-up; include affected communities' perspectives.
Examine the evidence for one named species' or habitat's threats; distinguish direct observations, inferred drivers and uncertainty about their relative importance.
Evaluate one habitat corridor using movement, habitat quality and land-use evidence; distinguish mapped connection from demonstrated ecological use.
Compare restoration objectives and observed outcomes at one site; examine reference conditions, time, maintenance and effects on existing users.
Trace community decision rights, benefits and responsibilities in one stewardship arrangement; use consented local accounts alongside program records.
Audit one biodiversity survey for location, season, observer effort and detection bias; identify which species or habitats its conclusions cannot represent.""",
"524": """Trace one regional food system through changes in production, processing and distribution; define the foods, geography and historical period.
Examine one food-system intervention through farmer, worker and consumer outcomes; compare claimed benefits with its chosen system boundary.
Document overlooked labor or knowledge in one food supply chain; use consented accounts and distinguish paid work from household or informal labor.
Explain production, processing, distribution and consumption through one food product; distinguish physical flows, prices and nutritional access.
Compare food-system analyses using consistent functional units, lifecycle boundaries, allocation and assumptions about waste or substitution.
Investigate one unexplained price, supply or loss pattern using production, trade and distribution evidence; compare multiple causes.
Evaluate one farming, processing or logistics technology in a defined food chain; include resource use, operating costs and effects on access.
Reconstruct one food policy or supply-chain decision through documented authority, incentives and affected participants' accounts.
Examine a dated harvest shock, trade change or infrastructure event through its effects on one regional food chain; state comparison limits.
Map one food from farm inputs through processing, transport, retail and consumption; identify handoffs, losses and evidence gaps.
Explain expansion or decline of one food-system practice using production, demand, policy and market evidence; avoid a single-cause account.
Compare one regional food chain across two periods using consistent products, prices, quantities and system boundaries.
Assess a proposed food-system change through land, labor, processing, distribution and consumer access requirements; label tradeoffs and assumptions.
Test one sustainable-food or food-security claim against its metrics, geography and supply-chain boundary; distinguish availability from affordability.
Build a sourced account of one regional food chain or disruption; connect producer records, worker experience and consumer access.
Examine one crop's or product's inputs in a defined region and season; compare material use, costs and environmental measures within stated boundaries.
Trace one processing stage through inputs, outputs, safety controls and resource use using published records; distinguish measured losses from assumed waste.
Follow one food product through storage and distribution; examine time, temperature, transport cost and access without prescribing handling beyond verified guidance.
Measure loss at a defined food-chain stage using consistent definitions and material accounting; distinguish avoidable loss, inedible material and diverted uses.
Examine whether a defined population can obtain nutritionally relevant foods; compare price, availability, household resources and access barriers.""",
"525": """Trace one fishery's management from earlier access arrangements through dated rules and stock assessments; name species, stock and jurisdiction.
Examine one fisheries-management intervention using stock, catch and livelihood evidence; distinguish a case study from proof of universal sustainability.
Document overlooked fishers, processors or community knowledge in one fishery; obtain consent and credit sources without exposing sensitive locations.
Explain stock, catch, fishing effort and management through one named fishery; distinguish species-wide labels from local stock conditions.
Compare assessment methods for one fish stock using data coverage, selectivity, uncertainty and model assumptions; state consequences for advice.
Investigate an unexplained change in catch or stock estimates using effort, environment and reporting evidence; distinguish competing causes.
Evaluate one monitoring or fishing technology using a defined fishery's catch, bycatch and operating evidence; examine unintended effects.
Reconstruct one management decision through assessments, legal authority and fisher participation; attribute disagreement and documented tradeoffs.
Follow a dated quota change, closure or stock reassessment through implementation and later monitoring; avoid judging success from one season.
Map one fishery from access rules and harvesting through landing, reporting and sale; identify custody and accountability gaps.
Explain growth or contraction of one fishery using stock, effort, market and policy evidence; distinguish ecological from reporting changes.
Compare two periods using consistent stock boundaries, survey methods and effort measures; document changes in assessments.
Assess one proposed fishery measure through enforcement, stock response, livelihoods and monitoring requirements; present outcomes conditionally.
Test one sustainable-seafood claim against the exact stock, gear, jurisdiction and assessment date; examine traceability and evidence limitations.
Build a sourced account of one management cycle from assessment through decision, fishing season and review; include affected communities' accounts.
Examine one stock assessment's survey, catch and biological inputs; compare uncertainty, missing data and sensitivity to assumptions.
Analyze bycatch for a defined gear, species and fishery using observation coverage and mortality estimates; avoid generalizing beyond the measured context.
Examine access, income and decision participation for a named small-scale fishery; compare formal rules with consented community experience.
Trace one seafood product from landing through sale using custody records; distinguish documented origin from unsupported labeling.
Compare one management choice's ecological, income and access effects for defined groups; state the objectives and uncertainties behind the tradeoff.""",
"516": """Trace one labor protection from the workplace problem it addressed through legislation and implementation; name jurisdiction, sector and employment status.
Examine one documented labor-rights intervention through coverage, enforcement and worker outcomes; distinguish legal entitlement from practical access.
Document overlooked organizing, interpretation or support work in one labor case; use consented accounts and protect workers from unnecessary identification.
Explain one workplace right through published rules and a documented process; distinguish employees, contractors and jurisdiction-specific eligibility.
Compare methods for assessing enforcement of one labor protection; examine complaint selection, informal work, reporting gaps and outcome measures.
Investigate a gap between a stated right and recorded workplace practice; compare enforcement, eligibility and employer or worker accounts.
Evaluate one payroll, scheduling or reporting technology against a defined labor-rights problem; examine transparency, access and dispute records.
Reconstruct one bargaining or policy decision through attributed records; distinguish worker representation, employer authority and government powers.
Examine a dated law, judgment or collective agreement through changes in coverage and enforcement; avoid treating one outcome as a universal rule.
Map how a worker learns of, claims and seeks enforcement of one right; identify deadlines, agencies and support in a named jurisdiction.
Explain expansion or weakening of one protection using policy, enforcement and employment records; compare competing explanations.
Compare one labor protection across two periods using consistent worker classifications, sectors and enforcement measures.
Assess a proposed labor reform through coverage, administration, enforcement and worker access; distinguish draft provisions from enacted rules.
Test one public claim about workplace rights against the relevant dated law, agreement or decision; avoid case-specific legal conclusions.
Build a sourced account of one workplace-rights case from the original issue through review and remedy; include consented affected voices.
Examine one bargaining process through representation rules, negotiations and the resulting agreement; distinguish negotiated terms from general legal minimums.
Trace one pay-protection issue through wage definitions, records, complaint handling and remedy; name jurisdiction and worker status.
Compare published working-time rules with documented schedules in one sector; examine exemptions, record quality and actual enforcement.
Examine how a named jurisdiction classifies one type of work arrangement; compare legal criteria, contracts and documented decisions without advising an individual case.
Follow one grievance route through submission, review, appeal and outcome; examine accessibility, retaliation concerns and limits of available records.""",
"517": """Trace one occupational safety system from a documented hazard or incident through rule and practice changes; define the industry and jurisdiction.
Examine one safety program using hazard controls, exposure or incident measures and evaluation limits; avoid treating low reports as proof of safety.
Document overlooked prevention, maintenance or worker-reporting activity in one workplace; use consented accounts and protect identifiable personal information.
Explain hazard identification, control, reporting and review through a published workplace example; avoid substituting editorial content for site training.
Compare safety measures used in one evaluation, including exposure, near misses and harm; examine reporting incentives and undercounting.
Investigate an unresolved difference between a safety procedure and observed outcomes using published records; distinguish documented factors from speculation.
Evaluate one safety technology under a defined task and setting; compare validation, maintenance and worker interaction with existing controls.
Reconstruct one safety decision using published responsibilities, worker consultation and investigation records; avoid unsupported personal blame.
Follow a dated incident, rule change or equipment redesign through investigation and corrective action; use official findings where available.
Map how a workplace identifies a hazard, chooses controls, checks performance and responds to reports; identify responsible roles.
Explain the adoption or withdrawal of one safety approach using incident, exposure, cost and implementation evidence; distinguish correlation from cause.
Compare safety outcomes across two periods using equivalent work hours, tasks, exposure measures and reporting rules.
Assess a proposed workplace safety intervention through task-specific evidence, control design, training and verification requirements; avoid certifying its suitability.
Test one safety claim against its measurement period, denominator and reporting conditions; examine what the metric cannot establish.
Build a sourced account of one prevention effort from worker reports through investigation, action and follow-up; retain unresolved questions.
Examine how one published assessment identifies and prioritizes hazards for a defined task; discuss reasoning without giving unsafe operating instructions.
Trace the evidence and causal findings in one public incident investigation; distinguish contributing system conditions from unproven allegations.
Evaluate one training program using task understanding, observed practice and follow-up evidence; distinguish attendance from demonstrated competence.
Compare protective design options described in a published case using exposure, usability and maintenance evidence; defer implementation to qualified site review.
Examine how workers report concerns and influence prevention in one documented system; include access, response, confidentiality and retaliation concerns.""",
"518": """Trace one cooperative from its founding need through changes in membership, ownership and trading activity; use bylaws and dated business records.
Examine one cooperative's documented performance using member benefits, finances and governance; test whether the case represents its wider sector.
Document overlooked member, administrative or community labor in one cooperative; obtain consent and distinguish paid from voluntary work.
Explain membership, voting, capital and surplus through one cooperative's actual rules; distinguish its model from other cooperative forms.
Compare methods of measuring cooperative success using financial resilience, member participation and distribution; identify conflicting objectives.
Investigate a gap between cooperative principles and practice in one organization; compare bylaws, decisions and attributed member accounts.
Evaluate one digital or production tool within a cooperative using member access, operating results and governance implications.
Reconstruct one board or membership decision through proposals, voting and implementation records; distinguish formal rights from practical influence.
Examine a dated merger, conversion or crisis through its effects on membership, finances and control; compare original aims with outcomes.
Map how one cooperative admits members, raises capital, makes decisions and distributes results; identify accountability and exit routes.
Explain growth or decline of one cooperative using market, financing, governance and membership records; avoid assuming ownership form determines success.
Compare one cooperative across two periods using consistent accounting and membership definitions; account for changes in products or sector conditions.
Assess a proposed cooperative model through capital, membership, governance and market requirements; distinguish aspirations from enforceable rights.
Test one claim about democratic ownership or shared benefits against the cooperative's rules and actual distributions.
Build a sourced account of one cooperative decision from member need through negotiation, implementation and outcome; include dissenting member perspectives.
Examine how members vote, stand for office, obtain information and challenge decisions in one cooperative; compare written rules with participation.
Trace one cooperative's financing through member contributions, borrowing and retained surplus; examine obligations and effects on member control.
Compare the stated surplus-allocation formula with actual member and organizational distributions over a defined accounting period.
Examine one cooperative competing in a defined market using prices, service, access and operating costs; compare like-for-like alternatives.
Investigate one cooperative's closure or restructuring using audited records and attributed accounts; separate governance, market and financing explanations.""",
"519": """Trace one poverty or inequality measure through its original policy purpose and methodological changes; distinguish changing definitions from changing living conditions.
Examine one documented poverty-reduction initiative using eligibility, comparison methods and household outcomes; identify whose circumstances the findings represent.
Document experiences missing from a public poverty narrative using consented accounts and household evidence; avoid stereotypes or unnecessary personal exposure.
Explain income, wealth, deprivation and inequality through a defined dataset; distinguish household averages from individual circumstances.
Compare analytical methods for one distributional question, including equivalence scales, price adjustment, sampling and treatment of missing wealth.
Investigate one unexplained change in poverty or inequality using alternative datasets and definitions; identify evidence that could distinguish causes.
Evaluate one data or service technology against a defined access problem; examine exclusion, privacy and measured household outcomes.
Reconstruct one policy or measurement decision using public records and affected households' perspectives; separate stated aims from demonstrated effects.
Examine a dated economic shock or social-policy change using comparable household measures before and after; state causal limitations.
Map how one dataset is collected, adjusted and used to classify household conditions; identify exclusions and uncertainty.
Explain growth or decline in one measured gap using earnings, prices, housing, transfers and population evidence; compare competing explanations.
Compare distribution across two periods using consistent units, household definitions and prices; account for revisions and survey coverage.
Assess a proposed anti-poverty intervention through eligibility, delivery, financing and evaluation requirements; present assumptions rather than promised results.
Test one poverty or inequality headline against its denominator, threshold and source data; distinguish percentage changes from household counts.
Build a sourced account of one household-support policy from proposal to delivery and follow-up; include consented experiences and administrative evidence.
Compare poverty thresholds for a named place and period; explain price basis, household adjustment and which deprivations each measure misses.
Examine how rent, utilities and other housing costs change a defined group's disposable resources; compare conditions before and after housing costs.
Analyze one wealth dataset by asset type, debt and household group; examine missing high wealth, valuation uncertainty and ownership differences.
Study mobility for a defined cohort using linked outcomes and consistent parental-background measures; distinguish population patterns from individual stories.
Evaluate one policy's distributional effects using a stated comparator and follow-up period; include take-up, exclusions and uncertainty about attribution.""",
"520": """Trace one government's budget process from its legal and institutional origins through a defined reform; distinguish formal rules from spending practice.
Examine one public budget initiative using appropriations, actual spending and service outcomes; state fiscal year, government level and accounting basis.
Document overlooked finance, audit or community-monitoring work in one budget case; credit attributed contributions and distinguish access from influence.
Explain revenue, appropriation, expenditure and audit through one published budget; separate planned spending from money actually paid.
Compare methods used to assess one budget choice, including accounting boundaries, inflation, liabilities and distributional effects.
Investigate one discrepancy between budget promises and service delivery using execution and audit records; identify missing or incomparable data.
Evaluate one digital budget or procurement system through transparency, access, data quality and actual decision use; avoid equating publication with accountability.
Reconstruct one spending decision through proposals, committee records and approval authority; attribute competing priorities and documented amendments.
Examine one dated budget reform, emergency appropriation or revenue shock through its implementation and subsequent audit.
Map one spending item from proposal and appropriation through procurement, payment and service delivery; identify institutional responsibilities.
Explain growth or contraction of one budget line using scope, prices, eligibility and execution data; distinguish reclassification from real change.
Compare two fiscal periods using consistent government boundaries, accounting treatment and price levels; flag revisions and one-off items.
Assess one proposed budget measure through financing, legal authority, implementation capacity and monitoring; distinguish forecasts from committed funds.
Test one public spending claim against original budget and execution documents; identify fiscal period, denominator and omitted obligations.
Build a sourced timeline for one public expenditure from promise through approval, delivery and audit; document unresolved findings.
Examine one government's revenue sources and their stated incidence over a defined fiscal period; distinguish projections, collections and arrears.
Trace one budget negotiation through proposals, amendments and recorded votes; distinguish announced priorities from final appropriations.
Follow one public contract through tender, award, changes and delivery using lawful public records; separate allegations from substantiated audit findings.
Examine one audit finding through the evidence, agency response and follow-up; distinguish financial irregularity, poor performance and established wrongdoing.
Assess one participatory-budget process using eligibility, access, proposals, decisions and delivered projects; examine which residents could influence outcomes.""",
"511": """Trace one semiconductor device or fabrication method from its original engineering problem through documented demonstrations and production changes.
Examine one influential chip using its intended workload, architecture, manufacturing context and measured performance; avoid treating one benchmark as universal.
Document overlooked fabrication, testing or packaging contributions within one chip program; use attributed technical records and worker accounts.
Explain design, fabrication, packaging and testing through one device type; distinguish a chip design from a manufacturing process node.
Compare one architectural or process tradeoff using power, performance, area and yield measurements under explicitly matched conditions.
Investigate a documented gap between expected and measured device behavior; compare test conditions and published explanations without inventing proprietary details.
Evaluate one semiconductor innovation against a stated baseline and workload; distinguish laboratory demonstration, qualification and production availability.
Reconstruct one chip-design or manufacturing-investment decision using public technical and business records; attribute the constraints described by participants.
Examine a dated fabrication milestone, supply disruption or policy decision through its effects on a specific device or production chain.
Map one chip from design files through fabrication, packaging and test; identify the role and evidence available at each stage.
Explain the adoption or decline of one device architecture using workload, cost, manufacturing and software-support evidence.
Compare two chip generations on equivalent workloads and measurement conditions; account for manufacturing, memory and system-level differences.
Assess a proposed semiconductor advance through required materials, tools, validation and production scale; distinguish targets from achieved results.
Test one chip-performance or process-node claim against its definitions and benchmark setup; separate marketing labels from measured device properties.
Build a sourced account of one chip's development, qualification and deployment; identify which production or performance claims remain unverified.
Examine how one architectural choice changes execution on a defined workload; compare memory access, parallelism, power and baseline implementation.
Follow one published fabrication process at an explanatory level; identify inputs, process control and inspection without presenting proprietary operating recipes.
Analyze yield measurements for a defined product and production stage; distinguish defect mechanisms, test rejection and assumptions about economic viability.
Compare packaging approaches for a specified device or system; examine thermal, interconnect, reliability and testing tradeoffs.
Trace a critical material or production input through a defined chip supply chain; use dated capacity and dependency evidence without assuming global substitutability.""",
"512": """Trace one quantum-computing idea from its theoretical task through a documented experiment; distinguish the original proposal from later hardware claims.
Examine one widely cited quantum demonstration using its task, device, comparison method and uncertainty; state what practical use it did not establish.
Document overlooked calibration, control or verification work in one experiment; credit contributors through publications and attributed accounts.
Explain qubits, operations, measurement and error through one defined experiment; distinguish quantum computing from ordinary parallel processing.
Compare resource and error estimates for one quantum task; separate physical qubits, logical qubits, circuit depth and classical verification costs.
Investigate one unresolved result or scalability question using published experiments and competing interpretations; identify a test that could resolve it.
Evaluate one new quantum hardware or control method against a defined baseline; distinguish component improvement from useful computational advantage.
Reconstruct one research or engineering decision through papers, funding records and attributed accounts; distinguish stated goals from achieved milestones.
Follow a dated quantum milestone through its original publication, replication and later interpretation; avoid turning announcements into settled outcomes.
Map preparation, control, execution and readout in one quantum experiment; identify where errors and validation enter the process.
Explain changing support for one quantum approach using measured performance, resource needs and independent results rather than publicity volume.
Compare two dated demonstrations using consistent task, error and resource definitions; describe where the devices cannot be directly compared.
Assess a proposed quantum application through algorithm, error correction, hardware and input-output requirements; label untested assumptions.
Test one quantum-advantage claim against its original task and classical comparison; distinguish theoretical speedup from measured end-to-end usefulness.
Build a sourced sequence from one proposed quantum experiment through execution, analysis and criticism; include unresolved verification questions.
Compare qubit platforms on the same stated experimental criteria; examine control, connectivity, coherence and measurement without declaring a universal winner.
Examine one error-correction experiment using code, logical error rate and resource overhead; distinguish error detection from sustained fault-tolerant computation.
Audit one benchmark's task selection, sampling, baseline and verification; identify whether its performance measure matches the public claim.
Evaluate the assumptions and resource requirements of one quantum algorithm for a named problem; include data preparation and classical alternatives.
Trace scaling constraints in one hardware design through control, calibration, interconnects and error; distinguish component counts from usable computational capacity.""",
"513": """Trace one interaction technique from its original user task through design and evaluation; distinguish prototype influence from widespread adoption.
Examine one documented interface using user population, task, environment and measured outcomes; assess whether its success transfers to other contexts.
Document overlooked participants, accessibility specialists or support workers in one interface project; use consented accounts and credit their contributions.
Explain users, tasks, interfaces and feedback through one bounded interaction; distinguish visual preference from successful and accessible use.
Compare usability-study methods for one interaction question; examine participant selection, task realism, learning effects and measurement uncertainty.
Investigate a mismatch between a usability test and real-world behavior; compare context, incentives, training and excluded user groups.
Evaluate one interaction technology on defined tasks with appropriate users; compare errors, accessibility, workload and fallback options.
Reconstruct one design decision using research findings, constraints and stakeholder authority; distinguish user consultation from decision-making power.
Examine a dated interface redesign or policy change through its effect on task completion and access; use comparable observation periods.
Map one user's task from goal through actions, feedback, error and recovery; identify system and organizational handoffs.
Explain adoption or abandonment of one interaction pattern using observed use, support records and alternatives; avoid treating popularity as usability.
Compare two interface versions on the same tasks and user conditions; account for familiarity, training and changes in underlying functionality.
Assess a proposed interface through user research, accessibility, evaluation and maintenance requirements; separate demonstration from validated benefit.
Test one intuitive-design or frictionless-use claim against task evidence; examine user diversity, error rates and conditions excluded from the claim.
Follow one consented design project from user research through prototypes, testing and revision; explain how evidence changed decisions.
Examine how one project recruits and studies users; compare the sample with intended users and identify who is missing.
Analyze one interaction error using the task sequence, feedback and recovery path; examine design conditions without assigning blame to users.
Evaluate a defined interface with users who have relevant access needs; compare conformance evidence with observed task performance.
Study how one interface communicates system state, uncertainty or failure; compare user expectations with actual behavior and available recourse.
Follow one design iteration through the original problem, change and retest; distinguish measured improvement from a cosmetic revision.""",
"514": """Trace one open-source project from its founding problem through releases and governance changes; use repository and licensing records.
Examine one influential project through documented use, maintenance and support conditions; distinguish download counts from sustainable adoption.
Document overlooked review, documentation, translation or release work in one project; credit maintainers and contributors from public records.
Explain code access, licensing, contribution and maintenance through one project; distinguish permission to use from promises of support.
Compare ways of measuring one project's health using activity, review, dependencies and concentration of responsibility; state the limits of each metric.
Investigate one unresolved maintenance or adoption problem through issues, release history and competing explanations; respect private contributor information.
Evaluate one development or security tool in a defined project workflow; compare verification, workload and observed outcomes before and after use.
Reconstruct one license, release or governance decision through recorded proposals and discussion; attribute disagreements and formal authority.
Examine a dated fork, license change or major incident through repository and governance records; distinguish events from later interpretations.
Map one contribution from issue to review, merge, release and user update; identify decision rights and maintenance responsibilities.
Explain growth, stagnation or abandonment of one project using maintenance capacity, dependencies, funding and adoption evidence.
Compare two project periods using consistent release, contribution and support measures; account for migrations and changes in data collection.
Assess a proposed project model through funding, governance, review and succession requirements; avoid predicting sustainability from initial attention.
Test one claim that open code is automatically secure or supported against a defined project's processes and evidence.
Build a source trail for one project change from proposal through release and user impact; include review decisions and unresolved issues.
Compare the permissions and obligations of licenses actually used by a named project and version; distinguish explanation from case-specific legal advice.
Examine how review, support and release duties are distributed in one project; use consented accounts and public activity without equating commits with labor.
Trace who can propose, approve, reject and appeal changes in one project; compare written governance with documented decisions.
Follow one publicly disclosed vulnerability through reporting, triage, fix and user notification; exclude exploit instructions and private reports.
Assess one project's funding, dependency burden and succession plans using dated evidence; distinguish present activity from long-term resilience.""",
"515": """Trace one internet governance institution or rule through its founding problem and later changes; distinguish technical coordination from state or platform authority.
Examine one documented governance decision through procedures, participants and implementation; assess whose access or interoperability was affected.
Document overlooked implementers, civil-society participants or affected users in one policy process; credit attributed contributions and representation limits.
Explain standards, addressing, domain names and policy authority through one concrete process; distinguish organizations with different mandates.
Compare governance models for one internet issue using decision rights, participation, enforcement and accountability; avoid treating consultation as equal influence.
Investigate an unresolved interoperability or authority dispute using public technical and policy records; attribute competing positions and dates.
Evaluate how one protocol or coordination tool changed a defined network problem; compare deployment, compatibility and operator constraints.
Reconstruct one standards or policy decision through proposals, objections and recorded authority; distinguish individual advocacy from institutional agreement.
Examine a dated internet coordination or regulatory decision through implementation records and affected users' experience in one jurisdiction.
Map how one internet rule moves from proposal to decision and implementation; identify which bodies can enforce it and where authority ends.
Explain adoption or rejection of one governance approach using deployment, incentives, legal constraints and participant records.
Compare governance across two periods using the same issue, institutional roles and participation measures; document changes in the network itself.
Assess a proposed internet-governance change through jurisdiction, implementation, participation and interoperability requirements; label unresolved negotiations.
Test one claim that a single institution controls the internet against the actual technical and legal powers involved in a named case.
Build a documented account of one governance dispute from initial proposal through decision, implementation and appeal; retain competing accounts.
Trace one protocol standard through drafts, review and deployment; distinguish an accepted specification from widespread implementation.
Follow one domain-name decision through allocation, administration and dispute procedures; identify the roles of registries, registrars and coordinating bodies.
Examine one network-neutrality rule in a defined jurisdiction and period; compare its text, enforcement and available traffic or market evidence.
Trace one cross-border internet rule through the jurisdictions, operators and users it affects; distinguish legal obligations from technical feasibility.
Evaluate participation in one multistakeholder process using attendance, resources, agenda access and recorded influence; examine whose voices remain absent.""",
"506": """Trace one city's rental or tenancy system through dated housing policies and market conditions; distinguish legal changes from actual access.
Examine one housing program using eligibility, delivered units, affordability and tenure outcomes; identify which households the evaluation represents.
Document overlooked tenant, maintenance or organizing work within one housing case; use consented accounts and avoid exposing vulnerable residents.
Explain rent, tenancy, deposits and housing quality through one jurisdiction's published rules and records; distinguish explanation from personal legal advice.
Compare housing affordability measures using rent, income, household composition and unavoidable costs; explain why different measures yield different pictures.
Investigate one unexplained rent or access pattern using supply, household and policy data; compare plausible causes without assuming a single driver.
Evaluate one housing-access technology or building intervention using tenant experience, operating costs and measured performance; examine exclusion and privacy.
Reconstruct one landlord, tenant-group or public-authority decision using documented powers, consultation and outcomes; attribute competing accounts.
Examine a dated housing reform, eviction shock or development decision in one place; compare affected households' conditions before and after.
Map how a household finds, applies for, occupies and leaves a rental home; identify fees, eligibility checks and dispute routes.
Explain changes in one rental sector or housing scheme using financing, regulation, demand and upkeep records; examine alternative explanations.
Compare housing conditions across two periods using consistent boundaries, unit types and household measures; account for inflation and quality changes.
Assess one proposed housing intervention through land, finance, delivery, maintenance and tenant access requirements; distinguish targets from completed homes.
Test one public housing or rent claim against its dataset, geography and definition; separate advertised listings from actual tenancies.
Follow one consented tenancy or housing-policy case through applications, decisions and outcomes; use documents alongside residents' accounts.
Compare rents with household incomes and unavoidable housing costs in a defined market; report distribution and data exclusions rather than one average.
Examine how one tenancy arrangement handles renewal, notice and dispute in a named jurisdiction; compare written rules with documented implementation.
Assess one housing-quality issue through inspection records, resident accounts and repair timelines; avoid diagnosing building safety from images alone.
Trace one eviction process through notice, review, support and outcome using lawful public records and consented testimony; protect personal details.
Evaluate the accessibility of a defined housing scheme from application through daily use; include physical access, communication and support requirements.""",
"507": """Trace one water or sanitation system from its original service problem through construction and expansion; compare design promises with delivery records.
Examine one documented utility project using service coverage, reliability and water-quality evidence; state the population and reporting period.
Follow overlooked operators, maintenance workers or underserved households in one system; use attributed accounts and protect sensitive facility information.
Explain collection, treatment, distribution and sanitation through one utility network; distinguish infrastructure presence from safely delivered service.
Compare methods for estimating service reliability and treatment performance; examine sampling, intermittent supply, losses and missing users.
Investigate one unresolved service or quality problem using monitoring and operational records; compare explanations without supplying tampering instructions.
Evaluate one treatment or monitoring technology under actual operating conditions; compare measured results, upkeep and staff requirements.
Reconstruct one utility investment or service-allocation decision using published mandates, budgets and consultation; include affected communities' accounts.
Examine one service expansion, drought response or sanitation reform through dated records; compare actual coverage and continuity with stated goals.
Map water or waste flow through one system and its institutional handoffs; identify where measurement and accountability change.
Explain why one utility approach expanded or failed using finance, maintenance, staffing and demand evidence; distinguish technical from governance causes.
Compare service across two periods using consistent quality, coverage and reliability definitions; account for changed sampling or network boundaries.
Assess a proposed water or sanitation upgrade through source availability, treatment, operations, affordability and monitoring requirements.
Test one safe-water or sanitation-coverage claim against sampling locations, service continuity and population definitions; identify unmeasured households.
Build a sourced account of one service project from planning through operation; include household experience, monitoring results and unresolved problems.
Follow water from one source through treatment and distribution to users; compare sampling points and losses without publishing sensitive vulnerabilities.
Trace wastewater collection, treatment and discharge in one system; compare permitted targets, actual measurements and periods of bypass or missing data.
Map service access for a defined settlement or group; compare connection status with reliability, affordability and usable sanitation.
Examine one water-quality monitoring program using contaminant definitions, sampling frequency and reporting limits; avoid judging safety from appearance.
Trace one utility decision through mandates, tariff setting, funding and complaint handling; examine whether households can obtain explanations and remedies.""",
"508": """Trace one municipality's waste system from earlier disposal practices to a dated reform; use service and policy records rather than tidy progress narratives.
Examine one waste-management program through collection coverage, material destinations and verified recovery; include operating costs and data limits.
Document overlooked waste workers or informal collectors within one material stream; use consented accounts and credit their contribution.
Explain one waste stream from household disposal through collection, sorting, treatment and final destination; distinguish collection from recycling.
Compare material-flow or lifecycle estimates for one waste option using consistent boundaries, contamination assumptions and transport distances.
Investigate one unexplained discrepancy in waste or recycling figures; compare weighing, reporting, stock changes and downstream destination records.
Evaluate one sorting or treatment technology under actual feedstock and operating conditions; include reject fractions, maintenance and resource use.
Reconstruct one disposal-site, contract or collection decision using procurement records and community input; attribute interests and stated reasons.
Examine a dated waste policy or facility change using collection, processing and destination records before and after implementation.
Map one municipal waste stream and the organizations handling each stage; identify custody transfers and gaps in destination evidence.
Explain the growth or withdrawal of one waste-management approach using contracts, markets, contamination and operating results.
Compare waste performance across two periods using consistent material definitions, population coverage and destination accounting.
Assess one proposed waste intervention through collection design, processing capacity, markets, residual disposal and worker conditions.
Test one zero-waste or recycling claim against its material boundary and downstream records; distinguish diversion from demonstrated recovery.
Follow one material through a documented disposal journey; connect household choices, worker activity and verified treatment or final disposal.
Examine which households receive usable collection service in one area; compare schedules, access constraints, fees and missed pickups.
Track losses and contamination through one sorting process using measured inputs and outputs; distinguish saleable material from total intake.
Examine one landfill's published monitoring and management records over a defined period; distinguish measured impacts from assumptions about all landfills.
Follow informal workers' role in one recovery system through consented accounts and material-flow evidence; examine pay, recognition and access changes.
Compare an original product and a redesign across collection, sorting and downstream processing; test compatibility with the local system actually available.""",
"509": """Trace one city's adaptation measure from documented hazard assessment through planning and delivery; distinguish historical conditions from projected risk.
Examine one completed adaptation project using the hazard, exposed population and measured performance; compare results with the original objectives.
Document overlooked residents or maintenance workers in one adaptation project; include consented accounts of burdens and uneven protection.
Explain hazard, exposure, vulnerability and adaptation through one neighborhood; distinguish a planned intervention from demonstrated risk reduction.
Compare methods for estimating one project's protection using baselines, counterfactuals, event severity and distribution of benefits.
Investigate an unresolved difference between predicted and observed protection; examine maintenance, hazard intensity, exposure and measurement gaps.
Evaluate one adaptation technology in its actual urban setting; compare operational performance, upkeep and who can use the protection.
Reconstruct one adaptation investment decision using risk assessments, budgets and public input; distinguish formal participation from influence.
Follow one heat event, flood or policy change through warnings, infrastructure performance and recovery records in a defined neighborhood.
Map how one adaptation measure is designed, funded, maintained and evaluated; identify responsibility for failures and follow-up.
Explain why one adaptation approach gained or lost support using performance, cost, maintenance and community records.
Compare neighborhood risk across two periods using consistent hazard and exposure measures; account for development and population changes.
Assess a proposed adaptation measure under stated climate, population and maintenance scenarios; identify assumptions that determine its usefulness.
Test one climate-resilience claim against the specific hazard, design conditions and performance evidence; avoid treating certification as proof of protection.
Build a sourced account of one adaptation project from risk identification through a documented event or evaluation; include remaining vulnerabilities.
Examine one urban heat intervention using temperature, exposure and access measurements; distinguish shaded surfaces from reduced personal heat burden.
Trace rainfall, runoff and drainage performance during one documented event; compare design assumptions, blockage records and affected locations.
Assess one coastal adaptation proposal using the named hazard, location and planning horizon; examine residual risk, access and displaced impacts.
Evaluate one green-infrastructure project using maintenance, water or heat performance and land-use records; include benefits and burdens for nearby residents.
Compare adaptation benefits and costs between defined groups; examine who participates, who remains exposed and whether protection shifts risk elsewhere.""",
"510": """Trace maintenance responsibility for one bridge, pipe or public facility through dated standards, budgets and ownership changes; avoid judging condition from age alone.
Examine one documented maintenance program using inspections, completed work and service reliability; compare its results with stated targets.
Follow overlooked inspection, cleaning or repair work on one asset; use attributed accounts and published records without operational vulnerability details.
Explain inspection, prioritization, repair and renewal through one public asset; distinguish routine maintenance from reconstruction or safety certification.
Compare condition and failure-risk models used for one asset class; examine assumptions, incomplete records and consequences of misclassification.
Investigate one unexplained service fault using authorized inspection and maintenance records; separate documented causes from visual speculation.
Evaluate one inspection or maintenance technology against an established method; compare detection limits, validation and operational requirements.
Reconstruct one maintenance-priority decision using inspection findings, budgets and service obligations; distinguish recorded reasons from assumed motives.
Examine a dated closure, inspection reform or funding decision and its effect on one asset's maintenance; use official reviews where available.
Map how a reported defect becomes an inspection, work order, repair and follow-up check; identify responsibility at every handoff.
Explain expansion or neglect of one maintenance program using funding, staffing, procurement and condition records; avoid a single-cause failure story.
Compare asset condition and service across two periods using consistent inspection grades, network size and maintenance accounting.
Assess a proposed maintenance strategy through inspection coverage, workforce, parts, funding and follow-up; frame reliability expectations conditionally.
Test one claim about infrastructure condition or repair savings against its inspection data and lifecycle assumptions; do not infer safety from photographs.
Build a sourced timeline of one public asset's defect, investigation and authorized repair; distinguish established findings from unresolved causes.
Examine inspection intervals and follow-up for a defined asset class; compare required checks, completed checks and documented reasons for delay.
Trace one backlog from identified defects through prioritization and funding; distinguish deferred work from work no longer required.
Examine one asset register's coverage, ownership and condition fields; identify how missing or outdated entries affect maintenance decisions.
Review precursors described in one published engineering investigation; explain their evidential role without offering unsupervised inspection or repair instructions.
Follow one maintenance-related outage through notice, alternative service and restoration; measure duration and impacts on defined users.""",
"501": """Trace one population-health program from the problem it addressed to its first implementation; distinguish contemporary records from later success stories.
Examine one documented prevention program, its target population, evaluation design and measured outcomes; test whether its results apply elsewhere.
Follow an overlooked contribution by community workers or residents to one public-health response; use attributed accounts and program records.
Explain surveillance, prevention and service delivery through one local program; distinguish population measures from individual diagnosis or treatment.
Compare methods used to estimate one program's effect, including comparison groups, confounding, missing data and unequal exposure.
Investigate one unresolved program-outcome question using competing explanations and available surveillance records; identify what evidence would distinguish them.
Evaluate one public-health tool in a defined deployment; compare uptake, data quality and measured outcomes with the earlier process.
Reconstruct one public-health decision, the formal decision makers and community input; separate their stated aims from observed results.
Follow a dated outbreak, policy change or funding decision in one place; compare service and outcome records before and after.
Map how one public-health program identifies need, allocates resources, delivers prevention and monitors results; name each responsible organization.
Explain the expansion or withdrawal of one program using funding, participation, delivery and evaluation records; consider competing causes.
Compare one population-health measure across two periods using consistent case definitions, age structure and reporting coverage.
Assess one proposed public-health change through its staffing, access, funding and evaluation requirements; present outcomes as conditional scenarios.
Test one public claim about a prevention program against its original evaluation; distinguish relative effects, absolute effects and uncertainty.
Build a sourced timeline of one community program from proposal to follow-up; include residents' experiences and documented unintended effects.
Follow one disease-surveillance system from case definition through reporting and action; examine missed cases, delays and changing testing coverage.
Examine a vaccination delivery program's eligibility, outreach, supply and uptake records; separate delivery performance from claims about individual care.
Compare versions of one health message, its intended audience and comprehension evidence; examine language access and unintended interpretations.
Evaluate one community prevention intervention with a defined population, baseline and follow-up; distinguish program participation from demonstrated benefit.
Compare outcomes between defined groups in one program using denominators, exposure and access data; investigate reporting gaps and structural explanations.""",
"502": """Trace one rehabilitation service from its original patient need through changes in goals, professional roles and delivery; name the condition and setting.
Examine one documented rehabilitation pathway using eligibility, participation and functional outcome data; state which patients the findings describe.
Follow patients' or therapists' overlooked work within one rehabilitation service; use consented accounts and avoid treating one experience as representative.
Explain assessment, goal setting, therapy and follow-up in one care pathway; describe roles without prescribing exercises or individual treatment.
Compare functional outcome measures used in one rehabilitation study; examine baseline differences, follow-up duration and clinically meaningful change.
Investigate an unexplained gap in one rehabilitation pathway using service records and competing explanations; identify missing follow-up evidence.
Evaluate a rehabilitation technology in a defined task and patient group; distinguish laboratory performance, clinical implementation and everyday use.
Reconstruct one decision about access, goals or service design using clinicians' records and patients' stated priorities; avoid attributing motives without evidence.
Examine one service reorganization or policy change and its effects on continuity and access; use comparable records across the change.
Map referrals, assessment, therapy, discharge and community support for one pathway; identify responsibility at each handoff.
Explain why one rehabilitation approach expanded or declined using evidence, reimbursement, staffing and patient access records.
Compare a service across two periods using equivalent eligibility rules, case mix and functional measures; document changes in measurement.
Assess a proposed rehabilitation service through workforce, access, evidence and follow-up requirements; avoid promising individual recovery.
Test one rehabilitation claim against the population, comparator and outcome actually studied; separate measured function from promotional testimonials.
Follow one consented rehabilitation journey through goals, service access and follow-up; place personal testimony alongside documented service conditions.
Examine how one service sets and revises patient goals; compare standardized assessments with priorities stated by the patient.
Trace referral, waiting time, transport and payment barriers for a defined patient group; distinguish service availability from usable access.
Follow selection, fitting, training and support for one assistive product within rehabilitation; examine task performance and user experience.
Track one patient's or cohort's transitions between hospital, outpatient and community services; identify documented handoff gaps and follow-up outcomes.
Compare professional outcome scores with patients' descriptions of meaningful daily activity; retain differences rather than reducing recovery to one score.""",
"503": """Trace one assistive product from the user need it addressed through design and service development; distinguish invention stories from documented adoption.
Study one assistive product in a defined user group and daily task; compare reported benefits, support needs and limits of the evaluation.
Document the contributions of disabled users, caregivers or repair workers to one product's development; obtain consent and credit their knowledge.
Explain how one assistive product and its associated services support a specific activity; separate device features from usable access.
Compare outcome measures for one assistive product, including participation, comfort and task success; examine whose priorities the measures reflect.
Investigate one unexplained difference between a product's test results and everyday use; compare fit, environment, training and maintenance evidence.
Evaluate a new assistive feature against an existing approach for a defined task; include usability, reliability and support requirements.
Trace one procurement or design decision through user consultation, technical constraints and funding; attribute the reasons recorded by participants.
Examine one access-policy or funding change and its effect on product provision; compare eligibility, waiting times and follow-up records.
Map assessment, product selection, fitting, training, repair and replacement for one service; identify responsibility and costs at each step.
Explain growth or withdrawal of one assistive product using availability, user feedback, support and service data; avoid equating sales with benefit.
Compare two generations of a product on the same user task and support conditions; include compatibility and repair access.
Assess a proposed assistive product through user testing, provision, maintenance and affordability requirements; distinguish prototypes from available services.
Test one claim of independence or accessibility against user-defined outcomes; examine context and groups excluded from the evidence.
Follow a consented product journey from assessment through everyday use and repair; include the user's decisions and unresolved barriers.
Examine how fitting and training affect one product's use for a defined activity; compare service records with users' reported difficulties.
Follow a repair or replacement case through diagnosis, parts, cost and downtime; document how service interruption affects daily participation.
Compare purchase, fitting, training, repair and replacement costs for one product in one jurisdiction; distinguish subsidies from actual out-of-pocket access.
Evaluate one interface or physical design with users who have different access needs; describe tradeoffs rather than claiming universal accessibility.
Investigate why users stopped using one product through consented accounts and follow-up records; distinguish poor fit, changing needs and service failure.""",
"504": """Trace one maternal or child health service from its original access problem through policy and delivery changes; define the population and jurisdiction.
Examine one documented maternal or child health program using eligibility, uptake and outcomes; separate evaluation findings from individual care advice.
Follow overlooked care work by families, community workers or staff in one pathway; use consented accounts and protect children's identities.
Explain one care pathway from eligibility through referral and follow-up; define the roles of services without providing personal medical instructions.
Compare measures used in one maternal or child health evaluation; examine denominators, case mix, follow-up and differences between access and outcomes.
Investigate one unexplained service or outcome gap using routine data and competing explanations; state where evidence cannot establish cause.
Evaluate one service technology in its actual care setting; compare reach, reliability and continuity with the previous process.
Reconstruct one service-design decision through published records and affected families' perspectives; distinguish authority, consultation and observed outcomes.
Follow a dated service expansion, closure or policy change; compare access and continuity records for the same population.
Map referrals, transport, appointments and follow-up across one maternal or child health pathway; identify responsibility at each transition.
Explain changes in participation in one service using eligibility, staffing, transport and cost evidence; avoid attributing them to parental attitudes alone.
Compare two periods using consistent age groups, eligibility and outcome definitions; account for changes in reporting or service coverage.
Assess one proposed service change through workforce, referral capacity, access and evaluation requirements; frame expected benefits as questions to test.
Test one public maternal or child health claim against its original evidence and defined population; avoid individualized recommendations.
Build a sourced account of one family's consented service journey; connect lived experience to documented care-system conditions.
Examine appointment availability, travel, language and affordability in one prenatal service; distinguish nominal eligibility from timely access.
Review a published birth-safety improvement program using its defined outcomes, implementation and follow-up; avoid interpreting one case as a clinical protocol.
Trace newborn referral and follow-up in one service network; examine continuity, caregiver communication and documented losses to follow-up.
Follow one child-development assessment and support pathway; examine referral criteria, waiting times and family access without diagnosing children.
Compare access or outcomes between defined groups using consistent measures and service context; examine reporting gaps and families' explanations.""",
"505": """Trace one nutrition concept or recommendation through the studies and methods that shaped it; distinguish historical belief from later evidence.
Examine one influential dietary study using population, exposure, comparator, outcome and limitations; test whether popular descriptions match its design.
Investigate overlooked participant, laboratory or data work in one nutrition study; credit contributions and examine whose diets were underrepresented.
Explain one nutrition-evidence concept through a defined study example; distinguish nutrients, foods and dietary patterns without prescribing a diet.
Compare causal-inference approaches for one dietary question; examine measurement error, confounding, substitution and uncertainty.
Investigate why studies on one dietary question disagree; compare exposure definitions, population, follow-up and analytical choices.
Evaluate one nutrition-measurement tool against an appropriate reference method; examine usability, error and which foods or populations it misses.
Trace one researcher, committee or funder's documented role in a nutrition decision; distinguish disclosed interests from demonstrated influence.
Examine a dated guideline revision or major study and its evidence base; identify which conclusions changed and which remained uncertain.
Follow how one dietary exposure is measured, analyzed and translated into a public claim; identify uncertainty at each step.
Explain the rise or decline of one nutrition claim using studies, guidance and marketing records; avoid equating popularity with scientific support.
Compare two periods of nutrition guidance using consistent questions, populations and outcomes; document changes in evidence standards.
Assess an emerging nutrition research method through validation, feasibility and unresolved bias; describe potential applications conditionally.
Test one food or nutrient claim against the original study; distinguish association, causation, relative risk and practical effect size.
Build a source trail from a nutrition study to a headline, label or recommendation; identify where qualifications were lost or preserved.
Compare dietary recall, food records and biomarkers for a defined exposure; explain error, participant burden and validation limits.
Examine how a study or survey estimates nutrient adequacy in a defined population; distinguish group estimates from individual diagnosis.
Analyze one food environment using availability, price, marketing and access measures; avoid attributing dietary choices solely to individuals.
Compare a trial and a cohort addressing the same dietary question; align outcomes and follow-up while explaining their different limitations.
Trace one nutrition label or advertising claim to its substantiation and jurisdiction-specific rules; distinguish regulatory permission from demonstrated health benefit.""",
}


FIELD_QUESTIONS = {
    "501": "Where does a disease-surveillance system miss or delay cases?|Which delivery barriers explain uneven vaccination uptake?|Does a public-health message reach its audience with the intended meaning?|Did a community prevention intervention change its target outcome?|Which access or exposure differences help explain a program's outcome gap?",
    "502": "How do patients' priorities shape rehabilitation goals?|Where does a rehabilitation referral become an access barrier?|Does an assistive product support the activity a patient values?|What is lost when care moves between rehabilitation services?|Do professional scores capture the functions patients consider meaningful?",
    "503": "How do fitting and training affect an assistive product's use?|What happens to participation while an assistive product awaits repair?|What does usable access to an assistive product actually cost?|Which users can complete the intended task with a product's design?|Why did users stop using a particular assistive product?",
    "504": "Which barriers prevent timely use of a prenatal service?|What did a documented birth-safety program actually improve?|Where are newborn referrals or follow-up appointments lost?|How do families move from a development concern to support?|Which groups experience different access or outcomes in one care pathway?",
    "505": "How accurately does a study measure what participants eat?|What can a population estimate establish about nutrient adequacy?|How do price and access shape a defined food environment?|Why do a trial and cohort reach different dietary conclusions?|What evidence supports a nutrition label or advertising claim?",
    "506": "How much income remains after a household pays its housing costs?|How secure is a tenancy under its actual renewal and dispute rules?|How quickly are documented housing-quality problems resolved?|How does an eviction case move from notice to outcome?|Can intended residents apply for and use an accessible housing scheme?",
    "507": "Where do water losses or measurement gaps appear between source and tap?|Does a wastewater system meet its stated treatment objectives?|Which households lack reliable and affordable usable service?|What does a water-quality monitoring program actually represent?|Who can explain or remedy a utility service decision?",
    "508": "Which households receive a usable waste-collection service?|How much incoming material leaves a sorting facility as usable output?|What do monitoring records establish about one landfill's impacts?|How does a recovery system distribute work and value to informal workers?|Can a redesigned product be processed by the local waste system?",
    "509": "Does a heat intervention reduce residents' actual exposure?|Why did drainage perform differently from its design assumptions?|Which risks remain after a proposed coastal protection measure?|What performance and maintenance evidence supports a green-infrastructure project?|Who benefits and who remains exposed after an adaptation project?",
    "510": "Are required inspections followed by documented action?|Why does a known maintenance backlog remain unresolved?|Does an asset register contain the information maintenance teams need?|What warning evidence did a published engineering investigation identify?|How does a maintenance outage affect different service users?",
    "511": "How does one chip architecture change performance on a defined workload?|Where do process controls and inspection enter chip fabrication?|What do reported yield figures include and exclude?|Which packaging tradeoffs matter for a specified device?|Which input dependencies constrain a defined chip supply chain?",
    "512": "How do qubit platforms compare on the same experimental criteria?|What did an error-correction experiment establish about logical errors?|Does a quantum benchmark measure the advantage being claimed?|Which resources would a quantum algorithm need for its proposed task?|Which control and error constraints limit a hardware design's scaling?",
    "513": "Does a project's user-research sample represent its intended users?|Which design conditions contributed to an interaction error?|Can users with relevant access needs complete the intended task?|Does an interface communicate its state and uncertainty clearly?|Did a design iteration improve measured task performance?",
    "514": "Which permissions and obligations apply to one project's licensed version?|How is maintenance labor distributed within an open-source project?|Who can approve, reject or appeal a project change?|How did a project communicate and address a disclosed vulnerability?|What evidence supports a project's capacity to continue maintaining its software?",
    "515": "How does a protocol move from specification to actual deployment?|Which institutions control each step of a domain-name decision?|How is a network-neutrality rule implemented in one jurisdiction?|How does a cross-border internet rule affect operators and users?|Whose participation influences a multistakeholder decision?",
    "516": "Which workplace terms were established through a bargaining process?|How does a pay-protection complaint reach a remedy?|How do recorded schedules compare with applicable working-time rules?|Which criteria determine a work arrangement's legal classification?|Can workers use a grievance route and obtain a response?",
    "517": "How are hazards identified and prioritized for one workplace task?|Which system conditions did a public incident investigation establish?|Does safety training produce demonstrated task understanding?|What evidence supports one protective design in its intended setting?|How do worker concerns change prevention decisions?",
    "518": "Can cooperative members use their stated decision rights?|How does financing affect a cooperative's member control?|How was a cooperative's surplus actually distributed?|How does one cooperative perform against comparable market alternatives?|Which factors contributed to a cooperative's closure or restructuring?",
    "519": "How do different poverty thresholds classify the same population?|How do housing costs change a group's available resources?|What does a wealth dataset miss about ownership and debt?|Which evidence supports an account of mobility across generations?|Who gained or lost under a documented policy change?",
    "520": "How do projected revenues compare with actual collections?|Which proposals survived a budget negotiation and why?|Did a public contract deliver what was authorized and purchased?|What happened after an audit identified a spending problem?|Which residents influenced a participatory budget and saw projects delivered?",
    "521": "What can one soil profile establish about its formation?|What does a microbial measurement establish about a soil function?|Which evidence distinguishes erosion from local sediment redistribution?|Does a soil-carbon estimate measure a durable change in stock?|How much of a soil difference can be attributed to land use?",
    "522": "Which evidence attributes a pollutant to particular sources?|Whose exposure is missing from an air-monitoring network?|How do indoor and outdoor exposure differ in one setting?|Which assumptions drive a published pollution health-burden estimate?|What changed after a clean-air policy was implemented?",
    "523": "Which evidence supports the identified threats to a species or habitat?|Does a mapped habitat connection support actual ecological movement?|How did a restored site's outcomes compare with its stated objectives?|Who controls and benefits from a community stewardship arrangement?|Which survey biases affect an apparent biodiversity trend?",
    "524": "Which inputs and impacts are counted for one food product?|Where do material and resource losses occur during processing?|Which distribution conditions determine a product's cost and reach?|How much food loss occurs at a defined supply-chain stage?|Can a defined population afford and obtain nutritionally relevant foods?",
    "525": "How sensitive is a stock assessment to its data and assumptions?|What does observation coverage establish about a fishery's bycatch?|How do management rules affect a named small-scale fishing community?|Can a seafood product's origin be followed through custody records?|How does a management choice distribute ecological and livelihood tradeoffs?",
    "526": "How do community positions and dated legal records describe a sovereignty issue?|What do land records preserve or omit about a community's occupation?|How does a community define and pursue language continuity?|How did a colonial collection's purpose shape its historical account?|Who authorizes and shapes the public memory of one community event?",
    "527": "How did an interview guide shape the recorded account?|How does the timing of an interview affect its retrospective account?|What changes between a recording and its transcript?|Which uses did a narrator consent to and which require further permission?|How do archival access conditions reflect narrator wishes and user needs?",
    "528": "Whose materials enter a collection under its acquisition policy?|How do catalog terms shape which histories users can find?|What evidence records a conservation treatment and its consequences?|Can intended users discover and use a digital collection?|Which rights and restrictions govern a particular item's reuse?",
    "529": "What does each lexical choice preserve or change in one passage?|How can a culturally specific term be rendered for a named audience?|How are translation contributions credited in one publication?|What changes when a text or interface is localized?|How do defined readers interpret one translated passage?",
    "530": "Does a public claim accurately represent its original evidence?|What can observations establish about a platform's ranking behavior?|How did one misleading claim travel through public channels?|Does an image's original context support its current caption?|Do learners apply a checking method to unfamiliar claims after a delay?",
}


def main():
    with (ROOT / "REGISTRY/NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as stream:
        rows = {row["id"]: row for row in csv.DictReader(stream)}
    if set(SCOPES) != {str(i) for i in range(501, 531)}:
        raise ValueError("Expected all thirty scope revision blocks")
    changes, focus_changes = [], []
    for number, block in SCOPES.items():
        path = ROOT / rows[number]["niche_path"] / "ANGLE_PLAN.json"
        plan = json.loads(path.read_text(encoding="utf-8"))
        scopes = block.splitlines()
        entries = plan["angles"]
        if len(scopes) != 20 or len(set(scopes)) != 20 or [a["slug"] for a in entries[:15]] != BASE or len(entries) != 20:
            raise ValueError(f"Scope count or stable order mismatch: {number}")
        for entry, scope in zip(entries, scopes):
            if entry["scope"] != scope:
                changes.append(dict(niche_id=number, slug=entry["slug"], previous_scope=entry["scope"], revised_scope=scope))
                entry["scope"] = scope
        questions = FIELD_QUESTIONS[number].split("|")
        if len(questions) != 5 or any(not q.endswith("?") for q in questions):
            raise ValueError(f"Expected five focus questions: {number}")
        for entry, question in zip(entries[15:], questions):
            if entry["question"] != question:
                focus_changes.append(dict(niche_id=number, slug=entry["slug"], previous_question=entry["question"], revised_question=question))
                entry["question"] = question
        plan["scope_review"] = {
            "date": "2026-10-16", "status": "scope_wording_revised",
            "basis": "Twenty angle-specific scopes define coverage, comparisons and limits. Episode case selection and source checks remain required.",
        }
        path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if changes:
        ledger = ROOT / "AUDIT/ANGLE_SCOPE_CHANGES.csv"
        with ledger.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(changes[0]))
            writer.writeheader()
            writer.writerows(changes)
    if focus_changes:
        with (ROOT / "AUDIT/ANGLE_FOCUS_CHANGES.csv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(focus_changes[0]))
            writer.writeheader()
            writer.writerows(focus_changes)
    pilot_defaults = {
        "001": (
            "original system papers, model or dataset documentation, reproducible evaluations and attributed contributor accounts appropriate to the selected question",
            "Name the system version, task and evaluation conditions; distinguish a demonstration from general capability and verify deployment claims separately.",
        ),
        "004": (
            "identified texts and editions, attributed translations or commentaries, dated performance records and consented community accounts appropriate to the selected narrative",
            "Attribute the text, version, period and community; distinguish sacred narrative, interpretation and historical evidence, and honor restrictions on living or restricted traditions.",
        ),
    }
    completed = 0
    for number, (evidence, boundary) in pilot_defaults.items():
        path = ROOT / rows[number]["niche_path"] / "ANGLE_PLAN.json"
        plan = json.loads(path.read_text(encoding="utf-8"))
        for entry in plan["angles"]:
            if not entry.get("evidence"):
                entry["evidence"] = evidence
                completed += 1
            if not entry.get("boundary"):
                entry["boundary"] = boundary
        path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Revised {len(changes)} scopes across {len(SCOPES)} plans; stable angle IDs and editorial statuses retained")
    print(f"Completed evidence and limit guidance for {completed} pilot angles")
    print(f"Aligned {len(focus_changes)} field-angle questions with their revised scopes")


if __name__ == "__main__":
    main()
