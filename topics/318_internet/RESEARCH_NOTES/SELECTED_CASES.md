# Selected internet outage — source review, 24 October 2026

All 20 archived pending and seven trending pitches are routed to active questions. The original records and IDs remain preserved. The new topic remains `proposed` with empty `verified_sources`.

## BANK-318-042 — Meta, 4 October 2021

- [Meta's engineering account](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) attributes the initial disconnection to a command during backbone maintenance and describes a failed safeguard, then withdrawal of BGP advertisements for authoritative DNS when facilities appeared unhealthy. It is the operator's postmortem, not an independent audit of every internal action.
- [Cloudflare's contemporaneous external observations](https://blog.cloudflare.com/october-2021-facebook-outage) show route withdrawal and resolver failures from its own vantage. Its timing and traffic measures should be attributed to that vantage, not generalized to every network or user.
- The case narrows BANK-318-031, -032 and -039: route reachability, DNS lookup and user-visible failure are linked but distinct. It concerns Meta services, not a shutdown of the global internet. A detailed chronology still needs timestamp normalization and other independent measurement archives.

## Editorial boundary

The archived “internet is the web,” record and speed-test hooks remain evidence tasks. No universal outage claim or production stage is approved.
