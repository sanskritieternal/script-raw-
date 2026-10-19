"""Direct question-design review of Bhagavad Gita and Purāṇic corpora."""
from review_angle_plans import revise_domain, audit

GITA = """history_origins|The Gita in Its Epic Setting|How does the Bhagavad Gita function within the Bhīṣma Parvan of the Mahābhārata?|Read the surrounding narrative and distinguish textual setting from dating claims.
famous_examples|A Famous Verse in Context|What does one widely quoted Gita verse say in its full exchange?|Compare Sanskrit, surrounding verses, and named commentaries.
hidden_stories|A Reader Beyond the Canonical Commentators|Whose interpretation of a Gita passage is missing from a familiar account?|Use dated translations, teaching records, and consented contemporary voices.
beginner_explainers|Arjuna's Question and Krishna's Reply|What problem does one chapter address, and how does the dialogue develop?|Follow the named chapter without reducing the whole text to one instruction.
advanced_concepts|Action, Knowledge, and Devotion|How do named commentators relate two paths described in the Gita?|Compare precise passages and attribute philosophical differences.
mysteries_unsolved_cases|A Disputed Verse Reading|Which textual or translation choice remains contested in one verse?|Check editions, manuscripts, grammar, and commentarial history.
technology_innovation|Digital Comparison of Gita Commentaries|Can aligned texts reveal how readings diverge?|Verify edition provenance, verse numbering, and limits of automated matching.
people_personalities|A Commentator's Gita|What did one named commentator argue about a specific passage?|Read primary commentary and later reception separately.
major_events|A Translation Shapes Reception|How did one dated translation change public use of the Gita?|Trace publication, audience, criticism, and later editions.
how_it_works|Reading a Gita Argument|How does one exchange move from objection to answer?|Map speaker turns, key Sanskrit terms, and rhetorical setting.
rise_fall|A Reading's Changing Influence|Why did one interpretation gain or lose prominence in a named setting?|Compare institutions, editions, teaching, and historical context.
then_vs_now|One Verse Across Centuries|How did a classical commentary and a present community read the same verse?|Attribute both readings and avoid assuming uninterrupted sameness.
future_developments|An Open Translation Question|Which source or study could clarify a disputed Gita rendering?|State needed evidence without predicting doctrinal agreement.
myths_vs_facts|A Single Message of the Gita?|Does a popular slogan fit the dialogue and its diverse commentaries?|Compare bounded passages, not an isolated line.
documentary_stories|A Gita Passage Through Editions|How did one verse move through manuscript, print, and translation?|Track edition choices, numbering, and reception.
text_source|Locating a Gita Claim|Where exactly does one claimed teaching appear in the text?|Cite chapter, verse, edition, speaker, and neighboring passage.
interpretive_lineages|Two Lineages, One Verse|How do two named traditions disagree over a verse?|Present each argument from its own commentary.
lived_practice|The Gita in a Community's Life|How is the text studied or recited in a specific setting?|Use consented participant accounts and identify local variation.
ritual_sequence|The Gita in an Observance|Where does a selected passage enter one documented observance?|Describe local practice with permission; do not prescribe it.
language_translation|A Term with Several Readings|How does translating one Sanskrit word alter a Gita argument?|Compare syntax, context, and major commentarial choices.
regional_variants|Teaching the Gita in Two Regions|How do local languages and institutions shape the text's use?|Compare named communities and dated materials without ranking authenticity.
art_and_devotion|A Gita Scene Reimagined|How does one artwork interpret a moment in the dialogue?|Distinguish the epic scene, artist's choices, and devotional reception.
community_memory|Remembering a Teacher's Gita|How does a community recount one teacher's interpretation?|Pair attributed memory with writings and dated records.
ethics_in_context|A Difficult Ethical Passage|How have named interpreters addressed a moral tension in the Gita?|Read literary context and include disagreement without issuing personal guidance.
source_and_history|Dating a Gita Witness|What can a manuscript or citation establish about textual history?|Distinguish surviving copy date, earlier citation, and composition claims.
encounter_and_exchange|The Gita in Another Debate|How was one passage cited in a later philosophical or political exchange?|Track exact citation and context; avoid endorsing the later use.
contemporary_voice|A Present Reader Explains a Verse|What does one practitioner or scholar find important in a selected passage?|Attribute standpoint and include alternative readings.
field_textual_lineage|One Verse Across Editions|Which variants or numbering differences appear in named Gita editions?|Record manuscript base and editorial notes.
field_regional_practice|A Local Gita Study Group|How is the text taught and discussed in one community?|Use consent and observe the group's own interpretive methods.
field_translation_choice|Two Translations of a Verse|Which Sanskrit choices produce two different English renderings?|Compare original wording, grammar, and notes.
field_ritual_context|A Verse in Local Practice|How is one verse used in a named devotional setting?|Ask practitioners and respect access restrictions.
field_community_interpretation|A Lineage Reads the Dialogue|How does one lineage understand a contested exchange?|Present its source texts and acknowledge internal variation."""

PURANAS = """history_origins|Formation of a Named Purāṇa|What can manuscript and citation evidence show about one Purāṇic text's development?|Distinguish layers, recensions, and much later printed editions.
famous_examples|A Familiar Purāṇic Story|How does one famous narrative differ across named sources?|Compare passages, versions, and local retellings with attribution.
hidden_stories|Local Custodians of a Purāṇic Narrative|Whose telling or performance is absent from a standard textual account?|Use consented community accounts and dated records.
beginner_explainers|What Is a Purāṇa?|How does one named Purāṇa combine narrative, genealogy, place, and practice?|Show its particular structure without imposing one template on all texts.
advanced_concepts|Textual Layers and Recensions|How can researchers identify changes within a named Purāṇa?|Compare manuscripts, citations, language, and regional editions.
mysteries_unsolved_cases|A Passage of Uncertain Origin|Why do witnesses disagree over one Purāṇic section?|Assess provenance, incorporation, and editorial uncertainty.
technology_innovation|Digitizing Purāṇic Witnesses|Can a searchable corpus clarify where one story appears?|Check transcription, manuscript base, omissions, and search limits.
people_personalities|A Purāṇic Figure Across Versions|How is one figure portrayed differently in two named texts?|Compare narrative function and later devotional reception.
major_events|A Text Enters a Regional Tradition|What documented change made one Purāṇa important in a place?|Use dated manuscripts, patronage, performance, and local voices.
how_it_works|Following a Purāṇic Narrative|How is one story framed, told, and interpreted within its source?|Identify narrator, audience, surrounding chapters, and edition.
rise_fall|A Text's Changing Circulation|Why did one recension become more visible than another?|Compare copying, printing, translation, and institutional use.
then_vs_now|One Story in Text and Living Practice|How does a community tell a Purāṇic story today?|Distinguish textual passage from local adaptation and meaning.
future_developments|A Manuscript Research Question|Which missing witness could clarify a contested Purāṇic passage?|Specify needed source evidence without predicting discovery.
myths_vs_facts|Narrative and Historical Evidence|How should a Purāṇic account be presented beside independent historical records?|Attribute devotional narrative and date external evidence.
documentary_stories|A Story's Version History|How did one Purāṇic episode travel through copies, translations, and performances?|Trace named witnesses, editions, and community adaptations.
text_source|Finding a Purāṇic Passage|Which text, recension, chapter, and edition contain a claimed story?|Check source numbering and variant locations.
interpretive_lineages|Different Readings of One Story|How do two named lineages interpret the same narrative?|Represent each reading in its textual and practice context.
lived_practice|A Purāṇa in Community Life|How is one text read, heard, or performed in a named community?|Use consented accounts and identify when and where.
ritual_sequence|A Story in an Observance|What role does one Purāṇic passage have in a documented local rite?|Separate textual prescription from observed practice.
language_translation|A Purāṇic Term in Context|How do translation choices shift the meaning of one narrative detail?|Compare Sanskrit or regional original, grammar, and parallel versions.
regional_variants|One Narrative in Two Regions|How do versions of one story differ across documented settings?|Compare sources of similar genre and date before inferring change.
art_and_devotion|Purāṇic Story in Art|How does one image interpret a named narrative?|Identify textual source, patron, visual choices, and devotional reception.
community_memory|Remembering a Local Sacred Story|How does a community connect a Purāṇic narrative to a place?|Attribute local memory and distinguish dated site history.
ethics_in_context|A Purāṇic Social Rule Revisited|How have communities interpreted or challenged one difficult passage?|Read source context and center affected contemporary voices.
source_and_history|The Provenance of a Purāṇa Edition|What manuscript base supports a commonly used printed text?|Examine editorial preface, witnesses, and known gaps.
encounter_and_exchange|A Story Shared Across Traditions|What documentary evidence links similar narratives in two traditions?|Trace chronology and direct borrowing claims carefully.
contemporary_voice|A Performer Interprets a Story|What does one present storyteller emphasize and why?|Use consented testimony and avoid making one account universal.
field_textual_lineage|A Chapter Across Manuscripts|Which differences appear in named witnesses of one Purāṇa?|Record provenance, dating, and edition decisions.
field_regional_practice|A Local Purāṇic Performance|How is one story performed in a specific region?|Document language, audience, permissions, and community meaning.
field_translation_choice|Two Versions of a Key Line|Which wording and translation choices change one story's interpretation?|Compare source passages and manuscript base.
field_ritual_context|Purāṇic Text in a Rite|How does a community use one passage in a named observance?|Respect restricted practice and distinguish local rule from broad claim.
field_community_interpretation|A Community's Version of a Story|How do local practitioners explain differences from a printed text?|Attribute their reasons and avoid ranking versions as authentic or false."""

if __name__ == "__main__":
    revise_domain("271", "271_bhagavad_gita", GITA,
                  "The Bhagavad Gita as a named Mahābhārata dialogue, its textual history, translations, commentaries, and living use.",
                  "specified Sanskrit editions and manuscript witnesses, named commentaries and translations, publication records, and consented community accounts",
                  "Cite chapter, verse, speaker, and edition; attribute philosophical readings to interpreters. Distinguish epic setting, textual history, devotional commitment, and later political uses.")
    revise_domain("272", "272_puranas", PURANAS,
                  "Named Purāṇic texts and recensions, narrative variation, manuscript history, regional performance, and community interpretation.",
                  "specified manuscript witnesses and editions, citations, translations, performance records, art and site archives, and consented practitioner accounts",
                  "Name the Purāṇa, recension, passage, and edition; attribute local stories and devotional beliefs. Distinguish narrative claims from independently dated history and avoid treating all Purāṇas as one fixed text.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
