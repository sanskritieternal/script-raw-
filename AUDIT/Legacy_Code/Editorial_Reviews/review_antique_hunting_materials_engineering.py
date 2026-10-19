"""Editorial question designs for antiques and materials engineering."""

from review_angle_plans import audit, revise_domain


ANTIQUE = """history_origins|The Antique Market's Changing Rules|How did collecting and export rules change for one object class?|Name jurisdiction and period.
famous_examples|An Antique with Documented Provenance|Which dated records establish its ownership path?|Check gaps and authenticity.
hidden_stories|People behind a Collected Object|Whose maker, user, or community history is missing from the sales label?|Use varied sources.
beginner_explainers|Antique, Reproduction, or Archaeological Object?|What evidence distinguishes age, maker, and legal category?|Define item and place.
advanced_concepts|Provenance and Authenticity|Why do material tests not replace a custody history?|Compare independent evidence.
mysteries_unsolved_cases|An Object with a Missing Period|Which archives or marks could explain the gap?|Do not invent ownership.
technology_innovation|Non-Destructive Object Analysis|What can imaging or spectroscopy identify and not date?|State instrument limits.
people_personalities|A Maker or Previous Owner|What documentary evidence connects a person to an object?|Avoid name-based guesswork.
major_events|A Restitution Decision|How did a documented claim change custody?|Read decision and community response.
how_it_works|From Find to Responsible Purchase|How do identification, provenance, condition, law, and conservation fit?|Use due-diligence checklist.
rise_fall|An Attribution Reversed|Which new evidence changed the object's label or value?|Trace catalog versions.
then_vs_now|Object's Original Use and Present Display|What context was lost or added in collecting?|Compare records.
future_developments|Researching an Unidentified Antique|What ethical, non-invasive next step could clarify it?|Preserve object and records.
myths_vs_facts|An Online Antique Claim|Which age and rarity assertions are actually documented?|Check comparable objects.
documentary_stories|One Object's Life History|How did manufacture, use, transfer, and interpretation unfold?|Show gaps clearly.
source_trail|A Seller's Provenance Story|Can each owner and date be supported by independent evidence?|Retain documents.
material_evidence|Marks and Construction|What can material and technique reveal about place and period?|Compare authenticated examples.
chronology_dispute|Conflicting Dates for an Object|Which method or document supports each?|State interval and uncertainty.
ordinary_lives|Everyday Use of an Antique|What wear and records show how it was used?|Avoid romantic invention.
power_and_institutions|Collecting under Unequal Power|Did conflict or colonial rule shape removal?|Examine custody history.
trade_and_exchange|Object's Route through Markets|What invoices or export records document movement?|Avoid assuming legal transfer.
language_and_labels|A Collector's Label|Does it reflect the source community's name and meaning?|Use original terms.
maps_and_borders|Where Was It Made or Found?|How did borders and place names change across its records?|Use dated maps.
conflicting_accounts|Seller and Community Histories|Which claims conflict and what evidence supports each?|Present voices fairly.
preservation_bias|What Antiques Survive?|How do taste and wealth shape the sample we see?|Compare ordinary material culture.
turning_point_test|A New Document Changes Attribution|Does it actually identify this object?|Check unique identifiers.
legacy_and_memory|An Object's Meaning Today|How do owners, descendants, and communities view its display?|Use attributed perspectives.
field_community_ownership|Who Should Hold the Object?|What legal and ethical interests do source communities assert?|Check current claims.
field_object_provenance|A Custody Timeline|Where are gaps and red flags in acquisition?|Apply ICOM due diligence.
field_living_practice|Object and Living Tradition|Is the practice still active and who may explain it?|Consult practitioners.
field_conservation_choice|Repair without Erasing Evidence|Which treatment is reversible and documented?|Use conservator assessment.
field_cultural_translation|Explaining without Mislabeling|How can a public label convey local meaning and uncertainty?|Review with community.
"""

MATERIALS = """history_origins|A Material Enters Engineering Use|Which measurements and production improvements enabled adoption?|Trace dated standards.
famous_examples|A Material in a Real Component|Why was it selected and what performance was measured?|Name grade and service conditions.
hidden_stories|Testing and Manufacturing Labor|Who prepared samples, controlled processes, and inspected quality?|Use production records.
beginner_explainers|Structure, Processing, Properties, Performance|How do these four stages connect for a named material?|Use one application.
advanced_concepts|Property Variability|How do defects, microstructure, and environment change strength?|Use distributions, not single values.
mysteries_unsolved_cases|A Component Failed Early|Which loading, corrosion, or manufacturing evidence could distinguish causes?|Preserve failed part.
technology_innovation|A New Alloy or Composite|What benefit survived independent testing and scale-up?|Compare commercial grade.
people_personalities|A Materials Team's Decision|What tradeoffs shaped one design choice?|Use attributed engineering record.
major_events|A Material-Related Recall|What defect and verification changed design or process?|Read official investigation.
how_it_works|From Lab Coupon to Component|How do formulation, processing, test, qualification, and service connect?|Track sample lineage.
rise_fall|A Material Replaced|Was cost, durability, regulation, or supply decisive?|Use dated product evidence.
then_vs_now|Material Data across Decades|How did test methods and reporting improve?|Compare like specimens.
future_developments|Candidate Material for a New Use|What test and manufacturing milestones are still required?|Frame conditional.
myths_vs_facts|A Miracle Material?|Which tradeoffs and test conditions limit headline properties?|Check full property set.
documentary_stories|A Failure Investigation's Record|How did collection, microscopy, testing, and redesign unfold?|Use official report.
system_boundary|The Material in Its Assembly|Which interfaces and loads affect performance?|Define component and environment.
input_output_trace|Processing to Measured Property|How do input composition and process history change output?|Record provenance.
design_tradeoff|Strength versus Toughness or Cost|Which property matters most under the actual load?|Compare candidate grades.
failure_mode|A Crack's Growth|What observed evidence supports fatigue, overload, or corrosion?|Avoid premature diagnosis.
testing_limits|What a Coupon Test Can Prove|How does a specimen differ from a manufactured part?|State scale and conditioning.
standards_interoperability|A Test Standard's Scope|Does a named method fit the material and use?|Check edition and specimen.
security_threat_model|Integrity of Materials Data|Could tampered records or counterfeit batches undermine assurance?|Audit traceability.
maintenance_lifecycle|Property Change in Service|How do heat, wear, and corrosion alter lifetime?|Use inspection data.
infrastructure_dependencies|Critical Material Supply|What happens if a grade or precursor is unavailable?|Map qualified substitutes.
accessibility_usability|Repairable Material Choice|Can field workers inspect and join the material?|Include tools and training.
independent_replication|Repeating a Material Result|Do another lab and batch reproduce the property?|Match method and uncertainty.
responsible_deployment|From Discovery to Safe Use|Which qualification and monitoring steps precede use?|Name application risk.
field_prototype_testing|A Component under Real Loads|Which bench and field tests reveal different failures?|Compare conditions.
field_design_tolerance|Manufacturing Variation|How much dimensional and property spread can design accept?|Use measured process capability.
field_manufacturing_method|Process Affects Microstructure|How do casting, forming, or printing change a specific property?|Use controlled comparison.
field_failure_investigation|Preserving Failure Evidence|Which fracture surface and records must be secured?|Maintain chain of custody.
field_repair_path|Can a Damaged Part Be Restored?|Which repair method preserves qualified properties?|Check reinspection and limits.
"""

if __name__ == "__main__":
    revise_domain("417", "417_antique_hunting", ANTIQUE,
                  "Antique hunting through authenticated identity, custody, condition, conservation, cultural meaning, legality, and community claims.",
                  "ICOM museum ethics and provenance guidance, UNESCO cultural-property convention, object records, conservation reports, and source-community accounts",
                  "Name object, place, date, and ownership evidence. A seller's story, mark, or test alone does not prove lawful provenance or authenticity.")
    revise_domain("442", "442_materials_engineering", MATERIALS,
                  "Materials engineering through processing, measured properties, qualification, manufacturing variation, service failures, and repair.",
                  "NIST Materials Genome Initiative data and quality guidance, applicable test standards, batch records, independent measurements, and failure reports",
                  "Name material grade, sample, process, test conditions, and use. Laboratory coupon performance does not certify a component in service.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
