# 531 — AI Software Agents: main topic bank

Updated: 2026-10-23 · **9 active BANK proposals · 5 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Agent foundations](#catalog-531-r01) → [Agent control](#catalog-531-r04).
- **Intermediate:** [Agent reliability](#catalog-531-r02) → [Agent control](#catalog-531-r05) → [Spending controls](#catalog-531-r09).
- **Advanced:** [Agent governance](#catalog-531-r03) → [Agent control](#catalog-531-r06) → [Memory evaluation](#catalog-531-r07) → [Delegation protocols](#catalog-531-r08) → [Authorized browser testing](#catalog-531-r10) → [Compensating actions](#catalog-531-r11).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-531-01) | 1 | 0 | 0 |
| [Methods and applications](#domain-531-02) | 0 | 1 | 0 |
| [Systems and interpretation](#domain-531-03) | 0 | 0 | 2 |
| [Agent system design](#domain-531-04) | 0 | 0 | 3 |
| [Agent action governance](#domain-531-05) | 0 | 1 | 1 |

<a id="domain-531-01"></a>
## Category: Foundations

<a id="catalog-531-r01"></a>
### Agent foundations

Subcategory `CATALOG-531-R01` · foundation.

Original subcategory metadata is preserved. Its overlapping proposal records are retained with primary-question referrals below and excluded from the active count.

<a id="catalog-531-r04"></a>
### Agent control

Subcategory `CATALOG-531-R04` · foundation.

<a id="bank-531-036"></a>
#### BANK-531-036 — How do reactive loops and explicit planning handle a changing task differently?

**Individual coverage scope:** Compare state, goals and tool responses.


<a id="domain-531-02"></a>
## Category: Methods and applications

<a id="catalog-531-r02"></a>
### Agent reliability

Subcategory `CATALOG-531-R02` · intermediate.

<a id="bank-531-044"></a>
#### BANK-531-044 — What did AgentDojo's 2024 benchmark separate between ordinary task success and prompt-injection outcomes?

**Individual coverage scope:** Read the original AgentDojo paper and published benchmark description for benign user tasks, untrusted tool-output attacks and distinct success measures; keep results bound to the tested models, task suite and 2024 version.

**Research follow-up:** [Bounded case and source-access note](CASE_SOURCE_NOTES.md). This does not change proposal or production status.

<a id="catalog-531-r05"></a>
### Agent control

Subcategory `CATALOG-531-R05` · intermediate.

Original subcategory metadata is preserved. Its overlapping proposal records are retained with primary-question referrals below and excluded from the active count.


<a id="domain-531-03"></a>
## Category: Systems and interpretation

<a id="catalog-531-r03"></a>
### Agent governance

Subcategory `CATALOG-531-R03` · advanced.

<a id="bank-531-035"></a>
#### BANK-531-035 — Why can multi-agent workflows amplify correlated mistakes?

**Individual coverage scope:** Trace shared assumptions, coordination and independent checks.

<a id="catalog-531-r06"></a>
### Agent control

Subcategory `CATALOG-531-R06` · advanced.

<a id="bank-531-038"></a>
#### BANK-531-038 — How should agent benchmarks account for leakage, cost and latency?

**Individual coverage scope:** Use end-to-end completion criteria and transparent boundaries.


<a id="domain-531-04"></a>
## Category: Agent system design

<a id="catalog-531-r07"></a>
### Memory evaluation

Subcategory `CATALOG-531-R07` · advanced.

<a id="bank-531-039"></a>
#### BANK-531-039 — How can a task-specific agent test whether a stored memory remains useful after a user's circumstances change?

**Individual coverage scope:** Build dated task episodes with corrected preferences, stale facts and justified forgetting; separate retrieval accuracy from task success.

<a id="catalog-531-r08"></a>
### Delegation protocols

Subcategory `CATALOG-531-R08` · advanced.

<a id="bank-531-040"></a>
#### BANK-531-040 — What must an agent delegate explicitly when a subagent can act on shared artifacts?

**Individual coverage scope:** Specify ownership, accepted inputs, cancellation, write conflicts and evidence returned at handoff in a sandbox workflow.

<a id="catalog-531-r11"></a>
### Compensating actions

Subcategory `CATALOG-531-R11` · advanced.

<a id="bank-531-043"></a>
#### BANK-531-043 — How should an agent recover when the first of two authorized actions succeeds and the second fails?

**Individual coverage scope:** Compare compensating actions, irreversible boundaries and explicit handoff using a simulated workflow rather than assume transaction rollback.


<a id="domain-531-05"></a>
## Category: Agent action governance

<a id="catalog-531-r09"></a>
### Spending controls

Subcategory `CATALOG-531-R09` · intermediate.

<a id="bank-531-041"></a>
#### BANK-531-041 — How can an agent enforce a cumulative task budget when several tools charge independently?

**Individual coverage scope:** Track reservations, settled costs, retries and concurrent calls against one task ledger; exclude financial advice.

<a id="catalog-531-r10"></a>
### Authorized browser testing

Subcategory `CATALOG-531-R10` · advanced.

<a id="bank-531-042"></a>
#### BANK-531-042 — How can a browser-agent test distinguish completing a form from successfully changing the intended external state?

**Individual coverage scope:** Use a consenting sandbox with redirects, delayed confirmation and duplicate submission tests; inspect final state and audit artifacts.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-531-010"></a>
### pending_topics/0 — The Architecture of AI Software Agents: History & Origins

**Original question:** Which documented problem led to the development of a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, trace dated origin records and distinguish contemporary aims from retrospective explanation. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Trace dated origin records and distinguish contemporary aims from retrospective explanation..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A broad agent history needs named systems and dated source versions.

<a id="bank-531-011"></a>
### pending_topics/1 — AI Software Agents: Famous Examples

**Original question:** What does a widely cited example of a versioned agent handling one bounded task establish and leave uncertain?

**Original planning scope:** For a versioned agent handling one bounded task, examine a named example against its stated aims, evidence and representativeness. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Examine a named example against its stated aims, evidence and representativeness..

**Editorial disposition:** Distinct bounded case proposed.. The 2024 AgentDojo paper provides a named benchmark case.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-012"></a>
### pending_topics/2 — AI Software Agents: Hidden Stories

**Original question:** Whose contribution or experience is missing from the usual account of a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, investigate documented labor, access and omitted perspectives among operators and affected users without inventing testimony. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Investigate documented labor, access and omitted perspectives among operators and affected users without inventing testimony..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A hidden-story claim needs specific published records, not conjecture about private systems.

<a id="bank-531-013"></a>
### pending_topics/3 — AI Software Agents: Beginner Explainers

**Original question:** Which definitions and boundaries are needed to understand a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, define essential terms, units or textual conventions using one bounded example, not an entire field survey. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Define essential terms, units or textual conventions using one bounded example, not an entire field survey..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal contrasts reactive loops and explicit planning.

**Scoped proposals:** [BANK-531-036](#bank-531-036).

<a id="bank-531-014"></a>
### pending_topics/4 — AI Software Agents: Advanced Concepts

**Original question:** Which methodological assumption changes how a versioned agent handling one bounded task should be interpreted?

**Original planning scope:** For a versioned agent handling one bounded task, test one difficult assumption, comparison or interpretive choice against an explicit alternative. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Test one difficult assumption, comparison or interpretive choice against an explicit alternative..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal addresses benchmark cost, latency and leakage.

**Scoped proposals:** [BANK-531-038](#bank-531-038).

<a id="bank-531-015"></a>
### pending_topics/5 — AI Software Agents: Mysteries & Unsolved Cases

**Original question:** What specific evidence gap remains unresolved for a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, map missing, conflicting or inaccessible evidence and state what could resolve the uncertainty. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Map missing, conflicting or inaccessible evidence and state what could resolve the uncertainty..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal leaves open general benchmark-validity questions.

**Scoped proposals:** [BANK-531-038](#bank-531-038).

<a id="bank-531-016"></a>
### pending_topics/6 — AI Software Agents: Technology & Innovation

**Original question:** What changed after a documented technical or material innovation affected a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, compare the documented change and its limitations; separate a proposed benefit from an observed result. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Compare the documented change and its limitations; separate a proposed benefit from an observed result..

**Editorial disposition:** Distinct bounded case proposed.. AgentDojo is a named evaluation environment for tool-using agents.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-017"></a>
### pending_topics/7 — AI Software Agents: People & Personalities

**Original question:** How did credited people and institutions shape a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, attribute decisions and contributions using primary records and avoid heroic or blame-centered simplification. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Attribute decisions and contributions using primary records and avoid heroic or blame-centered simplification..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. People profiles require attributed author or operator accounts; technical results alone do not supply them.

<a id="bank-531-018"></a>
### pending_topics/8 — AI Software Agents: Major Events

**Original question:** What changed around a dated turning point involving a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, reconstruct chronology from records available at each date; sequence alone does not establish cause. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Reconstruct chronology from records available at each date; sequence alone does not establish cause..

**Editorial disposition:** Distinct bounded case proposed.. The 2024 publication is a dated research event, not proof of broad deployment change.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-019"></a>
### pending_topics/9 — AI Software Agents: How It Works

**Original question:** How do the documented components or stages of a versioned agent handling one bounded task connect?

**Original planning scope:** For a versioned agent handling one bounded task, follow a defined process or argument with traceable inputs, decisions and outputs; avoid unsupported reconstruction. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Follow a defined process or argument with traceable inputs, decisions and outputs; avoid unsupported reconstruction..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal explains agent loop and plan distinctions.

**Scoped proposals:** [BANK-531-036](#bank-531-036).

<a id="bank-531-020"></a>
### pending_topics/10 — AI Software Agents: Rise & Fall

**Original question:** Which evidence explains increasing or declining use or reception of a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, define the adoption or reception measure and examine multiple documented explanations for change. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Define the adoption or reception measure and examine multiple documented explanations for change..

**Editorial disposition:** Distinct bounded case proposed.. The paper separates ordinary task failure from security-test outcomes.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-021"></a>
### pending_topics/11 — AI Software Agents: Then vs Now

**Original question:** Are earlier and later accounts of a versioned agent handling one bounded task comparable on the same terms?

**Original planning scope:** For a versioned agent handling one bounded task, match periods, definitions, versions and source survival before comparing change over time. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Match periods, definitions, versions and source survival before comparing change over time..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A then-versus-now comparison requires matched agent configurations and benchmark versions.

<a id="bank-531-022"></a>
### pending_topics/12 — AI Software Agents: Future Developments

**Original question:** Which conditions would need to hold for a proposed future change involving a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, separate observed evidence, conditional scenarios and unknowns; do not present a forecast as a fact. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Separate observed evidence, conditional scenarios and unknowns; do not present a forecast as a fact..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. Future-agent claims need a specified capability scenario and measured evidence.

<a id="bank-531-023"></a>
### pending_topics/13 — AI Software Agents: Myths vs Facts

**Original question:** Does the original evidence support a commonly repeated claim about a versioned agent handling one bounded task?

**Original planning scope:** For a versioned agent handling one bounded task, locate the original claim and compare its scope with the evidence, including legitimate interpretive disagreement. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Locate the original claim and compare its scope with the evidence, including legitimate interpretive disagreement..

**Editorial disposition:** Distinct bounded case proposed.. The named paper tests the false equivalence of benign task success and attack resistance.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-024"></a>
### pending_topics/14 — AI Software Agents: Documentary Stories

**Original question:** How can a source-led documentary explain a versioned agent handling one bounded task without overstating its evidence?

**Original planning scope:** For a versioned agent handling one bounded task, build a bounded story with attributed sources, clear illustration labels and explicit remaining uncertainty. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Build a bounded story with attributed sources, clear illustration labels and explicit remaining uncertainty..

**Editorial disposition:** Distinct bounded case proposed.. The paper and publication record provide an auditable benchmark evidence trail.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-025"></a>
### pending_topics/15 — AI Software Agents: Tool Permission Boundaries

**Original question:** Which actions may one agent perform without a person approving them?

**Original planning scope:** Trace tool schemas, authorization checks and actual permitted actions in a versioned task. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Trace tool schemas, authorization checks and actual permitted actions in a versioned task..

**Editorial disposition:** Distinct bounded case proposed.. The benchmark tests untrusted tool-output boundaries without authorizing real-account actions.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

<a id="bank-531-026"></a>
### pending_topics/16 — AI Software Agents: Planning Versus Execution

**Original question:** Where did an agent's plan diverge from its recorded actions?

**Original planning scope:** Compare a sanitized plan, tool trace and outcome without treating private reasoning as observable evidence. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Compare a sanitized plan, tool trace and outcome without treating private reasoning as observable evidence..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal covers planning versus reactive execution.

**Scoped proposals:** [BANK-531-036](#bank-531-036).

<a id="bank-531-027"></a>
### pending_topics/17 — AI Software Agents: Agent Evaluation Sets

**Original question:** Does one evaluation test realistic failures rather than only successful demos?

**Original planning scope:** Inspect task sampling, scoring, retries and unseen cases against a stated use setting. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Inspect task sampling, scoring, retries and unseen cases against a stated use setting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal covers general agent-evaluation design.

**Scoped proposals:** [BANK-531-038](#bank-531-038).

<a id="bank-531-028"></a>
### pending_topics/18 — AI Software Agents: Memory And State

**Original question:** What information survives between runs and who can inspect or remove it?

**Original planning scope:** Trace stored state, provenance, retention and reset behavior in one documented implementation. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Trace stored state, provenance, retention and reset behavior in one documented implementation..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal covers memory usefulness as circumstances change.

**Scoped proposals:** [BANK-531-039](#bank-531-039).

<a id="bank-531-029"></a>
### pending_topics/19 — AI Software Agents: Recovery And Escalation

**Original question:** When should a failed tool action trigger retry, rollback or human escalation?

**Original planning scope:** Inspect bounded failure tests and recovery records without executing destructive actions. Evidence base: Evidence: versioned tool schemas, sanitized execution traces, task evaluations and incident records. Choose a named source, version, period and case before scripting. Inspect bounded failure tests and recovery records without executing destructive actions..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal addresses recovery after partial authorized action.

**Scoped proposals:** [BANK-531-043](#bank-531-043).

### trending_topics/0 — AI Software Agents: Record Extremes & Superlatives

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A benchmark superlative needs fixed task set, version, cost and scoring rules.

### trending_topics/1 — AI Software Agents: Mysteries & Unsolved Cases

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal scopes unresolved evaluation methodology.

**Scoped proposals:** [BANK-531-038](#bank-531-038).

### trending_topics/2 — AI Software Agents: Technology & Innovation

**Editorial disposition:** Distinct bounded case proposed.. AgentDojo is a named published agent-testing environment.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

### trending_topics/3 — AI Software Agents: Myths vs Facts

**Editorial disposition:** Distinct bounded case proposed.. The paper distinguishes benign task completion from security-test outcomes.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

### trending_topics/4 — AI Software Agents: Major Events

**Editorial disposition:** Distinct bounded case proposed.. NeurIPS 2024 publication is a dated research milestone, not a universal turning point.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

### trending_topics/5 — AI Software Agents: Hidden Stories

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. Hidden-story framing needs documentary evidence about an actual system or author.

### trending_topics/6 — AI Software Agents: Documentary Stories

**Editorial disposition:** Distinct bounded case proposed.. The paper and repository form a traceable technical record.

**Scoped proposals:** [BANK-531-044](#bank-531-044).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-531-01"></a>
### Agent architectures

<a id="bank-531-001"></a>
- `BANK-531-001` — Tool-use loops → [BANK-531-036](#bank-531-036)
<a id="bank-531-002"></a>
- `BANK-531-002` — Planning versus reactive control → [BANK-531-036](#bank-531-036)
<a id="bank-531-003"></a>
- `BANK-531-003` — Persistent state → [BANK-001-081](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-081)

<a id="catalog-531-02"></a>
### Reliability

<a id="bank-531-004"></a>
- `BANK-531-004` — Permission boundaries → [BANK-001-082](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-082)
<a id="bank-531-005"></a>
- `BANK-531-005` — Recovery after tool failure → [BANK-001-080](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-080)
<a id="bank-531-006"></a>
- `BANK-531-006` — Human approval handoffs → [BANK-001-080](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-080)

<a id="catalog-531-03"></a>
### Evaluation

<a id="bank-531-007"></a>
- `BANK-531-007` — Task completion measures → [BANK-001-079](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-079)
<a id="bank-531-008"></a>
- `BANK-531-008` — Agent benchmark leakage → [BANK-531-038](#bank-531-038)
<a id="bank-531-009"></a>
- `BANK-531-009` — Cost and latency accounting → [BANK-531-038](#bank-531-038)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [001 AI + Technology Explainers](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [007 AI Tools / AI Tutorials](../007_ai_tools_ai_tutorials/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [337 AI Research](../337_ai_research/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [338 Developer AI](../338_developer_ai/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [532 Large Language Model Systems](../532_large_language_model_systems/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [533 No-Code & Low-Code Development](../533_no-code_low-code_development/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

### Retired overlaps and primary questions

<a id="bank-531-030"></a>
- `BANK-531-030` → [BANK-001-078](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-078): The foundation question is already scoped in the primary proposal; specialist additions in this pass address different system decisions.

  Preserved inactive question: How does an AI agent decide when to call a tool rather than answer directly?

  Preserved inactive scope: Separate model choice, interface constraints and permission.

<a id="bank-531-031"></a>
- `BANK-531-031` → [BANK-001-081](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-081): Long-running state beyond a transcript duplicates checkpoints, progress and recovery records already present in the agent foundation proposal.

  Preserved inactive question: Why does a long-running agent need state beyond a conversation transcript?

  Preserved inactive scope: Map task progress, artifacts and recovery points.

<a id="bank-531-032"></a>
- `BANK-531-032` → [BANK-001-046](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-046): The foundation question is already scoped in the primary proposal; specialist additions in this pass address different system decisions.

  Preserved inactive question: How can a tool response inject instructions into an agent's workflow?

  Preserved inactive scope: Explain trust boundaries through harmless authorized examples.

<a id="bank-531-033"></a>
- `BANK-531-033` → [BANK-001-079](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-079): The foundation question is already scoped in the primary proposal; specialist additions in this pass address different system decisions.

  Preserved inactive question: What makes an agent's declaration of completion insufficient evidence?

  Preserved inactive scope: Check artifacts, acceptance criteria and external state.

<a id="bank-531-034"></a>
- `BANK-531-034` → [BANK-001-082](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-082): The foundation question is already scoped in the primary proposal; specialist additions in this pass address different system decisions.

  Preserved inactive question: How can action permissions be limited without blocking useful agent work?

  Preserved inactive scope: Compare scope, approvals and reversible operations.

<a id="bank-531-037"></a>
- `BANK-531-037` → [BANK-001-080](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-080): The foundation question is already scoped in the primary proposal; specialist additions in this pass address different system decisions.

  Preserved inactive question: How can a failed tool call become a safe recovery rather than an endless retry loop?

  Preserved inactive scope: Map error classes and human handoffs.


## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Concrete case selection for Memory evaluation:** Build dated task episodes with corrected preferences, stale facts and justified forgetting; separate retrieval accuracy from task success. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Delegation protocols:** Specify ownership, accepted inputs, cancellation, write conflicts and evidence returned at handoff in a sandbox workflow. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Spending controls:** Track reservations, settled costs, retries and concurrent calls against one task ledger; exclude financial advice. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Authorized browser testing:** Use a consenting sandbox with redirects, delayed confirmation and duplicate submission tests; inspect final state and audit artifacts. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Compensating actions:** Compare compensating actions, irreversible boundaries and explicit handoff using a simulated workflow rather than assume transaction rollback. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/531_ai_software_agents/NICHE_531_ai_software_agents.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
