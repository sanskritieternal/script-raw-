import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_116_120 = {
    "116_mountains": {
        "id": "116",
        "slug": "mountains",
        "title": "Mountains",
        "category": "Earth_Environment",
        "audience": "Mountaineers, Geologists, High-Altitude Hikers, Alpine Explorers, Nature Documentarians (Global)",
        "progression": [
            ("Tier 1: Orogeny, Plate Tectonics & Mountain Formations (Beginner / Scratch)",
             "Continental drift, subduction zones, fold mountains vs fault-block vs volcanic arcs, the collision of the Indian and Eurasian plates, and isostasy."),
            ("Tier 2: Alpine Glaciology, Weather Systems & Mountain Microclimates (Intermediate)",
             "Cirque glaciers, moraines, orographic lift precipitation, Foehn/Chinook winds, avalanche mechanics, and crevasse formations."),
            ("Tier 3: Extreme High-Altitude Human Physiology & Survival (Upper Intermediate)",
             "The Death Zone (above 8,000 meters), High Altitude Pulmonary Edema (HAPE), High Altitude Cerebral Edema (HACE), supplemental oxygen physics, and Sherpa genetic adaptations (EPAS1)."),
            ("Tier 4: Legendary Peaks, Continental Divides & Geopolitical Borders (Advanced / Masterclass)",
             "The 14 Eight-Thousanders, K2's Bottleneck, Krummholz tree-line limits, Siachen glacier warfare, and transboundary alpine conservation corridors.")
        ],
        "flagship": {
            "title": "How the Himalayas Were Born: The 50-Million-Year Continental Collision",
            "angle": "historical_evolution",
            "slug": "116_mountains_historical_evolution_how_himalayas_were_born"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "How the Himalayas Were Born: The 50-Million-Year Continental Collision",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "how_himalayas_were_born_tectonics",
                "question": "How did the Indian tectonic plate smash into Asia at 15 centimeters per year to shove the seafloor into the stratosphere?",
                "focus": "Tethys ocean closure, marine limestone fossils on Everest's summit, crustal thickening, and active uplift rates.",
                "reason": "Crucial foundational episode explaining the planetary mechanics of orogeny and mountain building."
            },
            {
                "id": 2,
                "title": "The Types of Mountains: Fold, Fault-Block, Dome, and Volcanic Chains",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "types_of_mountains_geology",
                "question": "Why do the sharp spires of the Rocky Mountains look completely different from the rounded rolling Appalachians?",
                "focus": "Synclines and anticlines, horst and graben rifting, volcanic hot spots, and hundreds of millions of years of erosion.",
                "reason": "Teaches the basic morphological and geological classification of Earth's mountain ranges."
            },
            {
                "id": 3,
                "title": "Orographic Precipitation: Why One Side of a Mountain is a Jungle and the Other a Desert",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "orographic_precipitation_rain_shadow",
                "question": "How does moisture-laden ocean wind dumping rain on western mountain slopes create hyper-arid rain shadows on the lee side?",
                "focus": "Adiabatic lapse rates, condensation lifting, Chinook and Foehn wind thermodynamics, and the Great Basin desert formation.",
                "reason": "Demystifies the atmospheric physics creating extreme microclimates on opposite sides of mountain ridges."
            },
            {
                "id": 4,
                "title": "Glacial Carving: How Rivers of Ice Sculpted U-Shaped Valleys and Horns",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "glacial_carving_valleys_and_horns",
                "question": "How did slow-moving ice sheets carve the sheer granite walls of Yosemite and the pyramidal spire of the Matterhorn?",
                "focus": "Glacial plucking and abrasion, cirques, arêtes, hanging valleys, terminal moraines, and post-glacial rebound.",
                "reason": "Explains the monumental geomorphological forces that shaped iconic alpine landscapes."
            },
            {
                "id": 5,
                "title": "Avalanche Dynamics: Slab Avalanches, Weak Layers, and Snow Physics",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "root_cause_analysis",
                "slug": "avalanche_dynamics_snow_physics",
                "question": "What microscopic metamorphic crystal transformations turn a harmless snowpack into a 100 mph crushing slab?",
                "focus": "Depth hoar, faceted snow weak layers, crown fracture propagation, slope angles (30-45 degrees), and avalanche airbag survival.",
                "reason": "Essential safety science and mechanical failure analysis of high-mountain snowpacks."
            },
            {
                "id": 6,
                "title": "The Death Zone: Human Physiology Above 8,000 Meters",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "death_zone_human_physiology_altitude",
                "question": "Why does the human body slowly consume itself and suffocate in the thin air above 26,000 feet?",
                "focus": "Partial pressure of oxygen (33% of sea level), blood hyper-viscosity, Cheyne-Stokes breathing, and cellular necrosis.",
                "reason": "Masterclass on the lethal biological boundaries of human survival in extreme environments."
            },
            {
                "id": 7,
                "title": "HAPE and HACE: When High-Altitude Brains and Lungs Fill with Fluid",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "failure_mode_analysis",
                "slug": "hape_and_hace_altitude_sickness",
                "question": "How does hypoxic pulmonary vasoconstriction rupture alveolar capillaries and induce deadly cerebral edema?",
                "focus": "High Altitude Pulmonary Edema, High Altitude Cerebral Edema, Gamow hyperbaric bags, Dexamethasone, and rapid descent protocols.",
                "reason": "Rigorous medical examination of altitude-induced physiological collapse."
            },
            {
                "id": 8,
                "title": "Sherpa Genetics: The High-Altitude Superpowers of Himalayan Mountaineers",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "sherpa_genetics_epas1_altitude_adaptation",
                "question": "Why don't native Sherpas get altitude sickness while elite sea-level athletes collapse on Everest?",
                "focus": "EPAS1 'super-athlete' gene mutation inherited from Denisovans, mitochondrial ATP efficiency, and nitric oxide blood flow.",
                "reason": "Explores one of the clearest examples of recent natural selection in human evolutionary biology."
            },
            {
                "id": 9,
                "title": "The 14 Eight-Thousanders: The Deadliest Peaks on Planet Earth",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "famous_examples",
                "slug": "14_eight_thousanders_deadliest_peaks",
                "question": "Why are Annapurna and K2 statistically five times more fatal to summit than Mount Everest?",
                "focus": "Summit-to-fatality ratios, technical rock/ice climbing difficulty, Serac collapse hazards, and Reinhold Messner's alpine style.",
                "reason": "Profiles the ultimate theater of extreme mountaineering and human endurance."
            },
            {
                "id": 10,
                "title": "K2's Bottleneck: Inside the Most Terrifying Obstacle in Mountaineering",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "k2_bottleneck_serac_danger",
                "question": "Why must climbers spend hours traversing an 80-degree ice couloir directly underneath a 300-foot hanging ice cliff?",
                "focus": "2008 K2 disaster, fixed line severed ropes, glacial ice calving dynamics, and the savage geology of the Karakoram.",
                "reason": "Deconstructs the most notorious and objectively dangerous geographical bottleneck in high-altitude climbing."
            },
            {
                "id": 11,
                "title": "Volcanic Mountain Arcs: The Pacific Ring of Fire",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "volcanic_mountain_arcs_ring_of_fire",
                "question": "How does the subduction of oceanic crust melt bedrock into explosive stratovolcanoes like Mount St. Helens and Mount Fuji?",
                "focus": "Magma viscosity, silica content, pyroclastic flows, lahars, and caldera collapse mechanisms.",
                "reason": "Connects mountain geomorphology with planetary volcanism and seismic hazards."
            },
            {
                "id": 12,
                "title": "Mount Everest's Commercialization: Traffic Jams in the Death Zone",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "ethical_dimensions",
                "slug": "everest_commercialization_traffic_jams",
                "question": "How did high-paying amateur clients and guiding services turn the world's highest peak into an overcrowded death trap?",
                "focus": "2019 Hillary Step queue photos, oxygen tank exhaustion, waste pollution on the South Col, and exploitation of Sherpa labor.",
                "reason": "Critically examines the commodification, ethical crises, and safety risks of modern commercial expedition tourism."
            },
            {
                "id": 13,
                "title": "The Tree Line Limit: Why Trees Cannot Grow Past a Certain Altitude",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "alpine_tree_line_krummholz",
                "question": "Why does dense pine forest abruptly terminate into barren tundra at the exact same temperature threshold worldwide?",
                "focus": "6.5°C mean growing season root temperature threshold, winter desiccation, Krummholz stunted growth forms, and alpine tundra adaptations.",
                "reason": "Teaches the biological and thermal boundaries that govern ecological zoning on mountain slopes."
            },
            {
                "id": 14,
                "title": "War on the Roof of the World: The Siachen Glacier Conflict",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "siachen_glacier_high_altitude_warfare",
                "question": "How do Indian and Pakistani soldiers survive combat at 20,000 feet where 95% of casualties are caused by weather and avalanches?",
                "focus": "Operation Meghdoot, extreme frostbite logistics, artillery trajectories in thin air, and helicopter flight ceilings.",
                "reason": "Examines the highest, coldest, and most logistically absurd battlefield in modern military history."
            },
            {
                "id": 15,
                "title": "The Andes and Continental Divides: How Mountains Dictate Global River Basins",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "andes_continental_divide_river_basins",
                "question": "Why does a raindrop falling two inches apart on an alpine ridge end up in two different oceans 3,000 miles away?",
                "focus": "Great Continental Divide of the Americas, 4,500-mile Andean mountain spine, rain shadow creation of the Atacama, and Amazon river genesis.",
                "reason": "Shows how continuous mountain chains govern the hydrology, climate, and geography of entire continents."
            },
            {
                "id": 16,
                "title": "Glacial Lake Outburst Floods (GLOFs): Mountain Tsunamis",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "glofs_glacial_lake_outburst_floods",
                "question": "What happens when retreating glaciers fill unstable terminal moraine dams that suddenly breach and wipe out downstream valleys?",
                "focus": "Moraine hydrostatic pressure failure, satellite early warning radar, controlled siphon lake drainage, and Himalayan village evacuations.",
                "reason": "Investigates the escalating natural hazard threatening millions living downstream of melting mountain glaciers."
            },
            {
                "id": 17,
                "title": "The Matterhorn's Fall: How Permafrost Thaw is Causing Mountain Summits to Crumble",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "matterhorn_permafrost_thawing_rockfalls",
                "question": "Why is the internal ice glue holding Alpine peaks together melting, triggering massive catastrophic rock avalanches?",
                "focus": "Bedrock permafrost degradation, acoustic rockfall sensors in Switzerland, route closures on Mont Blanc, and mountain collapse modeling.",
                "reason": "Highlights the direct structural destabilization of iconic alpine summits under planetary warming."
            },
            {
                "id": 18,
                "title": "The Philosophy of the Summit: Why Humans Risk Death to Stand on High Rocks",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "philosophy_of_mountaineering_risk",
                "question": "Why did George Mallory answer 'Because it's there,' and what psychological drive impels humans toward voluntary suffering?",
                "focus": "Flow state psychology, sublime terror vs beauty, conquest vs communion, and the historical invention of mountaineering.",
                "reason": "Probes the deep existential, romantic, and anthropological reasons behind high-altitude exploration."
            },
            {
                "id": 19,
                "title": "The Rainbow Valley: The Grim Reality of Bodies Left on Mount Everest",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "rainbow_valley_mount_everest_bodies",
                "question": "Why do over 200 fallen mountaineers remain frozen in place along Everest's standard climbing routes as gruesome trail markers?",
                "focus": "'Green Boots' cave, Sleeping Beauty, extreme recovery logistics (requiring 8 Sherpas at risk of death), and mountain burial ethics.",
                "reason": "Sober, respectful investigation into the physical impossibility of body recovery in the Death Zone."
            },
            {
                "id": 20,
                "title": "The Master Alpine Architecture: Global Mountain Ecosystem Stewardship",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_alpine_architecture_stewardship",
                "question": "What comprehensive planetary framework preserves mountain water towers, endemic alpine biodiversity, and sustainable tourism?",
                "focus": "Integrated mountain watershed management, transboundary peace parks, ethical porter rights, and climate adaptation in high-altitude communities.",
                "reason": "Definitive capstone masterclass synthesizing all 20 mountain episodes into a visionary global alpine stewardship blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The 1996 Everest Disaster: The True Story Behind 'Into Thin Air'",
                "trend_score": "Massive Evergreen Curiosity Spike",
                "angle": "root_cause_analysis",
                "slug": "1996_everest_disaster_investigation",
                "why_trending": "The tragic storm that killed Rob Hall, Scott Fischer, and 6 others remains the ultimate cautionary tale in climbing history.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Why K2 is Statistically 5 Times Deadlier Than Mount Everest",
                "trend_score": "High Search Volume Hook",
                "angle": "comparative_analysis",
                "slug": "why_k2_is_deadlier_than_everest",
                "why_trending": "Climbers revealing the savage difficulty of K2's unpredictable storms and the House's Chimney captivated viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The 2008 K2 Disaster: The Bottleneck Serac Collapse That Trapped 11 Climbers",
                "trend_score": "Extremely High Retention Video",
                "angle": "field_investigation",
                "slug": "2008_k2_bottleneck_collapse_disaster",
                "why_trending": "Haunting survivor accounts of being trapped above 8,200 meters in pitch darkness without ropes went viral.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Who Was 'Green Boots'? The Tragic Mystery of Everest's Most Famous Landmark",
                "trend_score": "High Mystery & Curiosity Spike",
                "angle": "deep_dive",
                "slug": "green_boots_everest_tragic_identity",
                "why_trending": "The story of Indian climber Tsewang Paljor, whose frozen body marked the limestone cave on Everest for 20 years.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Traffic Jams at 29,000 Feet: Why Everest Looks Like a Theme Park Line",
                "trend_score": "Viral Outrage & Debate",
                "angle": "case_study",
                "slug": "everest_summit_traffic_jam_photos",
                "why_trending": "Nirmal Purja's viral photo of 100 climbers queued on the knife-edge ridge ignited global outrage over permits.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "How Reinhold Messner Climbed Everest Alone with Zero Supplemental Oxygen",
                "trend_score": "High Admiration & Legend Hook",
                "angle": "famous_examples",
                "slug": "reinhold_messner_solo_oxygenless_everest",
                "why_trending": "Doctors claimed oxygenless climbing was medically impossible until Messner proved them wrong through pure will.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The Swiss Alps Are Crumbling: How Melting Permafrost is Destroying Peaks",
                "trend_score": "Scientific News Spike",
                "angle": "emerging_trends",
                "slug": "swiss_alps_permafrost_thaw_rockfalls",
                "why_trending": "Dramatic footage of entire mountainsides collapsing in Switzerland as internal ice permafrost thaws shocked the internet.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "117_adventure_extreme_sports": {
        "id": "117",
        "slug": "adventure_extreme_sports",
        "title": "Adventure & Extreme Sports",
        "category": "Sports_Adventure",
        "audience": "Adrenaline Athletes, Climbers, Skydivers, Big-Wave Surfers, Extreme Sports Documentarians (Global)",
        "progression": [
            ("Tier 1: Fear Psychology, Biomechanics & Risk Mitigation (Beginner / Scratch)",
             "Sympathetic nervous system fight-or-flight triggers, flow state neurochemistry (dopamine/endorphins/anandamide), safety factor redundancy, and calculated vs reckless risk."),
            ("Tier 2: Technical Gravity & Aerial Disciplines (Intermediate)",
             "Free solo climbing physics, wingsuit BASE jumping glide ratios (aerodynamics), big-wave hydrodynamics at Nazaré, and whitewater kayaking Class V hydraulics."),
            ("Tier 3: Extreme Human Endurance & Survival Physiology (Upper Intermediate)",
             "Ultramarathon metabolic limits (glycogen depletion), open-ocean solo rowing, polar traverse frostbite survival, freediving mammalian dive reflex, and deep cave exploration (spelunking)."),
            ("Tier 4: Philosophy of Extreme Risk, Ethics & The Master Class (Advanced / Masterclass)",
             "The ethics of extreme stunts and sponsor pressures (Red Bull effect), post-mortem fatality forensics, family impact of fatal sports, and the master adventure expedition architecture.")
        ],
        "flagship": {
            "title": "Alex Honnold's Free Solo of El Capitan: The Greatest Athletic Feat in Human History",
            "angle": "case_study",
            "slug": "117_adventure_extreme_sports_case_study_alex_honnold_free_solo"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Alex Honnold's Free Solo of El Capitan: The Greatest Athletic Feat in Human History",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "alex_honnold_free_solo_el_capitan",
                "question": "How did Alex Honnold climb 3,000 vertical feet of slick granite without a rope, where a single mistake meant instant death?",
                "focus": "The Boulder Problem karate kick, amygdala fMRI brain scans showing muted fear response, years of meticulous rehearsal, and mental compartmentalization.",
                "reason": "Crucial foundational episode exploring the pinnacle of human focus, athletic mastery, and extreme risk management."
            },
            {
                "id": 2,
                "title": "The Neurochemistry of Flow: Inside the Extreme Athlete's Brain",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "neurochemistry_of_flow_state_action_sports",
                "question": "What neurochemical cocktail silences the inner critic and slows perceived time during life-or-death stunts?",
                "focus": "Transient hypofrontality, dopamine, norepinephrine, anandamide, endorphins, and Steven Kotler's flow state triggers.",
                "reason": "Teaches the biological mechanism that compels adrenaline athletes to repeatedly risk their lives."
            },
            {
                "id": 3,
                "title": "The Physics of Wingsuit BASE Jumping: Gliding at 150 MPH Next to Granite Cliffs",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "wingsuit_base_jumping_aerodynamics",
                "question": "How do ram-air wingsuit wings generate aerodynamic lift, and why does proximity flying have a 10% annual fatality rate?",
                "focus": "Glide ratio (3:1), angle of attack, burble turbulence behind the body, laser rangefinding, and emergency parachute deployment windows.",
                "reason": "Deconstructs the fluid mechanics and astronomical casualty statistics of humanity's closest equivalent to bird flight."
            },
            {
                "id": 4,
                "title": "Nazaré's Monster Waves: The Hydrodynamics of 100-Foot Swells",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "field_investigation",
                "slug": "nazare_100_foot_waves_underwater_canyon",
                "question": "How does an underwater submarine canyon in Portugal amplify Atlantic storm swells into 8-story watery avalanches?",
                "focus": "Nazaré Canyon refraction interference, wave speed physics, jet ski tow-in mechanics, impact inflatable vests, and hold-down survival.",
                "reason": "Examines the geological anomaly creating the most colossal, terrifying surf break on Earth."
            },
            {
                "id": 5,
                "title": "Freediving the Abyss: The Mammalian Dive Reflex and Squeezed Lungs",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "freediving_mammalian_dive_reflex_abyss",
                "question": "How do freedivers descend 400 feet on a single breath without their lungs being crushed flat by water pressure?",
                "focus": "Bradycardia heart rate deceleration, peripheral vasoconstriction, blood shift to thoracic cavity, nitrogen narcosis, and shallow water blackout.",
                "reason": "Explores the physiological miracle that allows humans to enter aquatic depths with zero scuba tanks."
            },
            {
                "id": 6,
                "title": "Whitewater Kayaking Class V+: Surviving Hydraulic Holes and Siphons",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "whitewater_kayaking_class_v_hydraulics",
                "question": "What happens when a kayaker gets trapped inside a recirculating hydraulic 'keeper hole' of aerated white water?",
                "focus": "Aerated water buoyancy loss, boil lines, underwater sieve entrapments, roll recovery reflexes, and throw-bag swiftwater rescues.",
                "reason": "Rigorous mechanical breakdown of river fluid dynamics and lethal hazard navigation."
            },
            {
                "id": 7,
                "title": "The Barkley Marathons: The 100-Mile Race That Only 1% of Runners Ever Finish",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "famous_examples",
                "slug": "barkley_marathons_ultramarathon_suffering",
                "question": "Why does Lazarus Lake's sadistic 60,000-foot vertical trail race in Tennessee briars break world-class ultra-runners?",
                "focus": "Book page checkpoints, sleep deprivation hallucinations, briar thickets, zero GPS navigation, and 60-hour strict cutoffs.",
                "reason": "Masterclass on the psychological frontier of endurance, disorientation, and extreme athletic suffering."
            },
            {
                "id": 8,
                "title": "Deep Cave Exploration (Spelunking): Inside Krubera and Veryovkina Caves",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "deep_cave_exploration_krubera_veryovkina",
                "question": "How do cavers spend two weeks underground descending 7,000 feet into the dark bowels of the Earth through flooded sumps?",
                "focus": "Single Rope Technique (SRT), flash flood entrapment risks, subterranean hypothermia, squeezes, and extreme psychological isolation.",
                "reason": "Explores the most claustrophobic, isolated, and perilous exploration discipline remaining on the planet."
            },
            {
                "id": 9,
                "title": "Solo Ocean Rowing: 3,000 Miles Across the Atlantic in a Plywood Rowboat",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "solo_ocean_rowing_atlantic_crossing",
                "question": "How do solo rowers survive rogue waves, salt sores, and total isolation rowing 16 hours a day for 60 days?",
                "focus": "Self-righting hull mechanics, solar desalinators, caloric burn (8,000 kcal/day), sleep fragmentation, and container ship collisions.",
                "reason": "Examines the ultimate test of human psychological self-reliance and mechanical ocean survival."
            },
            {
                "id": 10,
                "title": "Downhill Mountain Biking: Red Bull Rampage and 70-Foot Canyon Gaps",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "red_bull_rampage_downhill_freeride",
                "question": "How do freeride mountain bikers hand-carve razor-thin lines down 1,000-foot sandstone cliffs in Utah and backflip canyon gaps?",
                "focus": "Suspension travel (200mm), gyroscopic bike stability, line scouting, consequence calculus, and catastrophic spinal injury management.",
                "reason": "Details the supreme physical courage and technical engineering driving modern freeride cycling."
            },
            {
                "id": 11,
                "title": "The Red Bull Stratos Jump: Felix Baumgartner Breaking the Sound Barrier in Freefall",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "famous_examples",
                "slug": "red_bull_stratos_space_jump_baumgartner",
                "question": "What happened to human physiology when a skydiver stepped out of a space capsule at 128,000 feet and hit Mach 1.25?",
                "focus": "Armstrong limit pressure suits, supersonic shockwave buffer buffeting, uncontrollable flat spin centrifugal blood rush, and sonic booms.",
                "reason": "Documents the historic intersection between extreme stunts and aerospace engineering."
            },
            {
                "id": 12,
                "title": "The Red Bull Effect: Are Extreme Sports Sponsors Pushing Athletes to Their Deaths?",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "ethical_dimensions",
                "slug": "extreme_sports_sponsors_athlete_fatalities",
                "question": "Does corporate sponsorship revenue incentivize athletes to attempt stunts past the limits of human survivability?",
                "focus": "Energy drink marketing budgets, media rights contracts, social media viral pressure, and post-mortem liability waivers.",
                "reason": "Probes the dark economic and ethical bargain between commercial media brands and life-risking athletes."
            },
            {
                "id": 13,
                "title": "The Physiology of Hypothermia: Surviving Polar Traverses at -50°C",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "hypothermia_physiology_polar_traverses",
                "question": "How do explorer sled-haulers survive polar winds that freeze exposed human skin solid in less than 60 seconds?",
                "focus": "Vasoconstriction hunting reaction, paradoxical undressing, terminal burrowing behavior, frostbite tissue necrosis, and vapor barrier clothing.",
                "reason": "Analyzes the medical stages of extreme cold exposure and Antarctic survival techniques."
            },
            {
                "id": 14,
                "title": "Cave Diving: The Most Unforgiving Extreme Sport in the World",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "failure_mode_analysis",
                "slug": "cave_diving_fatalities_rule_of_thirds",
                "question": "Why do certified open-water divers die inside underwater cave systems within minutes of entering?",
                "focus": "Silt-outs (zero visibility), guideline navigation, the Rule of Thirds gas management, rebreather CO2 poisoning, and the 2018 Tham Luang rescue.",
                "reason": "A terrifying post-mortem analysis of the unforgiving margins of underwater cave penetration."
            },
            {
                "id": 15,
                "title": "Slacklining and Highlining: Walking a 1-Inch Webbing 1,000 Feet Above the Void",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "highlining_slackline_mechanics_psychology",
                "question": "How do highliners maintain balance on flexible nylon webbing swaying across Alpine gorges?",
                "focus": "Rigging anchor redundancy, dynamic rope drop tests, visual horizon spotting, and micro-proprioceptive ankle adjustments.",
                "reason": "Shows how pure balance, calm nervous system regulation, and rigging engineering eliminate vertigo."
            },
            {
                "id": 16,
                "title": "Big Wave Tow-In Surfing: Jet Skis, Rescues, and 2-Wave Hold-Downs",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "practical_playbook",
                "slug": "big_wave_tow_in_surfing_rescue_playbook",
                "question": "How do tow-in surf partners coordinate high-speed jet ski rescues inside the lethal impact zone before the next wave lands?",
                "focus": "Timing the white-water soup, rescue sled pickups, radio comms, carbon fiber tow-boards, and secondary impact vest triggers.",
                "reason": "Provides a high-speed operational breakdown of the life-saving partnership behind modern big-wave surfing."
            },
            {
                "id": 17,
                "title": "Speedflying and Proximity Paragliding: Skiing Off Cliffs at 80 MPH",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "speedflying_proximity_paragliding",
                "question": "How do speedflyers combine tiny 8-square-meter paraglider wings with alpine skis to carve down avalanches and cliffs?",
                "focus": "Wing loading physics, rapid roll authority, rotor turbulence behind mountain ridges, and razor-thin clearance margins.",
                "reason": "Investigates one of the fastest-growing and highest-risk hybrid gravity sports in modern alpine recreation."
            },
            {
                "id": 18,
                "title": "The Psychology of Sensation Seeking: The Dopamine D4 Receptor (DRD4-7R)",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "deep_dive",
                "slug": "sensation_seeking_drd4_7r_gene",
                "question": "Are extreme sports athletes biologically wired with a genetic craving for life-threatening risk?",
                "focus": "Zuckerman's Sensation Seeking Scale, 'wanderlust' 7R allele, baseline boredom intolerance, and evolutionary benefits of risk-taking.",
                "reason": "Connects biological genetic variation directly to high-risk behavioral psychology."
            },
            {
                "id": 19,
                "title": "Fatality Forensics in Extreme Sports: Learning from Pioneer Deaths",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "root_cause_analysis",
                "slug": "extreme_sports_fatality_forensics",
                "question": "How did the tragic deaths of Dean Potter, Shane McConkey, and Ueli Steck reshape equipment design and safety protocols?",
                "focus": "Gear failure vs pilot error, normalization of deviance in extreme stunts, backup parachute deployment kinematics, and sport safety reforms.",
                "reason": "A somber, evidence-driven memorial and technical investigation into why pioneers die and how their sports adapt."
            },
            {
                "id": 20,
                "title": "The Master Adventure Expedition Architecture: Planning Uncharted Journeys",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_adventure_expedition_architecture",
                "question": "What overarching framework unites navigation, caloric logistics, satellite communications, risk assessment, and rescue extraction?",
                "focus": "Comprehensive expedition planning, emergency protocols (Medevac/Garmin inReach), sponsor pitching, and ethical wilderness stewardship.",
                "reason": "Definitive capstone masterclass synthesizing all 20 adventure episodes into an actionable expedition blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Free Solo: How Alex Honnold Climbed 3,000 Feet with No Ropes and Survived",
                "trend_score": "Massive Viral Fascination (Evergreen)",
                "angle": "case_study",
                "slug": "alex_honnold_free_solo_breakdown_viral",
                "why_trending": "The Oscar-winning feat remains universally recognized as one of the most terrifying, breathtaking achievements in history.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Why Wingsuit BASE Jumping Has a 10% Death Rate: The Brutal Truth",
                "trend_score": "High Curiosity & Shock Hook",
                "angle": "root_cause_analysis",
                "slug": "wingsuit_base_jumping_death_rate_exposed",
                "why_trending": "Videos analyzing why virtually every pioneer in wingsuit proximity flying died within 5 years went massively viral.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Inside Nazaré: Riding the Terrifying 100-Foot Wave That Can Break Your Spine",
                "trend_score": "High Visual Spectacle Traffic",
                "angle": "field_investigation",
                "slug": "riding_100_foot_wave_nazare_portugal",
                "why_trending": "Mind-boggling drone footage of miniature surfers escaping towering multi-story walls of water dominates YouTube feeds.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The Barkley Marathons: The Impossible Race Designed to Make Everyone Quit",
                "trend_score": "High Cult Fascination Volume",
                "angle": "famous_examples",
                "slug": "barkley_marathons_impossible_race_culture",
                "why_trending": "The secretive culture, bizarre rituals, and 99% failure rate make Barkley the internet's favorite endurance obsession.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Nutty Putty Cave Tragedy: Why John Jones Was Left Upside Down Forever",
                "trend_score": "Viral Tragic Curiosity (High Retention)",
                "angle": "failure_mode_analysis",
                "slug": "nutty_putty_cave_tragedy_john_jones",
                "why_trending": "The horrifying 28-hour failed rescue of a caver stuck in a 10-inch crevice is one of the most watched disaster stories on YouTube.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Felix Baumgartner's Space Jump: The Day Red Bull Broke the Sound Barrier",
                "trend_score": "High Nostalgia & Science Hook",
                "angle": "deep_dive",
                "slug": "felix_baumgartner_space_jump_anniversary",
                "why_trending": "The terrifying moments when Baumgartner entered a flat spin at 800 mph and nearly passed out still grip audiences.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Deep Freediving Blackouts: What Happens When You Pass Out 300 Feet Underwater",
                "trend_score": "High Tension & Medical Curiosity",
                "angle": "mechanisms_and_systems",
                "slug": "shallow_water_blackout_freediving_rescue",
                "why_trending": "Emergency rescue videos showing unconscious freedivers brought to the surface and resuscitated pull massive viewership.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "118_scientists_discoverers": {
        "id": "118",
        "slug": "scientists_discoverers",
        "title": "Scientists & Discoverers",
        "category": "Math_Scientific_Methods",
        "audience": "Science Enthusiasts, History Buffs, STEM Students, Biographers, Intellectual Explorers (Global)",
        "progression": [
            ("Tier 1: Scientific Revolution & Empirical Foundations (Beginner / Scratch)",
             "Galileo's telescope trials, Newton's Principia laws of motion and gravitation, Francis Bacon's inductive scientific method, and Hooke's microscopic flea discoveries."),
            ("Tier 2: The Atomic, Chemical & Biological Tectonic Shifts (Intermediate)",
             "Darwin's Galapagos finches natural selection, Mendeleev's periodic table dreams, Marie Curie's radium discoveries, and Pasteur's germ theory disproving spontaneous generation."),
            ("Tier 3: Quantum, Relativity & The DNA Double Helix (Upper Intermediate)",
             "Einstein's 1905 Annus Mirabilis papers, Bohr vs Einstein quantum debates, Rosalind Franklin and the Photo 51 X-ray crystallography controversy, and Alan Turing's computable numbers."),
            ("Tier 4: Modern Scientific Frontiers, Unsung Geniuses & The Master Polymath (Advanced / Masterclass)",
             "Kary Mullis and the invention of PCR, Barbara McClintock's jumping genes (transposons), Vera Rubin's dark matter galaxy rotation curves, and the blueprint of scientific breakthrough discovery.")
        ],
        "flagship": {
            "title": "Newton's Annus Mirabilis: How a Plague Lockdown Invented Modern Physics",
            "angle": "historical_evolution",
            "slug": "118_scientists_discoverers_historical_evolution_newton_annus_mirabilis"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Newton's Annus Mirabilis: How a Plague Lockdown Invented Modern Physics",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "newton_annus_mirabilis_plague_physics",
                "question": "How did a 23-year-old Isaac Newton retreat to his family farm during the 1665 Great Plague and invent calculus, optics, and gravitation?",
                "focus": "Prism light decomposition experiments, inverse-square gravity calculation, calculus fluxions, and the Principia Mathematica.",
                "reason": "Crucial foundational episode introducing the most prolific individual burst of scientific discovery in human history."
            },
            {
                "id": 2,
                "title": "Galileo on Trial: How the Telescope Shattered the Geocentric Universe",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "galileo_telescope_inquisition_trial",
                "question": "Why did Galileo's observation of Jupiter's four moons and Venusian phases bring down the wrath of the Roman Inquisition?",
                "focus": "Sidereus Nuncius, telescopic grinding precision, Copernicus heliocentric theory, Dialogue Concerning the Two Chief World Systems, and 'And yet it moves'.",
                "reason": "Establishes empirical observation as the supreme arbiter of truth over religious dogma."
            },
            {
                "id": 3,
                "title": "The Scientific Method Decoded: Francis Bacon and the Death of Scholasticism",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "scientific_method_francis_bacon_empiricism",
                "question": "How did replacing Aristotle's deductive armchair philosophy with inductive experimentation launch modern technological civilization?",
                "focus": "Novum Organum, Idols of the Mind (Tribe, Cave, Marketplace, Theatre), controlled variable isolation, and repeatable experimentation.",
                "reason": "Teaches the universal operating system governing all legitimate scientific inquiry."
            },
            {
                "id": 4,
                "title": "Antonie van Leeuwenhoek: The Draper Who Discovered the Microscopic World",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "famous_examples",
                "slug": "leeuwenhoek_microscope_animalcules",
                "question": "How did a Dutch linen merchant grinding tiny glass bead lenses discover swimming 'animalcules' in pond water and dental plaque?",
                "focus": "Single-lens microscopy 200x magnification secret, Royal Society disbelief and verification, discovery of bacteria and red blood cells.",
                "reason": "Chronicles the revelation of the vast invisible microbial universe co-existing with humanity."
            },
            {
                "id": 5,
                "title": "Antoine Lavoisier: The Father of Modern Chemistry Who Lost His Head",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "lavoisier_conservation_of_mass_oxygen",
                "question": "How did rigorous scale weighing overthrow the phlogiston myth and establish the Law of Conservation of Mass?",
                "focus": "Oxygen combustion discovery, metric system nomenclature, chemical stoichiometry, and execution during the French Reign of Terror.",
                "reason": "Deconstructs the transition from medieval alchemy to precise quantitative chemistry."
            },
            {
                "id": 6,
                "title": "Darwin's Voyage on the Beagle: The 5-Year Journey That Unveiled Evolution",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "darwin_voyage_of_the_beagle_evolution",
                "question": "How did observing Galapagos finch beaks and giant armadillo fossils lead to the theory of Natural Selection?",
                "focus": "Malthusian population pressure, variation and inheritance, 20 years of secret notebook drafting, and the 1859 publication of On the Origin of Species.",
                "reason": "Masterclass on patient natural history observation synthesizing into biology's central unifying theory."
            },
            {
                "id": 7,
                "title": "Mendeleev's Dream: How the Periodic Table Predicted Undiscovered Elements",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "mendeleev_periodic_table_predictions",
                "question": "How did Dmitri Mendeleev arrange 63 known elements on cards while sleep-deprived and accurately predict the properties of Gallium and Germanium?",
                "focus": "Atomic mass patterns, periodic valence recurrence, deliberate empty gaps on the grid, and predictive validation.",
                "reason": "Highlights the supreme triumph of theoretical prediction in physical chemistry."
            },
            {
                "id": 8,
                "title": "Marie Curie: The Relentless Genius of Radioactivity",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "marie_curie_radium_polonium_radioactivity",
                "question": "How did Marie Curie manually boil tons of pitchblende ore in a drafty wooden shed to isolate Radium and Polonium?",
                "focus": "Piezoelectric electrometer measurements, two Nobel Prizes in two different sciences, ionizing radiation discovery, and radiation sickness sacrifice.",
                "reason": "Inspiring case study of unmatched scientific grit, laboratory precision, and groundbreaking physics."
            },
            {
                "id": 9,
                "title": "Louis Pasteur: The Battle Against Spontaneous Generation and Rabies",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "louis_pasteur_germ_theory_rabies",
                "question": "How did swan-neck flask broth experiments prove that life never generates spontaneously from non-living matter?",
                "focus": "Germ theory of disease, pasteurization of wine and milk, attenuated vaccine creation, and the first rabies cure on Joseph Meister.",
                "reason": "Shows how one microbiologist's experiments saved hundreds of millions of human lives from infectious disease."
            },
            {
                "id": 10,
                "title": "Michael Faraday: The Self-Taught Bookbinder Who Captured Electricity and Magnetism",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "michael_faraday_electromagnetic_induction",
                "question": "How did a laboratory assistant with zero mathematical training invent the electric motor and generator?",
                "focus": "Electromagnetic rotation, electromagnetic induction with iron rings, magnetic lines of force, and Maxwell's mathematical formalization.",
                "reason": "Demonstrates the power of pure intuitive visual experimentation that laid the groundwork for modern power grids."
            },
            {
                "id": 11,
                "title": "Einstein's Miracle Year (1905): Rewriting the Laws of the Universe in Four Papers",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "einstein_annus_mirabilis_1905_papers",
                "question": "How did a 26-year-old Swiss patent clerk simultaneously prove atoms exist, invent special relativity, and explain light quanta?",
                "focus": "Photoelectric effect (Nobel Prize), Brownian motion, Special Relativity (constancy of speed of light), and E=mc^2 mass-energy equivalence.",
                "reason": "Analyzes the most intellectually revolutionary single year in the history of theoretical physics."
            },
            {
                "id": 12,
                "title": "Rosalind Franklin and Photo 51: The Stolen Double Helix of DNA",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "ethical_dimensions",
                "slug": "rosalind_franklin_photo_51_dna_helix",
                "question": "Why did James Watson and Francis Crick win the Nobel Prize using Franklin's unpublished X-ray diffraction data without her knowledge?",
                "focus": "X-ray crystallography perfection, B-form DNA helical patterns, Maurice Wilkins's unauthorized sharing, and historical credit restoration.",
                "reason": "A critical, rigorous look at gender bias, intellectual property, and ethical attribution in monumental scientific breakthroughs."
            },
            {
                "id": 13,
                "title": "The Quantum Duel: Albert Einstein vs Niels Bohr (God Does Not Play Dice)",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "einstein_bohr_quantum_debates_entanglement",
                "question": "Why did the founder of relativity reject quantum indeterminacy and spend decades trying to disprove Heisenberg's uncertainty?",
                "focus": "Solvay conferences, Copenhagen interpretation, Einstein-Podolsky-Rosen (EPR) paradox, spooky action at a distance, and Bell's theorem validation.",
                "reason": "Examines the greatest philosophical and scientific debate in the history of modern quantum mechanics."
            },
            {
                "id": 14,
                "title": "Alan Turing: Deciphering Enigma and Inventing the Universal Computer",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "famous_examples",
                "slug": "alan_turing_enigma_universal_computer",
                "question": "How did a British mathematician prove theoretical machine computability and save an estimated 14 million lives in World War II?",
                "focus": "Turing machine abstraction, Halting Problem undecidability, Bletchley Park Bombe electro-mechanical decryption, and tragic persecution.",
                "reason": "Honors the founding father of computer science, artificial intelligence, and algorithmic theory."
            },
            {
                "id": 15,
                "title": "Barbara McClintock: The Maverick Who Discovered Jumping Genes",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "barbara_mcclintock_transposons_jumping_genes",
                "question": "Why was a female geneticist ridiculed for 30 years before winning a solo Nobel Prize for proving genes move across chromosomes?",
                "focus": "Maize corn kernel pigmentation mosaics, transposons (transposable elements), epigenetic gene regulation, and scientific dogmatic resistance.",
                "reason": "Shows how solitary perseverance and unmatched microscopic observation overturned rigid genetic orthodoxy."
            },
            {
                "id": 16,
                "title": "Vera Rubin and Dark Matter: The Galaxy Rotation Curve Mystery",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "mechanisms_and_systems",
                "slug": "vera_rubin_dark_matter_galaxy_rotation",
                "question": "How did measuring the orbital speeds of outer stars in spiral galaxies prove that 85% of cosmic matter is completely invisible?",
                "focus": "Flat galaxy rotation curves, Newtonian gravitational deviation, Fritz Zwicky cluster velocity dispersions, and dark matter halos.",
                "reason": "Explores the observational astrophysics that revealed humanity understands less than 15% of the universe's matter."
            },
            {
                "id": 17,
                "title": "Kary Mullis and PCR: The LSD-Fueled Midnight Drive That Revolutionized Biotechnology",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "kary_mullis_pcr_invention_biotechnology",
                "question": "How did an eccentric chemist imagine thermal cycling and DNA primers on a midnight drive in California to invent PCR?",
                "focus": "Polymerase Chain Reaction exponential DNA copying, Thermus aquaticus Taq polymerase heat stability, forensics, and modern molecular biology.",
                "reason": "Deconstructs the bizarre, non-linear flash of insight that unlocked the entire modern genetic testing and biotech industry."
            },
            {
                "id": 18,
                "title": "The Replication Crisis: Why Half of Published Scientific Studies Are False",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "failure_mode_analysis",
                "slug": "scientific_replication_crisis_p_hacking",
                "question": "How did p-hacking, publish-or-perish career pressures, and predatory journals poison biomedical and psychological research?",
                "focus": "John Ioannidis's seminal paper, p-value statistical manipulation, publication bias (the file drawer problem), and preregistration reforms.",
                "reason": "A critical systemic critique examining the modern institutional incentives degrading scientific truth."
            },
            {
                "id": 19,
                "title": "Serendipity in Discovery: How Accidents Created Penicillin, X-Rays, and Microwave Ovens",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "serendipity_in_science_penicillin_xrays",
                "question": "Why does chance only favor the prepared mind, and how did forgotten petri dishes change global medicine?",
                "focus": "Alexander Fleming's Penicillium mould, Roentgen's glowing barium screens, Percy Spencer's melted chocolate bar magnetron, and observational readiness.",
                "reason": "Analyzes the crucial role of accident, curiosity, and non-linear attention in revolutionary discoveries."
            },
            {
                "id": 20,
                "title": "The Architecture of Scientific Discovery: The Masterclass of Polymath Genius",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "architecture_of_scientific_discovery_masterclass",
                "question": "What common cognitive frameworks, heuristics, and mental models unite history's greatest scientists from Newton to Turing?",
                "focus": "Cross-disciplinary analogy transfer, first-principles deconstruction, anomaly obsession, thought experiments (Gedankenexperimente), and empirical rigor.",
                "reason": "Synthesizes the entire 20-episode scientific biography curriculum into an actionable cognitive blueprint for discovery."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "How Isaac Newton Invented Calculus and Modern Physics During a Plague Quarantine",
                "trend_score": "Massive Historical Fascination (High Retention)",
                "angle": "historical_evolution",
                "slug": "isaac_newton_plague_annus_mirabilis_viral",
                "why_trending": "The story of what Newton achieved while working from home during the 1665 plague exploded in popularity.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The Stolen Nobel Prize: The Real Story of Rosalind Franklin and DNA",
                "trend_score": "High Controversy & Injustice Hook",
                "angle": "case_study",
                "slug": "rosalind_franklin_stolen_nobel_prize",
                "why_trending": "Investigating how Photo 51 was taken without permission to give Watson and Crick the glory captured millions.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why Albert Einstein Spent His Final 30 Years Trying to Disprove Quantum Mechanics",
                "trend_score": "High Theoretical Physics Volume",
                "angle": "deep_dive",
                "slug": "einstein_quantum_mechanics_rejection",
                "why_trending": "Einstein's obsession with defeating quantum randomness and 'spooky action' fascinates physics lovers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The Replication Crisis: Why Most Published Scientific Studies Are Completely Wrong",
                "trend_score": "Viral Intellectual Debate",
                "angle": "failure_mode_analysis",
                "slug": "replication_crisis_p_hacking_science_broken",
                "why_trending": "Videos exposing that landmark psychological and medical experiments cannot be replicated shocked academic audiences.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Marie Curie's Belongings Are Still Radioactive 100 Years Later in Lead Boxes",
                "trend_score": "Evergreen Curiosity Hook",
                "angle": "famous_examples",
                "slug": "marie_curie_radioactive_notebooks_lead_box",
                "why_trending": "Visitors having to wear protective suits and sign waivers to read Marie Curie's original notebooks is a wild internet fact.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "How a Linen Merchant Grinding Glass Discovered the Microscopic World",
                "trend_score": "High Storytelling Appeal",
                "angle": "field_investigation",
                "slug": "leeuwenhoek_microscopic_world_discovery",
                "why_trending": "The story of Leeuwenhoek looking at his own teeth under a home-made lens and seeing swimming beasts fascinated viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The LSD Trip That Won a Nobel Prize: Kary Mullis and the Invention of PCR",
                "trend_score": "Bizarre Biography Spike",
                "angle": "philosophical_perspectives",
                "slug": "kary_mullis_pcr_biotech_invention_story",
                "why_trending": "The wild, eccentric story of the surfer-scientist who revolutionized COVID testing and biotech on a midnight drive.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "119_mathematics": {
        "id": "119",
        "slug": "mathematics",
        "title": "Mathematics",
        "category": "Math_Scientific_Methods",
        "audience": "Mathematicians, Computer Scientists, Logic Puzzle Enthusiasts, STEM Students, Number Theory Fans (Global)",
        "progression": [
            ("Tier 1: Number Theory, Geometry & Fundamental Constants (Beginner / Scratch)",
             "Prime numbers and the Fundamental Theorem of Arithmetic, Euclidean geometry axiomatic method, irrationality of sqrt(2) and Pi, Euler's identity, and mathematical induction."),
            ("Tier 2: Calculus, Linear Algebra & Probability Distributions (Intermediate)",
             "Leibniz-Newton fundamental theorem of calculus, matrix transformations and eigenvalues/eigenvectors, Bayes' theorem probability calculus, and infinite series convergence/divergence."),
            ("Tier 3: Abstract Algebra, Topology & Incompleteness Theorems (Upper Intermediate)",
             "Group theory and Galois symmetry (unsolvability of the quintic), topological homeomorphisms (coffee cup vs donut), Gödel's Incompleteness Theorems, and non-Euclidean hyperbolic geometry."),
            ("Tier 4: The Millennium Prize Problems, Complex Analysis & The Master Equation (Advanced / Masterclass)",
             "The Riemann Hypothesis and prime distribution zeros, P vs NP computational complexity, Navier-Stokes smooth solutions, Hodge Conjecture, and the unreasonable effectiveness of math in physics.")
        ],
        "flagship": {
            "title": "Euler's Identity: The Most Beautiful Equation in the Universe",
            "angle": "mechanisms_and_systems",
            "slug": "119_mathematics_mechanisms_and_systems_eulers_identity"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Euler's Identity: The Most Beautiful Equation in the Universe",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "eulers_identity_most_beautiful_equation",
                "question": "How does e^(i*pi) + 1 = 0 unite the five most fundamental mathematical constants in a single flawless line?",
                "focus": "Euler's formula via Taylor series expansions, complex plane geometry, rotation by imaginary numbers, and transcendental elegance.",
                "reason": "Crucial foundational episode celebrating the aesthetic pinnacle and conceptual synthesis of pure mathematics."
            },
            {
                "id": 2,
                "title": "The Mystery of Prime Numbers: The Atoms of Arithmetic",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "prime_numbers_atoms_of_arithmetic",
                "question": "Why do prime numbers follow no discernible sequence, yet govern modern internet encryption and number theory?",
                "focus": "Euclid's proof of infinite primes, Sieve of Eratosthenes, Fundamental Theorem of Arithmetic, and RSA public key encryption.",
                "reason": "Teaches the fundamental building blocks of all integer mathematics and modern cryptography."
            },
            {
                "id": 3,
                "title": "The Murder of Hippasus: The Dangerous Discovery of Irrational Numbers",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "irrational_numbers_hippasus_pythagoras",
                "question": "Why did the ancient Pythagoreans allegedly drown a member at sea for proving the square root of 2 cannot be written as a fraction?",
                "focus": "Pythagorean cult of integer harmony, geometric proof by contradiction of sqrt(2), and the birth of irrational numbers.",
                "reason": "Dramatic historical look at how intellectual dogma shattered when faced with rigorous mathematical proof."
            },
            {
                "id": 4,
                "title": "Euclid's Elements: The Book That Taught Humanity How to Think",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "euclids_elements_axiomatic_method",
                "question": "How did five simple geometric axioms build a deductive fortress that stood unchallenged for over 2,000 years?",
                "focus": "Axioms vs postulates, deductive logical chains, the controversial Fifth Parallel Postulate, and mathematical rigor.",
                "reason": "Establishes the axiomatic deductive method as the foundational standard of mathematical truth."
            },
            {
                "id": 5,
                "title": "The Invention of Zero and the Void: How Nothing Changed Everything",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "invention_of_zero_brahmagupta_india",
                "question": "How did ancient Indian mathematicians like Brahmagupta turn a philosophical void (shunya) into an operational number?",
                "focus": "Positional decimal notation, rules of zero arithmetic, division by zero black hole, and Islamic algebraic transmission.",
                "reason": "Chronicles the revolutionary conceptual leap that enabled modern calculation and algebra."
            },
            {
                "id": 6,
                "title": "Calculus: The Mathematics of Change and the Infinitesimal",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "beginner_guide",
                "slug": "calculus_derivatives_integrals_concept",
                "question": "How do you calculate the exact instantaneous slope of a curved line or the area under an irregular wave?",
                "focus": "Limits and infinitesimals, the derivative as instantaneous rate of change, the integral as accumulation, and the Fundamental Theorem of Calculus.",
                "reason": "Demystifies the supreme mathematical tool powering modern engineering, physics, and economics."
            },
            {
                "id": 7,
                "title": "Linear Algebra: The Matrix Engine Powering AI and Computer Graphics",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "linear_algebra_matrices_eigenvalues_ai",
                "question": "Why is the entire multi-billion dollar generative AI revolution just billions of matrix multiplications?",
                "focus": "Vector spaces, dot products, linear transformations, determinants, eigenvalues/eigenvectors, and GPU tensor cores.",
                "reason": "Connects pure matrix math directly to the technical engines driving 3D graphics and modern machine learning."
            },
            {
                "id": 8,
                "title": "Bayes' Theorem: The Mathematics of Updating Your Beliefs",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "bayes_theorem_probability_updating",
                "question": "If a medical test is 99% accurate and you test positive for a rare disease, why is your actual chance of being sick only 9%?",
                "focus": "Prior probability, likelihood ratio, posterior probability, base rate fallacy, and Bayesian spam filters.",
                "reason": "Provides the most practically useful mathematical framework for rational decision-making under uncertainty."
            },
            {
                "id": 9,
                "title": "Infinite Series and Paradoxes: Zeno, Gabriel's Horn, and 1+2+3+4+... = -1/12",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "infinite_series_paradoxes_convergence",
                "question": "How can a geometric trumpet have infinite surface area but finite volume, holding only Pi gallons of paint?",
                "focus": "Zeno's dichotomy paradox, convergent vs divergent series, Riemann rearrangement theorem, and Ramanujan summation.",
                "reason": "Explores the mind-bending counter-intuitive consequences of infinite mathematical processes."
            },
            {
                "id": 10,
                "title": "Fermat's Last Theorem: The 358-Year Riddle Solved by Andrew Wiles",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "famous_examples",
                "slug": "fermats_last_theorem_andrew_wiles",
                "question": "How did Pierre de Fermat's scribbled margin note obsess mathematicians for three centuries until a solitary 7-year breakthrough?",
                "focus": "Diophantine equations, a^n + b^n = c^n unsolvability for n>2, elliptic curves, modular forms, and the Taniyama-Shimura conjecture.",
                "reason": "The quintessential epic saga of mathematical obsession, secrecy, heartbreak, and ultimate triumph."
            },
            {
                "id": 11,
                "title": "Gödel's Incompleteness Theorems: The Mathematical Proof That Math Can Never Be Complete",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "godels_incompleteness_theorems_limits",
                "question": "How did Kurt Gödel shatter David Hilbert's dream by mathematically proving that some true mathematical statements can never be proven?",
                "focus": "Gödel numbering, self-referential paradoxes ('This statement cannot be proven'), formal axiomatic systems, and limits of knowledge.",
                "reason": "Deconstructs the most philosophically profound mathematical result of the 20th century."
            },
            {
                "id": 12,
                "title": "Topology: Why a Coffee Mug is Identical to a Donut",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "topology_rubber_sheet_geometry",
                "question": "Why does 'rubber-sheet geometry' care only about continuous deformations and through-holes rather than distances and angles?",
                "focus": "Homeomorphisms, Euler characteristic (V - E + F = 2), genus of surfaces, Möbius strips, and Poincaré Conjecture.",
                "reason": "Introduces the abstract geometric branch studying structural properties invariant under deformation."
            },
            {
                "id": 13,
                "title": "Group Theory and Symmetry: The Tragic Genius of Évariste Galois",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "historical_evolution",
                "slug": "group_theory_galois_unsolvability_quintic",
                "question": "How did a 20-year-old French revolutionary invent group theory the night before dying in a pistol duel?",
                "focus": "Permutations of polynomial roots, symmetry groups, algebraic insolvability of fifth-degree polynomials (quintics), and modern particle physics.",
                "reason": "Chronicles the dramatic life and revolutionary algebraic invention of one of mathematics' greatest martyrs."
            },
            {
                "id": 14,
                "title": "Non-Euclidean Geometry: The Curved Spaces That Enabled Einstein's General Relativity",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "non_euclidean_geometry_hyperbolic_spherical",
                "question": "What happens to triangles when you allow parallel lines to intersect or diverge on curved surfaces?",
                "focus": "Lobachevsky and Bolyai hyperbolic geometry, Riemann curved manifolds, triangles with angles > 180°, and spacetime curvature.",
                "reason": "Shows how pure mathematical rebellion against Euclid's fifth postulate gave Einstein the language for gravity."
            },
            {
                "id": 15,
                "title": "Game Theory: John Nash and the Mathematics of Human Conflict",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "game_theory_nash_equilibrium",
                "question": "How did John Nash prove that competing selfish individuals inevitably lock themselves into sub-optimal equilibrium traps?",
                "focus": "Prisoner's Dilemma, Nash Equilibrium, zero-sum vs non-zero-sum games, dominant strategies, and Cold War nuclear standoff logic.",
                "reason": "Applies mathematical rigor to strategic human conflict, evolutionary biology, and economics."
            },
            {
                "id": 16,
                "title": "The Riemann Hypothesis: The $1,000,000 Holy Grail of Prime Distribution",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "deep_dive",
                "slug": "riemann_hypothesis_zeta_function_primes",
                "question": "Why does proving that all non-trivial zeros of the Riemann Zeta Function lie on the critical line Re(s)=1/2 unlock prime secrets?",
                "focus": "Complex analysis analytic continuation, Riemann Zeta function, prime counting function Li(x), and Millennium Prize million-dollar bounty.",
                "reason": "Examines the single most celebrated, elusive unsolved problem in pure mathematics."
            },
            {
                "id": 17,
                "title": "P vs NP: The Unsolved Question That Could Break All Internet Security",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "p_vs_np_computational_complexity",
                "question": "Can every computational problem whose solution can be quickly verified also be quickly solved by an algorithm?",
                "focus": "Polynomial time (P) vs Non-deterministic polynomial time (NP), NP-completeness, Traveling Salesman Problem, and implications for all encryption.",
                "reason": "Deconstructs the defining unsolved problem of theoretical computer science."
            },
            {
                "id": 18,
                "title": "The Navier-Stokes Smoothness Riddle: Turbulence and the Million-Dollar Fluid Equations",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "failure_mode_analysis",
                "slug": "navier_stokes_smooth_solutions_singularity",
                "question": "Why cannot mathematicians prove whether smooth fluid flow solutions always exist or can break down into infinite velocity singularities?",
                "focus": "Non-linear partial differential equations, chaotic turbulence cascades, kinetic energy dissipation, and Millennium Prize mechanics.",
                "reason": "Highlights the baffling mathematical gap at the heart of everyday physical fluid mechanics."
            },
            {
                "id": 19,
                "title": "The Unreasonable Effectiveness of Mathematics in the Natural Sciences",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "unreasonable_effectiveness_of_math_wigner",
                "question": "Is mathematics an invention of the human brain, or the fundamental underlying code of the cosmos discovered by humanity?",
                "focus": "Eugene Wigner's essay, Platonism vs formalist nominalism, Maxwell's displacement current prediction, and mathematical universe hypothesis.",
                "reason": "Probes the deep philosophical mystery of why abstract equations predict physical cosmic reality with miraculous precision."
            },
            {
                "id": 20,
                "title": "The Master Mathematical Architecture: The Unified Web of Modern Math",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_mathematical_architecture_langlands",
                "question": "How does the Langlands Program weave number theory, harmonic analysis, and algebraic geometry into a grand unified theory of mathematics?",
                "focus": "Grand unified web of mathematics, modular forms and Galois representations, category theory, and the future of automated AI proof assistants (Lean).",
                "reason": "Definitive capstone masterclass synthesizing all 20 mathematical episodes into a grand vision of mathematical unity."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Equation That Baffled History: Why Euler's Identity is Considered Pure Art",
                "trend_score": "Massive Viral Aesthetic Spike",
                "angle": "case_study",
                "slug": "eulers_identity_pure_art_viral",
                "why_trending": "The mesmerizing simplicity of connecting e, i, pi, 1, and 0 routinely captures millions of curious internet viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The $1,000,000 Math Problem No One Can Solve: The Riemann Hypothesis",
                "trend_score": "High Mystery & Wealth Hook",
                "angle": "deep_dive",
                "slug": "riemann_hypothesis_million_dollar_prize",
                "why_trending": "The Millennium Prize bounty and the mysterious link between prime zeros and quantum chaos creates massive curiosity.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why 1 + 2 + 3 + 4 + ... = -1/12 Breaks Common Sense (Ramanujan's Riddle)",
                "trend_score": "High Paradox & Debate Volume",
                "angle": "root_cause_analysis",
                "slug": "sum_of_natural_numbers_minus_one_twelfth",
                "why_trending": "The mind-bending string theory result asserting infinite positive integers sum to -1/12 ignited furious internet debates.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The Man Who Knew Infinity: How Ramanujan Wrote Math Dictated by a Goddess",
                "trend_score": "Legendary Biography Spike",
                "angle": "famous_examples",
                "slug": "srinivasa_ramanujan_mathematical_prodigy",
                "why_trending": "The tragic, transcendent story of the poor clerk from Madras sending 120 unproven theorems to Cambridge went viral worldwide.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "How a 20-Year-Old Invented Modern Math the Night Before Dying in a Duel",
                "trend_score": "High Drama & Tragedy Hook",
                "angle": "historical_evolution",
                "slug": "evariste_galois_fatal_duel_group_theory",
                "why_trending": "Évariste Galois furiously scribbling group theory theorems on candlelight before being shot in the stomach is peak drama.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "P vs NP: The Problem That Could Unlock Every Bitcoin Wallet on Earth",
                "trend_score": "High Tech & Crypto Fascination",
                "angle": "mechanisms_and_systems",
                "slug": "p_vs_np_crypto_security_collapse",
                "why_trending": "Explains why proving P=NP would instantly crack RSA encryption, Bitcoin cryptography, and banking systems.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Gödel's Incompleteness: The Proof That Broke Mathematics Forever",
                "trend_score": "High Philosophical Retention",
                "angle": "philosophical_perspectives",
                "slug": "godels_incompleteness_proof_broken_math",
                "why_trending": "The devastating proof showing that mathematics can never prove all true mathematical statements is an existential mind-blower.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "120_logic_critical_thinking": {
        "id": "120",
        "slug": "logic_critical_thinking",
        "title": "Logic & Critical Thinking",
        "category": "Math_Scientific_Methods",
        "audience": "Debaters, Decision-Makers, Knowledge Workers, Philosophy Students, Cognitive Psychology Geeks (Global)",
        "progression": [
            ("Tier 1: Formal Syllogisms, Cognitive Biases & Fallacy Detection (Beginner / Scratch)",
             "Aristotelian syllogistic logic, modus ponens/modus tollens, ad hominem and straw man fallacies, confirmation bias, and Daniel Kahneman's System 1 vs System 2 thinking."),
            ("Tier 2: Probabilistic Reasoning, First Principles & Mental Models (Intermediate)",
             "Charlie Munger's latticework of mental models, Elon Musk's first principles physics deconstruction, Occam's Razor, Hanlon's Razor, and base rate neglect."),
            ("Tier 3: Epistemology, Dialectics & Propaganda Deconstruction (Upper Intermediate)",
             "Popperian falsificationism, Socratic dialogue questioning method, red teaming and steel-manning opposing arguments, cognitive dissonance mitigation, and manufactured consent media analysis."),
            ("Tier 4: Formal Symbolic Logic, Meta-Rationality & Master Cognitive Architecture (Advanced / Masterclass)",
             "Propositional calculus and Boolean truth tables, Bayesian cognitive calibration, superforecasting methodology (Philip Tetlock), algorithmic cognitive debiasing, and the master thinker's toolkit.")
        ],
        "flagship": {
            "title": "The Art of the Steel Man: How to Win Arguments by Making Your Opponent Stronger",
            "angle": "practical_playbook",
            "slug": "120_logic_critical_thinking_practical_playbook_art_of_the_steel_man"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Art of the Steel Man: How to Win Arguments by Making Your Opponent Stronger",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "practical_playbook",
                "slug": "art_of_the_steel_man_argumentation",
                "question": "Why is articulating the absolute strongest version of your opponent's belief the ultimate cognitive superpower?",
                "focus": "Straw man vs steel man methodology, Daniel Dennett's Rapoport rules, intellectual charity, and dialectical synthesis.",
                "reason": "Crucial foundational episode introducing high-integrity truth-seeking over petty rhetorical combat."
            },
            {
                "id": 2,
                "title": "System 1 vs System 2: Thinking, Fast and Slow with Daniel Kahneman",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "kahneman_system_1_system_2_thinking",
                "question": "How does your automatic, emotional brain constantly trick your lazy analytical executive mind into making irrational decisions?",
                "focus": "Heuristics and biases, substitution questions, cognitive ease vs cognitive strain, ego depletion, and anchoring effects.",
                "reason": "Teaches the core cognitive architecture underlying all human decision-making flaws."
            },
            {
                "id": 3,
                "title": "The Top 10 Logical Fallacies: How Everyday Arguments Deceive You",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "top_10_logical_fallacies_deconstructed",
                "question": "How do politicians and media pundits weaponize Ad Hominem, False Dilemma, Slippery Slope, and Whataboutism?",
                "focus": "Informal vs formal fallacies, Tu Quoque, Begging the Question, Post Hoc Ergo Propter Hoc, and spotting manipulative debate tactics.",
                "reason": "Equips viewers with an instant, tactical cognitive defense shield against rhetorical manipulation."
            },
            {
                "id": 4,
                "title": "Confirmation Bias: Why We Only See Evidence That Proves We Are Right",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "psychological_breakdown",
                "slug": "confirmation_bias_echo_chambers",
                "question": "Why does presenting stubborn people with objective, factual counter-evidence often cause them to double down on falsehoods?",
                "focus": "The Backfire Effect, motivated reasoning, identity-protective cognition, search algorithm filter bubbles, and actively open-minded thinking.",
                "reason": "Deconstructs the single most pervasive psychological barrier to objective truth."
            },
            {
                "id": 5,
                "title": "Occam's Razor vs Hanlon's Razor: The Essential Heuristic Blades",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "occams_razor_vs_hanlons_razor",
                "question": "When should you cut away complex conspiracy theories, and why should you never attribute to malice what is explained by stupidity?",
                "focus": "Parsimony in scientific explanation, Chatton's anti-razor, malice vs incompetence in bureaucracy, and heuristic efficiency.",
                "reason": "Introduces the classic philosophical razors used to slice through clutter and paranoia."
            },
            {
                "id": 6,
                "title": "First Principles Thinking: How Aristotle, Descartes, and Elon Musk Solve Impossible Problems",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "first_principles_thinking_reasoning",
                "question": "How do you break complex problems down to their fundamental atomic truths and build up solutions without reasoning by analogy?",
                "focus": "Cartesian doubt, physics raw material cost breakdowns, analogical thinking traps, and creative engineering breakthroughs.",
                "reason": "Provides a step-by-step masterclass on the most powerful innovative reasoning model in tech and engineering."
            },
            {
                "id": 7,
                "title": "Charlie Munger's Latticework: The Multidisciplinary Mental Model Machine",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "charlie_munger_mental_models_latticework",
                "question": "Why does a person with only a hammer treat every problem like a nail, and how do you build a latticework of 100 mental models?",
                "focus": "Man-with-a-hammer syndrome, inversion thinking ('Invert, always invert'), critical mass, compounding, and multi-disciplinary synthesis.",
                "reason": "Deconstructs the legendary Berkshire Hathaway billionaire investor's master cognitive framework."
            },
            {
                "id": 8,
                "title": "The Socratic Method: How to Question People into Discovering the Truth",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "famous_examples",
                "slug": "socratic_method_questioning_technique",
                "question": "Why did Socrates never lecture or assert facts, yet could lead anyone to realize their own foundational contradictions?",
                "focus": "Elenchus questioning sequence, uncovering hidden presuppositions, productive cognitive dissonance, and educational inquiry.",
                "reason": "Teaches the ancient art of humble, surgical questioning that cuts to core axioms."
            },
            {
                "id": 9,
                "title": "The Dunning-Kruger Effect: Why Incompetent People Are the Most Confident",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "dunning_kruger_effect_meta_cognition",
                "question": "Why does learning 5% of a topic create sky-high arrogance on 'Mount Stupid' while true experts suffer from imposter syndrome?",
                "focus": "Metacognitive incompetence, confidence vs competence curves, Valley of Despair, and calibrating self-awareness.",
                "reason": "Essential psychological examination of intellectual humility and the illusions of competence."
            },
            {
                "id": 10,
                "title": "Correlation vs Causation: The Spurious Statistics Deceiving the Public",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "correlation_vs_causation_spurious_statistics",
                "question": "Why does ice cream consumption correlate 98% with drowning deaths, and how do confounding variables distort news headlines?",
                "focus": "Confounders and lurking variables, reverse causality, selection bias, Judea Pearl's causal calculus, and randomized controlled trials (RCTs).",
                "reason": "Critical statistical training to prevent falling for misleading media science reporting."
            },
            {
                "id": 11,
                "title": "Popperian Falsification: What Makes a Claim Truly Scientific?",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "philosophical_perspectives",
                "slug": "popper_falsification_demarcation_problem",
                "question": "Why did Karl Popper declare that astrology and psychoanalysis are pseudosciences while Einstein's relativity is genuine science?",
                "focus": "The Demarcation Problem, black swan logic (no amount of white swans proves all swans are white), risky predictions, and unfalsifiable dogmas.",
                "reason": "Masterclass on the philosophy of science separating testable knowledge from dogma."
            },
            {
                "id": 12,
                "title": "Cognitive Dissonance and Self-Justification: The Architecture of Excuses",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "psychological_breakdown",
                "slug": "cognitive_dissonance_self_justification",
                "question": "What happens when our deep self-image clashes with undeniable proof that we did something terrible or foolish?",
                "focus": "Leon Festinger's cult prediction failure study, 'Mistakes Were Made (But Not by Me)', pyramid of choice, and rationalization mechanics.",
                "reason": "Probes the deep emotional discomfort that forces humans to invent elaborate self-delusions."
            },
            {
                "id": 13,
                "title": "Red Teaming and Pre-Mortems: Stress-Testing Plans Before Disaster Strikes",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "practical_playbook",
                "slug": "red_teaming_pre_mortem_decision_making",
                "question": "How do military strategists and NASA engineers assume a mission has completely failed before it even launches to identify fatal flaws?",
                "focus": "Gary Klein's pre-mortem protocol, devil's advocacy institutionalization, adversarial red teams, and groupthink immunization.",
                "reason": "Actionable enterprise risk assessment and strategic planning technique."
            },
            {
                "id": 14,
                "title": "Superforecasting: How Ordinary People Beat the CIA at Predicting the Future",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "superforecasting_philip_tetlock_predictions",
                "question": "How did Philip Tetlock's amateur 'Good Judgment Project' volunteers consistently out-predict intelligence agency analysts?",
                "focus": "Brier scores, probabilistic updating in micro-increments, fox vs hedgehog mindsets, Fermi estimation, and epistemic calibration.",
                "reason": "Teaches the quantitative, empirical habits of thought required to accurately predict real-world geopolitical and economic outcomes."
            },
            {
                "id": 15,
                "title": "Manufactured Consent: How Mass Media Filters Frame Reality",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "systemic_critique",
                "slug": "manufactured_consent_chomsky_propaganda",
                "question": "How do Noam Chomsky's five propaganda filters shape public consensus without overt government censorship?",
                "focus": "Corporate ownership, advertising revenue reliance, official source sourcing, flak pushback, and common enemy ideology.",
                "reason": "Rigorous critical analysis of institutional media bias and narrative engineering."
            },
            {
                "id": 16,
                "title": "Symbolic Logic and Propositional Calculus: Truth Tables and Boolean Algebra",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "mechanisms_and_systems",
                "slug": "symbolic_logic_truth_tables_boolean",
                "question": "How do AND, OR, NOT, and IMPLIES logic gates form the bridge between human philosophical deduction and silicon microchips?",
                "focus": "Truth tables, De Morgan's laws, modus tollens proofs, tautologies vs contradictions, and computer logic gate synthesis.",
                "reason": "Connects philosophical logic directly to formal mathematics and digital circuit architecture."
            },
            {
                "id": 17,
                "title": "Algorithmic Cognitive Debiasing: Can AI Help Humans Think Rationally?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "ai_cognitive_debiasing_rationality",
                "question": "Can large language models act as real-time dialectical sparing partners that detect our subconscious cognitive fallacies during writing?",
                "focus": "Automated fallacy detection, synthetic counter-argument generation, blind-spot mapping, and human-AI epistemic teaming.",
                "reason": "Explores the cutting-edge intersection of artificial intelligence and cognitive enhancement."
            },
            {
                "id": 18,
                "title": "The Epistemic Commons: Fighting Truth Decay in the Age of Generative AI",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "epistemic_commons_truth_decay_deepfakes",
                "question": "What happens to democratic self-governance when synthetic deepfakes and AI hallucinations make objective truth unverifiable?",
                "focus": "Infocalypse, cryptographic content provenance (C2PA), cognitive security (CogSec), and institutional trust reconstruction.",
                "reason": "Tackles the existential societal threat of truth erosion in the synthetic media era."
            },
            {
                "id": 19,
                "title": "Wittgenstein's Language Games: The Limits of Words and the Unspeakable",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "wittgenstein_language_games_tractatus",
                "question": "Why did Ludwig Wittgenstein declare that most philosophical problems are just linguistic misunderstandings and semantic confusion?",
                "focus": "Tractatus Logico-Philosophicus, 'Whereof one cannot speak, thereof one must be silent', language-games, and beetle-in-a-box.",
                "reason": "Probes the fundamental boundaries where human language breaks down and cannot express logical reality."
            },
            {
                "id": 20,
                "title": "The Master Thinker's Toolkit: The Complete Cognitive Architecture",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_thinkers_toolkit_cognitive_architecture",
                "question": "What unified daily operational system combines Bayesian updating, first principles, emotional detachment, and dialectical synthesis?",
                "focus": "Daily epistemic checklist, cognitive debiasing rituals, decision journals, probabilistic calibration exercises, and intellectual integrity.",
                "reason": "Definitive capstone masterclass synthesizing all 20 critical thinking episodes into a life-long cognitive operating system."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Steel Man Technique: How to Destroy Any Argument by Making It Stronger",
                "trend_score": "Massive Viral Intellectual Fascination",
                "angle": "practical_playbook",
                "slug": "steel_man_technique_debate_superpower",
                "why_trending": "The counter-intuitive power of steel-manning opponents blew up across debate channels and podcasts.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Thinking Fast and Slow: How Your Brain Tricks You Every Single Day",
                "trend_score": "High Evergreen Psychology Traffic",
                "angle": "beginner_guide",
                "slug": "kahneman_thinking_fast_slow_summary",
                "why_trending": "Daniel Kahneman's Nobel Prize-winning cognitive biases remain the most searched behavioral psychology topic.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The Top 5 Logical Fallacies Politicians Use to Manipulate You",
                "trend_score": "High Political Season Engagement",
                "angle": "case_study",
                "slug": "politicians_logical_fallacies_breakdown",
                "why_trending": "Exposing real-time debate clips with straw man and whataboutism labels pulls enormous social engagement.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why Incompetent People Think They Are Amazing: The Dunning-Kruger Effect",
                "trend_score": "High Humor & Relatability Spike",
                "angle": "root_cause_analysis",
                "slug": "dunning_kruger_effect_comedy_and_science",
                "why_trending": "Everyone loves understanding the coworker or relative who knows 1% of a topic but argues like an expert.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Elon Musk's First Principles Method: How to Think Like a Physicist",
                "trend_score": "High Tech & Entrepreneur Traffic",
                "angle": "deep_dive",
                "slug": "elon_musk_first_principles_framework",
                "why_trending": "Musk's explanation of breaking rockets down to raw aluminum and battery chemistry to slash costs is a creator favorite.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "The Socratic Method in Action: How to Win Debates Without Making Statements",
                "trend_score": "High Practical Skill Hook",
                "angle": "famous_examples",
                "slug": "socratic_method_practical_conversation",
                "why_trending": "Demonstrations of leading difficult people into realizing their own logical errors through calm questions go viral.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Superforecasting: How to Predict the Future Better Than Wall Street and the CIA",
                "trend_score": "High Business & Geopolitics Spike",
                "angle": "emerging_trends",
                "slug": "superforecasting_philip_tetlock_guide",
                "why_trending": "The exact probability tracking habits used by top tournament forecasters fascinate finance and betting audiences.",
                "status": "READY FOR COMPILATION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 116-120...")
    for folder, meta in BATCH_116_120.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 116-120 complete!")

if __name__ == "__main__":
    main()
