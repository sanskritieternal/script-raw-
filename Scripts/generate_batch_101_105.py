"""
Batch Generator for Niches 101 to 105:
- 101_memory_learning
- 102_communication
- 103_leadership_management
- 104_corporate_workplace
- 105_consumer_psychology
"""

import sys
from pathlib import Path

# Add Scripts to sys.path
sys.path.append(str(Path(__file__).parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_101_105 = {
    "101_memory_learning": {
        "id": "101",
        "slug": "memory_learning",
        "title": "Memory & Learning",
        "category": "Mind_Wellness",
        "audience": "Students, Knowledge Workers, Lifelong Learners, Neuro-hackers, Competitive Memorizers (Global)",
        "progression": [
            ("Tier 1: Synaptic Encoding, Active Recall & Spaced Repetition (Scratch / Beginner)",
             "Ebbinghaus forgetting curve, active recall vs. passive rereading, SuperMemo/Anki spaced repetition algorithms, Leitner flashcard boxes, and dual coding theory."),
            ("Tier 2: Ancient Mnemonic Architecture & Spatial Navigation (Intermediate)",
             "The Roman Method of Loci (Memory Palaces), Major System numbers-to-consonants encoding, Dominic system, and chunking working memory limits (Miller's 7 +/- 2)."),
            ("Tier 3: Cognitive Load Theory, Interleaving & The Feynman Technique (Upper Intermediate)",
             "Sweller's Cognitive Load Theory (intrinsic, extraneous, germane), interleaving practice vs. blocked practice, Barbara Oakley's focused vs. diffuse modes, and the Feynman simplification protocol."),
            ("Tier 4: Neuroplasticity, Ultra-Learning & Lifelong Cognitive Longevity (Advanced / Expert)",
             "Long-term potentiation (LTP) synaptic strengthening, Scott Young's Ultra-Learning meta-learning maps, neurogenesis in the hippocampus (BDNF), and cognitive reserve against dementia.")
        ],
        "flagship": {
            "title": "The Method of Loci: How Ancient Greek Orators Memorized Thousands of Facts with Memory Palaces",
            "angle": "mnemonic_architecture",
            "slug": "101_memory_learning_mnemonic_architecture_method_of_loci_memory_palace"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Method of Loci: How Ancient Greek Orators Memorized Thousands of Facts with Memory Palaces",
                "tier": "Tier 1: Synaptic Encoding & Spaced Repetition",
                "angle": "mnemonic_architecture",
                "slug": "method_of_loci_memory_palace_simonides_of_ceos_spatial_navigation",
                "question": "How did poet Simonides of Ceos in 500 BCE discover that linking abstract ideas to familiar rooms in a building unlocks superhuman photographic memory?",
                "key_focus": "The collapse of the banquet hall banquet origin story, evolutionary hippocampal spatial mapping (place cells and grid cells), converting words into absurd, visceral sensory images, placing loci along a mental walking path, and how World Memory Champions memorize a deck of cards in 14 seconds.",
                "reason": "Flagship launch episode; unlocks the oldest and most powerful mnemonic technique ever developed by human civilization."
            },
            {
                "id": 2,
                "title": "The Forgetting Curve: Hermann Ebbinghaus and The Mathematical Decay of Memory",
                "tier": "Tier 1: Synaptic Encoding & Spaced Repetition",
                "angle": "cognitive_psychology",
                "slug": "ebbinghaus_forgetting_curve_1885_exponential_decay_savings_method",
                "question": "Why does the human brain discard 70% of new information within 24 hours of learning it unless interrupted by timed strategic reviews?",
                "key_focus": "Hermann Ebbinghaus's 1885 nonsense syllable experiments, the exponential decay formula R = e^(-t/S), the 'savings' score upon relearning, and how reviewing right at the point of near-forgetting flattens the decay curve permanently.",
                "reason": "The foundational experimental psychology study that proved memory decay follows strict mathematical laws."
            },
            {
                "id": 3,
                "title": "Active Recall vs. Passive Rereading: The Highlighting Illusion That Wastes 1,000 Hours",
                "tier": "Tier 1: Synaptic Encoding & Spaced Repetition",
                "angle": "learning_methodologies",
                "slug": "active_recall_vs_passive_rereading_testing_effect_karpicke_blunt_illusion_of_competence",
                "question": "Why is highlighting textbooks and rereading notes the least effective study strategy in cognitive science, creating an 'illusion of competence'?",
                "key_focus": "Dr. Jeffrey Karpicke's testing effect experiments (retrieval practice generating 50% higher long-term retention than repeated studying), neurological friction of retrieval creating stronger synaptic connections, closed-book brain dumping, and self-quizzing.",
                "reason": "Saves students and learners hundreds of wasted study hours by dismantling ineffective school study habits."
            },
            {
                "id": 4,
                "title": "Anki and Spaced Repetition: How Piotr Wozniak's SuperMemo Algorithm Hacks Time",
                "tier": "Tier 1: Synaptic Encoding & Spaced Repetition",
                "angle": "spaced_repetition_tech",
                "slug": "anki_spaced_repetition_piotr_wozniak_sm2_algorithm_optimal_intervals",
                "question": "How can a simple open-source flashcard app calculate the exact day your brain is about to forget a word and prompt you to review it in 3 seconds?",
                "key_focus": "Piotr Wozniak's 1980s paper notebooks evolving into the SM-2 algorithm, ease factors, interval modifiers, flashcard minimum information principle (atomic cards), medical students learning 30,000 facts for board exams, and Anki workflow optimization.",
                "reason": "The software tool that transformed medical and language education across the modern digital world."
            },
            {
                "id": 5,
                "title": "Dual Coding Theory: Why Combining Words and Visual Images Doubles Memory Retention",
                "tier": "Tier 1: Synaptic Encoding & Spaced Repetition",
                "angle": "cognitive_science",
                "slug": "allan_paivio_dual_coding_theory_verbal_vs_visual_channels_sketchnoting",
                "question": "Why do humans remember pictures significantly better than words, and how does encoding a concept into two separate brain channels create cognitive redundancy?",
                "key_focus": "Allan Paivio's 1971 Dual Coding Theory, the verbal linguistic channel (logogens) vs. non-verbal visual channel (imagens), the Picture Superiority Effect, diagramming concepts, and sketchnoting.",
                "reason": "Explains the cognitive science behind visual thinking, mind mapping, and explanatory diagrams."
            },
            {
                "id": 6,
                "title": "The Major System: Converting Random 100-Digit Numbers into Unforgettable Stories",
                "tier": "Tier 2: Mnemonic Architecture & Spatial Systems",
                "angle": "mnemonic_systems",
                "slug": "the_major_system_phonetic_number_memory_consonants_to_digits_peg_words",
                "question": "How can you instantly memorize a 50-digit phone number, historical dates, or the periodic table using a 400-year-old phonetic code?",
                "key_focus": "Aimé Paris and Gregor von Feinaigle's phonetic consonant mappings (0=s/z, 1=t/d, 2=n, 3=m, etc.), vowel insertion rules, turning abstract digits into vivid physical nouns, creating a 00–99 master peg list, and linking stories together.",
                "reason": "The universal number-memorization code used by memory champions, historians, and mental athletes."
            },
            {
                "id": 7,
                "title": "Chunking and Working Memory: George Miller's Magical Number 7 Plus or Minus 2",
                "tier": "Tier 2: Mnemonic Architecture & Spatial Systems",
                "angle": "working_memory",
                "slug": "george_miller_magical_number_seven_working_memory_chunking_chess_masters",
                "question": "Why can your conscious working memory only hold 4 to 7 items at once, and how do chess grandmasters bypass this limit by chunking 50,000 board patterns?",
                "key_focus": "George Miller's 1956 paper, Nelson Cowan's modern working memory capacity limit (closer to 4 chunks), phonological loop limitations, de Groot and Chase/Simon chess board reconstruction experiments, and grouping information into meaningful conceptual super-chunks.",
                "reason": "Deconstructs the severe biological bandwidth bottleneck of the human conscious mind."
            },
            {
                "id": 8,
                "title": "The Dominic System vs. PAO: Person-Action-Object Frameworks for Mental Athletes",
                "tier": "Tier 2: Mnemonic Architecture & Spatial Systems",
                "angle": "competitive_mnemonics",
                "slug": "pao_system_person_action_object_dominic_obrien_competitive_memorization",
                "question": "How does 8-time World Memory Champion Dominic O'Brien pack 6 digits into a single mental image using Person-Action-Object choreography?",
                "key_focus": "Dominic O'Brien's two-letter initials encoding, the Person-Action-Object (PAO) tripartite image structure (e.g., Albert Einstein juggling moon rocks), compressing massive data streams into single composite mental movies, and training rapid recall speed.",
                "reason": "Deep-dives into the elite sport of competitive mental athletics and high-speed data encoding."
            },
            {
                "id": 9,
                "title": "Sleep and Memory Consolidation: What the Brain Does While You Are Unconscious",
                "tier": "Tier 2: Mnemonic Architecture & Spatial Systems",
                "angle": "sleep_neurobiology",
                "slug": "sleep_memory_consolidation_slow_wave_sleep_sleep_spindles_hippocampus_cortex",
                "question": "Why is pulling an all-nighter before an exam scientific self-sabotage that erases 40% of the facts you tried to memorize?",
                "key_focus": "Dr. Matthew Walker's sleep lab research, Stage 3 Slow-Wave Deep Sleep transferring temporary memories from the hippocampus to the permanent neocortex hard drive, sleep spindles stamping synaptic connections, and REM sleep integrating disparate ideas into creative insights.",
                "reason": "Proves scientifically that sleep is not lost study time, but the physical biological process of memory creation."
            },
            {
                "id": 10,
                "title": "The Baker/baker Paradox: Why You Remember a Man Is a Baker but Forget His Name Is Mr. Baker",
                "tier": "Tier 2: Mnemonic Architecture & Spatial Systems",
                "angle": "semantic_networks",
                "slug": "baker_baker_paradox_joshua_foer_semantic_anchoring_associative_networks",
                "question": "Why is the human brain hardwired to forget proper nouns like names while effortlessly remembering professions, smells, and places?",
                "key_focus": "Gillian Cohen's 1990 experiment, semantic network theory (baker the profession connects to bread, aprons, yeast, heat, and smell; Baker the name has zero semantic anchors), Joshua Foer's 'Moonwalking with Einstein', and turning names into visual caricatures.",
                "reason": "Explains the most common, embarrassing everyday memory glitch and how to permanently cure it."
            },
            {
                "id": 11,
                "title": "Cognitive Load Theory: John Sweller and The Architecture of Effective Instructional Design",
                "tier": "Tier 3: Cognitive Load & Interleaving",
                "angle": "instructional_science",
                "slug": "cognitive_load_theory_john_sweller_intrinsic_extraneous_germane_split_attention",
                "question": "Why do confusing PowerPoint slides and cluttered textbooks overwhelm your working memory and prevent actual deep learning?",
                "key_focus": "John Sweller's three cognitive loads: Intrinsic (inherent difficulty of material), Extraneous (wasteful mental effort caused by poor teaching format), and Germane (effort devoted to schema processing); the Split-Attention Effect, and the Redundancy Effect.",
                "reason": "The foundational educational psychology theory that separates world-class teaching from confusing academic lecturing."
            },
            {
                "id": 12,
                "title": "Interleaving vs. Blocked Practice: Why Mixing Up Problems Beats Practicing One Thing for Hours",
                "tier": "Tier 3: Cognitive Load & Interleaving",
                "angle": "learning_methodologies",
                "slug": "interleaving_vs_blocked_practice_desirable_difficulties_robert_bjork_math",
                "question": "Why does practicing 20 identical math problems feel satisfying but lead to exam failure, while jumbling 5 different problem types together creates mastery?",
                "key_focus": "Robert Bjork's concept of 'Desirable Difficulties', the illusion of mastery during blocked practice, interleaving forcing the brain to practice problem identification rather than rote execution, applications in tennis, musical instruments, and medical diagnostics.",
                "reason": "Challenges the intuitive human instinct to drill one thing over and over, unlocking true problem-solving agility."
            },
            {
                "id": 13,
                "title": "The Feynman Technique: How Explaining a Concept to a Child Exposes Your Hidden Ignorance",
                "tier": "Tier 3: Cognitive Load & Interleaving",
                "angle": "mastery_frameworks",
                "slug": "the_feynman_technique_richard_feynman_explain_to_a_child_analogies_blindspots",
                "question": "How did Nobel physicist Richard Feynman master the most complex quantum electrodynamics by pretending to explain it in plain English to an 8-year-old?",
                "key_focus": "The 4-step Feynman Technique: 1) Pick a concept, 2) Explain it to a child without jargon, 3) Identify exact gaps where you resort to complex words to hide confusion, 4) Refine and build intuitive analogies; and the illusion of explanatory depth.",
                "reason": "The ultimate self-testing protocol for identifying the boundary between real understanding and memorized jargon."
            },
            {
                "id": 14,
                "title": "Focused vs. Diffuse Thinking: How Salvador Dalí and Thomas Edison Used Naps to Solve Problems",
                "tier": "Tier 3: Cognitive Load & Interleaving",
                "angle": "neuroscience_of_insight",
                "slug": "focused_vs_diffuse_mode_barbara_oakley_a_mind_for_numbers_hypnagogia",
                "question": "Why did Thomas Edison hold heavy brass ball bearings in his hands while dozing off in a chair to solve impossible engineering dead ends?",
                "key_focus": "Dr. Barbara Oakley's 'A Mind for Numbers' dual-mode framework: Focused mode (prefrontal sequential logic) vs. Diffuse mode (broad associative daydreaming across distant brain networks), hypnagogic dream states dropping balls to wake up with solutions, and breaking mental fixation.",
                "reason": "Teaches knowledge workers how to deliberately toggle between intense concentration and creative subconscious synthesis."
            },
            {
                "id": 15,
                "title": "Metacognition: Learning How to Learn and The Dunning-Kruger Calibration",
                "tier": "Tier 3: Cognitive Load & Interleaving",
                "angle": "metacognition",
                "slug": "metacognition_thinking_about_thinking_dunning_kruger_calibration_self_monitoring",
                "question": "Why are beginners supremely confident in their flawed knowledge while true experts underestimate their abilities, and how do you calibrate your metacognitive monitor?",
                "key_focus": "Metacognitive monitoring vs. metacognitive control, the Dunning-Kruger effect, calibration testing (predicting your test score before taking it), error logging, and adopting the scientific mindset toward your own cognitive blind spots.",
                "reason": "Empowers learners to objectively audit their own comprehension without self-delusion."
            },
            {
                "id": 16,
                "title": "Long-Term Potentiation (LTP): The Molecular Mechanics of Synaptic Strengthening",
                "tier": "Tier 4: Neuroplasticity & Ultra-Learning",
                "angle": "cellular_neurobiology",
                "slug": "long_term_potentiation_ltp_nmda_receptors_synaptic_plasticity_eric_kandel",
                "question": "What is physically happening at the microscopic synaptic junction between two neurons when a thought turns into a permanent lifelong memory?",
                "key_focus": "Eric Kandel's Nobel Prize-winning Aplysia sea slug research, Donald Hebb's 1949 postulate ('neurons that fire together, wire together'), glutamate neurotransmission, NMDA and AMPA receptor dynamics, calcium ion influx triggering gene transcription, and dendritic spine enlargement.",
                "reason": "The hard biological cellular mechanism proving that learning physically sculpts the brain's wiring."
            },
            {
                "id": 17,
                "title": "Scott Young's Ultra-Learning: The 9 Principles for Mastering Hard Skills at 10x Speed",
                "tier": "Tier 4: Neuroplasticity & Ultra-Learning",
                "angle": "meta_learning_systems",
                "slug": "ultralearning_scott_young_mit_challenge_metalearning_directness_drills",
                "question": "How did Scott Young complete the entire 4-year MIT Computer Science curriculum in 12 months for $2,000 without taking a single official class?",
                "key_focus": "The 9 Ultralearning principles: Metalearning (mapping the territory: concepts, facts, procedures), Directness (practicing the exact skill in its real context rather than fake apps), Drilling the bottleneck, Overlearning, and aggressively pursuing hard feedback loops.",
                "reason": "The definitive self-directed education manifesto for acquiring career-defining skills in modern automated economies."
            },
            {
                "id": 18,
                "title": "Neurogenesis and BDNF: How Aerobic Exercise Grows New Brain Cells in the Hippocampus",
                "tier": "Tier 4: Neuroplasticity & Ultra-Learning",
                "angle": "exercise_neurobiology",
                "slug": "adult_neurogenesis_bdnf_brain_derived_neurotrophic_factor_exercise_hippocampus",
                "question": "Why did old medical textbooks falsely claim adults never grow new brain cells, and how does 30 minutes of zone 2 running spray 'Miracle-Gro' on your memory centers?",
                "key_focus": "Dr. Fred Gage discovering adult mammalian neurogenesis in the subgranular zone of the dentate gyrus, Brain-Derived Neurotrophic Factor (BDNF) stimulating neuron growth, Dr. John Ratey's 'Spark' research on aerobic exercise enhancing learning, and how sedentary lifestyles starve the brain.",
                "reason": "Connects cardiovascular physical fitness directly to cognitive intelligence, memory formation, and mental acuity."
            },
            {
                "id": 19,
                "title": "Cognitive Reserve: How Lifelong Education Shields the Brain from Alzheimer's Disease",
                "tier": "Tier 4: Neuroplasticity & Ultra-Learning",
                "angle": "cognitive_aging",
                "slug": "cognitive_reserve_dr_yaakov_stern_the_nun_study_alzheimers_pathology_compensation",
                "question": "How can an 85-year-old nun solve crossword puzzles and speak three languages with zero dementia symptoms, even though post-mortem autopsy reveals her brain was full of Alzheimer's plaques?",
                "key_focus": "Dr. Yaakov Stern's Cognitive Reserve hypothesis, the famous Minnesota Nun Study (David Snowdon), neural redundancy creating alternate detours around damaged brain tissue, bilingualism delaying dementia onset by 4 to 5 years, and challenging cognitive hobbies building structural resilience.",
                "reason": "An inspiring, evidence-based exploration of how lifelong learning builds an unbreakable shield against neurological decline."
            },
            {
                "id": 20,
                "title": "The Cyborg Brain: Neural Interfaces, Memory Augmentation, and The Future of Knowledge",
                "tier": "Tier 4: Neuroplasticity & Ultra-Learning",
                "angle": "future_horizons",
                "slug": "future_of_learning_brain_computer_interfaces_neuralink_hippocampal_prosthetics",
                "question": "When neural lace interfaces and AI chips can stream Wikipedia directly into the cerebral cortex, what will be the purpose of human memory and education?",
                "key_focus": "Theodore Berger's DARPA hippocampal memory prosthetics (restoring memory in damaged brains with silicon microchips), Neuralink BCI bandwidth, the Google Effect (digital amnesia outsourcing storage vs. synthesis), and why deep human understanding, wisdom, and emotional empathy remain irreplaceable.",
                "reason": "Capstones the master curriculum by projecting humanity's ancient quest to remember into the transhuman cyborg era."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The 'Second Brain' Craze: How Tiago Forte's PARA Method Rescues You from Information Overload",
                "tier": "Trending / High Retention",
                "angle": "digital_productivity_tools",
                "slug": "building_a_second_brain_tiago_forte_para_method_notion_obsidian_notes",
                "trend_score": 98,
                "why_trending": "Massive global viral wave of productivity YouTubers and knowledge workers adopting Tiago Forte's 'Building a Second Brain' framework using Notion and Obsidian.",
                "reason": "High-utility organizational masterclass explaining Projects, Areas, Resources, and Archives (PARA) to stop hoarding useless bookmarks.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why You Can't Study with Lofi Beats and Lyrics: The Irrelevant Speech Effect",
                "tier": "Trending / High Retention",
                "angle": "study_hacks_debunk",
                "slug": "studying_with_music_irrelevant_speech_effect_phonological_loop_distraction",
                "trend_score": 97,
                "why_trending": "Millions study while listening to music, but cognitive psychologists reveal that songs with lyrics hijack your phonological loop and cut reading comprehension by 30%.",
                "reason": "Immediate high-utility study advice: why pure instrumental ambient sound or pink noise works while your favorite Spotify playlist quietly wrecks your grade.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The 20-Hour Rule: Josh Kaufman on How to Learn Anything in Just 20 Hours of Focused Effort",
                "tier": "Trending / High Retention",
                "angle": "accelerated_skill_acquisition",
                "slug": "josh_kaufman_the_first_20_hours_how_to_learn_anything_fast_tedx",
                "trend_score": 98,
                "why_trending": "Josh Kaufman's TEDx talk 'The First 20 Hours' has over 40 million views, debunking Gladwell's 10,000-hour myth and showing how 20 hours takes you from zero to competent.",
                "reason": "Enormously motivating and liberating viral framework that encourages viewers to start learning a new language or instrument today.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Why Cramming for Exams Destroys Your Long-Term Career: The Illusory Short-Term Grade",
                "tier": "Trending / High Retention",
                "angle": "student_reality_check",
                "slug": "why_cramming_fails_short_term_working_memory_erasure_professional_incompetence",
                "trend_score": 96,
                "why_trending": "Viral college retrospectives where graduates realize they passed all their chemistry or law classes with cramming, yet remember zero facts two months after graduation.",
                "reason": "Hard-hitting, relatable reality check exposing the structural flaw of exam-focused academic cramming.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "How to Memorize a Deck of Cards in Under 60 Seconds: The Secret 3-Step Competition Method",
                "tier": "Trending / High Retention",
                "angle": "spectacular_mental_stunts",
                "slug": "how_to_memorize_a_deck_of_cards_step_by_step_pao_memory_palace_tutorial",
                "trend_score": 97,
                "why_trending": "Evergreen viral party trick that dazzles audiences: combining a 52-card PAO image library with a 17-room memory palace to memorize all 52 cards in order.",
                "reason": "Fun, step-by-step practical tutorial giving viewers an immediate superpower they can practice and show off.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Why You Forget People's Names 5 Seconds After Meeting Them (And How to Fix It)",
                "tier": "Trending / High Retention",
                "angle": "everyday_social_anxiety",
                "slug": "why_we_forget_names_immediately_social_anxiety_working_memory_hack",
                "trend_score": 98,
                "why_trending": "Universal social awkwardness: introducing yourself and forgetting the other person's name while they are still finishing their sentence.",
                "reason": "Empathic, hilarious behavioral breakdown: internal social anxiety consumes 100% of working memory bandwidth so the ears never encode the sound.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "The Lion's Mane Mushroom Myth vs. Science: Can Fungus Really Boost Your Brain and Memory?",
                "tier": "Trending / High Retention",
                "angle": "nootropics_fact_check",
                "slug": "lions_mane_hericium_erinaceus_ngf_hericenones_erinacines_nootropic_truth",
                "trend_score": 96,
                "why_trending": "Explosive TikTok and biohacking interest in Lion's Mane mushroom powders, coffee supplements, and claims of stimulating Nerve Growth Factor (NGF).",
                "reason": "Objective medical reality check examining active Erinacines and Hericenones, human clinical trials, and separating real neurobiology from supplement hype.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "102_communication": {
        "id": "102",
        "slug": "communication",
        "title": "Communication",
        "category": "Home_Living",
        "audience": "Public Speakers, Negotiators, Professionals, Couples, Storytellers (Global)",
        "progression": [
            ("Tier 1: Vocal Delivery, Non-Verbal Cues & The Shannon-Weaver Model (Scratch / Beginner)",
             "The Shannon-Weaver communication loop (sender, encoder, channel, noise, decoder), vocal pitch/cadence/pauses, eye contact geometry, and open vs. closed body language."),
            ("Tier 2: Active Listening, Nonviolent Communication & De-escalation (Intermediate)",
             "Marshall Rosenberg's Nonviolent Communication (NVC: Observations, Feelings, Needs, Requests), Chris Voss's tactical empathy and mirroring, perceptual positions, and emotional validation."),
            ("Tier 3: Rhetorical Framing, Persuasion & Difficult Conversations (Upper Intermediate)",
             "Aristotle's Ethos, Pathos, and Logos triad, cognitive dissonance reduction in persuasion, framing effects, and Douglas Stone's 'Difficult Conversations' 3-conversation model."),
            ("Tier 4: High-Stakes Negotiation, Executive Presence & Cross-Cultural Fluency (Advanced / Expert)",
             "Harvard PON negotiation frameworks (BATNA, ZOPA), executive gravitas, high-context vs. low-context cultural communication (Erin Meyer's Culture Map), and crisis rhetoric.")
        ],
        "flagship": {
            "title": "Tactical Empathy: The FBI Hostage Negotiation Secret of Mirroring and Labeling",
            "angle": "negotiation_psychology",
            "slug": "102_communication_negotiation_psychology_tactical_empathy_chris_voss"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Tactical Empathy: The FBI Hostage Negotiation Secret of Mirroring and Labeling",
                "tier": "Tier 1: Vocal Delivery & Non-Verbal Fundamentals",
                "angle": "negotiation_psychology",
                "slug": "tactical_empathy_chris_voss_never_split_the_difference_mirroring_labeling",
                "question": "How did former top FBI hostage negotiator Chris Voss get bank robbers and kidnappers to surrender without weapons by repeating their last three words?",
                "key_focus": "The Late-Night FM DJ Voice (deep, calm, slow downward inflection slowing heart rates), Mirroring (repeating the last 1 to 3 critical words to trigger unconscious elaboration), Labeling negative emotions ('It seems like you feel unappreciated'), calibrated open-ended 'How' and 'What' questions, and getting to 'That's right' instead of 'Yes'.",
                "reason": "Flagship launch episode; the definitive modern framework for psychological influence, conflict resolution, and high-stakes negotiation."
            },
            {
                "id": 2,
                "title": "The Shannon-Weaver Model: Why What You Said Is Never What They Heard",
                "tier": "Tier 1: Vocal Delivery & Non-Verbal Fundamentals",
                "angle": "communication_theory",
                "slug": "shannon_weaver_communication_model_1948_noise_encoding_decoding_feedback_loops",
                "question": "How does a mathematical 1948 Bell Labs telecommunications engineering model explain why marital arguments and corporate emails fail completely?",
                "key_focus": "Sender, Encoder, Channel, Noise (physical noise, psychological bias, semantic jargon), Decoder, Receiver, and the crucial feedback loop; how subjective internal emotional dictionaries distort identical words, and the power of closed-loop verification ('What did you take away from what I just said?').",
                "reason": "The foundational communication model that reveals why human misunderstanding is the default state."
            },
            {
                "id": 3,
                "title": "Vocal Dynamics: Pitch, Pace, Pauses, and The Power of the Downward Inflection",
                "tier": "Tier 1: Vocal Delivery & Non-Verbal Fundamentals",
                "angle": "vocal_mechanics",
                "slug": "vocal_delivery_upward_inflection_uptalk_downward_inflection_strategic_silence",
                "question": "Why does ending your sentences with an upward question tone ('uptalk') destroy your perceived authority, and why is an uncomfortable 4-second silence your most powerful weapon?",
                "key_focus": "Upward vs. downward tonal inflections, vocal fry acoustics, diaphragmatic chest resonance vs. nasal throat pitch, pacing (slowing down from 160 WPM to 120 WPM for gravitas), and using strategic silence to force counterparts to speak and concede information.",
                "reason": "The physical voice training tutorial that transforms weak, hesitant speaking into magnetic, commanding delivery."
            },
            {
                "id": 4,
                "title": "Non-Verbal Geometry: Eye Contact Triangles, Torso Alignment, and The Power of Open Palms",
                "tier": "Tier 1: Vocal Delivery & Non-Verbal Fundamentals",
                "angle": "body_language_science",
                "slug": "nonverbal_communication_eye_contact_triangle_open_palms_ventral_denial",
                "question": "Did you know crossing your arms doesn't always mean defensiveness? The real evolutionary science of non-verbal cues.",
                "key_focus": "Albert Mehrabian's 7-38-55 rule context and limitations, ventral fronting (pointing torso and feet toward interest vs. ventral denial turning away), the eye-contact triangle (gazing between eyes and forehead for authority vs. mouth for social warmth), and showing open empty palms as evolutionary trust cues signaling no concealed weapons.",
                "reason": "Dismantles shallow pop-psychology body language myths with rigorous FBI and behavioral science observation."
            },
            {
                "id": 5,
                "title": "The Art of the Storytelling Hook: How to Grab Attention in the First 7 Seconds",
                "tier": "Tier 1: Vocal Delivery & Non-Verbal Fundamentals",
                "angle": "narrative_craft",
                "slug": "storytelling_hooks_in_media_res_curiosity_gap_george_loewenstein_public_speaking",
                "question": "Why do terrible public speakers start with 'Good morning, thank you for having me', while world-class speakers drop you straight into an exploding car in the opening sentence?",
                "key_focus": "Starting In Media Res (in the middle of things), George Loewenstein's Information Gap Theory (creating a painful itch of curiosity that can only be scratched by listening), stakes establishment in the first sentence, and avoiding boring throat-clearing pleasantries.",
                "reason": "Essential narrative opening craft for keynote speakers, YouTubers, and corporate presenters."
            },
            {
                "id": 6,
                "title": "Marshall Rosenberg's Nonviolent Communication (NVC): Observations, Feelings, Needs, and Requests",
                "tier": "Tier 2: Active Listening, NVC & De-escalation",
                "angle": "conflict_resolution",
                "slug": "nonviolent_communication_nvc_marshall_rosenberg_observations_feelings_needs_requests",
                "question": "How did a clinical psychologist de-escalate violent ethnic conflicts in Rwanda using a 4-sentence formula that eliminates blame and judgment?",
                "key_focus": "The 4-step NVC process: 1) Concrete Observation without judgment ('When I see...'), 2) Identifying pure Feelings without blame ('I feel anxious...'), 3) Unearthing universal unmet Needs ('Because I need safety...'), 4) Concrete, actionable Requests ('Would you be willing to...?'); and distinguishing requests from demands.",
                "reason": "The gold-standard compassionate communication framework studied by therapists, diplomats, and couples worldwide."
            },
            {
                "id": 7,
                "title": "Active Listening: Paraphrasing, Validating, and The Trap of Immediate Problem Solving",
                "tier": "Tier 2: Active Listening, NVC & De-escalation",
                "angle": "relational_communication",
                "slug": "active_listening_reflective_listening_emotional_validation_dont_fix_it_it_is_not_about_the_nail",
                "question": "Why does immediately jumping to solve your partner's problem make them feel furious and emotionally abandoned? The 'It's Not About the Nail' phenomenon.",
                "key_focus": "The critical distinction between cognitive problem-solving and emotional co-regulation, Carl Rogers' reflective listening, paraphrasing core emotional content without parroting words, validating subjective feelings without agreeing with factual claims, and asking: 'Do you want comfort or solutions right now?'",
                "reason": "Saves countless relationships and workplace partnerships from the toxic trap of premature solutioneering."
            },
            {
                "id": 8,
                "title": "De-escalating Hostility: The Verbal Judo Method for Calming Screaming Aggressors",
                "tier": "Tier 2: Active Listening, NVC & De-escalation",
                "angle": "tactical_de_escalation",
                "slug": "verbal_judo_dr_george_thompson_gentle_art_of_persuasion_calming_angry_people",
                "question": "How did an English professor who became an undercover street cop develop the verbal martial art that police use to calm aggressive, irrational suspects?",
                "key_focus": "Dr. George Thompson's Verbal Judo, the Five Universal Truths of Human Interaction, redirecting hostile kinetic energy rather than meeting it with defensive counter-attacks, strip phrases ('I hear what you're saying, sir, but...'), and allowing the angry party to save face and keep their dignity.",
                "reason": "An invaluable tactical de-escalation manual for customer service, police, healthcare workers, and managers."
            },
            {
                "id": 9,
                "title": "The Art of the Apology: Why 'I'm Sorry You Feel That Way' Is a Toxic Non-Apology",
                "tier": "Tier 2: Active Listening, NVC & De-escalation",
                "angle": "relational_repairs",
                "slug": "anatomy_of_a_real_apology_harriet_lerner_non_apology_restitution_taking_ownership",
                "question": "Why does saying 'I'm sorry if I offended you' make people angrier, and what are the five mandatory components of a genuine, healing apology?",
                "key_focus": "Harriet Lerner's 'Why Won't You Apologize?', dismantling defensive qualifiers ('I'm sorry, BUT...'), owning full unreserved responsibility for impact regardless of intent, acknowledging specific emotional pain caused, offering concrete restitution, and committing to behavioral changes.",
                "reason": "A masterclass in relational repair that heals fractured personal trust and institutional public scandals."
            },
            {
                "id": 10,
                "title": "Giving Feedback Without Crushing Souls: Radical Candor vs. Ruinous Empathy",
                "tier": "Tier 2: Active Listening, NVC & De-escalation",
                "angle": "constructive_feedback",
                "slug": "radical_candor_kim_scott_care_personally_challenge_directly_ruinous_empathy",
                "question": "Why does holding back constructive criticism to 'spare someone's feelings' actually destroy their career? The 2x2 matrix of Radical Candor.",
                "key_focus": "Kim Scott's Radical Candor framework: Caring Personally while Challenging Directly, the trap of Ruinous Empathy (being so nice you let people fail), Obnoxious Aggression (brutal jerks), Manipulative Insincerity (passive-aggressive backstabbing), and delivering real-time private micro-feedback.",
                "reason": "The essential communication playbook for managers, mentors, and collaborative creative teams."
            },
            {
                "id": 11,
                "title": "Aristotle's Rhetoric: Ethos, Pathos, and Logos in Modern Speeches and Pitches",
                "tier": "Tier 3: Rhetorical Framing & Difficult Talks",
                "angle": "classical_rhetoric",
                "slug": "aristotles_rhetoric_ethos_credibility_pathos_emotion_logos_logic_steve_jobs_pitches",
                "question": "Why did Steve Jobs' 2007 iPhone keynote entrance captivate the world? The 2,400-year-old Athenian rhetoric formula.",
                "key_focus": "Ethos (establishing moral character, competence, and authority), Pathos (awakening emotional resonance, empathy, and urgency in the listener), Logos (logical proof, data, and structured syllogisms), and why pure logic without emotional framing persuades almost nobody.",
                "reason": "The foundational masterclass in persuasive public rhetoric that has powered every great speech in human history."
            },
            {
                "id": 12,
                "title": "Framing Effects: Amos Tversky, Daniel Kahneman, and How Words Change Reality",
                "tier": "Tier 3: Rhetorical Framing & Difficult Talks",
                "angle": "cognitive_framing",
                "slug": "framing_effects_tversky_kahneman_asian_disease_problem_loss_vs_gain_framing",
                "question": "Why will 80% of patients agree to a surgery with a '90% survival rate' while 60% reject the identical surgery framed as a '10% mortality rate'?",
                "key_focus": "Kahneman and Tversky's Asian Disease Problem experiment, loss framing (people take extreme risks to avoid losses) vs. gain framing (people are risk-averse with gains), positive priming, semantic reframing of conflicts, and political messaging linguistic architecture.",
                "reason": "Reveals how the linguistic frame through which an option is presented mathematically dictates human choice."
            },
            {
                "id": 13,
                "title": "Difficult Conversations: Douglas Stone's Three-Layer Framework for High-Stakes Talks",
                "tier": "Tier 3: Rhetorical Framing & Difficult Talks",
                "angle": "crucial_conversations",
                "slug": "difficult_conversations_harvard_negotiation_project_what_happened_feelings_identity",
                "question": "Why do conversations about firing employees, confronting infidelity, or discussing money explode into screaming matches?",
                "key_focus": "The Harvard Negotiation Project framework: 1) The 'What Happened?' Conversation (shifting from certainty about facts to curiosity about perceptions, moving from blame to contribution), 2) The Feelings Conversation, 3) The Identity Conversation ('Am I competent? Am I a good person?'); and moving to learning conversations.",
                "reason": "The supreme psychological manual for navigating the most terrifying and important conversations of your life."
            },
            {
                "id": 14,
                "title": "The Socratic Method: Asking Questions That Guide People to Change Their Own Minds",
                "tier": "Tier 3: Rhetorical Framing & Difficult Talks",
                "angle": "socratic_inquiry",
                "slug": "socratic_method_epistemic_inquiry_street_epistemology_dismantling_dogma",
                "question": "Why does telling someone they are wrong trigger defensiveness and entrenchment, while asking 3 gentle questions makes them dismantle their own beliefs?",
                "key_focus": "Socrates' elenchus inquiry, Street Epistemology methodology (asking how someone arrived at their confidence percentage rather than debating facts), cognitive dissonance induction without hostility, and leading people to their own self-generated insights.",
                "reason": "The ultimate respectful intellectual tool for changing minds in an era of hyper-polarized dogma."
            },
            {
                "id": 15,
                "title": "Humor as Communication: Timing, The Incongruity-Resolution Theory, and Disarming Tension",
                "tier": "Tier 3: Rhetorical Framing & Difficult Talks",
                "angle": "humor_mechanics",
                "slug": "psychology_of_humor_incongruity_resolution_benign_violation_timing_comedy",
                "question": "What is the neurological mechanism that makes human beings laugh, and how can self-deprecating humor instantly disarm a hostile boardroom?",
                "key_focus": "Incongruity-Resolution theory (the brain anticipating one pattern and resolving a sudden absurd second pattern), the Benign Violation Theory (Peter McGraw: something is threatening but simultaneously safe), punchline timing beats, status-lowering self-deprecation, and avoiding punch-down humor.",
                "reason": "Deconstructs the cognitive mechanics of laughter as the supreme social bonding and tension-release tool."
            },
            {
                "id": 16,
                "title": "Harvard PON Negotiation: BATNA, ZOPA, and Getting to Yes",
                "tier": "Tier 4: High-Stakes Negotiation & Global Fluency",
                "angle": "principled_negotiation",
                "slug": "getting_to_yes_harvard_program_on_negotiation_batna_zopa_principled_negotiation",
                "question": "How did Roger Fisher and William Ury reinvent modern dealmaking by separating people from the problem and focusing on underlying interests rather than rigid positions?",
                "key_focus": "Best Alternative to a Negotiated Agreement (BATNA: your true walk-away leverage), Zone of Possible Agreement (ZOPA), separating positions ('I want $100k') from underlying interests ('I need security and respect'), inventing options for mutual gain, and objective criteria benchmarks.",
                "reason": "The defining classic text of international corporate, diplomatic, and labor negotiation strategy."
            },
            {
                "id": 17,
                "title": "Executive Presence: Gravitas, Strategic Brevity, and The Bottom-Line-Up-Front (BLUF) Rule",
                "tier": "Tier 4: High-Stakes Negotiation & Global Fluency",
                "angle": "executive_presence",
                "slug": "executive_presence_bluf_bottom_line_up_front_military_briefing_gravitas",
                "question": "Why do CEOs tune out long PowerPoint presentations after 30 seconds, and how do top executives communicate using the military's BLUF framework?",
                "key_focus": "The Bottom-Line-Up-Front (BLUF) communication structure: stating the recommendation and conclusion in the first 10 seconds followed by supporting bullet points, eliminating verbal filler words ('um', 'like', 'sort of'), physical stillness, and gravitas under aggressive cross-examination.",
                "reason": "The high-level corporate playbook for communicating like a C-suite executive and board member."
            },
            {
                "id": 18,
                "title": "The Culture Map: Erin Meyer on High-Context vs. Low-Context Global Communication",
                "tier": "Tier 4: High-Stakes Negotiation & Global Fluency",
                "angle": "cross_cultural_communication",
                "slug": "the_culture_map_erin_meyer_high_vs_low_context_direct_negative_feedback",
                "question": "Why does a direct Dutch critique feel like a violent personal attack to a Japanese executive, while American pleasantries sound two-faced to a German engineer?",
                "key_focus": "Erin Meyer's 8 cultural communication scales: High-Context (reading between the lines: Japan, Arab world) vs. Low-Context (explicit, literal precision: US, Germany), Direct vs. Indirect negative feedback (the French paradox), egalitarian vs. hierarchical decision-making, and navigating multicultural teams.",
                "reason": "The indispensable modern guide to thriving in global multinational corporations and cross-border diplomacy."
            },
            {
                "id": 19,
                "title": "Crisis Rhetoric: How Leaders Command Calm in Times of War and Disaster",
                "tier": "Tier 4: High-Stakes Negotiation & Global Fluency",
                "angle": "crisis_leadership_speech",
                "slug": "crisis_rhetoric_winston_churchill_1940_fdr_fireside_chats_stockdale_paradox",
                "question": "How did Winston Churchill rally a defeated Britain in 1940 using archaic Anglo-Saxon monosyllables, and what is the Stockdale Paradox of crisis leadership?",
                "key_focus": "The Stockdale Paradox (retaining unwavering faith that you will prevail in the end, while simultaneously confronting the most brutal facts of current reality), using short, visceral Anglo-Saxon words ('blood, toil, tears, and sweat'), FDR's Fireside Chats psychological radio intimacy, and taking radical public ownership during corporate scandals.",
                "reason": "Dissects the profound linguistic and psychological architecture of historic wartime and crisis leadership speeches."
            },
            {
                "id": 20,
                "title": "The Future of Communication: AI Telepathy, Spatial Avatars, and The Survival of Genuine Presence",
                "tier": "Tier 4: High-Stakes Negotiation & Global Fluency",
                "angle": "future_horizons",
                "slug": "future_of_communication_ai_avatars_spatial_presence_loss_of_spontaneous_spark",
                "question": "When Large Language Models write our emails, real-time voice translation eliminates foreign languages, and photorealistic avatars replace Zoom calls, what remains uniquely human about communication?",
                "key_focus": "Algorithmic email flattening and homogenization, the loss of spontaneous interpersonal friction, the neurochemistry of shared physical co-presence (oxytocin release and pupil dilation in face-to-face contact), and why raw, vulnerable, unscripted human imperfection becomes the ultimate luxury signal.",
                "reason": "Capstones the master curriculum by reaffirming that genuine human vulnerability and presence remain the ultimate communicative superpower."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Never Split the Difference: Chris Voss's Top 5 Negotiation Hacks That Save You Thousands",
                "tier": "Trending / High Retention",
                "angle": "practical_money_hacks",
                "slug": "never_split_the_difference_car_buying_negotiation_ackerman_model_chris_voss",
                "trend_score": 98,
                "why_trending": "Chris Voss's book and masterclasses continue to dominate bestseller charts and TikTok clips as young buyers use his exact scripts to negotiate thousands off used cars and apartment rent.",
                "reason": "High-utility practical financial application of hostage negotiation scripts with immediate measurable dollar returns.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why You Should Stop Saying 'Sorry' and Say 'Thank You' Instead: The Subconscious Status Shift",
                "tier": "Trending / High Retention",
                "angle": "micro_behavioral_shifts",
                "slug": "stop_saying_sorry_say_thank_you_status_reframing_psychology",
                "trend_score": 97,
                "why_trending": "Massive viral workplace trend replacing reflexive apologies ('Sorry I'm late') with empowering gratitude ('Thank you for your patience'), eliminating subconscious guilt signaling.",
                "reason": "A 10-second behavioral tweak that immediately elevates personal authority, warmth, and professional presence.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "How to Win Any Argument by Asking One Question: The 'How Would You Implement That?' Trap",
                "tier": "Trending / High Retention",
                "angle": "argument_hacks",
                "slug": "illusion_of_explanatory_depth_how_question_dismantling_political_extremism",
                "trend_score": 98,
                "why_trending": "Cognitive science research proving that asking people to explain the step-by-step mechanical implementation of their extreme political views instantly pops their illusion of knowledge.",
                "reason": "The ultimate polite intellectual superpower for disarming stubborn relatives and aggressive debaters.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Dark Psychology of Gaslighting: 5 Specific Phrases Manipulators Use to Make You Doubt Reality",
                "tier": "Trending / High Retention",
                "angle": "toxic_behavior_identification",
                "slug": "gaslighting_tactics_manipulation_phrases_you_are_crazy_it_never_happened",
                "trend_score": 98,
                "why_trending": "Enormous search volume and viral engagement around identifying psychological manipulation in relationships, narcissistic abuse, and restoring personal reality testing.",
                "reason": "Empathetic, highly protective psychological content that equips viewers to spot and disarm covert emotional manipulation.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Public Speaking Panic: The 90-Second Physiological Reset for Dry Mouth and Shaking Hands",
                "tier": "Trending / High Retention",
                "angle": "stage_fright_cures",
                "slug": "stage_fright_adrenaline_surge_physiological_sigh_beta_blockers_grounding",
                "trend_score": 96,
                "why_trending": "Glossophobia (fear of public speaking) affects 75% of humans; viral interest in Stanford neurobiology physiological sighs and vagus nerve resets right before walking on stage.",
                "reason": "Immediate biological relief for the universal physical nightmare of panic surges, shaking hands, and throat constrictions.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Why Charismatic People Never Get Interrupted: The Conversational Gravity Secret",
                "tier": "Trending / High Retention",
                "angle": "social_charisma",
                "slug": "conversational_gravity_why_charismatic_people_dont_get_interrupted_cadence",
                "trend_score": 97,
                "why_trending": "Viral charisma breakdowns of Barack Obama, Oprah Winfrey, and Keanu Reeves showing how they maintain floor control through steady breathing, unhurried pauses, and eye stillness.",
                "reason": "Deconstructs subtle social mechanics that stop loud conversational bullies from talking over you.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "The 'That's Right' Trap: Why Getting Someone to Say 'Yes' Is Completely Useless",
                "tier": "Trending / High Retention",
                "angle": "persuasion_secrets",
                "slug": "counterfeit_yes_confirmation_bias_chris_voss_thats_right_breakthrough",
                "trend_score": 96,
                "why_trending": "FBI negotiation insight explaining the 'Counterfeit Yes' (people saying yes just to make you shut up and leave) vs. the profound psychological commitment of 'That's Right'.",
                "reason": "Saves salespeople, parents, and negotiators from the hollow illusion of artificial agreement.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "103_leadership_management": {
        "id": "103",
        "slug": "leadership_management",
        "title": "Leadership & Management",
        "category": "Careers_Workplace",
        "audience": "Executives, Team Leads, Founders, MBA Students, Project Managers (Global)",
        "progression": [
            ("Tier 1: Leadership Models, 1-on-1s & Delegation Frameworks (Scratch / Beginner)",
             "Situational Leadership (Hersey-Blanchard), effective 1-on-1 meeting agendas (listening vs. status updates), Andy Grove's High Output Management, and task-relevant maturity delegation."),
            ("Tier 2: Psychological Safety, Team Dynamics & Radical Candor (Intermediate)",
             "Amy Edmondson's Psychological Safety research (Google's Project Aristotle), Kim Scott's Radical Candor (Caring Personally while Challenging Directly), and Tuckman's stages (Forming, Storming, Norming, Performing)."),
            ("Tier 3: OKRs, Strategy Execution & High-Stakes Decision Making (Upper Intermediate)",
             "John Doerr's Objectives and Key Results (OKRs), Jeff Bezos's Type 1 vs. Type 2 reversible decisions, Porter's Five Forces, and avoiding the HIPPO (Highest Paid Person's Opinion) trap."),
            ("Tier 4: Organizational Scaling, Culture Architecture & Crisis Turnarounds (Advanced / Expert)",
             "Peter Drucker's 'Culture eats strategy for breakfast', Ben Horowitz's Peacetime vs. Wartime CEO doctrine, managing organizational debt, and leading systemic corporate transformations.")
        ],
        "flagship": {
            "title": "Psychological Safety: What Google's Project Aristotle Discovered About the World's Best Teams",
            "angle": "team_dynamics",
            "slug": "103_leadership_management_team_dynamics_psychological_safety_project_aristotle"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Psychological Safety: What Google's Project Aristotle Discovered About the World's Best Teams",
                "tier": "Tier 1: Leadership Models & Delegation Frameworks",
                "angle": "team_dynamics",
                "slug": "google_project_aristotle_amy_edmondson_psychological_safety_high_performing_teams",
                "question": "Why did Google spend millions studying 180 teams only to find that team member intelligence, experience, and personalities mattered far less than psychological safety?",
                "key_focus": "Google's multi-year Project Aristotle, Dr. Amy Edmondson's Harvard research defining psychological safety (the shared belief that team members will not be humiliated or punished for speaking up with ideas, questions, or mistakes), conversational turn-taking equality, and average social sensitivity scores.",
                "reason": "Flagship launch episode; the definitive empirical study that revolutionized modern management and team performance."
            },
            {
                "id": 2,
                "title": "Situational Leadership: Directing, Coaching, Supporting, and Delegating",
                "tier": "Tier 1: Leadership Models & Delegation Frameworks",
                "angle": "leadership_models",
                "slug": "situational_leadership_hersey_blanchard_directing_coaching_supporting_delegating",
                "question": "Why does micromanaging an expert cause them to quit, while hands-off delegating to an enthusiastic beginner leads to disaster? The Hersey-Blanchard model.",
                "key_focus": "Paul Hersey and Ken Blanchard's Situational Leadership matrix matching leader behavior (directive vs. supportive) to follower development levels (D1 Enthusiastic Beginner to D4 Self-Reliant Achiever), avoiding the one-size-fits-all management trap, and diagnosing competence vs. commitment.",
                "reason": "The foundational leadership framework taught in executive MBA programs worldwide."
            },
            {
                "id": 3,
                "title": "The Art of the 1-on-1 Meeting: Andy Grove's High Output Management Blueprint",
                "tier": "Tier 1: Leadership Models & Delegation Frameworks",
                "angle": "management_operations",
                "slug": "andy_grove_high_output_management_one_on_one_meeting_agenda_leverage",
                "question": "Why did legendary Intel CEO Andy Grove say that spending 90 minutes in a 1-on-1 with an employee can enhance their output for 2 weeks (200 hours of leverage)?",
                "key_focus": "The 1-on-1 as the employee's meeting (not the manager's status update), psychological listening, asking five 'Whys', uncovering subterranean organizational problems, discussing career progression and emotional energy, and maintaining an un-cancelable sacred cadence.",
                "reason": "The single highest-leverage management habit that separates elite managers from amateur bosses."
            },
            {
                "id": 4,
                "title": "Task-Relevant Maturity (TRM): How to Delegate Without Abdicating",
                "tier": "Tier 1: Leadership Models & Delegation Frameworks",
                "angle": "delegation_frameworks",
                "slug": "task_relevant_maturity_trm_delegation_vs_abdication_monitoring_methods",
                "question": "How do you delegate critical multi-million-dollar tasks to team members without either breathing down their necks or completely abandoning them to drown?",
                "key_focus": "Defining Task-Relevant Maturity (a senior VP can have low TRM for a brand-new task), matching monitoring frequency to TRM, sampling output randomly without creating distrust, clear handoff contracts, and avoiding the disaster of executive abdication.",
                "reason": "Solves the eternal managerial dilemma: how to scale output without losing quality control."
            },
            {
                "id": 5,
                "title": "The Peter Principle: Why Companies Keep Promoting Incompetent People to Management",
                "tier": "Tier 1: Leadership Models & Delegation Frameworks",
                "angle": "organizational_behavior",
                "slug": "peter_principle_dr_laurence_peter_promoted_to_level_of_incompetence_dual_track",
                "question": "Why are the best software engineers and star salespeople so often promoted into terrible, miserable managers who destroy team morale?",
                "key_focus": "Dr. Laurence J. Peter's 1969 principle ('in a hierarchy, every employee tends to rise to their level of incompetence'), the fallacy that technical individual contributor skills translate to people management, and modern dual-track career ladders (Staff/Principal Engineer tracks parallel to VP tracks).",
                "reason": "Explains the universal corporate phenomenon of managerial incompetence and the structural cures for it."
            },
            {
                "id": 6,
                "title": "Tuckman's Stages of Team Development: Forming, Storming, Norming, and Performing",
                "tier": "Tier 2: Psychological Safety & Team Dynamics",
                "angle": "team_evolution",
                "slug": "tuckman_stages_forming_storming_norming_performing_team_lifecycles",
                "question": "Why is the painful 'Storming' phase of interpersonal conflict a non-negotiable biological necessity before any team can achieve elite performance?",
                "key_focus": "Bruce Tuckman's 1965 group development model: Forming (polite artificial harmony), Storming (inevitable conflict over leadership, boundaries, and priorities), Norming (establishing shared rules and mutual trust), and Performing (autonomous high-speed execution); and how managers guide teams through the fire.",
                "reason": "Reassures leaders that team conflict is not a sign of failure, but a required developmental milestone."
            },
            {
                "id": 7,
                "title": "Radical Candor in Leadership: How to Praise and Criticize with Love and Ferocity",
                "tier": "Tier 2: Psychological Safety & Team Dynamics",
                "angle": "leadership_feedback",
                "slug": "radical_candor_leadership_praise_in_public_criticize_in_private_specificity",
                "question": "Why is vague praise ('Great job!') useless, and how do top leaders deliver sharp, immediate negative criticism that makes employees respect and thank them?",
                "key_focus": "Praise in public and criticize in private, delivering feedback within 24 hours (not saving it for annual reviews), Context-Observation-Impact feedback models, separating identity from performance, and encouraging teams to criticize the leader upward.",
                "reason": "A high-utility feedback manual that creates high-trust, low-drama high-performance corporate cultures."
            },
            {
                "id": 8,
                "title": "Servant Leadership: Robert Greenleaf and The Leader Who Sweeps the Floor",
                "tier": "Tier 2: Psychological Safety & Team Dynamics",
                "angle": "leadership_philosophies",
                "slug": "servant_leadership_robert_greenleaf_inverted_pyramid_removing_blockers",
                "question": "Why did AT&T executive Robert Greenleaf flip the corporate org chart upside down, putting the CEO at the very bottom serving the frontline workers?",
                "key_focus": "The 1970 essay 'The Servant as Leader', moving from command-and-control authoritarianism to servant stewardship, the manager's primary job as clearing roadblocks and securing resources for the team, and Simon Sinek's 'Leaders Eat Last' neurobiology of trust.",
                "reason": "The moral and operational counterweight to toxic command-and-control corporate cultures."
            },
            {
                "id": 9,
                "title": "Managing the Brilliant Jerk: The High-Performing Toxic Employee Dilemma",
                "tier": "Tier 2: Psychological Safety & Team Dynamics",
                "angle": "team_culture_protection",
                "slug": "managing_brilliant_jerks_toxic_high_performers_netflix_culture_memo_firing",
                "question": "If your top engineer writes 50% of the code but bullies colleagues and terrorizes junior staff, why must you fire them immediately to save the company?",
                "key_focus": "Reed Hastings' famous Netflix Culture memo ('Do not tolerate brilliant jerks; the cost to effective teamwork is too high'), measuring negative externalities on overall team retention, toxic culture erosion, and how firing a high-performing bully invariably increases overall team output.",
                "reason": "Tackles the hardest, most agonizing personnel decision every executive and startup founder eventually faces."
            },
            {
                "id": 10,
                "title": "Meeting Bankruptcy: How Shopify, Asana, and Amazon Eliminated Meeting Bloat",
                "tier": "Tier 2: Psychological Safety & Team Dynamics",
                "angle": "organizational_efficiency",
                "slug": "meeting_bankruptcy_shopify_calendar_purge_as_no_meeting_wednesdays_silent_reading",
                "question": "How did Shopify delete 12,000 recurring meetings in a single day, and why does Amazon start every executive meeting with 30 minutes of total silence?",
                "key_focus": "The economic cost of meetings (8 people in a 1-hour meeting = 8 person-hours of engineering time), Amazon's 6-page narrative memo read in silence before discussion, No-Meeting Wednesdays, asynchronous written updates, and calculating meeting financial cost in real-time.",
                "reason": "The urgent corporate antidote to the calendar bloat and context-switching that paralyzes modern knowledge workers."
            },
            {
                "id": 11,
                "title": "OKRs: John Doerr, Andy Grove, and How Google Scaled from 40 to 100,000 People",
                "tier": "Tier 3: OKRs, Strategy & Decision Making",
                "angle": "goal_setting_systems",
                "slug": "okrs_objectives_and_key_results_john_doerr_measure_what_matters_google_scaling",
                "question": "How did a venture capitalist give Larry Page and Sergey Brin a simple goal-setting framework in 1999 that guided Google's meteoric multi-billion-dollar expansion?",
                "key_focus": "John Doerr's 'Measure What Matters', Objectives (inspirational qualitative direction) matched with Key Results (aggressive, measurable, quantifiable metrics), committed vs. aspirational 'stretch' OKRs (aiming for 70% success), avoiding conflating OKRs with annual compensation, and transparent company-wide goal alignment.",
                "reason": "The definitive operational goal-setting framework driving modern tech Silicon Valley execution."
            },
            {
                "id": 12,
                "title": "Type 1 vs. Type 2 Decisions: Jeff Bezos on Speed, Reversibility, and The Two-Way Door",
                "tier": "Tier 3: OKRs, Strategy & Decision Making",
                "angle": "decision_making_models",
                "slug": "jeff_bezos_type_1_vs_type_2_decisions_one_way_vs_two_way_doors_decision_velocity",
                "question": "Why do large corporations slow to a crawl because they treat every minor reversible decision with the agonizing bureaucracy of an irreversible life-or-death choice?",
                "key_focus": "Amazon's 2015 Shareholder Letter, One-Way Doors (Type 1: irreversible, high-consequence decisions requiring deep analytical deliberation) vs. Two-Way Doors (Type 2: reversible decisions that should be made quickly with 70% information by empowered individuals), 'Disagree and Commit' culture, and decision velocity.",
                "reason": "The quintessential executive mental model that prevents high-growth companies from degenerating into bureaucratic sludge."
            },
            {
                "id": 13,
                "title": "Porter's Five Forces: The Classic Strategy Framework for Dominating Competitive Markets",
                "tier": "Tier 3: OKRs, Strategy & Decision Making",
                "angle": "business_strategy",
                "slug": "porters_five_forces_michael_porter_harvard_business_school_competitive_advantage",
                "question": "Why do airlines make almost zero profit despite generating hundreds of billions, while credit card networks print cash? Michael Porter's 5 forces.",
                "key_focus": "Harvard Professor Michael Porter's seminal 1979 framework: 1) Threat of new entrants, 2) Bargaining power of suppliers, 3) Bargaining power of buyers, 4) Threat of substitutes, 5) Industry rivalry; economic moats, and finding structurally profitable industry niches.",
                "reason": "The timeless strategic management framework taught in every elite business school on Earth."
            },
            {
                "id": 14,
                "title": "Avoiding the HIPPO Trap: Highest Paid Person's Opinion vs. Data-Driven Experimentation",
                "tier": "Tier 3: OKRs, Strategy & Decision Making",
                "angle": "decision_culture",
                "slug": "hippo_effect_highest_paid_persons_opinion_a_b_testing_data_driven_decisions",
                "question": "Why does a boardroom discussion where the CEO states an intuitive opinion instantly kill scientific experimentation and lead to catastrophic multi-million-dollar product flops?",
                "key_focus": "The HIPPO (Highest Paid Person's Opinion) syndrome, Avinash Kaushik's analytics principles, establishing A/B testing culture (letting real consumer behavior override executive hunches), pre-mortem risk audits (Gary Klein), and creating environments where junior data scientists can comfortably prove the CEO wrong.",
                "reason": "Protects organizations from executive hubris by establishing rigorous empirical experimentation over ego."
            },
            {
                "id": 15,
                "title": "The First 90 Days: Michael Watkins' Executive Transition Playbook",
                "tier": "Tier 3: OKRs, Strategy & Decision Making",
                "angle": "executive_transitions",
                "slug": "the_first_90_days_michael_watkins_executive_transition_stars_model_early_wins",
                "question": "Why do 40% of newly hired leaders fail within their first 18 months, and what is the exact step-by-step roadmap for surviving your first 90 days in a new leadership role?",
                "key_focus": "Michael Watkins' STARS model (Start-up, Turnaround, Accelerated Growth, Realignment, Sustaining Success), avoiding the action trap (listening and learning before restructuring), securing early cultural wins, building political coalitions, and negotiating expectations with your own boss.",
                "reason": "The indispensable survival guide for every newly appointed manager, director, and executive."
            },
            {
                "id": 16,
                "title": "Peter Drucker: 'Culture Eats Strategy for Breakfast' and The Power of Shared Values",
                "tier": "Tier 4: Scaling, Culture Architecture & Crisis",
                "angle": "corporate_culture",
                "slug": "peter_drucker_culture_eats_strategy_for_breakfast_shared_values_enron_vs_southwest",
                "question": "How can a company with a brilliant multi-billion-dollar strategic plan collapse into ruin if its underlying organizational culture is rotten and toxic?",
                "key_focus": "Peter Drucker's legendary management philosophy, defining culture (what people do when the CEO leaves the room), Southwest Airlines vs. legacy air carriers, Enron's paper code of ethics vs. real ruthless culture, and aligning incentives with genuine corporate behavior.",
                "reason": "The bedrock management truth that human behavioral culture will always overpower dry strategic spreadsheets."
            },
            {
                "id": 17,
                "title": "Peacetime CEO vs. Wartime CEO: Ben Horowitz on Leading Through Existential Catastrophe",
                "tier": "Tier 4: Scaling, Culture Architecture & Crisis",
                "angle": "crisis_leadership",
                "slug": "ben_horowitz_the_hard_thing_about_hard_things_peacetime_vs_wartime_ceo",
                "question": "Why does the consensus-building, empowering leadership style that works brilliantly during economic booms fail completely when the company is running out of cash?",
                "key_focus": "Ben Horowitz's 'The Hard Thing About Hard Things', Peacetime CEO (expanding markets, encouraging creativity, broad delegation) vs. Wartime CEO (existential survival, micro-command, decisive ruthlessness, zero tolerance for deviations), and knowing which leader your company needs right now.",
                "reason": "An unvarnished, gritty Silicon Valley perspective on leading through startup near-death experiences and economic recessions."
            },
            {
                "id": 18,
                "title": "Organizational Debt: The Hidden Cost of Postponed Hard Conversations and Legacy Systems",
                "tier": "Tier 4: Scaling, Culture Architecture & Crisis",
                "angle": "organizational_health",
                "slug": "organizational_debt_steve_blank_legacy_processes_unspoken_tensions_restructuring",
                "question": "Just like technical debt slows software down, what is 'Organizational Debt' and how does accumulated bureaucracy paralyze companies as they grow from 50 to 500 people?",
                "key_focus": "Steve Blank's organizational debt concept, outdated policies created to prevent single historical mistakes that now paralyze progress, accumulated unspoken interpersonal tensions, pruning vestigial committees, and routine organizational debt jubilees.",
                "reason": "Essential organizational scaling theory that prevents maturing companies from drowning in their own historical paperwork."
            },
            {
                "id": 19,
                "title": "The Turnaround Blueprint: How Lou Gerstner Saved IBM from The Corporate Graveyard",
                "tier": "Tier 4: Scaling, Culture Architecture & Crisis",
                "angle": "turnaround_leadership",
                "slug": "lou_gerstner_who_says_elephants_cant_dance_ibm_turnaround_1993_mainframe_services",
                "question": "How did an outsider from RJR Nabisco take over a dying, bleeding $8 billion loss IBM in 1993, reject Wall Street demands to break it up, and orchestrate the greatest corporate turnaround in history?",
                "key_focus": "'Who Says Elephants Can't Dance?', refusing to publish a grand vision statement in favor of relentless operational execution, shifting IBM from commodity hardware to enterprise software and IT services, dismantling internal warring fiefdoms, and tying executive compensation strictly to total company performance.",
                "reason": "The supreme historical case study in large-scale corporate turnaround and cultural transformation."
            },
            {
                "id": 20,
                "title": "The Future of Management: Decentralized Autonomous Organizations (DAOs) and AI Management Agents",
                "tier": "Tier 4: Scaling, Culture Architecture & Crisis",
                "angle": "future_horizons",
                "slug": "future_of_management_ai_co_pilots_flat_organizations_remote_leadership_algorithms",
                "question": "When algorithmic AI agents manage project timelines, assign GitHub issues, and optimize supply chains automatically, what is the evolving role of the human leader?",
                "key_focus": "The death of middle-management spreadsheet compilation, the rise of the autonomous IC (Individual Contributor), leadership evolving from project tracking to emotional inspiration, moral stewardship, high-level vision, and building compassionate human community.",
                "reason": "Capstones the master curriculum by defining the enduring, irreplaceable soul of human leadership in an AI-managed workforce."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Return-to-Office Mandates Are Backfiring: The Great RTO War Between Bosses and Workers",
                "tier": "Trending / High Retention",
                "angle": "workplace_conflict",
                "slug": "return_to_office_mandates_backfiring_rto_commercial_real_estate_quiet_quitting",
                "trend_score": 98,
                "why_trending": "Massive corporate clash as CEOs (Amazon, Dell, Zoom) mandate 3 to 5 days in-office, sparking employee petitions, top-talent resignations, and badge-swipe tracking controversies.",
                "reason": "The #1 high-conflict workplace topic in the world today, examining executive power struggles, commercial real estate leases, and remote productivity metrics.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "The 'Quiet Quitting' vs. 'Quiet Firing' Epidemic: The Silent Corporate Breakdown",
                "tier": "Trending / High Retention",
                "angle": "viral_workplace_phenomenon",
                "slug": "quiet_quitting_vs_quiet_firing_burnout_disengagement_passive_aggressive_management",
                "trend_score": 97,
                "why_trending": "Billions of views on social media documenting 'Quiet Quitting' (doing strictly your job description without extra unpaid overtime) clashing with 'Quiet Firing' (managers ignoring employees until they quit).",
                "reason": "Universal cultural resonance dissecting the silent breakdown of trust between employers and modern workers.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Why Steve Jobs Fired People in Elevators: The Reality Behind the Ruthless Genius Myth",
                "tier": "Trending / High Retention",
                "angle": "legendary_leadership_myths",
                "slug": "steve_jobs_elevator_firing_myth_reality_intensity_perfectionism_apple_culture",
                "trend_score": 98,
                "why_trending": "Continuous viral fascination with Steve Jobs' brutal management style, debunking urban legends while examining his uncompromising intensity, A-player obsession, and reality distortion field.",
                "reason": "Fascinating examination of whether extreme visionary leadership requires personal cruelty or if Jobs succeeded despite it.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "How to Fire Someone with Dignity: The Conversation Every Manager Dreads",
                "tier": "Trending / High Retention",
                "angle": "difficult_management_skills",
                "slug": "how_to_fire_someone_compassion_dignity_legal_protocols_no_surprises_rule",
                "trend_score": 96,
                "why_trending": "Spike in manager anxiety around terminations and layoffs; videos explaining the 'No Surprises' rule: a termination should never be the first time an employee hears their performance is failing.",
                "reason": "High-utility professional guide providing clear, compassionate scripts that protect both employee human dignity and corporate legal exposure.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "The Four-Day Work Week Experiment: Why Companies Working Less Are Making More Money",
                "tier": "Trending / High Retention",
                "angle": "future_of_work_experiments",
                "slug": "four_day_work_week_trial_results_uk_32_hour_week_productivity_revenue_surge",
                "trend_score": 98,
                "why_trending": "Massive global trials in the UK, Iceland, and US showing that shifting to 32 hours with 100% pay increased company revenues by 35% and virtually eliminated burnout.",
                "reason": "Eye-opening data challenging 100-year-old Industrial Revolution 40-hour assumptions with real modern productivity science.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Enron Smartest Guys in the Room: How Toxic 'Rank and Yank' Destroyed an Energy Titan",
                "tier": "Trending / High Retention",
                "angle": "corporate_disasters",
                "slug": "enron_collapse_rank_and_yank_performance_review_jeff_skilling_toxic_greed",
                "trend_score": 96,
                "why_trending": "Fascinating retrospective on Enron's catastrophic 'Performance Review Committee' forced ranking system that fired the bottom 15% of employees every single year, incentivizing fraud and backstabbing.",
                "reason": "The ultimate cautionary corporate horror story showing how perverse managerial incentives destroy even the most profitable companies.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Open-Plan Offices Destroy Productivity: The Harvard Study That Settled the Debate",
                "tier": "Trending / High Retention",
                "angle": "workplace_ergonomics",
                "slug": "open_plan_office_productivity_disaster_harvard_study_noise_headphones_isolation",
                "trend_score": 97,
                "why_trending": "Harvard researchers Ethan Bernstein and Stephen Turban proving that open-plan offices actually decreased face-to-face interaction by 70% as employees withdrew behind giant noise-canceling headphones.",
                "reason": "Universally shared workplace rage validated by rigorous academic data, explaining why modern office floorplans fail.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "104_corporate_workplace": {
        "id": "104",
        "slug": "corporate_workplace",
        "title": "Corporate & Workplace",
        "category": "Careers_Workplace",
        "audience": "Corporate Professionals, HR Leaders, Knowledge Workers, Career Changers (Global)",
        "progression": [
            ("Tier 1: Workplace Dynamics, Onboarding & Corporate Communication Etiquette (Scratch / Beginner)",
             "Slack/email asynchronous vs. synchronous norms, navigating matrix hierarchies, managing up, meeting discipline (no-agenda no-meeting), and professional boundaries."),
            ("Tier 2: Performance Reviews, Career Trajectories & Compensation Negotiation (Intermediate)",
             "Calibrating performance review rubrics, 360-degree feedback loops, promotional packet documentation (the 'Brag Sheet'), and equity/RSU vs. base salary negotiation."),
            ("Tier 3: Workplace Politics, Power Mapping & Burnout Prevention (Upper Intermediate)",
             "Jeffrey Pfeffer's Power dynamics, stakeholder coalition mapping, surviving corporate restructuring and layoffs, and Maslach Burnout Inventory recovery protocols."),
            ("Tier 4: Future of Work: Remote Architecture, AI Workplace Integration & The Hybrid Office (Advanced / Expert)",
             "Fully remote vs. hybrid productivity metrics, asynchronous documentation culture (GitLab handbook model), AI agent integration into knowledge workflows, and employee surveillance ethics.")
        ],
        "flagship": {
            "title": "Managing Up: How to Build an Unbreakable Strategic Partnership with Your Boss",
            "angle": "career_advancement",
            "slug": "104_corporate_workplace_career_advancement_managing_up_executive_alignment"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Managing Up: How to Build an Unbreakable Strategic Partnership with Your Boss",
                "tier": "Tier 1: Workplace Dynamics & Professional Etiquette",
                "angle": "career_advancement",
                "slug": "managing_up_executive_alignment_boss_priorities_no_surprises_career_acceleration",
                "question": "How do top performers make themselves indispensable to their manager without ever kissing up or engaging in toxic office politics?",
                "key_focus": "Understanding your boss's real OKRs and stressors (what keeps them awake at night), adapting to their preferred communication style (Slack vs. bulleted email vs. face-to-face), never presenting a problem without two actionable solutions, and making your manager look brilliant to their own leadership.",
                "reason": "Flagship launch episode; the single most transformative career management skill for corporate professionals."
            },
            {
                "id": 2,
                "title": "Corporate Communication Etiquette: Asynchronous vs. Synchronous Slack and Email Hygiene",
                "tier": "Tier 1: Workplace Dynamics & Professional Etiquette",
                "angle": "workplace_communication",
                "slug": "corporate_communication_slack_email_etiquette_asynchronous_communication_channel_hygiene",
                "question": "Why does sending a message that just says 'Hi' on Slack waste collective time, and how do top professionals write emails that get replies in 5 minutes?",
                "key_focus": "The 'No Hello' rule (including the question in the initial ping), clear subject lines with action tags ([ACTION REQUIRED], [INFO], [DECISION]), public channels vs. DMs for institutional knowledge retention, and setting healthy boundaries against late-night notifications.",
                "reason": "Essential digital office hygiene that immediately elevates your professional reputation and protects your sanity."
            },
            {
                "id": 3,
                "title": "Navigating Matrix Organizations: Multiple Bosses, Dotted Lines, and Cross-Functional Chaos",
                "tier": "Tier 1: Workplace Dynamics & Professional Etiquette",
                "angle": "organizational_navigation",
                "slug": "matrix_organization_solid_line_vs_dotted_line_multiple_managers_competing_priorities",
                "question": "How do you survive and thrive when you report to a functional manager for reviews but three different project leads for daily work who all think their task is priority #1?",
                "key_focus": "Solid line vs. dotted line reporting structures, transparent capacity signaling, bringing competing managers together to force priority arbitration ('I can do Project A or Project B by Friday, which would you like me to deprioritize?'), and cross-functional diplomacy.",
                "reason": "Deconstructs the most confusing, modern corporate organizational structure that paralyzes mid-level professionals."
            },
            {
                "id": 4,
                "title": "The No-Agenda, No-Meeting Rule: How to Protect Your Calendar from Corporate Black Holes",
                "tier": "Tier 1: Workplace Dynamics & Professional Etiquette",
                "angle": "calendar_discipline",
                "slug": "no_agenda_no_meeting_rule_calendar_blocking_declining_meetings_politely",
                "question": "How do you politely decline useless meetings called by senior colleagues without seeming uncooperative or damaging your career?",
                "key_focus": "Defending calendar time blocks for deep work, the standard meeting contract (every calendar invite must have a 3-bullet agenda and desired outcome), delegating async status updates, and professional decline scripts ('I'm heads-down on X deliverable, can I review the notes afterwards?').",
                "reason": "High-utility survival guide for reclaiming 15+ hours of wasted corporate meeting time every week."
            },
            {
                "id": 5,
                "title": "Corporate Onboarding: The 30-60-90 Day Plan for Hitting the Ground Running",
                "tier": "Tier 1: Workplace Dynamics & Professional Etiquette",
                "angle": "career_onboarding",
                "slug": "thirty_sixty_ninety_day_plan_corporate_onboarding_listening_tour_early_wins",
                "question": "What is the strategic difference between Month 1 (absorbing context), Month 2 (identifying bottlenecks), and Month 3 (executing changes) in a new corporate job?",
                "key_focus": "The 30-day listening tour (interviewing 20 stakeholders with identical diagnostic questions), understanding unwritten corporate norms, avoiding the trap of criticizing previous systems, securing low-hanging fruit early wins, and establishing your professional brand.",
                "reason": "The exact roadmap for ensuring new hires transition successfully through probation into high-impact roles."
            },
            {
                "id": 6,
                "title": "The 'Brag Sheet': How to Document Your Impact So Promotions Become Inevitable",
                "tier": "Tier 2: Performance Reviews & Compensation",
                "angle": "performance_management",
                "slug": "the_brag_sheet_documenting_workplace_impact_quantified_metrics_promotions",
                "question": "Why will working hard in silence NEVER get you promoted, and how do elite performers keep a running 'Brag Sheet' that writes their own promotion packets?",
                "key_focus": "The psychological recency bias of managers during annual reviews, keeping a weekly 5-minute achievement log, translating daily tasks into business impact metrics (revenue generated, hours saved, processes automated), collecting praise emails, and presenting undeniable data during calibration cycles.",
                "reason": "The single most actionable career advancement practice that guarantees your contributions are never overlooked."
            },
            {
                "id": 7,
                "title": "Deciphering Performance Review Calibrations: How Ratings and Bell Curves Really Work",
                "tier": "Tier 2: Performance Reviews & Compensation",
                "angle": "hr_systems",
                "slug": "performance_review_calibrations_forced_ranking_stack_ranking_rubrics",
                "question": "What actually happens behind closed doors when directors and HR sit in calibration meetings to fight over who gets the top 'Exceeds Expectations' rating?",
                "key_focus": "How forced distribution bell curves cap top ratings, manager advocacy capital (why your boss's reputation dictates your rating), 360-degree peer feedback strategy, reading between the lines of performance rubrics, and challenging unfair performance reviews.",
                "reason": "Pulls back the curtain on the secretive HR calibration sessions that determine corporate bonuses and raises."
            },
            {
                "id": 8,
                "title": "Compensation Negotiation: Base Salary, RSUs, Signing Bonuses, and Comp Ratios",
                "tier": "Tier 2: Performance Reviews & Compensation",
                "angle": "salary_negotiation",
                "slug": "compensation_negotiation_base_salary_rsus_equity_vesting_cliffs_comp_ratio",
                "question": "How do you negotiate an extra $30,000 in equity and signing bonuses on a job offer without risking the company rescinding the offer?",
                "key_focus": "Understanding corporate compensation bands (comp-ratios), Restricted Stock Units (RSUs) vs. stock options, 4-year vesting schedules with 1-year cliffs, the power of competing offers, counter-offering with data (Levels.fyi), and negotiating non-salary perks (extra PTO, remote flexibility).",
                "reason": "Empowers corporate workers with the exact vocabulary and leverage points to maximize their lifetime earning potential."
            },
            {
                "id": 9,
                "title": "PIP (Performance Improvement Plan): The 30-Day Countdown and How to Navigate It",
                "tier": "Tier 2: Performance Reviews & Compensation",
                "angle": "workplace_legalities",
                "slug": "performance_improvement_plan_pip_severance_negotiation_paper_trail_exit",
                "question": "When your manager places you on a PIP, is it ever a genuine attempt to help you improve, or is it simply HR building a paper trail to fire you legally?",
                "key_focus": "The reality of corporate PIPs as legal liability shields against wrongful termination lawsuits, assessing whether the goals are achievable or engineered for failure, negotiating a voluntary exit package (severance) in exchange for signing liability waivers, and updating your resume on day one.",
                "reason": "A realistic, protective survival guide that demystifies corporate America's most dreaded HR document."
            },
            {
                "id": 10,
                "title": "The Career Matrix: Moving from Individual Contributor (IC) to People Manager",
                "tier": "Tier 2: Performance Reviews & Compensation",
                "angle": "career_transitions",
                "slug": "individual_contributor_vs_manager_track_making_the_leap_loss_of_tangible_output",
                "question": "Why is the transition from star engineer/designer to first-time manager a complete career change where your old technical skills become irrelevant?",
                "key_focus": "The loss of immediate tangible dopamine (writing code/closing sales vs. ambiguous people coaching), learning to celebrate indirect output through others, managing former peers, avoiding the urge to jump in and do the work yourself, and evaluating if management is truly your calling.",
                "reason": "Guides ambitious professionals through the most difficult psychological transition in corporate careers."
            },
            {
                "id": 11,
                "title": "Jeffrey Pfeffer's 'Power': The Real Rules of Corporate Politics That Nobody Admits",
                "tier": "Tier 3: Workplace Politics & Burnout Defense",
                "angle": "organizational_power",
                "slug": "jeffrey_pfeffer_power_why_some_people_have_it_corporate_politics_rules",
                "question": "Why do naive believers in pure meritocracy get passed over while politically savvy colleagues who understand power dynamics rise to the top?",
                "key_focus": "Stanford Professor Jeffrey Pfeffer's seminal book 'Power', the 'Just World' fallacy (believing good work speaks for itself), building visibility with key decision-makers, controlling resource gateways, strategic networking across departments, and accumulating social capital ethically.",
                "reason": "The definitive antidote to corporate naivety, teaching professionals how power actually flows in organizations."
            },
            {
                "id": 12,
                "title": "Stakeholder Mapping: The RACI Matrix and Power-Interest Grids",
                "tier": "Tier 3: Workplace Politics & Burnout Defense",
                "angle": "stakeholder_management",
                "slug": "stakeholder_mapping_power_interest_grid_raci_matrix_responsible_accountable",
                "question": "How do you launch a major corporate initiative without getting blindsided by a quiet veto from a senior director you forgot to consult?",
                "key_focus": "The Power-Interest Grid (High Power/High Interest 'Manage Closely', High Power/Low Interest 'Keep Satisfied'), the RACI Matrix (Responsible, Accountable, Consulted, Informed), avoiding too many cooks in the kitchen, and holding pre-alignment meetings before formal steering committees.",
                "reason": "The essential project management and political alignment tool required for large-scale enterprise execution."
            },
            {
                "id": 13,
                "title": "Surviving Corporate Layoffs: WARN Act Notices, Severance Agreements, and Financial Triage",
                "tier": "Tier 3: Workplace Politics & Burnout Defense",
                "angle": "layoff_survival",
                "slug": "corporate_layoffs_warn_act_severance_negotiation_cobra_health_insurance",
                "question": "When mass corporate layoffs strike and your Slack access is suddenly cut off at 8:00 AM, what are your immediate legal rights and financial action steps?",
                "key_focus": "The federal WARN Act (60-day notice rules for mass layoffs), severance agreement review (never sign on day one), negotiating extended health insurance (COBRA) subsidies and unvested equity, filing for state unemployment immediately, and emotional shock recovery.",
                "reason": "A critical emergency toolkit providing immediate legal and financial clarity during corporate restructurings."
            },
            {
                "id": 14,
                "title": "The Maslach Burnout Inventory: Exhaustion, Cynicism, and The Architecture of Recovery",
                "tier": "Tier 3: Workplace Politics & Burnout Defense",
                "angle": "burnout_neurobiology",
                "slug": "maslach_burnout_inventory_emotional_exhaustion_depersonalization_recovery",
                "question": "Why is true clinical burnout NOT just feeling tired from a long week, but a serious neuro-endocrine breakdown of your adrenal system?",
                "key_focus": "Christina Maslach's 3 dimensions of burnout: Emotional Exhaustion, Depersonalization (cynicism and treating coworkers like obstacles), and Reduced Personal Efficacy; workplace causes (lack of autonomy, unfair rewards, values mismatch), and medical recovery protocols requiring systemic boundary resets.",
                "reason": "Validates the severe mental health crisis of corporate overwork and provides clinical recovery roadmaps."
            },
            {
                "id": 15,
                "title": "Imposter Syndrome in Corporate Spaces: Why Top Performers Feel Like Frauds",
                "tier": "Tier 3: Workplace Politics & Burnout Defense",
                "angle": "workplace_psychology",
                "slug": "imposter_syndrome_corporate_high_achievers_clance_impostor_phenomenon",
                "question": "Why does getting promoted to Director or VP make high achievers feel terrified that everyone is about to discover they are completely unqualified?",
                "key_focus": "Dr. Pauline Clance's 1978 Impostor Phenomenon research, the spotlight effect, attributing success to 'luck' or 'flukes' while attributing mistakes to permanent incompetence, distinguishing normal learning curves from fraud feelings, and adopting the growth mindset.",
                "reason": "Provides massive psychological relief to high-achieving corporate professionals suffering in silent anxiety."
            },
            {
                "id": 16,
                "title": "Asynchronous Remote Work Architecture: The GitLab Handbook Model That Ditched the Office",
                "tier": "Tier 4: Future of Work & Remote Architecture",
                "angle": "remote_operations",
                "slug": "gitlab_remote_work_handbook_asynchronous_documentation_first_culture",
                "question": "How does an enterprise software company with 2,000 employees across 65 countries operate with zero physical offices and almost zero live meetings?",
                "key_focus": "GitLab's 2,000-page public handbook, 'Documentation-First' culture (if it's not written down, it doesn't exist), asynchronous project tracking on merge requests, respecting global time zones, eliminating the 'tap on the shoulder' culture, and output-based compensation.",
                "reason": "The visionary operational blueprint for how modern global digital knowledge organizations operate without physical real estate."
            },
            {
                "id": 17,
                "title": "Employee Surveillance Tech: Bossware, Keystroke Logging, and Mouse Jigglers",
                "tier": "Tier 4: Future of Work & Remote Architecture",
                "angle": "workplace_surveillance",
                "slug": "bossware_employee_surveillance_keystroke_loggers_mouse_jigglers_productivity_theatre",
                "question": "Why are corporate IT departments installing software that takes webcam photos every 10 minutes and logs keystrokes, and why does it incentivize fake 'productivity theatre'?",
                "key_focus": "The explosion of 'bossware' monitoring software, keystroke logging and idle-time tracking, the underground market for USB hardware mouse jigglers, the destruction of employee trust, and why measuring activity inputs instead of business outcomes is a managerial catastrophe.",
                "reason": "Exposes the contentious digital cold war fought between micromanaging corporate executives and remote employees."
            },
            {
                "id": 18,
                "title": "AI in the Corporate Workflow: How LLMs and Automation Are Rewriting the White-Collar Job",
                "tier": "Tier 4: Future of Work & Remote Architecture",
                "angle": "ai_workplace_transformation",
                "slug": "ai_in_the_corporate_workplace_llm_copilots_automating_white_collar_gruntwork",
                "question": "Will generative AI eliminate entry-level corporate analysts, or will professionals who master AI copilots simply replace those who don't?",
                "key_focus": "Automating routine document synthesis, financial modeling code generation, customer service triaging, the shifting definition of corporate competence toward curation, verification, and critical strategic synthesis, and enterprise AI compliance policies.",
                "reason": "The defining technological transformation altering daily white-collar corporate workflows right now."
            },
            {
                "id": 19,
                "title": "The Fractional Executive Economy: Why Top Leaders Are Working for 5 Startups at Once",
                "tier": "Tier 4: Future of Work & Remote Architecture",
                "angle": "fractional_careers",
                "slug": "fractional_executive_economy_fractional_cmo_cfo_cto_freelance_high_leverage",
                "question": "Why are senior corporate VPs leaving $400k corporate jobs to work 10 hours a week for four different companies as 'Fractional' CMOs and CFOs?",
                "key_focus": "The rise of fractional leadership (startups getting elite executive strategy for $8k/month without full-time benefits or equity dilution), high hourly leverage, portfolio careers diversifying career risk, and the unbundling of traditional full-time corporate employment.",
                "reason": "Explores the rapidly expanding high-income career model transforming senior knowledge work."
            },
            {
                "id": 20,
                "title": "The Future of the Workplace: The 2035 Office, Virtual HQs, and The Search for Meaning",
                "tier": "Tier 4: Future of Work & Remote Architecture",
                "angle": "future_horizons",
                "slug": "future_of_the_workplace_2035_hybrid_spaces_vr_collaboration_search_for_purpose",
                "question": "What will the corporate office look like in 2035, and how will humanity decouple personal identity and life meaning from corporate job titles?",
                "key_focus": "The reimagining of physical offices as hospitality social clubs for collaboration rather than computer rows, spatial VR presence, asynchronous global contracts, and the cultural movement decoupling self-worth from corporate ladders toward holistic life design.",
                "reason": "Capstones the master curriculum with an empowering, human-centered vision of work in the decades ahead."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The 'Coffee Badging' Trend: How Employees Are Bypassing RTO Tracking Mandates",
                "tier": "Trending / High Retention",
                "angle": "viral_workplace_hacks",
                "slug": "coffee_badging_remote_workers_badge_swipe_tracking_bypass_rto",
                "trend_score": 98,
                "why_trending": "Massive viral trend where remote workers come to the office, badge in to trigger HR attendance tracking, grab a coffee, talk to a coworker, and leave 45 minutes later to work from home.",
                "reason": "Hilarious, widely covered corporate rebellion highlighting the absurdity of tracking physical presence rather than output.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Overemployed: How People Are Secretly Working Two Full-Time Remote Tech Jobs at Once",
                "tier": "Trending / High Retention",
                "angle": "underground_career_hacks",
                "slug": "overemployed_secretly_working_two_remote_jobs_double_salary_j1_j2_opsec",
                "trend_score": 98,
                "why_trending": "Explosive community and Reddit subculture (r/overemployed) where tech workers juggle two or three simultaneous $150k remote engineering jobs, making $450k annually with strict calendar OPSEC.",
                "reason": "Fascinating, morally contentious underground movement testing the boundaries of employment contracts and remote productivity.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "How to Answer 'What Is Your Greatest Weakness?' in a Job Interview (The Only Script That Works)",
                "tier": "Trending / High Retention",
                "angle": "interview_hacks",
                "slug": "interview_greatest_weakness_question_how_to_answer_without_sounding_cliche",
                "trend_score": 97,
                "why_trending": "Universally hated interview question; viral tutorials tearing down fake answers ('I'm too much of a perfectionist') and providing genuine, high-credibility vulnerability frameworks.",
                "reason": "Immediate high-utility career interview hack that helps millions of nervous job seekers stand out.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Toxic Positivity Trap: Why Forcing 'Good Vibes Only' at Work Destroys Morale",
                "tier": "Trending / High Retention",
                "angle": "corporate_culture_critiques",
                "slug": "toxic_positivity_in_the_workplace_good_vibes_only_suppressing_real_problems",
                "trend_score": 96,
                "why_trending": "Employees pushing back against corporate cultures that dismiss legitimate burnout and operational failures with hollow cheerleading and enforced optimism.",
                "reason": "Deeply validating critique of corporate gaslighting, teaching managers how to embrace constructive realism.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Why You Should Never Sign a Non-Compete: The FTC Ban and Employee Mobility",
                "tier": "Trending / High Retention",
                "angle": "labor_law_updates",
                "slug": "ftc_non_compete_ban_lina_khan_worker_mobility_california_ban_enforceability",
                "trend_score": 97,
                "why_trending": "Historic FTC legal battles seeking to ban non-compete agreements nationwide, liberating 30 million workers to switch jobs or start competing businesses.",
                "reason": "Crucial legal update protecting workers from corporate restrictive covenants that lock them into bad jobs.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The 'Meeting That Could Have Been an Email': Why Bad Communication Costs $37 Billion Annually",
                "tier": "Trending / High Retention",
                "angle": "workplace_humor",
                "slug": "this_meeting_could_have_been_an_email_corporate_satire_economic_waste",
                "trend_score": 96,
                "why_trending": "Perennial corporate meme culture supported by serious economic research showing that unnecessary meetings cost the US economy tens of billions in wasted payroll.",
                "reason": "Everyday humor backed by hard economic data that every office worker in the world identifies with.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Gen Z Is Rejecting Corporate Hustle Culture: The Rise of the 'Lazy Girl Job'",
                "tier": "Trending / High Retention",
                "angle": "generational_shifts",
                "slug": "lazy_girl_job_trend_gen_z_rejecting_hustle_culture_work_life_balance",
                "trend_score": 98,
                "why_trending": "Massive viral TikTok phenomenon celebrating quiet, non-stressful, fully remote corporate jobs that pay $70k without grueling 70-hour weeks or executive ambitions.",
                "reason": "A profound cultural shift where younger generations prioritize mental health and personal life over climbing the traditional corporate ladder.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "105_consumer_psychology": {
        "id": "105",
        "slug": "consumer_psychology",
        "title": "Consumer Psychology",
        "category": "Commerce_Industry",
        "audience": "Marketers, Behavioral Economists, Product Managers, Entrepreneurs, Smart Consumers (Global)",
        "progression": [
            ("Tier 1: Cognitive Biases in Purchasing, Anchoring & The Decoy Effect (Scratch / Beginner)",
             "Daniel Kahneman's System 1 vs. System 2 thinking, price anchoring, the decoy effect (The Economist subscription experiment), loss aversion, and social proof."),
            ("Tier 2: Behavioral Economics, Nudge Theory & Habit Formation (Intermediate)",
             "Richard Thaler's Nudge Theory (choice architecture, default options), Nir Eyal's Hook Model (Trigger, Action, Variable Reward, Investment), and the Scarcity Principle (FOMO)."),
            ("Tier 3: Sensory Branding, Neuromarketing & Loyalty Economics (Upper Intermediate)",
             "Olfactory and acoustic branding (the sound of an opening soda can), fMRI brain scan reactions to Coca-Cola vs. Pepsi, net promoter score (NPS), and the endowment effect (IKEA effect)."),
            ("Tier 4: Dark Patterns, Algorithmic Personalization & The Ethics of Persuasion (Advanced / Expert)",
             "Deceptive e-commerce dark patterns (roach motels, hidden fees), TikTok dopamine prediction algorithms, surveillance capitalism (Shoshana Zuboff), and designing ethical consumer choices.")
        ],
        "flagship": {
            "title": "The Decoy Effect: How Menus and Tech Companies Secretly Force You to Pick the Expensive Option",
            "angle": "behavioral_economics",
            "slug": "105_consumer_psychology_behavioral_economics_decoy_effect_pricing_hacks"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Decoy Effect: How Menus and Tech Companies Secretly Force You to Pick the Expensive Option",
                "tier": "Tier 1: Cognitive Biases & Price Anchoring",
                "angle": "behavioral_economics",
                "slug": "the_decoy_effect_asymmetric_dominance_dan_ariely_economist_pricing_experiment",
                "question": "Why did introducing a 'Print Only' subscription for $125 make 84% of readers choose the $125 'Print + Digital' combo over the $59 'Digital Only' option?",
                "key_focus": "Dan Ariely's famous Economist subscription experiment, Asymmetric Dominance pricing, how cinema popcorn sizes (Small $3, Medium $6.50, Large $7) manipulate choice, and how SaaS software pricing tiers engineer the middle tier as an irresistible target.",
                "reason": "Flagship launch episode; the most famous and universally applied pricing manipulation trick in modern commerce."
            },
            {
                "id": 2,
                "title": "System 1 vs. System 2 Thinking: Daniel Kahneman on How Your Brain Actually Shops",
                "tier": "Tier 1: Cognitive Biases & Price Anchoring",
                "angle": "cognitive_psychology",
                "slug": "system_1_vs_system_2_thinking_daniel_kahneman_fast_and_slow_shopping_heuristics",
                "question": "Why do consumers make 95% of grocery store purchases using automatic, subconscious emotional shortcuts rather than analytical calculation?",
                "key_focus": "Daniel Kahneman's 'Thinking, Fast and Slow', System 1 (fast, automatic, emotional, low-energy heuristics) vs. System 2 (slow, deliberate, analytical, high-effort), cognitive fatigue at supermarket checkouts, and packaging color psychology.",
                "reason": "The foundational Nobel Prize-winning psychological framework governing all consumer decision-making."
            },
            {
                "id": 3,
                "title": "Price Anchoring: How Steve Jobs Sold a $499 iPad by Starting with $999",
                "tier": "Tier 1: Cognitive Biases & Price Anchoring",
                "angle": "pricing_psychology",
                "slug": "price_anchoring_steve_jobs_ipad_launch_999_dollar_anchor_perceived_value",
                "question": "How did Steve Jobs project a giant '$999' on screen during the 2010 iPad keynote, making $499 feel like the bargain of the century when it dropped?",
                "key_focus": "Anchoring and Adjustment heuristic, luxury restaurant wine lists featuring an overpriced $300 bottle solely to make the $60 bottle seem reasonable, MSRP crossed-out strike-through pricing, and the psychological relativity of monetary value.",
                "reason": "A masterclass in how initial baseline figures anchor human perception of cheap vs. expensive."
            },
            {
                "id": 4,
                "title": "Loss Aversion and The Endowment Effect: Why Losing $100 Hurts Twice as Much as Winning $100",
                "tier": "Tier 1: Cognitive Biases & Price Anchoring",
                "angle": "behavioral_economics",
                "slug": "loss_aversion_prospect_theory_endowment_effect_free_trials_car_test_drives",
                "question": "Why do car dealerships let you take a car home for a weekend test drive? The psychological trap of instant ownership.",
                "key_focus": "Kahneman and Tversky's Prospect Theory (losses loom 2 to 2.5 times larger than equivalent gains), Richard Thaler's coffee mug Endowment Effect, free 30-day trials transforming subscriptions from 'buying' to 'not wanting to lose what is already yours', and return policies.",
                "reason": "Explains why holding or testing an object makes the human brain value it significantly higher."
            },
            {
                "id": 5,
                "title": "Social Proof and The Bandwagon Effect: Why 'Best Seller' Signs Double Conversion",
                "tier": "Tier 1: Cognitive Biases & Price Anchoring",
                "angle": "persuasion_principles",
                "slug": "social_proof_robert_cialdini_bandwagon_effect_hotel_towel_reuse_experiment",
                "question": "Why did changing hotel bathroom signs from 'Save the environment' to '75% of guests in this room reuse their towels' cause compliance to skyrocket?",
                "key_focus": "Dr. Robert Cialdini's 'Influence: The Psychology of Persuasion', social proof as an evolutionary survival shortcut in uncertainty, fake tip jars with seed cash, 'Over 1 Billion Served' McDonald's signage, and review star ratings overriding personal judgment.",
                "reason": "The definitive look at how collective human consensus directs individual purchasing decisions."
            },
            {
                "id": 6,
                "title": "Nudge Theory: Richard Thaler on Choice Architecture and The Power of Defaults",
                "tier": "Tier 2: Nudge Theory, Habits & Scarcity",
                "angle": "choice_architecture",
                "slug": "nudge_theory_richard_thaler_cass_sunstein_default_opt_in_organ_donation",
                "question": "Why does Austria have a 99% organ donation rate while neighboring Germany has 12%, based purely on whether a box is checked by default?",
                "key_focus": "Richard Thaler's Nobel Prize-winning Nudge Theory, Libertarian Paternalism, opt-in vs. opt-out default architecture, placing fruit at eye level in school cafeterias, automatic 401(k) retirement enrollment, and the fly painted in Amsterdam airport urinals cutting spillage by 80%.",
                "reason": "Shows how subtle environmental cues and default settings steer massive population-level behavior."
            },
            {
                "id": 7,
                "title": "The Hook Model: How Nir Eyal Dissected Social Media's Habit-Forming Loops",
                "tier": "Tier 2: Nudge Theory, Habits & Scarcity",
                "angle": "habit_engineering",
                "slug": "the_hook_model_nir_eyal_trigger_action_variable_reward_investment_app_design",
                "question": "How do Instagram, TikTok, and casino slot machines keep users returning 50 times a day using B.F. Skinner's variable reward schedules?",
                "key_focus": "The 4-phase Hook Cycle: 1) Trigger (external notification moving to internal boredom/loneliness), 2) Action (minimal effort click/scroll), 3) Variable Reward (intermittent dopamine schedule: likes, surprises, novel videos), 4) Investment (user uploading photos or data making switching painful).",
                "reason": "The psychological blueprint behind modern consumer app design, habit formation, and digital addiction."
            },
            {
                "id": 8,
                "title": "The Scarcity Principle: FOMO, Countdown Clocks, and Black Friday Madness",
                "tier": "Tier 2: Nudge Theory, Habits & Scarcity",
                "angle": "scarcity_psychology",
                "slug": "scarcity_principle_fomo_countdown_timers_booking_com_black_friday_rush",
                "question": "Why does seeing 'Only 2 rooms left at this price!' on Booking.com make your heart race and force you to book immediately?",
                "key_focus": "Cialdini's Scarcity Principle, psychological reactance (perceiving a loss of freedom when options disappear), artificial countdown timers in e-commerce, limited-edition sneaker drops (Supreme/Nike), and Black Friday retail stampedes.",
                "reason": "Deconstructs the most potent consumer urgency lever used across modern e-commerce and retail."
            },
            {
                "id": 9,
                "title": "The Paradox of Choice: Barry Schwartz on Why Having 24 Jams Freezes Consumers",
                "tier": "Tier 2: Nudge Theory, Habits & Scarcity",
                "angle": "choice_overload",
                "slug": "paradox_of_choice_barry_schwartz_sheena_iyengar_jam_experiment_decision_fatigue",
                "question": "Why did a supermarket tasting booth with 24 jams attract more lookers, but a booth with only 6 jams sold ten times more actual jars?",
                "key_focus": "Sheena Iyengar and Mark Lepper's 2000 Jam Study, Barry Schwartz's 'Paradox of Choice', choice overload causing decision paralysis, buyer's remorse and post-purchase regret, Maximizers vs. Satisficers, and why curated minimalist menus outperform giant phone-book menus.",
                "reason": "Proves that expanding consumer options beyond a threshold reduces actual buying and customer happiness."
            },
            {
                "id": 10,
                "title": "Charm Pricing: The Magic of $9.99 and Left-Digit Bias",
                "tier": "Tier 2: Nudge Theory, Habits & Scarcity",
                "angle": "numerical_cognition",
                "slug": "charm_pricing_left_digit_bias_why_nine_ninety_nine_works_brain_encoding",
                "question": "Why does changing a price from $34.00 to $39.00 sometimes INCREASE sales, and how does the human brain process numbers from left to right?",
                "key_focus": "Left-Digit Bias (the brain processes the leading digit before finishing reading the decimal, encoding $2.99 as fundamentally closer to $2.00 than $3.00), Eric Anderson and Duncan Simester's catalog experiments showing $39 outselling $34, and prestige pricing (why luxury brands round up to clean $1,000 figures).",
                "reason": "Explains the century-old retail pricing trick that exploits the chronological way the brain reads numbers."
            },
            {
                "id": 11,
                "title": "Sensory Branding: Martin Lindstrom on Scent, Sound, and Subconscious Purchasing",
                "tier": "Tier 3: Sensory Branding & Neuromarketing",
                "angle": "sensory_marketing",
                "slug": "sensory_branding_martin_lindstrom_ambient_scent_harley_davidson_exhaust_sound",
                "question": "Why does Singapore Airlines spray a patented custom perfume ('Stefan Floridian Waters') on every flight attendant, and why did Harley-Davidson try to patent its engine sound?",
                "key_focus": "Martin Lindstrom's 'Brand Sense', olfactory marketing bypassing the thalamus straight to the emotional amygdala/hippocampus, Abercrombie & Fitch cologne scent diffusion, Kellogg's patented cereal crunch sound acoustics, and multi-sensory brand anchoring.",
                "reason": "Examines how brands bypass conscious visual advertising to anchor loyalty through smell, touch, and sound."
            },
            {
                "id": 12,
                "title": "The Pepsi Challenge: How fMRI Brain Scans Proved That Brands Override Taste",
                "tier": "Tier 3: Sensory Branding & Neuromarketing",
                "angle": "neuromarketing_science",
                "slug": "the_pepsi_challenge_read_montague_fmri_coca_cola_prefrontal_cortex_branding",
                "question": "Why did consumers overwhelmingly prefer Pepsi in blind taste tests, but chose Coca-Cola the second they saw the red can inside an fMRI brain scanner?",
                "key_focus": "Read Montague's 2004 Baylor College of Medicine neuroimaging study: blind tasting activated the sensory ventral putamen (Pepsi wins on sweeter sugar taste), but seeing the Coca-Cola brand logo activated the hippocampus and dorsolateral prefrontal cortex (emotional memories overriding physical taste buds).",
                "reason": "The landmark medical imaging experiment proving that branding physically alters subjective neural perception."
            },
            {
                "id": 13,
                "title": "The IKEA Effect: Why We Love Furniture More Just Because We Built It Ourselves",
                "tier": "Tier 3: Sensory Branding & Neuromarketing",
                "angle": "effort_justification",
                "slug": "the_ikea_effect_michael_norton_dan_ariely_effort_justification_origami",
                "question": "Why did instant cake mixes fail in the 1950s until food manufacturers required housewives to crack their own fresh egg into the batter?",
                "key_focus": "Michael Norton, Daniel Mochon, and Dan Ariely's 2011 study on the IKEA Effect, cognitive effort justification (labor leading to love), General Mills Betty Crocker egg breakthrough, Build-A-Bear workshops, and why assembling flat-pack furniture creates irrational emotional attachment.",
                "reason": "A fascinating study showing how requiring customer labor increases perceived product value."
            },
            {
                "id": 14,
                "title": "Supermarket Architecture: The Gruen Effect, Eye-Level Shelves, and The Milk in the Back",
                "tier": "Tier 3: Sensory Branding & Neuromarketing",
                "angle": "retail_spatial_design",
                "slug": "supermarket_psychology_gruen_effect_why_milk_is_in_the_back_eye_level_shelving",
                "question": "Why is the grocery store produce section immediately at the entrance, while staple milk and eggs are hidden in the furthest back corner of the store?",
                "key_focus": "The Gruen Effect (deliberate disorienting architecture inducing impulse buying), sensory priming with fresh colorful produce and flowers, slotting fees paid by food conglomerates to secure eye-level 'buy-level' shelves, wider shopping carts increasing purchases by 40%, and slow-tempo background music slowing walking pace.",
                "reason": "Exposes the psychological retail maze designed into every grocery store to extract maximum spending."
            },
            {
                "id": 15,
                "title": "Luxury Pricing and Veblen Goods: When Making Something Expensive Increases Demand",
                "tier": "Tier 3: Sensory Branding & Neuromarketing",
                "angle": "conspicuous_consumption",
                "slug": "veblen_goods_thorstein_veblen_conspicuous_consumption_luxury_price_inversion",
                "question": "Why does raising the price of a Rolex watch or a bottle of Dom Pérignon champagne by 30% cause sales volume to surge rather than decline?",
                "key_focus": "Thorstein Veblen's 1899 'Theory of the Leisure Class', Conspicuous Consumption, upward-sloping demand curves violating standard classical economics, luxury goods functioning as positional status signals, manufactured scarcity, and the Snob Effect.",
                "reason": "Deconstructs the inverted economics of ultra-luxury markets where high price IS the product feature."
            },
            {
                "id": 16,
                "title": "Dark Patterns in UX: Roach Motels, Sneak into Basket, and Confirmshaming",
                "tier": "Tier 4: Dark Patterns, Ethics & Future Persuasion",
                "angle": "deceptive_design",
                "slug": "dark_patterns_ux_harry_brignull_roach_motel_confirmshaming_hidden_costs",
                "question": "Why is it one click to subscribe to a gym or newspaper online, but requires a 45-minute phone call during business hours to cancel?",
                "key_focus": "Harry Brignull's 'Dark Patterns' taxonomy: Roach Motel (easy to get in, impossible to get out), Confirmshaming ('No thanks, I hate saving money' opt-out buttons), Sneak into Basket (adding travel insurance automatically), disguised ads, and regulatory crackdowns by the FTC and EU Digital Services Act.",
                "reason": "An eye-opening expose of the deceptive user interface designs deliberately engineered to manipulate online shoppers."
            },
            {
                "id": 17,
                "title": "TikTok's Recommendation Algorithm: The Ultimate Hyper-Personalized Dopamine Machine",
                "tier": "Tier 4: Dark Patterns, Ethics & Future Persuasion",
                "angle": "algorithmic_consumerism",
                "slug": "tiktok_algorithm_for_you_page_watch_time_graph_latent_interest_prediction",
                "question": "How does TikTok's For You Page decipher your deepest subconscious interests within 40 minutes of download based on split-second watch time and replays?",
                "key_focus": "Moving from the social graph (who you follow) to the content interest graph, micro-signals (fractional second pauses, re-watches, comment scrolling), natural language processing and computer vision tagging video frames, dynamic exploration vs. exploitation algorithms, and consumer impulse buying on TikTok Shop.",
                "reason": "Analyzes the most powerful behavioral prediction and consumer engagement engine ever built."
            },
            {
                "id": 18,
                "title": "Surveillance Capitalism: Shoshana Zuboff on The Weaponization of Behavioral Surplus",
                "tier": "Tier 4: Dark Patterns, Ethics & Future Persuasion",
                "angle": "surveillance_economics",
                "slug": "surveillance_capitalism_shoshana_zuboff_behavioral_surplus_prediction_products",
                "question": "If you are not paying for the product, you are not the customer—you are the raw material. How tech giants mine human experience into behavioral futures.",
                "key_focus": "Harvard Professor Shoshana Zuboff's landmark 2019 book, 'Behavioral Surplus' (collecting digital exhaust far beyond what is needed to improve service), converting human behavior into prediction products sold in behavioral futures markets, micro-targeted psychological nudging, and the erosion of consumer autonomy.",
                "reason": "The defining macroeconomic and philosophical critique of the modern data-extractive digital economy."
            },
            {
                "id": 19,
                "title": "The Gamification of Shopping: Temu, Pinduoduo, and The Slot Machine E-Commerce War",
                "tier": "Tier 4: Dark Patterns, Ethics & Future Persuasion",
                "angle": "gamified_commerce",
                "slug": "gamified_ecommerce_temu_pinduoduo_spin_the_wheel_social_team_buying_dopamine",
                "question": "Why does shopping on Temu feel like playing a video game at a Vegas casino, with spin-the-wheels, countdown alarms, and free gifts for recruiting friends?",
                "key_focus": "Colin Huang's Pinduoduo social commerce model (team buying for massive factory discounts), integrating casino gamification loops directly into product browsing, manufacturing extreme variable reward schedules, dopamine-driven impulse consumerism, and air freight logistics.",
                "reason": "Examines the hyper-gamified Chinese e-commerce model that disrupted global retail in under 24 months."
            },
            {
                "id": 20,
                "title": "The Ethical Marketer: Nudging for Good vs. Cognitive Exploitation",
                "tier": "Tier 4: Dark Patterns, Ethics & Future Persuasion",
                "angle": "future_horizons",
                "slug": "ethical_marketing_nudging_for_good_transparency_consumer_autonomy_future",
                "question": "Where is the moral boundary between persuasive behavioral design that helps people save money and healthy living, versus predatory psychological extraction?",
                "key_focus": "The Nudge ethics test (is the choice transparent, easy to opt out of, and aligned with the consumer's own stated long-term goals?), Patagonia's 'Don't Buy This Jacket' anti-consumerism campaigns, designing for friction to prevent regret, and empowering conscious, resilient consumers in an age of algorithmic persuasion.",
                "reason": "Capstones the master curriculum with an inspiring ethical manifesto for marketers, designers, and consumers."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Temu Is So Insanely Addictive: The Psychology Behind the Free Wheel Spins and $1 Gadgets",
                "tier": "Trending / High Retention",
                "angle": "viral_app_breakdowns",
                "slug": "why_temu_is_so_addictive_slot_machine_psychology_pinduoduo_loss_leader",
                "trend_score": 98,
                "why_trending": "Temu's explosive rise to the #1 most downloaded app in the US and Europe, fueling intense viral curiosity and video essays on how it turns shopping into an addictive mobile video game.",
                "reason": "Incredible real-time cultural touchpoint analyzing variable reward schedules, gamified discounts, and social referral pressure.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why Fast Food Isn't Cheap Anymore: The $18 Big Mac and The Collapse of the Value Menu",
                "tier": "Trending / High Retention",
                "angle": "consumer_pricing_outrage",
                "slug": "fast_food_price_surges_eighteen_dollar_big_mac_value_menu_collapse_inflation",
                "trend_score": 98,
                "why_trending": "Massive viral consumer fury on TikTok and Reddit showing receipt shock as fast food prices outpace general inflation by 30%, pushing middle-class diners to sit-down restaurants.",
                "reason": "Universal consumer outrage backed by sharp economic reporting on franchise royalties, labor costs, and dynamic digital app pricing.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The Stanley Cup Phenomenon: How a 110-Year-Old Workmen's Thermos Became a $750 Million Status Symbol",
                "tier": "Trending / High Retention",
                "angle": "viral_product_crazes",
                "slug": "stanley_cup_phenomenon_the_buy_guide_tiktok_quencher_status_symbol",
                "trend_score": 98,
                "why_trending": "Lines outside Target at 4:00 AM, viral collector shelves of 40oz Quenchers, and car fire videos where the Stanley tumbler survived with ice still clinking inside.",
                "reason": "The quintessential modern masterclass in female influencer marketing, colorway drops, and turning utilitarian gear into viral status fashion.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Why Target and Walmart Put Essential Items in Locked Glass Cases (And Why It's Hurting Sales)",
                "tier": "Trending / High Retention",
                "angle": "retail_friction",
                "slug": "retail_theft_locked_glass_cases_target_walmart_customer_friction_sales_drop",
                "trend_score": 96,
                "why_trending": "Universal shopper frustration having to wait 15 minutes for an employee with a key to buy $4 deodorant or toothpaste, causing shoppers to abandon carts and buy on Amazon.",
                "reason": "Fascinating look at retail theft panic clashing with consumer psychology: how physical friction destroys the impulsive purchasing impulse.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Dynamic Pricing Is Coming to Grocery Stores: Electronic Shelf Labels and Surge Pricing",
                "tier": "Trending / High Retention",
                "angle": "consumer_surveillance_tech",
                "slug": "dynamic_pricing_electronic_shelf_labels_grocery_stores_surge_pricing_wendys",
                "trend_score": 97,
                "why_trending": "Wendy's backlash over 'surge pricing' announcements and grocery chains rolling out digital e-ink price tags that can raise ice cream prices on hot afternoons automatically.",
                "reason": "Eye-opening look into the high-tech future of retail pricing where fixed shelf tags disappear in favor of algorithmic real-time surge pricing.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Why Costco Hot Dogs Are Still $1.50: The Geniuses Behind Loss Leader Marketing",
                "tier": "Trending / High Retention",
                "angle": "legendary_loss_leaders",
                "slug": "costco_hot_dog_loss_leader_jim_sinegal_membership_economics_rotisserie_chicken",
                "trend_score": 97,
                "why_trending": "Jim Sinegal's legendary quote ('If you raise the effing hot dog, I will kill you'), explaining how $1.50 hot dogs and $4.99 rotisserie chickens drive $4 billion in membership fees.",
                "reason": "The most beloved, wholesome corporate pricing story in history demonstrating the strategic power of extreme loss leaders.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Shrinkflation Exposed: How Companies Shrink Your Cereal and Chips While Keeping the Price the Same",
                "tier": "Trending / High Retention",
                "angle": "covert_pricing_tactics",
                "slug": "shrinkflation_skimpflation_hidden_price_increases_smaller_cereal_air_in_bags",
                "trend_score": 98,
                "why_trending": "Viral before-and-after photos exposing major food conglomerates subtly reducing chocolate bar weights from 100g to 85g and indenting the bottom of peanut butter jars to mask inflation.",
                "reason": "High-outrage consumer watchdog topic that teaches viewers how to look past packaging redesigns and calculate unit prices per ounce.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 101-105...")
    for folder_name, meta in BATCH_101_105.items():
        process_niche(folder_name, meta)
    update_master_readme()
    print("Batch 101-105 complete!")

if __name__ == "__main__":
    main()
