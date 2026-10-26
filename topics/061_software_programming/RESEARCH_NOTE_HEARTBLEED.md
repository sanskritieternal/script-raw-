# Heartbleed: bounded version and disclosure note

Linked proposal: [BANK-061-064](IN_DEPTH_TOPIC_BANK.md#bank-061-064). Research checked 2026-10-24. This is a source trail for one historical defect, not a current vulnerability test or a claim that every affected installation leaked data.

## Primary project record

The [OpenSSL vulnerability record for CVE-2014-0160](https://mirror.openssl-library.org/news/vulnerabilities/) dates disclosure to 7 April 2014. It describes a missing bounds check in TLS heartbeat handling that could expose up to 64 kB of process memory per request. It identifies **OpenSSL 1.0.1 before 1.0.1g** as affected and states that earlier OpenSSL versions were not affected. The project’s [2014 advisory archive](https://wiki.openssl.org/index.php/SECADV_20140407) gives the technical and remediation context, though its summary table appears to mistype the CVE number; use the vulnerability record’s CVE-2014-0160 and verify against the advisory body before quoting an identifier.

## Checks for a researched episode

1. Name the OpenSSL version and heartbeat code path in every technical demonstration. Distinguish library version, application linkage and actual deployment exposure.
2. Show the mismatch between a requested payload length and available bytes, and explain why a bound check prevents reading beyond the supplied request. Keep the example in a safe local test environment.
3. Separate possible disclosure of process memory from proven extraction of a particular key or user record. The public advisory does not identify every victim.
4. Compare the fix version and suggested workaround in the project's dated advisory; avoid extending 2014 guidance to current releases without a new version check.

## Limits

The project records establish the flaw, affected release range and historical fix. They do not prove the sensational claim that the entire internet was compromised, or quantify aggregate financial harm. The active BANK record stays proposed with no verified-source designation.
