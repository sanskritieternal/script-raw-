"""Editorial question maps for manufacturing and architecture."""

from review_angle_plans import audit, revise_domain


MANUFACTURING = """history_origins|How a Factory System Emerged|Which demand, machinery, labor, and capital decisions produced one factory?|Compare dated company, worker, patent, and trade records.
famous_examples|A Famous Production Line Reexamined|What did one celebrated manufacturing system improve and at what cost?|Compare output, defects, wages, injuries, and supplier effects in a defined period.
hidden_stories|Workers Behind a Manufactured Product|Whose assembly, inspection, maintenance, or supplier work is missing from its story?|Use attributed accounts and production records, including contract workers.
beginner_explainers|From Raw Material to Finished Product|Which stages transform one input into a tested product?|Trace a named product's public process and controls without operating instructions.
advanced_concepts|Throughput, Quality, and Variability|How did one factory balance output speed with defects and rework?|Compare consistent denominators, process changes, and customer outcomes.
mysteries_unsolved_cases|An Unexplained Factory Defect|Which explanations for a documented quality problem fit the evidence?|Compare inspection, material, process, and field data without assigning unsupported blame.
technology_innovation|A Factory Technology in Practice|Did one automation or measurement change improve a specified outcome?|Compare baseline, implementation cost, worker effects, and sustained results.
people_personalities|A Production Decision and Its Makers|Who chose one consequential production change, and whose concerns were heard?|Use minutes, worker accounts, design records, and dated constraints.
major_events|A Plant Closure or Conversion|What caused one manufacturing site to change its output or close?|Trace orders, costs, policy, supply, and community effects over time.
how_it_works|How a Production System Coordinates|How do purchasing, scheduling, fabrication, inspection, and delivery connect?|Map one product's public value chain and feedback loops.
rise_fall|A Manufacturer's Expansion and Decline|Which product, process, demand, or capital choices changed its position?|Compare company records with industry data and competitor context.
then_vs_now|One Product Across Two Production Eras|How did materials, labor, quality, and waste change?|Use comparable product and process boundaries for both dates.
future_developments|A Proposed Factory Transition|What evidence would show whether a proposed process scales responsibly?|Specify yield, cost, worker safety, energy, supply, and durability measures.
myths_vs_facts|Testing a Factory Productivity Claim|Does a claim of greater output survive consistent measures?|Check units, quality losses, hours, outsourcing, and the chosen baseline.
documentary_stories|One Product Launch Through Its Records|How did a product move from design to reliable production?|Build a dated record of trials, ramp-up, defects, fixes, and users.
value_chain|Who Adds Value Along the Chain?|Which firms and workers contribute to one finished product?|Map material, component, assembly, distribution, and service stages.
incentive_map|Targets on the Factory Floor|How did one pay or performance target shape quality and worker behavior?|Compare target design with documented outcomes and unintended effects.
unit_economics|The Cost of One Unit|How did material, labor, energy, scrap, and overhead affect unit cost?|Use a stated production volume and disclosed or illustrative figures.
consumer_outcome|Does Better Production Reach the Buyer?|Did a process improvement change durability, price, or repair experience?|Compare matched product generations and independent field evidence.
market_structure|Who Can Supply the Product?|How concentrated was one component market and how did that affect production?|Define product, geography, period, and supplier shares where available.
risk_transfer|Who Bears a Production Disruption?|How did contracts distribute delay, defect, and inventory costs?|Compare public contract terms, supplier accounts, and observed effects.
regulatory_choice|A Rule Changes Manufacturing|How did one dated safety or environmental requirement alter a process?|Compare compliance plan, implementation, worker and community outcomes.
historical_shock|A Supply Shock Hits a Plant|How did one disruption propagate through suppliers and production?|Trace dated orders, inventory, substitutes, and recovery.
data_definition|What Counts as Output?|Why do two sources report different productivity or defect rates?|Audit units, time windows, exclusions, inspection stage, and denominator.
access_and_affordability|Who Can Obtain the Product?|Did production scale make one essential product more affordable or available?|Compare price, quality, distribution, and excluded groups.
business_failure|Why a Factory Investment Failed|Which assumptions about demand, yield, or cost proved wrong?|Compare original forecasts, actual ramp-up, financing, and alternatives.
long_term_tradeoff|A Product's Full Life|Did lower factory cost increase maintenance, waste, or energy use later?|Compare production and use-stage evidence over a defined lifespan.
field_supply_chain|A Component's Route to Assembly|Where did a critical input come from and which substitutions were feasible?|Trace public supplier and logistics records without exposing vulnerabilities.
field_brand_claims|Made Here, Built Better?|Does a manufacturing or origin claim match the documented process?|Check claim wording, component origins, audit scope, and product tests.
field_customer_experience|A Defect Reaches Customers|How did one manufacturing issue affect buyers and service teams?|Compare complaint, recall, warranty, and repair records with denominators.
field_market_entry|A New Manufacturer Scales Up|What barriers did a new producer face entering a defined market?|Compare tooling, certification, distribution, capital, and initial quality.
field_product_lifecycle|From Launch to Repair or Disposal|What happened to one manufactured product after sale?|Trace durability, spare parts, repair, reuse, and end-of-life records."""


ARCHITECTURE = """history_origins|How a Building Type Emerged|Which social needs, materials, and rules shaped an early example?|Compare dated plans, patron records, building fabric, and later alterations.
famous_examples|A Landmark Beyond Its Facade|How did one famous building serve its intended users?|Compare design claims, actual use, maintenance, and differing accounts.
hidden_stories|Who Built the Building?|Whose craft, labor, or displaced community is absent from its architectural story?|Use contracts, payroll, oral history, and land records where available.
beginner_explainers|Reading a Building|How do plan, structure, material, climate, and use relate in one building?|Explain a dated example through drawings and observed use, without construction instructions.
advanced_concepts|Form, Climate, and Performance|Did one architectural choice deliver its claimed comfort or efficiency?|Compare design modeling with measured use, occupancy, and climate.
mysteries_unsolved_cases|An Uncertain Design Attribution|Which records support or challenge credit for one building's design?|Compare drawings, contracts, correspondence, fabric, and later attributions.
technology_innovation|A Building Method in Use|How did one material or structural innovation affect space, cost, and maintenance?|Compare original tests and service history in a named building.
people_personalities|Architect, Patron, and Users|Whose priorities shaped a consequential design choice?|Read briefs, correspondence, budget changes, and occupant accounts.
major_events|A Building's Turning Point|What event changed one building's form, ownership, or use?|Trace dated permits, plans, damage records, and community response.
how_it_works|From Brief to Occupied Building|How did one project move through design, approval, construction, and use?|Follow a documented project with schedule, cost, and post-occupancy evidence.
rise_fall|A Building's Changing Fortunes|Why did one building become valued, neglected, or repurposed?|Compare ownership, maintenance, planning, use, and public perception.
then_vs_now|One Building Across Two Periods|How did alterations change its fabric, access, and function?|Use dated plans, photographs, surveys, and occupant accounts.
future_developments|A Proposed Building Adaptation|What evidence would support a planned retrofit or reuse?|Set preservation, accessibility, energy, cost, and user-outcome criteria.
myths_vs_facts|Testing an Architectural Legend|Does a celebrated design anecdote match contemporary records?|Trace its earliest source and compare drawings, letters, and fabric.
documentary_stories|A Building Through Its Records|How did a building change from proposal to present use?|Build a dated chronology of plans, construction, alterations, and lived experience.
source_trail|Who Wrote the Building's Story?|Which primary records support a repeated architectural interpretation?|Trace citations to plans, contracts, images, and surveys; identify gaps.
material_evidence|What the Building Fabric Shows|Which materials or alterations reveal construction sequence?|Compare physical survey with drawings and conservation records.
chronology_dispute|When Was This Part Built?|Why do sources disagree about the date of one architectural feature?|Compare permits, photographs, fabric analysis, and later copies.
ordinary_lives|Everyday Life in a Designed Space|How did one group actually use and adapt a building?|Use attributed occupants' accounts and documented changes over time.
power_and_institutions|Who Controlled the Design?|Which owner, funder, regulator, or institution decided a key feature?|Compare brief, approval, budget, and consultation records.
trade_and_exchange|Materials and Skills Across Regions|How did one building source materials and specialized labor?|Trace procurement, craft networks, transport, and local impacts.
language_and_labels|What Does Architectural Style Explain?|Does a style label clarify or obscure one building's history?|Compare dated design choices, local terms, and later classifications.
maps_and_borders|A Building in Its Setting|How did plot, street, climate, and neighboring uses shape its design?|Compare period maps, planning records, and site conditions.
conflicting_accounts|Competing Views of a Building|Why do architect, owner, and users describe one project differently?|Compare roles, dates, stated aims, and measured experience.
preservation_bias|Which Buildings Survive in the Canon?|Whose everyday or vernacular buildings were overlooked or demolished?|Compare inventories, selection criteria, and community memory.
turning_point_test|Did One Building Change Practice?|What evidence links a celebrated design to later architectural work?|Trace publications, adoption, and alternative influences.
legacy_and_memory|A Building's Public Meaning|How have preservation, tourism, or protest reshaped its meaning?|Use attributed community voices, designation records, and visitor evidence.
field_community_ownership|Who Shapes the Building's Future?|How were residents and users involved in a reuse decision?|Compare consultation records, decision authority, and later outcomes.
field_object_provenance|Tracing Architectural Fragments|Where did a reused or removed building element originate?|Check fabric, acquisition, custody, and documentation before attribution.
field_living_practice|Architecture in Daily Use|How does a community adapt a heritage building while retaining its meaning?|Use current user accounts, management plans, and observed changes.
field_conservation_choice|Repair, Replace, or Leave?|Why was one conservation intervention chosen for a building?|Compare condition survey, significance assessment, alternatives, and monitored effects.
field_cultural_translation|Design Ideas Across Cultures|How was one architectural idea adapted in a different place?|Trace designers, patrons, local builders, climate, and community interpretations."""


if __name__ == "__main__":
    revise_domain("051", "051_industrial_manufacturing_stories", MANUFACTURING,
                  "Manufacturing histories through production systems, workers, suppliers, quality, cost, customer outcomes, and product life cycles.",
                  "dated factory and company records, worker accounts, process and quality measures, public safety and environmental records, supply-chain data, and independent product evidence",
                  "Name product, plant, period, and jurisdiction. Separate company claims from measured outcomes; account for workers and neighbors; avoid operational safety instructions and undocumented confidential details.")
    revise_domain("052", "052_architecture", ARCHITECTURE,
                  "Architecture through design intent, material and construction evidence, daily use, preservation, access, and community meaning.",
                  "dated plans and permits, building surveys, conservation and designation records, contracts, measured performance, and attributed user and community accounts",
                  "Name building, place, period, and users. Distinguish original fabric from alterations and design intent from observed performance; verify current access and preservation rules before production.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
