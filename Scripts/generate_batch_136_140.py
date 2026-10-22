import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_136_140 = {
    "136_shopping_consumer_guides": {
        "id": "136",
        "slug": "shopping_consumer_guides",
        "title": "Shopping & Consumer Guides",
        "category": "Commerce_Industry",
        "audience": "Smart Shoppers, Consumer Advocates, Bargain Hunters, Product Testers, Personal Finance Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Cost-Per-Use, Built-to-Last Materials & Consumer Rights (Beginner / Scratch)",
             "Cost-per-use economics, identifying genuine leather vs bonded vinyl, statutory warranty rights, the Veblen luxury tax, and avoiding fast-fashion traps."),
            ("Tier 2: Deceptive Pricing, Black Friday Illusions & Affiliate Review Economics (Intermediate)",
             "CamelCamelCamel price-tracking history, fabricated MSRP markups, the hidden business model of review websites (Wirecutter/affiliate links), and grocery unit-price comparisons."),
            ("Tier 3: Right to Repair, Warranty Fine Print & Supply Chain Quality Shifting (Upper Intermediate)",
             "Enshittification of consumer goods, glued batteries and proprietary screws, extended warranty actuarial math, and how brands quietly substitute cheaper parts in second-generation revisions."),
            ("Tier 4: Algorithmic Price Discrimination, Buy-It-For-Life (BIFL) Curation & The Master Shopper (Advanced / Masterclass)",
             "Dynamic browser-based surge pricing, private-label manufacturing origins (Costco Kirkland secrets), curating a generational Buy-It-For-Life wardrobe, and consumer defense litigation.")
        ],
        "flagship": {
            "title": "The Black Friday Illusion: How Retailers Fake Discounts and Inflate Baselines",
            "angle": "root_cause_analysis",
            "slug": "136_shopping_consumer_guides_root_cause_analysis_black_friday_illusion"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Black Friday Illusion: How Retailers Fake Discounts and Inflate Baselines",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "root_cause_analysis",
                "slug": "black_friday_fake_discounts_inflated_msrp",
                "question": "How do major retailers inflate price tags in September just to slap a fake '60% OFF' sticker on them in November?",
                "focus": "Price history tracking algorithms, Black Friday derivative models (cheaper TV panel components made specifically for sales), and psychological anchoring.",
                "reason": "Crucial foundational episode training consumers to see through artificial promotional pricing and urgency manipulation."
            },
            {
                "id": 2,
                "title": "Cost-Per-Wear and Cost-Per-Use: The True Mathematics of Smart Buying",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "cost_per_use_economics_smart_buying",
                "question": "Why is a $300 Goodyear-welted leather boot drastically cheaper over 10 years than five $60 glued synthetic shoes?",
                "focus": "Cost-per-use calculation formulas, resoleability, maintenance depreciation, and Terry Pratchett's 'Boots Theory' of socioeconomic unfairness.",
                "reason": "Teaches the fundamental financial framework prioritizing long-term durability over initial purchase price."
            },
            {
                "id": 3,
                "title": "The Leather Lie: Genuine Leather, Top Grain, and Bonded Vinyl Scams",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "field_investigation",
                "slug": "leather_grades_scam_genuine_vs_full_grain",
                "question": "Why does a product labeled '100% Genuine Leather' peel and flake into plastic dust after only six months of use?",
                "focus": "Leather grading hierarchy (Full Grain, Top Grain, Genuine, Bonded leather scrap paste), polyurethane PU coatings, and tactile edge burnishing tests.",
                "reason": "Exposes the most widespread deceptive marketing terminology in apparel, furniture, and accessory retail."
            },
            {
                "id": 4,
                "title": "The Affiliate Review Conflict: Can You Trust Tech and Mattress Reviews?",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "affiliate_review_economics_wirecutter_mattress",
                "question": "How do mattress review websites pocket $300 bounties per click, turning independent review sites into corporate shills?",
                "focus": "Affiliate link commission economics, Wirecutter's acquisition by NYT, mattress affiliate lawsuits, and finding genuinely unbiased test labs (Consumer Reports).",
                "reason": "Deconstructs the compromised economic incentives behind the modern digital product review industry."
            },
            {
                "id": 5,
                "title": "Unit Pricing Mastery: How Supermarkets Trick You with Bigger Boxes",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "supermarket_unit_pricing_bulk_buying_tricks",
                "question": "Why is the giant 'family-size' cereal box frequently more expensive per ounce than buying two smaller boxes on the bottom shelf?",
                "focus": "Price per unit shelf tags, shrinkflation package downsizing, eye-level placement slotting fees, and warehouse club unit math.",
                "reason": "Provides an immediate, practical grocery shopping defense against deceptive supermarket packaging."
            },
            {
                "id": 6,
                "title": "Buy It For Life (BIFL): The Science of Unbreakable Kitchenware",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "buy_it_for_life_cookware_cast_iron_clad",
                "question": "Why will a $40 raw cast iron skillet or a tri-ply stainless steel pan outlive your grandchildren while Teflon pans die in 2 years?",
                "focus": "PTFE non-stick coating thermal degradation, cast iron polymerized oil seasoning chemistry, 3-ply aluminum-core heat conduction, and rivet construction.",
                "reason": "Guides consumers toward non-toxic, heirloom kitchen tools that eliminate perpetual disposable replacements."
            },
            {
                "id": 7,
                "title": "Dynamic Pricing and Browser Tracking: Are You Paying More Because of Your Mac?",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "dynamic_pricing_browser_fingerprinting_travel",
                "question": "Do airlines, hotels, and retail sites charge higher prices based on your device, location, and repeated search visits?",
                "focus": "Browser fingerprinting, cookie-based search count triggers, IP geolocation price discrimination, and private browsing test methodologies.",
                "reason": "Demystifies the real-time algorithmic price discrimination tailoring checkout prices to individual consumer demographics."
            },
            {
                "id": 8,
                "title": "The Kirkland Signature Secret: Who Actually Makes Costco's House Brands?",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "kirkland_signature_costco_private_label_secrets",
                "question": "How does Costco negotiate with name-brand giants like Starbucks, Duracell, and Grey Goose to bottle identical goods under their own label?",
                "focus": "Private label contract manufacturing, 14% maximum markup rule, co-packing agreements, and how Costco forces tier-1 quality into discount packaging.",
                "reason": "Reveals the corporate manufacturing secrets behind the most trusted and profitable private label in retail history."
            },
            {
                "id": 9,
                "title": "Extended Warranties: Why Financial Planners Call Them Pure Scams",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "extended_warranties_actuarial_scam_math",
                "question": "Why do electronics retailers push extended protection plans at checkout that carry an 80% profit margin for the store?",
                "focus": "Actuarial failure rate curves, credit card automatic warranty extensions, excluded wear-and-tear clauses, and self-insuring small electronics.",
                "reason": "Exposes the high-margin retail racket operating at cash registers and teaches smart risk self-insurance."
            },
            {
                "id": 10,
                "title": "Shrinkflation Unmasked: How Brands Cut 15% of Content Without Lowering Prices",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "shrinkflation_package_redesign_inflation_hiding",
                "question": "How do chip bags add nitrogen gas, chocolate bars widen pyramid indentations, and detergent bottles hide indent bottoms?",
                "focus": "Skimpflation ingredient substitution, subtle container volume reductions, consumer price sensitivity thresholds, and regulatory transparency laws.",
                "reason": "Investigates the deceptive corporate tactics used to pass price increases onto consumers without changing sticker prices."
            },
            {
                "id": 11,
                "title": "Outlet Stores vs Flagship Stores: The Made-for-Outlet Deception",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "field_investigation",
                "slug": "outlet_mall_deception_made_for_outlet_clothing",
                "question": "Why is 85% of clothing at J.Crew, Coach, and Nike outlet malls manufactured with inferior fabric specifically for discount malls?",
                "focus": "The myth of 'excess inventory clearance', separate manufacturing lines with diamond/dot label markings, polyester blends vs wool, and outlet retail margins.",
                "reason": "Debunks the common consumer belief that outlet malls offer genuine flagship clothing overstock at steep discounts."
            },
            {
                "id": 12,
                "title": "The Wool, Cashmere, and Synthetic Blend Minefield: Reading Apparel Labels",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "practical_playbook",
                "slug": "apparel_fabric_labels_cashmere_acrylic_blends",
                "question": "Why does a sweater labeled 'Cashmere Blend' with 3% cashmere feel itchy and pill into balls after two delicate washes?",
                "focus": "Microscopic staple fiber lengths, 100% long-staple virgin wool vs recycled short fiber blends, acrylic cheap synthetics, and fabric burn tests.",
                "reason": "Equips shoppers with the technical textile knowledge to spot overpriced synthetic blends masquerading as luxury knitwear."
            },
            {
                "id": 13,
                "title": "The Right to Repair War: Why Apple and John Deere Tried to Outlaw Fixing Your Own Stuff",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "ethical_dimensions",
                "slug": "right_to_repair_battle_apple_john_deere",
                "question": "How did software locks and parts pairing make it illegal for farmers to fix their own tractors and consumers to fix broken screens?",
                "focus": "Serialized parts pairing, software diagnostic lockouts, European union repair mandates, and the historic legislative victories of repair advocates.",
                "reason": "Masterclass on the legal and philosophical battle over property ownership in an era of software-locked consumer hardware."
            },
            {
                "id": 14,
                "title": "Car Buying Negotiations: How to Defeat Dealership Finance and Insurance (F&I) Offices",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "practical_playbook",
                "slug": "car_buying_negotiation_dealership_finance_office",
                "question": "How do dealership finance managers quietly add $4,000 in dealer prep, paint protection, and interest rate markups in the back room?",
                "focus": "The four-square sales sheet con, out-the-door (OTD) price negotiations, pre-approved credit union financing, dealer doc fees, and timing end-of-month quotas.",
                "reason": "Provides a comprehensive, tactical playbook to protect buyers during the second-largest purchase of their lives."
            },
            {
                "id": 15,
                "title": "Energy Star and Appliance Longevity: Why New Washers Die in 5 Years While Old Ones Lasted 30",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "appliance_longevity_failure_electronic_boards",
                "question": "Why did modern eco-friendly appliances with sensitive computer motherboards become fragile disposables compared to mechanical timers?",
                "focus": "Electronic control board heat/vibration degradation, plastic water pump impellers, sealed drum bearings, and Speed Queen mechanical simplicity.",
                "reason": "Examines the engineering trade-offs between regulatory energy efficiency mandates and physical mechanical longevity."
            },
            {
                "id": 16,
                "title": "Chargebacks, Section 75, and Small Claims: The Consumer Nuclear Options",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "mechanisms_and_systems",
                "slug": "credit_card_chargebacks_consumer_protection_laws",
                "question": "How do credit card dispute protocols legally force merchants to refund your money when customer service ignores you?",
                "focus": "Fair Credit Billing Act, merchant chargeback penalty thresholds, documentation evidence binders, Section 75 UK protections, and small claims court procedures.",
                "reason": "Teaches consumers their statutory legal rights and payment network dispute mechanisms to recover funds from dishonest merchants."
            },
            {
                "id": 17,
                "title": "The Resale Economy: Grailed, The RealReal, and Poshmark Counterfeit Risks",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "deep_dive",
                "slug": "luxury_resale_market_therealreal_authentication_scandals",
                "question": "How did fast-growing luxury resale platforms accidentally sell thousands of counterfeit designer bags despite '100% authentic' claims?",
                "focus": "High-volume underpaid authenticator quotas, super-fake Hermès and Chanel manufacturing, digital NFC authentication chips, and secondary market arbitrage.",
                "reason": "Investigates the explosive multi-billion dollar pre-owned luxury market and its persistent authentication vulnerabilities."
            },
            {
                "id": 18,
                "title": "Minimalism vs Consumerism: The Freedom of Owning Less and Buying Better",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "minimalism_intentional_consumption_bifl",
                "question": "Can curating an intentional, high-quality capsule wardrobe and durable home eliminate the psychological stress of endless consumption?",
                "focus": "Hedonic treadmill adaptation, visual clutter cortisol reduction, intentional budgeting, and the mental freedom of owning tools that never break.",
                "reason": "Probes the deep philosophical and emotional liberation found in stepping off the consumer replacement treadmill."
            },
            {
                "id": 19,
                "title": "AI Personal Shoppers and Algorithmic Price Snipers: The Future of Consumer Power",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "ai_personal_shopping_automated_negotiation_agents",
                "question": "Will autonomous AI browser agents crawl dark retail corners, negotiate bulk discounts, and auto-purchase when prices hit historic bottoms?",
                "focus": "Autonomous price tracking bots, API-driven inventory scraping, AI coupon stacking, synthetic review filtering, and the battle between buyer bots and retailer firewalls.",
                "reason": "Assesses the emerging technological frontier leveling the playing field between consumers and corporate pricing algorithms."
            },
            {
                "id": 20,
                "title": "The Master Consumer Architecture: The Lifetime Smart-Purchasing System",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_consumer_architecture_lifetime_purchasing_blueprint",
                "question": "What complete life operational system unites cost-per-use calculations, material inspection, warranty automation, and intentional ownership?",
                "focus": "The 48-hour purchase delay rule, material specification checklist, warranty digital vault tracking, seasonal clearance calendars, and building generational wealth.",
                "reason": "Definitive capstone masterclass synthesizing all 20 consumer guide episodes into an elite consumer's lifelong wealth-preservation blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Black Friday Scam: How Retailers Fake 70% Discounts (Price History Proof)",
                "trend_score": "Massive Holiday Season Spike (High Retention)",
                "angle": "case_study",
                "slug": "black_friday_fake_discounts_exposed_viral",
                "why_trending": "Price tracking charts showing Amazon and Walmart raising prices weeks before Black Friday to fake discounts always goes viral.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The Genuine Leather Scam: Why Your Expensive Jacket is Actually Plastic Dust",
                "trend_score": "High Consumer Shock & Education Hook",
                "angle": "field_investigation",
                "slug": "genuine_leather_scam_explained_leathercraft",
                "why_trending": "Leathercrafters slicing into designer belts and showing bonded cardboard and plastic scrap layers fascinates millions.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The Boots Theory: Why Being Poor Costs Way More Money Than Being Rich",
                "trend_score": "High Socioeconomic Resonance & Relatability",
                "angle": "beginner_guide",
                "slug": "boots_theory_socioeconomics_cost_of_poverty",
                "why_trending": "Terry Pratchett's famous boot parable explaining how cheap shoes keep people broke resonates deeply across social media.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why Modern Washing Machines Break in 4 Years When 1980s Ones Ran for 30",
                "trend_score": "High Frustration & Appliance Repair Hook",
                "angle": "root_cause_analysis",
                "slug": "why_modern_appliances_break_quickly_repair_tech",
                "why_trending": "Appliance technicians tearing apart new Samsung washers and showing cheap plastic brackets breaking inside drives huge viewership.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Costco Secret: The Famous Brands Hiding Behind Kirkland Signature Labels",
                "trend_score": "High Retail Curiosity & Brand Hype",
                "angle": "deep_dive",
                "slug": "costco_kirkland_brand_secrets_manufacturers",
                "why_trending": "Revealing that Kirkland batteries are Duracell and Kirkland vodka comes from top distilleries is internet gold.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Outlet Mall Scams: Why 90% of Outlet Clothes Were Never in Normal Stores",
                "trend_score": "High Retail Myth-Busting Spike",
                "angle": "famous_examples",
                "slug": "outlet_mall_clothing_scam_made_for_outlet",
                "why_trending": "Exposing the hidden dot marks on tags proving outlet clothing is manufactured with cheap polyester specifically for discount shoppers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Car Salesman Secrets: The Four-Square Trick They Use to Rob You in Finance",
                "trend_score": "High Consumer Defense & Automotive Hook",
                "angle": "practical_playbook",
                "slug": "car_dealership_four_square_negotiation_trick",
                "why_trending": "Former car salesmen breaking down the four-square sheet used to confuse buyers on trade-in and monthly payment math goes viral.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "137_repair_maintenance": {
        "id": "137",
        "slug": "repair_maintenance",
        "title": "Repair & Maintenance",
        "category": "Craft_Making",
        "audience": "DIY Fixers, Right-to-Repair Activists, Appliance Technicians, Homeowners, Mechanical Tinkerers (Global)",
        "progression": [
            ("Tier 1: Diagnostic Fundamentals, Hand Tool Mastery & Electrical Safety (Beginner / Scratch)",
             "Multimeter voltage/continuity testing, proper screwdriver bit sizing (avoiding stripped screws), safe capacitor discharge, mechanical diagnostic trees, and basic lubricant physics (WD-40 vs grease)."),
            ("Tier 2: Small Engine Carburetors, Household Appliances & Soldering Circuits (Intermediate)",
             "Small 2-stroke/4-stroke carburetor rebuilds, washing machine pump drain unclogging, through-hole and basic surface-mount soldering, copper pipe sweating, and drywall patching."),
            ("Tier 3: Planned Obsolescence Teardowns, Proprietary Fasteners & Schematics Reverse Engineering (Upper Intermediate)",
             "Defeating security Torx/pentalobe fasteners, troubleshooting blown electrolytic capacitors on power supply boards, schematic reading, multimeter diode check mode, and thermal paste reapplication."),
            ("Tier 4: Right-to-Repair Legislation, Component-Level Micro-Soldering & The Master Repair Workshop (Advanced / Masterclass)",
             "BGA chip reballing and hot-air rework stations, oscilloscope signal tracing, right-to-repair legal precedents (Magnuson-Moss Act), 3D printing custom replacement gears, and workshop tooling ergonomics.")
        ],
        "flagship": {
            "title": "Planned Obsolescence: How Lightbulb Cartels and Glue Encapsulation Killed Repair",
            "angle": "historical_evolution",
            "slug": "137_repair_maintenance_historical_evolution_planned_obsolescence"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Planned Obsolescence: How Lightbulb Cartels and Glue Encapsulation Killed Repair",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "planned_obsolescence_phoebus_cartel_lightbulbs",
                "question": "How did the 1924 Phoebus Cartel secretly fine manufacturers whose lightbulbs lasted longer than 1,000 hours, creating modern disposable culture?",
                "focus": "The Centennial Light in Livermore (burning since 1901), Phoebus Cartel fines, glued smartphone enclosures, proprietary pentalobe screws, and engineered product lifespans.",
                "reason": "Crucial foundational episode exploring the corporate history that systematically destroyed consumer repair culture."
            },
            {
                "id": 2,
                "title": "The Digital Multimeter Masterclass: Voltage, Resistance, and Continuity Testing",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "multimeter_testing_voltage_resistance_continuity",
                "question": "How does a $25 multimeter allow you to diagnose 90% of electrical and appliance failures without guessing?",
                "focus": "Continuity beeps for broken traces, AC vs DC voltage safety, resistance testing heating elements, diode checks, and never blowing internal meter fuses.",
                "reason": "Teaches the indispensable diagnostic instrument required for all electronic, automotive, and appliance troubleshooting."
            },
            {
                "id": 3,
                "title": "The Lubricant Lie: WD-40 vs White Lithium Grease vs Silicone Spray",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "lubricant_guide_wd40_grease_silicone_penetrating_oil",
                "question": "Why does spraying standard blue-can WD-40 into door hinges and bicycle chains attract dirt and ruin bearings?",
                "focus": "WD-40 as a solvent water-displacer, penetrating oils (Kroil/PB Blaster) for seized bolts, high-pressure lithium grease, silicone on rubber, and dry PTFE lubricants.",
                "reason": "Demystifies everyday lubricant chemistry and prevents the most common DIY mechanical maintenance mistake."
            },
            {
                "id": 4,
                "title": "Fasteners Decoded: Why Stripped Screws Happen and How to Extract Them",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "screw_fasteners_stripped_extraction_jis_vs_phillips",
                "question": "Why do Phillips screwdrivers deliberately 'cam out' and strip Japanese motorcycle and electronics screws?",
                "focus": "JIS (Japanese Industrial Standard) vs Phillips vs Torx vs Pozidriv, screw extractor drill bits, left-handed drill bits, rubber band tricks, and impact drivers.",
                "reason": "Provides vital mechanical workshop knowledge preventing stripped fasteners and teaching foolproof extraction techniques."
            },
            {
                "id": 5,
                "title": "The Capacitive Death Trap: Safely Discharging Power Supply and Microwave Capacitors",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "root_cause_analysis",
                "slug": "high_voltage_capacitor_discharge_safety_microwaves",
                "question": "Why can an unplugged microwave oven or old CRT TV store 2,000 lethal volts for weeks after being disconnected from the wall?",
                "focus": "Capacitor dielectric energy storage, bleed resistors, building a safe ceramic resistor discharge probe, one-hand rule safety, and high-voltage warnings.",
                "reason": "Vital life-safety engineering training to protect DIY repairers from fatal electrical shocks inside everyday appliances."
            },
            {
                "id": 6,
                "title": "Small Engine Rescue: Cleaning Gunked Carburetors on Lawnmowers and Generators",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "small_engine_carburetor_cleaning_lawnmower_ethanol",
                "question": "Why does letting ethanol gas sit over the winter plug microscopic carburetor jets, and how do you clean it with a guitar string?",
                "focus": "Ethanol fuel phase separation, needle and seat valves, float bowl gunk, main jet cleaning with wire, ultrasonic carburetor baths, and fuel stabilizers.",
                "reason": "The quintessential small-engine repair skill that saves millions of lawnmowers, pressure washers, and snowblowers from the scrap yard."
            },
            {
                "id": 7,
                "title": "Washing Machine Surgery: Clearing Clogged Drain Pumps and Faulty Pressure Switches",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "washing_machine_repair_drain_pump_coin_trap",
                "question": "Why does a front-load washer throw an error code and refuse to spin because of a single baby sock or quarter in the coin trap?",
                "focus": "Drain pump filter cleanout, testing pump impeller motors with multimeters, pressure switch air hoses, door latch interlocks, and replacing drive belts.",
                "reason": "Empowers homeowners to fix the most common, simple appliance breakdown without paying a $200 service call fee."
            },
            {
                "id": 8,
                "title": "Soldering Fundamentals: How to Solder Wires and Replace Blown Circuit Board Components",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "beginner_guide",
                "slug": "soldering_masterclass_flux_lead_free_desoldering",
                "question": "Why does cold solder look dull and break apart, and why is rosin flux the magical secret to perfect shiny joints?",
                "focus": "Lead vs lead-free solder alloys, temperature-controlled irons (650°F-750°F), flux chemistry, desoldering braid/pumps, and through-hole capacitor swaps.",
                "reason": "Teaches the fundamental electronics craftsmanship required to resurrect dead circuit boards and audio cables."
            },
            {
                "id": 9,
                "title": "The Capacitor Plague: How Stolen Chemical Formulas Bricked Millions of Motherboards",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "capacitor_plague_1999_2007_motherboard_failures",
                "question": "Why did computer motherboards and flat-screen TVs from 1999-2007 bulge, leak brown crust, and die by the millions?",
                "focus": "Industrial espionage theft of incomplete water-based electrolyte formulas, hydrogen gas bulging, ESR (Equivalent Series Resistance) meters, and recapping boards.",
                "reason": "Fascinating historical look into the global electronic manufacturing defect that birthed modern capacitor-swapping repair."
            },
            {
                "id": 10,
                "title": "Plumbing Rescues: Sweating Copper Pipes, PEX Crimp Rings, and Running Toilets",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "plumbing_repair_copper_sweating_pex_flapper_valves",
                "question": "How do you torch-sweat a leak-free copper pipe joint and fix a phantom-flushing toilet in 15 minutes?",
                "focus": "Propane torch soldering, water draining before heat, PEX tubing vs copper pros/cons, toilet flapper valve degradation, and shutoff valve emergencies.",
                "reason": "Crucial household maintenance skills to prevent catastrophic multi-thousand-dollar water damage."
            },
            {
                "id": 11,
                "title": "Refrigerator Diagnostics: When It's Warm on Top and Freezing on the Bottom",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "refrigerator_repair_defrost_heater_evaporator_fan",
                "question": "Why does ice buildup on the back freezer wall indicate a failed defrost thermostat rather than a dead compressor?",
                "focus": "Vapor compression refrigeration cycles, defrost heater element testing, bimetal defrost thermostats, evaporator fan motors, and condenser coil cleaning.",
                "reason": "Masterclass on diagnosing the true electrical root causes behind refrigerator cooling failures."
            },
            {
                "id": 12,
                "title": "Drywall Surgery: Patching Doorknob Holes and Seamless Mud Blending",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "practical_playbook",
                "slug": "drywall_patching_california_patch_feathering",
                "question": "How does the 'California Patch' use the drywall's own paper backing to create an invisible patch without wooden backing studs?",
                "focus": "California drywall patch technique, mesh tape vs paper tape, setting-type hot mud (20-minute) vs premixed joint compound, feathering edges, and sanding flush.",
                "reason": "Teaches the essential aesthetic craftsmanship required to make drywall repairs completely invisible under paint."
            },
            {
                "id": 13,
                "title": "Hot Air Micro-Soldering: Surface Mount (SMD) Rework and USB-C Port Replacement",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "micro_soldering_hot_air_smd_usb_c_replacement",
                "question": "How do board technicians replace 24 microscopic USB-C pins soldered beneath a phone motherboard without melting nearby chips?",
                "focus": "Hot air rework stations, solder paste stencils, kapton tape thermal shielding, microscope inspection, and surface tension self-alignment.",
                "reason": "Advanced electronic repair methodology necessary for modern smartphones, laptops, and tablets."
            },
            {
                "id": 14,
                "title": "3D Printing Replacement Parts: Rebuilding Obsolete Plastic Gears with CAD",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "field_investigation",
                "slug": "3d_printing_replacement_parts_reverse_engineering_gears",
                "question": "How can a $200 3D printer save a vintage KitchenAid mixer or car dashboard vent when the manufacturer discontinued the part in 1995?",
                "focus": "Digital caliper measurement precision, FreeCAD/Fusion 360 involute gear generation, PETG and Nylon filament strength vs brittle PLA, and print layer orientation.",
                "reason": "Showcases the empowering fusion of additive manufacturing and reverse-engineering to defeat planned obsolescence."
            },
            {
                "id": 15,
                "title": "Louis Rossmann and the Right to Repair: The Legal Battle Against Board-Level Monopolies",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "louis_rossmann_right_to_repair_movement",
                "question": "How did an independent MacBook repair shop owner in Manhattan build a national political movement with millions of supporters?",
                "focus": "Independent repair shop economics, customs border seizures of replacement glass, Apple Authorized Service Provider (AASP) restrictions, and passing state repair bills.",
                "reason": "Profiles the leading modern activist who transformed frustrating electronics repairs into a global consumer rights crusade."
            },
            {
                "id": 16,
                "title": "Oscilloscope Diagnostics: Tracing Power Rails and Clock Signals on Dead Laptops",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "deep_dive",
                "slug": "oscilloscope_diagnostics_power_rails_clock_signals",
                "question": "When a laptop draws zero amps from the charger, how do you trace sequential power rails (PPBUS_G3H) to find the single shorted capacitor?",
                "focus": "Boardview software (.fz / .brd), PDF schematic signal tracing, power sequence timing diagrams, short-circuit thermal cameras, and bench power supply current injection.",
                "reason": "The pinnacle of component-level logic board diagnostics separating parts-swappers from true electrical engineers."
            },
            {
                "id": 17,
                "title": "Rust Remediation and Metal Preservation: Electrolysis and Chemical Conversion",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "mechanisms_and_systems",
                "slug": "rust_removal_electrolysis_phosphoric_acid_conversion",
                "question": "How does submerged sacrificial iron and washing soda in water use 12 volts of DC current to gently strip 100 years of iron oxide rust?",
                "focus": "Electrolytic rust removal chemistry, sacrificial anodes, phosphoric acid iron phosphate conversion, Evapo-Rust chelating agents, and boiled linseed oil finishes.",
                "reason": "Explores the non-destructive chemical and electrical techniques used to restore antique tools and vintage machinery."
            },
            {
                "id": 18,
                "title": "Parts Pairing and Serialization: The Cryptographic Anti-Repair Nightmare",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "parts_pairing_serialization_cryptographic_anti_repair",
                "question": "Why does swapping two genuine, identical screens between two brand-new iPhones disable FaceID and True Tone on both devices?",
                "focus": "Cryptographic EEPROM handshake pairing, secure enclave authentication, blocking third-party repair shops, and EU eco-design regulatory bans on serialization.",
                "reason": "A critical technical examination of Big Tech's shift from mechanical glue barriers to cryptographic software locks against repair."
            },
            {
                "id": 19,
                "title": "The Repair Café Movement: Community Fixing vs Disposable Society",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "repair_cafe_movement_circular_economy_community",
                "question": "How are volunteer workshops in 3,000 cities across the globe bringing neighbors together to fix toasters and sew torn coats for free?",
                "focus": "Martine Postma's Amsterdam origins, knowledge transfer between retired tradespeople and youth, reducing municipal landfill e-waste, and community resilience.",
                "reason": "Celebrates the grassroots social movement reclaiming community repair as a joyful, ecological civic practice."
            },
            {
                "id": 20,
                "title": "The Master Repair Workshop Architecture: The Complete Professional Blueprint",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_repair_workshop_architecture_blueprint",
                "question": "What comprehensive operational framework organizes diagnostic stations, electrostatic discharge (ESD) protection, tool layout, and inventory?",
                "focus": "ESD mat grounding protocols, fume extraction ventilation, 5S workshop organization, standardized hardware bin inventory (metric/imperial), and safe chemical storage.",
                "reason": "Definitive capstone masterclass synthesizing all 20 repair episodes into an elite craftsman's workshop and diagnostic blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Phoebus Cartel: How Corporations Conspired to Make Lightbulbs Burn Out Quickly",
                "trend_score": "Massive Corporate Conspiracy Fascination (Evergreen)",
                "angle": "historical_evolution",
                "slug": "phoebus_cartel_planned_obsolescence_exposed_viral",
                "why_trending": "The declassified true story of the 1920s corporate cartel creating planned obsolescence remains the #1 favorite anti-corporate history story.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Why Blue-Can WD-40 is Ruining Your Tools (And What You Should Use Instead)",
                "trend_score": "High Everyday DIY Relatability & Debate",
                "angle": "beginner_guide",
                "slug": "stop_using_wd40_wrong_lubricant_guide",
                "why_trending": "Telling people they've been using the world's most famous blue can incorrectly on bike chains and door hinges generates millions of views.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why Apple Made It Illegal to Swap Screens Between Two Brand-New iPhones",
                "trend_score": "High Tech Outrage & Right-to-Repair Hook",
                "angle": "systemic_critique",
                "slug": "apple_parts_pairing_serialization_screen_swap_scandal",
                "why_trending": "Watching a repair YouTuber take two genuine Apple phones out of boxes, swap their screens, and have error messages appear went viral worldwide.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The Microwave Capacitor: The Deadliest Part in Your House (Safety Warning)",
                "trend_score": "High Danger & Safety Warning Spike",
                "angle": "root_cause_analysis",
                "slug": "microwave_high_voltage_capacitor_shock_danger",
                "why_trending": "Showing the massive 2,000-volt spark when shorting an unplugged microwave capacitor teaches viewers serious respect for electronics.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "How to Clean a Lawnmower Carburetor in 15 Minutes with a Guitar String",
                "trend_score": "High Springtime Homeowner Practical Traffic",
                "angle": "practical_playbook",
                "slug": "fix_surging_lawnmower_carburetor_clean_jet",
                "why_trending": "Every spring, millions of homeowners panic when their mower won't start; this simple fix saves them $150 and gets massive seasonal traffic.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Electrolysis Rust Removal: The Easiest Way to Clean Rusty Tools with Water & Electricity",
                "trend_score": "High Satisfying Restoration Chemistry Spike",
                "angle": "mechanisms_and_systems",
                "slug": "electrolysis_rust_removal_car_battery_charger",
                "why_trending": "Submerging a rusty 100-year-old vise in bubbly water and pulling out bare metal hours later is pure internet satisfaction.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The California Patch: The Secret Drywall Trick Every Painter Uses to Hide Holes",
                "trend_score": "High Satisfying Home Improvement Hook",
                "angle": "famous_examples",
                "slug": "california_drywall_patch_trick_seamless_repair",
                "why_trending": "Cutting paper backing on drywall to make a self-supporting invisible patch blows the minds of first-time homeowners on TikTok and YouTube.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "138_bicycles_cycling": {
        "id": "138",
        "slug": "bicycles_cycling",
        "title": "Bicycles & Cycling",
        "category": "Sports_Adventure",
        "audience": "Road Cyclists, Mountain Bikers, Commuters, Bike Mechanics, Frame Builders (Global)",
        "progression": [
            ("Tier 1: Bike Geometry, Drivetrain Ratios & Tire Pressure Physics (Beginner / Scratch)",
             "Head tube angles and trail stability, gear inches and cadence mathematics, Silca rolling resistance tire pressure curves, chain lubrication physics, and basic bike fit."),
            ("Tier 2: Frame Material Dynamics (Steel, Aluminum, Carbon, Titanium) & Disc Brakes (Intermediate)",
             "Yield strength and fatigue limits of 4130 chromoly vs 6061-T6 aluminum vs unidirectional carbon fiber vs Grade 9 titanium, hydraulic disc brake fluid dynamics, and wheel truing."),
            ("Tier 3: Aerodynamics, Marginal Gains, Tubeless Tech & The Tour de France (Upper Intermediate)",
             "Wind tunnel drag coefficient (CdA), marginal gains in pro peloton, tubeless sealant chemistry and bead hooks, aerodynamic wheel depth trade-offs, and power meter FTP pacing."),
            ("Tier 4: E-Bike Transits, Urban Cycling Infrastructure & The Master Custom Frame Blueprint (Advanced / Masterclass)",
             "Torque sensor mid-drive motors vs hub motors, Dutch protected junction civil engineering, custom frame jig welding/brazing, and the future of human-electric micromobility.")
        ],
        "flagship": {
            "title": "Steel is Real vs Carbon Fiber: The Great Frame Material Showdown",
            "angle": "comparative_analysis",
            "slug": "138_bicycles_cycling_comparative_analysis_steel_vs_carbon"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Steel is Real vs Carbon Fiber: The Great Frame Material Showdown",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "steel_vs_carbon_fiber_frame_materials",
                "question": "Why do bespoke frame builders swear by 4130 Chromoly steel while modern Tour de France pelotons race exclusively on carbon fiber?",
                "focus": "Tensile strength to weight ratios, fatigue limits (infinite fatigue endurance of steel/titanium vs aluminum), vibration damping, and catastrophic carbon failure modes.",
                "reason": "Crucial foundational episode exploring the physics, metallurgy, and soul behind bicycle frame materials."
            },
            {
                "id": 2,
                "title": "The Physics of Bicycle Stability: Why a Moving Bike Doesn't Fall Over",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "bicycle_stability_physics_gyroscopic_trail",
                "question": "Is it gyroscopic wheel precession or fork caster trail that keeps an unmanned moving bicycle perfectly upright?",
                "focus": "The 1970 David Jones unrideable bike experiments, head tube angle, fork rake, trail calculation, and forward center of mass self-steering.",
                "reason": "Teaches the counter-intuitive dynamics and centuries-old physics debate governing two-wheeled balance."
            },
            {
                "id": 3,
                "title": "Gear Inches and Cadence: The Mechanical Advantage of the Bicycle Drivetrain",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "gear_inches_cadence_drivetrain_ratios",
                "question": "Why is grinding at 60 RPM worse for your leg muscles than spinning smoothly at 90 RPM in a lower gear ratio?",
                "focus": "Gear inch formulas, chainring-to-cassette ratios, 1x vs 2x drivetrains, derailleur parallelogram mechanics, and neuromuscular efficiency.",
                "reason": "Demystifies the mechanical gearing and biological metabolic trade-offs behind human pedaling power."
            },
            {
                "id": 4,
                "title": "Tire Pressure and Rolling Resistance: Why High Pressure Actually Makes You Slower",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "root_cause_analysis",
                "slug": "tire_pressure_rolling_resistance_silca_breakdown",
                "question": "Why did pro cyclists spend 50 years pumping tires rock-hard to 120 PSI, and why does 75 PSI roll significantly faster?",
                "focus": "Casing hysteresis loss vs suspension impedance losses on rough asphalt, Silca breakpoint pressure curves, wider 28mm/30mm tire science, and contact patches.",
                "reason": "Deconstructs the single biggest paradigm shift in modern cycling performance and comfort."
            },
            {
                "id": 5,
                "title": "Bike Fit Ergonomics: Solving Knee Pain, Numb Hands, and Saddle Sores",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "practical_playbook",
                "slug": "bike_fit_ergonomics_saddle_height_reach",
                "question": "How does raising your saddle by 5 millimeters eliminate anterior knee pain and unlock 20 extra watts of pedaling power?",
                "focus": "Knee flexion angle at bottom dead center (25-35 degrees), saddle setback, reach and stack geometry, sit bone measurement, and ulnar nerve pressure.",
                "reason": "Essential practical guide to customizing bicycle contact points to human biomechanics for injury-free riding."
            },
            {
                "id": 6,
                "title": "Hydraulic Disc Brakes vs Rim Brakes: The Stopping Power Revolution",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "hydraulic_disc_brakes_vs_rim_brakes",
                "question": "How does Pascal's law of fluid pressure give index-finger braking power in pouring rain down a 15% alpine descent?",
                "focus": "Mineral oil vs DOT fluid, master cylinder to slave caliper piston area multiplication, rotor thermal dissipation, wet braking rim delamination, and thru-axle stiffness.",
                "reason": "Analyzes the technological and safety breakthrough that made rim caliper brakes obsolete across modern cycling."
            },
            {
                "id": 7,
                "title": "The Art of Wheel Truing: Spoke Tension, Radial Runout, and Dishing",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "wheel_truing_spoke_tension_radial_runout",
                "question": "How do 32 thin wires under 120 kilograms of tension suspend a 200-pound rider without buckling over potholes?",
                "focus": "Tensioned spoke wheel physics (standing on the hub vs hanging from upper spokes), truing stands, spoke nipple keys, tensiometer readings, and asymmetric rear dishing.",
                "reason": "Masterclass on the delicate structural craftsmanship and harmonic balance of building bicycle wheels."
            },
            {
                "id": 8,
                "title": "Tubeless Tires: How Liquid Latex and Rim Hooks Eliminated Pinch Flats",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "tubeless_tires_sealant_hookless_rims_debate",
                "question": "How does liquid latex seal a puncture from a thorny nail while riding at 25 MPH without losing tire pressure?",
                "focus": "Coagulation chemistry, Stan's NoTubes origins, hookless carbon rim blow-off controversies, lower operating pressures, and tubeless rim tape installation.",
                "reason": "Explores the off-road and road cycling revolution that relegated rubber inner tubes to emergency seat bags."
            },
            {
                "id": 9,
                "title": "Aerodynamics on Two Wheels: CdA, Wind Tunnels, and 80% Power Resistance",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "cycling_aerodynamics_cda_wind_tunnel_testing",
                "question": "Why is 80% of a cyclist's power spent pushing air aside at 20 MPH, and why does rider body position dwarf a $10,000 aero bike?",
                "focus": "Coefficient of drag area (CdA), deep-section carbon aero wheels (50mm vs 80mm crosswind stability), skinsuits, narrow handlebars, and aero tucks.",
                "reason": "Details the fluid dynamics governing road racing where saving 20 watts of aerodynamic drag decides Olympic medals."
            },
            {
                "id": 10,
                "title": "The Doping Dark Ages: EPO, Blood Bags, and the Lance Armstrong Era",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "lance_armstrong_epo_blood_doping_tour_de_france",
                "question": "How did synthetic erythropoietin (EPO) and refrigerated blood transfusion centrifuges turn cycling into a pharmaceutical arms race?",
                "focus": "Hematocrit 50% limit, nighttime heart attacks from sludge-thick blood, Michele Ferrari's protocols, USADA's Reasoned Decision report, and stripping 7 Tour titles.",
                "reason": "A sobering, rigorous investigation into the medical and systemic corruption that shattered professional cycling's credibility."
            },
            {
                "id": 11,
                "title": "Mountain Bike Suspension Kinematics: Horst Link vs VPP vs Single Pivot",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "mtb_suspension_kinematics_horst_link_vpp",
                "question": "How do four-bar linkages prevent pedaling forces from compressing the rear shock while keeping suspension active under hard braking?",
                "focus": "Instant centers, leverage rate curves (progressive vs linear), anti-squat percentages, anti-rise brake jack, and pedal kickback physics.",
                "reason": "Advanced mechanical engineering breakdown of full-suspension linkage design in modern mountain biking."
            },
            {
                "id": 12,
                "title": "The Chain Waxing Obsession: Why Molten Paraffin Beats Wet Lubes",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "chain_waxing_molten_paraffin_vs_drip_lubes",
                "question": "Why are competitive cyclists cleaning brand-new chains in mineral spirits and slow-cooking them in crockpots of paraffin wax?",
                "focus": "Factory grease removal, friction loss testing (Zero Friction Cycling data), avoiding grinding paste abrasive wear, and extending drivetrain lifespan by 400%.",
                "reason": "Examines the nerdy marginal-gains maintenance cult transforming mechanical drivetrain efficiency."
            },
            {
                "id": 13,
                "title": "The Hour Record: The Purest, Most Brutal Endurance Test in Sports",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "famous_examples",
                "slug": "uci_hour_record_filippo_ganna_merckx",
                "question": "How did Filippo Ganna ride 56.792 kilometers in exactly 60 minutes on an indoor velodrome track with zero gears or brakes?",
                "focus": "Fixed gear track bikes, aerodynamic 3D-printed titanium frames, metabolic threshold pacing (lactate clearance), and the historic Merckx vs Boardman equipment battles.",
                "reason": "Celebrates the ultimate individual battle against time, physics, and physiological agony in cycling."
            },
            {
                "id": 14,
                "title": "The 1817 Dandy Horse to Safety Bicycle: The Two-Wheeled Technological Leap",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "historical_evolution",
                "slug": "history_of_the_bicycle_dandy_horse_penny_farthing",
                "question": "How did Karl von Drais's wooden balance bike and the terrifying high-wheel Penny Farthing evolve into the chain-driven Safety Bicycle?",
                "focus": "Year Without a Summer horse famine, high-wheel rollover header crashes, John Kemp Starley's 1885 Rover safety bike, and John Boyd Dunlop's pneumatic tire.",
                "reason": "Chronicles the mechanical evolution that gave humanity its most energy-efficient vehicle and sparked the women's suffrage movement."
            },
            {
                "id": 15,
                "title": "E-Bikes: Torque Sensors vs Cadence Sensors and the Transit Revolution",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "ebike_motors_torque_vs_cadence_sensors_mid_drive",
                "question": "Why does a mid-drive motor with a strain-gauge torque sensor feel like having bionic legs, while cheap hub motors feel like a scooter throttle?",
                "focus": "Piezoelectric torque sensing math, brushless DC motor integration, planetary gear reduction, battery fire safety standards (UL 2849), and Class 1-3 regulations.",
                "reason": "Deconstructs the electro-mechanical technology powering the explosive global boom in e-mobility."
            },
            {
                "id": 16,
                "title": "The Dutch Cycling Miracle: How the Netherlands Banned Cars in the 1970s",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "case_study",
                "slug": "dutch_cycling_infrastructure_stop_de_kindermoord",
                "question": "How did grassroots protests over child traffic deaths and the 1973 oil crisis turn a car-centric country into a cycling paradise?",
                "focus": "'Stop de Kindermoord' civic protests, continuous separated cycle tracks, protected intersections, roundabouts with cyclist priority, and multimodal train commuting.",
                "reason": "Masterclass on urban planning and civil engineering proving that mass cycling is a policy choice, not an accident of geography."
            },
            {
                "id": 17,
                "title": "Frame Building: The Alchemy of TIG Welding and Silver Brazing Tubing",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "field_investigation",
                "slug": "custom_frame_building_tig_welding_lugged_brazing",
                "question": "How do artisan builders mitre paper-thin Columbus and Reynolds steel tubes and braze them into ornate cast lugs with silver flux?",
                "focus": "Heat-affected zones (HAZ), frame alignment jigs, tube butting profiles (double-butted walls), brass vs silver brazing temperatures, and liquid metal capillary flow.",
                "reason": "Explores the artisanal, precision metalworking craft behind custom bespoke bicycle construction."
            },
            {
                "id": 18,
                "title": "Ultra-Endurance Bikepacking: The Transcontinental Race and Self-Supported Survival",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "transcontinental_race_bikepacking_mike_hall",
                "question": "How do cyclists race 4,000 kilometers across Europe sleeping 3 hours a night in bank ATM vestibules with zero outside support?",
                "focus": "Mike Hall's legacy, dynamo hub lighting and USB charging, bivvy bag sleep setups, caloric fueling strategies (6,000 kcal/day), and mental hallucination management.",
                "reason": "Examines the extreme frontier where cycling merges with wilderness survival and psychological endurance."
            },
            {
                "id": 19,
                "title": "The Death of the Front Derailleur: The Rise of 1x Drivetrains in Gravel and Mountain",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "1x_drivetrain_revolution_narrow_wide_chainrings",
                "question": "How did narrow-wide chainring tooth profiles and clutch rear derailleurs allow riders to ditch front shifters forever?",
                "focus": "Alternating tooth thickness preventing chain drops, 10-52T wide-range cassettes, eliminating chain rub, frame tire clearance gains, and gear step gaps.",
                "reason": "Analyzes the recent mechanical design shift simplifying drivetrains across mountain, gravel, and commuter bikes."
            },
            {
                "id": 20,
                "title": "The Master Bicycle Fleet Architecture: Maintenance, Geometry & Fleet Management",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_bicycle_fleet_architecture_maintenance_blueprint",
                "question": "What comprehensive mechanical system covers torque wrench specifications, bearing overhauls, cable routing, and fleet longevity?",
                "focus": "Sealed cartridge vs cup-and-cone bearings, bottom bracket standards (threaded vs press-fit), systematic 500-mile maintenance checkouts, and pro shop workflow ergonomics.",
                "reason": "Definitive capstone masterclass synthesizing all 20 cycling episodes into a master mechanic's technical and operational guide."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Pro Cyclists Stopped Pumping Tires to 120 PSI (The Pressure Myth Exposed)",
                "trend_score": "Massive Cycling Tech & Everyday Hook (Evergreen)",
                "angle": "root_cause_analysis",
                "slug": "tire_pressure_myth_exposed_lower_pressure_faster",
                "why_trending": "The shocking revelation that lower tire pressure rolls faster by preventing microscopic vibrations blew the minds of road cyclists.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Why Cheap E-Bikes Keep Burning Down Apartments: The Battery Reality",
                "trend_score": "High Public Safety & Consumer Concern Spike",
                "angle": "root_cause_analysis",
                "slug": "ebike_lithium_battery_fires_thermal_runaway_cheap",
                "why_trending": "Fire department footage and investigations into uncertified lithium-ion packs undergoing explosive thermal runaway pulls huge traffic.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Steel vs Carbon: What Actually Happens When a Frame Crashes?",
                "trend_score": "High Frame Material Debate Volume",
                "angle": "comparative_analysis",
                "slug": "steel_vs_carbon_bike_crash_durability_test",
                "why_trending": "Stress tests crushing carbon and steel frames in hydraulic presses to show catastrophic fracture vs bending went massively viral.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "How the Netherlands Built the World's Best Bike Cities (It Wasn't Always Like This)",
                "trend_score": "High Urban Planning & Travel Wonder Hook",
                "angle": "case_study",
                "slug": "how_amsterdam_became_bicycle_capital_history",
                "why_trending": "Archival footage showing 1970s Amsterdam choked with car smog before citizens protested to build bike paths inspires millions.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Chain Waxing Obsession: Why Roadies Cook Chains in Slow Cookers",
                "trend_score": "High Marginal Gains & Bizarre Hobby Spike",
                "angle": "practical_playbook",
                "slug": "hot_melt_chain_waxing_guide_zero_friction",
                "why_trending": "The quirky ritual of melting paraffin wax in a Crock-Pot to save 3 watts and keep drivetrains clean fascinates cyclists.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "The Lance Armstrong Doping Machine: The Most Sophisticated Fraud in Sports",
                "trend_score": "High Sports Scandal & True Crime Hook",
                "angle": "deep_dive",
                "slug": "lance_armstrong_doping_program_usada_breakdown",
                "why_trending": "Deconstructing the secret motorhomes, taped EPO vials in bushes, and Swiss bank accounts behind the Tour de France empire.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Why You Don't Fall Off a Bike: The 100-Year Physics Mystery Solved",
                "trend_score": "High Science & Intuition Mystery Hook",
                "angle": "beginner_guide",
                "slug": "physics_of_bicycle_balance_mystery_solved",
                "why_trending": "Proving that gyroscopic forces have almost nothing to do with keeping a bike upright shocks viewers who assumed wheel spinning was the key.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "139_motorcycles": {
        "id": "139",
        "slug": "motorcycles",
        "title": "Motorcycles",
        "category": "Sports_Adventure",
        "audience": "Motorcycle Riders, Moto-Bloggers, Engine Tuners, Cafe Racer Builders, Track Day Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Two-Wheel Gyroscopic Physics, Countersteering & Motorcycle Ergonomics (Beginner / Scratch)",
             "Countersteering physics (push right to go right), gyroscopic precession, rake and trail geometry, friction circle traction budgets, and clutch friction zone control."),
            ("Tier 2: Engine Architectures, Carburetor vs EFI & Suspension Geometry (Intermediate)",
             "V-Twin vs Inline-4 vs Parallel-Twin vs Boxer torque curves, telescopic fork damping rods vs cartridge valves, chain drive vs shaft drive, and setting suspension sag."),
            ("Tier 3: Track Cornering Dynamics, Trail Braking & High-Speed Safety Electronics (Upper Intermediate)",
             "Trail braking past the turn-in point, highside vs lowside crashes, 6-axis Inertial Measurement Units (IMUs), cornering ABS, and quickshifter ignition cuts."),
            ("Tier 4: Adventure Touring Logistics, Isle of Man TT Danger & Electric Moto Futures (Advanced / Masterclass)",
             "The lethal Isle of Man TT course physics (135 mph average on country roads), round-the-world ADV logistics, electric motorcycle torque-density, and custom chassis fabrication.")
        ],
        "flagship": {
            "title": "Countersteering Explained: The Counter-Intuitive Physics of Turning a Motorcycle",
            "angle": "beginner_guide",
            "slug": "139_motorcycles_beginner_guide_countersteering_explained"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Countersteering Explained: The Counter-Intuitive Physics of Turning a Motorcycle",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "countersteering_physics_push_right_go_right",
                "question": "Why must you push the right handlebar forward (turning the front wheel left) to initiate a high-speed right turn?",
                "focus": "Out-tracking roll moment, gyroscopic precession of front wheel, tire contact patch displacement beneath center of mass, and Keith Code's No-BS Bike experiments.",
                "reason": "Crucial foundational episode demystifying the indispensable single control input governing all single-track vehicle steering."
            },
            {
                "id": 2,
                "title": "Engine Character: V-Twin vs Inline-4 vs Parallel Twin vs Boxer",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "motorcycle_engine_configurations_v_twin_inline_four",
                "question": "Why does a Harley 45-degree V-Twin rumble with low-end torque while an R1 Inline-4 screeches like a Formula 1 car at 14,000 RPM?",
                "focus": "Crankshaft pin offsets (270-degree crossplane firing orders), primary and secondary dynamic balancing, low-end torque vs high-RPM horsepower, and center of gravity.",
                "reason": "Teaches how mechanical engine cylinder layout dictates the sound, vibration, and handling soul of a motorcycle."
            },
            {
                "id": 3,
                "title": "The Traction Budget: The Friction Circle and Why Panicking Ruins Turns",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "motorcycle_traction_budget_friction_circle",
                "question": "Why does grabbing the front brake in the middle of a lean angle overload your front tire and cause an instant lowside crash?",
                "focus": "Kamm's friction circle, 100% traction budget split between lean force and braking/acceleration, tire contact patch squirm, and progressive control.",
                "reason": "Deconstructs the mathematical boundary of motorcycle grip essential for staying alive on two wheels."
            },
            {
                "id": 4,
                "title": "Clutch Friction Zone Mastery: Low-Speed Maneuvers and Police Rodeo Riding",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "practical_playbook",
                "slug": "clutch_friction_zone_police_motorcycle_rodeo",
                "question": "How do motor officers whip 900-pound Harley-Davidsons through tight 18-foot figure-8 cones without tipping over?",
                "focus": "Wet multi-plate clutch slipping, dragging the rear brake against engine torque (drivetrain tensioning), head-and-eyes target fixation, and counter-balancing.",
                "reason": "Provides a step-by-step masterclass on the fine motor clutch-and-brake coordination behind low-speed precision handling."
            },
            {
                "id": 5,
                "title": "Target Fixation: The Deadly Neurological Trap That Pulls You Toward Hazards",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "psychological_breakdown",
                "slug": "target_fixation_motorcycle_survival_reaction",
                "question": "Why do motorcyclists staring at a pothole or guardrail steer directly into the very obstacle they are desperate to avoid?",
                "focus": "Survival reactions (SRs), vestibular-ocular coupling, looking through the turn to the exit, panoramic peripheral vision, and panic reflex management.",
                "reason": "Examines the primary cognitive failure mode responsible for single-vehicle motorcycle run-off-road accidents."
            },
            {
                "id": 6,
                "title": "Motorcycle Suspension: Setting Sag, Compression, and Rebound Damping",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "motorcycle_suspension_tuning_sag_rebound_compression",
                "question": "How does spending an hour measuring spring preload and adjusting clicker valves transform a harsh, skittering bike into a glued cornering machine?",
                "focus": "Static and rider sag calculations (30-35mm target), shim stacks in cartridge forks, high vs low-speed compression, and packing down vs pogo rebound damping.",
                "reason": "Masterclass on demystifying suspension tuning to maximize tire contact patch grip over imperfect road surfaces."
            },
            {
                "id": 7,
                "title": "Trail Braking Masterclass: Why Modern Riders Brake All the Way to the Apex",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "trail_braking_technique_cornering_safety",
                "question": "Why did riding schools teach 'finish all braking in a straight line' for 30 years, and why is trail braking actually safer?",
                "focus": "Front fork compression steepening rake/trail for faster steering, trailing off brake pressure as lean angle increases, adjusting turn radius with front brake, and emergency stopping mid-corner.",
                "reason": "Explains the most important advanced riding technique that dramatically expands safety margins on unknown canyon roads."
            },
            {
                "id": 8,
                "title": "Highside vs Lowside Crashes: The Violent Physics of Losing Grip",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "highside_vs_lowside_motorcycle_crash_physics",
                "question": "What happens when a spinning rear tire breaks traction, steps out sideways, and suddenly bites into pavement?",
                "focus": "Lowside sliding friction loss, highside kinetic energy catapult (suspension unloading like a springboard), chassis rotational momentum, and avoiding panic throttle chops.",
                "reason": "Rigorous physical analysis of the two primary crash archetypes and how rider inputs trigger them."
            },
            {
                "id": 9,
                "title": "Chain Drive vs Belt vs Shaft Drive: The Power Transfer Battle",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "comparative_analysis",
                "slug": "motorcycle_final_drive_chain_belt_shaft",
                "question": "Why do sportbikes use greasy roller chains, cruisers use carbon belts, and BMW adventure tourers use heavy enclosed shafts?",
                "focus": "Mechanical power efficiency (98% for roller chains), un-sprung weight penalties, BMW Paralever anti-jacking shaft geometry, belt longevity without oiling, and maintenance trade-offs.",
                "reason": "Details the engineering rationale dictating final drive mechanisms across diverse motorcycle genres."
            },
            {
                "id": 10,
                "title": "The 1969 Honda CB750: The Four-Cylinder Machine That Invented the Superbike",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "honda_cb750_superbike_invention_1969",
                "question": "How did Soichiro Honda's transverse inline-4 with electric start and front disc brake kill the British motorcycle industry in one year?",
                "focus": "Oil-tight reliability, overhead camshaft smooth power, push-button electric start vs finicky British kickstarters, affordable performance, and the Universal Japanese Motorcycle (UJM).",
                "reason": "Chronicles the defining technological tipping point that established Japanese dominance over global motorcycle manufacturing."
            },
            {
                "id": 11,
                "title": "The Electronics Revolution: 6-Axis IMUs, Cornering ABS, and Wheelie Control",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "motorcycle_electronics_6_axis_imu_cornering_abs",
                "question": "How do gyro-sensors calculating roll, pitch, and yaw 1,000 times a second allow a 200-horsepower superbike to pin the throttle mid-corner without crashing?",
                "focus": "Bosch Motorcycle Stability Control (MSC), lean-angle sensitive ABS pressure modulation, ride-by-wire throttle mapping, slide control algorithms, and fly-by-wire rider aids.",
                "reason": "Deconstructs the silicon safety net that made 200+ horsepower production superbikes manageable for mortal humans."
            },
            {
                "id": 12,
                "title": "The Quickshifter and Autoblipper: Shifting Gears at Wide-Open Throttle in 50 Milliseconds",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "quickshifter_autoblipper_load_cell_shifting",
                "question": "How does a piezoelectric strain gauge on the shift rod allow clutchless upshifts and automatic throttle-blipped downshifts?",
                "focus": "Drivetrain dog-ring gear un-loading, ignition cut micro-bursts (40-60ms), electronic ride-by-wire throttle auto-blips on downshifts, and gearbox synchronization.",
                "reason": "Explains the electronic transmission technology adapted from MotoGP that eliminates clutch pulling during performance riding."
            },
            {
                "id": 13,
                "title": "The Isle of Man TT: The Most Dangerous Sporting Event on Earth",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "famous_examples",
                "slug": "isle_of_man_tt_danger_snaefell_mountain_course",
                "question": "Why do racers willingly blast past stone walls, lampposts, and village curb edges at 200 MPH where over 260 competitors have lost their lives?",
                "focus": "The 37.73-mile Snaefell Mountain Course, average lap speeds exceeding 135 MPH, jumping crests at Ballagarey (The Central Nervous System), mental memorization, and fatal risk philosophy.",
                "reason": "Profiles the absolute outer limit of motorcycling speed, human bravery, and archaic road-racing danger."
            },
            {
                "id": 14,
                "title": "Adventure Bike Logistics: How to Prepare a Motorcycle to Cross Continents",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "practical_playbook",
                "slug": "adventure_motorcycle_preparation_long_way_round",
                "question": "How do you outfit a BMW R1250GS or Yamaha Ténéré 700 to survive 20,000 miles of gravel, rivers, and zero mechanic support?",
                "focus": "Crash bar reinforcement, aluminum pannier weight balance, tire selection (50/50 knobbies), field tubeless tire plug kits, fuel filtration for bad gas, and Carnet de Passages border customs.",
                "reason": "Comprehensive operational guide to preparing two-wheeled machinery for intercontinental overland expedition travel."
            },
            {
                "id": 15,
                "title": "Cafe Racers and Custom Culture: Stripping Down Vintage Iron in the Ace Cafe Era",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "historical_evolution",
                "slug": "cafe_racer_history_ace_cafe_ton_up_boys",
                "question": "How did British 'Ton-Up Boys' in the 1960s strip down Triumph and Norton motorcycles to race between London transport cafes at 100 MPH?",
                "focus": "The Ton-Up 100 MPH milestone, clip-on handlebars, rearset footpegs, sweeping exhaust pipes, Triton hybrid builds (Norton featherbed frame with Triumph Bonneville engine), and custom culture.",
                "reason": "Celebrates the rebellious post-war subculture that invented the stripped-down minimalist custom motorcycle aesthetic."
            },
            {
                "id": 16,
                "title": "Motorcycle Safety Gear Science: CE Armor, Kevlar Abrasion, and Wireless Airbag Vests",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "deep_dive",
                "slug": "motorcycle_safety_gear_ce_armor_airbag_vests",
                "question": "How do standalone autonomous airbag vests inflate in 25 milliseconds before your body hits the pavement in a crash?",
                "focus": "D3O non-Newtonian shear-thickening impact armor, slide abrasion ratings (AA/AAA cordura and aramid), accelerometer crash detection algorithms, and CO2 canister deployment.",
                "reason": "Examines the cutting-edge impact biomechanics and wearable pyrotechnic airbags saving thousands of rider lives."
            },
            {
                "id": 17,
                "title": "Electric Motorcycles: Instant Torque vs The Highway Battery Range Problem",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "electric_motorcycles_instant_torque_battery_range",
                "question": "Why do electric bikes like the Zero SR/F offer blistering supercar acceleration in town, but drain their batteries in 45 minutes on the interstate?",
                "focus": "Zero-RPM peak torque dynamics, regenerative braking, lack of fairing aerodynamics at 75 MPH, thermal throttling in air-cooled packs, and fast-charging weight trade-offs.",
                "reason": "A sober, physics-based evaluation of the performance thrills and severe touring limitations facing battery-powered motorcycles."
            },
            {
                "id": 18,
                "title": "Chassis Geometry and Handling: Rake, Trail, Swingarm Angle, and Anti-Squat",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "mechanisms_and_systems",
                "slug": "motorcycle_chassis_geometry_rake_trail_anti_squat",
                "question": "How does dropping the front triple clamps by 3 millimeters completely transform how aggressively a motorcycle tips into corners?",
                "focus": "Steering head angle (rake), trail dimensions, offset triple clamps, swingarm pivot location relative to countershaft sprocket, and squat dynamics under acceleration.",
                "reason": "Advanced vehicle dynamics breakdown of frame geometry tuning for championship road racers."
            },
            {
                "id": 19,
                "title": "The Philosophy of the Open Road: Zen and the Art of Motorcycle Maintenance",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "zen_and_the_art_of_motorcycle_maintenance_pirsig",
                "question": "Why did Robert Pirsig use tuning a motorcycle's tappets as an inquiry into the nature of Quality and human technology?",
                "focus": "Classical rational understanding vs romantic sensory experience, gumption traps, mechanical empathy, and the meditative mindfulness of solo riding.",
                "reason": "Probes the deep existential, meditative, and psychological appeal of motorcycling as an antidote to modern alienation."
            },
            {
                "id": 20,
                "title": "The Master Rider Architecture: The Complete High-Performance & Survival System",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_motorcycle_rider_architecture_blueprint",
                "question": "What comprehensive daily riding framework unites visual scanning habits, trail braking execution, emergency swerves, and survival mental discipline?",
                "focus": "System of motorcycle control, pre-ride T-CLOCS mechanical inspection, SIPDE (Scan, Identify, Predict, Decide, Execute), weather contingency planning, and lifetime safety mastery.",
                "reason": "Definitive capstone masterclass synthesizing all 20 motorcycle episodes into an elite rider's survival and performance blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Countersteering: The Physics Trick That Feels 100% Wrong (Push Right to Turn Right)",
                "trend_score": "Massive Mind-Bending Riding Physics Spike (Evergreen)",
                "angle": "beginner_guide",
                "slug": "countersteering_push_right_turn_right_explained_viral",
                "why_trending": "Demonstrating that turning the handlebars left makes the bike drop right into a corner still sparks arguments among beginner riders.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The Isle of Man TT: Why Racers Willingly Risk Death at 200 MPH on Country Roads",
                "trend_score": "Massive High-Adrenaline Danger Hook",
                "angle": "famous_examples",
                "slug": "isle_of_man_tt_insane_speeds_danger_viral",
                "why_trending": "Onboard POV camera footage of superbikes flying past brick walls and garden hedges at 200 MPH is one of the most shared clips online.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Target Fixation: The Psychological Trap Killing Motorcyclists (And How to Stop It)",
                "trend_score": "High Motorcycle Safety & Viral Dashcam Analysis",
                "angle": "psychological_breakdown",
                "slug": "target_fixation_motorcycle_crashes_analyzed",
                "why_trending": "Dashcam clips analyzing why riders stare at a guardrail and ride directly into it despite plenty of room fascinates viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why You Should Trail Brake on the Street: The Modern Riding Revolution",
                "trend_score": "High Riding Technique & Debate Volume",
                "angle": "practical_playbook",
                "slug": "trail_braking_street_motorcycle_safety_guide",
                "why_trending": "Challenging old-school MSF advice by proving trail braking into corners saves lives sparked a massive online debate.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Police Motorcycle Rodeos: How Cops Whip 900lb Harleys in Impossible Tight Cones",
                "trend_score": "High Precision Skill & Admiration Spike",
                "angle": "field_investigation",
                "slug": "police_motorcycle_skills_rodeo_harley_friction_zone",
                "why_trending": "Footage of motorcycle police scraping floorboards while navigating tight cone mazes at slow speeds pulls tens of millions of views.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Highside Crashes Explained: The Physics of Being Thrown 15 Feet into the Air",
                "trend_score": "High Physics & Crash Analysis Hook",
                "angle": "root_cause_analysis",
                "slug": "highside_crash_physics_catapult_explained",
                "why_trending": "Slow-motion breakdowns showing the rear suspension compressing like a spring and bucking the rider over the handlebars.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Why Harley-Davidson Engines Shake Like Crazy (The 45-Degree V-Twin Secret)",
                "trend_score": "High Mechanical Engineering Curiosity",
                "angle": "comparative_analysis",
                "slug": "why_harley_davidson_v_twin_shakes_firing_order",
                "why_trending": "Explaining the single-pin crankshaft that causes the uneven 'potato-potato' firing order and iconic engine vibrations.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "140_sailing_yachting": {
        "id": "140",
        "slug": "sailing_yachting",
        "title": "Sailing & Yachting",
        "category": "Sports_Adventure",
        "audience": "Sailors, Yacht Skippers, Ocean Navigators, Boat Builders, America's Cup Fans (Global)",
        "progression": [
            ("Tier 1: Sail Aerodynamics (Bernoulli Lift), Points of Sail & Basic Nautical Knotwork (Beginner / Scratch)",
             "Sails as vertical airplane wings (lift vs drag), points of sail (close-hauled, beam reach, broad reach, run), tacking vs jibing, bowline knots, and keel ballast righting moments."),
            ("Tier 2: Celestial Navigation, Tide and Current Hydrodynamics & Heavy Weather Tactics (Intermediate)",
             "Marine sextants and noon sight latitude calculation, tidal flow vectors and dead reckoning, heaving-to in 40-knot gales, storm drogues, and anchor rode scope ratios."),
            ("Tier 3: Modern Hydrofoil Tech (America's Cup AC75), Offshore Passage Planning & Rigging Stress (Upper Intermediate)",
             "Apparent wind sailing faster than true wind, hydrofoil cavitation physics, standing rigging tension tuning, passage weather routing (GRIB files), and ocean survival rafts."),
            ("Tier 4: Solo Non-Stop Circumnavigations (Vendée Globe), Boatyard Maintenance & Master Ocean Skipper Blueprint (Advanced / Masterclass)",
             "The Vendée Globe Southern Ocean fury (Roaring Forties / Furious Fifties), fiberglass blister osmosis repair, dismasting jury-rigging, and the master ocean captain's offshore command system.")
        ],
        "flagship": {
            "title": "How Sailboats Sail Faster Than the Wind: Apparent Wind and Hydrofoil Physics",
            "angle": "mechanisms_and_systems",
            "slug": "140_sailing_yachting_mechanisms_and_systems_sailing_faster_than_wind"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "How Sailboats Sail Faster Than the Wind: Apparent Wind and Hydrofoil Physics",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "how_sailboats_sail_faster_than_wind_apparent_wind",
                "question": "How can a modern racing yacht sail at 50 knots when the natural wind speed is only blowing at 15 knots?",
                "focus": "Apparent wind vector addition (true wind + boat velocity), sails acting as aerodynamic aerofoils, hydrodynamic keel lift, and the elimination of downwind displacement sailing.",
                "reason": "Crucial foundational episode breaking the common misconception that sailboats merely get pushed downwind like leaves."
            },
            {
                "id": 2,
                "title": "Sails as Vertical Airplane Wings: Bernoulli's Principle on the Water",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "sail_aerodynamics_bernoulli_lift_circulation",
                "question": "Why can a sailboat sail toward the wind at a 45-degree angle without sliding backward?",
                "focus": "Low-pressure lift on the leeward camber, high pressure on the windward side, slot effect between jib and mainsail, and keel hydrofoil counteracting leeway drift.",
                "reason": "Teaches the essential fluid dynamics uniting aviation aerodynamics with nautical sailing."
            },
            {
                "id": 3,
                "title": "Points of Sail: Tacking, Jibing, and the Dangerous 'Death Roll'",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "points_of_sail_tacking_jibing_death_roll",
                "question": "Why is sailing directly downwind (running) the most dangerous point of sail for an inexperienced crew?",
                "focus": "Close-hauled, close reach, beam reach, broad reach, running, accidental jibe hazards (boom sweeps), preventer rigging, and recovering from broaching death rolls.",
                "reason": "Provides the essential sailing navigation compass and critical safety handling on open water."
            },
            {
                "id": 4,
                "title": "The Five Essential Knots: Bowlines, Cleat Hitches, and Figure Eights",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "practical_playbook",
                "slug": "essential_sailing_knots_bowline_cleat_hitch",
                "question": "Why is the Bowline called the King of Knots, and why will it never jam under thousands of pounds of line tension?",
                "focus": "Bowline loop knot, cleat hitch tying technique, figure-eight stopper knot, round turn and two half-hitches, sheet bend, and synthetic rope materials (Dyneema vs Dacron).",
                "reason": "Invaluable practical knotcraft and seamanship mastery required on every vessel afloat."
            },
            {
                "id": 5,
                "title": "Keel Ballast and Righting Moments: Why Monohulls Don't Capsize Permanently",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "keel_ballast_righting_moment_monohull_stability",
                "question": "What happens when a 50-foot ocean yacht gets knocked flat on its side by a rogue wave in the Atlantic?",
                "focus": "Center of gravity vs center of buoyancy, lead bulb keel ballast, righting lever curves (GZ curves), angle of vanishing stability (AVS > 120 degrees), and self-righting physics.",
                "reason": "Deconstructs the naval architecture keeping heavy displacement monohulls right-side up in violent seas."
            },
            {
                "id": 6,
                "title": "Celestial Navigation: How a Sextant and the Sun Find Your Latitude and Longitude",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "celestial_navigation_sextant_noon_sight",
                "question": "When all GPS satellites and shipboard electronics fry in a lightning strike, how do you cross oceans with a brass sextant?",
                "focus": "Index arm mirror angles, bringing the sun down to the horizon, local noon sight latitude, Marine Chronometer GMT longitude calculation, and sight reduction tables.",
                "reason": "Masterclass on the ancient, elegant mathematical art of reading the stars to pinpoint your position on a featureless ocean."
            },
            {
                "id": 7,
                "title": "The John Harrison Clock: The 40-Year War to Solve the Longitude Problem",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "longitude_problem_john_harrison_h4_chronometer",
                "question": "How did a Yorkshire carpenter invent frictionless marine chronometers that saved thousands of ships from crashing onto uncharted reefs?",
                "focus": "The 1714 British Longitude Act, Scilly naval disaster, bimetallic thermal compensation strips, grasshopper escapement, H4 pocket watch triumph, and Board of Longitude politics.",
                "reason": "The epic historical saga of precision horology and navigation that built the modern maritime world."
            },
            {
                "id": 8,
                "title": "Heavy Weather Tactics: Heaving-To, Sea Anchors, and Surfing Monster Waves",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "heavy_weather_sailing_tactics_heaving_to_drogues",
                "question": "How can a boat lock its rudder and backwind its jib to park itself peacefully in the middle of a 50-knot gale?",
                "focus": "Heaving-to mechanics, Jordan Series Drogues deployed off the stern, paratech sea anchors, pitchpoling risks, and reefing mainsails before the squall hits.",
                "reason": "Life-saving offshore seamanship protocols for surviving survival storms without engine power."
            },
            {
                "id": 9,
                "title": "The Art of Anchoring: Scope, Catches, and Why Boats Drag in the Night",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "root_cause_analysis",
                "slug": "boat_anchoring_physics_scope_ratio_holding_power",
                "question": "Why does an anchor hold like bedrock with a 7:1 rode scope ratio but pull clean out of mud with a 3:1 ratio?",
                "focus": "Chain catenary curve shock absorption, anchor shank horizontal pull angles, modern roll-bar scoop anchors (Rocna/Mantus) vs old CQR plows, and anchor watch alarms.",
                "reason": "Details the essential daily seamanship skill keeping cruising boats off jagged rocky shores while crews sleep."
            },
            {
                "id": 10,
                "title": "The America's Cup AC75: Flying 80-Foot Monohulls on Carbon Hydrofoils",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "americas_cup_ac75_hydrofoil_monohulls",
                "question": "How do 75-foot yachts lift completely out of the water and fly at 55 knots using canting T-foil arms and cyclist grinders?",
                "focus": "Hydrofoil cavitation speed limits, twin-skin D-section mainsails, battery hydraulic controls, cyclors pumping watts, and aerodynamic flight stability.",
                "reason": "Profiles the absolute pinnacle of high-tech naval architecture and aerospace fluid dynamics on the ocean."
            },
            {
                "id": 11,
                "title": "The Vendée Globe: The Everest of the Seas (Solo, Non-Stop, Unassisted)",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "famous_examples",
                "slug": "vendee_globe_solo_non_stop_circumnavigation",
                "question": "What kind of human spends 80 days alone in the freezing Southern Ocean racing a 60-foot IMOCA yacht through iceberg fields?",
                "focus": "The Roaring Forties and Screaming Fifties, Point Nemo isolation (nearest humans are on the Space Station), sleep polyphasic 20-minute naps, and mast climb repairs at sea.",
                "reason": "The quintessential extreme endurance challenge testing human psychological resilience and naval architecture."
            },
            {
                "id": 12,
                "title": "Tides, Currents, and Dead Reckoning: Navigating the English Channel",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "mechanisms_and_systems",
                "slug": "tidal_currents_dead_reckoning_vector_navigation",
                "question": "How do 5-knot tidal currents sweep sailboats sideways by 20 miles if a navigator fails to calculate vector set and drift?",
                "focus": "Rule of Twelfths tidal curve approximations, tidal diamond tables, Leeway angle compensation, course-to-steer vector triangles, and clearing bearings.",
                "reason": "Masterclass on the mathematical navigation required to safely cross tidal waterways with narrow rocky channels."
            },
            {
                "id": 13,
                "title": "The Golden Globe Race 1968: The Madness of Donald Crowhurst and Robin Knox-Johnston",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "1968_golden_globe_race_donald_crowhurst_tragedy",
                "question": "How did a bankrupt British inventor fake his position logs in the Atlantic before stepping into the ocean to drown in madness?",
                "focus": "The Sunday Times Golden Globe Race, Robin Knox-Johnston's wooden Suhaili victory, Donald Crowhurst's leaking trimaran, falsified radio cables, and philosophical breakdown.",
                "reason": "The haunting psychological tragedy that revealed the terrifying mental toll of solitary ocean isolation."
            },
            {
                "id": 14,
                "title": "Fiberglass Osmosis: The Gelcoat Cancer Rotting Boat Hulls from the Inside",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "failure_mode_analysis",
                "slug": "fiberglass_osmosis_gelcoat_blisters_boat_hull",
                "question": "Why do fluid-filled blisters smelling of vinegar bubble up on underwater fiberglass hulls, and how do boatyards cure it?",
                "focus": "Semi-permeable polyester gelcoat membranes, water-soluble binder breakdown (acetic acid pockets), moisture meter testing, hull peeling, and epoxy barrier coats.",
                "reason": "Rigorous materials science and maintenance analysis of the most feared hull defect in fiberglass yacht ownership."
            },
            {
                "id": 15,
                "title": "Standing Rigging Tuning: Tuning Mast Pre-Bend and Shroud Tension",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "field_investigation",
                "slug": "standing_rigging_tuning_mast_bend_shrouds",
                "question": "How do you tune forestays, backstays, and cap shrouds to give an aluminum mast proper pre-bend without bending it like a pretzel?",
                "focus": "Loos gauge wire tensioning, spreader sweep angles, mast rake, preventing dismasting under lee shroud slack, and swaged fitting crevice corrosion.",
                "reason": "Details the critical structural rigging mechanics supporting hundreds of square meters of sail in gale-force winds."
            },
            {
                "id": 16,
                "title": "Modern Weather Routing: Reading GRIB Files, Isobars, and Frontal Systems",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "deep_dive",
                "slug": "weather_routing_grib_files_isobars_ocean_passages",
                "question": "How do offshore skippers use satellite weather models (ECMWF/GFS) and polar curves to sail around storms before they form?",
                "focus": "GRIB wind vectors, polar boat velocity curves, isochrone routing algorithms (PredictWind), warm/cold frontal boundaries, and dodging low-pressure bomb cyclones.",
                "reason": "Teaches the meteorological science and software routing that transformed offshore ocean voyaging safety."
            },
            {
                "id": 17,
                "title": "Catamarans vs Monohulls: The Blue Water Cruising Civil War",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "comparative_analysis",
                "slug": "catamaran_vs_monohull_bluewater_cruising_debate",
                "question": "Is the flat sailing, spacious galley, and shallow draft of a multihull safer than a heavy monohull that can self-right after a knockdown?",
                "focus": "Form stability vs ballast stability, multihull capsize irreversibility, bridge deck slamming in heavy chop, marina docking fees, and offshore seaworthiness.",
                "reason": "Thoroughly analyzes the defining debate dividing modern liveaboard sailors and circumnavigators."
            },
            {
                "id": 18,
                "title": "Orca Encounters in the Strait of Gibraltar: Why Killer Whales Are Biting Rudders",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "field_investigation",
                "slug": "orca_attacks_strait_of_gibraltar_boat_rudders",
                "question": "Why did a pod of Iberian killer whales start systematically snapping fiberglass rudders off sailboats, sinking multiple yachts?",
                "focus": "Gladis pod behavioral culture transmission, cetacean playful trauma theories, pingers and acoustic deterrents, emergency drogue steering, and safety protocols.",
                "reason": "Investigates the bizarre, escalating maritime wildlife mystery baffling scientists and terrorizing sailors off Spain and Portugal."
            },
            {
                "id": 19,
                "title": "The Liveaboard Dream vs Reality: Maintenance in Exotic Places",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "liveaboard_sailing_reality_boatlife_maintenance",
                "question": "Why is the romantic fantasy of sipping rum in Caribbean anchorages actually 'fixing your boat in exotic locations'?",
                "focus": "Marine head toilet plumbing nightmares, diesel engine salt-water impeller changes, watermaker maintenance, anchoring stress, and true psychological freedom.",
                "reason": "A humorous, brutally honest, and insightful look into the true daily reality of full-time cruising life."
            },
            {
                "id": 20,
                "title": "The Master Ocean Skipper Architecture: Complete Offshore Passage Blueprint",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_ocean_skipper_architecture_offshore_blueprint",
                "question": "What comprehensive operational doctrine covers watch-keeping rotas, emergency abandon-ship drills, medical triage at sea, and passage provisioning?",
                "focus": "Watch schedules (Swedish 3-hour watch system), grab-bag ditch kits, EPIRB satellite registration, bilge pump manifold redundancy, and offshore leadership command.",
                "reason": "Definitive capstone masterclass synthesizing all 20 sailing episodes into an offshore ocean captain's master operational blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "How Sailboats Sail Faster Than the Wind: The Mind-Bending Physics Explained",
                "trend_score": "Massive Physics Curiosity Spike (Evergreen)",
                "angle": "mechanisms_and_systems",
                "slug": "how_sailboats_sail_faster_than_wind_viral_physics",
                "why_trending": "The counter-intuitive reality that modern boats generate their own apparent wind to sail at 50 knots in a 15-knot breeze blows minds.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Why Orcas Are Attacking Sailboats in the Strait of Gibraltar (The Real Reason)",
                "trend_score": "Massive Global News & Marine Mystery Spike",
                "angle": "field_investigation",
                "slug": "orca_rudder_attacks_gibraltar_why_explained",
                "why_trending": "Videos of killer whales ramming yachts and biting off rudders until boats sink have dominated news feeds worldwide.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The Vendée Globe: The Race Where Sailors Spend 80 Days Alone in Iceberg Seas",
                "trend_score": "High Extreme Endurance Adventure Hook",
                "angle": "famous_examples",
                "slug": "vendee_globe_everest_of_the_seas_viral_documentary",
                "why_trending": "Documentaries showing solo sailors in 60-foot foiling yachts flying off giant waves in the Southern Ocean pull millions of viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Heaving-To: The 200-Year-Old Trick That Parks a Sailboat in a 50-Knot Storm",
                "trend_score": "High Life-Saving Seamanship Hook",
                "angle": "practical_playbook",
                "slug": "heaving_to_storm_tactic_sailors_secret",
                "why_trending": "Watching a chaotic, tossing boat instantly settle into gentle, peaceful calm by backwinding the jib looks like magic.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "America's Cup AC75: The 55-Knot Flying Boats That Look Like Alien Spaceships",
                "trend_score": "High Sci-Fi Tech & Yachting Volume",
                "angle": "case_study",
                "slug": "americas_cup_ac75_hydrofoils_cyclors_breakdown",
                "why_trending": "The sight of 75-foot yachts completely flying on tiny foils with cyclist athletes grinding hydraulic pressure mesmerizes sports fans.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "The Madness of Donald Crowhurst: The Sailor Who Faked Sailing Around the World",
                "trend_score": "High Tragic Psychological Mystery Spike",
                "angle": "deep_dive",
                "slug": "donald_crowhurst_golden_globe_race_fake_tragedy",
                "why_trending": "The tragic true story of the amateur sailor sending fake coordinates while drifting in circles until losing his mind inspired books and movies.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Why You Should Never Buy a Boat with 'Osmosis': The Fiberglass Cancer",
                "trend_score": "High Practical Yacht Maintenance & Warning Spike",
                "angle": "failure_mode_analysis",
                "slug": "boat_hull_osmosis_gelcoat_blisters_scandal",
                "why_trending": "Marine surveyors popping acid blisters on fiberglass boat hulls and showing soft rotting resin saves buyers hundreds of thousands.",
                "status": "READY FOR COMPILATION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 131-135...")
    for folder, meta in BATCH_136_140.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 136-140 complete!")

if __name__ == "__main__":
    main()
