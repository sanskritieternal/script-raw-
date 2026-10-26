# Programming primary-source follow-up — 2026-10-24

## BANK-324-044 — PEP 238

- Primary source: Python Enhancement Proposal 238, *Changing the Division Operator*, created 11 March 2001, Python 2.2 target, final status: https://peps.python.org/pep-0238/
- The PEP defines classic versus true division, `//` for floor division, a `from __future__ import division` transition, and a planned Python 3 default. It explicitly cites backward compatibility as the reason for transition steps.
- Limit: this design document supports the language's proposed and accepted semantics; it does not measure how many projects adopted the future import or prove that all migrations succeeded. Anchor any before/after demonstration to named interpreter versions.

## BANK-324-045 — PEP 695

- Primary source: Python Enhancement Proposal 695, *Type Parameter Syntax*, created 15 June 2022, Python 3.12 target, final status: https://peps.python.org/pep-0695/
- The PEP specifies type-parameter syntax for generic classes/functions and a type-alias statement, including scoping and variance-inference provisions.
- Limit: the PEP is a specification and design rationale, not evidence that annotations enforce arbitrary values at runtime or that every type checker handles every edge case identically. Verify any implementation demo against the exact Python and checker versions used.

## Routing and overlap boundary

The archive's general programming-process pitches map to existing active questions. The two new questions isolate a named semantics migration and a named typing syntax decision. Existing BANK-324-043 remains retired because it duplicates BANK-061-026; no async task replacement is created. Neighboring software engineering bank 325 owns release and organizational process, while these cases focus language behavior and specification.
