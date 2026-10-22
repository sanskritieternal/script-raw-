import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_171_175 = {
    "171_human_behavior": {
        "id": "171",
        "slug": "human_behavior",
        "title": "Human Behavior",
        "category": "People_Communities",
        "audience": "Behavioral Economists, Evolutionary Psychologists, Cognitive Scientists, Decision-Making Analysts, Curious Human Observers (Global)",
        "progression": [
            ("Tier 1: Cognitive Biases, Heuristics & System 1 vs System 2 Thinking (Beginner / Scratch)",
             "Daniel Kahneman's dual-system framework, availability heuristic, anchoring bias, confirmation bias, loss aversion, and fundamental attribution error in everyday judgment."),
            ("Tier 2: Evolutionary Psychology, Social Status Games & Mating Signals (Intermediate)",
             "Costly signaling theory, status hierarchies and dominance vs prestige, Dunbar's number (150 social limit), in-group/out-group tribal cognition, and evolutionary mismatched environments."),
            ("Tier 3: Mob Psychology, Herd Contagion & De-individuation Dynamics (Upper Intermediate)",
             "Gustave Le Bon's crowd psychology, informational vs normative social influence, bystander effect diffusion of responsibility, panic stampede fluid dynamics, and moral outrage cascades."),
            ("Tier 4: Behavioral Economics Nudges, Choice Architecture & Neurobiology of Willpower (Advanced / Masterclass)",
             "Thaler and Sunstein's nudge theory, default opt-in choice architecture, dopamine reward prediction error loops, ego depletion controversies, and designing behavioral interventions for public health.")
        ],
        "flagship": {
            "title": "Thinking, Fast and Slow: How Daniel Kahneman's Two Systems Dictate Every Human Choice",
            "angle": "case_study",
            "slug": "171_human_behavior_case_study_thinking_fast_and_slow"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Thinking, Fast and Slow: How Daniel Kahneman's Two Systems Dictate Every Human Choice",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "thinking_fast_and_slow_kahneman_tversky_two_systems",
                "question": "Why does your brain rely on an automatic, unconscious mental autopilot for 95% of daily decisions, and how does it trick you into costly blunders?",
                "focus": "System 1 (fast, instinctive, emotional) vs System 2 (slow, deliberative, logical), cognitive ease, the Linda problem, prospect theory, and Kahneman's 2002 Nobel Prize.",
                "reason": "Crucial foundational episode exploring the core dual-process model that revolutionized economics and cognitive psychology."
            },
            {
                "id": 2,
                "title": "Loss Aversion: Why Losing $100 Hurts Twice as Much as Winning $100 Feels Good",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "loss_aversion_prospect_theory_asymmetric_emotional_pain",
                "question": "Why will people take reckless financial risks to avoid a guaranteed loss, but play it ultra-safe when facing guaranteed gains?",
                "focus": "The S-shaped value curve of prospect theory, the endowment effect (overvaluing things simply because you own them), sunk cost fallacies, and marketing trial periods.",
                "reason": "Deconstructs the most powerful cognitive bias governing human economic risk-taking and irrational consumer retention."
            },
            {
                "id": 3,
                "title": "Anchoring Bias: How a Random Number Dictates What You Are Willing to Pay",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "anchoring_bias_price_perception_negotiation_tactics",
                "question": "How do luxury jewelers, real estate agents, and restaurant menus use high decoy numbers to manipulate your perception of value?",
                "focus": "Kahneman and Tversky's wheel-of-fortune experiment, the first-number advantage in salary negotiations, 'was $199, now $99' retail tricks, and cognitive adjustment failure.",
                "reason": "Explains how subconscious mental anchors distort human estimations and transactional negotiations."
            },
            {
                "id": 4,
                "title": "Confirmation Bias: Why Facts Don't Change Our Minds",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "confirmation_bias_motivated_reasoning_identity_protective_cognition",
                "question": "Why do two opposing people look at the exact same scientific study and both walk away feeling even more convinced they were right all along?",
                "focus": "Motivated reasoning, identity-protective cognition (Dan Kahan), selective exposure in search algorithms, backfire effect nuances, and active epistemic humility techniques.",
                "reason": "Masterclass on the primary psychological barrier preventing objective truth-seeking in political and personal beliefs."
            },
            {
                "id": 5,
                "title": "Dunbar's Number: Why Your Brain Can Only Handle 150 Real Relationships",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "dunbars_number_neocortex_ratio_social_group_limits",
                "question": "How did Robin Dunbar predict that humans can only maintain 150 stable friendships based on the size of our primate neocortex?",
                "focus": "Neocortex ratio scaling in primates, hunter-gatherer village sizes, Roman military century units (maniple), Gore-Tex factory size caps (150 workers), and social media superficiality.",
                "reason": "Reveals the evolutionary neurobiological limits that constrain human social group architecture and institutional scaling."
            },
            {
                "id": 6,
                "title": "Costly Signaling Theory: Why Peacocks Grow Giant Tails and Humans Buy Rolexes",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "costly_signaling_theory_zahavi_handicap_principle_luxury",
                "question": "Why do biological organisms waste immense energy on bright feathers, heavy antlers, and diamond watches that provide zero survival utility?",
                "focus": "Amotz Zahavi's handicap principle, unforgeable honesty of expensive signals, conspicuous consumption (Thorstein Veblen), philanthropic donations as status displays, and virtue signaling.",
                "reason": "Deep dive into evolutionary biology explaining why humans deliberately waste resources to communicate social and genetic fitness."
            },
            {
                "id": 7,
                "title": "The Bystander Effect: Why a Crowd of 50 People is Less Likely to Help Than a Single Stranger",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "bystander_effect_kitty_genovese_diffusion_of_responsibility",
                "question": "What happens in a crowded subway station when someone collapses, and why does everyone freeze waiting for someone else to act?",
                "focus": "Diffusion of responsibility, pluralistic ignorance (looking at others' calm faces to gauge danger), the Kitty Genovese myth vs reality, and how to break the bystander spell by singling out individuals.",
                "reason": "Crucial behavioral study explaining why large social groups become paralyzed during sudden public emergencies."
            },
            {
                "id": 8,
                "title": "The Dunning-Kruger Effect: Why the Least Competent People Are the Most Confident",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "dunning_kruger_effect_metacognition_illusory_superiority",
                "question": "Why does a complete beginner on day two feel like an expert, while real PhDs suffer from crushing imposter syndrome?",
                "focus": "David Dunning and Justin Kruger's 1999 paper, lack of metacognitive awareness preventing people from recognizing their own incompetence, Mount Stupid vs Valley of Despair, and intellectual modesty.",
                "reason": "Examines the ubiquitous cognitive distortion that leads novices to overestimate their competence and experts to doubt their mastery."
            },
            {
                "id": 9,
                "title": "Mob Mentality: The Terrifying Psychology of De-individuation in Crowds",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "mob_mentality_deindividuation_crowd_psychology_le_bon",
                "question": "How do peaceful, law-abiding citizens turn into violent rioters when absorbed into a screaming, anonymous stadium crowd?",
                "focus": "Gustave Le Bon's The Crowd (1895), loss of individual self-awareness, diffusion of moral agency under anonymity, emergent norm theory, soccer hooliganism, and online digital lynch mobs.",
                "reason": "Explores how collective social environments strip away individual moral inhibition and replace it with volatile group contagion."
            },
            {
                "id": 10,
                "title": "Nudge Theory: How Changing a Default Option Can Save Billions in Healthcare and Retirement",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "nudge_theory_richard_thaler_choice_architecture_defaults",
                "question": "Why does switching an organ donation form from 'check box to opt in' to 'check box to opt out' increase donor rates from 15% to 99%?",
                "focus": "Richard Thaler and Cass Sunstein's libertarian paternalism, automatic enrollment 401(k) savings plans, plate size psychology in buffets, fly stickers in Schiphol urinals, and ethical boundaries of nudging.",
                "reason": "Deconstructs the powerful behavioral economics toolkit used by governments worldwide to gently guide human decisions."
            },
            {
                "id": 11,
                "title": "The Fundamental Attribution Error: Why We Blame Others' Character but Excuse Our Own Circumstances",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "deep_dive",
                "slug": "fundamental_attribution_error_actor_observer_bias_traffic",
                "question": "When someone cuts you off in traffic, why do you assume they are an aggressive jerk, but when you do it, you excuse yourself because you were late for an interview?",
                "focus": "Lee Ross' 1977 formulation, actor-observer asymmetry, dispositional vs situational attributions, cultural differences (Western individualist vs East Asian collectivist attribution), and building empathy.",
                "reason": "Identifies the single most common attribution bias that drives everyday interpersonal resentment and social conflict."
            },
            {
                "id": 12,
                "title": "Dopamine and Variable Reward Schedules: Why Slot Machines and TikTok Keep You Hooked",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "field_investigation",
                "slug": "dopamine_reward_prediction_error_b_f_skinner_slot_machines",
                "question": "How does unpredictable intermittent reward release more dopamine than guaranteed rewards, turning scrolling feeds into addiction machines?",
                "focus": "B.F. Skinner's operant conditioning chambers (variable ratio reinforcement), Wolfram Schultz's dopamine reward prediction error, pull-to-refresh swipe mechanics, and casino sensory architecture.",
                "reason": "Reveals the precise neurological and behavioral mechanisms exploited by gaming and social media engineers to capture human attention."
            },
            {
                "id": 13,
                "title": "Moral Outrage Contagion: Why Social Algorithms Run on Anger",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "systemic_critique",
                "slug": "moral_outrage_contagion_social_algorithms_rage_virality",
                "question": "Why do tweets and video clips containing moral-emotional words spread 20% faster for every additional emotional adjective included?",
                "focus": "Molly Crockett's research on digital moral outrage, low cost of online signaling vs physical protest risk, virtue reinforcement from in-group peers, algorithmic engagement amplification, and civic exhaustion.",
                "reason": "A critical analysis of how digital platform architectures deliberately stimulate ancient tribal outrage mechanisms for profit."
            },
            {
                "id": 14,
                "title": "The Hedonic Treadmill: Why Winning the Lottery Doesn't Make You Permanently Happy",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "comparative_analysis",
                "slug": "hedonic_treadmill_adaptation_lottery_winners_paraplegics",
                "question": "Why do lottery winners and accident survivors returning to identical baseline happiness levels just one year after their life-altering events?",
                "focus": "Brickman and Campbell's hedonic adaptation hypothesis, set-point theory of happiness, the evolutionary utility of never being permanently satisfied, and intentional activities that actually boost lasting well-being.",
                "reason": "Examines the neurochemical adaptation treadmill that keeps humans continuously striving, regardless of material success."
            },
            {
                "id": 15,
                "title": "The Decoy Effect: How a Fake Option Manipulates You into Buying the Most Expensive Drink",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "case_study",
                "slug": "decoy_effect_asymmetric_dominance_pricing_economist_subscription",
                "question": "Why does adding a 'print-only' option for $125 persuade 84% of readers to buy the 'print + digital' bundle for the exact same price?",
                "focus": "Dan Ariely's famous The Economist subscription experiment, Asymmetric Dominance Principle, altering choice sets to make a target option look like a no-brainer steal, and movie theater popcorn pricing.",
                "reason": "Exposes one of the most effective and pervasive pricing tricks used in global corporate commerce and retail sales."
            },
            {
                "id": 16,
                "title": "Halo and Horn Effects: How One Single Trait Distorts Everything People Think About You",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "field_investigation",
                "slug": "halo_effect_edward_thorndike_attractiveness_bias_courtrooms",
                "question": "Why do handsome courtroom defendants receive lighter prison sentences, and why do taller CEOs earn significantly higher corporate compensation?",
                "focus": "Edward Thorndike's 1920 discovery, cognitive spillover from one positive attribute (physical attractiveness) to unrelated virtues (intelligence, kindness, competence), horn effect demonization, and blind auditions.",
                "reason": "Investigates the unconscious perceptual bias that grants profound unearned privileges based on superficial physical traits."
            },
            {
                "id": 17,
                "title": "Tribalism and the Minimal Group Paradigm: Why We Form Gangs Over Tossed Coins",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "deep_dive",
                "slug": "minimal_group_paradigm_henri_tajfel_social_identity_theory",
                "question": "How did Henri Tajfel prove that sorting random strangers into 'Group X' and 'Group W' based on a coin flip makes them instantly discriminate against outsiders?",
                "focus": "Social Identity Theory, ingroup favoritism without pre-existing animosity, maximizing the relative advantage of one's own group even at the expense of absolute gains, and de-polarization strategies.",
                "reason": "Probes the deep, hardwired evolutionary instinct of humans to rapidly form tribal factions and punish outsiders."
            },
            {
                "id": 18,
                "title": "The Ultimatum Game: Why Humans Choose to Punish Unfairness Even at a Personal Cost",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "comparative_analysis",
                "slug": "ultimatum_game_behavioral_economics_altruistic_punishment_fairness",
                "question": "If someone offers you $1 out of $100 and you either accept it or you both get zero, why do 80% of humans reject the free dollar out of pure spite?",
                "focus": "Homo economicus rationality breakdown, altruistic punishment as an evolutionary enforcement mechanism for community cooperation, cross-cultural Machiguenga vs Western responses, and neural insula activation.",
                "reason": "Shatters classical economic models by proving that humans value fairness, honor, and retaliatory justice over cold mathematical self-interest."
            },
            {
                "id": 19,
                "title": "The Business of Behavioral Manipulation: How Casino Floor Design Traps Gamblers",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "cost_breakdown",
                "slug": "casino_floor_design_behavioral_manipulation_slot_placement_costs",
                "question": "Why are there no clocks, no windows, curved labyrinth carpets, and free alcohol on the gaming floors of Las Vegas and Macau?",
                "focus": "Natasha Dow Schüll's Addiction by Design, the 'machine zone' trance, placing high-hold slots at high-traffic maze corners, sensory overload audio-visual reinforcement, and player tracking telemetry analytics.",
                "reason": "Detailed architecture and financial analysis of the multi-billion-dollar commercial gaming industry engineered to exploit human behavioral vulnerabilities."
            },
            {
                "id": 20,
                "title": "The Masterclass on Behavioral Science: Designing Interventions That Actually Change Habits",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "masterclass",
                "slug": "masterclass_behavioral_science_com_b_model_habit_formation",
                "question": "How do top behavioral scientists systematically engineer lasting lifestyle and policy transformations that defeat human willpower failure?",
                "focus": "Susan Michie's COM-B behavioral system (Capability, Opportunity, Motivation -> Behavior), implementation intentions ('if-then' planning), habit stacking, environmental friction reduction, and randomized controlled trial (RCT) behavioral audits.",
                "reason": "The definitive masterclass synthesizing behavioral economics, neuroscience, and habit psychology into an actionable framework for personal and organizational change."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The 'Doomscrolling' Neurochemistry: Why Your Brain Refuses to Put the Phone Down at 1 AM",
                "trend_score": "High Global Velocity (9.6/10)",
                "angle": "deep_dive",
                "slug": "doomscrolling_neurochemistry_threat_monitoring_sleep_disruption",
                "why_trending": "Massive public resonance as millions struggle with late-night compulsive news consumption driven by ancient evolutionary threat-monitoring instincts.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "Why Daniel Kahneman's Death Sparked a Global Re-evaluation of Behavioral Economics",
                "trend_score": "Rapid Surge (9.5/10)",
                "angle": "case_study",
                "slug": "daniel_kahneman_legacy_behavioral_economics_replication_crisis",
                "why_trending": "Tributes and scientific retrospectives following the passing of Daniel Kahneman, assessing which behavioral heuristics stood the test of the replication crisis.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "The 'Lucky Girl Syndrome' and Manifestation: The Psychological Science Behind Placebo Luck",
                "trend_score": "Viral Peak (9.3/10)",
                "angle": "field_investigation",
                "slug": "lucky_girl_syndrome_manifestation_confirmation_bias_reticular_activating_system",
                "why_trending": "Viral social media trends claiming you can manifest luck deconstructed through the lens of the Reticular Activating System (RAS) and opportunistic confirmation bias.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "Dark Patterns in Apps: How Software Sneakily Tricks You into Unwanted Subscriptions",
                "trend_score": "Breakthrough Trend (9.1/10)",
                "angle": "systemic_critique",
                "slug": "dark_patterns_ux_design_roach_motel_forced_continuity_ftc",
                "why_trending": "FTC crackdowns and EU regulations targeting deceptive UI designs ('Roach Motel' easy to subscribe, impossible to cancel), sparking consumer awareness.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "Why Everyone Thinks They Are Better Than Average: The Illusory Superiority Epidemic",
                "trend_score": "High Velocity (8.9/10)",
                "angle": "root_cause_analysis",
                "slug": "illusory_superiority_better_than_average_effect_driving_skills",
                "why_trending": "Fascinating statistical studies showing 93% of drivers rate themselves 'above average', exploring how human self-esteem mechanisms preserve positive ego illusions.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "The Psychology of Luxury Dupes: Why Gen Z Wears Fake Cartier and Proudly Brags About It",
                "trend_score": "Emerging Niche (8.8/10)",
                "angle": "cultural_traditions",
                "slug": "psychology_of_luxury_dupes_counterfeit_culture_status_inversion",
                "why_trending": "Cultural status inversion where younger consumers reject gatekept luxury brand prices, finding social status instead in hunting down identical cheap alternatives.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The Multi-Billion Dollar Nudge Industry: How Governments and Airlines Profit from Choice Architecture",
                "trend_score": "Steady Long-Tail (8.5/10)",
                "angle": "cost_breakdown",
                "slug": "nudge_industry_economics_airline_seat_selection_fees_revenues",
                "why_trending": "Financial teardown showing how airlines extract billions in auxiliary fees by using loss aversion nudges during seat selection and baggage add-on checkout screens.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "172_social_experiments": {
        "id": "172",
        "slug": "social_experiments",
        "title": "Social Experiments",
        "category": "People_Communities",
        "audience": "Experimental Sociologists, Ethics Reviewers, Behavioral Researchers, Psychology Historians, Social Documentarians (Global)",
        "progression": [
            ("Tier 1: Experimental Design in Social Science, Independent Variables & Placebo Controls (Beginner / Scratch)",
             "Randomized control trial (RCT) design in social sciences, null hypothesis testing, placebo effects and Hawthorne observer effects, and ethical consent boundaries."),
            ("Tier 2: Conformity and Obedience (Asch line tests, Milgram electric shocks, Bystander intervention) (Intermediate)",
             "Stanley Milgram's obedience to authority variations, Solomon Asch's perceptual conformity line experiments, Darley and Latané's bystander intervention lab setups, and Albert Bandura's Bobo doll aggression modeling."),
            ("Tier 3: Unethical Historical Experiments, Institutional Review Boards (IRB) & Belmont Report Ethics (Upper Intermediate)",
             "The Monster Study on stuttering orphans, the Tuskegee syphilis study atrocities, the Belmont Report core principles (Respect, Beneficence, Justice), and modern IRB oversight mandates."),
            ("Tier 4: Large-Scale Field Experiments, Algorithmic Social A/B Testing & Digital Civic Sandboxes (Advanced / Masterclass)",
             "Facebook's 2012 emotional contagion study controversy, nationwide Universal Basic Income random trials, digital civic sandboxes, and evaluating long-term societal interventions.")
        ],
        "flagship": {
            "title": "The Milgram Obedience Experiment: The Shocking Reality of Authority and Conscience",
            "angle": "case_study",
            "slug": "172_social_experiments_case_study_the_milgram_obedience_experiment"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Milgram Obedience Experiment: The Shocking Reality of Authority and Conscience",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "milgram_obedience_experiment_yale_electric_shocks_authority",
                "question": "How did a Yale psychologist prove that 65% of ordinary citizens would administer lethal 450-volt electric shocks to a screaming stranger simply because a man in a lab coat told them to?",
                "focus": "Stanley Milgram's 1961 experiment, the banality of evil (Hannah Arendt link to Eichmann trials), the 'agentic state' shedding personal moral responsibility, variations (proximity of victim, conflicting authorities), and ethical trauma.",
                "reason": "Crucial foundational episode exploring the most famous, chilling, and influential behavioral compliance experiment in psychological history."
            },
            {
                "id": 2,
                "title": "The Asch Conformity Experiments: Denying Your Own Eyes to Fit In with the Group",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "asch_conformity_experiments_line_judgment_peer_pressure",
                "question": "Why will 75% of intelligent people look at three lines on a card and publicly agree with an obviously wrong answer because actors in the room gave it first?",
                "focus": "Solomon Asch's 1951 methodology, normative vs informational conformity, the power of a single lone dissenter dropping conformity from 37% to 5%, and the neurobiology of social rejection panic.",
                "reason": "Establishes the foundational laboratory demonstration showing how group consensus easily overrides objective physical sensory perception."
            },
            {
                "id": 3,
                "title": "The Hawthorne Effect: How Being Watched Radically Alters Human Productivity",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "hawthorne_effect_western_electric_observer_bias_productivity",
                "question": "Why did workers at a Chicago factory work faster when factory lights were made brighter, but also worked faster when the lights were dimmed to near darkness?",
                "focus": "Western Electric's Hawthorne Works experiments (1924-1932), the observer effect in social science, novelty effects, worker feeling of special attention, and controlling for observer bias in modern experiments.",
                "reason": "Deconstructs the foundational experimental artifact that every social scientist, industrial psychologist, and manager must account for."
            },
            {
                "id": 4,
                "title": "The Bobo Doll Experiment: How Children Learn Violence by Watching Adults",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "bobo_doll_experiment_albert_bandura_social_learning_theory",
                "question": "What happens when nursery school children watch an adult punch, kick, and yell insults at an inflatable clown doll?",
                "focus": "Albert Bandura's 1961 Social Learning Theory, observational modeling without direct reinforcement, novel aggressive behaviors invented by children, and the 60-year debate over media and video game violence.",
                "reason": "Masterclass on behavioral modeling, showing that human behavior is acquired through observation and social imitation rather than just conditioning."
            },
            {
                "id": 5,
                "title": "The Third Wave: The High School History Class That Accidentally Created a Fascist Movement in 5 Days",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "the_third_wave_ron_jones_cubberley_high_school_fascism_experiment",
                "question": "How did a California high school teacher in 1967 demonstrate how the German public fell under Nazi rule by turning his teenagers into a disciplined, fanatical political cult in under a week?",
                "focus": "Ron Jones' mottoes: 'Strength through Discipline, Strength through Community, Strength through Action', student informant networks turning on classmates, sudden out-of-control momentum, and the auditorium reveal.",
                "reason": "A stunning, frightening real-world demonstration of how rapidly authoritarian group dynamics and conformity can be induced in everyday populations."
            },
            {
                "id": 6,
                "title": "The Robbers Cave Experiment: How Intergroup Conflict is Created and Healed",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "robbers_cave_experiment_muzafer_sherif_eagles_vs_rattlers",
                "question": "How did researchers turn 22 well-adjusted boy scouts at an Oklahoma summer camp into bitter, violent tribal enemies in just four days?",
                "focus": "Muzafer Sherif's Realist Conflict Theory, the Eagles vs the Rattlers, zero-sum competition breeding hatred and cabin raids, failure of simple social contact to bring peace, and the power of superordinate goals (fixing the shared water supply) in uniting warring groups.",
                "reason": "The quintessential experimental demonstration of tribal conflict creation and how shared cooperative goals can dissolve deep-seated prejudice."
            },
            {
                "id": 7,
                "title": "The Belmont Report: How Unethical Horrors Built the Modern Human Subjects Protection Code",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "belmont_report_1979_tuskegee_syphilis_human_subjects_ethics",
                "question": "How did the 40-year Tuskegee Syphilis Study force the US government to establish the modern ethical rules governing all human medical and social research?",
                "focus": "Withholding penicillin from 400 Black men for decades, whistleblower Peter Buxtun, the 1979 Belmont Report's three core ethical principles: Respect for Persons (informed consent), Beneficence (do no harm), and Justice (fair subject selection), and the creation of Institutional Review Boards (IRBs).",
                "reason": "Essential historical and legal foundation explaining why modern social science enforces strict ethical boundaries on human experimentation."
            },
            {
                "id": 8,
                "title": "The Monster Study: The Darkest Experiment in Speech Pathology History",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "investigative_report",
                "slug": "the_monster_study_wendell_johnson_orphan_stuttering_experiment",
                "question": "Why did a renowned speech therapist deliberately induce permanent psychological damage and speech impediments in 22 healthy orphan children in 1939?",
                "focus": "Dr. Wendell Johnson and Mary Tudor's University of Iowa experiment, relentless negative conditioning berating children that their speech was terrible, lifelong psychological withdrawal, decades of institutional coverup, and modern multi-million-dollar state settlements.",
                "reason": "A somber cautionary study exposing the dark history of institutional vulnerable population exploitation in the name of scientific curiosity."
            },
            {
                "id": 9,
                "title": "The Smoke-Filled Room Experiment: When Pluralistic Ignorance Paralyzes Humans in Real Danger",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "smoke_filled_room_experiment_latane_darley_pluralistic_ignorance",
                "question": "When acrid white smoke begins pouring out of a wall vent, why will people sit calmly in a room for 20 minutes choking on fumes because two actors pretend nothing is wrong?",
                "focus": "Bibb Latané and John Darley's 1968 experiment, 75% of lone subjects reporting smoke in two minutes vs only 10% reporting it when sitting with passive confederates, pluralistic ignorance dynamics, and overcoming social embarrassment during emergencies.",
                "reason": "Demonstrates how the human terror of social awkwardness routinely overrides elementary biological self-preservation instincts."
            },
            {
                "id": 10,
                "title": "The Rosenhan Experiment: Being Sane in Insane Places",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "rosenhan_experiment_on_being_sane_in_insane_places_psychiatry",
                "question": "What happened when eight completely sane pseudopatients checked into mental asylums claiming to hear the word 'thud', and then acted completely normal?",
                "focus": "David Rosenhan's 1973 Science paper, average 19-day involuntary hospitalization, normal note-taking labeled as pathological 'writing behavior', the reverse experiment catching imaginary pseudopatients, and the overhaul of the DSM diagnostic manual.",
                "reason": "One of the most disruptive undercover experiments in psychiatric history, exposing the severe diagnostic subjectivity of institutional mental healthcare."
            },
            {
                "id": 11,
                "title": "The Good Samaritan Experiment: When Rushing Seminary Students Stepped Over a Groaning Man",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "deep_dive",
                "slug": "good_samaritan_experiment_darley_batson_time_pressure_morality",
                "question": "Why did theology students on their way to deliver a sermon on the Good Samaritan literally step over a slumping, coughing victim in an alleyway?",
                "focus": "John Darley and Daniel Batson's 1973 Princeton experiment, testing religious orientation vs situational time pressure, 63% stopping when having plenty of time vs only 10% stopping when in a hurry, and situational ethics.",
                "reason": "Proves that simple environmental time pressure has a vastly greater influence on altruistic moral behavior than deeply held religious or moral values."
            },
            {
                "id": 12,
                "title": "The Facebook Emotional Contagion Study: Manipulating the Feelings of 689,000 Unsuspecting Users",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "systemic_critique",
                "slug": "facebook_emotional_contagion_study_algorithmic_manipulation_ethics",
                "question": "How did Facebook secretly alter the news feeds of nearly 700,000 people to prove that suppressing positive or negative words changed what users posted?",
                "focus": "The 2014 PNAS paper by Kramer, Guillory, and Hancock; massive public and scientific backlash; lack of informed consent; emotional manipulation without debriefing; and the unregulated wild west of private corporate algorithmic experimentation.",
                "reason": "Investigates the landmark ethical crisis that brought big tech's covert behavioral experimentation into international regulatory scrutiny."
            },
            {
                "id": 13,
                "title": "The AClass Divided (Brown Eyes vs Blue Eyes): Jane Elliott's 1968 Third-Grade Revolution",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "case_study",
                "slug": "blue_eyes_brown_eyes_experiment_jane_elliott_discrimination",
                "question": "How did an Iowa schoolteacher teach eight-year-old children the visceral reality of racism the day after Martin Luther King Jr. was assassinated?",
                "focus": "Jane Elliott dividing her classroom by eye color, giving privileges and scientific praise to blue-eyed kids, watching children turn arrogant and cruel within hours, academic performance collapsing in the stigmatized group, and the enduring PBS Frontline documentary.",
                "reason": "One of the most famous, emotionally raw, and unforgettable classroom social experiments on the immediate psychology of prejudice and privilege."
            },
            {
                "id": 14,
                "title": "The Marshmallow Test: Does 4-Year-Old Delay of Gratification Truly Predict Lifetime Success?",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "comparative_analysis",
                "slug": "marshmallow_test_walter_mischel_delay_of_gratification_replication",
                "question": "Does being able to resist eating one marshmallow for 15 minutes to earn two predict higher SAT scores and career wealth 30 years later?",
                "focus": "Walter Mischel's 1970 Stanford experiment, the famous longitudinal follow-ups, modern 2018 replications revealing the hidden variable of socioeconomic background (wealthy kids trust adults to deliver the second marshmallow), and redefining willpower.",
                "reason": "Deconstructs a celebrated psychological classic to reveal how socioeconomic background and trust in adults mediate impulse control."
            },
            {
                "id": 15,
                "title": "The Invisible Gorilla: Inattentional Blindness and How We Miss What's Right in Front of Us",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "field_investigation",
                "slug": "invisible_gorilla_experiment_simons_chabris_inattentional_blindness",
                "question": "Why do 50% of people counting basketball passes completely fail to notice a person in a full gorilla suit walk into the center of the frame, beat its chest, and walk off?",
                "focus": "Christopher Chabris and Daniel Simons' 1999 experiment, selective attention limits, cognitive load blindness, radiologists missing a matchbox-sized gorilla on lung CT scans, and implications for distracted driving and eyewitness testimony.",
                "reason": "Masterclass on perceptual psychology and the profound cognitive limits of human conscious attention."
            },
            {
                "id": 16,
                "title": "The Universal Basic Income Trials: What Happens When You Hand Unconditional Cash to 10,000 People?",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "investigative_report",
                "slug": "universal_basic_income_randomized_trials_finland_kenya_stockton",
                "question": "Do people quit their jobs and buy drugs when given $1,000 a month with no strings attached, or do health, education, and entrepreneurship soar?",
                "focus": "GiveDirectly's 12-year Kenya village trial, Finland's 2,000-unemployed citizen trial, Stockton SEED project, testing work disincentive hypotheses, mental health improvements, and political policy feasibility.",
                "reason": "Examines the largest and most consequential ongoing randomized field experiments in modern welfare economics."
            },
            {
                "id": 17,
                "title": "The Replication Crisis: Why 50% of Psychology's Classic Experiments Can't Be Repeated",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "deep_dive",
                "slug": "replication_crisis_open_science_collaboration_p_hacking_file_drawer",
                "question": "What happened when 270 researchers attempted to replicate 100 famous psychology papers and discovered that over half failed to produce the original results?",
                "focus": "Brian Nosek's Open Science Collaboration, p-hacking, publication bias ('file drawer problem'), small sample sizes, academic incentives rewarding sensational headlines over replicable rigor, and the pre-registration revolution.",
                "reason": "A critical, honest reckoning with the foundational integrity of the social sciences and the movement toward open, reproducible science."
            },
            {
                "id": 18,
                "title": "Digital Civic Sandboxes: Large-Scale Social Experiments on Reddit and Twitter",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "future_predictions",
                "slug": "reddit_r_place_digital_civic_sandboxes_emergent_governance",
                "question": "How did a blank 1,000x1,000 pixel canvas where each user could place one colored pixel every five minutes spawn global alliances, wars, and art?",
                "focus": "Reddit's r/place social experiment (2017 & 2022), emergent self-organizing communities, defense pacts, diplomatic treaties between subreddits, automated bots vs human labor, and digital sociopolitical simulation.",
                "reason": "Highlights the modern digital sandbox frontier where millions of anonymous users demonstrate collective emergent governance in real time."
            },
            {
                "id": 19,
                "title": "The Cost of a Clinical Social Trial: The Economics of Field Experimentation",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "cost_breakdown",
                "slug": "economics_of_field_experimentation_randomized_trials_budgets",
                "question": "Why does a rigorous multi-year randomized social science field trial in 50 villages cost $5 million, and where does every research dollar go?",
                "focus": "Enumerator field staff payroll, biometric tracking hardware, attrition mitigation incentives, survey design translation, data auditing pipelines, and peer review publishing economics.",
                "reason": "Detailed financial and operational breakdown of large-scale international field experimentation in development economics."
            },
            {
                "id": 20,
                "title": "The Masterclass on Experimental Design: Crafting an Airtight Social Science Experiment",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "masterclass",
                "slug": "masterclass_experimental_design_rct_internal_external_validity",
                "question": "How does an experimental sociologist design a study that isolates causal mechanisms while ensuring absolute ethical compliance and high statistical power?",
                "focus": "Balancing internal validity (lab control) vs external validity (real-world generalizability), pre-registration protocols (OSF), power calculations determining sample size, double-blind confederate protocols, and managing post-experiment debriefing ethics.",
                "reason": "The definitive masterclass on experimental methodology, statistical rigor, and research ethics in the behavioral sciences."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Sam Altman Universal Basic Income Study Results: $1,000/Month Given to 3,000 Americans",
                "trend_score": "High Global Velocity (9.6/10)",
                "angle": "case_study",
                "slug": "sam_altman_ubi_study_results_open_research_unconditional_cash",
                "why_trending": "Massive global media coverage as OpenResearch releases the highly anticipated three-year randomized trial data on guaranteed income, employment, and health.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "The TikTok Blind Date Social Experiment: Millions Watching Strangers Meet Live in London",
                "trend_score": "Rapid Surge (9.5/10)",
                "angle": "field_investigation",
                "slug": "tiktok_blind_date_live_social_experiment_viral_dating",
                "why_trending": "Creators live-streaming unscripted public blind dates in restaurants, generating tens of millions of views and intense debates on modern dating etiquette.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "The 'NPC' Live Stream Phenomenon: Bizarre Human Compliance for Digital Pennies",
                "trend_score": "Viral Peak (9.3/10)",
                "angle": "deep_dive",
                "slug": "npc_livestream_phenomenon_behavioral_compliance_monetization",
                "why_trending": "Sociologists dissecting the viral trend of creators reciting repetitive robotic catchphrases when gifted digital stickers, exploring performative micro-labor.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "The 30-Day Smartphone Detox Experiment: Brain Scans Before and After Going Cold Turkey",
                "trend_score": "Breakthrough Trend (9.1/10)",
                "angle": "case_study",
                "slug": "smartphone_detox_experiment_fmri_brain_scans_dopamine_reset",
                "why_trending": "High-engagement self-experimentation channels documenting fMRI brain scans showing gray matter and anxiety alterations after replacing smartphones with dumbphones.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "The YouTube 'Fake Prank' Crackdown: When Staged Social Experiments Cross Legal Lines",
                "trend_score": "High Velocity (8.9/10)",
                "angle": "investigative_report",
                "slug": "fake_pranks_social_experiments_legal_prosecution_youtube",
                "why_trending": "Criminal convictions and YouTube policy bans following reckless 'social experiment' creators staging fake bank robberies and assaults for viral views.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "The 100-Hour No Sleep Hallucination Experiment: Peter Tripp's 1959 Broadcast Nightmare",
                "trend_score": "Emerging Niche (8.8/10)",
                "angle": "historical_evolution",
                "slug": "peter_tripp_sleep_deprivation_experiment_radio_broadcast_psychosis",
                "why_trending": "Horrifying medical history rediscovery of a radio DJ broadcasting for 201 consecutive hours from Times Square, suffering permanent personality-altering psychosis.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The $10 Million Psychology Lawsuit: The Real Cost of Unethical University Research",
                "trend_score": "Steady Long-Tail (8.5/10)",
                "angle": "cost_breakdown",
                "slug": "psychology_lawsuits_unethical_research_legal_settlements",
                "why_trending": "Financial analysis of historic and modern legal settlements paid out by universities and state hospitals to surviving subjects of non-consensual behavioral studies.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "173_family_history": {
        "id": "173",
        "slug": "family_history",
        "title": "Family History",
        "category": "Historical_People_Cultures",
        "audience": "Genealogists, Family Historians, Archival Sleuths, Genetic DNA Tracing Enthusiasts, Heritage Preservationists (Global)",
        "progression": [
            ("Tier 1: Vital Statistics Registries, Census Records & Family Tree Mapping (Beginner / Scratch)",
             "Civil registration of births, marriages, and deaths (BMD), decennial census records analysis, church baptism and burial registries, pedigree chart construction, and overcoming common surname pitfalls."),
            ("Tier 2: Autosomal DNA Matching, Centimorgan Triangulation & Genetic Genealogy (Intermediate)",
             "Autosomal DNA testing mechanics (AncestryDNA, 23andMe), Centimorgan (cM) shared segment analysis, the Shared cM Project probability tables, Y-DNA paternal haplogroups, and mitochondrial mtDNA maternal lineages."),
            ("Tier 3: Paleography (Deciphering Old Scripts), Land Deeds & Immigrant Ship Manifests (Upper Intermediate)",
             "Deciphering Secretary hand and Kurrentschrift historic scripts, Ellis Island and Castle Garden ship passenger manifests, probate wills and estate land deeds, and naturalization petitions."),
            ("Tier 4: Breaking 200-Year Brick Walls, Resolving Non-Paternity Events (NPE) & Preserving Oral Family Archives (Advanced / Masterclass)",
             "Investigative genetic genealogy solving 19th-century brick walls and adoption mysteries, managing sensitive Non-Paternity Events (NPE) and family secrets, archival digital digitization standards, and writing enduring family histories.")
        ],
        "flagship": {
            "title": "The Golden State Killer: How Investigative Genetic Genealogy Solved a 40-Year Cold Case",
            "angle": "case_study",
            "slug": "173_family_history_case_study_the_golden_state_killer"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Golden State Killer: How Investigative Genetic Genealogy Solved a 40-Year Cold Case",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "golden_state_killer_investigative_genetic_genealogy_gedmatch",
                "question": "How did genealogist Barbara Rae-Venter upload crime scene DNA to open-source genealogy databases to track down a serial killer using distant third cousins?",
                "focus": "GEDmatch public database search, building multi-branch descendancy trees back to 19th-century great-great-grandparents, centimorgan segment triangulation, eliminating branches, and the arrest of Joseph DeAngelo.",
                "reason": "Crucial foundational episode exploring the historic watershed that transformed family history research into a revolutionary forensic investigative tool."
            },
            {
                "id": 2,
                "title": "The Census Detective: How to Extract Secrets from 100-Year-Old Hand-Written Sheets",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "census_records_detective_analysis_72_year_privacy_rule",
                "question": "Why does the US keep federal census records locked in a vault for exactly 72 years, and what can a single 1930 line reveal about your ancestors?",
                "focus": "The 72-Year Privacy Rule, analyzing occupation columns, citizenship status, home ownership vs mortgages, radio ownership, literacy, and spotting enumerator spelling errors.",
                "reason": "Establishes the core primary record skill set required to build an unbroken documentary lineage through the 19th and 20th centuries."
            },
            {
                "id": 3,
                "title": "Autosomal DNA vs Y-DNA vs mtDNA: Which Genetic Test Actually Solves Your Mystery?",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "autosomal_vs_ydna_vs_mtdna_genetic_genealogy_testing",
                "question": "Why is autosomal DNA useless beyond 5 to 7 generations, while Y-DNA can trace your surname back 500 years to medieval clan chiefs?",
                "focus": "Autosomal chromosome recombination and halving every generation, Y-chromosome passing virtually unchanged father-to-son, mitochondrial DNA maternal lineage tracking, and selecting the right testing platform.",
                "reason": "Deconstructs the genetic inheritance mechanics separating short-range autosomal matching from deep-time paternal and maternal haplogroups."
            },
            {
                "id": 4,
                "title": "The Shared cM Project: Decoding the Math of Genetic Cousins",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "shared_cm_project_blaine_bettinger_centimorgan_probabilities",
                "question": "When Ancestry says you share 215 centimorgans with a total stranger, are they a second cousin, a first cousin twice removed, or a half-aunt?",
                "focus": "Blaine Bettinger's Shared cM Project, probability relationship histograms, endogamy distortions (Jewish, Amish, and island populations inflating shared DNA), and mapping segment overlaps.",
                "reason": "Masterclass on the statistical and biological math of centimorgan analysis used to identify unknown biological ancestors."
            },
            {
                "id": 5,
                "title": "The Ellis Island Myth: The Names Were Never Changed at the Docks",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "ellis_island_name_change_myth_ship_manifest_reality",
                "question": "Did immigration inspectors really butcher foreign surnames at Ellis Island, or did your ancestors choose to change their own names years later?",
                "focus": "Inspectors checking passengers against shipping line manifests created in Europe, lack of power to change legal documents at the port, court naturalization name petitions, and cultural assimilation pressure.",
                "reason": "Debunks family history's most persistent and widespread myth using primary immigration and maritime documentation."
            },
            {
                "id": 6,
                "title": "Breaking the Brick Wall: Strategies for Finding the Father of an 1850s Ancestor",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "breaking_genealogy_brick_walls_fan_club_methodology",
                "question": "What do you do when the trail goes completely cold and an ancestor seems to have dropped out of thin air with no birth certificate?",
                "focus": "Elizabeth Shown Mills' FAN Club methodology (Friends, Associates, Neighbors), collateral research, county courthouse probate court dockets, tax lists tracking missing years, and land platting.",
                "reason": "Actionable, rigorous investigative playbook teaching the universal methodology used by professional genealogists to bust dead-end brick walls."
            },
            {
                "id": 7,
                "title": "Paleography: How to Decipher 17th-Century Handwriting That Looks Like Hieroglyphs",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "step_by_step",
                "slug": "paleography_deciphering_old_handwriting_secretary_hand_kurrent",
                "question": "How do researchers read cursive wills and parish records written in Secretary Hand, Old English script, or German Kurrent?",
                "focus": "Historical ligature forms, long 's' (looks like an f), thorn symbol (Y = th, origin of 'Ye Olde'), archaic contractions, reading letter-by-letter with a tracing alphabet, and digital contrast enhancement.",
                "reason": "Essential practical linguistic skill unlocking primary documents from the 16th to 18th centuries."
            },
            {
                "id": 8,
                "title": "The Non-Paternity Event (NPE): Navigating DNA Discoveries That Shatter Family Trees",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "non_paternity_event_npe_dna_secrets_family_identity",
                "question": "What happens when a holiday DNA test reveals that the father who raised you—or your grandfather—is not your biological relative?",
                "focus": "Prevalence of NPEs in genetic genealogy (1-3% per generation), late-discovery adoptions, donor conceived individuals, emotional shock and ethical etiquette in contacting biological kin, and genetic counseling.",
                "reason": "Compassionate, clinical navigation of the profound personal and familial identity crises unleashed by consumer DNA testing."
            },
            {
                "id": 9,
                "title": "The WPA Slave Narratives and Freedmen's Bureau: Overcoming the 1870 African American Brick Wall",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "african_american_genealogy_freedmens_bureau_1870_brick_wall",
                "question": "How do Black genealogists trace enslaved ancestors back before the 1870 census, when enslaved people were listed only as anonymous tick marks on slave schedules?",
                "focus": "Freedmen's Bureau labor contracts and bank records, plantation account ledgers, wills and probate estate sales listing names and ages, slave manifests, and combining DNA clusters with local white family papers.",
                "reason": "Deep dive into the specialized methodologies and vital historical archives required to reconstruct African American ancestry past slavery."
            },
            {
                "id": 10,
                "title": "Church Parish Registers: Tracking Ancestors Back to the 1500s in European Villages",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "church_parish_registers_baptisms_marriages_burials_europe",
                "question": "Before governments kept birth certificates, how did village parish priests in England, Germany, and Italy keep records that survived for 500 years?",
                "focus": "Council of Trent (1563) mandating Catholic parish registers, English Parish Registers (1538 Henry VIII mandate), Latin terminology decoders, churchwardens' accounts, and microfilms in salt mine vaults.",
                "reason": "Examines the foundational religious record infrastructure that allows family historians to push genealogies back to the Tudor era."
            },
            {
                "id": 11,
                "title": "Land Deeds and Metes & Bounds: Mapping Ancestral Farms from 'White Oak to a Pile of Stones'",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "field_investigation",
                "slug": "land_deeds_metes_and_bounds_historical_platting_chains_rods",
                "question": "How can an 18th-century property description measured in surveying chains and boundary trees pinpoint your ancestor's exact log cabin on modern Google Earth?",
                "focus": "Metes and bounds surveying vs the Public Land Survey System (township/range/section grid), deed mapper software, following property chains of title back to original crown grants, and historical neighbors.",
                "reason": "Connects historical legal land surveying documents with modern spatial GIS cartography to physically locate ancestral homesteads."
            },
            {
                "id": 12,
                "title": "Military Service Records: Pension Files That Contain Intimate Family Letters and Bible Pages",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "case_study",
                "slug": "military_pension_files_revolutionary_war_civil_war_national_archives",
                "question": "Why are Revolutionary War and Civil War widow pension applications the richest goldmines in genealogical research?",
                "focus": "National Archives (NARA) Record Group 15, physical family Bible birth pages torn out and submitted as proof of marriage, sworn eyewitness neighbor affidavits, casualty surgeon notes, and bounty land warrants.",
                "reason": "Reveals the intimate, handwritten personal treasures preserved inside federal military pension dossiers."
            },
            {
                "id": 13,
                "title": "Oral History Interviews: How to Record Your Grandparents Before Their Stories Are Lost Forever",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "step_by_step",
                "slug": "oral_history_interviewing_grandparents_questions_archival_audio",
                "question": "What questions should you ask an aging elder to unlock vivid sensory memories rather than polite generic answers?",
                "focus": "StoryCorps interview techniques, open-ended sensory prompts ('what did your childhood kitchen smell like?'), using old photograph albums as memory triggers, high-resolution audio recording standards, and archiving transcripts.",
                "reason": "Actionable, urgent guide teaching creators and families how to professionally capture and preserve living family voices before it is too late."
            },
            {
                "id": 14,
                "title": "The Orphan Train Movement: Finding the Lost Roots of 250,000 Relocated Children",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "historical_evolution",
                "slug": "orphan_train_movement_charles_loring_brace_childrens_aid_society",
                "question": "How did a massive 19th-century social experiment take street children from New York tenements and place them on trains to farming families across the American West?",
                "focus": "Charles Loring Brace and the Children's Aid Society (1854-1929), train station inspection line lineups, Catholic New York Foundling Hospital placement books, changed names and lost siblings, and genetic reconnection.",
                "reason": "Explores a poignant, massive demographic migration chapter affecting millions of living American descendants."
            },
            {
                "id": 15,
                "title": "Coroner Inquests and Asylums: Uncovering the Dark and Tragic Chapters in Your Tree",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "investigative_report",
                "slug": "coroner_inquests_asylum_records_uncovering_tragic_ancestors",
                "question": "How do genealogists handle finding ancestral murders, suicides, workhouse pauper graves, and psychiatric institutionalizations?",
                "focus": "Coroner jury inquest transcripts, historical asylum patient case books, almshouse intake registers, sensational historical newspaper archives (Chronicling America), and ethical family narrative framing.",
                "reason": "Provides the historical tools and empathetic maturity required to research and document profound family tragedies."
            },
            {
                "id": 16,
                "title": "Endogamy and Pedigree Collapse: Why We All Have Fewer Ancestors Than Math Suggests",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "deep_dive",
                "slug": "pedigree_collapse_endogamy_charlemagne_common_ancestor",
                "question": "If you double your ancestors every generation back 40 generations, you get 1 trillion ancestors—more people than ever lived. Where does the math break?",
                "focus": "Pedigree collapse (ahnenschwund), royal inbreeding (Charles II of Spain), the Most Recent Common Ancestor (MRCA), why anyone of European descent is related to Charlemagne, and genetic implications of cousin marriage.",
                "reason": "Mind-bending mathematical and genetic analysis illustrating how all human family trees fold inward into a tightly knit interconnected web."
            },
            {
                "id": 17,
                "title": "Preserving Family Photos and Heirlooms: Archival Acid-Free Boxes and 1,200 DPI Scans",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "field_investigation",
                "slug": "preserving_family_photos_archival_scanning_daguerreotypes_tintypes",
                "question": "How do you preserve 150-year-old tintypes, fragile glass plate negatives, and crumbling paper scrapbooks for another two centuries?",
                "focus": "Daguerreotypes, ambrotypes, and albumen prints identification; avoiding sticky magnetic photo albums; archival acid-free lignin-free storage sleeves; flatbed 1,200 DPI TIFF master scanning; and offsite redundant cloud preservation.",
                "reason": "Practical archival conservation masterclass protecting precious physical family relics from environmental decay and loss."
            },
            {
                "id": 18,
                "title": "AI in Genealogy: Transcribing Cursive, Enhancing Blurry Faces, and Clustering DNA",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "future_predictions",
                "slug": "ai_in_genealogy_transcribing_handwritten_census_neural_networks",
                "question": "How are neural networks reading centuries of uncataloged handwritten cursive records that no human eye had time to index?",
                "focus": "Handwritten Text Recognition (HTR) on FamilySearch archives, AI facial clustering matching unknown tintype portraits, automated tree hint validation algorithms, and synthetic video animation of ancestor photos (Deep Nostalgia).",
                "reason": "Evaluates the cutting-edge technological revolution accelerating genealogical discovery and archival digitization."
            },
            {
                "id": 19,
                "title": "The Multi-Billion Dollar Family History Industry: The Economics of Ancestry and 23andMe",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "cost_breakdown",
                "slug": "genealogy_industry_economics_ancestry_private_equity_dna_banks",
                "question": "Why did private equity firms buy Ancestry.com for $4.7 billion, and how do consumer DNA databases monetize genetic data?",
                "focus": "Subscription recurring revenue models, DNA testing microarray chip manufacturing costs, pharmaceutical research partnerships (GSK using 23andMe genetic databases), and privacy regulatory scrutiny.",
                "reason": "Detailed business and data privacy breakdown of the commercial genetic and genealogical testing industry."
            },
            {
                "id": 20,
                "title": "The Masterclass on Writing a Family History Book: From Dry Pedigree to Compelling Narrative",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "masterclass",
                "slug": "masterclass_writing_family_history_narrative_nonfiction_memoir",
                "question": "How do you take names and dates on a chart and turn them into an unputdownable narrative non-fiction book that your family will treasure for generations?",
                "focus": "Weaving social history context around individual lives, handling historical trauma and secrets ethically, source citation standards (Board for Certification of Genealogists), photographic layout, and self-publishing archival hardcover editions.",
                "reason": "The definitive masterclass on transforming genealogical research into enduring literary historical heirlooms."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The 1950 US Census Release: Millions Searching the Records of Living Parents and Grandparents",
                "trend_score": "High Global Velocity (9.6/10)",
                "angle": "field_investigation",
                "slug": "1950_census_release_national_archives_ai_handwriting_indexing",
                "why_trending": "Massive public surge as the 72-year rule unlocks the 1950 US federal census, allowing millions to find childhood records of living family members.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "The Fall of 23andMe: Financial Collapse, Privacy Panic, and What Happens to Your DNA",
                "trend_score": "Rapid Surge (9.5/10)",
                "angle": "investigative_report",
                "slug": "23andme_financial_collapse_dna_privacy_data_sale_panic",
                "why_trending": "Tech and consumer frenzy following 23andMe's stock collapse and board resignations, sparking widespread panic over who could buy genetic databases in bankruptcy.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "Unknown Soldier Identified: How Forensic Genealogy Reunited WWI Heroes with Their Names",
                "trend_score": "Viral Peak (9.3/10)",
                "angle": "case_study",
                "slug": "unknown_soldier_wwi_identified_mitochondrial_dna_military",
                "why_trending": "Heartwarming viral stories of military defense POW/MIA agencies using advanced skeletal DNA extraction to return names to soldiers buried in anonymous graves for a century.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "Restoring Water-Damaged Family Photos with AI: The Step-by-Step Digital Rescue",
                "trend_score": "Breakthrough Trend (9.1/10)",
                "angle": "step_by_step",
                "slug": "restoring_water_damaged_family_photos_photoshop_ai_inpainting",
                "why_trending": "Viral tutorials showcasing generative AI inpainting and manual Photoshop healing brushes rescuing torn, faded, and flood-damaged 19th-century family heirlooms.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "The 'Switch at Birth' Discovery: Two 70-Year-Old Women Uncovering a Hospital Blunder with DNA",
                "trend_score": "High Velocity (8.9/10)",
                "angle": "case_study",
                "slug": "switched_at_birth_dna_discovery_hospital_nursery_blunders",
                "why_trending": "Sensational real-life investigations of elderly individuals discovering through commercial DNA tests that they were handed to the wrong parents in 1950s hospital nurseries.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "Tracing Royal Ancestry: Why Almost Everyone with European Blood is Related to Royalty",
                "trend_score": "Emerging Niche (8.8/10)",
                "angle": "deep_dive",
                "slug": "tracing_royal_ancestry_gateway_ancestors_charlemagne_math",
                "why_trending": "Mathematical and genealogical breakdowns showing how 'gateway ancestors' connect ordinary colonial settlers back to Plantagenet kings and European royalty.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The $10,000 Professional Genealogy Search: Inside the High-End Heir Hunting Industry",
                "trend_score": "Steady Long-Tail (8.5/10)",
                "angle": "cost_breakdown",
                "slug": "heir_hunting_industry_probate_genealogy_costs_unclaimed_estates",
                "why_trending": "Fascinating financial look into probate genealogists tracking down missing distant relatives to claim millions in intestate inheritance funds.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "174_aging_generations": {
        "id": "174",
        "slug": "aging_generations",
        "title": "Aging & Generations",
        "category": "People_Communities",
        "audience": "Gerontologists, Generational Cohort Analysts, Demographic Economists, Elder Care Advocates, Cultural Sociologists (Global)",
        "progression": [
            ("Tier 1: Biological vs Chronological Aging, Cellular Senescence & Global Demographic Inversion (Beginner / Scratch)",
             "Chronological vs epigenetic biological age (Horvath clock), Hayflick limit and telomere attrition, cellular senescence (SASP secretions), and the global demographic inverted pyramid (declining fertility + rising longevity)."),
            ("Tier 2: Generational Cohort Dynamics (Baby Boomers, Gen X, Millennials, Gen Z, Gen Alpha) (Intermediate)",
             "Strauss-Howe generational theory (Fourth Turning), economic asset divides between Boomers and Millennials, formative technology milestones shaping Gen Z, and generational culture clashes."),
            ("Tier 3: The Blue Zones (Diet, Community, Ikigai Centenarian Lifestyles) & Ageism in Modern Societies (Upper Intermediate)",
             "Dan Buettner's Blue Zones (Okinawa, Sardinia, Nicoya, Ikaria, Loma Linda), plant-slant diets, natural daily movement, social Moai support circles, purposeful aging (Ikigai), and deconstructing systemic ageism in hiring."),
            ("Tier 4: The Silver Tsunami Macroeconomics, Long-Term Elder Care Infrastructure & Intergenerational Wealth Transfers (Advanced / Masterclass)",
             "Long-term memory care and dementia economics, state pension solvency crises, Scandinavian universal social care models vs US nursing home private equity buyouts, and the $84 trillion intergenerational wealth transfer.")
        ],
        "flagship": {
            "title": "The Blue Zones Secret: Why Centenarians in Okinawa and Sardinia Live Past 100 with Zero Disease",
            "angle": "case_study",
            "slug": "174_aging_generations_case_study_the_blue_zones_secret"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Blue Zones Secret: Why Centenarians in Okinawa and Sardinia Live Past 100 with Zero Disease",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "blue_zones_centenarians_okinawa_sardinia_longevity_secrets",
                "question": "Why do people in five isolated regions across the world routinely live past 100 with one-fifth the rate of cardiovascular disease, dementia, and cancer?",
                "focus": "Dan Buettner's National Geographic research, the Power 9 principles (natural movement, plant-slant diet, 80% rule Hara Hachi Bu, downshifting stress, Moai social circles, and Ikigai purpose).",
                "reason": "Crucial foundational episode exploring the gold standard lifestyle and environmental factors that promote extreme healthy human longevity."
            },
            {
                "id": 2,
                "title": "Biological Age vs Chronological Age: How Old Are Your Cells Really?",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "biological_vs_chronological_age_horvath_epigenetic_clock",
                "question": "Why can two 50-year-olds have cellular biological health that looks like 35 in one and 70 in the other?",
                "focus": "Steve Horvath's epigenetic DNA methylation clock, telomere length decay, grip strength and VO2 max as longevity biomarkers, and lifestyle interventions that reverse biological age.",
                "reason": "Establishes the scientific distinction between calendar years lived and cellular physical health deterioration."
            },
            {
                "id": 3,
                "title": "The Hayflick Limit: Why Human Cells Refuse to Divide More Than 50 Times",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "hayflick_limit_leonard_hayflick_telomeres_cellular_senescence",
                "question": "How did Leonard Hayflick destroy the scientific myth that cells are immortal, proving that our bodies carry a built-in cellular death countdown clock?",
                "focus": "Telomere attrition at each cell replication cycle, end-replication problem of DNA polymerase, telomerase enzymes in cancer cells, cellular senescence, and the theoretical human lifespan ceiling (~120 years).",
                "reason": "Masterclass on the fundamental biological molecular limits that govern human mortality."
            },
            {
                "id": 4,
                "title": "The Global Demographic Inversion: The Silver Tsunami and the Death of the Pyramid",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "demographic_inversion_silver_tsunami_inverted_population_pyramid",
                "question": "What happens to a civilization when there are more people wearing adult diapers than baby diapers in Japan, Italy, and South Korea?",
                "focus": "Inverted population pyramids, declining fertility rates colliding with expanding elderly cohorts, shrinking working-age tax bases, elder care dependency ratios, and pension system solvency.",
                "reason": "Deconstructs the most profound macroeconomic and demographic transformation reshaping the 21st-century global economy."
            },
            {
                "id": 5,
                "title": "Generational Theory: The Strauss-Howe 'Fourth Turning' Cycle of History",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "strauss_howe_generational_theory_fourth_turning_cycles",
                "question": "Do historical epochs really follow an 80-year four-phase cycle driven by predictable generational archetypes (Prophet, Nomad, Hero, Artist)?",
                "focus": "The High, the Awakening, the Unraveling, and the Crisis (Fourth Turning); Baby Boomers as idealist Prophets, Gen X as pragmatic Nomads, Millennials as civic Heroes; and critical sociological evaluations.",
                "reason": "Examines the celebrated and controversial generational framework used by political strategists and cultural historians to interpret cyclical crises."
            },
            {
                "id": 6,
                "title": "Boomers vs Millennials: The True Wealth Divide Between Generations",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "boomers_vs_millennials_wealth_divide_housing_education_debt",
                "question": "Did Baby Boomers get lucky with a once-in-history economic boom, or are Millennials just spending too much on avocado toast?",
                "focus": "Federal Reserve wealth distribution data (Boomers holding 50% of US wealth vs Millennials holding under 10% at the same age), home-price-to-income ratios, student loan debt loads, and economic mobility hurdles.",
                "reason": "A data-driven, objective financial comparison untangling the economic realities separating generations."
            },
            {
                "id": 7,
                "title": "Ikigai: The Japanese Philosophy of Purpose That Keeps Elders Healthy at 100",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "cultural_traditions",
                "slug": "ikigai_japanese_philosophy_purpose_longevity_retirement",
                "question": "Why is there no word for 'retirement' in the traditional Okinawan dialect, and how does having a morning purpose lower cardiovascular inflammation?",
                "focus": "The intersection of what you love, what you are good at, what the world needs, and what you can get paid for; staying active in community gardens; social engagement; and mental cognitive health.",
                "reason": "Explores the psychological and philosophical factors linking daily purposeful activity to reduced mortality in older adults."
            },
            {
                "id": 8,
                "title": "Ageism: The Last Socially Acceptable Prejudice in Modern Society",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "systemic_critique",
                "slug": "ageism_in_workplace_hiring_algorithms_cultural_devaluation",
                "question": "Why are workers over 50 quietly pushed out of corporate jobs despite possessing decades of invaluable institutional wisdom?",
                "focus": "Workplace tech stereotyping, resume age screening algorithms, cultural youth obsession in media advertising, Becca Levy's Yale research showing negative aging beliefs take 7.5 years off life, and fighting internal ageism.",
                "reason": "Confronts the pervasive social stigma and corporate discrimination that devalues experienced older adults."
            },
            {
                "id": 9,
                "title": "Dementia and Alzheimer's: The Molecular Mystery Destroying Millions of Minds",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "alzheimers_dementia_amyloid_plaques_tau_tangles_caregiving",
                "question": "What actually happens to memories, personality, and brain tissue when amyloid plaques and tau tangles spread across the hippocampus?",
                "focus": "The amyloid cascade hypothesis controversies, tau neurofibrillary tangles, vascular dementia contributions, lecanemab antibody therapies, and the staggering emotional and physical toll on unpaid family caregivers.",
                "reason": "Crucial clinical and compassionate deep dive into the primary neurological illness threatening aging populations."
            },
            {
                "id": 10,
                "title": "Nursing Homes vs Aging in Place: The Scandinavia Model vs American Private Equity",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "nursing_homes_vs_aging_in_place_danish_elder_care_model",
                "question": "Why does Denmark ban the construction of traditional institutional nursing homes, prioritizing universal municipal in-home care instead?",
                "focus": "The Danish Aging in Place revolution, private equity ownership of US nursing homes linked to higher mortality rates, memory care village architectures (De Hogeweyk in Netherlands), and dignity in elder care.",
                "reason": "Compares global institutional elder care models, contrasting profit-driven private facilities with dignified community-based municipal care."
            },
            {
                "id": 11,
                "title": "Gen X: The Forgotten Middle Child Generation of Latchkey Kids and Corporate Burden",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "case_study",
                "slug": "gen_x_forgotten_generation_latchkey_kids_sandwich_generation",
                "question": "Why does the generation born between 1965 and 1980 rarely make the headlines, despite holding the highest leadership roles in business and politics?",
                "focus": "The latchkey kid self-reliance culture, MTV cynicism, navigating the economic sandwich generation (caring for elderly Boomer parents while supporting Gen Z children), and workplace pragmatic independence.",
                "reason": "A rich cultural and sociological portrait of the overlooked demographic cohort bridging the analogue and digital eras."
            },
            {
                "id": 12,
                "title": "The Sarcopenia Crisis: Why Muscle Mass is the Greatest Biomarker of Longevity",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "sarcopenia_muscle_loss_aging_resistance_training_fall_prevention",
                "question": "Why is an 80-year-old slipping and breaking a hip often a fatal event, and how does lifting weights in your 40s protect you 40 years later?",
                "focus": "Age-related muscle mass loss (sarcopenia 3-8% per decade after 30), metabolic glucose sink impairment, fall mechanics, bone mineral density resistance training, and dietary protein distribution in older adults.",
                "reason": "Essential physiological guide highlighting strength training and muscle preservation as vital life-saving medicine for healthy aging."
            },
            {
                "id": 13,
                "title": "Generation Z in the Workplace: Challenging Hustle Culture and Redefining Professionalism",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "comparative_analysis",
                "slug": "gen_z_in_the_workplace_boundaries_remote_work_culture_clashes",
                "question": "Why are corporate managers struggling to understand younger workers who prioritize mental health boundaries and refuse unpaid overtime?",
                "focus": "Digital native intuition, skepticism of corporate loyalty after witnessing parents' layoffs, demands for salary transparency, preference for asynchronous communication, and bridging intergenerational workplace culture gaps.",
                "reason": "Analyzes the dramatic cultural and behavioral friction occurring as the first fully digital generation enters the global corporate workforce."
            },
            {
                "id": 14,
                "title": "The $84 Trillion Great Wealth Transfer: The Largest Generational Inheritance in History",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "investigative_report",
                "slug": "great_wealth_transfer_84_trillion_boomer_inheritance_inequality",
                "question": "What happens to the global economy when Baby Boomers pass tens of trillions of dollars in real estate, stocks, and family businesses down over the next 20 years?",
                "focus": "Cerulli Associates estimates, estate tax planning, unequal wealth concentration among top 10% heirs multiplying national wealth inequality, philanthropic surges, and changing real estate market patterns.",
                "reason": "Examines the unprecedented generational financial tsunami set to reshape banking, luxury real estate, and wealth inequality over the coming two decades."
            },
            {
                "id": 15,
                "title": "Social Security and Pension Solvency: Can the State Afford Millions of 90-Year-Olds?",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "deep_dive",
                "slug": "social_security_pension_solvency_retirement_age_reforms",
                "question": "When retirement was invented in 1889, the retirement age was 65 and life expectancy was 45. What happens when retirement lasts 30 years?",
                "focus": "Bismarck's original German pension model, the pay-as-you-go funding trap, the US Social Security Trust Fund depletion timelines, French pension strikes over retirement age increases, and structural sovereign reform options.",
                "reason": "Directly confronts the mathematical and political crisis facing national retirement entitlement programs worldwide."
            },
            {
                "id": 16,
                "title": "Centenarians Re-Examined: Super-Agers and the Genetic Protection Against Cancer and Heart Disease",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "case_study",
                "slug": "super_agers_centenarians_genetic_variants_apoe_protection",
                "question": "Why do some 105-year-olds smoke and eat bacon every day and still show the arteries and brain volumes of 50-year-olds?",
                "focus": "SuperAger brain autopsies, protective genetic variants (APOE e2 vs e4, CETP longevity alleles, FOXO3 gene), compression of morbidity (staying completely healthy until the final months of life), and centenarian genetic sequencing.",
                "reason": "Investigates the extraordinary genetic biology of human outliers who achieve spontaneous natural resistance to chronic degenerative disease."
            },
            {
                "id": 17,
                "title": "Generation Alpha: The First iPad-Native Babies and the Future of Human Cognition",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "future_predictions",
                "slug": "generation_alpha_ipad_native_infants_ai_education_cognition",
                "question": "What happens to childhood brain architecture when infants swipe touchscreens before learning to speak full sentences?",
                "focus": "Mark McCrindle's Generation Alpha coining (children born 2010-2024), AI-powered adaptive tutoring from toddlerhood, visual-first literacy, the decline of physical book reading, and predicted societal impacts by 2040.",
                "reason": "Foresight analysis exploring the developmental and cognitive trajectory of humanity's youngest, technology-immersed generation."
            },
            {
                "id": 18,
                "title": "Dying with Dignity: Palliative Care, Hospice, and the Right to Die Movement",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "philosophical_perspectives",
                "slug": "dying_with_dignity_palliative_care_medical_aid_in_dying_ethics",
                "question": "Why does modern medicine often prolong the painful process of dying rather than maximizing comfort and human connection in final weeks?",
                "focus": "Atul Gawande's Being Mortal, palliative hospice care vs futile aggressive ICU interventions, Medical Aid in Dying (MAID) legal frameworks worldwide, advance healthcare directives, and honest conversations about mortality.",
                "reason": "A profound, compassionate medical and philosophical exploration of how humanity can restore dignity, autonomy, and peace to the final chapter of life."
            },
            {
                "id": 19,
                "title": "The $10,000-a-Month Memory Care Facility: The Staggering Financial Cost of Elder Care",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "cost_breakdown",
                "slug": "cost_of_elder_care_assisted_living_memory_care_medicaid_spenddown",
                "question": "Why does specialized dementia care cost over $120,000 a year, draining life savings until families are forced onto Medicaid spend-downs?",
                "focus": "Assisted living and memory care fee schedules, nurse staffing ratios, private equity real estate REIT ownership models, the Medicaid 'spend-down' asset liquidation trap, and long-term care insurance failures.",
                "reason": "Detailed economic teardown of the catastrophic elder care financial crisis confronting middle-class families."
            },
            {
                "id": 20,
                "title": "The Masterclass on Successful Aging: The Multi-Dimensional Framework for Lifelong Vitality",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "masterclass",
                "slug": "masterclass_successful_aging_rower_kahn_vitality_framework",
                "question": "How do elite gerontologists and longevity physicians design an actionable lifestyle blueprint that maximizes healthspan alongside lifespan?",
                "focus": "Rowe and Kahn's Successful Aging Model: Low probability of disease, High cognitive and physical capacity, and Active engagement with life; integrating cardiovascular zone-2 training, protein optimization, deep social networks, and cognitive reserve maintenance.",
                "reason": "The definitive masterclass synthesizing gerontology, preventive medicine, and sociology into a comprehensive blueprint for lifelong human flourishing."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Bryan Johnson's Project Blueprint: The $2 Million/Year Algorithm to Rejuvenate Human Organs",
                "trend_score": "High Global Velocity (9.6/10)",
                "angle": "case_study",
                "slug": "bryan_johnson_project_blueprint_anti_aging_protocol_reversal",
                "why_trending": "Massive viral fascination with tech entrepreneur Bryan Johnson's extreme daily protocol of 100+ supplements, biomarkers, and therapies claiming to reverse epigenetic age.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "The Blue Zones Docuseries Phenomenon: Why Viewers Are Tossing Out Steaks for Beans",
                "trend_score": "Rapid Surge (9.5/10)",
                "angle": "field_investigation",
                "slug": "blue_zones_netflix_docuseries_surge_plant_slant_beans",
                "why_trending": "Millions of global viewers revamping pantries following Dan Buettner's streaming documentary on centenarian diets and community lifestyle habits.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "The 'Sephora Kids' Trend: Why 10-Year-Old Gen Alpha Girls Are Obsessed with Anti-Aging Retinol",
                "trend_score": "Viral Peak (9.3/10)",
                "angle": "deep_dive",
                "slug": "sephora_kids_gen_alpha_skincare_drunkelephant_retinol_trend",
                "why_trending": "Heated cultural debates over pre-teens swarming beauty stores for expensive anti-aging skincare products, damaging skin barriers and reflecting TikTok beauty anxiety.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "The Death of the Starter Home: Why Boomers Refusing to Downsize is Freezing the Housing Market",
                "trend_score": "Breakthrough Trend (9.1/10)",
                "angle": "systemic_critique",
                "slug": "boomers_refusing_to_downsize_frozen_starter_home_market",
                "why_trending": "Real estate analytics revealing Baby Boomers are choosing to age in place in large 4-bedroom suburban homes, leaving younger families with zero inventory.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "Creatine for Brain Health in Aging: The Bodybuilding Powder Helping Protect Memory",
                "trend_score": "High Velocity (8.9/10)",
                "angle": "mechanisms_and_systems",
                "slug": "creatine_brain_health_aging_cognitive_protection_mitochondria",
                "why_trending": "Surge of clinical neurology trials showing everyday creatine monohydrate supplementation boosts cellular ATP in aging brains, improving memory and reducing mental fatigue.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "The Co-Housing Revolution: Senior Friends Buying Compounds to Grow Old Together Without Nursing Homes",
                "trend_score": "Emerging Niche (8.8/10)",
                "angle": "cultural_traditions",
                "slug": "senior_cohousing_revolution_friends_living_together_golden_girls",
                "why_trending": "Retirees pooling resources to build intentional cooperative neighborhoods, sharing communal meals and healthcare support while maintaining private living quarters.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The $50,000 Full-Body MRI Longevity Scan: Inside Prenuvo and the Boom in Pre-Symptomatic Detection",
                "trend_score": "Steady Long-Tail (8.5/10)",
                "angle": "cost_breakdown",
                "slug": "prenuvo_full_body_mri_scan_longevity_screening_costs",
                "why_trending": "Celebrities and longevity enthusiasts paying thousands for private preventive whole-body MRI scans, sparking debate over incidental findings and healthcare equity.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "175_childhood_history": {
        "id": "175",
        "slug": "childhood_history",
        "title": "Childhood History",
        "category": "Historical_People_Cultures",
        "audience": "Educational Historians, Child Psychologists, Pediatric Sociologists, Cultural Anthropologists, Parents (Global)",
        "progression": [
            ("Tier 1: The Invention of Childhood (Philippe Ariès), Infanticide and Swaddling in Antiquity (Beginner / Scratch)",
             "Philippe Ariès' Centuries of Childhood thesis, high infant mortality shaping emotional detachment, ancient and medieval swaddling practices, children as miniature adults, and apprentice systems."),
            ("Tier 2: Child Labor in the Industrial Revolution, Coal Breaker Boys & Factory Acts (Intermediate)",
             "Children in British textile mills and Appalachian coal breakers, Lewis Hine's investigative photography, the 1833 Factory Act, and the political fight for child labor eradication."),
            ("Tier 3: Compulsory Public Schooling, Play Theory (Froebel's Kindergarten), and Toy Industrialization (Upper Intermediate)",
             "Friedrich Fröbel's invention of kindergarten, compulsory education laws transforming children from economic assets into economic liabilities, the rise of mass toy manufacturing, and pediatric developmental milestones."),
            ("Tier 4: The Commercialization of the Child Consumer, Modern Helicopter/Snowplow Parenting & The Smartphone Generation (Advanced / Masterclass)",
             "The Saturday morning cartoon advertising explosion, shift to intensive hyper-vigilant parenting (helicopter/snowplow), children's independent mobility radius collapse, and evaluating the modern digital childhood.")
        ],
        "flagship": {
            "title": "The Coal Breaker Boys: The Child Labor Battles That Invented the Modern American Childhood",
            "angle": "case_study",
            "slug": "175_childhood_history_case_study_the_coal_breaker_boys"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Coal Breaker Boys: The Child Labor Battles That Invented the Modern American Childhood",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "coal_breaker_boys_lewis_hine_child_labor_reform",
                "question": "How did 8-year-old boys working 10-hour shifts sorting sharp slate from falling coal in Pennsylvania mines shock a nation into creating modern childhood?",
                "focus": "The physical horrors of anthracite coal breakers (shredded fingers, black lung), Lewis Hine's undercover investigative photography for the NCLC, political battles against factory owners, and the Keating-Owen Child Labor Act of 1916.",
                "reason": "Crucial foundational episode exploring the historic battle that legally separated childhood from the industrial wage labor market."
            },
            {
                "id": 2,
                "title": "The Invention of Childhood: When Children Stopped Being 'Miniature Adults'",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "invention_of_childhood_philippe_aries_centuries_of_childhood",
                "question": "Did the concept of childhood as a distinct, innocent, protected stage of human life exist before the 17th century?",
                "focus": "Philippe Ariès' landmark 1960 thesis, medieval art portraying babies with adult faces and muscles, children dressing in adult clothing and working by age seven, high infant mortality driving emotional distance, and the Enlightenment shift.",
                "reason": "Establishes the core historical historiography showing that 'childhood' is a modern cultural invention rather than a timeless biological given."
            },
            {
                "id": 3,
                "title": "Swaddling and Wet Nurses: How European Babies Were Raised for Centuries",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "swaddling_bands_wet_nurses_historical_infancy_practices",
                "question": "Why did parents bind infants tightly in linen swaddling bands like mummies for months, and why did wealthy mothers ship their babies away to wet nurses?",
                "focus": "Ancient beliefs that unswaddled infant limbs would grow crooked, hanging swaddled babies on wall pegs while working, the commercial wet nursing trade in 18th-century Paris, infant mortality rates in foster care, and Rousseau's Emile rebellion.",
                "reason": "Deconstructs the bizarre, foreign physical caretaking and infant feeding practices that dominated European civilization for 1,500 years."
            },
            {
                "id": 4,
                "title": "From Economic Asset to Economic Liability: The Price and Prejudice of the Modern Child",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "economic_transformation_of_childhood_viviana_zelizer_pricing_the_priceless_child",
                "question": "How did children transition in 50 years from being financial assets whose wages supported the family to emotionally priceless economic black holes?",
                "focus": "Sociologist Viviana Zelizer's Pricing the Priceless Child, calculating child labor value on farms vs modern $300,000 raising costs, changing legal compensation payouts for child deaths, and the shift from economic contributors to emotional centers of the home.",
                "reason": "Masterclass on the profound economic and cultural transformation of child value in industrial capitalism."
            },
            {
                "id": 5,
                "title": "The Invention of Kindergarten: Friedrich Fröbel's Garden of Children and Play Theory",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "invention_of_kindergarten_friedrich_froebel_play_gifts",
                "question": "Why was the idea that children should learn through playing with blocks and singing songs considered radical, dangerous, and even banned by Prussian authorities?",
                "focus": "Friedrich Fröbel's 1837 'Kindergarten' (children's garden), the 20 geometric 'Gifts' and 'Occupations' (blocks, origami, weaving) inspiring Frank Lloyd Wright, play as self-directed learning, and Margarethe Schurz bringing kindergarten to America.",
                "reason": "Examines the revolutionary pedagogical paradigm that validated play as the primary vehicle of human cognitive development."
            },
            {
                "id": 6,
                "title": "Spare the Rod: The Brutal History of Physical Discipline in Schools and Homes",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "history_of_corporal_punishment_birch_rod_paddle_spanking_bans",
                "question": "How did birch rods, canes, and wooden paddles move from mandatory classroom management tools to banned acts of child abuse?",
                "focus": "Puritan 'breaking the child's will' theology, standardized school corporal punishment ledgers, the 1979 Swedish world-first domestic spanking ban, modern neurological evidence on physical punishment, and evolving global legal prohibitions.",
                "reason": "Traces the dramatic shift in societal ethics and developmental psychology regarding the physical punishment of children."
            },
            {
                "id": 7,
                "title": "The Chimney Sweeps: The 'Climbing Boys' Trapped in Victorian Flues",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "chimney_sweeps_climbing_boys_victorian_child_labor_cancer",
                "question": "Why did London sweeps buy 4-year-old orphan boys to force them naked up pitch-black 9-inch brick flues, and how did it lead to the first recognized occupational cancer?",
                "focus": "Physical deformities of climbing boys, chimney sweeps' carcinoma (Percivall Pott's scrotal cancer discovery), chimney suffocation deaths, Lord Shaftesbury's 30-year legislative battle, and the 1875 licensing breakthrough.",
                "reason": "A harrowing historical investigation into the darkest, most dangerous exploitation of child labor in urban Victorian history."
            },
            {
                "id": 8,
                "title": "Compulsory Schooling: How Mass Education Replaced the Factory Floor",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "compulsory_schooling_horace_mann_industrial_factory_model",
                "question": "Why were ringing bells, age-segregated classrooms, and standardized tests modeled directly on the 19th-century industrial factory floor?",
                "focus": "Horace Mann's Prussian model adaptation in Massachusetts (1852), truant officers dragging children to school, educating an industrial workforce vs democratic citizenship, and the complete elimination of child labor through mandatory attendance.",
                "reason": "Reveals the historical architecture and underlying industrial motivations behind modern compulsory public education."
            },
            {
                "id": 9,
                "title": "The History of Toys: From Sticks and Mud to the Mass-Manufactured Plastic Boom",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "history_of_toys_handcrafted_wood_to_barbie_lego_plastic_boom",
                "question": "Before plastic molds and Saturday morning commercials, what did children across world history actually play with?",
                "focus": "Ancient Greek terracotta dolls with movable joints, Victorian tin soldiers, the post-WWII injection-molded plastic revolution (LEGO bricks, Barbie, G.I. Joe), and toys shifting from folk craft to a $100 billion commercial industry.",
                "reason": "Explores material culture and the industrial commercialization of play objects across centuries."
            },
            {
                "id": 10,
                "title": "The Children's Blizzard of 1888: The Prairie Disaster That Trapped Hundreds of Schoolchildren",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "childrens_blizzard_of_1888_prairie_schoolhouses_survival",
                "question": "What happened when an unseasonably warm 70°F day on the American Plains suddenly dropped to -40°F in three minutes as children walked home from one-room schoolhouses?",
                "focus": "The Schoolchildren's Blizzard of January 12, 1888; 235 deaths across Nebraska and Dakota; heroic young teachers tying children together with ropes (Minnie Freeman); lack of meteorological warning systems; and pioneer resilience.",
                "reason": "An unforgettable, dramatic historical tragedy illustrating the extreme environmental perils facing rural pioneer school children."
            },
            {
                "id": 11,
                "title": "The Collapse of the Roaming Radius: How Children Lost the Right to the Outdoors",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "field_investigation",
                "slug": "collapse_of_roaming_radius_children_independent_mobility_loss",
                "question": "Why did a great-grandfather roam six miles unsupervised across fields in 1919, while his great-grandson today is not permitted to cross the driveway alone?",
                "focus": "The four-generation Sheffield mobility study, automotive street domination (the invention of 'jaywalking' in the 1920s), stranger danger moral panics, GPS child tracking watches, and the loss of independent childhood adventure.",
                "reason": "Documents the dramatic, measurable spatial contraction of children's physical freedom over four generations."
            },
            {
                "id": 12,
                "title": "The Saturday Morning Cartoon Gold Rush: How Toy Companies Colonized the Child Brain",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "systemic_critique",
                "slug": "saturday_morning_cartoons_fcc_deregulation_toy_commercials",
                "question": "How did 1980s FCC deregulation allow toy companies to turn 30-minute television shows into direct, unregulated toy commercials?",
                "focus": "The 1984 FCC deregulation under Mark Fowler, He-Man and the Masters of the Universe, Transformers, G.I. Joe, sugar cereal marketing, Action for Children's Television (Peggy Charren), and the Children's Television Act of 1990.",
                "reason": "Examines the commercial, regulatory, and psychological mechanics of mass television marketing directly targeted at children."
            },
            {
                "id": 13,
                "title": "Helicopter to Snowplow Parenting: The Rise of Hyper-Vigilant Intensive Motherhood",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "comparative_analysis",
                "slug": "helicopter_parenting_intensive_motherhood_sharon_hays_snowplow",
                "question": "Why do modern middle-class parents spend more hours directly supervising and scheduling children today than stay-at-home mothers did in 1965?",
                "focus": "Sharon Hays' 'Cultural Contradictions of Motherhood' (intensive parenting thesis), college admissions meritocracy hyper-competition, snowplow parents clearing all obstacles, and the unintended epidemic of adolescent anxiety and fragility.",
                "reason": "Analyzes the sociological and economic pressures driving contemporary intensive, anxiety-driven parenting norms."
            },
            {
                "id": 14,
                "title": "Dr. Spock vs Dr. Watson: The Century-Long Battle Over How to Hold Your Baby",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "historical_evolution",
                "slug": "dr_spock_vs_john_watson_parenting_manuals_baby_and_child_care",
                "question": "Why did 1920s behaviorists tell mothers to never hug or kiss their babies, and how did Dr. Benjamin Spock spark a permissive revolution in 1946?",
                "focus": "John B. Watson's rigid behaviorist clock feeding and emotional withholding, Dr. Spock's Common Sense Book of Baby and Child Care ('Trust yourself, you know more than you think'), the Ferber sleep training debate, and shifting scientific advice.",
                "reason": "Deconstructs the wild historical pendulum swings of pediatric medical advice and parenting manual doctrine."
            },
            {
                "id": 15,
                "title": "The Foundling Hospital: Thomas Coram's Battle to Save London's Abandoned Infants",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "case_study",
                "slug": "foundling_hospital_thomas_coram_abandoned_infant_tokens",
                "question": "How did a retired sea captain build Britain's first incorporated charity, where desperate mothers left babies alongside unique personalized tokens?",
                "focus": "Captain Thomas Coram, artist William Hogarth and composer George Frideric Handel raising funds with Messiah concerts, the poignant scrap fabric and coin 'tokens' mothers pinned to swaddling clothes, and the origins of modern child welfare.",
                "reason": "A profound historical study in citizen philanthropy and the institutional origins of child rescue and social safety nets."
            },
            {
                "id": 16,
                "title": "Childhood Disease and Vaccines: Eradicating the Killers of One in Three Babies",
                "tier": "Tier 3: Advanced Methodologies & Frameworks",
                "angle": "deep_dive",
                "slug": "childhood_diseases_vaccines_polio_measles_diphtheria_iron_lungs",
                "question": "What was life like when every summer parents dreaded the knock of polio that locked thousands of children into metal iron lung chambers?",
                "focus": "Jonas Salk and Albert Sabin's polio vaccine trials, diphtheria 'the strangler of children', measles and smallpox mortality baselines, the 1950s March of Dimes mobilization, and the miraculous collapse in global under-five mortality.",
                "reason": "Essential historical and epidemiological perspective celebrating the greatest pediatric public health triumph in human history."
            },
            {
                "id": 17,
                "title": "The Shifting Age of Adulthood: Why 'Emerging Adulthood' Now Lasts Until Age 29",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "philosophical_perspectives",
                "slug": "shifting_age_of_adulthood_jeffrey_arnett_emerging_adulthood",
                "question": "Why did historical 18-year-olds buy homes, get married, and fight wars, while modern 25-year-olds are considered young adults still finding themselves?",
                "focus": "Jeffrey Arnett's 'Emerging Adulthood' developmental stage, prolonged credentialization requirements in knowledge economies, delayed financial independence and marriage, and whether adulthood was biologically delayed or economically postponed.",
                "reason": "Probes the changing sociocultural timeline separating childhood from full adult independence in the modern world."
            },
            {
                "id": 18,
                "title": "The Smartphone Generation: Jonathan Haidt on The Anxious Generation",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "investigative_report",
                "slug": "the_anxious_generation_jonathan_haidt_smartphone_play_based_childhood",
                "question": "Did the sudden arrival of front-facing cameras, Instagram, and algorithmic feeds in 2012 rewire childhood from 'play-based' to 'phone-based'?",
                "focus": "Jonathan Haidt's The Anxious Generation, adolescent female depression and self-harm spikes coinciding with social media mobile saturation, loss of unstructured free play, sleep deprivation, and policy moves to ban phones in schools.",
                "reason": "Examines the paramount ongoing public health and sociological debate concerning the impact of digital mobile platforms on child development."
            },
            {
                "id": 19,
                "title": "The $300,000 Child: The Real Financial Cost of Raising a Child from Birth to Age 18",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "cost_breakdown",
                "slug": "cost_of_raising_a_child_usda_childcare_infant_formula_college",
                "question": "Where does $310,000 go when raising a middle-class child in America, and why is infant childcare now more expensive than in-state college tuition?",
                "focus": "USDA Child-Rearing Expense calculations, infant daycare infant-to-staff ratio economics ($15,000-$25,000/yr), healthcare premiums, housing extra bedroom costs, food, and extracurricular activities.",
                "reason": "Detailed economic teardown explaining why childcare costs have become a primary driver of plummeting global birth rates."
            },
            {
                "id": 20,
                "title": "The Masterclass on Child Advocacy: Designing Communities That Prioritize Children",
                "tier": "Tier 4: Enterprise Strategy & Deep Mastery",
                "angle": "masterclass",
                "slug": "masterclass_child_friendly_cities_unicef_urban_design_play",
                "question": "How do world-class urban planners and child advocates design cities where eight-year-olds can safely walk, play, and navigate independently?",
                "focus": "UNICEF Child Friendly Cities Initiative, Dutch 'Woonerf' shared living streets, European protected bike networks, natural adventure playgrounds (junk playgrounds), traffic calming, and creating public spaces where children belong.",
                "reason": "The definitive masterclass showing how civil infrastructure, municipal policy, and urban planning can re-integrate children into healthy public life."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Smartphone-Free School Movement: Why Countries and States Are Banning Phones in Classrooms",
                "trend_score": "High Global Velocity (9.6/10)",
                "angle": "investigative_report",
                "slug": "smartphone_free_schools_movement_yondr_pouches_bans",
                "why_trending": "Sweeping momentum as UK, France, and US states mandate magnetic Yondr pouches and total school cell phone bans to combat learning loss and bullying.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "Jonathan Haidt's 'The Anxious Generation': The Bestseller Shaking Up School Boards and Parenting",
                "trend_score": "Rapid Surge (9.5/10)",
                "angle": "case_study",
                "slug": "jonathan_haidt_anxious_generation_bestseller_four_reforms",
                "why_trending": "Massive viral engagement around Haidt's four core norms: no smartphones before high school, no social media before 16, phone-free schools, and more unsupervised play.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "The Return of 'Adventure Playgrounds': Why Kids Need Mud, Hammers, and Fire",
                "trend_score": "Viral Peak (9.3/10)",
                "angle": "field_investigation",
                "slug": "adventure_playgrounds_junk_playgrounds_loose_parts_risk",
                "why_trending": "Fascinating viral video tours of European junk playgrounds where children saw wood, build treehouses, and start bonfires under watchful but non-interfering staff.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "The 'Gentle Parenting' Backlash: Why Exhausted Parents Are Re-evaluating Permissive Boundaries",
                "trend_score": "Breakthrough Trend (9.1/10)",
                "angle": "systemic_critique",
                "slug": "gentle_parenting_backlash_permissive_parenting_boundary_struggles",
                "why_trending": "Parenting experts and viral creator discussions on the burnout caused by endless verbal negotiation with toddlers and the return of authoritative boundary setting.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "The $2,000/Month Daycare Reality: Why Childcare Deserts Are Forcing Mothers Out of Careers",
                "trend_score": "High Velocity (8.9/10)",
                "angle": "cost_breakdown",
                "slug": "childcare_deserts_infant_daycare_costs_workforce_dropouts",
                "why_trending": "Economic investigative features detailing how daycare tuition exceeding mortgage payments is forcing working parents out of the labor market.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "The Vintage Toy Goldmine: The 1980s Plastic Toys in Attics Worth Tens of Thousands",
                "trend_score": "Emerging Niche (8.8/10)",
                "angle": "cultural_traditions",
                "slug": "vintage_toy_goldmine_star_wars_transformers_auction_records",
                "why_trending": "Record auction prices for mint-on-card 1978 Star Wars Kenner action figures and original Generation 1 Transformers turning childhood toys into alternative investments.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The Disappearing Children's Birthday Party: Why Parents Are Skipping the $500 Play Venue",
                "trend_score": "Steady Long-Tail (8.5/10)",
                "angle": "cost_breakdown",
                "slug": "kids_birthday_party_inflation_trampoline_parks_alternatives",
                "why_trending": "Families pushing back against hyper-commercialized $500 2-hour trampoline park birthday party rentals in favor of classic low-cost park gatherings.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 171-175...")
    for folder_name, meta in BATCH_171_175.items():
        process_niche(folder_name, meta)

    update_master_readme()
    print("Batch 171-175 complete!")

if __name__ == "__main__":
    main()
