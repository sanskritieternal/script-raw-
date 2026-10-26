"""
Integrate extensive topic bank, 20 playlists, 8-part botanical series, and editorial upload order
into Niche 281 Ayurveda topic tracking, roadmap documents, and machine-readable registries.
"""

import os
import json
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(r"h:\script-raw-")
TOPICS_DIR = ROOT_DIR / "topics" / "281_ayurveda"
OUTPUT_DIR = ROOT_DIR / "OUTPUT" / "281_ayurveda"

# 1. 20 Completed Episodes in OUTPUT/281_ayurveda
COMPLETED_EPISODES = [
    {
        "id": 1,
        "title": "Foundations of Ayurveda: Doshas, Agni, and Holistic Balance Explained",
        "tier": "Tier 1: Foundations (Scratch / Beginner)",
        "angle": "beginner_explainers",
        "folder": "281_ayurveda_beginner_explainers_foundations_of_doshas_agni_and_balance",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Panchamahabhutas (5 elements), Vata, Pitta, Kapha, Agni, Prakriti vs Vikriti."
    },
    {
        "id": 2,
        "title": "Discovering Your Prakriti: How to Determine Your Ayurvedic Mind-Body Constitution",
        "tier": "Tier 1: Foundations (Scratch / Beginner)",
        "angle": "beginner_explainers",
        "folder": "281_ayurveda_beginner_explainers_discovering_your_prakriti_ayurvedic_constitution",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Phenotypic markers of Vata, Pitta, and Kapha, self-assessment boundaries."
    },
    {
        "id": 3,
        "title": "The Philosophy of Health: Swasthya & The Definition of True Well-being",
        "tier": "Tier 1: Foundations (Scratch / Beginner)",
        "angle": "beginner_explainers",
        "folder": "281_ayurveda_beginner_explainers_philosophy_of_health_swasthya_true_wellbeing",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Sushruta Samhita Sutrasthana 15.41 (Samadosha samagnischa...), mental tranquility."
    },
    {
        "id": 4,
        "title": "Agni vs. Ama: The Root of Vitality and the Origin of Toxicity",
        "tier": "Tier 1: Foundations (Scratch / Beginner)",
        "angle": "beginner_explainers",
        "folder": "281_ayurveda_beginner_explainers_agni_vs_ama_vitality_and_toxicity",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "The 4 states of Agni (Sama, Vishama, Tikshna, Manda), signs of Ama, tongue coating."
    },
    {
        "id": 5,
        "title": "Dinacharya: The Science of the Ayurvedic Daily Circadian Routine",
        "tier": "Tier 2: Daily Lifestyle & Preventive Living (Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_dinacharya_science_of_circadian_routine",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Brahma Muhurta, tongue scraping (Jihwa Nirlekhana), oil pulling (Gandusha), modern chronobiology."
    },
    {
        "id": 6,
        "title": "Ritucharya: Seasonal Living and Preventing Disease Through Climate Transitions",
        "tier": "Tier 2: Daily Lifestyle & Preventive Living (Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_ritucharya_seasonal_living_and_climate_shifts",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Six seasons (Ritus), Sandhikal (seasonal junction), diet and lifestyle adaptations."
    },
    {
        "id": 7,
        "title": "Ahara Vijnana: The 6 Tastes (Shad Rasa) and Ayurvedic Nutritional Science",
        "tier": "Tier 2: Daily Lifestyle & Preventive Living (Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_ahara_vijnana_six_tastes_nutritional_science",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Elemental composition of 6 tastes, Vipaka (post-digestive effect), Virya (potency)."
    },
    {
        "id": 8,
        "title": "Viruddha Ahara: Incompatible Food Combinations and Gut Health",
        "tier": "Tier 2: Daily Lifestyle & Preventive Living (Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_viruddha_ahara_incompatible_food_combinations",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Milk and sour fruits, heated honey, enzymatic mismatch, and gut microbiome disturbance."
    },
    {
        "id": 9,
        "title": "Ayurvedic Sleep Science: Nidra, Insomnia, and Restorative Rest",
        "tier": "Tier 2: Daily Lifestyle & Preventive Living (Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_ayurvedic_sleep_science_nidra_restoration",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Nidra as one of Trayopastambha (three pillars), Shiroabhyanga, herbs (Brahmi, Shankhpushpi)."
    },
    {
        "id": 10,
        "title": "The Truth About Ashwagandha: Mechanism, Clinical Trials, and Safe Usage",
        "tier": "Tier 3: Formulations, Herbology & Therapies (Upper Intermediate)",
        "angle": "claim_evidence",
        "folder": "281_ayurveda_claim_evidence_truth_about_ashwagandha_clinical_trials_safety",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Withania somnifera adaptogenic pharmacology, cortisol reduction, withanolides, quality checks."
    },
    {
        "id": 11,
        "title": "Triphala: The Chemistry and Therapeutic Power of Three Sacred Fruits",
        "tier": "Tier 3: Formulations, Herbology & Therapies (Upper Intermediate)",
        "angle": "claim_evidence",
        "folder": "281_ayurveda_claim_evidence_triphala_chemistry_and_therapeutic_power",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Haritaki, Bibhitaki, Amalaki synergy, polyphenols, gentle laxative action, gut regulation."
    },
    {
        "id": 12,
        "title": "Curcumin & Turmeric (Haridra): Ancient Panacea vs. Modern Bioavailability",
        "tier": "Tier 3: Formulations, Herbology & Therapies (Upper Intermediate)",
        "angle": "claim_evidence",
        "folder": "281_ayurveda_claim_evidence_curcumin_turmeric_ancient_panacea_bioavailability",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Piperine synergy, anti-inflammatory pathways (NF-kB), culinary vs clinical doses."
    },
    {
        "id": 13,
        "title": "Panchakarma Demystified: The Five Classical Cleansing Therapies",
        "tier": "Tier 3: Formulations, Herbology & Therapies (Upper Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_panchakarma_demystified_five_cleansing_therapies",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Purvakarma (Snehana/Swedana), Vamana, Virechana, Basti, Nasya, Raktamokshana protocols."
    },
    {
        "id": 14,
        "title": "Abhyanga and Snehana: The Physiology of Transdermal Herbal Oil Therapies",
        "tier": "Tier 3: Formulations, Herbology & Therapies (Upper Intermediate)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_abhyanga_and_snehana_transdermal_oil_therapies",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Vata alleviation, vagal tone activation, lymphatic drainage, classical lipid carriers."
    },
    {
        "id": 15,
        "title": "Samprapti: The 6 Stages of Disease Progression in Ayurvedic Pathology",
        "tier": "Tier 4: Advanced Concepts & Integrative Evidence (Advanced / Expert)",
        "angle": "advanced_concepts",
        "folder": "281_ayurveda_advanced_concepts_samprapti_six_stages_of_disease_pathology",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Shad Kriya Kala: Sanchaya, Prakopa, Prasara, Sthana Samshraya, Vyakti, Bheda."
    },
    {
        "id": 16,
        "title": "Ashtavidha Pariksha: The 8-Fold Clinical Diagnostic Examination",
        "tier": "Tier 4: Advanced Concepts & Integrative Evidence (Advanced / Expert)",
        "angle": "advanced_concepts",
        "folder": "281_ayurveda_advanced_concepts_ashtavidha_pariksha_eightfold_diagnostic_examination",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Nadi (pulse), Mutra (urine), Mala (stool), Jihwa (tongue), Shabda, Sparsha, Druk, Akruti."
    },
    {
        "id": 17,
        "title": "Rasa Shastra & Heavy Metal Safety: Classical Detoxification vs. Modern Toxicology",
        "tier": "Tier 4: Advanced Concepts & Integrative Evidence (Advanced / Expert)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_rasa_shastra_heavy_metal_safety_and_toxicology",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Shodhana and Marana nano-mineralogy, heavy metal contamination testing, AYUSH/FDA rules."
    },
    {
        "id": 18,
        "title": "Ayurgenomics: How Ancient Prakriti Correlates with Modern DNA & Gene Expression",
        "tier": "Tier 4: Advanced Concepts & Integrative Evidence (Advanced / Expert)",
        "angle": "advanced_concepts",
        "folder": "281_ayurveda_advanced_concepts_ayurgenomics_ancient_prakriti_and_modern_dna",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "CSIR genomic studies, CYP2C19 variations across Prakriti, personalized medicine links."
    },
    {
        "id": 19,
        "title": "Ayurveda for Gut Dysbiosis & Autoimmunity: Integrative Protocols",
        "tier": "Tier 4: Advanced Concepts & Integrative Evidence (Advanced / Expert)",
        "angle": "advanced_concepts",
        "folder": "281_ayurveda_advanced_concepts_ayurveda_gut_dysbiosis_integrative_protocols",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Grahani Dosha, leaky gut syndrome, intestinal lining repair, integrative care handoffs."
    },
    {
        "id": 20,
        "title": "Critical Thinking in Herbal Medicine: Navigating Misinformation and Adulteration",
        "tier": "Tier 4: Advanced Concepts & Integrative Evidence (Advanced / Expert)",
        "angle": "how_it_works",
        "folder": "281_ayurveda_how_it_works_critical_thinking_herbal_medicine_misinformation",
        "status": "COMPLETED (Phases 0-5 Built)",
        "key_focus": "Extraction ratios, microbial & heavy metal lab testing, avoiding liver toxicity from spurious pills."
    }
]

# 2. Suggested First 20 Uploads (Editorial Sequence)
FIRST_20_UPLOADS = [
    {"num": 1, "title": "Ayurveda Explained: Beyond Herbs and Home Remedies", "angle": "beginner_explainers", "slug": "ayurveda_explained_beyond_herbs_and_home_remedies", "tier": "Tier 1: Foundations"},
    {"num": 2, "title": "Ashwagandha: Rooted in Tradition", "angle": "claim_evidence", "slug": "ashwagandha_rooted_in_tradition", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 3, "title": "Turmeric: The Golden Tradition", "angle": "claim_evidence", "slug": "turmeric_the_golden_tradition", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 4, "title": "Vata, Pitta, and Kapha Explained Simply", "angle": "beginner_explainers", "slug": "vata_pitta_and_kapha_explained_simply", "tier": "Tier 1: Foundations"},
    {"num": 5, "title": "Tulsi: The Story Behind the Sacred Plant", "angle": "history_origins", "slug": "tulsi_the_story_behind_the_sacred_plant", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 6, "title": "Amla: From Tree to Traditional Preparation", "angle": "how_it_works", "slug": "amla_from_tree_to_traditional_preparation", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 7, "title": "Agni: What Ayurveda Means by Digestive Fire", "angle": "beginner_explainers", "slug": "agni_what_ayurveda_means_by_digestive_fire", "tier": "Tier 1: Foundations"},
    {"num": 8, "title": "Fresh Ginger vs. Dried Ginger", "angle": "how_it_works", "slug": "fresh_ginger_vs_dried_ginger", "tier": "Tier 2: Daily Lifestyle & Dietetics"},
    {"num": 9, "title": "Triphala: Inside the Three-Fruit Formula", "angle": "claim_evidence", "slug": "triphala_inside_the_three_fruit_formula", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 10, "title": "A Realistic Ayurvedic Morning Routine", "angle": "how_it_works", "slug": "a_realistic_ayurvedic_morning_routine", "tier": "Tier 2: Daily Lifestyle & Regimen"},
    {"num": 11, "title": "Brahmi vs. Mandukaparni: The Naming Confusion", "angle": "myths_vs_facts", "slug": "brahmi_vs_mandukaparni_the_naming_confusion", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 12, "title": "Ghee: Tradition, Nutrition, and Common Claims", "angle": "myths_vs_facts", "slug": "ghee_tradition_nutrition_and_common_claims", "tier": "Tier 2: Daily Lifestyle & Dietetics"},
    {"num": 13, "title": "Shatavari: The Plant Behind the Name", "angle": "claim_evidence", "slug": "shatavari_the_plant_behind_the_name", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 14, "title": "Oil Pulling: Tradition and Evidence", "angle": "how_it_works", "slug": "oil_pulling_tradition_and_evidence", "tier": "Tier 2: Daily Lifestyle & Regimen"},
    {"num": 15, "title": "Neem: Why the Plant Part Matters", "angle": "how_it_works", "slug": "neem_why_the_plant_part_matters", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 16, "title": "Ayurvedic Body Types: What Quizzes Leave Out", "angle": "beginner_explainers", "slug": "ayurvedic_body_types_what_quizzes_leave_out", "tier": "Tier 1: Foundations"},
    {"num": 17, "title": "Chyawanprash: What Is Inside the Jar?", "angle": "how_it_works", "slug": "chyawanprash_what_is_inside_the_jar", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 18, "title": "Panchakarma: What It Actually Involves", "angle": "how_it_works", "slug": "panchakarma_what_it_actually_involves", "tier": "Tier 3: Formulations & Herbology"},
    {"num": 19, "title": "Natural Does Not Always Mean Safe", "angle": "myths_vs_facts", "slug": "natural_does_not_always_mean_safe", "tier": "Tier 4: Advanced Concepts & Evidence"},
    {"num": 20, "title": "How to Read an Ayurvedic Supplement Label", "angle": "how_it_works", "slug": "how_to_read_an_ayurvedic_supplement_label", "tier": "Tier 4: Advanced Concepts & Evidence"}
]

# 3. 20 Themed Playlists with All Topics (282 topics)
PLAYLISTS = [
    {
        "id": 1,
        "name": "Ayurveda Foundations",
        "description": "Beginner playlist explaining one core foundational concept per video.",
        "pillar": "Tradition Examined Through Research & Foundations",
        "topics": [
            "What Is Ayurveda? Its purpose, scope, and Indian origins",
            "Ayurveda Beyond Herbal Remedies: Food, routine, observation, and clinical practice",
            "The Five Elements: Understanding the traditional framework",
            "Vata Explained: Its meaning within Ayurveda",
            "Pitta Explained: Its meaning within Ayurveda",
            "Kapha Explained: Its meaning within Ayurveda",
            "Prakriti vs. Vikriti: Constitution and current imbalance",
            "Why Online Dosha Quizzes Can Oversimplify Ayurveda",
            "Agni: The Ayurvedic concept of digestive and transformative activity",
            "Ama: What classical descriptions mean—and why 'toxins' is an imprecise translation",
            "The Seven Dhatus: A guide to the traditional tissue framework",
            "The Three Malas: Ayurveda’s descriptions of bodily waste",
            "Srotas: Understanding the traditional channels framework",
            "Ojas: Its place in Ayurvedic thinking",
            "The Six Tastes: Sweet, sour, salty, pungent, bitter, and astringent",
            "Gunas: How Ayurveda describes qualities such as heavy, light, dry, and oily",
            "Rasa, Guna, Virya, Vipaka, and Prabhava: How substances are traditionally characterized",
            "The Eight Classical Branches of Ayurveda"
        ]
    },
    {
        "id": 2,
        "name": "Individual Herb Documentaries",
        "description": "Deep-dive monographs giving each plant a recognizable botanical and evidence identity.",
        "pillar": "Botanical Stories",
        "topics": [
            "Ashwagandha: Roots, botanical identity, traditional context, and research",
            "Turmeric: The golden rhizome beyond the spice jar",
            "Tulsi: Sacred plant, botanical diversity, and household traditions",
            "Amla: Fruit anatomy, food traditions, and Ayurvedic preparations",
            "Neem: Leaves, bark, seeds, and why preparation matters",
            "Brahmi: Understanding Bacopa monnieri",
            "Mandukaparni: Understanding Centella asiatica and naming confusion",
            "Shatavari: The plant behind the branching storage roots",
            "Guduchi/Giloy: Identification, traditional use, and safety questions",
            "Mulethi/Yashtimadhu: Licorice root and its precautions",
            "Haritaki: The fruit, its traditional classifications, and preparations",
            "Bibhitaki: The lesser-known Triphala ingredient",
            "Arjuna: The tree and its medicinal bark",
            "Guggulu: A resin, its source plant, and sourcing concerns",
            "Punarnava: Botanical identity and traditional context",
            "Manjistha: The red-rooted plant and its history",
            "Bhringraj: The plant behind familiar hair products",
            "Jatamansi: An aromatic Himalayan plant and conservation questions",
            "Shankhapushpi: Why the botanical identity needs careful checking",
            "Gokshura: The plant behind the supplement marketing",
            "Bael/Bilva: Fruit, leaves, and traditional preparations",
            "Moringa/Shigru: Food plant and Ayurvedic ingredient",
            "Hibiscus: Botanical identity, hair traditions, and research",
            "Aloe/Kumari: Gel, latex, and why they should not be confused"
        ]
    },
    {
        "id": 3,
        "name": "Kitchen Spices Through an Ayurvedic Lens",
        "description": "Everyday culinary botanicals analyzed for flavor, digestive impact, and traditional uses.",
        "pillar": "Practical Lifestyle Education & Dietetics",
        "topics": [
            "Ginger: Fresh versus dried",
            "Black pepper: Culinary use versus concentrated extracts",
            "Pippali: How long pepper differs from black pepper",
            "Cumin: The seed’s culinary and traditional roles",
            "Coriander: Leaves versus dried fruits commonly called seeds",
            "Fennel: Food traditions and digestive claims",
            "Fenugreek: Seeds, leaves, and preparations",
            "Ajwain: Traditional household uses examined",
            "Cinnamon: Why species identification matters",
            "Cardamom: Green and black varieties compared",
            "Clove: The dried flower bud behind the spice",
            "Nutmeg: Culinary quantities versus unsafe experimentation",
            "Saffron: Cultivation, authenticity, and research",
            "Hing: The resin behind the kitchen ingredient",
            "Curry leaves: Food use and popular health claims",
            "Sesame: Seeds, oil, and traditional applications"
        ]
    },
    {
        "id": 4,
        "name": "Plant Anatomy and Identification",
        "description": "Visual series exploring macro and micro botanical features, morphology, and authentication.",
        "pillar": "Botanical Stories",
        "topics": [
            "How to identify an Ashwagandha plant",
            "Turmeric versus ginger: Rhizomes compared",
            "Tulsi varieties: A botanical identification guide",
            "Brahmi versus Mandukaparni: Why common names cause confusion",
            "What is a root, rhizome, tuber, bulb, or bark?",
            "How leaf arrangement helps identify a plant",
            "How flowers and fruits reveal plant identity",
            "Why a scientific name matters when buying herbs",
            "Why different plant parts are not interchangeable",
            "How drying changes a botanical specimen",
            "Whole herbs versus powders: What identification can reveal",
            "Why visual identification alone cannot authenticate every herbal product"
        ]
    },
    {
        "id": 5,
        "name": "Ayurvedic Food Principles",
        "description": "Ahara philosophy, meal timing, food compatibility, and culinary preparation dynamics.",
        "pillar": "Practical Lifestyle Education & Dietetics",
        "topics": [
            "Ahara: Why food occupies a central place in Ayurveda",
            "The six tastes illustrated with everyday foods",
            "What 'heavy' and 'light' mean in traditional food descriptions",
            "Freshly cooked food: Traditional reasoning and practical considerations",
            "Meal quantity: Classical ideas and modern portion awareness",
            "Meal timing: Tradition compared with nutrition research",
            "Eating attentively: Habit, pace, and environment",
            "Food preparation: How roasting, boiling, and grinding change ingredients",
            "Viruddha Ahara: Understanding the traditional concept of incompatible foods",
            "Why traditional food rules need context",
            "Fermented foods in Indian food traditions",
            "Ghee: Culinary role, traditional status, and nutrition",
            "Curd versus buttermilk: Preparation and traditional distinctions",
            "Honey: Traditional use and common internet claims",
            "Warm water: What tradition says and what evidence establishes",
            "Why 'Ayurvedic food' is broader than khichdi"
        ]
    },
    {
        "id": 6,
        "name": "Recipe and Food Demonstration Videos",
        "description": "Step-by-step wholesome cooking without turning food into medical treatments.",
        "pillar": "Practical Lifestyle Education & Dietetics",
        "topics": [
            "A simple moong dal khichdi",
            "Three regional variations of khichdi",
            "Yavagu: Exploring traditional rice gruel",
            "Manda and Peya: Traditional preparations explained",
            "A simple takra preparation and its ingredients",
            "Amla chutney",
            "Fresh ginger in everyday cooking",
            "Turmeric milk: Recipe, variations, and exaggerated claims",
            "A mild culinary cumin-coriander-fennel infusion",
            "Sesame chutney",
            "Moringa leaf dishes",
            "Seasonal vegetable soups using familiar Indian ingredients",
            "How to use six tastes without making a complicated meal",
            "Traditional recipes adapted for a busy workday"
        ]
    },
    {
        "id": 7,
        "name": "Dinacharya: Daily Routine",
        "description": "Actionable daily routines, circadian balance, and self-care practices for modern living.",
        "pillar": "Practical Lifestyle Education & Daily Regimen",
        "topics": [
            "What is Dinacharya?",
            "A realistic morning routine for working adults",
            "Brahma Muhurta: Traditional meaning and modern sleep schedules",
            "Tongue cleaning: Technique, hygiene, and realistic expectations",
            "Oil pulling: Traditional practice and evidence",
            "Abhyanga: The tradition of oil massage",
            "Choosing a massage oil: Ingredients and skin tolerance",
            "Bathing practices in traditional routines",
            "Exercise in Ayurveda: The idea of individual capacity",
            "Why more exercise is not always better",
            "Meal regularity during a busy day",
            "An evening wind-down routine",
            "Adapting routine for shift workers",
            "Which daily practices are optional, practical, or clinically supervised?"
        ]
    },
    {
        "id": 8,
        "name": "Ritucharya: Seasonal Living",
        "description": "Aligning nutrition, hydration, and habits with seasonal climate shifts and transitions.",
        "pillar": "Practical Lifestyle Education & Daily Regimen",
        "topics": [
            "What is Ritucharya?",
            "The six-season framework in Indian tradition",
            "Spring routines in classical descriptions",
            "Summer food and hydration topics",
            "Monsoon food hygiene and traditional practices",
            "Autumn routines in Ayurvedic literature",
            "Early winter food and activity traditions",
            "Late winter routines",
            "Ritusandhi: The transition between seasons",
            "Adapting seasonal advice to your actual climate",
            "Why an Indian seasonal calendar does not fit every country",
            "Seasonal local foods: A market-to-kitchen series"
        ]
    },
    {
        "id": 9,
        "name": "Digestion and Gut Health Education",
        "description": "Bridging Agni, microbiome science, bloating, motility, and evidence-based GI evaluation.",
        "pillar": "Tradition Examined Through Research & Clinical Science",
        "topics": [
            "Agni versus digestive enzymes: Why they are different frameworks",
            "Bloating: Possible causes beyond 'weak digestion'",
            "Constipation: Food, activity, medication, and medical evaluation",
            "Acidity and reflux: Why recurring symptoms deserve assessment",
            "Appetite changes: What to observe",
            "Dietary fiber: Where it fits into a traditional food discussion",
            "Gut microbiome claims in Ayurveda marketing",
            "Probiotics versus traditional fermented foods",
            "Spice water: What it can and cannot establish",
            "Elimination diets: Why unnecessary restriction can be a problem",
            "'Gut cleansing' claims examined",
            "Digestive symptoms that should not be self-treated indefinitely"
        ]
    },
    {
        "id": 10,
        "name": "Sleep, Stress, and Mental Wellbeing",
        "description": "Ayurvedic Nidra, adaptogens, neurobiology, slow breathing, and sleep architecture.",
        "pillar": "Practical Lifestyle Education & Mental Health",
        "topics": [
            "Nidra: Sleep within Ayurvedic thinking",
            "The traditional relationship between food, sleep, and wellbeing",
            "A practical evening routine for better sleep habits",
            "Ashwagandha and sleep: Reviewing human studies",
            "Brahmi and memory: What research actually measures",
            "Meditation and Ayurveda: Related practices, distinct histories",
            "Slow breathing: A beginner educational overview",
            "Caffeine timing and sleep",
            "Screen habits before bedtime",
            "Stress versus an anxiety disorder: Why the distinction matters",
            "Shirodhara: Traditional context, experience, and research limits",
            "Why persistent insomnia needs more than a supplement"
        ]
    },
    {
        "id": 11,
        "name": "Skin, Scalp, and Hair",
        "description": "Traditional topical oils and botanicals compared with modern dermatological science.",
        "pillar": "Botanical Stories & Practical Care",
        "topics": [
            "Ayurvedic skin care: Traditional practices versus product advertising",
            "Neem for skin: Forms, claims, and irritation risks",
            "Turmeric face masks: Staining, irritation, and expectations",
            "Aloe gel versus whole-leaf products",
            "Bhringraj hair oil: Ingredient story and evidence",
            "Amla hair oil: Preparation and realistic expectations",
            "Hibiscus in traditional hair care",
            "Hair oiling: Scalp, hair shaft, and washing habits",
            "Dandruff versus a dry scalp",
            "Hair fall: Why identifying the cause matters",
            "Essential oils versus infused oils",
            "Patch testing and homemade skin preparations"
        ]
    },
    {
        "id": 12,
        "name": "Women’s Health and Life Stages",
        "description": "Qualified clinician-focused explainers across cycles, perimenopause, and maternal care.",
        "pillar": "Tradition Examined Through Research & Clinical Care",
        "topics": [
            "Menstrual health: What is commonly misunderstood",
            "Shatavari: Traditional context and research questions",
            "PCOS: What an Ayurveda discussion should address",
            "Menopause: Symptoms, supportive habits, and treatment choices",
            "Iron deficiency versus vague 'weakness'",
            "Pregnancy: Why herbs require individual safety review",
            "Breastfeeding and herbal supplements: Evidence gaps",
            "Postpartum food traditions across Indian regions",
            "Fertility marketing: How to evaluate claims",
            "Bone health across adulthood",
            "Sleep and stress during perimenopause",
            "When menstrual symptoms need prompt medical attention"
        ]
    },
    {
        "id": 13,
        "name": "Men’s Health and Healthy Ageing",
        "description": "Rasayana concepts, hormonal health, muscle maintenance, and supplement evaluation.",
        "pillar": "Tradition Examined Through Research & Healthy Ageing",
        "topics": [
            "Ashwagandha and testosterone: Reading the evidence carefully",
            "'Stamina' supplements: What does the word actually mean?",
            "Gokshura and performance marketing",
            "Fertility claims: Lab markers versus meaningful outcomes",
            "Rasayana: The traditional rejuvenation concept",
            "Healthy ageing versus 'anti-ageing' promises",
            "Muscle maintenance: Food, activity, and ageing",
            "Joint discomfort: Why diagnosis comes first",
            "Memory changes: Everyday forgetfulness versus concerning symptoms",
            "Polypharmacy: Why supplement interactions matter more with multiple medicines",
            "Appetite and nutrition in older adults",
            "What longevity studies can—and cannot—tell us"
        ]
    },
    {
        "id": 14,
        "name": "Classical Formulations and Preparation Methods",
        "description": "Inside traditional pharmaceutics: churnas, kwathas, ghritas, tailas, and asavas.",
        "pillar": "Tradition Examined Through Research & Pharmaceutics",
        "topics": [
            "Triphala: Its three ingredients and traditional context",
            "Trikatu: Its ingredients and intended traditional role",
            "Chyawanprash: History, ingredients, and product variation",
            "Dashamoola: Understanding a multi-ingredient group",
            "Churna: What a powdered preparation is",
            "Kwatha/Kashaya: How decoctions differ from tea",
            "Phanta and Hima: Traditional infusion methods",
            "Avaleha: Understanding herbal preparations in a paste-like base",
            "Ghrita: Medicated ghee preparations explained",
            "Taila: Medicated oils explained",
            "Asava and Arishta: Fermentation and product considerations",
            "Why a classical name does not guarantee identical products"
        ]
    },
    {
        "id": 15,
        "name": "Panchakarma and Clinical Therapies",
        "description": "In-depth clinical exploration of classical fivefold detox therapies vs commercial spas.",
        "pillar": "Tradition Examined Through Research & Clinical Therapies",
        "topics": [
            "What Panchakarma means in classical and contemporary practice",
            "Panchakarma versus a spa package",
            "Purvakarma: Preparatory procedures explained",
            "Snehana: Internal and external oleation in context",
            "Swedana: Traditional sudation procedures",
            "Vamana: What the clinical procedure involves",
            "Virechana: What the clinical procedure involves",
            "Basti: Its place in Ayurvedic clinical practice",
            "Nasya: Different forms and supervision considerations",
            "Raktamokshana: Historical and clinical context",
            "Why Shirodhara and Abhyanga are not synonyms for Panchakarma",
            "What to ask before booking a treatment programme",
            "Consent, hygiene, screening, and practitioner qualifications",
            "What does 'detoxification' mean in the treatment being advertised?"
        ]
    },
    {
        "id": 16,
        "name": "Classical Texts, History, and People",
        "description": "Manuscript history, historical figures, Brihat Trayi, Laghu Trayi, and medical evolution.",
        "pillar": "Tradition Examined Through Research & History",
        "topics": [
            "Charaka Samhita: What kind of text is it?",
            "Sushruta Samhita: Surgery and medical history",
            "Ashtanga Hridaya: An introduction",
            "Ashtanga Sangraha: How to approach the text",
            "Madhava Nidana: A text-focused documentary",
            "Sharangadhara Samhita: Preparation and clinical traditions",
            "Bhavaprakasha: Materia medica and historical context",
            "What is an Ayurvedic Nighantu?",
            "Manuscripts, commentaries, and changing interpretations",
            "Ayurveda’s relationship with Sanskrit learning",
            "Ayurveda and regional languages",
            "Medical education in historical India",
            "How plant names change across texts and regions",
            "Dhanvantari: Religious and cultural significance",
            "Ayurveda in the colonial period",
            "Ayurveda in contemporary education and research"
        ]
    },
    {
        "id": 17,
        "name": "Research, Safety, and Product Literacy",
        "description": "Critical thinking, reading clinical trials, testing certificates, and consumer safety.",
        "pillar": "Tradition Examined Through Research & Product Safety",
        "topics": [
            "Traditional use versus clinical evidence",
            "A laboratory result is not a proven human benefit",
            "Animal studies versus human trials",
            "How to read a herbal clinical trial",
            "Why sample size matters",
            "Why extract, dose, and preparation matter",
            "A statistically significant result versus a useful benefit",
            "How to spot exaggerated supplement claims",
            "Natural does not automatically mean safe",
            "Herb–medicine interactions explained",
            "Heavy metals: Intentional ingredients versus contamination",
            "What a product testing certificate can show",
            "Why 'standardized extract' needs further explanation",
            "How to report a suspected adverse reaction",
            "Pregnancy, childhood, and chronic illness: Why evidence may differ",
            "When to stop a product and seek clinical advice"
        ]
    },
    {
        "id": 18,
        "name": "Myth-Checking and Comparison Videos",
        "description": "Rigorous investigation of viral wellness myths, exaggerated claims, and internet misconceptions.",
        "pillar": "Tradition Examined Through Research & Myth-Busting",
        "topics": [
            "Does 'Ayurvedic' always mean plant-based?",
            "Does Ayurveda recommend the same routine for everyone?",
            "Can you determine your constitution from a short quiz?",
            "Is every bitter plant beneficial?",
            "Does more turmeric mean more benefit?",
            "Is turmeric powder equivalent to a curcumin extract?",
            "Are all Tulsi products interchangeable?",
            "Is Triphala suitable for everyone?",
            "Can a herbal drink 'clean' the liver?",
            "Does 'immunity booster' tell you anything precise?",
            "Does traditional use prove that a product is safe?",
            "Can pulse examination replace medical investigations?",
            "Are expensive imported herbs better than familiar local foods?",
            "Does an 'ancient formula' have one fixed modern composition?",
            "Ayurveda and modern medicine: How to discuss them without false equivalence",
            "Why 'permanent cure' claims deserve scrutiny"
        ]
    },
    {
        "id": 19,
        "name": "Field Documentaries and Behind-the-Scenes Stories",
        "description": "Visual documentary series touring farms, botanical labs, processing centers, and archives.",
        "pillar": "Botanical Stories & Field Reporting",
        "topics": [
            "An Ashwagandha farm through the growing season",
            "Turmeric: From rhizome planting to harvest",
            "Amla: From orchard to food preparation",
            "A medicinal plant garden tour",
            "A botanical authentication laboratory visit",
            "How herb samples are tested for contamination",
            "Inside a herbal drying facility",
            "Whole herb to finished product: Following one batch",
            "Cultivated versus wild-harvested plants",
            "Sustainable harvesting of roots and bark",
            "The conservation story behind a medicinal plant",
            "Meet a botanist working with medicinal plants",
            "Meet an Ayurvedic physician: Training and clinical responsibilities",
            "Regional household traditions documented with context",
            "A manuscript archive or medical history museum visit",
            "Herbal market names versus verified botanical identities"
        ]
    },
    {
        "id": 20,
        "name": "Shorts and Recurring Micro-Series",
        "description": "60-second high-density visual explainers, quizzes, label audits, and terminology breakdowns.",
        "pillar": "Short-Form Micro-Series & Audience Engagement",
        "topics": [
            "One Ayurvedic term in 60 seconds",
            "Guess the herb from its root",
            "Guess the plant from its leaf",
            "One plant, three different common names",
            "Root versus rhizome: A visual comparison",
            "Fresh ginger versus dried ginger",
            "One ingredient inside Triphala",
            "One misleading supplement label phrase",
            "One research claim explained simply",
            "One traditional belief checked against a source",
            "One seasonal food story",
            "One botanical naming mistake",
            "One question to ask before buying a supplement",
            "One difference between food and a concentrated extract",
            "One historical passage explained in plain English",
            "One viewer question answered with a qualified expert"
        ]
    }
]

# 4. Repeatable 8-Part Herb Series Framework
HERB_SERIES_STRUCTURE = [
    {"ep": 1, "focus": "Botanical Identity", "prompt": "What does the real plant look like, its taxonomic traits and morphological markers?"},
    {"ep": 2, "focus": "Plant Anatomy", "prompt": "Why are specific plant parts (roots, leaves, seeds, bark, resin) the main commercial and medicinal material?"},
    {"ep": 3, "focus": "Traditional Context", "prompt": "How is it described across classical Ayurvedic treatises (Charaka, Sushruta, Nighantus)?"},
    {"ep": 4, "focus": "Preparation", "prompt": "Whole herb vs. powder (Churna) vs. decoction (Kwatha) vs. standardized extract?"},
    {"ep": 5, "focus": "Research", "prompt": "What have randomized double-blind human clinical trials actually measured?"},
    {"ep": 6, "focus": "Safety", "prompt": "Documented adverse effects, organ toxicity risks, herb-drug interactions, and contraindications."},
    {"ep": 7, "focus": "Product Literacy", "prompt": "What should viewers look for on commercial product labels, testing certificates, and purity seals?"},
    {"ep": 8, "focus": "Origin Story", "prompt": "Agricultural lifecycle: cultivation, sustainable wild harvesting, processing, and supply chain."}
]

# 20 Featured Medicinal Plants for the 8-Part Series (160 distinct episodes)
FEATURED_HERBS = [
    {"name": "Ashwagandha", "botanical": "Withania somnifera", "part": "Roots", "family": "Solanaceae"},
    {"name": "Turmeric", "botanical": "Curcuma longa", "part": "Rhizome", "family": "Zingiberaceae"},
    {"name": "Tulsi", "botanical": "Ocimum sanctum / tenuiflorum", "part": "Leaves & aerial parts", "family": "Lamiaceae"},
    {"name": "Amla", "botanical": "Phyllanthus emblica", "part": "Fruit", "family": "Phyllanthaceae"},
    {"name": "Neem", "botanical": "Azadirachta indica", "part": "Leaves, bark, seeds", "family": "Meliaceae"},
    {"name": "Brahmi", "botanical": "Bacopa monnieri", "part": "Whole creeping herb", "family": "Plantaginaceae"},
    {"name": "Mandukaparni", "botanical": "Centella asiatica", "part": "Fan-shaped leaves", "family": "Apiaceae"},
    {"name": "Shatavari", "botanical": "Asparagus racemosus", "part": "Tuberous roots", "family": "Asparagaceae"},
    {"name": "Guduchi / Giloy", "botanical": "Tinospora cordifolia", "part": "Stem", "family": "Menispermaceae"},
    {"name": "Mulethi / Yashtimadhu", "botanical": "Glycyrrhiza glabra", "part": "Root & stolon", "family": "Fabaceae"},
    {"name": "Haritaki", "botanical": "Terminalia chebula", "part": "Fruit pericarp", "family": "Combretaceae"},
    {"name": "Bibhitaki", "botanical": "Terminalia bellirica", "part": "Fruit", "family": "Combretaceae"},
    {"name": "Arjuna", "botanical": "Terminalia arjuna", "part": "Stem bark", "family": "Combretaceae"},
    {"name": "Guggulu", "botanical": "Commiphora mukul", "part": "Oleo-gum resin", "family": "Burseraceae"},
    {"name": "Punarnava", "botanical": "Boerhavia diffusa", "part": "Root & whole plant", "family": "Nyctaginaceae"},
    {"name": "Manjistha", "botanical": "Rubia cordifolia", "part": "Roots & stems", "family": "Rubiaceae"},
    {"name": "Bhringraj", "botanical": "Eclipta alba", "part": "Whole herb", "family": "Asteraceae"},
    {"name": "Jatamansi", "botanical": "Nardostachys jatamansi", "part": "Rhizomes & roots", "family": "Caprifoliaceae"},
    {"name": "Shankhapushpi", "botanical": "Convolvulus pluricaulis", "part": "Whole flowering plant", "family": "Convolvulaceae"},
    {"name": "Gokshura", "botanical": "Tribulus terrestris", "part": "Spiny fruit & root", "family": "Zygophyllaceae"}
]

# 5. High-Retention / Trending Topics
TRENDING_TOPICS = [
    {"id": 1, "title": "Shilajit: The Himalayan Resin Explained — Testosterone, Fulvic Acid & Lab Scams", "trend_score": "Trending #1 (Ultra High Volume)", "angle": "claim_evidence", "slug": "shilajit_resin_fulvic_acid_testosterone_lab_testing", "why": "Massive viral explosion across fitness & wellness YouTube; consumers desperate for lab purity checks."},
    {"id": 2, "title": "The Golden Milk Trend: Ancient Turmeric Latte Recipe vs Viral TikTok Mistakes", "trend_score": "High Ever-Green Trend", "angle": "myths_vs_facts", "slug": "golden_milk_turmeric_latte_ayurvedic_science_vs_tiktok", "why": "Global viral drink; breaks down critical fat-piperine absorption mistakes viewers make."},
    {"id": 3, "title": "Castor Oil Packs & Navel Oiling (Nabhi Chikitsa): Fact vs Pseudoscience", "trend_score": "Viral Trend (High TikTok & Shorts Spike)", "angle": "myths_vs_facts", "slug": "castor_oil_nabhi_chikitsa_navel_oiling_science_vs_hype", "why": "Flooding social feeds; requires grounded historical text verification vs modern internet claims."},
    {"id": 4, "title": "Somatic Fasting (Langhana): How Ayurvedic Fasting Stimulates Autophagy", "trend_score": "Trending Scientific Angle", "angle": "how_it_works", "slug": "ayurvedic_fasting_langhana_autophagy_cellular_longevity", "why": "Bridges ancient fasting classifications (Langhana) with modern Nobel Prize autophagy science."},
    {"id": 5, "title": "Copper Water Vessels (Tamra Jal): Antimicrobial Power vs Copper Toxicity Risks", "trend_score": "High Search Everyday Query", "angle": "how_it_works", "slug": "copper_water_tamra_jal_antimicrobial_benefits_and_toxicity", "why": "Ubiquitous household health habit; viewers need safety guidelines (8-hour limit) to avoid heavy metal toxicity."},
    {"id": 6, "title": "Adaptogens for High-Performance: Ashwagandha vs Holy Basil (Tulsi) for Cortisol", "trend_score": "High Productivity/Wellness Crossover", "angle": "claim_evidence", "slug": "adaptogens_ashwagandha_vs_tulsi_holy_basil_cortisol_stress", "why": "High RPM audience of biohackers, entrepreneurs, and busy professionals seeking burnout relief."}
]

def generate_master_roadmap_md():
    lines = []
    lines.append("# Ayurveda Channel Master Topic Roadmap (Scratch to Advanced)")
    lines.append("**Niche:** 281 Ayurveda (Medicine_Healthcare)  ")
    lines.append("**Channel Language:** English (YouTube)  ")
    lines.append("**Target Audience:** Ayurveda Researchers, Healthcare Specialists, Documentary Viewers, General Public (Global)  ")
    lines.append("**Production Format:** 10 to 30-Minute In-Depth Documentary Explainer Episodes (600s–1800s, 75–225 Fixed 8s Scenes)  ")
    lines.append("**Execution & Sync Report:** [topics/281_ayurveda/TOPICS_COVERED_REPORT.md](./TOPICS_COVERED_REPORT.md)  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Channel Core Architecture: Three Pillars")
    lines.append("")
    lines.append("Rather than narrowing the channel to repetitive 'herb benefits' videos, the channel is built around three synergistic editorial pillars:")
    lines.append("1. **Botanical Stories** — Plant anatomy, morphology, wild-harvesting vs. cultivation, authentication, and the physical life of medicinal flora.")
    lines.append("2. **Practical Lifestyle Education** — Actionable Dinacharya (circadian routines), Ritucharya (seasonal adaptation), Ahara (food principles), home kitchen spices, and wholesome culinary demonstrations.")
    lines.append("3. **Tradition Examined Through Research** — Classical Sanskrit treatises (Brihat Trayi) audited against modern double-blind randomized clinical trials, pharmacology, safety pharmacovigilance, and consumer product literacy.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Four-Tier Curriculum Progression")
    lines.append("")
    lines.append("- **Tier 1: Foundations (Scratch / Beginner)** — Core philosophies, Panchamahabhutas (5 elements), Tridosha (Vata, Pitta, Kapha), Agni (digestive fire), Ama (metabolic waste), Dhatus (tissues), and constitutional self-understanding.")
    lines.append("- **Tier 2: Daily Lifestyle & Preventive Living (Intermediate)** — Translating principles into actionable circadian habits, seasonal living, Ahara nutritional science, and mental hygiene.")
    lines.append("- **Tier 3: Formulations, Herbology & Clinical Therapies (Upper Intermediate)** — Classical monographs, synergistic formulations (Triphala, Trikatu, Chyawanprash), Panchakarma clinical protocols, and pharmacology.")
    lines.append("- **Tier 4: Advanced Pathology, Safety & Integrative Horizons (Advanced / Expert)** — Classical pathogenesis (*Samprapti*), 8-fold diagnosis (*Ashtavidha Pariksha*), Rasa Shastra heavy metal toxicology, Ayurgenomics (DNA & Prakriti), and clinical research literacy.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Flagship Produced Foundation Episodes (Phase 0–5 Completed)")
    lines.append("The initial 20 core foundation episodes are fully researched and produced in `OUTPUT/281_ayurveda/`:")
    lines.append("")
    lines.append("| # | Episode Title | Curriculum Tier | Angle Preset | Output Project Folder |")
    lines.append("|---|---|---|---|---|")
    for ep in COMPLETED_EPISODES:
        folder_link = f"../../OUTPUT/281_ayurveda/{ep['folder']}"
        lines.append(f"| {ep['id']} | **{ep['title']}** | {ep['tier']} | `{ep['angle']}` | [{ep['folder']}]({folder_link}) |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. Suggested Editorial First 20 Uploads (Launch Sequence)")
    lines.append("Curated editorial sequence balancing beginner foundations, high-interest botanicals, daily routines, and evidence checks:")
    lines.append("")
    lines.append("| # | Working Video Title | Focus Area & Angle | Curriculum Tier |")
    lines.append("|---|---|---|---|")
    for up in FIRST_20_UPLOADS:
        lines.append(f"| {up['num']} | **{up['title']}** | `{up['angle']}` | {up['tier']} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 5. Master Topic Bank: 20 Themed Playlists (282 Core Topics)")
    lines.append("A complete editorial topic bank structured into 20 thematic playlists across all channel pillars:")
    lines.append("")
    
    total_topics = 0
    for pl in PLAYLISTS:
        total_topics += len(pl["topics"])
        lines.append(f"### Playlist {pl['id']}: {pl['name']} ({len(pl['topics'])} Topics)")
        lines.append(f"*{pl['description']}*  ")
        lines.append(f"**Channel Pillar:** {pl['pillar']}  ")
        lines.append("")
        for idx, top in enumerate(pl["topics"], 1):
            lines.append(f"- **{top}**")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    lines.append("## 6. Repeatable 8-Part Botanical Documentary Franchise (160 Episodes)")
    lines.append("Rather than producing generic single 'benefits' videos, each featured plant receives a dedicated 8-episode documentary series exploring its complete lifecycle from field to lab:")
    lines.append("")
    lines.append("### The 8-Episode Botanical Documentary Blueprint")
    lines.append("")
    lines.append("| Ep | Focus Phase | Core Documentary Scope & Visual Direction |")
    lines.append("|---|---|---|")
    for st in HERB_SERIES_STRUCTURE:
        lines.append(f"| {st['ep']} | **{st['focus']}** | {st['prompt']} |")
    lines.append("")
    lines.append("### 20 Featured Medicinal Plants (20 Plants x 8 Episodes = 160 Episodes)")
    lines.append("")
    lines.append("| # | Plant Common Name | Botanical Binomial | Primary Commercial/Medicinal Part | Botanical Family |")
    lines.append("|---|---|---|---|---|")
    for idx, h in enumerate(FEATURED_HERBS, 1):
        lines.append(f"| {idx} | **{h['name']}** | *{h['botanical']}* | {h['part']} | {h['family']} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 7. High-Retention & Trending Candidates")
    lines.append("")
    lines.append("| # | Video Title | Viral Velocity | Angle | Why It Performs |")
    lines.append("|---|---|---|---|---|")
    for t in TRENDING_TOPICS:
        lines.append(f"| {t['id']} | **{t['title']}** | **{t['trend_score']}** | `{t['angle']}` | {t['why']} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 8. Cross-Repository Wiring")
    lines.append("- **Topic Execution Report:** [`topics/281_ayurveda/TOPICS_COVERED_REPORT.md`](file:///h:/script-raw-/topics/281_ayurveda/TOPICS_COVERED_REPORT.md)")
    lines.append("- **Machine Registry:** [`topics/281_ayurveda/topics_status.json`](file:///h:/script-raw-/topics/281_ayurveda/topics_status.json)")
    lines.append("- **Niche Home:** [`REGISTRY/Niches/281_ayurveda/NICHE_281_ayurveda.md`](file:///h:/script-raw-/REGISTRY/Niches/281_ayurveda/NICHE_281_ayurveda.md)")
    lines.append("- **Category Configuration:** [`REGISTRY/Niches/281_ayurveda/CAT_281_ayurveda.md`](file:///h:/script-raw-/REGISTRY/Niches/281_ayurveda/CAT_281_ayurveda.md)")
    lines.append("- **Production Output Root:** [`OUTPUT/281_ayurveda/`](file:///h:/script-raw-/OUTPUT/281_ayurveda/)")
    
    return "\n".join(lines)

def generate_sync_report_md():
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_completed = len(COMPLETED_EPISODES)
    total_playlist_topics = sum(len(p["topics"]) for p in PLAYLISTS)
    total_herb_episodes = len(FEATURED_HERBS) * 8
    total_trending = len(TRENDING_TOPICS)
    grand_catalog = total_completed + total_playlist_topics + total_herb_episodes + total_trending

    lines = []
    lines.append("# 281 Ayurveda -- Master Topic Execution & Roadmap Sync Report")
    lines.append(f"> **Niche:** 281 Ayurveda (Medicine_Healthcare)  ")
    lines.append(f"> **Storage Directory:** `topics/281_ayurveda/`  ")
    lines.append(f"> **Synchronized With:** `OUTPUT/281_ayurveda/`, `REGISTRY/Niches/281_ayurveda/`, and `281_AYURVEDA_CHANNEL_TOPIC_ROADMAP.md`  ")
    lines.append(f"> **Last Synced:** `{now_str}`  ")
    lines.append(f"> **Production Format:** 10 to 30-Minute In-Depth Episodes (600s–1800s, 75–225 Fixed 8s Scenes, Strict 4.2–5.6s VO Ceiling)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Executive Progress Summary")
    lines.append("")
    lines.append("| Metric | Count | Percentage | Status |")
    lines.append("|---|---|---|---|")
    lines.append(f"| **Foundation Episodes Completed & Produced (Phases 0-5)** | **{total_completed}** | **{round((total_completed/grand_catalog)*100, 1)}%** | `COMPLETED IN OUTPUT (Ready for Rendering)` |")
    lines.append(f"| **Playlist Topic Bank Queue (20 Thematic Playlists)** | **{total_playlist_topics}** | **{round((total_playlist_topics/grand_catalog)*100, 1)}%** | `ACTIVE CURRICULUM QUEUE` |")
    lines.append(f"| **Botanical Documentary Franchise (20 Herbs x 8 Eps)** | **{total_herb_episodes}** | **{round((total_herb_episodes/grand_catalog)*100, 1)}%** | `PLANNED FRANCHISE REPERTORY` |")
    lines.append(f"| **Trending & High-Retention Candidates** | **{total_trending}** | **{round((total_trending/grand_catalog)*100, 1)}%** | `ALGORITHM & RETENTION OPTIMIZED` |")
    lines.append(f"| **Total Tracked Master Catalog** | **{grand_catalog}** | **100%** | `Full Strategic Channel Architecture` |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Covered Topics (Done / Produced in OUTPUT)")
    lines.append("All 20 flagship foundation episodes are completely written through Phase 5 Final Audit in `OUTPUT/281_ayurveda/`:")
    lines.append("")
    lines.append("| # | Topic Title | Curriculum Tier | Angle Preset | Associated Output Folder & Files | Status |")
    lines.append("|---|---|---|---|---|---|")
    for ep in COMPLETED_EPISODES:
        folder_link = f"../../OUTPUT/281_ayurveda/{ep['folder']}"
        lines.append(f"| {ep['id']} | **{ep['title']}** | {ep['tier']} | `{ep['angle']}` | [{ep['folder']}]({folder_link}) | <mark>**{ep['status']}**</mark> |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Priority Next Launch Sequence (Suggested First 20 Uploads)")
    lines.append("Curated editorial launch queue balancing foundations, popular botanicals, daily living, and evidence reviews:")
    lines.append("")
    lines.append("| # | Working Video Title | Recommended Angle | Target Tier | Launch Priority |")
    lines.append("|---|---|---|---|---|")
    for up in FIRST_20_UPLOADS:
        lines.append(f"| {up['num']} | **{up['title']}** | `{up['angle']}` | {up['tier']} | `QUEUED FOR PRODUCTION` |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. The 20 Curated Playlists (282 Core Topics Summary)")
    lines.append("")
    lines.append("| Playlist # | Playlist Name | Core Theme | Topic Count | Key Focus |")
    lines.append("|---|---|---|---|---|")
    for pl in PLAYLISTS:
        lines.append(f"| **{pl['id']}** | **{pl['name']}** | {pl['pillar']} | **{len(pl['topics'])}** | {pl['description']} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. Botanical Documentary Franchise (20 Plants x 8 Episodes = 160 Episodes)")
    lines.append("Repeatable 8-episode documentary structure covering Botanical Identity, Anatomy, Traditional Context, Preparation, Research, Safety, Product Literacy, and Origin Story:")
    lines.append("")
    lines.append("| # | Botanical Name | Common Name | Commercial Part | 8-Part Series Status |")
    lines.append("|---|---|---|---|---|")
    for idx, h in enumerate(FEATURED_HERBS, 1):
        lines.append(f"| {idx} | *{h['botanical']}* | **{h['name']}** | {h['part']} | `PLANNED (8 Episodes)` |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 5. Trending & High-Retention Topics (Algorithm & Search Optimized)")
    lines.append("")
    lines.append("| # | Trending Concept | Trend Velocity | Angle | Recommended Slug | Retention Hook & Value | Status |")
    lines.append("|---|---|---|---|---|---|---|")
    for t in TRENDING_TOPICS:
        lines.append(f"| {t['id']} | **{t['title']}** | **{t['trend_score']}** | `{t['angle']}` | `{t['slug']}` | {t['why']} | `Queued` |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 6. Cross-Document Sync & File Linkages")
    lines.append("- **Master Channel Roadmap:** [`topics/281_ayurveda/281_AYURVEDA_CHANNEL_TOPIC_ROADMAP.md`](file:///h:/script-raw-/topics/281_ayurveda/281_AYURVEDA_CHANNEL_TOPIC_ROADMAP.md)")
    lines.append("- **Output Topic Roadmap:** [`OUTPUT/281_ayurveda/AYURVEDA_CHANNEL_TOPIC_ROADMAP.md`](file:///h:/script-raw-/OUTPUT/281_ayurveda/AYURVEDA_CHANNEL_TOPIC_ROADMAP.md)")
    lines.append("- **Machine Status JSON:** [`topics/281_ayurveda/topics_status.json`](file:///h:/script-raw-/topics/281_ayurveda/topics_status.json)")
    lines.append("- **Niche Registry Home:** [`REGISTRY/Niches/281_ayurveda/NICHE_281_ayurveda.md`](file:///h:/script-raw-/REGISTRY/Niches/281_ayurveda/NICHE_281_ayurveda.md)")
    lines.append("- **Category Configuration:** [`REGISTRY/Niches/281_ayurveda/CAT_281_ayurveda.md`](file:///h:/script-raw-/REGISTRY/Niches/281_ayurveda/CAT_281_ayurveda.md)")
    lines.append("- **Angle Plan Data:** [`REGISTRY/Niches/281_ayurveda/ANGLE_PLAN.json`](file:///h:/script-raw-/REGISTRY/Niches/281_ayurveda/ANGLE_PLAN.json)")
    lines.append("- **Output Landing Directory:** [`OUTPUT/281_ayurveda/`](file:///h:/script-raw-/OUTPUT/281_ayurveda/)")
    lines.append("")
    lines.append("---")
    lines.append("*Generated by Script-Raw Workspace Topic Tracking Engine.*")
    
    return "\n".join(lines)

def generate_topics_status_json():
    total_completed = len(COMPLETED_EPISODES)
    total_playlist_topics = sum(len(p["topics"]) for p in PLAYLISTS)
    total_herb_episodes = len(FEATURED_HERBS) * 8
    total_trending = len(TRENDING_TOPICS)
    grand_catalog = total_completed + total_playlist_topics + total_herb_episodes + total_trending

    data = {
        "niche_id": "281",
        "niche_name": "ayurveda",
        "last_synced": datetime.now().isoformat(),
        "summary": {
            "completed": total_completed,
            "playlist_topics": total_playlist_topics,
            "botanical_franchise_episodes": total_herb_episodes,
            "trending": total_trending,
            "first_20_upload_queue": len(FIRST_20_UPLOADS),
            "total_catalog": grand_catalog
        },
        "completed_topics": COMPLETED_EPISODES,
        "first_20_uploads_queue": FIRST_20_UPLOADS,
        "playlists": PLAYLISTS,
        "botanical_franchise": {
            "structure": HERB_SERIES_STRUCTURE,
            "featured_herbs": FEATURED_HERBS
        },
        "trending_topics": TRENDING_TOPICS
    }
    return data

def main():
    print("Generating comprehensive Ayurveda topic architecture...")
    
    # 1. Write topics/281_ayurveda/281_AYURVEDA_CHANNEL_TOPIC_ROADMAP.md
    roadmap_path = TOPICS_DIR / "281_AYURVEDA_CHANNEL_TOPIC_ROADMAP.md"
    roadmap_content = generate_master_roadmap_md()
    with open(roadmap_path, "w", encoding="utf-8") as f:
        f.write(roadmap_content)
    print(f"Written: {roadmap_path}")
    
    # 2. Mirror into OUTPUT/281_ayurveda/AYURVEDA_CHANNEL_TOPIC_ROADMAP.md
    output_roadmap_path = OUTPUT_DIR / "AYURVEDA_CHANNEL_TOPIC_ROADMAP.md"
    with open(output_roadmap_path, "w", encoding="utf-8") as f:
        f.write(roadmap_content)
    print(f"Written: {output_roadmap_path}")
    
    # 3. Write topics/281_ayurveda/TOPICS_COVERED_REPORT.md
    report_path = TOPICS_DIR / "TOPICS_COVERED_REPORT.md"
    report_content = generate_sync_report_md()
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Written: {report_path}")
    
    # 4. Write topics/281_ayurveda/topics_status.json
    status_path = TOPICS_DIR / "topics_status.json"
    status_data = generate_topics_status_json()
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(status_data, f, indent=2)
    print(f"Written: {status_path}")
    
    # 5. Update topics/README.md row 281
    master_index_path = ROOT_DIR / "topics" / "README.md"
    if master_index_path.exists():
        with open(master_index_path, "r", encoding="utf-8") as f:
            idx_content = f.read()
        old_row = "| **281** | **Ayurveda** | **0** | **20** | **7** | [281_ayurveda Report](./281_ayurveda/TOPICS_COVERED_REPORT.md) |"
        new_row = f"| **281** | **Ayurveda** | **20** | **458** | **6** | [281_ayurveda Report](./281_ayurveda/TOPICS_COVERED_REPORT.md) |"
        if old_row in idx_content:
            idx_content = idx_content.replace(old_row, new_row)
            with open(master_index_path, "w", encoding="utf-8") as f:
                f.write(idx_content)
            print("Updated topics/README.md row 281")
        else:
            print("Note: old_row not found exactly in topics/README.md")
            
    print("All Ayurveda topic integrations completed successfully!")

if __name__ == "__main__":
    main()
