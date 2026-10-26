# 061 Software & Programming: Detailed Topic-Bank Draft

**9 categories · 40 individually authored episode proposals.**

Individually authored episode questions and coverage boundaries for Software & Programming. The subject progression is organized by concrete content rather than a topic-by-angle multiplication.

[All-niche progress](../DEPTH_COMPLETION_STATUS.md) · [All-niche index](../ALL_NICHE_TOPIC_BANKS.md) · [Editable bank](./IN_DEPTH_TOPIC_BANK.json)

Every question below has its own coverage boundary. All remain proposed; sources and current niche angle scopes have not been verified. Learning levels organize documentary research rather than physical difficulty. The older initial proposals remain in the JSON's prior_initial_map archive and are not counted again.

## 01. Programs, data and execution

**Level:** foundation. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-013 | What changes between writing source code and running a program? | Trace a small compiled example and an interpreted example through parsing, execution and errors; use versioned language documentation rather than claiming every runtime follows one pipeline. |
| BANK-061-014 | Why can two variables appear to contain the same object? | Use an explicit mutable-list example to distinguish identity, equality, references and copying; show the before-and-after state without generalizing one language's rules. |
| BANK-061-015 | How do types constrain the values a program can represent? | Compare a price, an optional username and a date in a named language; separate compile-time checks, runtime validation and business meaning. |
| BANK-061-016 | When does floating-point arithmetic change a seemingly simple calculation? | Investigate binary representation, rounding and comparison using documented numeric behavior; contrast decimal money representations without prescribing a universal numeric type. |

## 02. Decomposition and interfaces

**Level:** foundation. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-017 | How can a long script be divided into functions with testable responsibilities? | Refactor an original file-import example around parsing, validation and output; discuss explicit inputs and side effects instead of equating short functions with good design. |
| BANK-061-018 | What makes an interface stable while its implementation changes? | Compare two implementations behind a documented contract; inspect preconditions, returned errors and observable behavior rather than only matching method names. |
| BANK-061-019 | When does object composition clarify a design better than inheritance? | Use a bounded notification example with replaceable delivery components; examine substitutability and dependencies without declaring one paradigm universally superior. |
| BANK-061-020 | How should a command-line tool communicate failure to another program? | Separate exit status, standard output, standard error and structured messages in a harmless local example; consult the target platform's conventions. |

## 03. Algorithms and data structures

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-021 | Why can choosing a hash table change a lookup-heavy program? | Compare arrays, sorted collections and hashing on an explicit workload; include memory use, key equality and worst-case assumptions rather than only average timing. |
| BANK-061-022 | How do stacks and queues solve different ordering problems? | Model undo history and a work queue with original examples; trace operations and boundaries before discussing concurrency or production infrastructure. |
| BANK-061-023 | What does a complexity estimate reveal that a single benchmark cannot? | Compare input growth, operation counts and measured runtime for two search methods; identify constant factors and implementation effects separately. |
| BANK-061-024 | How can a graph model dependencies in a build system? | Represent files and prerequisites, trace topological ordering and detect a cycle; exclude unsupported claims about a particular build tool's internals. |
| BANK-061-025 | When should a program stream data rather than load everything into memory? | Use a generated log file to compare memory, latency and error recovery; state file size and buffering assumptions before extending to network streams. |

## 04. State, concurrency and asynchronous work

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-026 | Why does asynchronous execution not necessarily mean parallel computation? | Contrast waiting for independent I/O with CPU-bound work using runtime diagrams and controlled examples; verify the chosen language's scheduling model. |
| BANK-061-027 | How can two correct-looking updates produce a lost database change? | Trace an interleaving against an invented counter and compare transactions or version checks; keep the demonstration on a local test database. |
| BANK-061-028 | What does idempotency change when a request is retried? | Follow a simulated order submission with duplicate delivery and an idempotency key; separate transport retries from a guarantee of exactly-once processing. |
| BANK-061-029 | Why can cancellation fail to stop an entire asynchronous operation? | Inspect propagation, resource cleanup and partial effects in one runtime; distinguish a request to cancel from proof that every external side effect was reversed. |

## 05. Web services and data storage

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-030 | How does a browser action become a server request and a database query? | Trace an original read-only web example across DNS, HTTP, routing and storage; keep protocol roles distinct and record actual product versions. |
| BANK-061-031 | What belongs in a relational schema rather than application-only validation? | Model customers and orders with keys, constraints and nullability; compare rejected records and migration costs without asserting that constraints replace all validation. |
| BANK-061-032 | When does a database index improve reads but complicate writes? | Inspect query plans, selectivity and write overhead on a reproducible sample; avoid universal tuning recipes based on one table. |
| BANK-061-033 | How should an API evolve without silently breaking older clients? | Compare additive fields, removed fields, pagination and error shapes against a declared contract; include compatibility tests and deprecation evidence. |
| BANK-061-034 | What makes a cache return data that is fast but no longer appropriate? | Follow invalidation, expiration and read-after-write expectations in one bounded application; distinguish stale content tolerances from correctness requirements. |

## 06. Testing, debugging and observability

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-035 | How can a minimal reproducible example turn an intermittent bug into a clear question? | Reduce an original failure while preserving triggering inputs and environment; document what was removed and avoid exposing real user data. |
| BANK-061-036 | What should a unit test prove beyond repeating the implementation? | Compare boundary behavior, an independent oracle and a misleading test that mirrors the code; use observable requirements rather than implementation trivia. |
| BANK-061-037 | When can integration tests catch failures that mocks conceal? | Use an isolated service-and-database example with a schema mismatch; discuss test data, cleanup and reliability without requiring production access. |
| BANK-061-038 | How do logs, metrics and traces answer different debugging questions? | Follow one failed request across timestamped events, aggregate error rates and spans; include correlation and redaction rather than logging all payloads. |
| BANK-061-039 | Why can a benchmark become faster while the user experience gets worse? | Contrast a microbenchmark with end-to-end latency, warm-up, tail behavior and workload mix; label synthetic measurements and their limitations. |

## 07. Security and dependency hygiene

**Level:** advanced. **Evidence direction:** Inspect the actual product version, official documentation, terms and privacy policies. Test claims under stated conditions and distinguish account permissions, data retention, measured functionality and marketing.

**Source types to locate:** official versioned documentation and release notes; dated privacy policies and service terms; reproducible product tests and original validation reports. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-040 | How can a developer review permissions before adding a dependency? | Inspect official package metadata, requested privileges, maintenance history and a pinned version in a disposable environment; avoid treating popularity as proof of safety. |
| BANK-061-041 | What distinguishes validating input from encoding output safely? | Compare a constrained form field with rendering untrusted text using a defensive local example; consult framework guidance and omit exploit deployment instructions. |
| BANK-061-042 | Why should application secrets stay outside source control and logs? | Map configuration, deployment and rotation using placeholder credentials; include accidental exposure response from official guidance without accessing actual secrets. |
| BANK-061-043 | What does a software bill of materials reveal and leave unresolved? | Examine dependency identity, versions, transitive components and known-vulnerability matching; distinguish inventory from a completed security audit. |

## 08. Delivery and maintenance

**Level:** advanced. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-044 | How can a database migration be made reviewable before release? | Compare expand-and-contract changes, backups, compatibility and rollback limits on a local schema; require a tested recovery plan rather than promising reversible migrations. |
| BANK-061-045 | What does a continuous-integration pipeline need to reproduce a build? | Inspect dependency locks, toolchain versions, test fixtures and artifacts; distinguish a passing pipeline from evidence of runtime correctness. |
| BANK-061-046 | Why can a feature flag outlive the experiment it was created for? | Trace ownership, default behavior, exposure rules and removal in an invented rollout; include technical debt and auditability without naming real users. |
| BANK-061-047 | How should a team investigate a regression introduced several commits ago? | Combine a reproducible failing case, revision bisection and change review; note nondeterministic-test limits and preserve unrelated local work. |
| BANK-061-048 | What makes a technical debt decision visible rather than merely postponed? | Describe the affected behavior, cost of delay, owner and revisit trigger for one bounded shortcut; avoid equating all old code with debt. |

## 09. Programming ecosystems and learning paths

**Level:** advanced. **Evidence direction:** Define the rival claims and their evidence standards. Compare sources on equal terms, separate empirical findings from values or interpretations and do not imply that all positions have equal evidential support.

**Source types to locate:** the original sources behind the compared claims; explicit definitions and measurement methods; independent critiques with traceable evidence. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-061-049 | How do functional and imperative styles handle the same data transformation? | Compare transparent original implementations for state, composition and error handling; keep language features separate from broad paradigm claims. |
| BANK-061-050 | What changes when a script becomes software maintained by several people? | Follow packaging, review, documentation, compatibility and incident ownership; use a staged original project rather than implying enterprise infrastructure is always necessary. |
| BANK-061-051 | How should a developer evaluate generated code before relying on it? | Inspect requirements, boundary cases, dependency provenance and tests on a harmless example; distinguish plausible syntax from verified behavior and rights clearance. |
| BANK-061-052 | When is rewriting a legacy application riskier than changing it incrementally? | Map hidden requirements, interfaces, migration cutovers and available tests in a documented or explicitly invented case; do not infer business success from code age. |

## Coverage limits and next step

This is an expanded topic-bank draft, not exhaustive scholarship or a researched episode package. Each question has an individually written boundary. Source access, claim verification, current angle-scope review and publication approval remain pending. Add new branches and cases when they fill a real gap; no numeric topic cap applies.

Select an exact case, edition, population, jurisdiction or product version, inspect sources and refine the question before using the existing registry idea/depth planning workflow. These BANK IDs are catalog identities, not approved IDEA IDs. Existing Q1-Q42 defaults, production queues and approval gates are unchanged.

## Related niche homes

- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [321 Satellite Internet](../321_satellite_internet/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
