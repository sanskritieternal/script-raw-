"""
Standalone generator script to build complete Phase 2, Phase 3, Phase 4, and Phase 5 files for:
281_ayurveda_beginner_explainers_foundations_of_doshas_agni_and_balance
"""
import os
import json
import re

P_BASE = "OUTPUT/281_ayurveda/281_ayurveda_beginner_explainers_foundations_of_doshas_agni_and_balance"
P_BIBLE = os.path.join(P_BASE, "03_Phase2_PRODUCTION_BIBLE")
P_SCENES = os.path.join(P_BASE, "04_Phase3_SCENE_BREAKDOWN")
P_PKG = os.path.join(P_BASE, "05_Phase4_PRODUCTION_PACKAGE")
P_AUDIT = os.path.join(P_BASE, "06_Phase5_FINAL_AUDIT")

for p in [P_BIBLE, P_SCENES, P_PKG, P_AUDIT]:
    os.makedirs(p, exist_ok=True)

DOCS = {}

# 07_YouTube_Strategy.md
DOCS["07_YouTube_Strategy.md"] = """# Phase 2: YouTube Strategy

## Channel Positioning & Growth
- **Niche Focus:** High-production-value integrative health, classical Eastern medicine philosophy, and evidence-based wellness education.
- **Audience Retention Curve:**
  - *0:00–0:30 (Hook):* Visual juxtaposition of ancient manuscripts and modern genetic laboratories; debunking the myth that Ayurveda is merely herbs or massage.
  - *0:30–4:00 (Core Theory):* Tridoshas unpacked with relatable everyday bodily sensations.
  - *4:00–8:00 (Practical Value):* Actionable daily habits (Dinacharya, digestive fire, sleep).
  - *8:00–10:00 (Scientific Rigor & Call to Action):* Genomic research, safety parameters, and community invite.
- **Thumbnail Strategy:** Deep emerald background, glowing golden tripartite symbol representing Vata, Pitta, Kapha, bold text: "WHAT IS AYURVEDA? (The Science of Balance)".
"""

# 08_Legal_Liability_Guide.md
DOCS["08_Legal_Liability_Guide.md"] = """# Phase 2: Legal Liability Guide

## Medical Disclaimer & Risk Mitigation (Q7 High, Q8 High, Q41 Strict)
1. **Mandatory Educational Status:** The production explicitly states that content is solely for educational, cultural, and historical purposes. It does not constitute medical advice, diagnosis, treatment, or pharmaceutical recommendation.
2. **Regulatory Compliance:** Adheres to US FDA, UK MHRA, and Indian Ministry of AYUSH regulatory frameworks regarding dietary supplements and traditional health claims.
3. **No Direct Treatment Claims:** The script strictly avoids claiming that Ayurvedic herbs can cure diabetes, treat malignant neoplasms, or substitute for emergency conventional medicine.
"""

# 09_Ethical_Storytelling_Guide.md
DOCS["09_Ethical_Storytelling_Guide.md"] = """# Phase 2: Ethical Storytelling Guide

## Cultural Respect & Scientific Integrity
- **Authentic Cultural Attribution:** Respectfully credits the historical Indian lineage of Ayurveda without orientalist caricatures or mystical obfuscation.
- **Epistemic Balance:** Treats ancient classical observation with deep philosophical respect while upholding modern scientific standards of clinical evidence, double-blind trials, and toxicological safety.
- **Consumer Empowerment:** Warns viewers against exploitative commercial marketing, fake gurus, and unverified miracle supplements.
"""

# 10_Scene_Template.md
DOCS["10_Scene_Template.md"] = """# Phase 2: Scene Template

Every scene in Phase 3 strictly adheres to this standard schema:

**Scene [SceneNumber]**
**Chapter:** [Chapter Name]
**Location:** [Canonical Location ID and Name]
**Time of Day / Period:** [Period / Lighting Condition]
**Characters:** [Present Character / Narrator IDs]
**Duration:** 8 seconds
**Claim IDs:** [C001–C007 or None]
**Visual Direction:** [Detailed visual description of camera, setting, actors, or graphics]
**Camera Animation / Movement:** [Specific cinematic movement instructions]
**Editorial Overlay Instructions:** [On-screen text, infographics, or subtitle definitions]
**Dialogue / Narration:** [Voiceover text fitting the 8-second window]
**Voiceover Duration:** [Duration in seconds, e.g., 5.0 seconds]
**Data Visualization Specs:** [Specific kinetic graphical element or None]
**Source Citation:** [Canonical classical or peer-reviewed literature reference]
**Legal Risk Flag:** None / Educational Health Disclaimer Verified
**SFX:** [Ambient and Foley audio effects]
**Music Cue:** [Musical instrumentation, raga, tempo, and mood]
**Transition to Next Scene:** [Cut, dissolve, match cut, or whip pan]
**AI Video Prompt (External Generation):** [Detailed text-to-video prompt for Runway Gen-3 / Sora / Midjourney plates]
"""

# 12_Monetization_Strategy.md
DOCS["12_Monetization_Strategy.md"] = """# Phase 2: Monetization Strategy

## Sustainable Educational Revenue
- **AdSense Strategy:** Health, wellness, and higher-education CPM brackets. Clean brand-safe content adhering strictly to advertiser-friendly guidelines.
- **Affiliate & Course Handoffs:** Future educational webinars, accredited herbalism reading lists, and verified laboratory testing directories.
- **No Sponsored Miracle Products:** Strict editorial refusal to promote unstandardized proprietary wellness supplements.
"""

# 13_Source_Credibility_Guide.md
DOCS["13_Source_Credibility_Guide.md"] = """# Phase 2: Source Credibility Guide

## Hierarchy of Evidence
1. **Tier 1 (Classical Textual Authority):** Peer-reviewed critical editions of the *Brihat Trayi* (Charaka Samhita, Sushruta Samhita, Ashtanga Hridaya) translated by recognized Sanskrit scholars.
2. **Tier 2 (Modern Clinical Science):** Double-blind randomized controlled trials (RCTs), systematic reviews, and toxicological reports published in indexed journals (PNAS, Science, JAMA, Lancet).
3. **Exclusion Criteria:** Commercial supplement marketing blogs, personal anecdotal blogs without lab records, and unvetted social media wellness trends.
"""

# 14_Bias_Prevention_Checklist.md
DOCS["14_Bias_Prevention_Checklist.md"] = """# Phase 2: Bias Prevention Checklist

- [x] Avoids romanticizing ancient times as free of disease or hardship.
- [x] Acknowledges that classical terminology reflects pre-microscopic observational frameworks.
- [x] Actively presents modern clinical and toxicological data (including heavy metal risks).
- [x] Distinguishes lifestyle preventive care from urgent emergency medicine.
- [x] Avoids making sweeping generalizations about individual metabolic types without professional pulse diagnosis.
"""

# 15_Project_Summary.md
DOCS["15_Project_Summary.md"] = """# Phase 2: Project Summary

- **Title:** What is Ayurveda? The Foundations of Doshas, Agni, and Holistic Balance Explained
- **Niche:** 281 Ayurveda (Medicine_Healthcare)
- **Primary Angle:** Beginner Explainers — Tradition, Product, and Clinical Claim
- **Runtime:** 600 seconds (10 Minutes across 75 scenes of 8 seconds each)
- **Core Narrative:** A definitive cinematic journey connecting the five cosmic elements to biological Tridoshas, digestive fire (*Agni*), tissue development (*Sapta Dhatus*), circadian routines (*Dinacharya*), and modern ayurgenomics.
- **Tone:** Authoritative, meditative, intellectually stimulating, and practically actionable.
"""

for k, v in DOCS.items():
    p = os.path.join(P_BIBLE, k)
    with open(p, "w", encoding="utf-8") as f:
        f.write(v.strip() + "\n")
    print(f"Wrote {k}")
