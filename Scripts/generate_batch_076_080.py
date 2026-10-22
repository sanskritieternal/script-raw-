"""
Batch Generator for Niches 076 to 080:
- 076_world_religions_civilization
- 077_yoga_wellness
- 078_books_literature
- 079_creative_arts
- 080_film_entertainment_analysis
"""

import sys
from pathlib import Path

# Add Scripts to sys.path
sys.path.append(str(Path(__file__).parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_076_080 = {
    "076_world_religions_civilization": {
        "id": "076",
        "slug": "world_religions_civilization",
        "title": "World Religions & Civilization",
        "category": "Culture_Philosophy",
        "audience": "Comparative Religion Scholars, Philosophy Enthusiasts, Cultural Historians, Curious Thinkers (Global)",
        "progression": [
            ("Tier 1: Axial Age Awakenings, Sacred Texts & Fundamental Doctrines (Scratch / Beginner)",
             "The 8th-3rd century BCE Axial Age (Jaspers), foundational scriptures (Vedas, Torah, Tripitaka, Tao Te Ching, Avesta), and core cosmologies."),
            ("Tier 2: Monotheism, Dharma, Dao & The Trans-Eurasian Silk Road Syncretism (Intermediate)",
             "Abrahamic developments, Vedic-Buddhist-Jain dialectics, Confucian social order vs Daoist naturalism, and Silk Road monastery trade networks."),
            ("Tier 3: Schisms, Mystical Traditions & Theological Revolutions (Upper Intermediate)",
             "Sufi poetry and Dhikr, Christian monasticism and the Reformation, Kabbalah, Bhakti movement saints (Kabir, Mirabai), Zen Koans, and scholastic disputations."),
            ("Tier 4: Secularization, Interfaith Dialogue & Sacred Architecture in the Modern Era (Advanced / Expert)",
             "Max Weber's disenchantment thesis, comparative eschatology, sacred geometry in cathedrals/temples/mosques, and the evolution of faith in high-tech societies.")
        ],
        "flagship": {
            "title": "The Axial Age: When Humanity's Greatest Philosophies and Religions Were Born Simultaneously",
            "angle": "history_origins",
            "slug": "076_world_religions_civilization_history_origins_axial_age_revolution"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Axial Age: When Humanity's Greatest Philosophies and Religions Were Born Simultaneously",
                "tier": "Tier 1: Axial Age Awakenings & Sacred Texts",
                "angle": "history_origins",
                "slug": "axial_age_revolution_karl_jaspers_simultaneous_spiritual_birth_eurasia",
                "question": "Why did Buddhism, Confucianism, Daoism, Zoroastrianism, and Greek philosophy emerge simultaneously between 800 and 200 BCE without direct contact?",
                "key_focus": "Karl Jaspers' Axial Age thesis, urban transitions and bronze-to-iron metallurgy, the shift from ritual sacrifices to moral self-reflection across India, China, the Levant, and Greece.",
                "reason": "Flagship launch episode; establishes the synchronized civilizational awakening that forms the foundation of all major world faiths."
            },
            {
                "id": 2,
                "title": "The Vedas & Upanishads: Decoding the World's Oldest Continuous Spiritual Literature",
                "tier": "Tier 1: Axial Age Awakenings & Sacred Texts",
                "angle": "textual_analysis",
                "slug": "vedas_and_upanishads_oldest_spiritual_canon_tat_tvam_asi_brahman",
                "question": "What is the philosophical journey from the ritual hymns of the Rigveda to the non-dual metaphysics of the Upanishads?",
                "key_focus": "Oral chanting preservation (patha methods), Rigvedic Nasadiya Sukta (Creation Hymn), Brahman (ultimate reality) and Atman (soul), 'Tat Tvam Asi' identity statement.",
                "reason": "Crucial foundational episode exploring the bedrock texts of Sanatan Dharma and South Asian metaphysics."
            },
            {
                "id": 3,
                "title": "The Four Noble Truths and the Eightfold Path: The Buddha's Diagnosis of Human Suffering",
                "tier": "Tier 1: Axial Age Awakenings & Sacred Texts",
                "angle": "beginner_explainers",
                "slug": "four_noble_truths_eightfold_path_buddha_diagnosis_of_dukkha",
                "question": "How did Prince Siddhartha formulate an empirical, psychological roadmap to conquer suffering (Dukkha) without reliance on supernatural revelation?",
                "key_focus": "Dukkha (suffering/unsatisfactoriness), Samudaya (origin in craving/tanha), Nirodha (cessation/Nirvana), and Magga (the noble eightfold path: right view to right mindfulness).",
                "reason": "Essential introduction to Buddhist philosophy, pragmatism, and psychological ethics."
            },
            {
                "id": 4,
                "title": "The Abrahamic Covenant: How One Nomadic Patriarch Shaped Judaism, Christianity, and Islam",
                "tier": "Tier 1: Axial Age Awakenings & Sacred Texts",
                "angle": "historical_lineage",
                "slug": "abrahamic_covenant_monotheism_ur_of_chaldees_to_jerusalem",
                "question": "How did the ancient covenant made between God and Abraham in the Bronze Age Middle East evolve into three global religions encompassing over 4 billion people?",
                "key_focus": "The journey from Ur to Canaan, covenant theology (Brit), the Binding of Isaac/Ishmael, shared prophetic lineages through Moses, Jesus, and Muhammad.",
                "reason": "Provides the essential lineage linking Jewish monotheism, Christian salvation, and Islamic submission to divine will."
            },
            {
                "id": 5,
                "title": "Daoism vs. Confucianism: The Yin and Yang of Classical Chinese Civilization",
                "tier": "Tier 1: Axial Age Awakenings & Sacred Texts",
                "angle": "comparative_analysis",
                "slug": "daoism_vs_confucianism_yin_yang_social_order_vs_natural_flow",
                "question": "Why did traditional Chinese scholars live by Confucius in the daytime and meditate like Laozi in the evening?",
                "key_focus": "Confucian filial piety (Xiao), ritual propriety (Li), benevolence (Ren) vs. Daoist Wu Wei (effortless action), spontaneity (Ziran), and harmonization with the watercourse way.",
                "reason": "Deconstructs the dual complementary philosophical engines that steered imperial China for over two millennia."
            },
            {
                "id": 6,
                "title": "The Silk Road Monastery Network: How Buddhism Conquered Asia Through Merchants and Caves",
                "tier": "Tier 2: Monotheism, Dharma & Silk Road Syncretism",
                "angle": "geographical_trade_routes",
                "slug": "silk_road_buddhist_monastery_network_dunhuang_bamiyan_merchants",
                "question": "How did trade caravans carrying silk, jade, and spices transform Buddhism from an Indian ascetic movement into an East Asian civilizational force?",
                "key_focus": "Kushan empire patronage (King Kanishka), Dunhuang Mogao caves, translation bureau of Kumarajiva, Gandharan Hellenistic-Buddhist art, and merchant monastery banking systems.",
                "reason": "Reveals the crucial intersection of economics, geography, and religious transmission along ancient trade arteries."
            },
            {
                "id": 7,
                "title": "The Torah and the Talmud: The Architecture of Jewish Law, Exile, and Endless Debate",
                "tier": "Tier 2: Monotheism, Dharma & Silk Road Syncretism",
                "angle": "scriptural_commentary",
                "slug": "torah_and_talmud_jewish_jurisprudence_mishnah_gemara_diaspora",
                "question": "How did the rabbinic tradition transform a temple-centric religion into an unbreakable portable homeland through debate and legal argumentation?",
                "key_focus": "Destruction of the Second Temple (70 CE), Mishnah and Gemara composition, the dialectical method of 'arguments for the sake of heaven' (Hillel vs. Shammai), halakha vs. aggadah.",
                "reason": "Explains how intellectual debate and textual study sustained Jewish identity throughout centuries of exile."
            },
            {
                "id": 8,
                "title": "Early Christianity in the Roman Empire: From Underground Catacombs to Imperial Faith",
                "tier": "Tier 2: Monotheism, Dharma & Silk Road Syncretism",
                "angle": "historical_turning_points",
                "slug": "early_christianity_roman_empire_catacombs_to_edict_of_milan_nicaea",
                "question": "How did a persecuted Jewish sect in Roman Judea become the official religion of the Roman Empire in less than 300 years?",
                "key_focus": "Pauline epistles to Gentiles, Pax Romana transport networks, martyr resilience, Constantine's conversion, the Edict of Milan (313 CE), and the Council of Nicaea (325 CE).",
                "reason": "Covers one of the most consequential religious and political pivots in world history."
            },
            {
                "id": 9,
                "title": "The Revelation in Mecca: The Life of Prophet Muhammad and the Unification of Arabia",
                "tier": "Tier 2: Monotheism, Dharma & Silk Road Syncretism",
                "angle": "biographical_origins",
                "slug": "revelation_in_mecca_prophet_muhammad_hijra_unification_of_arabia",
                "question": "How did the 7th-century revelation in the Cave of Hira transform a fragmented tribal desert society into a unified civilization based on ethical monotheism?",
                "key_focus": "Pre-Islamic Jahiliyyah tribal conflicts, the Night of Power (Laylat al-Qadr), the Hijra from Mecca to Medina (622 CE), the Constitution of Medina, and core Quranic themes of Tawhid.",
                "reason": "Documents the genesis of Islamic civilization and its rapid socio-ethical restructuring of Arabia."
            },
            {
                "id": 10,
                "title": "Zoroastrianism: The Lost Dualism of Cosmic Light vs. Absolute Darkness",
                "tier": "Tier 2: Monotheism, Dharma & Silk Road Syncretism",
                "angle": "ancient_forgotten_faiths",
                "slug": "zoroastrianism_ahura_mazda_angra_mainyu_fire_temples_persia",
                "question": "Why is ancient Persian Zoroastrianism considered the original source for concepts of Heaven, Hell, Angels, and the Final Judgment in Western faiths?",
                "key_focus": "Zarathustra's Gathas, Ahura Mazda (Lord of Wisdom) vs. Angra Mainyu (Destructive Spirit), sacred fire altars (Atashgah), Towers of Silence, and the Parsi diaspora in India.",
                "reason": "Examines the Persian empire's spiritual backbone that profoundly influenced all subsequent apocalyptic traditions."
            },
            {
                "id": 11,
                "title": "Sufism: The Mystical Heart of Islam, Divine Ecstasy, and Sacred Poetry",
                "tier": "Tier 3: Schisms, Mystical Traditions & Theological Revolutions",
                "angle": "mystical_esotericism",
                "slug": "sufism_mystical_heart_of_islam_rumi_dhikr_whirling_dervishes",
                "question": "How did Sufi mystics like Rumi, Al-Ghazali, and Mansur Al-Hallaj seek direct, experiential union with the Divine through poetry, music, and love?",
                "key_focus": "Tariqas (orders), Dhikr (remembrance), Fana (ego annihilation) and Baqa (eternal abiding), Rumi's Masnavi, Sema whirling ceremonies, and Al-Ghazali's synthesis of law and mysticism.",
                "reason": "Highlights the rich aesthetic, emotional, and transcendent dimension of Islamic spirituality."
            },
            {
                "id": 12,
                "title": "The Great Schism of 1054: Why Eastern Orthodoxy and Roman Catholicism Split",
                "tier": "Tier 3: Schisms, Mystical Traditions & Theological Revolutions",
                "angle": "theological_disputes",
                "slug": "great_schism_1054_eastern_orthodoxy_vs_roman_catholicism_filioque",
                "question": "How did a dispute over the Latin word 'Filioque' and papal supremacy tear Christian Christendom into Eastern and Western halves for a thousand years?",
                "key_focus": "The Filioque clause in the Nicene Creed, papal primacy claims vs. conciliar patriarchate model, unleavened bread controversies, and the mutual excommunications in Constantinople.",
                "reason": "Deconstructs the foundational geopolitical and doctrinal split that permanently divided European Christendom."
            },
            {
                "id": 13,
                "title": "The Protestant Reformation: Gutenberg, Martin Luther, and the Shattering of Church Authority",
                "tier": "Tier 3: Schisms, Mystical Traditions & Theological Revolutions",
                "angle": "historical_revolutions",
                "slug": "protestant_reformation_martin_luther_95_theses_printing_press",
                "question": "How did Martin Luther's 95 Theses, combined with Gutenberg's moveable type press, spark religious wars and midwife modern individual consciousness?",
                "key_focus": "Indulgence sales scandals, Sola Fide (faith alone) and Sola Scriptura (scripture alone), vernacular German Bible translation, the Diet of Worms, and John Calvin's Geneva.",
                "reason": "Covers the revolution that democratized literacy, ended church monopolies, and laid the groundwork for modern secular democracies."
            },
            {
                "id": 14,
                "title": "The Bhakti Movement: Medieval India's Radical Rebellion Against Caste and Ritualism",
                "tier": "Tier 3: Schisms, Mystical Traditions & Theological Revolutions",
                "angle": "social_spiritual_reforms",
                "slug": "bhakti_movement_medieval_india_kabir_mirabai_rebellion_against_caste",
                "question": "How did poet-saints like Kabir, Mirabai, Ravidas, and Tukaram ignite a spiritual revolution by discarding Sanskrit elitism for heartfelt vernacular devotion?",
                "key_focus": "Nirguna (formless divine) vs. Saguna (embodied divine) bhakti, radical egalitarianism rejecting caste and orthodox priesthood, community singing (kirtan), and vernacular literature.",
                "reason": "Showcases India's greatest egalitarian renaissance that democratized spirituality across all social strata."
            },
            {
                "id": 15,
                "title": "Zen and Chan Buddhism: The Art of Sudden Enlightenment, Koans, and Empty Mind",
                "tier": "Tier 3: Schisms, Mystical Traditions & Theological Revolutions",
                "angle": "philosophical_contemplation",
                "slug": "zen_and_chan_buddhism_bodhidharma_koans_mu_satori_tea_ceremony",
                "question": "Why does Zen proclaim 'no reliance on words or letters, pointing directly to the human mind, seeing one's true nature and becoming a Buddha'?",
                "key_focus": "Bodhidharma's arrival in China, Huineng's Platform Sutra, Rinzai Koan practice ('What is the sound of one hand clapping?'), Soto Zazen sitting, and aesthetic Zen arts (tea, rock gardens).",
                "reason": "Explores the radical minimalism and direct meditative insight of East Asian Zen traditions."
            },
            {
                "id": 16,
                "title": "Kabbalah and Jewish Mysticism: The Tree of Life, Sefirot, and Tikkun Olam",
                "tier": "Tier 3: Schisms, Mystical Traditions & Theological Revolutions",
                "angle": "esoteric_cosmology",
                "slug": "kabbalah_jewish_mysticism_tree_of_life_sefirot_zohar_tikkun_olam",
                "question": "What is the secret mystical architecture of the 10 Sefirot, and why does Lurianic Kabbalah teach that humans are tasked with 'repairing a shattered universe' (Tikkun Olam)?",
                "key_focus": "The Zohar, Ein Sof (the Infinite), the breaking of the vessels (Shevirat Ha-Kelim), gathering divine sparks, and ethical action as cosmic restoration.",
                "reason": "Illuminates one of the world's most sophisticated symbolic cosmologies of divine-human partnership."
            },
            {
                "id": 17,
                "title": "Sacred Architecture: How Temples, Cathedrals, and Mosques Map Heaven onto Earth",
                "tier": "Tier 4: Secularization, Interfaith & Sacred Architecture",
                "angle": "sacred_spaces_geometry",
                "slug": "sacred_architecture_cathedrals_mandirs_mosques_sacred_geometry",
                "question": "How do Gothic cathedrals, Hindu Vastu Shastra mandirs, and Islamic geometric arabesques use acoustics, light, and geometry to induce transcendent awe?",
                "key_focus": "Gothic flying buttresses and stained-glass divine light (Abbot Suger), Hindu temple Mount Meru symbolism and Garbhagriha womb chambers, Islamic non-representational fractal tessellations and acoustic domes.",
                "reason": "Analyzes the physical manifestation of theology through breathtaking architectural engineering."
            },
            {
                "id": 18,
                "title": "Comparative Eschatology: How World Faiths Envision the End of the World",
                "tier": "Tier 4: Secularization, Interfaith & Sacred Architecture",
                "angle": "comparative_analysis",
                "slug": "comparative_eschatology_apocalypse_kalki_yugas_ragnarok_armageddon",
                "question": "Is time a straight line heading toward apocalyptic judgment, or a cyclical wheel endlessly dying and rebirthing across cosmic yugas?",
                "key_focus": "Linear Abrahamic apocalypses (Book of Revelation, Day of Qiyamah) vs. Cyclical Indic cosmologies (Kalki avatar, Kalpas, Yuga cycles), Hopi prophecy, and comparative mythology of world renewal.",
                "reason": "Contrasts the fundamental worldview divide between linear historical destinies and cyclical cosmic renewal."
            },
            {
                "id": 19,
                "title": "Max Weber and the Disenchantment of the World: Faith in the Age of Science",
                "tier": "Tier 4: Secularization, Interfaith & Sacred Architecture",
                "angle": "sociological_philosophy",
                "slug": "max_weber_disenchantment_secularization_faith_in_scientific_age",
                "question": "What happens to human meaning, ritual, and community when rational scientific empiricism displaces sacred myth and enchantment?",
                "key_focus": "Entzauberung (disenchantment), secularization hypothesis vs. religious resurgence in the Global South, the rise of 'spiritual but not religious' demographics, and modern existential vacuums.",
                "reason": "Provides the sociological lens necessary to understand the role of religion in 21st-century secularized societies."
            },
            {
                "id": 20,
                "title": "The Future of Religion: Artificial Intelligence, Transhumanism, and the Search for Transcendence",
                "tier": "Tier 4: Secularization, Interfaith & Sacred Architecture",
                "angle": "future_horizons",
                "slug": "future_of_religion_artificial_intelligence_transhumanism_new_sacred",
                "question": "Can AI write sacred scripture, will consciousness-uploading replace the afterlife, and how are world faiths responding to biomedical godhood?",
                "key_focus": "Theological responses to AGI, mind uploading as techno-immortality, algorithms as new oracles, religious ethics applied to gene editing, and the enduring human hunger for sacred mystery.",
                "reason": "Capstones the master curriculum by projecting humanity's ancient spiritual instincts into the high-tech 21st century."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Dead Sea Scrolls: 5 New AI Breakthroughs Decoding Ancient Biblical Secrets",
                "tier": "Trending / High Retention",
                "angle": "trending_breakthroughs",
                "slug": "dead_sea_scrolls_ai_decoding_breakthroughs_qumran_caves",
                "trend_score": 96,
                "why_trending": "Deep learning models are currently piecing together thousands of micro-fragments from Qumran caves, revealing never-before-seen variants of biblical texts.",
                "reason": "Viral intersection of artificial intelligence, ancient biblical archaeology, and explosive theological discoveries.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why Millions of Young Secular People Are Turning to Stoicism and Buddhism for Mental Health",
                "tier": "Trending / High Retention",
                "angle": "cultural_shifts",
                "slug": "young_generations_embracing_stoicism_and_buddhism_mental_health",
                "trend_score": 93,
                "why_trending": "Massive Gen Z/Millennial interest in secular mindfulness, Epictetus, and Vipassana meditation as an antidote to screen burnout and modern anxiety.",
                "reason": "Captures the massive cultural migration toward practical philosophical living without dogmatic dogma.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The Secret Underground Cities of Cappadocia: Christian Refugees and Ancient Bunkers",
                "tier": "Trending / High Retention",
                "angle": "archaeological_mysteries",
                "slug": "derinkuyu_underground_city_cappadocia_christian_sanctuary_deep_bunkers",
                "trend_score": 95,
                "why_trending": "Derinkuyu and Kaymakli 18-story subterranean cities continue to trend worldwide as archeological 3D LiDAR scans reveal vast defensive networks.",
                "reason": "Extreme fascination with subterranean civilizations, religious persecution, and jaw-dropping ancient engineering.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Lost Gospel of Thomas: Why Was This Text Excluded from the New Testament?",
                "tier": "Trending / High Retention",
                "angle": "historical_investigations",
                "slug": "gospel_of_thomas_gnostic_sayings_why_excluded_canon_nag_hammadi",
                "trend_score": 94,
                "why_trending": "Evergreen viral curiosity surrounding the 1945 Nag Hammadi library discovery and Gnostic 'sayings' gospels showing an esoteric, non-orthodox Jesus.",
                "reason": "High-retention historical mystery exploring suppressed theological manuscripts and canonical curation.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Ram Janmabhoomi and Varanasi: The Architectural Revival of Sacred Indian Tirthas",
                "tier": "Trending / High Retention",
                "angle": "modern_geopolitics_heritage",
                "slug": "ram_mandir_varanasi_corridor_architectural_revival_sacred_india",
                "trend_score": 97,
                "why_trending": "Huge global engagement and search volume around new mega-temple architecture, Vastu Shastra revivals, and heritage corridor reconstructions across India.",
                "reason": "Timely, culturally resonant exploration of living heritage engineering and sacred geography.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Vatican Secret Archives: What Is Actually Hidden Behind the Bronze Doors?",
                "tier": "Trending / High Retention",
                "angle": "documentary_investigation",
                "slug": "vatican_secret_archives_what_is_actually_hidden_pope_francis_declassified",
                "trend_score": 95,
                "why_trending": "Pope Francis declassified WWII-era documents; pop culture myths continue to circulate regarding 53 miles of secret shelving.",
                "reason": "Unbeatable hook debunking wild conspiracy theories while showcasing genuine historical treasures like Templar trial rolls and Galilean trial transcripts.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "The Simulation Hypothesis vs. Maya: Are Scientists Rediscovering Ancient Vedic Cosmology?",
                "tier": "Trending / High Retention",
                "angle": "philosophy_vs_physics",
                "slug": "simulation_hypothesis_vs_maya_quantum_physics_vedic_reality",
                "trend_score": 98,
                "why_trending": "Elon Musk, Nick Bostrom, and modern quantum physicists debating whether the universe is code, mirroring the 3,000-year-old Advaita concept of Maya and Lila.",
                "reason": "Ultra-viral philosophical bridge linking cutting-edge theoretical physics with timeless Eastern non-dualism.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "077_yoga_wellness": {
        "id": "077",
        "slug": "yoga_wellness",
        "title": "Yoga & Wellness",
        "category": "Health_Wellness",
        "audience": "Yoga Practitioners, Holistic Wellness Seekers, Breathwork Enthusiasts, Movement Artists (Global)",
        "progression": [
            ("Tier 1: The Eight Limbs (Ashtanga), Surya Namaskar & Breath Fundamentals (Scratch / Beginner)",
             "Patanjali's Yoga Sutras (Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi), sun salutation biomechanics, and diaphragmatic Ujjayi breath."),
            ("Tier 2: Vinyasa Flows, Fascial Meridians & Pranayama Physiology (Intermediate)",
             "Nadi Shodhana (alternate nostril breathing) balancing sympathetic/parasympathetic tone, myofascial lines in standing postures, Bandhas (energy locks), and restorative Yin yoga."),
            ("Tier 3: Kundalini Mechanics, Subtle Body Nadis & The Polyvagal Vagus Nerve Bridge (Upper Intermediate)",
             "Ida, Pingala, Sushumna nadis, 7 chakra psycho-energetic nodes, polyvagal theory (Stephen Porges) through chanting and pranayama, and Hatha Yoga Pradipika cleansing Kriyas."),
            ("Tier 4: Raja Yoga Consciousness, Samadhi States & Neuroscience of Modern Mind-Body Mastery (Advanced / Expert)",
             "EEG brainwave mapping during deep meditation (Gamma/Theta surges), neuroplastic down-regulation of the amygdala, non-dual Advaita integration, and ethical living off the mat.")
        ],
        "flagship": {
            "title": "The Eight Limbs of Yoga: How Patanjali Built the Ultimate Science of Human Consciousness",
            "angle": "philosophy_origins",
            "slug": "077_yoga_wellness_philosophy_origins_patanjali_eight_limbs_ashtanga"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Eight Limbs of Yoga: How Patanjali Built the Ultimate Science of Human Consciousness",
                "tier": "Tier 1: Eight Limbs & Breath Fundamentals",
                "angle": "philosophy_origins",
                "slug": "patanjali_eight_limbs_ashtanga_yoga_sutras_chitta_vritti_nirodha",
                "question": "Why is physical posture (Asana) only one-eighth of traditional Yoga, and what was Patanjali's actual blueprint to still the fluctuations of the mind?",
                "key_focus": "Sutra 1.2 'Yogas chitta vritti nirodha', the progression from ethical restraints (Yamas/Niyamas) to internal absorption (Pratyahara, Dharana, Dhyana, Samadhi).",
                "reason": "Flagship launch episode; clarifies the authentic multidimensional discipline of yoga beyond modern gym stereotypes."
            },
            {
                "id": 2,
                "title": "Surya Namaskar: The Biomechanical and Energetic Anatomy of the Sun Salutation",
                "tier": "Tier 1: Eight Limbs & Breath Fundamentals",
                "angle": "biomechanical_breakdown",
                "slug": "surya_namaskar_biomechanics_spinal_flexion_extension_solar_energy",
                "question": "What happens to your spine, endocrine system, and fascial web when you perform the 12 linked postures of Surya Namaskar with synchronized breath?",
                "key_focus": "Alternating spinal flexion and extension, hamstring and hip flexor mobilization, solar plexus activation, aerobic circulation, and mantra resonance.",
                "reason": "Foundational movement sequence practiced by millions globally every morning."
            },
            {
                "id": 3,
                "title": "Pranayama Demystified: The Science of Using Breath to Control Heart Rate and the Brain",
                "tier": "Tier 1: Eight Limbs & Breath Fundamentals",
                "angle": "scientific_physiology",
                "slug": "pranayama_science_respiratory_sinus_arrhythmia_vagus_nerve",
                "question": "How does deliberate breath manipulation immediately modulate blood pressure, heart rate variability (HRV), and prefrontal cortex activity?",
                "key_focus": "Inhalation vs. exhalation duration, nitric oxide production in nasal breathing, respiratory sinus arrhythmia, and downregulating the fight-or-flight response.",
                "reason": "Provides the hard biological science explaining why breath control transforms nervous system state."
            },
            {
                "id": 4,
                "title": "The Biomechanics of Standing Postures: Building Rooted Stability from Tadasana to Warrior",
                "tier": "Tier 1: Eight Limbs & Breath Fundamentals",
                "angle": "posture_alignment",
                "slug": "standing_postures_biomechanics_tadasana_virabhadrasana_pelvic_neutral",
                "question": "Why do common postural misalignments in Warrior poses strain knees and lower backs, and how does Tadasana (Mountain Pose) calibrate whole-body posture?",
                "key_focus": "Pada Bandha (foot locks), pelvic neutral tilt, hip joint internal vs external rotation, glute engagement, and thoracic spine expansion.",
                "reason": "Essential injury-prevention guide for everyday practitioners and yoga teachers."
            },
            {
                "id": 5,
                "title": "Ujjayi and Box Breathing: The Navy SEAL & Yogi Secret to Instant Calm Under Stress",
                "tier": "Tier 1: Eight Limbs & Breath Fundamentals",
                "angle": "breathwork_protocols",
                "slug": "ujjayi_and_box_breathing_glottis_constriction_stress_regulation",
                "question": "Why does constricting the back of your throat during breathing trigger an instant parasympathetic brake in high-stress situations?",
                "key_focus": "Ocean breath glottis mechanics, baroreceptor stimulation, box breathing 4-4-4-4 ratios, and applications in athletic recovery and anxiety management.",
                "reason": "Highly practical breath protocol connecting ancient yogic Ujjayi to modern tactical performance."
            },
            {
                "id": 6,
                "title": "The Fascial Web: How Yoga Remodels Connective Tissue and Unlocks Stored Tension",
                "tier": "Tier 2: Vinyasa Flows & Fascial Physiology",
                "angle": "anatomical_science",
                "slug": "fascia_and_yoga_myofascial_lines_interstitial_hydration_tension",
                "question": "Why does stretching muscles alone fail to relieve chronic tightness unless you target the collagenous fascial sheath wrapping your entire body?",
                "key_focus": "Tom Myers' Anatomy Trains (superficial back and front lines), fascial glide and hyaluronic acid hydration, mechanotransduction, and somatic tension storage.",
                "reason": "Explains the modern myofascial breakthroughs validating traditional long-hold yogic postures."
            },
            {
                "id": 7,
                "title": "Yin Yoga vs. Yang Yoga: Balancing Dynamic Flow with Deep Joint Stillness",
                "tier": "Tier 2: Vinyasa Flows & Fascial Physiology",
                "angle": "comparative_practice",
                "slug": "yin_yoga_vs_yang_vinyasa_collagen_remodeling_meridians_parasympathetic",
                "question": "Why do 5-minute passive floor holds remodel ligaments and tendons in ways dynamic sweating vinyasa flows never can?",
                "key_focus": "Paul Grilley and Bernie Clark's Yin foundations, plastic vs. elastic tissue stress, Chinese meridian lines mapped onto yoga postures, and emotional release during hip openers.",
                "reason": "Deconstructs the complementary balance between high-energy flows and restorative, introspective stillness."
            },
            {
                "id": 8,
                "title": "The Bandhas: Unlocking the Body's Three Internal Energy Locks",
                "tier": "Tier 2: Vinyasa Flows & Fascial Physiology",
                "angle": "internal_energetics",
                "slug": "the_three_bandhas_mula_uddiyana_jalandhara_pelvic_core_stability",
                "question": "How do Mula Bandha, Uddiyana Bandha, and Jalandhara Bandha create intra-abdominal pressure, prevent pelvic floor dysfunction, and lighten handstands?",
                "key_focus": "Pelvic floor levator ani engagement (Mula), diaphragmatic vacuum lift (Uddiyana), cervical chin lock (Jalandhara), and Maha Bandha (the great lock).",
                "reason": "Demystifies the most elusive and misunderstood internal physical locks in intermediate yoga."
            },
            {
                "id": 9,
                "title": "Nadi Shodhana: The Neuroscience of Alternate Nostril Breathing and Hemispheric Balance",
                "tier": "Tier 2: Vinyasa Flows & Fascial Physiology",
                "angle": "neurobiology_breath",
                "slug": "nadi_shodhana_alternate_nostril_breathing_brain_hemispheres_autonomic",
                "question": "Does breathing through your left versus right nostril actually alter cerebral blood flow and balance autonomic nervous system activity?",
                "key_focus": "The ultradian nasal cycle, Ida (cooling/parasympathetic) and Pingala (heating/sympathetic) nadis, EEG brain hemisphere synchronization, and cortisol regulation.",
                "reason": "Provides scientific evidence validating the primary balancing pranayama of Hatha Yoga."
            },
            {
                "id": 10,
                "title": "The Spine in Yoga: Preventing Degeneration Through 6 Movements of Daily Spinal Mobility",
                "tier": "Tier 2: Vinyasa Flows & Fascial Physiology",
                "angle": "spinal_health",
                "slug": "six_movements_of_the_spine_intervertebral_discs_axial_extension",
                "question": "Why does ancient yoga claim 'you are as young as your spine is flexible,' and what are the 6 non-negotiable spinal vectors for longevity?",
                "key_focus": "Flexion, extension, lateral flexion (left/right), axial rotation (left/right), and axial elongation; disc imbibition, facet joint nourishment, and preventing desk-slouch kyphosis.",
                "reason": "A high-utility health masterclass for combating modern sedentary spine degradation."
            },
            {
                "id": 11,
                "title": "The Polyvagal Theory and Yoga: Healing the Vagus Nerve Through Chanting and Movement",
                "tier": "Tier 3: Kundalini, Nadis & Polyvagal Science",
                "angle": "somatic_psychology",
                "slug": "polyvagal_theory_vagus_nerve_yoga_dr_stephen_porges_nervous_system",
                "question": "How do OM chanting, prolonged exhalations, and restorative asanas activate the ventral vagal complex to shift the body out of chronic freeze/fight trauma?",
                "key_focus": "Dr. Stephen Porges' Polyvagal hierarchy (Dorsal vagal freeze, Sympathetic mobilization, Ventral vagal social engagement), laryngeal vibration during chanting, and somatic safety cues.",
                "reason": "Connects ancient yogic sound and movement to cutting-edge trauma recovery and nervous system healing."
            },
            {
                "id": 12,
                "title": "The Subtle Body: Nadis, Chakras, and the Psycho-Energetic Map of Human Experience",
                "tier": "Tier 3: Kundalini, Nadis & Polyvagal Science",
                "angle": "esoteric_anatomy",
                "slug": "subtle_body_nadis_chakras_sushumna_nerve_plexuses_endocrine_glands",
                "question": "What is the historical reality behind the 7 Chakras, and how do they correspond to major biological nerve plexuses and endocrine gland clusters?",
                "key_focus": "Sushumna, Ida, Pingala channels, the 7 primary chakras from Muladhara to Sahasrara, psychological developmental themes per chakra, and distinguishing myth from somatic experience.",
                "reason": "Provides a mature, non-commercialized demystification of the chakra system grounded in authentic texts."
            },
            {
                "id": 13,
                "title": "Hatha Yoga Pradipika: The 6 Shatkarmas and Medieval Cleansing Techniques",
                "tier": "Tier 3: Kundalini, Nadis & Polyvagal Science",
                "angle": "historical_texts",
                "slug": "hatha_yoga_pradipika_shatkarmas_neti_nauli_kapalbhati_purification",
                "question": "What are the six ancient purification kriyas designed to prepare the body for intense energy work, and which ones survive in modern medicine?",
                "key_focus": "Jala Neti (nasal irrigation), Kapalbhati (frontal brain cleansing breath), Nauli (abdominal churning), Trataka (candle gazing), Dhauti, and Basti; hygiene and mucus clearance in pre-modern India.",
                "reason": "Explores the 15th-century root manual of Hatha Yoga and its radical bodily cleansing protocols."
            },
            {
                "id": 14,
                "title": "Yoga Nidra: The Science of Non-Sleep Deep Rest (NSDR) and Brainwave Modulation",
                "tier": "Tier 3: Kundalini, Nadis & Polyvagal Science",
                "angle": "sleep_neuroscience",
                "slug": "yoga_nidra_non_sleep_deep_rest_nsdr_theta_delta_brainwaves_dopamine",
                "question": "How can a 30-minute guided Yoga Nidra session replenish dopamine reserves and induce neurochemical recovery equivalent to 2-3 hours of deep sleep?",
                "key_focus": "Body scanning rotation of consciousness, sankalpa (resolve), EEG progression into Theta (4-8 Hz) and Delta waves, Andrew Huberman's NSDR protocols, and reducing insomnia.",
                "reason": "Massively popular evidence-based relaxation technique used by neuroscientists, athletes, and meditators."
            },
            {
                "id": 15,
                "title": "Kundalini Awakening: Deconstructing the Serpent Power Between Psychology and Mysticism",
                "tier": "Tier 3: Kundalini, Nadis & Polyvagal Science",
                "angle": "psychospiritual_investigations",
                "slug": "kundalini_awakening_serpent_power_gopi_krishna_carl_jung_kundalini",
                "question": "What happens when latent psychosomatic energy uncoils from the base of the spine, and why did Carl Jung warn of premature Kundalini activation?",
                "key_focus": "Arthur Avalon's The Serpent Power, Gopi Krishna's autobiographical accounts, involuntary tremors (Kriyas), Carl Jung's 1932 Kundalini seminars, and spiritual emergence vs. psychosis.",
                "reason": "Tackles one of the most intense, intriguing, and misunderstood phenomena in advanced yoga."
            },
            {
                "id": 16,
                "title": "The Neuroscience of Meditation: How Daily Mindfulness Shrinks the Amygdala and Thickens the Cortex",
                "tier": "Tier 4: Raja Yoga & Neuroscience of Consciousness",
                "angle": "neuroimaging_breakthroughs",
                "slug": "neuroscience_of_meditation_mri_amygdala_prefrontal_cortex_dr_sara_lazar",
                "question": "What do Harvard fMRI brain scans reveal about the permanent structural remodeling of grey matter in regular meditators after just 8 weeks?",
                "key_focus": "Dr. Sara Lazar's neuroplasticity research, amygdala down-regulation (reduced fear response), hippocampus enlargement, Default Mode Network (DMN) quieting, and cellular telomere protection.",
                "reason": "Irrefutable hard medical evidence supporting the brain-altering power of yogic mental training."
            },
            {
                "id": 17,
                "title": "Pratyahara to Dharana: Bridging Sensory Withdrawal to Unbroken Concentration",
                "tier": "Tier 4: Raja Yoga & Neuroscience of Consciousness",
                "angle": "cognitive_training",
                "slug": "pratyahara_to_dharana_sensory_withdrawal_attention_span_digital_age",
                "question": "How can you intentionally disconnect the senses from external digital stimulation to achieve laser-focused mental concentration on a single point?",
                "key_focus": "The turtle retracting its limbs metaphor, sensory deprivation mechanisms, Ekagrata (one-pointed focus), attentional blink reduction, and training deep cognitive stamina.",
                "reason": "The essential cognitive training tool for reclaiming shattered attention spans in the smartphone era."
            },
            {
                "id": 18,
                "title": "Samadhi and Non-Dual States: What Transcending the Ego Actually Feels Like",
                "tier": "Tier 4: Raja Yoga & Neuroscience of Consciousness",
                "angle": "transpersonal_psychology",
                "slug": "samadhi_savikalpa_nirvikalpa_non_dual_consciousness_oceanic_feeling",
                "question": "What are the distinctions between Savikalpa (with object) and Nirvikalpa (objectless) Samadhi, and what is the neurobiology of ego dissolution?",
                "key_focus": "Parietal lobe deactivation (loss of physical body boundaries), Gamma brainwave coherence (>40 Hz), oceanic oneness experiences, and returning from peak states to grounded daily life.",
                "reason": "The summit of classical Raja Yoga philosophy and peak human experiential states."
            },
            {
                "id": 19,
                "title": "Yoga Beyond the Mat: Living Karma Yoga and the Bhagavad Gita's Formula for Action",
                "tier": "Tier 4: Raja Yoga & Neuroscience of Consciousness",
                "angle": "philosophical_ethics",
                "slug": "karma_yoga_bhagavad_gita_nishkama_karma_action_without_attachment",
                "question": "How do you practice yoga while answering emails, running a business, or raising children, according to Krishna's teachings in the Gita?",
                "key_focus": "Nishkama Karma (action without desire for fruits), equanimity in success and failure, duty (Svadharma), transforming daily labor into meditative offering.",
                "reason": "Brings the entire physical practice back into grounded, ethical daily action in the real world."
            },
            {
                "id": 20,
                "title": "The Longevity Blueprint: Integrating Yogic Asana, Fasting, and Circadian Rhythms",
                "tier": "Tier 4: Raja Yoga & Neuroscience of Consciousness",
                "angle": "holistic_longevity",
                "slug": "yogic_longevity_blueprint_asana_mitochondrial_health_circadian_rhythm",
                "question": "How does combining daily mobility, conscious breathing, intermittent fasting (Mitahara), and sleep hygiene add 15+ healthy biological years to life?",
                "key_focus": "Autophagy stimulation through Mitahara, mitochondrial biogenesis from gentle hypoxia in pranayama, joint longevity via synovial fluid pumping, and long-term vitality metrics.",
                "reason": "Synthesizes the entire 20-episode curriculum into an actionable daily lifelong wellness routine."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Huberman Vagus Nerve Hack: Why Box Breathing Works in Under 90 Seconds",
                "tier": "Trending / High Retention",
                "angle": "viral_neuroscience",
                "slug": "huberman_vagus_nerve_box_breathing_physiological_sigh_fast_calm",
                "trend_score": 98,
                "why_trending": "Massive global viral wave of interest in the 'Physiological Sigh' and fast autonomic nervous system resets popularized by Stanford neurobiology podcasts.",
                "reason": "Immediate real-time retention hook combining laboratory neurobiology with accessible yogic breathwork.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Somatic Exercises for Trapped Emotional Trauma: What Actually Happens in the Psoas Muscle?",
                "tier": "Trending / High Retention",
                "angle": "somatic_healing",
                "slug": "psoas_muscle_somatic_emotional_release_trauma_fight_or_flight",
                "trend_score": 97,
                "why_trending": "Explosive TikTok and YouTube search volume around 'somatic shaking', hip releases, and why crying often occurs during deep pigeon pose hip openers.",
                "reason": "Extremely high viewer empathy and curiosity regarding somatic trauma storage in pelvic musculature.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Yoga vs. Gym Lifting: Can You Build Real Muscle and Strength with Just Bodyweight Asana?",
                "tier": "Trending / High Retention",
                "angle": "fitness_debate",
                "slug": "yoga_vs_weightlifting_calisthenics_hypertrophy_handstands_strength",
                "trend_score": 94,
                "why_trending": "Continuous viral debate among fitness enthusiasts comparing gymnastic calisthenics/handstand strength with traditional barbell bodybuilding.",
                "reason": "High-engagement comparative debate with practical strength and flexibility breakdowns.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Dark Side of Kundalini: Spontaneous Kriyas, Nerve Burnout, and Spiritual Emergencies",
                "tier": "Trending / High Retention",
                "angle": "investigative_warning",
                "slug": "dark_side_of_kundalini_spiritual_emergency_nervous_system_overload",
                "trend_score": 93,
                "why_trending": "Surging curiosity around intense meditative side effects, nervous system overstimulation, and the clinical psychiatric classification of Kundalini syndrome.",
                "reason": "Riveting cautionary topic that cuts through superficial new-age fluff with serious physiological analysis.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Cold Showers + Tummo Breath: The Wim Hof Method vs. Ancient Tibetan Monks",
                "tier": "Trending / High Retention",
                "angle": "extreme_physiology",
                "slug": "wim_hof_method_vs_tibetan_tummo_inner_fire_cold_exposure_immune",
                "trend_score": 96,
                "why_trending": "Wim Hof ice baths, Tummo breathing, and voluntary immune system control demonstrated under university hospital laboratory monitoring.",
                "reason": "Captivating clash of modern biohacking culture with ancient Himalayan asceticism.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Why Modern Chairs Are Destroying Your Hips: How Ancient Floor Sitting Rebuilds Posture",
                "tier": "Trending / High Retention",
                "angle": "lifestyle_ergonomics",
                "slug": "modern_chairs_destroying_hips_floor_sitting_squatting_longevity",
                "trend_score": 95,
                "why_trending": "Surge in ergonomic interest around Japanese Seiza, lotus floor-sitting, and the 'sitting-rising test' predicting all-cause mortality.",
                "reason": "Everyday relatability with eye-opening anatomical evidence showing the hidden physical cost of office chairs.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Does Chanting 'OM' at 432 Hz Actually Change Brainwaves? Scientific Analysis of Vedic Mantras",
                "tier": "Trending / High Retention",
                "angle": "acoustic_neuroscience",
                "slug": "chanting_om_432hz_cymatics_vagus_nerve_fmri_mantra_sound",
                "trend_score": 95,
                "why_trending": "Cymatics soundwave demonstrations and fMRI scans measuring cerebral vascular changes during prolonged Om chanting continue to go viral across social media.",
                "reason": "Separates pseudo-scientific frequency myths from verified neuro-acoustic mechanisms of chanting.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "078_books_literature": {
        "id": "078",
        "slug": "books_literature",
        "title": "Books & Literature",
        "category": "Arts_Culture",
        "audience": "Avid Readers, Book Clubs, Literature Students, Aspiring Novelists, Classic Lore Lovers (Global)",
        "progression": [
            ("Tier 1: Literary Classics, Narrative Arcs & The Hero's Journey (Scratch / Beginner)",
             "Joseph Campbell's Monomyth, Freytag's pyramid, foundational classics (Homer's Odyssey, Shakespeare's Hamlet, Austen's Pride and Prejudice), and close reading strategies."),
            ("Tier 2: Literary Movements: Realism, Modernism, Magical Realism & Dystopia (Intermediate)",
             "Victorian industrial realism (Dickens), Modernist stream-of-consciousness (Woolf, Joyce), Latin American Magical Realism (Garcia Marquez), and 20th-century dystopian warnings (Orwell, Huxley)."),
            ("Tier 3: Unreliable Narrators, Deep Symbolism & Subtext Deconstruction (Upper Intermediate)",
             "Nabokov's narrative misdirection, Russian existentialism (Dostoevsky, Tolstoy), post-colonial literature (Achebe, Rushdie), and multi-layered poetic meters."),
            ("Tier 4: The Western & Eastern Canons, Epics Across Epochs & The Future of Storytelling (Advanced / Expert)",
             "Harold Bloom's canon disputes, the Mahabharata & Gilgamesh structural scope, postmodern metafiction (Borges, Calvino), and interactive narrative forms in the digital age.")
        ],
        "flagship": {
            "title": "The Hero with a Thousand Faces: The Universal Story Formula That Powers All Epic Fiction",
            "angle": "narrative_structure",
            "slug": "078_books_literature_narrative_structure_joseph_campbell_monomyth"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Hero with a Thousand Faces: The Universal Story Formula That Powers All Epic Fiction",
                "tier": "Tier 1: Classics & Narrative Arcs",
                "angle": "narrative_structure",
                "slug": "joseph_campbell_monomyth_hero_journey_star_wars_lord_of_the_rings",
                "question": "Why does almost every legendary story from Gilgamesh to Star Wars follow the exact same 17-stage psychological journey?",
                "key_focus": "Departure, Initiation, Return; Campbell's synthesis of Jungian archetypes, George Lucas's conscious script design, and why the Monomyth resonates universally in the human brain.",
                "reason": "Flagship launch episode; unlocks the underlying structural code of all world storytelling."
            },
            {
                "id": 2,
                "title": "Homer's Odyssey: The Blueprint of Adventure, Nostos, and Monster Archetypes",
                "tier": "Tier 1: Classics & Narrative Arcs",
                "angle": "classical_origins",
                "slug": "homers_odyssey_nostos_homecoming_cyclops_sirens_cleverness",
                "question": "How did Homer's 2,800-year-old tale of a clever king's voyage home invent modern narrative techniques like in media res and non-linear flashbacks?",
                "key_focus": "Nostos (longing for home), Odysseus's Metis (cunning intelligence) vs. Achilles' brute force, Polyphemus and the Sirens as psychological trials, oral formulaic poetry.",
                "reason": "The foundational epic that established Western narrative fiction and character psychology."
            },
            {
                "id": 3,
                "title": "Shakespeare's Hamlet: Decoding the Architecture of Soliloquy and Existential Paralysis",
                "tier": "Tier 1: Classics & Narrative Arcs",
                "angle": "dramatic_analysis",
                "slug": "shakespeares_hamlet_soliloquies_to_be_or_not_to_be_paralysis_of_intellect",
                "question": "Why is 'To be or not to be' the most analyzed speech in human history, and how did Shakespeare invent modern self-reflective consciousness on stage?",
                "key_focus": "The invention of inwardness (Harold Bloom thesis), revenge tragedy conventions subverted by philosophical delay, memento mori Yorick scene, and metatheatre ('the play's the thing').",
                "reason": "Deep-dives into the masterpiece that defined English dramatic literature and modern psychology."
            },
            {
                "id": 4,
                "title": "Jane Austen's Free Indirect Discourse: The Revolutionary Style That Modernized the Novel",
                "tier": "Tier 1: Classics & Narrative Arcs",
                "angle": "literary_craft",
                "slug": "jane_austen_free_indirect_discourse_pride_and_prejudice_irony",
                "question": "How did Jane Austen secretly blend the third-person narrator's voice with her characters' private biases, creating modern psychological realism?",
                "key_focus": "Free indirect style mechanics in Pride and Prejudice and Emma, social satire of Regency class and marriage economics, dramatic irony, and dialogue pacing.",
                "reason": "Highlights the crucial technical evolution in novelistic point-of-view and character interiority."
            },
            {
                "id": 5,
                "title": "Freytag's Pyramid: How to Analyze Dramatic Tension in Any Novel in 5 Minutes",
                "tier": "Tier 1: Classics & Narrative Arcs",
                "angle": "structural_breakdown",
                "slug": "freytags_pyramid_dramatic_arc_exposition_climax_catastrophe",
                "question": "Why do the greatest tragedies and thrillers rely on Gustav Freytag's five-act triangular arc of rising action, turning point, and catastrophe?",
                "key_focus": "Inciting incident, rising complications, central peripeteia (reversal of fortune), falling action, and denouement/anagnorisis (recognition).",
                "reason": "The fundamental analytical tool every literature student and reader needs to deconstruct plot pacing."
            },
            {
                "id": 6,
                "title": "1984 vs. Brave New World: Which Dystopia Actually Came True?",
                "tier": "Tier 2: Literary Movements & Dystopias",
                "angle": "comparative_dystopia",
                "slug": "1984_orwell_vs_brave_new_world_huxley_fear_vs_pleasure_surveillance",
                "question": "Did our modern world become George Orwell's terrifying boot-stamping surveillance state, or Aldous Huxley's drug-sedated pleasure prison?",
                "key_focus": "Newspeak and Doublethink vs. Soma and conditioning, Neil Postman's 'Amusing Ourselves to Death' analysis, algorithms, social media dopamine loops, and state control.",
                "reason": "One of the most provocative and culturally relevant comparative literature discussions of all time."
            },
            {
                "id": 7,
                "title": "One Hundred Years of Solitude: How Gabriel García Márquez Invented Magical Realism",
                "tier": "Tier 2: Literary Movements & Dystopias",
                "angle": "literary_movements",
                "slug": "one_hundred_years_of_solitude_magical_realism_macondo_buendia",
                "question": "Why does treating flying carpets and yellow butterflies as ordinary facts—while treating modern magnets and ice as miracles—create the magic of Macondo?",
                "key_focus": "Grandmother storytelling tone, cyclical historical trauma in Latin America, memory and forgetting plagues, Macondo as an allegory for post-colonial Colombia.",
                "reason": "Celebrates the towering masterpiece of Latin American Boom literature and surreal truth-telling."
            },
            {
                "id": 8,
                "title": "Modernism and Stream of Consciousness: How Virginia Woolf and James Joyce Broke Time",
                "tier": "Tier 2: Literary Movements & Dystopias",
                "angle": "modernist_revolutions",
                "slug": "stream_of_consciousness_woolf_mrs_dalloway_joyce_ulysses_interior_monologue",
                "question": "Why did World War I convince modernist writers that traditional chronological plots were lies, prompting them to write novels covering only a single day?",
                "key_focus": "Mrs. Dalloway's Big Ben chiming against psychological time (Bergson's la durée), Ulysses' Dublin labyrinth, interior monologue, fracturing of Victorian certainty.",
                "reason": "Deconstructs the 20th-century aesthetic revolution that mirrored quantum physics and psychoanalysis."
            },
            {
                "id": 9,
                "title": "Charles Dickens and Victorian Social Realism: How Novels Changed Child Labor Laws",
                "tier": "Tier 2: Literary Movements & Dystopias",
                "angle": "societal_impact",
                "slug": "charles_dickens_victorian_realism_oliver_twist_bleak_house_reform",
                "question": "How did serialized installments of Oliver Twist and Bleak House shame the British Empire into passing public health and labor reforms?",
                "key_focus": "Workhouse exposes, serialized cliffhangers creating mass public obsession, Chancery court legal satire in Bleak House, and unforgettable caricatures grounded in London squalor.",
                "reason": "Demonstrates the tangible political and legislative power of empathetic narrative fiction."
            },
            {
                "id": 10,
                "title": "Franz Kafka: The Anatomy of Bureaucratic Nightmare and 'The Metamorphosis'",
                "tier": "Tier 2: Literary Movements & Dystopias",
                "angle": "existential_absurdism",
                "slug": "franz_kafka_metamorphosis_gregor_samsa_bureaucratic_absurdism_the_trial",
                "question": "What makes an experience truly 'Kafkaesque', and why does waking up as a giant insect expose the dehumanizing reality of modern wage labor?",
                "key_focus": "Gregor Samsa's immediate worry about missing his train, The Trial's faceless legal apparatus, alienation, shame, and Kafka's strained relationship with his father.",
                "reason": "Explores the author whose name became the global adjective for modern institutional absurdity."
            },
            {
                "id": 11,
                "title": "Crime and Punishment: Dostoevsky's Psychological Dissection of the Superman Delusion",
                "tier": "Tier 3: Unreliable Narrators & Subtext",
                "angle": "psychological_depth",
                "slug": "crime_and_punishment_dostoevsky_raskolnikov_extraordinary_man_guilt",
                "question": "Why does Raskolnikov's intellectual theory that extraordinary men have the right to murder collapse under the weight of his own feverish conscience?",
                "key_focus": "The Napoleonic theory of moral exemption, the yellow ticket of Sonya Marmeladova, Porfiry Petrovich's cat-and-mouse interrogation psychology, and redemption in Siberia.",
                "reason": "Widely regarded as the supreme psychological thriller and philosophical interrogation of moral hubris."
            },
            {
                "id": 12,
                "title": "The Master of the Unreliable Narrator: How Nabokov Tricked You in Lolita and Pale Fire",
                "tier": "Tier 3: Unreliable Narrators & Subtext",
                "angle": "narrative_deception",
                "slug": "nabokov_unreliable_narrator_humbert_humbert_lolita_pale_fire_kinbote",
                "question": "How does Vladimir Nabokov weaponize dazzling, lyrical prose to seduce the reader into sympathizing with monsters and madmen?",
                "key_focus": "Humbert Humbert's rhetorical trap for the jury, poetic diversion tactics, Charles Kinbote's deranged 999-line poem commentary in Pale Fire, reader complicity.",
                "reason": "A masterclass in advanced literary analysis deconstructing the limits of narrative truth."
            },
            {
                "id": 13,
                "title": "Things Fall Apart: Chinua Achebe's Powerful Reclamation of African History",
                "tier": "Tier 3: Unreliable Narrators & Subtext",
                "angle": "post_colonial_studies",
                "slug": "things_fall_apart_chinua_achebe_okonkwo_igbo_culture_colonial_collapse",
                "question": "How did Chinua Achebe's portrait of Okonkwo dismantle Joseph Conrad's racist colonial depiction of Africa as a 'Heart of Darkness'?",
                "key_focus": "Sophistication of Igbo judicial and agricultural traditions, Okonkwo's tragic fear of weakness, Yeats' 'The Second Coming' epigraph, and the District Commissioner's insulting concluding paragraph.",
                "reason": "The defining post-colonial novel that restored authentic African agency to world literature."
            },
            {
                "id": 14,
                "title": "The Russian Soul: Tolstoy's War and Peace vs. Dostoevsky's Brothers Karamazov",
                "tier": "Tier 3: Unreliable Narrators & Subtext",
                "angle": "comparative_titans",
                "slug": "tolstoy_vs_dostoevsky_war_and_peace_brothers_karamazov_grand_inquisitor",
                "question": "Are you a Tolstoy person or a Dostoevsky person? The ultimate clash between panoramic historical realism and volcanic theological passion.",
                "key_focus": "Tolstoy's microscopic sensory observation and theory of history vs. Dostoevsky's fever dreams, Ivan Karamazov's 'The Grand Inquisitor' parable, and the problem of evil.",
                "reason": "Explores the greatest rivalry in world literary history and its two radically different worldviews."
            },
            {
                "id": 15,
                "title": "The Great Gatsby and the Death of the American Dream: The Green Light Deconstructed",
                "tier": "Tier 3: Unreliable Narrators & Subtext",
                "angle": "symbolism_and_myth",
                "slug": "the_great_gatsby_f_scott_fitzgerald_green_light_eyes_of_dr_eckleburg",
                "question": "Why is F. Scott Fitzgerald's slim novel considered the defining autopsy of American optimism, wealth, and self-invention?",
                "key_focus": "Nick Carraway's ambivalent narration, Gatsby's manufactured identity, the valley of ashes, the billboard eyes of Dr. T.J. Eckleburg, and the boats beating back ceaselessly into the past.",
                "reason": "Dissects the quintessential American high-school and university classic to reveal its dark economic cynicism."
            },
            {
                "id": 16,
                "title": "The Mahabharata: The World's Longest Epic and Its Unforgiving Moral Ambiguity",
                "tier": "Tier 4: Canons, Epics & The Future of Story",
                "angle": "epic_traditions",
                "slug": "mahabharata_longest_epic_dharma_kurukshetra_karna_yudhishthira",
                "question": "Why does the 100,000-verse Sanskrit epic refuse to give simple heroes or villains, presenting a world where Dharma itself is subtle and contested?",
                "key_focus": "The dice game humiliation of Draupadi, Karna's tragic loyalty to Duryodhana, Krishna's pragmatic wartime ethics, Yudhishthira's final vision of Hell and Heaven.",
                "reason": "Examines an epic four times the size of the Iliad and Odyssey combined, possessing unmatched philosophical complexity."
            },
            {
                "id": 17,
                "title": "Jorge Luis Borges: The Labyrinths, Infinite Libraries, and Mirrors That Anticipated the Internet",
                "tier": "Tier 4: Canons, Epics & The Future of Story",
                "angle": "postmodern_metafiction",
                "slug": "jorge_luis_borges_library_of_babel_garden_of_forking_paths_infinite_data",
                "question": "How did a blind Argentine librarian predict search algorithms, parallel universes, and Wikipedia in five-page philosophical short stories?",
                "key_focus": "The Library of Babel (infinite permutations of text), The Garden of Forking Paths (multiverse branching narratives), Funes the Memorious (the curse of total recall), and metafictional paradoxes.",
                "reason": "Celebrates the patron saint of speculative intellectuals and postmodern digital architecture."
            },
            {
                "id": 18,
                "title": "Harold Bloom's Western Canon: The Anxiety of Influence and Who Deserves Immortality",
                "tier": "Tier 4: Canons, Epics & The Future of Story",
                "angle": "literary_criticism",
                "slug": "harold_bloom_western_canon_anxiety_of_influence_aesthetic_supremacy",
                "question": "Do certain books possess transcendent aesthetic genius that defies political fashion, or are canons simply instruments of historical power?",
                "key_focus": "The Anxiety of Influence (poets misreading predecessors to carve out original space), the School of Resentment debate, Shakespeare as the center of the canon, and aesthetic autonomy.",
                "reason": "Engages directly with the most passionate and contentious literary debate of the late 20th century."
            },
            {
                "id": 19,
                "title": "The Art of the Ending: How the Greatest Final Sentences Echo in Eternity",
                "tier": "Tier 4: Canons, Epics & The Future of Story",
                "angle": "craft_analysis",
                "slug": "the_art_of_the_ending_greatest_final_sentences_gatsby_ulysses_blood_meridian",
                "question": "What separates an ending that satisfies from an ending that shatters you, and why do final sentences linger for decades?",
                "key_focus": "James Joyce's 'The Dead' ('falling softly upon all the living and the dead'), Cormac McCarthy's Blood Meridian dance, Toni Morrison's Beloved, resonance and poetic cadences.",
                "reason": "An inspiring masterclass in craft dissecting how legendary authors land the final emotional punch."
            },
            {
                "id": 20,
                "title": "The Future of the Book: AI Authorship, Interactive Novels, and the Survival of Deep Reading",
                "tier": "Tier 4: Canons, Epics & The Future of Story",
                "angle": "future_horizons",
                "slug": "future_of_the_book_ai_novels_deep_reading_maryanne_wolf_bi-literate_brain",
                "question": "In an era of hyper-fast video feeds and Large Language Models, will long-form narrative novels survive, or will human attention permanently mutate?",
                "key_focus": "Maryanne Wolf's 'Reader, Come Home' neuroscience of deep reading, generative AI co-writing tools, branching narrative interactive games, and the enduring uniqueness of human soul in prose.",
                "reason": "Concludes the curriculum by defending the irreplaceable neurological and spiritual value of the printed word."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Cormac McCarthy's 'Blood Meridian' Is Called the Most Terrifying American Novel",
                "tier": "Trending / High Retention",
                "angle": "viral_dark_literature",
                "slug": "blood_meridian_cormac_mccarthy_judge_holden_violence_philosophy",
                "trend_score": 98,
                "why_trending": "Massive ongoing viral obsession across BookTube and TikTok dissecting Judge Holden as the ultimate literary incarnation of evil and violence.",
                "reason": "Incredible hook exploring McCarthy's biblical, archaic prose and the horrifying historical reality of the Glanton Gang.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Dune: How Frank Herbert Predicted Ecology, Jihad, and Water Wars in 1965",
                "tier": "Trending / High Retention",
                "angle": "pop_culture_classics",
                "slug": "dune_frank_herbert_ecology_sandworms_paul_atreides_white_savior_myth",
                "trend_score": 97,
                "why_trending": "Blockbuster cinematic releases have propelled Frank Herbert's epic back to the top of worldwide bestseller charts and intellectual video essays.",
                "reason": "High-interest cultural touchpoint examining warning against charismatic leaders and ecological exploitation.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "BookTok's Dark Romance Obsession: Why Are Young Women Reading Extreme Thrillers?",
                "tier": "Trending / High Retention",
                "angle": "cultural_investigation",
                "slug": "booktok_dark_romance_phenomenon_colleen_hoover_psychological_taboo",
                "trend_score": 95,
                "why_trending": "BookTok has completely upended global publishing economics, driving billions of views and reshaping bestseller lists with dark romance and romantasy.",
                "reason": "Timely cultural critique of modern reading habits and social-algorithm-driven literary phenomena.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Mysterious Voynich Manuscript: Will AI Finally Crack the Unreadable 600-Year-Old Book?",
                "tier": "Trending / High Retention",
                "angle": "historical_enigma",
                "slug": "voynich_manuscript_ai_deciphering_unknown_language_botanical_mystery",
                "trend_score": 96,
                "why_trending": "Perennial fascination with the medieval cipher manuscript full of alien flora and bizarre astrological charts as machine learning teams attempt decryption.",
                "reason": "Irresistible historical cipher mystery blending book history, linguistics, and high-tech codebreaking.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Brandon Sanderson's Secret $40 Million Kickstarter: How Indie Authors Slay Big Publishing",
                "tier": "Trending / High Retention",
                "angle": "publishing_revolution",
                "slug": "brandon_sanderson_kickstarter_cosmere_indie_publishing_disruption",
                "trend_score": 94,
                "why_trending": "Fantasy author Brandon Sanderson broke Kickstarter records with a $41M campaign, proving modern authors can bypass legacy New York publishers entirely.",
                "reason": "Fascinating insider breakdown of creator economy economics, worldbuilding systems, and direct-to-consumer fantasy.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Haruki Murakami's Surreal Formula: Jazz, Cats, Spaghetti, and Deep Wells",
                "tier": "Trending / High Retention",
                "angle": "author_aesthetic",
                "slug": "haruki_murakami_surrealism_norwegian_wood_wind_up_bird_chronicle",
                "trend_score": 93,
                "why_trending": "Murakami remains an evergreen global icon for moody, atmospheric, magical realist fiction beloved by collegiate readers and café dwellers.",
                "reason": "Dissects the hypnotic, repetitive motifs that make Murakami's prose instantly recognizable and emotionally addictive.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Can an AI Win the Nobel Prize in Literature? Testing GPT-4 vs. Human Masters",
                "tier": "Trending / High Retention",
                "angle": "tech_vs_art",
                "slug": "can_ai_win_nobel_prize_in_literature_turing_test_for_poetry_and_prose",
                "trend_score": 96,
                "why_trending": "Heated debates among literary circles and tech conferences over whether artificial neural networks can possess genuine emotional vulnerability and poetic grief.",
                "reason": "Provocative, high-retention experiment putting AI-generated prose side-by-side with Nobel laureates for blind reader evaluations.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "079_creative_arts": {
        "id": "079",
        "slug": "creative_arts",
        "title": "Creative Arts",
        "category": "Arts_Design",
        "audience": "Visual Artists, Designers, Art Historians, Painters, Creative Directors, Museum Goers (Global)",
        "progression": [
            ("Tier 1: Visual Grammar, Color Theory & Foundational Composition (Scratch / Beginner)",
             "The color wheel (hues, values, saturation), rule of thirds, Golden Ratio (Fibonacci spiral), pencil grade values, and linear one-point/two-point perspective."),
            ("Tier 2: Art Epochs: Renaissance, Baroque Chiaroscuro & Impressionism (Intermediate)",
             "Da Vinci's sfumato, Caravaggio & Rembrandt dramatic lighting (chiaroscuro/tenebrism), Monet's plein-air light capture, and Japanese Ukiyo-e woodblock influence."),
            ("Tier 3: Modernist Revolutions: Cubism, Surrealism & Abstract Expressionism (Upper Intermediate)",
             "Picasso's multi-perspective deconstruction, Dali's subconscious dreamscapes, Pollock's action painting, Bauhaus form-follows-function manifesto, and color field theory (Rothko)."),
            ("Tier 4: Contemporary Art Markets, Installation / Conceptual Art & AI as Medium (Advanced / Expert)",
             "Marcel Duchamp's readymades, biennial curation ecosystems, monumental land art (Christo, Robert Smithson), digital generative art, and the philosophical definition of authorship.")
        ],
        "flagship": {
            "title": "The Golden Ratio in Art: Why Da Vinci, Michelangelo, and Nature Use the Sacred 1.618",
            "angle": "compositional_geometry",
            "slug": "079_creative_arts_compositional_geometry_golden_ratio_fibonacci_da_vinci"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Golden Ratio in Art: Why Da Vinci, Michelangelo, and Nature Use the Sacred 1.618",
                "tier": "Tier 1: Visual Grammar & Composition",
                "angle": "compositional_geometry",
                "slug": "golden_ratio_phi_fibonacci_spiral_in_art_da_vinci_parthenon",
                "question": "Is the 1:1.618 proportion a mystical biological preference wired into human vision, or an overhyped myth retrofitted onto ancient masterworks?",
                "key_focus": "The mathematics of Phi, the Fibonacci spiral in nautilus shells and sunflower seeds, Luca Pacioli's De Divina Proportione illustrated by Leonardo da Vinci, and practical grid construction.",
                "reason": "Flagship launch episode; bridges mathematics, biology, and fine art composition into one captivating visual investigation."
            },
            {
                "id": 2,
                "title": "Color Theory Demystified: How Hue, Saturation, and Value Control Human Emotion",
                "tier": "Tier 1: Visual Grammar & Composition",
                "angle": "color_science",
                "slug": "color_theory_hue_saturation_value_ittern_albers_emotional_palette",
                "question": "Why do complementary colors vibrate when placed side-by-side, and why did Josef Albers claim that 'color is the most relative medium in art'?",
                "key_focus": "The subtractive vs. additive color wheels, Johannes Itten's 7 color contrasts, simultaneous contrast, warm vs. cool temperature harmonies, and value keys controlling drama.",
                "reason": "The non-negotiable cornerstone of visual art, graphic design, and cinematography."
            },
            {
                "id": 3,
                "title": "Linear Perspective: How Brunelleschi Invented the Illusion of 3D Depth on Flat Canvas",
                "tier": "Tier 1: Visual Grammar & Composition",
                "angle": "historical_technique",
                "slug": "linear_perspective_filippo_brunelleschi_vanishing_point_florence_1415",
                "question": "How did a Florentine architect's mirror experiment in 1415 permanently transform medieval flat painting into mathematical, three-dimensional realism?",
                "key_focus": "The vanishing point, horizon line, orthogonal rays, one-point vs. two-point and three-point perspective, and Masaccio's Holy Trinity fresco demonstrating depth.",
                "reason": "Explains the technological breakthrough that launched the Italian High Renaissance."
            },
            {
                "id": 4,
                "title": "Value and Contrast: Why 'Value Does All the Work, But Color Gets All the Credit'",
                "tier": "Tier 1: Visual Grammar & Composition",
                "angle": "foundational_technique",
                "slug": "value_and_contrast_grayscale_thumbnailing_focal_points_clarity",
                "question": "Why does a painting with stunning colors look flat and muddy if its black-and-white tonal value structure is flawed?",
                "key_focus": "The 9-step value scale, high-key vs. low-key compositions, squinting technique for identifying local values, leading eye paths through contrast gradients.",
                "reason": "Crucial training advice for every beginner artist to escape muddy, unreadable drawings."
            },
            {
                "id": 5,
                "title": "Drawing from Life: The Battle Between What Your Eyes See and What Your Brain Assumes",
                "tier": "Tier 1: Visual Grammar & Composition",
                "angle": "cognitive_drawing",
                "slug": "drawing_from_life_betty_edwards_drawing_on_the_right_side_of_brain",
                "question": "Why do humans naturally draw childish symbol icons (circles for heads, almond eyes) instead of the actual foreshortened angles before them?",
                "key_focus": "Betty Edwards' 'Drawing on the Right Side of the Brain', negative space observation, blind contour exercises, upside-down drawing to bypass cognitive labeling.",
                "reason": "Breaks the psychological barrier preventing beginners from drawing realistic forms."
            },
            {
                "id": 6,
                "title": "Chiaroscuro and Tenebrism: How Caravaggio Weaponized Shadow and Violent Light",
                "tier": "Tier 2: Epochs: Renaissance to Impressionism",
                "angle": "baroque_mastery",
                "slug": "caravaggio_chiaroscuro_tenebrism_calling_of_st_matthew_baroque_shadow",
                "question": "How did a murderer and fugitive painter revolutionize European art by dragging dirty-footed peasants into church paintings illuminated by theatrical spotlighting?",
                "key_focus": "Tenebrism (the 'dark manner'), high-contrast directional lighting, emotional theatricality of the Counter-Reformation, and influence on Rembrandt and Gentileschi.",
                "reason": "Dives into the bad-boy genius of Baroque Rome whose lighting technique paved the way for modern Hollywood cinematography."
            },
            {
                "id": 7,
                "title": "Da Vinci's Sfumato: The Secret Smoky Glazes Behind the Mona Lisa's Uncatchable Smile",
                "tier": "Tier 2: Epochs: Renaissance to Impressionism",
                "angle": "renaissance_glazes",
                "slug": "da_vinci_sfumato_mona_lisa_micro_glazes_optical_illusion_smile",
                "question": "How did Leonardo apply 40 layers of translucent oil glazes thinner than a human red blood cell to make the Mona Lisa's expression change depending on where you look?",
                "key_focus": "Sfumato (smoke/without lines or borders), peripheral vision vs. foveal vision processing, anatomical facial dissections informing muscle movement, and aerial perspective in landscapes.",
                "reason": "Unlocks the technical and optical magic behind the most famous portrait in human history."
            },
            {
                "id": 8,
                "title": "Impressionism: When French Rebels Abandoned the Studio to Chase Fleeting Light",
                "tier": "Tier 2: Epochs: Renaissance to Impressionism",
                "angle": "rebellious_movements",
                "slug": "impressionism_monet_sunrise_plein_air_paint_tubes_salon_des_refuses",
                "question": "Why did the Parisian art establishment violently reject Monet, Renoir, and Degas in 1874, calling their paintings 'wallpaper in its embryonic state'?",
                "key_focus": "The invention of collapsible tin paint tubes allowing plein-air outdoor work, optical color mixing (broken brushstrokes), capturing transient atmospheric light, and the Salon des Refuses.",
                "reason": "The birth of modern art, chronicling the brave break from academic neoclassical orthodoxy."
            },
            {
                "id": 9,
                "title": "The Japanese Wave: How Ukiyo-e Woodblock Prints Redesigned European Art",
                "tier": "Tier 2: Epochs: Renaissance to Impressionism",
                "angle": "cross_cultural_influence",
                "slug": "japonisme_hokusai_great_wave_ukiyo_e_influence_on_van_gogh_monet",
                "question": "How did cheap Japanese wrapping paper and woodblock prints by Hokusai and Hiroshige completely rewrite Van Gogh's and Degas's understanding of space?",
                "key_focus": "Japonisme craze after Japan opened in 1853, flat color planes, radical asymmetrical cropping, bird's-eye perspective, and Van Gogh copying Hiroshige in oils.",
                "reason": "Exposes the massive Asian artistic influence that catalyzed Western Post-Impressionism."
            },
            {
                "id": 10,
                "title": "Van Gogh's Impasto: Sculpting Raw Psychological Pain Directly onto Canvas",
                "tier": "Tier 2: Epochs: Renaissance to Impressionism",
                "angle": "post_impressionism",
                "slug": "van_gogh_impasto_starry_night_emotional_color_palette_knife_energy",
                "question": "Why are Van Gogh's paint strokes so thick you can measure their height in millimeters, and how did he use swirling impasto to convey internal turbulence?",
                "key_focus": "Impasto technique using palette knife and straight-from-tube application, complementary yellow-blue color theory conveying spiritual ecstasy, Starry Night painted from the Saint-Remy asylum.",
                "reason": "Celebrates the emotional purity and physical texture of history's most beloved post-impressionist painter."
            },
            {
                "id": 11,
                "title": "Cubism: How Picasso and Braque Smashed 500 Years of Perspective to Pieces",
                "tier": "Tier 3: Modernist Revolutions",
                "angle": "avant_garde_deconstruction",
                "slug": "cubism_picasso_braque_demoiselles_davignon_multiple_viewpoints_1907",
                "question": "Why did Picasso draw a face with eyes looking forward while the nose pointed sideways, and how did African masks inspire the destruction of Renaissance space?",
                "key_focus": "Les Demoiselles d'Avignon (1907), Analytic Cubism (monochromatic geometric dissection) vs. Synthetic Cubism (collage invention), capturing four-dimensional time on 2D surfaces.",
                "reason": "The most radical visual revolution since Brunelleschi, smashing traditional representational art forever."
            },
            {
                "id": 12,
                "title": "Surrealism: Painting the Uncensored Subconscious with Salvador Dalí and René Magritte",
                "tier": "Tier 3: Modernist Revolutions",
                "angle": "subconscious_realms",
                "slug": "surrealism_salvador_dali_melting_clocks_magritte_treachery_of_images",
                "question": "How did Freud's dream interpretation theories inspire Salvador Dalí's melting clocks and René Magritte's 'This is not a pipe' philosophical painting?",
                "key_focus": "Andre Breton's Surrealist Manifesto, Dalí's paranoiac-critical method, hyper-realistic rendering of irrational nightmares, Magritte's semiotic word-image puzzles.",
                "reason": "Explores the dreamscape movement that turned psychology into indelible visual iconography."
            },
            {
                "id": 13,
                "title": "The Bauhaus: How a German School Invented the Aesthetic of Modern Cities and Chairs",
                "tier": "Tier 3: Modernist Revolutions",
                "angle": "design_philosophy",
                "slug": "bauhaus_walter_gropius_form_follows_function_kandinsky_modern_design",
                "question": "Why do your IKEA furniture, glass skyscrapers, and minimalist smartphone fonts trace directly back to Walter Gropius's school in 1919 Weimar Germany?",
                "key_focus": "'Form follows function', total work of art (Gesamtkunstwerk), merging fine art craft with industrial mass-production, Wassily Kandinsky and Paul Klee's foundational course.",
                "reason": "The design revolution that stripped away Victorian clutter to engineer the modern functional world."
            },
            {
                "id": 14,
                "title": "Abstract Expressionism and the CIA: Jackson Pollock, Rothko, and Cold War Cultural Warfare",
                "tier": "Tier 3: Modernist Revolutions",
                "angle": "geopolitical_art_history",
                "slug": "abstract_expressionism_cia_pollock_action_painting_rothko_cold_war",
                "question": "Why did Jackson Pollock fling paint onto canvases on the floor, and did the CIA secretly fund touring exhibits of American abstract art to fight Soviet realism?",
                "key_focus": "Action painting and all-over composition, Harold Rosenberg's 'arena' concept, Mark Rothko's spiritual color fields, the Congress for Cultural Freedom and Cold War soft power.",
                "reason": "Riveting blend of avant-garde artistic breakthroughs and clandestine geopolitical propaganda."
            },
            {
                "id": 15,
                "title": "Pop Art and Consumerism: Warhol, Lichtenstein, and the Factory Line of Culture",
                "tier": "Tier 3: Modernist Revolutions",
                "angle": "consumer_culture",
                "slug": "pop_art_andy_warhol_campbells_soup_marilyn_silkscreen_mass_media",
                "question": "How did Andy Warhol turn a $0.10 can of Campbell's Soup and a silkscreen print of Marilyn Monroe into the defining monuments of 20th-century culture?",
                "key_focus": "The Factory studio ethos, commodification of celebrity and death, Roy Lichtenstein's Ben-Day dots imitating comic books, erasing the divide between high art and commercial packaging.",
                "reason": "Analyzes the mirror held up to American consumer abundance, celebrity obsession, and media repetition."
            },
            {
                "id": 16,
                "title": "Duchamp's Urinal: The Moment an Idea Became More Important Than Craft",
                "tier": "Tier 4: Markets, Concepts & AI Mediums",
                "angle": "conceptual_art_origins",
                "slug": "marcel_duchamp_fountain_1917_readymade_urinal_conceptual_art",
                "question": "Why was a signed porcelain urinal (Fountain, 1917) voted the most influential artwork of the 20th century by 500 British art experts?",
                "key_focus": "The Readymade concept (R. Mutt), rejecting 'retinal art' in favor of intellectual inquiry, institutional critique (what makes a gallery space declare something art?), and the birth of Conceptualism.",
                "reason": "The philosophical turning point that decoupled manual artistic craft from conceptual artistic status."
            },
            {
                "id": 17,
                "title": "Land Art and Monumental Earthworks: Leaving the White Cube for the Open Desert",
                "tier": "Tier 4: Markets, Concepts & AI Mediums",
                "angle": "environmental_scale",
                "slug": "land_art_robert_smithson_spiral_jetty_christo_wrapped_reichstag_scale",
                "question": "Why did Robert Smithson dump 6,000 tons of black basalt into the Great Salt Lake, and why did Christo spend 24 years trying to wrap the German Reichstag in fabric?",
                "key_focus": "Spiral Jetty and entropy, Christo and Jeanne-Claude's temporary public interventions, Walter De Maria's Lightning Field, rejecting gallery commercialization through untransferable scale.",
                "reason": "Showcases art at the titanic scale of geology, meteorology, and architectural landscape."
            },
            {
                "id": 18,
                "title": "Inside the Contemporary Art Market: Art Basel, Freeports, and Tax-Shelter Masterpieces",
                "tier": "Tier 4: Markets, Concepts & AI Mediums",
                "angle": "market_economics",
                "slug": "contemporary_art_market_art_basel_geneva_freeport_blue_chip_investing",
                "question": "How do billionaire collectors use Swiss duty-free storage vaults, auction house guarantees, and mega-galleries like Gagosian to turn canvas into a financial asset class?",
                "key_focus": "Primary vs. secondary art market dynamics, auction house bidding wars (Sotheby's and Christie's), the Geneva Freeport holding billions in invisible masterpieces, and artist resale royalties.",
                "reason": "An eye-opening expose of the hyper-wealthy, unregulated global financial machinery funding contemporary fine art."
            },
            {
                "id": 19,
                "title": "The Art of Forgery: How Master Con Artists Fooled the World's Best Museums for Decades",
                "tier": "Tier 4: Markets, Concepts & AI Mediums",
                "angle": "investigative_forensics",
                "slug": "art_forgery_wolfgang_beltracchi_han_van_meegeren_vermeer_provenance",
                "question": "How did Wolfgang Beltracchi invent fake paintings by famous artists and pass scientific museum pigment tests, earning millions before a single tube of titanium white caught him?",
                "key_focus": "Han van Meegeren forging Vermeer for Hermann Göring, Beltracchi's fake vintage photographs proving provenance, pigment chemistry, radiocarbon dating, and forensic connoisseurship.",
                "reason": "Thrilling true-crime art history exploring the psychological hubris and scientific detection of forgeries."
            },
            {
                "id": 20,
                "title": "Generative AI and the Future of Creativity: Is Human Artistry Dead, or Just Reborn?",
                "tier": "Tier 4: Markets, Concepts & AI Mediums",
                "angle": "future_horizons",
                "slug": "generative_ai_art_midjourney_stable_diffusion_copyright_human_craft",
                "question": "When diffusion models can generate Rembrandt-level lighting in 4 seconds, what remains uniquely human about creativity, intention, and aesthetic soul?",
                "key_focus": "Latent space mechanics, copyright disputes over training datasets, AI as a collaborative brush vs. replacement, the revival of tactile physical mediums (oil, ceramics), and the essence of artistic vulnerability.",
                "reason": "The definitive capstone addressing the biggest crisis and renaissance in visual art since the invention of the camera."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Banksy Shredded His Own $1.4 Million Painting at Auction: The Greatest Stunt in Art History",
                "tier": "Trending / High Retention",
                "angle": "viral_art_stunt",
                "slug": "banksy_love_is_in_the_bin_shredded_sothebys_auction_prank_worth",
                "trend_score": 98,
                "why_trending": "Continuous viral fascination with Banksy's 'Girl with Balloon' self-destructing via a built-in frame shredder—and subsequently doubling in market value.",
                "reason": "Unbeatable hook blending anti-capitalist street art irony with multi-million dollar auction house drama.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "The Dark Secrets Hidden Inside the Mona Lisa: 3D Multi-Spectral Scans Reveal All",
                "tier": "Trending / High Retention",
                "angle": "forensic_discoveries",
                "slug": "mona_lisa_hidden_layers_pascal_cotte_multi_spectral_3d_scan",
                "trend_score": 97,
                "why_trending": "Pascal Cotte's high-resolution multi-spectral camera scans showing the original hidden underdrawing and eyebrow hairs erased by 500 years of varnish.",
                "reason": "Massive global recognition combined with brand-new high-tech forensic revelations.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Why Modern Art Is So 'Stupid' (And Why You're Actually Wrong About It)",
                "tier": "Trending / High Retention",
                "angle": "viral_cultural_debate",
                "slug": "why_modern_art_is_so_stupid_maurizio_cattelan_banana_duct_tape",
                "trend_score": 96,
                "why_trending": "Maurizio Cattelan taping a $120,000 banana to a wall sparked international outrage and millions of hot takes across YouTube and Reddit.",
                "reason": "High-conflict retention hook taking on common viewer cynicism with sharp, hilarious, and enlightening analysis.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Restoration Disasters: The Funniest and Most Horrifying Botched Paintings Ever",
                "tier": "Trending / High Retention",
                "angle": "humorous_history",
                "slug": "botched_art_restoration_monkey_christ_ecce_homo_borja_spain",
                "trend_score": 95,
                "why_trending": "The 'Monkey Christ' (Ecce Homo) in Spain and botched Virgin Mary restorations remain eternal internet memes generating hundreds of millions of views.",
                "reason": "Hilarious, lighthearted entertainment that seamlessly transitions into serious restoration chemistry and museum preservation.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Vantablack vs. Pinkest Pink: The Pettiest, Funniest War in Contemporary Art",
                "tier": "Trending / High Retention",
                "angle": "art_feuds",
                "slug": "vantablack_anish_kapoor_vs_stuart_semple_pinkest_pink_art_war",
                "trend_score": 96,
                "why_trending": "Anish Kapoor buying exclusive rights to the blackest black substance, and Stuart Semple retaliating by selling 'The Pinkest Pink' to anyone except Anish Kapoor.",
                "reason": "Wildly entertaining, pettiest grudge match in modern art history that teaches light absorption physics and copyright ethics.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "How Michelangelo Painted the Sistine Chapel Standing Up: The Brutal 4-Year Ordeal",
                "tier": "Trending / High Retention",
                "angle": "historical_endurance",
                "slug": "michelangelo_sistine_chapel_painted_standing_up_scaffold_fresco_fumes",
                "trend_score": 94,
                "why_trending": "Dispelling the Hollywood myth that Michelangelo lay on his back, revealing the torturous reality of wet fresco plaster dripping into his eyes for 4 years.",
                "reason": "Extreme physical grit and artistic devotion that makes viewers appreciate the monumental ceiling on a visceral human level.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why You Can't Buy Real Ultramarine: The Pigment Once Worth More Than Pure Gold",
                "tier": "Trending / High Retention",
                "angle": "material_mysteries",
                "slug": "ultramarine_blue_lapis_lazuli_afghanistan_badakhshan_pigment_history",
                "trend_score": 95,
                "why_trending": "Material science and craftsmanship videos showing hand-grinding lapis lazuli from Afghan mines to extract the heavenly blue reserved strictly for the Virgin Mary's robe.",
                "reason": "Fascinating blend of mining history, economics, and ancient pigment alchemy that viewers love watching.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "080_film_entertainment_analysis": {
        "id": "080",
        "slug": "film_entertainment_analysis",
        "title": "Film & Entertainment Analysis",
        "category": "Media_Entertainment",
        "audience": "Cinephiles, Filmmakers, Screenwriters, Video Essay Fans, Pop Culture Analysts (Global)",
        "progression": [
            ("Tier 1: Cinematic Language: Framing, Mise-en-Scène & Three-Act Structure (Scratch / Beginner)",
             "Shot composition (wide, medium, close-up, Dutch angle), Syd Field's screenplay structure, lighting keys (high-key vs low-key noir), and visual exposition without dialogue."),
            ("Tier 2: Montage Theory, Sound Design & The Invisible Art of Editing (Intermediate)",
             "Kuleshov effect, Soviet montage (Eisenstein), Walter Murch's Rule of Six, diegetic vs non-diegetic soundscapes, and leitmotifs in scoring (Ennio Morricone, John Williams)."),
            ("Tier 3: Auteur Theory, Genre Subversion & Color Psychology (Upper Intermediate)",
             "Directorial signatures (Hitchcock suspense, Kubrick symmetry, Nolan non-linear time, Tarantino non-sequential narrative), neon noir aesthetics, and genre deconstruction."),
            ("Tier 4: Industry Economics, Streaming Disruptions & The Philosophy of Cinema (Advanced / Expert)",
             "Hollywood studio system vs independent cinema, franchise IP fatigue vs algorithm-driven greenlighting, Tarkovsky's 'Sculpting in Time', and the evolution of the theatrical experience.")
        ],
        "flagship": {
            "title": "The Visual Grammar of Cinema: How Great Directors Tell Stories Without a Single Word of Dialogue",
            "angle": "visual_storytelling",
            "slug": "080_film_entertainment_analysis_visual_storytelling_framing_mise_en_scene"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Visual Grammar of Cinema: How Great Directors Tell Stories Without a Single Word of Dialogue",
                "tier": "Tier 1: Cinematic Language & Structure",
                "angle": "visual_storytelling",
                "slug": "cinematic_grammar_framing_blocking_mise_en_scene_show_dont_tell",
                "question": "How do framing, camera height, and actor blocking subconsciously tell you who has power in a scene before anyone speaks?",
                "key_focus": "Rule of thirds, low-angle vs. high-angle psychological dominance, leading lines, headroom, negative space, and Mad Max: Fury Road's crosshair center framing.",
                "reason": "Flagship launch episode; teaches viewers how to decode visual cinematic grammar like a veteran director."
            },
            {
                "id": 2,
                "title": "The Three-Act Screenplay Structure: Syd Field, Blake Snyder, and Why All Movies Hit the Midpoint at Minute 55",
                "tier": "Tier 1: Cinematic Language & Structure",
                "angle": "screenwriting_structure",
                "slug": "three_act_structure_save_the_cat_midpoint_reversal_all_is_lost_moment",
                "question": "Why does almost every Hollywood movie from Die Hard to The Lion King have a devastating 'All is Lost' crisis exactly 75% into the runtime?",
                "key_focus": "Inciting incident, Plot Point 1, Midpoint stakes raise, Dark Night of the Soul, Climax, and Blake Snyder's 15-beat 'Save the Cat' sheet.",
                "reason": "Unlocks the timing blueprint used across the global commercial film industry."
            },
            {
                "id": 3,
                "title": "Mise-en-Scène: How Every Object, Color, and Shadow in the Frame Tells a Subconscious Story",
                "tier": "Tier 1: Cinematic Language & Structure",
                "angle": "production_design",
                "slug": "mise_en_scene_production_design_costume_set_lighting_parasite",
                "question": "How did Bong Joon-ho use staircases, basement flooding, and architecture in Parasite to visually diagram class warfare without preaching?",
                "key_focus": "Definition of mise-en-scène (everything placed in the frame), set dressing, costume color progression, practical props carrying thematic weight.",
                "reason": "Deconstructs the total spatial worldbuilding that separates amateur video from cinematic art."
            },
            {
                "id": 4,
                "title": "Camera Movement Psychology: Dolly, Steadicam, Handheld, and the Legendary Tracking Shot",
                "tier": "Tier 1: Cinematic Language & Structure",
                "angle": "camera_movement",
                "slug": "camera_movement_steadicam_dolly_zoom_vertigo_goodfellas_copacabana",
                "question": "Why does a Steadicam make you feel like a ghost, handheld makes you feel panicked, and the Hitchcock Dolly Zoom warps reality?",
                "key_focus": "Vertigo effect (zolly / dolly zoom), Goodfellas Copacabana continuous long take, Children of Men car ambush handheld choreography, emotional kinematics.",
                "reason": "Essential visual masterclass on how camera movement directs the viewer's heartbeat."
            },
            {
                "id": 5,
                "title": "Lighting Keys in Cinema: Low-Key Film Noir Shadows vs. High-Key Commercial Brilliance",
                "tier": "Tier 1: Cinematic Language & Structure",
                "angle": "cinematography_lighting",
                "slug": "lighting_keys_three_point_lighting_chiaroscuro_film_noir_roger_deakins",
                "question": "How does three-point lighting (key, fill, backlight) work, and why does Roger Deakins prefer practical soft light over harsh studio lamps?",
                "key_focus": "Three-point lighting triangle, high-key lighting for comedies, low-key lighting and Venetian blind shadows in Film Noir, catchlights in the actor's eye.",
                "reason": "Teaches viewers how light sculpts face, atmosphere, and psychological genre."
            },
            {
                "id": 6,
                "title": "The Kuleshov Effect: The Soviet Experiment That Proved Editing Creates Emotion",
                "tier": "Tier 2: Montage & Invisible Editing",
                "angle": "montage_theory",
                "slug": "kuleshov_effect_soviet_montage_eisenstein_battleship_potemkin_collision",
                "question": "How did Lev Kuleshov prove in 1918 that the audience's emotion doesn't come from an actor's performance, but from the cut between two images?",
                "key_focus": "Actor looking blankly cut to soup (hunger), coffin (grief), woman (lust); Sergei Eisenstein's collision montage in Battleship Potemkin, intellectual vs. rhythmic cutting.",
                "reason": "The psychological breakthrough that established film editing as the world's only unique art form."
            },
            {
                "id": 7,
                "title": "Walter Murch's Rule of Six: The Invisible Hierarchy of the Cut",
                "tier": "Tier 2: Montage & Invisible Editing",
                "angle": "editing_mastery",
                "slug": "walter_murch_rule_of_six_in_the_blink_of_an_eye_apocalypse_now_cut",
                "question": "Why is emotion 51% of a good edit, while physical continuity is only 4%, according to the legendary editor of The Godfather and Apocalypse Now?",
                "key_focus": "Emotion (51%), Story (23%), Rhythm (10%), Eye-trace (7%), 2D screen direction (5%), 3D spatial continuity (4%); cutting on character blinks.",
                "reason": "The golden standard philosophy of film editing read by every professional filmmaker."
            },
            {
                "id": 8,
                "title": "Sound Design: The Invisible 50% of the Movie You Only Notice When It Fails",
                "tier": "Tier 2: Montage & Invisible Editing",
                "angle": "audio_engineering",
                "slug": "sound_design_foley_diegetic_vs_non_diegetic_star_wars_soundscapes",
                "question": "Why did Ben Burtt hit high-voltage radio tower guy-wires with a wrench to create the Star Wars blaster sound, and why is audio half the cinematic experience?",
                "key_focus": "Diegetic vs. non-diegetic sound, Foley art recreating everyday footsteps and clothing rustle, room tone, frequency equalization, sub-bass creating anxiety in horror.",
                "reason": "Celebrates the uncredited sonic artists who manipulate half our cinematic emotions."
            },
            {
                "id": 9,
                "title": "The Musical Leitmotif: How John Williams and Hans Zimmer Hack Your Memory",
                "tier": "Tier 2: Montage & Invisible Editing",
                "angle": "film_scoring",
                "slug": "musical_leitmotif_john_williams_jaws_two_notes_hans_zimmer_interstellar",
                "question": "How can two simple piano notes in Jaws make an audience terrified of water without ever showing a shark?",
                "key_focus": "Wagnerian leitmotif technique applied to cinema (Darth Vader's Imperial March, Indiana Jones), Hans Zimmer's minimalist Shepherd tone illusion, emotional anchoring.",
                "reason": "Analyzes how orchestral and electronic themes become permanent cultural earworms."
            },
            {
                "id": 10,
                "title": "The Long Take vs. The Hyper-Cut: From Hitchcock's Rope to the Jason Bourne Frenzy",
                "tier": "Tier 2: Montage & Invisible Editing",
                "angle": "editing_rhythm",
                "slug": "long_take_vs_hyper_cutting_alfred_hitchcock_rope_1917_bourne_identity",
                "question": "Why does an uncut 10-minute shot create unbearable claustrophobic tension, while a 150-cuts-per-minute action scene causes sensory exhaustion?",
                "key_focus": "Hidden cuts in Hitchcock's Rope and Sam Mendes' 1917, average shot length (ASL) drop from 10s in 1940 to 2.5s today, action clarity vs. chaos cinema.",
                "reason": "Examines the modern battle between sustained spatial immersion and hyperactive attention edits."
            },
            {
                "id": 11,
                "title": "Hitchcock's Bomb Under the Table: The Crucial Difference Between Surprise and Suspense",
                "tier": "Tier 3: Auteurs, Subversion & Color",
                "angle": "directorial_technique",
                "slug": "alfred_hitchcock_suspense_vs_surprise_bomb_under_table_rear_window",
                "question": "Why does surprising the audience with a sudden explosion give 15 seconds of shock, while letting them see the timer gives 15 minutes of agonizing suspense?",
                "key_focus": "Information asymmetry (audience knows more than characters), MacGuffins, voyeurism in Rear Window, Vertigo spiral obsession, and psychological mastery.",
                "reason": "The defining lesson in audience information control from the Master of Suspense."
            },
            {
                "id": 12,
                "title": "Stanley Kubrick's Symmetry and The One-Point Perspective: The Cold Architecture of Dread",
                "tier": "Tier 3: Auteurs, Subversion & Color",
                "angle": "auteur_style",
                "slug": "stanley_kubrick_one_point_perspective_symmetry_the_shining_2001",
                "question": "Why does Stanley Kubrick force the vanishing point dead-center in almost every shot of 2001: A Space Odyssey and The Shining?",
                "key_focus": "One-point perspective symmetry, the 'Kubrick Stare' tilted head glance, emotional detachment, classical music juxtaposition with extreme violence (A Clockwork Orange).",
                "reason": "Dissects the mathematical rigor and haunting perfectionism of cinema's greatest visual architect."
            },
            {
                "id": 13,
                "title": "Quentin Tarantino and Non-Linear Storytelling: Why Pulp Fiction Works Backwards",
                "tier": "Tier 3: Auteurs, Subversion & Color",
                "angle": "narrative_subversion",
                "slug": "quentin_tarantino_pulp_fiction_non_linear_narrative_dialogue_pacing",
                "question": "How did a 1994 indie film where the protagonist dies in the middle and reappears in the finale win the Palme d'Or and rewrite 90s cinema?",
                "key_focus": "Episodic anthology structure, mundane conversation about hamburgers humanizing hitmen, needle-drop soundtrack curation, pop-culture pastiche, Mexican standoffs.",
                "reason": "Analyzes the postmodern indie explosion that reshaped screenwriting and dialogue forever."
            },
            {
                "id": 14,
                "title": "Christopher Nolan and the Architecture of Time: Inception, Interstellar, and Memento",
                "tier": "Tier 3: Auteurs, Subversion & Color",
                "angle": "auteur_mechanics",
                "slug": "christopher_nolan_time_dilation_cross_cutting_inception_interstellar_tenet",
                "question": "Why is time the primary antagonist in every Christopher Nolan film, and how does he cross-cut between four timelines moving at different speeds?",
                "key_focus": "Simultaneous multi-level climax cross-cutting (Inception dream tiers, Dunkirk hour/day/week timelines), practical stunts over CGI, IMAX scale, practical ticking score motifs.",
                "reason": "Deep-dives into the modern era's most commercially successful auteur director."
            },
            {
                "id": 15,
                "title": "Color Psychology in Cinema: How The Matrix, Her, and Amélie Use Palettes to Hack Mood",
                "tier": "Tier 3: Auteurs, Subversion & Color",
                "angle": "color_grading",
                "slug": "color_grading_cinema_matrix_green_tint_her_warm_red_amélie_yellow",
                "question": "Why is every scene inside the Matrix sickly fluorescent green, while the real world is cold steel blue, and why is romance film Her bathed in red?",
                "key_focus": "Digital intermediate (DI) color grading revolution, teal-and-orange blockbuster contrast obsession, monochromatic isolation, emotional saturation cues.",
                "reason": "Illuminates how modern digital color grading manipulates mood before your brain processes the plot."
            },
            {
                "id": 16,
                "title": "The Golden Age of Television: How The Sopranos, Breaking Bad, and Mad Men Beat Hollywood",
                "tier": "Tier 4: Economics, Streaming & The Future",
                "angle": "television_renaissance",
                "slug": "golden_age_of_television_sopranos_breaking_bad_anti_hero_evolution",
                "question": "How did HBO and cable drama replace the 2-hour movie with the 60-hour novelistic character study, making audiences root for murderers and meth kingpins?",
                "key_focus": "The rise of the morally compromised anti-hero (Tony Soprano, Walter White, Don Draper), serialized plotting replacing episodic resets, cinematic production values in TV.",
                "reason": "Documents the seismic cultural shift when television surpassed feature film in narrative depth."
            },
            {
                "id": 17,
                "title": "The Death of the Mid-Budget Movie: Why Hollywood Only Makes $200M Blockbusters and $5M Horror",
                "tier": "Tier 4: Economics, Streaming & The Future",
                "angle": "industry_economics",
                "slug": "death_of_mid_budget_movie_dvd_collapse_streaming_algorithm_ip_franchise",
                "question": "Where did the $40 million comedy, courtroom drama, and adult romance go? The economic collapse of DVD secondary markets and the rise of IP blockbusters.",
                "key_focus": "The physical DVD revenue safety net, international box office and China reliance demanding dialogue-free explosions, studio risk aversion, Blumhouse micro-budget models.",
                "reason": "Essential economic autopsy explaining why movie theaters today feel monopolized by superhero sequels."
            },
            {
                "id": 18,
                "title": "Andrei Tarkovsky's 'Sculpting in Time': The Spiritual Power of Slow Cinema",
                "tier": "Tier 4: Economics, Streaming & The Future",
                "angle": "film_philosophy",
                "slug": "andrei_tarkovsky_sculpting_in_time_stalker_solaris_slow_cinema",
                "question": "Why did legendary Soviet director Tarkovsky believe that cinema's true purpose isn't telling stories or entertaining, but letting the audience experience the raw passage of time?",
                "key_focus": "Stalker's iconic railway handcar sequence, elemental water and fire imagery, resisting montage collision to preserve real-time psychological meditation, slow cinema legacy.",
                "reason": "The philosophical peak of world cinema theory, challenging viewers to experience film beyond consumerism."
            },
            {
                "id": 19,
                "title": "The Streaming Wars Hangover: Algorithms, Tax Write-Downs, and the Crisis of Content Saturation",
                "tier": "Tier 4: Economics, Streaming & The Future",
                "angle": "modern_streaming_crisis",
                "slug": "streaming_wars_netflix_algorithm_warner_bros_tax_write_offs_saturation",
                "question": "Why are multi-million dollar films being erased from existence for corporate tax write-downs, and why has streaming platform debt forced Hollywood to re-evaluate algorithms?",
                "key_focus": "Peak TV bubble burst, Warner Bros. Discovery deleting finished movies, Netflix completion-rate metrics determining cancelations, theatrical window rebounds.",
                "reason": "Provides timely, insider economic insight into the turbulent current state of Hollywood entertainment."
            },
            {
                "id": 20,
                "title": "The Future of Cinema: Virtual Production, AI Actors, and the Fight for the Big Screen",
                "tier": "Tier 4: Economics, Streaming & The Future",
                "angle": "future_horizons",
                "slug": "future_of_cinema_volume_virtual_production_ai_actors_theatrical_experience",
                "question": "Will LED Volume stages (The Mandalorian) and digital de-aging eliminate on-location shooting, and can the shared communal theatrical experience survive the living room couch?",
                "key_focus": "Unreal Engine in-camera VFX, SAG-AFTRA digital likeness rights debates, IMAX 70mm viral renaissance (Oppenheimer), and the enduring irreplaceable magic of dark rooms with strangers.",
                "reason": "The ultimate capstone celebrating the enduring, immortal human experience of communal moviegoing."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Oppenheimer in 70mm IMAX Made People Fly Across Continents: The Physics of Celluloid",
                "tier": "Trending / High Retention",
                "angle": "theatrical_phenomenon",
                "slug": "oppenheimer_70mm_imax_christopher_nolan_film_strip_physical_celluloid",
                "trend_score": 98,
                "why_trending": "Christopher Nolan's 11-mile-long, 600-pound 70mm IMAX film print drove sold-out screenings for months, triggering an analog cinema renaissance.",
                "reason": "High-retention technical breakdown of resolution, analog warmth, and why digital projectors still can't match true 15-perf 70mm.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "The Volume vs. Real Locations: Why Star Wars and Marvel Shows Look Weirdly Flat",
                "tier": "Trending / High Retention",
                "angle": "vfx_breakdown",
                "slug": "the_volume_led_screens_stagecraft_why_marvel_looks_flat_parallax",
                "trend_score": 97,
                "why_trending": "Huge cinephile debate comparing The Batman and Dune's physical location shooting against Marvel/Disney+ LED StageCraft Volume screens.",
                "reason": "Eye-opening technical critique explaining parallax, focal length mismatch, and lighting contamination in modern VFX.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Why Superhero Movies Are Crashing at the Box Office: The Anatomy of IP Fatigue",
                "tier": "Trending / High Retention",
                "angle": "box_office_analysis",
                "slug": "superhero_fatigue_box_office_crash_mcu_multiverse_homework_crisis",
                "trend_score": 96,
                "why_trending": "Consecutive box office misfires and streaming backlash have dominated industry headlines as audiences tire of interconnected homework universes.",
                "reason": "Massively popular cultural autopsy exploring narrative overload, visual exhaustion, and changing audience appetites.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "How A24 Built a Cult Studio: The Marketing Genius Behind Low-Budget Masterpieces",
                "tier": "Trending / High Retention",
                "angle": "studio_spotlight",
                "slug": "a24_cult_studio_branding_marketing_everything_everywhere_hereditary",
                "trend_score": 95,
                "why_trending": "A24's record-breaking Oscar sweeps (Everything Everywhere All at Once, The Whale) and merchandise obsession among young tastemakers.",
                "reason": "Fascinating analysis of how indie cinema turned its distributor logo into a global fashion and lifestyle badge.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Why You Can't Hear the Dialogue in Modern Movies: The Dialogue Intelligibility Crisis",
                "tier": "Trending / High Retention",
                "angle": "audio_investigation",
                "slug": "why_you_cant_hear_dialogue_in_movies_mumbling_dynamic_range_subtitles",
                "trend_score": 98,
                "why_trending": "Viral frustration across all demographics about why everyone has subtitles permanently turned on, even for native English speakers.",
                "reason": "Universally relatable hook explaining naturalistic mumbling acting, theatrical wide dynamic range, and flat-screen TV downward-firing speakers.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Horror Movie Renaissance: Why $5 Million Movies Are Making $150 Million",
                "tier": "Trending / High Retention",
                "angle": "box_office_trends",
                "slug": "horror_renaissance_blumhouse_smile_weapons_of_cinema_profit_margins",
                "trend_score": 94,
                "why_trending": "Films like Smile, Terrifier, Barbarian, and Talk to Me generating astronomical profit margins while $250M blockbusters flop.",
                "reason": "Exposes the most profitable, creatively daring genre in modern Hollywood that still reliably packs theatrical auditoriums.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "AI in Hollywood: Why Screenwriters and Actors Went on Strike to Save Human Cinema",
                "tier": "Trending / High Retention",
                "angle": "industry_conflict",
                "slug": "ai_hollywood_strikes_wga_sagaftra_digital_extras_synthetic_scripts",
                "trend_score": 96,
                "why_trending": "The historic 2023 WGA and SAG-AFTRA strikes established the first legal boundaries against AI scriptwriting and background extra facial replication.",
                "reason": "High-stakes historical investigation into the battle between labor, creative dignity, and corporate automation in entertainment.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 076-080...")
    for folder_name, meta in BATCH_076_080.items():
        process_niche(folder_name, meta)
    update_master_readme()
    print("Batch 076-080 complete!")

if __name__ == "__main__":
    main()
