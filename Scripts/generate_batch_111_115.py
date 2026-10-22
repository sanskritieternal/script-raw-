import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_111_115 = {
    "111_cities_urbanism": {
        "id": "111",
        "slug": "cities_urbanism",
        "title": "Cities & Urbanism",
        "category": "Home_Living",
        "audience": "Urban Planners, Architects, Civil Geographers, City Dwellers, Civic Activists (Global)",
        "progression": [
            ("Tier 1: Urban Evolution, Street Grids & Human Scale (Beginner / Scratch)",
             "From ancient Jericho and Roman hippodamian grids to modern zoning laws, Jane Jacobs vs Robert Moses street philosophy, pedestrian ergonomics, and superblocks."),
            ("Tier 2: Infrastructure Systems, Densification & Public Space (Intermediate)",
             "Barcelona superilles, transit-oriented development (TOD), missing middle housing, urban heat island mitigation, and mixed-use commercial vitality."),
            ("Tier 3: Housing Crises, Gentrification & Adaptive Reuse (Upper Intermediate)",
             "Global affordability crunches, speculative property vacancy taxes, land value capture (Henry George), redlining historical impacts, and post-industrial brownfield remediation."),
            ("Tier 4: Megacities, Climate Resilience & The Future Metropolis (Advanced / Masterclass)",
             "Sponge cities against flash floods, delta urbanism (Tokyo/Rotterdam), master-planned capitals (Brasilia/Nusantara), smart sensor governance, and sustainable urban biophilia.")
        ],
        "flagship": {
            "title": "The Death and Life of Great Cities: Jane Jacobs vs Robert Moses",
            "angle": "case_study",
            "slug": "111_cities_urbanism_case_study_death_and_life_of_great_cities"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Death and Life of Great Cities: Jane Jacobs vs Robert Moses",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "death_and_life_of_great_cities",
                "question": "How did a community activist stop a Master Builder from bulldozing Lower Manhattan for an expressway?",
                "focus": "Eyes on the street, short blocks, sidewalk ballet, expressway devastation, and community resistance.",
                "reason": "Crucial foundational clash defining modern human-scale urbanism vs car-centric destruction."
            },
            {
                "id": 2,
                "title": "The Origin of the Grid: How Hippodamus and Commissioners Planned New York",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "origin_of_the_urban_grid",
                "question": "Why did New York's 1811 Commissioners' Plan carve Manhattan into 2,000 rectangular blocks?",
                "focus": "Real estate speculation, airflow, surveyor logistics, central park omission and correction.",
                "reason": "Establishes how geometry and speculative finance shaped modern world capitals."
            },
            {
                "id": 3,
                "title": "Zoning Laws and Single-Family Mandates: How Laws Shaped the Suburbs",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "zoning_laws_and_suburban_sprawl",
                "question": "Why is it illegal to build a corner cafe or a duplex in 75% of American residential land?",
                "focus": "Euclidean zoning, setback rules, minimum lot sizes, parking minimums, and car dependency.",
                "reason": "Deconstructs the invisible legal code forcing urban sprawl and segregation."
            },
            {
                "id": 4,
                "title": "Barcelona Superblocks: Giving Neighborhood Streets Back to Humans",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "famous_examples",
                "slug": "barcelona_superblocks_superilles",
                "question": "How did Barcelona divert 80% of through-traffic to perimeter streets to create quiet neighborhood plazas?",
                "focus": "Ildefons Cerdà's octagonal blocks, traffic calming, children's play corridors, and noise pollution drops.",
                "reason": "Showcases the gold standard in modern urban reclaiming of asphalt for pedestrian life."
            },
            {
                "id": 5,
                "title": "The Urban Heat Island Effect: Why Concrete Cities Trap Boiling Temperatures",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "urban_heat_island_mechanics",
                "question": "Why are downtown core temperatures 10 degrees hotter than surrounding countryside at night?",
                "focus": "Thermal mass of asphalt, albedo reflection coefficients, green canopy deficit, and air conditioning feedback loops.",
                "reason": "Connects city material science directly to climate adaptation and public health."
            },
            {
                "id": 6,
                "title": "Transit-Oriented Development (TOD): How Tokyo and Curitiba Build Around Stations",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "transit_oriented_development_tod",
                "question": "How do private railways fund transit lines by developing towering commercial hubs over train terminals?",
                "focus": "Rail plus property business model, pedestrian shed radiuses, air rights development, and farebox recovery.",
                "reason": "Teaches the self-funding real estate and transit integration that makes Japanese rail profitable."
            },
            {
                "id": 7,
                "title": "The Missing Middle Housing: Why Cities Have Skyscrapers and Mansions but Nothing In Between",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "missing_middle_housing",
                "question": "Why did brownstones, courtyard apartments, and triplexes disappear from modern city construction?",
                "focus": "Two-staircase building codes, construction finance hurdles, community NIMBYism, and density scales.",
                "reason": "Exposes the architectural missing link essential for walkable, affordable urban neighborhoods."
            },
            {
                "id": 8,
                "title": "Sponge Cities: How Wuhan and Copenhagen Absorb 500-Year Floods",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "sponge_cities_flood_resilience",
                "question": "How can permeable pavements, sunken public parks, and bioswales prevent multi-billion dollar flood disasters?",
                "focus": "Stormwater retention basins, urban wetland restoration, cloudburst boulevards, and green roofs.",
                "reason": "Highlights revolutionary civil engineering adapting coastal and riverine cities to extreme precipitation."
            },
            {
                "id": 9,
                "title": "The High Line Effect: Park Architecture and the Double-Edged Sword of Gentrification",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "high_line_effect_urban_gentrification",
                "question": "How did an abandoned elevated rail spur generate billions in luxury towers while displacing local residents?",
                "focus": "Adaptive landscape architecture, property value surges, tourism crowding, and wealth concentration.",
                "reason": "Analyzes the complex tension between high-profile public revitalization and neighborhood affordability."
            },
            {
                "id": 10,
                "title": "Parking Minimums: How Empty Spaces for Cars Destroyed Downtowns",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "parking_minimums_donald_shoup",
                "question": "Why are there 8 parking spots for every car in America while housing remains unaffordable?",
                "focus": "Donald Shoup's high cost of free parking, structured garage costs, retail vacancy, and parking reform.",
                "reason": "Deconstructs the most destructive land-use regulation in twentieth-century urban planning."
            },
            {
                "id": 11,
                "title": "Land Value Tax: Henry George's 150-Year-Old Solution to Speculation",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "philosophical_perspectives",
                "slug": "land_value_tax_henry_george",
                "question": "What happens when you tax the unimproved value of land rather than the buildings sitting on top of it?",
                "focus": "Georgism, vacant lot penalty, development incentives, Pennsylvania split-rate experiments, and economic rent.",
                "reason": "Explores the most elegant, progressive fiscal mechanism to cure urban real estate hoarding."
            },
            {
                "id": 12,
                "title": "The Redlining Legacy: How Maps Drawn in 1934 Created Modern Urban Inequity",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "historical_evolution",
                "slug": "redlining_legacy_urban_inequity",
                "question": "How did the Home Owners' Loan Corporation mortgage grading maps institutionalize racial segregation for a century?",
                "focus": "HOLC color-coded maps, highway demolition through minority neighborhoods, tree canopy disparities, and generational wealth gaps.",
                "reason": "Essential historical investigation into systemic structural injustice embedded in city geography."
            },
            {
                "id": 13,
                "title": "Master-Planned Disasters: Brasilia, Chandigarh, and the Failure of Radiant Cities",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "failure_mode_analysis",
                "slug": "master_planned_cities_brasilia_chandigarh",
                "question": "Why did Le Corbusier and Oscar Niemeyer's utopian geometric capitals become lifeless, car-choked wastelands?",
                "focus": "Monumental scale arrogance, lack of spontaneous street life, pedestrian hostility, and satellite slum growth.",
                "reason": "Rigorous critique of top-down modernist urban planning divorced from human psychology."
            },
            {
                "id": 14,
                "title": "Tokyo's Zoning Secret: How Japan Avoided the Housing Affordability Crisis",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "tokyo_zoning_housing_affordability",
                "question": "Why does Tokyo build more housing units per year than California while keeping rent affordable for decades?",
                "focus": "Nationalized 12-zone hierarchy, as-of-right development, elimination of local municipal vetoes, and micro-studios.",
                "reason": "Shows how national regulatory reform creates abundant housing in the world's largest metropolis."
            },
            {
                "id": 15,
                "title": "The Subterranean City: Underground Tunnels, Sewers, and Utilities in Montreal and London",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "subterranean_city_underground_networks",
                "question": "How do underground pedestrian cities like Montreal's RESO keep 500,000 citizens moving comfortably in -20°C blizzards?",
                "focus": "Sub-surface right-of-ways, utility conduits, Victorian sewer engineering, and underground mall connectivity.",
                "reason": "Explores the vertical downward expansion of modern urban centers under extreme climates."
            },
            {
                "id": 16,
                "title": "Delta Megacities: How Tokyo, Rotterdam, and New Orleans Defend Against Sea-Level Rise",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "delta_megacities_sea_level_defense",
                "question": "How does Tokyo's underground G-Cans cathedral discharge 200 tons of floodwater per second into Tokyo Bay?",
                "focus": "Storm surge storm gates (Maeslantkering), levee subsiding, saltwater intrusion, and floating architecture.",
                "reason": "Examines monumental mega-engineering protecting coastal civilization from oceanic threats."
            },
            {
                "id": 17,
                "title": "Building New Capitals: Nusantara, Egypt's New Administrative Capital, and Songdo",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "comparative_analysis",
                "slug": "new_capital_cities_nusantara_egypt",
                "question": "Why are nations spending hundreds of billions carving brand-new smart capitals out of jungles and deserts?",
                "focus": "Jakarta sinking dynamics, Cairo congestion relief, IoT sensor infrastructure, and empty luxury city risks.",
                "reason": "Analyzes the high-stakes geopolitical gambles of 21st-century master-planned capital construction."
            },
            {
                "id": 18,
                "title": "Smart Cities and Surveillance Capitalism: Did the Sidewalk Toronto Experiment Fail?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "smart_cities_surveillance_sidewalk_labs",
                "question": "Why did Google's urban subsidiary abandon its high-tech waterfront smart city in Toronto amidst public outrage?",
                "focus": "Data governance, biometric tracking sensors, intellectual property disputes, and civic privatization fears.",
                "reason": "Critically examines the limits of corporate tech platforms trying to rule municipal civic space."
            },
            {
                "id": 19,
                "title": "Biophilic Urbanism: Integrating Living Forests into High-Rise Architecture",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "biophilic_urbanism_vertical_forests",
                "question": "Can Stefano Boeri's Bosco Verticale and Singapore's Supertrees genuinely clean air and lower city temperatures?",
                "focus": "Vertical forest irrigation maintenance, structural root barriers, bird biodiversity corridors, and urban well-being.",
                "reason": "Explores the ecological synthesis blending living natural ecosystems into concrete city skylines."
            },
            {
                "id": 20,
                "title": "The Master Urban Architecture: Designing the 100-Year Resilient City",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "resilient_city_master_urban_architecture",
                "question": "What comprehensive planning framework unites transit, housing abundance, flood resilience, and civic joy?",
                "focus": "Holistic master-planning, circular municipal waste/water loops, human-scale street design, and adaptable zoning codes.",
                "reason": "Capstone masterclass synthesizing all 20 urbanism episodes into a visionary urban roadmap for the next century."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Indonesia is Abandoning Jakarta to Build a Brand New Jungle Capital",
                "trend_score": "Massive Global Curiosity Spike",
                "angle": "case_study",
                "slug": "indonesia_abandoning_jakarta_nusantara",
                "why_trending": "Jakarta is sinking into the sea faster than Venice, prompting a $35B scramble to build Nusantara in Borneo.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Tokyo's Underground Storm Cathedral: The Mind-Blowing G-Cans Flood Defense",
                "trend_score": "Viral Visual Fascination (High Retention)",
                "angle": "field_investigation",
                "slug": "tokyo_g_cans_underground_flood_cathedral",
                "why_trending": "Massive 70-foot concrete pillars beneath suburban Tokyo look like an alien sci-fi temple.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The Line in Saudi Arabia: Can a 170-Kilometer Mirror City Actually Be Built?",
                "trend_score": "Extremely High Search Volume",
                "angle": "systemic_critique",
                "slug": "saudi_arabia_the_line_neom_reality_check",
                "why_trending": "NEOM's scaling back of construction phases ignited global debate on megalomaniac architecture.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why European Cities Are Tearing Down Highway Overpasses to Build Canals",
                "trend_score": "High Urbanism Interest",
                "angle": "famous_examples",
                "slug": "tearing_down_urban_highways_utrecht",
                "why_trending": "Utrecht and Seoul restoring historic waterways over demolished urban freeways sparked copycats worldwide.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Why America Stopped Building Missing Middle Housing: The Staircase Law",
                "trend_score": "Housing Policy Viral Debate",
                "angle": "root_cause_analysis",
                "slug": "single_staircase_housing_regulations",
                "why_trending": "Architects exposing how double-staircase requirements ruin small apartment layouts went viral on YouTube.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Inside Egypt's $60 Billion Desert Megacity: Why Move Out of Cairo?",
                "trend_score": "High Geopolitical Search Spike",
                "angle": "deep_dive",
                "slug": "egypt_new_administrative_capital_desert",
                "why_trending": "Examines the towering skyscrapers, massive defense Pentagon, and debt behind the new capital.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "How Singapore Solved Public Housing: Why 80% of Citizens Live in Government Flats",
                "trend_score": "Evergreen High Retention Hook",
                "angle": "economic_breakdown",
                "slug": "singapore_hdb_public_housing_model",
                "why_trending": "Deconstructs the world's most successful public housing corporation where HDB apartments appreciate as assets.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "112_real_estate": {
        "id": "112",
        "slug": "real_estate",
        "title": "Real Estate",
        "category": "Finance_Banking",
        "audience": "Property Investors, First-Time Homebuyers, Mortgage Brokers, Commercial Developers, RE Analysts (Global)",
        "progression": [
            ("Tier 1: Property Valuation, Cap Rates & Mortgage Mechanics (Beginner / Scratch)",
             "Discounted cash flow, Net Operating Income (NOI), Capitalization Rates (Cap Rates), 30-year fixed mortgages, amortization schedules, and title insurance."),
            ("Tier 2: Commercial Asset Classes, Syndications & Value-Add Playbooks (Intermediate)",
             "Multifamily vs industrial vs retail, real estate syndication waterfalls, BRRRR method (Buy, Rehab, Rent, Refinance, Repeat), 1031 tax-deferred exchanges, and lease structures (Triple Net / NNN)."),
            ("Tier 3: Institutional Capital, REITs & Debt Securitization (Upper Intermediate)",
             "Commercial Mortgage-Backed Securities (CMBS), Real Estate Investment Trusts (REITs), mezzanine financing, debt-service coverage ratios (DSCR), and distressed asset workouts."),
            ("Tier 4: Macro Cycles, Demographic Shifts & Tokenized Property (Advanced / Masterclass)",
             "Homer Hoyt 18-year real estate cycle, demographic flight corridors, climate risk insurance insolvency, proptech fractionalization, and multi-billion development underwriting.")
        ],
        "flagship": {
            "title": "The Anatomy of a Real Estate Deal: How $10M Buildings Are Bought with 10% Down",
            "angle": "beginner_guide",
            "slug": "112_real_estate_beginner_guide_anatomy_of_a_real_estate_deal"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Anatomy of a Real Estate Deal: How $10M Buildings Are Bought with 10% Down",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "anatomy_of_a_real_estate_deal",
                "question": "How do real estate investors use bank leverage, debt coverage, and equity syndication to acquire multi-million dollar assets?",
                "focus": "Loan-to-Value (LTV), equity capital stacks, mortgage covenants, and deal closing economics.",
                "reason": "Crucial foundational episode demystifying how real estate transactions are actually structured and financed."
            },
            {
                "id": 2,
                "title": "Cap Rates Decoded: The Most Important Number in Commercial Real Estate",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "cap_rates_valuation_mechanics",
                "question": "Why does a 1% shift in Capitalization Rate alter the market value of a building by millions of dollars?",
                "focus": "Net Operating Income (NOI), cap rate compression vs expansion, treasury bond spreads, and risk premiums.",
                "reason": "Teaches the universal mathematical valuation metric used across commercial property."
            },
            {
                "id": 3,
                "title": "Rent vs Buy: The Mathematical Truth Behind Homeownership",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "rent_vs_buy_mathematical_analysis",
                "question": "Is buying a home always the best financial investment, or does renting and investing the difference win?",
                "focus": "Opportunity cost of down payment, property taxes, maintenance capital reserves, amortization drag, and inflation hedges.",
                "reason": "Debunks emotional myths around residential property with rigorous financial accounting."
            },
            {
                "id": 4,
                "title": "The 1031 Exchange: The Wealth Engine That Defers Capital Gains Forever",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "practical_playbook",
                "slug": "1031_exchange_tax_deferral",
                "question": "How do billionaire property moguls roll profits from small duplexes into skyscrapers without paying capital gains tax?",
                "focus": "Like-kind property rules, 45-day identification windows, qualified intermediaries, and 'swap until you drop' estate step-up.",
                "reason": "Explains the single most powerful tax shelter fueling American real estate wealth compounding."
            },
            {
                "id": 5,
                "title": "Triple Net Leases (NNN): The Passive Cash Flow Holy Grail of Fast Food and Pharmacies",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "triple_net_nnn_leases_explained",
                "question": "Why do family offices buy standalone Dollar General and Walgreens buildings for zero-headache monthly dividends?",
                "focus": "Tenant obligations (taxes, insurance, maintenance), lease terms (15-20 years), corporate credit backing, and bond-proxy stability.",
                "reason": "Introduces beginner investors to the mechanics of hands-off commercial property cash flow."
            },
            {
                "id": 6,
                "title": "The BRRRR Method: How Small Investors Scale Rental Portfolios with Zero Money Left In",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "brrrr_method_rental_portfolio_scale",
                "question": "How does Buy, Rehab, Rent, Refinance, Repeat allow investors to recycle the same initial capital repeatedly?",
                "focus": "Forced appreciation, hard money loans, cash-out refinancing underwriting, and appraisal management.",
                "reason": "Provides a step-by-step breakdown of the most popular residential wealth-building strategy."
            },
            {
                "id": 7,
                "title": "Multifamily Syndications: How Real Estate Fund Managers Pool Capital and Take 20% Carried Interest",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "multifamily_syndication_waterfalls",
                "question": "What is a waterfall equity split, preferred return, and sponsor promote in private real estate syndications?",
                "focus": "General Partner (GP) vs Limited Partner (LP) duties, PPM disclosures, preferred hurdle rates, and acquisition fees.",
                "reason": "Deconstructs the institutional structure behind apartment complex syndication."
            },
            {
                "id": 8,
                "title": "Industrial Warehouses: The Unsexy Asset Class That Crushed Office Buildings",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "industrial_warehouse_logistics_real_estate",
                "question": "Why did Prologis and Blackstone pour hundreds of billions into drab concrete distribution centers near interstate exits?",
                "focus": "Clear ceiling heights, dock-high doors, e-commerce last-mile demand, and low tenant turnover costs.",
                "reason": "Analyzes the massive secular boom in logistics and supply chain real estate."
            },
            {
                "id": 9,
                "title": "The Commercial Office Meltdown: What Happens When Skyscrapers Sit 50% Empty?",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "failure_mode_analysis",
                "slug": "commercial_office_building_crisis",
                "question": "Why are Class-B and Class-C office towers in downtown San Francisco and Chicago selling for 80% discounts?",
                "focus": "Remote work vacancy rates, non-recourse debt hand-backs to lenders, converting offices to residential, and regional bank exposure.",
                "reason": "Investigates the unfolding historic repricing in downtown commercial office buildings."
            },
            {
                "id": 10,
                "title": "Real Estate Investment Trusts (REITs): Wall Street's Liquid Real Estate Market",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "reits_public_vs_private_real_estate",
                "question": "Should you buy physical rental houses or invest in publicly traded dividend REITs like Realty Income (O)?",
                "focus": "90% taxable income distribution rule, NAV discounts/premiums, stock market liquidity, and management overhead.",
                "reason": "Contrasts direct property ownership with liquid publicly traded commercial portfolios."
            },
            {
                "id": 11,
                "title": "The 18-Year Real Estate Cycle: Homer Hoyt's Predictive Clock",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "historical_evolution",
                "slug": "18_year_real_estate_cycle_homer_hoyt",
                "question": "Why has the real estate market followed a remarkably consistent 18-year boom-bust cadence for two centuries?",
                "focus": "Recovery, expansion, hyper-supply, and recession phases; Fred Harrison's cycle timing, and land speculation peaks.",
                "reason": "Teaches macro cycle forecasting to prevent catastrophic timing mistakes during market peaks."
            },
            {
                "id": 12,
                "title": "Commercial Debt Securitization: How CMBS Works and Why It Spreads Contagion",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "cmbs_debt_securitization_mechanics",
                "question": "How do commercial banks slice property mortgages into tranched bonds for pension funds and insurance companies?",
                "focus": "Senior AAA vs junior unrated tranches, special servicers, defeasance fees, and maturity refinancing walls.",
                "reason": "Demystifies the multi-trillion dollar Wall Street bond machinery behind commercial property loans."
            },
            {
                "id": 13,
                "title": "Property Insurance Insolvency: Why Insurers Are Fleeing Florida and California",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "property_insurance_crisis_florida_california",
                "question": "What happens to home values and mortgages when annual hurricane and wildfire insurance premiums exceed mortgage payments?",
                "focus": "Citizens Property Insurance state backstops, reinsurance costs, climate risk underwriting, and uninsurable property markets.",
                "reason": "Examines the existential insurance bottleneck threatening sunbelt and western real estate markets."
            },
            {
                "id": 14,
                "title": "Land Banking and Entitlement: The Highest Returns in Real Estate Development",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "field_investigation",
                "slug": "land_entitlement_development_returns",
                "question": "How do developers buy raw dirt for $50,000 an acre and sell it for $500,000 an acre without laying a single brick?",
                "focus": "Rezoning approvals, environmental impact statements (EIRs), utility hookup agreements, and political lobbying.",
                "reason": "Reveals the secretive high-margin world of municipal land entitlement and paper development."
            },
            {
                "id": 15,
                "title": "Manufactured Housing and Mobile Home Parks: The Recession-Proof Cash Flow Machine",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "mobile_home_parks_investment_strategy",
                "question": "Why did private equity firms like Carlyle and Blackstone quietly purchase thousands of mobile home parks?",
                "focus": "Tenant-owned homes, lot rent margins, extreme tenant retention (cost to move a mobile home), and municipal supply restrictions.",
                "reason": "Deconstructs the contrarian, high-yielding niche of affordable land-lease communities."
            },
            {
                "id": 16,
                "title": "The Great Sunbelt Migration: How Taxes, Air Conditioning, and Costs Reshaped the US Map",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "sunbelt_migration_real_estate_shift",
                "question": "Why did millions of residents and corporate headquarters move from New York and California to Texas and Florida?",
                "focus": "Zero state income taxes, business deregulation, pro-growth housing permitting, and demographic momentum.",
                "reason": "Analyzes the generational geographic realignment of capital, labor, and real estate equity."
            },
            {
                "id": 17,
                "title": "Tokenized Real Estate and Blockchain Deeds: Disruption or Unnecessary Complexity?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "tokenized_real_estate_blockchain_deeds",
                "question": "Can security token offerings (STOs) democratize fractional commercial property ownership and eliminate title insurance?",
                "focus": "Smart contract rent distributions, secondary market liquidity, legal jurisdiction compliance, and deed registry friction.",
                "reason": "Provides a grounded, critical evaluation of blockchain applications in property markets."
            },
            {
                "id": 18,
                "title": "Corporate Landlords and Institutional Single-Family Homes: The Housing Debate",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "institutional_single_family_rental_homes",
                "question": "Are Wall Street giants like Invitation Homes locking first-time families out of the American Dream?",
                "focus": "Build-to-rent communities, algorithmic bidding, maintenance management platforms, and legislative ban proposals.",
                "reason": "Tackles the intense socioeconomic and political controversy surrounding institutional single-family rentals."
            },
            {
                "id": 19,
                "title": "Distressed Debt and Note Buying: How Predators Profit from Real Estate Foreclosures",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "distressed_debt_note_buying_strategy",
                "question": "How do debt funds buy defaulted mortgage paper at 40 cents on the dollar and take over landmark buildings?",
                "focus": "Loan-to-own strategies, non-performing note auctions, judicial vs non-judicial foreclosure, and deed-in-lieu workouts.",
                "reason": "Exposes the ruthless vulture capital mechanics operating during real estate downturns."
            },
            {
                "id": 20,
                "title": "The Master Real Estate Portfolio Architecture: Building Multi-Generational Wealth",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_real_estate_portfolio_architecture",
                "question": "What comprehensive strategic framework balances leverage, asset class diversification, tax shielding, and risk management?",
                "focus": "End-to-end portfolio construction, entity structuring (LLCs/Trusts), cost segregation depreciation, and generational wealth transfer.",
                "reason": "Synthesizes the entire 20-episode real estate curriculum into an elite investor's masterclass."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Commercial Office Crash: Why Billion-Dollar Towers Are Selling for $1",
                "trend_score": "Massive Business Curiosity Spike",
                "angle": "case_study",
                "slug": "office_towers_selling_for_huge_losses",
                "why_trending": "Iconic downtown skyscrapers selling for less than the cost of their land captivated financial media.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The Florida Insurance Meltdown: Why Homeowners Are Abandoning the State",
                "trend_score": "Huge Consumer Concern Spike",
                "angle": "root_cause_analysis",
                "slug": "florida_home_insurance_crisis_explained",
                "why_trending": "Skyrocketing premiums and insurer insolvencies are freezing sales across coastal Florida markets.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why Buying a House is Now Twice as Expensive as Renting in Most Cities",
                "trend_score": "Extremely High Search Volume",
                "angle": "economic_breakdown",
                "slug": "housing_affordability_mortgage_rate_shock",
                "why_trending": "7% mortgage rates combined with record-high home prices created the worst affordability index in 40 years.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The 6% Realtor Commission Settlement: How the NAR Lawsuit Changes Home Buying",
                "trend_score": "National Industry Realignment",
                "angle": "deep_dive",
                "slug": "nar_commission_settlement_realtor_fees",
                "why_trending": "The landmark antitrust settlement ending mandatory buyer agent commissions disrupted 1.5 million agents.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Squatters Hijacking Luxury Homes: The Legal Loophole Terrifying Landlords",
                "trend_score": "Viral Outrage & High Retention",
                "angle": "field_investigation",
                "slug": "squatters_rights_property_law_loopholes",
                "why_trending": "Wild stories of unauthorized occupants claiming tenant rights in million-dollar mansions shocked homeowners.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Cost Segregation and Bonus Depreciation: The Tax Hack Saving Millionaires Millions",
                "trend_score": "High Real Estate Investor Traffic",
                "angle": "practical_playbook",
                "slug": "cost_segregation_bonus_depreciation_tax_hack",
                "why_trending": "Accelerating 20-year building depreciation into Year 1 against ordinary income became an investor obsession.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The Airbnb Bust: Why Short-Term Rental Hosts Are Panic-Selling Properties",
                "trend_score": "High Social Media Trend",
                "angle": "failure_mode_analysis",
                "slug": "airbnb_bust_short_term_rental_selloff",
                "why_trending": "City bans in NYC, cleaning fee pushback, and falling occupancy rates ended the easy-money Airbnb era.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "113_energy_power": {
        "id": "113",
        "slug": "energy_power",
        "title": "Energy & Power",
        "category": "Energy_Industry",
        "audience": "Electrical Engineers, Energy Traders, Utility Regulators, Climate Tech Observers, Industrial Planners (Global)",
        "progression": [
            ("Tier 1: Thermodynamics, Grid Physics & Fossil Fundamentals (Beginner / Scratch)",
             "First and second laws of thermodynamics, AC vs DC War of Currents (Tesla vs Edison), coal and combined cycle natural gas turbines, 50Hz/60Hz frequency balancing, and transformer substations."),
            ("Tier 2: Nuclear Fission, Hydroelectric Giants & Baseload Reliability (Intermediate)",
             "Pressurized water reactors (PWR), pumped storage hydro batteries, levelized cost of energy (LCOE), spinning reserves, and high-voltage direct current (HVDC) transmission lines."),
            ("Tier 3: The Renewable Inversion: Solar Photovoltaics, Wind & Grid Duck Curves (Upper Intermediate)",
             "Silicon PV bandgap physics, offshore wind nacelles, California duck curve overgeneration, lithium-ion grid storage, and wholesale nodal pricing markets (ERCOT/PJM)."),
            ("Tier 4: Nuclear Fusion, SMRs & The Net-Zero Supergrid (Advanced / Masterclass)",
             "Small Modular Reactors (SMRs), magnetic confinement tokamak fusion, green hydrogen electrolysis, geothermal enhanced systems (EGS), and the master transcontinental supergrid.")
        ],
        "flagship": {
            "title": "The War of Currents: How Tesla and Westinghouse Electrified the Earth",
            "angle": "historical_evolution",
            "slug": "113_energy_power_historical_evolution_war_of_currents_tesla_edison"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The War of Currents: How Tesla and Westinghouse Electrified the Earth",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "war_of_currents_tesla_edison",
                "question": "How did Nikola Tesla's alternating current defeat Thomas Edison's direct current to build the world's power grids?",
                "focus": "Transformer step-up voltage physics, copper line resistance losses, Niagara Falls power plant, and public electrocution propaganda.",
                "reason": "Crucial foundational episode introducing the electrical architecture powering modern civilization."
            },
            {
                "id": 2,
                "title": "The Physics of the Electric Grid: Why 60 Hertz Frequency Must Never Fail",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "physics_of_the_electric_grid_frequency",
                "question": "What happens when electricity consumption does not match generation down to the exact millisecond?",
                "focus": "Grid inertia, rotational kinetic energy in turbines, frequency deviations, automatic under-frequency load shedding, and blackouts.",
                "reason": "Teaches the fundamental thermodynamic law: electricity cannot be easily buffered on transmission wires."
            },
            {
                "id": 3,
                "title": "Combined Cycle Natural Gas: The Workhorse of Modern Baseload Power",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "combined_cycle_gas_turbines",
                "question": "How do combined cycle power plants achieve 60%+ thermodynamic efficiency using waste heat?",
                "focus": "Brayton cycle gas turbines, Heat Recovery Steam Generators (HRSG), Rankine steam cycles, and peaker plant economics.",
                "reason": "Deconstructs the most prevalent and flexible fossil generation technology in the global power mix."
            },
            {
                "id": 4,
                "title": "Transformer Substations and High-Voltage Transmission: Moving Megawatts Across Continents",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "transformer_substations_hvdc",
                "question": "Why do transmission lines carry 765,000 volts across states only to step it down to 120 volts at your wall socket?",
                "focus": "Ohm's law, Joulean heating losses (I^2*R), step-up/step-down transformers, SF6 switchgear, and coronal discharge.",
                "reason": "Details the essential high-voltage transmission plumbing linking distant generators to cities."
            },
            {
                "id": 5,
                "title": "Levelized Cost of Energy (LCOE): How Wall Street Calculates the Cheapest Megawatt",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "economic_breakdown",
                "slug": "levelized_cost_of_energy_lcoe",
                "question": "How do utility analysts compare the true lifetime cost of solar panels, nuclear reactors, and coal plants?",
                "focus": "Capital expenditures (capex), operating expenses (opex), capacity factors, discount rates, and decommissioning liabilities.",
                "reason": "Provides the universal financial yardstick used by investors and energy regulators."
            },
            {
                "id": 6,
                "title": "Nuclear Fission Engineering: Inside a Pressurized Water Reactor (PWR)",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "nuclear_fission_pressurized_water_reactor",
                "question": "How do uranium fuel pellets generate gigawatts of carbon-free steam for two years straight without refueling?",
                "focus": "U-235 fission chain reactions, neutron moderators, control rod scrams, primary vs secondary coolant loops, and containment domes.",
                "reason": "Masterclass on the physics, safety redundancies, and thermal mechanics of commercial nuclear power."
            },
            {
                "id": 7,
                "title": "Hydroelectric Giants: The Engineering of Hoover Dam and Three Gorges",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "hydroelectric_power_hoover_three_gorges",
                "question": "How does the kinetic weight of billions of gallons of river water spin Francis turbines to power entire nations?",
                "focus": "Gravitational potential energy, penstock water hammer pressure, cavitation wear, and seasonal reservoir management.",
                "reason": "Examines the largest renewable power source and mechanical feats of civil hydraulic engineering."
            },
            {
                "id": 8,
                "title": "The Duck Curve: Why Solar Energy Breaks the Electric Grid at Sunset",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "failure_mode_analysis",
                "slug": "california_duck_curve_solar_grid",
                "question": "Why does midday solar overgeneration cause electricity prices to go negative, followed by extreme evening price spikes?",
                "focus": "Net load curves, rapid ramping requirements for gas peakers, solar curtailment, and grid strain.",
                "reason": "Deconstructs the defining operational challenge facing modern high-renewable grids."
            },
            {
                "id": 9,
                "title": "Pumped Storage Hydropower: The Forgotten Giant of Global Energy Storage",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "pumped_storage_hydropower_batteries",
                "question": "Why does 90% of the world's energy storage capacity consist of two water reservoirs at different elevations?",
                "focus": "Reversible pump-turbines, round-trip efficiency (70-80%), black start capability, and topographic site scarcity.",
                "reason": "Highlights the massive gravitational battery infrastructure dwarfing all lithium-ion installations combined."
            },
            {
                "id": 10,
                "title": "Wholesale Electricity Markets: How ERCOT and PJM Set Power Prices Every 5 Minutes",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "wholesale_electricity_markets_ercot_pjm",
                "question": "How do algorithmic auctions balance supply, demand, and transmission congestion across thousands of grid nodes?",
                "focus": "Locational Marginal Pricing (LMP), capacity markets vs energy-only markets, reserve margin adequacy, and market manipulation.",
                "reason": "Reveals the financial and mathematical trading architecture running behind national power grids."
            },
            {
                "id": 11,
                "title": "Solar Photovoltaic Physics: From Silicon Sand to Free Photons",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "solar_photovoltaic_physics_swanson_law",
                "question": "How does the photoelectric effect in doped p-n silicon junctions knock electrons free to generate electric current?",
                "focus": "Shockley-Queisser limit, mono-crystalline vs poly-crystalline, Swanson's law price crashes, and perovskite tandem cells.",
                "reason": "Explains the physics and manufacturing scale that made solar the cheapest electricity in human history."
            },
            {
                "id": 12,
                "title": "Offshore Wind Megastructures: 15-Megawatt Giants Anchored in the Ocean",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "offshore_wind_turbine_engineering",
                "question": "How do engineers erect 850-foot wind turbines with 350-foot carbon fiber blades in tempestuous ocean waters?",
                "focus": "Monopile vs jacket foundations, floating tension-leg platforms, direct-drive permanent magnet generators, and subsea cabling.",
                "reason": "Explores the cutting-edge heavy marine engineering unlocking high-capacity ocean wind corridors."
            },
            {
                "id": 13,
                "title": "Grid-Scale Battery Storage: Lithium Iron Phosphate vs Flow Batteries",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "grid_scale_battery_storage_chemistries",
                "question": "Can multi-megawatt battery installations provide 4-hour, 8-hour, or multi-day baseload backup for renewable grids?",
                "focus": "LFP thermal runaway resistance, vanadium redox flow batteries, iron-air 100-hour storage, and degradation cycles.",
                "reason": "Assesses the chemical energy storage frontier competing to smooth renewable intermittency."
            },
            {
                "id": 14,
                "title": "Blackout Forensics: What Caused the 2003 Northeast and 2021 Texas Grid Collapses?",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "blackout_forensics_texas_2021_northeast_2003",
                "question": "How did overgrown tree branches in Ohio and frozen gas wellheads in Texas knock out power to tens of millions?",
                "focus": "Cascading transmission trips, SCADA alarm failure, lack of winterization, islanding failure, and multi-day black start recovery.",
                "reason": "Rigorous forensic breakdown of systemic electrical grid failures and disaster preparedness."
            },
            {
                "id": 15,
                "title": "Geothermal Energy: Tapping Earth's Superheated Core with Oil Drilling Tech",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "emerging_trends",
                "slug": "geothermal_enhanced_systems_egs",
                "question": "How are startups using hydraulic fracturing horizontal drilling to extract 24/7 clean baseload steam from deep granite?",
                "focus": "Enhanced Geothermal Systems (EGS), binary cycle power plants, supercritical fluids, and seismic monitoring.",
                "reason": "Investigates the massive scalable baseload potential of next-generation deep geothermal."
            },
            {
                "id": 16,
                "title": "Small Modular Reactors (SMRs): Factory-Built Nuclear Power for Data Centers",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "small_modular_reactors_smrs_ai_power",
                "question": "Why are tech giants like Microsoft, Amazon, and Google backing SMRs to power their AI data center campuses?",
                "focus": "Passive safety systems, factory assembly vs on-site capex, high-temperature gas reactors (HTGR), and NRC regulatory hurdles.",
                "reason": "Examines the revival of nuclear energy driven by explosive corporate computing power demands."
            },
            {
                "id": 17,
                "title": "Nuclear Fusion: Taming the Power of the Sun in a Magnetic Bottle",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "nuclear_fusion_iter_tokamak_stellarator",
                "question": "What physics hurdles stand between scientific net energy gain (Q > 1) and commercially viable grid electricity?",
                "focus": "ITER tokamak, magnetic confinement with REBCO high-temp superconductors, National Ignition Facility laser fusion, and plasma turbulence.",
                "reason": "Explores humanity's ultimate dream: limitless, clean, zero-waste fusion energy."
            },
            {
                "id": 18,
                "title": "High-Voltage Direct Current (HVDC): The Superhighways of the Global Supergrid",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "hvdc_transmission_global_supergrid",
                "question": "Why is DC transmission superior to AC for moving gigawatts of wind and solar power across 2,000 miles?",
                "focus": "Voltage Source Converters (VSC), zero capacitive charging losses, undersea cable interties, and continental grid interconnects.",
                "reason": "Details the technological key to linking distant deserts and oceans to metropolitan load centers."
            },
            {
                "id": 19,
                "title": "Green Hydrogen: The Clean Molecule for Steel, Fertilizer, and Long-Duration Power",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "green_hydrogen_electrolysis_industrial_decarbonization",
                "question": "Why can't batteries solve industrial emissions, and how does green hydrogen crack the heavy industry decarbonization puzzle?",
                "focus": "PEM vs alkaline electrolyzers, round-trip efficiency penalties, pipeline embrittlement, and salt cavern storage.",
                "reason": "Examines the vital molecular energy carrier needed for sectors that cannot be electrified directly."
            },
            {
                "id": 20,
                "title": "The Net-Zero Supergrid Masterclass: Architecting the 100% Clean Energy Civilization",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "net_zero_supergrid_masterclass",
                "question": "What unified energy architecture balances intermittent solar/wind, nuclear baseload, hydro storage, and continental HVDC grids?",
                "focus": "Capacity expansion modeling, grid resilience against solar storms and cyberattacks, sector coupling, and dynamic demand response.",
                "reason": "Synthesizes the complete 20-episode energy curriculum into an executive-level masterplan for the global energy transition."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Big Tech is Buying Entire Nuclear Power Plants to Feed AI Data Centers",
                "trend_score": "Massive Tech & Energy Spike",
                "angle": "case_study",
                "slug": "big_tech_restarting_nuclear_plants_three_mile_island",
                "why_trending": "Microsoft reopening Three Mile Island and Amazon buying nuclear-powered data center campuses shocked the world.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The California Duck Curve Disaster: When Electricity Prices Turn Negative",
                "trend_score": "High Search Interest Spike",
                "angle": "economic_breakdown",
                "slug": "california_duck_curve_negative_power_prices",
                "why_trending": "Solar power floods the grid so heavily that power plants literally pay consumers to take electricity off the wires.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Inside Three Mile Island: The Real Story of America's Worst Nuclear Accident",
                "trend_score": "Evergreen High Curiosity Hook",
                "angle": "root_cause_analysis",
                "slug": "three_mile_island_nuclear_meltdown_investigation",
                "why_trending": "Deconstructs the stuck pilot-operated relief valve and misleading control room indicator that halted US nuclear for decades.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "China's Massive Clean Energy Blitz: Building More Solar in 1 Year Than the US Ever Built",
                "trend_score": "High Global Geopolitical Volume",
                "angle": "field_investigation",
                "slug": "china_renewable_energy_expansion_scale",
                "why_trending": "China installing 200+ gigawatts of solar and wind annually in the Gobi desert stunned international observers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Why Nuclear Fusion is Always 30 Years Away: The Brutal Plasma Physics Reality",
                "trend_score": "High Tech Post-Mortem Traffic",
                "angle": "deep_dive",
                "slug": "nuclear_fusion_brutal_physics_challenges",
                "why_trending": "Breaks down why laser target gain at NIF doesn't mean commercial fusion power is anywhere near your wall outlet.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "How Texas Froze to Death: The 2021 Winter Storm Uri Grid Disaster",
                "trend_score": "Viral Documentary Fascination",
                "angle": "root_cause_analysis",
                "slug": "texas_winter_storm_uri_grid_collapse",
                "why_trending": "The isolated ERCOT grid came within 4 minutes and 37 seconds of an apocalyptic multi-month total blackout.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Gravity Batteries: Can Dropping Giant Concrete Blocks Solve Energy Storage?",
                "trend_score": "High Curiosity Tech Hook",
                "angle": "emerging_trends",
                "slug": "gravity_batteries_energy_vault_critique",
                "why_trending": "Energy Vault's massive crane towers moving 30-ton bricks sparked intense engineering debates across the web.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "114_water": {
        "id": "114",
        "slug": "water",
        "title": "Water",
        "category": "Earth_Environment",
        "audience": "Hydrologists, Environmental Engineers, Geopoliticians, Utility Directors, Water Conservationists (Global)",
        "progression": [
            ("Tier 1: Hydrological Cycles, Groundwater Aquifers & Water Treatment (Beginner / Scratch)",
             "Global freshwater distribution, precipitation dynamics, the Ogallala aquifer depletion, coagulation/flocculation, rapid sand filtration, and chlorination."),
            ("Tier 2: Desalination, Dam Infrastructure & Urban Distribution (Intermediate)",
             "Reverse osmosis energy thermodynamics, brine disposal toxicity, canal lock engineering, municipal pipe water loss (non-revenue water), and lead pipe replacement."),
            ("Tier 3: Geopolitical Water Wars, River Basin Treaties & Agricultural Thirst (Upper Intermediate)",
             "Nile river GERD dam conflict, Indus Waters Treaty, Colorado River compact overuse, flood irrigation vs drip systems, and industrial water footprints (cotton/semiconductors)."),
            ("Tier 4: Atmospheric Harvesting, Wastewater Potable Reuse & The Future Hydrosphere (Advanced / Masterclass)",
             "Direct potable reuse ('toilet-to-tap' membrane bioreactors), atmospheric water generation, wastewater nutrient recovery (struvite), and transcontinental water transfers.")
        ],
        "flagship": {
            "title": "The Disappearing Aquifer: How America is Draining the Ogallala",
            "angle": "field_investigation",
            "slug": "114_water_field_investigation_disappearing_ogallala_aquifer"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Disappearing Aquifer: How America is Draining the Ogallala",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "field_investigation",
                "slug": "disappearing_ogallala_aquifer",
                "question": "What happens to the global food supply when the ancient underground water table beneath 8 US states runs dry?",
                "focus": "Fossil groundwater recharge rates, center-pivot irrigation, crop yield dependency, and aquifer depletion tipping points.",
                "reason": "Crucial foundational episode exploring the invisible freshwater reserves sustaining modern global agriculture."
            },
            {
                "id": 2,
                "title": "The Chemistry of Tap Water: How Dirty Rivers Become Safe Drinking Water",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "chemistry_of_tap_water_treatment",
                "question": "How do municipal water treatment plants turn turbid, bacteria-laden river water into pristine potable tap water?",
                "focus": "Coagulation and flocculation with alum, sedimentation, rapid gravity sand filters, and chlorine residual disinfection.",
                "reason": "Demystifies the civil engineering and chemistry behind the greatest public health triumph in human history."
            },
            {
                "id": 3,
                "title": "The Global Freshwater Paradox: Why 97% of Earth's Water Cannot Be Drunk",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "global_freshwater_paradox_distribution",
                "question": "Why is human civilization concentrated around the tiny 1% of accessible liquid freshwater on Earth?",
                "focus": "Ocean salinity, ice cap lockup, atmospheric moisture budgets, and historical river-valley civilizations.",
                "reason": "Establishes the planetary boundaries and hydrological constraints shaping human geography."
            },
            {
                "id": 4,
                "title": "Desalination Thermodynamics: Turning the Oceans into Drinking Water",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "desalination_reverse_osmosis_thermodynamics",
                "question": "How do polyamide membranes filter sodium ions at 1,000 PSI, and why does desalination consume so much energy?",
                "focus": "Osmotic pressure thresholds, energy recovery devices (pressure exchangers), kilowatt-hours per cubic meter, and capex costs.",
                "reason": "Explains the engineering marvel keeping arid nations like Israel, Saudi Arabia, and the UAE hydrated."
            },
            {
                "id": 5,
                "title": "The Toxic Brine Dilemma: Where Does the Waste from Desalination Plants Go?",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "failure_mode_analysis",
                "slug": "desalination_toxic_brine_disposal",
                "question": "What ecological damage occurs when billions of gallons of super-concentrated, boiling chemical brine are dumped back into bays?",
                "focus": "Hypoxia, marine dead zones, anti-scalant chemical discharge, mineral extraction (lithium/magnesium from brine).",
                "reason": "Exposes the severe ecological trade-off and environmental bottleneck of widespread ocean desalination."
            },
            {
                "id": 6,
                "title": "The Colorado River Crisis: Dividing a Dying River Among 40 Million People",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "colorado_river_compact_overuse",
                "question": "Why did the 1922 Colorado River Compact promise more water than the river actually produces in a normal year?",
                "focus": "Lake Mead and Lake Powell dead pool levels, alfalfa irrigation subsidies, priority water rights, and Western city cuts.",
                "reason": "Masterclass on legal infrastructure flaws, overallocation, and climate aridity in the American West."
            },
            {
                "id": 7,
                "title": "Lead in the Pipes: The Chemistry of the Flint Water Disaster",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "flint_water_crisis_lead_corrosion_chemistry",
                "question": "How did omitting a $100-a-day orthophosphate anti-corrosion chemical poison an entire American city?",
                "focus": "Lead pipe scale passivation, galvanic corrosion, switch to acidic river water, neurotoxin biological damage, and cover-up forensics.",
                "reason": "Rigorous forensic breakdown of chemical neglect, regulatory failure, and municipal infrastructure collapse."
            },
            {
                "id": 8,
                "title": "Agricultural Thirst: Drip Irrigation vs Flood Irrigation in Global Farming",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "drip_vs_flood_irrigation_agriculture",
                "question": "Why does agriculture consume 70% of all global freshwater, and why hasn't micro-drip technology solved it?",
                "focus": "Jevons paradox in water conservation, soil salinization, evapo-transpiration, and Israeli Netafim drip innovations.",
                "reason": "Deconstructs the massive farming water footprint and technological efficiency trade-offs."
            },
            {
                "id": 9,
                "title": "Water Wars on the Nile: The Grand Ethiopian Renaissance Dam (GERD)",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "nile_river_gerd_dam_geopolitics",
                "question": "Why did Ethiopia's giant hydroelectric dam push Egypt and Sudan to the brink of military conflict?",
                "focus": "Blue Nile hydrology, reservoir filling timelines, historical colonial water treaties, and downstream Egyptian drought risks.",
                "reason": "Analyzes the most dangerous transboundary water conflict of the 21st century."
            },
            {
                "id": 10,
                "title": "Non-Revenue Water: How Cities Lose 30% of Their Treated Water Through Leaky Pipes",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "non_revenue_water_pipe_leakage",
                "question": "Why do aging municipal pipe networks leak trillions of gallons of treated drinking water into subterranean dirt before it reaches faucets?",
                "focus": "Acoustic leak detection, pressure management zones, smart water meters, and infrastructure replacement deficits.",
                "reason": "Highlights the hidden multi-billion dollar financial and resource drain plaguing world cities."
            },
            {
                "id": 11,
                "title": "Toilet-to-Tap: The Science and Stigma of Direct Potable Water Reuse",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "psychological_breakdown",
                "slug": "toilet_to_tap_potable_reuse_science",
                "question": "How do multi-barrier purification plants turn raw sewage into water purer than bottled spring water?",
                "focus": "Microfiltration, reverse osmosis, ultraviolet (UV) with hydrogen peroxide advanced oxidation, and the psychological 'yuck factor'.",
                "reason": "Shows how closed-loop water recycling provides unlimited drought-proof water for cities like Singapore (NEWater) and Orange County."
            },
            {
                "id": 12,
                "title": "The Aral Sea Catastrophe: How the Soviets Destroyed the 4th Largest Lake on Earth",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "historical_evolution",
                "slug": "aral_sea_environmental_catastrophe",
                "question": "How did diverting two rivers for cotton monoculture turn a 26,000-square-mile sea into a toxic desert in 30 years?",
                "focus": "Amu Darya and Syr Darya diversions, blowing salt/pesticide dust storms, extinction of endemic fish, and localized climate shift.",
                "reason": "The quintessential cautionary tale of human hubris and ecocidal agricultural planning."
            },
            {
                "id": 13,
                "title": "Industrial Water Footprints: How Much Water Does It Take to Make an iPhone or T-Shirt?",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "economic_breakdown",
                "slug": "virtual_water_embedded_industrial_footprints",
                "question": "Why does making a single semiconductor microchip require 2,000 gallons of ultra-pure water?",
                "focus": "Virtual water trade, ultra-pure water (UPW) polishing, 2,700 liters of water for a cotton shirt, and corporate water stewardship.",
                "reason": "Reveals the massive invisible water embedded inside every manufactured commodity on Earth."
            },
            {
                "id": 14,
                "title": "Atmospheric Water Harvesting: Pulling Moisture from Desert Air",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "emerging_trends",
                "slug": "atmospheric_water_harvesting_mof",
                "question": "Can Metal-Organic Frameworks (MOFs) and fog nets extract drinking water in hyper-arid climates with 15% humidity?",
                "focus": "Adsorption-desorption thermodynamics, solar-powered thermal cycles, dew condensation, and energy consumption per liter.",
                "reason": "Assesses the viability of off-grid atmospheric water generators for remote water-stressed communities."
            },
            {
                "id": 15,
                "title": "The Indus Waters Treaty: How Nuclear Rivals India and Pakistan Share One River",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "indus_waters_treaty_india_pakistan",
                "question": "How has a 1960 World Bank treaty survived three major wars between two nuclear-armed adversaries?",
                "focus": "Eastern vs Western river division, run-of-the-river hydropower rights, permanent Indus commission, and climate glacier melting.",
                "reason": "Examines the world's most enduring and fragile transboundary water-sharing mechanism."
            },
            {
                "id": 16,
                "title": "China's South-to-North Water Diversion Project: Moving Rivers Across a Subcontinent",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "south_to_north_water_diversion_china",
                "question": "How did China build a $60 billion network of giant canals and tunnels to pump the Yangtze River 1,000 miles north to Beijing?",
                "focus": "Eastern, Central, and Western routes, inverted siphons beneath the Yellow River, relocation of 300,000 people, and water quality control.",
                "reason": "Chronicles the largest hydraulic transfer project in human history and its massive engineering scale."
            },
            {
                "id": 17,
                "title": "PFAS Forever Chemicals: The Microscopic Contaminants Poisoning Global Waterways",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "pfas_forever_chemicals_water_contamination",
                "question": "Why are carbon-fluorine bonds virtually indestructible, and how did Teflon and firefighting foam enter 99% of human blood?",
                "focus": "Bioaccumulation, parts-per-trillion toxicity limits, granular activated carbon (GAC) filtration, and multi-billion chemical settlements.",
                "reason": "Investigates the most urgent water quality and public health regulatory crisis of the modern era."
            },
            {
                "id": 18,
                "title": "Glacial Retreat in the Third Pole: The Looming Water Shock for 2 Billion People",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "himalayan_glacier_melt_third_pole",
                "question": "What happens when the Himalayan glaciers feeding the Yangtze, Yellow, Ganges, and Mekong rivers disappear?",
                "focus": "Glacial lake outburst floods (GLOFs), post-peak water flow declines, seasonal monsoon shifts, and geopolitical instability.",
                "reason": "Analyzes the catastrophic downstream water supply risks facing Asian population centers."
            },
            {
                "id": 19,
                "title": "Privatizing the Rain: The Cochabamba Water War and the Ethics of Water as a Human Right",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "cochabamba_water_war_privatization",
                "question": "Why did citizens in Bolivia take to the streets in violent revolt when a foreign consortium privatized municipal rainwater?",
                "focus": "World Bank structural adjustment policies, 300% tariff spikes, civic disobedience, and the UN declaration of water as a fundamental right.",
                "reason": "Explores the fundamental philosophical conflict between market commodity and universal human right."
            },
            {
                "id": 20,
                "title": "The Master Hydrological Architecture: Securing Planetary Freshwater Resilience",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_hydrological_architecture_blueprint",
                "question": "What integrated global strategy combines desalination, regenerative agriculture, closed-loop recycling, and aquifer recharge?",
                "focus": "Managed aquifer recharge (MAR), smart catchment modeling, virtual water trade rebalancing, and transboundary watershed treaties.",
                "reason": "Synthesizes the complete 20-episode water curriculum into a definitive planetary water security roadmap."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Lake Mead Dead Pool: What Happens If Hoover Dam Can No Longer Spin Its Turbines?",
                "trend_score": "Massive US Interest Spike",
                "angle": "root_cause_analysis",
                "slug": "lake_mead_dead_pool_hoover_dam_threat",
                "why_trending": "Drought shrinking Lake Mead to historic lows and revealing sunken boats and mob bodies went viral worldwide.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "How Israel Conquered Drought and Now Exports Freshwater to Its Neighbors",
                "trend_score": "High Admiration & Tech Fascination",
                "angle": "case_study",
                "slug": "israel_desalination_water_superpower",
                "why_trending": "Shows how Israel went from chronic water deficits to generating 85% of domestic water via mega-desalination plants.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The Disappearing Aral Sea: The Man-Made Disaster You Can See From Space",
                "trend_score": "Evergreen High Retention Hook",
                "angle": "historical_evolution",
                "slug": "aral_sea_ship_graveyard_disaster",
                "why_trending": "Rusting fishing trawlers stranded in the middle of vast desert dunes is one of the most haunting visuals on YouTube.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why It Takes 2,000 Gallons of Water to Make a Single Microchip",
                "trend_score": "High Tech Curiosity Hook",
                "angle": "mechanisms_and_systems",
                "slug": "semiconductor_ultra_pure_water_crisis",
                "why_trending": "Explores TSMC and Intel's extreme dependence on ultra-pure water during regional droughts in Taiwan and Arizona.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The PFAS Lawsuit Settlement: How Chemical Giants Will Pay $12 Billion for Poisoning Tap Water",
                "trend_score": "High Legal & Health Spike",
                "angle": "deep_dive",
                "slug": "pfas_forever_chemicals_12_billion_settlement",
                "why_trending": "3M and DuPont paying billions to municipal water providers put 'forever chemicals' on every evening news broadcast.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Singapore's NEWater: Why Millions Drink Recycled Sewage with Pride",
                "trend_score": "Viral Fascination (High Retention)",
                "angle": "field_investigation",
                "slug": "singapore_newater_recycled_sewage",
                "why_trending": "Singapore's brilliant branding and ultra-pure filtration turned 'toilet-to-tap' into a national symbol of resilience.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Saudi Arabia's Floating Desalination Barges: The World's Most Expensive Water",
                "trend_score": "Futuristic Tech Surge",
                "angle": "emerging_trends",
                "slug": "saudi_arabia_floating_desalination_barges",
                "why_trending": "Giant specialized desalination ships deployed along the Red Sea coast to hydrate coastal cities fascinated viewers.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "115_forests_ecology": {
        "id": "115",
        "slug": "forests_ecology",
        "title": "Forests & Ecology",
        "category": "Earth_Environment",
        "audience": "Foresters, Conservation Biologists, Ecologists, Nature Lovers, Carbon Market Analysts (Global)",
        "progression": [
            ("Tier 1: Forest Ecology, Mycorrhizal Networks & Photosynthetic Mechanics (Beginner / Scratch)",
             "Old-growth canopy stratification, mycorrhizal fungal communication ('Wood Wide Web'), carbon sequestration biology, primary vs secondary succession, and nurse logs."),
            ("Tier 2: Forest Management, Wildfire Ecology & Timber Economics (Intermediate)",
             "Controlled burns vs fire suppression catastrophe, the 1910 Big Burn, clear-cutting vs selective logging, mass timber (cross-laminated timber / CLT), and invasive bark beetles."),
            ("Tier 3: Rainforest Depletion, Biodiversity Loss & Carbon Credits (Upper Intermediate)",
             "Amazon basin tipping point dynamics, cattle ranching slash-and-burn, REDD+ carbon offset market fraud, keystone species cascades, and tropical cloud forest hydrology."),
            ("Tier 4: Rewilding, Boreal Peatlands & Planetary Restoration (Advanced / Masterclass)",
             "Boreal permafrost peatlands as carbon time-bombs, Pleistocene rewilding, Miyawaki micro-forest methodology, assisted tree migration under climate shifts, and the global restoration blueprint.")
        ],
        "flagship": {
            "title": "The Wood Wide Web: How Trees Secretly Talk and Share Nutrients",
            "angle": "mechanisms_and_systems",
            "slug": "115_forests_ecology_mechanisms_and_systems_wood_wide_web"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Wood Wide Web: How Trees Secretly Talk and Share Nutrients",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "wood_wide_web_mycorrhizal_networks",
                "question": "How do underground fungal mycorrhizal networks allow 'mother trees' to nurture dying seedlings and warn neighbors of pests?",
                "focus": "Suzanne Simard's research, carbon and phosphorus isotope tracking, mycorrhizal fungi mutualism, and defense signaling.",
                "reason": "Crucial foundational episode introducing the revolutionary biological understanding of forests as interconnected superorganisms."
            },
            {
                "id": 2,
                "title": "Old-Growth vs Tree Plantations: Why Mono-Crops Are Biological Deserts",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "old_growth_vs_monoculture_plantations",
                "question": "Why does planting 10,000 identical pine trees fail to replace the biodiversity and carbon storage of a native forest?",
                "focus": "Canopy complexity, dead wood decaying habitat, soil microbiome richness, pest vulnerability, and structural diversity.",
                "reason": "Debunks simplistic corporate tree-planting public relations campaigns with rigorous ecological science."
            },
            {
                "id": 3,
                "title": "The Physics of Photosynthesis and Carbon Sequestration: The Planet's Green Lungs",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "photosynthesis_and_carbon_sequestration_mechanics",
                "question": "How do trees turn invisible atmospheric carbon dioxide gas into hundreds of tons of solid wooden cellulose?",
                "focus": "Calvin cycle, stomata gas exchange, lignin and cellulose synthesis, soil carbon storage, and biomass calculations.",
                "reason": "Teaches the core biochemical mechanics powering terrestrial life and global carbon buffering."
            },
            {
                "id": 4,
                "title": "The 100-Year Mistake: How Smokey Bear and Fire Suppression Ruined Forests",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "fire_suppression_history_smokey_bear",
                "question": "How did a century of extinguishing every forest fire create catastrophic overgrown fuel loads that burn down entire towns?",
                "focus": "1910 Great Burn in Idaho/Montana, US Forest Service 10:00 AM policy, loss of indigenous cultural burning, and catastrophic mega-fires.",
                "reason": "Chronicles the colossal policy blunder that turned natural forest cycles into explosive wildfire powder kegs."
            },
            {
                "id": 5,
                "title": "Inside the Giant Redwoods and Sequoias: The Tallest Living Giants on Earth",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "field_investigation",
                "slug": "giant_redwoods_sequoias_botany",
                "question": "How do 380-foot Coastal Redwoods pull water hundreds of feet into the sky against gravity?",
                "focus": "Xylem capillary tension, coastal fog foliar uptake, fire-resistant tannic bark, and 2,000-year longevity strategies.",
                "reason": "Celebrates the botanical and hydraulic miracles achieved by the ancient temperate rainforests."
            },
            {
                "id": 6,
                "title": "Controlled Prescribed Burns: Fighting Fire with Fire",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "controlled_prescribed_burns_forest_management",
                "question": "How do foresters safely burn thousands of understory acres to prevent uncontrolled wildfire infernos?",
                "focus": "Drip torches, fuel moisture windows, fire behavior modeling, anchor points, and reviving indigenous cultural fire regimes.",
                "reason": "Provides an actionable operational breakdown of modern fire ecology and forest resilience management."
            },
            {
                "id": 7,
                "title": "The Bark Beetle Epidemic: How Warming Winters Killed Millions of Acres of Pines",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "bark_beetle_epidemic_pine_forests",
                "question": "How does a rice-grain-sized insect overwhelm a tree's resin defenses and turn entire mountain ranges ghost-grey?",
                "focus": "Mountain pine beetle pheromone attacks, blue stain fungus symbiosis, drought-stressed tree defenses, and mild winter survival.",
                "reason": "Examines the biological cascade linking climate warming directly to massive forest die-offs."
            },
            {
                "id": 8,
                "title": "Mass Timber and Cross-Laminated Timber (CLT): Can Wooden Skyscrapers Save the Planet?",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "emerging_trends",
                "slug": "mass_timber_clt_wooden_skyscrapers",
                "question": "How can engineered wood replace carbon-heavy concrete and steel in 20-story urban towers?",
                "focus": "Cross-Laminated Timber manufacturing, structural fire resistance (charring layers), embodied carbon lockup, and sustainable forestry certification.",
                "reason": "Bridges sustainable commercial forestry with next-generation architectural civil engineering."
            },
            {
                "id": 9,
                "title": "The Amazon Rainforest Tipping Point: From Carbon Sink to Carbon Source",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "amazon_rainforest_dieback_tipping_point",
                "question": "At what percentage of deforestation does the Amazon basin lose its self-generated rain and flip into a dry savanna?",
                "focus": "Flying rivers atmospheric moisture, Carlos Nobre's 20-25% deforestation threshold, cattle ranching borders, and carbon emission flips.",
                "reason": "Masterclass on the planetary hydrological and climatic significance of the world's greatest tropical forest."
            },
            {
                "id": 10,
                "title": "The Carbon Offset Scam: Do Corporate Tree-Planting Credits Actually Work?",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "failure_mode_analysis",
                "slug": "carbon_offset_market_tree_planting_scam",
                "question": "Why did major corporate carbon credits (Verra/REDD+) turn out to be worthless phantom offsets that protected nothing?",
                "focus": "Additionality fraud, baseline inflation, permanence risks (trees burning in wildfires), leakage, and voluntary carbon market collapse.",
                "reason": "Exposes the greenwashing accounting and financial loopholes in international forest carbon markets."
            },
            {
                "id": 11,
                "title": "The Boreal Peatland Bomb: The Planet's Largest and Most Vulnerable Carbon Vault",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "boreal_forest_peatland_carbon_vault",
                "question": "Why does the freezing northern Taiga store twice as much carbon as all tropical rainforests combined?",
                "focus": "Sphagnum moss peat accumulation, anaerobic preservation, permafrost thaw sinkholes (thermokarst), and zombie overwintering fires.",
                "reason": "Explores the colossal, often neglected circumpolar biome holding the key to global climate stability."
            },
            {
                "id": 12,
                "title": "Keystone Species and Trophic Cascades: How Wolves Changed Rivers in Yellowstone",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "famous_examples",
                "slug": "trophic_cascades_yellowstone_wolves_forests",
                "question": "How did reintroducing 14 gray wolves to Yellowstone National Park regenerate aspen forests and stabilize riverbanks?",
                "focus": "Ecology of fear, elk herd movement, beaver dam return, riparian willow regeneration, and river erosion control.",
                "reason": "The quintessential case study demonstrating top-down ecological regulation and forest biodiversity recovery."
            },
            {
                "id": 13,
                "title": "The Great Green Wall of Africa: Planting an 8,000 km Forest Across the Sahara",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "field_investigation",
                "slug": "great_green_wall_africa_sahara_desert",
                "question": "Can 11 African nations halt the southward march of the Sahara desert by planting a wall of drought-hardy acacia trees?",
                "focus": "Sahel desertification, indigenous Zaï pit water harvesting, agroforestry farmer-managed natural regeneration (FMNR), and community ownership.",
                "reason": "Highlights the epic ecological restoration struggle against desertification across an entire continent."
            },
            {
                "id": 14,
                "title": "Invasive Species in the Forest: Kudzu, Emerald Ash Borer, and Dutch Elm Disease",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "invasive_species_forest_devastation",
                "question": "How did international shipping pallets wipe out millions of majestic American Chestnut and Ash trees forever?",
                "focus": "Chestnut blight cryphonectria parasitica, emerald ash borer larvae feeding, lack of co-evolutionary defenses, and biocontrol wasps.",
                "reason": "Investigates the devastating ecological and economic consequences of globalized biological invasions."
            },
            {
                "id": 15,
                "title": "Cloud Forests in the Mist: The Rarest and Most Fragile Habitats on Earth",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "cloud_forests_epiphytes_biodiversity",
                "question": "How do high-altitude mountain forests harvest their entire water supply directly from passing low-altitude clouds?",
                "focus": "Epiphyte orchids and bromeliads, horizontal precipitation interception, endemic biodiversity hotspots, and climate lifting condensation levels.",
                "reason": "Examines the delicate canopy hydrology and extreme sensitivity of mountain cloud forest ecosystems."
            },
            {
                "id": 16,
                "title": "Miyawaki Micro-Forests: Growing Ultra-Dense Mini-Jungles in Urban Centers",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "miyawaki_micro_forest_methodology",
                "question": "How did Japanese botanist Akira Miyawaki invent a technique to grow mature native forests 10x faster in tiny city plots?",
                "focus": "Dense multi-layered planting, native species selection, deep soil aeration with compost, rapid self-thinning, and biodiversity hubs.",
                "reason": "Introduces a powerful, scalable urban rewilding methodology spreading across global cities."
            },
            {
                "id": 17,
                "title": "Assisted Tree Migration: Moving Entire Forests North Before the Climate Kills Them",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "assisted_tree_migration_climate_change",
                "question": "Should humans artificially dig up and replant southern tree species hundreds of miles north to save them from heatwaves?",
                "focus": "Velocity of climate change vs natural seed dispersal rates, forestry provenance trials, genetic adaptation, and ecological disruption ethics.",
                "reason": "Tackles a cutting-edge, high-stakes ethical and biological dilemma in modern forestry management."
            },
            {
                "id": 18,
                "title": "De-Extinction and Pleistocene Rewilding: Can Woolly Mammoths Save the Siberian Tundra?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "pleistocene_rewilding_mammoth_tundra",
                "question": "How could resurrecting cold-adapted megafauna pack down winter snow to prevent permafrost methane emissions?",
                "focus": "Sergey Zimov's Pleistocene Park, mammoth steppe grassland restoration, genetic editing (Colossal Biosciences), and ecosystem engineering.",
                "reason": "Explores the wild frontier blending genetic de-extinction with planetary climate stabilization."
            },
            {
                "id": 19,
                "title": "Illegal Logging and Forest Mafias: The Shadow Economy Destroying Rare Hardwoods",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "field_investigation",
                "slug": "illegal_logging_rosewood_forest_mafias",
                "question": "How do organized criminal syndicates launder endangered rosewood and teak from Madagascar and Cambodia into luxury furniture?",
                "focus": "CITES timber treaties, satellite radar deforestation tracking, DNA wood fingerprinting, ranger assassinations, and supply chain laundering.",
                "reason": "Exposes the violent, multi-billion-dollar global black market driving rare tree species to extinction."
            },
            {
                "id": 20,
                "title": "The Master Ecological Restoration Architecture: Rewilding the Biosphere",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_ecological_restoration_architecture",
                "question": "What comprehensive planetary blueprint unites old-growth protection, sustainable timber, indigenous land sovereignty, and wildlife corridors?",
                "focus": "E.O. Wilson's Half-Earth concept, continental wildlife overpasses, biodiversity finance, and holistic ecosystem stewardship.",
                "reason": "Definitive capstone masterclass synthesizing all 20 episodes into an actionable masterplan for the future of Earth's forests."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Wood Wide Web: The Mind-Blowing Secret Life of Underground Tree Networks",
                "trend_score": "Massive Viral Curiosity Spike",
                "angle": "case_study",
                "slug": "wood_wide_web_fungal_networks_viral",
                "why_trending": "The revelation that trees talk, send distress signals, and feed their children via fungi captivated millions of viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Why Tree-Planting Charities Are Doing More Harm Than Good",
                "trend_score": "High Controversy & Retention Spike",
                "angle": "failure_mode_analysis",
                "slug": "tree_planting_charities_failure_scandal",
                "why_trending": "Investigating how planting monoculture saplings in deserts leads to dead plantations and corporate greenwashing.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "How One Man Accidentally Destroyed America's Forests with Smokey Bear",
                "trend_score": "Evergreen High Engagement Hook",
                "angle": "root_cause_analysis",
                "slug": "smokey_bear_wildfire_suppression_paradox",
                "why_trending": "The counter-intuitive story of how zero-tolerance fire suppression created modern catastrophic mega-fires.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The Amazon Flying Rivers: How a Single Tree Pumps 1,000 Liters of Water Daily",
                "trend_score": "High Scientific Wonder Volume",
                "angle": "mechanisms_and_systems",
                "slug": "amazon_flying_rivers_evapotranspiration",
                "why_trending": "Visualizing the invisible aerial rivers that carry more moisture than the entire Amazon river itself.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Secret Location of Hyperion: Why Officials Hide the World's Tallest Tree",
                "trend_score": "High Mystery & Curiosity Spike",
                "angle": "deep_dive",
                "slug": "hyperion_tallest_tree_hidden_location",
                "why_trending": "Park rangers banning anyone from visiting the 380-foot giant redwood under threat of arrest ignited intense fascination.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Miyawaki Forests: How to Grow a 100-Year Forest in Your Tiny Backyard in 10 Years",
                "trend_score": "Viral DIY & Ecology Trend",
                "angle": "practical_playbook",
                "slug": "grow_miyawaki_micro_forest_backyard",
                "why_trending": "Urban homeowners transforming small suburban lawns into dense mini-jungles went viral across social media.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The Zombie Fires Burning Underneath the Arctic Snow Right Now",
                "trend_score": "High Winter News Curiosity",
                "angle": "field_investigation",
                "slug": "zombie_fires_arctic_peat_overwinter",
                "why_trending": "Peat fires smoldering under 6 feet of sub-zero snow all winter and re-emerging in spring fascinated viewers.",
                "status": "READY FOR COMPILATION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 111-115...")
    for folder, meta in BATCH_111_115.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 111-115 complete!")

if __name__ == "__main__":
    main()
