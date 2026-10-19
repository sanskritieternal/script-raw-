"""Apply the second hand-edited question-design batch; preserve every angle slug."""
import argparse
import json
from pathlib import Path

from review_angle_plans import HOMES, audit

# Stable slug | title | question | bounded editorial direction.
BANKING = """history_origins|How a Banking Institution Began|Which need and rule shaped the founding of one bank?|Use charter, founders' records, and the original operating context.
famous_examples|A Bank That Shaped the Debate|What does a widely cited bank actually reveal about banking design?|Compare its documented practices with claims made about it.
hidden_stories|The Workers Behind a Bank|Whose labor or exclusion is missing from a bank's official history?|Trace one role or affected group through records and accounts.
beginner_explainers|What a Bank Does With a Deposit|What happens after a customer deposits money at a bank?|Explain a dated jurisdiction's accounts, lending, liquidity, and protections.
advanced_concepts|Liquidity and Solvency|How can a bank face a cash shortage while its assets exceed liabilities?|Use a simplified balance sheet and distinguish timing from asset quality.
mysteries_unsolved_cases|Why a Bank Failed|Which causes of one bank failure remain disputed after investigation?|Compare official findings with alternative explanations and evidence gaps.
technology_innovation|When Banking Went Digital|Which task changed when one bank introduced a digital channel?|Compare access, cost, reliability, fraud exposure, and exclusions.
people_personalities|The Decision That Changed a Bank|Which documented leadership decision altered a bank's risk or service?|Trace authority, incentives, contemporaneous records, and outcomes.
major_events|A Banking Rule After Crisis|What did one dated banking reform change in practice?|Compare enacted rule, compliance evidence, and intended result.
how_it_works|A Payment From Start to Finish|How does a customer payment travel through one banking system?|Map participants, settlement, delays, fees, and failure points.
rise_fall|Growth and Failure of One Bank|Which balance-sheet changes preceded one bank's expansion or failure?|Use comparable dated disclosures and avoid hindsight certainty.
then_vs_now|Banking Across Two Periods|How did access to a common banking service change over time?|Hold jurisdiction and customer group steady for comparison.
future_developments|A Conditional Banking Scenario|Which rule or technology could change banking access or risk?|State assumptions and current constraints; do not forecast as fact.
myths_vs_facts|Testing a Banking Claim|Does a popular claim about bank deposits match the relevant rules?|Check dated legal terms and regulator explanations for one jurisdiction.
documentary_stories|One Customer, One Banking Process|What do records show about a customer's route through a bank process?|Use a consented or anonymized case and distinguish general rules.
product_terms|Reading an Account Agreement|Which clause changes an account's cost or access?|Compare account terms, fee schedule, and effective dates.
household_cash_flow|When a Payment Arrives Late|How does settlement timing affect a household's available funds?|Use an illustrative cash-flow timeline and disclosed bank rules.
risk_and_time|A Bank's Maturity Mismatch|How do short-term liabilities and long-term assets create risk?|Use a simplified balance sheet with a dated institutional case.
fee_effect|The Total Cost of an Account|How do recurring account and transaction fees add up?|Show transparent examples based on a dated fee schedule.
consumer_protection|What Deposit Protection Covers|Which deposits are protected under one jurisdiction's rules?|Specify institution type, limits, ownership, and exclusions.
market_vs_household|Rates and the Account Holder|Why can a rate change affect savers and borrowers differently?|Compare two labeled household examples with contract terms.
historical_policy|A Banking Policy in Practice|Who gained access after a dated banking policy change?|Compare official aims, implementation data, and affected groups.
inflation_effect|Savings Rate and Purchasing Power|When can an account balance grow while its buying power falls?|Use dated nominal rates and a labeled inflation scenario.
fraud_warning|Verifying a Banking Message|Which details of a suspicious bank message can be checked safely?|Use official consumer alerts without repeating attack instructions.
comparison_method|Two Accounts on Equal Terms|How do two accounts compare for the same pattern of use?|Include fees, access, rate terms, protection, and dates.
access_gap|Who Cannot Open an Account?|Which identification, cost, or location rule limits bank access?|Use eligibility rules and evidence from a defined community.
uncertainty_range|More Than One Rate Path|Which assumption changes a banking cost illustration most?|Vary rates and fees transparently without personal advice.
field_fee_structure|Where Bank Fees Appear|Which fees are visible upfront and which depend on behavior?|Read a dated account disclosure and model distinct customer patterns.
field_risk_disclosure|What a Bank Discloses About Risk|Which risk can a public bank disclosure reveal or conceal?|Compare stated risk metrics with a defined subsequent outcome.
field_regulatory_protection|Bank Supervision and Its Limits|What did a regulator require before one documented bank problem?|Trace the rule, supervisory record, and legal limits.
field_household_effect|Banking Access in Daily Life|How does losing a banking service affect a defined household?|Use consented accounts alongside service and cost data.
field_market_cycle|Credit Across a Cycle|How did a bank's lending change during one dated economic cycle?|Compare consistent lending measures and relevant policy shifts."""

HEALTH_SYSTEMS = """history_origins|How a Care System Took Shape|Which policy or institution established a present care pathway?|Use dated legislation, budgets, and service records.
famous_examples|A Health System Often Held Up as a Model|What does one celebrated system do well, and for whom?|Use comparable measures and specify population and period.
hidden_stories|The Workforce Behind Care|Which workers are absent from a system's public account?|Use staffing records and attributed worker accounts.
beginner_explainers|Following a Patient Through the System|What happens between first contact and follow-up for one service?|Map referral, payment, records, and handoffs in one jurisdiction.
advanced_concepts|Why More Spending May Not Mean More Access|Where does additional health funding fail to reach patients?|Trace a bounded budget through workforce and service capacity.
mysteries_unsolved_cases|An Unexplained Care Gap|Which causes of a measured service gap remain uncertain?|Compare geography, need, referral, and data quality.
technology_innovation|A Health Record System in Practice|Did one digital record change continuity of care?|Compare measured workflow and safety outcomes before and after.
people_personalities|Who Decided the Service Design?|Whose decisions set the location or eligibility of a care service?|Use policy records, consultation, and affected community accounts.
major_events|A Shock to a Care System|Which services changed during one documented disruption?|Use dated utilization and capacity data; distinguish short and long effects.
how_it_works|From Funding to Appointment|How does funding become an available appointment?|Trace allocation, staffing, scheduling, and unmet demand.
rise_fall|An Expansion Followed by Strain|Why did one health service's capacity rise and then stall?|Compare workforce, funding, demand, and governance over time.
then_vs_now|Two Periods of Care Access|How did waiting time or coverage change for a defined group?|Use the same service and measurement method in both periods.
future_developments|A Conditional Service Plan|Which constraint would determine whether a proposed care expansion works?|State workforce, financing, facility, and demand assumptions.
myths_vs_facts|Testing a Health System Ranking|What does a popular system ranking measure and omit?|Inspect indicator definitions, weighting, years, and missing data.
documentary_stories|One Referral Through the System|Where did documented handoffs help or delay one patient?|Use a consented or anonymized account with system records.
claim_evidence|A System Performance Claim Checked|Does a claim about quality match the outcome being measured?|Compare claim, denominator, comparator, and time window.
care_pathway|Where the Referral Slows|At which step in a defined pathway do delays accumulate?|Map timestamps, eligibility, capacity, and lost follow-up.
benefit_harm|A Service Redesign's Tradeoffs|Who benefited and who faced new barriers after a redesign?|Compare access and outcomes across defined groups.
mechanism_vs_outcome|A Plausible Reform, a Measured Result|Did a policy's intended mechanism improve patient outcomes?|Separate implementation evidence from outcome evidence.
population_difference|Whose Outcomes Are Missing?|Which patient group is absent from a service evaluation?|Inspect eligibility, data coverage, and subgroup results.
quality_of_guidance|From Guideline to Clinic|Where does a clinical guideline change during implementation?|Compare the published recommendation with local pathway records.
access_to_care|The Cost of Reaching Care|Which travel, fee, language, or scheduling barrier prevents access?|Use service maps and local data for a defined population.
patient_experience|A Patient's Handoff|What can one patient describe about continuity across providers?|Use consented testimony and distinguish individual from system-wide evidence.
misinformation_path|A Claim About System Performance|How did a misleading performance statistic enter public debate?|Trace its denominator, original source, and later corrections.
prevention_boundary|Prevention and Service Capacity|Can a preventive program reach the population it targets?|Compare eligibility, staffing, take-up, and measured outcomes.
system_pressure|Care Under Capacity Pressure|How did demand and staffing interact in one bounded period?|Use dated workforce, utilization, and waiting-time series.
historical_revision|A Reform That Changed Course|Why was a health system reform revised after implementation?|Compare policy aims with evaluation findings and stakeholder accounts.
field_clinical_evidence|Evidence Used for System Decisions|Which clinical result can guide service design, and which cannot?|Check generalizability, local population, and resource assumptions.
field_care_quality|Quality Beyond Throughput|Does a high activity count correspond to better patient outcomes?|Compare volume, safety, experience, and follow-up measures.
field_patient_safety|A System-Level Safety Failure|Which handoff or process failed in a published safety investigation?|Trace contributing conditions and documented corrective actions.
field_health_equity|A Gap in Care Delivery|How do service outcomes differ for two defined groups?|Use comparable denominators and examine access barriers.
field_service_capacity|The Bottleneck in a Care Network|Which resource limits completion of a defined care pathway?|Compare staffing, beds, supplies, and referral data."""

WORLD_RELIGIONS = """history_origins|Tracing a Tradition's Early Sources|What do the earliest surviving sources show about one tradition's development?|Date the sources and distinguish later retellings.
famous_examples|A Familiar Religious Site in Context|How did one widely cited site serve different communities over time?|Compare local records, material evidence, and attributed practice.
hidden_stories|Voices Outside the Canonical Account|Whose practice is missing from a standard account of a tradition?|Use regional or community sources with clear attribution.
beginner_explainers|Studying a Tradition Without Flattening It|How can one practice vary within a named religious tradition?|Compare two located communities and avoid a universal rule.
advanced_concepts|Belief, Text, and Practice|Why can a text's teaching and a community's practice differ?|Study a named text and community in a bounded period.
mysteries_unsolved_cases|A Historical Question With Sparse Evidence|What can and cannot be established about one religious past?|Separate tradition, material record, and scholarly inference.
technology_innovation|Media That Carried a Tradition|How did one writing, printing, or broadcast medium alter access?|Trace a specific text or teaching across a dated medium change.
people_personalities|An Interpreter in Context|How did one named interpreter influence a community's practice?|Use attributed works and contemporary responses, not a hero narrative.
major_events|A Religious Turning Point Revisited|Did one event change practice across all communities equally?|Compare records from multiple locations before and after.
how_it_works|A Practice in Its Community|What happens in one ritual or practice and how do participants explain it?|Use local participants and identified sources; avoid prescriptive instructions.
rise_fall|Change in an Institution|Why did one religious institution gain or lose influence?|Trace membership, patronage, law, and community response.
then_vs_now|One Practice Across Generations|What changed and persisted in a named practice over time?|Compare dated accounts from the same community or region.
future_developments|A Present-Day Community Question|Which current choices might change a religious institution's future?|Attribute proposals and conditions without forecasting belief.
myths_vs_facts|A Historical Claim About a Tradition|Which parts of a popular historical claim are supportable?|Compare source traditions with independent historical evidence.
documentary_stories|One Community's Documented Story|What does one community archive reveal about religious life?|Build a dated account with the community's own terminology.
text_source|A Teaching in Its Textual Setting|How does a passage read in the surrounding text and tradition?|Identify edition, language, translation, and interpreter.
interpretive_lineages|Two Interpretations, One Passage|Why do two named lineages interpret a passage differently?|Compare commentaries and their contexts without declaring one universal.
lived_practice|Practice Beyond the Textbook|How does a local community actually carry out a named practice?|Use attributed interviews and observation with consent.
ritual_sequence|A Step in Context|What meaning do participants give to one step of a ritual?|Study one community's sequence and its own explanations.
language_translation|A Term Across Languages|What changes when a religious term is translated?|Compare original usage, two translations, and commentary.
regional_variants|One Practice in Two Regions|How and why does a practice differ between two regions?|Compare dated local sources without treating either as default.
art_and_devotion|An Image in Devotional Life|How is one work used or interpreted by a community?|Use visual evidence, maker records, and practitioner accounts.
community_memory|Remembering a Shared Past|How does a community commemorate one event?|Separate documented event from later memory and meaning.
ethics_in_context|An Ethical Debate Within a Tradition|How do named interpreters disagree about one ethical question?|Give each view its textual and social context.
source_and_history|Tradition and Historical Method|What does a source claim, and what can independent evidence test?|Identify genre, date, transmission, and limits of verification.
encounter_and_exchange|A Documented Encounter|What changed when two religious communities interacted in one place?|Use sources from both sides and specify period.
contemporary_voice|A Present-Day Practitioner Speaks|How does one practitioner describe their practice and its variation?|Use consented testimony without claiming to represent all members.
field_source_tradition|How a Text Was Transmitted|Which choices shaped the version of a religious text used today?|Compare manuscripts, editions, and translation decisions.
field_lived_practice|Institution and Household Practice|How does an institution's formal teaching relate to household practice?|Compare a named institution and consenting household in context.
field_regional_variation|Movement Between Regions|How did migration change one practice across two locations?|Trace a specific community and date the change.
field_translation_issue|A Translation Dispute|What evidence supports competing translations of one term?|Compare linguistic context and attributed scholarly readings.
field_intercommunity_contact|Shared Space, Different Meanings|How do two communities understand one shared place or event?|Use both communities' accounts and relevant historical records."""

SPECS = {
    "293": ("293_banking", BANKING,
            "Banking institutions, accounts, payments, protection, access, and financial stability in named jurisdictions.",
            "dated account agreements, bank disclosures, regulator records, legislation, and attributed customer accounts",
            "Specify jurisdiction, date, institution type, and protection limits; avoid individualized financial advice."),
    "180": ("180_healthcare_systems", HEALTH_SYSTEMS,
            "The financing, workforce, governance, information, access, and quality of defined healthcare systems.",
            "dated health system indicators, budgets, policy records, service data, investigations, and consented accounts",
            "Define population and jurisdiction; distinguish system measures from individual medical guidance."),
    "076": ("076_world_religions_civilization", WORLD_RELIGIONS,
            "Religious traditions as internally diverse, historically changing, and embedded in communities and cultures.",
            "identified texts and translations, material and historical records, attributed scholarship, and consented community accounts",
            "Attribute beliefs and interpretations; distinguish devotional truth claims from independently testable history."),
}


def apply_revision(niche_id):
    home, spec, purpose, evidence, boundary = SPECS[niche_id]
    path = HOMES / home / "ANGLE_PLAN.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    edits = {}
    for line in spec.splitlines():
        slug, title, question, scope = line.split("|", 3)
        edits[slug] = title, question, scope
    if data["niche_id"] != niche_id or {a["slug"] for a in data["angles"]} != set(edits):
        raise ValueError(f"Stable slugs differ: {path}")
    for entry in data["angles"]:
        title, question, scope = edits[entry["slug"]]
        entry.update(angle=title, question=question, scope=scope, evidence=evidence, boundary=boundary)
    data.update(status="editorial_question_reviewed", purpose=purpose,
                review_note="All 32 question designs and scopes reviewed for niche fit. Sources and claims require episode-level verification.",
                editorial_principles=[
                    "Choose a bounded case with a named community, institution, population, or jurisdiction.",
                    "Date and attribute evidence; represent uncertainty and variation.",
                    boundary,
                ])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.apply:
        for niche_id in SPECS:
            apply_revision(niche_id)
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
