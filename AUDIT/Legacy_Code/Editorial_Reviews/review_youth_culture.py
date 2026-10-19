"""Editorial questions for youth culture."""

from review_angle_plans import audit, revise_domain


YOUTH = """history_origins|A Youth Scene's Local Beginning|Which young people created one named scene and where?|Trace dated venues, media, objects, and participant accounts.
famous_examples|A Widely Copied Youth Trend|What did one trend mean to its first participants?|Compare original context, later branding, and varied voices.
hidden_stories|Work Behind a Youth Event|Who organized, financed, designed, moderated, and cleaned up?|Follow consented youth and adult roles without erasing either.
beginner_explainers|What Counts as Youth Culture?|Which age group, place, and practice does one label describe?|Use self-description and avoid treating all young people alike.
advanced_concepts|From Subculture to Market|How does commercial adoption alter one youth-created practice?|Trace ownership, income, access, authenticity debates, and change.
mysteries_unsolved_cases|Who Invented a Trend?|Which origin claims can be supported by dated evidence?|Compare early posts, performances, archives, and parallel development.
technology_innovation|A Platform Shapes a Scene|How do ranking and sharing tools change one youth practice?|Check exposure, moderation, monetization, privacy, and offline activity.
people_personalities|A Young Creator in Context|How does one person's contribution relate to peers and mentors?|Use consented interview, dated work, credits, and collaborations.
major_events|A Ban or Closure Changes a Scene|How did one policy or venue loss alter participation?|Compare before and after activity, alternatives, and affected groups.
how_it_works|How a Youth Scene Spreads|What routes carry one practice between peers and places?|Trace events, schools, platforms, imitation, and local adaptation.
rise_fall|A Scene's Changing Popularity|Did one practice decline, migrate, or change form?|Compare participation, venue, platform, and naming over time.
then_vs_now|Youth Expression Across Generations|How do two youth scenes differ beyond surface style?|Compare access, costs, media, surveillance, and social conditions.
future_developments|A Youth-Led Space Proposal|Would one project meet young participants' stated needs?|Check governance, safety, funding, access, and youth control.
myths_vs_facts|A Panic About Young People|Does evidence support one claim about a youth trend's harm?|Check original claim, population, outcomes, confounding, and uncertainty.
documentary_stories|One Scene Through Its Participants|What does a season of activity reveal about belonging and work?|Follow voluntary participants and avoid pressure on minors.
lived_experience|Meaning to One Young Participant|Why does a person value one practice?|Use their own terms and avoid generalizing to a generation.
institutional_pathway|Schools and Youth Expression|How does one institution permit, shape, or restrict a practice?|Compare policy, enforcement, resources, and student perspectives.
incentives_norms|Status Within a Scene|Which rewards and informal rules guide participation?|Use varied accounts and avoid exposing private conflicts.
access_and_exclusion|Who Can Join?|Which cost, disability, gender, language, or location barriers matter?|Check venues, equipment, rules, and participant experiences.
community_variation|A Scene Has More Than One Voice|How do members disagree about meaning and direction?|Represent varied voluntary accounts and roles.
policy_in_practice|A Rule Aimed at Youth|Did one policy change actual access or safety?|Compare stated aim, implementation, outcomes, and youth feedback.
survey_vs_story|A Trend and One Viral Clip|Does a popular clip represent a broader youth pattern?|Check sample, platform selection, date, and counterexamples.
power_and_voice|Who Profits from Youth Creativity?|How are rights, money, and credit divided?|Trace contracts, platform terms, sponsors, and creator accounts.
unintended_consequence|Visibility Changes the Scene|Did publicity bring surveillance, crowding, or new opportunity?|Compare before and after conditions and participant preferences.
comparative_setting|One Practice in Two Cities|How did a scene adapt to different local resources?|Compare venues, rules, platforms, transport, and culture.
change_over_time|Growing Out or Carrying Forward?|How do participants' relationships to a practice change with age?|Use longitudinal accounts without an inevitable maturity story.
ethical_dilemma|Filming a Minor in a Youth Scene|Can participation be safe and genuinely voluntary?|Seek age-appropriate assent, guardian consent where required, privacy, and withdrawal.
field_social_norms|Rules Made by Participants|How do young people set and enforce scene norms?|Use permissioned observation and avoid adult-only interpretation.
field_relationship_network|Peer Links Behind a Scene|Which connections support collaboration?|Map minimally with consent and protect minors and third parties.
field_group_identity|A Label People Accept or Reject|Do participants identify with the name given to their scene?|Compare self-names, media labels, and local differences.
field_community_support|A Safe Place to Practice|Which spaces and resources keep participation possible?|Check cost, staff, transport, accessibility, and youth governance.
field_power_difference|Adults Filming Youth|How can production reduce pressure from teachers, parents, or sponsors?|Use independent consent, safeguarding, review, and no penalty for refusal.
"""


if __name__ == "__main__":
    revise_domain("176", "176_youth_culture", YOUTH,
                  "Youth culture through youth-created practices, venues, platforms, markets, identity, access, and participant agency.",
                  "dated artifacts and media, venue and policy records, platform and contract terms, appropriately sampled data, and voluntary age-appropriate participant accounts",
                  "Name practice, age group, place, and period. Avoid generation-wide stereotypes and moral panic; for minors use safeguarding, age-appropriate assent, guardian consent where required, privacy protection, and meaningful refusal.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
