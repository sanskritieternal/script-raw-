"""Editorial question designs for niche 222, Temple Tourism."""

from review_angle_plans import audit, revise_domain


TEMPLE_TOURISM = """history_origins|A Temple's Layers of History|Which dated building, worship, and patronage records explain one temple?|Separate archaeological phases from living traditions and later accounts.
famous_examples|A Famous Temple Visit Rechecked|What does a popular visitor account omit about the site?|Check worship rules, conservation needs, workers, neighbors, and source dates.
hidden_stories|The People Who Sustain a Temple|Whose care, craft, ritual, cleaning, and conservation work enables visits?|Use consented accounts and distinguish roles and authority.
beginner_explainers|Before Visiting a Living Temple|Which site-specific rules and meanings should a visitor learn?|Check current official hours, dress, entry, ritual, photography, and accessibility.
advanced_concepts|Worship and Visitor Capacity|How can a temple manage devotional use and tourism together?|Compare peak flows, sacred areas, queues, conservation, and community priorities.
mysteries_unsolved_cases|A Contested Temple Story|Which evidence supports competing claims about one site's past?|Attribute inscriptions, archaeology, texts, oral accounts, and uncertainties.
technology_innovation|Digital Access to a Temple|Does one booking or interpretation tool improve access?|Compare inclusion, privacy, queue time, worship experience, and maintenance.
people_personalities|A Custodian's Decision|How did one named authority or group change visitor practice?|Use dated rules, consultations, objections, and results.
major_events|A Festival's Effect on a Site|How did one documented event change access or conservation needs?|Compare ritual calendar, visitor flow, transport, waste, and safeguards.
how_it_works|Who Manages a Temple Visit?|How do custodians, trust, heritage authority, vendors, and local government interact?|Map site-specific roles without assuming one governance model.
rise_fall|A Temple's Visitor Trend|What explains a measured change in visits?|Check counts, reporting, pilgrimage season, transport, rules, and closures.
then_vs_now|One Temple Across Two Eras|How have worship, access, fabric, and neighborhood changed?|Use comparable dated records and consented current perspectives.
future_developments|Scenarios for a Busy Temple|Which conditions could shape visitor management?|State worship needs, conservation, transport, climate, and local priorities.
myths_vs_facts|A Popular Temple Fact Checked|Which primary evidence supports a repeated age or origin claim?|Separate dated fabric, tradition, legend, and modern reconstruction.
documentary_stories|One Temple's Visitor Decision|Why did a site change an entry or photography rule?|Trace rationale, stakeholder input, implementation, and effects.
map_vs_ground|What the Site Map Omits|Which active worship or access conditions differ from the map?|Check current routes, restricted areas, surface, crowds, and signage.
route_choices|Approaching a Sacred Site|Why do visitors and worshippers use different routes?|Compare ritual sequence, accessibility, transport, queues, and rights.
seasonality|A Temple Through the Calendar|How do festivals and weather alter use?|Specify tradition and site; compare current schedule and historical patterns.
local_voice|Neighbors and Worshippers Speak|How do different local groups describe visitor growth?|Seek consented voices and avoid one spokesperson standing for all.
landscape_process|The Temple and Its Setting|How do river, hill, coast, or climate affect the site?|Use mapped hazards, building evidence, and local management records.
accessibility|Who Can Participate in a Visit?|Which physical, information, or rule barriers matter?|Check paths, queues, facilities, language, timing, and site-specific policy.
infrastructure|The Hidden Work of Pilgrim Flow|Which water, sanitation, transport, and staff systems sustain visits?|Trace capacity, maintenance, funding, and peak demand.
environmental_pressure|What Visits Cost the Site|Which measurable pressures affect stone, water, waste, or neighbors?|Compare baseline, peak period, mitigation, and cultural priorities.
safety_decision|Current Conditions for One Visit|Which official information should a visitor verify before travel?|Check opening, closures, weather, crowd measures, transport, and site guidance.
place_history|Before the Current Temple Complex|What earlier uses and communities shaped the location?|Attribute archaeology, land records, texts, and living memory.
comparison_of_places|Two Temples, Different Visitor Rules|Why do two sites manage access differently?|Compare worship practice, governance, conservation, setting, and capacity.
responsible_access|Opening a Sacred Area|Who benefits and who may be harmed by expanded access?|Weigh custodial authority, worship, equity, conservation, and local livelihoods.
field_map_accuracy|Checking a Temple Access Map|Does the published route match current permitted movement?|Verify date, scale, entrances, restricted areas, and on-site signs.
field_place_names|Names of One Sacred Site|How do formal, local, and devotional names differ?|Record language, source, community use, and respectful attribution.
field_local_history|A Temple and Its Neighborhood|How did trade, housing, and worship reshape the surrounding place?|Compare maps, archives, and consented resident accounts.
field_visitor_access|A Temple Visit Access Audit|Which stage presents a barrier to a defined visitor?|Check travel, booking, queue, steps, toilets, information, and support.
field_landscape_change|A Sacred Setting in Motion|How has land use or a river or coast around the temple changed?|Use comparable maps, conservation records, and local accounts.
"""


if __name__ == "__main__":
    revise_domain("222", "222_temple_tourism", TEMPLE_TOURISM,
                  "Temple tourism through living worship, custodianship, historical evidence, visitor access, conservation, and local livelihoods.",
                  "current site and custodial rules, archaeological and conservation records where relevant, dated visitor and service data, maps, and consented worshipper, worker, and neighbor accounts",
                  "Name temple, tradition, custodian, jurisdiction, and date. Attribute legends and contested histories; verify current entry and photography rules and do not assume a living temple functions only as a monument.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
