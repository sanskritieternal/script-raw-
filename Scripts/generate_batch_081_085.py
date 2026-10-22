"""
Batch Generator for Niches 081 to 085:
- 081_theatre_performing_arts
- 082_fashion_clothing
- 083_jewelry_precious_materials
- 084_collectibles_antiques
- 085_diy_making
"""

import sys
from pathlib import Path

# Add Scripts to sys.path
sys.path.append(str(Path(__file__).parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_081_085 = {
    "081_theatre_performing_arts": {
        "id": "081",
        "slug": "theatre_performing_arts",
        "title": "Theatre & Performing Arts",
        "category": "Literature_Performance",
        "audience": "Theatre Enthusiasts, Actors, Stage Directors, Playwrights, Performing Arts Students (Global)",
        "progression": [
            ("Tier 1: Classical Drama, Stagecraft & Physical Presence (Scratch / Beginner)",
             "Greek chorus and Dionysian festivals, Elizabethan stage (The Globe), Commedia dell'arte stock masks, stage geography (upstage/downstage), and vocal projection fundamentals."),
            ("Tier 2: Acting Methodologies: Stanislavski to The Method (Intermediate)",
             "Konstantin Stanislavski's 'An Actor Prepares' (magic if, emotional memory), Lee Strasberg's Method vs. Stella Adler's imagination, and Bertolt Brecht's alienation effect (Verfremdungseffekt)."),
            ("Tier 3: Non-Western Traditions: Noh, Kabuki, Kathakali & Beijing Opera (Upper Intermediate)",
             "Zeami's Yugen aesthetic in Noh, Kabuki Mie poses and Onnagata gender performance, Kathakali mudras and eye-muscle facial grammar, and Beijing Opera acrobatics and percussion."),
            ("Tier 4: Avant-Garde Performance, Broadway Economics & Post-Dramatic Theatre (Advanced / Expert)",
             "Jerzy Grotowski's Poor Theatre, Antonin Artaud's Theatre of Cruelty, immersive site-specific experiences (Sleep No More), Broadway/West End capitalization and recoupment cycles.")
        ],
        "flagship": {
            "title": "The Method Acting Revolution: How Stanislavski and Strasberg Changed Human Performance Forever",
            "angle": "performance_history",
            "slug": "081_theatre_performing_arts_performance_history_method_acting_revolution"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Method Acting Revolution: How Stanislavski and Strasberg Changed Human Performance Forever",
                "tier": "Tier 1: Classical Drama & Physical Presence",
                "angle": "performance_history",
                "slug": "method_acting_revolution_stanislavski_strasberg_adler_emotional_memory",
                "question": "How did a 19th-century Russian director's rebellion against melodramatic posturing give birth to Marlon Brando, Al Pacino, and modern naturalistic acting?",
                "key_focus": "The Moscow Art Theatre, Stanislavski's system ('The Magic If', affective memory, action objectives), Strasberg's Actors Studio, and Stella Adler's fierce counter-philosophy of imagination.",
                "reason": "Flagship launch episode; unlocks the most influential, misunderstood, and transformative acting revolution in human history."
            },
            {
                "id": 2,
                "title": "Ancient Greek Theatre: Dionysian Rituals, The Chorus, and Aristotle's Catharsis",
                "tier": "Tier 1: Classical Drama & Physical Presence",
                "angle": "historical_origins",
                "slug": "ancient_greek_theatre_dionysus_chorus_aristotle_poetics_catharsis",
                "question": "How did religious wine sacrifices in Athens evolve into amphitheatre tragedies that purged civic emotion through pity and terror?",
                "key_focus": "The City Dionysia festival, Thespis stepping out of the chorus, tragic masks with megaphone mouthpieces, Aristotle's Poetics, Hamartia (tragic flaw), and Anagnorisis (realization).",
                "reason": "The foundational birth of Western theatrical drama, dramatic theory, and civic catharsis."
            },
            {
                "id": 3,
                "title": "Shakespeare's Globe: Acoustics, Groundlings, and The Mechanics of Bare-Stage Magic",
                "tier": "Tier 1: Classical Drama & Physical Presence",
                "angle": "stagecraft_history",
                "slug": "shakespeares_globe_thrust_stage_groundlings_daylight_acoustics",
                "question": "How did Elizabethan actors command 3,000 rowdy beer-drinking spectators under open daylight with zero artificial lighting or microphones?",
                "key_focus": "The wooden 'O' thrust stage architecture, spoken scenery ('What light through yonder window breaks'), iambic pentameter breath rhythms, trapdoors, and groundling audience interaction.",
                "reason": "Deconstructs the physical engineering and verbal pyrotechnics of Shakespearean performance."
            },
            {
                "id": 4,
                "title": "Commedia dell'Arte: The Improvisational Street Comedy That Invented Slapstick",
                "tier": "Tier 1: Classical Drama & Physical Presence",
                "angle": "performance_traditions",
                "slug": "commedia_dellarte_leather_masks_stock_characters_slapstick_lazzi",
                "question": "Why do the greedy Pantalone, arrogant Il Dottore, and nimble Arlecchino still form the comic DNA of modern sitcoms and cartoons?",
                "key_focus": "Renaissance Italian traveling troupes, leather half-masks, stock character physical postures, the literal wooden slapstick batte, and rehearsed comic routines (lazzi).",
                "reason": "Explores the root system of all Western physical comedy, improvisation, and stock character archetypes."
            },
            {
                "id": 5,
                "title": "Stage Geography and Blocking: Why 'Upstage' and 'Downstage' Control the Audience's Eye",
                "tier": "Tier 1: Classical Drama & Physical Presence",
                "angle": "directorial_craft",
                "slug": "stage_geography_blocking_raked_stages_proscenium_sightlines",
                "question": "Where did the terms 'upstage' and 'downstage' come from, and how do theatrical directors compose live human paintings using geometric diagonals?",
                "key_focus": "Historic raked stages tilted toward audiences, 9-zone proscenium grid, body angles (full front, profile, turned away), triangular staging, and stealing focus.",
                "reason": "Essential visual grammar tutorial explaining how directors steer audience attention on live stages."
            },
            {
                "id": 6,
                "title": "Bertolt Brecht and Epic Theatre: Why He Wanted Audiences to Think, Not Cry",
                "tier": "Tier 2: Acting Methodologies & Politics",
                "angle": "theatrical_revolution",
                "slug": "bertolt_brecht_epic_theatre_verfremdungseffekt_alienation_effect",
                "question": "Why did playwright Bertolt Brecht deliberately destroy theatrical illusion with harsh lighting, placards, and songs to prevent viewers from emotional escapism?",
                "key_focus": "Verfremdungseffekt (defamiliarization/alienation), Aristotelian dramatic theatre vs. Brechtian epic theatre, Gestus (physical social attitude), and Marxist political critique in Mother Courage.",
                "reason": "The defining counter-tradition to psychological realism, demanding intellectual engagement from spectators."
            },
            {
                "id": 7,
                "title": "Voice and Projection: How Stage Actors Fill a 2,000-Seat Hall Without Microphones",
                "tier": "Tier 2: Acting Methodologies & Politics",
                "angle": "vocal_mechanics",
                "slug": "vocal_projection_theatre_diaphragm_pharyngeal_resonance_cicely_berry",
                "question": "What is the physiological difference between screaming and theatrical projection, and how does resonance amplify whisper sound waves over 100 feet?",
                "key_focus": "Diaphragmatic intercostal breath support, hard palate and pharyngeal acoustic resonance chambers, Cicely Berry and Kristin Linklater vocal techniques, and articulation consonants.",
                "reason": "A high-utility masterclass in the acoustic bio-mechanics of the human vocal instrument."
            },
            {
                "id": 8,
                "title": "Antonin Artaud and The Theatre of Cruelty: Shaking the Bourgeoisie Out of Numbness",
                "tier": "Tier 2: Acting Methodologies & Politics",
                "angle": "avant_garde_theory",
                "slug": "antonin_artaud_theatre_of_cruelty_balinese_dance_sensory_assault",
                "question": "Why did French visionary Antonin Artaud believe theatre should be like a plague—shattering civilized rationalism through guttural screams and raw trance?",
                "key_focus": "The Theatre and Its Double (1938), Balinese dance influence, rejecting literary text dominance in favor of visceral physical incantation, and the cruelty of inescapable reality.",
                "reason": "Examines the radical manifesto that inspired 1960s experimental performance art and rock concerts."
            },
            {
                "id": 9,
                "title": "Stage Lighting Design: Adolphe Appia and The Power of Living Light",
                "tier": "Tier 2: Acting Methodologies & Politics",
                "angle": "theatrical_design",
                "slug": "stage_lighting_design_adolphe_appia_gobo_mood_spatial_sculpting",
                "question": "How did the transition from smelly gaslight footlights to electric spotlights transform the stage into a three-dimensional psychological dreamscape?",
                "key_focus": "Adolphe Appia's living light theories, Edward Gordon Craig's scenic symbolism, color gels and psychological mood, Gobo shadow projections, and cue timing during scene transitions.",
                "reason": "Highlights the unsung technical art form that sculpts emotion and architectural depth in live performance."
            },
            {
                "id": 10,
                "title": "The Absurdist Revolution: Waiting for Godot and The Comedy of Existential Despair",
                "tier": "Tier 2: Acting Methodologies & Politics",
                "angle": "modernist_drama",
                "slug": "theatre_of_the_absurd_samuel_beckett_waiting_for_godot_ionesco",
                "question": "Why did a 1953 Parisian play where 'nothing happens, nobody comes, nobody goes, it's awful' become the defining masterpiece of post-WWII theatre?",
                "key_focus": "Samuel Beckett's circular dialogue, Martin Esslin's Theatre of the Absurd definition, Eugene Ionesco's Rhinoceros, clowning traditions applied to post-holocaust trauma.",
                "reason": "Deconstructs the existential masterpiece that captured humanity's search for meaning in an indifferent universe."
            },
            {
                "id": 11,
                "title": "Japanese Noh Theatre: The Ghostly World of Masks, Slow Footwork, and Yūgen",
                "tier": "Tier 3: Non-Western Performance Traditions",
                "angle": "traditional_world_theatre",
                "slug": "japanese_noh_theatre_zeami_yugen_carved_hinoki_masks_suriashi",
                "question": "Why does a Noh actor take 30 seconds to walk 5 steps across a cypress bridge, and how can a tilted wooden mask change its emotional expression?",
                "key_focus": "Zeami Motokiyo's treatises, Yugen (mysterious, shadowy beauty), Suriashi sliding walk, Shite (principal actor) and Waki, carved cypress (hinoki) masks catching ceiling shadows.",
                "reason": "Explores the world's oldest continuously practiced masked drama with over 650 years of refined spiritual discipline."
            },
            {
                "id": 12,
                "title": "Kathakali: The 500-Year-Old Indian Dance-Drama of Epic Battle and Ocular Grammar",
                "tier": "Tier 3: Non-Western Performance Traditions",
                "angle": "traditional_world_theatre",
                "slug": "kathakali_kerala_dance_drama_mudras_facial_muscles_navarasas",
                "question": "How do Kathakali performers in Kerala train for 10 years to independently move their eyelids, cheek muscles, and fingertips into 24 distinct hand mudras?",
                "key_focus": "Kerala temple origins, 3-hour Chutti facial makeup application (green Paccha for heroes, black Kari for demons), the 9 emotional Navarasas, and drumming rhythms (Chenda).",
                "reason": "Celebrates one of the world's most physically demanding and visually stunning classical performance traditions."
            },
            {
                "id": 13,
                "title": "Kabuki: Feudal Japan's Pop Spectacle of Revolving Stages and Gender Bending",
                "tier": "Tier 3: Non-Western Performance Traditions",
                "angle": "traditional_world_theatre",
                "slug": "kabuki_theatre_onnagata_mie_pose_hanamichi_revolving_stage",
                "question": "How did an outlawed female riverbank dance in 1603 transform into Japan's most spectacular all-male theatrical spectacle featuring flying actors and dramatic freezes?",
                "key_focus": "Okuni of Izumo origins, the Onnagata (male actor specializing in female roles), Mie frozen dramatic poses, Hanamichi footbridge runway, and inventing the world's first revolving stage.",
                "reason": "Examines the vibrant, high-energy counterpoint to austere Noh drama that defined Edo-period urban culture."
            },
            {
                "id": 14,
                "title": "Beijing Opera: The Four Skills of Singing, Dialogue, Acting, and Acrobatics",
                "tier": "Tier 3: Non-Western Performance Traditions",
                "angle": "traditional_world_theatre",
                "slug": "beijing_opera_jingju_sheng_dan_jing_chou_acrobatic_martial_arts",
                "question": "How do Beijing Opera performers combine martial arts acrobatics, falsetto vocal gymnastics, and painted Lianpu faces into a total physical language?",
                "key_focus": "The four character types (Sheng, Dan, Jing, Chou), Lianpu face paint color symbolism (red for loyalty, white for treachery), water sleeves (Shuixiu) choreography, and Mei Lanfang's global tours.",
                "reason": "Highlights the synthesis of martial arts, classical music, and symbolic movement in Chinese Jingju."
            },
            {
                "id": 15,
                "title": "The Natyashastra: The World's Most Comprehensive Ancient Treatise on Performing Arts",
                "tier": "Tier 3: Non-Western Performance Traditions",
                "angle": "classical_treatises",
                "slug": "natyashastra_bharata_muni_rasa_theory_bhavas_ancient_theatre_encyclopedia",
                "question": "What is Bharata Muni's 2,000-year-old Rasa Theory, and how does it explain the chemical relationship between an actor's emotion and the spectator's taste?",
                "key_focus": "The 36 chapters of the Natyashastra, Bhavas (underlying psychological states) producing Rasas (aesthetic tastes), stage architecture, costume design, and musical scales.",
                "reason": "Documents the ancient Sanskrit foundational encyclopedia that predates Aristotle in breadth and systematic depth."
            },
            {
                "id": 16,
                "title": "Jerzy Grotowski's 'Poor Theatre': Stripping Away Sets, Costumes, and Tech for the Holy Actor",
                "tier": "Tier 4: Avant-Garde, Economics & The Future",
                "angle": "experimental_theatre",
                "slug": "jerzy_grotowski_towards_a_poor_theatre_holy_actor_via_negativa",
                "question": "Why did Polish visionary Jerzy Grotowski throw away all stage lighting, microphones, costumes, and makeup to build the 'Holy Actor'?",
                "key_focus": "'Towards a Poor Theatre' (1968), Via Negativa (eradicating bodily blocks rather than teaching tricks), psycho-physical acrobatics, dissolving the boundary between actor and spectator.",
                "reason": "The radical monastic experiment that re-centered live theatre entirely around the raw human animal."
            },
            {
                "id": 17,
                "title": "Broadway Economics: Why 80% of Broadway Shows Lose Every Penny They Invest",
                "tier": "Tier 4: Avant-Garde, Economics & The Future",
                "angle": "commercial_economics",
                "slug": "broadway_economics_capitalization_recoupment_weekly_running_costs_shubert",
                "question": "How can a musical that sells out every seat at $250 a ticket for six months still close as a complete financial catastrophe?",
                "key_focus": "$15M–$25M capitalization costs, weekly running costs (rent, orchestra, union crew), the Shubert/Nederlander theatre real estate monopoly, recoupment curves, and tourist economics.",
                "reason": "An eye-opening breakdown of the brutal, high-stakes financial casino that funds American musical theatre."
            },
            {
                "id": 18,
                "title": "Immersive Theatre: How 'Sleep No More' Eliminated Seats and Invented the Sandbox Play",
                "tier": "Tier 4: Avant-Garde, Economics & The Future",
                "angle": "spatial_innovation",
                "slug": "immersive_theatre_punchdrunk_sleep_no_more_mckittrick_hotel_masks",
                "question": "How did British theatre company Punchdrunk transform a 100-room abandoned warehouse into a silent, mask-wearing, choose-your-own-adventure Macbeth?",
                "key_focus": "Environmental storytelling, audience wearing white venetian masks for anonymity, 1-on-1 secret actor encounters, kinetic dance replacing dialogue, and video-game sandbox dramaturgy.",
                "reason": "Explores the most profitable and influential theatrical innovation of the 21st century."
            },
            {
                "id": 19,
                "title": "Augusto Boal and Theatre of the Oppressed: Transforming Spectators into 'Spect-Actors'",
                "tier": "Tier 4: Avant-Garde, Economics & The Future",
                "angle": "social_activism",
                "slug": "theatre_of_the_oppressed_augusto_boal_forum_theatre_spect_actors",
                "question": "How did Brazilian activist Augusto Boal use interactive street scenes to empower marginalized communities to stop a scene and step in to rehearse social liberation?",
                "key_focus": "Forum Theatre mechanics, the Joker facilitator role, Image Theatre, Invisible Theatre performed in real public markets, and using drama as a rehearsal for real-world political revolt.",
                "reason": "Demonstrates the power of dramatic technique used as a therapeutic, grassroots democratic weapon."
            },
            {
                "id": 20,
                "title": "The Future of Live Theatre: Holograms, AI Playwrights, and The Irreplaceable Live Room",
                "tier": "Tier 4: Avant-Garde, Economics & The Future",
                "angle": "future_horizons",
                "slug": "future_of_theatre_holograms_ai_playwriting_shared_communal_breath",
                "question": "In an era of VR headsets and synthetic video, why is the physical co-presence of shared breathing between human actor and human audience more vital than ever?",
                "key_focus": "Experiments with generative AI real-time improv, ABBA Voyage digital avatars, binaural audio headphone plays, and neuroscience showing synchronized heartbeats in live audiences.",
                "reason": "Concludes the master curriculum by celebrating the immortal, unreplicable magic of human bodies in a live physical space."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Method Acting Goes Too Far: Jared Leto, Heath Ledger, and the Cost of Never Breaking Character",
                "tier": "Trending / High Retention",
                "angle": "viral_acting_debates",
                "slug": "dark_side_of_method_acting_jared_leto_heath_ledger_daniel_day_lewis",
                "trend_score": 98,
                "why_trending": "Continuous viral debates online questioning whether extreme 'method' habits (sending rats, staying in wheelchairs) are genuine craft or self-indulgent narcissism.",
                "reason": "Incredible hook diving into celebrity anecdotes, psychological boundaries, and acting technique.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "How Lin-Manuel Miranda Wrote 'Hamilton': Deconstructing Hip-Hop Rhyme Schemes in Musicals",
                "tier": "Trending / High Retention",
                "angle": "musical_deconstruction",
                "slug": "hamilton_lyrical_deconstruction_lin_manuel_miranda_multisyllabic_rhymes",
                "trend_score": 97,
                "why_trending": "Videos analyzing multisyllabic internal rhymes, leitmotifs, and wordplay in 'My Shot' and 'Satisfied' regularly clock tens of millions of views across YouTube and TikTok.",
                "reason": "Engages Broadway fans and hip-hop heads alike with brilliant technical breakdowns of lyrical craft.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Why You Can't Say 'Macbeth' in a Theatre: The 400-Year-Old Curse of 'The Scottish Play'",
                "tier": "Trending / High Retention",
                "angle": "theatrical_superstitions",
                "slug": "curse_of_the_scottish_play_macbeth_superstition_real_stage_accidents",
                "trend_score": 95,
                "why_trending": "Evergreen curiosity about theatre superstitions, real sword combat fatalities on stage, and the bizarre counter-curse ritual (spinning 3 times, spitting, quoting Hamlet).",
                "reason": "Spooky, high-retention folklore grounded in real historical stage disasters.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Phantom of the Opera Chandelier Drop: How the Stage Illusion Works Every Night",
                "tier": "Trending / High Retention",
                "angle": "stage_magic_mechanics",
                "slug": "phantom_of_the_opera_chandelier_drop_rigging_safety_pyrotechnics",
                "trend_score": 94,
                "why_trending": "Closing of Phantom's historic 35-year Broadway run sparked a wave of nostalgic retrospectives on its massive 1-ton falling chandelier mechanics.",
                "reason": "Fascinating backstage engineering breakdown showing computer winches, counterweights, and failsafes.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Why Live Theatre Tickets Cost $400: Inside the Broadway Scalper and Dynamic Pricing Crisis",
                "tier": "Trending / High Retention",
                "angle": "ticket_economics",
                "slug": "why_theatre_tickets_cost_400_dollars_broadway_ticketmaster_scalpers",
                "trend_score": 96,
                "why_trending": "Widespread consumer fury over $800 Sweeney Todd and Cabaret tickets, bot scalping, and dynamic algorithms pricing ordinary people out of live arts.",
                "reason": "Deeply relatable consumer outrage backed by sharp economic and legal reporting.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Stage Slaps and Fake Blood: The Secret Science of Fight Choreography and Stage Combat",
                "tier": "Trending / High Retention",
                "angle": "stage_combat_secrets",
                "slug": "stage_combat_fight_choreography_fake_slap_knap_sound_blunt_swords",
                "trend_score": 95,
                "why_trending": "Viral clips showing how a staged punch uses a hidden hand clap ('knap') for sound, and how blunt rapiers protect actors while looking lethal.",
                "reason": "Instant visual satisfaction revealing the illusion tricks behind heart-pounding stage fights.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Sleep No More Closes: Why the World's Most Famous Immersive Experience Ended",
                "tier": "Trending / High Retention",
                "angle": "cultural_milestone",
                "slug": "sleep_no_more_closing_mckittrick_hotel_immersive_theatre_legacy",
                "trend_score": 96,
                "why_trending": "Huge global coverage of the definitive immersive theatrical show closing its doors after 13 years and millions of attendees.",
                "reason": "Timely retrospective celebrating the landmark phenomenon that birthed the global escape room and immersive art movement.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "082_fashion_clothing": {
        "id": "082",
        "slug": "fashion_clothing",
        "title": "Fashion & Clothing",
        "category": "Food_Fashion",
        "audience": "Fashion Designers, Garment Technologists, Stylists, Textile Geeks, Vintage Collectors (Global)",
        "progression": [
            ("Tier 1: Textile Foundations, Garment Anatomy & Silhouette Construction (Scratch / Beginner)",
             "Natural vs. synthetic fibers (cotton, wool, silk, linen, polyester), warp/weft weaving, garment anatomy (darts, yokes, seams, hems), and classic silhouettes (A-line, hourglass, sheath)."),
            ("Tier 2: Haute Couture, Tailoring Traditions & Modern Fashion Epochs (Intermediate)",
             "Parisian Chambre Syndicale de la Haute Couture rules, Savile Row bespoke suit architecture, Christian Dior's 1947 'New Look', Coco Chanel's little black dress, and Yves Saint Laurent's Le Smoking."),
            ("Tier 3: Subcultural Streetwear, Japanese Avant-Garde & Antwerp Six (Upper Intermediate)",
             "Harajuku and Japanese denim craftsmanship, Rei Kawakubo (Comme des Garcons) deconstructivism, Martin Margiela's invisible identity, and Antwerp Six tailoring radicalism."),
            ("Tier 4: Fast Fashion Supply Chains, Circular Textiles & Digital Fashion (Advanced / Expert)",
             "Ultra-fast fashion logistics (Shein/Zara supply chains), ecological impact (microplastics, water consumption), textile recycling chemistry, digital 3D virtual garments, and archival fashion investing.")
        ],
        "flagship": {
            "title": "Haute Couture: The Secret Rules, Impossible Craftsmanship, and Economics of Million-Dollar Dresses",
            "angle": "craftsmanship_economics",
            "slug": "082_fashion_clothing_craftsmanship_economics_haute_couture_secrets"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Haute Couture: The Secret Rules, Impossible Craftsmanship, and Economics of Million-Dollar Dresses",
                "tier": "Tier 1: Textile Foundations & Garment Anatomy",
                "angle": "craftsmanship_economics",
                "slug": "haute_couture_secret_rules_chambre_syndicale_lesage_embroidery",
                "question": "Why is the term 'Haute Couture' protected by French criminal law, and why do billionaire fashion houses lose millions producing hand-stitched runway gowns?",
                "key_focus": "The strict legal criteria of the Federation de la Haute Couture (Parisian ateliers, 15+ full-time artisans, custom fittings), Maison Lesage embroidery taking 1,000 hours, and using couture as a marketing halo for perfumes.",
                "reason": "Flagship launch episode; unlocks the pinnacle of garment craft, luxury prestige, and high-fashion economics."
            },
            {
                "id": 2,
                "title": "Textile Science: Why Natural Fibers Outperform Synthetics in Breathability and Longevity",
                "tier": "Tier 1: Textile Foundations & Garment Anatomy",
                "angle": "material_science",
                "slug": "textile_science_natural_vs_synthetic_fibers_cotton_wool_silk_polyester",
                "question": "What is happening at the microscopic filament level when wool wicks sweat, linen cools skin, and polyester traps body odor?",
                "key_focus": "Cellulose vs. protein fibers, staple length in Egyptian cotton, crimp and keratin structure in Merino wool, filament extrusion in polyester/nylon, and microplastic shedding.",
                "reason": "The foundational material education every smart consumer and aspiring designer needs."
            },
            {
                "id": 3,
                "title": "Garment Anatomy: Darts, Yokes, and Seams That Shape 2D Fabric to 3D Human Bodies",
                "tier": "Tier 1: Textile Foundations & Garment Anatomy",
                "angle": "patternmaking_basics",
                "slug": "garment_anatomy_patternmaking_darts_yokes_french_seams_bias_cut",
                "question": "How do flat sheets of woven fabric curve smoothly over human shoulders, waists, and hips without bunching or tearing?",
                "key_focus": "Dart manipulation (bust, waist, French darts), yokes supporting weight, grainline vs. bias cut (Madeline Vionnet's drape innovation), and seam finishes (French, flat-felled, bound).",
                "reason": "Deconstructs the engineering mechanics behind clothing construction and tailoring fit."
            },
            {
                "id": 4,
                "title": "The Power of Silhouette: How A-Line, Hourglass, and Cocoon Shapes Redefined History",
                "tier": "Tier 1: Textile Foundations & Garment Anatomy",
                "angle": "design_history",
                "slug": "power_of_silhouette_dior_hourglass_balenciaga_cocoon_chanel_box",
                "question": "Why does changing the outline of a dress from 10 feet away communicate wealth, authority, or rebellion before a single detail is seen?",
                "key_focus": "The Victorian crinoline cage, Christian Dior's 1947 New Look wasp waist, Cristóbal Balenciaga's architectural barrel and cocoon coats, and modern oversized tailoring.",
                "reason": "Teaches viewers how to analyze the macro-geometry of fashion history."
            },
            {
                "id": 5,
                "title": "Color and Dyeing: From Royal Tyrian Purple Snail Slime to Synthetic Coal-Tar Mauve",
                "tier": "Tier 1: Textile Foundations & Garment Anatomy",
                "angle": "chemical_history",
                "slug": "history_of_fabric_dyes_tyrian_purple_cochineal_william_perkin_mauveine",
                "question": "How did an 18-year-old chemist trying to cure malaria accidentally invent the first synthetic purple dye in 1856 and democratize fashion?",
                "key_focus": "Crushed Murex sea snails in ancient Phoenicia, cochineal insect red, William Perkin's synthetic Mauveine revolution, and modern azo dyes and toxic effluent challenges.",
                "reason": "Riveting scientific and cultural journey revealing why certain colors used to be reserved exclusively for emperors."
            },
            {
                "id": 6,
                "title": "Savile Row: The Anatomy of a Bespoke Suit and 50 Hours of Hand Stitching",
                "tier": "Tier 2: Haute Couture & Tailoring Epochs",
                "angle": "bespoke_craft",
                "slug": "savile_row_bespoke_suit_canvas_floating_interfacing_pad_stitching",
                "question": "Why does a genuine bespoke suit from London's Savile Row cost $6,000+ and take three fittings, while a fused off-the-rack jacket bubbles after dry cleaning?",
                "key_focus": "Horsehair floating canvas interfacing, hand pad-stitching on lapels, horn buttons, surgeon's cuffs (working buttonholes), and sculpting wool with heavy irons.",
                "reason": "The ultimate deep dive into classic menswear tailoring, heritage longevity, and craftsmanship."
            },
            {
                "id": 7,
                "title": "Christian Dior's 1947 'New Look': How 20 Yards of Fabric Healed Post-War Europe",
                "tier": "Tier 2: Haute Couture & Tailoring Epochs",
                "angle": "historical_turning_points",
                "slug": "christian_dior_1947_new_look_bar_suit_fabric_rationing_rebellion",
                "question": "Why did Christian Dior's extravagant, full-skirted Bar Suit cause street protests in post-WWII Paris among women still living under fabric rationing?",
                "key_focus": "Wartime austerity and utility clothing, Dior's restoration of opulent feminine curves, Carmel Snow's famous 'New Look' proclamation, and establishing Paris as the eternal fashion capital.",
                "reason": "Examines the single most commercially and culturally impactful fashion collection of the 20th century."
            },
            {
                "id": 8,
                "title": "Coco Chanel vs. Elsa Schiaparelli: The Bitter Rivalry Between Functional Chic and Surrealist Shock",
                "tier": "Tier 2: Haute Couture & Tailoring Epochs",
                "angle": "design_rivalries",
                "slug": "chanel_vs_schiaparelli_little_black_dress_vs_lobster_dress_rivalry",
                "question": "How did Chanel's minimalist jersey dresses clash with Schiaparelli's Salvador Dalí lobster gowns in 1930s Paris?",
                "key_focus": "Chanel freeing women from corsets with sporty tweed and the Little Black Dress, Schiaparelli inventing Shocking Pink, shoe hats, and skeleton dresses; high society cultural war.",
                "reason": "A thrilling clash of aesthetic philosophies: quiet functional modernism versus avant-garde surrealist art."
            },
            {
                "id": 9,
                "title": "Yves Saint Laurent and 'Le Smoking': When Putting Women in Tuxedos Was an Act of Defiance",
                "tier": "Tier 2: Haute Couture & Tailoring Epochs",
                "angle": "gender_subversion",
                "slug": "yves_saint_laurent_le_smoking_1966_tuxedo_women_pantsuit_revolution",
                "question": "Why were women wearing YSL's Le Smoking tuxedo banned from high-end New York and Parisian restaurants in the late 1960s?",
                "key_focus": "The 1966 Autumn/Winter collection, Helmut Newton's iconic alleyway photograph, subverting masculine power codes, and Yves Saint Laurent's Rive Gauche ready-to-wear revolution.",
                "reason": "Documents the political and social liberation of women through the adaptation of menswear."
            },
            {
                "id": 10,
                "title": "Cristóbal Balenciaga: The Master of Us All and The Architecture of Fabric",
                "tier": "Tier 2: Haute Couture & Tailoring Epochs",
                "angle": "master_spotlight",
                "slug": "cristobal_balenciaga_master_of_us_all_architectural_cutting_gazar",
                "question": "Why did Christian Dior call Cristóbal Balenciaga 'the master of us all' and Coco Chanel claim he was the only true couturier capable of cutting and sewing his own fabric?",
                "key_focus": "Basque heritage, inventing silk Gazar fabric with Abraham textile mills, the sack dress, baby doll dress, and eliminating waistlines to flatter women of all ages.",
                "reason": "Celebrates the purest architect of haute couture whose radical geometries still influence design today."
            },
            {
                "id": 11,
                "title": "Japanese Denim: How Kurashiki Re-Engineered Vintage Levi's Better Than America",
                "tier": "Tier 3: Subcultural Streetwear & Avant-Garde",
                "angle": "craftsmanship_geography",
                "slug": "japanese_selvedge_denim_kkojima_kurashiki_vintage_shuttle_looms",
                "question": "Why did Japanese craftsmen buy vintage 1950s American Toyoda shuttle looms to create the world's most coveted selvedge raw denim?",
                "key_focus": "Kojima denim district, selvedge edge vs. modern projectile looms, natural indigo rope dyeing, slub and nep texture, and the raw denim fading subculture.",
                "reason": "A fascinating tale of cultural obsession, vintage preservation, and superior artisanal re-engineering."
            },
            {
                "id": 12,
                "title": "Rei Kawakubo and Comme des Garçons: The 1981 Paris Earthquake of Black and Holes",
                "tier": "Tier 3: Subcultural Streetwear & Avant-Garde",
                "angle": "avant_garde_revolutions",
                "slug": "rei_kawakubo_comme_des_garcons_1981_paris_debut_post_hiroshima_aesthetic",
                "question": "Why did French fashion critics scream in horror at Rei Kawakubo's 1981 debut of torn, asymmetrical, oversized black knitwear dubbed 'Hiroshima Chic'?",
                "key_focus": "Wabi-sabi imperfect aesthetics, deliberately loosening sewing machine tension to create moth-eaten knit holes, rejecting Western notions of sexiness, and Dover Street Market curation.",
                "reason": "The explosive moment when Eastern deconstruction smashed Western luxury conventions."
            },
            {
                "id": 13,
                "title": "Martin Margiela: The Invisible Designer Who Deconstructed Fashion Itself",
                "tier": "Tier 3: Subcultural Streetwear & Avant-Garde",
                "angle": "deconstructivism",
                "slug": "martin_margiela_blank_labels_tabi_boots_recycled_materials_anonymity",
                "question": "Why did Belgian genius Martin Margiela refuse to be photographed, use plain white stitched tags with no brand name, and dress models in mask hoods?",
                "key_focus": "The 1989 debut in a Parisian immigrant playground, the split-toe Tabi boot, Artisanal line using recycled flea-market seatbelts and gloves, and anti-celebrity ethos.",
                "reason": "Examines the cult anti-fashion prophet who anticipated 21st-century upcycling and brand skepticism."
            },
            {
                "id": 14,
                "title": "The Rise of Streetwear: How Stüssy, Supreme, and Skate Culture Took Over Luxury Paris",
                "tier": "Tier 3: Subcultural Streetwear & Avant-Garde",
                "angle": "cultural_mergers",
                "slug": "rise_of_streetwear_shawn_stussy_supreme_drop_model_louis_vuitton_collab",
                "question": "How did Shawn Stüssy scrawling his signature on surfboards in Laguna Beach lead to Supreme collaborating with Louis Vuitton on the Paris runway?",
                "key_focus": "Tribal community building, the scarcity-driven weekly drop model, hip-hop and skate crossover, and luxury conglomerates adopting streetwear merchandise logic.",
                "reason": "Chronicles the biggest commercial power shift in fashion: subculture conquering legacy luxury."
            },
            {
                "id": 15,
                "title": "Alexander McQueen: Savile Row Tailoring Meets Savage Romance and Dark Theatre",
                "tier": "Tier 3: Subcultural Streetwear & Avant-Garde",
                "angle": "theatrical_runway",
                "slug": "alexander_mcqueen_savage_beauty_bumsters_highland_rape_spray_paint_dress",
                "question": "How did a working-class East London boy become the visionary rebel of Givenchy and create runway spectacles that left fashion editors weeping?",
                "key_focus": "Savile Row apprentice cutting mastery, low-rise 'bumster' trousers shifting the torso line, Shalom Harlow sprayed by industrial robot arms (Spring 1999), and gothic macabre storytelling.",
                "reason": "Tribute to the tragic genius whose runway shows elevated fashion into supreme performance art."
            },
            {
                "id": 16,
                "title": "The Ultra-Fast Fashion Machine: How Shein and Zara Turned 6-Month Seasons into 3-Day Cycles",
                "tier": "Tier 4: Supply Chains, Sustainability & The Future",
                "angle": "supply_chain_logistics",
                "slug": "ultra_fast_fashion_shein_algorithm_guangzhou_micro_factories_zara",
                "question": "How do algorithmic scrapers and real-time micro-factories in Guangzhou produce 6,000 new garment designs every single day at under $10 a piece?",
                "key_focus": "Zara's Spanish short-lead production vs. Shein's algorithmic on-demand test-and-reorder model, direct-to-consumer air freight bypassing customs tariffs, and rapid obsolescence cycles.",
                "reason": "Exposes the staggering technical, economic, and logistical machinery driving global fast fashion."
            },
            {
                "id": 17,
                "title": "The Environmental Cost of Clothes: The Atacama Desert Clothes Mountain and Water Scarcity",
                "tier": "Tier 4: Supply Chains, Sustainability & The Future",
                "angle": "ecological_investigation",
                "slug": "environmental_cost_of_fashion_atacama_desert_garment_graveyard_aral_sea",
                "question": "Why can satellites in space see a mountain of discarded Western clothes in Chile's Atacama Desert, and why does one cotton T-shirt consume 2,700 liters of water?",
                "key_focus": "The drying of the Aral Sea for cotton irrigation, synthetic microplastic shedding into ocean food webs, synthetic polyester taking 500 years to decompose, and greenwashing claims.",
                "reason": "Unflinching investigative reality check on the catastrophic ecological price of disposable garments."
            },
            {
                "id": 18,
                "title": "The Circular Textile Revolution: Can Chemical Recycling Actually Close the Loop?",
                "tier": "Tier 4: Supply Chains, Sustainability & The Future",
                "angle": "sustainable_innovation",
                "slug": "circular_fashion_chemical_recycling_mycelium_leather_circulose_fiber",
                "question": "Why is recycling clothing into new clothing almost impossible today, and what breakthrough chemical enzymes can separate poly-cotton blends?",
                "key_focus": "Mechanical vs. chemical textile recycling, Circulose dissolving pulp from worn cotton, mushroom mycelium leather (Mylo), pineapple fiber (Piñatex), and closed-loop dyeing systems.",
                "reason": "Explores the cutting-edge biochemical innovations striving to build a truly circular garment economy."
            },
            {
                "id": 19,
                "title": "Archival Fashion: Why Collectors Pay $50,000 for Vintage Raf Simons and Helmut Lang",
                "tier": "Tier 4: Supply Chains, Sustainability & The Future",
                "angle": "collector_economics",
                "slug": "archival_fashion_raf_simons_riot_bomber_helmut_lang_grailed_investing",
                "question": "How did worn military bomber jackets from Raf Simons' 2001 'Riot Riot Riot' collection become six-figure investment assets traded like rare fine art?",
                "key_focus": "The rise of Grailed and vintage luxury platforms, hip-hop artists (A$AP Rocky, Travis Scott) driving archival clout, historical provenance tracking, and preservation ethics.",
                "reason": "Dissects the explosive collector economy where clothing from the 1990s and 2000s outperforms traditional stock portfolios."
            },
            {
                "id": 20,
                "title": "Digital Fashion and 3D Virtual Garments: Dressing Avatars in Zero-Waste Metaverse Couture",
                "tier": "Tier 4: Supply Chains, Sustainability & The Future",
                "angle": "future_horizons",
                "slug": "digital_fashion_clo3d_virtual_runways_hyper_customization_metaverse",
                "question": "If millions of people only dress up to take Instagram photos, why not buy digital 3D-rendered clothes that generate zero factory waste and ignore gravity?",
                "key_focus": "CLO 3D pattern software revolutionizing fashion sampling, AR filters fitting virtual garments in real-time video, digital-only luxury fashion houses, and on-demand zero-waste manufacturing.",
                "reason": "Capstones the curriculum by envisioning a future where digital self-expression decouples from physical environmental strain."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Luxury Quality Is Crashing: Inside the $3,000 Handbags Made from Cardboard and Glue",
                "tier": "Trending / High Retention",
                "angle": "luxury_debunk",
                "slug": "luxury_quality_collapse_tanner_leatherstein_deconstruction_chanel_dior",
                "trend_score": 98,
                "why_trending": "Tanner Leatherstein's viral YouTube and TikTok videos cutting open $3,000 Chanel and Prada bags to show cheap materials, bonded leather, and huge markups.",
                "reason": "Enormous global viewer fascination with tearing down luxury brand myths using hands-on craft forensics.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Quiet Luxury vs. Mob Wife Aesthetic: The Billionaire Stealth Wealth Trend Deconstructed",
                "tier": "Trending / High Retention",
                "angle": "cultural_trend_wars",
                "slug": "quiet_luxury_stealth_wealth_loro_piana_succession_vs_mob_wife_fur",
                "trend_score": 97,
                "why_trending": "The cultural explosion of 'Quiet Luxury' (Succession, Loro Piana $2,000 cashmere baseball caps) clashing violently with the flashy 'Mob Wife' animal print resurgence.",
                "reason": "Hilarious, insightful analysis of how social classes use subtle and loud wardrobe signals to signal status.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The Birkin Bag Waitlist Is a Lie: The Hermès Game and Secret Prespend Rules",
                "tier": "Trending / High Retention",
                "angle": "luxury_investigation",
                "slug": "hermes_birkin_bag_waitlist_myth_secret_prespend_ratio_lawsuit",
                "trend_score": 98,
                "why_trending": "Recent federal antitrust lawsuits in California alleging Hermès forces customers to buy thousands of dollars in scarves and plates before offering a Birkin.",
                "reason": "Explosive behind-the-scenes look into the most coveted luxury handbag on earth and the psychological sales manipulation behind it.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Why Fast Fashion Pants Have Fake Pockets: The Sexist History of Women's Clothing",
                "tier": "Trending / High Retention",
                "angle": "historical_quirks",
                "slug": "history_of_womens_pockets_why_fake_pockets_handbag_industry_conspiracy",
                "trend_score": 96,
                "why_trending": "Perennial viral anger and comedic videos asking why men's jeans can hold an iPad while women's jeans feature sewn-shut faux pocket seams.",
                "reason": "Universally shared frustration explaining the historic divergence between 18th-century tie-on pockets and modern purse marketing.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "How to Tell If Your Thrifted Clothes Are Actually Vintage in 30 Seconds",
                "tier": "Trending / High Retention",
                "angle": "thrifting_guide",
                "slug": "how_to_date_vintage_clothing_single_stitch_zippers_union_tags",
                "trend_score": 95,
                "why_trending": "Massive Gen Z thrifting and reselling community obsessing over single-stitch hems, Talon vs. YKK zippers, care label fonts, and ILGWU union tags.",
                "reason": "High-utility practical guide empowering thrift shoppers to spot valuable vintage garments instantly.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Fake Sneaker Capital of the World: Inside Putian, China's Underground Replica Factories",
                "tier": "Trending / High Retention",
                "angle": "counterfeit_underworld",
                "slug": "putian_china_fake_sneaker_capital_superfakes_jordan_replica_industry",
                "trend_score": 96,
                "why_trending": "Investigative documentaries showing Putian factories producing 'super-replicas' identical to real Nike Jordans down to the exact glue smell and UV barcode scans.",
                "reason": "Thrilling look into global sneakerhead obsession, grey-market supply chains, and industrial espionage.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Everyone Dressed the Same in the 2020s: The Death of Distinct Fashion Subcultures",
                "tier": "Trending / High Retention",
                "angle": "sociological_critique",
                "slug": "death_of_subcultures_tiktok_micro_trends_why_everyone_looks_the_same",
                "trend_score": 94,
                "why_trending": "Deep video essays dissecting how the TikTok algorithm converts subcultures into 2-week aesthetic micro-trends (Tomato Girl, Gorpcore, Clean Girl) before throwing them away.",
                "reason": "Resonant critique of modern social-media homogenization and the longing for authentic youth tribes.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "083_jewelry_precious_materials": {
        "id": "083",
        "slug": "jewelry_precious_materials",
        "title": "Jewelry & Precious Materials",
        "category": "Home_Living",
        "audience": "Gemologists, Metalsmiths, Luxury Collectors, Mineral Enthusiasts, Fine Jewelry Lovers (Global)",
        "progression": [
            ("Tier 1: Mineralogy, The 4 Cs & Precious Metals Metallurgy (Scratch / Beginner)",
             "Mohs hardness scale, diamond grading 4 Cs (Carat, Cut, Color, Clarity), gold karatage (24K to 10K alloys), sterling silver, and platinum density."),
            ("Tier 2: Gemstone Origins, Lapidary Faceting & Historic Jewelry Houses (Intermediate)",
             "Ruby, sapphire (corundum), and emerald (beryl) geology, brilliant vs. emerald vs. cabochon cuts, Cartier, Van Cleef & Arpels (Mystery Set), and Faberge imperial eggs."),
            ("Tier 3: Gemological Testing, Treatments & Forensic Authentication (Upper Intermediate)",
             "Heat treatments, fracture filling, refractive index and specific gravity testing, spectroscope identification, detecting lab-grown CVD/HPHT diamonds, and antique hallmarks."),
            ("Tier 4: Ethical Mining, Sovereign Wealth & High Jewelry Investment (Advanced / Expert)",
             "The Kimberley Process, artisanal vs. industrial gemstone mining, auction house provenance records (Sotheby's Magnificent Jewels), and precious material market cycles.")
        ],
        "flagship": {
            "title": "The Hope Diamond Curse and the Geology of Ultra-Rare Blue Diamonds",
            "angle": "historical_mineralogy",
            "slug": "083_jewelry_precious_materials_historical_mineralogy_hope_diamond_geology"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Hope Diamond Curse and the Geology of Ultra-Rare Blue Diamonds",
                "tier": "Tier 1: Mineralogy & Precious Metallurgy",
                "angle": "historical_mineralogy",
                "slug": "hope_diamond_geology_boron_impurities_red_phosphorescence_curse_myth",
                "question": "Why does the 45.52-carat Hope Diamond glow blood-red in the dark after exposure to UV light, and how did boron atoms from ancient ocean floors get trapped in its crystal lattice?",
                "key_focus": "Subduction of tectonic plates carrying oceanic boron 400 miles deep into Earth's mantle, Type IIb diamond categorization, red phosphorescence physics, and debunking the 1908 jeweler curse marketing myth.",
                "reason": "Flagship launch episode; weaves world-famous historical provenance with cutting-edge deep-mantle diamond geology."
            },
            {
                "id": 2,
                "title": "The 4 Cs of Diamonds: Carat, Cut, Color, and Clarity Demystified",
                "tier": "Tier 1: Mineralogy & Precious Metallurgy",
                "angle": "gemological_standards",
                "slug": "diamond_4cs_gia_grading_cut_proportions_internally_flawless_color_scale",
                "question": "Why can an 'Excellent Cut' 1-carat diamond look bigger and sparkle brighter than a poorly cut 1.5-carat diamond with higher clarity?",
                "key_focus": "The GIA (Gemological Institute of America) grading standards established by Robert Shipley, Marcel Tolkowsky's 1919 ideal cut mathematics, table percentage and depth ratio, and clarity inclusions (feathers, pinpoints).",
                "reason": "The universal standard benchmark every diamond buyer and collector must master."
            },
            {
                "id": 3,
                "title": "Gold Metallurgy: 24K, 18K, 14K, and The Chemistry of Rose and White Gold",
                "tier": "Tier 1: Mineralogy & Precious Metallurgy",
                "angle": "metallurgical_chemistry",
                "slug": "gold_alloys_karatage_white_gold_rhodium_plating_rose_gold_copper",
                "question": "Why is pure 24K gold too soft to hold a diamond securely, and why does white gold turn yellowish over time if you don't replug it with rhodium?",
                "key_focus": "Karat system fractions (parts per 24), alloying copper for rose gold, nickel/palladium for white gold, electroplated rhodium wear, density testing, and tarnish resistance.",
                "reason": "Explains the physical science and day-to-day durability of the world's most desired precious metal."
            },
            {
                "id": 4,
                "title": "Platinum vs. Gold: The King of Precious Metals and Its Brutal Melting Point",
                "tier": "Tier 1: Mineralogy & Precious Metallurgy",
                "angle": "comparative_metallurgy",
                "slug": "platinum_vs_gold_density_patina_melting_point_hypoallergenic_prongs",
                "question": "Why did Spanish conquistadors throw platinum into rivers thinking it was 'unripe gold,' and why is it superior for holding heirloom engagement diamonds?",
                "key_focus": "Extreme density (21.45 g/cm³), 1,768°C melting point requiring oxy-hydrogen torches, naturally white non-fading alloy (950 platinum), displaced metal patina vs. metal loss.",
                "reason": "Deconstructs why platinum commands unmatched technical respect among master bench jewelers."
            },
            {
                "id": 5,
                "title": "The Big Three Colored Gemstones: Ruby, Sapphire, and Emerald",
                "tier": "Tier 1: Mineralogy & Precious Metallurgy",
                "angle": "gemstone_mineralogy",
                "slug": "big_three_gemstones_corundum_ruby_sapphire_beryl_emerald_chromium",
                "question": "How can a red ruby and a blue sapphire be the exact same mineral (Corundum), while an emerald is an unstable beryl crystal born in tectonic trauma?",
                "key_focus": "Corundum (Al2O3) crystal lattice, trace chromium producing pigeon-blood red, iron and titanium creating royal blue, Beryl pegmatite geology, and emerald inclusions ('jardin').",
                "reason": "Foundational introduction to the three classic colored stones that hold historical market supremacy."
            },
            {
                "id": 6,
                "title": "The Art of Lapidary: How Master Faceters Turn Rough Rocks into Light Cannons",
                "tier": "Tier 2: Gemstone Origins & Historic Houses",
                "angle": "lapidary_craft",
                "slug": "lapidary_faceting_critical_angle_total_internal_reflection_brilliance",
                "question": "How does a lapidary use mathematics and rotating copper laps coated in diamond paste to make sure zero light leaks out the back of a gemstone?",
                "key_focus": "Refractive index (RI), Snell's Law, critical angle calculations, pavilion vs. crown angles, total internal reflection, step cuts vs. brilliant cuts, and cabochon polishing.",
                "reason": "Reveals the optical geometry that transforms cloudy, jagged river gravel into dazzling gemological jewels."
            },
            {
                "id": 7,
                "title": "Cartier and The Art Deco Revolution: Platinum, Tutti Frutti, and Royal Panthères",
                "tier": "Tier 2: Gemstone Origins & Historic Houses",
                "angle": "historic_jewelry_houses",
                "slug": "cartier_art_deco_tutti_frutti_panthere_jeanne_toussaint_platinum",
                "question": "How did Louis Cartier's pioneering use of platinum wire allow the creation of garland tiaras that looked like diamonds floating on air?",
                "key_focus": "The 1925 Paris Art Deco exposition, Tutti Frutti carved Indian emerald/ruby/sapphire necklaces, Jeanne Toussaint ('The Panther') creating the 3D diamond Panthère for the Duchess of Windsor.",
                "reason": "Examines the legendary maison dubbed 'the jeweler of kings and the king of jewelers'."
            },
            {
                "id": 8,
                "title": "Van Cleef & Arpels' Mystery Set: The Holy Grail of Invisible Stone Setting",
                "tier": "Tier 2: Gemstone Origins & Historic Houses",
                "angle": "proprietary_techniques",
                "slug": "van_cleef_arpels_mystery_set_serti_mysterieux_invisible_setting_grooves",
                "question": "How do jewelers set hundreds of rubies on a curved surface with zero visible prongs or metal holding them from above?",
                "key_focus": "The 1933 Serti Mystérieux patent, cutting micro-grooves into the pavilion of calibrated square-cut rubies, sliding stones onto hidden gold rails, and 300+ hours per flower brooch.",
                "reason": "Deep-dives into what is universally acknowledged as the most technically complex jewelry setting technique in the world."
            },
            {
                "id": 9,
                "title": "Fabergé Imperial Eggs: The Mechanical Enameling Miracles of the Romanov Dynasty",
                "tier": "Tier 2: Gemstone Origins & Historic Houses",
                "angle": "imperial_masterpieces",
                "slug": "faberge_imperial_eggs_guilloche_enamel_romanov_easter_surprises",
                "question": "How did Peter Carl Fabergé create 50 unique imperial Easter eggs containing clockwork peacocks and miniature golden trains before the Russian Revolution?",
                "key_focus": "Guilloché engine-turned engraving, multiple firings of translucent vitreous enamel at 800°C, master workmaster Mikhail Perkhin, and the dispersal of the eggs after 1917.",
                "reason": "Celebrates the pinnacle of decorative goldsmithing, lapidary engineering, and tragic imperial history."
            },
            {
                "id": 10,
                "title": "Mogul Kundan and Meenakari: The Unmatched Enamel and Gemcraft of Mughal India",
                "tier": "Tier 2: Gemstone Origins & Historic Houses",
                "angle": "traditional_world_jewelry",
                "slug": "mughal_kundan_meenakari_jadau_hyper_pure_gold_foil_gem_setting",
                "question": "How did Mughal royal court jewelers set uncut diamonds into solid gold using pure 24K room-temperature gold foil and secret reverse-side enameling?",
                "key_focus": "Kundan technique (layering purified 24K gold ribbons that fuse cold through molecular pressure), Meenakari vitreous enameling on reverse sides, Polki uncut diamonds, and Shah Jahan's treasures.",
                "reason": "Explores the opulent South Asian royal jewelry technique unmatched in European goldsmithing."
            },
            {
                "id": 11,
                "title": "Gemstone Treatments: Heating, Oiling, Irradiation, and What Must Be Disclosed",
                "tier": "Tier 3: Gemological Testing & Forensics",
                "angle": "gemological_treatments",
                "slug": "gemstone_treatments_heat_treated_sapphires_cedarwood_oil_emeralds",
                "question": "Why are 95% of all sapphires on the market baked in high-temperature ovens at 1,800°C, and why does an untreated sapphire cost 500% more?",
                "key_focus": "High-temperature heating diffusing titanium, fracture filling with lead glass in rubies, cedarwood oil and resin in emerald fissures, irradiation creating blue topaz, and GIA disclosure ethics.",
                "reason": "Crucial consumer and collector education on separating natural unheated gems from laboratory-altered stones."
            },
            {
                "id": 12,
                "title": "Lab-Grown vs. Natural Diamonds: CVD, HPHT, and The Great Market Disruption",
                "tier": "Tier 3: Gemological Testing & Forensics",
                "angle": "synthetic_disruptions",
                "slug": "lab_grown_diamonds_cvd_vs_hpht_spectroscopy_carbon_lattice_price_crash",
                "question": "If a lab-grown diamond is 100% pure carbon with the identical crystal structure, refractive index, and hardness of an earth-mined diamond, how can machines tell them apart?",
                "key_focus": "HPHT (High Pressure High Temperature) simulating Earth's mantle vs. CVD (Chemical Vapor Deposition) growing diamond films from methane gas plasma, UV photoluminescence detection, and the 80% price crash.",
                "reason": "Covers the greatest technological earthquake to hit the global diamond industry in 150 years."
            },
            {
                "id": 13,
                "title": "Forensic Gemology: Refractometers, Polariscopes, and Specific Gravity",
                "tier": "Tier 3: Gemological Testing & Forensics",
                "angle": "laboratory_forensics",
                "slug": "gemological_instruments_refractometer_polariscope_specific_gravity_fluorescence",
                "question": "How can a gemologist identify an unknown red stone without scratching it or damaging it in under 60 seconds?",
                "key_focus": "Total shadow line on a critical angle refractometer, polariscope testing for isotropic vs. anisotropic double refraction, hydrostatic specific gravity weighing, and Raman spectroscopy.",
                "reason": "The core diagnostic tool kit and scientific testing principles of certified gemological laboratories."
            },
            {
                "id": 14,
                "title": "Antique Hallmarks: Decoding 500 Years of Goldsmith Stamps, Assay Marks, and Purity",
                "tier": "Tier 3: Gemological Testing & Forensics",
                "angle": "historical_hallmarks",
                "slug": "antique_jewelry_hallmarks_assay_offices_london_leopard_date_letters",
                "question": "How can four tiny stamped symbols inside a vintage ring tell you the exact year, city, goldsmith, and gold purity from 1782?",
                "key_focus": "The London Assay Office leopard's head, British hallmark system (maker's mark, fineness standard, assay office, date letter), French eagle head for 18K gold, and detecting forged antique stamps.",
                "reason": "The essential authentication guide for antique jewelry pickers, collectors, and auction house specialists."
            },
            {
                "id": 15,
                "title": "Pearls: The Only Gem Created by a Living Organism and The Kokichi Mikimoto Miracle",
                "tier": "Tier 3: Gemological Testing & Forensics",
                "angle": "organic_gems",
                "slug": "pearl_science_kokichi_mikimoto_cultured_pearls_nacre_akoya_south_sea",
                "question": "How did a Japanese noodle merchant's son figure out how to implant mother-of-pearl nucleus beads into live oysters and crash the global natural pearl market?",
                "key_focus": "Natural vs. cultured pearls, mantle tissue grafting, calcium carbonate aragonite platelets and conchiolin nacre, Akoya vs. South Sea vs. Tahitian black pearls, and luster orient.",
                "reason": "Chronicles the biology, craftsmanship, and historic market collapse that democratized pearls."
            },
            {
                "id": 16,
                "title": "The Blood Diamond Reality: The Kimberley Process and Conflict Mineral Supply Chains",
                "tier": "Tier 4: Ethical Mining, Wealth & Markets",
                "angle": "geopolitical_ethics",
                "slug": "blood_diamonds_kimberley_process_sierra_leone_conflict_free_flaws",
                "question": "Did the 2003 Kimberley Process actually eliminate conflict diamonds from war zones, or does systemic corruption allow uncertified stones to enter global hubs?",
                "key_focus": "Civil wars in Sierra Leone and Angola, RUF rebel funding, Kimberley Process Certification Scheme mechanics, smuggling pipelines through transit nations, and the rise of blockchain provenance tracking.",
                "reason": "Unflinching geopolitical investigation into the human rights and ethical supply chain realities behind diamonds."
            },
            {
                "id": 17,
                "title": "Artisanal Gemstone Mining: Inside the Ratnapura Gem Pits of Sri Lanka and Mogok, Myanmar",
                "tier": "Tier 4: Ethical Mining, Wealth & Markets",
                "angle": "field_gemology",
                "slug": "artisanal_gem_mining_sri_lanka_ratnapura_alluvial_illam_burma_mogok",
                "question": "How do artisanal miners in Sri Lanka and Myanmar dig 50-foot bamboo-supported mud pits by hand to wash gravel for million-dollar Padparadscha sapphires?",
                "key_focus": "Alluvial Illam gravel washing, traditional water-wheel pit dewatering, Mogok Valley marble-hosted ruby deposits, ethical artisanal cooperative mining, and the field gemology journey.",
                "reason": "Brings viewers directly to the rugged, muddy frontier where precious gemstones are pulled from the earth."
            },
            {
                "id": 18,
                "title": "Sotheby's and Christie's: Anatomy of an Auction Record for Magnificent Jewels",
                "tier": "Tier 4: Ethical Mining, Wealth & Markets",
                "angle": "auction_market_dynamics",
                "slug": "sothebys_christies_magnificent_jewels_pink_star_oppenheimer_blue_records",
                "question": "How did the 59.60-carat 'Pink Star' diamond sell for $71.2 million, and what hidden auction guarantees, paddle codes, and buyer's premiums operate behind closed doors?",
                "key_focus": "The Pink Star and Oppenheimer Blue auctions, third-party irrevocable bids, chandelier bidding mechanics, royal provenance premiums, and high jewelry as portable wealth insurance.",
                "reason": "An exclusive look inside the ultra-elite auction rooms where sovereign wealth funds and billionaires trade portable gem fortunes."
            },
            {
                "id": 19,
                "title": "Extreme Materials: Meteorite Dials, Damascus Titanium, and Tantalum in Modern Jewelry",
                "tier": "Tier 4: Ethical Mining, Wealth & Markets",
                "angle": "space_age_materials",
                "slug": "space_age_jewelry_materials_gibeon_meteorite_widmanstatten_tantalum_timascus",
                "question": "Why are luxury jewelers and watchmakers using 4-billion-year-old nickel-iron asteroid slices and refractory metals that require aerospace laser sintering?",
                "key_focus": "Gibeon meteorite Widmanstätten crystal cross-hatch etchings, Timascus (pattern-welded titanium), hypoallergenic tantalum, carbon fiber forging, and the democratization of non-traditional luxury.",
                "reason": "Showcases how modern metallurgy combines extraterrestrial iron and aerospace refractory metals with fine jewelry."
            },
            {
                "id": 20,
                "title": "The Future of Fine Jewelry: Molecular Diamond Synthesis, Laser Welding, and Ethical Traceability",
                "tier": "Tier 4: Ethical Mining, Wealth & Markets",
                "angle": "future_horizons",
                "slug": "future_of_jewelry_laser_welding_3d_wax_printing_blockchain_provenance",
                "question": "How are 3D wax printers, pulse laser bench welders, and DNA-tagged gemstone nanotechnology reshaping jewelry making for the next century?",
                "key_focus": "Stereolithography 3D resin wax printing replacing hand carving, micro-laser welders allowing repairs next to heat-sensitive stones without unsetting, and immutable laser-inscribed QR serials.",
                "reason": "Capstones the curriculum by harmonizing 5,000 years of traditional goldsmithing with space-age digital precision."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Natural Diamonds Lost 50% of Their Value: The Lab-Grown Diamond Price War",
                "tier": "Trending / High Retention",
                "angle": "market_crash_analysis",
                "slug": "natural_diamond_price_crash_de_beers_lightbox_lab_grown_disruption",
                "trend_score": 98,
                "why_trending": "De Beers slashing prices and diamond market indices dropping sharply as couples overwhelmingly choose identical 3-carat lab-grown diamonds for $1,500 instead of $15,000.",
                "reason": "Massive real-time financial and consumer interest in the greatest market disruption in luxury jewelry history.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "The $10 Diamond Tester Hack: Why Moissanite Fools Every Pawn Shop Pen",
                "tier": "Trending / High Retention",
                "angle": "gadget_debunk",
                "slug": "cheap_diamond_tester_pen_flaws_thermal_vs_electrical_conductivity_moissanite",
                "trend_score": 97,
                "why_trending": "Viral TikTok and YouTube shorts showing cheap $15 handheld thermal diamond tester pens beeping positive on synthetic moissanite and fake stones.",
                "reason": "High-retention gadget debunking explaining thermal conductivity vs. electrical conductivity and double refraction.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Why Titanium and Tungsten Wedding Rings Can't Be Cut Off in Emergencies (Myth vs. Fact)",
                "tier": "Trending / High Retention",
                "angle": "medical_emergency_myths",
                "slug": "tungsten_titanium_rings_emergency_room_myths_vise_grip_cracking",
                "trend_score": 96,
                "why_trending": "Urgent, viral debates among men regarding whether buying an unbreakable tungsten carbide or titanium wedding band will cost them their finger in an ER room.",
                "reason": "Fascinating material science demonstrating how ER doctors use standard vise grips to instantly shatter brittle tungsten rings safely.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Koh-i-Noor Diamond: The Stolen 105-Carat Gem That Britain Refuses to Return",
                "tier": "Trending / High Retention",
                "angle": "geopolitical_heritage",
                "slug": "koh_i_noor_diamond_curse_queen_victoria_tower_of_london_india_repatriation",
                "trend_score": 97,
                "why_trending": "Heated diplomatic discussions and cultural controversies during the coronation of King Charles III surrounding the Queen Mother's crown and the Koh-i-Noor.",
                "reason": "High-conflict historical investigation into imperial loot, the Hindu male curse legend, and modern repatriation demands.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "How to Clean Cloudy Diamonds at Home: Why Ultrasonic Cleaners Destroy Emeralds",
                "tier": "Trending / High Retention",
                "angle": "jewelry_maintenance",
                "slug": "how_to_clean_fine_jewelry_at_home_why_ultrasonic_destroys_emeralds_opals",
                "trend_score": 95,
                "why_trending": "Viral cleaning videos showing sparkling ring transformations, alongside horrifying cautionary tales of shattered emeralds and fractured opals in ultrasonic baths.",
                "reason": "High-utility everyday advice explaining cavitation vibrations, thermal shock, and safe dish-soap cleaning techniques.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Cursed Black Orlov: The Diamond That Made Its Owners Jump Off Buildings",
                "tier": "Trending / High Retention",
                "angle": "dark_history",
                "slug": "black_orlov_diamond_curse_eye_of_brahma_suicide_legends_provenance",
                "trend_score": 94,
                "why_trending": "Perennial fascination with the 67.50-carat cushion-cut black diamond allegedly plucked from the eye of a Hindu idol in Pondicherry leading to mysterious suicides.",
                "reason": "Irresistible blend of mystery, luxury, and debunking sensationalist 20th-century jewelry press exaggerations.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Silver Tarnishes and Gold Doesn't: The Electrochemistry of Dark Patina",
                "tier": "Trending / High Retention",
                "angle": "everyday_science",
                "slug": "why_sterling_silver_tarnishes_sulfur_silver_sulfide_baking_soda_aluminum_hack",
                "trend_score": 95,
                "why_trending": "Viral life hack videos showing boiling water, baking soda, and aluminum foil instantly reversing silver tarnish through an electrochemical reduction circuit.",
                "reason": "Super satisfying visual science demonstration that solves a common household headache in under 2 minutes.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "084_collectibles_antiques": {
        "id": "084",
        "slug": "collectibles_antiques",
        "title": "Collectibles & Antiques",
        "category": "Cultural_Heritage",
        "audience": "Antique Collectors, Pickers, Estate Appraisers, Memorabilia Enthusiasts, Auction Watchers (Global)",
        "progression": [
            ("Tier 1: The Collector's Eye: Identifying Periods, Patina & Basic Valuation (Scratch / Beginner)",
             "Victorian, Edwardian, Art Nouveau, and Mid-Century Modern design cues, authentic wood patina vs. fake wear, hallmarks and maker's marks."),
            ("Tier 2: Pop Culture Memorabilia: Trading Cards, Comic Books & Vintage Toys (Intermediate)",
             "PSA/CGC grading standards (centering, corners, edges, surface), condition scarcity, first appearance comics (Action Comics #1), and pristine unopened toy packaging value."),
            ("Tier 3: Estate Appraisals, Authentication Science & Provenance Tracking (Upper Intermediate)",
             "Blacklight UV testing for glue and repainting, dendrochronology and radiocarbon dating of timber, paper watermarks, and tracking bills of sale through historic registries."),
            ("Tier 4: The Psychology of Collecting, Auction House Dynamics & Alternate Asset Classes (Advanced / Expert)",
             "Jean Baudrillard's 'System of Objects', speculative collector bubbles (Beanie Babies to NFTs), hammer price psychology, and luxury collectibles as inflation hedges.")
        ],
        "flagship": {
            "title": "The Science of Patina: How to Tell Real 200-Year-Old Wear from Artificial Aging",
            "angle": "forensic_identification",
            "slug": "084_collectibles_antiques_forensic_identification_science_of_patina"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Science of Patina: How to Tell Real 200-Year-Old Wear from Artificial Aging",
                "tier": "Tier 1: The Collector's Eye & Periods",
                "angle": "forensic_identification",
                "slug": "science_of_patina_authentic_wood_wear_micro_shrinkage_fake_antiques",
                "question": "How do expert appraisers instantly tell whether the dark patina on an 18th-century mahogany desk is 250 years of oxidized beeswax or brown shoe polish applied yesterday?",
                "key_focus": "Chemical oxidation of lignin, directional pocket wear on chair rungs, hand-planed tool chatter marks vs. circular saw grooves, wood shrinkage along the grain creating oval dowels.",
                "reason": "Flagship launch episode; teaches the fundamental diagnostic skill separating genuine antique treasures from cheap distress-job reproductions."
            },
            {
                "id": 2,
                "title": "Antique Furniture Periods: Identifying Chippendale, Victorian, and Mid-Century Modern",
                "tier": "Tier 1: The Collector's Eye & Periods",
                "angle": "design_history",
                "slug": "antique_furniture_periods_chippendale_cabriole_legs_victorian_eames",
                "question": "What is the giveaway difference between an English Queen Anne cabriole leg, a Victorian Eastlake relief carving, and a 1950s molded plywood Eames chair?",
                "key_focus": "Thomas Chippendale ball-and-claw feet, Hepplewhite shield backs, Victorian industrial machine ornamentation, Art Nouveau whip-lash curves, and Mid-Century Modern teak simplicity.",
                "reason": "The essential architectural field guide for identifying furniture eras at flea markets and estate sales."
            },
            {
                "id": 3,
                "title": "Porcelain and Pottery Marks: Decoding Meissen Crossed Swords and Wedgwood Basalt",
                "tier": "Tier 1: The Collector's Eye & Periods",
                "angle": "maker_marks",
                "slug": "porcelain_pottery_marks_meissen_crossed_swords_wedgwood_transferware",
                "question": "How did European kings bankrupt themselves trying to crack the secret of Chinese hard-paste porcelain, and how do you read the blue underglaze marks on the base?",
                "key_focus": "Meissen crossed swords, Sèvres royal interlaced Ls, Josiah Wedgwood's black basalt and Jasperware, flow blue transferware, and detecting stamped fake maker's marks.",
                "reason": "Unlocks the centuries-old history of European ceramics and the tiny underglaze hallmarks that determine value."
            },
            {
                "id": 4,
                "title": "Antique Glassware: Spotting Uranium Glass, Carnival Iridescence, and Depression Glass",
                "tier": "Tier 1: The Collector's Eye & Periods",
                "angle": "material_identification",
                "slug": "antique_glassware_uranium_glass_uv_fluorescence_carnival_depression_glass",
                "question": "Why does green Depression-era Uranium glass glow neon bright under a 395nm blacklight, and why was Carnival glass originally given away as carnival prizes?",
                "key_focus": "Diuranate glass chemistry and harmless low-level alpha radiation, Fenton carnival metallic spray iridescence, Depression glass mold lines and pastel colors, and pontil mark scars on blown glass.",
                "reason": "One of the most active and viral collector subcultures with visually dramatic blacklight testing."
            },
            {
                "id": 5,
                "title": "Antique Clocks: Escapements, Pendulums, and The Mechanism of Centuries",
                "tier": "Tier 1: The Collector's Eye & Periods",
                "angle": "horological_antiques",
                "slug": "antique_clocks_deadbeat_escapement_grandfather_clocks_black_forest_cuckoo",
                "question": "How can you date a tall-case Grandfather clock by looking at its brass pendulum escapement and whether the dial is hand-painted iron or engraved brass?",
                "key_focus": "Deadbeat escapement accuracy, fusee chain movements, Black Forest carved cuckoo clocks, weight-driven vs. spring-driven barrels, and recognizing reproduction quartz movements.",
                "reason": "Explores the mechanical majesty of antique horology where precision clockwork meets fine furniture craftsmanship."
            },
            {
                "id": 6,
                "title": "Trading Card Grading: The Difference Between a PSA 9 and a $1,000,000 PSA 10",
                "tier": "Tier 2: Pop Culture Memorabilia",
                "angle": "condition_grading",
                "slug": "trading_card_grading_psa_bgs_centering_micro_creases_hologram_scratches",
                "question": "How can a 55/45 centering offset invisible to the naked eye cut the value of a 1999 1st Edition Charizard or 1952 Mickey Mantle card by 80%?",
                "key_focus": "Professional Sports Authenticator (PSA) vs. Beckett (BGS) sub-grades, 10x magnification corner whitening inspection, surface foil scratches, tamper-proof ultrasonic sonic slabs.",
                "reason": "The defining condition science governing the multi-billion-dollar modern trading card investment industry."
            },
            {
                "id": 7,
                "title": "Comic Book Anatomy: Golden Age Grails, CGC Slabs, and The Danger of Restoration",
                "tier": "Tier 2: Pop Culture Memorabilia",
                "angle": "comic_collecting",
                "slug": "comic_book_grading_action_comics_1_cgc_restoration_purple_label_scarcity",
                "question": "Why does professionally repairing a torn cover with archival tape give a comic book a dreaded 'Purple Label' and destroy half its auction value?",
                "key_focus": "Golden Age (Action Comics #1) vs. Silver Age (Amazing Fantasy #15), Certified Guaranty Company (CGC) 10-point scale, page micro-chamber paper preservation, and unrestored original condition.",
                "reason": "Covers the pinnacle of pop-culture paper ephemera and the strict preservation ethics of serious comic archives."
            },
            {
                "id": 8,
                "title": "Vintage Toys: The Holy Grail of Mint on Sealed Card (MOSC) Kenner Star Wars",
                "tier": "Tier 2: Pop Culture Memorabilia",
                "angle": "toy_collecting",
                "slug": "vintage_star_wars_toys_kenner_1977_cardback_yellowed_bubble_prototypes",
                "question": "Why is a 3.75-inch piece of 1977 molded plastic worth $50 loose, but $25,000 if it's still glued to a piece of cardboard with an unpunched peg hole?",
                "key_focus": "Kenner 12-back card packaging, bubble yellowing from UV light and bromine fire retardants, AFA toy grading standards, vinyl cape Jawa variants, and unreleased rocket-firing Boba Fett prototypes.",
                "reason": "Dissects the massive nostalgia economy where childhood playthings become blue-chip auction trophies."
            },
            {
                "id": 9,
                "title": "Vintage Vinyl Records: First Pressings, Dead Wax Runout Matrix Codes, and Blue Note Jazz",
                "tier": "Tier 2: Pop Culture Memorabilia",
                "angle": "music_memorabilia",
                "slug": "vintage_vinyl_records_first_pressings_dead_wax_matrix_codes_blue_note",
                "question": "How do you read the hand-scratched letters in the runout groove of an LP record to prove it came off the original stamper at Abbey Road in 1969?",
                "key_focus": "Dead wax matrix numbers, Rudy Van Gelder 'RVG' stamps on Blue Note jazz, deep groove pressing rings, Goldmine grading standards (Mint, NM, VG+), and mono vs. stereo mixes.",
                "reason": "A masterclass for record collectors on authenticating original first pressings over modern digitally remastered reissues."
            },
            {
                "id": 10,
                "title": "Classic Car Memorabilia: Automobilia, Enamel Gas Signs, and Garage Relics",
                "tier": "Tier 2: Pop Culture Memorabilia",
                "angle": "automobilia",
                "slug": "automobilia_porcelain_enamel_gas_signs_route_66_pump_globes_fakes",
                "question": "Why do original 1930s Route 66 and Sinclair Dino porcelain enamel pump signs sell for $30,000+, and how do you spot modern laser-printed rust fakes?",
                "key_focus": "Multi-layer vitreous porcelain baked on heavy-gauge steel, authentic chipping revealing dark primer vs. acid-etched fake rust, glass gas pump globes, and car dealership neon signs.",
                "reason": "Explores the booming, hyper-masculine subculture of high-dollar garage and petroliana collecting."
            },
            {
                "id": 11,
                "title": "Blacklight Forensics: Using Ultraviolet Light to Unmask Repairs, Glues, and Modern Paint",
                "tier": "Tier 3: Estate Appraisals & Authentication",
                "angle": "forensic_tools",
                "slug": "blacklight_forensics_antiques_uv_light_glue_fluorescence_infilled_cracks",
                "question": "Why does a 365nm UV flashlight make invisible porcelain repairs, touch-up oil paint, and modern synthetic glues glow like radioactive green beacons?",
                "key_focus": "Differential fluorescence of aged natural varnish vs. modern polymers, invisible restoration on Chinese vases, optical brighteners in post-1950s paper, and jade authentication.",
                "reason": "The essential, portable field-forensics tool every serious antique picker carries in their pocket."
            },
            {
                "id": 12,
                "title": "Dendrochronology in Antiques: How Tree Rings Date Wooden Chests and Stradivarius Violins",
                "tier": "Tier 3: Estate Appraisals & Authentication",
                "angle": "scientific_dating",
                "slug": "dendrochronology_tree_ring_dating_stradivarius_violins_historic_furniture",
                "question": "How can counting and measuring microscopic tree-growth rings on the soundboard of a violin prove it was crafted from spruce cut in 1696?",
                "key_focus": "Tree-ring master chronology curves, heartwood vs. sapwood felling dates, validating Antonio Stradivari's Alpine spruce sources, and detecting 19th-century Victorian fakes of medieval chests.",
                "reason": "The definitive botanical science used by major auction houses to provide absolute, irrefutable dating."
            },
            {
                "id": 13,
                "title": "The Paper Trail: Watermarks, Chain Lines, and Authenticating Historic Documents",
                "tier": "Tier 3: Estate Appraisals & Authentication",
                "angle": "manuscript_authentication",
                "slug": "historic_document_authentication_watermarks_laid_paper_iron_gall_ink",
                "question": "How do you distinguish an original 1776 printing of the Declaration of Independence from the millions of brown antiqued souvenir parchment copies sold in gift shops?",
                "key_focus": "Handmade rag laid paper with visible wire chain lines, wire watermarks held to the light, chemical degradation of acidic iron gall ink, and letterpress bite impressions.",
                "reason": "Teaches historical literacy and paper diagnostics to avoid the most common tourist document scams."
            },
            {
                "id": 14,
                "title": "Estate Sale Hunting: The Picker's Playbook for Spotting Hidden Treasure in Attics",
                "tier": "Tier 3: Estate Appraisals & Authentication",
                "angle": "field_picking",
                "slug": "estate_sale_picking_playbook_basement_attic_hunting_undervalued_antiques",
                "question": "Why do the best estate sale pickers head straight for the dirty basement workbench or attic boxes instead of the polished dining room display cabinet?",
                "key_focus": "Spotting cast iron cookware (Griswold, Wagner), vintage mid-century barware, old fountain pens with 14K gold nibs, early electronic audio gear, and estate tag negotiation psychology.",
                "reason": "A deeply practical, tactical guide for anyone looking to hunt treasures and flip undervalued goods."
            },
            {
                "id": 15,
                "title": "Military Relics and Militaria: Authenticating Helmets, Medals, and Trench Art",
                "tier": "Tier 3: Estate Appraisals & Authentication",
                "angle": "military_antiques",
                "slug": "militaria_authenticating_wwii_helmets_medals_trench_art_fake_decals",
                "question": "Why is the WWII German helmet market flooded with 90% modern replicas, and how do you test for authentic rolled steel edges and original factory paint?",
                "key_focus": "M35 vs. M40 vs. M42 helmet stampings, batch lot numbers, original decal micro-crazing, trench art hammered brass artillery shells from WWI, and military medal provenance.",
                "reason": "Navigates one of the most minefield-ridden, lucrative, and forgery-plagued niches in collecting."
            },
            {
                "id": 16,
                "title": "Jean Baudrillard and The System of Objects: Why Humans Are Obsessed with Owning the Past",
                "tier": "Tier 4: Psychology, Bubbles & Alternate Assets",
                "angle": "collector_psychology",
                "slug": "jean_baudrillard_system_of_objects_psychology_of_collecting_nostalgia_mortality",
                "question": "Why do collectors feel intense anxiety until they complete a full set, and does collecting objects reflect a subconscious human terror of mortality?",
                "key_focus": "Baudrillard's 1968 treatise, the object as a surrogate lover, psychological completion compulsion, nostalgia as emotional armor against aging, and the collector vs. hoarder boundary.",
                "reason": "The supreme philosophical exploration of why humans spend fortunes gathering material artifacts."
            },
            {
                "id": 17,
                "title": "The Beanie Baby Bubble: How 1990s Suburban America Lost Its Mind Over $5 Plush Toys",
                "tier": "Tier 4: Psychology, Bubbles & Alternate Assets",
                "angle": "speculative_bubbles",
                "slug": "beanie_baby_bubble_ty_warner_manufactured_scarcity_suburban_mania",
                "question": "How did Ty Warner's intentional retirement of plush stuffed bears convince middle-class families that $5 toys would fund their children's college education?",
                "key_focus": "Manufactured scarcity, the birth of early eBay speculative auctions, price guides quoting Princess Di bears at $10,000, the psychological mechanics of mania, and the inevitable 1999 crash.",
                "reason": "The quintessential case study in speculative frenzy that foretold modern meme stocks, sneaker flips, and crypto hype."
            },
            {
                "id": 18,
                "title": "The Hammer Price: Inside Auction House Psychology, Chandelier Bidding, and Reserves",
                "tier": "Tier 4: Psychology, Bubbles & Alternate Assets",
                "angle": "auction_mechanics",
                "slug": "auction_house_mechanics_chandelier_bidding_reserve_prices_buyers_premium",
                "question": "How do auctioneers legally bid against the wall ('chandelier bidding') to drive up prices until the hidden reserve price is met?",
                "key_focus": "Consignment contracts, low-ball estimates encouraging bidding wars, the 25% buyer's premium surcharge, telephone bidding choreography, and the winner's curse phenomenon.",
                "reason": "Demystifies the theatrical tricks and legal mechanisms used by auction houses to extract maximum bids."
            },
            {
                "id": 19,
                "title": "Collectibles as an Asset Class: Inflation Hedges, Capital Gains Taxes, and Custodial Storage",
                "tier": "Tier 4: Psychology, Bubbles & Alternate Assets",
                "angle": "financial_investing",
                "slug": "collectibles_as_asset_class_inflation_hedges_tax_rates_vault_storage",
                "question": "Can rare stamps, vintage Rolex watches, and classic Ferraris genuinely beat the S&P 500, or do insurance, storage, and 28% collectible tax rates eat all your gains?",
                "key_focus": "Knight Frank Luxury Investment Index, illiquidity risks, high IRS collectible capital gains tax (28% vs 20% ordinary capital gains), climate-controlled vault storage fees, and authentication insurance.",
                "reason": "A sober, financially literate analysis of treating physical hobbies as diversified investment portfolios."
            },
            {
                "id": 20,
                "title": "The Future of Antiques: The Death of Brown Furniture and The Rise of Digital Curation",
                "tier": "Tier 4: Psychology, Bubbles & Alternate Assets",
                "angle": "future_horizons",
                "slug": "future_of_antiques_death_of_brown_furniture_millennial_minimalism_digital_nfts",
                "question": "Why can you buy a 200-year-old solid mahogany dining table today for less than an IKEA flat-pack table, and what will people collect 50 years from now?",
                "key_focus": "Millennial downsizing and small urban apartments rejecting heavy 'brown furniture', the explosion of 1980s/90s plastic pop culture nostalgia, provenance tracking, and the enduring human love for tactile history.",
                "reason": "Capstones the master curriculum by analyzing generational shifts and predicting the next century of collecting."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The $5 Thrift Store Bowl That Sold for $37 Million: Inside the Ru Ware Discovery",
                "tier": "Trending / High Retention",
                "angle": "viral_jackpot_finds",
                "slug": "ru_ware_chinese_ceramic_thrift_store_jackpot_sothebys_37_million",
                "trend_score": 98,
                "why_trending": "Massive viral curiosity around real-life yard sale finds turning into multi-million dollar Chinese Song Dynasty ceramics at international auction houses.",
                "reason": "The ultimate picker's fantasy hook blending everyday garage hunting with astronomical wealth.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why You Should Never Clean Antique Coins: How One Polish Job Erases $50,000",
                "tier": "Trending / High Retention",
                "angle": "costly_mistakes",
                "slug": "never_clean_antique_coins_harsh_abrasives_micro_scratches_erasing_value",
                "trend_score": 97,
                "why_trending": "Viral Antiques Roadshow clips and numismatic videos showing devastated owners finding out that scrubbing their old silver dollar with baking soda destroyed 90% of its value.",
                "reason": "Instant high-retention cautionary lesson explaining mint luster, hairline abrasions, and original toning.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The Pokemon Card Heist Epidemic: Why Comic Shops Are Getting Smashed and Grabbed",
                "tier": "Trending / High Retention",
                "angle": "true_crime_collectibles",
                "slug": "pokemon_card_heists_hobby_shops_smash_and_grab_untraceable_cash",
                "trend_score": 96,
                "why_trending": "Spike in high-profile burglaries targeting graded vintage Pokémon booster boxes and cards across Japan, the US, and Europe due to portable untraceable value.",
                "reason": "Gripping true-crime story showcasing how trading cards became as targetable as diamond jewelry.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Cast Iron Pan Hunting: Why Griswold Skillets with the 'Slanted Logo' Are Pure Gold",
                "tier": "Trending / High Retention",
                "angle": "culinary_antiques",
                "slug": "cast_iron_pan_collecting_griswold_slanted_logo_erie_smooth_seasoning",
                "trend_score": 95,
                "why_trending": "Huge cooking and thrift community obsessing over vintage Erie Griswold and Wagner skillets that are lighter and smoother than modern rough Lodge pans.",
                "reason": "Everyday accessible collecting with immense practical utility in the kitchen.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Flea Market Scams: 5 Fake Antiques Flooding Modern Antique Malls",
                "tier": "Trending / High Retention",
                "angle": "buyer_warnings",
                "slug": "flea_market_scams_fake_cast_iron_mechanical_banks_aged_brass_signs",
                "trend_score": 96,
                "why_trending": "Consumer warning videos exposing modern cast iron mechanical piggy banks, fake aged brass belt buckles, and artificial distressing made in overseas factories.",
                "reason": "Eye-opening protective guide that saves viewers hundreds of dollars on their weekend antique trips.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Antiques Roadshow Best Reactions: Tears, Shaking Hands, and Total Shock",
                "tier": "Trending / High Retention",
                "angle": "human_interest",
                "slug": "antiques_roadshow_best_reactions_rolex_daytona_navajo_blanket_tears",
                "trend_score": 94,
                "why_trending": "Perennially beloved viral compilations of veterans collapsing in disbelief when an untouched $300 Vietnam-era Rolex Daytona is appraised at $700,000.",
                "reason": "Emotional, wholesome human drama celebrating ordinary working people discovering life-changing treasures.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "The Mysterious Disappearance of the Amber Room: The Eighth Wonder of the World",
                "tier": "Trending / High Retention",
                "angle": "lost_treasures",
                "slug": "lost_amber_room_eighth_wonder_nazi_gold_train_kaliningrad_looting",
                "trend_score": 97,
                "why_trending": "Deep sea and underground mine expeditions continuing the search for the 6 tons of amber panels looted by the Nazis from St. Petersburg in 1941.",
                "reason": "Legendary historical lost-treasure investigation with unmatched geopolitical and archaeological intrigue.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "085_diy_making": {
        "id": "085",
        "slug": "diy_making",
        "title": "DIY & Making",
        "category": "Craft_Making",
        "audience": "Makers, Woodworkers, Electronics Hackers, DIY Home Improvers, Fabricators (Global)",
        "progression": [
            ("Tier 1: Workshop Safety, Core Hand Tools & Fastener Mechanics (Scratch / Beginner)",
             "PPE protocols, measuring and marking accuracy (tape, square, calipers), hand saw/chisel basics, screw and anchor shear vs. tensile loads."),
            ("Tier 2: Power Tools, Joinery Techniques & Finishing Chemistry (Intermediate)",
             "Table saw kickback prevention, pocket holes vs. mortise and tenon joinery, sanding grit progression (80 to 220), and oil vs. polyurethane vs. lacquer finishes."),
            ("Tier 3: Digital Fabrication: 3D Printing, CNC Routing & Laser Cutting (Upper Intermediate)",
             "FDM vs. resin SLA 3D printing slicer settings, CNC feeds and speeds, vector laser cutting kerf compensation, and CAD modeling fundamentals."),
            ("Tier 4: Custom Automation, Microcontrollers (Arduino/ESP32) & Full Maker Systems (Advanced / Expert)",
             "Microcontroller sensor integration, relay switches for mains power control, custom PCB design, structural welding, and off-grid maker workshop infrastructure.")
        ],
        "flagship": {
            "title": "The Ultimate Beginner Workshop: 10 Essential Tools That Can Build Almost Anything",
            "angle": "foundational_guide",
            "slug": "085_diy_making_foundational_guide_10_essential_workshop_tools"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Ultimate Beginner Workshop: 10 Essential Tools That Can Build Almost Anything",
                "tier": "Tier 1: Safety & Hand Tool Foundations",
                "angle": "foundational_guide",
                "slug": "10_essential_workshop_tools_beginner_maker_toolkit_budget_setup",
                "question": "What 10 versatile tools allow a total beginner to build shelves, tables, electronics, and home repairs without spending thousands on fancy equipment?",
                "key_focus": "Combination square, cordless drill/driver, Japanese Ryoba pull saw, block plane, quality chisels, digital calipers, clamps, multimeter, and personal protective equipment (PPE).",
                "reason": "Flagship launch episode; removes intimidation and gives beginners a realistic, high-leverage entry point into the maker movement."
            },
            {
                "id": 2,
                "title": "The Physics of Fasteners: Wood Screws, Drywall Anchors, and Shear vs. Tensile Load",
                "tier": "Tier 1: Safety & Hand Tool Foundations",
                "angle": "mechanical_engineering",
                "slug": "physics_of_fasteners_screws_vs_nails_shear_tensile_strength_anchors",
                "question": "Why will a drywall anchor hold a 50 lb picture frame hanging down, but pull right out of the wall if you pull it forward, and when should you use nails instead of screws?",
                "key_focus": "Shear strength (sideways force) vs. tensile strength (pulling force), pilot hole diameter sizing, thread pitch for hardwood vs. softwood, toggle bolts vs. plastic wall anchors.",
                "reason": "Crucial foundational structural knowledge that prevents embarrassing wall collapses and stripped screws."
            },
            {
                "id": 3,
                "title": "Measuring and Marking: Why 'Measure Twice, Cut Once' Still Fails Without a Marking Knife",
                "tier": "Tier 1: Safety & Hand Tool Foundations",
                "angle": "precision_craftsmanship",
                "slug": "measuring_and_marking_pencil_thickness_error_marking_knife_reference_faces",
                "question": "Why does a thick carpenter pencil lead introduce a 1/16th-inch error that ruins your joints, and how does a marking knife sever wood fibers for laser-straight cuts?",
                "key_focus": "Pencil lead kerf error, marking knife registration, reading tape measure hook slack (designed play for inside vs. outside measurements), story sticks, and zeroing calipers.",
                "reason": "Eliminates the number one cause of beginner woodworking frustration: cumulative measurement error."
            },
            {
                "id": 4,
                "title": "Japanese Pull Saws vs. Western Push Saws: The Science of Saw Kerf and Tension",
                "tier": "Tier 1: Safety & Hand Tool Foundations",
                "angle": "tool_biomechanics",
                "slug": "japanese_pull_saw_vs_western_push_saw_ryoba_dozuki_blade_tension",
                "question": "Why does cutting on the pull stroke allow Japanese saws (Ryoba, Dozuki) to use blades three times thinner than Western push saws, leaving cleaner cuts with half the effort?",
                "key_focus": "Tensile stress pulling a blade straight vs. compressive stress buckling a pushed blade, crosscut vs. rip cut tooth geometry, kerf waste comparison, and muscle fatigue.",
                "reason": "Celebrates the brilliant mechanical advantages of Japanese hand saw design."
            },
            {
                "id": 5,
                "title": "The Art of the Chisel: How to Flatten, Sharpen, and Pare Wood to a Razor Edge",
                "tier": "Tier 1: Safety & Hand Tool Foundations",
                "angle": "sharpening_mastery",
                "slug": "sharpening_chisels_scary_sharp_method_waterstones_micro_bevel_burr",
                "question": "Why is a dull tool ten times more dangerous than a razor-sharp one, and how can you sharpen a cheap $10 hardware store chisel until it shaves arm hair cleanly?",
                "key_focus": "Flattening the back of the blade, primary bevel (25°) vs. secondary micro-bevel (30°), the 'Scary Sharp' sandpaper-on-glass system vs. waterstones, feeling the burr, and leather stropping.",
                "reason": "The essential workshop rite-of-passage skill that transforms wood paring from a gouging struggle into effortless butter."
            },
            {
                "id": 6,
                "title": "Table Saw Safety: The Terrifying Physics of Kickback and How to Prevent It",
                "tier": "Tier 2: Power Tools & Joinery Chemistry",
                "angle": "workshop_safety",
                "slug": "table_saw_kickback_physics_riving_knife_push_sticks_blade_height",
                "question": "How can a 3-horsepower table saw blade spinning at 4,000 RPM launch a piece of oak backwards at 100 miles per hour in 1/100th of a second?",
                "key_focus": "The anatomy of kickback (pinching behind the blade), why the riving knife is the single most critical safety device ever invented, push stick ergonomics, and SawStop skin-detection brakes.",
                "reason": "The most important safety video any woodworker or DIYer will ever watch to save their fingers and life."
            },
            {
                "id": 7,
                "title": "Woodworking Joinery: Pocket Holes vs. Mortise & Tenon vs. Dowels vs. Biscuits",
                "tier": "Tier 2: Power Tools & Joinery Chemistry",
                "angle": "structural_joinery",
                "slug": "woodworking_joinery_comparison_pocket_holes_mortise_tenon_dowels_strength",
                "question": "Are Kreg pocket holes a lazy cheat, or are traditional mortise and tenon joints over-engineered? Scientific destructive strength testing of 5 popular joints.",
                "key_focus": "End grain gluing failure mechanics, long-grain to long-grain glue shear strength, pocket screw shear limits, dowel alignment jigs, domino joinery, and aesthetic vs. structural balance.",
                "reason": "Direct, data-driven comparison cutting through internet woodworking elitism and dogmatic debates."
            },
            {
                "id": 8,
                "title": "Wood Movement: The Unstoppable Seasonal Expansion That Tears Furniture Apart",
                "tier": "Tier 2: Power Tools & Joinery Chemistry",
                "angle": "material_science",
                "slug": "wood_movement_seasonal_expansion_tangential_radial_breadboard_ends",
                "question": "Why does a solid tabletop glued tightly to a wooden base split in half during winter or bow into a taco during humid summers?",
                "key_focus": "Cellular moisture equilibrium, tangential vs. radial shrinkage rates, why wood expands across the width but never along its length, figure-8 fasteners, and breadboard end construction.",
                "reason": "Explains the number one architectural mistake that causes amateur heirloom furniture to crack."
            },
            {
                "id": 9,
                "title": "The Sanding Truth: Why Skipping Grits from 80 to 220 Leaves Ugly Swirls in Your Stain",
                "tier": "Tier 2: Power Tools & Joinery Chemistry",
                "angle": "surface_preparation",
                "slug": "sanding_progression_random_orbital_sander_pigtails_water_popping_grain",
                "question": "Why does wiping wood with a wet rag ('water popping') before your final sand double the depth of your wood stain and highlight hidden scratches?",
                "key_focus": "Grit progression rules (80 -> 120 -> 150 -> 180 -> 220), random orbital sander speed and down-pressure, wiping away dust between stages, raising the grain, and inspection raking light.",
                "reason": "Transforms amateur, unevenly stained wood into professional, silky-smooth furniture surfaces."
            },
            {
                "id": 10,
                "title": "Finishes Demystified: Boiled Linseed Oil vs. Polyurethane vs. Lacquer vs. Hardwax",
                "tier": "Tier 2: Power Tools & Joinery Chemistry",
                "angle": "finishing_chemistry",
                "slug": "wood_finishes_guide_polyurethane_vs_oil_vs_lacquer_rubio_monocoat",
                "question": "Which finish should you pick when you want bulletproof waterproof protection versus an all-natural organic matte feel that breathes with the wood?",
                "key_focus": "Penetrating oils (tung, linseed) vs. film-forming finishes (wipe-on poly, spray lacquer), molecular cross-linking in two-part hardwax oils (Rubio Monocoat), and spontaneous combustion danger of oily rags.",
                "reason": "A comprehensive buyer's and applicator's guide to the complex, chemically intimidating world of wood finishes."
            },
            {
                "id": 11,
                "title": "3D Printing Foundations: FDM vs. Resin SLA and The Slicer Settings That Actually Matter",
                "tier": "Tier 3: Digital Fabrication & CAD",
                "angle": "digital_fabrication",
                "slug": "3d_printing_fdm_vs_resin_slicer_settings_layer_height_infill_supports",
                "question": "Why do your FDM prints keep warping off the bed, and when should you switch to an ultraviolet liquid resin printer for microscopic precision?",
                "key_focus": "Fused Deposition Modeling (PLA, PETG, ABS) thermal adhesion, first layer squish (Z-offset), infill patterns (Gyroid vs. Grid for strength), and stereolithography (SLA) toxic resin washing/curing.",
                "reason": "The essential digital maker guide for getting perfect, functional plastic parts on the first try."
            },
            {
                "id": 12,
                "title": "CAD for Absolute Beginners: Designing Your First Functional Part in Fusion 360",
                "tier": "Tier 3: Digital Fabrication & CAD",
                "angle": "cad_design",
                "slug": "fusion_360_beginner_cad_parametric_modeling_sketch_extrude_fillet",
                "question": "How can you turn a broken plastic refrigerator clip into a 3D-printable replacement model in Fusion 360 in under 15 minutes using parametric sketches?",
                "key_focus": "Parametric design principles, fully defining 2D sketches with geometric constraints, extrude/cut operations, shell and fillet tools, exporting clean STLs, and measuring broken parts with calipers.",
                "reason": "Demystifies professional 3D computer-aided design and empowers viewers to solve their own household repair problems."
            },
            {
                "id": 13,
                "title": "CNC Routers: Feeds, Speeds, and The Physics of Chip Load",
                "tier": "Tier 3: Digital Fabrication & CAD",
                "angle": "cnc_machining",
                "slug": "cnc_router_feeds_and_speeds_chip_load_end_mills_chatter_prevention",
                "question": "Why does running your CNC router spindle too fast without moving fast enough burn your wood and dull your $40 carbide end mill in two minutes?",
                "key_focus": "Calculating chip load (Feed rate / [RPM x Flutes]), up-cut vs. down-cut spiral end mills, holding workpieces with blue tape and superglue, climb vs. conventional milling, and g-code basics.",
                "reason": "Explains the science of machine cutting to prevent broken bits, chatter marks, and burned stock."
            },
            {
                "id": 14,
                "title": "Laser Cutters: Kerf Compensation, Vector Cutting vs. Raster Engraving, and Material Safety",
                "tier": "Tier 3: Digital Fabrication & CAD",
                "angle": "laser_fabrication",
                "slug": "laser_cutter_kerf_vector_cutting_raster_engraving_diode_vs_co2_safety",
                "question": "Why will cutting PVC or vinyl on a laser cutter produce chlorine gas that destroys your lungs and corrodes the machine's steel rails, and how do you compensate for laser beam kerf?",
                "key_focus": "Diode vs. CO2 vs. Fiber lasers, vector paths vs. raster dithering, kerf calculation for press-fit finger joints in plywood, honeycomb bed maintenance, and exhaust filtration.",
                "reason": "Critical material safety and mechanical precision guide for laser cutting and engraving enthusiasts."
            },
            {
                "id": 15,
                "title": "Soldering Electronics: The Molecular Science of Intermetallic Bonds and Flux",
                "tier": "Tier 3: Digital Fabrication & CAD",
                "angle": "electronics_assembly",
                "slug": "soldering_electronics_guide_rosin_flux_cold_joints_lead_vs_lead_free",
                "question": "Why is flux the magical ingredient that makes solder flow like liquid silver, and what causes a dull, brittle 'cold solder joint' that fails after a week?",
                "key_focus": "Thermal mass transfer, iron tip tinning, rosin core flux cleaning oxidation, leaded (60/40) vs. lead-free (SAC305) melting temperatures, desoldering braid, and inspecting shiny concave fillets.",
                "reason": "The foundational electrical skill every maker needs to wire custom circuits, drones, and sensors reliably."
            },
            {
                "id": 16,
                "title": "Arduino vs. ESP32 vs. Raspberry Pi: Choosing the Right Brain for Your Project",
                "tier": "Tier 4: Microcontrollers, Automation & Full Systems",
                "angle": "embedded_systems",
                "slug": "arduino_vs_esp32_vs_raspberry_pi_microcontroller_vs_single_board_computer",
                "question": "When should you use a $3 ESP32 with built-in Wi-Fi and Bluetooth instead of a full $60 Raspberry Pi Linux computer for your home automation project?",
                "key_focus": "Microcontroller (real-time loop execution, low power, GPIO control) vs. Single-Board Computer (full OS, multimedia, network server), GPIO pin voltages (5V vs 3.3V logic danger), and sleep modes.",
                "reason": "Clears up the most common hardware architecture confusion in modern DIY robotics and smart home builds."
            },
            {
                "id": 17,
                "title": "Controlling Mains Power Safely: Relays, Optocouplers, and Solid State Switches",
                "tier": "Tier 4: Microcontrollers, Automation & Full Systems",
                "angle": "electrical_safety",
                "slug": "controlling_mains_power_safely_relays_optocouplers_solid_state_flyback_diode",
                "question": "How can a 3.3V microcontroller switch on a 120V/240V workshop vacuum or water pump without frying the computer chip or shocking the user?",
                "key_focus": "Galvanic isolation using optocouplers, electromechanical relays vs. Solid State Relays (SSR) zero-crossing switching, flyback diodes quenching inductive coil spikes, and fusing protections.",
                "reason": "Crucial high-voltage safety engineering tutorial bridging delicate digital logic to heavy machinery."
            },
            {
                "id": 18,
                "title": "Basic MIG Welding: How to Melt Steel Together Without Blowing Holes Through It",
                "tier": "Tier 4: Microcontrollers, Automation & Full Systems",
                "angle": "metal_fabrication",
                "slug": "mig_welding_for_beginners_wire_feed_voltage_shielding_gas_c25_penetration",
                "question": "How do you set your wire feed speed and voltage so your MIG welder sounds like frying bacon instead of sputtering and spitting hot sparks everywhere?",
                "key_focus": "Metal Inert Gas (GMAW) principles, 75/25 Argon/CO2 shielding gas, push vs. pull torch angle, cleaning mill scale with an angle grinder, penetration inspection, and safety gear.",
                "reason": "Expands maker capabilities beyond wood and plastic into permanent, load-bearing steel fabrication."
            },
            {
                "id": 19,
                "title": "Custom PCB Design: From Breadboard Prototype to Finished Printed Circuit Board in 7 Days",
                "tier": "Tier 4: Microcontrollers, Automation & Full Systems",
                "angle": "circuit_design",
                "slug": "custom_pcb_design_kicad_schematic_trace_routing_gerber_manufacturing",
                "question": "How do you turn a messy rat's nest of breadboard jumper wires into a sleek, professional two-layer custom green PCB for less than $10 shipped?",
                "key_focus": "KiCad schematic capture, PCB layout routing, trace width calculators for current carrying, ground planes and decoupling capacitors for electrical noise, and exporting Gerber files.",
                "reason": "The pinnacle of hardware maker maturity: graduating from prototype spaghetti wires to commercial-grade hardware."
            },
            {
                "id": 20,
                "title": "The Self-Sustaining Maker Workshop: Dust Collection, Solar Power, and System Integration",
                "tier": "Tier 4: Microcontrollers, Automation & Full Systems",
                "angle": "workshop_infrastructure",
                "slug": "ultimate_maker_workshop_cyclone_dust_collector_solar_battery_smart_shop",
                "question": "How do you design an airtight 2-stage cyclone dust collection ducting system, clean workshop air down to 1 micron, and power tools with solar batteries?",
                "key_focus": "Bill Pentz cyclone dust separation physics, static electricity grounding in PVC pipe, automated blast gates with micro-switches, workshop ergonomics, and battery bank sizing.",
                "reason": "Capstones the master curriculum with the ultimate blueprint for a clean, automated, healthy, and sustainable creative laboratory."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why You Should Never Use Expanding Foam on Plumbing: 5 Costly DIY Disasters",
                "tier": "Trending / High Retention",
                "angle": "diy_fail_warnings",
                "slug": "worst_diy_mistakes_expanding_spray_foam_plumbing_crushed_pipes",
                "trend_score": 98,
                "why_trending": "Viral homeowner and plumbing shorts showing closed-cell expanding foam crushing PVC drain pipes and jamming window frames, causing thousands in damage.",
                "reason": "High-retention cautionary lesson warning viewers against deceptively simple hardware store quick-fix hacks.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "The $50 3D-Printed Power Tool Hack: Turning Cheap Drills into Metal Lathes",
                "tier": "Trending / High Retention",
                "angle": "maker_hacks",
                "slug": "3d_printed_power_tool_mods_cordless_drill_into_mini_lathe_drill_press",
                "trend_score": 96,
                "why_trending": "Massive viral maker community obsession on YouTube and Reddit with 3D-printing modular jigs that convert basic drills into mini lathes, disc sanders, and drill presses.",
                "reason": "Incredible budget hack providing high-utility maker capability for the cost of a single filament spool.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Why Epoxy Resin River Tables Are Dying: The Rise of Modern Minimalist Solid Wood",
                "tier": "Trending / High Retention",
                "angle": "trend_autopsy",
                "slug": "death_of_epoxy_river_tables_yellowing_microplastics_return_to_joinery",
                "trend_score": 95,
                "why_trending": "Widespread creator backlash against neon blue epoxy river tables due to UV yellowing, plastic waste, and the cultural return to clean, authentic joinery.",
                "reason": "Sharp, culturally resonant design critique breaking down why a 5-year viral fad is crashing.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Home Depot Stud Finder Myth: Why You Keep Hitting Pipes Instead of Studs",
                "tier": "Trending / High Retention",
                "angle": "practical_home_repair",
                "slug": "stud_finder_calibration_magnetic_vs_dielectric_capacitive_sensors",
                "trend_score": 97,
                "why_trending": "Universal viral frustration over cheap capacitive stud finders giving false positives over electrical conduit, drain vents, and plaster-and-lath walls.",
                "reason": "Everyday problem solved with brilliant, practical magnet hacks (rare earth neodymium magnets finding drywall screws every time).",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "How to Strip Paint in 5 Minutes with Baking Soda Blasting: The Chemical-Free Hack",
                "tier": "Trending / High Retention",
                "angle": "restoration_hacks",
                "slug": "soda_blasting_paint_removal_diy_air_compressor_baking_soda_media",
                "trend_score": 95,
                "why_trending": "TikTok and YouTube restoration videos demonstrating cheap DIY air compressor siphon setups using Arm & Hammer baking soda to blast paint off vintage brass and car parts.",
                "reason": "Deeply satisfying visual before-and-after demonstration that avoids toxic chemical methylene chloride paint strippers.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "Why Cordless Tool Batteries Die After 2 Years: The BMS Sleep Mode You Can Revive",
                "tier": "Trending / High Retention",
                "angle": "battery_hacks",
                "slug": "reviving_dead_lithium_tool_batteries_bms_low_voltage_jumpstart_hack",
                "trend_score": 98,
                "why_trending": "Huge DIY and contractor interest in 'jumpstarting' DeWalt and Milwaukee 18V/20V lithium battery packs whose Battery Management System shut down due to micro-undervoltage.",
                "reason": "Saves viewers $100+ on new replacement tool batteries with a clear, safe 60-second multimeter and jumper-wire guide.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "The French Cleat Wall System: Why It's the Ultimate Modular Workshop Storage",
                "tier": "Trending / High Retention",
                "angle": "workshop_organization",
                "slug": "french_cleat_tool_wall_system_45_degree_bevel_modular_workshop_storage",
                "trend_score": 96,
                "why_trending": "Perennial workshop organization trend generating millions of views showing satisfying 45-degree angled plywood cleat walls with custom tool caddies.",
                "reason": "The quintessential satisfying maker project that makes any garage or basement look like an elite professional atelier.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 081-085...")
    for folder_name, meta in BATCH_081_085.items():
        process_niche(folder_name, meta)
    update_master_readme()
    print("Batch 081-085 complete!")

if __name__ == "__main__":
    main()
