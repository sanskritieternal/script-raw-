# 326 — Cybersecurity: main topic bank

Updated: 2026-10-23 · **13 active BANK proposals · 9 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Threat models](#catalog-326-r01).
- **Intermediate:** [Authentication](#catalog-326-r02) → [Patching](#catalog-326-r03) → [Least privilege](#catalog-326-r05) → [Network segmentation](#catalog-326-r08).
- **Advanced:** [Defense in depth](#catalog-326-r04) → [Backup isolation](#catalog-326-r06) → [Disclosure](#catalog-326-r07) → [Authorized testing](#catalog-326-r09) → [Security metrics](#catalog-326-r10) → [Incident containment choices](#catalog-326-r11).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-326-01) | 1 | 0 | 0 |
| [Identity](#domain-326-02) | 0 | 1 | 0 |
| [Operations](#domain-326-03) | 0 | 2 | 0 |
| [Risk](#domain-326-04) | 0 | 0 | 2 |
| [Architecture](#domain-326-05) | 0 | 2 | 0 |
| [Recovery](#domain-326-06) | 0 | 0 | 1 |
| [Governance](#domain-326-07) | 0 | 0 | 2 |
| [Measurement](#domain-326-08) | 0 | 0 | 1 |
| [Response](#domain-326-09) | 0 | 0 | 1 |

<a id="domain-326-01"></a>
## Category: Foundations

<a id="catalog-326-r01"></a>
### Threat models

Subcategory `CATALOG-326-R01` · foundation.

<a id="bank-326-030"></a>
#### BANK-326-030 — Why does cybersecurity begin with identifying what needs protection?

**Individual coverage scope:** Map assets, adversaries, entry points and consequences for a hypothetical service without intrusion instructions.


<a id="domain-326-02"></a>
## Category: Identity

<a id="catalog-326-r02"></a>
### Authentication

Subcategory `CATALOG-326-R02` · intermediate.

<a id="bank-326-031"></a>
#### BANK-326-031 — Why does multi-factor authentication still require account recovery design?

**Individual coverage scope:** Compare factors, recovery channels, support access and bypass risks from a defensive perspective.


<a id="domain-326-03"></a>
## Category: Operations

<a id="catalog-326-r03"></a>
### Patching

Subcategory `CATALOG-326-R03` · intermediate.

<a id="bank-326-032"></a>
#### BANK-326-032 — Why can applying a security patch be operationally difficult?

**Individual coverage scope:** Trace compatibility, inventory, testing, deployment and compensating controls without exploiting vulnerabilities.

<a id="bank-326-042"></a>
#### BANK-326-042 — What did the December 2021 Log4j response reveal about finding a vulnerable dependency across products?

**Individual coverage scope:** Use the archived CISA joint advisory to trace the vendor-to-operator information chain and affected-version uncertainty at that date; avoid exploit mechanics and present-day patch prescriptions.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.


<a id="domain-326-04"></a>
## Category: Risk

<a id="catalog-326-r04"></a>
### Defense in depth

Subcategory `CATALOG-326-R04` · advanced.

<a id="bank-326-033"></a>
#### BANK-326-033 — How can several security controls fail through one shared dependency?

**Individual coverage scope:** Compare identity, logging, backups and control-plane access; focus on defensive architecture and incident learning.

<a id="bank-326-041"></a>
#### BANK-326-041 — How did CISA's December 2020 SolarWinds Orion directive turn uncertain compromise into a bounded federal response?

**Individual coverage scope:** Examine the dated ED 21-01 and later supplemental guidance as an agency decision record: affected product scope, disconnection, reporting, and evidence limits. Do not infer every Orion installation or agency was compromised or give incident-response instructions.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.


<a id="domain-326-05"></a>
## Category: Architecture

<a id="catalog-326-r05"></a>
### Least privilege

Subcategory `CATALOG-326-R05` · intermediate.

<a id="bank-326-034"></a>
#### BANK-326-034 — How can a permission become excessive even if it was originally necessary?

**Individual coverage scope:** Trace role changes, service accounts, temporary access, inheritance and review from a defensive perspective.

<a id="catalog-326-r08"></a>
### Network segmentation

Subcategory `CATALOG-326-R08` · intermediate.

<a id="bank-326-037"></a>
#### BANK-326-037 — How can network segmentation limit the consequences of one compromised system?

**Individual coverage scope:** Compare permitted flows, identities, enforcement points and monitoring from a defensive perspective.


<a id="domain-326-06"></a>
## Category: Recovery

<a id="catalog-326-r06"></a>
### Backup isolation

Subcategory `CATALOG-326-R06` · advanced.

<a id="bank-326-035"></a>
#### BANK-326-035 — Why must backup access be separated from ordinary administrative access?

**Individual coverage scope:** Compare shared credentials, deletion paths, recovery testing and independent safeguards without attack instructions.


<a id="domain-326-07"></a>
## Category: Governance

<a id="catalog-326-r07"></a>
### Disclosure

Subcategory `CATALOG-326-R07` · advanced.

<a id="bank-326-036"></a>
#### BANK-326-036 — How can vulnerability disclosure coordinate researchers, maintainers and affected users?

**Individual coverage scope:** Trace authorization, evidence, timelines, remediation and communication; exclude publishing exploitable details before appropriate coordination.

<a id="catalog-326-r09"></a>
### Authorized testing

Subcategory `CATALOG-326-R09` · advanced.

<a id="bank-326-038"></a>
#### BANK-326-038 — What must a security-testing scope settle before testing begins?

**Individual coverage scope:** Specify assets, accounts, methods, data handling, time windows, stop conditions and reporting under explicit authorization.


<a id="domain-326-08"></a>
## Category: Measurement

<a id="catalog-326-r10"></a>
### Security metrics

Subcategory `CATALOG-326-R10` · advanced.

<a id="bank-326-039"></a>
#### BANK-326-039 — Why can closing more security tickets fail to reduce the most important risks?

**Individual coverage scope:** Compare severity, exposure, asset importance, recurrence and outcome measures without treating one score as complete risk.


<a id="domain-326-09"></a>
## Category: Response

<a id="catalog-326-r11"></a>
### Incident containment choices

Subcategory `CATALOG-326-R11` · advanced.

<a id="bank-326-040"></a>
#### BANK-326-040 — Why can disconnecting a compromised system protect one service while disrupting evidence collection and other essential work?

**Individual coverage scope:** Compare incident objectives, authority, service dependencies, logs, recovery and documented tradeoffs in a fictional defensive exercise; exclude live containment instructions.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-326-010"></a>
### pending_topics/0 — The Architecture of Cybersecurity: A Security Practice Takes Shape

**Original question:** Which documented incident or need changed one defensive practice?

**Original planning scope:** Use dated standards and incident records. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Early security-practice history remains a broad framing; asset and threat identification is the active entry point.

**Scoped proposals:** [BANK-326-030](#bank-326-030).

<a id="bank-326-011"></a>
### pending_topics/1 — Cybersecurity: A Widely Cited Breach Revisited

**Original question:** Which failures are supported by public evidence?

**Original planning scope:** Separate investigation findings from speculation. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** new_bounded_case. The named SolarWinds directive supplies a public incident decision record.

**Scoped proposals:** [BANK-326-041](#bank-326-041).

<a id="bank-326-012"></a>
### pending_topics/2 — Cybersecurity: Security Work After Headlines

**Original question:** Who restores service, supports victims, and fixes controls?

**Original planning scope:** Use public records and consented accounts. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Post-headline triage and restoration already sit in incident containment and backup scope.

**Scoped proposals:** [BANK-326-040](#bank-326-040), [BANK-326-035](#bank-326-035).

<a id="bank-326-013"></a>
### pending_topics/3 — Cybersecurity: What a Security Control Protects

**Original question:** What asset and failure does one control address?

**Original planning scope:** Define threat, user, boundary, and expected outcome. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Threat modeling gives the bounded control purpose.

**Scoped proposals:** [BANK-326-030](#bank-326-030).

<a id="bank-326-014"></a>
### pending_topics/4 — Cybersecurity: Defense in Depth Tested

**Original question:** Do multiple controls fail independently in a defined scenario?

**Original planning scope:** Map dependencies and validation evidence. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Shared dependencies already test defense in depth.

**Scoped proposals:** [BANK-326-033](#bank-326-033).

<a id="bank-326-015"></a>
### pending_topics/5 — Cybersecurity: An Incident's Unknown Cause

**Original question:** Which facts are established and what remains uncertain?

**Original planning scope:** Compare official timeline, logs, and plausible alternatives. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Unknown cause requires evidence and uncertainty handling in existing incident scope.

**Scoped proposals:** [BANK-326-040](#bank-326-040).

<a id="bank-326-016"></a>
### pending_topics/6 — Cybersecurity: A New Defensive Product

**Original question:** Did it reduce a defined risk without unacceptable costs?

**Original planning scope:** Compare detection quality, false alarms, coverage, and operations. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. No named product or evaluation protocol in archive; use risk metrics and testing scope.

**Scoped proposals:** [BANK-326-039](#bank-326-039), [BANK-326-038](#bank-326-038).

<a id="bank-326-017"></a>
### pending_topics/7 — Cybersecurity: A Risk Decision

**Original question:** Who accepted a residual risk and with what information?

**Original planning scope:** Trace governance records and affected groups. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Risk prioritization is covered by metric and consequence framing.

**Scoped proposals:** [BANK-326-039](#bank-326-039).

<a id="bank-326-018"></a>
### pending_topics/8 — Cybersecurity: A Public Incident Timeline

**Original question:** What happened from detection through recovery?

**Original planning scope:** Use dated notices and postmortem; avoid operational attack steps. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** new_bounded_case. ED 21-01 gives a dated, jurisdiction-bound incident timeline.

**Scoped proposals:** [BANK-326-041](#bank-326-041).

<a id="bank-326-019"></a>
### pending_topics/9 — Cybersecurity: From Alert to Response

**Original question:** How does a team validate and triage a signal?

**Original planning scope:** Describe roles, evidence preservation, and escalation at a safe level. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Alert-to-response belongs to incident containment choices.

**Scoped proposals:** [BANK-326-040](#bank-326-040).

<a id="bank-326-020"></a>
### pending_topics/10 — Cybersecurity: Changing Threat Reports

**Original question:** Is an apparent increase a change in attacks or reporting?

**Original planning scope:** Check definitions, detection, population, and time window. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** new_bounded_case. CISA's dated Log4j advisory makes evolving dependency reports concrete.

**Scoped proposals:** [BANK-326-042](#bank-326-042).

<a id="bank-326-021"></a>
### pending_topics/11 — Cybersecurity: A Control Before and After Deployment

**Original question:** Did exposure and response improve?

**Original planning scope:** Match assets, measurement, and threat context. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Control deployment and shared-dependency failure already scoped.

**Scoped proposals:** [BANK-326-033](#bank-326-033).

<a id="bank-326-022"></a>
### pending_topics/12 — Cybersecurity: An Emerging Security Claim

**Original question:** What evidence would show a proposed defense works?

**Original planning scope:** Define adversary capability, deployment limits, and independent test. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. An unspecified emerging claim needs a named product and evidence before a new case.

**Scoped proposals:** [BANK-326-039](#bank-326-039).

<a id="bank-326-023"></a>
### pending_topics/13 — Cybersecurity: One Tool Makes a System Secure?

**Original question:** Which risks lie outside a tool's scope?

**Original planning scope:** Map assets, people, process, and dependencies. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Single-tool security claim is tested by shared dependency and threat model.

**Scoped proposals:** [BANK-326-033](#bank-326-033), [BANK-326-030](#bank-326-030).

<a id="bank-326-024"></a>
### pending_topics/14 — Cybersecurity: Recovery After an Incident

**Original question:** How did an organization restore trusted service?

**Original planning scope:** Use public timeline, impacted users, and documented lessons. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Recovery planning already has backup and containment questions.

**Scoped proposals:** [BANK-326-035](#bank-326-035), [BANK-326-040](#bank-326-040).

<a id="bank-326-025"></a>
### pending_topics/15 — Cybersecurity: Who Secures a Shared Service?

**Original question:** Which duties belong to provider, customer, vendor, and user?

**Original planning scope:** Use named architecture and contractual responsibility. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** cross_niche_overlap. Managed-service responsibility belongs with cloud shared-responsibility case BANK-322-038; least privilege remains local context.

**Scoped proposals:** [BANK-322-038](../322_cloud_computing/IN_DEPTH_TOPIC_BANK.md#bank-322-038), [BANK-326-034](#bank-326-034).

<a id="bank-326-026"></a>
### pending_topics/16 — Cybersecurity: A Security Alert's Evidence

**Original question:** What data triggers an alert and what does it actually prove?

**Original planning scope:** Trace logging, detection rule, context, and false positives. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Alert evidence and service interruption belong to incident containment.

**Scoped proposals:** [BANK-326-040](#bank-326-040).

<a id="bank-326-027"></a>
### pending_topics/17 — Cybersecurity: Stronger Control and User Friction

**Original question:** How does a control affect security and access?

**Original planning scope:** Test intended users, bypass pressure, and recovery. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. MFA recovery gives a bounded security-friction example.

**Scoped proposals:** [BANK-326-031](#bank-326-031).

<a id="bank-326-028"></a>
### pending_topics/18 — Cybersecurity: A Defensive Control Fails

**Original question:** Why did a control miss or misclassify an event?

**Original planning scope:** Analyze public incident and avoid reproduction instructions. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** new_bounded_case. SolarWinds is a named case for a trusted-control failure and response limits.

**Scoped proposals:** [BANK-326-041](#bank-326-041).

<a id="bank-326-029"></a>
### pending_topics/19 — Cybersecurity: What a Security Exercise Misses

**Original question:** Which actors or conditions were outside the test?

**Original planning scope:** State scope, authorization, environment, and uncertainty. Evidence base: NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts.

**Editorial disposition:** existing_scope. Authorized testing scope sets a bounded exercise question.

**Scoped proposals:** [BANK-326-038](#bank-326-038).

### trending_topics/0 — Cybersecurity: Record Extremes & Superlatives

**Editorial disposition:** out_of_scope. No dated record measure, denominator or comparable case is named; superlative framing is unsupported.

### trending_topics/1 — Cybersecurity: An Incident's Unknown Cause

**Editorial disposition:** existing_scope. Same unknown-cause pitch as pending/5.

**Scoped proposals:** [BANK-326-040](#bank-326-040).

### trending_topics/2 — Cybersecurity: A New Defensive Product

**Editorial disposition:** existing_scope. Same unnamed defensive-product pitch as pending/6.

**Scoped proposals:** [BANK-326-039](#bank-326-039).

### trending_topics/3 — Cybersecurity: One Tool Makes a System Secure?

**Editorial disposition:** existing_scope. Same single-tool pitch as pending/13.

**Scoped proposals:** [BANK-326-033](#bank-326-033).

### trending_topics/4 — Cybersecurity: A Public Incident Timeline

**Editorial disposition:** new_bounded_case. Same timeline pitch as pending/8; route to the SolarWinds case.

**Scoped proposals:** [BANK-326-041](#bank-326-041).

### trending_topics/5 — Cybersecurity: Security Work After Headlines

**Editorial disposition:** existing_scope. Same post-headline pitch as pending/2.

**Scoped proposals:** [BANK-326-040](#bank-326-040).

### trending_topics/6 — Cybersecurity: Recovery After an Incident

**Editorial disposition:** existing_scope. Same recovery pitch as pending/14.

**Scoped proposals:** [BANK-326-035](#bank-326-035).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-326-01"></a>
### Defensive foundations

<a id="bank-326-001"></a>
- `BANK-326-001` — Threat modeling → [BANK-326-030](#bank-326-030)
<a id="bank-326-002"></a>
- `BANK-326-002` — Least privilege → [BANK-326-034](#bank-326-034)
<a id="bank-326-003"></a>
- `BANK-326-003` — Patch prioritization → [BANK-326-032](#bank-326-032)

<a id="catalog-326-02"></a>
### System protections

<a id="bank-326-004"></a>
- `BANK-326-004` — Multifactor authentication → [BANK-326-031](#bank-326-031)
<a id="bank-326-005"></a>
- `BANK-326-005` — Network segmentation → [BANK-326-037](#bank-326-037)
<a id="bank-326-006"></a>
- `BANK-326-006` — Backup isolation → [BANK-326-035](#bank-326-035)

<a id="catalog-326-03"></a>
### Assessment

<a id="bank-326-007"></a>
- `BANK-326-007` — Authorized security testing scope → [BANK-326-038](#bank-326-038)
<a id="bank-326-008"></a>
- `BANK-326-008` — Vulnerability disclosure → [BANK-326-036](#bank-326-036)
<a id="bank-326-009"></a>
- `BANK-326-009` — Security metrics versus actual risk → [BANK-326-039](#bank-326-039)

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

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/326_cybersecurity/NICHE_326_cybersecurity.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
