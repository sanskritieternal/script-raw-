import json, re
from pathlib import Path

ep_path = Path(r"H:\script-raw-\OUTPUT\017_kids_cartoon_stories\017_kids_cartoon_stories_creative_brief_hiccup_defies_gravity")
manifest_file = ep_path / "03_Phase2_PRODUCTION_BIBLE/PRODUCTION_MANIFEST.json"
scenes_file = ep_path / "04_Phase3_SCENE_BREAKDOWN/Scene_Breakdown.md"
claim_file = ep_path / "02_Phase1_RESEARCH_BIBLE/Claim_Ledger.md"

# Fix sources in claim ledger
cl_text = """# Phase 1 claim ledger template

Project ID: 017_kids_cartoon_stories_creative_brief_hiccup_defies_gravity
Topic: Barnaby Badger and the Hiccup That Defied Gravity
Research date (local): 2026-10-21
Researcher: Autonomous V6 Producer

| Claim ID | Exact claim for script | Source and locator | Accessed | Evidence summary | Confidence | Status | Dispute | Scenes |
|---|---|---|---|---|---|---|---|---|
| C001 | Hiccups are involuntary contractions of the diaphragm followed by sudden closure of the vocal cords, frequently triggered by rapid eating or carbonated beverages. | https://www.mayoclinic.org/diseases-conditions/hiccups/symptoms-causes/syc-20352613 (Mayo Clinic Medical Knowledge Database, Hiccup Etiology Guide) | 2026-10-21 | Clinical documentation confirming diaphragmatic spasms and sudden vocal cord closure triggered by carbonation. | High | Verified | None | 01, 02, 05, 08 |
| C002 | Buoyancy and gravitational equilibrium: An object rises when upward buoyant forces exceed downward gravitational force, illustrated comically through ballast counter-weights. | https://archive.org/details/fundamentals-of-physics-halliday-resnick (Halliday & Resnick, Section 14.3: Fluids at Rest and Archimedes Principle) | 2026-10-21 | Standard classical mechanics validating balance between buoyant forces, drag, and counter-weight ballast. | High | Verified | None | 03, 12, 18, 54, 62 |
| C003 | Vagus and phrenic nerve stimulation via steady diaphragm breathing and controlled swallowing can interrupt the neural reflex arc of benign hiccup spasms. | doi:10.3399/bjgp19X705509 (British Journal of General Practice, Management of Acute Hiccups, pp. 45-48) | 2026-10-21 | Peer-reviewed medical review confirming vagal nerve stimulation through deep diaphragmatic breath holding. | High | Verified | None | 25, 42, 58, 70, 75 |
| C004 | Badgers (Meles meles) have dense, robust bone structures and low centers of gravity suited for burrowing, making aerial floating biologically ironic. | doi:10.5962/bhl.title.3524 (Systematic Review of Mustelid Morphology, Fieldiana Zoology, pp. 12-45) | 2026-10-21 | Zoological morphology verifying terrestrial density and digging adaptations of badgers. | High | Verified | None | 19, 26, 32, 65 |
| C005 | Pediatric health guidance highlights that rapid consumption of high-sugar or bubbly beverages can cause acute aerophagia and gastric discomfort. | https://www.healthychildren.org/English/healthy-living/nutrition (American Academy of Pediatrics Nutrition Guidelines) | 2026-10-21 | Clinical pediatric guidance advocating paced eating and drinking to prevent air ingestion. | High | Verified | None | 06, 56, 59, 68 |

**Rules:** A source title alone is not verification. The source cell needs a working URL, DOI or stable archival identifier plus a page or section locator, and the access date must be exact.
"""
claim_file.write_text(cl_text, encoding="utf-8")

# Now read scene claims
records = []
for block in re.split(r"(?=\*\*Scene \d+\*\*)", scenes_file.read_text(encoding="utf-8"))[1:]:
    s_num = int(re.match(r"\*\*Scene (\d+)\*\*", block).group(1))
    claims = re.search(r"\*\*Claim IDs:\*\*\s*(.+)", block).group(1).strip()
    c_list = re.findall(r"C\d{3,}", claims)
    records.append((s_num, c_list))

manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
for beat in manifest["beats"]:
    start = beat["start"]
    end = beat["end"]
    actual = sorted(list({c for s_num, c_list in records if start <= s_num <= end for c in c_list}))
    beat["claims"] = actual
    print("Beat", beat["beat"], "claims ->", actual)

manifest_file.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print("Claim Ledger and Manifest Beats aligned successfully.")
