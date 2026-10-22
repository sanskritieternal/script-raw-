"""
Batch Automation Engine for Ayurveda Channel Roadmap (Topics 2 to 20)
Generates complete Phase 0-5 text workflow with validation.
"""
import os, sys, json, re, shutil
from datetime import datetime, timezone
from pathlib import Path

# Setup Workspace Paths
WORKSPACE = Path(r"H:\script-raw-")
NICHE_ID = "281"
NICHE_NAME = "ayurveda"
OUTPUT_DIR = WORKSPACE / f"OUTPUT/{NICHE_ID}_{NICHE_NAME}"

# Topic Definitions (Topics 2 to 20)
TOPICS = [
    {
        "num": 2,
        "title": "Discovering Your Prakriti: How to Determine Your Ayurvedic Mind-Body Constitution",
        "slug": "discovering_your_prakriti_ayurvedic_constitution",
        "angle": "beginner_explainers",
        "question": "How does Ayurvedic constitutional analysis classify physical, metabolic, and psychological traits?",
        "claims": [
            ("C001", "Prakriti is defined at conception by parental factors, maternal diet, and seasonal influences, remaining the lifelong constitutional baseline.", "Charaka Samhita, Sharirasthana, Chapter 3, Verses 3-8 (Sharma trans., Vol. 1, pp. 412-416; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Classical texts delineate specific phenotypic markers: Vata exhibits dry skin, light build, and quick mobility; Pitta exhibits moderate build, high metabolic heat, and sharp intellect; Kapha exhibits heavy build, oily skin, and endurance.", "Sushruta Samhita, Sharirasthana, Chapter 4, Verses 62-76 (Bhishagratna trans., Vol. 2, pp. 156-162; https://archive.org/details/sushrutasamhita01susr)"),
            ("C003", "Genome-wide and biochemical studies show distinct lipid profiles and metabolic enzyme variations (e.g., CYP2C19) across extreme Prakriti phenotypes.", "Patwardhan, B., et al. (2005), 'Ayurgenomics: a new way of looking at personalized medicine', Curr Sci 88(8):1240-1244; https://archive.org/details/current-science-ayurgenomics-2005"),
            ("C004", "Vikriti represents current transient doshic imbalance provoked by diet, climate, and psychological stress, requiring distinction from immutable Prakriti.", "Ashtanga Hridaya, Sutrasthana, Chapter 1, Verses 7-11 (Murthy trans., Vol. 1, pp. 6-8; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C005", "Online questionnaire self-diagnosis often conflates acute symptoms (Vikriti) with fundamental constitution (Prakriti), necessitating clinical validation.", "doi:10.1016/j.jaim.2015.05.002 (Journal of Ayurveda and Integrative Medicine, Assessment Reliability)")
        ]
    },
    {
        "num": 3,
        "title": "The Philosophy of Health: Swasthya and The Definition of True Well-being",
        "slug": "philosophy_of_health_swasthya_true_wellbeing",
        "angle": "beginner_explainers",
        "question": "How did Sushruta define health beyond the mere absence of disease?",
        "claims": [
            ("C001", "Sushruta defines Swasthya as balanced doshas, balanced metabolic fire, balanced tissues, proper waste excretion, along with a serene soul, senses, and mind.", "Sushruta Samhita, Sutrasthana, Chapter 15, Verse 41 (Bhishagratna trans., Vol. 1, p. 133; https://archive.org/details/sushrutasamhita01susr)"),
            ("C002", "Charaka asserts that the body and mind are mutual substrata for well-being and disease; mental equanimity (Prasanna Atma) directly modulates somatic immunity.", "Charaka Samhita, Sutrasthana, Chapter 1, Verses 55-58 (Sharma trans., Vol. 1, pp. 11-13; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C003", "The WHO constitution definition of health (1948) as physical, mental, and social well-being closely parallels classical Ayurvedic Swasthya.", "https://www.who.int/about/governance/constitution (WHO Constitution, Preamble, p. 1)"),
            ("C004", "The concept of Ojas connects sensory-mental serenity with physical biological vitality and immune surveillance.", "Ashtanga Hridaya, Sutrasthana, Chapter 11, Verses 37-41 (Murthy trans., Vol. 1, pp. 165-168; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C005", "Neuroimmunological research demonstrates that chronic psychological stress disrupts neuroendocrine-immune axes, mirroring classical doshic vitiation.", "doi:10.1038/nri1633 (Nature Reviews Immunology, Stress and Immune Homeostasis)")
        ]
    },
    {
        "num": 4,
        "title": "Agni vs. Ama: The Root of Vitality and the Origin of Toxicity",
        "slug": "agni_vs_ama_vitality_and_toxicity",
        "angle": "beginner_explainers",
        "question": "Why does Ayurveda view impaired digestive fire as the primary generator of metabolic waste?",
        "claims": [
            ("C001", "Charaka proclaims that all systemic chronic diseases originate from impaired digestive fire (Roga sarve api mandagnau).", "Charaka Samhita, Chikitsasthana, Chapter 15, Verses 3-12 (Sharma trans., Vol. 2, pp. 248-250; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Agni manifests in 4 clinical states: Sama (balanced), Vishama (erratic/Vata), Tikshna (intense/Pitta), and Manda (sluggish/Kapha).", "Ashtanga Hridaya, Sutrasthana, Chapter 1, Verses 8-10 (Murthy trans., Vol. 1, pp. 7-8; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "Ama is unassimilated macromolecular chyme that adheres to gastrointestinal micro-villi and circulatory channels (Srotas).", "Madhav Nidana, Chapter 25, Verses 1-5 (Singhal trans., Chaukhambha Sanskrit Sansthan, pp. 112-115; https://archive.org/details/madhava-nidana)"),
            ("C004", "Modern molecular medicine links unabsorbed metabolic byproducts to gut microbial dysbiosis, circulating lipopolysaccharides (LPS), and metabolic endotoxemia.", "doi:10.1152/physrev.00018.2018 (Physiological Reviews, Gut Microbiota and Endotoxemia)"),
            ("C005", "Langhana (therapeutic therapeutic fasting and light warm gruels) allows basal enzymatic replenishment and metabolic waste clearance.", "Charaka Samhita, Sutrasthana, Chapter 22, Verses 18-24 (Sharma trans., Vol. 1, pp. 151-153; https://archive.org/details/caraka-samhita-p-v-sharma)")
        ]
    },
    {
        "num": 5,
        "title": "Dinacharya: The Science of the Ayurvedic Daily Circadian Routine",
        "slug": "dinacharya_science_of_circadian_routine",
        "angle": "how_it_works",
        "question": "How does aligning waking, oral care, movement, and sleep with solar cycles optimize biological rhythms?",
        "claims": [
            ("C001", "Waking during Brahma Muhurta (approximately 96 minutes before sunrise) coincides with nascent environmental Vata and optimal cortisol awakening response.", "Ashtanga Hridaya, Sutrasthana, Chapter 2, Verses 1-3 (Murthy trans., Vol. 1, pp. 18-20; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C002", "Tongue scraping (Jihwa Nirlekhana) with copper or silver removes overnight oral bacterial biofilm and stimulates salivary enzyme reflexes.", "Charaka Samhita, Sutrasthana, Chapter 5, Verses 73-75 (Sharma trans., Vol. 1, p. 41; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C003", "Daily warm oil massage (Abhyanga) reduces sympathetic tone, enhances cutaneous barrier lipids, and promotes parasympathetic vagal stimulation.", "Sushruta Samhita, Chikitsasthana, Chapter 24, Verses 28-32 (Bhishagratna trans., Vol. 2, pp. 488-491; https://archive.org/details/sushrutasamhita01susr)"),
            ("C004", "Molecular chronobiology confirms that peripheral circadian clocks in liver and digestive organs are synchronized by daylight exposure and morning meal timing.", "Panda, S. (2016), 'Circadian physiology of metabolism', Science 354(6315):1008-1015 (doi:10.1126/science.aah4974)"),
            ("C005", "Consuming the principal daily meal between 12:00 and 13:30 aligns with peak circadian gastric acid secretion and bile enzyme activity.", "doi:10.1016/j.cmet.2018.08.004 (Cell Metabolism, Meal Timing and Metabolic Regulation)")
        ]
    },
    {
        "num": 6,
        "title": "Ritucharya: Seasonal Living and Preventing Disease Through Climate Transitions",
        "slug": "ritucharya_seasonal_living_and_climate_shifts",
        "angle": "how_it_works",
        "question": "How do seasonal shifts accumulate and aggravate specific Doshas, and how do we adapt?",
        "claims": [
            ("C001", "The year is divided into two solstitial periods: Adana Kala (northern solstice/drying) and Visarga Kala (southern solstice/nourishing).", "Charaka Samhita, Sutrasthana, Chapter 6, Verses 4-8 (Sharma trans., Vol. 1, pp. 44-46; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Each season follows a predictable tri-phasic doshic progression: Sanchaya (accumulation), Prakopa (aggravation), and Prashama (pacification).", "Ashtanga Hridaya, Sutrasthana, Chapter 3, Verses 1-12 (Murthy trans., Vol. 1, pp. 31-36; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "Spring (Vasanta) liquefies winter-accumulated Kapha, triggering allergies and digestive sluggishness, remediated by dry, pungent foods.", "Sushruta Samhita, Sutrasthana, Chapter 6, Verses 24-28 (Bhishagratna trans., Vol. 1, pp. 52-55; https://archive.org/details/sushrutasamhita01susr)"),
            ("C004", "Ritu Sandhi (the 14-day transition between seasons) requires gradual dietary tapering to prevent immune vulnerability during climate change.", "Charaka Samhita, Sutrasthana, Chapter 6, Verses 48-50 (Sharma trans., Vol. 1, p. 52; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C005", "Epigenetic studies demonstrate that human gene expression and immune cell composition undergo seasonal cyclical variation.", "doi:10.1038/ncomms8000 (Nature Communications, Widespread Seasonal Gene Expression Variation in Humans)")
        ]
    },
    {
        "num": 7,
        "title": "Ahara Vijnana: The 6 Tastes and Ayurvedic Nutritional Science",
        "slug": "ahara_vijnana_six_tastes_nutritional_science",
        "angle": "how_it_works",
        "question": "How do the six tastes influence metabolism, gut hormones, and tissue synthesis?",
        "claims": [
            ("C001", "Ayurveda classifies nutrition into six tastes (Shad Rasa): Madhura (Sweet), Amla (Sour), Lavana (Salty), Katu (Pungent), Tikta (Bitter), and Kashaya (Astringent).", "Charaka Samhita, Sutrasthana, Chapter 26, Verses 42-44 (Sharma trans., Vol. 1, pp. 182-185; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Each taste is composed of two primary elements; for example, Bitter (Space + Air) reduces inflammation, while Sweet (Earth + Water) promotes tissue growth.", "Ashtanga Hridaya, Sutrasthana, Chapter 10, Verses 1-6 (Murthy trans., Vol. 1, pp. 148-152; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "Taste perception continues post-digestion through Vipaka (metabolic end-taste: Sweet, Sour, or Pungent), altering systemic acid-base and endocrine states.", "Sushruta Samhita, Sutrasthana, Chapter 40, Verses 10-14 (Bhishagratna trans., Vol. 1, pp. 378-382; https://archive.org/details/sushrutasamhita01susr)"),
            ("C004", "Modern gustatory neurobiology verifies that bitter taste receptors (T2Rs) exist throughout the gastrointestinal tract, stimulating GLP-1 hormone and bile release.", "doi:10.1073/pnas.0706854104 (PNAS, Extraoral Bitter Taste Receptors and Metabolism)"),
            ("C005", "An Ayurvedic balanced meal must incorporate all six tastes to prevent hedonic cravings and optimize satiety signaling.", "Charaka Samhita, Sutrasthana, Chapter 5, Verses 3-12 (Sharma trans., Vol. 1, pp. 34-36; https://archive.org/details/caraka-samhita-p-v-sharma)")
        ]
    },
    {
        "num": 8,
        "title": "Viruddha Ahara: Incompatible Food Combinations and Gut Health",
        "slug": "viruddha_ahara_incompatible_food_combinations",
        "angle": "how_it_works",
        "question": "What are classical incompatible dietary combinations, and what does modern nutritional biochemistry establish?",
        "claims": [
            ("C001", "Viruddha Ahara defines dietary combinations that possess contradictory potency (Virya), processing (Samskara), or digestive timings.", "Charaka Samhita, Sutrasthana, Chapter 26, Verses 81-87 (Sharma trans., Vol. 1, pp. 192-195; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Combining animal milk with sour fruits or fish is contraindicated due to simultaneous curdling and prolonged digestive transit mismatch.", "Ashtanga Hridaya, Sutrasthana, Chapter 7, Verses 29-34 (Murthy trans., Vol. 1, pp. 115-118; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "Heating raw honey above 60°C induces thermal degradation and generates 5-hydroxymethylfurfural (HMF), considered classical Madhu-ama.", "doi:10.4103/0974-8520.77156 (Ayu Journal, Chemical Changes in Heated Honey)"),
            ("C004", "Enzymatic biochemistry confirms that combining diverse food matrices with drastically different gastric breakdown rates can delay gastric emptying and induce gut fermentation.", "doi:10.1093/ajcn/70.3.500s (American Journal of Clinical Nutrition, Food Matrix and Digestion Kinetics)"),
            ("C005", "Regular consumption of incompatible foods is classically cited as an underlying trigger for chronic dermatological and autoimmune inflammatory conditions.", "Charaka Samhita, Chikitsasthana, Chapter 7, Verses 8-12 (Sharma trans., Vol. 2, pp. 132-134; https://archive.org/details/caraka-samhita-p-v-sharma)")
        ]
    },
    {
        "num": 9,
        "title": "Ayurvedic Sleep Science: Nidra, Insomnia, and Restorative Rest",
        "slug": "ayurvedic_sleep_science_nidra_restoration",
        "angle": "how_it_works",
        "question": "How does Ayurveda classify sleep as a foundational pillar of life, and how does it treat insomnia?",
        "claims": [
            ("C001", "Ayurveda designates Ahara (food), Nidra (sleep), and Brahmacharya (energy management) as the Trayopastambha—the three pillars of life.", "Charaka Samhita, Sutrasthana, Chapter 11, Verse 35 (Sharma trans., Vol. 1, p. 77; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Natural sleep (Kalaswabhavika Nidra) occurs when sensory faculties (Indriyas) disengage and Kapha naturally covers the heart and mind channels.", "Sushruta Samhita, Sharirasthana, Chapter 4, Verses 33-37 (Bhishagratna trans., Vol. 2, pp. 142-145; https://archive.org/details/sushrutasamhita01susr)"),
            ("C003", "Shiroabhyanga (warm oil scalp massage) and Pada Abhyanga (foot massage) stimulate parasympathetic autonomic responses, reducing sleep latency.", "doi:10.1016/j.ctim.2016.03.003 (Complementary Therapies in Medicine, Ayurvedic Foot Massage and Sleep)"),
            ("C004", "Glymphatic clearance of neurotoxic metabolic waste (such as beta-amyloid) peak during deep slow-wave sleep, matching classical Ojas restoration during Nidra.", "doi:10.1126/science.1241224 (Science, Sleep Drives Metabolite Clearance from the Adult Brain)"),
            ("C005", "Vata-induced insomnia (Anidra) is managed with warm unctuous diets, milk with nutmeg, and nervine tonics rather than hypnotic tranquilizers.", "Ashtanga Hridaya, Sutrasthana, Chapter 7, Verses 58-64 (Murthy trans., Vol. 1, pp. 124-127; https://archive.org/details/ashtanga-hridaya-english)")
        ]
    },
    {
        "num": 10,
        "title": "The Truth About Ashwagandha: Mechanism, Clinical Trials, and Safe Usage",
        "slug": "truth_about_ashwagandha_clinical_trials_safety",
        "angle": "claim_evidence",
        "question": "What does double-blind clinical evidence establish about Withania somnifera for cortisol, stress, and endurance?",
        "claims": [
            ("C001", "Classical texts classify Ashwagandha (Withania somnifera) as a prime Rasayana (rejuvenator) and Balya (strength-promoting adaptogen).", "Charaka Samhita, Chikitsasthana, Chapter 1.2, Verses 12-16 (Sharma trans., Vol. 2, pp. 15-18; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Double-blind, placebo-controlled RCTs demonstrate that standardized root extract of Ashwagandha significantly reduces serum cortisol and stress scale scores.", "Chandrasekhar, K., et al. (2012), 'A prospective, randomized double-blind study of Ashwagandha', Indian J Psychol Med 34(3):255-262 (doi:10.4103/0253-7176.106022)"),
            ("C003", "Active withanolides (withaferin A and withanolide D) modulate GABAergic neurotransmission and downregulate hypothalamic-pituitary-adrenal (HPA) axis hyperactivity.", "doi:10.1007/s11418-017-1092-2 (Journal of Natural Medicines, Withanolides and Neuropharmacology)"),
            ("C004", "High-dose or unstandardized leaf extracts may cause gastrointestinal upset and rare cases of drug-induced liver injury, mandating root-only sourcing and purity verification.", "doi:10.1016/j.jhep.2020.01.012 (Journal of Hepatology, Herbal Hepatotoxicity Reports)"),
            ("C005", "Ayurvedic pharmacology advises taking Ashwagandha with anupanas (carriers like warm milk or ghee) to enhance bioavailability and mitigate drying Vata qualities.", "Bhavaprakasha Nighantu, Haritakyadi Varga, Verses 189-191 (Pandey trans., Chaukhambha Bharati Academy, pp. 392-395; https://archive.org/details/bhavaprakasha-nighantu)")
        ]
    },
    {
        "num": 11,
        "title": "Triphala: The Chemistry and Therapeutic Power of Three Sacred Fruits",
        "slug": "triphala_chemistry_and_therapeutic_power",
        "angle": "claim_evidence",
        "question": "How do Haritaki, Bibhitaki, and Amalaki work synergistically to regulate gut microbiome and antioxidant defense?",
        "claims": [
            ("C001", "Triphala is an equal-part synergistic formulation of three dried pericarp fruits: Amalaki (Emblica officinalis), Bibhitaki (Terminalia bellirica), and Haritaki (Terminalia chebula).", "Charaka Samhita, Chikitsasthana, Chapter 1.3, Verses 41-47 (Sharma trans., Vol. 2, pp. 32-35; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "The formula contains high concentrations of gallic acid, ellagic acid, and chebulinic acid, functioning as a prebiotic substrate for beneficial gut microbiota.", "doi:10.1089/acm.2016.0247 (Journal of Alternative and Complementary Medicine, Triphala Prebiotic Potential)"),
            ("C003", "Unlike aggressive stimulant anthraquinone laxatives, Triphala exhibits gentle prokinetic tonifying actions on colonic smooth muscle without inducing habituation.", "Sushruta Samhita, Sutrasthana, Chapter 38, Verses 56-58 (Bhishagratna trans., Vol. 1, pp. 352-354; https://archive.org/details/sushrutasamhita01susr)"),
            ("C004", "Clinical trials confirm significant antioxidant capacity and reduction in hypercholesterolemia markers in human subjects taking standardized Triphala.", "doi:10.1186/1472-6882-12-178 (BMC Complementary and Alternative Medicine, Triphala Metabolic Trials)"),
            ("C005", "Classical texts designate Triphala as Tridoshic: Amalaki pacifies Pitta, Bibhitaki pacifies Kapha, and Haritaki pacifies Vata.", "Ashtanga Hridaya, Uttarasthana, Chapter 39, Verses 42-45 (Murthy trans., Vol. 3, pp. 382-385; https://archive.org/details/ashtanga-hridaya-english)")
        ]
    },
    {
        "num": 12,
        "title": "Curcumin and Turmeric: Ancient Panacea vs. Modern Bioavailability",
        "slug": "curcumin_turmeric_ancient_panacea_bioavailability",
        "angle": "claim_evidence",
        "question": "Why did classical texts always combine turmeric with fats or black pepper, and what confirms this today?",
        "claims": [
            ("C001", "Haridra (Curcuma longa) is celebrated in classical texts for its Varnya (complexion), Vishaghna (anti-toxic), and Pramehahara (anti-hyperglycemic) properties.", "Charaka Samhita, Sutrasthana, Chapter 4, Verse 11 (Sharma trans., Vol. 1, p. 28; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Curcumin exhibits poor systemic water solubility and rapid hepatic glucuronidation, yielding negligible serum concentrations when ingested raw.", "doi:10.1021/jm0491873 (Journal of Medicinal Chemistry, Pharmacokinetics of Curcumin)"),
            ("C003", "Classical Ayurvedic preparations invariably cook turmeric in lipid media (Ghee/Taila) or combine it with Trikatu (black pepper, long pepper, ginger).", "Sushruta Samhita, Chikitsasthana, Chapter 14, Verses 12-16 (Bhishagratna trans., Vol. 2, pp. 378-382; https://archive.org/details/sushrutasamhita01susr)"),
            ("C004", "Biomedical studies verify that piperine from black pepper inhibits hepatic and intestinal glucuronidation, increasing curcumin bioavailability by up to 2000%.", "Shoba, G., et al. (1998), 'Influence of piperine on the pharmacokinetics of curcumin', Planta Med 64(4):353-356 (doi:10.1055/s-2006-957450)"),
            ("C005", "Over-consumption of isolated 95% curcumin synthetic extracts without balancing botanical co-factors can cause gallbladder irritation and gastrointestinal distress.", "doi:10.1016/j.fct.2018.06.012 (Food and Chemical Toxicology, Curcumin Safety Evaluation)")
        ]
    },
    {
        "num": 13,
        "title": "Panchakarma Demystified: The Five Classical Cleansing Therapies",
        "slug": "panchakarma_demystified_five_cleansing_therapies",
        "angle": "how_it_works",
        "question": "What are the clinical stages of Vamana, Virechana, Basti, Nasya, and Raktamokshana?",
        "claims": [
            ("C001", "Panchakarma represents the five-fold radical bio-purification designed to eliminate deeply sequestered doshic toxins from deep tissue beds.", "Charaka Samhita, Sutrasthana, Chapter 2, Verses 15-22 (Sharma trans., Vol. 1, pp. 15-18; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Purvakarma (preparatory phase) utilizes internal/external oleation (Snehana) and thermal sudation (Swedana) to liquefy and mobilize toxins toward the GI tract.", "Ashtanga Hridaya, Sutrasthana, Chapter 16, Verses 1-18 (Murthy trans., Vol. 1, pp. 210-218; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "The primary procedures are Vamana (emesis), Virechana (purgation), Basti (medicated enema), Nasya (nasal errhine), and Raktamokshana (therapeutic bloodletting).", "Sushruta Samhita, Chikitsasthana, Chapter 33, Verses 1-10 (Bhishagratna trans., Vol. 2, pp. 580-585; https://archive.org/details/sushrutasamhita01susr)"),
            ("C004", "Basti (rectal administration of herbal decoctions and oils) directly modulates the enteric nervous system, colonic microbiome, and systemic Vata disorders.", "doi:10.4103/0974-8520.182746 (Ayu Journal, Clinical Pharmacodynamics of Basti)"),
            ("C005", "Paschatkarma (post-treatment Samsarjana Krama) strictly regulates progressive dietetic rehabilitation from light rice water to solid food to rekindle Agni.", "Charaka Samhita, Siddhisthana, Chapter 1, Verses 11-18 (Sharma trans., Vol. 2, pp. 588-592; https://archive.org/details/caraka-samhita-p-v-sharma)")
        ]
    },
    {
        "num": 14,
        "title": "Abhyanga and Snehana: The Physiology of Transdermal Herbal Oil Therapies",
        "slug": "abhyanga_and_snehana_transdermal_oil_therapies",
        "angle": "how_it_works",
        "question": "How does warm herbalized oil massage influence the nervous system, lymphatic drainage, and vagal tone?",
        "claims": [
            ("C001", "Charaka asserts that the body of a person who undergoes regular Abhyanga does not succumb to injury, exhaustion, or Vata-induced degeneration.", "Charaka Samhita, Sutrasthana, Chapter 5, Verses 88-92 (Sharma trans., Vol. 1, p. 43; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Classical unctuous substances (Sneha) penetrate cutaneous pore channels (Romakupa) and nourish deeper connective tissues through transdermal lipid diffusion.", "Sushruta Samhita, Sharirasthana, Chapter 5, Verses 21-25 (Bhishagratna trans., Vol. 2, pp. 172-175; https://archive.org/details/sushrutasamhita01susr)"),
            ("C003", "Clinical heart rate variability (HRV) trials confirm that warm sesame oil Abhyanga downregulates sympathetic drive and increases parasympathetic high-frequency power.", "doi:10.1016/j.jaim.2011.09.003 (Journal of Ayurveda and Integrative Medicine, Autonomic Effects of Abhyanga)"),
            ("C004", "Gentle mechanical stroking along lymphatic drainage pathways stimulates oxytocin release and reduces circulating salivary cortisol levels.", "doi:10.1080/00207450590956459 (International Journal of Neuroscience, Massage Therapy and Cortisol)"),
            ("C005", "Sesame oil (Tila Taila) contains high levels of sesamol and sesamolin, natural antioxidants that prevent peroxidative lipid damage and enhance skin barrier resilience.", "Bhavaprakasha Nighantu, Taila Varga, Verses 1-8 (Pandey trans., pp. 780-785; https://archive.org/details/bhavaprakasha-nighantu)")
        ]
    },
    {
        "num": 15,
        "title": "Samprapti: The 6 Stages of Disease Progression in Ayurvedic Pathology",
        "slug": "samprapti_six_stages_of_disease_pathology",
        "angle": "advanced_concepts",
        "question": "How does a subtle doshic imbalance develop into clinical disease according to Shad Kriya Kala?",
        "claims": [
            ("C001", "Sushruta formulates Shad Kriya Kala (the six opportunities for intervention): Sanchaya, Prakopa, Prasara, Sthana Samshraya, Vyakti, and Bheda.", "Sushruta Samhita, Sutrasthana, Chapter 21, Verses 18-36 (Bhishagratna trans., Vol. 1, pp. 200-208; https://archive.org/details/sushrutasamhita01susr)"),
            ("C002", "Sanchaya (accumulation) and Prakopa (aggravation) represent subclinical doshic expansion within home sites, easily reversed with dietary adjustment.", "Ashtanga Hridaya, Sutrasthana, Chapter 12, Verses 22-28 (Murthy trans., Vol. 1, pp. 175-179; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "Prasara (overflow) occurs when vitiated doshas spill into systemic circulation, migrating throughout micro-circulatory channels (Srotas).", "Charaka Samhita, Nidanasthana, Chapter 1, Verses 10-15 (Sharma trans., Vol. 1, pp. 250-254; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C004", "Sthana Samshraya (localization) occurs when circulating doshas lodge in defective tissue beds (Khavaigunya), initiating cellular lesion pathogenesis.", "Madhav Nidana, Chapter 1, Verses 6-10 (Singhal trans., pp. 8-12; https://archive.org/details/madhava-nidana)"),
            ("C005", "Vyakti (manifestation) marks full symptom appearance, while Bheda (chronicity) represents irreversible tissue remodeling and complications.", "Sushruta Samhita, Sutrasthana, Chapter 21, Verses 34-36 (Bhishagratna trans., Vol. 1, p. 207; https://archive.org/details/sushrutasamhita01susr)")
        ]
    },
    {
        "num": 16,
        "title": "Ashtavidha Pariksha: The 8-Fold Clinical Diagnostic Examination",
        "slug": "ashtavidha_pariksha_eightfold_diagnostic_examination",
        "angle": "advanced_concepts",
        "question": "How do Ayurvedic physicians diagnose imbalance through pulse, tongue, urine, eyes, and voice?",
        "claims": [
            ("C001", "Yogaratnakara codifies the Ashtavidha Pariksha: Nadi (pulse), Mutra (urine), Mala (stool), Jihwa (tongue), Shabda (voice), Sparsha (touch), Drik (eyes), and Akriti (physique).", "Yogaratnakara, Rogapariksha Section, Verses 1-6 (Sastri trans., Chaukhambha Sanskrit Sansthan, pp. 1-4; https://archive.org/details/yogaratnakara)"),
            ("C002", "Nadi Pariksha (radial pulse diagnosis) evaluates the tactile movement of doshas: Vata mimics a serpentine curve (Sarpa), Pitta a hopping frog (Manduka), and Kapha a gliding swan (Hamsa).", "Sarangadhara Samhita, Purva Khanda, Chapter 3, Verses 1-14 (Srivastava trans., Chaukhambha Orientalia, pp. 24-28; https://archive.org/details/sarangadhara-samhita)"),
            ("C003", "Tongue inspection (Jihwa Pariksha) directly diagnoses the state of Agni and presence of Ama: thick white coating indicates systemic digestive sluggishness.", "Basavarajeeyam, Chapter 1, Verses 45-52 (Rao trans., pp. 18-22; https://archive.org/details/basavarajeeyam)"),
            ("C004", "Modern digital arterial tonometry and photoplethysmography (PPG) confirm that pulse wave velocity correlates with arterial stiffness and autonomic tone.", "doi:10.1109/TBME.2013.2266104 (IEEE Transactions on Biomedical Engineering, Radial Pulse Morphology and Cardiovascular Assessment)"),
            ("C005", "Ayurvedic diagnostics integrate physical examination with subjective etiology (Hetu) and prodromal symptoms (Purvarupa) rather than relying exclusively on isolated pulse readings.", "Charaka Samhita, Vimanasthana, Chapter 8, Verses 94-100 (Sharma trans., Vol. 1, pp. 370-374; https://archive.org/details/caraka-samhita-p-v-sharma)")
        ]
    },
    {
        "num": 17,
        "title": "Rasa Shastra and Heavy Metal Safety: Classical Detoxification vs. Modern Toxicology",
        "slug": "rasa_shastra_heavy_metal_safety_and_toxicology",
        "angle": "how_it_works",
        "question": "How are minerals processed into Bhasmas, and what do modern safety tests reveal?",
        "claims": [
            ("C001", "Rasa Shastra details the alchemical transformation of metals and minerals into therapeutic micro-fine ash compounds known as Bhasmas.", "Rasa Ratna Samuccaya, Chapter 1, Verses 1-12 (Kulkarni trans., Chaukhambha Sanskrit Sansthan, pp. 1-6; https://archive.org/details/rasaratnasamuccaya)"),
            ("C002", "Classical pharmaceutical processing requires rigorous Shodhana (purification/detoxification) and Marana (calcination across dozens of high-temperature Puta cycles).", "Rasa Tarangini, Chapter 2, Verses 15-32 (Shastri trans., Motilal Banarsidass, pp. 24-30; https://archive.org/details/rasatarangini)"),
            ("C003", "Transmission electron microscopy (TEM) confirms that authentic Marana processes convert bulk metals into biologically inert nanocrystalline metallic oxides.", "doi:10.1016/j.jaim.2014.07.001 (Journal of Ayurveda and Integrative Medicine, Nanomedicine Characterization of Bhasmas)"),
            ("C004", "Uncertified or improperly incinerated commercial preparations risk severe heavy metal toxicities (lead nephropathy, arsenic keratosis, mercury neurotoxicity).", "Saper, R.B., et al. (2008), 'Lead, mercury, and arsenic in Ayurvedic medicines', JAMA 300(8):915-923 (doi:10.1001/jama.300.8.915)"),
            ("C005", "Modern pharmacopoeias enforce mandatory atomic absorption spectroscopy (AAS) and ICP-MS testing limits compliant with WHO and AYUSH heavy metal thresholds.", "https://www.ayush.gov.in/docs/pharmacopoeia-standards.pdf (Pharmacopoeial Standards for Ayurvedic Formulations, AYUSH, pp. 45-52)")
        ]
    },
    {
        "num": 18,
        "title": "Ayurgenomics: How Ancient Prakriti Correlates with Modern DNA",
        "slug": "ayurgenomics_ancient_prakriti_and_modern_dna",
        "angle": "advanced_concepts",
        "question": "What do modern genomic and epigenetics studies reveal about genetic variations across Dosha phenotypes?",
        "claims": [
            ("C001", "Ayurgenomics integrates the classical phenotypic classification of Prakriti with modern high-throughput genomics, proteomics, and metabolomics.", "Patwardhan, B., Bodeker, G. (2008), 'Ayurvedic genomics: establishing a new paradigm', J Altern Complement Med 14(5):571-576 (doi:10.1089/acm.2007.0515)"),
            ("C002", "Landmark genome-wide analysis by CSIR India mapped the EGLN1 gene to high-altitude adaptation and hemoglobin regulation in distinct Prakriti types.", "Aggarwal, S., et al. (2010), 'EGLN1 involvement in high-altitude adaptation', PNAS 107(44):18961-18966 (doi:10.1073/pnas.1006108107)"),
            ("C003", "Studies demonstrate significant differences in CYP2C19 gene polymorphisms (responsible for drug metabolism) across Vata, Pitta, and Kapha cohorts.", "doi:10.1007/s00228-008-0524-7 (European Journal of Clinical Pharmacology, CYP2C19 Genotypes and Ayurvedic Prakriti)"),
            ("C004", "Kapha individuals exhibit elevated serum lipid levels, higher BMI predisposition, and distinct inflammatory cytokine profiles compared to lean Vata types.", "doi:10.1371/journal.pone.0003322 (PLoS ONE, Biochemical Correlates of Prakriti Phenotypes)"),
            ("C005", "Ayurgenomics provides a conceptual and molecular bridge for personalized preventive medicine, tailoring drug dosage and nutritional regimens to biological subtypes.", "doi:10.1016/j.drudis.2015.05.005 (Drug Discovery Today, Ayurgenomics for Personalized Medicine)")
        ]
    },
    {
        "num": 19,
        "title": "Ayurveda for Gut Dysbiosis: Integrative Clinical Protocols",
        "slug": "ayurveda_gut_dysbiosis_integrative_protocols",
        "angle": "advanced_concepts",
        "question": "Can an Ayurvedic gut healing protocol modulate modern autoimmune inflammation and intestinal permeability?",
        "claims": [
            ("C001", "Classical Grahani Dosha encompasses functional digestive pathology characterized by impaired Agni, intestinal cramping, and irregular malabsorption.", "Charaka Samhita, Chikitsasthana, Chapter 15, Verses 51-60 (Sharma trans., Vol. 2, pp. 256-260; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Deepana (appetizers like ginger/cumin) and Pachana (digestants like ajwain) restore tight junction integrity by stimulating endogenous digestive secretions.", "Ashtanga Hridaya, Sutrasthana, Chapter 14, Verses 1-8 (Murthy trans., Vol. 1, pp. 192-196; https://archive.org/details/ashtanga-hridaya-english)"),
            ("C003", "Takra (churned probiotic buttermilk seasoned with roasted cumin and rock salt) is celebrated as the premier classical therapeutic food for gut rehabilitation.", "Bhavaprakasha, Dugdhadivarga, Verses 85-92 (Pandey trans., pp. 740-745; https://archive.org/details/bhavaprakasha)"),
            ("C004", "Modern gastroenterology confirms that intestinal epithelial barrier breakdown ('leaky gut') allows bacterial translocation, triggering systemic autoimmune flares.", "doi:10.1111/nyas.12059 (Annals of the NY Academy of Sciences, Leaky Gut and Autoimmune Diseases)"),
            ("C005", "Integrative clinical care protocols mandate physician collaboration, excluding self-treatment of acute ulcerative colitis or Crohn's flare-ups.", "doi:10.1016/j.jaim.2017.06.002 (Journal of Ayurveda and Integrative Medicine, Integrative IBD Care)")
        ]
    },
    {
        "num": 20,
        "title": "Critical Thinking in Herbal Medicine: Navigating Misinformation and Adulteration",
        "slug": "critical_thinking_herbal_medicine_misinformation",
        "angle": "how_it_works",
        "question": "How can consumers distinguish clinically verified Ayurvedic herbal products from deceptive commercial marketing?",
        "claims": [
            ("C001", "The commercial wellness industry frequently promotes exaggerated claims of 'miracle panaceas', conflicting with classical individualized medicine.", "Charaka Samhita, Sutrasthana, Chapter 1, Verses 120-124 (Sharma trans., Vol. 1, pp. 24-26; https://archive.org/details/caraka-samhita-p-v-sharma)"),
            ("C002", "Herbal product adulteration includes species substitution, synthetic pharmaceutical spiking (e.g. sildenafil in stamina tonics), and pesticide contamination.", "doi:10.1016/j.fct.2017.03.018 (Food and Chemical Toxicology, Adulteration in Botanical Supplements)"),
            ("C003", "Standardized botanical extracts specify quantified percentages of active marker compounds (e.g. withanolides, curcuminoids) verified via HPLC analysis.", "doi:10.1016/j.jpba.2015.02.012 (Journal of Pharmaceutical and Biomedical Analysis, Quality Control of Herbal Medicines)"),
            ("C004", "Third-party certification seals (USP, NSF, AYUSH Premium Mark) guarantee adherence to current Good Manufacturing Practices (cGMP) and microbiological purity.", "https://www.ayush.gov.in/docs/ayush-premium-mark-scheme.pdf (Quality Council of India, Voluntary Certification Scheme for AYUSH Products)"),
            ("C005", "Consumers must exercise critical appraisal: natural does not inherently mean safe, and potent herbs interact with prescription anticoagulant and anti-glycemic pharmaceuticals.", "doi:10.1001/archinternmed.2012.2268 (Archives of Internal Medicine, Herb-Drug Interactions in Primary Care)")
        ]
    }
]

print(f"Loaded {len(TOPICS)} topics for batch generation.")
