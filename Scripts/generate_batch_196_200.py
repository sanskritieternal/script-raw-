import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_196_200 = {
    "196_birds": {
        "id": "196",
        "slug": "birds",
        "title": "Birds",
        "category": "Life_Biology",
        "audience": "Ornithologists, Birdwatchers, Wildlife Photographers, Raptor Enthusiasts, Evolutionary Biologists (Global)",
        "progression": [
            ("Tier 1: Avian Biology & Evolutionary Flight Mechanics: Theropod Ancestry, Hollow Bones, Feathers & Air Sac Respiration (Beginner / Scratch)",
             "Avian anatomy, theropod dinosaur lineage (Archaeopteryx), continuous unidirectional air-sac lung ventilation, hollow bone weight optimization, and feather aerodynamic physics."),
            ("Tier 2: Sensory Systems, Song & Courtship: Syringes, Vocal Learning, Ultraviolet Plumage & Bowerbird Architecture (Intermediate)",
             "The dual syrinx vocal organ, complex birdsong dialects, tetrachromatic ultraviolet vision, woodpecker brain deceleration shock absorbers, and hummingbird hover physics."),
            ("Tier 3: Epic Migrations & Extreme Predators: Trans-Global Flyways, Magnetic Navigation, Peregrine Dives & Owl Silence (Upper Intermediate)",
             "Trans-oceanic non-stop migratory flights (Godwit), quantum cryptochrome magnetic navigation, peregrine falcon 240-MPH dive physics, silent owl flight serrations, and vulture immune chemistry."),
            ("Tier 4: Avian Cognition, Island Gigantism & Modern Extinction: Corvids, Parrots, Moas, Dodos & Habitat Conservation (Advanced / Masterclass)",
             "Corvid tool making and episodic memory, island gigantism and flightlessness (Moa, Dodo), passenger pigeon extinction lessons, and urban concrete jungle adaptations.")
        ],
        "flagship": {
            "title": "The Masterpiece of Flight: How Avian Anatomy Conquered the Sky",
            "angle": "deep_dive",
            "slug": "196_birds_deep_dive_the_masterpiece_of_flight"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Masterpiece of Flight: How Avian Anatomy Conquered the Sky",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "masterpiece_of_flight_how_avian_anatomy_conquered_sky",
                "question": "What structural and metabolic adaptations allow a living vertebrate to sustain powered flight across thousands of continuous miles?",
                "focus": "Aerodynamic lift vs drag, asymmetric primary feathers, high metabolic body temperatures (104°F+), pectoralis major muscle output, and fused furcula spring energy storage.",
                "reason": "The quintessential avian masterclass deconstructing the biological triumph of powered flight."
            },
            {
                "id": 2,
                "title": "Dinosaurs Among Us: Archaeopteryx, Theropod Fossils, and the Origin of Feathers",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "evolutionary_milestone",
                "slug": "dinosaurs_among_us_archaeopteryx_theropod_fossils_feathers",
                "question": "How did Chinese Liaoning shale fossils prove beyond doubt that modern birds are living, surviving avian dinosaurs?",
                "focus": "Archaeopteryx transitional morphology, proto-feathers evolving first for thermal insulation and mating displays rather than flight, theropod wishbones, and surviving the Chicxulub asteroid.",
                "reason": "Grounds ornithology in its deep, awe-inspiring dinosaurian evolutionary heritage."
            },
            {
                "id": 3,
                "title": "The Unidirectional Lung: How Air Sacs and Continuous Flow Power High-Altitude Flight",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "unidirectional_lung_air_sacs_continuous_flow_high_altitude",
                "question": "Why can bar-headed geese fly over Mount Everest at 29,000 feet without supplemental oxygen while human mountaineers suffocate?",
                "focus": "Nine respiratory air sacs circulating fresh air during both inhalation and exhalation, cross-current parabronchial blood gas exchange, and high-affinity avian hemoglobin.",
                "reason": "Technical breakdown of the most efficient respiratory system ever evolved by a vertebrate."
            },
            {
                "id": 4,
                "title": "Feather Aerodynamics: Barbules, Rachis Elasticity, and Asymmetric Flight Pinions",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biomechanics",
                "slug": "feather_aerodynamics_barbules_rachis_elasticity_pinions",
                "question": "How do microscopic hook-and-groove barbules interlock like biological velcro to create an airtight yet self-healing wing surface?",
                "focus": "Calamus, rachis, and vane structure, preening gland oil distribution, slotting wingtips (alula) preventing aerodynamic stalls at low speeds, and molt cycles.",
                "reason": "Deep dive into the complex microscopic engineering of nature's most sophisticated integumentary structure."
            },
            {
                "id": 5,
                "title": "The Avian Skeleton: Pneumatized Hollow Bones, Keel Sternums, and Fused Furcula",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "avian_skeleton_pneumatized_hollow_bones_keel_sternums_furcula",
                "question": "How do internal bone struts provide immense structural stiffness while reducing skeletal mass to less than the weight of a bird's feathers?",
                "focus": "Pneumatized hollow long bones infused with respiratory air, the large carina/keel for massive flight muscle attachment, the pygostyle tail anchor, and fused synsacrum pelvis.",
                "reason": "Essential skeletal anatomy breakdown highlighting extreme biological weight optimization."
            },
            {
                "id": 6,
                "title": "The Dual Syrinx: How Songbirds Sing Two Independent Harmonies Simultaneously",
                "tier": "Tier 2: Sensory Systems & Courtship",
                "angle": "sensory_science",
                "slug": "dual_syrinx_songbirds_two_independent_harmonies_simultaneously",
                "question": "How does a thrush produce polyphonic two-part duets with its own throat without using vocal cords?",
                "focus": "The tracheobronchial syrinx junction, independent left and right sound-producing tympaniform membranes, neuromuscular firing at 200 Hz, and regional dialect learning in young chicks.",
                "reason": "Fascinating acoustic and neuromuscular exploration of how birdsong is physically generated."
            },
            {
                "id": 7,
                "title": "Courtship Architecture: Bowerbirds Constructing Color-Sorted Optical Illusions",
                "tier": "Tier 2: Sensory Systems & Courtship",
                "angle": "behavioral_habits",
                "slug": "courtship_architecture_bowerbirds_color_sorted_optical_illusions",
                "question": "Why do male bowerbirds arrange blue plastic bottle caps, berries, and bleached shells in forced perspective gradients to impress females?",
                "focus": "Vogelkop and Satin bowerbird construction, forced perspective avenues making courting males appear larger, color discrimination preferences, and evaluating non-physical artistic intelligence.",
                "reason": "Celebrates one of the most astonishing non-human displays of architectural aesthetics and artistic choice."
            },
            {
                "id": 8,
                "title": "Ultraviolet Vision: How Birds See a Radiant 4-Cone Spectrum of Plumage and Fruit",
                "tier": "Tier 2: Sensory Systems & Courtship",
                "angle": "scientific_phenomenon",
                "slug": "ultraviolet_vision_birds_4_cone_spectrum_plumage_fruit",
                "question": "Why do seemingly dull, identical brown birds look like glowing multicolored neon beacons to other birds in UV wavelengths?",
                "focus": "Tetrachromatic vision (red, green, blue, and ultraviolet cone pigments), oil droplet optical filters on retinas, tracking rodent urine trails across meadows, and spotting ripe berries.",
                "reason": "Reveals the radiant, hidden optical spectrum through which birds perceive and navigate their environment."
            },
            {
                "id": 9,
                "title": "Woodpecker Shock Absorption: Spongy Hyoid Bones Preventing Brain Trauma at 1,200G",
                "tier": "Tier 2: Sensory Systems & Courtship",
                "angle": "engineering_marvels",
                "slug": "woodpecker_shock_absorption_hyoid_bone_prevents_brain_trauma",
                "question": "How does a woodpecker smash its beak into hardwood 20 times per second with a force of 1,200G without suffering severe concussions?",
                "focus": "The wrap-around tongue hyoid apparatus acting as an internal biological seatbelt, spongy trabecular cranial bone distribution, third nictitating eyelid preventing eye ejection, and football helmet biomimicry.",
                "reason": "Spectacular biomechanical case study inspiring modern helmet and aerospace crash-impact engineering."
            },
            {
                "id": 10,
                "title": "Hummingbird Hover Physics: Figure-Eight Wing Strokes and 1,200 Beats Per Minute",
                "tier": "Tier 2: Sensory Systems & Courtship",
                "angle": "extreme_scenarios",
                "slug": "hummingbird_hover_physics_figure_eight_wing_strokes_metabolism",
                "question": "How do hummingbirds generate lift on both the forward and backward stroke, and how do they survive nighttime torpor without starving?",
                "focus": "Inverting wings at the shoulder joint, 80 wing beats per second, hovering fluid dynamics like helicopter rotors, feeding on pure sugar nectar, and dropping body temperature by 50°F during overnight torpor.",
                "reason": "High-speed physiological examination of the most metabolically intense vertebrate on Earth."
            },
            {
                "id": 11,
                "title": "The Peregrine Falcon: Aerodynamic Stoop Physics Hitting 240 MPH in Mid-Air",
                "tier": "Tier 3: Migrations & Extreme Predators",
                "angle": "extreme_scenarios",
                "slug": "peregrine_falcon_aerodynamic_stoop_physics_240_mph",
                "question": "What anatomical adaptations keep a falcon's lungs from bursting when diving through the air at high-speed racecar velocity?",
                "focus": "Teardrop body streamlining, nasal bony tuberculi baffles channeling airflow like jet engine intake cones, nictitating membranes clearing eyes at 240 MPH, and the concussive taloned kill strike.",
                "reason": "Thrilling showcase of the fastest animal on planet Earth."
            },
            {
                "id": 12,
                "title": "Barn Owl Stealth Mechanics: Comb Serrations and Velvety Feathers Eliminating Sound",
                "tier": "Tier 3: Migrations & Extreme Predators",
                "angle": "technical_breakdown",
                "slug": "barn_owl_stealth_mechanics_comb_serrations_velvety_feathers",
                "question": "How does a barn owl fly directly over a sensitive microphone without generating a single decibel of audible noise?",
                "focus": "Leading-edge comb serrations breaking air turbulence into micro-vortices, soft downy feather velvet damping high frequencies, porous trailing-edge fringes, asymmetric ear openings for 3D sound triangulation.",
                "reason": "Deconstructs the world's most advanced natural acoustic stealth technology."
            },
            {
                "id": 13,
                "title": "The Bar-Tailed Godwit: Flying 7,000 Miles Non-Stop Across the Pacific Without Sleeping",
                "tier": "Tier 3: Migrations & Extreme Predators",
                "angle": "case_study",
                "slug": "bar_tailed_godwit_flying_7000_miles_nonstop_pacific_ocean",
                "question": "How can a shorebird take off from Alaska and fly 11 consecutive days across open ocean to New Zealand without stopping once for food, water, or rest?",
                "focus": "Doubling body mass with fat reserves, shrinking digestive organs before departure to reduce weight, unihemispheric slow-wave sleep (sleeping with half a brain while flying), and satellite telemetry tracks.",
                "reason": "The undisputed world record holder for non-stop animal endurance migration."
            },
            {
                "id": 14,
                "title": "Quantum Navigation: Cryptochrome Proteins in Avian Retinas Sensing Earth's Magnetic Field",
                "tier": "Tier 3: Migrations & Extreme Predators",
                "angle": "scientific_phenomenon",
                "slug": "quantum_navigation_cryptochrome_proteins_sensing_magnetic_field",
                "question": "How do migrating birds physically 'see' the invisible inclination lines of Earth's geomagnetic field across total darkness?",
                "focus": "Cryptochrome 4 (Cry4) proteins in retinal photoreceptors, blue light-induced radical pair quantum entanglement mechanisms, magnetoreception inclination angles, and celestial star map orientation.",
                "reason": "Mind-bending intersection of quantum physics, retinal biochemistry, and global migratory navigation."
            },
            {
                "id": 15,
                "title": "Vultures and Carcass Ecology: Sulfuric Stomach Acid Neutralizing Anthrax and Rabies",
                "tier": "Tier 3: Migrations & Extreme Predators",
                "angle": "biological_guide",
                "slug": "vultures_carcass_ecology_stomach_acid_neutralizing_anthrax",
                "question": "Why don't scavenging vultures die of botulism, anthrax, and cholera when dining on rotting, putrid animal corpses?",
                "focus": "Gastric acid with a pH of 1.0 (approaching battery acid), specialized gut microbiome dominated by pathogenic Clostridia that vultures domesticate, featherless bald heads for sanitation, and ecosystem disease cleansing.",
                "reason": "Essential rehabilitation and appreciation of the vital ecological health service rendered by scavengers."
            },
            {
                "id": 16,
                "title": "Corvid Intelligence: Crows Fabricating Tools, Recognizing Faces, and Passing Grudges",
                "tier": "Tier 4: Cognition, Extinction & Conservation",
                "angle": "cognitive_science",
                "slug": "corvid_intelligence_crows_fabricating_tools_recognizing_faces",
                "question": "How does a New Caledonian crow solve an eight-stage puzzle box requiring compound hook tools and water displacement?",
                "focus": "High neuronal packing density in the avian nidopallium, Aesop's fable water displacement experiments, multi-generational facial recognition and scolding warnings, and causal reasoning matching great apes.",
                "reason": "Masterclass in animal cognition proving brain size relative to body size matters more than raw cortex volume."
            },
            {
                "id": 17,
                "title": "Island Gigantism and Extinction: The Haast's Eagle, Moa, Dodo, and Flightless Giants",
                "tier": "Tier 4: Cognition, Extinction & Conservation",
                "angle": "prehistoric_deep_dive",
                "slug": "island_gigantism_extinction_haasts_eagle_moa_dodo_giants",
                "question": "Why did oceanic islands without mammalian predators evolve 12-foot flightless moas and 35-pound eagles with predatory talons capable of hunting humans?",
                "focus": "Foster's rule on islands, losing flight musculature to conserve metabolic energy, the catastrophic arrival of humans and introduced rats/cats, and the rapid collapse of naive endemic bird faunas.",
                "reason": "Fascinating evolutionary case study exploring the fragility and wonder of isolated island ecosystems."
            },
            {
                "id": 18,
                "title": "The Passenger Pigeon: How Humanity Wiped Out 5 Billion Birds in Under 50 Years",
                "tier": "Tier 4: Cognition, Extinction & Conservation",
                "angle": "investigative",
                "slug": "passenger_pigeon_how_humanity_wiped_out_5_billion_birds",
                "question": "How did the most abundant bird species on Earth—whose migrating flocks darkened the skies for days—vanish into complete extinction by 1914?",
                "focus": "Flocks of 3.5 billion birds breaking tree branches, commercial market hunting enabled by telegraph and railroads, clearing eastern deciduous forests, captive breeding failure, and Martha dying alone in Cincinnati Zoo.",
                "reason": "The defining tragedy of modern wildlife conservation that sparked the birth of the conservation movement."
            },
            {
                "id": 19,
                "title": "Urban Adaptations: How Pigeons, Peregrines, and Gulls Conquered Concrete Canyons",
                "tier": "Tier 4: Cognition, Extinction & Conservation",
                "angle": "environmental_dilemma",
                "slug": "urban_adaptations_how_pigeons_peregrines_conquered_cities",
                "question": "Why do rock doves and peregrine falcons treat 60-story Manhattan skyscrapers exactly like their ancestral Mediterranean sea cliffs?",
                "focus": "Urban heat islands, artificial nesting ledges, abundant food waste and rodent prey, behavioral shifts in nocturnal singing under streetlights, and surviving window collisions.",
                "reason": "Insightful ecological examination of species flourishing in human-dominated urban biomes."
            },
            {
                "id": 20,
                "title": "The Global Songbird Decline: Habitat Loss, Cat Predation, and Window Mitigation",
                "tier": "Tier 4: Cognition, Extinction & Conservation",
                "angle": "conservation_action",
                "slug": "global_songbird_decline_habitat_loss_cat_predation_windows",
                "question": "Why have North American and European forests lost nearly 3 billion birds since 1970, and how can individual citizens reverse the trend?",
                "focus": "The 2019 Science 3-Billion Birds study, domestic outdoor cat predation (2.4 billion birds/year in the US), building glass UV collision decals, native plant insect gardens, and shade-grown coffee certification.",
                "reason": "Actionable, urgent conservation capstone empowering viewers to protect wild bird populations."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Harpy Eagle: The Massive Canopy Predator with Talons Bigger Than Grizzly Claws",
                "trend_score": 96,
                "angle": "wildlife_spectacle",
                "slug": "harpy_eagle_massive_canopy_predator_talons_grizzly_claws",
                "why_trending": "Massive ongoing social media fascination showcasing enormous 20-pound eagles snatching howler monkeys and sloths from rainforest canopies.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Crow Funerals: Why Crows Gather to Investigate Dead Flocks and Identify Threats",
                "trend_score": 95,
                "angle": "animal_behavior",
                "slug": "crow_funerals_why_crows_gather_investigate_dead_identify_threats",
                "why_trending": "High-interest viral behavioral biology videos demonstrating crows gathering in silent circles around dead members to identify predators.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "The Shoebill Stork: The Prehistoric Dinosaur-Like Stork of Ugandan Papyrus Swamps",
                "trend_score": 97,
                "angle": "viral_phenomenon",
                "slug": "shoebill_stork_prehistoric_dinosaur_stork_uganda_swamps",
                "why_trending": "Immense viral popularity across TikTok and YouTube featuring the 5-foot-tall, machine-gun-sounding shoebill that stares unblinkingly at visitors.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "De-Extinction of the Dodo: Colossal Biosciences Using Gene Editing to Resurrect Lost Birds",
                "trend_score": 94,
                "angle": "biotechnology",
                "slug": "de_extinction_of_dodo_colossal_biosciences_gene_editing",
                "why_trending": "Major biotech venture capital funding announced to sequence dodo ancient DNA and edit Nicobar pigeon primordial germ cells.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Smart Birdfeeders with AI: Cameras Identifying Hundreds of Backyard Species in Real Time",
                "trend_score": 93,
                "angle": "tech_disruption",
                "slug": "smart_birdfeeders_with_ai_cameras_identifying_species",
                "why_trending": "Huge consumer tech trend (Bird Buddy, Netvue) delivering high-res notifications and species ID cards directly to smartphones.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Lyrebird Audio Mimicry: The Australian Bird That Copies Chainsaws and Camera Shutters",
                "trend_score": 96,
                "angle": "natural_wonder",
                "slug": "lyrebird_audio_mimicry_australian_bird_chainsaw_camera_sounds",
                "why_trending": "Perennial multi-million view documentary spectacle showcasing Superb Lyrebirds producing uncanny mechanical audio recordings.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Condor Lead Poisoning: The Battle to Ban Lead Ammunition and Save America's Largest Bird",
                "trend_score": 91,
                "angle": "conservation_ethics",
                "slug": "california_condor_lead_poisoning_ammunition_ban_battle",
                "why_trending": "Ongoing high-stakes wildlife recovery narrative following the comeback of the California Condor from 22 individuals to over 500.",
                "status": "Queued"
            }
        ]
    },
    "197_marine_mammals": {
        "id": "197",
        "slug": "marine_mammals",
        "title": "Marine Mammals",
        "category": "Life_Biology",
        "audience": "Cetologists, Marine Biologists, Wildlife Filmmakers, Conservationists, Ocean Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Evolution & Physiological Adaptations: From Terrestrial Ungulates to Ocean Leviathans (Pakicetus, Blubber, Bradycardia) (Beginner / Scratch)",
             "Mammalian return to the sea, land-to-sea fossil transitions (Pakicetus, Ambulocetus), diving bradycardia, thick blubber countercurrent vascular heat systems, and baleen vs toothed lines."),
            ("Tier 2: Echolocation, Acoustics & Sensory Systems: Melon Anatomy, Click Trains, Whale Songs & Hydrophones (Intermediate)",
             "Odontocete biosonar acoustic lenses, humpback whale complex multi-part songs, sea otter dense insulation and kelp forest keystone roles, pinniped haulouts, and bubble-net hunting choreography."),
            ("Tier 3: Deep Diving & Apex Predation: Sperm Whales vs Giant Squid, Orca Dialects & Bubble-Net Feeding (Upper Intermediate)",
             "Sperm whale 7,000-foot abyss diving to battle giant squid, orca pod matriarchal dialects and hunting specialization, bowhead 200-year lifespans, and narwhal sensory spiral tusks."),
            ("Tier 4: Culture, Intelligence & Anthropogenic Threats: Ship Strikes, Sonar Strandings, Captivity Ethics & Sanctuaries (Advanced / Masterclass)",
             "Cetacean cultural transmission, historical industrial whaling collapse and recovery, naval active sonar acoustic trauma, post-'Blackfish' captivity bans, and marine traffic noise pollution.")
        ],
        "flagship": {
            "title": "The Return to the Sea: How Land Mammals Evolved into Ocean Giants",
            "angle": "historical_evolution",
            "slug": "197_marine_mammals_historical_evolution_return_to_the_sea"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Return to the Sea: How Land Mammals Evolved into Ocean Giants",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "return_to_the_sea_how_land_mammals_evolved_ocean_giants",
                "question": "How did four-legged, deer-like land ungulates transform into 100-foot blue whales in under 50 million years?",
                "focus": "Pakicetus walking whale fossils in Pakistan, Ambulocetus swimming transitions, Basilosaurus vestigial hind limbs, blowhole migration to the skull roof, and genetic kinship with hippopotamuses.",
                "reason": "The quintessential evolutionary masterclass documenting the most dramatic anatomical reversal in vertebrate history."
            },
            {
                "id": 2,
                "title": "Bradycardia and Blood Satiation: How Marine Mammals Hold Their Breath for Two Hours",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "bradycardia_blood_satiation_marine_mammals_breath_hold",
                "question": "Why don't deep-diving Cuvier's beaked whales get the bends or suffer brain damage when holding their breath for 138 minutes?",
                "focus": "Extreme mammalian dive reflex, dropping heart rate from 100 to 4 BPM, myoglobin-saturated dark red muscle tissue, collapsing rib cages to avoid nitrogen absorption, and blood shunting to brain and heart.",
                "reason": "In-depth physiological breakdown of the extreme diving adaptations that conquer ocean pressure."
            },
            {
                "id": 3,
                "title": "Blubber Dynamics: Vascular Countercurrent Heat Exchangers in Polar Seas",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "blubber_dynamics_vascular_countercurrent_heat_exchangers",
                "question": "How does a warm-blooded whale maintain a 98.6°F body core while submerged in 28°F freezing saltwater?",
                "focus": "One-foot-thick subcutaneous blubber matrix, retia mirabilia (countercurrent heat exchange vessels where warm arterial blood warms returning venous blood in flippers), and blubber energy storage.",
                "reason": "Technical thermodynamic breakdown explaining how mammals colonized the freezing polar oceans."
            },
            {
                "id": 4,
                "title": "Baleen vs Teeth: The Evolutionary Split Between Filter-Feeders and Hunters",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "evolutionary_milestone",
                "slug": "baleen_vs_teeth_evolutionary_split_filter_feeders_hunters",
                "question": "How did keratinous fringe plates replace teeth to allow baleen whales to swallow millions of krill in a single gulp?",
                "focus": "The Oligocene evolutionary split, Mysticeti (baleen filter-feeders) vs Odontoceti (toothed echolocators), rorqual throat pleat expansion physics, and bulk-feeding energetics fueling gigantism.",
                "reason": "Explores the pivotal macro-evolutionary divergence that created the largest animals to ever exist."
            },
            {
                "id": 5,
                "title": "The Sirenians: Manatees and Dugongs, the Gentle Herbivorous Mermaids of Coastal Shallows",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "field_guide",
                "slug": "sirenians_manatees_dugongs_herbivorous_mermaids_shallows",
                "question": "How did land-dwelling elephant ancestors evolve into slow-moving, peaceful sea cows feeding entirely on seagrass meadows?",
                "focus": "Order Sirenia evolutionary ties to proboscideans (elephants), pachyostosis (extremely dense solid bones acting as biological divers' dive belts), boat propeller strike scars, and cold stress syndrome.",
                "reason": "Charming, essential profile of the only living herbivorous marine mammals."
            },
            {
                "id": 6,
                "title": "Biosonar and the Melon: How Toothed Whales Focus Sound Beams in Turbid Water",
                "tier": "Tier 2: Sensory Systems & Acoustics",
                "angle": "sensory_science",
                "slug": "biosonar_and_the_melon_how_toothed_whales_focus_sound",
                "question": "How does a dolphin use acoustic fat tissue in its forehead to detect a single coin dropped in murky water from 200 feet away?",
                "focus": "Phonic lips producing ultrasonic click trains, the fatty acoustic lens 'melon' directing sound cones, lower jaw bone transmitting return echoes to the middle ear, and acoustic target resolution.",
                "reason": "Deep dive into nature's most sophisticated bio-acoustic echolocation system."
            },
            {
                "id": 7,
                "title": "The Song of the Humpback: Global Pop Anthems, Rhyming Sequences, and Transmission",
                "tier": "Tier 2: Sensory Systems & Acoustics",
                "angle": "scientific_phenomenon",
                "slug": "song_of_the_humpback_global_pop_anthems_cultural_transmission",
                "question": "How do male humpback whales compose 30-minute structured songs that spread across entire ocean basins like viral pop music?",
                "focus": "Hierarchical song structure (units, sub-phrases, themes), Roger Payne's 1970 discovery, cultural horizontal transmission across Pacific populations, and deep mating display theories.",
                "reason": "Fascinating examination of non-human musical culture and complex vocal communication."
            },
            {
                "id": 8,
                "title": "Sea Otters: The Densest Fur in the Animal Kingdom, Tool Use, and Kelp Forests",
                "tier": "Tier 2: Sensory Systems & Acoustics",
                "angle": "keystone_species",
                "slug": "sea_otters_densest_fur_animal_kingdom_tool_use_kelp",
                "question": "How does a marine mammal without blubber survive freezing surf using 1 million hairs per square inch and stone anvils?",
                "focus": "Dense two-layer fur trapping air bubbles, high metabolic rate (eating 25% of body weight daily), using rocks to smash open abalone and urchins, and preventing sea urchin barren deserts.",
                "reason": "Celebrates the charismatic keystone predator that keeps coastal kelp forest ecosystems alive."
            },
            {
                "id": 9,
                "title": "Pinniped Locomotion: Phocids (True Seals) vs Otariids (Sea Lions) and Beach Colonies",
                "tier": "Tier 2: Sensory Systems & Acoustics",
                "angle": "comparative_analysis",
                "slug": "pinniped_locomotion_true_seals_vs_sea_lions_beach_colonies",
                "question": "Why can sea lions gallop on dry land using four flippers while true harbor seals must undulate like fat caterpillars?",
                "focus": "Earless Phocidae (swimming with rear flippers, wriggling on land) vs eared Otariidae (rotating hind flippers forward, swimming with front pectoral flippers), vibrissae whiskers, and haulout breeding.",
                "reason": "Clear comparative anatomical guide demystifying the pinniped family tree."
            },
            {
                "id": 10,
                "title": "Bubble-Net Feeding: Humpback Whales Coordinating Spiral Air Curtains to Trap Krill",
                "tier": "Tier 2: Sensory Systems & Acoustics",
                "angle": "behavioral_habits",
                "slug": "bubble_net_feeding_humpback_whales_spiral_air_curtains",
                "question": "How do pods of humpback whales use synchronized acoustic calls and spiral bubble rings to herd thousands of herring into a living corral?",
                "focus": "Blowhole bubble release creating cylindrical reflective acoustic walls that fish refuse to cross, dedicated trumpet call leader whales, synchronized upward lunges, and cultural pod transmission.",
                "reason": "Spectacular documentary showcase of cooperative hunting strategy and tactical ingenuity."
            },
            {
                "id": 11,
                "title": "Sperm Whales in the Abyss: Diving 7,000 Feet to Battle Giant Squid in Darkness",
                "tier": "Tier 3: Extreme Predation & Deep Diving",
                "angle": "extreme_scenarios",
                "slug": "sperm_whales_in_the_abyss_diving_7000_feet_battle_giant_squid",
                "question": "What happens when a 50-ton bull sperm whale descends into freezing, pitch-black abyssal trenches to hunt monstrous Architeuthis squid?",
                "focus": "Spermaceti organ cooling and crystallizing wax to adjust buoyancy, circular suction cup sucker scars, echolocating squid in zero light, and 230-decibel clicks capable of stunning prey.",
                "reason": "The quintessential deep-sea clash of titans documentary narrative."
            },
            {
                "id": 12,
                "title": "Orca Pod Cultures: Resident Fish Hunters vs Transient Marine Mammal Killers",
                "tier": "Tier 3: Extreme Predation & Deep Diving",
                "angle": "case_study",
                "slug": "orca_pod_cultures_resident_fish_hunters_transient_killers",
                "question": "Why do resident and transient orcas living in the exact same waters never interbreed, speak different dialects, and eat entirely different foods?",
                "focus": "Matriarchal clan leadership, resident salmon-eating pods vs transient mammal-hunting Bigg's killer whales, intentional beach-stranding hunting in Patagonia, and wave-washing seals off ice floes.",
                "reason": "Masterclass in cetacean culture, strategic intelligence, and distinct ecotype evolution."
            },
            {
                "id": 13,
                "title": "Bowhead Whales: 200-Year Lifespans, Cancer-Resistance Genetics, and Arctic Ice Breakers",
                "tier": "Tier 3: Extreme Predation & Deep Diving",
                "angle": "medical_science",
                "slug": "bowhead_whales_200_year_lifespans_cancer_resistance_genetics",
                "question": "How do bowhead whales live for over two centuries without developing cancer, despite having 1,000 times more cells than humans?",
                "focus": "Peto's Paradox, ancient stone and 19th-century slate harpoon points found in living whales, ERCC1 DNA repair gene duplication, reinforced heavy skulls breaking through 2-foot sea ice, and Arctic life.",
                "reason": "Incredible medical and evolutionary biology breakthrough illuminating the secrets of extreme longevity."
            },
            {
                "id": 14,
                "title": "The Beluga and Narwhal: The Canaries of the Sea and the Mystery of the Spiral Tusk",
                "tier": "Tier 3: Extreme Predation & Deep Diving",
                "angle": "biological_guide",
                "slug": "beluga_and_narwhal_canaries_of_sea_spiral_tusk_mystery",
                "question": "Is the narwhal's 9-foot spiraled ivory tusk a medieval unicorn horn, a jousting weapon, or a giant sensory organ with 10 million nerve endings?",
                "focus": "Monodontidae family biology, flexible neck vertebrae in belugas, narwhal left canine tooth tusk hydrodynamics and salinity sensing, melodic acoustic chirps, and living in packed leads of Arctic pack ice.",
                "reason": "Fascinating examination of the high-Arctic's two most enigmatic and specialized cetaceans."
            },
            {
                "id": 15,
                "title": "Elephant Seals: Fighting for Beach Harems and Deep-Diving Sleep Drifts",
                "tier": "Tier 3: Extreme Predation & Deep Diving",
                "angle": "field_guide",
                "slug": "elephant_seals_fighting_beach_harems_deep_diving_sleep_drifts",
                "question": "How do 4-ton bull elephant seals battle bloody territorial duels on beaches, and how do they take 10-minute micro-sleep naps while spiraling toward the ocean floor?",
                "focus": "Inflatable proboscis acoustic amplifiers, chest shield keratin calluses, 5,000-foot foraging dives, slow-wave sleep while drifting like leaves in deep water, and surviving near-extinction from sealing.",
                "reason": "Dramatic, gritty documentary look at the sheer brute power and deep-water endurance of elephant seals."
            },
            {
                "id": 16,
                "title": "Cetacean Culture and Dialects: Maternal Grammars, Tool Passing, and Non-Human Culture",
                "tier": "Tier 4: Culture, Intelligence & Human Impact",
                "angle": "cognitive_science",
                "slug": "cetacean_culture_dialects_maternal_grammars_tool_passing",
                "question": "Why do marine biologists now officially classify whales and dolphins as non-human beings with distinct cultural traditions passed down generations?",
                "focus": "Spindle neurons in cetacean insular cortices, Shark Bay bottlenose dolphins teaching daughters to use sea sponges as protective nose-guards, coda click dialects, and post-menopausal grandmother orcas leading pods.",
                "reason": "Profound cognitive science overview challenging human exceptionalism."
            },
            {
                "id": 17,
                "title": "The Whaling Catastrophe: Industrial Harpoons, the Save the Whales Movement, and Recovery",
                "tier": "Tier 4: Culture, Intelligence & Human Impact",
                "angle": "historical_moment",
                "slug": "whaling_catastrophe_industrial_harpoons_save_the_whales",
                "question": "How did explosive harpoons and factory ships slaughter 3 million whales in the 20th century before Greenpeace and the IWC moratorium stopped the carnage?",
                "focus": "Svend Foyn's 1864 explosive harpoon gun, whale oil lighting cities and lubricating machinery, the 1986 International Whaling Commission commercial ban, and the slow, miraculous recovery of humpbacks and blues.",
                "reason": "The landmark environmental narrative that gave birth to modern global conservation consciousness."
            },
            {
                "id": 18,
                "title": "Naval Active Sonar and Mass Strandings: Acoustic Trauma in Beaked Whales",
                "tier": "Tier 4: Culture, Intelligence & Human Impact",
                "angle": "investigative",
                "slug": "naval_active_sonar_mass_strandings_acoustic_trauma_beaked_whales",
                "question": "Why do 235-decibel mid-frequency military sonar exercises cause terrified deep-diving whales to panic, surface too fast, and bleed from their brains?",
                "focus": "The Bahamas 2000 and Canary Islands naval exercises, acoustic tissue cavitation, decompression sickness in marine mammals, legal battles between NRDC and the US Navy, and real-time acoustic monitoring.",
                "reason": "Urgent investigative report on the invisible sound weapons wreaking havoc on deep-sea cetaceans."
            },
            {
                "id": 19,
                "title": "The Captivity Reckoning: How 'Blackfish' and Neuroscientific Research Ended Orca Shows",
                "tier": "Tier 4: Culture, Intelligence & Human Impact",
                "angle": "ethical_dilemma",
                "slug": "captivity_reckoning_blackfish_neuroscience_ended_orca_shows",
                "question": "What psychological damage causes killer whales in concrete theme park tanks to chew metal gates, collapse dorsal fins, and attack trainers?",
                "focus": "The capture of Tilikum, sensory deprivation in chlorinate pools, acoustic echo reverberation torture, neuroimaging of the expanded cetacean paralimbic system, SeaWorld ending captive breeding, and coastal sanctuaries.",
                "reason": "Powerful ethical and scientific turning point in human society's relationship with intelligent ocean mammals."
            },
            {
                "id": 20,
                "title": "Ocean Decibel Pollution: Ship Propeller Cavitation Drowning Out Communication",
                "tier": "Tier 4: Culture, Intelligence & Human Impact",
                "angle": "environmental_action",
                "slug": "ocean_decibel_pollution_ship_propeller_cavitation_communication",
                "question": "How has the relentless background roar of 60,000 commercial cargo ships shrunk the communication space of North Atlantic right whales by 90%?",
                "focus": "Propeller blade cavitation acoustics, chronic acoustic stress measured in whale feces cortisol, slowing container ships down to 10 knots in migratory corridors, and electric/quieter propeller hull designs.",
                "reason": "Forward-looking capstone addressing the solvable challenge of quieting human industrial noise in global oceans."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Orcas Attacking Yachts in Gibraltar: Gladis the Whale and the Spreading Rudder Trend",
                "trend_score": 97,
                "angle": "viral_news",
                "slug": "orcas_attacking_yachts_gibraltar_gladis_rudder_trend",
                "why_trending": "Massive global viral news fascination covering Iberian killer whales systematically snapping rudders and sinking luxury sailboats.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "The 52-Hertz Whale: The 'Loneliest Whale in the World' Singing Unheard",
                "trend_score": 96,
                "angle": "emotional_legend",
                "slug": "52_hertz_whale_loneliest_whale_in_world_unheard",
                "why_trending": "Perennial emotional pop culture and documentary favorite tracking the solitary sonic nomad whose song is too high-pitched for other baleen whales.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Sperm Whale Click Decoders: Project CETI Using AI to Translate Whale Language",
                "trend_score": 95,
                "angle": "tech_breakthrough",
                "slug": "sperm_whale_click_decoders_project_ceti_ai_translation",
                "why_trending": "Major breakthrough in machine learning linguistics decoding phonetic alphabets and rhythm codas in sperm whale acoustic communications.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "The Vaquita Marina: Racing to Save the 10 Remaining Porpoises from Extinction",
                "trend_score": 93,
                "angle": "conservation_urgency",
                "slug": "vaquita_marina_racing_to_save_10_remaining_porpoises",
                "why_trending": "High-tension documentary drama following Sea Shepherd gunboat patrols confiscating illegal totoaba gillnets in Mexico's Sea of Cortez.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Blue Whale Heart Mechanics: The Size of a Small Car Pumping 60 Gallons per Beat",
                "trend_score": 94,
                "angle": "biological_wonder",
                "slug": "blue_whale_heart_mechanics_car_sized_circulatory_pump",
                "why_trending": "Viral biological facts showcasing the 400-pound heart of Balaenoptera musculus with aorta arteries wide enough for a human toddler to crawl through.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Walrus Tusk Battles: Massive Arctic Tusks Used as Sled Runners and Deadly Weapons",
                "trend_score": 90,
                "angle": "arctic_wildlife",
                "slug": "walrus_tusk_battles_arctic_sled_runners_deadly_weapons",
                "why_trending": "Spectacular Arctic wildlife footage showing 3,000-pound bulls clashing on pack ice and using 3-foot tusks to haul themselves out of freezing water.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Dolphin Echolocation Vision: Can Bottlenose Dolphins 'See' Unborn Human Babies?",
                "trend_score": 92,
                "angle": "sensory_wonder",
                "slug": "dolphin_echolocation_vision_seeing_unborn_human_babies",
                "why_trending": "Intriguing biological question explaining how ultrasound echolocation penetrative acoustic waves reveal human skeletons and fetal heartbeats.",
                "status": "Queued"
            }
        ]
    },
    "198_marine_life": {
        "id": "198",
        "slug": "marine_life",
        "title": "Marine Life",
        "category": "Life_Biology",
        "audience": "Marine Biologists, Scuba Divers, Oceanographers, Aquarium Curators, Documentary Fans (Global)",
        "progression": [
            ("Tier 1: Oceanic Ecosystems & Pelagic Zones: Sunlight to Hadal Trenches, Plankton Foundations & Buoyancy Mechanics (Beginner / Scratch)",
             "Vertical ocean bathymetry (epipelagic to hadal zones), phytoplankton photosynthetic oxygen engines, swim bladder and squalene liver buoyancy, and marine food webs."),
            ("Tier 2: Cephalopods & Invertebrate Intelligence: Chromatophore Camouflage, Giant Squids, Nautiluses & Jellyfish Stings (Intermediate)",
             "Cephalopod chromatophore and iridophore color shifting, decentralized arm neural architecture, cnidocyte explosive cell mechanics in jellyfish, and chambered nautilus buoyancy physics."),
            ("Tier 3: Sharks & Apex Fish Predators: Ampullae of Lorenzini, Great Whites, Manta Rays & Deep-Sea Adaptations (Upper Intermediate)",
             "Shark electroreception through Ampullae of Lorenzini, great white predatory breach hunting, twilight zone bioluminescent counterillumination, and bizarre anglerfish sexual parasitism."),
            ("Tier 4: Abyssal Frontiers, Extremophiles & Ocean Acidification: Hydrothermal Vents, Plastic Gyres & Marine Reserves (Advanced / Masterclass)",
             "Chemosynthetic hydrothermal vent ecology, hadal trench pressure survival, ocean acidification calcium carbonate degradation, microplastic biomagnification, and High Seas treaties.")
        ],
        "flagship": {
            "title": "The Vertical Ocean: Journey from the Sunlit Surface to the Challenger Deep",
            "angle": "deep_dive",
            "slug": "198_marine_life_deep_dive_the_vertical_ocean"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Vertical Ocean: Journey from the Sunlit Surface to the Challenger Deep",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "vertical_ocean_journey_from_sunlit_surface_to_challenger_deep",
                "question": "How do temperature, light, and pressure transform marine life as you descend 36,000 feet into the ocean abyss?",
                "focus": "The five vertical ocean zones: Epipelagic (sunlight), Mesopelagic (twilight), Bathypelagic (midnight), Abyssopelagic (abyss), and Hadalpelagic (trenches), pressure gradients (1 atm every 33 feet), and biological adaptations.",
                "reason": "The quintessential masterclass roadmap organizing the entire vertical architecture of ocean life."
            },
            {
                "id": 2,
                "title": "Phytoplankton and the Ocean's Lungs: How Microscopic Diatoms Generate 50% of Oxygen",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "phytoplankton_oceans_lungs_microscopic_diatoms_oxygen",
                "question": "How does every second breath of air you breathe come not from rainforest trees, but from microscopic floating algae drifting in the sea?",
                "focus": "Diatoms with silica glass frustules, coccolithophores with calcium carbonate shells, the marine biological carbon pump sequestering gigatons of CO2, and satellite bloom monitoring.",
                "reason": "Grounds marine biology in the indispensable planetary oxygen engine sustaining all terrestrial animal life."
            },
            {
                "id": 3,
                "title": "Buoyancy Engineering: Swim Bladders, Squalene Livers, and Neutral Equilibrium",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "buoyancy_engineering_swim_bladders_squalene_livers_equilibrium",
                "question": "How do fish hover motionless at 50 feet without floating to the surface or sinking to the bottom like stones?",
                "focus": "Gas gland rete mirabile concentrating oxygen into swim bladders against immense pressure gradients, barotrauma stomach eversion when brought up too fast, and sharks using oil-rich squalene livers.",
                "reason": "Technical physics and biological breakdown of how marine organisms control density and depth."
            },
            {
                "id": 4,
                "title": "Osmoregulation in Marine Fish: Drinking Seawater and Excreting Brine via Chloride Cells",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "scientific_phenomenon",
                "slug": "osmoregulation_in_marine_fish_drinking_seawater_excreting_brine",
                "question": "Why would a freshwater goldfish die of dehydration in the ocean, while saltwater tuna drink ocean water continuously?",
                "focus": "Osmotic pressure gradient (water flowing out of fish into saltier ocean), specialized gill chloride cells actively pumping out sodium and chloride ions, concentrated urine, and salmon transitioning between fresh and saltwater.",
                "reason": "Fascinating biochemical exploration of the cellular cellular salt-water balance required in marine life."
            },
            {
                "id": 5,
                "title": "The Pelagic Food Web: Zooplankton, Krill Swarms, and Marine Energy Transfer",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "pelagic_food_web_zooplankton_krill_swarms_energy_transfer",
                "question": "How does solar energy captured by microscopic algae travel up trophic levels to fuel 100-ton whales and apex sharks?",
                "focus": "Copepods and Antarctic krill (Euphausia superba) biomass exceeding 500 million tons, the 10% trophic energy transfer rule, forage fish (anchovies, sardines) schooling dynamics, and marine trophic cascades.",
                "reason": "Establishes the fundamental thermodynamic and ecological food web driving all ocean productivity."
            },
            {
                "id": 6,
                "title": "Cephalopod Camouflage: Chromatophores, Iridophores, and Texture-Shifting Papillae",
                "tier": "Tier 2: Invertebrates & Cephalopod Wonders",
                "angle": "materials_science",
                "slug": "cephalopod_camouflage_chromatophores_iridophores_papillae",
                "question": "How does a colorblind cuttlefish instantly mimic the color, pattern, and 3D texture of coral reef rocks in 200 milliseconds?",
                "focus": "Neuromuscular chromatophore pigment sacs, reflective structural iridophores, white leucophores, dermal papillae muscles puckering skin into rough spikes, and opsin skin photoreception.",
                "reason": "Masterclass in active optical camouflage and biological metamaterials."
            },
            {
                "id": 7,
                "title": "The Octopus Mind: Distributed Neurons in Eight Arms and Decentralized Problem Solving",
                "tier": "Tier 2: Invertebrates & Cephalopod Wonders",
                "angle": "cognitive_science",
                "slug": "octopus_mind_distributed_neurons_eight_arms_decentralized",
                "question": "What is it like to possess two-thirds of your nervous system distributed inside your eight semi-autonomous arms?",
                "focus": "500 million neurons organized in a decentralized peripheral architecture, arms exploring and tasting independently, opening childproof jars, play behavior, and navigating mazes.",
                "reason": "Mind-bending exploration of an alien form of intelligence that evolved completely independently from vertebrate brains."
            },
            {
                "id": 8,
                "title": "Jellyfish and Cnidocytes: The Fastest Cellular Hypodermic Launchers in the Animal Kingdom",
                "tier": "Tier 2: Invertebrates & Cephalopod Wonders",
                "angle": "extreme_scenarios",
                "slug": "jellyfish_cnidocytes_fastest_cellular_hypodermic_launchers",
                "question": "How does a Box Jellyfish fire hundreds of thousands of venomous barbed needles with an acceleration of 5 million Gs?",
                "focus": "Osmotic pressure spring loading (200 atmospheres of internal pressure), microsecond coiled tubule eversion, neurotoxins causing cardiac arrest within minutes, and vinegar neutralization chemistry.",
                "reason": "High-tension cellular biomechanics breakdown of one of the deadliest and most ancient predatory mechanisms on Earth."
            },
            {
                "id": 9,
                "title": "The Chambered Nautilus: Living Fossils and Siphuncle Osmotic Gas-Buoyancy Pumps",
                "tier": "Tier 2: Invertebrates & Cephalopod Wonders",
                "angle": "evolutionary_milestone",
                "slug": "chambered_nautilus_living_fossils_siphuncle_buoyancy_pumps",
                "question": "How has an ancient shelled cephalopod survived 500 million years without evolving, using an internal living pipe to regulate buoyancy?",
                "focus": "Septate logarithmic spiral shell chambers, the living siphuncle tissue strand pumping ions to draw water out and replace it with gas, pinhole camera eye without a lens, and surviving deep reef slopes.",
                "reason": "Fascinating examination of an ancient living fossil possessing one of the most elegant geometric shells in nature."
            },
            {
                "id": 10,
                "title": "Giant and Colossal Squids: Swiveling Tentacle Hooks, 10-Inch Eyes, and Deep-Sea Enigmas",
                "tier": "Tier 2: Invertebrates & Cephalopod Wonders",
                "angle": "mystery_unsolved",
                "slug": "giant_and_colossal_squids_swiveling_hooks_10_inch_eyes",
                "question": "What makes the colossal squid (Mesonychoteuthis hamiltoni) the heaviest invertebrate on Earth, armed with 360-degree swiveling talon claws?",
                "focus": "Giant squid (Architeuthis) vs Colossal squid, 10-inch diameter eyes detecting bioluminescent silhouettes of approaching sperm whales, ammonium chloride tissue buoyancy, and specimen dissections.",
                "reason": "Legendary marine mystery documentary examining the real-life sea monsters of the deep ocean."
            },
            {
                "id": 11,
                "title": "Ampullae of Lorenzini: How Sharks Detect Microvolt Electrical Signals of Hearts",
                "tier": "Tier 3: Apex Predators & Deep Frontiers",
                "angle": "sensory_science",
                "slug": "ampullae_of_lorenzini_sharks_detect_microvolt_signals",
                "question": "How can a hammerhead shark locate a stingray buried completely under sand using electroreceptive pores across its snout?",
                "focus": "Gel-filled pores lined with semiconductor-like glycoprotein, detecting electrical fields down to 5 nanovolts/cm (equivalent to detecting an AA battery 1,000 miles away), and geomagnetic navigation.",
                "reason": "Explores the extraordinary sixth sense that crowns sharks as the ocean's ultimate sensory hunters."
            },
            {
                "id": 12,
                "title": "The Great White Shark: Endothermic Retia Mirabilia, Hunting Breaches, and Farallon Dynamics",
                "tier": "Tier 3: Apex Predators & Deep Frontiers",
                "angle": "apex_predators",
                "slug": "great_white_shark_endothermic_retia_mirabilia_hunting_breaches",
                "question": "Why can great white sharks sprint at 25 MPH and launch their 2-ton bodies 10 feet into the air to strike seals?",
                "focus": "Regional endothermy (warming stomach, red muscle, and eyes 25°F above water temperature), explosive vertical breach strikes at Seal Island, serrated triangular cutting teeth, and satellite tracking across the 'White Shark Café'.",
                "reason": "The quintessential apex predator profile detailing the physiology, hydrodynamics, and hunting genius of Carcharodon carcharias."
            },
            {
                "id": 13,
                "title": "Bioluminescence in the Twilight Zone: Counterillumination, Burglar Alarms, and Glowing Lures",
                "tier": "Tier 3: Apex Predators & Deep Frontiers",
                "angle": "natural_marvels",
                "slug": "bioluminescence_twilight_zone_counterillumination_alarms",
                "question": "Why do 90% of creatures in the ocean's midnight zone produce their own light, and how do hatchetfish erase their own shadows?",
                "focus": "Photophore light organs along belly scales matching downwelling sunlight (counterillumination cloaking), jellyfish flashing burglar alarms to summon larger predators, and red light searchlights in dragonfish.",
                "reason": "Spectacular visual journey into the glowing alien galaxy of the deep ocean."
            },
            {
                "id": 14,
                "title": "Giant Manta Rays and Whale Sharks: Gentle Filter-Feeding Behemoths of the Open Ocean",
                "tier": "Tier 3: Apex Predators & Deep Frontiers",
                "angle": "field_guide",
                "slug": "giant_manta_rays_whale_sharks_filter_feeding_behemoths",
                "question": "How do 20-foot manta rays and 40-foot whale sharks find dense plankton blooms across millions of square miles of desert-like blue water?",
                "focus": "Manta ray cephalic horn fins funneling water, largest brain-to-body ratio of any fish, self-recognition mirror test results, whale shark dermal denticles as thick as car tires, and ecotourism guidelines.",
                "reason": "Uplifting, majestic showcase of the gentle giants of the open pelagic realm."
            },
            {
                "id": 15,
                "title": "Anglerfish Reproduction: Extreme Sexual Parasitism and Bioluminescent Bacterial Escas",
                "tier": "Tier 3: Apex Predators & Deep Frontiers",
                "angle": "bizarre_biology",
                "slug": "anglerfish_reproduction_sexual_parasitism_bioluminescent_escas",
                "question": "Why does a tiny male deep-sea anglerfish bite into a massive female's belly and permanently fuse his circulatory system into hers?",
                "focus": "Illophore fishing rod with symbiotic bioluminescent Photobacterium esca lure, severe immune system shutdown preventing tissue rejection in fused males, sperm banking, and expanding expandable jaws.",
                "reason": "Examines one of the most bizarre and extreme reproductive adaptations in all of zoology."
            },
            {
                "id": 16,
                "title": "Hydrothermal Vents and Chemosynthesis: Ecosystems Thriving Without Sunlight",
                "tier": "Tier 4: Extreme Frontiers & Conservation",
                "angle": "extremophiles",
                "slug": "hydrothermal_vents_chemosynthesis_ecosystems_without_sunlight",
                "question": "How do 6-foot giant tube worms with bright red plumes flourish around 700°F black smokers without a mouth, gut, or sunlight?",
                "focus": "The 1977 Alvin submersible discovery, hydrogen sulfide chemosynthesis via symbiotic bacteria inside the trophosome, Yeti crabs farming bacteria on hairy claws, and origins of life hypotheses.",
                "reason": "Groundbreaking biological discovery proving life can flourish entirely decoupled from the sun."
            },
            {
                "id": 17,
                "title": "The Hadal Zone: Mariana Trench Pressures Exceeding 1,000 Atmospheres and Snailfish",
                "tier": "Tier 4: Extreme Frontiers & Conservation",
                "angle": "extreme_scenarios",
                "slug": "hadal_zone_mariana_trench_pressures_snailfish_survival",
                "question": "How can delicate, translucent Mariana snailfish swim comfortably at 26,000 feet under water pressure that would crush a steel submarine like a soda can?",
                "focus": "Trimethylamine N-oxide (TMAO) piezolyte molecules stabilizing cellular proteins against pressure denaturation, absence of swim bladders, flexible cartilaginous skulls, and feeding on sinking amphipods.",
                "reason": "Fascinating examination of life pushed to the absolute extreme physical limits of our planet."
            },
            {
                "id": 18,
                "title": "Ocean Acidification: How Dissolving Carbonic Acid Degrades Calcium Carbonate Shells",
                "tier": "Tier 4: Extreme Frontiers & Conservation",
                "angle": "investigative",
                "slug": "ocean_acidification_carbonic_acid_calcium_carbonate_pteropods",
                "question": "Why are sea butterfly (pteropod) shells literally dissolving in acidic ocean waters like chalk in vinegar?",
                "focus": "CO2 absorption forming carbonic acid (H2CO3) and stripping carbonate ions, pteropod shell dissolution experiments, impacts on larval oyster hatcheries, and the threat to marine food web foundations.",
                "reason": "Crucial investigative science report on the 'evil twin of climate change' threatening ocean chemistry."
            },
            {
                "id": 19,
                "title": "The Great Pacific Garbage Patch: Microplastic Biomagnification Up the Food Chain",
                "tier": "Tier 4: Extreme Frontiers & Conservation",
                "angle": "environmental_dilemma",
                "slug": "great_pacific_garbage_patch_microplastic_biomagnification",
                "question": "How do millions of tons of plastic waste trapped in circulating ocean gyres break down into toxic microplastics consumed by fish?",
                "focus": "Subtropical oceanic convergence zones, photolytic fragmentation into microscopic particles, endocrine-disrupting chemicals (phthalates, BPA) adsorbing to plastic pellets, and The Ocean Cleanup barrier system.",
                "reason": "High-urgency ecological investigation into global plastic pollution affecting marine and human health."
            },
            {
                "id": 20,
                "title": "High Seas Governance: The UN Treaty for the High Seas and Global Sanctuaries",
                "tier": "Tier 4: Extreme Frontiers & Conservation",
                "angle": "policy_conservation",
                "slug": "high_seas_governance_un_biodiversity_treaty_marine_sanctuaries",
                "question": "How will the historic 2023 UN High Seas Biodiversity Treaty protect two-thirds of the world's oceans that lie outside any country's jurisdiction?",
                "focus": "The 30x30 global conservation target (protecting 30% of oceans by 2030), environmental impact assessments for deep-sea activities, sharing marine genetic resources, and enforcing international anti-poaching patrols.",
                "reason": "Visionary capstone outlining the international legal architecture guarding the future of our living oceans."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Immortal Jellyfish (Turritopsis Dohrnii): Transdifferentiating Cells to Age in Reverse",
                "trend_score": 97,
                "angle": "viral_biology",
                "slug": "immortal_jellyfish_turritopsis_dohrnii_reversing_age_cells",
                "why_trending": "Massive global virality exploring the only known animal capable of reverting from sexually mature medusa back into a baby polyp forever.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Megalodon vs Modern Whales: Debunking Internet Myths About Extinct Giant Sharks",
                "trend_score": 96,
                "angle": "prehistoric_debate",
                "slug": "megalodon_vs_modern_whales_debunking_internet_myths",
                "why_trending": "Unmatched YouTube view counts analyzing the 50-foot Otodus megalodon, bite mechanics, and definitively disproving Discovery Channel fake sightings.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "The Blue-Ringed Octopus: A Golf-Ball Sized Tidepool Creature Carrying Lethal Tetrodotoxin",
                "trend_score": 95,
                "angle": "thrill_seeker",
                "slug": "blue_ringed_octopus_tidepool_creature_tetrodotoxin",
                "why_trending": "Viral TikToks showing tourists accidentally holding deadly glowing blue-ringed octopuses on Australian beaches with zero clue of lethal danger.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Greenland Shark Longevity: The 400-Year-Old Vertebrate Swimming Since the Renaissance",
                "trend_score": 94,
                "angle": "biological_wonder",
                "slug": "greenland_shark_longevity_400_year_old_vertebrate_arctic",
                "why_trending": "Fascinating radiocarbon eye lens dating proving slow-moving Arctic Greenland sharks can live up to 500 years in icy waters.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Deep-Sea Mining Controversies: Companies Harvesting Polymetallic Nodules on the Abyssal Plain",
                "trend_score": 93,
                "angle": "controversial_debate",
                "slug": "deep_sea_mining_controversies_polymetallic_nodules_abyssal",
                "why_trending": "Heated international geopolitical clash over scraping the Clarion-Clipperton Zone floor for EV battery nickel vs destroying pristine ecosystems.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Deep-Sea Barreleye Fish: The Translucent Dome Head with Upward-Rotating Green Tubular Eyes",
                "trend_score": 92,
                "angle": "natural_wonder",
                "slug": "deep_sea_barreleye_fish_translucent_dome_head_green_eyes",
                "why_trending": "High-retention visual spectacle showing MBARI high-def ROV video of Macropinna microstoma glowing green eyes inside a transparent skull.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "The Great Sardine Run: Millions of Fish Forming Giant Bait Balls Under Attack",
                "trend_score": 91,
                "angle": "wildlife_spectacle",
                "slug": "great_sardine_run_billions_fish_bait_balls_predator_feeding",
                "why_trending": "Epic wildlife spectacle along South Africa's Wild Coast featuring dolphins, sharks, cape gannets, and Bryde's whales attacking swirling bait balls.",
                "status": "Queued"
            }
        ]
    },
    "199_coral_reefs": {
        "id": "199",
        "slug": "coral_reefs",
        "title": "Coral Reefs",
        "category": "Life_Biology",
        "audience": "Marine Ecologists, Scuba Divers, Reef Aquarists, Coral Restoration Specialists, Ocean Conservationists (Global)",
        "progression": [
            ("Tier 1: Coral Biology & Symbiotic Foundations: Polyps, Zooxanthellae, Calcium Carbonate Skeletons & Reef Types (Beginner / Scratch)",
             "Cnidarian polyp anatomy, endosymbiotic dinoflagellate algae (zooxanthellae) photosynthesis, aragonite biomineralization, and the 3 classic reef formations (fringing, barrier, atoll)."),
            ("Tier 2: Biodiversity & Interspecies Symbiosis: Clownfish, Cleaner Shrimp, Parrotfish Grazing & Territorial Warfare (Intermediate)",
             "Synchronized lunar mass spawning, chemical warfare (sweeper tentacles), clownfish-anemone mutualism, parrotfish bioerosion creating white sand beaches, and cleaner stations."),
            ("Tier 3: Environmental Pressures & Thermal Bleaching: Marine Heatwaves, Ocean Acidification & Crown-of-Thorns Outbreaks (Upper Intermediate)",
             "Cellular mechanics of thermal bleaching, the Great Barrier Reef consecutive heatwaves, venomous Crown-of-Thorns starfish plagues, ocean acidification, and deep mesophotic twilight reefs."),
            ("Tier 4: Coral Restoration Science & Future Resilience: Super Corals, Larval Seeding, Cryopreservation & Marine Parks (Advanced / Masterclass)",
             "Micro-fragmentation nursery propagation, selective breeding of heat-resilient 'super corals', coral gamete cryopreservation biobanks, artificial 3D-printed reefs, and global economic value.")
        ],
        "flagship": {
            "title": "The Rainforest of the Sea: How Tiny Polyps Build the Only Living Structures Visible from Space",
            "angle": "deep_dive",
            "slug": "199_coral_reefs_deep_dive_rainforest_of_the_sea"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Rainforest of the Sea: How Tiny Polyps Build Living Structures Visible from Space",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "rainforest_of_the_sea_polyps_build_structures_visible_from_space",
                "question": "How do soft, centimeter-sized colonial animals build 1,400-mile long limestone ramparts that support 25% of all marine species?",
                "focus": "Cnidarian colonial morphology, shared gastrovascular networks connecting thousands of polyps, symbiotic energy transfer, and why coral reefs cover less than 1% of the ocean floor yet harbor a quarter of all marine life.",
                "reason": "The quintessential masterclass establishing the breathtaking scale and biological wonder of coral reef ecosystems."
            },
            {
                "id": 2,
                "title": "The Coral-Algae Symbiosis: How Zooxanthellae Photosynthesize to Feed Animal Hosts",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "coral_algae_symbiosis_zooxanthellae_photosynthesize_feed_hosts",
                "question": "What mutualistic biochemical contract allows plant-like microalgae living inside animal cells to trade glucose for shelter and nitrogen?",
                "focus": "Symbiodiniaceae dinoflagellates residing within coral gastrodermal cells, transferring up to 90% of photosynthetic sugars to the host, coral waste recycling (ammonia and CO2), and vibrant coral pigments.",
                "reason": "Explores the fundamental microscopic partnership upon which all coral reef existence depends."
            },
            {
                "id": 3,
                "title": "Scleractinian Biomineralization: How Polyps Precipitate Aragonite Calcium Carbonate Skeletons",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "scleractinian_biomineralization_polyps_precipitate_aragonite",
                "question": "How does the basal ectoderm of a coral polyp extract calcium and bicarbonate ions from seawater to build crystalline rock houses?",
                "focus": "The sub-calicoblastic extracellular space, proton pumping enzymes raising local pH, organic matrix scaffolding, aragonite crystal lattice deposition, and annual skeletal growth rings.",
                "reason": "Deep dive into the biochemical and crystallographic engineering of limestone reef building."
            },
            {
                "id": 4,
                "title": "The Three Reef Morphologies: Fringing Reefs, Barrier Reefs, and Darwin's Atoll Theory",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "three_reef_morphologies_fringing_barrier_darwin_atoll_theory",
                "question": "How did Charles Darwin deduce that ring-shaped coral atolls in the deep ocean are the tombstones of sunken volcanic islands?",
                "focus": "Darwin's 1842 The Structure and Distribution of Coral Reefs, fringing reefs hugging shorelines, barrier reefs separated by lagoons, volcanic island tectonic subsidence, and deep drilling verification.",
                "reason": "Combines geomorphology, tectonic plate movement, and historical scientific discovery."
            },
            {
                "id": 5,
                "title": "Soft Corals vs Hard Corals: Octocorals, Gorgonians, and Calcareous Spicules",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "soft_corals_vs_hard_corals_octocorals_gorgonians_spicules",
                "question": "Why do flexible sea fans sway gracefully in ocean currents while stony brain corals remain rigid and rock-solid?",
                "focus": "Hexacorallia (hard corals with 6-fold polyp symmetry) vs Octocorallia (soft corals with 8 feathery tentacles), gorgonin protein internal rods, microscopic calcium spicules (sclerites), and current feeding.",
                "reason": "Essential taxonomic comparison clarifying the structural divergence of coral forms."
            },
            {
                "id": 6,
                "title": "Synchronized Mass Coral Spawning: Chemical Triggers, Moonlight Cues, and Gamete Slicks",
                "tier": "Tier 2: Biodiversity & Interspecies Symbiosis",
                "angle": "natural_marvels",
                "slug": "synchronized_mass_coral_spawning_chemical_moonlight_triggers",
                "question": "How do dozens of distinct coral species across hundreds of miles release billions of egg and sperm bundles on the exact same hour of the same night?",
                "focus": "Spring water temperature triggers, twilight cryptochrome moonlight reception, synchronized gamete release over a 20-minute window, pink surface slicks visible from space, and free-swimming planula larvae.",
                "reason": "One of the most awe-inspiring, coordinated reproductive spectacles on planet Earth."
            },
            {
                "id": 7,
                "title": "Territorial Warfare on the Reef: Mesenterial Filaments and Sweeper Tentacles",
                "tier": "Tier 2: Biodiversity & Interspecies Symbiosis",
                "angle": "behavioral_habits",
                "slug": "territorial_warfare_on_reef_mesenterial_filaments_sweepers",
                "question": "What happens when two slow-growing coral colonies compete for sunlight, and how do they digest their neighbors at night?",
                "focus": "Sweeper tentacles extending 5x normal length packed with cnidocytes, extruding digestive mesenterial gut filaments directly onto adjacent competitors, and chemical spatial dominance battles.",
                "reason": "Reveals the fierce, silent nighttime territorial warfare raging among seemingly stationary corals."
            },
            {
                "id": 8,
                "title": "The Anemone and the Clownfish: Mucus Chemical Immunity and Mutualistic Protection",
                "tier": "Tier 2: Biodiversity & Interspecies Symbiosis",
                "angle": "symbiosis_study",
                "slug": "anemone_and_clownfish_mucus_immunity_mutualistic_protection",
                "question": "Why doesn't a sea anemone's lethal stinging tentacles fire when an Amphiprion clownfish snuggles directly into them?",
                "focus": "The clownfish sugar-based mucus coat mimicking the anemone's own chemical signature, cleaning the anemone of parasites, providing nitrogen waste fertilizer, and aggressive territorial defense by clownfish.",
                "reason": "Celebrates the most iconic, heartwarming mutualistic partnership in marine biology."
            },
            {
                "id": 9,
                "title": "Parrotfish and Bioerosion: How Coral-Munching Herbivores Produce Tropical Sand Beaches",
                "tier": "Tier 2: Biodiversity & Interspecies Symbiosis",
                "angle": "ecological_keystone",
                "slug": "parrotfish_and_bioerosion_coral_grazing_white_sand_beaches",
                "question": "How does a single colorful parrotfish scrape dead coral with a fused beak to poop out 900 pounds of pristine white sand every single year?",
                "focus": "Fused bird-like dental plates stronger than copper and gold, pharyngeal mill grinding limestone rock into fine sand, grazing macroalgae that would otherwise smother corals, and nighttime sleeping mucus cocoons.",
                "reason": "Incredible demonstration of keystone ecological grazing and natural beach formation."
            },
            {
                "id": 10,
                "title": "Cleaner Stations: Mutualistic Parasite Removal and the Etiquette of Reef Predators",
                "tier": "Tier 2: Biodiversity & Interspecies Symbiosis",
                "angle": "field_guide",
                "slug": "cleaner_stations_mutualistic_parasite_removal_predator_etiquette",
                "question": "Why do ferocious 6-foot moray eels and groupers open their mouths wide and never bite the tiny cleaner shrimp picking food out of their teeth?",
                "focus": "Labroides dimidiatus cleaner wrasses and Lysmata cleaner shrimp, visual dance advertising, client pose signaling (mouth open, color blanched), mutual trust economics, and mimic fangblenny cheats.",
                "reason": "Fascinating behavioral ecology study in cross-species mutualism and social contracts."
            },
            {
                "id": 11,
                "title": "Coral Bleaching Dynamics: How a 1°C Temperature Spike Expels Algal Engines",
                "tier": "Tier 3: Environmental Pressures & Bleaching",
                "angle": "scientific_phenomenon",
                "slug": "coral_bleaching_dynamics_1c_spike_expels_algal_engines",
                "question": "What exact cellular breakdown turns a thriving, colorful living reef into a ghostly white bone field within weeks of a summer marine heatwave?",
                "focus": "Thermal stress destabilizing algal photosystem II, producing toxic reactive oxygen species (ROS), host polyps expelling poisoned zooxanthellae to survive, starvation timeline, and fluorescent glowing sunscreen death cries.",
                "reason": "Essential cellular pathology breakdown explaining the mechanism behind the global coral crisis."
            },
            {
                "id": 12,
                "title": "The Great Barrier Reef: Exploring the Largest Coral Ecosystem and Bleaching Events",
                "tier": "Tier 3: Environmental Pressures & Bleaching",
                "angle": "case_study",
                "slug": "great_barrier_reef_largest_coral_ecosystem_bleaching_events",
                "question": "What happens when back-to-back mass bleaching events strike 2,900 individual reefs along 1,400 miles of Australian coast?",
                "focus": "The northern, central, and southern sectors, aerial bleaching survey methodologies, cyclone damage vs thermal bleaching, crown-of-thorns culls, and the remarkable resilience of fast-growing Acropora corals.",
                "reason": "Comprehensive status report on the world's most famous and massive marine World Heritage site."
            },
            {
                "id": 13,
                "title": "Crown-of-Thorns Starfish Outbreaks: Runoff Algae Blooms Fueling Venomous Destroyers",
                "tier": "Tier 3: Environmental Pressures & Bleaching",
                "angle": "challenges_obstacles",
                "slug": "crown_of_thorns_starfish_outbreaks_runoff_venomous_destroyers",
                "question": "How can an invasion of 20-armed, venomous Acanthaster starfish strip an entire healthy coral reef down to bare white rock in months?",
                "focus": "Agricultural fertilizer runoff feeding larval starfish, loss of the giant triton snail predator, stomach eversion directly onto corals digesting live tissue, and diver bile salt injection culling programs.",
                "reason": "Examines one of the most destructive natural biological plagues threatening Indo-Pacific coral reefs."
            },
            {
                "id": 14,
                "title": "Ocean Acidification and Dissolving Foundations: How Lower pH Inhibits Calcification",
                "tier": "Tier 3: Environmental Pressures & Bleaching",
                "angle": "investigative",
                "slug": "ocean_acidification_dissolving_foundations_lower_ph_calcification",
                "question": "What happens when seawater saturation states of aragonite fall below critical thresholds, causing living coral skeletons to dissolve faster than they grow?",
                "focus": "Chemical equilibrium equations of CO2 absorption, lowering ocean pH from 8.2 to 8.1 (a 30% increase in hydrogen ion acidity), skeletal porosity weakness, and natural volcanic CO2 seeps acting as time machines to 2100.",
                "reason": "Rigorous geochemical analysis of the structural degradation facing coral reef foundations."
            },
            {
                "id": 15,
                "title": "Mesophotic Twilight Reefs: Coral Communities Surviving 150 to 500 Feet Below Storms",
                "tier": "Tier 3: Environmental Pressures & Bleaching",
                "angle": "deep_frontiers",
                "slug": "mesophotic_twilight_reefs_coral_communities_150_to_500_feet",
                "question": "Can deep twilight reefs that escape surface heatwaves and storm waves act as lifeboats to re-seed dying shallow-water corals?",
                "focus": "Mesophotic Coral Ecosystems (MCEs) at 100-500 feet depth, ultra-efficient light-capturing flat plate coral morphologies, technical rebreather diving exploration, and evaluating the 'Deep Reef Refugia' hypothesis.",
                "reason": "Frontier exploration into the mysterious, sheltered deep coral realms hidden from surface turmoil."
            },
            {
                "id": 16,
                "title": "The Super Coral Revolution: Identifying Heat-Tolerant Clades and Assisted Evolution",
                "tier": "Tier 4: Restoration Frontiers & Future Hope",
                "angle": "biotechnology",
                "slug": "super_coral_revolution_heat_tolerant_clades_assisted_evolution",
                "question": "How are marine geneticists in Hawaii and Australia breeding resilient 'super corals' that survive water temperatures 2°C hotter than normal?",
                "focus": "Durusdinium trenchii heat-tolerant clade D symbionts, selective breeding trials, epigenetic heat hardening, microbial probiotic inoculation (beneficial bacteria for corals), and assisted gene flow.",
                "reason": "Cutting-edge biotechnology investigation into helping corals evolve at 10x natural speeds to survive climate warming."
            },
            {
                "id": 17,
                "title": "Micro-Fragmentation and Coral Nurseries: Accelerating 100 Years of Growth into 2 Years",
                "tier": "Tier 4: Restoration Frontiers & Future Hope",
                "angle": "innovations",
                "slug": "micro_fragmentation_coral_nurseries_accelerating_growth",
                "question": "How did Dr. David Vaughan accidentally discover that cutting brain coral into 1-centimeter micro-tiles triggers hyper-accelerated growth?",
                "focus": "Micro-fragmentation diamond saw slicing, colonial self-healing response multiplying growth rates by 40x, fusing micro-fragments back together into mature boulder corals, and underwater tree nurseries.",
                "reason": "The most widely adopted and revolutionary active coral restoration breakthrough in the world."
            },
            {
                "id": 18,
                "title": "Larval Seeding and Coral Cryopreservation: Freezing Gametes in Liquid Nitrogen Biobanks",
                "tier": "Tier 4: Restoration Frontiers & Future Hope",
                "angle": "future_trends",
                "slug": "larval_seeding_coral_cryopreservation_liquid_nitrogen_biobanks",
                "question": "Can cryogenic coral sperm banks preserved at -196°C safeguard the genetic diversity of the world's reefs for centuries?",
                "focus": "The Taronga Conservation Society and Smithsonian cryo-biobanks, catching spawn slicks in floating mega-tents, rear-and-release larval settlement onto degraded reefs, and maintaining genetic variety.",
                "reason": "High-tech future vision preserving biodiversity against worst-case environmental scenarios."
            },
            {
                "id": 19,
                "title": "Artificial Reefs and Shipwrecks: Submerged Substrates, 3D Tiles, and Bio-Rock Electrolysis",
                "tier": "Tier 4: Restoration Frontiers & Future Hope",
                "angle": "engineering_marvels",
                "slug": "artificial_reefs_shipwrecks_substrates_3d_tiles_biorock",
                "question": "How do scuttled military warships, 3D-printed terracotta tiles, and low-voltage electrified steel cages turn into thriving coral ecosystems?",
                "focus": "The Biorock accretion process (mineral electrolysis precipitating limestone coating), ship sinking protocols (stripping fuel and asbestos), recruitment substrate textures, and fish aggregation.",
                "reason": "Fascinating intersection of marine civil engineering, art, and artificial habitat creation."
            },
            {
                "id": 20,
                "title": "The Global Coral Reef Financial Value: Coastal Storm Protection, Tourism, and Fisheries",
                "tier": "Tier 4: Restoration Frontiers & Future Hope",
                "angle": "economic_ecological_capstone",
                "slug": "global_coral_reef_financial_value_storm_protection_tourism",
                "question": "Why is the global economic value of coral reefs estimated at $2.7 trillion annually in flood defense, pharmaceutical drugs, and tourism?",
                "focus": "Dissipating 97% of ocean wave energy before striking coastlines, reef insurance policies paying out immediately after hurricanes for diver repair teams, artisanal fisheries food security, and our moral obligation to preserve them.",
                "reason": "Comprehensive socioeconomic and ethical capstone uniting environmental stewardship with global human survival."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Fourth Global Coral Bleaching Event: Unprecedented Sea Temperatures Across 50 Nations",
                "trend_score": 97,
                "angle": "urgent_crisis",
                "slug": "fourth_global_coral_bleaching_event_unprecedented_temperatures",
                "why_trending": "Urgent breaking global news as NOAA officially declared the fourth planet-wide coral bleaching event affecting Atlantic, Pacific, and Indian reefs.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Coral Spawning Underwater Documentaries: Millions of Pink Pearls Exploding in Synchrony",
                "trend_score": 95,
                "angle": "viral_nature",
                "slug": "coral_spawning_underwater_documentaries_pink_pearls_exploding",
                "why_trending": "Massive viral engagement every autumn on YouTube and Instagram following divers filming the underwater 'upside-down pink snowstorm'.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Bio-Rock and Electric Reefs: Low-Voltage Current Spurring Calcification at Triple Speed",
                "trend_score": 93,
                "angle": "tech_innovation",
                "slug": "biorock_electric_reefs_low_voltage_current_spurring_calcification",
                "why_trending": "High tech interest in Wolf Hilbertz's electrified steel dome structures accelerating coral survival in Indonesia and Maldives.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Sunscreen Bans in Hawaii and Palau: Oxybenzone and Octinoxate Bleaching Toxicity",
                "trend_score": 94,
                "angle": "controversial_policy",
                "slug": "sunscreen_bans_hawaii_palau_oxybenzone_octinoxate_toxicity",
                "why_trending": "Popular consumer debate over mineral non-nano zinc oxide sunscreens vs chemical sunscreens that deform coral larvae.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Chasing Coral: The Netflix Documentary Behind-the-Scenes Time-Lapse Engineering",
                "trend_score": 91,
                "angle": "media_impact",
                "slug": "chasing_coral_netflix_behind_the_scenes_timelapse_engineering",
                "why_trending": "Ongoing high viewership and educational impact following camera crews inventing custom underwater wipe-down housings to capture bleaching.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "3D-Printed Terracotta Coral Tiles: Restoring Hong Kong and Caribbean Habitats",
                "trend_score": 92,
                "angle": "design_engineering",
                "slug": "3d_printed_terracotta_coral_tiles_restoring_habitats",
                "why_trending": "Architectural and design buzz around clay 3D-printed biomimetic tiles providing micro-grooves for coral larvae settlement.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "The Red Sea Coral Mystery: Why Gulf of Aqaba Corals Refuse to Bleach in Boiled Waters",
                "trend_score": 96,
                "angle": "scientific_breakthrough",
                "slug": "red_sea_coral_mystery_gulf_of_aqaba_heat_tolerance",
                "why_trending": "Fascinating evolutionary discovery: northern Red Sea corals migrated through an ancient southern thermal gate, making them pre-adapted to survive 6°C above average.",
                "status": "Queued"
            }
        ]
    },
    "200_botany": {
        "id": "200",
        "slug": "botany",
        "title": "Botany",
        "category": "Life_Biology",
        "audience": "Botanists, Plant Scientists, Horticulturalists, Ethnobotanists, Nature Documentary Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Plant Anatomy & Photosynthetic Machinery: Chloroplasts, Xylem/Phloem Hydraulics & Stomata Regulation (Beginner / Scratch)",
             "Plant structural biology, endosymbiotic cyanobacterial chloroplast origins, xylem cohesion-tension transpirational pull, stomatal guard cell osmolarity, and major plant divisions."),
            ("Tier 2: Plant Communication & Chemical Warfare: Volatile Organic Compounds (VOCs), Mycorrhizal Networks & Allelopathy (Intermediate)",
             "Airborne volatile warning signals, mycorrhizal Wood Wide Web fungal resource sharing, allelopathic chemical soil poisoning, auxin phototropic bending, and rapid thigmonastic leaf snaps."),
            ("Tier 3: Extreme Botanical Adaptations: Carnivorous Pitchers, Epiphytes, Succulent CAM Crassulacean Metabolism & Desert Seeds (Upper Intermediate)",
             "Carnivorous insect digestive enzymes, CAM nighttime acid storage in desert succulents, thermogenic carrion corpse flowers, soilless canopy epiphytes, and pyriscent wildfire-opening seeds."),
            ("Tier 4: Ethnobotany, Plant Domestication & Future Biotechnology: Agricultural Revolutions, CRISPR Crops & Synthetic Photosynthesis (Advanced / Masterclass)",
             "The Green Revolution semi-dwarf genetics, indigenous ethnopharmacology (aspirin, taxol, quinine), CRISPR C4 rice engineering, Svalbard seed vault conservation, and plant neurobiology debates.")
        ],
        "flagship": {
            "title": "The Solar Engine: How Chloroplasts Transformed Sunlight into All Terrestrial Life",
            "angle": "deep_dive",
            "slug": "200_botany_deep_dive_the_solar_engine"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Solar Engine: How Chloroplasts Transformed Sunlight into All Terrestrial Life",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "solar_engine_how_chloroplasts_transformed_sunlight_terrestrial_life",
                "question": "How does a green leaf convert photons from 93 million miles away into glucose sugars that power every animal on Earth?",
                "focus": "Thylakoid membranes, chlorophyll a and b photon absorption, the water-splitting photolysis reaction generating oxygen, and the Calvin-Benson cycle fixing carbon via RuBisCO enzymes.",
                "reason": "The defining foundational masterclass deconstructing the most essential chemical process on planet Earth."
            },
            {
                "id": 2,
                "title": "Endosymbiotic Theory: How a Primitive Cell Engulfed a Cyanobacterium to Create Plants",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "evolutionary_milestone",
                "slug": "endosymbiotic_theory_primitive_cell_cyanobacterium_create_plants",
                "question": "How did Lynn Margulis prove that every green plant leaf contains the captured descendants of free-living ancient cyanobacteria?",
                "focus": "Primary endosymbiosis 1.5 billion years ago, double membranes around chloroplasts, circular bacterial DNA and 70S ribosomes inside plant plastids, and the dawn of the Archaeplastida lineage.",
                "reason": "Foundational evolutionary milestone establishing the origin of the entire plant kingdom."
            },
            {
                "id": 3,
                "title": "The Vascular Highway: Xylem Cohesion-Tension Transporting Water 300 Feet Up Redwoods",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "vascular_highway_xylem_cohesion_tension_water_redwoods",
                "question": "How do 350-foot coast redwoods pull thousands of gallons of water from soil up to canopy needles without a mechanical pump?",
                "focus": "Cohesion-Tension theory, hydrogen bonding between water molecules creating unbroken tensile columns, negative pressure (tension) generated by leaf transpiration, and phloem sugar translocation.",
                "reason": "Technical breakdown of the extraordinary hydraulic engineering enabling plants to grow tall."
            },
            {
                "id": 4,
                "title": "Stomata and Guard Cells: Osmotic Pores Balancing CO2 Ingestion with Water Evaporation",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "scientific_phenomenon",
                "slug": "stomata_and_guard_cells_osmotic_pores_balancing_co2_water",
                "question": "How do microscopic microscopic dumbbell-shaped cells open and close millions of leaf valves in response to sunlight and drought?",
                "focus": "Potassium ion (K+) pumping driving osmotic water swelling of guard cells, microfibril radial cellulose rings causing outward bending, abscisic acid (ABA) drought signaling, and transpiration tradeoffs.",
                "reason": "Fascinating look at the microscopic gatekeepers controlling global gas and water exchange."
            },
            {
                "id": 5,
                "title": "The Five Plant Groups: Bryophytes, Pteridophytes, Gymnosperms, and Angiosperms",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "five_plant_groups_bryophytes_pteridophytes_gymnosperms_angiosperms",
                "question": "How did plants evolve from non-vascular creeping mosses into naked-seed conifers and spectacular flowering fruit trees?",
                "focus": "Bryophytes (mosses without vascular tissue), Pteridophytes (ferns with spores), Gymnosperms (naked-seed pines and cycads), and Angiosperms (flowering plants with encased ovaries), alternation of generations.",
                "reason": "Establishes the fundamental taxonomic evolutionary framework organizing all botanical science."
            },
            {
                "id": 2,
                "title": "Plant Communication and VOC Alarms: Chewed Leaves Signaling Neighbors",
                "tier": "Tier 2: Communication & Chemical Ecology",
                "angle": "sensory_science",
                "slug": "plant_communication_voc_alarms_chewed_leaves_signaling",
                "question": "When a caterpillar chews on a tobacco leaf, how does the plant warn downwind neighbors to produce bitter nicotine toxins before they are attacked?",
                "focus": "Volatile Organic Compounds (VOCs), methyl jasmonate signaling through air currents, recruiting parasitoid wasps to attack chewing herbivores, and systemic acquired resistance (SAR).",
                "reason": "Groundbreaking look at the dynamic, chemical communication networks operating continuously in forests."
            },
            {
                "id": 7,
                "title": "The Wood Wide Web: Mycorrhizal Fungal Networks Trading Phosphorus for Plant Sugars",
                "tier": "Tier 2: Communication & Chemical Ecology",
                "angle": "biological_guide",
                "slug": "wood_wide_web_mycorrhizal_fungal_networks_trading_sugars",
                "question": "How do underground fungal hyphae connect hundreds of individual trees into an interconnected resource-sharing subterranean network?",
                "focus": "Ectomycorrhizal vs arbuscular mycorrhizal fungi, trading soil mineral nutrients (phosphorus, nitrogen) for 20% of the tree's photosynthetic carbon, nutrient routing, and mother tree theories.",
                "reason": "Explores the world-renowned ecological concept of underground plant-fungal cooperation."
            },
            {
                "id": 8,
                "title": "Allelopathy and Chemical Warfare: Black Walnuts and Eucalyptus Poisoning Soil",
                "tier": "Tier 2: Communication & Chemical Ecology",
                "angle": "chemical_ecology",
                "slug": "allelopathy_chemical_warfare_black_walnuts_eucalyptus_soil",
                "question": "Why does almost nothing grow beneath a black walnut tree, and how do eucalyptus trees use flammable volatile oils to torch competitors?",
                "focus": "Juglone hydroquinone exudation inhibiting seed germination and enzyme respiration in neighboring plants, terpenes in eucalyptus needles promoting intense wildfires to which the trees are fire-adapted.",
                "reason": "Deconstructs the ruthless chemical competition and botanical sabotage occurring quietly in wild soils."
            },
            {
                "id": 9,
                "title": "Auxins and Phototropism: How Hormonal Elongation Makes Stems Bend Toward Sunlight",
                "tier": "Tier 2: Communication & Chemical Ecology",
                "angle": "hands_on_tutorial",
                "slug": "auxins_and_phototropism_hormonal_elongation_bending_sunlight",
                "question": "Why do houseplants on windowsills always curve their stems directly toward the glass, and what hormone drives the bend?",
                "focus": "Indole-3-acetic acid (IAA auxin), phototropin photoreceptors detecting blue light, lateral auxin redistribution to the shaded side of the stem, cellular acid-growth elongation, and gravitropism in roots.",
                "reason": "Clear, practical demonstration of plant developmental physiology and hormonal regulation."
            },
            {
                "id": 10,
                "title": "Thigmonasty: Rapid Action Potentials Snapping Venus Flytraps and Mimosa Shut",
                "tier": "Tier 2: Communication & Chemical Ecology",
                "angle": "extreme_scenarios",
                "slug": "thigmonasty_rapid_action_potentials_snapping_flytraps_mimosa",
                "question": "How can a plant with no nerves or muscles trigger electric action potentials and snap a leaf shut in 100 milliseconds?",
                "focus": "Venus flytrap mechanosensory trigger hairs requiring two mechanical touches within 20 seconds, calcium ion influx, sudden loss of turgor pressure in pulvinus cells, and Mimosa pudica sensitive leaf folding.",
                "reason": "Thrilling examination of rapid plant movement challenging the boundary between animal and plant kinetics."
            },
            {
                "id": 11,
                "title": "Carnivorous Plants: Pitcher Traps, Sticky Sundews, and Digesting Insects in Bogs",
                "tier": "Tier 3: Extreme Botanical Adaptations",
                "angle": "field_guide",
                "slug": "carnivorous_plants_pitcher_traps_sticky_sundews_digesting",
                "question": "Why did plants in nutrient-poor peat bogs evolve downward-pointing hairs, slippery wax crystals, and digestive acid pools to eat insects?",
                "focus": "Nepenthes and Sarracenia pitfall traps, Drosera mucilaginous tentacle glue, Utricularia underwater vacuum bladder traps snapping in 1 millisecond, and absorbing nitrogen/phosphorus from bug shells.",
                "reason": "Fascinating examination of predatory botany thriving in acidic, nutrient-starved wetlands."
            },
            {
                "id": 12,
                "title": "CAM Photosynthesis: How Cacti and Succulents Open Stomata Exclusively at Night",
                "tier": "Tier 3: Extreme Botanical Adaptations",
                "angle": "technical_breakdown",
                "slug": "cam_photosynthesis_cacti_succulents_open_stomata_at_night",
                "question": "How do desert cacti survive in 115°F scorching heat without losing water, taking in all their CO2 in pitch darkness?",
                "focus": "Crassulacean Acid Metabolism (CAM), nocturnal PEP carboxylase carbon fixation, temporary malic acid storage in central vacuoles, daytime closed stomata with decarboxylation for the Calvin cycle, and water conservation.",
                "reason": "Masterclass in biochemical evolutionary adaptation to extreme arid environments."
            },
            {
                "id": 13,
                "title": "The Corpse Flower (Rafflesia & Titan Arum): Mimicking Rotting Flesh Thermogenically",
                "tier": "Tier 3: Extreme Botanical Adaptations",
                "angle": "natural_marvels",
                "slug": "corpse_flower_rafflesia_titan_arum_mimicking_rotting_flesh",
                "question": "Why do the world's largest individual flower (Rafflesia) and tallest unbranched bloom (Amorphophallus titanum) smell like dead decaying bodies?",
                "focus": "Thermogenesis (heating spadix up to 98°F using cyanide-resistant mitochondrial respiration), vaporizing dimethyl disulfide and trisulfide rotting odors, attracting carrion flies and beetles, and parasitic endophytic lifestyles.",
                "reason": "Spectacular botanical spectacle examining extreme deceptive pollination biology."
            },
            {
                "id": 14,
                "title": "Epiphytic Marvels: Air Plants and Orchids Surviving Without Soil in Tree Tops",
                "tier": "Tier 3: Extreme Botanical Adaptations",
                "angle": "botanical_guide",
                "slug": "epiphytic_marvels_air_plants_orchids_surviving_without_soil",
                "question": "How do tropical orchids and Tillandsia bromeliads thrive high on rainforest tree bark without their roots ever touching the ground?",
                "focus": "Velamen radicum (spongy multi-layered aerial root dead epidermis absorbing water vapor from fog), tank bromeliad reservoir micro-ecosystems, absorbing bird droppings, and commensal non-parasitic lifestyles.",
                "reason": "Celebrates the diverse aerial canopy gardens that blanket tropical rainforests."
            },
            {
                "id": 15,
                "title": "Seed Dormancy and Pyriscence: Pinecones That Require Wildfires to Release Seeds",
                "tier": "Tier 3: Extreme Botanical Adaptations",
                "angle": "environmental_adaptation",
                "slug": "seed_dormancy_pyriscence_pinecones_require_wildfires_release",
                "question": "Why do lodgepole pine and giant sequoia cones glue their scales shut with resin for decades until boiling wildfire heat melts them open?",
                "focus": "Serotiny and pyriscence, post-fire mineral ash beds providing nutrient-rich weed-free seedbeds, karrikin molecules in wildfire smoke chemically waking dormant seeds, and evolutionary fire ecology.",
                "reason": "Deep dive into the counterintuitive fire ecology driving forest regeneration."
            },
            {
                "id": 16,
                "title": "The Green Revolution: Norman Borlaug, Semi-Dwarf Wheat, and Saving a Billion Lives",
                "tier": "Tier 4: Ethnobotany & Future Biotechnology",
                "angle": "historical_moment",
                "slug": "green_revolution_norman_borlaug_semi_dwarf_wheat_billion_lives",
                "question": "How did a plant geneticist breeding short, lodging-resistant wheat stalks in Mexico prevent catastrophic global famines in the 1960s?",
                "focus": "The Rht reduced-height genes, preventing heavy grain heads from falling over in fertilizer rains, photoperiod insensitivity, shuttle breeding between different altitudes, and the Nobel Peace Prize.",
                "reason": "The single most consequential humanitarian agricultural breakthrough in modern history."
            },
            {
                "id": 17,
                "title": "Ethnobotany and Pharmacognosy: How Indigenous Healers Guided Modern Aspirin and Taxol",
                "tier": "Tier 4: Ethnobotany & Future Biotechnology",
                "angle": "cultural_context",
                "slug": "ethnobotany_pharmacognosy_how_indigenous_healers_guided_drugs",
                "question": "Why do over 50% of all modern pharmaceutical drugs trace their active molecular roots back to traditional plant medicines?",
                "focus": "Willow bark salicin yielding aspirin, Pacific yew bark yielding chemotherapy drug Taxol, Cinchona bark quinine treating malaria, ethnobotanical field methodology, and intellectual property ethics.",
                "reason": "Vital synthesis celebrating indigenous botanical wisdom and modern drug discovery."
            },
            {
                "id": 18,
                "title": "CRISPR and C4 Rice: Engineering Supercharged Photosynthesis to Feed the Planet",
                "tier": "Tier 4: Ethnobotany & Future Biotechnology",
                "angle": "biotechnology",
                "slug": "crispr_and_c4_rice_engineering_supercharged_photosynthesis",
                "question": "Can scientists use CRISPR gene editing to rewrite the internal leaf anatomy of rice from inefficient C3 to supercharged C4 photosynthesis?",
                "focus": "Kranz anatomy in maize and sugarcane, eliminating RuBisCO photorespiration oxygen waste, boosting grain yields by 50% with 60% less water, and global genetic collaboration consortia.",
                "reason": "Frontier biotechnology exploration aiming to secure the future food supply of billions."
            },
            {
                "id": 19,
                "title": "The Svalbard Global Seed Vault: Preserving 1 Million Crop Varieties Beneath Permafrost",
                "tier": "Tier 4: Ethnobotany & Future Biotechnology",
                "angle": "behind_the_scenes",
                "slug": "svalbard_global_seed_vault_preserving_1_million_crop_varieties",
                "question": "What is inside the frozen 'Doomsday Vault' carved 400 feet into a Norwegian Arctic mountain guarding humanity's agricultural heirloom seeds?",
                "focus": "Sub-zero permafrost storage at -18°C, three-ply foil moisture barrier envelopes, preserving seed viability for hundreds of years, the first withdrawal by Syria's ICARDA gene bank, and global food security.",
                "reason": "Fascinating look at the ultimate geopolitical and botanical insurance policy protecting human civilization."
            },
            {
                "id": 20,
                "title": "Plant Sentience and Memory: Do Root Apices Think? Debating Plant Neurobiology",
                "tier": "Tier 4: Ethnobotany & Future Biotechnology",
                "angle": "philosophical_debate",
                "slug": "plant_sentience_and_memory_do_root_apices_think_debate",
                "question": "Did Charles Darwin foresee modern plant neurobiology when he proposed that root tips act like the brain of a lower animal?",
                "focus": "The root apex transition zone, electrical action potential propagation along phloem cables, habituation learning in Mimosa pudica, debating plant consciousness vs complex biochemical automation.",
                "reason": "Thought-provoking philosophical and scientific capstone on the frontiers of plant intelligence."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Wood Wide Web Controversy: Do Trees Truly 'Share' or Compete Ruthlessly?",
                "trend_score": 96,
                "angle": "controversial_debate",
                "slug": "wood_wide_web_controversy_do_trees_share_or_compete",
                "why_trending": "Heated debate across scientific literature pushing back against over-romanticized 'mother tree' narratives in favor of fungal market self-interest.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Glowing GMO Houseplants: Firefly Petunias Shining in Living Rooms via Fungal Genes",
                "trend_score": 95,
                "angle": "consumer_biotech",
                "slug": "glowing_gmo_houseplants_firefly_petunias_bioluminescent_genes",
                "why_trending": "Massive viral consumer hit as USDA approves continuous bioluminescent petunias engineered with neon fungal caffeic acid cycle genes.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "The 30,000-Year-Old Flower Resurrected: Russian Scientists Blooming Siberian Seeds",
                "trend_score": 94,
                "angle": "scientific_breakthrough",
                "slug": "30000_year_old_flower_resurrected_siberian_permafrost_seeds",
                "why_trending": "Astounding paleobotanical feat of regenerating Silene stenophylla from fossilized squirrel burrows frozen since the Pleistocene Ice Age.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Titan Arum Bloom Alerts: Why Botanical Gardens Attract Thousands at 2:00 AM",
                "trend_score": 93,
                "angle": "viral_event",
                "slug": "titan_arum_bloom_alerts_why_botanical_gardens_attract_thousands",
                "why_trending": "Perennial livestream and viral in-person sensation as massive Corpse Flowers bloom for only 24 hours smelling like rotting carcasses.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Monster Houseplant Poaching: The Black Market Trade in Rare Variegated Monsteras",
                "trend_score": 92,
                "angle": "investigative",
                "slug": "monster_houseplant_poaching_black_market_variegated_monsteras",
                "why_trending": "Eye-opening investigative look into high-dollar theft of rare aroids from botanical conservatories and wild plant smuggling rings.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Crying Plants: Microphones Recording Ultrasonic Pop Sounds from Dehydrated Stems",
                "trend_score": 95,
                "angle": "viral_science",
                "slug": "crying_plants_microphones_ultrasonic_pops_dehydration",
                "why_trending": "Viral Tel Aviv University study demonstrating stressed tomato and tobacco plants emit 40-80 kHz acoustic cavitation clicks when thirsty.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Restoring the American Chestnut: Blight-Resistant Genetic Engineering Reviving a Giant",
                "trend_score": 91,
                "angle": "conservation_action",
                "slug": "restoring_american_chestnut_darling_58_blight_resistant",
                "why_trending": "High-interest conservation biotechnology story introducing wheat oxalate oxidase genes to bring back the 4 billion lost canopy kings of eastern forests.",
                "status": "Queued"
            }
        ]
    }
}

if __name__ == "__main__":
    print("Generating suites for Batch 196-200...")
    for folder, meta in BATCH_196_200.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 196-200 complete!")
