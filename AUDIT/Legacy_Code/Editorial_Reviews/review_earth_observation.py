"""Editorial questions for satellites and Earth observation."""

from review_angle_plans import audit, revise_domain


EARTH_OBSERVATION = """history_origins|How One Satellite Record Began|Which mission choices made a particular Earth observation series possible?|Trace design, launch, calibration, coverage, and archive policy.
famous_examples|A Widely Shared Image Explained|What does one satellite image actually measure and show?|Name sensor, band, date, processing, scale, and ground reference.
hidden_stories|The Work Behind a Pixel|Who calibrates instruments, processes imagery, and checks results?|Follow agencies, field teams, archivists, and local partners.
beginner_explainers|A Pixel Is a Measurement|How does one sensor turn observed radiation into a map?|Use a high-level signal path, resolution, and uncertainty.
advanced_concepts|When Two Images Are Comparable|What must match before inferring change between dates?|Check season, orbit, bands, calibration, atmosphere, and processing version.
mysteries_unsolved_cases|A Change Visible Only from Space?|Which explanations fit one anomalous image pattern?|Compare artifacts, weather, land use, ground data, and uncertainty.
technology_innovation|A New Sensor's Real Advantage|Which feature improves a defined observation?|Compare resolution, revisit, spectral range, noise, and validation.
people_personalities|The Scientist Who Checked the Map|How did one team test a satellite-derived claim?|Trace field checks, reference data, methods, and published revisions.
major_events|Observing a Disaster Over Time|What could satellites establish during one documented event?|Compare acquisition times, cloud cover, ground reports, and response use.
how_it_works|From Orbit to Usable Data|Which stages turn one observation into a public dataset?|Follow sensing, downlink, calibration, correction, processing, and archive.
rise_fall|A Mission's End and Data Continuity|What changed when one satellite failed or retired?|Examine overlap, sensor differences, data gaps, and replacement.
then_vs_now|One Landscape Across Decades|How can long-term satellite images support a change claim?|Use harmonized data, common season, classification, and field context.
future_developments|A Planned Earth Observation Mission|What gap is the new sensor designed to close?|Check design requirements, validation plan, access, and realistic limits.
myths_vs_facts|Can Satellites See Everything?|Which features remain hidden by resolution, clouds, timing, or interpretation?|Use one sensor and one specific claimed observation.
documentary_stories|A Dataset Behind a Public Decision|How did an Earth observation product inform one land or hazard choice?|Trace data version, analysis, decision, ground checks, and outcome.
system_boundary|What Counts as the Observation System?|Which spacecraft, ground, software, and reference components matter?|Map the data chain and dependencies for one product.
input_output_trace|Raw Signal to Thematic Map|What assumptions transform measurements into a land-cover label?|Compare input bands, algorithm, training data, accuracy, and uncertainty.
design_tradeoff|Resolution Versus Revisit|Why did one mission prioritize detail, coverage, or frequency?|Compare orbit, sensor, data volume, cost, and intended use.
failure_mode|A Sensor Artifact Mistaken for Change|How was one anomaly found and corrected?|Review known-issues log, calibration, affected scenes, and reprocessing.
testing_limits|A Map's Accuracy Outside Its Test Area|Does performance hold in a different landscape or season?|Check reference sampling, domain shift, class balance, and error matrix.
standards_interoperability|Combining Two Satellite Series|What makes observations from different missions comparable?|Check units, geometry, calibration, metadata, and versioning.
security_threat_model|Sensitive Uses of Imagery|What privacy or security risks arise from one data product?|Assess resolution, access, inference, retention, and governance.
maintenance_lifecycle|Keeping a Satellite Record Trustworthy|How are sensors monitored and datasets revised?|Trace calibration sites, anomalies, new algorithms, and version notices.
infrastructure_dependencies|Ground Segment and Data Access|What does one mission need beyond the spacecraft?|Examine stations, processing, storage, network, and open access policy.
accessibility_usability|Who Can Use the Data?|Which cost, bandwidth, language, or expertise barriers matter?|Compare interfaces, licensing, training, and local use cases.
independent_replication|A Satellite Claim Reproduced|Can another analyst reach the same map or estimate?|Share scene IDs, version, code, reference data, and uncertainty.
responsible_deployment|A Map Used to Govern People|What happens when one classification informs policy?|Check false positives, affected communities, appeal, and human review.
field_route_capacity|How Often Can the Sensor Return?|How do orbit and acquisition rules constrain coverage of one area?|Compare scheduled revisits, usable scenes, cloud, and tasking.
field_vehicle_design|The Satellite Platform's Constraints|How do power, mass, and pointing affect one sensor's data?|Use public mission specs and observed performance.
field_maintenance_system|Maintaining a Mission in Orbit|How are faults, calibration drift, and updates handled?|Trace public operations reports and data-quality notices.
field_safety_case|Debris and End-of-Life Planning|What safety obligations apply to one satellite mission?|Check current jurisdiction, mitigation plan, collision data, and disposal.
field_construction_impact|Building the Ground Network|What local effects did one station or data facility create?|Compare land, energy, water, labor, permits, and community input.
"""


if __name__ == "__main__":
    revise_domain("159", "159_satellites_earth_observation", EARTH_OBSERVATION,
                  "Earth observation through sensor physics, calibration, data processing, validation, long-term records, access, and responsible uses.",
                  "versioned mission specifications and data products, calibration and known-issue logs, independent ground reference, processing methods, and records of downstream decisions",
                  "Name mission, sensor, product version, scene date, resolution, and place. A satellite image is a measurement and interpretation, not direct proof of a cause; validate sensitive claims and assess privacy and security implications.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
