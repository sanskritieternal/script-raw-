# Shared episode idea layer

Implemented 2026-10-18. Applies to the current 550-niche system without creating a bank for every niche or changing configuration Q1-Q42.

## Delivered

- REGISTRY/IDEA_BANK_SCHEMA.json: versioned bank/entry/source/status field structure.
- idea_bank.py: preview-first optional bank initialization/addition, stable ID allocation, validation, related-reference/duplicate checks and generated master index.
- REGISTRY/IDEA_BANK_GUIDE.md and IDEA_MASTER_LIST.md: documented lifecycle and current proposals, linked from the niche master list.
- create_project.py --idea-id: selected-niche readiness gate, derived angle/story question, conflict rejection and immutable creation-time snapshot with canonical hash.
- validate_project.py: snapshot field/hash/identity/story/angle checks that do not require a mutable live bank to match later.
- validate_repository.py and audit_repository.py: optional bank/index validation and the new behavioral test module.
- Root usage/agent/tool instructions and phase handoffs updated. CONFIG remains the production source; bank proposals are not verified research claims.

## Current content

Two concrete ideas are seeded: IDEA-501-0001, a proposed reading of the New York saliva-exposure evaluation; IDEA-531-0001, a proposed reading of a named workflow/agent architecture article. Both are proposed, with unverified source leads and explicit blocking gaps. No project, ready status, human approval or publication was created from them. No generic bulk idea population was performed.

## Verification

41 contract/workflow/idea tests passed. Tests cover malformed niche/angle/status/date fields, readiness constraints, preview/no-overwrite behavior, duplicate questions, related references, rejected proposed selection, conflict-free project routing, story conflicts and hash tampering. Tests use independent temporary fixtures rather than changing live idea readiness. A snapshot validates without its source bank, demonstrating frozen rather than live-link semantics. Existing direct project creation and production tests remain green.

The full repository audit result is recorded in STRUCTURAL_AUDIT.md and FILE_VERIFICATION.md. The original 550 niche identities and production review gates remain intact. Source access/feasibility and human review authenticity cannot be established by a JSON flag or an automated test.
