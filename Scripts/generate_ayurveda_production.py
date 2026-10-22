# Generator script to populate complete Phase 2 documents, manifest, Phase 3 scenes, Phase 4 package, and Phase 5 audit
import os, json, re

P_BASE = "OUTPUT/281_ayurveda/281_ayurveda_beginner_explainers_foundations_of_doshas_agni_and_balance"
P_BIBLE = os.path.join(P_BASE, "03_Phase2_PRODUCTION_BIBLE")
P_SCENES = os.path.join(P_BASE, "04_Phase3_SCENE_BREAKDOWN")
P_PKG = os.path.join(P_BASE, "05_Phase4_PRODUCTION_PACKAGE")
P_AUDIT = os.path.join(P_BASE, "06_Phase5_FINAL_AUDIT")

def write_files(file_dict, base_dir):
    for name, content in file_dict.items():
        path = os.path.join(base_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Wrote {name} ({len(content)} chars)")

print("Script framework ready.")
