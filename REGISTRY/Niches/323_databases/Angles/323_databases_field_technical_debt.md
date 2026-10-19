# 323_databases_field_technical_debt: Databases — A Schema That Cannot Evolve

> Subject category: Computing_Software
> CAT: ../CAT_323_databases.md
> NICHE: ../NICHE_323_databases.md

This angle supplies Q3 only. All other defaults come from the niche CAT file.

## Q3: Primary Story Angle
**Default:** A Schema That Cannot Evolve

## Editorial scope

**Focus / example question:** Which undocumented dependencies make a data change risky?

**Coverage:** Trace queries, clients, ownership, backfills, and migration path.

**Evidence to seek:** database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems

**Limits:** Name engine, version, isolation settings, schema, and workload. Do not generalize one engine's guarantees or expose production records.

Before Phase 1, narrow this guidance to a specific case, source or work, and the relevant place, population, version or period. Record that choice in the episode's story question and research summary.
