"""
Align chapters in manifest and YOUTUBE_METADATA.md
"""
import json
import os

P_BASE = "OUTPUT/281_ayurveda/281_ayurveda_beginner_explainers_foundations_of_doshas_agni_and_balance"
P_BIBLE = os.path.join(P_BASE, "03_Phase2_PRODUCTION_BIBLE")

P_MAN = os.path.join(P_BIBLE, "PRODUCTION_MANIFEST.json")
with open(P_MAN) as f:
    m = json.load(f)

chapters = [
    "The Elemental Architecture of Life",
    "The Tridoshas Decoded: Vata, Pitta, Kapha",
    "Agni, Ama & The Seven Dhatus",
    "Dinacharya: Circadian Daily Living",
    "Modern Ayurgenomics, Safety & Integration"
]

m["chapters"] = [
    {"title": chapters[0], "start_seconds": 0},
    {"title": chapters[1], "start_seconds": 120},
    {"title": chapters[2], "start_seconds": 240},
    {"title": chapters[3], "start_seconds": 360},
    {"title": chapters[4], "start_seconds": 480}
]

with open(P_MAN, "w") as f:
    json.dump(m, f, indent=2)

P_META = os.path.join(P_BIBLE, "YOUTUBE_METADATA.md")

meta_content = f"""# YouTube Metadata: What is Ayurveda?

## Primary title
What is Ayurveda? The Foundations of Doshas, Agni, and Holistic Balance Explained

## Description
What is Ayurveda, and how does this foundational medical tradition explain health, vitality, and mind-body balance? 

In this comprehensive, evidence-based documentary explainer, we explore the core foundations of Ayurvedic science: from the Five Elements (Panchamahabhutas) and the Three Doshas (Vata, Pitta, and Kapha) to the power of digestive fire (Agni), tissue nutrition (Sapta Dhatus), and daily circadian routines (Dinacharya). 

We also examine what modern clinical medicine, genomics, and chronobiology reveal about ancient constitutional types—while addressing essential safety guidelines and quality standards for herbal preparations.

### Video Chapters:
00:00 {chapters[0]}
02:00 {chapters[1]}
04:00 {chapters[2]}
06:00 {chapters[3]}
08:00 {chapters[4]}

MEDICAL DISCLAIMER:
This video is for educational, cultural, and informational purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## Tags
Ayurveda, What is Ayurveda, Doshas, Vata Pitta Kapha, Ayurvedic Medicine, Agni, Dinacharya, Holistic Health, Integrative Medicine, Ayurgenomics, Herbal Medicine, Ancient Wisdom, Health and Wellness

## Thumbnail design
- Background: Moody, deep emerald green with warm golden rim lighting.
- Focal Image: Sleek tripartite mandala diagram glowing with subtle ember, wind, and water particles, flanking a serene Ayurvedic physician examining dried herbs.
- Foreground Text: "WHAT IS AYURVEDA? (The Science of Balance)" in bold modern typography.

## Pinned comment
Welcome to our channel! Have you ever explored your Ayurvedic constitution (Prakriti), or noticed how your energy shifts across different seasons? Let us know your thoughts and questions in the comments below—and remember to check out our source bibliography in the video description!

## Upload decisions
- Category: Education / Health
- Visibility: Public
- Language: English (EN)
- License: Standard YouTube License
- Age Restriction: None (All Audiences)

## Publication record
- Project ID: 281_ayurveda_beginner_explainers_foundations_of_doshas_agni_and_balance
- Status: Scheduled Production Package
- Release Target: Season 1, Episode 1

## Corrections
No corrections logged at release. Any future scientific errata or regulatory safety advisories will be updated here and pinned in the comments.
"""

with open(P_META, "w", encoding="utf-8") as f:
    f.write(meta_content.strip() + "\n")

print("Aligned chapters successfully.")
