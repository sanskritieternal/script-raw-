"""Direct question-design review of Śaiva, Vaiṣṇava, and Śākta traditions."""
from review_angle_plans import revise_domain, audit

SHAIVISM = """history_origins|A Śaiva Lineage in Dated Sources|Which records show one named Śaiva community or institution taking shape?|Compare inscriptions, texts, sites, and later lineage narratives.
famous_examples|A Śaiva Site in Its Own Tradition|How do custodians explain one prominent site, and what does its history show?|Attribute devotional meaning and use dated material evidence separately.
hidden_stories|People Sustaining a Śaiva Community|Whose work in teaching, art, care, or maintenance is absent from familiar histories?|Use consented accounts and institutional records.
beginner_explainers|Many Śaiva Traditions|How do two named Śaiva communities differ in text, practice, or philosophy?|Describe each on its own terms without a single universal template.
advanced_concepts|Śiva, Liberation, and Interpretation|How do named Śaiva texts differ over one philosophical question?|Compare specified passages and commentaries, not generic doctrine.
mysteries_unsolved_cases|A Śaiva Text's Attribution|Which evidence supports or complicates the attribution of a named text?|Examine manuscript colophons, citations, and later tradition.
technology_innovation|Digitizing a Śaiva Manuscript|Can a new edition clarify one disputed reading without erasing context?|Record witness provenance, access permission, and editorial choices.
people_personalities|A Śaiva Teacher in the Sources|What can a named teacher's writings and institutional records establish?|Separate their argument from later devotional biography.
major_events|A Change at a Śaiva Institution|How did one dated event alter teaching, worship, or stewardship?|Compare records before and after with practitioner voices.
how_it_works|A Local Śaiva Observance|How do participants explain the public sequence of one observance?|Identify community and place; respect restricted elements.
rise_fall|Patronage of a Śaiva Site|Why did resources to one shrine or teaching center change?|Use grants, accounts, inscriptions, and local history.
then_vs_now|One Śaiva Practice Across Generations|What changed in one community's practice or teaching?|Compare dated descriptions with consented present accounts.
future_developments|A Śaiva Heritage Choice|What would one conservation or teaching proposal preserve or alter?|Assess custodial priorities, access, cost, and living use.
myths_vs_facts|A Claim About All Śaivas|Does one generalization fit distinct Śaiva lineages?|Compare named texts and communities; attribute their own descriptions.
documentary_stories|A Śaiva Text or Site Through Time|How did one source or place acquire its present form?|Trace manuscripts, patronage, alterations, and living memory.
text_source|A Śaiva Passage in Context|What does one passage say within its named text and recension?|Cite original, edition, translation, and neighboring argument.
interpretive_lineages|Two Śaiva Readings|How do two lineages interpret one shared term or practice?|Represent each account with its own authoritative sources.
lived_practice|A Community's Everyday Devotion|What role does Śaiva practice play in a named community's daily life?|Use consented voices and specify time and place.
ritual_sequence|A Rite as Locally Performed|Which stages of one public Śaiva rite do participants identify?|Distinguish text prescription from observed practice and respect permissions.
language_translation|A Śaiva Term in Translation|How does translating one Sanskrit or regional term alter interpretation?|Compare usage, grammar, and practitioner explanation.
regional_variants|Śaiva Practice in Two Regions|How do comparable communities differ in liturgy, art, or institutions?|Match period and lineage; explain local history.
art_and_devotion|An Image of Śiva in Context|How do form, placement, and use shape one image's meaning?|Use art records and attributed devotional interpretations.
community_memory|Remembering a Śaiva Teacher or Site|How does community memory relate to the surviving historical record?|Present both with their provenance and limits.
ethics_in_context|Entry and Participation|How have rules at one Śaiva institution affected different people?|Use dated policy, law, and affected voices without imposing a universal pattern.
source_and_history|Dating a Śaiva Source|What can an inscription or manuscript establish about a named tradition?|Check provenance, date, text, and later copying.
encounter_and_exchange|Śaiva Exchange with a Neighboring Tradition|What documented contact shaped one text, practice, or image?|Trace specific citations or patronage rather than presumed borrowing.
contemporary_voice|A Present Śaiva Custodian Speaks|What issue does one practitioner or custodian identify as urgent?|Use consented testimony and other affected perspectives.
field_textual_lineage|A Śaiva Passage Across Witnesses|Which variants appear in a named text's manuscripts?|Record source provenance and editorial uncertainty.
field_regional_practice|One Local Śaiva Community|How is a named practice taught and sustained there?|Document consent, institutions, and regional context.
field_translation_choice|A Contested Śaiva Word|Which rendering fits one bounded passage?|Compare grammar, commentary, and local usage.
field_ritual_context|Text and Śaiva Rite|How is one named text used in a specific observance?|Ask participants and distinguish prescribed from practiced sequence.
field_community_interpretation|A Śaiva Lineage's Reading|How does one community explain a disputed concept?|Attribute its account and acknowledge internal differences."""

VAISHNAVISM = """history_origins|A Vaiṣṇava Community in the Record|Which dated texts and institutions show one lineage forming?|Compare inscriptions, commentaries, patronage, and later memory.
famous_examples|A Celebrated Vaiṣṇava Practice|How does one community understand a widely known observance?|Specify lineage and place; compare texts and living accounts.
hidden_stories|Workers Behind Vaiṣṇava Devotion|Whose teaching, music, cooking, or care work is overlooked?|Use consented community voices and records.
beginner_explainers|One Family of Many Lineages|How do two Vaiṣṇava traditions differ in deity focus, texts, or worship?|Describe each in its own terms without ranking authenticity.
advanced_concepts|Grace and Human Effort|How do named Vaiṣṇava commentators approach one theological tension?|Compare exact passages and context.
mysteries_unsolved_cases|A Lineage Attribution Under Review|What evidence supports one disputed date or authorship?|Examine manuscripts, quotations, and institutional tradition.
technology_innovation|Preserving a Vaiṣṇava Song Corpus|Can digitization help document one local repertoire with community control?|Compare recording fidelity, permissions, metadata, and access.
people_personalities|A Vaiṣṇava Teacher's Documented Work|What did one named teacher write or organize?|Separate surviving texts from later hagiography.
major_events|A Temple or Lineage Turning Point|How did one dated reform or migration alter practice?|Use institutional records and practitioner accounts.
how_it_works|A Local Devotional Gathering|How do participants describe the public order and purpose of one gathering?|Attribute meanings to the named community; avoid instructions.
rise_fall|A Vaiṣṇava Institution's Resources|Why did one institution expand or lose capacity?|Compare patronage, accounts, membership, and local conditions.
then_vs_now|A Vaiṣṇava Song Across Generations|What changed in performance or interpretation of one named song?|Compare recordings, texts, and consented performers.
future_developments|A Living Heritage Decision|Which proposal would support teaching while preserving community control?|Assess staffing, access, funding, and practitioner priorities.
myths_vs_facts|One Vaiṣṇava View?|Does a broad claim about Vaiṣṇavism survive comparison of named lineages?|Read their own sources and state differences fairly.
documentary_stories|A Devotional Text's Journey|How did one Vaiṣṇava poem or commentary spread?|Trace manuscripts, translations, performance, and institutions.
text_source|A Vaiṣṇava Passage in Context|What does a named passage say in its source text?|Cite edition, language, setting, and surrounding lines.
interpretive_lineages|Different Readings of a Shared Verse|How do two Vaiṣṇava commentators interpret one passage?|Compare original explanations and theological assumptions.
lived_practice|Vaiṣṇava Life in One Community|How do members describe the place of devotion in daily life?|Use consented voices and avoid universalizing.
ritual_sequence|A Named Temple Observance|Which public stages do local practitioners identify?|Distinguish local custom from textual instruction; respect restrictions.
language_translation|A Devotional Term's Meaning|How does translating one Sanskrit or vernacular word affect a song?|Compare poetic context, commentary, and performer interpretation.
regional_variants|A Practice Across Two Regions|How do two communities adapt a shared Vaiṣṇava form?|Compare lineage, language, patronage, and date.
art_and_devotion|Viṣṇu or a Related Form in Art|How does one image's iconography relate to local devotion?|Use provenance, texts, and attributed practitioner interpretation.
community_memory|Remembering a Vaiṣṇava Saint|How does a community narrate one figure's life beside historical sources?|Present tradition and dated evidence distinctly.
ethics_in_context|Access to Devotional Space|How have participation rules affected a named community?|Use local policy, law, and affected voices.
source_and_history|A Vaiṣṇava Text's Witnesses|What can manuscripts and quotations tell us about a work's history?|Separate copy date, claimed authorship, and later reception.
encounter_and_exchange|A Shared Devotional Form|What evidence shows exchange between named communities?|Trace dated songs, teachers, and institutions, not resemblance alone.
contemporary_voice|A Practitioner Interprets Change|What does one current Vaiṣṇava teacher or singer value in a changing practice?|Use consent and include differing community views.
field_textual_lineage|A Commentary Across Copies|Which variants affect one Vaiṣṇava argument?|Compare provenance, edition, and translation.
field_regional_practice|One Regional Vaiṣṇava Setting|How is a named practice taught and sustained?|Document language, lineage, institution, and local voices.
field_translation_choice|A Verse in Two Languages|What changes when a devotional verse is translated?|Compare original imagery, meter, and explanatory tradition.
field_ritual_context|A Text Within Worship|Where does one passage enter a documented local rite?|Ask practitioners and avoid presenting a universal order.
field_community_interpretation|A Lineage Explains Devotion|How does one Vaiṣṇava community define a contested idea?|Attribute its own sources and acknowledge internal variation."""

SHAKTISM = """history_origins|A Śākta Tradition's Early Records|Which dated sources document one goddess-centered community or site?|Compare inscriptions, texts, images, and later origin stories.
famous_examples|A Goddess Festival in Local Context|How does one community explain a celebrated observance?|Specify place and lineage; distinguish public practice from generalized claims.
hidden_stories|Women and Other Stewards of a Tradition|Whose labor or authority is overlooked in one Śākta history?|Use consented accounts and institutional evidence without assumptions from gender alone.
beginner_explainers|Many Ways of Honoring Devī|How do two Śākta communities differ in theology, texts, and practice?|Present each tradition in its own terms.
advanced_concepts|Power and the Divine Feminine|How do named texts or teachers explain śakti differently?|Compare passages and historical contexts, avoiding a single doctrine.
mysteries_unsolved_cases|A Goddess Site's Contested History|Which evidence bears on one disputed site identification or date?|Separate archaeology, inscription, later narrative, and living belief.
technology_innovation|Documenting a Living Śākta Tradition|Can an archive preserve one public repertoire while honoring restrictions?|Ask custodians about consent, access, and context.
people_personalities|A Śākta Teacher or Patron|What can dated records establish about one named contributor?|Separate source-backed acts from devotional biography.
major_events|A Shrine or Community Changes|How did one dated event affect Śākta worship or access?|Compare records and affected practitioner perspectives.
how_it_works|A Public Goddess Observance|What do participants say occurs and why in one named observance?|Describe local stages without revealing restricted practice or instructing worship.
rise_fall|Patronage of a Goddess Site|How did resources and custodianship change at one site?|Use grants, accounts, buildings, and local testimony.
then_vs_now|One Śākta Festival Across Generations|Which elements changed and which remain meaningful to participants?|Compare dated accounts with consented voices.
future_developments|Conserving a Living Shrine|What would one preservation plan protect or limit?|Consider material condition, ritual use, access, and custodians' priorities.
myths_vs_facts|A Single Goddess Tradition?|Does a broad claim fit different Śākta texts and communities?|Compare named sources without reducing diversity to a stereotype.
documentary_stories|A Goddess Narrative Through Sources|How did one story move across texts, images, and performance?|Trace versions, dates, and local meaning.
text_source|A Devī Passage in Context|What does one passage say in its named source and recension?|Cite original, edition, translation, and narrative setting.
interpretive_lineages|Two Readings of Devī|How do two named Śākta lineages interpret one divine figure or concept?|Use each community's own sources and voices.
lived_practice|Devī Devotion in One Community|How do participants describe their everyday or seasonal practice?|Use consent and specify place, date, and community.
ritual_sequence|A Locally Documented Rite|Which public stages are described by practitioners at one site?|Respect restricted elements and distinguish text from practice.
language_translation|A Goddess Epithet in Translation|How does rendering one name or term shift meaning?|Compare original-language context and practitioner explanations.
regional_variants|One Goddess Across Regions|How do two communities relate to a similarly named divine figure?|Compare sources, ritual, history, and self-description without assuming identity.
art_and_devotion|A Devī Image in Use|How do image form, placement, and festival context shape meaning?|Use art provenance and attributed devotional interpretation.
community_memory|A Goddess Site in Local Memory|How do custodians recount one site's origin and change?|Pair attributed memory with dated material evidence.
ethics_in_context|Access, Authority, and Representation|How are roles in one Śākta institution assigned and contested?|Use local rules, history, and affected voices; avoid romanticizing empowerment.
source_and_history|Dating a Śākta Text or Image|What can provenance and citation establish about one source?|Separate manuscript or object date from earlier tradition.
encounter_and_exchange|Śākta Contact with Other Traditions|What documented exchange shaped one practice or image?|Trace named texts, patrons, and places instead of assuming influence.
contemporary_voice|A Current Śākta Custodian's View|What change does one practitioner identify at a living site?|Use consent and include other affected community perspectives.
field_textual_lineage|A Devī Text Across Witnesses|Which variants appear in a specified passage?|Record manuscripts, edition choices, and uncertainties.
field_regional_practice|One Regional Goddess Tradition|How is a named observance taught and maintained?|Document local language, custodians, permissions, and date.
field_translation_choice|Two Renderings of a Divine Name|What contextual evidence favors each translation?|Compare grammar, textual usage, and local interpretation.
field_ritual_context|A Text in Goddess Worship|How does one community use a passage during an observance?|Ask participants and respect restrictions on documentation.
field_community_interpretation|A Śākta Community Explains Its Practice|How do members interpret a contested symbol or rite?|Represent internal diversity and attribute every account."""

if __name__ == "__main__":
    revise_domain("273", "273_shaivism", SHAIVISM,
                  "Distinct Śaiva lineages, philosophical texts, temple and community practice, art, and living stewardship.",
                  "specified Śaiva texts and editions, dated inscriptions and institutional records, site archives, and consented practitioner and custodian accounts",
                  "Name the lineage, place, source, and date; attribute devotional claims and respect restricted practice. Do not describe one Śaiva community as representative of all.")
    revise_domain("274", "274_vaishnavism", VAISHNAVISM,
                  "Distinct Vaiṣṇava lineages, commentaries, devotional song, temple practice, and community interpretation.",
                  "specified texts, editions, commentaries and songs, dated temple and institutional records, recordings with permission, and consented accounts",
                  "Name the lineage, text, language, and place; attribute theological claims and distinguish historical evidence from hagiography. Do not generalize one practice across all Vaiṣṇavas.")
    revise_domain("275", "275_shaktism", SHAKTISM,
                  "Distinct Śākta communities, goddess narratives, texts, sites, public observances, access, and custodianship.",
                  "specified Śākta texts and editions, dated inscriptions and object records, site archives, and consented practitioner and custodian accounts",
                  "Attribute sacred claims and local meanings; respect restricted practices and community consent. Do not treat all goddess traditions as one or assume social roles from theology alone.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
