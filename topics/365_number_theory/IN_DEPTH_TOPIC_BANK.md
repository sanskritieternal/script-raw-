# 365 — Number Theory: main topic bank

Updated: 2026-10-23 · **13 active BANK proposals · 9 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Primes](#catalog-365-r01).
- **Intermediate:** [Remainders](#catalog-365-r02) → [Infinite primes](#catalog-365-r03) → [Diophantine problems](#catalog-365-r05) → [Fermat's little theorem](#catalog-365-r06) → [Squares](#catalog-365-r07) → [Checksums](#catalog-365-r08).
- **Advanced:** [Prime patterns](#catalog-365-r04) → [Cryptography](#catalog-365-r09) → [Pseudorandomness](#catalog-365-r10) → [Constructive existence](#catalog-365-r11).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-365-01) | 1 | 0 | 0 |
| [Modular arithmetic](#domain-365-02) | 0 | 1 | 0 |
| [Proof](#domain-365-03) | 0 | 1 | 1 |
| [Frontiers](#domain-365-04) | 0 | 0 | 1 |
| [Equations](#domain-365-05) | 0 | 2 | 0 |
| [Theorems](#domain-365-06) | 0 | 2 | 0 |
| [Residues](#domain-365-07) | 0 | 1 | 0 |
| [Applications](#domain-365-08) | 0 | 1 | 1 |
| [Sequences](#domain-365-09) | 0 | 0 | 1 |

<a id="domain-365-01"></a>
## Category: Foundations

<a id="catalog-365-r01"></a>
### Primes

Subcategory `CATALOG-365-R01` · foundation.

<a id="bank-365-030"></a>
#### BANK-365-030 — Why are prime numbers useful for understanding all whole-number multiplication?

**Individual coverage scope:** Explain divisibility, factorization and uniqueness through worked small examples without assuming an even spacing of primes.


<a id="domain-365-02"></a>
## Category: Modular arithmetic

<a id="catalog-365-r02"></a>
### Remainders

Subcategory `CATALOG-365-R02` · intermediate.

<a id="bank-365-031"></a>
#### BANK-365-031 — How can arithmetic wrap around while preserving useful structure?

**Individual coverage scope:** Compare congruence, addition, multiplication and clock examples; distinguish modular division from ordinary division.


<a id="domain-365-03"></a>
## Category: Proof

<a id="catalog-365-r03"></a>
### Infinite primes

Subcategory `CATALOG-365-R03` · intermediate.

<a id="bank-365-032"></a>
#### BANK-365-032 — Why does Euclid's argument establish infinitely many primes without listing them?

**Individual coverage scope:** Trace the finite-list assumption, constructed number and contradiction; avoid implying the constructed number must itself be prime.

<a id="catalog-365-r11"></a>
### Constructive existence

Subcategory `CATALOG-365-R11` · advanced.

<a id="bank-365-040"></a>
#### BANK-365-040 — How can a number-theory proof establish that an integer exists without providing an efficient way to find it?

**Individual coverage scope:** Compare existence, construction, bounds, search and computational complexity through a selected accessible theorem; do not conflate proof with a practical algorithm.


<a id="domain-365-04"></a>
## Category: Frontiers

<a id="catalog-365-r04"></a>
### Prime patterns

Subcategory `CATALOG-365-R04` · advanced.

<a id="bank-365-033"></a>
#### BANK-365-033 — Why can strong numerical evidence fail to settle a number-theory conjecture?

**Individual coverage scope:** Compare checked ranges, proof, counterexample and asymptotic claims using a clearly labeled unsolved question.


<a id="domain-365-05"></a>
## Category: Equations

<a id="catalog-365-r05"></a>
### Diophantine problems

Subcategory `CATALOG-365-R05` · intermediate.

<a id="bank-365-034"></a>
#### BANK-365-034 — Why does requiring whole-number solutions change an ordinary-looking equation?

**Individual coverage scope:** Compare integer constraints, divisibility, bounds and worked small examples.

<a id="bank-365-041"></a>
#### BANK-365-041 — What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem?

**Individual coverage scope:** Track the published modular-elliptic-curve result and companion ring-theoretic argument at the level of stated theorem and dependency; avoid presenting a short sketch as a verification of the full proof.

**Research follow-up:** [Bounded case and source-access note](365_NUMBER_THEORY_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-365-034](#bank-365-034) — A named theorem/proof publication versus general integer-solution constraints.

**Neighboring scope:** [BANK-365-033](#bank-365-033) — Proved historical claim versus numerical evidence for unsolved conjectures.


<a id="domain-365-06"></a>
## Category: Theorems

<a id="catalog-365-r06"></a>
### Fermat's little theorem

Subcategory `CATALOG-365-R06` · intermediate.

<a id="bank-365-035"></a>
#### BANK-365-035 — What does Fermat's little theorem guarantee and what does it not say about primality?

**Individual coverage scope:** State assumptions, demonstrate modular powers and distinguish necessary conditions from sufficient tests.

<a id="bank-365-042"></a>
#### BANK-365-042 — What did the AKS primality paper prove about deterministic polynomial-time testing, and what did its 2019 erratum repair?

**Individual coverage scope:** Compare the 2004 theorem statement with the authors' specific correction to Lemma 4.3; separate asymptotic existence of an algorithm from a claim that it is fastest in practical use.

**Research follow-up:** [Bounded case and source-access note](365_NUMBER_THEORY_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-365-035](#bank-365-035) — Deterministic full primality algorithm versus the limited statement of Fermat's little theorem.

**Neighboring scope:** [BANK-365-038](#bank-365-038) — Complexity theorem for primality versus generic forward/reverse computational asymmetry.

**Neighboring scope:** [BANK-366-030](../366_infinity/IN_DEPTH_TOPIC_BANK.md#bank-366-030) — Finite integer decision problem versus the distinction between endless processes and completed infinite sets.


<a id="domain-365-07"></a>
## Category: Residues

<a id="catalog-365-r07"></a>
### Squares

Subcategory `CATALOG-365-R07` · intermediate.

<a id="bank-365-036"></a>
#### BANK-365-036 — Why are only some remainders possible when integers are squared modulo a number?

**Individual coverage scope:** Compare residue classes, examples, structure and prime versus composite moduli.


<a id="domain-365-08"></a>
## Category: Applications

<a id="catalog-365-r08"></a>
### Checksums

Subcategory `CATALOG-365-R08` · intermediate.

<a id="bank-365-037"></a>
#### BANK-365-037 — How can modular arithmetic detect a mistyped number without recovering the intended one?

**Individual coverage scope:** Compare weighted sums, error patterns, collision limits and a small invented identifier.

<a id="catalog-365-r09"></a>
### Cryptography

Subcategory `CATALOG-365-R09` · advanced.

<a id="bank-365-038"></a>
#### BANK-365-038 — Why can a number-theory problem be easy in one direction and difficult to reverse?

**Individual coverage scope:** Compare computation, problem assumptions, key sizes conceptually and security limits; exclude cryptographic implementation advice.


<a id="domain-365-09"></a>
## Category: Sequences

<a id="catalog-365-r10"></a>
### Pseudorandomness

Subcategory `CATALOG-365-R10` · advanced.

<a id="bank-365-039"></a>
#### BANK-365-039 — How can a deterministic arithmetic process produce random-looking numbers?

**Individual coverage scope:** Compare state, recurrence, period, distribution tests and predictability; distinguish appearance from cryptographic security.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-365-010"></a>
### pending_topics/0 — The Architecture of Number Theory: A Divisibility Question Emerges

**Original question:** Which problem led to a named number-theoretic method?

**Original planning scope:** Use dated primary proofs and context. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 1 (The Architecture of Number Theory: A Divisibility Question Emerges) through: Why are prime numbers useful for understanding all whole-number multiplication? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-030](#bank-365-030).

<a id="bank-365-011"></a>
### pending_topics/1 — Number Theory: A Classic Prime Proof Rechecked

**Original question:** What does the argument establish exactly?

**Original planning scope:** Trace contradiction and avoid claiming a constructed next prime. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 2 (Number Theory: A Classic Prime Proof Rechecked) through: Why does Euclid's argument establish infinitely many primes without listing them? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-032](#bank-365-032).

<a id="bank-365-012"></a>
### pending_topics/2 — Number Theory: Contributors to a Number-Theory Result

**Original question:** Whose proof, computation, or correspondence is overlooked?

**Original planning scope:** Use dated publications and attribution. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 3 (Number Theory: Contributors to a Number-Theory Result) through: What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-041](#bank-365-041).

<a id="bank-365-013"></a>
### pending_topics/3 — Number Theory: Divisibility and Remainders

**Original question:** How does modular arithmetic answer one concrete question?

**Original planning scope:** Define congruence and show a small example. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 4 (Number Theory: Divisibility and Remainders) through: How can arithmetic wrap around while preserving useful structure? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-031](#bank-365-031).

<a id="bank-365-014"></a>
### pending_topics/4 — Number Theory: Proof Beyond Computation

**Original question:** Why can checking many integers never establish a universal claim?

**Original planning scope:** Compare finite evidence with deduction. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 5 (Number Theory: Proof Beyond Computation) through: What did the AKS primality paper prove about deterministic polynomial-time testing, and what did its 2019 erratum repair? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-042](#bank-365-042).

<a id="bank-365-015"></a>
### pending_topics/5 — Number Theory: A Current Number-Theory Conjecture

**Original question:** Which ranges are checked and what remains unproved?

**Original planning scope:** Use dated authoritative status and exact statement. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 6 (Number Theory: A Current Number-Theory Conjecture) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

<a id="bank-365-016"></a>
### pending_topics/6 — Number Theory: Computers in Number Theory

**Original question:** Did computation discover a pattern or certify a proof?

**Original planning scope:** Describe algorithm, bounds, and verification. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 7 (Number Theory: Computers in Number Theory) through: What did the AKS primality paper prove about deterministic polynomial-time testing, and what did its 2019 erratum repair? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-042](#bank-365-042).

<a id="bank-365-017"></a>
### pending_topics/7 — Number Theory: A Proof Claim Examined

**Original question:** How did mathematicians check a proposed argument?

**Original planning scope:** Follow paper, critique, and correction. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 8 (Number Theory: A Proof Claim Examined) through: What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-041](#bank-365-041).

<a id="bank-365-018"></a>
### pending_topics/8 — Number Theory: A Theorem's Proof Milestone

**Original question:** Which lemma resolved a previously open case?

**Original planning scope:** Use original work and independent exposition. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 9 (Number Theory: A Theorem's Proof Milestone) through: What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-041](#bank-365-041).

<a id="bank-365-019"></a>
### pending_topics/9 — Number Theory: A Modular Proof

**Original question:** How do residue classes constrain solutions?

**Original planning scope:** Write definitions, inference, and boundary cases. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 10 (Number Theory: A Modular Proof) through: How can arithmetic wrap around while preserving useful structure? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-031](#bank-365-031).

<a id="bank-365-020"></a>
### pending_topics/10 — Number Theory: A Conjectured Pattern Reassessed

**Original question:** What counterexample or theorem changed it?

**Original planning scope:** Show exact statement before and after. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 11 (Number Theory: A Conjectured Pattern Reassessed) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

<a id="bank-365-021"></a>
### pending_topics/11 — Number Theory: One Problem Across Methods

**Original question:** How did elementary, analytic, or computational approaches differ?

**Original planning scope:** Compare what each proves. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 12 (Number Theory: One Problem Across Methods) through: What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-041](#bank-365-041).

<a id="bank-365-022"></a>
### pending_topics/12 — Number Theory: A Number-Theory Research Direction

**Original question:** Which exact special case might advance an open question?

**Original planning scope:** State known bounds and proof gap. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 13 (Number Theory: A Number-Theory Research Direction) through: What did the AKS primality paper prove about deterministic polynomial-time testing, and what did its 2019 erratum repair? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-042](#bank-365-042).

<a id="bank-365-023"></a>
### pending_topics/13 — Number Theory: Large Test Equals Proof?

**Original question:** What remains outside a finite search?

**Original planning scope:** Explain quantifier and possible counterexample. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 14 (Number Theory: Large Test Equals Proof?) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

<a id="bank-365-024"></a>
### pending_topics/14 — Number Theory: A Conjecture's Evidence Trail

**Original question:** How did examples, partial results, and proofs accumulate?

**Original planning scope:** Date claims and correct status. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 15 (Number Theory: A Conjecture's Evidence Trail) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

<a id="bank-365-025"></a>
### pending_topics/15 — Number Theory: Pattern in Integers to Theorem

**Original question:** What conjecture follows from examples and how could it be tested?

**Original planning scope:** Separate data and proof. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 16 (Number Theory: Pattern in Integers to Theorem) through: How can a number-theory proof establish that an integer exists without providing an efficient way to find it? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-040](#bank-365-040).

<a id="bank-365-026"></a>
### pending_topics/16 — Number Theory: Counting Arithmetic Objects

**Original question:** Which algorithm and bound produced a reported count?

**Original planning scope:** State exactness, code, and verification. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 17 (Number Theory: Counting Arithmetic Objects) through: Why are prime numbers useful for understanding all whole-number multiplication? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-030](#bank-365-030).

<a id="bank-365-027"></a>
### pending_topics/17 — Number Theory: Small Numbers to All Integers

**Original question:** When does an observed pattern stop generalizing?

**Original planning scope:** Seek structural proof or counterexample. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 18 (Number Theory: Small Numbers to All Integers) through: Why does Euclid's argument establish infinitely many primes without listing them? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-032](#bank-365-032).

<a id="bank-365-028"></a>
### pending_topics/18 — Number Theory: Computation and Formal Proof

**Original question:** What can a search establish for a finite range?

**Original planning scope:** State machine, method, bound, and theorem status. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 19 (Number Theory: Computation and Formal Proof) through: What did the AKS primality paper prove about deterministic polynomial-time testing, and what did its 2019 erratum repair? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-042](#bank-365-042).

<a id="bank-365-029"></a>
### pending_topics/19 — Number Theory: Residue Classes

**Original question:** How does a result differ across congruence classes?

**Original planning scope:** Partition cases and verify coverage. Evidence base: original theorems and proofs, mathematical society expositions, verified algorithms, dated conjecture status, and formal counterexamples.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 20 (Number Theory: Residue Classes) through: Why are only some remainders possible when integers are squared modulo a number? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-036](#bank-365-036).

### trending_topics/0 — Number Theory: A Boundary Integer

**Editorial disposition:** merge_existing. Existing question covers archived pitch 21 (Number Theory: A Boundary Integer) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

### trending_topics/1 — Number Theory: A Current Number-Theory Conjecture

**Editorial disposition:** merge_existing. Existing question covers archived pitch 22 (Number Theory: A Current Number-Theory Conjecture) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

### trending_topics/2 — Number Theory: Computers in Number Theory

**Editorial disposition:** new_case. Named sourced case covers archived pitch 23 (Number Theory: Computers in Number Theory) through: What did the AKS primality paper prove about deterministic polynomial-time testing, and what did its 2019 erratum repair? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-042](#bank-365-042).

### trending_topics/3 — Number Theory: Large Test Equals Proof?

**Editorial disposition:** merge_existing. Existing question covers archived pitch 24 (Number Theory: Large Test Equals Proof?) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

### trending_topics/4 — Number Theory: A Theorem's Proof Milestone

**Editorial disposition:** new_case. Named sourced case covers archived pitch 25 (Number Theory: A Theorem's Proof Milestone) through: What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-041](#bank-365-041).

### trending_topics/5 — Number Theory: Contributors to a Number-Theory Result

**Editorial disposition:** new_case. Named sourced case covers archived pitch 26 (Number Theory: Contributors to a Number-Theory Result) through: What did the paired 1995 Wiles and Taylor–Wiles papers establish on the route to Fermat's Last Theorem? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-041](#bank-365-041).

### trending_topics/6 — Number Theory: A Conjecture's Evidence Trail

**Editorial disposition:** merge_existing. Existing question covers archived pitch 27 (Number Theory: A Conjecture's Evidence Trail) through: Why can strong numerical evidence fail to settle a number-theory conjecture? Original archive wording remains in topics_status.json and does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-365-033](#bank-365-033).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-365-01"></a>
### Integer structures

<a id="bank-365-001"></a>
- `BANK-365-001` — Prime factorization → [BANK-365-030](#bank-365-030)
<a id="bank-365-002"></a>
- `BANK-365-002` — Modular arithmetic → [BANK-365-031](#bank-365-031)
<a id="bank-365-003"></a>
- `BANK-365-003` — Diophantine equations → [BANK-365-034](#bank-365-034)

<a id="catalog-365-02"></a>
### Theorems and methods

<a id="bank-365-004"></a>
- `BANK-365-004` — Euclid's infinitude proof → [BANK-365-032](#bank-365-032)
<a id="bank-365-005"></a>
- `BANK-365-005` — Fermat's little theorem → [BANK-365-035](#bank-365-035)
<a id="bank-365-006"></a>
- `BANK-365-006` — Quadratic residues → [BANK-365-036](#bank-365-036)

<a id="catalog-365-03"></a>
### Applications

<a id="bank-365-007"></a>
- `BANK-365-007` — Cryptographic number theory → [BANK-365-038](#bank-365-038)
<a id="bank-365-008"></a>
- `BANK-365-008` — Error-detecting checksums → [BANK-365-037](#bank-365-037)
<a id="bank-365-009"></a>
- `BANK-365-009` — Pseudorandomness and periods → [BANK-365-039](#bank-365-039)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [119 Mathematics](../119_mathematics/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [120 Logic & Critical Thinking](../120_logic_critical_thinking/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [121 Statistics & Data](../121_statistics_data/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [364 Geometry](../364_geometry/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [366 Infinity](../366_infinity/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/365_number_theory/NICHE_365_number_theory.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
