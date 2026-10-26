# Selected operator source note — databases

Inspected 2026-10-24 for `BANK-323-041`. This is a historical hosted-service postmortem, not a database recovery runbook.

- [GitLab, GitLab.com database incident timeline](https://about.gitlab.com/blog/gitlab-dot-com-database-incident/): contemporaneous operator account records 31 January 2017 replication trouble, accidental loss of primary-database data and backup/restore obstacles. It states repository and wiki data and self-managed instances were not affected by the data loss.
- [GitLab, 10 February 2017 postmortem](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/): reports prolonged GitLab.com outage and some unrecovered database changes; describes how available snapshots and storage speed constrained restoration. The account provides GitLab's estimate of affected items, not independently audited exact loss for every user.

Both GitLab pages were accessible. They are provider-authored accounts from 2017; later database versions and operational practices may differ. Do not reproduce deletion commands, credentials, customer details or step-by-step restore instructions. The question concerns backup recoverability in niche 323; cloud regional dependencies in 322 and general software engineering in 325 remain separate.
