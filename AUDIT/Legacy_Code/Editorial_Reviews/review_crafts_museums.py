"""Editorial question designs for craft traditions and museums."""

from review_angle_plans import audit, revise_domain


CRAFTS = """history_origins|Where a Craft Tradition Took Shape|What dated evidence shows how one craft practice developed?|Compare objects, maker accounts, trade records, and later origin stories.
famous_examples|A Celebrated Craft Object|What does one well-known object reveal about materials, makers, and use?|Trace provenance, production context, and reception without treating it as typical.
hidden_stories|The Makers Missing from the Label|Whose work is obscured by a workshop or collector's name?|Compare signatures, wage records, oral histories, and family knowledge.
beginner_explainers|What Makes This a Craft?|Which learned skills and material choices define one local practice?|Follow a maker's authorized explanation without disclosing restricted knowledge.
advanced_concepts|Variation Within a Tradition|How do makers distinguish acceptable variation from a changed method?|Compare practitioner views, function, market demand, and historical evidence.
mysteries_unsolved_cases|A Maker or Origin Disputed|What can be established about an object's maker or place of origin?|Compare marks, materials, provenance gaps, and conflicting testimony.
technology_innovation|A New Tool in an Old Workshop|How did one tool alter time, quality, training, or livelihoods?|Compare documented methods and makers' assessments across generations.
people_personalities|A Master and Their Apprentices|How was one craft skill passed between named people?|Credit teachers, apprentices, households, and community rules of access.
major_events|A Market Shift for Makers|How did one dated trade or policy change affect a craft community?|Compare orders, prices, materials, and household accounts before and after.
how_it_works|From Material to Object|Which stages turn a raw material into one craft product?|Explain observable stages at a non-instructional level with maker consent.
rise_fall|Why a Craft Workshop Closed|Which pressures explain the decline of one local workshop network?|Compare material supply, labor, market, policy, and succession records.
then_vs_now|A Craft Across Two Periods|What changed in material, technique, use, and maker income?|Use dated examples and current practitioners without defining a pure past.
future_developments|Can Training Sustain the Skill?|What would make a proposed apprenticeship viable for makers and learners?|Compare time, pay, access to materials, demand, and community priorities.
myths_vs_facts|The Handmade Label Tested|Does a product's craft claim match its actual production?|Check maker contribution, mechanized steps, label rules, and supply records.
documentary_stories|One Object's Working Life|How did an object move from maker to user to collector or museum?|Build a documented chain of making, sale, repair, ownership, and display.
source_trail|The Story Behind the Pattern|Where did a widely repeated interpretation of one motif originate?|Trace catalogues, interviews, and makers' own explanations.
material_evidence|What the Object Can Tell Us|Which material traces reveal how a craft object was made or used?|Compare tool marks, wear, repairs, and non-destructive analysis limits.
chronology_dispute|How Old Is This Technique?|Do objects and oral histories support a claimed age for a method?|Compare dated examples and evidence gaps without dismissing oral knowledge.
ordinary_lives|Work in a Maker Household|How are time, care, and income shared around one craft?|Use consented accounts and work records without making one household typical.
power_and_institutions|Who Controls Craft Recognition?|How do guilds, certifiers, traders, or state bodies determine who counts as a maker?|Compare rules, benefits, exclusions, and practitioner perspectives.
trade_and_exchange|The Craft Beyond Its Home|How did one object or technique travel through trade?|Map dated buyers, intermediaries, prices, and changes in production.
language_and_labels|Naming the Technique|What is lost when a maker's term becomes a commercial category?|Compare local usage, translations, labels, and maker consent.
maps_and_borders|A Craft Across Regions|Do political borders match the places where one skill is practiced?|Use dated maps and practitioner networks, avoiding exclusive origin claims.
conflicting_accounts|Who Owns the Design Story?|Why do makers, dealers, and collectors describe one object differently?|Attribute each account and test against provenance and material evidence.
preservation_bias|What Collectors Chose to Keep|Which everyday objects and makers were omitted from collections?|Compare acquisition records with household and workshop evidence.
turning_point_test|Did a Craft Scheme Help?|Did one training, subsidy, or market program improve maker livelihoods?|Compare income, control, participation, and sustained practice over time.
legacy_and_memory|Remembering a Workshop|How do former makers and their families describe a closed craft center?|Pair consented memories with records and acknowledge differing accounts.
field_community_ownership|Who Can Share the Skill?|Who decides which craft knowledge may be filmed, taught, or sold?|Follow community permissions, restricted knowledge, and benefit sharing.
field_object_provenance|Tracing One Craft Object|Can an object's maker and ownership path be reconstructed?|Document marks, transactions, oral accounts, and unresolved gaps.
field_living_practice|A Skill Still Being Made|How do present-day makers adapt a technique for current needs?|Observe consented practice and ask makers which changes matter.
field_conservation_choice|Repairing a Craft Object|Whose priorities shape whether a used object is repaired or preserved?|Compare maker, owner, conservator, and community views before intervention.
field_cultural_translation|Explaining Craft Without Extraction|How can a craft story be shared across languages without exposing restricted knowledge?|Co-review terms and footage with practitioners before publication."""


MUSEUMS = """history_origins|Why This Museum Was Founded|Which aims and power relations shaped one museum's founding?|Compare charters, acquisition records, donors, and community accounts.
famous_examples|A Famous Exhibition Revisited|What did a celebrated exhibition teach, and what did it omit?|Compare curatorial files, visitor responses, and source-community views.
hidden_stories|Who Built the Collection?|Whose collecting, conservation, or interpretation labor is uncredited?|Trace staff, field workers, donors, and affected communities in records.
beginner_explainers|How an Object Enters a Museum|What decisions occur between acquisition and display?|Follow one documented object through title, provenance, cataloguing, and care.
advanced_concepts|Legal Title and Ethical Claim|Can an acquisition be lawful yet still contested by a source community?|Separate law, provenance, consent, and ethical arguments in one case.
mysteries_unsolved_cases|A Provenance Gap|Which periods in one object's ownership history remain unknown?|Identify documents found, missing transfers, and competing claims without filling gaps.
technology_innovation|Digitizing a Collection|Who gains access when a collection is digitized, and who may face harm?|Compare metadata quality, rights, culturally sensitive access, and use data.
people_personalities|Who Interprets the Object?|How did curators and community experts disagree or collaborate on one display?|Use attributed decisions and document changes to labels and authority.
major_events|A Museum Policy Turning Point|What changed after one return request, protest, or policy revision?|Compare dated decisions, collection records, and stakeholder accounts.
how_it_works|Conservation in Context|How does a museum decide whether and how to treat one object?|Trace condition, materials, consultation, risk, and documentation.
rise_fall|Why an Exhibition Closed|Which evidence explains the end or redesign of one gallery?|Compare budgets, visitor data, criticism, conservation needs, and policy.
then_vs_now|An Object's Labels Across Time|How did a museum's description of one object change?|Compare dated labels, source evidence, and who contributed to revision.
future_developments|A Proposed Return or Shared Custody|What would each proposed arrangement require in one contested case?|Examine claims, law, care, access, and community priorities conditionally.
myths_vs_facts|The Rescue Narrative Checked|Does a museum's claim of saving an object fit its acquisition history?|Trace transfer, condition, legal context, and source-community testimony.
documentary_stories|An Object's Museum File|What does a complete case file reveal about one collection item?|Build a dated chain of acquisition, cataloguing, display, loans, and disputes.
source_trail|Who Wrote the Label?|Which source underlies an authoritative-sounding museum statement?|Trace original catalogues, later citations, and corrections.
material_evidence|Reading Conservation Records|What can imaging or condition reports establish about one object?|Distinguish physical observations from cultural interpretation and ownership.
chronology_dispute|When Was It Acquired?|Why do museum and source-community records date one transfer differently?|Compare transaction files, oral history, and the event each date describes.
ordinary_lives|The Workers Behind a Museum|How do registrars, guards, educators, and cleaners shape visitor access?|Compare work routines, resources, and attributed staff perspectives.
power_and_institutions|Who Decides What Is Displayed?|How are acquisition, loans, labels, and returns governed in one institution?|Examine boards, policies, budgets, and source-community participation.
trade_and_exchange|The Market Before the Museum|Through which dealers or collectors did one object pass?|Trace documented transfers, prices where available, and legal context.
language_and_labels|Naming a Collection|How does a museum's terminology affect a community's representation?|Compare catalog names, community language, search access, and label revisions.
maps_and_borders|Objects Across Changing Borders|How do changing borders complicate an object's origin and return claims?|Use dated maps and legal contexts without equating borders with identity.
conflicting_accounts|Two Histories of One Acquisition|Where do institutional and community accounts of an acquisition diverge?|Attribute both accounts and test against documents without presuming symmetry.
preservation_bias|Why Some Objects Survive in Catalogues|How did acquisition priorities shape the record of one culture?|Compare collected objects with documented everyday practice and absences.
turning_point_test|Did Co-Curation Change the Gallery?|What changed after source-community participation in one exhibition?|Compare authority, labels, access, resources, and participant assessments.
legacy_and_memory|A Museum and Its Neighbors|How have local communities experienced a museum over time?|Compare access, programs, employment, and consented memories across periods.
field_oral_history|Recording an Object's Memory|What does a consented oral history add to an object's file?|Keep narrator control, context, restrictions, and archival preservation visible.
field_archive_gap|When the Acquisition File Is Thin|Which missing records matter most to a provenance question?|List known gaps, alternative archives, and limits on inference.
field_material_culture|Object Study With Community Experts|What do material features and community knowledge jointly reveal?|Record methods and permissions; distinguish analysis from restricted knowledge.
field_community_memory|Memory of a Collection|How do different generations describe one museum-held object?|Use consented accounts and note change, disagreement, and access wishes.
field_representation_ethics|Who Can Approve the Display?|How does a museum handle sensitive material and community objections?|Examine consultation, consent, restrictions, remedies, and revision authority."""


if __name__ == "__main__":
    revise_domain("095", "095_handicrafts_traditional_skills", CRAFTS,
                  "Living craft skills, materials, makers, transmission, livelihoods, trade, attribution, and community control.",
                  "dated objects and workshop records, material studies, market and training records, and consented maker and community accounts",
                  "Name craft, community, object, and period. Seek maker permission for filming or sharing knowledge, protect restricted practices, and avoid a single authentic version.")
    revise_domain("096", "096_museums_cultural_heritage", MUSEUMS,
                  "Museums as institutions of acquisition, care, interpretation, access, provenance research, and contested authority.",
                  "museum acquisition and conservation files, dated labels, applicable law and ethics guidance, source-community records, and consented interviews",
                  "Name object, institution, jurisdiction, and date. Distinguish legal title from ethical claim, document provenance gaps, and respect source-community restrictions and consent.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
