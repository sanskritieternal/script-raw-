"""Editorial question designs for niche 187, Outdoor Life."""

from review_angle_plans import audit, revise_domain


OUTDOOR = """history_origins|Who Defined Outdoor Recreation?|When did access to one landscape become framed as recreation?|Compare earlier land use, ownership, conservation policy, and local accounts.
famous_examples|A Celebrated Park Experience Examined|Who could take part in a widely praised outdoor experience?|Check admission, transport, cost, physical access, and the people displaced or excluded.
hidden_stories|The Workers Behind a Day Outside|Whose labor keeps an outdoor site usable?|Trace rangers, cleaners, guides, maintenance crews, and seasonal workers.
beginner_explainers|Planning a First Outdoor Visit|What decisions should a newcomer make before visiting one site?|Check current rules, weather, transport, route, water, facilities, and return time.
advanced_concepts|Access, Conservation, and Capacity|How can a land manager balance visitor access with ecological limits?|Compare visitor demand, monitoring, closures, mitigation, and public input.
mysteries_unsolved_cases|Why Use Changed at One Site|What explains an unexplained change in visits or impacts?|Test counting methods, access rules, transport, weather, and local events.
technology_innovation|When Equipment Changes Access|Did one outdoor technology expand participation or shift risk?|Compare adoption, price, usability, failures, and ecological effects.
people_personalities|A Steward's Decision|How did one named person's decision change a site's use?|Use dated plans, correspondence, objections, and outcomes.
major_events|A Closure That Changed Outdoor Use|What changed after one documented fire, flood, protest, or policy event?|Separate immediate disruption from lasting management change.
how_it_works|How an Outdoor Site Is Managed|Who maintains trails, facilities, habitats, and visitor information?|Follow budgets, staffing, inspections, permits, and feedback.
rise_fall|A Place's Visitor Boom|Why did visits to one outdoor site rise and later change?|Compare counts with population, publicity, access, season, and measurement.
then_vs_now|A Site Across Two Periods|How has one site's access and ecological condition changed?|Use comparable maps, counts, monitoring, rules, and local testimony.
future_developments|Scenarios for a Busy Outdoor Site|How might climate and visitor demand alter site management?|State assumptions and compare feasible adaptation options.
myths_vs_facts|Does Nature Always Recover Quickly?|What evidence supports a popular claim about recreation impacts?|Define ecosystem, activity, exposure, recovery measure, and timeframe.
documentary_stories|One Site, Multiple Stakeholders|How did visitors, residents, workers, and land stewards respond to one decision?|Build a dated record and attribute each perspective.
map_vs_ground|A Map's Missing Barriers|Which obstacles does a site map fail to show?|Compare mapped routes with grade, surface, shade, signage, and current closures.
route_choices|The Route People Actually Take|Why do visitors leave a designated route at one site?|Study wayfinding, desire lines, congestion, safety, and habitat impacts.
seasonality|When the Same Place Changes|How do seasonal conditions alter access and ecological sensitivity?|Compare local forecasts, closures, water, daylight, and habitat calendars.
local_voice|Residents' View of an Outdoor Site|What do neighboring communities say about visitor use?|Seek consented perspectives and distinguish shared concerns from individual views.
landscape_process|The Ground Beneath the Trail|Which physical process shapes one outdoor landscape?|Use geology, hydrology, vegetation, and dated field observations.
accessibility|Who Can Use This Outdoor Site?|Which barriers affect visitors with different mobility or sensory needs?|Check published accessibility details against on-site conditions and user accounts.
infrastructure|The Hidden Cost of Access|What infrastructure makes visits possible and who pays for it?|Follow parking, toilets, water, trails, maintenance budgets, and beneficiaries.
environmental_pressure|Where Recreation Leaves a Trace|Which activity creates a measurable impact at one site?|Measure soil, vegetation, waste, noise, or wildlife response with context.
safety_decision|The Turnaround Decision|What information should shape a go or turn-back decision?|Use current local alerts, weather, route condition, daylight, and group capability.
place_history|Before the Recreation Site|How was one place used and governed before today's designation?|Use land records and community accounts, including Indigenous perspectives where relevant.
comparison_of_places|Two Sites, Different Access|Why do two nearby outdoor sites serve different visitors?|Compare transport, cost, facilities, rules, terrain, and use data.
responsible_access|A Crowding Policy's Trade-offs|Who gains and loses when a site limits visitor numbers?|Study permits, displacement to nearby sites, ecological outcomes, and local economy.
field_land_stewardship|Who Stewards the Land?|How do stewardship rights and responsibilities work at one site?|Identify legal authority, Indigenous or community roles, funding, and decision power.
field_seasonal_conditions|A Seasonal Risk Window|When does a site's safe and permitted use change during the year?|Check current operator notices against historical seasonal patterns.
field_skill_and_safety|Matching Activity to Ability|What skills does one outdoor activity require at a specific site?|Define route difficulty, supervision, equipment, emergency access, and alternatives.
field_resource_use|Water, Waste, and Visitor Demand|How does recreation affect one limited local resource?|Use measured use, replenishment, treatment capacity, and management response.
field_local_knowledge|What Local Knowledge Adds|Which place-specific observation improves an official visitor guide?|Attribute consented local accounts and verify against site records.
"""


if __name__ == "__main__":
    revise_domain("187", "187_outdoor_life", OUTDOOR,
                  "Outdoor life through access, stewardship, visitor decisions, labor, ecology, and place history.",
                  "site management plans, current closures and alerts, land records, visitor and ecological monitoring, accessibility details, and consented local accounts",
                  "Name the site, jurisdiction, season, and date. Check current local conditions before practical safety advice; distinguish recreation from land rights and avoid treating one visitor experience as universal.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
