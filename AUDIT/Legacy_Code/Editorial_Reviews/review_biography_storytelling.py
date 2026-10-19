"""Editorial questions for biography storytelling methods."""

from review_angle_plans import audit, revise_domain


BIOGRAPHY = """history_origins|How a Life Story First Took Shape|Which early source established the familiar narrative of one life?|Trace publication, author access, audience, and later copying.
famous_examples|A Biography with Competing Editions|How did revisions change the portrayal of one subject?|Compare editions, newly available sources, cuts, and author notes.
hidden_stories|The People a Biography Leaves Out|Which relationships and support roles disappear in a one-person narrative?|Compare archive, acknowledgments, collaborators, and consented accounts.
beginner_explainers|The Evidence Behind a Life Story|What source types can support a claim about one person's life?|Distinguish records, interviews, memoir, hearsay, and inference.
advanced_concepts|Memory Against the Archive|How can a biographer handle conflicting recollection and records?|Establish dates, provenance, context, and irreducible uncertainty.
mysteries_unsolved_cases|A Gap in a Life's Timeline|What can and cannot be said about one undocumented interval?|List sources, check chronology, and avoid imagined scenes.
technology_innovation|Digital Archives and Biography|How has searchable material changed one biographical finding?|Compare original context, OCR errors, access, and missing collections.
people_personalities|The Biographer's Relationship to the Subject|How did access or distance shape one portrayal?|Review interview terms, funding, correspondence, and author disclosure.
major_events|One Event, Several Life Narratives|How do biographies differ in their treatment of a turning point?|Compare their citations, chronology, framing, and omissions.
how_it_works|From Records to a Scene|How can a documentary build a scene without inventing thoughts?|Show source selection, verified detail, narration, and uncertainty labels.
rise_fall|A Biography's Changing Reputation|Why did a once authoritative life story lose or gain trust?|Trace source access, criticism, corrections, and later scholarship.
then_vs_now|A Person Reintroduced to New Audiences|How does a later biography reflect changed questions?|Compare evidence base, social context, and claims retained or revised.
future_developments|What a New Archive Might Change|Which specific biographical question could new records answer?|Identify collection, access limits, and rival explanations.
myths_vs_facts|A Dramatic Origin Story Tested|Is a familiar early-life episode supported by independent evidence?|Find earliest telling, contemporary records, and variant versions.
documentary_stories|Following One Claim Through Sources|What happens when a film tests a compelling life anecdote?|Show the search, corroboration, contradiction, and honest conclusion.
lived_experience|The Subject's Own Voice|How should a memoir or interview be used in a biography?|Preserve date, audience, editorial context, and possible self-presentation.
institutional_pathway|The Records a Life Leaves Behind|Which institutions created the sources available to a biographer?|Map schools, employers, courts, media, archives, and missing lives.
incentives_norms|Access in Exchange for Control|How do authorized biography terms affect editorial independence?|Read contracts, approval rights, archive access, and disclosure.
access_and_exclusion|Who Gets a Full Biography?|Why are some lives richly documented and others scarcely recorded?|Compare archival power, publishing demand, language, and wealth.
community_variation|A Life in Several Communities|How do family, colleagues, and neighbors describe one person differently?|Use attributed accounts and identify each vantage point.
policy_in_practice|A Life Within Changing Rules|How did one policy shape opportunities in a person's life?|Trace applicable law, practice, exceptions, and personal records.
survey_vs_story|A Singular Life and a Wider Pattern|When is one biography typical or unusual for its cohort?|Use compatible population data without erasing individual experience.
power_and_voice|Control of Letters and Interviews|Who decides what private source material becomes public?|Examine ownership, access restrictions, consent, and public interest.
unintended_consequence|What Publication Changed|Did one biography alter relationships, reputation, or archival access?|Use dated responses and avoid attributing all later change to the book.
comparative_setting|The Same Life in Two Cultures|How do translations or editions change a biography's emphasis?|Compare text, context, marketing, and reception.
change_over_time|A Life Without a Simple Arc|Which changes resist a rise-fall-redemption structure?|Use dated decisions and acknowledge simultaneous roles and contradictions.
ethical_dilemma|A Sensitive Detail in a Life Story|Is publication justified by relevance and evidence?|Weigh source quality, consent, privacy, harm, and explanatory need.
field_source_verification|A Biographical Fact Check|Can each consequential line be traced to a source?|Build a claim ledger with date, provenance, corroboration, and uncertainty.
field_story_framing|Choosing the Opening Scene|Does one vivid opening mislead about the rest of the life?|Test chronology, representative value, omitted context, and evidence.
field_audience_measurement|What Readers Take Away|Does an audience distinguish established facts from interpretation?|Use consented feedback and explicit labels for uncertain scenes.
field_platform_incentive|Biography for a Feed|How do short-form formats reward simplified life arcs?|Compare edits, reach, source links, omitted caveats, and correction paths.
field_editorial_correction|Revising a Life Story Publicly|How should a biography change after a substantive error is found?|Keep original claim, new evidence, transparent correction, and affected voices.
"""


if __name__ == "__main__":
    revise_domain("147", "147_biography_storytelling", BIOGRAPHY,
                  "Biography as a research and storytelling practice through source provenance, memory, archive gaps, narrative framing, privacy, and correction.",
                  "dated primary records, archival provenance and access terms, versioned biographies, recorded interviews with use agreements, claim ledgers, and published corrections",
                  "Name subject, biographer, edition, and period. Label inference, do not invent thoughts or scenes as fact, verify consequential claims, and weigh privacy and consent before using intimate details.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
