# 061 — Software & Programming: main topic bank

Updated: 2026-10-24 · **63 active BANK proposals · 5 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Programs, data and execution](#catalog-061-d01) → [Decomposition and interfaces](#catalog-061-d02).
- **Intermediate:** [Algorithms and data structures](#catalog-061-d03) → [State, concurrency and asynchronous work](#catalog-061-d04) → [Web services and data storage](#catalog-061-d05) → [Testing, debugging and observability](#catalog-061-d06) → [Reviewable changes](#catalog-061-r02).
- **Advanced:** [Security and dependency hygiene](#catalog-061-d07) → [Delivery and maintenance](#catalog-061-d08) → [Programming ecosystems and learning paths](#catalog-061-d09) → [Representation across systems](#catalog-061-r01).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Execution, design and computational structures](#domain-061-g01) | 13 | 5 | 0 |
| [State, services and test evidence](#domain-061-g02) | 0 | 18 | 0 |
| [Security, delivery and learning paths](#domain-061-g03) | 0 | 0 | 22 |
| [Programming boundaries](#domain-061-10) | 0 | 0 | 4 |
| [Maintained software](#domain-061-11) | 0 | 1 | 0 |

<a id="domain-061-g01"></a>
## Category: Execution, design and computational structures

<a id="catalog-061-d01"></a>
### Programs, data and execution

Subcategory `CATALOG-061-D01` · foundation.

<a id="bank-061-013"></a>
#### BANK-061-013 — What changes between writing source code and running a program?

**Individual coverage scope:** Trace a small compiled example and an interpreted example through parsing, execution and errors; use versioned language documentation rather than claiming every runtime follows one pipeline.

<a id="bank-061-014"></a>
#### BANK-061-014 — Why can two variables appear to contain the same object?

**Individual coverage scope:** Use an explicit mutable-list example to distinguish identity, equality, references and copying; show the before-and-after state without generalizing one language's rules.

<a id="bank-061-015"></a>
#### BANK-061-015 — How do types constrain the values a program can represent?

**Individual coverage scope:** Compare a price, an optional username and a date in a named language; separate compile-time checks, runtime validation and business meaning.

<a id="bank-061-016"></a>
#### BANK-061-016 — When does floating-point arithmetic change a seemingly simple calculation?

**Individual coverage scope:** Investigate binary representation, rounding and comparison using documented numeric behavior; contrast decimal money representations without prescribing a universal numeric type.

<a id="bank-061-058"></a>
#### BANK-061-058 — How can a nullable reference break a program even when every value has a declared type?

**Individual coverage scope:** Trace one null dereference through API contract, static checks and runtime behavior; do not infer a global monetary cost from an anecdotal estimate.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-060"></a>
#### BANK-061-060 — How do stack frames and dynamic allocation affect object lifetime in a specific program?

**Individual coverage scope:** Trace one compiled example with toolchain and platform named; avoid claiming every language or object uses a universal stack-versus-heap rule.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-068"></a>
#### BANK-061-068 — Which transformations can a compiler make without changing a program?s observable behavior?

**Individual coverage scope:** Use a named language, compiler release and optimization level to inspect generated code; distinguish permitted transformations from benchmark folklore.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="catalog-061-d02"></a>
### Decomposition and interfaces

Subcategory `CATALOG-061-D02` · foundation.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-017"></a>
#### BANK-061-017 — How can a long script be divided into functions with testable responsibilities?

**Individual coverage scope:** Refactor an original file-import example around parsing, validation and output; discuss explicit inputs and side effects instead of equating short functions with good design.

<a id="bank-061-018"></a>
#### BANK-061-018 — What makes an interface stable while its implementation changes?

**Individual coverage scope:** Compare two implementations behind a documented contract; inspect preconditions, returned errors and observable behavior rather than only matching method names.

<a id="bank-061-019"></a>
#### BANK-061-019 — When does object composition clarify a design better than inheritance?

**Individual coverage scope:** Use a bounded notification example with replaceable delivery components; examine substitutability and dependencies without declaring one paradigm universally superior.

<a id="bank-061-020"></a>
#### BANK-061-020 — How should a command-line tool communicate failure to another program?

**Individual coverage scope:** Separate exit status, standard output, standard error and structured messages in a harmless local example; consult the target platform's conventions.

<a id="bank-061-067"></a>
#### BANK-061-067 — When should a service boundary become an in-process module instead?

**Individual coverage scope:** Compare one system?s latency, deployment, failure and ownership costs at a named scale; do not infer a universal move from microservices to monoliths.

**Neighboring scope:** [BANK-061-074](#bank-061-074) — Service-boundary trade-offs are general; Prime Video monitoring is one reported architecture change.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-074"></a>
#### BANK-061-074 — What did Prime Video?s video-quality monitoring team actually change in its architecture?

**Individual coverage scope:** Trace the team?s published 2023 design, bottleneck and reported cost result for that service; do not generalize it to all of Prime Video or all microservices.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="catalog-061-d03"></a>
### Algorithms and data structures

Subcategory `CATALOG-061-D03` · intermediate.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-021"></a>
#### BANK-061-021 — Why can choosing a hash table change a lookup-heavy program?

**Individual coverage scope:** Compare arrays, sorted collections and hashing on an explicit workload; include memory use, key equality and worst-case assumptions rather than only average timing.

<a id="bank-061-022"></a>
#### BANK-061-022 — How do stacks and queues solve different ordering problems?

**Individual coverage scope:** Model undo history and a work queue with original examples; trace operations and boundaries before discussing concurrency or production infrastructure.

<a id="bank-061-023"></a>
#### BANK-061-023 — What does a complexity estimate reveal that a single benchmark cannot?

**Individual coverage scope:** Compare input growth, operation counts and measured runtime for two search methods; identify constant factors and implementation effects separately.

<a id="bank-061-024"></a>
#### BANK-061-024 — How can a graph model dependencies in a build system?

**Individual coverage scope:** Represent files and prerequisites, trace topological ordering and detect a cycle; exclude unsupported claims about a particular build tool's internals.

<a id="bank-061-025"></a>
#### BANK-061-025 — When should a program stream data rather than load everything into memory?

**Individual coverage scope:** Use a generated log file to compare memory, latency and error recovery; state file size and buffering assumptions before extending to network streams.


<a id="domain-061-g02"></a>
## Category: State, services and test evidence

<a id="catalog-061-d04"></a>
### State, concurrency and asynchronous work

Subcategory `CATALOG-061-D04` · intermediate.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-026"></a>
#### BANK-061-026 — Why does asynchronous execution not necessarily mean parallel computation?

**Individual coverage scope:** Contrast waiting for independent I/O with CPU-bound work using runtime diagrams and controlled examples; verify the chosen language's scheduling model.

<a id="bank-061-027"></a>
#### BANK-061-027 — How can two correct-looking updates produce a lost database change?

**Individual coverage scope:** Trace an interleaving against an invented counter and compare transactions or version checks; keep the demonstration on a local test database.

<a id="bank-061-028"></a>
#### BANK-061-028 — What does idempotency change when a request is retried?

**Individual coverage scope:** Follow a simulated order submission with duplicate delivery and an idempotency key; separate transport retries from a guarantee of exactly-once processing.

<a id="bank-061-029"></a>
#### BANK-061-029 — Why can cancellation fail to stop an entire asynchronous operation?

**Individual coverage scope:** Inspect propagation, resource cleanup and partial effects in one runtime; distinguish a request to cancel from proof that every external side effect was reversed.

<a id="bank-061-065"></a>
#### BANK-061-065 — What does the CAP result actually say about a distributed service during a network partition?

**Individual coverage scope:** Walk one partitioned replica example with consistency and availability definitions; avoid treating the result as a three-way product score.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-066"></a>
#### BANK-061-066 — How can a race condition differ from a deadlock in the same concurrent program?

**Individual coverage scope:** Build two minimal traces and show the scheduling and locking assumptions; distinguish incorrect interleaving from lack of progress.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-073"></a>
#### BANK-061-073 — How did Python?s GIL behavior change across specific CPython releases?

**Individual coverage scope:** Compare documented thread execution and the optional free-threaded build in a named CPython release; distinguish interpreter behavior from all Python implementations.

**Neighboring scope:** [BANK-061-026](#bank-061-026) — The GIL is CPython runtime behavior; asynchronous execution and parallel computation remain a general distinction.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="catalog-061-d05"></a>
### Web services and data storage

Subcategory `CATALOG-061-D05` · intermediate.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-030"></a>
#### BANK-061-030 — How does a browser action become a server request and a database query?

**Individual coverage scope:** Trace an original read-only web example across DNS, HTTP, routing and storage; keep protocol roles distinct and record actual product versions.

<a id="bank-061-031"></a>
#### BANK-061-031 — What belongs in a relational schema rather than application-only validation?

**Individual coverage scope:** Model customers and orders with keys, constraints and nullability; compare rejected records and migration costs without asserting that constraints replace all validation.

<a id="bank-061-032"></a>
#### BANK-061-032 — When does a database index improve reads but complicate writes?

**Individual coverage scope:** Inspect query plans, selectivity and write overhead on a reproducible sample; avoid universal tuning recipes based on one table.

<a id="bank-061-033"></a>
#### BANK-061-033 — How should an API evolve without silently breaking older clients?

**Individual coverage scope:** Compare additive fields, removed fields, pagination and error shapes against a declared contract; include compatibility tests and deprecation evidence.

<a id="bank-061-034"></a>
#### BANK-061-034 — What makes a cache return data that is fast but no longer appropriate?

**Individual coverage scope:** Follow invalidation, expiration and read-after-write expectations in one bounded application; distinguish stale content tolerances from correctness requirements.

<a id="catalog-061-d06"></a>
### Testing, debugging and observability

Subcategory `CATALOG-061-D06` · intermediate.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-035"></a>
#### BANK-061-035 — How can a minimal reproducible example turn an intermittent bug into a clear question?

**Individual coverage scope:** Reduce an original failure while preserving triggering inputs and environment; document what was removed and avoid exposing real user data.

<a id="bank-061-036"></a>
#### BANK-061-036 — What should a unit test prove beyond repeating the implementation?

**Individual coverage scope:** Compare boundary behavior, an independent oracle and a misleading test that mirrors the code; use observable requirements rather than implementation trivia.

<a id="bank-061-037"></a>
#### BANK-061-037 — When can integration tests catch failures that mocks conceal?

**Individual coverage scope:** Use an isolated service-and-database example with a schema mismatch; discuss test data, cleanup and reliability without requiring production access.

<a id="bank-061-038"></a>
#### BANK-061-038 — How do logs, metrics and traces answer different debugging questions?

**Individual coverage scope:** Follow one failed request across timestamped events, aggregate error rates and spans; include correlation and redaction rather than logging all payloads.

<a id="bank-061-039"></a>
#### BANK-061-039 — Why can a benchmark become faster while the user experience gets worse?

**Individual coverage scope:** Contrast a microbenchmark with end-to-end latency, warm-up, tail behavior and workload mix; label synthetic measurements and their limitations.

<a id="bank-061-071"></a>
#### BANK-061-071 — What can formal verification prove about a specified program, and what remains outside the proof?

**Individual coverage scope:** Examine one verified component, assumptions and property statement; reject claims that mathematics makes all crashes impossible.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-061-g03"></a>
## Category: Security, delivery and learning paths

<a id="catalog-061-d07"></a>
### Security and dependency hygiene

Subcategory `CATALOG-061-D07` · advanced.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-040"></a>
#### BANK-061-040 — How can a developer review permissions before adding a dependency?

**Individual coverage scope:** Inspect official package metadata, requested privileges, maintenance history and a pinned version in a disposable environment; avoid treating popularity as proof of safety.

<a id="bank-061-041"></a>
#### BANK-061-041 — What distinguishes validating input from encoding output safely?

**Individual coverage scope:** Compare a constrained form field with rendering untrusted text using a defensive local example; consult framework guidance and omit exploit deployment instructions.

<a id="bank-061-042"></a>
#### BANK-061-042 — Why should application secrets stay outside source control and logs?

**Individual coverage scope:** Map configuration, deployment and rotation using placeholder credentials; include accidental exposure response from official guidance without accessing actual secrets.

<a id="bank-061-043"></a>
#### BANK-061-043 — What does a software bill of materials reveal and leave unresolved?

**Individual coverage scope:** Examine dependency identity, versions, transitive components and known-vulnerability matching; distinguish inventory from a completed security audit.

<a id="bank-061-064"></a>
#### BANK-061-064 — How did Heartbleed expose a missing length check in affected OpenSSL releases?

**Individual coverage scope:** Trace CVE-2014-0160, heartbeat request handling, affected versions and the 1.0.1g fix using OpenSSL?s advisory; distinguish possible exposure from proven theft.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTE_HEARTBLEED.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-061-041](#bank-061-041) — Heartbleed is a specific OpenSSL bounds-check case; the general question separates input validation from output encoding.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-069"></a>
#### BANK-061-069 — Which memory errors does safe Rust prevent, and which risks remain?

**Individual coverage scope:** Use a named stable Rust edition and documented unsafe boundary; compare compiler-checked ownership with logic, concurrency and dependency risks.

**Neighboring scope:** [BANK-061-075](#bank-061-075) — Rust language guarantees are one implementation subject; the 2024 report is a policy recommendation across technologies.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-075"></a>
#### BANK-061-075 — What did the 2024 US software-security report recommend about memory-safe languages?

**Individual coverage scope:** Read the Office of the National Cyber Director report in context, including exceptions and complementary methods; distinguish a recommendation from a legal ban on C or C++.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTE_MEMORY_SAFETY_REPORT.md). This does not change proposal or production status.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="catalog-061-d08"></a>
### Delivery and maintenance

Subcategory `CATALOG-061-D08` · advanced.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-044"></a>
#### BANK-061-044 — How can a database migration be made reviewable before release?

**Individual coverage scope:** Compare expand-and-contract changes, backups, compatibility and rollback limits on a local schema; require a tested recovery plan rather than promising reversible migrations.

<a id="bank-061-045"></a>
#### BANK-061-045 — What does a continuous-integration pipeline need to reproduce a build?

**Individual coverage scope:** Inspect dependency locks, toolchain versions, test fixtures and artifacts; distinguish a passing pipeline from evidence of runtime correctness.

<a id="bank-061-046"></a>
#### BANK-061-046 — Why can a feature flag outlive the experiment it was created for?

**Individual coverage scope:** Trace ownership, default behavior, exposure rules and removal in an invented rollout; include technical debt and auditability without naming real users.

<a id="bank-061-047"></a>
#### BANK-061-047 — How should a team investigate a regression introduced several commits ago?

**Individual coverage scope:** Combine a reproducible failing case, revision bisection and change review; note nondeterministic-test limits and preserve unrelated local work.

<a id="bank-061-048"></a>
#### BANK-061-048 — What makes a technical debt decision visible rather than merely postponed?

**Individual coverage scope:** Describe the affected behavior, cost of delay, owner and revisit trigger for one bounded shortcut; avoid equating all old code with debt.

<a id="bank-061-061"></a>
#### BANK-061-061 — How did Y2K remediation identify and test two-digit-year assumptions?

**Individual coverage scope:** Use a documented system migration, test plan and post-2000 outcome; avoid equating avoided failures with evidence that the risk was imaginary.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-062"></a>
#### BANK-061-062 — Why did Git?s early design prioritize distributed history and content identity?

**Individual coverage scope:** Compare initial Git documentation and dated releases with the Linux kernel collaboration problem; avoid a precise creation-time legend.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-072"></a>
#### BANK-061-072 — How did the left-pad package removal propagate through npm dependency graphs?

**Individual coverage scope:** Use dated npm and package records to trace affected builds, restoration and dependency resolution; separate documented disruption from claims the entire internet failed.

**Neighboring scope:** [BANK-514-033](../514_open-source_software/IN_DEPTH_TOPIC_BANK.md#bank-514-033) — Left-pad is a dated package incident; the open-source bank asks how to respond when a maintainer stops responding.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="catalog-061-d09"></a>
### Programming ecosystems and learning paths

Subcategory `CATALOG-061-D09` · advanced.

Prerequisites: [CATALOG-061-D01](#catalog-061-d01).

<a id="bank-061-049"></a>
#### BANK-061-049 — How do functional and imperative styles handle the same data transformation?

**Individual coverage scope:** Compare transparent original implementations for state, composition and error handling; keep language features separate from broad paradigm claims.

<a id="bank-061-050"></a>
#### BANK-061-050 — What changes when a script becomes software maintained by several people?

**Individual coverage scope:** Follow packaging, review, documentation, compatibility and incident ownership; use a staged original project rather than implying enterprise infrastructure is always necessary.

<a id="bank-061-051"></a>
#### BANK-061-051 — How should a developer evaluate generated code before relying on it?

**Individual coverage scope:** Inspect requirements, boundary cases, dependency provenance and tests on a harmless example; distinguish plausible syntax from verified behavior and rights clearance.

<a id="bank-061-052"></a>
#### BANK-061-052 — When is rewriting a legacy application riskier than changing it incrementally?

**Individual coverage scope:** Map hidden requirements, interfaces, migration cutovers and available tests in a documented or explicitly invented case; do not infer business success from code age.

<a id="bank-061-059"></a>
#### BANK-061-059 — Which design choices made C portable while leaving memory management to programmers?

**Individual coverage scope:** Compare a dated C standard and implementation examples with Unix-era constraints; distinguish language design from present adoption forecasts.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-063"></a>
#### BANK-061-063 — What does a Unix-style composable command gain and lose when data formats vary?

**Individual coverage scope:** Use a reproducible pipeline and documented command interfaces; distinguish the historical design principle from a claim that it conquered all software.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-061-070"></a>
#### BANK-061-070 — What changes when a browser runs a WebAssembly module beside JavaScript?

**Individual coverage scope:** Use a named browser/runtime and Wasm core specification; compare sandbox, host calls, startup and measured workload rather than assuming native speed.

**Neighboring scope:** [BANK-318-030](../318_internet/IN_DEPTH_TOPIC_BANK.md#bank-318-030) — Wasm runtime and host calls are programming mechanics; the internet bank covers network architecture.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-061-10"></a>
## Category: Programming boundaries

<a id="catalog-061-r01"></a>
### Representation across systems

Subcategory `CATALOG-061-R01` · advanced.

<a id="bank-061-053"></a>
#### BANK-061-053 — Why can a serialized object lose meaning when another program reads it?

**Individual coverage scope:** Compare schema, numeric precision, missing values, encoding and version compatibility with a small JSON example.

<a id="bank-061-054"></a>
#### BANK-061-054 — How can time zones turn a correct-looking schedule into the wrong instant?

**Individual coverage scope:** Separate local dates, offsets, daylight transitions, recurring events and stored instants using fictional appointments.

<a id="bank-061-055"></a>
#### BANK-061-055 — Why can two identical-looking strings fail an equality check?

**Individual coverage scope:** Trace Unicode code points, normalization, combining marks and comparison rules in a named language.

<a id="bank-061-056"></a>
#### BANK-061-056 — What can a garbage collector reclaim and what can still leak?

**Individual coverage scope:** Compare reachability, retained references, external resources and profiling; distinguish memory management from closing every resource.


<a id="domain-061-11"></a>
## Category: Maintained software

<a id="catalog-061-r02"></a>
### Reviewable changes

Subcategory `CATALOG-061-R02` · intermediate.

<a id="bank-061-057"></a>
#### BANK-061-057 — What does a code review need to explain beyond whether a patch compiles?

**Individual coverage scope:** Trace the intended behavior change, diff, assumptions, interfaces, meaningful tests, compatibility and reviewer questions through a benign fictional patch; distinguish review from proof of security or correctness.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

### pending_topics/0 — The Billion-Dollar Null Pointer Bug: How One Missing Check Cost Tony Hoare and the World Billions

**Original question:** Why did computer scientist Tony Hoare apologize in 2009 for inventing the 'null pointer' in 1965, and how has it caused millions of server crashes and security breaches?

**Original planning scope:** Null references vs memory pointers, segmentation faults (SIGSEGV), Rust's Option<T> and Kotlin null safety, the economic cost of preventable runtime crashes.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-058](#bank-061-058).

### pending_topics/1 — The C Programming Language: Dennis Ritchie and the Bedrock of Modern Computing

**Original question:** How did Dennis Ritchie create a language in 1972 that remains the untouchable foundation of Linux, Windows, macOS, and every game engine 50 years later?

**Original planning scope:** Bell Labs Unix rewrite, pointer arithmetic, manual memory management (malloc/free), bridging high-level abstraction with bare-metal machine performance.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-059](#bank-061-059).

### pending_topics/2 — Stack vs Heap: What Actually Happens to Your Computer's RAM When Code Runs

**Original question:** Why is stack memory blazing fast but tiny, while heap memory is massive but prone to memory leaks, fragmentation, and pointer bugs?

**Original planning scope:** LIFO stack pointer adjustments, dynamic heap allocation algorithms, memory alignment and fragmentation, stack overflow crashes and buffer overflows.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-060](#bank-061-060).

### pending_topics/3 — The Y2K Bug: The 1999 Panic That Was Only Solved by Millions of Lines of Overtime

**Original question:** Was Y2K an overhyped media hoax, or did society avoid catastrophic infrastructure collapse because programmers quietly repaired billions of lines of COBOL code?

**Original planning scope:** Early memory storage constraints (saving two bytes per date), mainframe COBOL legacy code, $300 billion global remediation effort, the upcoming 2038 Unix epoch problem.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-061](#bank-061-061).

### pending_topics/4 — Garbage Collection: How Java and Python Clean Up Your Mess Behind the Scenes

**Original question:** How does your computer identify dead memory objects without stopping code execution, and why do high-frequency trading platforms ban garbage-collected languages?

**Original planning scope:** Reference counting and circular reference traps, Mark-and-Sweep algorithms, generational hypothesis (Young vs Old generation), 'Stop-the-World' latency pauses.

**Editorial disposition:** existing_scope. Garbage collection and remaining leaks already have a bounded question.

**Scoped proposals:** [BANK-061-056](#bank-061-056).

### pending_topics/5 — Linus Torvalds and Git: How a 10-Day Rage Project Changed Software Forever

**Original question:** How did the creator of Linux write the core of the world's most dominant version control system in just two weeks after being locked out of BitKeeper?

**Original planning scope:** Directed Acyclic Graphs (DAG), content-addressable storage using SHA-1 object hashes, decentralized branching vs centralized SVN, why Git's architecture is pure math.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-062](#bank-061-062).

### pending_topics/6 — Object-Oriented Programming vs Functional Programming: The 40-Year Holy War

**Original question:** Why did Alan Kay say 'I made up the term object-oriented, and I can tell you I did not have C++ in mind', and why are modern languages moving to functional immutability?

**Original planning scope:** Inheritance vs composition, mutable state bugs in concurrency, pure functions and side-effect elimination, modern hybrid language synthesis (Rust, Swift, TypeScript).

**Editorial disposition:** existing_scope. Paradigm comparison and composition already have scoped questions; culture-war framing adds no distinct program.

**Scoped proposals:** [BANK-061-049](#bank-061-049), [BANK-061-019](#bank-061-019).

### pending_topics/7 — The Unix Philosophy: Why Doing One Thing and Doing It Well Conquered the World

**Original question:** How did Doug McIlroy's invention of the simple text pipe (|) allow tiny command-line programs to chain together into infinitely powerful data pipelines?

**Original planning scope:** Write programs that do one thing well, write programs to work together, write programs to handle text streams, 'everything is a file' abstraction in POSIX.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-063](#bank-061-063).

### pending_topics/8 — The Heartbleed Bug: How a Single Missing Bounds Check Compromised the Entire Internet

**Original question:** How did a missing payload length check in OpenSSL's TLS heartbeat extension allow anonymous hackers to leak passwords and encryption keys from two-thirds of the web?

**Original planning scope:** Buffer over-read mechanics, leaking 64KB of server memory per heartbeat, the fragility of global internet infrastructure maintained by unpaid volunteer coders.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-064](#bank-061-064).

### pending_topics/9 — The CAP Theorem: Why You Can Never Have a Perfect Distributed Database

**Original question:** Why does physical network latency force every distributed database on Earth (PostgreSQL, Cassandra, DynamoDB) to sacrifice either immediate consistency or availability?

**Original planning scope:** Eric Brewer's 2000 proof, CP vs AP architectures, network partitions (split-brain scenarios), eventual consistency models and Amazon's high-availability shopping cart.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-065](#bank-061-065).

### pending_topics/10 — Race Conditions and Deadlocks: The Nightmare of Multi-Threaded Concurrency

**Original question:** What happened when the Therac-25 radiation therapy machine gave patients lethal radiation overdoses because two software tasks modified the same variable simultaneously?

**Original planning scope:** Therac-25 fatal medical bug, Dining Philosophers problem, Mutexes, semaphores, and spinlocks, lock contention vs atomic compare-and-swap operations.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-066](#bank-061-066).

### pending_topics/11 — Microservices vs Monoliths: Why Tech Giants Are Rebuilding Their Monoliths

**Original question:** Why did Amazon Prime Video slash server costs by 90% by ditching serverless microservices and returning to a single monolithic application?

**Original planning scope:** Conway's Law (architecture mirrors communication structure), network serialization latency and JSON parsing overhead, distributed tracing headaches, modular monolith balance.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-067](#bank-061-067).

### pending_topics/12 — How Compilers Optimize Code: Turning Ugly Human Logic into Machine Art

**Original question:** How does an optimizing compiler (GCC/Clang) transform human source code through Abstract Syntax Trees and LLVM IR to produce assembly faster than hand-written machine code?

**Original planning scope:** Lexing and parsing tokens, Intermediate Representation (IR), dead-code elimination, constant folding, SIMD vectorization, and cache-conscious instruction scheduling.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-068](#bank-061-068).

### pending_topics/13 — Rust and Memory Safety: The Language That Solved C's Fatal Flaw Without Garbage Collection

**Original question:** How does Rust's compile-time Borrow Checker guarantee zero memory leaks and zero data races with zero runtime speed penalty?

**Original planning scope:** Ownership rules and lifetimes, eliminating use-after-free and double-free vulnerabilities, White House and NSA endorsements to deprecate C/C++, Linux kernel adoption.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-069](#bank-061-069).

### pending_topics/14 — WebAssembly (WASM): Running Native C++ and Rust in Web Browsers at Near-Native Speed

**Original question:** How does Figma run a full desktop-class graphics design engine inside Google Chrome, and will WASM replace Docker containers in the cloud?

**Original planning scope:** Stack-based virtual machine bytecodes, sandboxed memory linear array, Wasmtime and WASI (WebAssembly System Interface) edge serverless runtimes, Solomon Hykes Docker quote.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-070](#bank-061-070).

### pending_topics/15 — AI Pair Programming: How LLMs and Transformers Write Code and Where They Fail

**Original question:** Do Large Language Models understand software architecture, or are they stochastic pattern-matchers producing subtle security hallucinations?

**Original planning scope:** Attention mechanisms over code context windows, AST tokenization, hallucinated libraries and dependency confusion supply chain risks, the future role of software engineers.

**Editorial disposition:** existing_scope. Generated-code evaluation already has a professional and learner-specific question.

**Scoped proposals:** [BANK-061-051](#bank-061-051), [BANK-463-034](../463_coding_education/IN_DEPTH_TOPIC_BANK.md#bank-463-034).

### pending_topics/16 — Formal Verification: Writing Software That Is Mathematically Impossible to Crash

**Original question:** How did Australian computer scientists mathematically prove that the seL4 operating system microkernel contains zero buffer overflows, zero null pointer bugs, and can never crash?

**Original planning scope:** Interactive theorem provers (Coq, Isabelle/HOL), formal mathematical proofs of machine code, aerospace and nuclear control software, why full verification costs $500 per line.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-071](#bank-061-071).

### pending_topics/17 — The Left-Pad Incident: How 11 Lines of Code Broke the Global Internet in 2016

**Original question:** How did an angry developer unpublishing an 11-line open-source string-padding function break Babel, React, and build systems across Facebook, Netflix, and Spotify?

**Original planning scope:** NPM package registry dependency tree explosion, transitive dependencies, supply chain fragility, why modern web projects download 500 megabytes of node_modules.

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-072](#bank-061-072).

### pending_topics/18 — Clean Code vs Fast Code: Casey Muratori's Rebuttal to Uncle Bob

**Original question:** Does following object-oriented 'Clean Code' principles make software 15 times slower on modern hardware by thrashing CPU L1/L2 caches?

**Original planning scope:** Data-Oriented Design (DOD) vs Object-Oriented Design (OOD), polymorphic virtual function call overhead, CPU cache line spatial locality, Mike Acton's DoD manifesto.

**Editorial disposition:** existing_scope. Benchmark interpretation and visible technical-debt decisions already cover the trade-off without a personal debate.

**Scoped proposals:** [BANK-061-039](#bank-061-039), [BANK-061-048](#bank-061-048).

### pending_topics/19 — The Future of Programming in 2040: Will Anyone Write Source Code Manually?

**Original question:** Will traditional programming languages disappear as natural language specifications and AI verification systems compile intent directly into machine binaries?

**Original planning scope:** From punch cards to assembly to high-level languages to prompt specification, the enduring need for algorithmic thinking, system boundary architecture, and formal specification logic.

**Editorial disposition:** out_of_scope. The 2040 source-code forecast has no specified capability or testable time-series premise; retain it as a speculative archive pitch.

### trending_topics/0 — Why 11 Lines of Code Broke Facebook, Netflix, and the Entire Internet (Left-Pad)

**Editorial disposition:** merged_case. Same npm left-pad incident as pending 18; headline reach is unverified.

**Scoped proposals:** [BANK-061-072](#bank-061-072).

### trending_topics/1 — Why Is Python Slow? The Single Line of Code That Cripples Multi-Threading (The GIL)

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-073](#bank-061-073).

### trending_topics/2 — The $10 Billion Cloud Bill: Why Amazon Prime Video Ditched Microservices

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-074](#bank-061-074).

### trending_topics/3 — Why C is Still Undefeated 52 Years Later (And Never Dying)

**Editorial disposition:** merged_case. Same C design/history subject as pending 2; never-dying forecast is not adopted.

**Scoped proposals:** [BANK-061-059](#bank-061-059).

### trending_topics/4 — What Actually Happens When You Type google.com and Hit Enter?

**Editorial disposition:** existing_scope. The browser-to-server path already has a concrete request-and-database question; internet transport detail has a separate neighboring home.

**Scoped proposals:** [BANK-061-030](#bank-061-030).

### trending_topics/5 — Why the White House Warned Everyone to Stop Using C and C++

**Editorial disposition:** new_case. Distinct bounded programming or historical software question; title superlatives are not findings.

**Scoped proposals:** [BANK-061-075](#bank-061-075).

### trending_topics/6 — Will AI Actually Replace Software Engineers by 2030?

**Editorial disposition:** existing_scope. Evaluating generated code and model upgrades has existing questions; engineer-replacement timing is an unsupported forecast.

**Scoped proposals:** [BANK-061-051](#bank-061-051), [BANK-532-034](../532_large_language_model_systems/IN_DEPTH_TOPIC_BANK.md#bank-532-034).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-061-01"></a>
### Programming foundations

<a id="bank-061-001"></a>
- `BANK-061-001` — Variables and state changes → [BANK-061-014](#bank-061-014)
<a id="bank-061-002"></a>
- `BANK-061-002` — Functions and side effects → [BANK-061-017](#bank-061-017), [BANK-061-049](#bank-061-049)
<a id="bank-061-003"></a>
- `BANK-061-003` — Data structures and access patterns → [BANK-061-021](#bank-061-021), [BANK-061-022](#bank-061-022)
<a id="bank-061-004"></a>
- `BANK-061-004` — Algorithmic complexity and input size → [BANK-061-023](#bank-061-023)

<a id="catalog-061-02"></a>
### Software execution

<a id="bank-061-005"></a>
- `BANK-061-005` — Compilation versus interpretation → [BANK-061-013](#bank-061-013)
<a id="bank-061-006"></a>
- `BANK-061-006` — Memory allocation and lifetime → [BANK-061-056](#bank-061-056)
<a id="bank-061-007"></a>
- `BANK-061-007` — Concurrency and race conditions → [BANK-061-027](#bank-061-027)
<a id="bank-061-008"></a>
- `BANK-061-008` — Network calls and failure handling → [BANK-061-020](#bank-061-020), [BANK-061-028](#bank-061-028)

<a id="catalog-061-03"></a>
### Working practice

<a id="bank-061-009"></a>
- `BANK-061-009` — Debugging from reproducible cases → [BANK-061-035](#bank-061-035)
<a id="bank-061-010"></a>
- `BANK-061-010` — Version control and review → [BANK-061-057](#bank-061-057)
<a id="bank-061-011"></a>
- `BANK-061-011` — Testing behavior rather than implementation → [BANK-061-036](#bank-061-036), [BANK-061-037](#bank-061-037)
<a id="bank-061-012"></a>
- `BANK-061-012` — Dependencies and reproducible builds → [BANK-061-045](#bank-061-045)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [321 Satellite Internet](../321_satellite_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Further case and comparison depth:** Select distinct named cases, regional and language variants, overlooked participants, and contrary examples within Programs, data and execution, Decomposition and interfaces, Algorithms and data structures. Review actual scopes before adding an episode; these are coverage directions rather than a claim that present questions exhaust the niche.
- **Sources and readiness:** Inspect actual source access, dates, editions, versions, methods and competing evidence. No new source verification, research certification or production approval was performed.
- **Neighboring-niche boundary review:** Before producing an episode, compare related banks and assign one primary home. A lexical duplicate check does not establish semantic uniqueness across every pair.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/061_software_programming/NICHE_061_software_programming.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
