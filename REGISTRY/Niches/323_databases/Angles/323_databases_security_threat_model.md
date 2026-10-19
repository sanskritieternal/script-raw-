# 323_databases_security_threat_model: Databases — Who Can Read a Record?

> Subject category: Computing_Software
> CAT: ../CAT_323_databases.md
> NICHE: ../NICHE_323_databases.md

This angle supplies Q3 only. All other defaults come from the niche CAT file.

## Q3: Primary Story Angle
**Default:** Who Can Read a Record?

## Editorial scope

**Focus / example question:** Which identities, services, backups, and operators can access data?

**Coverage:** Define privileges, encryption endpoints, logs, and retention.

**Evidence to seek:** database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems

**Limits:** Name engine, version, isolation settings, schema, and workload. Do not generalize one engine's guarantees or expose production records.

Before Phase 1, narrow this guidance to a specific case, source or work, and the relevant place, population, version or period. Record that choice in the episode's story question and research summary.
