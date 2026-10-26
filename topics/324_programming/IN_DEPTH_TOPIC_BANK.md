# 324 — Programming: main topic bank

Updated: 2026-10-23 · **15 active BANK proposals · 10 categories · 14 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Execution](#catalog-324-r01) → [Type inference](#catalog-324-r05) → [Pattern matching](#catalog-324-r06).
- **Intermediate:** [State](#catalog-324-r02) → [Reproduction](#catalog-324-r03) → [Closures](#catalog-324-r07) → [Composition](#catalog-324-r08) → [Dispatch](#catalog-324-r09) → [Logic programming](#catalog-324-r10) → [Parsing](#catalog-324-r11) → [Async tasks](#catalog-324-r14).
- **Advanced:** [Abstraction](#catalog-324-r04) → [Garbage collection](#catalog-324-r12) → [Optimization](#catalog-324-r13).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-324-01) | 2 | 0 | 0 |
| [Reasoning](#domain-324-02) | 0 | 1 | 0 |
| [Debugging](#domain-324-03) | 0 | 1 | 0 |
| [Design](#domain-324-04) | 0 | 0 | 1 |
| [Languages](#domain-324-05) | 3 | 1 | 0 |
| [Functions](#domain-324-06) | 0 | 2 | 0 |
| [Objects](#domain-324-07) | 0 | 1 | 0 |
| [Compilers](#domain-324-08) | 0 | 1 | 1 |
| [Runtime](#domain-324-09) | 0 | 0 | 1 |
| [Execution](#domain-324-10) | 0 | 0 | 0 |

<a id="domain-324-01"></a>
## Category: Foundations

<a id="catalog-324-r01"></a>
### Execution

Subcategory `CATALOG-324-R01` · foundation.

<a id="bank-324-030"></a>
#### BANK-324-030 — What happens between writing a program and seeing its output?

**Individual coverage scope:** Trace parsing, compilation or interpretation, runtime and input through a small conceptual example.

<a id="bank-324-044"></a>
#### BANK-324-044 — How did PEP 238 move Python from classic integer division toward true division without changing every Python 2 program at once?

**Individual coverage scope:** Use Python 2.2's future statement, the explicit // operator and the planned Python 3 default to trace one language migration; distinguish proposed transition design from an empirical account of every project's migration.

**Research follow-up:** [Bounded case and source-access note](324_PROGRAMMING_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-324-030](#bank-324-030) — A named operator-semantics migration versus the general path from program text to output.

**Neighboring scope:** [BANK-324-042](#bank-324-042) — Language compatibility across versions versus compiler optimization preserving behavior.


<a id="domain-324-02"></a>
## Category: Reasoning

<a id="catalog-324-r02"></a>
### State

Subcategory `CATALOG-324-R02` · intermediate.

<a id="bank-324-031"></a>
#### BANK-324-031 — Why can a function produce a different result when it depends on hidden state?

**Individual coverage scope:** Compare inputs, mutation, side effects and reproducibility; distinguish deterministic behavior from apparent randomness.


<a id="domain-324-03"></a>
## Category: Debugging

<a id="catalog-324-r03"></a>
### Reproduction

Subcategory `CATALOG-324-R03` · intermediate.

<a id="bank-324-032"></a>
#### BANK-324-032 — Why is reproducing a programming bug often harder than fixing it?

**Individual coverage scope:** Trace environment, timing, data, dependencies and minimum examples without language-specific claims.


<a id="domain-324-04"></a>
## Category: Design

<a id="catalog-324-r04"></a>
### Abstraction

Subcategory `CATALOG-324-R04` · advanced.

<a id="bank-324-033"></a>
#### BANK-324-033 — When does a programming abstraction simplify a system and when does it hide essential details?

**Individual coverage scope:** Compare interfaces, invariants, coupling, leaks and maintenance using one bounded design problem.


<a id="domain-324-05"></a>
## Category: Languages

<a id="catalog-324-r05"></a>
### Type inference

Subcategory `CATALOG-324-R05` · foundation.

<a id="bank-324-034"></a>
#### BANK-324-034 — How can a language detect type errors without requiring every type to be written?

**Individual coverage scope:** Trace constraints, inference, ambiguity and annotations through a small conceptual example.

<a id="bank-324-045"></a>
#### BANK-324-045 — What did PEP 695 change about declaring generic type parameters in Python 3.12?

**Individual coverage scope:** Compare the PEP's new class and function parameter syntax and type alias statement with earlier TypeVar declarations; keep static typing and runtime enforcement distinct.

**Research follow-up:** [Bounded case and source-access note](324_PROGRAMMING_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-324-034](#bank-324-034) — A dated generic declaration design versus general type-inference errors.

**Neighboring scope:** [BANK-061-073](../061_software_programming/IN_DEPTH_TOPIC_BANK.md#bank-061-073) — Generic declaration syntax versus Python's GIL and concurrency.

<a id="catalog-324-r06"></a>
### Pattern matching

Subcategory `CATALOG-324-R06` · foundation.

<a id="bank-324-035"></a>
#### BANK-324-035 — How is structural pattern matching different from a chain of equality checks?

**Individual coverage scope:** Compare decomposition, cases, bindings and exhaustiveness without assuming all languages implement the same rules.

<a id="catalog-324-r10"></a>
### Logic programming

Subcategory `CATALOG-324-R10` · intermediate.

<a id="bank-324-039"></a>
#### BANK-324-039 — How can a program specify relationships instead of an ordered list of commands?

**Individual coverage scope:** Trace facts, rules, queries, unification and search without treating execution order as irrelevant to performance.


<a id="domain-324-06"></a>
## Category: Functions

<a id="catalog-324-r07"></a>
### Closures

Subcategory `CATALOG-324-R07` · intermediate.

<a id="bank-324-036"></a>
#### BANK-324-036 — How can a function remember a variable after its outer function has returned?

**Individual coverage scope:** Trace lexical scope, captured bindings, lifetime and mutation with a simple hypothetical program.

<a id="catalog-324-r08"></a>
### Composition

Subcategory `CATALOG-324-R08` · intermediate.

<a id="bank-324-037"></a>
#### BANK-324-037 — When does combining small functions simplify a program's data flow?

**Individual coverage scope:** Compare types, intermediate values, side effects and error propagation rather than equating short code with clarity.


<a id="domain-324-07"></a>
## Category: Objects

<a id="catalog-324-r09"></a>
### Dispatch

Subcategory `CATALOG-324-R09` · intermediate.

<a id="bank-324-038"></a>
#### BANK-324-038 — How does a program choose which object's method runs at runtime?

**Individual coverage scope:** Compare interfaces, inheritance, dynamic dispatch and overriding with a bounded class hierarchy.


<a id="domain-324-08"></a>
## Category: Compilers

<a id="catalog-324-r11"></a>
### Parsing

Subcategory `CATALOG-324-R11` · intermediate.

<a id="bank-324-040"></a>
#### BANK-324-040 — How does source text become a syntax tree before a program runs?

**Individual coverage scope:** Compare tokens, grammar, ambiguity and tree structure using an invented expression.

<a id="catalog-324-r13"></a>
### Optimization

Subcategory `CATALOG-324-R13` · advanced.

<a id="bank-324-042"></a>
#### BANK-324-042 — Why must a compiler preserve observable behavior while transforming code?

**Individual coverage scope:** Compare semantics, undefined assumptions, aliasing and target costs through one conceptual optimization.


<a id="domain-324-09"></a>
## Category: Runtime

<a id="catalog-324-r12"></a>
### Garbage collection

Subcategory `CATALOG-324-R12` · advanced.

<a id="bank-324-041"></a>
#### BANK-324-041 — How does a runtime decide which objects are no longer reachable?

**Individual coverage scope:** Compare roots, references, cycles, collection pauses and memory limits; distinguish unreachable from unnecessary to a programmer.


<a id="domain-324-10"></a>
## Category: Execution

<a id="catalog-324-r14"></a>
### Async tasks

Subcategory `CATALOG-324-R14` · intermediate.

Original subcategory metadata is preserved. Its overlapping proposal records are retained with primary-question referrals below and excluded from the active count.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-324-010"></a>
### pending_topics/0 — The Architecture of Programming: A Language Feature's Origin

**Original question:** What problem did a named language feature originally solve?

**Original planning scope:** Use dated proposals, specifications, and early programs. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 1 (The Architecture of Programming: A Language Feature's Origin). Target: How did PEP 238 move Python from classic integer division toward true division without changing every Python 2 program at once? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-044](#bank-324-044).

<a id="bank-324-011"></a>
### pending_topics/1 — Programming: A Program Reconsidered

**Original question:** Why is one example taught so often and what does it omit?

**Original planning scope:** Run it with a named language version and examine its limits. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 2 (Programming: A Program Reconsidered). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

<a id="bank-324-012"></a>
### pending_topics/2 — Programming: The Maintainers Behind a Library

**Original question:** Who reviews changes, answers issues, and keeps compatibility?

**Original planning scope:** Use public project records and attributed accounts. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 3 (Programming: The Maintainers Behind a Library). Target: How does a runtime decide which objects are no longer reachable? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-041](#bank-324-041).

<a id="bank-324-013"></a>
### pending_topics/3 — Programming: A Program from Input to Output

**Original question:** How does a short program transform one input?

**Original planning scope:** Trace variables, control flow, errors, and output. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 4 (Programming: A Program from Input to Output). Target: What happens between writing a program and seeing its output? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-030](#bank-324-030).

<a id="bank-324-014"></a>
### pending_topics/4 — Programming: What an Abstraction Costs

**Original question:** When does a useful abstraction add time, memory, or complexity?

**Original planning scope:** Compare equivalent programs on a bounded task. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 5 (Programming: What an Abstraction Costs). Target: When does a programming abstraction simplify a system and when does it hide essential details? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-033](#bank-324-033).

<a id="bank-324-015"></a>
### pending_topics/5 — Programming: A Bug That Appears Only Sometimes

**Original question:** Which runtime conditions explain a documented intermittent error?

**Original planning scope:** Reproduce safely with version, input, and environment. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 6 (Programming: A Bug That Appears Only Sometimes). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

<a id="bank-324-016"></a>
### pending_topics/6 — Programming: A New Language Feature Tested

**Original question:** Did it improve a particular programming task?

**Original planning scope:** Compare readability, correctness, compatibility, and runtime. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 7 (Programming: A New Language Feature Tested). Target: What did PEP 695 change about declaring generic type parameters in Python 3.12? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-045](#bank-324-045).

<a id="bank-324-017"></a>
### pending_topics/7 — Programming: A Language Design Debate

**Original question:** Who argued for competing semantics and why?

**Original planning scope:** Read dated proposals and decisions, credit contributors. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 8 (Programming: A Language Design Debate). Target: What did PEP 695 change about declaring generic type parameters in Python 3.12? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-045](#bank-324-045).

<a id="bank-324-018"></a>
### pending_topics/8 — Programming: A Breaking Language Release

**Original question:** Which programs changed behavior after one release?

**Original planning scope:** Test documented examples across exact versions. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 9 (Programming: A Breaking Language Release). Target: How did PEP 238 move Python from classic integer division toward true division without changing every Python 2 program at once? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-044](#bank-324-044).

<a id="bank-324-019"></a>
### pending_topics/9 — Programming: Parsing to Execution

**Original question:** What happens between source text and a result?

**Original planning scope:** Trace parser, representation, runtime, and system calls for one implementation. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 10 (Programming: Parsing to Execution). Target: How does source text become a syntax tree before a program runs? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-040](#bank-324-040).

<a id="bank-324-020"></a>
### pending_topics/10 — Programming: Why a Language Gained Users

**Original question:** Which tasks, tools, institutions, and measures explain adoption?

**Original planning scope:** Separate surveys, code counts, and real use. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 11 (Programming: Why a Language Gained Users). Target: What happens between writing a program and seeing its output? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-030](#bank-324-030).

<a id="bank-324-021"></a>
### pending_topics/11 — Programming: One Task Across Versions

**Original question:** How did syntax, safety, and performance change?

**Original planning scope:** Use matched code and versioned documentation. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 12 (Programming: One Task Across Versions). Target: How did PEP 238 move Python from classic integer division toward true division without changing every Python 2 program at once? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-044](#bank-324-044).

<a id="bank-324-022"></a>
### pending_topics/12 — Programming: A Proposed Language Change

**Original question:** What compatibility and implementation questions remain?

**Original planning scope:** Distinguish proposal from accepted specification and deployed compiler. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 13 (Programming: A Proposed Language Change). Target: What did PEP 695 change about declaring generic type parameters in Python 3.12? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-045](#bank-324-045).

<a id="bank-324-023"></a>
### pending_topics/13 — Programming: Shorter Code Is Better?

**Original question:** When does brevity help or hide a defect?

**Original planning scope:** Compare comprehension and tests for a defined audience. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 14 (Programming: Shorter Code Is Better?). Target: When does a programming abstraction simplify a system and when does it hide essential details? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-033](#bank-324-033).

<a id="bank-324-024"></a>
### pending_topics/14 — Programming: A Bug Fix from Report to Release

**Original question:** How did a real issue become a tested change?

**Original planning scope:** Follow issue, patch, review, release, and user impact. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 15 (Programming: A Bug Fix from Report to Release). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

<a id="bank-324-025"></a>
### pending_topics/15 — Programming: Where Code Meets Its Environment

**Original question:** Which behavior comes from language, library, OS, or service?

**Original planning scope:** Name implementation and version for one program. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 16 (Programming: Where Code Meets Its Environment). Target: What happens between writing a program and seeing its output? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-030](#bank-324-030).

<a id="bank-324-026"></a>
### pending_topics/16 — Programming: A Function's Actual Contract

**Original question:** What inputs, exceptions, side effects, and outputs does it have?

**Original planning scope:** Use tests and documentation on one version. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 17 (Programming: A Function's Actual Contract). Target: Why can a function produce a different result when it depends on hidden state? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-031](#bank-324-031).

<a id="bank-324-027"></a>
### pending_topics/17 — Programming: Mutable or Immutable State

**Original question:** How do two designs affect clarity, performance, and mistakes?

**Original planning scope:** Compare matched tasks and measured outcomes. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 18 (Programming: Mutable or Immutable State). Target: Why can a function produce a different result when it depends on hidden state? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-031](#bank-324-031).

<a id="bank-324-028"></a>
### pending_topics/18 — Programming: An Error Path Nobody Tested

**Original question:** What input exposed a failure and how was it handled?

**Original planning scope:** Use a harmless reproduction and avoid exploit instructions. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 19 (Programming: An Error Path Nobody Tested). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

<a id="bank-324-029"></a>
### pending_topics/19 — Programming: Passing Tests and Missing Bugs

**Original question:** Which cases remain outside a program's test suite?

**Original planning scope:** Inspect boundaries, properties, platforms, and dependencies. Evidence base: language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 20 (Programming: Passing Tests and Missing Bugs). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

### trending_topics/0 — Programming: Record Extremes & Superlatives

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 21 (Programming: Record Extremes & Superlatives). Target: What happens between writing a program and seeing its output? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-030](#bank-324-030).

### trending_topics/1 — Programming: A Bug That Appears Only Sometimes

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 22 (Programming: A Bug That Appears Only Sometimes). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

### trending_topics/2 — Programming: A New Language Feature Tested

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 23 (Programming: A New Language Feature Tested). Target: What did PEP 695 change about declaring generic type parameters in Python 3.12? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-045](#bank-324-045).

### trending_topics/3 — Programming: Shorter Code Is Better?

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 24 (Programming: Shorter Code Is Better?). Target: When does a programming abstraction simplify a system and when does it hide essential details? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-033](#bank-324-033).

### trending_topics/4 — Programming: A Breaking Language Release

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 25 (Programming: A Breaking Language Release). Target: How did PEP 238 move Python from classic integer division toward true division without changing every Python 2 program at once? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-044](#bank-324-044).

### trending_topics/5 — Programming: The Maintainers Behind a Library

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 26 (Programming: The Maintainers Behind a Library). Target: How does a runtime decide which objects are no longer reachable? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-041](#bank-324-041).

### trending_topics/6 — Programming: A Bug Fix from Report to Release

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 27 (Programming: A Bug Fix from Report to Release). Target: Why is reproducing a programming bug often harder than fixing it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-324-032](#bank-324-032).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-324-01"></a>
### Language concepts

<a id="bank-324-001"></a>
- `BANK-324-001` — Type inference → [BANK-324-034](#bank-324-034)
<a id="bank-324-002"></a>
- `BANK-324-002` — Pattern matching → [BANK-324-035](#bank-324-035)
<a id="bank-324-003"></a>
- `BANK-324-003` — Closures → [BANK-324-036](#bank-324-036)

<a id="catalog-324-02"></a>
### Paradigms

<a id="bank-324-004"></a>
- `BANK-324-004` — Functional composition → [BANK-324-037](#bank-324-037)
<a id="bank-324-005"></a>
- `BANK-324-005` — Object-oriented dispatch → [BANK-324-038](#bank-324-038)
<a id="bank-324-006"></a>
- `BANK-324-006` — Logic programming → [BANK-324-039](#bank-324-039)

<a id="catalog-324-03"></a>
### Language implementation

<a id="bank-324-007"></a>
- `BANK-324-007` — Parsing and syntax trees → [BANK-324-040](#bank-324-040)
<a id="bank-324-008"></a>
- `BANK-324-008` — Garbage collection → [BANK-324-041](#bank-324-041)
<a id="bank-324-009"></a>
- `BANK-324-009` — Compiler optimization boundaries → [BANK-324-042](#bank-324-042)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

### Retired overlaps and primary questions

<a id="bank-324-043"></a>
- `BANK-324-043` → [BANK-061-026](../061_software_programming/IN_DEPTH_TOPIC_BANK.md#bank-061-026): Both explain why asynchronous operations do not imply parallel CPU computation using scheduling and I/O examples.

  Preserved inactive question: Why does starting several asynchronous operations not necessarily run several computations in parallel?

  Preserved inactive scope: Compare event loops, waiting, scheduling, CPU work, cancellation and shared state through a small language-neutral trace.


## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/324_programming/NICHE_324_programming.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
