# Selected operator source note — cloud computing

Inspected 2026-10-24 for `BANK-322-042`. This is a dated service-event premise check, not a current AWS availability or configuration recommendation.

- [AWS, summary of the 7 December 2021 Northern Virginia (US-EAST-1) service event, published 10 December 2021](https://aws.amazon.com/message/12721/): operator account describes an internal network hosting foundational services including monitoring, internal DNS, authorization and parts of the EC2 control plane. It distinguishes running EC2 instances from increased error rates and latencies in EC2 APIs. The account is a primary provider statement, not an independent measurement of every customer's downtime.
- [AWS Well-Architected Framework, 2023-04-10 edition, OPS11-BP02 post-incident analysis](https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_evolve_ops_perform_rca_process.html): versioned vendor guidance describes review of customer-impacting events and contributing factors. It is general guidance, not evidence that a specific customer architecture would have avoided this outage.

The AWS pages were accessible. No customer logs, independent network telemetry or later service-version behavior were examined. Keep the 2021 region and named services separate from global AWS claims; avoid incident-response steps or promises about future resilience. General database restore guarantees belong in niche 323.
