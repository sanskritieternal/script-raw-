# 327 — Privacy: main topic bank

Updated: 2026-10-23 · **14 active BANK proposals · 11 categories · 12 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Data flows](#catalog-327-r01) → [Purpose limitation](#catalog-327-r11).
- **Intermediate:** [Metadata](#catalog-327-r02) → [Consent](#catalog-327-r03) → [Differential privacy](#catalog-327-r05) → [Retention](#catalog-327-r06) → [End-to-end encryption](#catalog-327-r08).
- **Advanced:** [Anonymization](#catalog-327-r04) → [Minimization](#catalog-327-r07) → [Access requests](#catalog-327-r09) → [Personalization](#catalog-327-r10) → [Privacy defaults](#catalog-327-r12).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-327-01) | 1 | 0 | 0 |
| [Identification](#domain-327-02) | 0 | 1 | 0 |
| [Design](#domain-327-03) | 0 | 2 | 1 |
| [Measurement](#domain-327-04) | 0 | 0 | 1 |
| [Statistics](#domain-327-05) | 0 | 2 | 0 |
| [Lifecycle](#domain-327-06) | 0 | 1 | 0 |
| [Communication](#domain-327-07) | 0 | 1 | 0 |
| [Rights](#domain-327-08) | 0 | 0 | 1 |
| [Products](#domain-327-09) | 0 | 0 | 1 |
| [Governance](#domain-327-10) | 1 | 0 | 0 |
| [Interfaces](#domain-327-11) | 0 | 0 | 1 |

<a id="domain-327-01"></a>
## Category: Foundations

<a id="catalog-327-r01"></a>
### Data flows

Subcategory `CATALOG-327-R01` · foundation.

<a id="bank-327-030"></a>
#### BANK-327-030 — Why does deleting an app not necessarily delete the data it collected?

**Individual coverage scope:** Trace device storage, accounts, backups, processors and retention without assuming a named service's practices.


<a id="domain-327-02"></a>
## Category: Identification

<a id="catalog-327-r02"></a>
### Metadata

Subcategory `CATALOG-327-R02` · intermediate.

<a id="bank-327-031"></a>
#### BANK-327-031 — How can metadata reveal information even when message content is encrypted?

**Individual coverage scope:** Compare timing, participants, location inference and aggregation; exclude instructions for tracking individuals.


<a id="domain-327-03"></a>
## Category: Design

<a id="catalog-327-r03"></a>
### Consent

Subcategory `CATALOG-327-R03` · intermediate.

<a id="bank-327-032"></a>
#### BANK-327-032 — Why is a long privacy notice different from meaningful user choice?

**Individual coverage scope:** Compare comprehension, defaults, purpose, alternatives and interface design without legal compliance claims.

<a id="bank-327-042"></a>
#### BANK-327-042 — What did the FTC's 2023 BetterHelp order reveal about privacy promises and advertising data flows?

**Individual coverage scope:** Compare the FTC complaint allegations with its final consent order on sensitive health-data sharing, consent and retention. Treat allegations as allegations and the order as a settlement record; avoid asserting current compliance or giving legal advice.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.

<a id="catalog-327-r07"></a>
### Minimization

Subcategory `CATALOG-327-R07` · advanced.

<a id="bank-327-036"></a>
#### BANK-327-036 — How can a service collect less data while still meeting its actual requirements?

**Individual coverage scope:** Compare required functions, optional personalization, aggregation and on-device processing without promising complete anonymity.


<a id="domain-327-04"></a>
## Category: Measurement

<a id="catalog-327-r04"></a>
### Anonymization

Subcategory `CATALOG-327-R04` · advanced.

<a id="bank-327-033"></a>
#### BANK-327-033 — Why can removing names fail to make a dataset anonymous?

**Individual coverage scope:** Explain linkage, rare combinations, background information and privacy-risk evaluation using invented records.


<a id="domain-327-05"></a>
## Category: Statistics

<a id="catalog-327-r05"></a>
### Differential privacy

Subcategory `CATALOG-327-R05` · intermediate.

<a id="bank-327-034"></a>
#### BANK-327-034 — How does differential privacy limit what an output reveals about one record?

**Individual coverage scope:** Compare neighboring datasets, randomized mechanisms, privacy budgets and utility using invented data rather than reidentification instructions.

<a id="bank-327-043"></a>
#### BANK-327-043 — How did the 2020 Census TopDown algorithm balance disclosure protection and redistricting-data utility?

**Individual coverage scope:** Use the Census Bureau?s 2022 technical account of the 2020 P.L. 94-171 product to examine noisy measurements, policy invariants and privacy-loss accounting, while noting product-specific accuracy and coverage limits.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.


<a id="domain-327-06"></a>
## Category: Lifecycle

<a id="catalog-327-r06"></a>
### Retention

Subcategory `CATALOG-327-R06` · intermediate.

<a id="bank-327-035"></a>
#### BANK-327-035 — Why does a data retention rule need more than a scheduled deletion job?

**Individual coverage scope:** Trace purpose, replicas, backups, logs, exceptions and evidence of implementation.


<a id="domain-327-07"></a>
## Category: Communication

<a id="catalog-327-r08"></a>
### End-to-end encryption

Subcategory `CATALOG-327-R08` · intermediate.

<a id="bank-327-037"></a>
#### BANK-327-037 — What does end-to-end encryption protect when the sender's or receiver's device is still vulnerable?

**Individual coverage scope:** Separate transit, endpoints, metadata, backups and identity verification without tool-specific security guarantees.


<a id="domain-327-08"></a>
## Category: Rights

<a id="catalog-327-r09"></a>
### Access requests

Subcategory `CATALOG-327-R09` · advanced.

<a id="bank-327-038"></a>
#### BANK-327-038 — Why can responding to a personal-data access request be technically complex?

**Individual coverage scope:** Trace identity checks, distributed records, third-party information, retention and applicable legal scope pending research.


<a id="domain-327-09"></a>
## Category: Products

<a id="catalog-327-r10"></a>
### Personalization

Subcategory `CATALOG-327-R10` · advanced.

<a id="bank-327-039"></a>
#### BANK-327-039 — How can a product compare the benefit of personalization against the additional data it needs?

**Individual coverage scope:** Specify purpose, measurable improvement, alternatives, local processing and user choice rather than assuming collection always helps.


<a id="domain-327-10"></a>
## Category: Governance

<a id="catalog-327-r11"></a>
### Purpose limitation

Subcategory `CATALOG-327-R11` · foundation.

<a id="bank-327-040"></a>
#### BANK-327-040 — Why should a service define its purpose for personal data before collecting it?

**Individual coverage scope:** Compare original need, later reuse, compatible purposes and user expectations; reserve actual legal obligations for current jurisdiction-specific research.


<a id="domain-327-11"></a>
## Category: Interfaces

<a id="catalog-327-r12"></a>
### Privacy defaults

Subcategory `CATALOG-327-R12` · advanced.

<a id="bank-327-041"></a>
#### BANK-327-041 — How can a service offer the same privacy choices yet produce different outcomes through its default settings?

**Individual coverage scope:** Compare opt-in paths, friction, repeated prompts, comprehension and reversibility with a hypothetical interface; distinguish a usable choice from legal consent certification.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-327-010"></a>
### pending_topics/0 — The Architecture of Privacy: A Privacy Practice Emerges

**Original question:** Which data practice prompted a documented privacy response?

**Original planning scope:** Use dated records and avoid claiming one universal origin. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. General practice history lacks a named event; purpose, consent and minimization are active.

**Scoped proposals:** [BANK-327-040](#bank-327-040), [BANK-327-032](#bank-327-032).

<a id="bank-327-011"></a>
### pending_topics/1 — Privacy: A Privacy Case Revisited

**Original question:** What harm and remedy are supported by case evidence?

**Original planning scope:** Separate allegations, findings, and individual experience. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. A named FTC order anchors a public privacy case.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

<a id="bank-327-012"></a>
### pending_topics/2 — Privacy: People Behind Data Records

**Original question:** Whose information or labor is overlooked in a privacy debate?

**Original planning scope:** Use consented accounts and avoid exposing identifiers. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Human consequences are addressed via data flow and access-request questions; no individual story is identified.

**Scoped proposals:** [BANK-327-030](#bank-327-030), [BANK-327-038](#bank-327-038).

<a id="bank-327-013"></a>
### pending_topics/3 — Privacy: What Happens to One Data Point

**Original question:** Where does a volunteered detail travel after collection?

**Original planning scope:** Map collection, inference, sharing, retention, and deletion. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Data-flow and retention questions trace a data point.

**Scoped proposals:** [BANK-327-030](#bank-327-030), [BANK-327-035](#bank-327-035).

<a id="bank-327-014"></a>
### pending_topics/4 — Privacy: Beyond Secrecy

**Original question:** Can data processing harm people even without a breach?

**Original planning scope:** Examine inference, context, power, and affected groups. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Metadata and inferred-record risk make privacy broader than secrecy.

**Scoped proposals:** [BANK-327-031](#bank-327-031), [BANK-327-033](#bank-327-033).

<a id="bank-327-015"></a>
### pending_topics/5 — Privacy: An Unclear Data Recipient

**Original question:** What evidence shows who received a dataset?

**Original planning scope:** Inspect disclosures, contracts, technical flow, and gaps. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. FTC BetterHelp case documents alleged recipient and purpose mismatch; do not speculate beyond complaint.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

<a id="bank-327-016"></a>
### pending_topics/6 — Privacy: A Privacy Feature Tested

**Original question:** Does one feature reduce a defined risk in actual use?

**Original planning scope:** Check defaults, usability, data flows, and residual exposure. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. Census TopDown is a named, product-specific privacy method.

**Scoped proposals:** [BANK-327-043](#bank-327-043).

<a id="bank-327-017"></a>
### pending_topics/7 — Privacy: A Data Governance Decision

**Original question:** Who approved one use of personal data and who could object?

**Original planning scope:** Trace authority, affected people, and decision record. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Purpose definition and minimization make the governance decision bounded.

**Scoped proposals:** [BANK-327-040](#bank-327-040), [BANK-327-036](#bank-327-036).

<a id="bank-327-018"></a>
### pending_topics/8 — Privacy: A Data Practice Changes

**Original question:** What changed after a public inquiry or policy decision?

**Original planning scope:** Compare actual processing before and after by date. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. FTC final order is a dated change to a named practice; current behavior unverified.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

<a id="bank-327-019"></a>
### pending_topics/9 — Privacy: Controls in a Service

**Original question:** How do access, retention, and deletion work for one record?

**Original planning scope:** Use a named system and version; test user-visible outcomes. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Consent, retention and access controls cover the generic service architecture.

**Scoped proposals:** [BANK-327-032](#bank-327-032), [BANK-327-035](#bank-327-035), [BANK-327-038](#bank-327-038).

<a id="bank-327-020"></a>
### pending_topics/10 — Privacy: Collection Expands or Contracts

**Original question:** Did a service truly minimize data over time?

**Original planning scope:** Compare fields, inference, partners, and storage periods. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Minimization and purpose limit collection changes without an unspecified trend claim.

**Scoped proposals:** [BANK-327-036](#bank-327-036), [BANK-327-040](#bank-327-040).

<a id="bank-327-021"></a>
### pending_topics/11 — Privacy: A User's Data Journey Across Versions

**Original question:** What collection and control changed?

**Original planning scope:** Compare notices and measured behavior for dated releases. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. No service versions specified; app-data-flow question supplies method.

**Scoped proposals:** [BANK-327-030](#bank-327-030).

<a id="bank-327-022"></a>
### pending_topics/12 — Privacy: A Proposed Privacy Safeguard

**Original question:** What evidence would demonstrate reduced individual risk?

**Original planning scope:** Specify threat, coverage, use, and audit method. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. Census TopDown is a deployed safeguard with documented limits.

**Scoped proposals:** [BANK-327-043](#bank-327-043).

<a id="bank-327-023"></a>
### pending_topics/13 — Privacy: Anonymous by Removing Names?

**Original question:** Can records still be linked to people?

**Original planning scope:** Assess context and reidentification risk without demonstrating targeting. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Existing reidentification question directly covers removing names.

**Scoped proposals:** [BANK-327-033](#bank-327-033).

<a id="bank-327-024"></a>
### pending_topics/14 — Privacy: A Person Seeks Their Data

**Original question:** Can a user see, correct, or delete a record?

**Original planning scope:** Follow consented steps, response time, and limits. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Access-request complexity is already active; no identified person or jurisdiction is supplied.

**Scoped proposals:** [BANK-327-038](#bank-327-038).

<a id="bank-327-025"></a>
### pending_topics/15 — Privacy: Who Controls the Data?

**Original question:** Which controller, processor, vendor, and user can decide processing?

**Original planning scope:** Map one service and dated contracts. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. Purpose limitation and access requests cover control boundaries.

**Scoped proposals:** [BANK-327-040](#bank-327-040), [BANK-327-038](#bank-327-038).

<a id="bank-327-026"></a>
### pending_topics/16 — Privacy: From Consent Screen to Processing

**Original question:** What does an action permit and what flows actually occur?

**Original planning scope:** Compare interface words with technical and contractual evidence. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. BetterHelp complaint and order distinguish notice/consent from downstream processing.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

<a id="bank-327-027"></a>
### pending_topics/17 — Privacy: Useful Data and Individual Risk

**Original question:** What data is necessary for a named task?

**Original planning scope:** Test minimization, alternatives, and affected users. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. Census TopDown gives a named utility/privacy tradeoff for one data product.

**Scoped proposals:** [BANK-327-043](#bank-327-043).

<a id="bank-327-028"></a>
### pending_topics/18 — Privacy: A Privacy Control That Fails

**Original question:** Why did a deletion or opt-out request not take effect?

**Original planning scope:** Use a documented case and avoid exposing private records. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** new_bounded_case. FTC order provides a bounded alleged privacy-promise failure.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

<a id="bank-327-029"></a>
### pending_topics/19 — Privacy: A Privacy Audit's Blind Spots

**Original question:** Which partners, backups, or inferred data were outside the test?

**Original planning scope:** State audit scope and uncertainty. Evidence base: NIST privacy frameworks, dated product disclosures, contracts, data-flow observations, audits, and consented user accounts.

**Editorial disposition:** existing_scope. A generic audit gap is covered by data-flow, retention and control questions; no audit record named.

**Scoped proposals:** [BANK-327-030](#bank-327-030), [BANK-327-035](#bank-327-035).

### trending_topics/0 — Privacy: Record Extremes & Superlatives

**Editorial disposition:** out_of_scope. No metric, denominator or dated comparative dataset supports a privacy superlative.

### trending_topics/1 — Privacy: An Unclear Data Recipient

**Editorial disposition:** new_bounded_case. Same recipient pitch as pending/5; route to BetterHelp.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

### trending_topics/2 — Privacy: A Privacy Feature Tested

**Editorial disposition:** new_bounded_case. Same feature pitch as pending/6; route to Census TopDown.

**Scoped proposals:** [BANK-327-043](#bank-327-043).

### trending_topics/3 — Privacy: Anonymous by Removing Names?

**Editorial disposition:** existing_scope. Same anonymization pitch as pending/13.

**Scoped proposals:** [BANK-327-033](#bank-327-033).

### trending_topics/4 — Privacy: A Data Practice Changes

**Editorial disposition:** new_bounded_case. Same changed-practice pitch as pending/8; route to BetterHelp.

**Scoped proposals:** [BANK-327-042](#bank-327-042).

### trending_topics/5 — Privacy: People Behind Data Records

**Editorial disposition:** existing_scope. Same unspecified people-behind-records pitch as pending/2.

**Scoped proposals:** [BANK-327-030](#bank-327-030).

### trending_topics/6 — Privacy: A Person Seeks Their Data

**Editorial disposition:** existing_scope. Same access-request pitch as pending/14.

**Scoped proposals:** [BANK-327-038](#bank-327-038).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-327-01"></a>
### Data governance

<a id="bank-327-001"></a>
- `BANK-327-001` — Purpose limitation → [BANK-327-040](#bank-327-040)
<a id="bank-327-002"></a>
- `BANK-327-002` — Data minimization → [BANK-327-036](#bank-327-036)
<a id="bank-327-003"></a>
- `BANK-327-003` — Retention schedules → [BANK-327-035](#bank-327-035)

<a id="catalog-327-02"></a>
### Technical measures

<a id="bank-327-004"></a>
- `BANK-327-004` — End-to-end encryption → [BANK-327-037](#bank-327-037)
<a id="bank-327-005"></a>
- `BANK-327-005` — Differential privacy → [BANK-327-034](#bank-327-034)
<a id="bank-327-006"></a>
- `BANK-327-006` — Pseudonymization limits → [BANK-327-033](#bank-327-033)

<a id="catalog-327-03"></a>
### User experience

<a id="bank-327-007"></a>
- `BANK-327-007` — Consent interface clarity → [BANK-327-032](#bank-327-032)
<a id="bank-327-008"></a>
- `BANK-327-008` — Data access requests → [BANK-327-038](#bank-327-038)
<a id="bank-327-009"></a>
- `BANK-327-009` — Privacy tradeoffs in personalization → [BANK-327-039](#bank-327-039)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Routed every archived pitch by stable position; retained broad existing scopes and added two dated institutional cases with explicit evidence limits.


## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/327_privacy/NICHE_327_privacy.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
