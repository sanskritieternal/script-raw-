# Software engineering primary-source follow-up — 2026-10-24

## BANK-325-043 — Knight Capital

- Primary institutional source: US Securities and Exchange Commission, *SEC Charges Knight Capital With Violations of Market Access Rule*, 16 October 2013: https://www.sec.gov/newsroom/press-releases/2013-222
- The SEC says its investigation found inadequate safeguards and reviews in the 1 August 2012 incident. Its account describes dormant router functionality, an incorrect 2012 deployment and resulting erroneous orders. These are regulator findings related to a settlement.
- Limit: attribute the incident narrative to the SEC. This release is a summary of enforcement findings, not a complete independent technical reconstruction or proof that one deployment step was the sole cause. Regulatory conclusions are jurisdiction- and date-specific; avoid operational trading instructions.

## BANK-325-044 — Mars Climate Orbiter

- Primary institutional source: NASA Jet Propulsion Laboratory, *Mars Climate Orbiter Team Finds Likely Cause of Loss*, 30 September 1999: https://www.jpl.nasa.gov/news/mars-climate-orbiter-team-finds-likely-cause-of-loss/
- JPL reported *preliminary* peer-review findings: an information transfer between the spacecraft team in Colorado and navigation team in California used English versus metric units, and checks did not detect the mismatch before spacecraft loss.
- Limit: this dated release is explicitly preliminary. It supports a bounded interface/verification case, not the full final causal chain, a numerical trajectory calculation, or a claim that software alone was responsible. Seek the final mishap report before scripting a definitive cause account.

## Routing and overlap boundary

Generic requirements, testing, review, rollback and dependency pitches map to existing bank questions. The new cases focus a documented deployment/control incident and a documented mission-team interface failure. Bank 324 covers programming-language semantics, bank 322 cloud operation and bank 326 security; neither incident is recast as a generic language, cloud or intrusion story.
