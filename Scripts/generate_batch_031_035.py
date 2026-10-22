"""
Batch Generator for Niches 031 to 035:
- 031_megastructures_engineering
- 032_space_exploration
- 033_ufo_extraterrestrial
- 034_exploration_adventure
- 035_military_history
"""

import sys
from pathlib import Path

# Add Scripts to sys.path
sys.path.append(str(Path(__file__).parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_031_035 = {
    "031_megastructures_engineering": {
        "id": "031",
        "slug": "megastructures_engineering",
        "title": "Megastructures / Engineering",
        "category": "Transport_Engineering",
        "audience": "Civil Engineers, Architecture Lovers, Infrastructure Enthusiasts, Futurists (Global)",
        "progression": [
            ("Tier 1: Foundations of Structural Engineering & Super-Spans (Scratch / Beginner)",
             "Cantilever loads, buttressed core skyscraper dynamics, suspension bridge aerodynamics, and deep foundation caissons."),
            ("Tier 2: Mega-Dams, Deep Tunnels & Artificial Land Reclamation (Intermediate)",
             "Arch-gravity hydrostatic pressure, tunnel boring machine (TBM) shield mechanics, marine suction dredging, and seismic isolation."),
            ("Tier 3: Extreme Environment Civil Works & Seismic Defenses (Upper Intermediate)",
             "Permafrost railway engineering, hurricane-resistant tuned mass dampers, subsea immersed tube tunnels, and desert canal grids."),
            ("Tier 4: Planetary Engineering, Orbital Elevators & Macro-Inventions (Advanced / Expert)",
             "Carbon nanotube tether physics, O'Neill cylinder artificial gravity stresses, Straits of Gibraltar dam proposals, and mega-scale geoengineering.")
        ],
        "flagship": {
            "title": "Burj Khalifa: The Aerodynamic and Foundation Engineering of the World's Tallest Tower",
            "angle": "beginner_explainers",
            "slug": "031_megastructures_engineering_beginner_explainers_burj_khalifa"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Burj Khalifa: The Aerodynamic and Foundation Engineering of the World's Tallest Tower",
                "tier": "Tier 1: Structural Engineering & Super-Spans",
                "angle": "beginner_explainers",
                "slug": "burj_khalifa_buttressed_core_wind_vortex_shedding_piles",
                "question": "How do 194 friction piles drilled into soft sandstone and a Y-shaped stepped core prevent an 828-meter needle from snapping in desert gales?",
                "key_focus": "Bill Baker (SOM) buttressed core design, vortex shedding mitigation via stepped setbacks, pumping concrete 600m vertically at night.",
                "reason": "Flagship launch episode; the ultimate masterclass in modern supertall skyscraper engineering."
            },
            {
                "id": 2,
                "title": "The Three Gorges Dam: The Concrete Titan That Literally Slowed Earth's Rotation",
                "tier": "Tier 1: Structural Engineering & Super-Spans",
                "angle": "scale_and_timespan",
                "slug": "three_gorges_dam_hydroelectric_gravity_dam_earth_rotation",
                "question": "How did 28 million cubic meters of concrete holding 40 billion cubic meters of Yangtze water alter Earth's moment of inertia by 0.06 microseconds?",
                "key_focus": "Gravity dam hydrostatic resistance, 34 massive Francis turbines, five-tier ship locks, relocating 1.3 million residents, seismic induced risk.",
                "reason": "The largest concrete structure and hydroelectric power plant in human history."
            },
            {
                "id": 3,
                "title": "The Channel Tunnel: How French and British TBMs Met with Millimeter Precision Under the Sea",
                "tier": "Tier 1: Structural Engineering & Super-Spans",
                "angle": "famous_examples",
                "slug": "channel_tunnel_chunnel_tbm_laser_guidance_underwater_breakthrough",
                "question": "How did two 1,000-ton tunneling machines boring through chalk marl 150 feet beneath the English Channel meet in 1990 without missing by an inch?",
                "key_focus": "Laser survey guidance, hydrostatic water pressure management, crossover cavern excavation, segmental precast concrete lining.",
                "reason": "One of the greatest subterranean civil engineering triumphs of the 20th century."
            },
            {
                "id": 4,
                "title": "Suspension Bridges & Resonance: How the Tacoma Narrows Disaster Rewrote Aerodynamics",
                "tier": "Tier 1: Structural Engineering & Super-Spans",
                "angle": "rise_fall",
                "slug": "tacoma_narrows_bridge_collapse_aerodynamic_flutter_resonance",
                "question": "Why did a 40-mph wind cause 'Galloping Gertie' to twist apart in 1940, and how do modern truss decks prevent aerodynamic flutter?",
                "key_focus": "Aeroelastic flutter (von Kármán vortex shedding), open truss girders vs solid plate girders, Akashi Kaikyo bridge design.",
                "reason": "The defining cautionary tale and aerodynamic turning point in bridge engineering."
            },
            {
                "id": 5,
                "title": "The Palm Jumeirah: How GPS Satellites and Vibroflotation Created an Island from Sand",
                "tier": "Tier 2: Mega-Dams, Tunnels & Land Reclamation",
                "angle": "technology_innovation",
                "slug": "palm_jumeirah_land_reclamation_vibroflotation_dredging",
                "question": "How did Dutch dredging engineers spray 94 million cubic meters of seabed sand into a palm-shaped archipelago that resists tidal erosion?",
                "key_focus": "Trailer suction hopper dredgers ('rainbowing'), differential GPS pinpointing, crescent breakwater geotextile filters, vibro-compaction.",
                "reason": "The largest artificial island and land-reclamation mega-project ever constructed."
            },
            {
                "id": 6,
                "title": "Gotthard Base Tunnel: Drilling 35 Miles Through the Boiling Roots of the Swiss Alps",
                "tier": "Tier 2: Mega-Dams, Tunnels & Land Reclamation",
                "angle": "extreme_case",
                "slug": "gotthard_base_tunnel_switzerland_deepest_rail_tunnel_geology",
                "question": "How did engineers tunnel through rock under 7,500 feet of mountain overburden where temperatures reached 115°F and rock squeezed shut?",
                "key_focus": "Squeezing kakirite rock, explosive rockburst mitigation, multi-stage ventilation shafts, high-speed flat-rail alpine transit.",
                "reason": "The world's longest and deepest rail tunnel, conquering the European alpine barrier."
            },
            {
                "id": 7,
                "title": "The Panama Canal Locks: Gravity-Powered Hydraulics Moving 100,000-Ton Ships",
                "tier": "Tier 2: Mega-Dams, Tunnels & Land Reclamation",
                "angle": "how_it_works",
                "slug": "panama_canal_locks_culverts_mules_gatun_lake_gravity_hydraulics",
                "question": "How does an 85-foot water elevator lift massive container ships across the continental divide using zero water pumps?",
                "key_focus": "Gatun Lake freshwater reservoir, 18-foot subterranean culverts, electric towing locomotives ('mules'), Neopanamax water-saving basins.",
                "reason": "A 110-year-old marvel of purely gravity-driven hydraulic civil engineering."
            },
            {
                "id": 8,
                "title": "The Delta Works: How the Netherlands Built the World's Greatest Storm Surge Barrier",
                "tier": "Tier 2: Mega-Dams, Tunnels & Land Reclamation",
                "angle": "incident_timeline",
                "slug": "delta_works_netherlands_oosterscheldekering_storm_surge_barrier",
                "question": "Following the tragic 1953 North Sea flood, how did Dutch engineers build movable steel gates on the seabed that close during hurricanes?",
                "key_focus": "Oosterscheldekering open-gate barrier, preserving tidal ecology, lifting 62 massive steel sluice doors, 10,000-year flood safety standard.",
                "reason": "The global gold standard in coastal defense, flood protection, and climate adaptation."
            },
            {
                "id": 9,
                "title": "Taipei 101: The 660-Ton Golden Pendulum That Defies Earthquakes and Typhoons",
                "tier": "Tier 3: Extreme Environments & Seismic Defenses",
                "angle": "famous_examples",
                "slug": "taipei_101_tuned_mass_damper_pendulum_earthquake_typhoon_defense",
                "question": "How does a giant suspended steel sphere between the 87th and 92nd floors sway to cancel out building vibrations during a magnitude 7.0 quake?",
                "key_focus": "Tuned Mass Damper (TMD) inertia, hydraulic shock absorber pistons, outrigger steel trusses, surviving the 2002 earthquake during construction.",
                "reason": "The most visible, elegant mechanical solution to wind and seismic resonance in supertall architecture."
            },
            {
                "id": 10,
                "title": "The Qinghai-Tibet Railway: Laying Tracks Across Melting Permafrost at 16,000 Feet",
                "tier": "Tier 3: Extreme Environments & Seismic Defenses",
                "angle": "documentary_stories",
                "slug": "qinghai_tibet_railway_permafrost_thermosyphons_high_altitude",
                "question": "How did civil engineers prevent train tracks from sinking into permafrost mud during summer thaws while operating in oxygen-starved thin air?",
                "key_focus": "Ammonia thermosyphon cooling pipes inserted into ground, ventilated crushed-rock embankments, pressurized oxygen passenger cars.",
                "reason": "High-altitude civil engineering triumph across the most hostile terrain in Asia."
            },
            {
                "id": 11,
                "title": "Hong Kong-Zhuhai-Macau Bridge: The 34-Mile Sea Crossing with an Immersed Subsea Tunnel",
                "tier": "Tier 3: Extreme Environments & Seismic Defenses",
                "angle": "field_vs_lab",
                "slug": "hong_kong_zhuhai_macau_bridge_immersed_tube_tunnel_pearl_river",
                "question": "Why did engineers drop a 4-mile bridge underwater into a concrete tunnel resting on the seabed to allow international shipping lanes to pass?",
                "key_focus": "Artificial island construction, 80,000-ton precast concrete immersed tubes, rubber GINA gasket water seals, 120-year design lifespan.",
                "reason": "The world's longest open-sea bridge and immersed tunnel transit corridor."
            },
            {
                "id": 12,
                "title": "The Danyang-Kunshan Grand Bridge: The 102-Mile Viaduct Carrying High-Speed Rail Over Rice Paddies",
                "tier": "Tier 3: Extreme Environments & Seismic Defenses",
                "angle": "scale_and_timespan",
                "slug": "danyang_kunshan_grand_bridge_longest_bridge_high_speed_rail",
                "question": "Why did China construct a 102-mile elevated viaduct across the Yangtze River Delta instead of building railbeds on the ground?",
                "key_focus": "Soft marshland soil subsidence, prefabricated modular box girders, massive launching gantry cranes, high-speed rail tolerances.",
                "reason": "The world's longest bridge, showcasing modern industrial prefabrication and rapid infrastructure scaling."
            },
            {
                "id": 13,
                "title": "The Space Elevator: Can Carbon Nanotubes Build a 62,000-Mile Tether into Geostationary Orbit?",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "advanced_concepts",
                "slug": "space_elevator_carbon_nanotubes_geostationary_orbit_climbers",
                "question": "What tensile strength is required to anchor a cable on the equator and stretch it past 35,786 km with a counterweight asteroid?",
                "key_focus": "Arthur C. Clarke concept, 100 GPa tensile strength requirement, laser-powered mechanical climbers, space debris collision mitigation.",
                "reason": "The holy grail of space infrastructure that could reduce launch costs from $2,000/kg to $10/kg."
            },
            {
                "id": 14,
                "title": "Atlantropa: The Mad 1920s Plan to Dam the Mediterranean and Drain the Sea",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "rise_fall",
                "slug": "atlantropa_herman_sorgel_dam_gibraltar_mediterranean_drainage",
                "question": "How did German architect Herman Sörgel propose damming the Strait of Gibraltar to generate 50,000 megawatts and create a Euro-African supercontinent?",
                "key_focus": "Evaporative water loss lowering sea levels by 200 meters, unlocking millions of square kilometers of farmland, ecological catastrophe realities.",
                "reason": "The most audaciously ambitious macro-engineering proposal in early 20th-century history."
            },
            {
                "id": 15,
                "title": "Boring Under London: The Crossrail (Elizabeth Line) Surgical Squeeze",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "hidden_stories",
                "slug": "crossrail_elizabeth_line_london_subterranean_surgical_tunneling",
                "question": "How did engineers thread 1,000-ton tunnel boring machines within inches of centuries-old Victorian building foundations and active Tube lines?",
                "key_focus": "Compensation grouting to prevent surface subsidence, laser displacement monitors, unexploded WWII bomb clearances, archaeological excavations.",
                "reason": "Masterclass in modern urban subterranean megaproject execution in a living metropolis."
            },
            {
                "id": 16,
                "title": "The Venice MOSE Barrier: The Floating Gates Defending St. Mark's Square from High Water",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "myths_vs_facts",
                "slug": "venice_mose_flood_barrier_floating_pneumatic_flaps_acqua_alta",
                "question": "How do 78 submerged hollow steel gates rise to seal Venice's lagoon inlets during Acqua Alta storm surges using compressed air?",
                "key_focus": "Pneumatic buoyancy mechanics, sediment fouling on hinges, 2020 maiden operational deployment, rising sea level limitations.",
                "reason": "Critical modern engineering intervention saving historical world heritage from rising tides."
            },
            {
                "id": 17,
                "title": "O'Neill Cylinders: The Structural Physics of 20-Mile Spinning Space Habitats",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "field_experimental_setup",
                "slug": "oneill_cylinders_space_habitat_centrifugal_artificial_gravity",
                "question": "How do you calculate hoop stress, atmospheric pressure retention, and gyroscopic counter-rotation for a city floating inside a spinning cylinder?",
                "key_focus": "Gerard K. O'Neill (The High Frontier), 1G centrifugal gravity simulation, atmospheric radiation shielding (slag/regolith), solar mirrors.",
                "reason": "The engineering foundation for long-term human civilization beyond planetary surfaces."
            },
            {
                "id": 18,
                "title": "The Grand Inga Dam: The Unbuilt Mega-Project That Could Power the Entire African Continent",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "future_developments",
                "slug": "grand_inga_dam_congo_river_40000_megawatt_hydroelectric_plan",
                "question": "Why has a 40,000-megawatt hydroelectric proposal on the massive Congo River rapids remained unbuilt despite twice the capacity of Three Gorges?",
                "key_focus": "Inga Falls hydrodynamics, high-voltage direct current (HVDC) continental transmission, financing hurdles, political instability.",
                "reason": "Examines the world's greatest unrealized renewable energy mega-project."
            },
            {
                "id": 19,
                "title": "The South-to-North Water Diversion: Moving 44 Billion Cubic Meters Across China",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "then_vs_now",
                "slug": "south_to_north_water_diversion_project_china_canals_aqueducts",
                "question": "How did China build three massive 700-mile canal and tunnel networks to pump southern river water to the arid industrial north?",
                "key_focus": "Mao Zedong's 1952 vision, crossing beneath the Yellow River via elevated aqueducts, massive electrical pumping stations, water quality preservation.",
                "reason": "The most expensive and extensive water engineering intervention on planet Earth."
            },
            {
                "id": 20,
                "title": "Dyson Spheres and Megastructures: Kardashev Type II Civilization Civil Engineering",
                "tier": "Tier 4: Planetary Engineering & Macro-Inventions",
                "angle": "human_impact",
                "slug": "dyson_spheres_kardashev_type_ii_stellar_energy_megastructures",
                "question": "Could an advanced civilization disassemble Mercury to build a swarm of solar energy collectors encircling their home star?",
                "key_focus": "Freeman Dyson's original paper, Dyson Swarm vs rigid solid shell impossibility, waste heat infrared signatures, search for alien megastructures.",
                "reason": "The ultimate theoretical scale of engineering, bridging macro-civil works with astrophysics."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Line, Saudi Arabia: Engineering Reality Check on the 105-Mile Mirror Skyscraper City",
                "trend_score": "Trending #1 (Massive Global Architectural News Search)",
                "angle": "myths_vs_facts",
                "slug": "neom_the_line_saudi_arabia_mirror_city_engineering_feasibility",
                "why_trending": "Downscaling reports from 170km to 2.4km by 2030, wind load simulation challenges, and glass facade bird hazard concerns.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "Fehmarnbelt Tunnel: Building the World's Longest Immersed Rail/Road Tunnel Under the Baltic",
                "trend_score": "High Infrastructure & Mega-Tunnel Search",
                "angle": "technology_innovation",
                "slug": "fehmarnbelt_tunnel_denmark_germany_immersed_concrete_segments",
                "why_trending": "Massive ongoing 18-kilometer tunnel project between Denmark and Germany dropping precast hollow concrete sections onto the seafloor.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "Jeddah Tower: Construction Resumes on the World's First 1,000-Meter Kilometer-High Skyscraper",
                "trend_score": "High Skyscraper Record Search",
                "angle": "rise_fall",
                "slug": "jeddah_tower_saudi_arabia_one_kilometer_high_construction_restart",
                "why_trending": "Adrian Smith's triangular aerodynamic design resuming construction after a 5-year freeze to eclipse the Burj Khalifa.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "The Gordie Howe International Bridge: The Epic Cable-Stayed Span Between Detroit and Canada",
                "trend_score": "High North American Civil Engineering Search",
                "angle": "famous_examples",
                "slug": "gordie_howe_bridge_detroit_windsor_cable_stayed_deck_connection",
                "why_trending": "The historic deck connection meeting over the Detroit River with the longest cable-stayed main span in North America.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "Baku Crystal Hall & The Sinkhole Defense: How Azerbaijan Built an Island on Shifting Mud",
                "trend_score": "High Structural Curiosity CTR",
                "angle": "field_vs_lab",
                "slug": "baku_caspian_sea_megastructure_foundations_mud_volcanoes",
                "why_trending": "Building monumental stadiums and skyscrapers in a seismic oil basin plagued by active subterranean mud volcanism.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "The Chacao Channel Bridge: Building South America's Longest Suspension Bridge Over Treacherous Currents",
                "trend_score": "High Engineering Challenge CTR",
                "angle": "incident_timeline",
                "slug": "chacao_channel_bridge_chile_chiloe_island_marine_currents",
                "why_trending": "Constructing deep caisson piers in 12-knot tidal currents in southern Chile connecting Chiloé Island to the mainland.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "Why Can't We Build a Bridge Across the Strait of Gibraltar?: African-European Transit Physics",
                "trend_score": "Evergreen Mega-Engineering Mystery Search",
                "angle": "advanced_concepts",
                "slug": "gibraltar_bridge_tunnel_why_it_hasnt_been_built_geology",
                "why_trending": "3,000-foot ocean depths, tectonic subduction zones, and heavy gale winds explaining why the 9-mile crossing remains unbuilt.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "032_space_exploration": {
        "id": "032",
        "slug": "space_exploration",
        "title": "Space Exploration",
        "category": "Space_Astronomy",
        "audience": "Aerospace Engineers, Space Enthusiasts, Astronomy Buffs, Tech Observers (Global)",
        "progression": [
            ("Tier 1: Rocketry Foundations, Orbital Mechanics & Early Spaceflight (Scratch / Beginner)",
             "Tsiolkovsky rocket equation, Hohmann transfer orbits, staging mass ratios, and the V-2 to Sputnik Space Race origins."),
            ("Tier 2: Lunar Landings, Deep Space Probes & Robotic Rovers (Intermediate)",
             "Apollo Lunar Module guidance computers (AGC), gravity assist slingshots (Voyager), Mars rover entry/descent/landing (Sky Crane), and sample return."),
            ("Tier 3: Space Stations, In-Orbit Assembly & Orbital Telecommunications (Upper Intermediate)",
             "ISS modular orbital mechanics, extravehicular activity (EVA) suit engineering, ion electric propulsion, and reusable booster landings."),
            ("Tier 4: Interplanetary Colonization, Propulsion Breakthroughs & Deep Space Telescopy (Advanced / Expert)",
             "Nuclear thermal rockets (NTR), in-situ resource utilization (ISRU) methane synthesis, James Webb optical cryo-alignment, and interstellar solar sails.")
        ],
        "flagship": {
            "title": "Apollo 11: The Critical 1202 Alarm and the Final 60 Seconds of Lunar Descent",
            "angle": "beginner_explainers",
            "slug": "032_space_exploration_beginner_explainers_apollo_11_lunar_descent"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Apollo 11: The Critical 1202 Alarm and the Final 60 Seconds of Lunar Descent",
                "tier": "Tier 1: Rocketry Foundations & Early Spaceflight",
                "angle": "beginner_explainers",
                "slug": "apollo_11_lunar_module_descent_1202_program_alarm_armstrong",
                "question": "How did Neil Armstrong and Buzz Aldrin land the Eagle on the Sea of Tranquility with 20 seconds of fuel remaining while computers rebooted?",
                "key_focus": "Margaret Hamilton's asynchronous Apollo Guidance Computer software, radar rendezvous overflow, manual joystick takeover, fuel slosh.",
                "reason": "Flagship launch episode; the most dramatic human achievement in exploration history."
            },
            {
                "id": 2,
                "title": "The Tsiolkovsky Rocket Equation: The Tyranny of the Fuel-to-Mass Ratio",
                "tier": "Tier 1: Rocketry Foundations & Early Spaceflight",
                "angle": "how_it_works",
                "slug": "tsiolkovsky_rocket_equation_delta_v_exhaust_velocity_staging",
                "question": "Why must 90% of a rocket's total launch pad mass be propellant just to lift a tiny payload into low Earth orbit?",
                "key_focus": "Konstantin Tsiolkovsky, Delta-v requirements, specific impulse (Isp), why multistage rocketry is physically mandatory.",
                "reason": "The foundational mathematical law governing every spacecraft ever launched by humanity."
            },
            {
                "id": 3,
                "title": "Orbital Mechanics 101: How Moving Faster Drops You into a Lower Orbit",
                "tier": "Tier 1: Rocketry Foundations & Early Spaceflight",
                "angle": "famous_examples",
                "slug": "orbital_mechanics_hohmann_transfer_elliptical_orbits_rendezvous",
                "question": "Why is navigation in space completely counter-intuitive: why burning engines forward raises your orbit and slows you down?",
                "key_focus": "Johannes Kepler's laws, Hohmann transfer orbits, orbital rendezvous phasing, prograde vs retrograde burns.",
                "reason": "Essential astrodynamics education for anyone wanting to understand spaceflight trajectories."
            },
            {
                "id": 4,
                "title": "Sputnik & Yuri Gagarin: How the Soviet Union Won the First Rounds of the Space Race",
                "tier": "Tier 1: Rocketry Foundations & Early Spaceflight",
                "angle": "history_origins",
                "slug": "sputnik_yuri_gagarin_sergei_korolev_r7_semyorka_space_race",
                "question": "How did Chief Designer Sergei Korolev hide his identity while beating America into orbit with a modified intercontinental ballistic missile?",
                "key_focus": "R-7 Semyorka rocket, Sputnik's 20 MHz radio beep, Vostok 1 spherical ejection capsule, Gagarin's 108-minute orbit.",
                "reason": "The geopolitical ignition point that transformed space from speculative science fiction into national priority."
            },
            {
                "id": 5,
                "title": "Gravity Assists: How Voyager Used Planetary Slingshots to Escape the Solar System",
                "tier": "Tier 2: Lunar Landings & Deep Space Probes",
                "angle": "technology_innovation",
                "slug": "gravity_assist_slingshot_voyager_grand_tour_orbital_energy",
                "question": "How did Gary Flandro calculate a once-in-176-year planetary alignment that allowed two probes to steal orbital energy from Jupiter and Saturn?",
                "key_focus": "Conservation of momentum, hyperbolic flybys, stealing orbital velocity from gas giants, Pale Blue Dot photograph.",
                "reason": "The navigational breakthrough that enabled human probes to reach the interstellar void."
            },
            {
                "id": 6,
                "title": "Seven Minutes of Terror: The Insane Physics of the Mars Curiosity Sky Crane",
                "tier": "Tier 2: Lunar Landings & Deep Space Probes",
                "angle": "incident_timeline",
                "slug": "mars_curiosity_sky_crane_entry_descent_landing_supersonic_parachute",
                "question": "How do you decelerate a 1-ton rover from 13,000 mph to zero in Mars' thin atmosphere using heat shields, parachutes, and rocket cables?",
                "key_focus": "Atmospheric entry ablation, supersonic disk-gap-band parachute deployment, radar altimetry, tethered rocket-powered sky crane.",
                "reason": "The most audacious, high-risk mechanical engineering feat in planetary robotics history."
            },
            {
                "id": 7,
                "title": "Saturn V: The Machine That Stood 363 Feet Tall and Burned 15 Tons of Fuel per Second",
                "tier": "Tier 2: Lunar Landings & Deep Space Probes",
                "angle": "famous_examples",
                "slug": "saturn_v_rocket_f1_engines_combustion_instability_von_braun",
                "question": "How did Wernher von Braun's team cure the violent combustion instability in the massive F-1 rocket engines that threatened to blow the rocket apart?",
                "key_focus": "RP-1 kerosene and liquid oxygen turbopumps, combustion chamber injector baffles, 7.5 million pounds of thrust, 100% launch success.",
                "reason": "The undisputed heavy-lift masterpiece of the 20th century."
            },
            {
                "id": 8,
                "title": "New Horizons: Flying by Pluto at 36,000 MPH and Unveiling a Living World",
                "tier": "Tier 2: Lunar Landings & Deep Space Probes",
                "angle": "documentary_stories",
                "slug": "new_horizons_pluto_flyby_sputnik_planitia_nitrogen_glaciers",
                "question": "What did humanity's fastest launch vehicle discover when it swept past Pluto after a 9.5-year journey across 3 billion miles of darkness?",
                "key_focus": "Sputnik Planitia nitrogen ice heart, convecting glacial cells, cryovolcanoes, Charon's dark red tholin north pole.",
                "reason": "Transformed Pluto from a blurry pixel into a geologically dynamic, breathtaking planetary body."
            },
            {
                "id": 9,
                "title": "The International Space Station: Assembling a 450-Ton Habitat in Zero Gravity",
                "tier": "Tier 3: Space Stations & Orbital Telecommunications",
                "angle": "famous_examples",
                "slug": "iss_international_space_station_orbital_assembly_truss_canadarm2",
                "question": "How did 15 nations connect 16 pressurized modules, solar arrays spanning a football field, and cooling radiators during 160 spacewalks?",
                "key_focus": "Zarya and Unity module docking, Canadarm2 robotic manipulation, orbital ammonia cooling loops, living continuously in orbit since 2000.",
                "reason": "The longest continuous human presence in space and the greatest peacetime international collaboration."
            },
            {
                "id": 10,
                "title": "Falcon 9 & Reusability: How Propulsive Landing Landed the Rocket Business",
                "tier": "Tier 3: Space Stations & Orbital Telecommunications",
                "angle": "rise_fall",
                "slug": "spacex_falcon_9_reusable_booster_propulsive_landing_grid_fins",
                "question": "Why did aerospace giants believe landing a 14-story orbital booster on an autonomous droneship in rolling seas was impossible?",
                "key_focus": "Titanium grid fins aerodynamic steering, Merlin 1D throttle control, supersonic retro-propulsion, cutting launch costs by 70%.",
                "reason": "The commercial revolution that permanently shattered expendable rocketry economics."
            },
            {
                "id": 11,
                "title": "Spacewalk Hazards: The Extravehicular Mobility Unit (EMU) as an Independent Spaceship",
                "tier": "Tier 3: Space Stations & Orbital Telecommunications",
                "angle": "extreme_case",
                "slug": "spacesuit_engineering_emu_luca_parmitano_water_leak_spacewalk",
                "question": "How does an astronaut survive in a vacuum of 250°F swings, and what happened when water flooded Luca Parmitano's helmet in 2013?",
                "key_focus": "Liquid cooling and ventilation garments, micrometeorite shielding layers, pure oxygen pre-breathe to avoid decompression sickness, sublimation cooling.",
                "reason": "Deconstructs the human body's ultimate survival shell in open vacuum."
            },
            {
                "id": 12,
                "title": "Ion Propulsion: How Xenon Gas Accelerates Spacecraft to Millions of Miles per Hour",
                "tier": "Tier 3: Space Stations & Orbital Telecommunications",
                "angle": "field_vs_lab",
                "slug": "ion_propulsion_hall_effect_thrusters_xenon_dawn_mission",
                "question": "Why does a thruster that produces the gentle force of a sheet of paper resting on your hand allow probes to explore multiple asteroids?",
                "key_focus": "Hall effect thrusters, electrostatic ion acceleration, specific impulse of 3,000+ seconds, Dawn mission visiting Vesta and Ceres.",
                "reason": "The revolutionary electric propulsion technology unlocking deep solar system endurance."
            },
            {
                "id": 13,
                "title": "James Webb Space Telescope: Unfolding a Golden Honeycomb in Deep Space",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "technology_innovation",
                "slug": "jwst_unfolding_344_single_point_failures_sunshield_lagrange_point",
                "question": "How did engineers execute 344 single-point failures to deploy a tennis-court-sized sunshield and gold beryllium mirrors at Lagrange Point 2?",
                "key_focus": "Kapton 5-layer sunshield thermal differential (300K drop), cryocooler at 7 Kelvin, micro-actuator hex mirror alignment.",
                "reason": "The most complex precision robotic deployment in astronomical engineering history."
            },
            {
                "id": 14,
                "title": "Starship: The Architecture of Fully Reusable Heavy-Lift Interplanetary Transit",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "future_developments",
                "slug": "spacex_starship_super_heavy_raptor_methalox_catch_tower",
                "question": "Why did SpaceX choose stainless steel and liquid methane over carbon fiber to build a 150-ton payload rocket caught by mechanical chopsticks?",
                "key_focus": "Full-flow staged combustion cycle (Raptor engine), belly-flop atmospheric skydive, Mechazilla tower catch arms, orbital propellant transfer.",
                "reason": "The next-generation launch system designed to enable permanent human settlements on Mars."
            },
            {
                "id": 15,
                "title": "Nuclear Thermal Propulsion: How Atomic Rockets Cut Mars Transit Time in Half",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "field_experimental_setup",
                "slug": "nuclear_thermal_propulsion_draco_project_rover_mars_transit",
                "question": "How does pumping liquid hydrogen through an ultra-hot nuclear fission core double specific impulse compared to chemical rockets?",
                "key_focus": "Project Rover and NERVA testing, modern DRACO (Demonstration Rocket for Agile Cislunar Operations), reducing cosmic radiation exposure for astronauts.",
                "reason": "The indispensable propulsion technology required for safe, rapid crewed missions to Mars."
            },
            {
                "id": 16,
                "title": "The Kessler Syndrome: How Space Debris Could Trap Humanity on Earth",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "myths_vs_facts",
                "slug": "kessler_syndrome_orbital_debris_cascading_collisions_leo",
                "question": "Can high-velocity collisions between defunct satellites create an exponential cascade of shrapnel that renders Low Earth Orbit unusable?",
                "key_focus": "Donald J. Kessler's 1978 paper, tracking 30,000 objects over 10cm, anti-satellite missile tests, active debris removal harpoons and lasers.",
                "reason": "The looming environmental crisis threatening global telecommunications, weather satellites, and future space exploration."
            },
            {
                "id": 17,
                "title": "In-Situ Resource Utilization (ISRU): Making Fuel from the Martian Atmosphere",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "measurement_method",
                "slug": "isru_sabatier_reactor_making_methane_oxygen_mars_atmosphere",
                "question": "How did the MOXIE instrument on the Perseverance rover successfully extract breathable oxygen from Mars' carbon dioxide atmosphere?",
                "key_focus": "Sabatier catalytic reaction (CO2 + 4H2 -> CH4 + 2H2O), solid oxide electrolysis, manufacturing return propellant on the Martian surface.",
                "reason": "The fundamental engineering concept that makes human round-trip planetary exploration economically viable."
            },
            {
                "id": 18,
                "title": "The Parker Solar Probe: Flying into the Fiery Atmosphere of the Sun at 430,000 MPH",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "famous_examples",
                "slug": "parker_solar_probe_fastest_human_object_carbon_composite_shield",
                "question": "How does a carbon-composite foam shield protect scientific instruments from 2,500°F solar heat as it touches the Sun's corona?",
                "key_focus": "Fastest human-made object in history, solving the coronal heating paradox, Alfvén critical surface crossing, solar wind origin.",
                "reason": "Extreme thermal engineering probing the mysterious thermonuclear engine of our Solar System."
            },
            {
                "id": 19,
                "title": "Solar Sails: Propelling Starships with the Momentum of Pure Starlight",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "then_vs_now",
                "slug": "solar_sails_photon_momentum_breakthrough_starshot_interstellar",
                "question": "How does reflected photon momentum push ultra-thin reflective aluminized mylar sheets across the solar system without any fuel?",
                "key_focus": "LightSail 2, JAXA IKAROS mission, Breakthrough Starshot 100-gigawatt ground laser array aiming for Alpha Centauri at 20% speed of light.",
                "reason": "The only currently conceivable physical technology capable of reaching another star within a human lifespan."
            },
            {
                "id": 20,
                "title": "The Overview Effect: How Seeing Earth from Space Changes Human Consciousness",
                "tier": "Tier 4: Interplanetary Colonization & Frontier Telescopy",
                "angle": "human_impact",
                "slug": "overview_effect_astronaut_psychology_earth_borders_fragility",
                "question": "Why do astronauts from opposing nations weep and experience permanent shifts in identity upon viewing the fragile borderless blue sphere?",
                "key_focus": "Frank White's psychological concept, Edgar Mitchell's epiphany on Apollo 14, thin atmospheric blue line, cognitive reorganization.",
                "reason": "The profound philosophical and psychological legacy of human space exploration for civilization on Earth."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "SpaceX Starship Flight 5: The Historic Chopstick Catch of the Super Heavy Booster",
                "trend_score": "Trending #1 (Massive Global Aerospace Record Velocity)",
                "angle": "technology_innovation",
                "slug": "starship_flight_5_super_heavy_booster_chopstick_tower_catch",
                "why_trending": "The historic October 2024 achievement of catching a 230-foot rocket booster out of the sky using giant mechanical tower arms.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "Boeing Starliner Disaster: Why Suni Williams and Butch Wilmore Got Stranded on the ISS",
                "trend_score": "High Live News & NASA Investigation Search",
                "angle": "incident_timeline",
                "slug": "boeing_starliner_calypso_thruster_helium_leaks_crew_stranded",
                "why_trending": "Reaction control thruster failures, helium manifold leaks, and NASA's decision to return Starliner uncrewed while rebooking on Crew-9.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "Polaris Dawn: The First Commercial Civilian Spacewalk in History",
                "trend_score": "High Commercial Space Search",
                "angle": "famous_examples",
                "slug": "polaris_dawn_jared_isaacman_spacex_eva_suit_van_allen_belt",
                "why_trending": "Jared Isaacman and Sarah Gillis venting the entire Crew Dragon cabin to perform the highest-altitude spacewalk since Apollo.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "Artemis II & III Timeline Delays: The Lunar Heat Shield & Starship Tanker Bottlenecks",
                "trend_score": "High NASA Moon Mission Search",
                "angle": "evidence_integrity",
                "slug": "artemis_program_timeline_delays_orion_heat_shield_charring_starship_tankers",
                "why_trending": "Orion spacecraft Avcoat ablative heat shield erosion mysteries from Artemis I and the requirement for 10+ orbital refueling tanker flights.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "China's Chang'e 6: The First Samples Ever Recovered from the Far Side of the Moon",
                "trend_score": "High Space Geopolitics & Science Search",
                "angle": "documentary_stories",
                "slug": "change_6_china_far_side_lunar_sample_return_south_pole_aitken",
                "why_trending": "Retrieving volcanic basalt from the South Pole-Aitken Basin using the Queqiao-2 relay satellite, beating NASA to far-side lunar samples.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "Europa Clipper Launched: NASA's Giant Flagship on a 1.8-Billion-Mile Journey to an Alien Ocean",
                "trend_score": "High Astrobiology & Mission Launch Search",
                "angle": "future_developments",
                "slug": "europa_clipper_launch_radiation_transistor_fix_subsurface_ocean",
                "why_trending": "Successfully resolving MOSFET radiation switch flaws to launch on Falcon Heavy toward Jupiter's ice-covered ocean moon.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The End of the ISS in 2030: How NASA Will Crash the 450-Ton Station into Point Nemo",
                "trend_score": "High Deorbit & Space Station Future CTR",
                "angle": "rise_fall",
                "slug": "iss_deorbit_united_states_deorbit_vehicle_spacex_point_nemo",
                "why_trending": "NASA awarding SpaceX $843 million to build a specialized high-thrust deorbit vehicle to steer the space station into the Pacific oceanic graveyard.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "033_ufo_extraterrestrial": {
        "id": "033",
        "slug": "ufo_extraterrestrial",
        "title": "UFO / Extraterrestrial",
        "category": "Speculative_Stories",
        "audience": "UAP Observers, Defense Analysts, Astrobiologists, Skeptics, Speculative Researchers (Global)",
        "progression": [
            ("Tier 1: Historical Sightings, Cold War Encounters & Declassified Records (Scratch / Beginner)",
             "Roswell military balloon vs saucer history, Kenneth Arnold flying discs, Project Blue Book, and the 1952 Washington D.C. radar flap."),
            ("Tier 2: Military Sensor Telemetry, Radar Tracking & UAP Physical Performance (Intermediate)",
             "FLIR infrared tracking, radar multi-sensor fusion, instantaneous acceleration without sonic booms, and transmedium travel physics."),
            ("Tier 3: Government Programs, Congressional Hearings & Whistleblower Claims (Upper Intermediate)",
             "AATIP, David Grusch congressional testimony, reverse-engineering claims, unclassified UAP reports, and defense black budgets."),
            ("Tier 4: Scientific SETI, Technosignature Detection & Interstellar Astrobiology (Advanced / Expert)",
             "Radio/optical technosignatures, Dyson swarm searches, planetary biosignatures (methane/oxygen disequilibria), and the Fermi Paradox.")
        ],
        "flagship": {
            "title": "The 2004 USS Nimitz Tic-Tac Encounter: What the FLIR1 Video and Radar Actually Tracked",
            "angle": "beginner_explainers",
            "slug": "033_ufo_extraterrestrial_beginner_explainers_nimitz_tic_tac_uap"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The 2004 USS Nimitz Tic-Tac Encounter: What the FLIR1 Video and Radar Actually Tracked",
                "tier": "Tier 1: Historical Sightings & Declassified Records",
                "angle": "beginner_explainers",
                "slug": "uss_nimitz_2004_tic_tac_uap_commander_david_fravor_flir1",
                "question": "What did Commander David Fravor and the SPY-1 radar operators witness off San Diego that dropped 80,000 feet in under a second?",
                "key_focus": "Commander David Fravor eyewitness account, Princeton radar tracking logs, FLIR1 infrared targeting pod lock loss, lack of flight control surfaces.",
                "reason": "Flagship launch episode; the most credible, multi-sensor military UAP encounter in modern history."
            },
            {
                "id": 2,
                "title": "Roswell 1947: Project Mogul, Declassified Balloons, and the Birth of Modern UFO Mythology",
                "tier": "Tier 1: Historical Sightings & Declassified Records",
                "angle": "history_origins",
                "slug": "roswell_1947_project_mogul_soviet_nuclear_detection_balloon",
                "question": "How did a crashed top-secret acoustic microphone balloon spying on Soviet nuclear tests spawn 75 years of alien saucer lore?",
                "key_focus": "Mac Brazel debris discovery, 509th Bomb Group press release, Project Mogul classified spy balloons, 1994 Air Force report.",
                "reason": "Separates rigorous Cold War military espionage history from UFO folklore."
            },
            {
                "id": 3,
                "title": "Project Blue Book: How the US Air Force Investigated 12,618 UFO Cases",
                "tier": "Tier 1: Historical Sightings & Declassified Records",
                "angle": "famous_examples",
                "slug": "project_blue_book_edward_ruppelt_j_allen_hynek_condon_report",
                "question": "Why did astronomer J. Allen Hynek start as an Air Force debunker and end up a believer in unexplained aerial phenomena?",
                "key_focus": "Swamp gas explanations, 701 officially unsolved cases, 1969 Condon Committee report shut down, close encounters classification system.",
                "reason": "The foundational government investigation establishing the terminology and scientific skepticism of ufology."
            },
            {
                "id": 4,
                "title": "The 1952 Washington D.C. Radar Flap: When Unidentified Targets Flew Over the Capitol",
                "tier": "Tier 1: Historical Sightings & Declassified Records",
                "angle": "incident_timeline",
                "slug": "1952_washington_dc_ufo_radar_flap_national_airport_intercepts",
                "question": "What triggered simultaneous radar and visual sightings over the White House, prompting the largest military press conference since WWII?",
                "key_focus": "Washington National Airport and Andrews AFB radar returns, F-94 jet scrambles, temperature inversion mirage debunks, CIA Robertson Panel.",
                "reason": "The most dramatic public Cold War UAP event that led directly to national security surveillance policies."
            },
            {
                "id": 5,
                "title": "The Five Observables: How AATIP Defined Anomalous Flight Physics",
                "tier": "Tier 2: Military Sensors & Physical Performance",
                "angle": "technology_innovation",
                "slug": "five_observables_aatip_luis_elizondo_uap_physics_anomalies",
                "question": "What specific aerodynamic behaviors (anti-gravity lift, hypersonic velocity, low observability) distinguish UAPs from drones?",
                "key_focus": "Luis Elizondo framework: positive lift without wings, instant acceleration without sonic booms, transmedium travel, signature management.",
                "reason": "The operational defense taxonomy used by Pentagon analysts to evaluate anomalous encounters."
            },
            {
                "id": 6,
                "title": "The GIMBAL and GOFAST Videos: Deconstructing Navy Infrared Targeting Telemetry",
                "tier": "Tier 2: Military Sensors & Physical Performance",
                "angle": "evidence_integrity",
                "slug": "gimbal_gofast_navy_atflir_infrared_pod_optical_glare_analysis",
                "question": "Does the GIMBAL video show a flying saucer rotating against the wind, or is the rotation an artifact of the ATFLIR optical pod mirror?",
                "key_focus": "Raytheon ATFLIR sensor mechanics, rotating de-rotation prism artifacts, Mick West parallax trigonometry on GOFAST, pilot audio reactions.",
                "reason": "Rigorous forensic breakdown of the military videos that convinced the world to take UAPs seriously."
            },
            {
                "id": 7,
                "title": "Transmedium Travel: Objects Moving Seamlessly from Vacuum to Air to Deep Ocean",
                "tier": "Tier 2: Military Sensors & Physical Performance",
                "angle": "field_vs_lab",
                "slug": "transmedium_vehicles_water_air_entry_hydrodynamic_drag_supercavitation",
                "question": "Why would an object striking the ocean surface at Mach 2 normally disintegrate, and what physics would permit entry without a splash?",
                "key_focus": "Hydrodynamic drag equations, supercavitation gas bubbles, boundary layer plasma manipulation, Aguadilla Puerto Rico 2013 thermal footage.",
                "reason": "Examines the theoretical physics boundaries between fluid dynamics, air resistance, and propulsion."
            },
            {
                "id": 8,
                "title": "The Rendlesham Forest Incident: Britain's Military UFO Mystery at RAF Woodbridge",
                "tier": "Tier 2: Military Sensors & Physical Performance",
                "angle": "documentary_stories",
                "slug": "rendlesham_forest_incident_1980_raf_woodbridge_charles_halt",
                "question": "What landed in a Suffolk pine forest outside a nuclear-armed NATO base over two consecutive nights in December 1980?",
                "key_focus": "Lt. Col. Charles Halt audio recording, Geiger counter radiation readings, triangular landing gear impressions, Orford Ness lighthouse debunk debate.",
                "reason": "Universally known as 'Britain's Roswell', featuring credible military officer documentation."
            },
            {
                "id": 9,
                "title": "David Grusch and the Congressional UAP Hearings: Whistleblowers Under Oath",
                "tier": "Tier 3: Government Programs & Whistleblowers",
                "angle": "famous_examples",
                "slug": "david_grusch_congressional_uap_hearing_whistleblower_testimony",
                "question": "What claims did a decorated former intelligence officer make under oath regarding secret multi-decade crash-retrieval programs?",
                "key_focus": "House Oversight Committee hearing (July 2023), non-human biologics claims, lack of first-hand physical documentation, Inspector General referral.",
                "reason": "The historic political turning point bringing UAP crash retrieval discussions into the halls of Congress."
            },
            {
                "id": 10,
                "title": "AATIP and the Black Budget: How Harry Reid Secretly Funded Pentagon UFO Research",
                "tier": "Tier 3: Government Programs & Whistleblowers",
                "angle": "hidden_stories",
                "slug": "aatip_pentagon_ufo_program_harry_reid_bigelow_aerospace",
                "question": "How did a $22 million earmark in 2007 establish the Advanced Aerospace Threat Identification Program inside the DIA?",
                "key_focus": "Senator Harry Reid, Robert Bigelow Aerospace, Defense Intelligence Reference Documents (DIRDs), 2017 New York Times front-page scoop.",
                "reason": "The origin story of the modern disclosure era and government defense black-budget funding."
            },
            {
                "id": 11,
                "title": "The Malmstrom AFB Incident: Did a UFO Disable Ten Nuclear ICBMs in 1967?",
                "tier": "Tier 3: Government Programs & Whistleblowers",
                "angle": "incident_timeline",
                "slug": "malmstrom_afb_1967_nuclear_icbm_shutdown_robert_salas",
                "question": "Why did Captain Robert Salas and launch control officers report Minuteman nuclear missiles going into 'No-Go' failure as a red saucer hovered?",
                "key_focus": "Nuclear command and control fail-safes, electromagnetic pulse vs guidance software glitch, declassified SAC messages, strategic defense vulnerability.",
                "reason": "The most chilling military intersection: unidentified craft demonstrating control over strategic nuclear deterrence."
            },
            {
                "id": 12,
                "title": "The Robertson Panel & The Stigmatization of UAP Science: How Inquiries Were Silenced",
                "tier": "Tier 3: Government Programs & Whistleblowers",
                "angle": "rise_fall",
                "slug": "robertson_panel_1953_cia_debunking_policy_stigmatization_science",
                "question": "How did a 1953 secret CIA scientific panel intentionally weaponize pop-culture ridicule to prevent civilian panic from jamming radar channels?",
                "key_focus": "H.P. Robertson, using Disney animators and magicians to debunk sightings, civilian surveillance channels, lasting 70-year scientific stigma.",
                "reason": "Explains why mainstream academia refused to touch the topic of unidentified aerial phenomena for seven decades."
            },
            {
                "id": 13,
                "title": "SETI & The Search for Technosignatures: Beyond Radio Waves to Laser Beacons",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "advanced_concepts",
                "slug": "seti_technosignatures_optical_lasers_dyson_swarms_breakthrough_listen",
                "question": "Why is the search for extraterrestrial intelligence expanding from 1.42 GHz 'water hole' radio to megawatt pulsed laser and infrared heat searches?",
                "key_focus": "Frank Drake, Breakthrough Listen, fast optical pulses, waste heat infrared anomalies in Gaia stellar catalogs, megastructure detection.",
                "reason": "The rigorous, peer-reviewed scientific methodology for detecting technological civilizations across interstellar distances."
            },
            {
                "id": 14,
                "title": "The Galileo Project: Avi Loeb's Search for Extraterrestrial Artifacts in Our Solar System",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "technology_innovation",
                "slug": "galileo_project_avi_loeb_harvard_interstellar_meteor_fragments",
                "question": "How is a Harvard astrophysicist using deep-ocean magnetic sleds and calibrated rooftop telescopes to hunt for artificial technology?",
                "key_focus": "IM1 interstellar meteor expedition off Papua New Guinea, magnetic spherules isotopic analysis, systematic sensor networks observing skies 24/7.",
                "reason": "The first open, well-funded academic attempt to bypass government secrecy with civilian scientific instrumentation."
            },
            {
                "id": 15,
                "title": "Planetary Biosignatures: How James Webb Sniffs Atmospheric Disequilibrium on Alien Worlds",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "measurement_method",
                "slug": "planetary_biosignatures_jwst_methane_oxygen_coexistence_k2_18b",
                "question": "Why does the simultaneous presence of methane and oxygen in an exoplanet atmosphere form chemical proof of biological metabolism?",
                "key_focus": "Atmospheric thermodynamic disequilibrium, transit transmission spectroscopy, K2-18b dimethyl sulfide debate, false positive photochemistry.",
                "reason": "The most likely way humanity will actually confirm the existence of extraterrestrial life in the next decade."
            },
            {
                "id": 16,
                "title": "The Fermi Paradox: If Extraterrestrials Exist, Why Is the Universe Silent?",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "myths_vs_facts",
                "slug": "fermi_paradox_great_filter_dark_forest_theory_hart_tipler",
                "question": "Does Enrico Fermi's lunchtime question prove intelligent life is extraordinarily rare, or are civilizations hiding in a 'Dark Forest'?",
                "key_focus": "Hart-Tipler conjecture (self-replicating von Neumann probes), Liu Cixin's Dark Forest hypothesis, Zoo hypothesis, planetary filters.",
                "reason": "The great intellectual debate reconciling astronomical scales with our apparent cosmic solitude."
            },
            {
                "id": 17,
                "title": "Warp Drives and Alcubierre Metrics: Does General Relativity Allow Faster-Than-Light Travel?",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "field_experimental_setup",
                "slug": "alcubierre_warp_drive_general_relativity_negative_energy_physics",
                "question": "How did Miguel Alcubierre show that contracting spacetime in front of a ship while expanding it behind bypasses Einstein's light-speed limit?",
                "key_focus": "Negative energy density requirements, Casimir effect, Erik Lentz positive-energy soliton alternatives, micro-warp bubbles.",
                "reason": "Advanced theoretical physics evaluating how an advanced interstellar intelligence could realistically traverse light-years."
            },
            {
                "id": 18,
                "title": "Astrobiology in the Ice: Why Europa and Enceladus Are Better Bets Than Mars",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "then_vs_now",
                "slug": "astrobiology_europa_enceladus_subsurface_oceans_hydrothermal_life",
                "question": "Why do the tidal heating, liquid water oceans, and hydrothermal plumes of icy outer moons make them the prime candidates for alien life?",
                "key_focus": "Cassini plume flybys detecting organic molecules and molecular hydrogen, Europa Clipper radar sounding, methanogenesis potential.",
                "reason": "Shifts astrobiological focus from dry surface dust to active, warm subterranean alien oceans."
            },
            {
                "id": 19,
                "title": "The Drake Equation Recalculated: What Modern Exoplanet Data Proves About Cosmic Odds",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "scale_and_timespan",
                "slug": "drake_equation_modern_exoplanet_kepler_data_recalculation",
                "question": "How did NASA's Kepler mission nail down the astronomical terms of the Drake equation, leaving only the biological and longevity unknowns?",
                "key_focus": "Eta-Earth (average habitable planets per star), abiogenesis probability, civilization lifetime L, Adam Frank and Woodruff Sullivan's archaeological fraction.",
                "reason": "Provides mathematical grounding turning an ideological debate into quantified scientific probability."
            },
            {
                "id": 20,
                "title": "First Contact Protocols: What Actually Happens the Day We Detect an Alien Signal",
                "tier": "Tier 4: Scientific SETI & Interstellar Astrobiology",
                "angle": "human_impact",
                "slug": "first_contact_protocols_post_detection_policy_international_iaa",
                "question": "Who gets notified first, who verifies the signal, and who has the legal authority to transmit a reply on behalf of Earth?",
                "key_focus": "International Academy of Astronautics (IAA) Post-Detection Declaration, Rio 2.0 Scale of Significance, METI (Messaging Extraterrestrial Intelligence) controversy.",
                "reason": "The ultimate geopolitical, social, and existential policy dilemma humanity will face upon discovery."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Pentagon AARO 2024 Historical Report: The Defense Department's Formal Verdict on Alien Tech",
                "trend_score": "Trending #1 (High Defense & UFO News Search)",
                "angle": "evidence_integrity",
                "slug": "aaro_historical_report_2024_pentagon_uap_investigation_verdict",
                "why_trending": "Dr. Sean Kirkpatrick's formal 63-page Pentagon report stating zero empirical evidence of extraterrestrial craft or reverse engineering.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "The Bizarre 'Nazca Mummies' Scandal: CT Scans, Llama Skulls, and Forensic Debunking",
                "trend_score": "Ultra High Viral Controversy Search",
                "angle": "myths_vs_facts",
                "slug": "nazca_mummies_peru_jaime_maussan_forensic_dna_debunking",
                "why_trending": "Jaime Maussan presenting three-fingered mummified specimens to the Mexican Congress; forensic analyses revealing altered pre-Columbian human and animal bones.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "The New 2024 Congressional UAP Hearing: Ex-Admirals and NASA Officials Testify Again",
                "trend_score": "High Live Political & Whistleblower Search",
                "angle": "documentary_stories",
                "slug": "congressional_uap_hearing_november_2024_admirals_testimony",
                "why_trending": "Bipartisan House hearing featuring Rear Admiral Tim Gallaudet and former intelligence officials detailing underwater USO phenomena.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "The Sol Foundation: How Stanford Scientists and Pentagon Insiders Are Legitimatizing UAP Research",
                "trend_score": "High Academic & Institutional Search",
                "angle": "people_personalities",
                "slug": "sol_foundation_stanford_dr_garry_nolan_uap_scientific_institutionalization",
                "why_trending": "Dr. Garry Nolan and former national security officials building an elite academic think tank to coordinate global UAP science.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "Underwater USOs: Are Unidentified Submerged Objects More Common Than Aerial UFOs?",
                "trend_score": "High Oceanic Mystery & Military CTR",
                "angle": "famous_examples",
                "slug": "unidentified_submerged_objects_uso_sonar_submarine_encounters",
                "why_trending": "Submarine sonar operators reporting submerged objects tracking at hundreds of knots; declassified Russian naval archives.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "K2-18b Update 2024–2026: What Follow-Up JWST Data Says About the Alien Gas DMS",
                "trend_score": "High Space Science & Astrobiology Search",
                "angle": "technology_innovation",
                "slug": "k2_18b_jwst_follow_up_observations_dms_biosignature_truth",
                "why_trending": "Nikku Madhusudhan's follow-up cycle observations with NIRSpec testing whether dimethyl sulfide is truly present on the habitable-zone sub-Neptune.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "The WOW! Signal 2024 Breakthrough: Arecibo Archive Data Suggests a Magnetar Masar Flash",
                "trend_score": "Evergreen Radio Astronomy Mystery CTR",
                "angle": "historical_origins",
                "slug": "wow_signal_solved_2024_arecibo_archive_hydrogen_cloud_maser",
                "why_trending": "Abel Méndez and planetary scientists discovering identical rare narrowband hydrogen flaring from interstellar clouds, offering a natural explanation.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "034_exploration_adventure": {
        "id": "034",
        "slug": "exploration_adventure",
        "title": "Exploration / Adventure",
        "category": "Travel_Experiences",
        "audience": "Adventurers, Mountaineers, Polar Enthusiasts, Extreme Survival Buffs (Global)",
        "progression": [
            ("Tier 1: Polar Frontiers & The Age of Extreme Earth Exploration (Scratch / Beginner)",
             "Scurvy biochemistry, dog sled logistics, polar ice navigation, and the heroic age of Antarctic exploration."),
            ("Tier 2: The Death Zone: High-Altitude Mountaineering & 8,000-Meter Peaks (Intermediate)",
             "Hypoxia, cerebral and pulmonary edema (HACE/HAPE), Sherpa genetic adaptations, and the 1996 Everest tragedy."),
            ("Tier 3: Uncharted Jungles, Desert Crossings & Subterranean Spelunking (Upper Intermediate)",
             "Percy Fawcett's Lost City of Z, Rub' al Khali Empty Quarter crossings, deep cave asphyxiation, and equatorial survival."),
            ("Tier 4: Solo Circumnavigations, Extreme Survival Psychology & Modern Frontier Expeditions (Advanced / Expert)",
             "Golden Globe solo non-stop sailing, extreme survival psychology under isolation, Mariana trench diving, and unmapped frontiers.")
        ],
        "flagship": {
            "title": "The Race to the South Pole: Amundsen vs Scott and the Logistics of Survival",
            "angle": "beginner_explainers",
            "slug": "034_exploration_adventure_beginner_explainers_race_to_south_pole"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Race to the South Pole: Amundsen vs Scott and the Logistics of Survival",
                "tier": "Tier 1: Polar Frontiers & Extreme Earth Exploration",
                "angle": "beginner_explainers",
                "slug": "race_to_south_pole_amundsen_vs_scott_polar_logistics_skis_ponies",
                "question": "Why did Roald Amundsen return safely using skis and sled dogs while Robert Falcon Scott's party froze to death pulling sledges by hand?",
                "key_focus": "Inuit survival techniques (fur garments vs wool), dog nutrition and culling strategy, motor sled and Manchurian pony failures, scurvy caloric deficits.",
                "reason": "Flagship launch episode; the ultimate study in expedition planning, humility before nature, and lethal hubris."
            },
            {
                "id": 2,
                "title": "The Franklin Expedition: What Lead Poisoning, Cannibalism, and Arctic Ice Did to 129 Men",
                "tier": "Tier 1: Polar Frontiers & Extreme Earth Exploration",
                "angle": "incident_timeline",
                "slug": "franklin_expedition_hms_erebus_terror_lead_poisoning_ice_lock",
                "question": "How did the Royal Navy's two most advanced steam-assisted ice ships vanish into the Northwest Passage in 1845?",
                "key_focus": "King William Island retreat, lead-soldered tinned food toxicity, King William Island bone cut marks, 2014/2016 shipwreck discoveries.",
                "reason": "The most haunting, iconic polar maritime catastrophe in history."
            },
            {
                "id": 3,
                "title": "Scurvy: The Nutritional Monster That Killed 2 Million Sailors",
                "tier": "Tier 1: Polar Frontiers & Extreme Earth Exploration",
                "angle": "how_it_works",
                "slug": "scurvy_vitamin_c_collagen_james_lind_first_clinical_trial",
                "question": "How does a lack of ascorbic acid cause old surgical scars to reopen, teeth to fall out, and psychological terror to grip sailors?",
                "key_focus": "Collagen synthesis hydroxylase enzymes, James Lind's 1747 citrus trial (first controlled clinical trial), British Navy 'limeys', Arctic meat cures.",
                "reason": "Crucial biochemical history explaining why nutrition was the greatest barrier to global geographic exploration."
            },
            {
                "id": 4,
                "title": "Fridtjof Nansen and the Fram: Intentionally Freezing a Ship into the Arctic Pack Ice",
                "tier": "Tier 1: Polar Frontiers & Extreme Earth Exploration",
                "angle": "famous_examples",
                "slug": "fridtjof_nansen_fram_expedition_arctic_pack_ice_drift_kayak_dash",
                "question": "How did a Norwegian scientist build a round-hulled wooden ship designed to be squeezed upward by sea ice rather than crushed?",
                "key_focus": "Transpolar drift hypothesis, Fram round hull physics, Nansen and Johansen 86°14'N ski dash, surviving a winter on walrus blubber in a stone hut.",
                "reason": "Masterclass in bold, counter-intuitive exploration engineering based on deep environmental observation."
            },
            {
                "id": 5,
                "title": "The Death Zone: What Happens to the Human Body Above 8,000 Meters",
                "tier": "Tier 2: The Death Zone & High-Altitude Mountaineering",
                "angle": "extreme_case",
                "slug": "the_death_zone_8000_meters_hypoxia_hace_hape_everest",
                "question": "Why does human tissue slowly die above 26,000 feet, where ambient oxygen is only one-third of sea level pressure?",
                "key_focus": "High Altitude Cerebral Edema (HACE), High Altitude Pulmonary Edema (HAPE), supplementary oxygen bottle flow rates, why rescues are impossible.",
                "reason": "The biological reality of extreme altitude that tests every high-altitude mountaineer to the limit."
            },
            {
                "id": 6,
                "title": "The 1996 Mount Everest Disaster: How Ambition, Commercialization, and a Blizzard Killed 8 Climbers",
                "tier": "Tier 2: The Death Zone & High-Altitude Mountaineering",
                "angle": "documentary_stories",
                "slug": "everest_1996_disaster_rob_hall_scott_fischer_hillary_step_bottleneck",
                "question": "How did rival commercial expedition leaders Rob Hall and Scott Fischer get trapped on the South Summit past the 2:00 PM turnaround time?",
                "key_focus": "Hillary Step bottleneck delays, Jon Krakauer's Into Thin Air account, Anatoli Boukreev heroic rescues, Beck Weathers surviving two nights frozen.",
                "reason": "The definitive turning point in commercial mountaineering, risk assessment, and turnaround discipline."
            },
            {
                "id": 7,
                "title": "Sherpa Genetics: The 6,000-Year Evolutionary Mutation That Conquered Everest",
                "tier": "Tier 2: The Death Zone & High-Altitude Mountaineering",
                "angle": "technology_innovation",
                "slug": "sherpa_genetics_epas1_mutation_mitochondrial_efficiency_high_altitude",
                "question": "Why do Himalayan Sherpas perform grueling physical labor in the death zone without thick blood or elevated hematocrit risks?",
                "key_focus": "EPAS1 gene variant inherited from Denisovans, enhanced capillary density, superior mitochondrial ATP production per oxygen molecule.",
                "reason": "Highlights the indigenous, genetically gifted heroes who make all commercial Himalayan mountaineering possible."
            },
            {
                "id": 8,
                "title": "K2: The Savage Mountain That Kills One in Every Four Who Reach the Summit",
                "tier": "Tier 2: The Death Zone & High-Altitude Mountaineering",
                "angle": "famous_examples",
                "slug": "k2_savage_mountain_bottleneck_serac_avalanche_abruzzi_spur",
                "question": "Why is the world's second-tallest peak exponentially more deadly, technical, and brutal than Mount Everest?",
                "key_focus": "The Bottleneck couloir beneath a 300-foot hanging serac, Karakoram unpredictable weather, vertical technical ice climbing, 2008 disaster.",
                "reason": "Revered by elite mountaineers as the ultimate test of pure alpine climbing mastery."
            },
            {
                "id": 9,
                "title": "The Lost City of Z: Percy Fawcett's Obsession and Disappearance in the Amazon",
                "tier": "Tier 3: Jungles, Deserts & Deep Spelunking",
                "angle": "hidden_stories",
                "slug": "lost_city_of_z_percy_fawcett_disappearance_xingu_amazon",
                "question": "Did a legendary British surveyor vanish into the Mato Grosso jungle seeking an advanced ancient civilization that really existed?",
                "key_focus": "Kuhikugu archaeological earthworks, terra preta black soil fertility, 1925 disappearance in the Xingu river basin, hundreds dying in rescue searches.",
                "reason": "The quintessential jungle exploration enigma bridging Victorian obsession with modern Amazonian archaeology."
            },
            {
                "id": 10,
                "title": "Crossing the Empty Quarter: Wilfred Thesiger and the Bedouin in the Rub' al Khali",
                "tier": "Tier 3: Jungles, Deserts & Deep Spelunking",
                "angle": "documentary_stories",
                "slug": "wilfred_thesiger_empty_quarter_rub_al_khali_bedouin_survival",
                "question": "How did an eccentric British adventurer traverse 250,000 square miles of hyper-arid sand dunes on camels with only water skins and dates?",
                "key_focus": "Arabian Sands memoir, navigating moving barchan dunes, finding ancient wells tasting of camel urine, Bedu hospitality and survival honor.",
                "reason": "Poignant, unforgettable chronicle of the ultimate desert crossing before oil changed Arabia forever."
            },
            {
                "id": 11,
                "title": "Nutty Putty Cave: The 28-Hour Agony of John Edward Jones",
                "tier": "Tier 3: Jungles, Deserts & Deep Spelunking",
                "angle": "incident_timeline",
                "slug": "nutty_putty_cave_john_edward_jones_trapped_upside_down_rescue",
                "question": "How did an experienced 26-year-old caver get stuck upside-down in an unmapped 10x18-inch fissure where physics prevented rescue?",
                "key_focus": "Inverted suspension trauma, pulley system failure in soft clay, heroic efforts of 137 rescue workers, sealing the cave as a permanent tomb.",
                "reason": "One of the most terrifying, widely analyzed spelunking survival tragedies in modern history."
            },
            {
                "id": 12,
                "title": "The Darién Gap: The 60 Miles of Impassable Jungle Dividing the Americas",
                "tier": "Tier 3: Jungles, Deserts & Deep Spelunking",
                "angle": "field_vs_lab",
                "slug": "darien_gap_panama_colombia_impassable_jungle_pan_american_highway",
                "question": "Why is the 30,000-mile Pan-American Highway from Alaska to Argentina broken only by a roadless expanse of swamp and jungle?",
                "key_focus": "Atrato swamp wetlands, venomous fer-de-lance vipers, historical Trans-Darién expedition attempts (Range Rovers winched through mud), modern migrant routes.",
                "reason": "The most formidable natural geographic barrier in the Western Hemisphere."
            },
            {
                "id": 13,
                "title": "The 1968 Sunday Times Golden Globe Race: The Madness of Solo Non-Stop Sailing",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "rise_fall",
                "slug": "golden_globe_race_1968_donald_crowhurst_robin_knox_johnston",
                "question": "How did the first solo non-stop around-the-world yacht race drive Donald Crowhurst to fake his logs and leap into the Atlantic?",
                "key_focus": "Robin Knox-Johnston 312 days on wooden boat Suhaili, Bernard Moitessier abandoning the race to 'save his soul' in Tahiti, Crowhurst's diary descent.",
                "reason": "A psychological and maritime masterpiece about isolation, ego, and the terrifying expanse of the open ocean."
            },
            {
                "id": 14,
                "title": "Alone on the Ice: Douglas Mawson's 100-Mile Solo Antarctic Death March",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "famous_examples",
                "slug": "douglas_mawson_antarctic_death_march_crevasse_survival",
                "question": "When his companion and sledge fell into a crevasse with all their food, how did Mawson trek 100 miles alone eating dog liver while his skin peeled off?",
                "key_focus": "Vitamin A toxicity (hypervitaminosis A) from Husky livers, sawing sled in half to reduce weight, falling into crevasse twice on ropes, missing ship by hours.",
                "reason": "Considered by Sir Edmund Hillary as the greatest solo survival story in human history."
            },
            {
                "id": 15,
                "title": "Free Solo: Alex Honnold and the Psychology of Zero Margin for Error",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "people_personalities",
                "slug": "free_solo_alex_honnold_el_capitan_freerider_amygdala_psychology",
                "question": "How does a human being climb 3,000 feet of sheer granite on El Capitan without ropes, where a single slip means instant death?",
                "key_focus": "The Boulder Problem karate kick, years of rehearsing moves in a journal, fMRI scans of an unresponsive amygdala fear center.",
                "reason": "Universally recognized as one of the greatest athletic and mental feats ever achieved by a single human being."
            },
            {
                "id": 16,
                "title": "The Deepest Cave on Earth: Descending 7,200 Feet into Veryovkina",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "extreme_case",
                "slug": "veryovkina_cave_abkhazia_deepest_cave_in_the_world_syphons",
                "question": "What is it like to spend weeks underground in freezing, dripping total darkness descending into the 'Everest of Caves' in Abkhazia?",
                "key_focus": "Krubera vs Veryovkina, flash floods subterranean pulses, ascending thousands of meters of single rope, hauling underground base camps.",
                "reason": "Superb exploration of Earth's true vertical subterranean frontier."
            },
            {
                "id": 17,
                "title": "Thor Heyerdahl and the Kon-Tiki: Sailing a Balsa Raft Across 4,300 Miles of Open Pacific",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "myths_vs_facts",
                "slug": "kon_tiki_thor_heyerdahl_balsa_wood_raft_polynesian_migration",
                "question": "Did six Scandinavian researchers really prove pre-Columbian South Americans could settle Polynesia by drifting on green balsa logs?",
                "key_focus": "Humboldt Current drift mechanics, Guara centerboards navigation, modern DNA proving Heyerdahl's primary migration direction wrong but contact right.",
                "reason": "Classic experimental archaeology adventure testing ancient maritime migration theories."
            },
            {
                "id": 18,
                "title": "The Endurance Found: How Underwater Drones Located Shackleton's Ship at 10,000 Feet",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "technology_innovation",
                "slug": "endurance_22_expedition_shackleton_shipwreck_found_weddell_sea",
                "question": "How did modern marine archaeologists use autonomous underwater submersibles to find a wooden ship crushed by pack ice 107 years earlier?",
                "key_focus": "SA Agulhas II icebreaker, Sabertooth hybrid underwater vehicles, zero-rot timber preservation in freezing Antarctic waters, 4K 3D photogrammetry.",
                "reason": "Bridges the golden age of heroic polar exploration with 21st-century autonomous robotic discovery."
            },
            {
                "id": 19,
                "title": "Solo Across Antarctica: Colin O'Brady, Lou Rudd, and the Unassisted Crossing Debate",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "evidence_integrity",
                "slug": "colin_obrady_lou_rudd_antarctica_crossing_leverett_glacier_controversy",
                "question": "Did American Colin O'Brady truly complete the first solo, unassisted, unsupported crossing of Antarctica in 2018?",
                "key_focus": "54 days pulling 400-pound pulk sled, 932 miles, skipping the floating ice shelves debate, National Geographic investigative critique.",
                "reason": "Examines the modern debates over strict definitions, sponsorship ethics, and purism in polar exploration."
            },
            {
                "id": 20,
                "title": "The Last Unexplored Corners of Earth: What Remains Undiscovered in 2026?",
                "tier": "Tier 4: Solo Circumnavigations & Extreme Frontier Exploration",
                "angle": "human_impact",
                "slug": "unexplored_frontiers_earth_trench_depths_subglacial_lakes_unclimbed_peaks",
                "question": "In an era of Google Earth and satellite reconnaissance, where can a human being still go where no person has ever set foot?",
                "key_focus": "Gangkhar Puensum (highest unclimbed mountain in Bhutan), subglacial Lake Ellsworth, hadal ocean trenches, unexplored Tepui cave systems.",
                "reason": "An inspiring tribute to the enduring human spirit of exploration and curiosity."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Everest Traffic Jams 2024: Record Deaths, Stolen Oxygen Bottles, and Filthy Camps",
                "trend_score": "Trending #1 (Massive Global Viral News & Mountaineering Search)",
                "angle": "incident_timeline",
                "slug": "everest_overcrowding_2024_trash_death_zone_traffic_jams",
                "why_trending": "Viral drone footage of hundreds of climbers waiting in line at 28,000 feet, microplastic pollution, and mandatory GPS chip tracking rules.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "Nimsdai Purja: 14 Peaks in 6 Months vs Assault Allegations and Oxygen Controversies",
                "trend_score": "High Ongoing Mountaineering Drama Search",
                "angle": "rise_fall",
                "slug": "nimsdai_purja_project_possible_14_peaks_controversies",
                "why_trending": "The superstar Nepali climber who shattered speed records on all 8,000m peaks facing intense investigative reporting and ethics debates.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "The Green Boots Mystery on Everest: Who Was the Famous Marker in Cave 8,500m?",
                "trend_score": "Evergreen Everest Lore CTR",
                "angle": "hidden_stories",
                "slug": "green_boots_everest_tsewang_paljor_indo_tibetan_border_police",
                "why_trending": "The tragic identity of Tsewang Paljor, an Indian border policeman who died in the 1996 blizzard, whose boots served as a waypoint for 20 years.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "K2 Winter Ascent: How 10 Nepali Climbers Accomplished the 'Impossible' Singing Together",
                "trend_score": "High Inspiring Achievement Search",
                "angle": "famous_examples",
                "slug": "k2_first_winter_ascent_nepali_team_singing_national_anthem",
                "why_trending": "January 2021 triumph when 10 Sherpas united to claim the final grand prize in high-altitude mountaineering: K2 in brutal winter.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "Lost in the Clouds: The Mysterious Disappearance of Mallory and Irvine in 1924",
                "trend_score": "High Historical Mystery Search",
                "angle": "myths_vs_facts",
                "slug": "mallory_and_irvine_1924_did_they_summit_everest_first_vestpocket_kodak",
                "why_trending": "Centenary of the 1924 expedition; the 1999 discovery of George Mallory's body and the elusive hunt for Sandy Irvine's Kodak camera.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "Titan Cave Diving: The Extreme Tech Required to Survive 300 Feet Deep in Flooded Caves",
                "trend_score": "High Danger & Technical Diving Search",
                "angle": "technology_innovation",
                "slug": "extreme_cave_diving_trimix_rebreathers_plur_cave_exploration",
                "why_trending": "Explores closed-circuit rebreathers, trimix helium gases to prevent nitrogen narcosis, and continuous guideline protocols in labyrinthine caves.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "Gangkhar Puensum: Why the World's Highest Unclimbed Mountain Will Never Be Scaled",
                "trend_score": "High Geography Curiosity CTR",
                "angle": "then_vs_now",
                "slug": "gangkhar_puensum_bhutan_highest_unclimbed_mountain_sacred_peaks",
                "why_trending": "A 24,836-foot peak in Bhutan protected by law honoring local spiritual beliefs that mountain peaks are the sacred dwellings of gods.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    },

    "035_military_history": {
        "id": "035",
        "slug": "military_history",
        "title": "Military History",
        "category": "Conflict_Power_Exploration",
        "audience": "Military Historians, Strategy Enthusiasts, Wargamers, Defense Analysts (Global)",
        "progression": [
            ("Tier 1: Classical Strategy, Phalanxes & Ancient Battlefield Logistics (Scratch / Beginner)",
             "Double envelopment tactics (Cannae), Macedonian sarissa phalanx geometry, Roman legion cohort modularity, and baggage train supply logistics."),
            ("Tier 2: The Gunpowder Revolution, Napoleonic Maneuver Warfare & Naval Broadsides (Intermediate)",
             "Tercios and trace italienne star forts, Frederick the Great oblique order, Napoleonic corps d'armée decentralization, and line-of-battle naval tactics."),
            ("Tier 3: Industrialized Attrition, Combined Arms & Blitzkrieg Dynamics (Upper Intermediate)",
             "Trench interlocking machine-gun fields, German stormtrooper infiltration tactics, 1940 Ardennes armored breakout, and carrier naval aviation."),
            ("Tier 4: Asymmetric Warfare, Nuclear Deterrence & Drone Battlefield Integration (Advanced / Expert)",
             "Counter-insurgency doctrine (COIN), mutual assured destruction (MAD) triad, precision-guided munitions, and FPV drone revolution on modern frontlines.")
        ],
        "flagship": {
            "title": "The Battle of Cannae (216 BCE): Hannibal's Masterclass in Double Envelopment",
            "angle": "beginner_explainers",
            "slug": "035_military_history_beginner_explainers_battle_of_cannae_hannibal"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Battle of Cannae (216 BCE): Hannibal's Masterclass in Double Envelopment",
                "tier": "Tier 1: Classical Strategy & Ancient Logistics",
                "angle": "beginner_explainers",
                "slug": "battle_of_cannae_216_bce_hannibal_barca_double_envelopment",
                "question": "How did Hannibal Barca lure 86,000 Roman legionaries into a convex collapsing center to surround and annihilate a numerically superior army?",
                "key_focus": "Convex-to-concave crescent withdrawal, elite African veteran flank anchors, Hasdrubal's heavy cavalry rear charge, 70,000 Roman casualties in one afternoon.",
                "reason": "Flagship launch episode; universally regarded as the tactical masterpiece of battlefield encirclement in military history."
            },
            {
                "id": 2,
                "title": "The Macedonian Phalanx: How Philip II and Alexander Built the 18-Foot Sarissa Wall",
                "tier": "Tier 1: Classical Strategy & Ancient Logistics",
                "angle": "how_it_works",
                "slug": "macedonian_phalanx_alexander_the_great_sarissa_companion_cavalry",
                "question": "How did an 18-foot two-handed pike and the 'hammer and anvil' cavalry charge shatter Greek hoplites and the Persian Empire?",
                "key_focus": "Sarissa counterbalance weights, five ranks of overlapping pike tips, syntagma 256-man formation, Companion cavalry wedge hammer.",
                "reason": "The tactical battlefield revolution that conquered the known ancient world."
            },
            {
                "id": 3,
                "title": "The Roman Legion vs The Greek Phalanx: Cynoscephalae and the Triumph of Flexibility",
                "tier": "Tier 1: Classical Strategy & Ancient Logistics",
                "angle": "famous_examples",
                "slug": "battle_of_cynoscephalae_197_bce_roman_legion_vs_macedonian_phalanx",
                "question": "Why did the seemingly unstoppable wall of Macedonian pikes collapse when confronted by Roman maniples on broken ground in 197 BCE?",
                "key_focus": "Rigidity of the phalanx on uneven terrain, Roman gladius close-quarters lethality, Titus Quinctius Flamininus rear assault, birth of Roman Mediterranean hegemony.",
                "reason": "The classic doctrine-versus-doctrine clash proving that tactical flexibility defeats brute frontal momentum."
            },
            {
                "id": 4,
                "title": "Ancient Military Logistics: How Armies Fed 50,000 Men Before Canned Food or Railroads",
                "tier": "Tier 1: Classical Strategy & Ancient Logistics",
                "angle": "history_origins",
                "slug": "ancient_military_logistics_alexander_baggage_trains_roman_grain_supply",
                "question": "Why did Napoleon say an army marches on its stomach, and how did Alexander the Great eliminate slow ox carts to create a rapid strike force?",
                "key_focus": "Donald Engels' logistical models, daily caloric and water requirements for horses and soldiers, maritime river supply routes, foraging limits.",
                "reason": "Logistics is the unglamorous backbone that actually decides wars before battles are even fought."
            },
            {
                "id": 5,
                "title": "Trace Italienne: How Gunpowder Cannon Created the Star Fort Revolution",
                "tier": "Tier 2: Gunpowder Revolution & Napoleonic Maneuver",
                "angle": "technology_innovation",
                "slug": "trace_italienne_star_forts_bastion_geometry_cannon_siege",
                "question": "Why did medieval tall stone castle walls suddenly become death traps against bronze cannon, giving birth to angled, earthen star fortresses?",
                "key_focus": "Low-profile earth-backed masonry, interlocking triangular bastions, eliminating dead zones for enfilade crossfire, Vauban's siegecraft parallels.",
                "reason": "Geometric military engineering revolution that changed siege warfare for three centuries."
            },
            {
                "id": 6,
                "title": "The Battle of Austerlitz (1805): Napoleon's Masterstroke on the Pratzen Heights",
                "tier": "Tier 2: Gunpowder Revolution & Napoleonic Maneuver",
                "angle": "famous_examples",
                "slug": "battle_of_austerlitz_1805_napoleon_battle_of_three_emperors_pratzen",
                "question": "How did Napoleon deliberately feign weakness on his right flank to bait the Austro-Russian army into abandoning the high ground?",
                "key_focus": "The Battle of the Three Emperors, Marshal Davout's forced march defense, Marshal Soult's fog-shrouded center strike, shattering the Third Coalition.",
                "reason": "Napoleon Bonaparte's tactical masterpiece and greatest military triumph."
            },
            {
                "id": 7,
                "title": "The Corps d'Armée System: How Napoleon Revolutionized Command, Movement, and Logistics",
                "tier": "Tier 2: Gunpowder Revolution & Napoleonic Maneuver",
                "angle": "how_it_works",
                "slug": "napoleonic_corps_system_decentralized_command_march_divided_fight_united",
                "question": "Why did self-contained 25,000-man combined-arms corps marching on separate roads allow the Grande Armée to outmaneuver all of Europe?",
                "key_focus": "March divided, fight united ('Bataillon Carré'), delegated subordinate marshal command, operational speed and surprise.",
                "reason": "The organizational structural revolution that birthed modern operational warfare."
            },
            {
                "id": 8,
                "title": "The Battle of Trafalgar (1805): Lord Nelson Breaking the Line at Sea",
                "tier": "Tier 2: Gunpowder Revolution & Napoleonic Maneuver",
                "angle": "documentary_stories",
                "slug": "battle_of_trafalgar_1805_lord_nelson_breaking_the_line_hms_victory",
                "question": "Why did Horatio Nelson abandon traditional parallel battle lines to charge two vertical columns directly into the Franco-Spanish broadsides?",
                "key_focus": "HMS Victory leading the weather column, raking fire through stern windows, chaotic melee gunnery, Nelson's fatal sniper wound, 100 years of British naval rule.",
                "reason": "The defining naval engagement that permanently established Britain as the undisputed ruler of the oceans."
            },
            {
                "id": 9,
                "title": "The Machine Gun & The Somme (1916): The Day Industrial Firepower Slaughtered 57,000 British Soldiers",
                "tier": "Tier 3: Industrialized Attrition & Blitzkrieg Dynamics",
                "angle": "extreme_case",
                "slug": "battle_of_the_somme_1916_maxim_machine_guns_creeping_barrage",
                "question": "Why did a week-long artillery bombardment of 1.5 million shells fail to destroy German deep concrete bunkers, leading to mass slaughter?",
                "key_focus": "Vickers and Maxim machine gun overlapping fields of fire, barbed wire entanglement belts, failure of unexploded shrapnel shells, the bloodiest day in British military history.",
                "reason": "The horrifying climax of industrialized military attrition that broke Victorian optimism forever."
            },
            {
                "id": 10,
                "title": "Stormtrooper Tactics: How Germany Solved the Trench Stalemate in 1918",
                "tier": "Tier 3: Industrialized Attrition & Blitzkrieg Dynamics",
                "angle": "technology_innovation",
                "slug": "stoßtruppen_stormtrooper_tactics_1918_kaiserschlacht_infiltration",
                "question": "How did light, mobile shock squads armed with submachine guns and flamethrowers bypass strongpoints to restore movement to the Western Front?",
                "key_focus": "Captain Willy Rohr, Georg Bruchmüller hurricane artillery bombardment, infiltration tactics bypassing strongpoints, precursor to Blitzkrieg.",
                "reason": "The tactical tactical doctrine shift from static attrition to decentralized infantry infiltration."
            },
            {
                "id": 11,
                "title": "Blitzkrieg 1940: The Ardennes Breakout and the Sickle Cut (Sichelschnitt)",
                "tier": "Tier 3: Industrialized Attrition & Blitzkrieg Dynamics",
                "angle": "famous_examples",
                "slug": "blitzkrieg_1940_fall_of_france_manstein_plan_ardennes_sedan",
                "question": "How did Erich von Manstein and Heinz Guderian push 45,000 panzers through 'impassable' forested ravines to trap the Allied armies in 10 days?",
                "key_focus": "Manstein Plan, bypassing the Maginot Line, Stuka dive-bombers as flying artillery, crossing the Meuse at Sedan, the race to the English Channel.",
                "reason": "The most stunning, rapid military campaign in modern warfare, dismantling the dominant land army of Western Europe in six weeks."
            },
            {
                "id": 12,
                "title": "The Battle of Midway (1942): Five Minutes That Changed the Pacific War",
                "tier": "Tier 3: Industrialized Attrition & Blitzkrieg Dynamics",
                "angle": "incident_timeline",
                "slug": "battle_of_midway_1942_five_minutes_dive_bombers_four_japanese_carriers",
                "question": "How did Joseph Rochefort's codebreakers and Wade McClusky's Dauntless dive bombers sink four Japanese fleet carriers in an afternoon?",
                "key_focus": "JN-25 naval code decryption (identifying 'AF' as Midway), Akagi, Kaga, Soryu, Hiryu, fateful Japanese re-arming delays on hangar decks.",
                "reason": "The decisive naval turning point of WWII and the moment aircraft carriers replaced battleships forever."
            },
            {
                "id": 13,
                "title": "The Battle of Stalingrad (1942–1943): The Meatgrinder on the Volga and Operation Uranus",
                "tier": "Tier 3: Industrialized Attrition & Blitzkrieg Dynamics",
                "angle": "documentary_stories",
                "slug": "battle_of_stalingrad_operation_uranus_encirclement_sixth_army_paulus",
                "question": "How did Chuikov's 62nd Army 'hug the enemy' in ruined factories before Zhukov launched a 1-million-man pincer to trap the German 6th Army?",
                "key_focus": "Urban rattenkrieg ('rat war') combat, Pavlov's House defense, Operation Uranus pincer crushing Romanian flanks, Field Marshal Paulus surrender.",
                "reason": "The bloodiest battle in human history (2 million casualties) and the definitive turning point of World War II in Europe."
            },
            {
                "id": 14,
                "title": "The Nuclear Triad: Land, Submarine, and Air Deterrence and Mutual Assured Destruction",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "advanced_concepts",
                "slug": "nuclear_triad_mad_deterrence_icbm_ssbn_strategic_bombers",
                "question": "How do ballistic missile submarines (SSBNs) lurking in silent ocean depths guarantee that a surprise nuclear first strike remains impossible?",
                "key_focus": "Second-strike capability, Minuteman III ICBMs, B-2 stealth bombers, Ohio/Columbia class submarines, Herman Kahn thermonuclear game theory.",
                "reason": "The grim mathematical and military architecture that has prevented great-power world war since 1945."
            },
            {
                "id": 15,
                "title": "Operation Desert Storm (1991): The 100-Hour Ground War and the Revolution in Military Affairs",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "famous_examples",
                "slug": "desert_storm_1991_revolution_in_military_affairs_schwarzkopf_left_hook",
                "question": "How did stealth F-117s, GPS guidance, SEAD air doctrine, and General Schwarzkopf's desert 'Left Hook' destroy the world's 4th largest army in 100 hours?",
                "key_focus": "Suppression of Enemy Air Defenses (SEAD), Tomahawk cruise missiles, thermal optics tank dominance (73 Easting), precision-guided munitions debut.",
                "reason": "The showcase demonstration of modern American combined-arms technological dominance."
            },
            {
                "id": 16,
                "title": "The Battle of Mogadishu (1993): Black Hawk Down and the Realities of Urban MOUT Warfare",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "incident_timeline",
                "slug": "battle_of_mogadishu_1993_black_hawk_down_super_61_urban_combat",
                "question": "What happens when an elite 45-minute capture raid descends into a 15-hour overnight perimeter defense after RPGs down two Black Hawks?",
                "key_focus": "Super 61 and Super 64 shoot-downs, Task Force Ranger and Delta Force snipers (Gordon and Shughart), urban ambush choke points, political aftermath.",
                "reason": "The benchmark modern military study in military operations on urbanized terrain (MOUT) and airframe vulnerability."
            },
            {
                "id": 17,
                "title": "Counter-Insurgency (COIN): Why Conventional Armies Struggle Against Guerrilla Fighters",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "rise_fall",
                "slug": "counter_insurgency_coin_doctrine_vietnam_algeria_afghanistan",
                "question": "Why did winning every tactical battlefield engagement fail to secure strategic victory for superpowers in Vietnam and Afghanistan?",
                "key_focus": "Mao Zedong's three-stage guerrilla warfare, David Galula's pacification theory, winning hearts and minds paradox, political will as center of gravity.",
                "reason": "Essential strategic analysis of asymmetric conflict dynamics in modern history."
            },
            {
                "id": 18,
                "title": "The FPV Drone Revolution: How $500 Quadcopters Transformed Modern Artillery and Armor",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "technology_innovation",
                "slug": "fpv_drones_warfare_ukraine_electronic_warfare_tank_vulnerability",
                "question": "How did cheap consumer racing drones armed with RPG warheads make 70-ton main battle tanks vulnerable and transform the modern trench line?",
                "key_focus": "First-Person-View (FPV) pilot piloting, analog vs digital video links, thermal spotting, electronic warfare jamming frequencies, cage armor defenses.",
                "reason": "The most profound, rapid technological disruption in land warfare since the invention of the machine gun."
            },
            {
                "id": 19,
                "title": "Electronic Warfare: The Invisible Battle Across the Electromagnetic Spectrum",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "field_vs_lab",
                "slug": "electronic_warfare_gps_spoofing_radar_jamming_sigint_battlefield",
                "question": "How do military forces blind enemy radar, sever drone command uplinks, and spoof satellite GPS navigation across entire war zones?",
                "key_focus": "Krasukha-4 and mobile EW complexes, directional RF jamming, radar cross-section spoofing, passive SIGINT direction-finding.",
                "reason": "The silent electronic war that underpins all modern missile, drone, and aircraft effectiveness."
            },
            {
                "id": 20,
                "title": "The Fog of War: Carl von Clausewitz and the Timeless Nature of Combat Friction",
                "tier": "Tier 4: Asymmetric Warfare, Nuclear Deterrence & Modern Frontlines",
                "angle": "human_impact",
                "slug": "carl_von_clausewitz_on_war_friction_fog_of_war_politics_by_other_means",
                "question": "No matter how advanced our sensors and AI become, why will human fear, exhaustion, and unpredictable friction always dominate warfare?",
                "key_focus": "Vom Kriege (On War), war as the continuation of politics by other means, the 'trinity' of passion/chance/reason, battlefield friction.",
                "reason": "The timeless philosophical and strategic foundation for understanding all armed human conflict."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Drone Warfare in Ukraine: How Fiber-Optic Tethered Drones Defeat Electronic Jamming",
                "trend_score": "Trending #1 (High Modern Military Tech News Velocity)",
                "angle": "technology_innovation",
                "slug": "fiber_optic_drones_ukraine_immune_to_electronic_warfare",
                "why_trending": "Spooling 10km of hair-thin glass fiber wire to make strike drones completely unjammable by radio-frequency EW systems.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 22,
                "title": "The Red Sea Naval War: US Navy Aegis Destroyers Firing $2M Missiles at $20k Drones",
                "trend_score": "High Modern Naval Defense Search",
                "angle": "evidence_integrity",
                "slug": "red_sea_naval_war_us_navy_destroyers_sm2_vs_houthi_drones",
                "why_trending": "The economics of naval air defense: Standard Missile-2/6 intercepts vs asymmetric cheap Houthi anti-ship cruise missiles and drones.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 23,
                "title": "Glide Bombs (FAB-1500/3000): How Standoff Satellite Wings Changed Frontline Warfare",
                "trend_score": "High Tactical Warfare Search",
                "angle": "how_it_works",
                "slug": "russian_fab_glide_bombs_umpk_wings_standoff_demolition",
                "why_trending": "Retrofitting massive Soviet unguided high-explosive iron bombs with pop-out wings and GPS guidance kits outside air-defense range.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 24,
                "title": "The Suwalki Corridor & Kaliningrad: NATO's Most Vulnerable Defense Bottleneck",
                "trend_score": "High Geopolitical & Military Analysis CTR",
                "angle": "famous_examples",
                "slug": "suwalki_corridor_nato_kaliningrad_belarus_defense_chokepoint",
                "why_trending": "The 40-mile strip between Poland and Lithuania flanked by Russian anti-access/area-denial (A2/AD) missile enclaves in Kaliningrad.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 25,
                "title": "Tanks Are Not Dead: Active Protection Systems (Trophy) and the Future of Armor",
                "trend_score": "High Military Technology Debate Search",
                "angle": "myths_vs_facts",
                "slug": "are_tanks_obsolete_trophy_active_protection_systems_radar_shot",
                "why_trending": "Rafael's Trophy radar-detecting incoming RPGs and detonating explosively formed penetrators to destroy them in mid-air.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 26,
                "title": "The Battle of Avdiivka: Dissecting the 5-Month Siege, Underground Pipes, and Attrition",
                "trend_score": "High Modern Tactical Analysis Search",
                "angle": "incident_timeline",
                "slug": "battle_of_avdiivka_siege_coke_plant_tactical_attrition_breakdown",
                "why_trending": "Detailed military breakdown of defensive fortified lines, subterranean storm sewer infiltrations, and flanking pressure.",
                "status": "TRENDING CANDIDATE"
            },
            {
                "id": 27,
                "title": "Hypersonic Missiles: The Physics of Mach 10 Maneuvering Glide Vehicles (HGV)",
                "trend_score": "High Defense Engineering CTR",
                "angle": "field_vs_lab",
                "slug": "hypersonic_missiles_glide_vehicles_scramjets_kinzhal_zircon_physics",
                "why_trending": "Evaluating plasma sheath communications blackout, thermal shielding at 3,000°C, and Patriot missile interception realities.",
                "status": "TRENDING CANDIDATE"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 031-035...")
    for folder_name, meta in BATCH_031_035.items():
        process_niche(folder_name, meta)
    update_master_readme()
    print("Batch 031-035 complete!")

if __name__ == "__main__":
    main()
