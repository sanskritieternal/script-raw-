import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_191_195 = {
    "191_fishing": {
        "id": "191",
        "slug": "fishing",
        "title": "Fishing",
        "category": "Land_Outdoor",
        "audience": "Anglers, Fly Fishers, Saltwater Fishermen, Marine Biologists, Conservationists, Outdoor Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Fundamentals of Angling: Tackle Systems, Knot Tying, Reading Water & Catch-and-Release Ethics (Beginner / Scratch)",
             "The foundational mechanics of sport fishing, rod and reel selection, terminal tackle, essential knot strength physics, reading freshwater currents and structure, and catch-and-release mortality prevention."),
            ("Tier 2: Freshwater Mastery: Bass Tournament Tactics, Fly Fishing Entomology & River Drift Presentations (Intermediate)",
             "Freshwater predatory behavior, seasonal bass migrations, matching insect hatches with artificial flies, the double haul fly casting technique, and forward-facing sonar electronics."),
            ("Tier 3: Saltwater & Inshore Frontiers: Surf Casting, Flats Stalking (Bonefish/Tarpon), and Tidal Currents (Upper Intermediate)",
             "Inshore tidal hydrology, sight-fishing the shallow flats for bonefish and permit, surfcasting migrating striped bass through heavy ocean swells, and ice fishing shelter engineering."),
            ("Tier 4: Pelagic Big Game & Conservation Science: Bluefin Tuna, Deep-Drop Swordfishing, and Fishery Management (Advanced / Masterclass)",
             "Extreme pelagic big game angling (marlin, giant bluefin tuna), 1,800-foot daytime swordfish deep-dropping, commercial trawl impacts, marine protected areas, and contemplative angling philosophy.")
        ],
        "flagship": {
            "title": "The Art of Reading Water: How Master Anglers Decode Currents, Structure, and Fish Behavior",
            "angle": "beginner_guide",
            "slug": "191_fishing_beginner_guide_the_art_of_reading_water"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Art of Reading Water: How Master Anglers Decode Currents, Structure, and Fish Behavior",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "art_of_reading_water_how_anglers_decode_currents_structure",
                "question": "How do veteran fishermen look at a river or lake surface and pinpoint exactly where predatory fish are holding?",
                "focus": "Seam lines between fast and slow current, eddy circulation, undercut banks, submerged timber and rock drop-offs, temperature thermoclines, and ambush points.",
                "reason": "The quintessential foundational angling skill that separates lucky casts from consistent success."
            },
            {
                "id": 2,
                "title": "The Five Essential Fishing Knots: Palomar, Improved Clinch, Loop, FG, and Uni-Knot",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "five_essential_fishing_knots_palomar_clinch_loop_fg_uni",
                "question": "Why does a knot fail at 50% of rated line strength, and which knots preserve 95%+ of breaking strain under shock loads?",
                "focus": "Friction knot mechanics, lubricating monofilament to prevent heat friction burns, the slim profile of the FG knot for braid-to-fluoro leaders, and lure action loop knots.",
                "reason": "Essential practical skill guide ensuring anglers never lose trophy fish to preventable knot failures."
            },
            {
                "id": 3,
                "title": "Spinning vs Baitcasting vs Fly Reels: Gear Ratios, Braking Systems, and Line Capacity",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "gear_guide",
                "slug": "spinning_vs_baitcasting_vs_fly_reels_gear_ratios_brakes",
                "question": "What mechanical differences dictate when to choose an open-face spinning reel, a precision baitcaster, or a 1:1 fly reel?",
                "focus": "Centrifugal and magnetic spool braking to prevent backlashes ('birds nests'), drag stack washers (carbon fiber vs felt), line twist physics, and gear ratio retrieval rates.",
                "reason": "Comprehensive tackle architecture overview guiding equipment selection for any fishing environment."
            },
            {
                "id": 4,
                "title": "Monofilament vs Fluorocarbon vs Braided Line: The Physics of Stretch, Abrasion, and Visibility",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "monofilament_vs_fluorocarbon_vs_braided_line_physics",
                "question": "How does line refraction index match water to make fluorocarbon virtually invisible while braid offers zero stretch sensitivity?",
                "focus": "Refraction index comparison (water 1.33 vs fluorocarbon 1.42), nylon monofilament shock absorption stretch, Spectra/Dyneema micro-braid diameter, and abrasion resistance.",
                "reason": "Deep dive into the materials science connecting the angler's hands to the fish's mouth."
            },
            {
                "id": 5,
                "title": "Catch and Release Science: Minimizing Air Exposure, Barbless Hooks, and Mortality Rates",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "conservation_protocol",
                "slug": "catch_and_release_science_air_exposure_barbless_hooks",
                "question": "Why does keeping a fought fish out of water for 60 seconds cause irreversible lactic acidosis and delayed post-release mortality?",
                "focus": "Fish gill lamellae collapse in air, rubberized knotless landing nets, barbless hook advantages, deep hook removal techniques, water temperature stress, and revival protocols.",
                "reason": "Vital ethical and biological guidelines ensuring released sport fish survive to spawn."
            },
            {
                "id": 6,
                "title": "Bass Behavior and Seasonal Movements: Spring Pre-Spawn to Winter Deep Suspensions",
                "tier": "Tier 2: Freshwater Mastery",
                "angle": "behavioral_habits",
                "slug": "bass_behavior_seasonal_movements_prespawn_to_winter",
                "question": "How do water temperature and photoperiod trigger largemouth bass to migrate from 30-foot river channels onto 2-foot spawning beds?",
                "focus": "Pre-spawn staging points, bed guarding aggression, post-spawn summer thermocline patterns, fall baitfish chasing in creek arms, and cold-water lethargic winter jigs.",
                "reason": "Deconstructs the biological rhythms driving the multi-billion-dollar tournament bass fishing sport."
            },
            {
                "id": 7,
                "title": "Matching the Hatch: Aquatic Entomology, Mayfly Nymphs, and Dry Fly Imitations",
                "tier": "Tier 2: Freshwater Mastery",
                "angle": "field_guide",
                "slug": "matching_the_hatch_aquatic_entomology_mayfly_nymphs_dry_fly",
                "question": "How do fly fishermen turn over river stones to identify insect nymphs and match the exact artificial feather patterns trout demand?",
                "focus": "The life cycle of mayflies (Ephemeroptera), caddisflies (Trichoptera), and stoneflies (Plecoptera), nymph vs emerger vs spinner stages, and hackle floating surface tension.",
                "reason": "Examines the sophisticated blend of natural history, entomology, and artistic fly tying."
            },
            {
                "id": 8,
                "title": "The Double Haul Cast: Aerodynamics and Muscle Timing for 80-Foot Presentations",
                "tier": "Tier 2: Freshwater Mastery",
                "angle": "master_skills",
                "slug": "double_haul_cast_aerodynamics_muscle_timing_80_foot",
                "question": "How does pulling the line with your non-casting hand during the forward and back strokes add tremendous line speed to cut through ocean gales?",
                "focus": "Loading the fly rod blank, tight casting loops (narrow arrowheads), haul timing at maximum line acceleration, shooting line, and overcoming wind resistance.",
                "reason": "Masterclass breakdown of the single most powerful technical casting mechanic in fly fishing."
            },
            {
                "id": 9,
                "title": "Crankbaits, Jigs, and Soft Plastics: Action, Deflection, and Triggering Predatory Strikes",
                "tier": "Tier 2: Freshwater Mastery",
                "angle": "tactical_analysis",
                "slug": "crankbaits_jigs_soft_plastics_deflection_predatory_strikes",
                "question": "Why does bumping a plastic lip crankbait off an underwater boulder provoke an instinctual strike from a non-feeding bass?",
                "focus": "Deflection theory, lateral line sensory triggering, Texas rig vs drop shot soft plastic presentations, skirted football jigs in rocky cover, and color selection in stained water.",
                "reason": "Detailed tactical breakdown of artificial lure dynamics and predatory fish psychology."
            },
            {
                "id": 10,
                "title": "Sonar and Forward-Facing Sonar (LiveScope): How Real-Time Electronics Changed Fishing",
                "tier": "Tier 2: Freshwater Mastery",
                "angle": "innovations",
                "slug": "sonar_forward_facing_sonar_livescope_real_time_electronics",
                "question": "How did phased-array transducers allowing anglers to watch fish react to lures on high-definition video screens upend tournament competition?",
                "focus": "Traditional CHIRP sonar vs DownScan/SideScan vs real-time live forward sonar (Garmin Panoptix LiveScope), transducer beam cones, fish spotting, and fair-chase debates.",
                "reason": "Examines the biggest technological disruption in the history of recreational angling."
            },
            {
                "id": 11,
                "title": "Stalking the Saltwater Flats: Ghosting After Bonefish, Permit, and Tarpon",
                "tier": "Tier 3: Saltwater & Inshore Frontiers",
                "angle": "destination_guide",
                "slug": "stalking_saltwater_flats_bonefish_permit_tarpon_skiff",
                "question": "What makes polling a shallow skiff in 12 inches of crystal water to sight-cast to shimmering silver tails the ultimate hunting-fishing hybrid?",
                "focus": "The Florida Keys and Bahamas flats, polarized lens amber tint advantages, lead calculations on moving fish, the notoriously finicky permit crab bite, and 'jumping' 100-pound tarpon.",
                "reason": "Thrilling showcase of the most stealth-intensive, visually demanding discipline in saltwater angling."
            },
            {
                "id": 12,
                "title": "Surfcasting the Graveyard of the Atlantic: Striped Bass Migration and Ocean Waves",
                "tier": "Tier 3: Saltwater & Inshore Frontiers",
                "angle": "extreme_scenarios",
                "slug": "surfcasting_graveyard_atlantic_striped_bass_migration_waves",
                "question": "How do surfcasters dressed in drysuits stand on slick granite boulders in 10-foot crashing waves at 2:00 AM to battle migrating stripers?",
                "focus": "Montauk Point blitzes, reading breaking surf bars and rip sluiceways, wooden needlefish and darter plugs, studded Korker wading boots, and the annual striper coastal migration.",
                "reason": "High-octane look at hardcore surfcasting culture on the edge of the roaring ocean."
            },
            {
                "id": 13,
                "title": "Ice Fishing Engineering: Tip-Ups, Sonar Flashers, Ice Augers, and Thermal Shacks",
                "tier": "Tier 3: Saltwater & Inshore Frontiers",
                "angle": "specialized_study",
                "slug": "ice_fishing_engineering_tip_ups_sonar_flashers_augers",
                "question": "How do sub-zero anglers safely navigate 18 inches of frozen lake ice to locate schools of perch and walleye in total darkness below?",
                "focus": "Clear black ice vs white snow ice load ratings, gas/lithium auger cutting flutes, spring-loaded tip-up spool flags, mechanical flasher circular displays, and insulated hub shacks with propane heaters.",
                "reason": "Fascinating examination of winter angling technology and cold-climate lake hydrology."
            },
            {
                "id": 14,
                "title": "Trolling Dynamics: Downriggers, Planer Boards, and Speed Calculations for Salmon",
                "tier": "Tier 3: Saltwater & Inshore Frontiers",
                "angle": "process_walkthrough",
                "slug": "trolling_dynamics_downriggers_planer_boards_salmon_walleye",
                "question": "How do Great Lakes and ocean charter captains run 12 lines simultaneously behind a boat without tangling while targeting specific depths?",
                "focus": "Lead weights on steel cable downriggers, offshore planer boards spreading spreads 100 feet wide, dipsy divers hydrofoils, GPS speed control down to 0.1 knots, and temperature probe sensors.",
                "reason": "Reveals the complex multi-line geometry and precision physics of commercial and sport trolling."
            },
            {
                "id": 15,
                "title": "The Atlantic Salmon: The King of Fish, Classic Spey Rods, and Conservation",
                "tier": "Tier 3: Saltwater & Inshore Frontiers",
                "angle": "cultural_history",
                "slug": "atlantic_salmon_king_of_fish_spey_rods_conservation",
                "question": "Why does an anadromous fish that never feeds upon returning to its natal freshwater river still strike ornate, hand-tied salmon flies?",
                "focus": "Salmo salar migration from Greenland to Scottish and Norwegian rivers, two-handed Spey casting technique, historic 19th-century Victorian salmon flies, and the battle against open-net salmon farming.",
                "reason": "Rich historical and cultural chronicle of the most aristocratic sport fish in world angling lore."
            },
            {
                "id": 16,
                "title": "Pelagic Big Game: Chasing 1,000-Pound Blue Marlin on Heavy Stand-Up Tackle",
                "tier": "Tier 4: Pelagic Giants & Conservation",
                "angle": "extreme_scenarios",
                "slug": "pelagic_big_game_1000_pound_blue_marlin_heavy_tackle",
                "question": "What happens when a 1,000-pound 'grander' blue marlin strikes a resin trolling lure at 50 MPH and dumps 800 yards of line in 30 seconds?",
                "focus": "Custom offshore sportfishers, teaser spreader bars, bucket fighting harnesses, flying gaffs vs tag-and-release flags, backing down in heavy seas, and crew cockpit coordination.",
                "reason": "The pinnacle of high-stakes, adrenaline-fueled oceanic big-game angling."
            },
            {
                "id": 17,
                "title": "Giant Bluefin Tuna: Commercial Harpooning, Rod-and-Reel Giants, and Quota Battles",
                "tier": "Tier 4: Pelagic Giants & Conservation",
                "angle": "industry_secrets",
                "slug": "giant_bluefin_tuna_commercial_harpooning_rod_and_reel_quotas",
                "question": "How did a fish once considered worthless cat food become worth $100,000 per specimen on Tokyo's Toyosu fish market auction floors?",
                "focus": "Warm-blooded vascular countercurrent heat exchangers (retia mirabilia), 130-pound class bent-butt reels, electric harpoon darts, ICCAT international quotas, and the fight against bluefin extinction.",
                "reason": "Combines commercial fishery economics, marine physiology, and extreme deep-sea battle documentary."
            },
            {
                "id": 18,
                "title": "Deep-Drop Daytime Swordfishing: Electric Reels, Sinkers, and 1,800-Foot Depths",
                "tier": "Tier 4: Pelagic Giants & Conservation",
                "angle": "engineering_marvels",
                "slug": "deep_drop_daytime_swordfishing_sinkers_1800_foot_depths",
                "question": "How did Florida Keys fishermen discover that broadbill swordfish feed near the pitch-black ocean floor during bright daylight hours?",
                "focus": "10-pound sacrificial sash weights, hydraulic/electric Kristal reels, strobe light attractors, reading bottom contour canyons on bathymetric maps, and detecting delicate 2-inch tip bites at 300 fathoms.",
                "reason": "Deconstructs one of the most innovative and technologically challenging offshore techniques pioneered in the 21st century."
            },
            {
                "id": 19,
                "title": "The Tragedy of Overfishing: Cod Fisheries Collapse, Trawler Destruction, and Sanctuaries",
                "tier": "Tier 4: Pelagic Giants & Conservation",
                "angle": "investigative",
                "slug": "tragedy_of_overfishing_grand_banks_cod_collapse_trawlers",
                "question": "How did industrial factory bottom trawlers wipe out Newfoundland's seemingly infinite 500-year-old Grand Banks cod population in three decades?",
                "focus": "The 1992 Canadian cod moratorium, sea floor habitat devastation from weighted roller nets, bycatch mortality, Marine Protected Areas (MPAs), and consumer sustainable seafood certification (MSC).",
                "reason": "Sobering, vital ecological investigation into the limits of global marine harvesting."
            },
            {
                "id": 20,
                "title": "Izaak Walton and The Compleat Angler: The 400-Year Philosophy of Contemplative Angling",
                "tier": "Tier 4: Pelagic Giants & Conservation",
                "angle": "historical_evolution",
                "slug": "izaak_walton_the_compleat_angler_400_year_philosophy",
                "question": "Why has a 1653 English book about pastoral fishing remained one of the most reprinted works in English literary history?",
                "focus": "Izaak Walton's 'The Contemplative Man's Recreation', fishing as meditation and communion with nature, escaping political strife during the English Civil War, and the enduring soul of the sport.",
                "reason": "Philosophical masterclass capstone connecting the modern angler to 400 years of contemplative outdoor tradition."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Forward-Facing Sonar (LiveScope) Bans: Is Live Video Screen Fishing Cheating?",
                "trend_score": 96,
                "angle": "controversial_debate",
                "slug": "forward_facing_sonar_livescope_bans_cheating_debate",
                "why_trending": "Massive ongoing controversy across professional bass and crappie tournaments with purists claiming video game fishing ruins angling skill.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Urban Fishing: Catching 30-Pound Monster Carp in Downtown Storm Canals",
                "trend_score": 93,
                "angle": "subculture_trend",
                "slug": "urban_fishing_catching_monster_carp_downtown_canals",
                "why_trending": "Huge viral trend on TikTok and YouTube with street anglers pulling giant fish out of storm drains, city parks, and industrial drainage ditches.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Magnet Fishing: Pulling Safes, Grenades, and Historic Relics from Urban Rivers",
                "trend_score": 95,
                "angle": "viral_phenomenon",
                "slug": "magnet_fishing_pulling_safes_grenades_relics_rivers",
                "why_trending": "Explosive YouTube view counts following hobbyists throwing neodymium magnet rigs from bridges and discovering weapons and stolen safes.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Monster Catfish of the Amazon: Piraíba and Goliath Catfish River Battles",
                "trend_score": 92,
                "angle": "thrill_seeker",
                "slug": "monster_catfish_amazon_piraiba_goliath_battles",
                "why_trending": "Perennial high-reverence monster fish documentaries following deep Amazonian expeditions targeting 300-pound river giants.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Micro-Fishing: The Japanese Tanago Tradition of Catching 1-Inch Fish with Micro-Hooks",
                "trend_score": 90,
                "angle": "cultural_curiosity",
                "slug": "micro_fishing_japanese_tanago_tradition_micro_hooks",
                "why_trending": "Growing minimalist niche celebrating micro-tackle, bamboo rods, and catching tiny, jewel-colored bitterling species.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Kayak Fishing Offshore: Battling Sharks and Sailfish from 12-Foot Plastic Hulls",
                "trend_score": 94,
                "angle": "extreme_scenarios",
                "slug": "kayak_fishing_offshore_battling_sharks_sailfish_pedal_drive",
                "why_trending": "Heart-pounding POV action footage of pedal-drive kayak anglers being towed miles out to sea by monster pelagic gamefish.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Ghost Nets and Ocean Plastics: How Anglers Are Cleaning Up Abandoned Gear",
                "trend_score": 91,
                "angle": "conservation_action",
                "slug": "ghost_nets_ocean_plastics_anglers_cleaning_abandoned_gear",
                "why_trending": "High-engagement grassroots conservation trend highlighting recreational divers and fishermen retrieving abandoned commercial trawler nets.",
                "status": "Queued"
            }
        ]
    },
    "192_beekeeping": {
        "id": "192",
        "slug": "beekeeping",
        "title": "Beekeeping",
        "category": "Land_Outdoor",
        "audience": "Backyard Apiarists, Commercial Beekeepers, Pollination Biologists, Honey Producers, Sustainability Advocates (Global)",
        "progression": [
            ("Tier 1: Hive Fundamentals & Honeybee Biology: Castes (Queen, Worker, Drone), Anatomy & The Langstroth Hive (Beginner / Scratch)",
             "Colony superorganism biology, bee castes and divisions of labor, L.L. Langstroth's 3/8-inch 'bee space' discovery, protective gear, and hexagonal wax physics."),
            ("Tier 2: Colony Management & Hive Inspection: Smoker Protocol, Brood Patterns, Swarm Prevention & Splits (Intermediate)",
             "Safe hive inspections, decoding brood frames, the waggle dance navigational language, catching and preventing swarms, colony splits, and centrifugal honey harvesting."),
            ("Tier 3: Apiary Health & Pest Warfare: Varroa Mite Diagnostics, Integrated Pest Management (IPM) & Foulbrood (Upper Intermediate)",
             "The Varroa destructor parasite threat, organic oxalic/formic acid treatments, American Foulbrood containment, winter cluster thermal dynamics, and harvesting propolis."),
            ("Tier 4: Commercial Apiculture & Global Ecosystem Impact: Migratory Almond Pollination, Queen Breeding & Honey Fraud (Advanced / Masterclass)",
             "Industrial migratory beekeeping logistics, queen rearing grafting protocols, combating ultra-filtered syrup honey adulteration, Africanized bees, and solitary bee conservation.")
        ],
        "flagship": {
            "title": "The Secret Architecture of the Hive: How 50,000 Bees Act as a Single Superorganism",
            "angle": "deep_dive",
            "slug": "192_beekeeping_deep_dive_secret_architecture_of_the_hive"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Secret Architecture of the Hive: How 50,000 Bees Act as a Single Superorganism",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "secret_architecture_of_hive_50000_bees_single_superorganism",
                "question": "How does a colony of 50,000 individual honeybees make decentralized democratic decisions without a central command?",
                "focus": "Superorganism concept, pheromonal communication (queen mandibular pheromone), collective thermoregulation (fanning and clustering), and physiological division of labor.",
                "reason": "The defining foundational masterclass explaining the astonishing social complexity of the honeybee colony."
            },
            {
                "id": 2,
                "title": "The Langstroth Revolution: How L.L. Langstroth Discovered 'Bee Space' and Rewrote Apiculture",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "langstroth_revolution_bee_space_rewrote_apiculture",
                "question": "Why did beekeepers have to slaughter entire hives with sulfur smoke to harvest honey before 1851?",
                "focus": "Lorenzo Langstroth discovering the precise 3/8-inch (6 to 9mm) gap that bees neither glue shut with propolis nor fill with comb, movable frame design, and modern hive boxes.",
                "reason": "The single most consequential technological invention in modern apicultural history."
            },
            {
                "id": 3,
                "title": "The Three Castes: Queen, Worker, and Drone Roles, Lifespans, and Anatomical Specializations",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "three_castes_queen_worker_drone_roles_anatomy_lifespans",
                "question": "How does an identical fertilized egg develop into a 5-year-old egg-laying Queen rather than a 6-week sterile Worker?",
                "focus": "Royal jelly diet epigenetic triggers, queen spermatheca storage, worker temporal polyethism (nurse, guard, undertaker, forager), and the tragic, single-purpose mating fate of drones.",
                "reason": "Foundational entomological breakdown of hive caste genetics and developmental biology."
            },
            {
                "id": 4,
                "title": "First Apiary Equipment: The Smoker, Hive Tool, Veil, and Leather Gloves",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "first_apiary_equipment_smoker_hive_tool_veil_gloves",
                "question": "Why does cool pine needle smoke instantly pacify an agitated hive of stinging insects?",
                "focus": "Smoke masking alarm pheromones (isopentyl acetate) and triggering instinctive honey-gorging instincts, J-hook hive tools for prying propolis frames, bee suits, and gentle movements.",
                "reason": "Essential practical guide for aspiring beekeepers to approach their first colony safely and confidently."
            },
            {
                "id": 5,
                "title": "The Hexagonal Wax Comb: Mathematical Efficiency, Comb Building, and Honey Storage",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "hexagonal_wax_comb_mathematical_efficiency_physics",
                "question": "Why is the hexagon the only geometric shape that can tile a plane with maximum volume and minimum wax perimeter?",
                "focus": "The honeycomb conjecture mathematically proven, abdominal wax glands secreting wax scales, chewing wax with mandibular enzymes, 8 pounds of honey consumed to produce 1 pound of wax.",
                "reason": "Deep dive into the incredible geometry, structural mechanics, and biochemistry of natural beeswax."
            },
            {
                "id": 6,
                "title": "The Hive Inspection: Smoker Technique, Frame Pulling, and Reading Brood Patterns",
                "tier": "Tier 2: Colony Management & Hive Inspection",
                "angle": "process_walkthrough",
                "slug": "hive_inspection_smoker_technique_frame_pulling_brood_patterns",
                "question": "What is a beekeeper looking for when gently levering out the central frames of a brood chamber on a sunny afternoon?",
                "focus": "Spotting the queen or verifying standing 3-day rice-grain eggs, solid vs shotgun brood patterns (cappings), pearly white C-shaped larvae, nectar halos, and royal queen cups.",
                "reason": "Step-by-step masterclass in conducting a healthy, systematic apiary diagnostic inspection."
            },
            {
                "id": 7,
                "title": "The Waggle Dance: How Foragers Communicate Distance and Sun Angle Coordinates",
                "tier": "Tier 2: Colony Management & Hive Inspection",
                "angle": "scientific_phenomenon",
                "slug": "waggle_dance_foragers_communicate_distance_sun_angle",
                "question": "How did Karl von Frisch prove that bees translate polar sun vectors and flight distance into rhythmic body wiggles in pitch darkness?",
                "focus": "The Nobel Prize-winning discovery, dance angle relative to vertical gravity equaling angle to sun, duration of waggle run correlating to distance, floral odor sample distribution, and solar drift adjustment.",
                "reason": "One of the most astonishing symbolic communication systems discovered in the animal kingdom."
            },
            {
                "id": 8,
                "title": "Swarm Season: Recognizing Queen Cells, Prime Swarms, and Capturing Swarms in Trees",
                "tier": "Tier 2: Colony Management & Hive Inspection",
                "angle": "field_guide",
                "slug": "swarm_season_queen_cells_prime_swarms_capturing_in_trees",
                "question": "Why does half a prosperous colony suddenly take flight with the old queen, leaving a docile 15,000-bee cluster hanging on a tree branch?",
                "focus": "Reproductive colony fission, supersedure vs swarm cells, scout bees evaluating new cavities via quorum sensing, shaking swarms into nuc boxes, and swarm trap bait lures (lemongrass oil).",
                "reason": "Thrilling, practical guide to understanding and catching one of nature's greatest biological spectacles."
            },
            {
                "id": 9,
                "title": "Making Colony Splits: Creating New Hives, Introducing Queens, and Pheromone Acceptance",
                "tier": "Tier 2: Colony Management & Hive Inspection",
                "angle": "hands_on_tutorial",
                "slug": "making_colony_splits_creating_new_hives_introducing_queens",
                "question": "How do apiarists double their colony counts and prevent spring swarms by mathematically dividing frames of brood and bees?",
                "focus": "Walk-away splits vs mated queen splits, ensuring nurse bees and resource balance, candy-plug queen cages allowing slow pheromone introduction over 3 days, and avoiding queen rejection.",
                "reason": "Crucial apiary expansion and colony management skill set for intermediate beekeepers."
            },
            {
                "id": 10,
                "title": "Honey Harvesting: Uncapping Wax Cappings, Centrifugal Extractors, and Moisture Content",
                "tier": "Tier 2: Colony Management & Hive Inspection",
                "angle": "production_workflow",
                "slug": "honey_harvesting_uncapping_extractors_moisture_refractometry",
                "question": "How do you extract golden liquid honey from wax combs without destroying the reusable foundation, and why must moisture stay below 18.6%?",
                "focus": "Heated uncapping knives, radial and tangential centrifugal spinners, fine mesh straining (raw vs processed), optical honey refractometers preventing fermentation, and bottling hygiene.",
                "reason": "Fascinating production walkthrough detailing the sweet harvest reward of apiculture."
            },
            {
                "id": 11,
                "title": "Varroa Destructor: The Parasitic Mite Decimating Colonies and Vectoring Viruses",
                "tier": "Tier 3: Apiary Health & Pest Warfare",
                "angle": "challenges_obstacles",
                "slug": "varroa_destructor_parasitic_mite_decimating_colonies_viruses",
                "question": "Why did a tiny pinhead-sized Asian mite that crossed into European honeybees in the 1980s become the leading killer of managed hives worldwide?",
                "focus": "Feeding on bee fat bodies (not hemolymph as previously thought), vectoring Deformed Wing Virus (DWV) and Israeli Acute Paralysis Virus, reproduction inside capped drone brood, and exponential autumn mite spikes.",
                "reason": "Investigates the single greatest biological enemy facing global beekeeping today."
            },
            {
                "id": 12,
                "title": "Integrated Pest Management (IPM): Oxalic Acid Vaporization, Formic Acid, and Screened Floors",
                "tier": "Tier 3: Apiary Health & Pest Warfare",
                "angle": "technical_breakdown",
                "slug": "integrated_pest_management_ipm_oxalic_acid_formic_screened_floors",
                "question": "How do modern beekeepers eradicate mites without contaminating pure honey supers with toxic synthetic pesticides?",
                "focus": "Alcohol wash mite threshold counting (over 3 mites per 100 bees triggers treatment), oxalic acid sublimation vaporizers in winter, formic acid penetrating capped cells in summer, and hygienic grooming genetics.",
                "reason": "In-depth guide to modern, sustainable, chemical-smart apiary defense protocols."
            },
            {
                "id": 13,
                "title": "American Foulbrood (AFB): Spore Longevity, the Ropiness Test, and Burning Infected Hives",
                "tier": "Tier 3: Apiary Health & Pest Warfare",
                "angle": "investigative",
                "slug": "american_foulbrood_afb_spore_longevity_ropiness_test_burning",
                "question": "Why does a single outbreak of Paenibacillus larvae bacteria legally mandate state inspectors to incinerate entire wooden hives in open bonfires?",
                "focus": "Bacterial endospores surviving for 70+ years in wood and honey, the matchstick ropiness test of sunken brown brood, foul fishy odor, antibiotic resistance risks, and irradiation quarantine.",
                "reason": "Dramatic, serious look at the most dreaded bacterial disease in beekeeping regulatory history."
            },
            {
                "id": 14,
                "title": "Winterizing the Apiary: Candy Boards, Upper Ventilation, and Clustered Thermoregulation",
                "tier": "Tier 3: Apiary Health & Pest Warfare",
                "angle": "seasonal_guide",
                "slug": "winterizing_apiary_candy_boards_ventilation_clustering",
                "question": "How do bees survive sub-zero blizzards without heating the interior of the box, and why is moisture—not cold—their greatest winter killer?",
                "focus": "Tight cluster physics (outer insulating shell of bees around queen and brood), shivering flight muscles producing 95°F core heat, upper hive ventilation to vent damp respiration condensation, and emergency sugar fondant.",
                "reason": "Vital winter survival guide ensuring colonies emerge healthy and strong in spring."
            },
            {
                "id": 15,
                "title": "Propolis, Royal Jelly, and Bee Venom: Harvesting Apiary Byproducts for Apitherapy",
                "tier": "Tier 3: Apiary Health & Pest Warfare",
                "angle": "specialized_study",
                "slug": "propolis_royal_jelly_bee_venom_harvesting_apitherapy",
                "question": "What antimicrobial tree resins do bees transform into 'bee glue' that coats every millimeter of the hive interior to sterilize their home?",
                "focus": "Harvesting propolis grids for tinctures, collecting royal jelly from queen cells within 72 hours, electric shock venom collection grids, and scientific evaluation of apitherapy claims.",
                "reason": "Explores the diverse secondary biochemical treasures produced by the hive beyond honey."
            },
            {
                "id": 16,
                "title": "The California Almond Pollination: Migratory Beekeeping Moving Millions of Hives by Semi-Truck",
                "tier": "Tier 4: Commercial Apiculture & Ecology",
                "angle": "industry_secrets",
                "slug": "california_almond_pollination_migratory_beekeeping_semi_trucks",
                "question": "Why do over 2 million beehives—more than 80% of all managed colonies in the United States—migrate to California's Central Valley every February?",
                "focus": "The largest pollination event on Earth, flatbed semi-truck interstate transport, $200+ per hive rental economics, pesticide exposure risks, and the immense logistical stress on commercial beekeepers.",
                "reason": "Eye-opening look into the colossal industrial agricultural engine keeping the global food supply running."
            },
            {
                "id": 17,
                "title": "Queen Rearing Mastery: The Doolittle Grafting Method, Mating Nucs, and Insemination",
                "tier": "Tier 4: Commercial Apiculture & Ecology",
                "angle": "master_skills",
                "slug": "queen_rearing_doolittle_grafting_mating_nucs_insemination",
                "question": "How do master queen breeders transfer 1-day-old microscopic larvae with a tiny steel needle to rear thousands of genetically superior queens?",
                "focus": "G.M. Doolittle's 1888 cell builder system, queenless cell builder hives, Drone Congregation Areas (DCAs) where virgin queens mate at 50 feet in the air, and microscopic instrumental insemination.",
                "reason": "Masterclass in advanced apicultural genetics and queen production."
            },
            {
                "id": 18,
                "title": "Fake Honey and Adulteration: Rice Syrup Dilution, NMR Testing, and Market Fraud",
                "tier": "Tier 4: Commercial Apiculture & Ecology",
                "angle": "investigative",
                "slug": "fake_honey_adulteration_rice_syrup_nmr_testing_fraud",
                "question": "Why is pure honey the third most adulterated food product on the planet, and how do illicit brokers disguise cheap industrial syrups as wildflower honey?",
                "focus": "Ultra-filtration to strip floral pollen signatures, high-fructose corn syrup and C4/C3 plant sugar blending, Nuclear Magnetic Resonance (NMR) spectral testing, and the collapse of honest domestic honey prices.",
                "reason": "High-urgency investigative report uncovering global food fraud and consumer deception."
            },
            {
                "id": 19,
                "title": "Africanized Honeybees ('Killer Bees'): Genetics, Defense Radii, and Managing Aggression",
                "tier": "Tier 4: Commercial Apiculture & Ecology",
                "angle": "case_study",
                "slug": "africanized_honeybees_killer_bees_genetics_defense_radii",
                "question": "How did 26 Tanzanian queen bees accidentally escaping a Brazilian breeding laboratory in 1957 permanently transform the genetics of the Americas?",
                "focus": "Warwick Kerr's hybridization experiment, hyper-defensive alarm pheromone responses (attacking 10x faster and pursuing victims for 1,000 yards), rapid swarming traits, and requeening strategies.",
                "reason": "Gripping, factual deconstruction of the most notorious insect hybridization event in modern history."
            },
            {
                "id": 20,
                "title": "Saving Native Solitary Bees vs Honeybees: Biodiversity, Mason Bees, and Competition",
                "tier": "Tier 4: Commercial Apiculture & Ecology",
                "angle": "ethical_dilemma",
                "slug": "saving_native_solitary_bees_vs_honeybees_competition",
                "question": "Does placing European honeybee hives in urban parks actually harm endangered native solitary pollinators like mason and sweat bees?",
                "focus": "European honeybees as domestic livestock vs 4,000 native North American bee species, floral resource competition, viral spillover from commercial hives, and building native bee hotel habitats.",
                "reason": "Essential ecological capstone examining the nuanced conservation distinction between agricultural livestock and wild pollinator preservation."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Flow Hive Technology: Does Tapping Honey Directly from the Hive Harm Bees?",
                "trend_score": 94,
                "angle": "tech_review",
                "slug": "flow_hive_technology_tapping_honey_directly_pros_cons",
                "why_trending": "Massive viral crowdfunded invention sparking ongoing passionate debates between traditionalist beekeepers and backyard hobbyists.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Urban Rooftop Beekeeping: Hives on Skyscrapers from Paris to New York City",
                "trend_score": 92,
                "angle": "urban_trend",
                "slug": "urban_rooftop_beekeeping_hives_on_skyscrapers_paris_nyc",
                "why_trending": "Growing metropolitan trend showing thriving rooftop apiaries atop luxury hotels producing hyper-local city honey.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Comb Honey Production: The High-End Market for Raw, Unprocessed Honeycomb Slices",
                "trend_score": 91,
                "angle": "artisanal_food",
                "slug": "comb_honey_production_raw_unprocessed_honeycomb_slices",
                "why_trending": "Huge sensory food trend on TikTok and Instagram featuring ASMR honeycomb cutting and high retail margins for square comb sections.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "AI Smart Hives: Acoustic Sensors Detecting Swarms and Mites via Frequency Analysis",
                "trend_score": 95,
                "angle": "innovations",
                "slug": "ai_smart_hives_acoustic_sensors_detecting_swarms_mites",
                "why_trending": "Cutting-edge IoT technology bringing cellular monitoring and machine learning audio analysis to commercial apiaries.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Horned Invaders: The Northern Giant Hornet (Murder Hornet) Eradication Operations",
                "trend_score": 96,
                "angle": "invasive_species",
                "slug": "northern_giant_hornet_murder_hornet_eradication_operations",
                "why_trending": "High-tension documentary coverage of state entomologists tracking radio-tagged giant hornets through Pacific Northwest forests.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "The 48-Hour Swarm Capture: Free Bees Falling from Neighborhood Lamp Posts",
                "trend_score": 93,
                "angle": "viral_craft",
                "slug": "48_hour_swarm_capture_free_bees_neighborhood_calls",
                "why_trending": "Viral social media videos showing fearless beekeepers gently scooping 20,000 docile bees into cardboard boxes with bare hands.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Colony Collapse Disorder (CCD) Ten Years Later: What Actually Caused the Disappearances?",
                "trend_score": 90,
                "angle": "investigative",
                "slug": "colony_collapse_disorder_ccd_ten_years_later_causes",
                "why_trending": "Scientific retrospective analyzing the multi-factor convergence of neonicotinoids, Varroa mites, poor nutrition, and monocultures.",
                "status": "Queued"
            }
        ]
    },
    "193_insects": {
        "id": "193",
        "slug": "insects",
        "title": "Insects",
        "category": "Life_Biology",
        "audience": "Entomologists, Naturalists, Biology Students, Macro Photographers, Science Documentary Viewers (Global)",
        "progression": [
            ("Tier 1: Entomology Foundations: Arthropod Anatomy (Head, Thorax, Abdomen), Exoskeletons & Metamorphosis (Beginner / Scratch)",
             "Insect structural biology, tripartite body division, chitinous exoskeleton mechanics, complete (holometabolous) vs incomplete metamorphosis, and the major taxonomic orders."),
            ("Tier 2: Extreme Adaptations & Defenses: Chemical Warfare, Mimicry, Bioluminescence & Super-Strength (Intermediate)",
             "Specialized evolutionary adaptations: bombardier beetle boiling chemical bursts, Batesian/Müllerian defensive mimicry, luciferin bioluminescence, and parasitoid wasp lifecycles."),
            ("Tier 3: Eusocial Superorganisms: Ants, Termites, Army Ant Raids & Fungus Farming Civilizations (Upper Intermediate)",
             "Eusocial colonial architecture: leafcutter ant agricultural monocultures, nomadic army ant bivouac swarms, passive termite cooling mounds, and periodic cicada prime number emergences."),
            ("Tier 4: Evolutionary Entomology & The Global Insect Crisis: Fossil Record, Pollination Collapse & Edible Insects (Advanced / Masterclass)",
             "Prehistoric Carboniferous giant dragonflies, the global windshield phenomenon and insect decline, gene-drive vector control, and industrial insect protein farming.")
        ],
        "flagship": {
            "title": "The Master Architects: How Ants and Termites Built Complex Civilizations Millions of Years Before Humans",
            "angle": "deep_dive",
            "slug": "193_insects_deep_dive_the_master_architects"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Master Architects: How Ants and Termites Built Complex Civilizations Millions of Years Before Humans",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "master_architects_how_ants_termites_built_civilizations",
                "question": "How did eusocial insects invent agriculture, climate-controlled skyscrapers, and waste management 50 million years before humanity appeared?",
                "focus": "Macrotermes termite mound engineering, leafcutter fungal gardens, cast-based labor systems, pheromonal communication, and collective superorganism intelligence.",
                "reason": "The ultimate flagship opener showcasing the astonishing scale and societal complexity of the insect world."
            },
            {
                "id": 2,
                "title": "Complete vs Incomplete Metamorphosis: The Cellular Melting Inside the Chrysalis",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "complete_vs_incomplete_metamorphosis_cellular_melting",
                "question": "What happens inside a butterfly pupa when the caterpillar literally dissolves into biological soup before assembling wings and antennae?",
                "focus": "Imaginal discs, histolysis enzymes digesting larval tissues, holometabolous (beetles, butterflies) vs hemimetabolous (grasshoppers, roaches) lifecycles, and evolutionary advantages.",
                "reason": "Explores the most miraculous and biologically bizarre developmental transformation in nature."
            },
            {
                "id": 3,
                "title": "The Exoskeleton Engine: Chitin Chemistry, Resilin Springs, and Hydraulic Leg Extension",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "exoskeleton_engine_chitin_resilin_springs_hydraulics",
                "question": "How can a flea jump 200 times its body length and a rhinoceros beetle lift 850 times its weight without collapsing?",
                "focus": "Chitin polymer chains cross-linked with sclerotin proteins, the rubber-like protein resilin storing 97% elastic energy, hydraulic hemolymph pressure, and scaling square-cube law limits.",
                "reason": "Fascinating biomechanical breakdown of the lightweight armored structures that make insects super-strong."
            },
            {
                "id": 4,
                "title": "Compound Eyes and Polarized Light: How Insects Perceive Ultraviolet Flowers and Angles",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "scientific_phenomenon",
                "slug": "compound_eyes_polarized_light_insects_perceive_ultraviolet",
                "question": "How do thousands of hexagonal ommatidia assemble a 360-degree panorama capable of detecting flickering motion at 300 frames per second?",
                "focus": "Ommatidia lens physics, ultraviolet bullseye nectar guides on flowers invisible to humans, detecting E-vector skylight polarization for overcast navigation, and night-vision adaptations.",
                "reason": "Reveals the alien visual sensory world through which insects navigate and hunt."
            },
            {
                "id": 5,
                "title": "The Big Four Insect Orders: Coleoptera, Diptera, Hymenoptera, and Lepidoptera",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "big_four_insect_orders_coleoptera_diptera_hymenoptera_lepidoptera",
                "question": "Why did British biologist J.B.S. Haldane famously remark that the Creator has an 'inordinate fondness for beetles'?",
                "focus": "Coleoptera (400,000 species of hardened elytron beetles), Diptera (two-winged true flies with halteres), Hymenoptera (wasps, bees, ants), and Lepidoptera (scaled-wing butterflies/moths).",
                "reason": "Establishes the indispensable taxonomic framework covering 80% of all named insect species."
            },
            {
                "id": 6,
                "title": "Chemical Weaponry: Bombardier Beetles Spraying Boiling Hydroquinone at 212°F",
                "tier": "Tier 2: Extreme Adaptations & Defenses",
                "angle": "extreme_scenarios",
                "slug": "chemical_weaponry_bombardier_beetles_spraying_boiling_hydroquinone",
                "question": "How does a half-inch beetle mix two lethal chemicals inside an internal combustion chamber and fire a boiling toxic spray without blowing itself up?",
                "focus": "Hydroquinone and hydrogen peroxide dual-chamber storage, catalase and peroxidase enzyme catalyst mixing, steam flash evaporation pressure, and 360-degree aiming nozzles.",
                "reason": "Masterclass in natural chemical engineering and one of biology's most astonishing defensive mechanisms."
            },
            {
                "id": 7,
                "title": "Batesian and Müllerian Mimicry: Toxic Monarchs, Harmless Viceroys, and Visual Deception",
                "tier": "Tier 2: Extreme Adaptations & Defenses",
                "angle": "evolutionary_science",
                "slug": "batesian_mullerian_mimicry_monarchs_viceroys_deception",
                "question": "How do completely harmless hoverflies and caterpillars deceive deadly predators into thinking they are venomous wasps and pit vipers?",
                "focus": "Aposematic warning coloration, Henry Walter Bates' palatable copycats, Fritz Müller's mutual toxic honesty rings, snake-mimic hawkmoth caterpillars, and predator learning curves.",
                "reason": "Deep dive into the optical illusion and deceptive evolutionary arms races among insects."
            },
            {
                "id": 8,
                "title": "Bioluminescent Wonders: Fireflies, Luciferin Chemistry, and Synchronized Forests",
                "tier": "Tier 2: Extreme Adaptations & Defenses",
                "angle": "natural_marvels",
                "slug": "bioluminescent_wonders_fireflies_luciferin_synchronized_forests",
                "question": "How do thousands of fireflies in the Great Smoky Mountains and Southeast Asian mangroves synchronize their glowing pulses to the exact millisecond?",
                "focus": "Luciferin-luciferase enzymatic cold light reaction (nearly 100% efficient with zero heat loss), nitric oxide nerve triggering, optical flashing courtship dialects, and predatory Photuris mimicry.",
                "reason": "Spellbinding aesthetic exploration of natural cold light and biological synchronization."
            },
            {
                "id": 9,
                "title": "Parasitoid Wasps: Zombie Cockroach Jewels, Polydnaviruses, and Alien-Like Cycles",
                "tier": "Tier 2: Extreme Adaptations & Defenses",
                "angle": "biological_guide",
                "slug": "parasitoid_wasps_zombie_cockroaches_polydnaviruses_alien_cycles",
                "question": "Why did Charles Darwin write that the cruel lifecycles of Ichneumonid wasps made him doubt an omnibenevolent creator?",
                "focus": "The emerald jewel wasp injecting venom into cockroach subesophageal ganglions to remove free will, symbiotic polydnaviruses disabling host immune systems, and eating hosts alive from the inside out.",
                "reason": "Chilling, riveting examination of the real-life biological horror that inspired modern sci-fi monsters."
            },
            {
                "id": 10,
                "title": "Macro Photography in Entomology: Extreme Focus Stacking, Diffusers, and Insect Worlds",
                "tier": "Tier 2: Extreme Adaptations & Defenses",
                "angle": "creative_skills",
                "slug": "macro_photography_entomology_focus_stacking_diffusers",
                "question": "How do wildlife photographers capture microscopic compound eye facets and velvet wing scales at 5x magnification with razor-sharp depth of field?",
                "focus": "Extreme macro lenses (Laowa 25mm 2.5-5x), automated motorized focus stacking rails combining 100 slices, custom strobe flash diffusion cones, and ethical live field shooting.",
                "reason": "Engaging hands-on technical masterclass connecting science with breathtaking visual art."
            },
            {
                "id": 11,
                "title": "Leafcutter Ants: The Subterranean Agronomists Cultivating Fungal Monocultures",
                "tier": "Tier 3: Eusocial Superorganisms",
                "angle": "case_study",
                "slug": "leafcutter_ants_subterranean_agronomists_fungal_monocultures",
                "question": "How do millions of Atta ants cut tons of fresh rainforest foliage not to eat, but to compost specialized subterranean mushroom gardens?",
                "focus": "Leucoagaricus gongylophorus fungus symbiosis, caste divisions (minims, medias, majors), antibiotic-producing Streptomyces bacteria carried on ant chests to weed parasitic mold, and waste disposal chambers.",
                "reason": "Fascinating examination of non-human agriculture that has flourished uninterrupted for 50 million years."
            },
            {
                "id": 12,
                "title": "Army Ants on the March: Nomadic Bivouacs, Living Flesh Bridges, and Swarm Raids",
                "tier": "Tier 3: Eusocial Superorganisms",
                "angle": "behavioral_habits",
                "slug": "army_ants_on_the_march_nomadic_bivouacs_flesh_bridges",
                "question": "How does a blind swarm of 700,000 Eciton burchellii army ants build living bridges and temporary nests out of their own interlocking bodies?",
                "focus": "Bivouac structures formed by tarsal claws, 20-meter fan-shaped raid fronts flushing out scorpions and snakes, nomadic vs statary cycles linked to queen egg laying, and ant-following bird ecology.",
                "reason": "Spectacular exploration of one of the planet's most formidable predatory natural forces."
            },
            {
                "id": 13,
                "title": "Termite Mounds: Passive Thermoregulation, Chimney Convection, and Biomimicry",
                "tier": "Tier 3: Eusocial Superorganisms",
                "angle": "engineering_marvels",
                "slug": "termite_mounds_passive_thermoregulation_biomimetic_architecture",
                "question": "How do African termites keep their underground fungal core at an exact 87°F year-round while outside desert temperatures swing from 30°F to 110°F?",
                "focus": "Thermal chimney flue convection currents, tidal wind-driven ventilation pores, soil and saliva concrete engineering, and Mike Pearce's Eastgate Centre in Zimbabwe copying termite airflow.",
                "reason": "Masterclass in vernacular natural engineering inspiring modern carbon-neutral human skyscrapers."
            },
            {
                "id": 14,
                "title": "The Locust Plague: How Solitary Grasshoppers Transform into Voracious Billions via Serotonin",
                "tier": "Tier 3: Eusocial Superorganisms",
                "angle": "disaster_ecology",
                "slug": "locust_plague_how_solitary_grasshoppers_transform_serotonin",
                "question": "What chemical trigger turns shy, solitary, green desert grasshoppers into dark, aggressive, swarm-forming locust plagues devouring whole nations?",
                "focus": "Hind leg mechanosensory stimulation in crowded drought oases, sudden serotonin spikes triggering gregarization, wing and brain restructuring, rolling swarm dynamics, and satellite radar tracking.",
                "reason": "Crucial intersection of behavioral neurochemistry, catastrophic agricultural disaster, and climate patterns."
            },
            {
                "id": 15,
                "title": "The Cicada Broods: 13-Year and 17-Year Prime Number Emergence Math and Predator Satiation",
                "tier": "Tier 3: Eusocial Superorganisms",
                "angle": "mathematical_biology",
                "slug": "cicada_broods_13_17_year_prime_number_emergence_math",
                "question": "Why did periodical Magicicada species evolve to emerge from underground root-feeding exclusively in 13-year and 17-year prime number cycles?",
                "focus": "Prime number evolutionary mathematics preventing predator population synchrony, 'predator satiation' strategy (billions emerge so all predators gorge and leave 99% untouched), tymbal acoustic organs.",
                "reason": "Brilliant synthesis of evolutionary game theory, number theory mathematics, and entomological drama."
            },
            {
                "id": 16,
                "title": "Carboniferous Giants: Meganeura Dragonflies and Why 35% Oxygen Allowed Monster Insects",
                "tier": "Tier 4: Evolutionary Frontiers & Crises",
                "angle": "prehistoric_deep_dive",
                "slug": "carboniferous_giants_meganeura_dragonflies_35_percent_oxygen",
                "question": "Why did dragonflies with 2.5-foot wingspans and 8-foot millipedes (Arthropleura) rule the ancient Earth 300 million years ago?",
                "focus": "The Carboniferous coal swamp atmospheric pulse (35% O2 vs 21% today), passive spiracle and tracheal tube oxygen diffusion limits, giant predatory griffinflies, and the Permian collapse.",
                "reason": "Fascinating paleobiological journey explaining why modern insects are physically constrained to small sizes."
            },
            {
                "id": 17,
                "title": "The Insect Apocalypse: German Nature Reserve Studies, Windshield Phenom, and Habitat Fragmentation",
                "tier": "Tier 4: Evolutionary Frontiers & Crises",
                "angle": "investigative",
                "slug": "insect_apocalypse_german_reserve_studies_windshield_phenom",
                "question": "Why have flying insect biomass numbers plunged by over 75% in European nature reserves over the last three decades?",
                "focus": "The 2017 Krefeld Entomological Society malaise trap study, the 'windshield phenomenon' (cars no longer covered in bug splatters), neonics, light pollution destroying nocturnal mating, and food web collapse.",
                "reason": "Vital, hard-hitting investigative report on the silent collapse underpinning all terrestrial life."
            },
            {
                "id": 18,
                "title": "Vector Entomology: Mosquitoes, Malaria, Dengue, and Genetic Gene-Drive Eradication",
                "tier": "Tier 4: Evolutionary Frontiers & Crises",
                "angle": "biotechnology",
                "slug": "vector_entomology_mosquitoes_malaria_crispr_gene_drives",
                "question": "Can CRISPR-Cas9 gene drives intentionally drive Anopheles and Aedes mosquitoes into extinction to wipe out human malaria and dengue fever?",
                "focus": "Mosquito mouthpart micro-needles (fascicle insertion and anticoagulant saliva), Plasmodium parasite transmission cycles, self-propagating CRISPR gene drives, sterility release, and ecological safety debates.",
                "reason": "Examines the cutting-edge biotechnology frontier where insect genetics directly decides human survival."
            },
            {
                "id": 19,
                "title": "Ento-Agriculture: Black Soldier Fly Larvae, Mealworms, and the Future of Sustainable Protein",
                "tier": "Tier 4: Evolutionary Frontiers & Crises",
                "angle": "future_trends",
                "slug": "ento_agriculture_black_soldier_fly_larvae_sustainable_protein",
                "question": "How are automated insect mega-factories turning food waste into high-protein animal feed and human nutrition with 90% less water than cattle?",
                "focus": "Hermetia illucens bioconversion efficiency, converting brewery mash and food waste into frass fertilizer and lipid-rich larvae, vertical insect farming automation, and Western cultural hurdles.",
                "reason": "Visionary look at how insects are poised to solve global agricultural resource depletion."
            },
            {
                "id": 20,
                "title": "Coevolution with Angiosperms: How Insects Shaped Every Flower, Fruit, and Forest on Earth",
                "tier": "Tier 4: Evolutionary Frontiers & Crises",
                "angle": "evolutionary_milestone",
                "slug": "coevolution_with_angiosperms_insects_shaped_every_flower",
                "question": "How did a 100-million-year-old romantic dance between flowering plants and beetles, bees, and moths paint the green planet with color?",
                "focus": "Darwin's 'Abominable Mystery' of sudden angiosperm radiation, pollinator syndrome flower shapes, mutualistic specialized adaptations (fig wasps, long-tongued hawk moths), and the bedrock of terrestrial life.",
                "reason": "Masterclass capstone uniting botany, evolutionary biology, and the irreplaceable majesty of insects."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Cordyceps and 'Zombie Ants': The Mind-Controlling Fungi Inspiring 'The Last of Us'",
                "trend_score": 97,
                "angle": "viral_biology",
                "slug": "cordyceps_zombie_ants_mind_controlling_fungi_last_of_us",
                "why_trending": "Massive global pop culture and scientific obsession with Ophiocordyceps unilateralis forcing ants to clamp onto leaves before fungal stalks sprout from their heads.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "The Velvet Ant: Why the 'Cow Killer' Wasp Has One of the Most Agonizing Stings on Earth",
                "trend_score": 95,
                "angle": "thrill_seeker",
                "slug": "velvet_ant_cow_killer_wasp_agonizing_schmidt_sting_index",
                "why_trending": "Huge virality driven by wildlife creators testing Justin Schmidt's Sting Pain Index on wingless velvet mutillid wasps.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Giant Japanese Hornet Raids: 30 Hornets Decimating a 30,000-Bee Colony in Hours",
                "trend_score": 96,
                "angle": "animal_battles",
                "slug": "giant_japanese_hornet_raids_slaughtering_30000_bees",
                "why_trending": "Perennial multi-million view YouTube documentary format highlighting the brutal slaughter phase and native bees' 'hot bee ball' thermal defense.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Orchid Mantis Camouflage: The Evolutionary Marvel That Looks More Like a Flower Than a Flower",
                "trend_score": 93,
                "angle": "visual_spectacle",
                "slug": "orchid_mantis_camouflage_evolutionary_marvel_predatory_flower",
                "why_trending": "High-retention visual spectacle showcasing predatory mantises using petal-like walking legs to lure pollinating prey directly into raptorial claws.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Genetically Modified Mosquitoes: Oxitec Releasing Millions of Sterile Males in Florida",
                "trend_score": 94,
                "angle": "controversial_debate",
                "slug": "genetically_modified_mosquitoes_oxitec_florida_keys_debate",
                "why_trending": "Intense public debate and news coverage surrounding local government approvals of bio-engineered sterile mosquito field releases.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Dung Beetles Navigating by the Milky Way: Celestial Navigation in Miniature",
                "trend_score": 91,
                "angle": "scientific_phenomenon",
                "slug": "dung_beetles_navigating_by_milky_way_celestial_orientation",
                "why_trending": "Fascinating viral science story explaining how nocturnal African dung beetles wear miniature caps to prove they roll balls in straight lines using starlight.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Raising Mealworms at Home: The Backyard Micro-Livestock Trend for Zero-Waste Protein",
                "trend_score": 89,
                "angle": "sustainability_trend",
                "slug": "raising_mealworms_at_home_backyard_micro_livestock_trend",
                "why_trending": "Emerging homesteading and chicken-keeper subculture farming Tenebrio molitor beetles in plastic drawers using kitchen scraps.",
                "status": "Queued"
            }
        ]
    },
    "194_arachnids": {
        "id": "194",
        "slug": "arachnids",
        "title": "Arachnids",
        "category": "Life_Biology",
        "audience": "Arachnologists, Herpetologists, Pet Tarantula Keepers, Venom Researchers, Nature Documentary Fans (Global)",
        "progression": [
            ("Tier 1: Arachnid Anatomy & Evolutionary Roots: Chelicerae, Pedipalps, Book Lungs & Silk Glands (Beginner / Scratch)",
             "Arachnid anatomy distinct from insects (8 legs, chelicerae fangs, lack of antennae, cephalothorax), Silurian evolutionary origins, book lung respiration, and silk spinnerets."),
            ("Tier 2: Web Architecture & Sensory Mechanics: Orb Webs, Slit Sensilla Vibrations & Hydraulic Jumping Spiders (Intermediate)",
             "Tensile web engineering geometry, microscopic slit sensilla acoustic vibration sensing, the 360-degree telescopic eyes of jumping spiders, and sacrificial matriphagy."),
            ("Tier 3: Venom Biochemistry & Extreme Predators: Scorpions, Funnel-Webs, Brown Recluses & Sun Spiders (Upper Intermediate)",
             "Venom biochemistry: Sydney Funnel-Web neurotoxins, Brazilian Wandering Spider priapism, Brown Recluse necrosis, UV-fluorescent scorpions, and non-venomous camel spiders."),
            ("Tier 4: Diversity Beyond Spiders & Future Biotech: Whip Scorpions, Harvestmen, Ticks, and Spider Silk Bio-Manufacturing (Advanced / Masterclass)",
             "Obscure arachnid orders (Amblypygi, Opiliones, Acari/ticks), electro-receptive aerodynamic ballooning, synthetic spider silk bio-factories, and arachnophobia desensitization.")
        ],
        "flagship": {
            "title": "The Architectural Masterpiece: How Spiders Engineer Orb Webs with Micron Precision",
            "angle": "deep_dive",
            "slug": "194_arachnids_deep_dive_the_architectural_masterpiece"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Architectural Masterpiece: How Spiders Engineer Orb Webs with Micron Precision",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "architectural_masterpiece_how_spiders_engineer_orb_webs",
                "question": "How does a nearly blind garden spider construct a geometric web spanning six feet across a wind-blown gap in complete darkness?",
                "focus": "Bridging silk line drifting on breeze currents, radial hub spokes, non-sticky scaffolding spiral, sticky capture spiral laced with microscopic glue droplets, and vibration monitoring.",
                "reason": "The quintessential arachnid masterclass deconstructing one of the greatest structural feats in biology."
            },
            {
                "id": 2,
                "title": "Spiders vs Insects: Eight Legs, Chelicerae Fangs, Cephalothorax, and Silurian Roots",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "spiders_vs_insects_eight_legs_chelicerae_silurian_roots",
                "question": "What anatomical and evolutionary breakthroughs fundamentally distinguish arachnids from their six-legged insect cousins?",
                "focus": "Cephalothorax (prosoma) and abdomen (opisthosoma), lack of antennae and wings, chelicerae fangs with internal venom ducts, pedipalp sensory manipulation, and 430-million-year Silurian fossils.",
                "reason": "Establishes the foundational biological baseline separating Class Arachnida from Insecta."
            },
            {
                "id": 3,
                "title": "The Chemistry of Spider Silk: Seven Distinct Glands Producing Materials Stronger Than Steel",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "materials_science",
                "slug": "chemistry_of_spider_silk_seven_glands_stronger_than_steel",
                "question": "How can a spider convert liquid protein stored inside its abdomen into a solid fiber with higher tensile strength than Kevlar in milliseconds?",
                "focus": "Major ampullate silk (dragline), flagelliform silk (elastic capture spiral), spidroin protein folding, shear-induced phase crystallization in spinneret ducts, and thermal stability from -40°C to 200°C.",
                "reason": "Deep dive into the premier natural polymer that has captivated materials scientists for decades."
            },
            {
                "id": 4,
                "title": "Hydraulic Locomotion: How Spiders Jump and Move Without Extensor Muscles",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biomechanics",
                "slug": "hydraulic_locomotion_how_spiders_jump_without_extensor_muscles",
                "question": "Why do spider legs instantly curl up inward when they die, and how do they sprint using internal blood pressure spikes?",
                "focus": "Flexor muscles vs lack of extensor muscles in leg joints, prosoma hydraulic fluid pumping, sudden hemolymph pressure spikes extending legs, and biomechanical jumping physics.",
                "reason": "Fascinating biomechanical examination of spider hydraulic motion systems."
            },
            {
                "id": 5,
                "title": "Book Lungs and Open Circulatory Systems: How Arachnids Breathe and Circulate Hemolymph",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "book_lungs_open_circulatory_systems_how_arachnids_breathe",
                "question": "How do stacks of paper-thin blood leaves inside abdominal slits allow massive tarantulas to oxygenate copper-based blue blood?",
                "focus": "Book lung lamellae architecture, hemocyanin copper respiratory pigments turning blue when oxygenated, dorsal tubular heart pumping into open sinuses, and low-metabolic rate survival.",
                "reason": "Reveals the unique internal organ physiology sustaining arachnids across extreme environments."
            },
            {
                "id": 6,
                "title": "Jumping Spiders (Salticidae): Telescopic Vision, Courtship Dances, and 3D Perception",
                "tier": "Tier 2: Web Architecture & Sensory Mechanics",
                "angle": "behavioral_habits",
                "slug": "jumping_spiders_telescopic_vision_courtship_3d_perception",
                "question": "How do fuzzy, centimeter-sized jumping spiders plan complex multi-step stalk routes and calculate leaps with camera-like visual depth?",
                "focus": "Principal anterior median eyes acting as telephoto tubes with movable retinas, image defocus depth perception, vibrant courtship displays (Peacock spiders), and high cognitive problem solving.",
                "reason": "Celebrates the charismatic, intelligent, and visually dazzling pinnacle of the spider family."
            },
            {
                "id": 7,
                "title": "Trapdoor Spiders: Silk Hinges, Subterranean Burrow Acoustics, and Ambush Strikes",
                "tier": "Tier 2: Web Architecture & Sensory Mechanics",
                "angle": "specialized_study",
                "slug": "trapdoor_spiders_silk_hinges_burrow_acoustics_ambush_strikes",
                "question": "How does a spider construct a camouflaged beveled soil door with a silk hinge that seals shut seamlessly against floodwaters and predators?",
                "focus": "Excavating burrows with cheliceral rastellum rakes, soil and silk composite door plugs, radial tripwire silk lines transmitting ground vibrations, and 0.03-second strike speeds.",
                "reason": "Fascinating examination of subterranean ambush architecture and tactile vibration sensing."
            },
            {
                "id": 8,
                "title": "The Golden Silk Orb Weaver (Nephila): Tensile Strength, Carotenoids, and Giant Canopies",
                "tier": "Tier 2: Web Architecture & Sensory Mechanics",
                "angle": "field_guide",
                "slug": "golden_silk_orb_weaver_tensile_strength_carotenoids_giant_webs",
                "question": "Why do giant tropical golden orb weavers spin golden-yellow webs strong enough to ensnare small birds and bats?",
                "focus": "Xanthophyll carotenoid pigments giving silk its golden sheen (attracting bees while remaining invisible to predatory wasps), extreme sexual dimorphism (tiny males), and multi-meter community webs.",
                "reason": "Showcase of the most visually spectacular web-weavers on Earth."
            },
            {
                "id": 9,
                "title": "Slit Sensilla and Trichobothria: How Spiders Hear Sound and Air Currents Through Leg Hairs",
                "tier": "Tier 2: Web Architecture & Sensory Mechanics",
                "angle": "scientific_phenomenon",
                "slug": "slit_sensilla_trichobothria_how_spiders_hear_air_currents",
                "question": "How can a web-bound spider detect the wingbeat frequency of a passing mosquito without ears or eardrums?",
                "focus": "Trichobothria (microscopic hairs hinged in nerve-lined sockets detecting air particle displacement down to nanometers), lyriform slit organs measuring cuticle strain, and listening through webs.",
                "reason": "Reveals the unbelievable acoustic and vibrational sensory apparatus of web-building arachnids."
            },
            {
                "id": 10,
                "title": "Maternal Devotion and Matriphagy: Mother Spiders Sacrificing Their Bodies as Food",
                "tier": "Tier 2: Web Architecture & Sensory Mechanics",
                "angle": "human_interest",
                "slug": "maternal_devotion_matriphagy_mother_spiders_sacrificing_bodies",
                "question": "Why do velvet and Stegodyphus spider mothers feed their babies regurgitated liquid before intentionally letting their hundreds of offspring devour them alive?",
                "focus": "Wolf spiders carrying hundreds of spiderlings on their backs, egg sac guarding without feeding for months, matriphagic autolysis (self-digesting internal organs to nourish spiderlings), and evolutionary survival.",
                "reason": "Deeply shocking yet poignant look at the ultimate evolutionary sacrifice in animal parenting."
            },
            {
                "id": 11,
                "title": "The Sydney Funnel-Web Spider: Delta-Atracotoxin, Primates, and Antivenom",
                "tier": "Tier 3: Venom Biochemistry & Extreme Predators",
                "angle": "extreme_scenarios",
                "slug": "sydney_funnel_web_delta_atracotoxin_primates_antivenom",
                "question": "Why is the venom of an Australian suburban spider harmless to most mammals yet catastrophically lethal to human beings within two hours?",
                "focus": "Delta-atracotoxin neurotoxin opening sodium channels to cause massive autonomic nervous storm, male wandering mating aggression, canine/feline resistance, and the 1981 antivenom breakthrough that eliminated deaths.",
                "reason": "The quintessential venom biology documentary examining the deadliest spider on Earth."
            },
            {
                "id": 12,
                "title": "Scorpions: Fluorescent UV Exoskeletons, Venom Stings, and Desert Survival",
                "tier": "Tier 3: Venom Biochemistry & Extreme Predators",
                "angle": "biological_guide",
                "slug": "scorpions_fluorescent_uv_exoskeletons_venom_stings_survival",
                "question": "Why do scorpions glow a brilliant neon cyan under ultraviolet blacklight, and how do they survive months without food in scorching deserts?",
                "focus": "Beta-carboline molecules in the hyaline cuticle layer emitting green-blue fluorescence, pedipalp pinchers vs venomous telson metasoma balance (rule of thumb: big claws = weak venom), and low metabolic rate.",
                "reason": "Comprehensive overview of the ancient, heavily armored desert survivors of the arachnid lineage."
            },
            {
                "id": 13,
                "title": "The Brown Recluse and Loxoscelism: Sphingomyelinase D Necrosis vs Exaggerated Myths",
                "tier": "Tier 3: Venom Biochemistry & Extreme Predators",
                "angle": "investigative",
                "slug": "brown_recluse_loxoscelism_sphingomyelinase_d_necrosis_myths",
                "question": "How much of the terrifying internet lore surrounding rotting flesh wounds from brown recluse spider bites is medical misdiagnosis?",
                "focus": "Loxosceles reclusa violin markings, Sphingomyelinase D enzyme disrupting endothelial cell membranes, MRSA and diabetic ulcers frequently misdiagnosed as spider bites, and real treatment protocols.",
                "reason": "Debunks widespread medical hysteria while examining the genuine biochemistry of necrotic venom."
            },
            {
                "id": 14,
                "title": "Brazilian Wandering Spider (Phoneutria): Neurotoxins, Priapism, and Cardiac Symptoms",
                "tier": "Tier 3: Venom Biochemistry & Extreme Predators",
                "angle": "medical_science",
                "slug": "brazilian_wandering_spider_neurotoxins_priapism_cardiac",
                "question": "Why is the venom of the banana spider being actively studied by pharmaceutical laboratories to develop new erectile dysfunction and cardiac medications?",
                "focus": "Tx2-6 peptide triggering nitric oxide release, intense pain, muscle spasms, dangerous hypertensive spikes, banana crate stowaway stories, and therapeutic drug pipelines.",
                "reason": "Fascinating intersection of acute lethal toxicology and cutting-edge pharmaceutical bioprospecting."
            },
            {
                "id": 15,
                "title": "Camel Spiders (Solifugae): Non-Venomous Desert Sprinters, Chelicerae, and Myths",
                "tier": "Tier 3: Venom Biochemistry & Extreme Predators",
                "angle": "case_study",
                "slug": "camel_spiders_solifugae_non_venomous_sprinters_chelicerae_myths",
                "question": "Are camel spiders really 25-MPH screaming desert monsters that chew through sleeping soldiers' stomachs, or harmless misunderstood predators?",
                "focus": "Solifugid anatomy (neither true spiders nor scorpions), massive dual-action vertical shear chelicerae, sprinting at 10 MPH chasing human shade (not attacking), and zero venom production.",
                "reason": "Debunks legendary military urban legends while admiring one of the desert's fiercest micro-predators."
            },
            {
                "id": 16,
                "title": "The Secret World of Amblypygi (Tailless Whip Scorpions): Feelers and Harmless Terrors",
                "tier": "Tier 4: Diversity Beyond Spiders & Biotech",
                "angle": "bizarre_creatures",
                "slug": "secret_world_of_amblypygi_tailless_whip_scorpions_feelers",
                "question": "Why did the horrifying creature featured in Harry Potter's Defense Against the Dark Arts class turn out to be a completely harmless gentle giant?",
                "focus": "Elongated antenniform whip-legs acting as sensory probes in dark caves, spiny raptorial pedipalps, complex social interactions and maternal bonding, and lack of venom glands.",
                "reason": "Fascinating celebration of an obscure, misunderstood arachnid order that looks terrifying but is completely benign."
            },
            {
                "id": 17,
                "title": "Harvestmen (Daddy Longlegs): Opiliones Biology, Non-Venomous Defenses, and Repellents",
                "tier": "Tier 4: Diversity Beyond Spiders & Biotech",
                "angle": "comparative_analysis",
                "slug": "harvestmen_daddy_longlegs_opiliones_non_venomous_defenses",
                "question": "Why is the common playground myth that 'daddy longlegs are the most poisonous spiders on earth but can't bite you' 100% false?",
                "focus": "Order Opiliones (fused single-body segment, two eyes, zero venom, zero silk), repugnatorial scent glands secreting quinones to repel ants, and harvestmen leg shedding autotomy.",
                "reason": "Busts the most ubiquitous childhood animal myth on the planet with real anatomical science."
            },
            {
                "id": 18,
                "title": "Ticks and Mites (Acari): Lyme Disease Pathogens, Lone Star Alpha-Gal, and Dust Mites",
                "tier": "Tier 4: Diversity Beyond Spiders & Biotech",
                "angle": "health_science",
                "slug": "ticks_and_mites_acari_lyme_disease_lone_star_alpha_gal",
                "question": "How did microscopic parasitic arachnids evolve barbed hypostome mouthparts that anchor into human skin to feed undisturbed for days?",
                "focus": "Blacklegged tick (Ixodes scapularis) transmitting Borrelia burgdorferi, the Lone Star tick (Amblyomma americanum) triggering mammalian meat allergies (Alpha-Gal), and microscopic eyelash Demodex mites.",
                "reason": "Vital public health and medical parasitology guide exploring the arachnid order that most directly impacts humans."
            },
            {
                "id": 19,
                "title": "Synthetic Spider Silk: Genetically Modified Yeast, Silkworms, and Mass Bio-Manufacturing",
                "tier": "Tier 4: Diversity Beyond Spiders & Biotech",
                "angle": "biotechnology",
                "slug": "synthetic_spider_silk_genetically_modified_yeast_silkworms",
                "question": "Why can't you farm spiders like silkworms (cannibalism), and how are synthetic biology startups brewing spider silk in beer-brewing vats?",
                "focus": "Recombinant DNA insertion into Pichia pastoris yeast and E. coli, microfluidic spinning nozzles replicating spider duct shear forces, biodegradable surgical sutures, and lightweight bulletproof composites.",
                "reason": "Cutting-edge biotechnology investigation into mass-producing nature's greatest structural super-material."
            },
            {
                "id": 20,
                "title": "Arachnophobia to Fascination: Cognitive Behavioral Therapy and Appreciating Apex Predators",
                "tier": "Tier 4: Diversity Beyond Spiders & Biotech",
                "angle": "psychological_profile",
                "slug": "arachnophobia_to_fascination_cbt_exposure_therapy_predators",
                "question": "Why are human brains evolutionarily primed to fear eight-legged creatures, and how can systematic exposure turn terror into admiration?",
                "focus": "Evolutionary preparedness theory (Seligman), amygdala visual threat detection shortcuts, gradual in-vivo exposure therapy with docile tarantulas, and recognizing spiders as essential pest-control ecosystem guardians.",
                "reason": "Transformative, compassionate masterclass capstone turning widespread human fear into deep ecological appreciation."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Goliath Birdeater Tarantula: Keeping the Heaviest Spider in the World as a Pet",
                "trend_score": 95,
                "angle": "pet_enthusiast",
                "slug": "goliath_birdeater_tarantula_heaviest_spider_in_world",
                "why_trending": "Massive exotic pet community interest in Theraphosa blondi with dinner-plate leg spans and 1.5-inch fangs.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Peacock Spiders (Maratus): The Dazzling Mating Dances Captivating Millions on TikTok",
                "trend_score": 96,
                "angle": "viral_nature",
                "slug": "peacock_spiders_maratus_dazzling_mating_dances_viral",
                "why_trending": "Ultra-viral macro footage of colorful Australian jumping spiders raising iridescent abdomen flaps and waving legs to rhythmic drum beats.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Underwater Diving Bell Spider (Argyroneta Aquatica): The Only Spider Living Submerged",
                "trend_score": 92,
                "angle": "natural_wonder",
                "slug": "underwater_diving_bell_spider_only_spider_living_submerged",
                "why_trending": "Fascinating documentary topic exploring how a spider captures air bubbles on surface hairs to construct an underwater physical gill.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Black Widow vs Brown Recluse: Identifying Real Medical Threats vs Harmless Spiders",
                "trend_score": 94,
                "angle": "safety_guide",
                "slug": "black_widow_vs_brown_recluse_identifying_real_threats",
                "why_trending": "Consistently high-ranking search and YouTube guide helping homeowners accurately identify venomous species vs harmless cobweb spiders.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Spider Silk Bulletproof Vests: Are We Finally Close to Commercial Bio-Engineered Armor?",
                "trend_score": 93,
                "angle": "tech_disruption",
                "slug": "spider_silk_bulletproof_vests_commercial_bio_engineered_armor",
                "why_trending": "Breakthrough military defense contracts testing bio-engineered recombinant spider silk body armor panels.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "The Lone Star Tick and Red Meat Allergy: The Medical Mystery of Alpha-Gal Syndrome",
                "trend_score": 95,
                "angle": "medical_mystery",
                "slug": "lone_star_tick_red_meat_allergy_alpha_gal_syndrome",
                "why_trending": "Surging public curiosity and news coverage regarding tick bites causing lifelong allergic anaphylaxis to beef, pork, and dairy.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Ballooning Spiders: How Spiders Use Earth's Electric Field to Fly Hundreds of Miles",
                "trend_score": 94,
                "angle": "scientific_breakthrough",
                "slug": "ballooning_spiders_earths_electric_field_electrostatic_flight",
                "why_trending": "Mind-blowing discovery that spiders use atmospheric electric potential gradients (APGs) and electrostatic repulsion—not just wind—to take flight into the jet stream.",
                "status": "Queued"
            }
        ]
    },
    "195_reptiles": {
        "id": "195",
        "slug": "reptiles",
        "title": "Reptiles",
        "category": "Life_Biology",
        "audience": "Herpetologists, Reptile Keepers, Zoo Educators, Wildlife Photographers, Evolutionary Biologists (Global)",
        "progression": [
            ("Tier 1: Reptilian Biology & Evolutionary Breakthroughs: The Amniotic Egg, Ectothermy & Keratin Scales (Beginner / Scratch)",
             "The evolutionary conquest of dry land, amniotic egg membrane anatomy, ectothermic metabolic efficiency, keratinized beta-scales and ecdysis shedding, and heart hemodynamics."),
            ("Tier 2: Sensory Systems & Locomotion: Jacobson's Organ, Pit Organs (Infrared Vision) & Snake Movement Mechanics (Intermediate)",
             "Chemosensory tracking via Jacobson's organ, infrared pit organ thermal imaging, serpentine/sidewinding biomechanics, chameleon guanine nanocrystal color changes, and turtle shell evolution."),
            ("Tier 3: Apex Predators & Extreme Adaptations: Crocodilians, Sea Turtles, Monitor Lizards & Constrictors (Upper Intermediate)",
             "Saltwater crocodile 3,700 PSI bite force physics, Komodo dragon anticoagulant venom glands, giant constrictor muscular suffocation, sea turtle magnetic navigation, and venomous helodermatid lizards."),
            ("Tier 4: Venom Systems, Ancient Lineages & Conservation: Elapids vs Viperids, Tuatara, and Habitat Preservation (Advanced / Masterclass)",
             "Venom evolution and hinged fangs (elapids vs vipers), the ancient Tuatara third parietal eye, parthenogenic virgin births, invasive Everglades pythons, and captive herpetoculture conservation.")
        ],
        "flagship": {
            "title": "The Amniotic Revolution: How Reptiles Conquered Dry Land 310 Million Years Ago",
            "angle": "historical_evolution",
            "slug": "195_reptiles_historical_evolution_the_amniotic_revolution"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Amniotic Revolution: How Reptiles Conquered Dry Land 310 Million Years Ago",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "amniotic_revolution_how_reptiles_conquered_dry_land",
                "question": "How did an ancient tetrapod enclosing a pond inside a leathery eggshell trigger the greatest terrestrial expansion in vertebrate history?",
                "focus": "Amnion, chorion, allantois, and yolk sac anatomy, freeing vertebrates from reproductive dependence on water bodies, Hylonomus in Carboniferous tree hollows, and the dawn of amniotes.",
                "reason": "The defining evolutionary milestone that birthed all reptiles, birds, and mammals."
            },
            {
                "id": 2,
                "title": "Ectothermy vs Endothermy: The Energetic Brilliance of Basking and Low Metabolic Overhead",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "ectothermy_vs_endothermy_energetic_brilliance_basking",
                "question": "Why can an alligator survive on one meal every six months while a lion of equal weight starves to death in three weeks?",
                "focus": "Basal metabolic rate comparison (ectotherms consuming 90% less energy than endotherms), behavioral thermoregulation (shuttling between sun and shade), and surviving in resource-scarce deserts.",
                "reason": "Establishes the brilliant physiological energy-conservation strategy underlying all reptilian survival."
            },
            {
                "id": 3,
                "title": "Keratin Scales and Ecdysis: How Snakes and Lizards Shed Their Skin in One Piece",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "process_walkthrough",
                "slug": "keratin_scales_ecdysis_how_snakes_lizards_shed_skin",
                "question": "What chemical lymph layer lubricates the old epidermis allowing a growing snake to turn its skin completely inside out?",
                "focus": "Beta-keratin vs alpha-keratin rigidity, the 'blue' phase of milky clouded eye spectacle scales, lymphatic fluid separation, rubbing rostral scales against rocks, and health diagnostics from sheds.",
                "reason": "Detailed biological guide explaining the growth and dermatological regeneration of scaled reptiles."
            },
            {
                "id": 4,
                "title": "The Four Living Reptile Orders: Crocodilia, Sphenodontia, Squamata, and Testudines",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "four_living_reptile_orders_crocodilia_sphenodontia_squamata",
                "question": "How do turtles, crocodilians, tuataras, and snakes/lizards map onto the deep diapsid family tree?",
                "focus": "Anapsid vs diapsid skull morphology, Squamata (10,000 species of lizards and snakes), Testudines (turtles/tortoises), Crocodilia (alligators/crocs/gharial), and the solitary Sphenodontia (Tuatara).",
                "reason": "Essential taxonomic overview clarifying the phylogenetic relationships across the class Reptilia."
            },
            {
                "id": 5,
                "title": "The Three-Chambered Heart: Blood Shunting, Submergence, and Crocodilian Exceptions",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "three_chambered_heart_blood_shunting_submergence_crocodilian",
                "question": "How do reptiles bypass their lungs while holding their breath underwater without starving their vital brain organs of oxygen?",
                "focus": "Two atria and one partially divided ventricle, physiological right-to-left cardiac shunting, the unique four-chambered crocodilian heart with the Foramen of Panizza, and underwater endurance.",
                "reason": "In-depth cardiovascular engineering breakdown explaining reptilian underwater physiological mastery."
            },
            {
                "id": 6,
                "title": "Jacobson's Organ and the Forked Tongue: Smelling in Stereo and Chemosensory Tracking",
                "tier": "Tier 2: Sensory Systems & Locomotion",
                "angle": "sensory_science",
                "slug": "jacobsons_organ_forked_tongue_smelling_in_stereo",
                "question": "How does a snake flicking its wet forked tongue through the air extract a 3D directional scent map of a rodent 50 yards away?",
                "focus": "Vomeronasal (Jacobson's) organ in the roof of the mouth, forked tongue tips sampling differential odor concentrations in stereo, transferring non-volatile lipid molecules, and trailing prey scents.",
                "reason": "Examines one of the most elegant and refined chemical sensing systems in vertebrate evolution."
            },
            {
                "id": 7,
                "title": "Pit Organs and Thermal Vision: How Pit Vipers and Pythons See Warm Prey in Darkness",
                "tier": "Tier 2: Sensory Systems & Locomotion",
                "angle": "scientific_phenomenon",
                "slug": "pit_organs_thermal_vision_pit_vipers_pythons_darkness",
                "question": "How do rattlesnakes strike a mouse's head with pinpoint accuracy in pitch-black caves without using their eyes?",
                "focus": "Loreal pit organ membranes packed with TRPA1 heat-sensitive ion channels, detecting infrared radiation wavelengths (5 to 30 microns) down to 0.003°C differences, and optic tectum visual overlay.",
                "reason": "Fascinating exploration of natural thermal imaging technology operating in predatory snakes."
            },
            {
                "id": 8,
                "title": "The Biomechanics of Snake Locomotion: Serpentine, Concertina, Sidewinding, and Rectilinear",
                "tier": "Tier 2: Sensory Systems & Locomotion",
                "angle": "biomechanics",
                "slug": "biomechanics_of_snake_locomotion_serpentine_concertina_sidewinding",
                "question": "How do limbless vertebrates climb vertical pine trees, glide down loose desert sand dunes, and sprint through thick brush?",
                "focus": "Lateral undulation (pushing against lateral resistance points), concertina movement in tight tunnels, sidewinding physics on loose shifting sand, and ventral scale caterpillar rectilinear crawl in heavy vipers.",
                "reason": "Masterclass in mechanical physics and limbless locomotive engineering."
            },
            {
                "id": 9,
                "title": "Color Change in Chameleons: Guanine Nanocrystals, Structural Coloration, and Mood",
                "tier": "Tier 2: Sensory Systems & Locomotion",
                "angle": "materials_science",
                "slug": "color_change_in_chameleons_guanine_nanocrystals_structural",
                "question": "Why did science overturn the myth that chameleons change color to match their background, and how do photonic crystals shift color in seconds?",
                "focus": "Dermal iridophores tuning lattice spacing of guanine nanocrystals to reflect different light wavelengths, pigmentary melanin dispersal, mood and social dominance signaling, and temperature regulation.",
                "reason": "Reveals the astonishing quantum optical and photonic physics operating in chameleon skin."
            },
            {
                "id": 10,
                "title": "Turtle Shell Anatomy: The Plastron, Carapace, and How Ribs Evolved to Encase the Skeleton",
                "tier": "Tier 2: Sensory Systems & Locomotion",
                "angle": "evolutionary_milestone",
                "slug": "turtle_shell_anatomy_plastron_carapace_ribs_encasing_skeleton",
                "question": "How did ancestral turtles pull their shoulder blades and pelvic girdles inside their rib cages—something no other vertebrate has ever done?",
                "focus": "Fossil transitions (Eunotosaurus, Odontochelys, Proganochelys), dermal bone fusion, keratinous scute overlays, bridge junctions between dorsal carapace and ventral plastron, and shell respiration.",
                "reason": "Deep evolutionary analysis of nature's most impenetrable and structurally bizarre body armor."
            },
            {
                "id": 11,
                "title": "Saltwater Crocodiles: 20-Foot Apex Hunters, Death Rolls, and 3,700 PSI Bite Force",
                "tier": "Tier 3: Apex Predators & Extreme Adaptations",
                "angle": "extreme_scenarios",
                "slug": "saltwater_crocodiles_death_rolls_3700_psi_bite_force",
                "question": "What allows Crocodylus porosus to dominate both freshwater rivers and open oceans, crushing prey with the strongest bite force measured in nature?",
                "focus": "Lingual salt glands excreting ocean brine, massive pterygoid and jaw-closing muscles, the death roll kinetic energy tearing limbs, pressure-sensitive integumentary sense organs, and hunting buffalo.",
                "reason": "Thrilling, terrifying documentary profile of the largest living reptile on the planet."
            },
            {
                "id": 12,
                "title": "The Komodo Dragon: Venomous Anticoagulants, Serrated Teeth, and Megafauna Stalking",
                "tier": "Tier 3: Apex Predators & Extreme Adaptations",
                "angle": "case_study",
                "slug": "komodo_dragon_venomous_anticoagulants_serrated_teeth_megafauna",
                "question": "How did Dr. Bryan Fry disprove the classic myth that Komodo dragons kill water buffalo with dirty mouth bacteria, proving they possess complex venom glands?",
                "focus": "Varanus komodoensis mandibular venom glands secreting anticoagulants and shock-inducing proteins, ziphodont serrated teeth acting like steak knives, vomeronasal tracking over 6 miles, and island gigantism.",
                "reason": "Debunks a decades-old wildlife myth with cutting-edge venomological and anatomical science."
            },
            {
                "id": 13,
                "title": "Reticulated Pythons and Green Anacondas: Muscular Constriction Physics and Giant Swallows",
                "tier": "Tier 3: Apex Predators & Extreme Adaptations",
                "angle": "field_guide",
                "slug": "reticulated_pythons_green_anacondas_constriction_physics",
                "question": "How do giant constrictors kill 100-pound deer in under two minutes without breaking their prey's bones?",
                "focus": "Hemodynamic arrest theory (circulatory shutdown from chest cavity pressure rather than slow suffocation), kinetic skull flexibility with quadrate bones disengaging, stomach acid pH dropping to 1.5, and organ hypertrophy.",
                "reason": "Deconstructs the immense mechanical power and extreme digestive physiology of giant constrictors."
            },
            {
                "id": 14,
                "title": "Sea Turtles: Trans-Oceanic Magnetic Navigation, Arribada Nesting, and Marine Hazards",
                "tier": "Tier 3: Apex Predators & Extreme Adaptations",
                "angle": "destination_guide",
                "slug": "sea_turtles_trans_oceanic_magnetic_navigation_arribada_nesting",
                "question": "How does a female sea turtle return 30 years later to the exact 50-yard stretch of beach where she hatched to lay her eggs?",
                "focus": "Geomagnetic imprinting and magnetic inclination sensing, mass synchronized nesting 'arribadas' in Costa Rica, temperature-dependent sex determination (TSD) in sand, longline bycatch, and plastic bag ingestion.",
                "reason": "Epic oceanic voyage documentary exploring the timeless navigation and survival struggles of sea turtles."
            },
            {
                "id": 15,
                "title": "The Gila Monster and Mexican Beaded Lizard: North America's Venomous Lizards and Exenatide",
                "tier": "Tier 3: Apex Predators & Extreme Adaptations",
                "angle": "medical_breakthrough",
                "slug": "gila_monster_mexican_beaded_lizard_venom_exenatide_diabetes",
                "question": "How did a venomous Southwestern desert lizard chewing venom into wounds via grooved teeth lead to a breakthrough multi-billion-dollar diabetes drug?",
                "focus": "Heloderma suspectum osteoderm-studded bead skin, chewing venom mechanics (mandibular glands without pressurized fangs), exendin-4 peptide discovery, and GLP-1 receptor agonist drug synthesis (Byetta).",
                "reason": "Remarkable case study proving the immense, unexpected medical and pharmaceutical value of reptile conservation."
            },
            {
                "id": 16,
                "title": "The Tuatara of New Zealand: Surviving 200 Million Years, a Third Parietal Eye, and Mesozoic Roots",
                "tier": "Tier 4: Venom Systems, Ancient Lineages & Conservation",
                "angle": "prehistoric_deep_dive",
                "slug": "tuatara_new_zealand_third_parietal_eye_mesozoic_roots",
                "question": "Why is New Zealand's Tuatara not a lizard at all, but the sole surviving ghost lineage of an ancient Triassic reptile order that outlived the dinosaurs?",
                "focus": "Order Sphenodontia, the functional parietal 'third eye' on top of juvenile skulls with retina and lens, primitive amphicoelous vertebrae, low-temperature metabolic activity (down to 40°F), and island rat eradication.",
                "reason": "Captivating paleobiological exploration of the most ancient living fossil in the reptile world."
            },
            {
                "id": 17,
                "title": "Vipers vs Elapids: Hemotoxins vs Neurotoxins, Hinged Fangs, and Antivenom",
                "tier": "Tier 4: Venom Systems, Ancient Lineages & Conservation",
                "angle": "venom_science",
                "slug": "vipers_vs_elapids_hemotoxins_neurotoxins_hinged_fangs",
                "question": "How does a viper's folding hypodermic fang delivering tissue-destroying hemotoxin compare to a cobra's fixed short fang delivering paralyzing neurotoxin?",
                "focus": "Solenoglyphous (vipers) vs proteroglyphous (elapids) dentition, phospholipase A2 and metalloproteinases causing tissue necrosis vs post-synaptic neurotoxins stopping diaphragms, and horse antivenom immunization.",
                "reason": "Masterclass in comparative toxinology, venom delivery mechanics, and medical immunology."
            },
            {
                "id": 18,
                "title": "Parthenogenesis in Reptiles: Virgin Births in Mourning Geckos, Komodo Dragons, and Blind Snakes",
                "tier": "Tier 4: Venom Systems, Ancient Lineages & Conservation",
                "angle": "genetic_phenomenon",
                "slug": "parthenogenesis_in_reptiles_virgin_births_mourning_geckos",
                "question": "How can female Komodo dragons and mourning geckos fertilize their own eggs and produce healthy offspring without ever mating with a male?",
                "focus": "Automictic parthenogenesis, terminal fusion of polar bodies with the egg cell, all-female clonal species (Lepidodactylus lugubris), colonizing remote volcanic islands, and genetic diversity trade-offs.",
                "reason": "Mind-bending genetic deep dive revealing how reptiles bend traditional vertebrate reproductive rules."
            },
            {
                "id": 19,
                "title": "The Invasive Burmese Python Crisis in the Florida Everglades: Rewriting Wetland Ecosystems",
                "tier": "Tier 4: Venom Systems, Ancient Lineages & Conservation",
                "angle": "environmental_dilemma",
                "slug": "invasive_burmese_python_crisis_florida_everglades_ecosystem",
                "question": "How did escaped exotic pets establish a breeding population of tens of thousands of giant pythons, collapsing 90% of small mammal populations in South Florida?",
                "focus": "Hurricane Andrew 1992 breeding facility destruction myths vs decades of pet releases, 99% decline in marsh rabbits and raccoons, python vs alligator battles, tracking sentinel 'Judas snakes', and bounty contractor programs.",
                "reason": "Urgent, high-stakes investigative case study of modern biological invasion and ecological collapse."
            },
            {
                "id": 20,
                "title": "Herpetoculture and Modern Conservation: Ethical Captive Breeding vs Poaching and Habitat Destruction",
                "tier": "Tier 4: Venom Systems, Ancient Lineages & Conservation",
                "angle": "conservation_ethics",
                "slug": "herpetoculture_modern_conservation_ethical_captive_breeding",
                "question": "Can private hobbyist captive breeding programs and assurance colonies help save endangered reptiles from total extinction in the wild?",
                "focus": "CITES appendix listings, combating illegal wildlife smuggling in Southeast Asia and Madagascar, captive assurance colonies for extinct-in-the-wild species, bioactive terrarium ecology, and ethical keeping standards.",
                "reason": "Thoughtful, forward-looking capstone exploring the balance between responsible private husbandry and wild habitat preservation."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The King Cobra: Inside the Physiology and Intellect of the World's Longest Venomous Snake",
                "trend_score": 96,
                "angle": "wildlife_spectacle",
                "slug": "king_cobra_physiology_intellect_longest_venomous_snake",
                "why_trending": "Massive global documentary virality showcasing Ophiophagus hannah standing a third of its 18-foot length at eye level, nest-building intelligence, and hunting other snakes.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Ball Python Morphs: The Multi-Million Dollar Designer Genetics Industry",
                "trend_score": 94,
                "angle": "subculture_trend",
                "slug": "ball_python_morphs_designer_genetics_industry_pied_banana",
                "why_trending": "High-interest commercial pet phenomenon exploring co-dominant and recessive color morph genetics (Piebald, Banana, Clown) fetching thousands per animal.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Monster Crocodiles: The Legend and Reality of Lolong and Gustave of Lake Tanganyika",
                "trend_score": 97,
                "angle": "legendary_beasts",
                "slug": "monster_crocodiles_legend_reality_lolong_gustave",
                "why_trending": "Unmatched view counts surrounding true accounts of 20-foot monster crocodiles and elusive maneaters surviving decades in remote waters.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Black Mamba Speed and Strike: The Fastest and Most Feared Snake in Africa",
                "trend_score": 95,
                "angle": "thrill_seeker",
                "slug": "black_mamba_speed_strike_most_feared_snake_africa",
                "why_trending": "High-retention documentary focus on Dendroaspis polylepis coffin-shaped head, pitch-black buccal lining threat display, and 12-MPH terrestrial speed.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Everglades Python Hunting: Bounty Hunters Wrestling 18-Foot Pythons Out of Swamps",
                "trend_score": 93,
                "angle": "reality_action",
                "slug": "everglades_python_hunting_bounty_hunters_wrestling_giants",
                "why_trending": "Viral reality action content following state-contracted python hunters stalking Everglades levees at midnight to capture record-breaking constrictors.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "The Leatherback Sea Turtle: Deep Diving with the Largest Living Reptile Down to 4,000 Feet",
                "trend_score": 91,
                "angle": "marine_marvel",
                "slug": "leatherback_sea_turtle_deep_diving_largest_living_reptile",
                "why_trending": "Fascinating marine biology interest in 1,500-pound leathery-shelled leviathans feeding on jellyfish in icy arctic depths via gigantothermy.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Bearded Dragons as Pets: Why Australia's Desert Lizard Conquered Living Rooms Worldwide",
                "trend_score": 92,
                "angle": "pet_guide",
                "slug": "bearded_dragons_as_pets_australian_desert_lizard_care",
                "why_trending": "Immense lifestyle and beginner pet interest detailing UV lighting, gut-loaded insects, and friendly behavioral cues (arm waving and head bobbing).",
                "status": "Queued"
            }
        ]
    }
}

if __name__ == "__main__":
    print("Generating suites for Batch 191-195...")
    for folder, meta in BATCH_191_195.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 191-195 complete!")
