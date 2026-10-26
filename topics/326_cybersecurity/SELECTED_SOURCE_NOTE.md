# Selected primary-source premise check ? cybersecurity (2026-10-24)

## SolarWinds / CISA ED 21-01 ? BANK-326-041
CISA issued Emergency Directive 21-01 on 2020-12-13 for federal civilian executive-branch agencies. Its own supplemental guidance describes affected Orion versions, required agency review and reporting, and later changes to the response. CISA's 2021 eviction guidance describes malicious code in multiple Orion versions and says follow-on activity occurred in some instances. This supports a question about making decisions under uncertain exposure, not a claim that every user of Orion was breached.

Primary/institutional records: https://www.cisa.gov/news-events/directives ; https://github.com/cisagov/cyber.dhs.gov/blob/master/pages/ed-21-01-supplemental-guidance.md ; https://www.cisa.gov/sites/default/files/publications/AR21-133A_Remediating_Networks_Affected_by_the_SolarWinds_and_Active_Directory_M365_Compromise%20%281%29.pdf . CISA's directive page may block automated retrieval; the agency-maintained GitHub mirror and CISA PDF expose the dated scope. Later supplemental versions superseded some initial actions. Do not state current mandatory controls from this 2020?21 record or supply attack/response instructions.

## Log4j / CISA joint advisory ? BANK-326-042
The joint CISA and partner advisory, revised 2021-12-23, asked vendors to identify affected products and inform users, and organizations to identify affected assets. This supports a supply-chain inventory and communication case. The archived version recommendations and threat assessment are historical; product versions and current guidance may differ.

Primary record: https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-356a . The page is marked archived by CISA. Avoid exploit mechanism, compromise claims about any particular organization, and present-day remediation advice.

## Semantic boundaries
BANK-326-040 is the general containment tradeoff; 041 traces one public federal directive. BANK-326-032 is general patch operations; 042 traces information flow for a named dependency. BANK-322-038 owns cloud shared responsibility; BANK-325-033 owns general incident review. The proposed 328/329 WannaCry and forensic-tool subjects are left there.
