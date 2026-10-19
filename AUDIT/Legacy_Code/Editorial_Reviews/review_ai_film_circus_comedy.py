"""Editorial question designs for AI film and performance histories."""

from review_angle_plans import audit, revise_domain


FILM = """history_origins|AI Tools Enter Film Production|Which earlier automation led to current generative workflows?|Trace dated films and tools.
famous_examples|One AI-Assisted Sequence|What did people and software each contribute?|Use credits and production evidence.
hidden_stories|Labor behind Generated Shots|Which artists, data workers, editors, and performers are obscured?|Follow one asset.
beginner_explainers|Where AI Fits a Film Pipeline|How do script, previsualization, image, voice, and edit uses differ?|Name stage and tool.
advanced_concepts|Controlling Continuity|How do filmmakers maintain character, light, and action across shots?|Compare iterations and fixes.
mysteries_unsolved_cases|A Claimed Fully AI Film|Which human choices and source materials are unreported?|Audit credits and process.
technology_innovation|A New Generation Tool|Did it improve a measured production task?|Compare same brief and review burden.
people_personalities|A Filmmaker's Creative Choice|Why did one director accept or reject AI output?|Use attributed interview.
major_events|A Film-Labor Agreement|How did a dated rule change consent or credit?|Read actual agreement.
how_it_works|From Prompt to Final Shot|How do generation, selection, revision, sound, and delivery connect?|Record version trail.
rise_fall|A Tool Removed from a Production|Was quality, rights, cost, or trust decisive?|Use project record.
then_vs_now|Traditional VFX and Generative Work|Which tasks and controls changed?|Compare matching shot type.
future_developments|Future AI Film Workflow|Which consistency, licensing, and labor conditions remain?|Conditional outlook.
myths_vs_facts|Prompt Alone Makes a Film?|Which human direction and finishing work are involved?|Use a documented case.
documentary_stories|One Film's AI Decision Trail|How did brief, test, approval, and release unfold?|Use dated production sources.
creative_brief|A Bounded AI Film Experiment|What artistic purpose justifies this tool for a specific scene?|State deliverable.
materials_and_tools|Input and Model Provenance|What footage, likeness, audio, and tool terms shaped output?|Keep permission record.
process_breakdown|Production Step by Step|Where do storyboard, generation, edit, grading, and review happen?|Map labor.
composition_choice|Frame Design after Generation|Who selects staging, movement, and visual emphasis?|Compare alternatives.
collaborative_authorship|Credit the Whole Team|How are writers, performers, artists, and tool operators represented?|Check credits and contracts.
adaptation_across_media|Script to Generated Sequence|Which dramatic beats survive translation to image and sound?|Review scene function.
audience_reception|Viewer Response to AI Disclosure|Does labeling alter interpretation of the work?|Use audience evidence.
cultural_context|Style and Borrowed Traditions|Which visual references require context or permission?|Examine sources.
preservation_restoration|Archiving AI Film Assets|Can a project reproduce and preserve versions and licenses?|Check files and metadata.
rights_and_attribution|Likeness, Copyright, Consent|Which permissions apply to each input and output?|Name jurisdiction and contract.
style_comparison|Two Approaches to a Shot|What expressive differences arise with and without generation?|Hold brief fixed.
creative_failure|An Output That Missed the Story|What did the failure reveal about control or bias?|Show revision process.
field_shot_design|Designing an AI-Assisted Shot|Can camera logic and continuity be documented?|Use shot plan.
field_production_workflow|Human Review at Each Stage|Who can approve, reject, or revise material?|Map authority.
field_sound_choices|Voice and Sound Consent|What source, performance, and mix decisions are made?|Check performer terms.
field_editing_rhythm|Pace of Generated Footage|How does shot duration affect narrative clarity?|Compare cuts.
field_distribution_format|Release and Disclosure|What provenance and technical information reaches platforms?|Check delivery requirements.
"""

CIRCUS = """history_origins|Which Circus Tradition?|How did a named troupe and place shape a performance form?|Avoid single-origin story.
famous_examples|A Circus Poster and Its Act|What does advertisement claim and what can corroborate it?|Compare programs and press.
hidden_stories|Workers beyond the Ring|Who built, transported, cooked, and maintained a touring show?|Use payroll and oral history.
beginner_explainers|A Circus as Performance and Business|How do acts, route, venue, crew, and audience connect?|Map one season.
advanced_concepts|Publicity versus Performance|How can posters exaggerate scale or novelty?|Compare surviving records.
mysteries_unsolved_cases|An Unattributed Performer|Which cast list, image, or contract could identify them?|State uncertainty.
technology_innovation|A Change in Stage or Transport|How did a material or route technology alter the show?|Use dated logistics evidence.
people_personalities|A Performer's Career|What do contracts and accounts show about skill and risk?|Use named sources.
major_events|A Troupe's Turning Point|How did regulation, accident, or economic change affect it?|Trace contemporary reports.
how_it_works|A Touring Circus Day|What sequence moves equipment, people, animals, and audience?|Use operational records.
rise_fall|A Circus Closes or Changes|Which costs, norms, and audience patterns mattered?|Avoid one-cause tale.
then_vs_now|Circus Forms across Time|How did acrobatics, animal acts, and labor practice vary?|Specify place and period.
future_developments|What Can New Archives Reveal?|Which uncatalogued records might revise a claim?|Name collection.
myths_vs_facts|A Famous Circus Legend|Which parts appear in contemporary documents?|Separate promotion and evidence.
documentary_stories|A Troupe on the Road|How did route, performance, labor, and reception unfold?|Build dated itinerary.
creative_brief|A Historical Circus Segment|Whose story and sources set the focus?|Avoid spectacle without context.
materials_and_tools|The Material Show|What can posters, costumes, rigs, and tickets establish?|Record provenance.
process_breakdown|Making a Historical Act|Which rehearsal, safety, music, and crew work supported it?|Use period evidence.
composition_choice|A Poster Frames the Audience|How did design direct attention to selected performers?|Compare artifact and billing.
collaborative_authorship|Credit a Circus Act|Who created, trained, and performed it?|Check contracts and programs.
adaptation_across_media|From Live Act to Film|What movement and audience interaction changed?|Use a documented adaptation.
audience_reception|Who Attended the Circus?|What do sales, reviews, and venue records reveal?|Account for source bias.
cultural_context|Display and Exploitation|How were people or animals represented and treated?|Use contemporary and affected voices.
preservation_restoration|A Fragile Circus Poster|What conservation decisions affect color and context?|Use archive notes.
rights_and_attribution|Using Historic Circus Images|Which rights and creator credits are known?|Check item record.
style_comparison|Two Circus Companies|How did repertoire and labor organization differ?|Match region and era.
creative_failure|An Act That Failed|What evidence shows risk or audience response?|Avoid inventing backstage motive.
field_textual_form|Program and Promotional Copy|How do wording and omissions shape history?|Compare editions.
field_performance_choice|Reconstructing an Act|Which moves are evidenced and which are interpretation?|Label reenactment.
field_audience_history|Audience across Venues|How did ticket price and location alter access?|Use venue data.
field_translation_or_adaptation|Touring across Languages|What changed in billing and staging for new audiences?|Compare programs.
field_critical_reception|Reviews of a Circus Season|Whose judgments were published and whose were not?|Contextualize press.
"""

COMEDY = """history_origins|Origins of a Stand-Up Form|Which club, vaudeville, or monologue tradition shaped a local scene?|Avoid universal origin.
famous_examples|A Recorded Comedy Performance|What can audio establish about timing and audience?|Use dated recording.
hidden_stories|Writers and Venues behind a Comic|Who shaped material, bookings, and production?|Use credits and contracts.
beginner_explainers|Stand-Up versus Related Forms|How do monologue, vaudeville, sketch, and improvisation differ?|Use period examples.
advanced_concepts|Joke Ownership and Revision|How can a bit change across sets and recordings?|Compare versions and attribution.
mysteries_unsolved_cases|A Disputed First Recording|Which definitions and archival gaps affect the claim?|State scope.
technology_innovation|Microphone, Record, Broadcast|How did a medium change delivery and reach?|Use contemporary recordings.
people_personalities|A Comic's Changing Act|What do dated sets reveal about voice and constraints?|Avoid unsupported psychology.
major_events|A Venue or Media Shift|How did television, albums, or streaming alter a scene?|Use booking and release evidence.
how_it_works|From Open Mic to Recorded Set|How do writing, testing, revision, performance, and edit connect?|Use attributed process.
rise_fall|A Comedy Venue's Closure|Which finances, audiences, or policy changes mattered?|Use records.
then_vs_now|A Joke in Two Periods|How did social context and audience interpretation change?|Present dated context.
future_developments|What Remains Unarchived?|Which ephemeral local scenes need oral history?|Describe collection limits.
myths_vs_facts|A Comic Invented a Style?|What earlier acts complicate a sole-inventor claim?|Compare primary records.
documentary_stories|One Set's Journey|How did a routine move from stage to recording and later reception?|Track versions.
creative_brief|A Comedy History Episode|Which place, performers, and records define scope?|Avoid greatest-ever ranking.
materials_and_tools|Scripts, Audio, and Flyers|What does each artifact preserve or omit?|Check provenance.
process_breakdown|How a Set Was Built|Which drafting, rehearsal, and performance evidence survives?|Avoid guessing.
composition_choice|Timing in a Recorded Bit|How do pause, emphasis, and audience sound create meaning?|Use short fair excerpt.
collaborative_authorship|Shared Comedy Work|Who wrote, performed, booked, and edited a set?|Credit documented roles.
adaptation_across_media|Stage to Album or Screen|Which jokes or audience reactions changed in edit?|Compare versions.
audience_reception|Who Laughed and Why?|What do reviews and recordings show without assuming unanimity?|Note audience limits.
cultural_context|Humor and Social Power|How did race, gender, class, or censorship shape a joke?|Use historical context.
preservation_restoration|Keeping Historic Comedy Audio|What transfers and metadata preserve performance context?|Use archive practice.
rights_and_attribution|A Comic's Material|Who owns a recording and who is credited for writing?|Check contract and law.
style_comparison|Two Comics in One Era|How do topic, rhythm, venue, and audience differ?|Avoid simple progress narrative.
creative_failure|A Joke That Landed Differently|What evidence shows changed reception?|Compare dated performances.
field_textual_form|Setup, Turn, and Callback|How does structure appear in a specific recorded set?|Analyze without long quotation.
field_performance_choice|Delivery Changes Meaning|How do pace and persona alter the same line?|Use paired versions.
field_audience_history|Club and Broadcast Audiences|Who had access and what feedback was audible?|Use venue and broadcast records.
field_translation_or_adaptation|Comedy across Languages|Which references resist translation and how were they adapted?|Compare credited versions.
field_critical_reception|Review and Retrospect|How did contemporary critics and later historians differ?|Read both in context.
"""

if __name__ == "__main__":
    revise_domain("342", "342_ai_filmmaking", FILM,
                  "AI filmmaking through documented production decisions, human authorship, performer consent, rights, quality control, and preservation.",
                  "production records and credits, US Copyright Office AI copyrightability report, applicable performer agreements, release documentation, and audience research",
                  "Name production, tool, stage, jurisdiction, and agreement. A prompt or generated shot is not an entire film, and rights depend on facts and law.")
    revise_domain("385", "385_circus_history", CIRCUS,
                  "Circus history through specific troupes, routes, performers, backstage labor, promotional artifacts, audiences, and changing norms.",
                  "Library of Congress circus poster collection, programs, contracts, contemporary press, oral histories, and conservation records",
                  "Name troupe, place, and era. Posters are advertisements, not neutral proof of an act; handle exploitation and animal use with context.")
    revise_domain("392", "392_stand-up_comedy_history", COMEDY,
                  "Stand-up and comedy history through dated performances, evolving routines, venues, media formats, collaborative labor, and social context.",
                  "Library of Congress variety-stage recordings and comedy collections, set lists, credited releases, venue records, and contemporary reviews",
                  "Name performer, scene, medium, and date. Do not declare a universal first from a partial archive or reproduce lengthy protected routines.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
