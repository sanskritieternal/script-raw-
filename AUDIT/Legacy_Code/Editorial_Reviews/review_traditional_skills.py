"""Editorial question review for traditional skills."""

from review_angle_plans import audit, revise_domain


SKILLS = """history_origins|A Skill in Its Local History|When and why did one community begin practicing a named skill?|Trace dated records and practitioner accounts; avoid an invented single origin.
famous_examples|A Celebrated Craft Tradition Revisited|What does one widely displayed craft reveal about its makers?|Compare community accounts, production records, objects, and exhibition labels.
hidden_stories|Labor Behind the Finished Object|Whose gathering, preparation, and teaching work is left out?|Follow the full process through consented practitioner testimony.
beginner_explainers|What Makes a Skill Traditional?|How do practitioners define continuity and change in one practice?|Use local terms and distinguish living knowledge from fixed style.
advanced_concepts|The Economics of Transmission|What conditions let an apprentice sustain one traditional skill?|Compare teaching time, income, materials, access, and local demand.
mysteries_unsolved_cases|An Uncertain Craft Attribution|What can establish who made one older object?|Compare provenance, material, technique, testimony, and uncertainty.
technology_innovation|New Tools in a Living Practice|How did one tool change a craft without ending its continuity?|Compare practitioner choices, output, time, and community meaning.
people_personalities|A Teacher and Their Students|How does one craft teacher transmit judgment beyond technique?|Use consented interviews and observe learning within agreed boundaries.
major_events|A Policy That Changed a Craft|How did one rule or development alter access to materials or markets?|Trace dated policy, supply, livelihoods, and community response.
how_it_works|The Decisions Behind One Object|Which material and design choices shape a named craft product?|Follow an authorized maker's explanation, leaving restricted knowledge private.
rise_fall|Why a Workshop Closed or Reopened|Which conditions explain one workshop's changing fortunes?|Compare orders, income, succession, materials, and location.
then_vs_now|One Skill Across Generations|What changed and what remained important to practitioners?|Compare dated objects and consented intergenerational accounts.
future_developments|A Safeguarding Plan Under Review|Would one proposed program help a community continue its skill?|Check practitioner priorities, teaching capacity, resources, and control.
myths_vs_facts|The Myth of an Unchanged Tradition|Does evidence show that one craft has always used the same materials?|Compare dated objects, oral history, trade, and documented adaptations.
documentary_stories|A Season in One Craft Community|How do material cycles, teaching, and sales shape practitioners' lives?|Follow consented participants through a defined production period.
source_trail|Tracing a Craft Description|Where did a common description of one skill originate?|Compare early records, translations, interviews, and later copying.
material_evidence|What an Object Can and Cannot Tell Us|Which production choices are visible in one surviving object?|Use qualified examination and distinguish observation from inference.
chronology_dispute|When Was a Technique Adopted?|Why do accounts differ on the date of one technique's introduction?|Compare dated examples, records, and practitioner memory.
ordinary_lives|A Maker's Working Week|How does one practitioner divide time among making, teaching, and selling?|Use consented observation and avoid treating one person as representative.
power_and_institutions|Who Gets to Define Authenticity?|How do museums, buyers, and practitioners disagree on a craft's standards?|Compare selection criteria, market effects, and community authority.
trade_and_exchange|The Journey of a Material|How does one craft material reach its makers?|Trace sourcing, cost, trade, access rights, and environmental effects.
language_and_labels|What Is This Skill Called?|How do local names differ from a museum or market label?|Document translations with practitioner review and historical context.
maps_and_borders|A Craft Across Communities|How does a skill travel across a border without one simple owner?|Map documented movement, shared techniques, and distinct local meanings.
conflicting_accounts|Two Histories of a Skill|Where do official and practitioner accounts agree or diverge?|Present attributed sources, timing, and uncertainty without forced resolution.
preservation_bias|Which Craft Objects Survive?|How have collecting practices shaped what we think a tradition was?|Compare durable museum objects with everyday work and missing records.
turning_point_test|Was This an Endangered Skill?|What evidence supports a claim that one practice was declining?|Compare practitioner numbers, training, income, and changing forms.
legacy_and_memory|A Skill After Its Public Recognition|Did recognition change practitioners' control and livelihood?|Compare before and after accounts, funding, markets, and local views.
field_community_ownership|Who Controls the Story?|What permission and decision rights do practitioners want in a documentary?|Agree on consent, attribution, restricted knowledge, review, and benefits.
field_object_provenance|An Object's Path to a Collection|How did one craft object move from maker to current holder?|Trace acquisition, consent, ownership records, and contested gaps.
field_living_practice|A Skill Still Being Made|How do current makers adapt an inherited practice for present needs?|Follow named practitioners and distinguish their choices from stereotypes.
field_conservation_choice|Preserve an Object or Support a Maker?|How do conservation and living transmission needs differ in one case?|Compare museum care, teaching resources, access, and practitioner priorities.
field_cultural_translation|Explaining a Craft Across Languages|Which concepts lose meaning in a short translated explanation?|Review language and framing with speakers and practitioners.
"""


if __name__ == "__main__":
    revise_domain("141", "141_traditional_skills", SKILLS,
                  "Traditional skills as living practices shaped by makers, teaching, materials, livelihood, changing tools, and community authority.",
                  "consented practitioner and apprentice accounts, dated objects and records, local terminology, workshop and material records, museum provenance, and community-led safeguarding documents",
                  "Name practice, community, place, and period. Seek free, informed, ongoing consent; respect restricted knowledge and community control; avoid claiming a single origin or frozen authentic form.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
