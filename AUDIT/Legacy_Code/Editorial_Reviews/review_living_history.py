"""Editorial question review for living history."""

from review_angle_plans import audit, revise_domain


LIVING_HISTORY = """history_origins|When a Site Began Interpreting Its Past|Why did one museum or site adopt living-history interpretation?|Trace planning records, goals, staffing, and community response.
famous_examples|A Renowned Reenactment Examined|Which sources support the event as visitors see it?|Compare script, objects, records, omissions, and audience questions.
hidden_stories|The Labor a Scene Leaves Out|Which workers and households are missing from one historical portrayal?|Compare payroll, census, oral histories, and presentation choices.
beginner_explainers|What Is Living History?|How does a staged interpretation differ from a primary source?|Use one scene to label evidence, inference, and deliberate invention.
advanced_concepts|Accuracy Beyond Costume|How should a program judge accuracy when sources disagree?|Compare period evidence, uncertainty, audience context, and interpretive choices.
mysteries_unsolved_cases|An Uncertain Historic Routine|What can sources establish about one everyday activity?|Compare records, artifacts, oral memory, experiments, and gaps.
technology_innovation|A Digital Layer at a Historic Site|Does one digital tool help visitors understand evidence and uncertainty?|Compare accessibility, source links, visitor testing, and privacy.
people_personalities|The Interpreter's Research Work|How does one interpreter prepare, revise, and explain a portrayal?|Review source notes, training, visitor dialogue, and supervision.
major_events|A Reenactment After New Evidence|How did a discovery or public challenge change one program?|Compare scripts, research records, decisions, and responses over time.
how_it_works|Building a Historical Scene|How does a site turn records into a visitor encounter?|Follow source selection, script review, props, accessibility, and feedback.
rise_fall|Why a Program Ended or Returned|What explains one living-history program's closure or revival?|Check funding, visitor use, staff, safety, and community support.
then_vs_now|The Same Past Told at Two Dates|How did one site's interpretation change across decades?|Compare dated scripts, signs, source base, and who was represented.
future_developments|A Proposed New Interpretation|Would one plan address a documented gap in a site's story?|Check source access, community input, staff capacity, and evaluation.
myths_vs_facts|An Authenticity Claim Tested|Does a scene's claim of exact historical accuracy survive source review?|Identify sourced details, plausible inference, and modern compromise.
documentary_stories|A Day of Interpretation|What does one program reveal through visitor questions and staff choices?|Observe with permission and link filmed scenes to their source trail.
source_trail|From Archive to Spoken Line|Which document supports one statement made by an interpreter?|Trace citation, context, translation, and revision.
material_evidence|Reading a Replica Object|Which details copy surviving artifacts and which were inferred?|Compare provenance, maker notes, material substitutions, and labels.
chronology_dispute|Which Year Is the Scene?|Do objects and dialogue represent one period or several?|Date each element and explain any composite presentation.
ordinary_lives|A Household Beyond the Famous Figure|How might one program portray routine work and care?|Use records of ordinary people and state where evidence is thin.
power_and_institutions|Who Authorizes the Story?|Who decides which roles and voices appear at one public site?|Examine governance, funding, consultation, and interpretive policy.
trade_and_exchange|Goods in a Recreated Marketplace|What do props reveal about actual trade and access?|Use inventories, prices, supply records, and material provenance.
language_and_labels|Period Words in a Modern Program|Which historical terms need context or should not be performed?|Check original usage, harm, audience, and community guidance.
maps_and_borders|The Site Outside the Stage|How did land, borders, and movement shape the portrayed community?|Use period maps, property records, migration, and present geography.
conflicting_accounts|Two Memories of the Same Event|How can a program present contradictory accounts honestly?|Attribute speakers, dates, incentives, and remaining uncertainty.
preservation_bias|What the Site Could Preserve|How do surviving buildings and records skew the story toward some lives?|Compare preserved material with missing places and marginalized accounts.
turning_point_test|Did One Event Change Daily Life?|Does evidence support treating one event as a local turning point?|Compare before and after records for several affected groups.
legacy_and_memory|What Visitors Remember|Do visitors distinguish documented history from performance?|Use consented evaluation, source prompts, and follow-up questions.
field_oral_history|A Narrator's Account in Interpretation|How may one recorded memory be used in a public program?|Document informed consent, review rights, attribution, and limitations.
field_archive_gap|A Role with Few Surviving Records|How should a site portray people absent from its archive?|Seek other source types, community expertise, and transparent uncertainty.
field_material_culture|A Demonstration Object's Evidence|What can one working replica demonstrate about a historical task?|Compare originals, construction records, observed use, and limits.
field_community_memory|A Community's Relationship to the Site|How do descendants and neighbors interpret the place today?|Use ongoing consent, varied views, and community-led framing.
field_representation_ethics|Who Should Portray Whom?|How can a program avoid exclusion and stereotype while staying evidence-led?|Review casting, training, scripts, community input, and visitor impact.
"""


if __name__ == "__main__":
    revise_domain("143", "143_living_history", LIVING_HISTORY,
                  "Living history as evidence-led public interpretation, examined through scripts, objects, performers, archives, visitor learning, and community representation.",
                  "dated program scripts and planning records, primary documents and object provenance, interpreter research notes, visitor evaluation, and consented oral histories and community accounts",
                  "Name site, period, program, and date. Distinguish documented fact, plausible inference, and performance; secure narrator consent and review rights; avoid portraying a community as a single voice.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
