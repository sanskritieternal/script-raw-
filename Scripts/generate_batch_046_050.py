"""
Batch Generator for Niches 046 to 050:
- 046_disaster_survival
- 047_aviation
- 048_maritime
- 049_pirates_outlaws
- 050_treasure_hunting
"""

import sys
from pathlib import Path

# Add Scripts to sys.path
sys.path.append(str(Path(__file__).parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_046_050 = {
    "046_disaster_survival": {
        "id": "046",
        "slug": "disaster_survival",
        "title": "Disaster & Survival",
        "category": "Conflict_Power_Exploration",
        "audience": "Survivalists, History Buffs, Outdoor Enthusiasts, Disaster Analysts, Resiliency Seekers (Global)",
        "progression": [
            ("Tier 1: Survival Physiology, The Rule of Threes & Catastrophe Psychology (Scratch / Beginner)",
             "Rule of threes (air, shelter, water, food), hypothermia dynamics, freeze vs action amygdala responses, and wilderness triage priority."),
            ("Tier 2: Epic Historic Survival Sagas & Natural Cataclysms (Intermediate)",
             "The 1972 Andes flight disaster, Shackleton's Endurance ice drift, the 1883 Krakatoa volcanic tsunami, and the 1906 San Francisco earthquake fires."),
            ("Tier 3: Industrial Failures, Structural Collapses & Extreme Technical Crises (Upper Intermediate)",
             "The Chernobyl reactor meltdown (1986), Bhopal toxic gas leak (1984), Deepwater Horizon blowout, and the Tham Luang Thai cave rescue (2018)."),
            ("Tier 4: Global Extinction Hazards, Nuclear Winter & Next-Gen Disaster Engineering (Advanced / Expert)",
             "Supervolcanic winter models, solar coronal mass ejections (Carrington event), deep subterranean fallout bunkers, and disaster robotics.")
        ],
        "flagship": {
            "title": "The Miracle in the Andes: 72 Days Trapped on a Glacier and the Ultimate Human Will",
            "angle": "beginner_explainers",
            "slug": "046_disaster_survival_beginner_explainers_andes_miracle"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Miracle in the Andes: 72 Days Trapped on a Glacier and the Ultimate Human Will",
                "tier": "Tier 1: Survival Physiology & Emergency Psychology",
                "angle": "beginner_explainers",
                "slug": "miracle_in_the_andes_1972_uruguayan_flight_571_survival",
                "question": "How did 16 Uruguayan rugby players survive 72 days in the freezing Andes at 11,500 feet after their search was called off?",
                "key_focus": "The fuselage shelter engineering, melting snow with metal sheets, agonizing moral decision of anthropophagy, Nando Parrado and Roberto Canessa's 10-day trek.",
                "reason": "Flagship launch episode; the most profound, harrowing testament to the human survival instinct in modern history."
            },
            {
                "id": 2,
                "title": "The Rule of Threes: The Biomechanics of How the Human Body Dies in the Wild",
                "tier": "Tier 1: Survival Physiology & Emergency Psychology",
                "angle": "how_it_works",
                "slug": "rule_of_threes_survival_physiology_oxygen_shelter_water_food",
                "question": "Why does a human body expire in 3 minutes without air, 3 hours without shelter in freezing wetness, 3 days without water, and 3 weeks without food?",
                "key_focus": "Hypothermia paradox, renal failure in dehydration, metabolic ketoacidosis and starvation stages, shelter insulation physics.",
                "reason": "The foundational medical and physiological framework for understanding survival priorities."
            },
            {
                "id": 3,
                "title": "Shackleton's Endurance: 18 Months Stranded on Antarctic Sea Ice Without Losing a Man",
                "tier": "Tier 1: Survival Physiology & Emergency Psychology",
                "angle": "case_studies",
                "slug": "ernest_shackleton_endurance_expedition_antarctica_survival_1914",
                "question": "How did Sir Ernest Shackleton lead 27 men across crushing pack ice, open stormy seas in a 22-foot lifeboat, and uncharted mountain peaks to safety?",
                "key_focus": "Crushing of the Endurance, camp discipline on drifting ice floes, the 800-mile James Caird open-boat navigation, crossing South Georgia glaciers.",
                "reason": "The supreme historical masterpiece of crisis leadership and wilderness endurance."
            },
            {
                "id": 4,
                "title": "The Psychology of Panic: Why 80% of People Freeze During Catastrophes",
                "tier": "Tier 1: Survival Physiology & Emergency Psychology",
                "angle": "psychological_tricks",
                "slug": "survival_psychology_amygdala_hijack_and_the_10_80_10_rule",
                "question": "Why do the majority of airplane crash passengers sit paralyzed in their seats while survivors immediately unbuckle and run toward exits?",
                "key_focus": "Cognitive paralysis and behavioral freeze, John Leach 10-80-10 rule of disaster behavior, stress inoculation training, situational awareness.",
                "reason": "Crucial psychological survival insight that saves lives in real-world emergencies."
            },
            {
                "id": 5,
                "title": "127 Hours: Aron Ralston's Agonizing Choice in Bluejohn Canyon",
                "tier": "Tier 1: Survival Physiology & Emergency Psychology",
                "angle": "hidden_stories",
                "slug": "aron_ralston_127_hours_bluejohn_canyon_arm_amputation_survival",
                "question": "What pushed a solo canyoneer pinned by an 800-pound boulder to snap his own arm bones with torque and sever his limb with a dull pocketknife?",
                "key_focus": "Crush syndrome toxin buildup, self-amputation torque physics, hallucination and hypothermia, rappelling single-handed to rescue.",
                "reason": "Visceral, unforgettable modern demonstration of radical individual determination."
            },
            {
                "id": 6,
                "title": "Krakatoa 1883: The Volcanic Detonation That Heard Around the World Four Times",
                "tier": "Tier 2: Epic Historic Sagas & Natural Cataclysms",
                "angle": "history_origins",
                "slug": "krakatoa_1883_volcanic_eruption_tsunami_and_global_climate_shock",
                "question": "How did a volcanic caldera explosion generate a 310 dB sound pressure wave that ruptured eardrums 40 miles away and circled the globe 4 times?",
                "key_focus": "Pyroclastic flow travel over open seawater, 120-foot tsunamis obliterating coastal Sunda Strait towns, 5-year global temperature drop.",
                "reason": "The loudest and most devastating natural detonation in recorded human history."
            },
            {
                "id": 7,
                "title": "The 1906 San Francisco Earthquake: When Firestorm Smashed a Gilded Age Metropolis",
                "tier": "Tier 2: Epic Historic Sagas & Natural Cataclysms",
                "angle": "famous_examples",
                "slug": "1906_san_francisco_earthquake_and_firestorm_urban_destruction",
                "question": "Why did ruptured water mains force the US Army to dynamite whole city blocks, accidentally sparking an inferno that destroyed 80% of San Francisco?",
                "key_focus": "San Andreas fault 20-foot strike-slip displacement, firestorm thermal convection, Ham and Eggs fire origin, refugee tent cities in the Presidio.",
                "reason": "The foundational disaster that revolutionized modern American building codes and earthquake geology."
            },
            {
                "id": 8,
                "title": "Juliane Koepcke: Falling 10,000 Feet from the Sky into the Peruvian Amazon",
                "tier": "Tier 2: Epic Historic Sagas & Natural Cataclysms",
                "angle": "case_studies",
                "slug": "juliane_koepcke_lansa_508_plane_crash_amazon_jungle_survival",
                "question": "How did a 17-year-old girl strapped to a row of airplane seats survive a two-mile plunge through the clouds and walk out of the jungle 11 days later?",
                "key_focus": "LANSA Flight 508 thunderstorm breakup, canopy foliage cushioning physics, following downstream water flow rule, treating maggot-infested wounds with gasoline.",
                "reason": "One of the most astonishing solo aviation survival stories ever recorded."
            },
            {
                "id": 9,
                "title": "The 2004 Indian Ocean Tsunami: The 9.1 Megathrust Quake and the Unwarned Coastlines",
                "tier": "Tier 2: Epic Historic Sagas & Natural Cataclysms",
                "angle": "timeline_evolution",
                "slug": "2004_indian_ocean_tsunami_boxing_day_banda_aceh_disaster",
                "question": "Why did a seafloor rupture off Sumatra unleash a series of ocean surges that claimed 230,000 lives across 14 nations with zero early warning systems?",
                "key_focus": "Megathrust fault subduction dynamics, deep-ocean wave velocity (500 mph) vs coastal shoaling, Tilly Smith saving a beach, creation of the DART buoy network.",
                "reason": "The deadliest tsunami in human history and the catalyst for global ocean monitoring grids."
            },
            {
                "id": 10,
                "title": "Mount St. Helens 1980: The Lateral Blast That Flattened 230 Square Miles of Forest",
                "tier": "Tier 2: Epic Historic Sagas & Natural Cataclysms",
                "angle": "scientific_breakthroughs",
                "slug": "mount_st_helens_1980_eruption_lateral_blast_and_david_johnston",
                "question": "How did a 5.1 earthquake trigger the largest subaerial landslide in history, venting volcanic pressure sideways at 670 mph?",
                "key_focus": "Debris avalanche mechanics, volcanologist David Johnston's final radio call ('Vancouver! This is it!'), blowdown zone timber shockwaves.",
                "reason": "The defining event in modern physical volcanology and hazard boundary mapping."
            },
            {
                "id": 11,
                "title": "Chernobyl 1986: The 60-Second Turbine Test That Blew Open Reactor No. 4",
                "tier": "Tier 3: Industrial Failures & Extreme Technical Crises",
                "angle": "behind_the_scenes",
                "slug": "chernobyl_1986_reactor_four_meltdown_rmbk_flaw_and_liquidators",
                "question": "What fatal sequence of human error, xenon gas poisoning, and a graphite-tipped control rod flaw transformed Pripyat into a radioactive ghost town?",
                "key_focus": "RBMK positive void coefficient design flaw, AZ-5 scram button disaster trigger, three divers in the bubbler pool, 600,000 liquidators sarcophagus construction.",
                "reason": "The ultimate industrial technological disaster, speeding the collapse of the Soviet Union."
            },
            {
                "id": 12,
                "title": "Bhopal 1984: The Deadly Midnight Cloud That Murdered a Sleeping City",
                "tier": "Tier 3: Industrial Failures & Extreme Technical Crises",
                "angle": "dark_secrets",
                "slug": "bhopal_disaster_1984_union_carbide_methyl_isocyanate_gas_leak",
                "question": "How did cost-cutting, disabled refrigeration units, and water leaking into Tank 610 release 40 tons of lethal methyl isocyanate gas across Bhopal?",
                "key_focus": "Exothermic runaway reaction chemistry, pulmonary edema choking victims in their sleep, corporate negligence, ongoing environmental contamination.",
                "reason": "The world's worst industrial chemical catastrophe with enduring corporate accountability lessons."
            },
            {
                "id": 13,
                "title": "The Deepwater Horizon Blowout: 87 Days of Oil Spewing into the Gulf of Mexico",
                "tier": "Tier 3: Industrial Failures & Extreme Technical Crises",
                "angle": "how_it_works",
                "slug": "deepwater_horizon_blowout_macondo_well_bp_oil_spill_mechanics",
                "question": "Why did faulty cement, misread negative pressure tests, and an uninspected blind shear ram cause the Macondo well to explode in 5,000 feet of water?",
                "key_focus": "Methane gas kick mechanics, blowout preventer (BOP) hydraulic shear failure, 4.9 million barrels spilled, ROV capping stack success on Day 87.",
                "reason": "The worst offshore environmental and petroleum engineering disaster in US history."
            },
            {
                "id": 14,
                "title": "The Thai Cave Rescue (2018): Anaesthetizing 12 Boys to Swim Them Out of a Flooded Cavern",
                "tier": "Tier 3: Industrial Failures & Extreme Technical Crises",
                "angle": "case_studies",
                "slug": "thai_cave_rescue_2018_tham_luang_wild_boars_cave_diving_miracle",
                "question": "How did an international team of cave divers execute a medical plan considered impossible: ketamine sedation of 12 children through zero-visibility sumps?",
                "key_focus": "Sump diving navigation in muddy currents, Dr. Richard Harris ketamine dosing protocol, full-face positive pressure masks, Saman Kunan's sacrifice.",
                "reason": "The most complex, audacious, and victorious multinational search-and-rescue operation ever mounted."
            },
            {
                "id": 15,
                "title": "Apollo 13: 'Houston, We've Had a Problem' and the Orbital Lifeboat Triumph",
                "tier": "Tier 3: Industrial Failures & Extreme Technical Crises",
                "angle": "hidden_stories",
                "slug": "apollo_13_oxygen_tank_explosion_lunar_module_lifeboat_rescue",
                "question": "How did three astronauts and mission control jury-rig carbon dioxide lithium hydroxide scrubbers with duct tape and cardboard 200,000 miles from Earth?",
                "key_focus": "Teflon wire short circuit in Service Module Oxygen Tank 2, Aquarius lunar module lifeboat power-down, manual alignment burns using the Earth's terminator.",
                "reason": "The gold standard of engineering improvisation, teamwork, and composure under extreme mortal peril."
            },
            {
                "id": 16,
                "title": "The Carrington Event (1859): The Solar Superstorm That Electrified Telegraph Lines",
                "tier": "Tier 4: Global Extinction Hazards & Next-Gen Preparedness",
                "angle": "history_origins",
                "slug": "carrington_event_1859_coronal_mass_ejection_solar_geomagnetic_storm",
                "question": "What happens when a direct-hit solar flare creates auroras bright enough to read newspapers at midnight and shocks telegraph operators through disconnected lines?",
                "key_focus": "Coronal mass ejection (CME) physics, magnetosphere compression, induction currents in copper wire grids, 2012 near-miss STEREO spacecraft data.",
                "reason": "A real cosmic hazard that would collapse the entire modern power grid and satellite communication network."
            },
            {
                "id": 17,
                "title": "Yellowstone and Toba: The Physics and Aftermath of a Supervolcanic Winter",
                "tier": "Tier 4: Global Extinction Hazards & Next-Gen Preparedness",
                "angle": "unsolved_mysteries",
                "slug": "supervolcano_eruption_yellowstone_lake_toba_genetic_bottleneck",
                "question": "Did the eruption of Mount Toba 74,000 years ago reduce the entire human species to fewer than 10,000 breeding individuals in a decade-long winter?",
                "key_focus": "Volcanic Explosivity Index (VEI 8), stratospheric sulfate aerosol solar shielding, continental ash accumulation models, genetic bottleneck controversy.",
                "reason": "Examines the planetary-scale natural hazard with the highest potential extinction consequence."
            },
            {
                "id": 18,
                "title": "Nuclear Winter: The Climatic Catastrophe Behind Global Thermonuclear War",
                "tier": "Tier 4: Global Extinction Hazards & Next-Gen Preparedness",
                "angle": "scientific_breakthroughs",
                "slug": "nuclear_winter_climatic_consequences_soot_injection_climate_models",
                "question": "Why would the true killer in a nuclear conflict not be the initial blast or prompt radiation, but 150 million tons of black carbon soot blocking the sun for a decade?",
                "key_focus": "Carl Sagan and TTAPS study, modern Robock-Toon climate simulation models, ozone layer destruction, agricultural collapse and global famine.",
                "reason": "The defining scientific deterrent concept that shaped Cold War disarmament diplomacy."
            },
            {
                "id": 19,
                "title": "Bunker Engineering: How Billionaires and Governments Prepare for the Apocalypse",
                "tier": "Tier 4: Global Extinction Hazards & Next-Gen Preparedness",
                "angle": "behind_the_scenes",
                "slug": "underground_survival_bunkers_cheyenne_mountain_svalbard_seed_vault",
                "question": "How do deep underground facilities like Cheyenne Mountain, Raven Rock, and private billionaire survival complexes maintain independent air, power, and security?",
                "key_focus": "EMP Faraday shielding, spring-mounted blast dampers, CBRN air filtration scrubbers, geothermal water recycling, Svalbard Global Seed Vault design.",
                "reason": "Fascinating intersection of extreme engineering, geopolitics, and doomsday contingency planning."
            },
            {
                "id": 20,
                "title": "Disaster Robotics and AI First Responders: The Future of Search and Rescue",
                "tier": "Tier 4: Global Extinction Hazards & Next-Gen Preparedness",
                "angle": "future_predictions",
                "slug": "search_and_rescue_robotics_ai_drones_thermal_imaging_future",
                "question": "Can autonomous quadruped robots, drone swarms, and snake-bots navigate rubble to find heartbeat signals faster than human sniffer dogs?",
                "key_focus": "DARPA Subterranean Challenge, UWB through-wall radar respiration detection, autonomous swarm mapping in GPS-denied environments, earthquake response.",
                "reason": "The cutting-edge frontier of robotics and AI dedicated to saving human lives during catastrophic events."
            }
        ],
        "trending": [
            {
                "id": 1,
                "title": "What Actually Happens to Your Body When You Freeze to Death? (Paradoxical Undressing)",
                "angle": "scientific_breakthroughs",
                "hook": "Why do victims of extreme hypothermia take off all their clothes in freezing blizzards and cram themselves into tiny enclosed spaces before dying?",
                "target_audience": "Curious minds, biology nerds, true crime and mystery lovers",
                "estimated_views": "2.9M - 5.2M",
                "production_effort": "Low",
                "why_it_works": "Fascinating biological mystery solving Dyatlov Pass and wilderness deaths."
            },
            {
                "id": 2,
                "title": "The Only Man to Survive Two Atomic Bombs: Tsutomu Yamaguchi",
                "angle": "case_studies",
                "hook": "He was burned by the Hiroshima bomb on Monday. He bandaged his wounds, caught the train home to Nagasaki, and survived the second nuclear blast on Thursday.",
                "target_audience": "History buffs, war documentary viewers, resilience seekers",
                "estimated_views": "3.4M - 6.0M",
                "production_effort": "Medium",
                "why_it_works": "An unbelievable, officially certified human survival miracle from World War II."
            },
            {
                "id": 3,
                "title": "How to Survive a Nuclear Blast: The First 60 Minutes That Decide Your Fate",
                "angle": "survival_tips",
                "hook": "If you see a blinding flash on the horizon, do NOT get in your car to drive away. Here is the exact physics-based protocol FEMA recommends.",
                "target_audience": "Preppers, curious citizens, geopolitics followers",
                "estimated_views": "4.2M - 7.5M",
                "production_effort": "Medium",
                "why_it_works": "Extreme evergreen search volume and viral survival utility."
            },
            {
                "id": 4,
                "title": "The Scariest 20 Minutes in Aviation: British Airways Flight 9 in Volcanic Ash",
                "angle": "famous_examples",
                "hook": "At 37,000 feet, all four engines on a Boeing 747 stopped dead at once due to invisible volcanic ash. How Captain Eric Moody glided in silence.",
                "target_audience": "Aviation geeks, thrill-seekers, disaster fans",
                "estimated_views": "2.2M - 4.1M",
                "production_effort": "Medium",
                "why_it_works": "The famous calm captain announcement ('We have a small problem...') and unbelievable dead-stick engine restart."
            },
            {
                "id": 5,
                "title": "The Harrison Okene Miracle: 60 Hours Trapped in an Air Pocket 100 Feet Underwater",
                "angle": "case_studies",
                "hook": "When a tugboat sank to the Atlantic seabed in total darkness, a ship cook survived 3 days in freezing saltwater inside a 4-foot air bubble.",
                "target_audience": "Documentary viewers, scuba divers, ocean lovers",
                "estimated_views": "3.8M - 6.5M",
                "production_effort": "Medium",
                "why_it_works": "Real terrifying diver helmet-cam footage of finding a living hand in a sunken shipwreck."
            },
            {
                "id": 6,
                "title": "What If the Carrington Event Happened Tomorrow? How Society Collapses in 72 Hours",
                "angle": "future_predictions",
                "hook": "No water pumps, no cell towers, no financial transactions, and transformers melting on electric poles. The mathematical reality of a solar grid collapse.",
                "target_audience": "Tech nerds, survivalists, apocalyptic scenario lovers",
                "estimated_views": "2.5M - 4.8M",
                "production_effort": "Medium",
                "why_it_works": "Terrifying plausible catastrophe grounded in astrophysics and infrastructure fragility."
            },
            {
                "id": 7,
                "title": "5 Cheap Everyday Items That Will Save Your Life in a Real Disaster",
                "angle": "actionable_challenges",
                "hook": "You don't need a $10,000 bunker. A plastic water bottle, a piece of charcoal, and a sheet of tin foil can keep you alive when society breaks down.",
                "target_audience": "Everyday preppers, camping enthusiasts, budget-conscious viewers",
                "estimated_views": "1.8M - 3.4M",
                "production_effort": "Low",
                "why_it_works": "Actionable, highly shareable practical DIY utility."
            }
        ]
    },
    "047_aviation": {
        "id": "047",
        "slug": "aviation",
        "title": "Aviation",
        "category": "Transport_Engineering",
        "audience": "Avgeeks, Aerospace Engineers, Commercial Pilots, Military History Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Lift Physics, Wind Tunnels & The Pioneering Wright Era (Scratch / Beginner)",
             "Bernoulli principle vs Newton's third law of lift, Kitty Hawk 1903 wing-warping, pitot-static tube flight instruments, and the standard cross-check."),
            ("Tier 2: The Sound Barrier, The Jet Age & The Queen of the Skies (Intermediate)",
             "Chuck Yeager's Bell X-1 Mach 1 dive, the Boeing 707 barrel roll, Concorde's Mach 2 ogival delta wing, and the Boeing 747 high-bypass turbofan revolution."),
            ("Tier 3: Air Disaster Forensics, Windshear & CRM Cockpit Psychology (Upper Intermediate)",
             "Tenerife 1977 runway disaster, Aloha Airlines 243 fuselage skin peeling, microburst windshear detection, and Cockpit Resource Management (CRM)."),
            ("Tier 4: Stealth Radar Cross-Sections, Hypersonic Scramjets & Autonomous Flight (Advanced / Expert)",
             "SR-71 Blackbird titanium thermal expansion, B-2 Spirit flying wing radar evasion, scramjet Mach 7 combustion physics, and autonomous eVTOL urban flight.")
        ],
        "flagship": {
            "title": "Tenerife 1977: The 583-Fatality Disaster That Rewrote Cockpit Psychology Forever",
            "angle": "beginner_explainers",
            "slug": "047_aviation_beginner_explainers_tenerife_disaster"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Tenerife 1977: The 583-Fatality Disaster That Rewrote Cockpit Psychology Forever",
                "tier": "Tier 1: Lift Physics & The Pioneering Flight Era",
                "angle": "beginner_explainers",
                "slug": "tenerife_airport_disaster_1977_klm_pan_am_collision_cockpit_crm",
                "question": "How did dense fog, simultaneous radio heterodyne squeals, and hierarchical cockpit deference cause two Boeing 747s to collide on a single runway?",
                "key_focus": "Captain Jacob van Zanten's departure pressure, Dutch radio phraseology confusion ('We are now at takeoff'), Pan Am Flight 1736 missed exit, birth of modern CRM.",
                "reason": "Flagship launch episode; the deadliest accident in aviation history and the watershed moment for airline safety culture."
            },
            {
                "id": 2,
                "title": "How Wings Actually Generate Lift: Debunking the High School Bernoulli Myth",
                "tier": "Tier 1: Lift Physics & The Pioneering Flight Era",
                "angle": "how_it_works",
                "slug": "how_airplanes_fly_lift_physics_bernoulli_vs_newton_downwash",
                "question": "Why does the common 'equal transit time' school explanation fail completely to explain how stunt airplanes can fly upside down?",
                "key_focus": "Newton's third law and wing downwash momentum, circulation and Kutta condition, angle of attack stall limits, boundary layer airflow.",
                "reason": "Clarifies the single most misunderstood physics concept in aerodynamic science."
            },
            {
                "id": 3,
                "title": "Kitty Hawk 1903: How Two Bicycle Mechanics Solved the 3-Axis Control Riddle",
                "tier": "Tier 1: Lift Physics & The Pioneering Flight Era",
                "angle": "history_origins",
                "slug": "wright_brothers_kitty_hawk_1903_three_axis_control_and_wind_tunnel",
                "question": "Why did previous aviation pioneers die in crashes while Orville and Wilbur Wright mastered flight using homebuilt bicycle wind tunnels and wing warping?",
                "key_focus": "Pitch, roll, and yaw 3-axis flight control patent, wind tunnel lift tables correcting Lilienthal's errors, Charles Taylor's custom aluminum engine block.",
                "reason": "The defining technological breakthrough that inaugurated the age of powered flight."
            },
            {
                "id": 4,
                "title": "The Pitot Tube and the Six Pack: How Analog Cockpit Instruments Read the Sky",
                "tier": "Tier 1: Lift Physics & The Pioneering Flight Era",
                "angle": "behind_the_scenes",
                "slug": "analog_cockpit_six_pack_instruments_pitot_static_system_and_gyros",
                "question": "How do ram air pressure and miniature spinning gyroscopes tell a pilot their airspeed, altitude, and artificial horizon in pitch-black cloud cover?",
                "key_focus": "Pitot-static tube pressure differentials, aneroid wafer altitude contraction, rigidity in space and precession gyroscopic laws, instrument cross-check scan.",
                "reason": "The fundamental engineering hardware behind blind instrument flight (IFR)."
            },
            {
                "id": 5,
                "title": "Breaking the Sound Barrier: Chuck Yeager, Glamorous Glennis, and the Mach 1 Shockwave",
                "tier": "Tier 1: Lift Physics & The Pioneering Flight Era",
                "angle": "famous_examples",
                "slug": "chuck_yeager_bell_x1_breaking_sound_barrier_1947_mach_one",
                "question": "Why did wartime aircraft disintegrate when approaching 700 mph, and how did a rocket-powered bullet with an all-moving tailplane conquer compressibility?",
                "key_focus": "Transonic shockwave formation and shock stall, Yeager flying with broken ribs using a broom handle, all-flying horizontal stabilizer invention.",
                "reason": "The landmark frontier of high-speed aerodynamics unlocking supersonic flight."
            },
            {
                "id": 6,
                "title": "The Boeing 707: The Jet Airliner That Shrank the Planet and Did a Barrel Roll",
                "tier": "Tier 2: The Sound Barrier, Jet Age & Jumbo Era",
                "angle": "history_origins",
                "slug": "boeing_707_dash_80_tex_johnston_barrel_roll_and_jet_age_dawn",
                "question": "How did test pilot Tex Johnston shock airline executives by barrel-rolling a 100-ton jet prototype over Seattle's Lake Washington to sell the Jet Age?",
                "key_focus": "Dash 80 1-G positive maneuver, Pratt & Whitney JT3C turbojets, swept-wing 35-degree cruise efficiency, replacing piston propellers overnight.",
                "reason": "The birth of modern mass commercial airline travel."
            },
            {
                "id": 7,
                "title": "The Boeing 747: The Queen of the Skies and the Billion-Dollar Gamble That Saved Boeing",
                "tier": "Tier 2: The Sound Barrier, Jet Age & Jumbo Era",
                "angle": "case_studies",
                "slug": "boeing_747_queen_of_the_skies_joe_sutter_everett_factory_gamble",
                "question": "How did lead engineer Joe Sutter design the world's first wide-body jumbo jet in just 29 months while Boeing pushed itself to the brink of bankruptcy?",
                "key_focus": "High-bypass turbofan engines, constructing the world's largest building by volume in Everett, nose cargo door design, democratizing global long-haul travel.",
                "reason": "The most beloved, iconic commercial airliner ever built."
            },
            {
                "id": 8,
                "title": "Concorde: The 1,350-MPH Engineering Triumph That Arrived 30 Years Too Early",
                "tier": "Tier 2: The Sound Barrier, Jet Age & Jumbo Era",
                "angle": "behind_the_scenes",
                "slug": "concorde_supersonic_airliner_mach_two_engineering_and_economic_demise",
                "question": "How did British and French engineers pump fuel between trim tanks in flight to compensate for supersonic center-of-lift migration at Mach 2?",
                "key_focus": "Ogival delta wing aerodynamics, droop snoot cockpit visibility visor, Rolls-Royce Olympus 593 reheat afterburners, sonic boom ban and fuel economics.",
                "reason": "The technological pinnacle of civilian supersonic luxury and aesthetic elegance."
            },
            {
                "id": 9,
                "title": "The de Havilland Comet: Square Windows and the Deadly Lessons of Metal Fatigue",
                "tier": "Tier 2: The Sound Barrier, Jet Age & Jumbo Era",
                "angle": "dark_secrets",
                "slug": "de_havilland_comet_crashes_square_windows_metal_fatigue_discovery",
                "question": "Why did the world's first commercial jetliner suddenly tear apart in mid-air in 1954, and how did water tank testing reveal stress concentrations in window corners?",
                "key_focus": "Cabin pressurization cycling stress, water submersion fatigue rig tests at Farnborough, why all airplane windows are oval/round today.",
                "reason": "The foundational forensic breakthrough that taught aerospace engineers how to build safe pressurized hulls."
            },
            {
                "id": 10,
                "title": "The Tupolev Tu-144 'Concordski': The Stolen Blueprints and the Paris Air Show Crash",
                "tier": "Tier 2: The Sound Barrier, Jet Age & Jumbo Era",
                "angle": "hidden_stories",
                "slug": "tupolev_tu144_concordski_paris_air_show_1973_crash_and_espionage",
                "question": "Did Soviet intelligence steal Concorde plans to build the world's first supersonic passenger jet, and why did it disintegrate in front of 250,000 spectators in Paris?",
                "key_focus": "KGB operation Brunnhilde espionage, retractable front canards, 1973 Paris Air Show crash dodging a French Mirage jet, unreliability as a mail carrier.",
                "reason": "Cold War aerospace espionage drama paired with tragic engineering compromise."
            },
            {
                "id": 11,
                "title": "Aloha Airlines Flight 243: The Convertible Boeing 737 at 24,000 Feet",
                "tier": "Tier 3: Air Disaster Forensics & Safety Systems",
                "angle": "case_studies",
                "slug": "aloha_airlines_flight_243_explosive_decompression_landing",
                "question": "How did Captain Robert Schornstheimer land a Boeing 737 with an 18-foot section of the cabin roof ripped clean off over the Pacific Ocean?",
                "key_focus": "Multi-site fatigue damage (MSD) in lap joints, salty humid Hawaiian coastal corrosion, flight attendant Clarabelle Lansing tragedy, miraculous emergency touchdown at Kahului.",
                "reason": "One of the greatest piloting feats in history and a landmark study in structural maintenance cycles."
            },
            {
                "id": 12,
                "title": "Delta Flight 191 and Microbursts: How a Invisible Weather Monster Revolutionized Radars",
                "tier": "Tier 3: Air Disaster Forensics & Safety Systems",
                "angle": "scientific_breakthroughs",
                "slug": "delta_flight_191_dallas_microburst_windshear_doppler_radar",
                "question": "What happens when a 100-mph downdraft of rain-cooled air strikes the runway threshold right as an airliner slows to landing speed?",
                "key_focus": "Dr. Ted Fujita's microburst discovery, rapid headwind-to-tailwind airspeed collapse, mandatory airborne windshear warning radar installations.",
                "reason": "Saved thousands of lives by eliminating the single deadliest weather threat in commercial aviation."
            },
            {
                "id": 13,
                "title": "Cockpit Resource Management: How Eliminating Captain Authoritarianism Saved Flying",
                "tier": "Tier 3: Air Disaster Forensics & Safety Systems",
                "angle": "psychological_tricks",
                "slug": "cockpit_resource_management_crm_aviation_safety_communication",
                "question": "Why did co-pilots in the 1970s watch their captains fly into terrain rather than speak up, and how did NASA and United Airlines fix the hierarchy?",
                "key_focus": "United Flight 173 Portland fuel starvation crash, steep authority gradients, assertive challenge-response protocols (Two-Challenge Rule), modern airline crew training.",
                "reason": "The psychological revolution that transformed commercial flying into the safest mode of transport on Earth."
            },
            {
                "id": 14,
                "title": "Air France Flight 447: The Frozen Pitot Tubes and the Deep Ocean Stall",
                "tier": "Tier 3: Air Disaster Forensics & Safety Systems",
                "angle": "unsolved_mysteries",
                "slug": "air_france_447_rio_paris_atlantic_crash_frozen_pitot_tubes_stall",
                "question": "How did an ultra-modern Airbus A330 fall 38,000 feet into the pitch-black mid-Atlantic while the pilots held the side-stick pulled back the entire time?",
                "key_focus": "Ice crystal blockage in Thales pitot probes, autopilot disconnect into Alternate Law, dual-input side-stick design debates, deep ocean recovery at 13,000 feet.",
                "reason": "The ultimate cautionary study on human-automation interface failure in modern computerized cockpits."
            },
            {
                "id": 15,
                "title": "The Black Box: Inside the Indestructible Orange Flight Data Recorders",
                "tier": "Tier 3: Air Disaster Forensics & Safety Systems",
                "angle": "how_it_works",
                "slug": "black_box_flight_data_recorder_cockpit_voice_recorder_engineering",
                "question": "How does a brightly painted orange cylinder withstand 3,400 G-forces of impact, 1,100°C kerosene fires, and the crushing pressure of the ocean floor?",
                "key_focus": "David Warren's 1953 Australian invention, Flight Data Recorder (FDR) vs Cockpit Voice Recorder (CVR), titanium armor and thermal insulation, underwater locator beacons (ULBs).",
                "reason": "The unsung technological hero responsible for diagnosing every mystery and driving 70 years of safety improvements."
            },
            {
                "id": 16,
                "title": "SR-71 Blackbird: The Spyplane That Leaked Fuel on the Runway to Fly at Mach 3.2",
                "tier": "Tier 4: Stealth, Scramjets & Autonomous Flight",
                "angle": "behind_the_scenes",
                "slug": "sr71_blackbird_lockheed_skunk_works_kelly_johnson_titanium_mach_3",
                "question": "Why was the SR-71 built with loose-fitting titanium panels that leaked fuel until aerodynamic friction at 2,000 mph heated the airframe to 600°F?",
                "key_focus": "Kelly Johnson and Lockheed Skunk Works, Soviet CIA titanium procurement shell companies, Pratt & Whitney J58 continuous-bleed turbojet/ramjet engines, evading 4,000 SAM missiles.",
                "reason": "The supreme, unmatched engineering wonder of the Cold War and the fastest air-breathing manned jet ever flown."
            },
            {
                "id": 17,
                "title": "The B-2 Spirit and Radar Cross-Section: How a Flying Wing Becomes as Small as an Insect",
                "tier": "Tier 4: Stealth, Scramjets & Autonomous Flight",
                "angle": "scientific_breakthroughs",
                "slug": "b2_spirit_stealth_bomber_radar_cross_section_pyotr_ufimtsev",
                "question": "How does a 172-foot-wingspan nuclear bomber appear on enemy radar screens as no larger than a bumblebee or a marble?",
                "key_focus": "Pyotr Ufimtsev's diffraction equations, continuous curvature and radar-absorbent materials (RAM), serpentine engine intake ducts, fly-by-wire stability on tailless wings.",
                "reason": "The foundational breakthrough in modern stealth military aerospace technology."
            },
            {
                "id": 18,
                "title": "The Scramjet Frontier: How to Light a Match in a Category 5 Hurricane at Mach 7",
                "tier": "Tier 4: Stealth, Scramjets & Autonomous Flight",
                "angle": "how_it_works",
                "slug": "scramjet_hypersonic_propulsion_supersonic_combustion_ramjet",
                "question": "Why do conventional jet turbines melt at hypersonic speeds, and how does a Supersonic Combustion Ramjet sustain combustion in milliseconds?",
                "key_focus": "Ram compression vs supersonic flow deceleration, X-43A and X-51 Waverider test flights, thermal barrier materials, hypersonic glide weapons arms race.",
                "reason": "The current frontier of high-speed propulsion bridging atmospheric flight and orbital spaceflight."
            },
            {
                "id": 19,
                "title": "The Boeing 737 MAX Crisis: MCAS, Angle-of-Attack Sensors, and Regulatory Capture",
                "tier": "Tier 4: Stealth, Scramjets & Autonomous Flight",
                "angle": "ethical_debates",
                "slug": "boeing_737_max_mcas_crisis_lion_air_ethiopian_faa_investigation",
                "question": "How did software designed to mimic older flight characteristics rely on a single fragile angle-of-attack sensor, causing two crashes and a worldwide grounding?",
                "key_focus": "LEAP-1B engine placement pitching moment, Maneuvering Characteristics Augmentation System (MCAS) secrecy, FAA delegated certification oversight, 20-month fleet grounding.",
                "reason": "The definitive modern case study in software architecture, corporate pressure, and aeronautical safety ethics."
            },
            {
                "id": 20,
                "title": "eVTOL and Pilotless Commercial Airliners: The Sky in 2040",
                "tier": "Tier 4: Stealth, Scramjets & Autonomous Flight",
                "angle": "future_predictions",
                "slug": "evtol_electric_aviation_autonomous_airliners_future_of_flight",
                "question": "Will electric vertical takeoff air taxis replace highway commutes, and will passenger jets ever fly safely without a human in the cockpit?",
                "key_focus": "Distributed electric propulsion (DEP) battery density limits, Joby and Archer urban certification, AI autonomy redundancy vs passenger psychological trust.",
                "reason": "The next major industrial revolution poised to transform aviation over the next two decades."
            }
        ],
        "trending": [
            {
                "id": 1,
                "title": "Why Don't Commercial Airplanes Have Parachutes for All Passengers?",
                "angle": "beginner_explainers",
                "hook": "It seems so obvious: why can't airlines put a parachute under every seat in case of an engine flameout? The surprising aerodynamics and military realities.",
                "target_audience": "Curious flyers, avgeeks, everyday travelers",
                "estimated_views": "3.5M - 6.2M",
                "production_effort": "Low",
                "why_it_works": "Universal everyday question answered with clear aviation physics and logistics."
            },
            {
                "id": 2,
                "title": "What Actually Happens When a Bird Hits an Airplane Jet Engine at 200 MPH?",
                "angle": "scientific_breakthroughs",
                "hook": "Titanium fan blades spin at 10,000 RPM. Here is the frozen chicken cannon test aerospace engineers use to certify engine containment rings.",
                "target_audience": "Engineering nerds, travelers, aviation enthusiasts",
                "estimated_views": "2.4M - 4.5M",
                "production_effort": "Medium",
                "why_it_works": "Visceral, high-speed camera footage interest with fascinating engineering testing methods."
            },
            {
                "id": 3,
                "title": "The Ghost Flights: How 3 Helios Pilots and 118 Passengers Fell Asleep at 35,000 Feet",
                "angle": "case_studies",
                "hook": "A ground engineer left one selector switch on 'Manual'. When Greek F-16 fighters intercepted the Boeing 737, the captain's seat was empty and passengers were lifeless.",
                "target_audience": "True crime and mystery buffs, avgeeks, documentary viewers",
                "estimated_views": "4.0M - 7.2M",
                "production_effort": "Medium",
                "why_it_works": "Chilling real-world hypoxia mystery that plays like a psychological thriller."
            },
            {
                "id": 4,
                "title": "Why Airline Food Tastes So Bland (It's Not the Airline's Fault)",
                "angle": "psychological_tricks",
                "hook": "At 35,000 feet, dry pressurized air and white noise background hum deaden 30% of your salt and sweet taste buds. How airlines compensate with umami.",
                "target_audience": "Casual travelers, foodies, biology nerds",
                "estimated_views": "1.9M - 3.6M",
                "production_effort": "Low",
                "why_it_works": "Fun, surprising biological insight that everyone who has flown can relate to."
            },
            {
                "id": 5,
                "title": "The Craziest Emergency Landing Ever: Gimli Glider 767",
                "angle": "famous_examples",
                "hook": "Air Canada ran out of fuel at 41,000 feet because someone confused pounds with kilograms. The captain was an amateur glider pilot who side-slipped a 130-ton jet onto a race track.",
                "target_audience": "Avgeeks, sports car fans, aviation documentary viewers",
                "estimated_views": "3.1M - 5.6M",
                "production_effort": "Medium",
                "why_it_works": "Pure thrilling piloting heroism and a metric conversion blunder."
            },
            {
                "id": 6,
                "title": "How Pilots Dump 20 Tons of Fuel in Minutes Without It Reaching the Ground",
                "angle": "how_it_works",
                "hook": "When a heavy long-haul flight has an immediate emergency after takeoff, it must dump tens of thousands of gallons of kerosene over your neighborhood. Why doesn't it rain jet fuel?",
                "target_audience": "Environmentalists, travelers, curious minds",
                "estimated_views": "1.8M - 3.3M",
                "production_effort": "Low",
                "why_it_works": "Explains fuel jettison nozzle physics and high-altitude evaporation."
            },
            {
                "id": 7,
                "title": "Can a Passenger with Zero Flight Experience Actually Land a Modern Airliner?",
                "angle": "actionable_challenges",
                "hook": "If both pilots pass out over the Atlantic, can you grab the headset, talk to air traffic control, and let the autoland computer save you?",
                "target_audience": "Travelers, gamers, flight simulator fans",
                "estimated_views": "3.8M - 6.8M",
                "production_effort": "Medium",
                "why_it_works": "The ultimate universal airplane nightmare and wish-fulfillment scenario."
            }
        ]
    },
    "048_maritime": {
        "id": "048",
        "slug": "maritime",
        "title": "Maritime",
        "category": "Transport_Engineering",
        "audience": "Nautical Historians, Ocean Liner Buffs, Naval Architects, Deep Sea Salvage Seekers (Global)",
        "progression": [
            ("Tier 1: Buoyancy Physics, Hull Metacenters & Celestial Navigation (Scratch / Beginner)",
             "Archimedes principle, center of gravity vs center of buoyancy, metacentric height stability, sextant sighting, and the marine chronometer."),
            ("Tier 2: The Golden Age of Liners, Dreadnoughts & Epic Naval Clashes (Intermediate)",
             "The sinking of RMS Titanic (1912), Lusitania torpedo attack, Battle of Midway carrier doctrine, and the hunt for the battleship Bismarck."),
            ("Tier 3: Deep Submergence Engineering, Containerization & Rogue Waves (Upper Intermediate)",
             "USS Thresher crush depth disaster, Malcolm McLean's intermodal shipping container revolution, non-linear rogue wave fluid dynamics, and pirate lane defenses."),
            ("Tier 4: Ultra Large Container Vessels, Nuclear Propulsion & Deep Sea Robotics (Advanced / Expert)",
             "Ever Given Suez canal hydrodynamics (bank effect), nuclear submarine naval propulsion shielding, autonomous zero-emission container ships, and deep salvage ROVs.")
        ],
        "flagship": {
            "title": "The Sinking of the Bismarck: How a 1930s Canvas Biplane Crippled the Mightiest Warship in Europe",
            "angle": "beginner_explainers",
            "slug": "048_maritime_beginner_explainers_sinking_of_the_bismarck"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Sinking of the Bismarck: How a 1930s Canvas Biplane Crippled the Mightiest Warship in Europe",
                "tier": "Tier 1: Buoyancy Physics & Celestial Navigation",
                "angle": "beginner_explainers",
                "slug": "sinking_of_the_bismarck_1941_swordfish_biplane_torpedo_rudder_hit",
                "question": "How did an obsolete open-cockpit Fairey Swordfish biplane jam the dual rudders of Nazi Germany's 50,000-ton dreadnought, sealing its doom in the North Atlantic?",
                "key_focus": "Sinking of HMS Hood at the Denmark Strait, radar evasion, Royal Navy carrier strike from Ark Royal, Bismarck circling into the guns of King George V and Rodney.",
                "reason": "Flagship launch episode; the dramatic zenith of battleship naval warfare and asymmetrical aerial torpedo tactics."
            },
            {
                "id": 2,
                "title": "Archimedes and Metacentric Height: Why Massive 200,000-Ton Ships Float and Don't Capsize",
                "tier": "Tier 1: Buoyancy Physics & Celestial Navigation",
                "angle": "how_it_works",
                "slug": "ship_stability_buoyancy_physics_metacentric_height_and_heeling",
                "question": "How does a steel container ship carrying 24,000 heavy boxes maintain upright stability instead of rolling upside down in stormy seas?",
                "key_focus": "Center of buoyancy vs center of gravity, metacentric height (GM) calculations, righting moment lever arm (GZ curve), free surface liquid effect hazards.",
                "reason": "The foundational naval architecture physics governing every surface vessel on Earth."
            },
            {
                "id": 3,
                "title": "John Harrison's Clock: How a Carpenter Solved the Longitude Riddle and Saved Thousands of Sailors",
                "tier": "Tier 1: Buoyancy Physics & Celestial Navigation",
                "angle": "history_origins",
                "slug": "longitude_problem_john_harrison_h4_marine_chronometer_navigation",
                "question": "Why did ships routinely wreck on invisible reefs for centuries until an uneducated clockmaker built an anti-friction pocket watch immune to sea salt and motion?",
                "key_focus": "Scilly naval disaster of 1707, Board of Longitude prize competition, Nevil Maskelyne's lunar distance rivalry, the genius of the H4 marine chronometer.",
                "reason": "The technological masterstroke that enabled global ocean navigation and empire building."
            },
            {
                "id": 4,
                "title": "The Sextant and the Stars: How Sailors Plotted Their Position with a Brass Instrument and a Horizon",
                "tier": "Tier 1: Buoyancy Physics & Celestial Navigation",
                "angle": "behind_the_scenes",
                "slug": "how_a_sextant_works_celestial_navigation_sight_reduction_tables",
                "question": "How does measuring the angle between the noon sun or Polaris and the ocean horizon give a navigator their exact latitude on a blank ocean?",
                "key_focus": "Double-reflection optical mirrors, index error calibration, sight reduction tables and nautical almanac, emergency GPS-denied backup navigation today.",
                "reason": "The ancient, romantic mathematical art of reading the sky across thousands of miles of empty water."
            },
            {
                "id": 5,
                "title": "The Vasa Disaster (1628): The Swedish Warship That Capsized 20 Minutes into Her Maiden Voyage",
                "tier": "Tier 1: Buoyancy Physics & Celestial Navigation",
                "angle": "famous_examples",
                "slug": "vasa_warship_disaster_1628_stockholm_harbor_stability_failure",
                "question": "Why did King Gustavus Adolphus' brand new double-gun-deck flagship topple over and sink in Stockholm harbor before even leaving sight of the docks?",
                "key_focus": "Top-heavy hull geometry, lower gun ports flooded by a gentle gust of wind, 333-year preservation in brackish Baltic mud, salvage intact in 1961.",
                "reason": "The supreme historical lesson in catastrophic engineering compromise driven by royal ego."
            },
            {
                "id": 6,
                "title": "Titanic (1912): The 6 Water-Tight Bulkhead Myth and the Physics of the Sinking",
                "tier": "Tier 2: The Golden Age of Liners & Naval Clashes",
                "angle": "myths_vs_facts",
                "slug": "rms_titanic_1912_iceberg_collision_watertight_bulkheads_physics",
                "question": "Why was the 'unsinkable' liner fatally doomed the moment the iceberg grazed the forward five compartments, and did high-sulfur brittle steel cause it?",
                "key_focus": "Spillover of water over transverse bulkhead tops, low-temperature brittle rivet shearing metallurgy, Harland and Wolff shipyard logistics, California ship mystery.",
                "reason": "The most famous shipwreck in human history scrutinized with modern naval forensic analysis."
            },
            {
                "id": 7,
                "title": "The Lusitania Torpedo (1915): The Second Explosion That Accelerated America's Entry into WWI",
                "tier": "Tier 2: The Golden Age of Liners & Naval Clashes",
                "angle": "hidden_stories",
                "slug": "rms_lusitania_sinking_1915_u20_torpedo_and_second_explosion_mystery",
                "question": "Why did the 31,000-ton Cunard ocean liner sink in an astonishing 18 minutes from a single German torpedo, and what caused the massive secondary blast?",
                "key_focus": "U-20 Captain Walther Schwieger's logbook, longitudinal bunker coal dust explosion vs contraband munitions debate, lifeboats flipping during severe starboard list.",
                "reason": "A geopolitical and maritime tragedy that shifted world history toward the defeat of imperial Germany."
            },
            {
                "id": 8,
                "title": "The Battle of Midway (1942): 5 Minutes That Shattered the Imperial Japanese Navy",
                "tier": "Tier 2: The Golden Age of Liners & Naval Clashes",
                "angle": "case_studies",
                "slug": "battle_of_midway_1942_five_minutes_dive_bombers_aircraft_carrier_doctrine",
                "question": "How did American SBD Dauntless dive bombers arriving simultaneously from high clouds turn three Japanese aircraft carriers into burning hulks in 300 seconds?",
                "key_focus": "Hypo station codebreakers (Joe Rochefort 'AF' water plant trap), Admiral Nagumo's fateful rearming order (torpedoes to bombs), end of the battleship supremacy era.",
                "reason": "The turning point of the Pacific War and the birth of carrier-centric naval doctrine."
            },
            {
                "id": 9,
                "title": "The Mary Celeste: The Ghost Ship Found Sailing in Perfect Order with Zero Crew",
                "tier": "Tier 2: The Golden Age of Liners & Naval Clashes",
                "angle": "unsolved_mysteries",
                "slug": "mary_celeste_ghost_ship_1872_abandonment_alcohol_vapor_theory",
                "question": "Why did Captain Benjamin Briggs, his wife, daughter, and 7 seasoned sailors abandon a seaworthy brigantine with 6 months of provisions and untouched cargo?",
                "key_focus": "Industrial denatured alcohol cargo pressure rupture, sea-quake sonic shock hypothesis, absence of violence or piracy evidence, the eternal maritime enigma.",
                "reason": "The quintessential maritime ghost mystery that has baffled investigators for over 150 years."
            },
            {
                "id": 10,
                "title": "The Edmund Fitzgerald: The 29 Men Swallowed by Lake Superior's November Witch",
                "tier": "Tier 2: The Golden Age of Liners & Naval Clashes",
                "angle": "dark_secrets",
                "slug": "ss_edmund_fitzgerald_sinking_1975_lake_superior_rogue_waves",
                "question": "How did a 729-foot iron ore freighter vanish without a single distress call during a ferocious gale on the cold, fresh waters of Lake Superior?",
                "key_focus": "Six Fathom Shoal grounding vs rogue three-sisters wave theory, hatch cover structural failure, Gordon Lightfoot ballad cultural immortalization.",
                "reason": "The most haunting, legendary shipwreck in North American freshwater shipping history."
            },
            {
                "id": 11,
                "title": "USS Thresher (1963): The Nuclear Submarine Crush Depth Disaster That Birthed SUBSAFE",
                "tier": "Tier 3: Submarine Engineering, Containers & Rogue Waves",
                "angle": "case_studies",
                "slug": "uss_thresher_ssn593_sub_crush_depth_disaster_and_subsafe_program",
                "question": "What sequence of silver-brazed pipe failures, reactor scrams, and frozen emergency ballast blow valves sent 129 men into the abyss off Cape Cod?",
                "key_focus": "High-pressure seawater pipe rupture, condensation freezing in compressed air lines, crush depth acoustic implosion signatures, rigorous SUBSAFE QA reform.",
                "reason": "The worst submarine disaster in US Navy history that established unmatched structural safety standards."
            },
            {
                "id": 12,
                "title": "The Containerization Revolution: How Malcolm McLean's Steel Box Transformed Global Trade",
                "tier": "Tier 3: Submarine Engineering, Containers & Rogue Waves",
                "angle": "history_origins",
                "slug": "malcolm_mclean_intermodal_shipping_container_revolution_1956",
                "question": "How did a North Carolina trucker turning truck trailers into standardized 20-foot steel boxes slash port loading costs from $5.86 per ton to 16 cents?",
                "key_focus": "The Ideal X maiden voyage (1956), death of the traditional break-bulk longshoreman, ISO twistlock standardization, enabler of globalized manufacturing.",
                "reason": "The single most consequential logistical revolution in the modern world economy."
            },
            {
                "id": 13,
                "title": "Rogue Waves: How Oceanographers Proved 100-Foot Monster Waves Were Real",
                "tier": "Tier 3: Submarine Engineering, Containers & Rogue Waves",
                "angle": "scientific_breakthroughs",
                "slug": "rogue_waves_draupner_wave_1995_non_linear_schrodinger_equation",
                "question": "Why did scientists dismiss sailor tales of 80-foot vertical walls of water as drunken myths until a laser sensor on the Draupner oil rig recorded one in 1995?",
                "key_focus": "Draupner wave 84-foot laser measurement, non-linear Schrödinger equation wave packet focusing, Agulhas and Gulf Stream opposing current wave-trapping.",
                "reason": "Vindicated centuries of mariner lore and revolutionized naval architecture hull stress limits."
            },
            {
                "id": 14,
                "title": "The Malacca Strait and Gulf of Guinea: Modern High-Seas Piracy Tactics",
                "tier": "Tier 3: Submarine Engineering, Containers & Rogue Waves",
                "angle": "behind_the_scenes",
                "slug": "modern_maritime_piracy_malacca_strait_gulf_of_guinea_and_citadels",
                "question": "How do skiffs armed with RPGs hijack massive oil tankers in narrow chokepoints, and how do crews lock down in armored citadel safe rooms?",
                "key_focus": "Chokepoint maritime geography, Long Range Acoustic Devices (LRAD), razor wire perimeter defense, citadel survival tactics, armed private maritime security.",
                "reason": "Exposes the real-world operational security and asymmetric danger modern merchant mariners face daily."
            },
            {
                "id": 15,
                "title": "The Kursk Submarine Explosion (2000): The Torpedo Fuel Leak That Trapped 23 Men",
                "tier": "Tier 3: Submarine Engineering, Containers & Rogue Waves",
                "angle": "dark_secrets",
                "slug": "kursk_submarine_disaster_2000_htp_torpedo_explosion_compartment_nine",
                "question": "How did a faulty high-test peroxide (HTP) practice torpedo blast open the nose of an Oscar II nuclear submarine, and why did 23 survivors slowly suffocate in Compartment 9?",
                "key_focus": "HTP explosive decomposition chemistry, Russian Navy refusal of foreign rescue aid, Lieutenant Captain Dmitri Kolesnikov's handwritten final letter.",
                "reason": "Heartbreaking tragedy that revealed Cold War hangover pride, naval coverups, and international rescue limits."
            },
            {
                "id": 16,
                "title": "Ever Given and the Suez Canal: The Hydrodynamic Bank Effect That Paralyzed Global Trade",
                "tier": "Tier 4: Ultra Large Freighters & Deep Sea Salvage",
                "angle": "how_it_works",
                "slug": "ever_given_suez_canal_blockage_bank_effect_and_squat_physics",
                "question": "How did a 400-meter container ship get wedge-stuck across the Suez Canal, holding up $10 billion in trade per day due to Bernoulli suction against the canal walls?",
                "key_focus": "Bank effect and bank cushion hydrodynamic forces, ship squat phenomenon in shallow water, Dutch Smit Salvage dredging and high-tide refloat operation.",
                "reason": "Reveals the extreme fragility of modern maritime global supply chains and shallow-water fluid dynamics."
            },
            {
                "id": 17,
                "title": "Nuclear Marine Propulsion: How Submarines and Supercarriers Sail for 25 Years Without Refueling",
                "tier": "Tier 4: Ultra Large Freighters & Deep Sea Salvage",
                "angle": "scientific_breakthroughs",
                "slug": "naval_nuclear_propulsion_pressurized_water_reactor_admiral_rickover",
                "question": "How did Admiral Hyman G. Rickover create a naval nuclear program that has sailed over 150 million miles without a single reactor casualty?",
                "key_focus": "Pressurized Water Reactors (PWR), highly enriched uranium cores lasting 25+ years, silent steam turbine propulsion, zero-defect engineering culture.",
                "reason": "The pinnacle of marine power generation and deep endurance military naval engineering."
            },
            {
                "id": 18,
                "title": "Deep Sea Salvage Robotics: Operating at 20,000 Feet Below the Surface",
                "tier": "Tier 4: Ultra Large Freighters & Deep Sea Salvage",
                "angle": "behind_the_scenes",
                "slug": "deep_sea_salvage_rov_robotics_submersibles_alvin_and_nautile",
                "question": "How do fiber-optic tethered Remotely Operated Vehicles (ROVs) withstand 10,000 PSI of water pressure to recover flight recorders and sunken gold?",
                "key_focus": "Syntactic foam buoyancy blocks, hydraulic manipulators, subsea acoustic positioning grids (USBL), finding Air France 447 and SS Central America.",
                "reason": "Fascinating breakdown of high-pressure robotics operating in the most hostile environment on Earth."
            },
            {
                "id": 19,
                "title": "Ghost Ships and Abandoned Fleets: The Strange World of Shipbreaking in Chittagong and Alang",
                "tier": "Tier 4: Ultra Large Freighters & Deep Sea Salvage",
                "angle": "cultural_impact",
                "slug": "shipbreaking_beaches_alang_india_chittagong_bangladesh_economics",
                "question": "Where do giant 300,000-ton steel supertankers go to die, and how do thousands of barefoot workers dismantle them by hand on tidal mudflats?",
                "key_focus": "Beach grounding at full speed on spring tides, asbestos and heavy metal pollution, scrap steel recycling economics, worker safety and international conventions.",
                "reason": "The gritty, dangerous end-of-life cycle for the world's commercial maritime fleet."
            },
            {
                "id": 20,
                "title": "Autonomous Cargo Ships and Green Ammonia: The Maritime Industry in 2050",
                "tier": "Tier 4: Ultra Large Freighters & Deep Sea Salvage",
                "angle": "future_predictions",
                "slug": "autonomous_container_ships_green_ammonia_wind_wings_future_fleet",
                "question": "Will computer-piloted cargo ships powered by green hydrogen or giant rigid wind sails replace diesel-burning container vessels across the oceans?",
                "key_focus": "Yara Birkeland crewless electric ship, rigid wing-sail aerodynamics (Flettner rotors / Oceanbird), IMO decarbonization targets, port automation.",
                "reason": "The ecological and autonomous technological transformation revolutionizing global shipping."
            }
        ],
        "trending": [
            {
                "id": 1,
                "title": "Why Are Modern Ships Painted with a Giant Red Bulb Under the Waterline?",
                "angle": "how_it_works",
                "hook": "Look at the front of any massive cargo ship or cruise liner: there is a huge protruding bulb below the water. How this strange shape cuts fuel burn by 15%.",
                "target_audience": "Curious learners, engineers, travelers, maritime buffs",
                "estimated_views": "3.1M - 5.5M",
                "production_effort": "Low",
                "why_it_works": "Clear, elegant fluid mechanics explanation of wave cancellation physics."
            },
            {
                "id": 2,
                "title": "The Terrifying Phenomenon of 'The Bermuda Triangle' Finally Debunked by Science",
                "angle": "myths_vs_facts",
                "hook": "Methane gas bubbles? Alien vortexes? Magnetic anomalies? Oceanographers and insurance statistics finally explain the truth about the Bermuda Triangle.",
                "target_audience": "Mystery lovers, science geeks, documentary viewers",
                "estimated_views": "2.8M - 4.9M",
                "production_effort": "Low",
                "why_it_works": "Universal internet search staple debunked with rigorous Lloyd's of London shipping data."
            },
            {
                "id": 3,
                "title": "What Happens When a Sailor Falls Overboard in the Middle of the Pacific Ocean?",
                "angle": "survival_tips",
                "hook": "It takes miles for a mega-ship to stop. In pitch-black water with 20-foot swell, what are your actual chances of survival when nobody sees you slip?",
                "target_audience": "Thrill seekers, survival enthusiasts, cruise passengers",
                "estimated_views": "4.2M - 7.6M",
                "production_effort": "Medium",
                "why_it_works": "Visceral, terrifying nightmare scenario with practical survival protocols."
            },
            {
                "id": 4,
                "title": "Why Did the OceanGate Titan Submersible Implode in Less Than 20 Milliseconds?",
                "angle": "case_studies",
                "hook": "Carbon-fiber delamination, cyclical pressure fatigue, and 400 atmospheres of deep ocean pressure: the complete physics breakdown of the Titan implosion.",
                "target_audience": "Tech enthusiasts, engineering geeks, news followers",
                "estimated_views": "5.0M - 9.0M",
                "production_effort": "Medium",
                "why_it_works": "Massive global media consciousness and definitive materials science explanation."
            },
            {
                "id": 5,
                "title": "The $100 Million Mega-Yachts of Russian Oligarchs: Floating Fortresses with Submarines",
                "angle": "financial_breakdown",
                "hook": "Helipads that submerge into hangars, missile defense lasers, armor-plated owner suites, and private submarines: inside the world's most secretive superyachts.",
                "target_audience": "Luxury lovers, finance enthusiasts, geopolitical watchers",
                "estimated_views": "2.4M - 4.5M",
                "production_effort": "Medium",
                "why_it_works": "High curiosity factor surrounding ultra-wealth, engineering excess, and geopolitical sanctions."
            },
            {
                "id": 6,
                "title": "Point Nemo: The Most Isolated Place on Earth Where Spacecraft Go to Die",
                "angle": "hidden_stories",
                "hook": "The closest human beings to this spot in the South Pacific are the astronauts on the International Space Station orbiting 250 miles above. The spacecraft cemetery revealed.",
                "target_audience": "Space fans, geography nerds, ocean lovers",
                "estimated_views": "3.3M - 5.8M",
                "production_effort": "Low",
                "why_it_works": "Mind-bending geographic isolation and the final resting place of the Mir space station."
            },
            {
                "id": 7,
                "title": "The Deadliest Wave in History: Lituya Bay 1958 and the 1,720-Foot Tsunami",
                "angle": "famous_examples",
                "hook": "A massive rockslide in an Alaskan fjord triggered a wave taller than the Empire State Building. How a fisherman and his son rode the crest over the trees and survived.",
                "target_audience": "Disaster buffs, nature documentary fans, survival lovers",
                "estimated_views": "3.9M - 7.0M",
                "production_effort": "Medium",
                "why_it_works": "Unbelievable natural record: the tallest recorded wave in human history."
            }
        ]
    },
    "049_pirates_outlaws": {
        "id": "049",
        "slug": "pirates_outlaws",
        "title": "Pirates & Outlaws",
        "category": "Conflict_Power_Exploration",
        "audience": "True Crime Buffs, Maritime Lore Seekers, Wild West Historians, Rebellion Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Sloop Tactics, Pirate Codes & The Wild West Frontier Origins (Scratch / Beginner)",
             "The Articles of Agreement democratic pirate code, shallow-draft Caribbean sloops, careening hull mechanics, and frontier colts & stagecoaches."),
            ("Tier 2: The Infamous Captains & Bandit Gangs (Intermediate)",
             "Blackbeard's Queen Anne's Revenge, Ching Shih's 70,000-pirate Red Flag Fleet, Billy the Kid and the Lincoln County War, and Jesse James' James-Younger Gang."),
            ("Tier 3: Outlaw Havens, Criminal Economics & The Rise of Law Enforcement (Upper Intermediate)",
             "The Nassau pirate republic (1706-1718), Port Royal's sinful collapse, Allan Pinkerton's national detective agency, and the 1930s Public Enemies era (Dillinger, Bonnie & Clyde)."),
            ("Tier 4: The Outlaw Antihero Myth, Modern Somali Piracy & Organized Smuggling Syndicates (Advanced / Expert)",
             "The romanticization of outlaws in popular culture, the 2009 Maersk Alabama capture, Gulf of Guinea high-seas bunkering, and dark-web digital contraband syndicates.")
        ],
        "flagship": {
            "title": "Ching Shih: The Brothel Madam Who Commanded 1,800 Pirate Ships and Defeated the Qing Empire",
            "angle": "beginner_explainers",
            "slug": "049_pirates_outlaws_beginner_explainers_ching_shih"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Ching Shih: The Brothel Madam Who Commanded 1,800 Pirate Ships and Defeated the Qing Empire",
                "tier": "Tier 1: Sloop Tactics, Pirate Codes & Frontier Origins",
                "angle": "beginner_explainers",
                "slug": "ching_shih_madame_ching_red_flag_fleet_commander_history",
                "question": "How did a former Cantonese courtesan command 70,000 pirates in 1,800 armed junks, smash the Chinese imperial navy, and negotiate full amnesty with her plunder intact?",
                "key_focus": "The Red Flag Fleet code of laws, beheading for rape/theft, defeating joint Chinese-Portuguese-British naval blockades, retiring as a wealthy casino aristocrat.",
                "reason": "Flagship launch episode; the most powerful, successful, and undefeated pirate admiral in world history."
            },
            {
                "id": 2,
                "title": "The Pirate Code: The Surprising Democracy and Health Insurance of the High Seas",
                "tier": "Tier 1: Sloop Tactics, Pirate Codes & Frontier Origins",
                "angle": "how_it_works",
                "slug": "the_pirate_code_articles_of_agreement_democracy_and_disability_pay",
                "question": "Why did 18th-century pirate ships practice radical direct democracy, equal voting rights, racial integration, and worker disability compensation 150 years before governments?",
                "key_focus": "Bartholomew Roberts' 11 Articles of Agreement, quartermaster checks on captain power, fixed payouts for loss of eyes/limbs (the origin of eye patches and peg legs).",
                "reason": "Shatters Hollywood myths and reveals the proto-democratic social revolution aboard outlaw vessels."
            },
            {
                "id": 3,
                "title": "The Caribbean Sloop: The Ferrari of the 18th-Century Spanish Main",
                "tier": "Tier 1: Sloop Tactics, Pirate Codes & Frontier Origins",
                "angle": "behind_the_scenes",
                "slug": "jamaica_sloop_pirate_vessels_shallow_draft_and_fore_and_aft_rigging",
                "question": "Why did pirates prefer small 60-foot Bermuda and Jamaica sloops over massive galleons when hunting merchantmen?",
                "key_focus": "Fore-and-aft sail rigging sailing into the wind, shallow 8-foot draft hiding over sandbars and mangrove swamps, careening hulls to scrape shipworms.",
                "reason": "The naval tactical engine that enabled pirates to outrun and outmaneuver royal naval frigates."
            },
            {
                "id": 4,
                "title": "Blackbeard's Reign of Terror: Slow-Burning Matches in the Beard and Psychological Warfare",
                "tier": "Tier 1: Sloop Tactics, Pirate Codes & Frontier Origins",
                "angle": "famous_examples",
                "slug": "blackbeard_edward_teach_queen_annes_revenge_and_oracoke_inlet",
                "question": "How did Edward Teach capture 40 ships without killing a single captive by turning himself into a smoking demonic apparition of pure dread?",
                "key_focus": "Hemp cannon slow-matches braided under his tricorn hat, Queen Anne's Revenge flagship, the Charleston harbor blockade, Robert Maynard's bloody ambush at Ocracoke.",
                "reason": "The quintessential embodiment of psychological terror and branding in pirate history."
            },
            {
                "id": 5,
                "title": "Anne Bonny and Mary Read: The Fiercest Women of the Golden Age",
                "tier": "Tier 1: Sloop Tactics, Pirate Codes & Frontier Origins",
                "angle": "hidden_stories",
                "slug": "anne_bonny_mary_read_calico_jack_rackham_female_pirates",
                "question": "How did two disguised women aboard Calico Jack's sloop become the only fighters left standing on deck when British navy hunters boarded their drunken crew?",
                "key_focus": "Disguised male identities, Calico Jack Rackham's capture, 'Pleading their bellies' (pregnancy trial reprieve), Anne's scathing final words to Jack in prison.",
                "reason": "Defiant and extraordinary saga of female rebellion against strict 18th-century social caste."
            },
            {
                "id": 6,
                "title": "The Republic of Pirates: How Nassau Became an Outlaw Haven for 1,000 Marauders",
                "tier": "Tier 2: Infamous Captains & Bandit Gangs",
                "angle": "history_origins",
                "slug": "republic_of_pirates_nassau_new_providence_woodes_rogers_pardon",
                "question": "How did a bankrupt Caribbean island become a lawless pirate fortress governed by Benjamin Hornigold, Charles Vane, and Blackbeard from 1706 to 1718?",
                "key_focus": "New Providence harbor geography, the Flying Gang brotherhood, King George I's Royal Act of Grace pardon, Woodes Rogers' iron-fisted cleanup.",
                "reason": "The real historical inspiration for pirate fiction, exploring the rise and fall of an outlaw utopian republic."
            },
            {
                "id": 7,
                "title": "Billy the Kid: 21 Deaths or 4? The Real Bloodshed of the Lincoln County War",
                "tier": "Tier 2: Infamous Captains & Bandit Gangs",
                "angle": "myths_vs_facts",
                "slug": "billy_the_kid_william_h_bonney_lincoln_county_war_pat_garrett",
                "question": "Was Henry McCarty a cold-blooded sociopathic killer who shot 21 men, or a charming, bilingual youth caught in an Irish-British merchant monopoly turf war?",
                "key_focus": "The Regulators vs the Murphy-Dolan faction, Tunstall assassination catalyst, Pat Garrett's midnight shooting at Fort Sumner, dime novel myth-making.",
                "reason": "Deconstructs the most romanticized outlaw legend of the American frontier."
            },
            {
                "id": 8,
                "title": "Jesse James and the James-Younger Gang: Confederate Guerrillas Turned Bank Robbers",
                "tier": "Tier 2: Infamous Captains & Bandit Gangs",
                "angle": "dark_secrets",
                "slug": "jesse_james_james_younger_gang_confederate_bushwhackers_northfield_raid",
                "question": "How did post-Civil War Confederate guerrilla vengeance spawn America's first peacetime daylight bank and train robbery spree?",
                "key_focus": "Bloody Bill Anderson bushwhacker roots, John Newman Edwards newspaper Robin Hood propaganda, Northfield Minnesota bank raid disaster, Robert Ford's betrayal.",
                "reason": "Analyzes how brutal civil war trauma transformed into organized frontier banditry."
            },
            {
                "id": 9,
                "title": "Port Royal: The 'Wickedest City on Earth' That Slid into the Sea",
                "tier": "Tier 2: Infamous Captains & Bandit Gangs",
                "angle": "case_studies",
                "slug": "port_royal_jamaica_1692_earthquake_wickedest_city_liquefaction",
                "question": "Did divine wrath really swallow the Caribbean's pirate capital in 1692, or did sand soil liquefaction drag two-thirds of the city into the harbor in 3 minutes?",
                "key_focus": "Henry Morgan's privateer haven, rum taverns and brothels economy, 1692 earthquake and tsunami, marine archaeological excavations of underwater sunken taverns.",
                "reason": "The dramatic, apocalyptic destruction of the world's most infamous pirate haven."
            },
            {
                "id": 10,
                "title": "Ned Kelly: The Australian Bushranger Who Forged a Suit of Iron Armor",
                "tier": "Tier 2: Infamous Captains & Bandit Gangs",
                "angle": "famous_examples",
                "slug": "ned_kelly_glenrowan_shootout_iron_armor_suit_australian_bushranger",
                "question": "How did an Irish-Australian rebel blacksmith plowshares into an 96-pound bulletproof plate helmet and armor suit to fight his final stand at Glenrowan?",
                "key_focus": "The Jerilderie Letter political manifesto against Victorian police tyranny, Euroa and Jerilderie bank heists, Glenrowan hotel siege, 'Such is life' final execution words.",
                "reason": "Australia's greatest cultural folk legend bridging outlaw violence and working-class colonial rebellion."
            },
            {
                "id": 11,
                "title": "Allan Pinkerton: The Birth of the Private Intelligence Agency That Hunted the Outlaws",
                "tier": "Tier 3: Havens, Economics & Rise of Law Enforcement",
                "angle": "behind_the_scenes",
                "slug": "allan_pinkerton_national_detective_agency_we_never_sleep_history",
                "question": "How did a Scottish cooper invent modern corporate espionage, undercover surveillance, the 'mug shot', and the first national detective agency?",
                "key_focus": "The 'We Never Sleep' unblinking eye logo (origin of 'Private Eye'), Kate Warne the first female detective, Baltimore Plot Lincoln protection, ruthless strike-breaking.",
                "reason": "The corporate and technological counter-revolution that brought the wild frontier to heel."
            },
            {
                "id": 12,
                "title": "Bartholomew Roberts (Black Bart): The Most Successful Pirate Who Didn't Drink Alcohol",
                "tier": "Tier 3: Havens, Economics & Rise of Law Enforcement",
                "angle": "case_studies",
                "slug": "black_bart_bartholomew_roberts_400_ships_captured_teetotaler",
                "question": "How did a strict, tea-drinking Welsh puritan capture over 400 ships across three continents in just three years?",
                "key_focus": "Dressing in scarlet damask and a diamond cross, capturing Portuguese treasure fleets in Bahia, Battle of Cape Lopez death by grapeshot, end of the Golden Age (1722).",
                "reason": "Statistically the most prolific pirate plunderer in maritime history."
            },
            {
                "id": 13,
                "title": "The Wild Bunch and the Hole-in-the-Wall: Butch Cassidy and the Sundance Kid",
                "tier": "Tier 3: Havens, Economics & Rise of Law Enforcement",
                "angle": "hidden_stories",
                "slug": "butch_cassidy_sundance_kid_wild_bunch_hole_in_the_wall_bolivia",
                "question": "How did Robert LeRoy Parker and Harry Longabaugh use relay horses and secret canyon hideouts to outrun modern telegraphs and train posses?",
                "key_focus": "Hole-in-the-Wall and Robbers Roost mountain hideouts, Fort Worth Five formal portrait mistake that exposed them, South American flight, San Vicente Bolivia shootout.",
                "reason": "The last romantic hurrah of the Old West outlaws facing modern industrial surveillance."
            },
            {
                "id": 14,
                "title": "Bonnie and Clyde: The Barrow Gang's 1930s Bloodbath Across the Dust Bowl",
                "tier": "Tier 3: Havens, Economics & Rise of Law Enforcement",
                "angle": "case_studies",
                "slug": "bonnie_and_clyde_barrow_gang_1934_gibland_ambush_ford_v8",
                "question": "Why did poverty-stricken Depression-era Americans idolize two small-time grocery store stickup kids who murdered nine law enforcement officers?",
                "key_focus": "Browning Automatic Rifle (BAR) firepower advantage, Bonnie's cigar photos and poetry, Clyde's letter praising Henry Ford's V8 engine, Frank Hamer's Louisiana highway ambush.",
                "reason": "The transition from 19th-century frontier outlaws to modern motorized Public Enemies."
            },
            {
                "id": 15,
                "title": "John Dillinger: The Wooden Gun Escape and the Biograph Theater Betrayal",
                "tier": "Tier 3: Havens, Economics & Rise of Law Enforcement",
                "angle": "famous_examples",
                "slug": "john_dillinger_wooden_gun_escape_crown_point_biograph_theater",
                "question": "How did Public Enemy No. 1 escape an 'escape-proof' Indiana county jail with a carved wooden pistol stained with black shoe polish?",
                "key_focus": "Crown Point jailbreak bravado, vault leaping theatrics, plastic surgery attempts to alter fingerprints, 'Lady in Red' Anna Sage betrayal at the Biograph Theater.",
                "reason": "The iconic criminal celebrity whose headline escapades empowered J. Edgar Hoover to forge the modern FBI."
            },
            {
                "id": 16,
                "title": "Why Did We Turn Violent Marauders into Children's Fairy Tales?",
                "tier": "Tier 4: Antihero Pop Culture & Modern Piracy",
                "angle": "cultural_impact",
                "slug": "pirate_romanticization_treasure_island_disney_antihero_mythology",
                "question": "How did Robert Louis Stevenson, Captain Charles Johnson, and Walt Disney transform syphilis-ridden oceanic killers into lovable rogues who say 'Arrr'?",
                "key_focus": "Treasure Island tropes (treasure maps with an X, parrots on shoulders, black spot), Howard Pyle illustrations creating pirate costume tropes, anti-authoritarian wish-fulfillment.",
                "reason": "A profound cultural and literary dissection of how brutal historical reality converts into global commercial folklore."
            },
            {
                "id": 17,
                "title": "The 2009 Maersk Alabama Hijacking: Somali Pirates vs Navy SEAL Snipers",
                "tier": "Tier 4: Antihero Pop Culture & Modern Piracy",
                "angle": "case_studies",
                "slug": "maersk_alabama_hijacking_2009_captain_richard_phillips_seal_team_six",
                "question": "How did illegal toxic dumping and fishing depletion off the Horn of Africa evolve into heavily armed skiff ransoms of 50,000-ton American merchant ships?",
                "key_focus": "Somali coastal socioeconomic breakdown, pirate stock exchanges in Harardhere, lifeboat standoff, SEAL Team Six simultaneous 3-sniper shot through lifeboat windows.",
                "reason": "The landmark 21st-century modern maritime piracy crisis and military hostage extraction."
            },
            {
                "id": 18,
                "title": "The Barbary Corsairs: The Mediterranean Slave Raids That Created the US Navy",
                "tier": "Tier 4: Antihero Pop Culture & Modern Piracy",
                "angle": "history_origins",
                "slug": "barbary_corsairs_ottoman_privateers_white_slavery_and_us_navy_birth",
                "question": "Why did the young United States spend 20% of its federal budget paying tribute to North African corsairs before sending the USS Constitution to Tripoli?",
                "key_focus": "Ottoman corsair galley fleets (Hayreddin Barbarossa), 1 million European captives enslaved, Naval Act of 1794 creating US Navy frigates, 'To the shores of Tripoli'.",
                "reason": "Massive historical maritime conflict that defined early American foreign policy and naval power."
            },
            {
                "id": 19,
                "title": "Gulf of Guinea Oil Bunkering: The Modern Industrial Outlaws Stealing Millions in Crude",
                "tier": "Tier 4: Antihero Pop Culture & Modern Piracy",
                "angle": "behind_the_scenes",
                "slug": "gulf_of_guinea_oil_bunkering_niger_delta_maritime_theft_syndicates",
                "question": "How do heavily armed militias in speedboats siphon millions of barrels of crude oil directly from offshore production platforms into shadow-fleet tankers?",
                "key_focus": "Niger Delta environmental devastation, clandestine STS (ship-to-ship) petroleum transfers, transnational money laundering, kidnapping for ransom vs cargo theft.",
                "reason": "The active, multi-billion-dollar modern face of organized maritime robbery and resource plunder."
            },
            {
                "id": 20,
                "title": "Digital Outlaws: From Pirate Bay and Silk Road to the Decentralized Frontier",
                "tier": "Tier 4: Antihero Pop Culture & Modern Piracy",
                "angle": "future_predictions",
                "slug": "digital_piracy_the_pirate_bay_silk_road_ross_ulbricht_crypto_outlaws",
                "question": "Is Ross Ulbricht or The Pirate Bay founders the ideological heirs of the 18th-century Nassau pirates, operating outside state sovereignty?",
                "key_focus": "BitTorrent peer-to-peer data distribution, Tor onion routing and Bitcoin anonymous transactions, state surveillance vs sovereign cyberspace philosophy.",
                "reason": "Bridges classical physical outlaws with the digital counter-culture and decentralized cryptography."
            }
        ],
        "trending": [
            {
                "id": 1,
                "title": "Why Pirates Actually Wore Eye Patches (It Had Nothing to Do with Missing Eyes)",
                "angle": "myths_vs_facts",
                "hook": "Pirates didn't wear eye patches because their eye was stabbed out. They wore them so they could storm below dark decks and instantly see in the dark without waiting 20 minutes for night vision.",
                "target_audience": "Curious learners, history buffs, trivia lovers",
                "estimated_views": "4.5M - 8.2M",
                "production_effort": "Low",
                "why_it_works": "The ultimate viral debunking of a universal pirate trope with clean ocular biology."
            },
            {
                "id": 2,
                "title": "Where Is Blackbeard's Sunken Treasure? Inside the Wreck of 'Queen Anne's Revenge'",
                "angle": "case_studies",
                "hook": "In 1996, marine divers found cannons off the coast of North Carolina. What they uncovered in Blackbeard's personal flagship surprised historians.",
                "target_audience": "Treasure seekers, archaeology fans, pirate nerds",
                "estimated_views": "2.7M - 5.1M",
                "production_effort": "Medium",
                "why_it_works": "Combines legendary pirate lore with real-world underwater archaeological recovery."
            },
            {
                "id": 3,
                "title": "The Only Pirate to Ever Retire with Millions: Captain Henry Every",
                "angle": "hidden_stories",
                "hook": "He pulled off the biggest heist in history by capturing the Grand Mughal of India's treasure ship Ganj-i-sawai, sparked the first global manhunt, and vanished completely.",
                "target_audience": "True crime fans, heist enthusiasts, history lovers",
                "estimated_views": "3.1M - 5.8M",
                "production_effort": "Medium",
                "why_it_works": "The ultimate real-world pirate victory story: massive loot, zero capture, and vanished identity."
            },
            {
                "id": 4,
                "title": "What Happened to Billy the Kid's Body? The Tombstone Stolen Twice",
                "angle": "unsolved_mysteries",
                "hook": "Floods washed away his cemetery markers in Fort Sumner, his headstone was stolen by pranksters twice, and some claim 'Brushy Bill' Roberts survived until 1950.",
                "target_audience": "Wild West buffs, mystery enthusiasts, folklore fans",
                "estimated_views": "1.9M - 3.5M",
                "production_effort": "Low",
                "why_it_works": "Fascinating post-mortem frontier folklore and identity conspiracy theories."
            },
            {
                "id": 5,
                "title": "The Wild West Was Actually Safer Than Modern US Cities (The Crime Statistics)",
                "angle": "myths_vs_facts",
                "hook": "In Tombstone, Arizona in 1881, there were only 5 murders all year, and carrying guns inside town was strictly illegal. Hollywood lied to you about the Wild West.",
                "target_audience": "History nerds, statistics buffs, pop culture fans",
                "estimated_views": "3.4M - 6.0M",
                "production_effort": "Low",
                "why_it_works": "Completely shatters Hollywood frontier shoot-em-up mythology with historical municipal arrest records."
            },
            {
                "id": 6,
                "title": "The Real Story Behind the Jolly Roger: What the Skull and Crossbones Really Meant",
                "angle": "history_origins",
                "hook": "If a pirate ship flew the Black Flag, you had one chance to surrender and live. If they raised the Blood-Red Flag, it meant 'No Quarter': every single person on board would die.",
                "target_audience": "History lovers, trivia fans, culture nerds",
                "estimated_views": "2.6M - 4.8M",
                "production_effort": "Low",
                "why_it_works": "Fascinating deep dive into the maritime flag signaling language and psychological terror tactics."
            },
            {
                "id": 7,
                "title": "The Modern Somali Pirate Kingpin Who Hijacked Oil Supertankers from an Internet Café",
                "angle": "dark_secrets",
                "hook": "Mohamed Abdi Hassan 'Afweyne' made $100 million hijacking supertankers, bought luxury villas, and was only brought down by a fake Hollywood film producer sting operation in Belgium.",
                "target_audience": "True crime lovers, modern warfare fans, thriller readers",
                "estimated_views": "2.8M - 5.2M",
                "production_effort": "Medium",
                "why_it_works": "Incredible undercover espionage operation that reads like a James Bond script."
            }
        ]
    },
    "050_treasure_hunting": {
        "id": "050",
        "slug": "treasure_hunting",
        "title": "Treasure Hunting",
        "category": "Conflict_Power_Exploration",
        "audience": "Adventure Seekers, Metal Detecting Enthusiasts, Shipwreck Salvage Buffs, Mystery Solvers (Global)",
        "progression": [
            ("Tier 1: Pulse Magnetometers, Sonar Mapping & The Science of Metal Detecting (Scratch / Beginner)",
             "Very Low Frequency (VLF) vs Pulse Induction detectors, side-scan sonar waterfall imaging, the Law of Finds vs Maritime Salvage, and georeferencing antique charts."),
            ("Tier 2: Sunken Spanish Galleons, Emeralds & Shipwreck Salvage Sagas (Intermediate)",
             "Mel Fisher's 16-year quest for the Nuestra Señora de Atocha, the 1715 Florida Treasure Fleet, the SS Central America 'Ship of Gold', and the Odyssey Marine Black Swan dispute."),
            ("Tier 3: Land-Based Caches, Buried Imperial Hoards & High-Stakes Riddles (Upper Intermediate)",
             "The Oak Island Money Pit booby-trapped water channels, the Beale Ciphers, Forrest Fenn's Rocky Mountain bronze chest hunt, and Howard Carter's King Tutankhamun tomb clearance."),
            ("Tier 4: The San José Galleon, Sovereign Restitution & Deep-Ocean Space Salvage (Advanced / Expert)",
             "The $20 billion San José galleon battle between Colombia and Spain, 15,000-foot ROV salvage robotics, satellite space archaeology (Sarah Parcak), and UNESCO underwater cultural heritage ethics.")
        ],
        "flagship": {
            "title": "The Nuestra Señora de Atocha: Mel Fisher's 16-Year Search for $450 Million in Sunken Emeralds and Silver",
            "angle": "beginner_explainers",
            "slug": "050_treasure_hunting_beginner_explainers_mel_fisher_atocha"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Nuestra Señora de Atocha: Mel Fisher's 16-Year Search for $450 Million in Sunken Emeralds and Silver",
                "tier": "Tier 1: Magnetometers & The Science of Detecting",
                "angle": "beginner_explainers",
                "slug": "mel_fisher_nuestra_senora_de_atocha_16_year_treasure_hunt_florida_keys",
                "question": "How did a chicken farmer turned scuba diver endure personal tragedy, bankruptcy, and 16 years of digging empty sand until finding 40 tons of Spanish silver bars in 1985?",
                "key_focus": "The 1622 hurricane fleet disaster, 'Today's the day!' daily mantra, mailbox deflector propeller invention, son Dirk's tragic drowning, US Supreme Court title victory.",
                "reason": "Flagship launch episode; the quintessential triumphant modern treasure hunt saga of the 20th century."
            },
            {
                "id": 2,
                "title": "How Metal Detectors Actually Work: VLF vs Pulse Induction in Mineralized Ground",
                "tier": "Tier 1: Magnetometers & The Science of Detecting",
                "angle": "how_it_works",
                "slug": "how_metal_detectors_work_vlf_pulse_induction_eddy_currents_physics",
                "question": "How does transmitting a 15 kHz electromagnetic field through a copper coil detect a tiny gold coin 12 inches deep through wet, conductive saltwater sand?",
                "key_focus": "Faraday's law of induction, eddy currents and phase shift discrimination, target ID numbers, VLF frequency tradeoffs vs pulse induction depth in iron minerals.",
                "reason": "The essential physical and electrical engineering principles powering everyday and professional detecting."
            },
            {
                "id": 3,
                "title": "Side-Scan Sonar and Magnetometers: How Oceanographers See Through Deep Seafloor Mud",
                "tier": "Tier 1: Magnetometers & The Science of Detecting",
                "angle": "behind_the_scenes",
                "slug": "side_scan_sonar_and_proton_precession_magnetometers_shipwreck_detection",
                "question": "How do search teams tow 'fish' sensors 100 feet above the ocean bottom to spot the magnetic signature of iron cannonballs buried under 20 feet of sand?",
                "key_focus": "Proton precession and cesium vapor magnetometers measuring nanotesla field distortions, high-frequency acoustic shadow sonar mapping, towfish navigation.",
                "reason": "The high-tech sensor toolkit that turned blind ocean searches into precise scientific archaeology."
            },
            {
                "id": 4,
                "title": "The Law of Finds vs Maritime Salvage: Who Actually Owns Sunken Treasure?",
                "tier": "Tier 1: Magnetometers & The Science of Detecting",
                "angle": "rules_regulations",
                "slug": "maritime_admiralty_law_law_of_finds_vs_salvage_sovereign_immunity",
                "question": "If you find a $500 million sunken Spanish galleon in international waters, why can the King of Spain show up in US court and take every single coin back?",
                "key_focus": "Sovereign immunity of sunken warships, Abandoned Shipwreck Act of 1987, Salvage award percentages vs Law of Finds ownership, admiralty arrest of shipwreck sites.",
                "reason": "Crucial legal reality that has bankrupted dozens of salvage companies after finding historic gold."
            },
            {
                "id": 5,
                "title": "The 1715 Spanish Treasure Fleet: How 11 Ships Lost in a Hurricane Turned Florida into the Treasure Coast",
                "tier": "Tier 1: Magnetometers & The Science of Detecting",
                "angle": "famous_examples",
                "slug": "1715_spanish_treasure_fleet_florida_treasure_coast_salvage",
                "question": "How did a July hurricane smash 11 gold-laden Spanish galleons into Florida reefs, scattering millions of 'pieces of eight' that still wash onto public beaches today?",
                "key_focus": "General Don Juan Esteban de Ubilla, Henry Jennings' pirate raid on the salvage camp (sparking the Nassau pirate republic), modern beach detecting recoveries.",
                "reason": "The legendary disaster that named Florida's 'Treasure Coast' and launched modern beach treasure culture."
            },
            {
                "id": 6,
                "title": "SS Central America: The 'Ship of Gold' and the Genius Engineer Who Vanished with the Loot",
                "tier": "Tier 2: Sunken Galleons & Shipwreck Sagas",
                "angle": "case_studies",
                "slug": "ss_central_america_ship_of_gold_tommy_thompson_salvage_and_fugitive",
                "question": "How did engineer Tommy Thompson build the deep-water robot 'Nemo' to recover 3 tons of California Gold Rush gold from 7,200 feet down, only to become a federal fugitive?",
                "key_focus": "1857 hurricane sinking triggering Wall Street panic, Bayesian search theory search grid, recovery of 50-pound gold ingots, Tommy Thompson's 2015 hotel arrest and contempt of court.",
                "reason": "The greatest deep-water salvage triumph and subsequent true crime legal scandal in American history."
            },
            {
                "id": 7,
                "title": "The Black Swan Project: Odyssey Marine's $500 Million Gold Haul That Spain Took Back",
                "tier": "Tier 2: Sunken Galleons & Shipwreck Sagas",
                "angle": "dark_secrets",
                "slug": "odyssey_marine_black_swan_our_lady_of_mercedes_spain_legal_battle",
                "question": "How did a Tampa exploration company secretly fly 500,000 silver and gold coins out of Gibraltar on chartered Boeings, only for the US federal court to order them returned to Madrid?",
                "key_focus": "Nuestra Señora de las Mercedes warship identification, Peruvian independence coin heritage claims, sovereign warship immunity legal precedent, the 2012 military cargo transfer.",
                "reason": "The landmark international precedent that permanently ended speculative private salvage of historical sovereign wrecks."
            },
            {
                "id": 8,
                "title": "The Whydah Gally: Barry Clifford and the World's Only Authenticated Pirate Shipwreck",
                "tier": "Tier 2: Sunken Galleons & Shipwreck Sagas",
                "angle": "history_origins",
                "slug": "whydah_gally_black_sam_bellamy_cape_cod_shipwreck_salvage",
                "question": "How did Barry Clifford find 'Black Sam' Bellamy's flagship buried under 30 feet of sand in the raging Cape Cod surf, proving its identity with a 1716 bronze ship's bell?",
                "key_focus": "Black Sam Bellamy's egalitarian Robin Hood pirate ideology, the Cape Cod 1717 nor'easter storm, concretion conservation chemistry, real pirate jewelry and gold dust.",
                "reason": "The only verified pirate shipwreck ever recovered in the world with fully documented archaeological artifacts."
            },
            {
                "id": 9,
                "title": "The San José Galleon: The $20 Billion Holy Grail at the Bottom of the Caribbean",
                "tier": "Tier 2: Sunken Galleons & Shipwreck Sagas",
                "angle": "unsolved_mysteries",
                "slug": "san_jose_galleon_holy_grail_of_shipwrecks_colombia_spain_dispute",
                "question": "Why is a 64-gun Spanish galleon resting at 2,000 feet off Cartagena carrying 200 tons of emeralds, silver, and gold considered the richest shipwreck in human history?",
                "key_focus": "1708 Wager's Action naval battle explosion, 2015 REMUS 6000 autonomous submarine confirmation, three-way legal tug-of-war (Colombia, Spain, indigenous groups).",
                "reason": "The ultimate active mega-treasure mystery and multi-billion-dollar sovereign heritage standoff."
            },
            {
                "id": 10,
                "title": "The Flor de la Mar: The Lost Portuguese Fleet of Alfonso de Albuquerque",
                "tier": "Tier 2: Sunken Galleons & Shipwreck Sagas",
                "angle": "unsolved_mysteries",
                "slug": "flor_de_la_mar_lost_portuguese_treasure_shipwreck_strait_of_malacca",
                "question": "Where is the 400-ton Portuguese nau that sank off Sumatra in 1511 with the entire looted royal treasury of the Sultanate of Malacca?",
                "key_focus": "60 tons of gold, golden tables, jewel-encrusted lions, treacherous reef shallows of Timia reef, shifting sand dunes hiding the wreck in Indonesian waters.",
                "reason": "The most legendary unlocated lost treasure shipwreck in Asian maritime history."
            },
            {
                "id": 11,
                "title": "The Oak Island Money Pit: 220 Years of Booby Traps, Coconut Fiber, and Tragic Deaths",
                "tier": "Tier 3: Land-Based Caches & Buried Hoards",
                "angle": "myths_vs_facts",
                "slug": "oak_island_money_pit_nova_scotia_booby_trapped_shaft_mystery",
                "question": "Did someone bury the Holy Grail, Shakespeare's manuscripts, or French crown jewels in a 150-foot shaft rigged with artificial flood tunnels to the ocean?",
                "key_focus": "1795 Daniel McGinnis oak tree discovery, coconut fiber filtering layers, 90-foot stone inscription decipherment hoax vs reality, modern heavy drilling sonic core data.",
                "reason": "The longest-running, most famous, and most commercially documented treasure hunt in the world."
            },
            {
                "id": 12,
                "title": "The Forrest Fenn Bronze Chest: The 10-Year Rocky Mountain Hunt That Claimed 5 Lives",
                "tier": "Tier 3: Land-Based Caches & Buried Hoards",
                "angle": "case_studies",
                "slug": "forrest_fenn_treasure_hunt_rocky_mountains_24_line_poem_solved",
                "question": "How did an eccentric art dealer's 24-line poem inspire 350,000 searchers to scour the Rocky Mountains for a bronze chest containing $2 million in gold nuggets?",
                "key_focus": "'Where warm waters halt' poem riddle analysis, tragic searcher drownings, Jack Stuef's 2020 discovery in Wyoming wilderness, posthumous legal controversies.",
                "reason": "The greatest real-world participatory treasure hunt of the internet era."
            },
            {
                "id": 13,
                "title": "The Beale Ciphers: The 1820s Secret Codes That Promised 4 Tons of Buried Virginia Gold",
                "tier": "Tier 3: Land-Based Caches & Buried Hoards",
                "angle": "unsolved_mysteries",
                "slug": "the_beale_ciphers_thomas_j_beale_unsolved_cryptographic_hoax",
                "question": "Did Thomas Beale bury a massive hoard of Santa Fe gold in Bedford County, Virginia, or is the entire cipher pamphlet a brilliant 19th-century publishing hoax?",
                "key_focus": "The Declaration of Independence key deciphering Paper No. 2, undeciphered Paper 1 (exact location) and Paper 3 (heirs), Edgar Allan Poe connection theories.",
                "reason": "One of cryptography's most famous unsolved riddles and historical treasure puzzles."
            },
            {
                "id": 14,
                "title": "The Staffordshire Hoard: How a Metal Detectorist with a $40 Machine Found Anglo-Saxon Gold",
                "tier": "Tier 3: Land-Based Caches & Buried Hoards",
                "angle": "famous_examples",
                "slug": "staffordshire_hoard_terry_herbert_anglo_saxon_gold_discovery_2009",
                "question": "How did an unemployed metal detecting hobbyist searching a plowed English farm field uncover 4,000 pieces of 7th-century warrior gold worth £3.3 million?",
                "key_focus": "Garnet cloisonné craftsmanship, Kingdom of Mercia battle trophies, UK Treasure Act 1996 valuation and 50/50 split between finder and landowner.",
                "reason": "The largest hoard of Anglo-Saxon gold and silver metalwork ever found, revolutionizing Dark Age history."
            },
            {
                "id": 15,
                "title": "Howard Carter and King Tut: 'Can You See Anything?' 'Yes, Wonderful Things!'",
                "tier": "Tier 3: Land-Based Caches & Buried Hoards",
                "angle": "history_origins",
                "slug": "howard_carter_king_tutankhamun_tomb_discovery_1922_valley_of_the_kings",
                "question": "How did Howard Carter and Lord Carnarvon persist through 5 fruitless seasons in the Valley of the Kings to find the only unplundered pharaonic tomb in Egypt?",
                "key_focus": "Workers hut rubble clearing, nested gilded shrines, solid gold death mask and innermost coffin (240 pounds of pure gold), the 'Curse of the Pharaohs' myth origin.",
                "reason": "The supreme high-water mark of archaeological treasure discovery in human history."
            },
            {
                "id": 16,
                "title": "Satellite Space Archaeology: Finding Lost Cities and Tombs from 400 Miles Up",
                "tier": "Tier 4: Deep Salvage, Sovereign Rights & Space Archaeology",
                "angle": "scientific_breakthroughs",
                "slug": "satellite_archaeology_sarah_parcak_infrared_space_imaging_lost_ruins",
                "question": "How does Dr. Sarah Parcak use multispectral infrared satellite sensors to reveal buried Egyptian pyramids, Roman amphitheaters, and Viking settlements invisible on the ground?",
                "key_focus": "Vegetation moisture anomalies and crop marks, subterranean mudbrick thermal absorption differentials, crowdsourced satellite platform GlobalXplorer.",
                "reason": "The modern space-age evolution of archaeological exploration and treasure prospecting."
            },
            {
                "id": 17,
                "title": "LiDAR and the Lost Cities: Piercing the Dense Jungle Canopies of Guatemala and Cambodia",
                "tier": "Tier 4: Deep Salvage, Sovereign Rights & Space Archaeology",
                "angle": "scientific_breakthroughs",
                "slug": "lidar_archaeology_maya_lost_cities_tikal_angkor_wat_mapping",
                "question": "How did pulsing 500,000 laser shots per second from airplanes strip away dense jungle canopies to reveal 60,000 hidden Maya structures in Guatemala?",
                "key_focus": "Light Detection and Ranging (LiDAR) bare-earth elevation models, defensive causeways and monumental pyramids, rewriting Maya population estimates to 10+ million.",
                "reason": "The single most revolutionary remote sensing technology in archaeological history."
            },
            {
                "id": 18,
                "title": "The UK Treasure Act: Why British Hobbyists Hand in Millions in Roman Gold to Museums",
                "tier": "Tier 4: Deep Salvage, Sovereign Rights & Space Archaeology",
                "angle": "rules_regulations",
                "slug": "uk_treasure_act_1996_portable_antiquities_scheme_coroners_court",
                "question": "Why does Britain uncover more ancient coins and Roman hoards than any nation, while treasure hunting is criminalized across the Mediterranean?",
                "key_focus": "The Portable Antiquities Scheme (PAS) database, Treasure Valuation Committee independent market appraisals, equal rewards protecting landowner-finder relationships.",
                "reason": "A masterclass in public policy aligning hobbyist enthusiasm with scientific archaeological preservation."
            },
            {
                "id": 19,
                "title": "The Nazi Gold Train: The Wałbrzych Tunnel Legend That Fooled the World in 2015",
                "tier": "Tier 4: Deep Salvage, Sovereign Rights & Space Archaeology",
                "angle": "dark_secrets",
                "slug": "nazi_gold_train_walbrzych_poland_project_riese_ground_penetrating_radar",
                "question": "Why did international media and treasure hunters descend on a Polish mountain town convinced an armored train laden with gold was sealed inside an underground tunnel?",
                "key_focus": "Project Riese underground bunker complex, ground-penetrating radar false positives, geological anomalies vs man-made tunnels, the psychology of wartime gold myths.",
                "reason": "A modern case study in media hysteria and the enduring magnetic power of Nazi treasure mythology."
            },
            {
                "id": 20,
                "title": "Autonomous Underwater Submersibles: The Robotic Future of Deep Ocean Exploration",
                "tier": "Tier 4: Deep Salvage, Sovereign Rights & Space Archaeology",
                "angle": "future_predictions",
                "slug": "autonomous_underwater_vehicles_auv_deep_ocean_mapping_future",
                "question": "Will AI-piloted AUVs like REMUS and Hugin map 100% of the Earth's ocean floors by 2030, finding every lost galleon, submarine, and aircraft?",
                "key_focus": "Seabed 2030 international initiative, synthetic aperture sonar (SAS) millimeter resolution, AI computer-vision anomaly recognition in abyssal plains.",
                "reason": "The cutting-edge frontier where autonomous artificial intelligence completes the mapping of our planet's final wilderness."
            }
        ],
        "trending": [
            {
                "id": 1,
                "title": "Why You Can Legally Keep Sunken Treasure in the UK but Go to Prison in France and Greece",
                "angle": "rules_regulations",
                "hook": "Find an ancient Roman coin in England, and the British Museum pays you fair market cash. Find that exact coin across the channel in Greece, and you face 10 years in prison.",
                "target_audience": "Detectorists, history buffs, travel lovers, legal nerds",
                "estimated_views": "2.4M - 4.5M",
                "production_effort": "Low",
                "why_it_works": "Fascinating comparative legal reality that shocks hobbyists and history fans."
            },
            {
                "id": 2,
                "title": "How a $100 Used Metal Detector Found a $4,000,000 Anglo-Saxon Treasure",
                "angle": "case_studies",
                "hook": "Terry Herbert was living on welfare when he bought a secondhand detector from a garage sale. Five days later in a neighbor's plowed field, his detector screamed non-stop.",
                "target_audience": "Metal detecting hobbyists, aspirational dreamers, history lovers",
                "estimated_views": "3.8M - 6.5M",
                "production_effort": "Low",
                "why_it_works": "The ultimate working-class Cinderella lottery story rooted in real archaeological history."
            },
            {
                "id": 3,
                "title": "The $20 Billion Galleon Found in Colombia: Who Gets the Gold?",
                "angle": "financial_breakdown",
                "hook": "The San José galleon is resting 2,000 feet deep with 11 million gold coins. Colombia, Spain, indigenous Bolivians, and a US salvage firm all claim 100% of it.",
                "target_audience": "Finance fans, true crime lovers, history buffs",
                "estimated_views": "3.2M - 5.8M",
                "production_effort": "Medium",
                "why_it_works": "Active, multi-billion-dollar modern legal battle with breathtaking sunken gold imagery."
            },
            {
                "id": 4,
                "title": "Did Anyone Actually Find Forrest Fenn's Treasure? The Bizarre Ending",
                "angle": "unsolved_mysteries",
                "hook": "In 2020, an anonymous 32-year-old medical student cracked the poem and found the chest in Wyoming. Then the lawsuits, death threats, and identity unmasking began.",
                "target_audience": "Fenn searchers, outdoor enthusiasts, puzzle geeks",
                "estimated_views": "2.9M - 5.1M",
                "production_effort": "Medium",
                "why_it_works": "The explosive, dramatic conclusion to America's most famous modern real-world treasure hunt."
            },
            {
                "id": 5,
                "title": "5 Signs a Beach Has Sunken Gold Washed Up on the Shore",
                "angle": "diy_hacks",
                "hook": "You don't need a boat or scuba gear. Heavy storms strip away feet of sand, exposing coin lines and black sand cuts where gold naturally collects.",
                "target_audience": "Beachgoers, detectorists, outdoor hobbyists",
                "estimated_views": "2.2M - 4.0M",
                "production_effort": "Low",
                "why_it_works": "Actionable, highly practical beach reading tips that inspire immediate weekend adventure."
            },
            {
                "id": 6,
                "title": "The Bizarre Booby Trap That Drowned 6 Men on Oak Island",
                "angle": "dark_secrets",
                "hook": "Every time diggers reached 90 feet, millions of gallons of seawater surged into the pit. How engineers discovered 5 artificial box drains built into Smith's Cove.",
                "target_audience": "Oak Island fans, mystery solvers, engineering geeks",
                "estimated_views": "3.5M - 6.2M",
                "production_effort": "Medium",
                "why_it_works": "Classic enduring mystery with clever hydraulic booby trap engineering."
            },
            {
                "id": 7,
                "title": "What Happened to the Amber Room? The $500 Million 8th Wonder of the World",
                "angle": "unsolved_mysteries",
                "hook": "6 tons of carved Baltic amber backed with gold leaf covered the walls of Catherine Palace. In 1945, Nazi forces crated it up in Königsberg and it vanished from history.",
                "target_audience": "WWII history buffs, art detectives, mystery lovers",
                "estimated_views": "2.7M - 4.9M",
                "production_effort": "Medium",
                "why_it_works": "The ultimate unsolved missing treasure of World War II with enduring global fascination."
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 046-050...")
    for niche_folder, meta in BATCH_046_050.items():
        process_niche(niche_folder, meta)
    update_master_readme()
    print("Batch 046-050 complete!")

if __name__ == "__main__":
    main()
