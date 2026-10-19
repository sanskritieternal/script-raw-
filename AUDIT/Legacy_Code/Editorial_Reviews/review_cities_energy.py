"""Question-design reviews for cities and electricity systems."""

from review_angle_plans import audit, revise_domain


CITIES = """history_origins|Why This Neighborhood Grew|Which land, transport, work, and policy changes shaped one district?|Use dated plans, maps, census records, and resident accounts.
famous_examples|A Model City Project Tested|Did a celebrated urban project deliver its stated benefits?|Compare original goals with access, affordability, maintenance, and resident experience.
hidden_stories|Who Built and Maintains the City?|Whose construction, care, cleaning, and informal work is absent from the city story?|Use workforce records and attributed worker accounts.
beginner_explainers|How a City Decision Gets Made|Who controls land use, streets, utilities, and public spaces in one place?|Map relevant authorities, funding, consultation, and appeals.
advanced_concepts|Density, Access, and Cost|Does more density improve access without displacing residents?|Compare housing costs, travel times, services, and land values in one area.
mysteries_unsolved_cases|Why This Place Floods|Which factors best explain repeated flooding on one street?|Compare rainfall, drainage, elevation, paving, and maintenance data.
technology_innovation|A Smart-City Tool in Practice|Did one urban sensor or app improve a public service?|Compare measured service outcomes, privacy, access, and upkeep.
people_personalities|Residents in the Planning Record|Whose proposal changed one urban plan and whose was rejected?|Trace public submissions, revisions, decisions, and affected groups.
major_events|A City's Response to Heat|How did one dated heat event expose differences in urban protection?|Compare shade, housing, services, health records, and local response.
how_it_works|From Plan to Street|What steps turn a planning designation into a built change?|Follow one project through land, permits, budgets, construction, and maintenance.
rise_fall|A District Loses Its Center|Why did one shopping or civic district decline or recover?|Compare employment, housing, transport, rents, and public investment.
then_vs_now|One Street Across Two Periods|How did use of public space and access change?|Compare maps, counts, business records, and residents' accounts.
future_developments|A Proposed Urban Redesign|Who would gain or lose access under one proposed plan?|Compare modeled trips, housing costs, safety, climate exposure, and upkeep.
myths_vs_facts|The Empty Land Claim|Was a site truly unused before redevelopment?|Check tenure, informal use, ecology, and community accounts.
documentary_stories|The Life of a Planning Decision|How did one zoning or street decision change from proposal to reality?|Build a dated record of objections, amendments, construction, and outcomes.
lived_experience|A Resident's Daily Route|What does one route reveal about access to services and public space?|Use consented account and mapped timings without generalizing from one person.
institutional_pathway|Fixing a Broken Sidewalk|Which authority receives and resolves one public-space problem?|Trace reporting, budgeting, repair, and accountability.
incentives_norms|Why Plans and Buildings Diverge|What incentives shape actual construction under one land-use rule?|Compare code, developer finance, enforcement, and observed buildings.
access_and_exclusion|Who Can Use the Park?|Which design or policing choices limit use of one public space?|Observe mobility, hours, cost, safety, and resident perspectives.
community_variation|One City, Different Conditions|Why do two neighborhoods receive different services?|Compare need, budget, infrastructure, political voice, and history.
policy_in_practice|Did a Housing Rule Change Supply?|What followed one enacted zoning or housing policy?|Separate permits, completions, prices, displacement, and preexisting trends.
survey_vs_story|The City Satisfaction Score|Where do aggregate city surveys miss neighborhood experience?|Check sampling, geography, wording, and consented local accounts.
power_and_voice|Who Shapes Redevelopment?|How can residents influence one redevelopment decision?|Compare formal consultation with actual revisions and land control.
unintended_consequence|A Better Street, Higher Rent?|Did one improvement change affordability for nearby households?|Compare rent, tenure, displacement, businesses, and other market trends.
comparative_setting|Two Blocks, One Design Goal|Why did similar public-space designs work differently?|Compare land use, climate, upkeep, access, and resident use.
change_over_time|A Neighborhood After Investment|Which outcomes persisted years after one urban project?|Track access, housing, environment, and maintenance on a consistent boundary.
ethical_dilemma|Protection Versus Displacement|How should a city weigh flood protection against relocation costs?|Present residents' options, rights, budgets, and uncertainty without prescribing.
field_space_constraints|Making Room on a Narrow Street|How does limited right-of-way affect uses of one street?|Measure actual space and compare safety, access, and service needs.
field_household_cost|The Total Cost of an Address|How do housing, utilities, and transport costs combine for residents?|Use comparable household types and a dated price basis.
field_design_for_access|An Accessible Public Route|Can a resident with a defined access need reach one civic destination?|Audit crossings, gradients, surfaces, signage, and user feedback.
field_maintenance_burden|Who Maintains the New Space?|Are upkeep funds and responsibilities adequate after construction?|Compare design plan, budgets, actual repairs, and user reports.
field_material_lifecycle|A Street Material Over Time|How do pavement or building-material choices affect repair and heat?|Compare service life, embodied impacts, maintenance, and local conditions."""


ENERGY = """history_origins|Why This Power System Took Shape|Which resources, demand, policy, and ownership decisions shaped one grid?|Trace dated plans, investment, and affected communities.
famous_examples|A Power Project's Full Record|Did a celebrated project meet its reliability, cost, and emissions goals?|Compare forecast and actual output, costs, outages, and local effects.
hidden_stories|Workers Behind the Switch|Whose mining, construction, operations, and maintenance work is omitted?|Follow one electricity supply chain with attributed worker accounts.
beginner_explainers|From Generator to Socket|How does electricity move through generation, transmission, distribution, and use?|Use a named network and explain losses, control, and billing at a high level.
advanced_concepts|Energy, Capacity, and Reliability|Why can a plant's rated capacity differ from delivered electricity?|Compare capacity factor, availability, peak demand, and grid constraints.
mysteries_unsolved_cases|What Caused an Outage?|Which public evidence identifies the initiating and contributing factors?|Use official investigation and avoid exposing operational vulnerabilities.
technology_innovation|Storage on One Grid|Did storage change reliability, peak use, or renewable integration?|Compare dispatch records, cost, losses, and operating limits.
people_personalities|Who Chose the Power Source?|Which public and company decisions shaped one generation project?|Trace authority, alternatives, consultation, and conflicts of interest.
major_events|A Heatwave Tests the Grid|How did one dated weather event affect demand and service?|Compare loads, failures, response, and unequal household impacts.
how_it_works|Balancing Supply and Demand|How does a grid keep electricity available as demand changes?|Explain scheduling, reserves, transmission, and demand response without control details.
rise_fall|Why a Power Plant Closed|Which factors led to closure or repurposing of one facility?|Compare age, cost, safety, regulation, fuel, and community transition.
then_vs_now|One Grid Across Two Eras|How did fuel mix, reliability, tariffs, and access change?|Use comparable metrics and clear boundaries for both dates.
future_developments|A Proposed Energy Mix|What conditions would make a proposed supply plan reliable and affordable?|Model demand, build time, grid needs, uncertainty, and distributional costs.
myths_vs_facts|The Zero-Emission Claim|Does a generation claim include upstream and construction emissions?|Compare lifecycle boundaries, method, and measured operation.
documentary_stories|A Power Project From Plan to Operation|How did one project change through approval, build, and service?|Build a dated record of cost, output, delays, and public commitments.
system_boundary|What Counts in the Energy Bill?|Which costs and losses sit outside a simple generator comparison?|Define generation, grid, storage, backup, fuel, and externalities.
input_output_trace|Following a Unit of Energy|Where are electricity and energy lost from source to final use?|Use metered data and clear conversion and accounting rules.
design_tradeoff|Local Generation or Long Lines|How do two supply designs trade cost, reliability, land, and losses?|Compare the same demand and time horizon with uncertainty.
failure_mode|A Publicly Documented Grid Failure|Which safeguards failed or worked in one outage?|Rely on official findings at a high level without exploit steps.
testing_limits|Pilot Project Versus System Need|What did an energy demonstration actually prove?|Check scale, duration, weather, demand, and independent data.
standards_interoperability|Connecting a New Generator|What must be demonstrated before one project can join a grid?|Explain public technical and regulatory requirements without settings.
security_threat_model|Protecting Essential Power|How do operators balance reliability, cyber defense, and public transparency?|Use aggregate public guidance; omit vulnerabilities and control procedures.
maintenance_lifecycle|The Aging Grid|How do inspection and replacement choices affect reliability?|Compare asset ages, outages, budgets, and planned work.
infrastructure_dependencies|Energy Depends on Other Systems|How do water, fuel transport, telecoms, or roads affect one plant?|Trace a documented dependency and response with public records.
accessibility_usability|Who Can Use the Energy Program?|Which households cannot access a tariff or efficiency program?|Check eligibility, housing tenure, language, disability, and enrollment.
independent_replication|Can This Energy Model Travel?|Which local resource and grid conditions limit transfer of a success?|Compare climate, demand, finance, regulation, and infrastructure.
responsible_deployment|Before a Plant Goes Live|What public evidence demonstrates readiness and oversight?|Review permits, safety case, community measures, monitoring, and emergency planning.
field_energy_balance|Accounting for Delivered Power|How do losses and curtailment change a project's delivered energy?|Use a defined period and meter boundary.
field_grid_integration|The Grid Connection Queue|Which bottlenecks delay one proposed connection?|Compare published queue, network works, costs, and timeline.
field_material_inputs|Materials Behind Generation|Which materials and upstream impacts are needed for one technology?|Trace quantities, sourcing, recycling, and data limits.
field_operational_safety|Operating Risk in Context|How does a facility publicly report safety performance?|Use regulator findings and aggregate outcomes, avoiding instructions.
field_lifecycle_emissions|Emissions Across a Power Source's Life|How do construction, fuel, operation, and end-of-life affect emissions?|Compare methods on the same output unit and time basis."""


if __name__ == "__main__":
    revise_domain("111", "111_cities_urbanism", CITIES,
                  "Urban places as lived and governed systems of housing, streets, public space, infrastructure, climate exposure, and resident voice.",
                  "dated plans and maps, land and housing records, city budgets and service data, measured environmental outcomes, and consented resident and worker accounts",
                  "Name city, neighborhood, jurisdiction, and period. Include informal uses, affordability, accessibility, and maintenance; distinguish proposals from observed outcomes.")
    revise_domain("113", "113_energy_power", ENERGY,
                  "Energy and power systems through generation, grids, demand, reliability, costs, workers, safety governance, and lifecycle impacts.",
                  "dated generation and grid data, regulator and utility records, project appraisals, independent lifecycle studies, and attributed worker and community accounts",
                  "Name technology, grid, jurisdiction, and period. Compare delivered energy on equal boundaries, verify current standards, and omit exploitable control or security details.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
