# Research note: electricity and electronics cases

Checked 2026-10-24. This note records source access and bounded premises for proposed BANK questions. It does not mark any topic ready for an IDEA or fill verified_sources.

## BANK-161-044 — USB-C cable rating

- USB Implementers Forum, [USB Charger (USB Power Delivery)](https://www.usb.org/usb-charger-pd), current page accessed 2026-10-24. It dates USB PD Revision 3.1 to 2021, describes up to 240W and the 28V/36V/48V fixed-voltage options, and makes clear that the powered device requests what it needs.
- USB-IF, [Cables and Connectors compliance updates](https://compliance.usb.org/index.asp?Format=Standard&UpdateFile=Cables+and+Connectors), updates effective December 2021 and March 2022, accessed 2026-10-24. The USB-IF compliance program requires power capability labels of 60W or 240W on USB-C to USB-C cable submissions and, apart from USB 2.0 cable exceptions, suitable data-rate markings.
- USB-IF, [Type-C cable power-rating logo guidelines (2022 PDF)](https://www.usb.org/sites/default/files/usb_type-c_cable_power_rating_logo_usage_guidelines_020222.pdf). The 240W packaging logo is for a rated cable that passed specified USB-IF tests and appears on its Integrators List.

**Claim limit:** These are the program's requirements and capability ceilings. They do not establish that any uninspected retail cable is certified, that a 240W-marked cable delivers 240W with any charger/device pair, or that a power rating tells the cable's data speed. Recheck the applicable standard revision and product listing before scripting a purchase or compatibility claim.

## BANK-161-045 — Hydro-Québec 1989

- Hydro-Québec, [Understanding electricity: March 1989 blackout](https://pannes.hydroquebec.com/learning/notions-de-base/tempete-mars-1989.html), operator learning page, accessed 2026-10-24. The utility dates the grid protection trip to March 13, 1989, about 2:44 a.m., after geomagnetic disturbance and voltage fluctuations, and describes later protection, monitoring and operating changes. The page does not display a clear original publication date.
- Hydro-Québec, [Successfully manages the effects of solar storms](https://news.hydroquebec.com/content/hydroquebec/en/news/press-releases/all-quebec/hydro-quebec-successfully-manages-the-effects-of-solar-storms.html), September 12, 2014. The operator attributes the 1989 blackout to storm-induced currents and protection-system effects and describes mitigation measures as of 2014.
- NOAA Space Weather Prediction Center, [Space weather primer (2010 PDF)](https://www.swpc.noaa.gov/sites/default/files/images/u33/primer_2010_new.pdf), explains the induced-current mechanism and cites the March 13 outage.

**Claim limit:** The operator's retrospective account supports a named historical failure and subsequent changes, not a measured universal blackout probability or an assertion that all grids are equally vulnerable. The 2014 statement about later Hydro-Québec performance is date-bound; do not extend it to 2026 without a new operating record. Avoid operational switching advice.
