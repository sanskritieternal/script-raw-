"""Editorial question designs for interior design, home gardening, and tiny houses."""

from review_angle_plans import audit, revise_domain


INTERIORS = """history_origins|A Room Plan in Its Period|Which use, material, or household constraint shaped a dated interior?|Compare plans, photographs, and occupant records.
famous_examples|A Celebrated Interior Rechecked|Which spatial choices actually support daily use in a named room?|Use measured plan and occupant evidence, not photographs alone.
hidden_stories|Who Made the Room?|Whose installation, cleaning, repair, and household work does a design account omit?|Trace labor records and user accounts.
beginner_explainers|Reading a Room Plan|How do circulation, light, storage, and furniture fit a measured space?|Show dimensions and intended users.
advanced_concepts|Tradeoffs in an Interior|How do acoustics, air, light, privacy, and access compete?|Compare options against explicit requirements and measured conditions.
mysteries_unsolved_cases|An Unverified Design Claim|Does a marketed layout solve the problem it promises?|Define outcome and seek use evidence or mark gap.
technology_innovation|A New Interior Product|Which task does a device or material change in practice?|Compare documented performance, cost, and maintenance.
people_personalities|A Designer's Revision|Why did a documented plan change after occupant feedback?|Use versioned drawings and attributed interviews.
major_events|A Home Renovation|What changed for residents after a specific remodel?|Compare before and after access, use, cost, and disruption.
how_it_works|From Brief to Installed Room|Which decisions connect measurements, layout, procurement, and use?|Trace dated plans, invoices, and postoccupancy evidence.
rise_fall|A Design Trend Reconsidered|What practical costs or user needs changed a once-popular layout?|Use dated examples and occupant reports.
then_vs_now|One Room across Renovations|Which functions improved or worsened between two plans?|Compare dimensions, use, and household composition.
future_developments|A Proposed Interior Upgrade|What budget, code, access, and maintenance questions remain?|Treat concept images as conditional plans.
myths_vs_facts|A Room Looks Bigger?|What do photographs hide about clearances and actual capacity?|Compare lens view with measured floor plan.
documentary_stories|A Room's Design Trail|How did brief, plans, installation, and feedback reshape it?|Use versions and credit every contributor.
lived_experience|Living with the Layout|Which daily tasks became easier or harder after a redesign?|Use consented occupant accounts and a defined follow-up period.
institutional_pathway|Approving an Interior Change|Which landlord, building, or permit decision controls a proposed alteration?|Trace actual authority and jurisdiction.
incentives_norms|Why a Room Looks This Way|How do budget, resale expectations, and household norms shape the plan?|Compare brief, quotes, and resident priorities.
access_and_exclusion|Who Can Use the Room?|Which route, reach, sensory, or cost barriers exclude users?|Test with named user needs and applicable rules.
community_variation|Different Households, Same Floor Plan|How do varied household routines change a layout's usefulness?|Compare situated use without universalizing.
policy_in_practice|A Design Rule Applied|How was an applicable housing or access requirement interpreted in one renovation?|Check adopted rule and approval record.
survey_vs_story|What Feedback Can Show|Does a satisfaction score match residents' accounts of daily use?|Compare survey design with interviews and observation.
power_and_voice|Whose Needs Set the Brief?|Which occupant could shape the design and who was overlooked?|Use meeting and revision records with consent.
unintended_consequence|A Design Tradeoff after Move-In|Which new cleaning, noise, or privacy burden followed a change?|Compare intended benefit with observed use.
comparative_setting|One Layout in Two Homes|How does the same design perform under different dimensions or households?|Hold task definition steady and measure differences.
change_over_time|A Room as Needs Change|What happens when household size or mobility needs shift?|Compare dated occupancy and alterations.
ethical_dilemma|Style versus Resident Access|How were conflicting aesthetic and access goals resolved?|Attribute decisions and examine alternatives.
field_space_constraints|Clearance in a Real Room|Can intended users move and work in the measured plan?|Check actual dimensions and applicable guidance.
field_household_cost|Full Room Cost|Which purchase, installation, energy, and upkeep costs are missing from a quote?|Use dated itemized estimates.
field_design_for_access|An Accessible Daily Task|Can users with stated needs reach, enter, and use the space?|Check applicable rules and user testing.
field_maintenance_burden|The Cleaning and Repair Plan|Which surfaces or mechanisms require continuing labor?|Compare manuals with actual use.
field_material_lifecycle|Where Materials Come and Go|Which sourcing, durability, and disposal claims have evidence?|Use product documentation and local recovery options.
"""

GARDENING = """history_origins|A Home Garden Practice in Context|Which local climate or household need shaped a dated practice?|Use extension archives and garden records without a universal origin.
famous_examples|A Productive Small Garden|Which site conditions and choices explain an observed result?|Record soil, sun, season, water, and harvest method.
hidden_stories|Labor behind a Garden|Who supplies seed, water, soil care, and ongoing maintenance?|Use grower accounts and cost records.
beginner_explainers|Match Plant to Place|What soil, light, space, and season does one plant need locally?|Use region-specific extension advice and actual site measurements.
advanced_concepts|The Garden as a System|How do soil, water, plant health, pollinators, and harvest interact?|Trace measured conditions and competing explanations.
mysteries_unsolved_cases|Why Did a Plant Fail?|Which causes can testing distinguish and which remain uncertain?|Check soil, weather, pests, and care records before diagnosis.
technology_innovation|A Garden Tool Tested|Does irrigation or monitoring equipment improve a defined outcome?|Compare measured water use and plant response.
people_personalities|A Gardener Changes Methods|What observation prompted a documented change in one plot?|Use logs and contextual interviews.
major_events|A Weather Shock in a Garden|How did a dated frost, heat event, or flood affect one crop?|Use local weather and garden records.
how_it_works|From Soil Test to Planting|How does a site assessment inform one growing decision?|Show sample method, test limits, and local guidance.
rise_fall|A Garden Method Reconsidered|Which evidence supports or challenges a popular technique?|Compare trials under comparable conditions.
then_vs_now|One Plot across Seasons|What changed in yield, soil, and labor between two dated seasons?|Hold measurement and crop definitions steady.
future_developments|Planning Next Season|Which uncertain weather or resource factor drives a garden plan?|Present conditional choices, not harvest promises.
myths_vs_facts|A Universal Garden Tip?|When does a common rule fail across soil or climate?|Compare extension guidance by region.
documentary_stories|A Garden's Year|How do preparation, planting, care, and harvest unfold?|Follow dated logs and measured outcomes.
lived_experience|A Season of Gardening|How did weather, care, and harvest fit a grower's daily life?|Use dated logs and consented accounts.
institutional_pathway|Access to Growing Space|Which lease, allotment, or local rule determines who can garden?|Read governing documents and actual allocation practice.
incentives_norms|Why This Plot Is Grown|Do food, habitat, enjoyment, or tradition drive the crop choices?|Ask growers and compare stated goals with practice.
access_and_exclusion|Who Can Garden Here?|Which cost, reach, path, time, or water barrier limits participation?|Measure site and record affected users' views.
community_variation|Gardens for Different Households|How do crop and care priorities vary among local growers?|Use bounded interviews without treating one group as uniform.
policy_in_practice|A Water or Compost Rule|How does a local garden rule shape actual decisions?|Compare rule text with observed implementation.
survey_vs_story|A Garden Success Claim|Do harvest totals capture growers' experience of the plot?|Compare quantities, labor, and qualitative goals.
power_and_voice|Who Decides a Shared Garden?|Whose choices set planting, access, and maintenance rules?|Trace meetings and participation.
unintended_consequence|A Garden Intervention's Side Effects|Did a change increase water use, labor, or conflict?|Compare intended and observed outcomes.
comparative_setting|The Same Crop in Two Sites|How do soil, light, and water differences change results?|Hold variety and season as comparable as possible.
change_over_time|A Plot across Seasons|What changes in soil, yield, and effort after repeated growing?|Use dated tests and logs.
ethical_dilemma|Food, Habitat, and Water|How were competing garden goals balanced under a constraint?|State who decided and which evidence was considered.
field_space_constraints|A Bed within Reach|How do sun, path width, and reach limit usable planting area?|Measure the actual garden and user needs.
field_household_cost|Cost per Growing Season|What do seeds, soil, water, tools, and labor add?|Record dated expenses and harvest quantity without promised savings.
field_design_for_access|Gardening for More Users|Which bed height, path, tool, or information change helps a named user group?|Test with participants and site constraints.
field_maintenance_burden|Care through the Season|How much watering, weeding, and monitoring did a crop require?|Log time and variation in weather.
field_material_lifecycle|Inputs and Garden Waste|Where do pots, soil amendments, plant debris, and water come from and go?|Check local reuse and disposal options.
"""

TINY_HOUSES = """history_origins|A Small Dwelling in Context|Which local housing rule or need shaped a dated tiny-house project?|Use permits, plans, and occupant testimony.
famous_examples|A Small Home under Use|How does a named design meet sleeping, cooking, hygiene, storage, and exit needs?|Compare measured plan and lived use.
hidden_stories|Land and Infrastructure Costs|Which utility, transport, site, and permit work is left out of a build story?|Use itemized records and local rules.
beginner_explainers|Tiny House or Another Type?|How is a proposed home classified in a specific jurisdiction?|Check current definitions, foundation, mobility, and occupancy.
advanced_concepts|Space versus Whole-Life Cost|Does a smaller floor area lower total housing cost for one case?|Compare site, construction, utility, insurance, and upkeep over time.
mysteries_unsolved_cases|Can This Home Be Occupied Here?|Which permits and inspections remain unresolved for a proposed site?|Read local zoning and building authority records.
technology_innovation|A Compact Building System|Which spatial or energy problem does a specific product solve?|Check performance, serviceability, and code applicability.
people_personalities|Residents Redesign a Small Home|Which documented daily use led to a layout change?|Compare plans and consented occupant accounts.
major_events|A Local Rule Changes|How did an adopted code or zoning change affect a specific project?|Date enactment, applicability, and permits.
how_it_works|From Plan to Legal Occupancy|Which approvals, utilities, inspections, and documents are required?|Map one jurisdiction and dwelling classification.
rise_fall|A Tiny-House Proposal Stalls|What documented cost or approval issue blocked it?|Use records and avoid attributing motive without evidence.
then_vs_now|A Home after Occupancy|Which space, moisture, energy, and maintenance issues appeared over time?|Compare design estimates with measured use.
future_developments|A Proposed Tiny-House Site|What local decisions must precede construction and occupancy?|Treat concept as conditional and verify current law.
myths_vs_facts|Smaller Always Cheaper?|Which fixed costs can offset the smaller footprint?|Use transparent dated comparison cases.
documentary_stories|One Tiny House's Paper Trail|How did site choice, plan review, construction, and move-in unfold?|Follow dated permits and actual costs.
lived_experience|Living Small over Time|Which daily tasks improve or strain after a year of occupancy?|Use consented resident accounts across seasons.
institutional_pathway|Approval to Occupy|Which zoning, permit, utility, and inspection steps applied to a named site?|Trace current local records and dwelling classification.
incentives_norms|Why Choose a Tiny House?|Which housing costs, preferences, and land opportunities shaped a household choice?|Compare stated reasons with actual budget.
access_and_exclusion|Who Can Live Here?|Which loft, entry, bath, cost, or land barrier excludes a potential resident?|Use measured plan and named needs.
community_variation|Tiny Homes in Different Places|How do climate, land tenure, and services change feasibility?|Compare named jurisdictions and households.
policy_in_practice|A Model Code Locally Adopted?|Did the relevant tiny-house appendix apply to this permit?|Check adopted edition, amendments, and official decision.
survey_vs_story|Satisfaction versus Daily Burden|Do resident ratings capture maintenance and space constraints?|Compare bounded survey with interviews and logs.
power_and_voice|Who Sets the Housing Rules?|How did residents, neighbors, builders, and officials influence a proposal?|Use public records and attributed testimony.
unintended_consequence|A Smaller Footprint's Hidden Burden|Did transport, utility, or storage needs offset expected savings?|Compare planned and actual costs.
comparative_setting|Same Plan, Different Site|How do climate, utilities, and rules change one design's performance?|Hold plan constant and document local variation.
change_over_time|A Tiny House after Several Years|What repairs, energy use, and household changes appeared?|Use dated occupancy and maintenance records.
ethical_dilemma|Affordability and Access|How were low initial cost, accessibility, and safety requirements balanced?|State alternatives and who bears each tradeoff.
field_space_constraints|Clearance and Exit|Can occupants use essential spaces and leave safely under applicable rules?|Check local adopted code and qualified review.
field_household_cost|The Full Housing Budget|What land, connection, permit, transport, tax, and maintenance costs apply?|Use dated itemized records, not a generic price.
field_design_for_access|Access in a Small Footprint|Which doorway, route, bath, and sleeping choice affects a named occupant?|Review actual needs and applicable local standards.
field_maintenance_burden|Moisture and Service Access|Which compact assemblies are difficult to inspect or repair?|Check manuals and occupancy history.
field_material_lifecycle|Materials over a Home's Life|Do claimed environmental savings include sourcing, energy, repairs, and disposal?|Use defined boundary and measured data.
"""


if __name__ == "__main__":
    revise_domain("393", "393_interior_design", INTERIORS,
                  "Interior design as measured planning of rooms for actual occupants, tasks, access, light, acoustics, materials, cost, and maintenance.",
                  "dimensioned plans, dated briefs and revisions, product specifications, applicable access guidance, itemized costs, and consented occupant evidence",
                  "Name room, occupants, jurisdiction, and date. Do not infer usability from photographs or claim code compliance without the applicable rule and qualified review.")
    revise_domain("394", "394_home_gardening", GARDENING,
                  "Home gardening as site-specific growing and care under local soil, light, climate, water, space, labor, and household goals.",
                  "local extension guidance, soil and water tests, dated weather records, grower logs, plant labels, measured harvests, and bounded comparisons",
                  "Specify region, season, site, plant, and test method. A single garden result does not establish a universal growing rule or guaranteed yield.")
    revise_domain("395", "395_tiny_houses", TINY_HOUSES,
                  "Tiny houses as small permanent or movable dwellings whose usability, legality, cost, access, and performance depend on site and classification.",
                  "current local zoning and adopted code, plans and permits, utility and cost records, product data, measured performance, and consented occupant accounts",
                  "Name jurisdiction, code edition, dwelling type, site, and date. Model appendices do not apply automatically; do not offer permit, engineering, or financial guarantees.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
