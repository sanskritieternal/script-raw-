"""
Batch Generator for Niches 091 to 095:
- 091_cooking_culinary
- 092_beverage_culture
- 093_agriculture_farming
- 094_rural_life_village_culture
- 095_handicrafts_traditional_skills
"""

import sys
from pathlib import Path

# Add Scripts to sys.path
sys.path.append(str(Path(__file__).parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_091_095 = {
    "091_cooking_culinary": {
        "id": "091",
        "slug": "cooking_culinary",
        "title": "Cooking & Culinary",
        "category": "Food_Fashion",
        "audience": "Home Cooks, Food Science Geeks, Culinary Students, Professional Chefs, Gastronomy Lovers (Global)",
        "progression": [
            ("Tier 1: Heat Transfer, Knife Skills & The Samin Nosrat Quartet (Scratch / Beginner)",
             "Salt, Fat, Acid, Heat foundations, conduction/convection/radiation, pinch grip knife mechanics, Maillard reaction browning vs. caramelization, and basic mother sauces."),
            ("Tier 2: Emulsions, Gluten Networks & Fermentation Science (Intermediate)",
             "Mayonnaise and hollandaise lecithin emulsions, sourdough wild yeast hydration and gluten development, lacto-fermentation pickles, and pan sauces and deglazing fond."),
            ("Tier 3: Regional Flavor Matrices, Wok Hei & Low-and-Slow Barbecue (Upper Intermediate)",
             "Cantonese wok hei thermal Leidenfrost aerosolization, authentic Texas brisket collagen-to-gelatin stalls, Indian tadka spice oil blooming, and French classical braising."),
            ("Tier 4: Molecular Gastronomy, Umami Layering & Modernist Kitchen Labs (Advanced / Expert)",
             "Sous-vide precision temperature baths, spherification with sodium alginate, meat glue (transglutaminase), deep umami nucleotide synergies, and Michelin-star menu engineering.")
        ],
        "flagship": {
            "title": "The Science of Searing: Why the Maillard Reaction Makes Meat Delicious",
            "angle": "culinary_chemistry",
            "slug": "091_cooking_culinary_culinary_chemistry_maillard_reaction_meat_searing"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Science of Searing: Why the Maillard Reaction Makes Meat Delicious",
                "tier": "Tier 1: Heat Transfer, Knife Skills & Foundations",
                "angle": "culinary_chemistry",
                "slug": "maillard_reaction_meat_searing_amino_acids_reducing_sugars_cast_iron",
                "question": "Why does high-heat crust formation produce hundreds of brand-new savory flavor molecules that raw or boiled meat can never produce?",
                "key_focus": "Louis-Camille Maillard's 1912 reaction, amino acids reacting with reducing sugars between 140°C and 165°C, why surface moisture is the enemy of searing (steam cooling), patting dry with paper towels, and the thermal mass of cast iron pans.",
                "reason": "Flagship launch episode; the bedrock chemical transformation that governs delicious cooking across all global cuisines."
            },
            {
                "id": 2,
                "title": "Salt, Fat, Acid, Heat: How Four Elements Govern Every Delicious Dish on Earth",
                "tier": "Tier 1: Heat Transfer, Knife Skills & Foundations",
                "angle": "culinary_frameworks",
                "slug": "salt_fat_acid_heat_samin_nosrat_flavor_balance_osmosis_palate_reset",
                "question": "How does salting meat 24 hours in advance alter muscle proteins via osmosis, and why does a squeeze of lemon cut through heavy animal fats?",
                "key_focus": "Samin Nosrat's four-part cooking philosophy, kosher salt vs. table salt density, fat as a flavor delivery vehicle and heat transfer medium, acid brightening dullness and salivation, and heat vectors.",
                "reason": "The defining modern culinary framework that transforms amateur recipe followers into intuitive master cooks."
            },
            {
                "id": 3,
                "title": "Knife Skills 101: The Pinch Grip, The Claw, and Why Sharp Knives Never Slip",
                "tier": "Tier 1: Heat Transfer, Knife Skills & Foundations",
                "angle": "knife_mechanics",
                "slug": "knife_skills_pinch_grip_the_claw_julienne_brunoise_onion_dicing",
                "question": "Why do professional chefs hold the blade itself rather than the wooden handle, and how do you dice an entire onion in 15 seconds without tears?",
                "key_focus": "Pinch grip blade control, 'The Claw' protecting guide hand knuckles, rock chopping vs. push cutting, classic French vegetable cuts (Julienne, Brunoise, Chiffonade), and why dull knives cause 90% of kitchen lacerations.",
                "reason": "The fundamental mechanical hand skill required before any cooking can begin."
            },
            {
                "id": 4,
                "title": "The Five French Mother Sauces: Béchamel, Velouté, Espagnole, Tomato, and Hollandaise",
                "tier": "Tier 1: Heat Transfer, Knife Skills & Foundations",
                "angle": "classical_foundations",
                "slug": "five_french_mother_sauces_escoffier_roux_thickening_hollandaise_emulsion",
                "question": "How did Auguste Escoffier organize thousands of restaurant sauces into five master formulas built from equal parts flour, butter, and stock?",
                "key_focus": "White, blond, and brown roux starch gelatinization, Béchamel (milk), Velouté (white stock), Espagnole (brown stock), classic tomato, Hollandaise warm egg-butter emulsion, and daughter sauce derivatives (Mornay, Béarnaise).",
                "reason": "The classical European foundation of restaurant cooking and sauce architecture."
            },
            {
                "id": 5,
                "title": "The Three Heat Transfer Vectors: Conduction, Convection, and Radiant Heat in the Kitchen",
                "tier": "Tier 1: Heat Transfer, Knife Skills & Foundations",
                "angle": "thermal_physics",
                "slug": "heat_transfer_in_cooking_conduction_convection_radiation_cast_iron_air_fryer",
                "question": "Why does a metal pan sear a steak via conduction, while an oven bakes via convection and a charcoal grill roasts via infrared radiation?",
                "key_focus": "Direct molecular collision in conduction, thermal fluid currents in convection ovens, electromagnetic infrared photons in broiling and coals, and matching heat vectors to specific meats and vegetables.",
                "reason": "Teaches home cooks to stop thinking in terms of 'dial settings' and start thinking in terms of thermodynamic energy transfer."
            },
            {
                "id": 6,
                "title": "The Emulsion Miracle: How Egg Yolks Bind Oil and Vinegar in Mayonnaise and Hollandaise",
                "tier": "Tier 2: Emulsions, Gluten & Fermentation",
                "angle": "food_emulsions",
                "slug": "science_of_emulsions_mayonnaise_lecithin_oil_droplets_broken_sauce_fix",
                "question": "How can a single egg yolk suspend two whole cups of oil into a thick, creamy white mayonnaise without separating back into oil and water?",
                "key_focus": "Lecithin phospholipid molecules (hydrophilic heads and lipophilic tails), mechanical shearing breaking oil into microscopic 1-micron droplets, phase inversion limits, and the rescue trick for fixing broken sauces with a tablespoon of warm water.",
                "reason": "Demystifies the kitchen chemistry behind dressings, aiolis, and delicate French butter emulsions."
            },
            {
                "id": 7,
                "title": "Sourdough Bread Science: Wild Yeast, Lactic Acid Bacteria, and Gluten Mesh Hydration",
                "tier": "Tier 2: Emulsions, Gluten & Fermentation",
                "angle": "baking_chemistry",
                "slug": "sourdough_science_starter_lactobacillus_gluten_network_bakers_percentages_steam",
                "question": "How do wild yeast spores and friendly bacteria captured from kitchen air digest flour starch to blow bubbles through stretchy gluten walls?",
                "key_focus": "Symbiosis between Candida humilis wild yeast and Lactobacillus sanfranciscensis bacteria, baker's percentages (hydration levels), autolyse resting, glutenin and gliadin cross-linking, and Dutch oven steam creating blistering crackly crusts.",
                "reason": "The definitive artisan bread tutorial combining microbiology, gluten mechanics, and baking physics."
            },
            {
                "id": 8,
                "title": "The Chemistry of Fond: Deglazing Pan Brownings into World-Class Pan Sauces",
                "tier": "Tier 2: Emulsions, Gluten & Fermentation",
                "angle": "pan_sauces",
                "slug": "deglazing_pan_fond_wine_reduction_cold_butter_monter_au_beurre_gloss",
                "question": "Why is the stuck brown glaze on the bottom of a stainless steel pan pure liquid gold, and how does cold butter create a restaurant-gloss sauce?",
                "key_focus": "Maillard brownings forming fond, dissolving concentrated flavors with acidic liquids (wine, vinegar, stock), alcohol solubility of aromatic compounds, reducing liquid, and mounting with cold butter (monter au beurre) without breaking the emulsion.",
                "reason": "The single fastest technique that turns a home-cooked dinner into a 5-star restaurant meal in 3 minutes."
            },
            {
                "id": 9,
                "title": "Lacto-Fermentation: How Salt and Lactic Acid Bacteria Preserve Pickles, Kimchi, and Kraut",
                "tier": "Tier 2: Emulsions, Gluten & Fermentation",
                "angle": "fermentation_science",
                "slug": "lacto_fermentation_sauerkraut_kimchi_salinity_percentage_anaerobic_ph",
                "question": "How does submerged cabbage in a 2% salt brine kill dangerous rot bacteria while letting beneficial lactic acid bacteria turn it tangy and crisp?",
                "key_focus": "Halotolerant Leuconostoc mesenteroides and Lactobacillus plantarum, converting glucose into lactic acid, dropping pH below 4.6 for botulism defense, anaerobic submerged glass weights, and probiotic gut microbiome benefits.",
                "reason": "Unlocks the ancient, global culinary art of vegetable preservation without heat, cans, or vinegar."
            },
            {
                "id": 10,
                "title": "Pasta Water Gold: Why Starch and Fat Create Cacio e Pepe Without Clumping",
                "tier": "Tier 2: Emulsions, Gluten & Fermentation",
                "angle": "pasta_emulsions",
                "slug": "cacio_e_pepe_science_pasta_water_starch_pecorino_cheese_emulsion_no_clumps",
                "question": "Why does melted Pecorino cheese turn into rubbery chewy clumps in pasta unless you whip it with cloudy, salty boiling pasta water?",
                "key_focus": "Amylose and amylopectin starch granules leaching into boiling water, acting as colloidal emulsifiers preventing cheese fats and milk proteins from separating, pan agitation kinetics, and maintaining sauce temperature below 65°C.",
                "reason": "Deconstructs the most notoriously difficult and elegant 3-ingredient Roman pasta dish in the world."
            },
            {
                "id": 11,
                "title": "Wok Hei: The Breath of the Wok, Leidenfrost Aerosols, and 1,000°F Jet Burners",
                "tier": "Tier 3: Regional Matrices & Live Fire",
                "angle": "high_heat_mechanics",
                "slug": "wok_hei_breath_of_the_wok_cantonese_stir_fry_leidenfrost_oil_droplet_vapor",
                "question": "Why can you never recreate true restaurant Chinese stir-fry at home on a standard electric stove? The physics of Wok Hei.",
                "key_focus": "100,000 BTU jet flame burners, thin carbon steel wok conductivity, the Leidenfrost effect preventing food from burning, parabolic tossing atomizing oil droplets into open flame for smoky combustion vapor, and rapid moisture evaporation.",
                "reason": "Explores the supreme Cantonese culinary technique combining thermal speed, flame aerosolization, and metallurgy."
            },
            {
                "id": 12,
                "title": "Texas Barbecue: The 12-Hour Chemistry of Collagen, Smoke Rings, and The Stall",
                "tier": "Tier 3: Regional Matrices & Live Fire",
                "angle": "wood_smoke_science",
                "slug": "texas_brisket_barbecue_collagen_gelatin_evaporative_cooling_stall_smoke_ring",
                "question": "Why does a beef brisket get stuck at 160°F for four agonizing hours without rising in temperature, and how does tough connective tissue turn into tender jelly?",
                "key_focus": "Evaporative cooling causing the famous 'stall', butcher paper crutch wrapping, collagen denaturation into melting gelatin between 160°F and 180°F, nitric oxide smoke rings binding to myoglobin, and lignin wood smoke aromatics (guaiacol).",
                "reason": "The ultimate scientific breakdown of authentic low-and-slow wood pit smoking."
            },
            {
                "id": 13,
                "title": "The Indian Tadka: Fat-Soluble Spices and The Rapid Chemistry of Blooming in Oil",
                "tier": "Tier 3: Regional Matrices & Live Fire",
                "angle": "spice_chemistry",
                "slug": "indian_tadka_tempering_spices_fat_soluble_flavor_compounds_mustard_cumin",
                "question": "Why do Indian chefs sizzle whole cumin seeds, mustard seeds, and dried chilies in hot ghee for 15 seconds before pouring it over lentils?",
                "key_focus": "Fat-soluble volatile organic compounds (cuminaldehyde, allyl isothiocyanate) requiring hot lipids to dissolve, popping seeds rupturing cell walls, pyrolyzing harsh raw flavors into sweet nutty notes, and layering aromatic finish.",
                "reason": "Unlocks the ancient South Asian flavor delivery engine that powers the world's most complex curries and dals."
            },
            {
                "id": 14,
                "title": "French Braising: How Low Simmering Melts Tough Muscle Cuts into Spoon-Tender Stews",
                "tier": "Tier 3: Regional Matrices & Live Fire",
                "angle": "slow_cooking_science",
                "slug": "french_braising_beef_bourguignon_collagen_denaturation_cartilage_reduction",
                "question": "Why does boiling a cheap beef shank for 20 minutes make it tough as leather, while braising it at 200°F for 3 hours lets you cut it with a butter spoon?",
                "key_focus": "Muscle fibers (actin and myosin) contracting and expelling water vs. perimysium and endomysium collagen connective sheaths unraveling into gelatin, braising liquid reduction creating rich mouthfeel, and resting stews overnight.",
                "reason": "The quintessential home comfort technique that turns inexpensive cuts of meat into culinary luxury."
            },
            {
                "id": 15,
                "title": "The Art of Sushi Rice: Shari Vinegar Chemistry, Polishing, and Body Temperature Serving",
                "tier": "Tier 3: Regional Matrices & Live Fire",
                "angle": "traditional_gastronomy",
                "slug": "sushi_rice_shari_chemistry_japonica_amylose_red_vinegar_akasu_temperature",
                "question": "Why does a legendary Tokyo sushi master train apprentices for 5 years just to cook and fan rice with wooden hangiri tubs?",
                "key_focus": "Short-grain Japonica rice starch ratio (low amylose, high amylopectin), washing surface starch without fracturing grains, Akasu aged sake lees red vinegar seasoning, cutting and fanning to create glossy single-grain separation, and serving at human body temperature (36°C).",
                "reason": "Reveals the obsessive micro-craftsmanship and chemistry behind the true foundation of authentic Edomae sushi."
            },
            {
                "id": 16,
                "title": "Sous-Vide: The Precision Physics of Cooking Meat to the Exact Degree",
                "tier": "Tier 4: Molecular Gastronomy & Modernist Labs",
                "angle": "modernist_techniques",
                "slug": "sous_vide_cooking_immersion_circulator_myoglobin_protein_coagulation_137_steak",
                "question": "Why does cooking a ribeye vacuum-sealed in a 137°F water bath melt intramuscular fat while keeping the entire interior edge-to-edge medium-rare?",
                "key_focus": "Water thermal immersion circulators, protein coagulation temperatures (myosin at 50°C, actin at 66°C), pasteurization time-temperature curves (Dr. Douglas Baldwin), rendering fat without overcooking surrounding meat, and torch/sear finishes.",
                "reason": "The modernist laboratory technique that conquered high-end restaurant kitchens and home cooking."
            },
            {
                "id": 17,
                "title": "Molecular Gastronomy: Spherification, Sodium Alginate, and Liquid Olives",
                "tier": "Tier 4: Molecular Gastronomy & Modernist Labs",
                "angle": "food_hydrocolloids",
                "slug": "molecular_gastronomy_spherification_ferran_adria_el_bulli_sodium_alginate",
                "question": "How did Ferran Adrià at El Bulli create liquid pea ravioli and fruit caviar that burst in your mouth using brown seaweed extracts and calcium baths?",
                "key_focus": "Direct vs. reverse spherification, sodium alginate polymer chains cross-linking in the presence of calcium ions (calcium lactate gluconate) to form an ultra-thin edible gelatinous membrane, pH sensitivity, and hydrocolloid texture design.",
                "reason": "Celebrates the avant-garde Spanish culinary movement that dissolved the boundary between kitchen and chemistry lab."
            },
            {
                "id": 18,
                "title": "Umami Synergy: The Nucleotide Equation That Multiplies Savory Taste by Eight",
                "tier": "Tier 4: Molecular Gastronomy & Modernist Labs",
                "angle": "taste_neurobiology",
                "slug": "umami_synergy_glutamate_plus_inosinate_guanylate_dashi_parmesan_multiplier",
                "question": "Why does combining kombu kelp and bonito fish flakes in Japanese dashi taste eight times more savory than either ingredient on its own?",
                "key_focus": "Kikunae Ikeda's 1908 discovery of monosodium glutamate (MSG), the T1R1/T1R3 taste bud receptor, nucleotide synergy where purine nucleotides (IMP inosinate and GMP guanylate) lock glutamate into the receptor, and Western pairings (beef and mushrooms, tomato and parmesan).",
                "reason": "The molecular holy grail of deep deliciousness used by food scientists and Michelin chefs to engineer irresistible flavor."
            },
            {
                "id": 19,
                "title": "Meat Glue (Transglutaminase): The Invisible Enzyme Binding Steaks and Restructuring Proteins",
                "tier": "Tier 4: Molecular Gastronomy & Modernist Labs",
                "angle": "enzymatic_cooking",
                "slug": "meat_glue_transglutaminase_activa_cross_linking_proteins_culinary_uses",
                "question": "How do professional chefs bond two completely separate pieces of fish or beef together into a seamless cylinder that survives boiling without falling apart?",
                "key_focus": "Microbial transglutaminase enzyme catalyzing covalent bonds between glutamine and lysine amino acid side chains, culinary uses in roulades, shrimp noodles, and bacon-wrapped tenderloins, and safety standards vs. commercial deception.",
                "reason": "Demystifies the controversial, fascinating modernist enzyme used in elite restaurant kitchens."
            },
            {
                "id": 20,
                "title": "The Anatomy of a Michelin-Star Menu: Flavor Memory, Storytelling, and Multi-Sensory Design",
                "tier": "Tier 4: Molecular Gastronomy & Modernist Labs",
                "angle": "fine_dining_architecture",
                "slug": "anatomy_of_michelin_star_menu_the_french_laundry_noma_multi_sensory",
                "question": "How do restaurants like The French Laundry and Noma orchestrate 20-course tasting menus using sensory contrast, acoustic pairing, and psychological pacing?",
                "key_focus": "Thomas Keller's 'Law of Diminishing Returns' (small portions peaking flavor pleasure), pacing acid and rich fats, temperature surprises, tableware textures, culinary narrative arcs, and kitchen brigade hierarchy.",
                "reason": "Capstones the master curriculum with the ultimate artistic and operational synthesis of world-class fine dining."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The MSG Myth Debunked: The Racist Hoax That Fooled the World for 50 Years",
                "tier": "Trending / High Retention",
                "angle": "food_myth_busting",
                "slug": "msg_myth_chinese_restaurant_syndrome_racist_hoax_glutamate_science",
                "trend_score": 98,
                "why_trending": "Massive viral video essays exposing the 1968 fake medical letter that coined 'Chinese Restaurant Syndrome' and showing MSG naturally occurs in parmesan and tomatoes.",
                "reason": "Incredible social-conflict hook that combines food science, racial bias history, and delicious kitchen seasoning hacks.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why You Should Never Wash Raw Chicken: The Cross-Contamination Bacteria Blast",
                "tier": "Trending / High Retention",
                "angle": "kitchen_safety_warnings",
                "slug": "never_wash_raw_chicken_campylobacter_salmonella_water_spray_contamination",
                "trend_score": 97,
                "why_trending": "Fierce perennial online debate between cultural washing traditions and USDA food safety videos showing invisible fluorescent bacterial mist spraying 3 feet across counters.",
                "reason": "High-conflict, eye-opening hygiene science that saves viewers from salmonella and campylobacter food poisoning.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The Cast Iron Soap Lie: Why You CAN Wash Your Skillet with Dawn Dish Soap Today",
                "tier": "Trending / High Retention",
                "angle": "kitchen_folklore",
                "slug": "washing_cast_iron_with_soap_myth_lye_vs_modern_detergent_polymerized_oil",
                "trend_score": 96,
                "why_trending": "Satisfying debunking of old wives' tales explaining that grandfather's warning was about harsh caustic lye soap—while modern dish detergents won't touch polymerized oil seasoning.",
                "reason": "Empowers home cooks and settles decades of heated Reddit and YouTube cast-iron maintenance arguments.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Why Gordon Ramsay's Scrambled Eggs Go Viral: The On-and-Off Heat Method Explained",
                "tier": "Trending / High Retention",
                "angle": "celebrity_chef_science",
                "slug": "gordon_ramsay_scrambled_eggs_cold_pot_on_and_off_heat_creme_fraiche",
                "trend_score": 98,
                "why_trending": "Gordon Ramsay's classic scrambled egg tutorial remains one of the most-watched cooking clips in YouTube history with over 50 million views.",
                "reason": "Deconstructs the exact protein curd coagulation physics: keeping eggs below 80°C to prevent weeping water and rubbery rubber texture.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Reverse Searing: Why Cooking Steaks Backwards Destroys the Traditional Method",
                "tier": "Trending / High Retention",
                "angle": "cooking_breakthroughs",
                "slug": "reverse_sear_steak_j_kenji_lopez_alt_low_oven_searing_gray_band",
                "trend_score": 97,
                "why_trending": "Popularized by J. Kenji López-Alt, baking thick steaks in a low 225°F oven first dries the surface and yields edge-to-edge pink without the dreaded gray overcooked ring.",
                "reason": "High-utility culinary breakthrough that guarantees restaurant-quality thick ribeyes and steaks every time.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Truffle Oil Scam: Why 95% of Luxury Truffle Fries Contain Zero Real Truffles",
                "tier": "Trending / High Retention",
                "angle": "restaurant_industry_scams",
                "slug": "truffle_oil_scam_2_4_dithiapentane_synthetic_petroleum_derivative_restaurants",
                "trend_score": 96,
                "why_trending": "Exposé showing high-end restaurants charging $20 extra for truffle fries flavored with cheap olive oil spiked with 2,4-dithiapentane derived from petroleum.",
                "reason": "Eye-opening consumer warning tearing down pretentious restaurant upcharges with chemical facts.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Wooden Cutting Boards Are More Sanitary Than Plastic: The Antimicrobial Grain",
                "tier": "Trending / High Retention",
                "angle": "kitchen_science_myths",
                "slug": "wooden_vs_plastic_cutting_boards_dr_cliver_study_capillary_antimicrobial",
                "trend_score": 95,
                "why_trending": "Dr. Dean Cliver's famous UC Davis study proving wood pores suck bacteria deep inside where they desiccate and die, while knife grooves in plastic harbor active salmonella.",
                "reason": "Fascinating natural material science that flips common health inspector assumptions on their head.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "092_beverage_culture": {
        "id": "092",
        "slug": "beverage_culture",
        "title": "Beverage Culture",
        "category": "Food_Fashion",
        "audience": "Coffee Geeks, Tea Connoisseurs, Mixologists, Sommelier Students, Drink Enthusiasts (Global)",
        "progression": [
            ("Tier 1: Brewing Extraction, Water Chemistry & Foundational Tastings (Scratch / Beginner)",
             "Coffee grind size and TDS extraction yields, tea oxidation levels (green to black), water mineral hardness (calcium/magnesium ratios), and basic barware balance."),
            ("Tier 2: Terroir, Fermentation & Regional Botanical Traditions (Intermediate)",
             "Specialty coffee bean processing (washed vs. natural vs. anaerobic), single-estate teas (Darjeeling, Matcha, Oolong), wine terroir and fermentation yeasts, and craft beer hop chemistry (alpha acids)."),
            ("Tier 3: Distillation Chemistry, Barrel Aging & Mixology Ratios (Upper Intermediate)",
             "Copper pot vs. continuous column stills, barrel char oak lactones and vanillin extraction, classic cocktail golden ratios (Sour, Old Fashioned, Negroni), and clarified milk punches."),
            ("Tier 4: Sommelier Mastery, Rare Vintages & The Future of Alcohol-Free Spirits (Advanced / Expert)",
             "Blind tasting grids (Court of Master Sommeliers), Grand Cru Burgundy investment economics, non-alcoholic vacuum distillation botanical spirits, and modern cold-brew flash-chilling technology.")
        ],
        "flagship": {
            "title": "Espresso Science: Extraction Yield, Grind Distribution, and The 9-Bar Pressure Standard",
            "angle": "beverage_extraction_science",
            "slug": "092_beverage_culture_beverage_extraction_science_espresso_9_bar"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Espresso Science: Extraction Yield, Grind Distribution, and The 9-Bar Pressure Standard",
                "tier": "Tier 1: Brewing Extraction & Water Chemistry",
                "angle": "beverage_extraction_science",
                "slug": "espresso_science_9_bar_pressure_extraction_yield_channelling_crema_physics",
                "question": "Why does pushing 93°C water through a compacted coffee puck at 9 atmospheres of pressure extract rich golden crema in 28 seconds while 10 bars causes channeling?",
                "key_focus": "Ernesto Valente's 1961 Faema E61 rotary pump standard, Total Dissolved Solids (TDS) refractometry, optimal 18–22% extraction yield, bimodal grinder particle distribution, channeling voids, and carbon dioxide emulsion crema.",
                "reason": "Flagship launch episode; the ultimate masterclass in precision hydraulic extraction and specialty coffee science."
            },
            {
                "id": 2,
                "title": "The Chemistry of Coffee Water: How Calcium, Magnesium, and Bicarbonate Dictate Flavor",
                "tier": "Tier 1: Brewing Extraction & Water Chemistry",
                "angle": "water_mineralogy",
                "slug": "coffee_water_chemistry_james_hoffmann_calcium_magnesium_bicarbonate_buffer",
                "question": "Why does the exact same expensive specialty coffee bean taste bright and fruity in London but flat, bitter, and muddy in New York?",
                "key_focus": "Christopher Hendon and Maxwell Colonna-Dashwood's 'Water for Coffee' research, magnesium extracting oxygen-rich fruit flavors, calcium extracting heavy body, bicarbonate alkalinity buffer neutralizing acidity, and DIY mineral water recipes (Lotus drops).",
                "reason": "Unlocks the invisible 98.5% of the cup that determines whether great coffee beans taste transcendent or terrible."
            },
            {
                "id": 3,
                "title": "The Six Types of Tea: How One Single Camellia Sinensis Leaf Makes Green, Black, and Oolong",
                "tier": "Tier 1: Brewing Extraction & Water Chemistry",
                "angle": "tea_processing",
                "slug": "tea_processing_camellia_sinensis_polyphenol_oxidase_green_white_oolong_black_puerh",
                "question": "How can green, yellow, white, oolong, black, and fermented pu-erh teas come from the exact same plant species?",
                "key_focus": "Polyphenol oxidase enzymatic oxidation, Sha Qing (kill-green heating) halting oxidation in green tea, bruising leaf edges in oolong, full enzymatic darkening in black tea, microbial post-fermentation in Pu-erh caves, and L-theanine caffeine synergy.",
                "reason": "The foundational botanical and processing guide to the world's most consumed beverage after water."
            },
            {
                "id": 4,
                "title": "Pour-Over Coffee Physics: Particle Size, Flow Rate, and The V60 Vortex",
                "tier": "Tier 1: Brewing Extraction & Water Chemistry",
                "angle": "filter_brewing",
                "slug": "v60_pourover_physics_percolation_darcy_law_bypass_water_agitation",
                "question": "Why do the 60-degree cone angle and spiral ribs of the Hario V60 allow air to escape while controlling water drawdown according to Darcy's Law?",
                "key_focus": "Percolation vs. immersion brewing, Darcy's law of fluid flow through porous media, fines migration clogging filter paper pores, the blooming degas phase (CO2 release), and swirling agitation.",
                "reason": "Teaches the fluid dynamics behind the favorite manual brewing tool of coffee geeks worldwide."
            },
            {
                "id": 5,
                "title": "The Golden Ratio of Cocktails: The 2:1:1 Rule That Powers Margaritas, Sours, and Daiquiris",
                "tier": "Tier 1: Brewing Extraction & Water Chemistry",
                "angle": "mixology_ratios",
                "slug": "cocktail_golden_ratio_sour_formula_two_parts_spirit_one_sweet_one_sour",
                "question": "Why does almost every legendary shaken cocktail on earth share the identical mathematical formula: 2 parts spirit, 1 part sour, 1 part sweet?",
                "key_focus": "David Embury's 'Fine Art of Mixing Drinks' classification, balancing citric/malic acids against simple syrup brix sweetness, shaking dilution delivering 25% melted ice water, chill aeration, and wash lines.",
                "reason": "The master formula that liberates home bartenders from memorizing hundreds of separate cocktail recipes."
            },
            {
                "id": 6,
                "title": "Coffee Processing: Washed vs. Natural vs. Anaerobic Fermentation Fruit Bombs",
                "tier": "Tier 2: Terroir, Fermentation & Regional Brews",
                "angle": "coffee_agronomy",
                "slug": "coffee_processing_washed_vs_natural_anaerobic_maceration_yeast_esters",
                "question": "How does leaving the coffee cherry skin on while drying in the sun create wild strawberry and blueberry flavors without adding a single drop of flavoring?",
                "key_focus": "Washed processing (depulping and water tank fermentation for clean terroir clarity) vs. Natural dry-process (sugars fermenting into the bean on raised African beds), anaerobic tank maceration, carbonic maceration, and thermal shock processing.",
                "reason": "Explores the agricultural frontier revolutionizing the global specialty coffee sensory landscape."
            },
            {
                "id": 7,
                "title": "Japanese Matcha: Shade Growing, Tencha Stone-Grinding, and The Chasen Whisking Foam",
                "tier": "Tier 2: Terroir, Fermentation & Regional Brews",
                "angle": "traditional_tea_ceremony",
                "slug": "matcha_production_shade_growing_chlorophyll_tencha_granite_mill_chasen_froth",
                "question": "Why do Japanese tea farmers cover green tea fields with black tarp canopies for 3 weeks before harvest, and why does a granite mill take 1 hour to grind 30g of powder?",
                "key_focus": "Shading boosting chlorophyll and umami-rich L-theanine while suppressing bitter catechins, de-stemming into Tencha flakes, slow granite stone-milling keeping flour cool, Chanoyu tea ceremony aesthetics, and the 100-prong bamboo Chasen whisk suspension.",
                "reason": "Dives into the refined, ancient Japanese aesthetic and pharmacological world of ceremonial green tea."
            },
            {
                "id": 8,
                "title": "Wine Terroir Demystified: Soil Chemistry, Microclimates, and The Old World vs. New World War",
                "tier": "Tier 2: Terroir, Fermentation & Regional Brews",
                "angle": "viticulture_science",
                "slug": "wine_terroir_soil_drainage_limestone_diurnal_temperature_old_vs_new_world",
                "question": "Can you actually 'taste the limestone' in a Chablis wine, or is terroir an intricate combination of diurnal temperature swings, vine stress, and wild indigenous yeast?",
                "key_focus": "The physical reality of terroir (soil drainage, root depth, diurnal temperature fluctuation preserving grape malic acidity), French AOC classification vs. New World grape varietal labeling, and the Judgement of Paris blind tasting that shocked France.",
                "reason": "Separates romantic wine marketing myths from real viticultural science and climate realities."
            },
            {
                "id": 9,
                "title": "Craft Beer Hop Chemistry: Alpha Acids, Dry Hopping, and The Hazy IPA Juice Phenomenon",
                "tier": "Tier 2: Terroir, Fermentation & Regional Brews",
                "angle": "brewing_biochemistry",
                "slug": "beer_hop_chemistry_humulone_alpha_acids_isomerization_dry_hopping_terpenes",
                "question": "How does boiling green hop cones isomerize alpha acids into mouth-drying bitterness, while adding hops cold into fermentation tanks releases explosions of mango and passionfruit juice?",
                "key_focus": "Humulone alpha acid thermal isomerization into iso-alpha acids (IBU measurement), volatile essential hop oils (myrcene, linalool, humulene), dry-hopping biotransformation with New England IPA London Ale III yeasts, and oat/wheat protein haze.",
                "reason": "Deconstructs the chemical revolution that transformed modern craft beer from bitter IPAs into juicy hazy fruit bombs."
            },
            {
                "id": 10,
                "title": "The Magic of Kombucha: Inside the SCOBY Symbiotic Fermentation Biofilm",
                "tier": "Tier 2: Terroir, Fermentation & Regional Brews",
                "angle": "fermentation_microbiology",
                "slug": "kombucha_scoby_symbiosis_gluconacetobacter_cellulose_pellicle_acetic_acid",
                "question": "What is the rubbery pancake floating on top of kombucha tea, and how do yeasts and bacteria negotiate an unwritten chemical treaty to brew fizzy, sour tea?",
                "key_focus": "Symbiotic Culture of Bacteria and Yeast (SCOBY), Gluconacetobacter xylinus weaving a bacterial cellulose pellicle shield, yeast fermenting sugar into ethanol, acetic acid bacteria immediately oxidizing ethanol into sour acetic and gluconic acid, and secondary carbonation bottling.",
                "reason": "A fascinating look at living microbial architecture that turns sweet tea into a global functional health beverage."
            },
            {
                "id": 11,
                "title": "Whiskey Distillation: Copper Pot Stills, Reflux Cuts, and The Chemistry of Charred White Oak",
                "tier": "Tier 3: Distillation, Barrels & Mixology",
                "angle": "distillation_science",
                "slug": "whiskey_distillation_copper_pot_stills_heads_hearts_tails_oak_barrel_char",
                "question": "Why must single malt Scotch be distilled in giant swan-necked copper pots, and how does 10 years inside a charred American oak barrel generate 70% of the whiskey's final flavor?",
                "key_focus": "Ethanol boiling point (78.3°C) vs. water, copper catalytic stripping of sulfur compounds, cut points separating toxic heads (methanol/acetone) from hearts and tails (fusel oils), Level 4 'Alligator' barrel char, thermal expansion pumping whiskey through wood capillaries, and lignin breaking down into vanillin.",
                "reason": "The quintessential masterclass in spirit distillation, fractionation cuts, and cooperage barrel aging."
            },
            {
                "id": 12,
                "title": "Gin and Botanicals: Vapor Infusion, The Carter-Head Still, and Juniper Terpenes",
                "tier": "Tier 3: Distillation, Barrels & Mixology",
                "angle": "botanical_distillation",
                "slug": "gin_botanical_distillation_carter_head_vapor_infusion_juniper_pinene",
                "question": "How did a lethal 18th-century London street poison ('Mother's Ruin') evolve into the world's most aromatic botanical spirit crafted with hanging copper baskets?",
                "key_focus": "Neutral grain alcohol redistillation, alpha-pinene in Juniperus communis berries, maceration vs. Carter-Head vapor infusion (gentle alcohol steam extracting delicate floral notes without boiling stewing), coriander, angelica root fixatives, and citrus peels.",
                "reason": "Chronicles the botanical chemistry and dramatic social history of the world's original flavored craft spirit."
            },
            {
                "id": 13,
                "title": "Clarified Milk Punch: The 300-Year-Old English Secret to Silky Clear Cocktails",
                "tier": "Tier 3: Distillation, Barrels & Mixology",
                "angle": "cocktail_science",
                "slug": "clarified_milk_punch_casein_curd_filtration_tannin_stripping_mouthfeel",
                "question": "Why did Benjamin Franklin and Queen Victoria drink glowing, crystal-clear whiskey punch made by curdling whole milk with lemon juice?",
                "key_focus": "Casein milk protein curdling in acidic cocktail wash, curd mesh acting as an ultra-fine natural depth filter, trapping bitter polyphenols and particulate matter, leaving whey proteins behind that impart an astonishing velvety silk mouthfeel and infinite shelf stability.",
                "reason": "One of the most viral and impressive modern cocktail lab techniques, steeped in 18th-century historical genius."
            },
            {
                "id": 14,
                "title": "The Physics of Ice in Cocktails: Directional Freezing, Surface Area, and Dilution Rates",
                "tier": "Tier 3: Distillation, Barrels & Mixology",
                "angle": "ice_thermodynamics",
                "slug": "crystal_clear_ice_directional_freezing_cooler_hack_surface_area_dilution",
                "question": "Why is cloudiness in freezer ice caused by trapped air bubbles and minerals, and why does a single 2-inch clear ice sphere dilute an Old Fashioned 3 times slower?",
                "key_focus": "Directional freezing physics in insulated picnic coolers (forcing air and dissolved gasses to the bottom), hand carving ice blocks, surface area-to-volume ratio (sphere having the minimum surface area for maximum thermal cooling), and preventing watery cocktail ruin.",
                "reason": "A high-utility home bartending masterclass that transforms clouded home drinks into luxury speakeasy presentations."
            },
            {
                "id": 15,
                "title": "Agave Spirits: Tequila vs. Mezcal, Volcanic Piña Roasting, and Wild Terroir",
                "tier": "Tier 3: Distillation, Barrels & Mixology",
                "angle": "traditional_spirits",
                "slug": "tequila_vs_mezcal_blue_weber_agave_underground_earthen_pit_roasting",
                "question": "Why does Blue Weber Agave take 8 years in Jalisco red volcanic soil to mature, and how does roasting wild agaves in underground rock pits give Mezcal its mystical campfire smoke?",
                "key_focus": "Jimador harvesting agave hearts (piñas), autoclave steam baking vs. conical earthen pit roasting with mesquite wood, inulin hydrolysis into fermentable fructose sugars, wild ambient yeast fermentation in open pine vats, and ancestral clay pot distillation.",
                "reason": "Celebrates the deep botanical heritage, geological terroir, and artisanal indigenous craft of Mexican agave distillation."
            },
            {
                "id": 16,
                "title": "The Court of Master Sommeliers Blind Tasting Grid: Deductive Sensory Analysis",
                "tier": "Tier 4: Sommelier Mastery & Future Beverages",
                "angle": "sensory_deduction",
                "slug": "master_sommelier_blind_tasting_grid_deductive_logic_sight_nose_palate",
                "question": "How can an elite master sommelier sniff a dark glass of wine for 30 seconds and accurately identify the exact grape varietal, European river valley, and vintage year?",
                "key_focus": "The Deductive Tasting Method: Sight (color rim variation, tears/viscosity), Nose (fruit condition, non-fruit botanicals, oak barrel cues, minerality), Palate (sweetness, acid levels, tannin astringency, alcohol warmth), and systematic elimination of candidate grapes.",
                "reason": "The legendary intellectual pinnacle of sensory tasting discipline featured in documentaries like 'SOMM'."
            },
            {
                "id": 17,
                "title": "Grand Cru Burgundy Economics: How 2 Hectares of Soil Produce $25,000 Bottles",
                "tier": "Tier 4: Sommelier Mastery & Future Beverages",
                "angle": "luxury_beverage_economics",
                "slug": "burgundy_wine_economics_domaine_de_la_romanee_conti_grand_cru_scarcity",
                "question": "Why does a single bottle of Domaine de la Romanée-Conti cost as much as a new car, and how did medieval Cistercian monks map France's most expensive vineyard dirt?",
                "key_focus": "Côte d'Or limestone micro-climates, Romanée-Conti's tiny 1.8-hectare monopole footprint yielding only 5,000 bottles annually, Napoleonic inheritance laws fragmenting family plots, auction house investment funds, and counterfeiting scandals (Rudy Kurniawan).",
                "reason": "An exclusive inside look at the most expensive agricultural real estate and luxury liquid asset class on Earth."
            },
            {
                "id": 18,
                "title": "The Science of Alcohol-Free Spirits: Reverse Osmosis, Spinning Cones, and Botanicals",
                "tier": "Tier 4: Sommelier Mastery & Future Beverages",
                "angle": "modern_beverage_tech",
                "slug": "non_alcoholic_spirits_spinning_cone_columns_vacuum_distillation_capsaicin_burn",
                "question": "How do modern food scientists distill genuine botanical spirits, strip out the ethanol, and duplicate the natural 'throat burn' of high-proof whiskey without alcohol?",
                "key_focus": "Vacuum low-temperature distillation preserving fragile aromatics, spinning cone vacuum distillation stripping ethanol at room temperature, using capsaicin, gingerols, and Sichuan peppercorn to replicate ethanol trigeminal burn, and the $10B sober-curious market shift.",
                "reason": "Explores the fastest growing technological frontier in the global beverage industry."
            },
            {
                "id": 19,
                "title": "Cold Brew vs. Flash Chilling: Why Hot Water Extraction and Instant Ice Wins the Flavor War",
                "tier": "Tier 4: Sommelier Mastery & Future Beverages",
                "angle": "coffee_extraction_debates",
                "slug": "cold_brew_vs_flash_chilled_iced_coffee_volatile_aromatics_oxidation",
                "question": "Why does 24-hour steeping in cold water extract flat, heavy chocolate notes while flash-chilling piping-hot pour-over coffee directly over ice locks in delicate floral aromatics?",
                "key_focus": "Solubility curves (certain delicious coffee acids and floral aromatic compounds only dissolve above 90°C), atmospheric oxidation during long cold brewing, flash-freezing aroma molecules in direct contact with ice, and TDS flavor density comparison.",
                "reason": "High-conflict specialty coffee debate that permanently changes how viewers brew their summer iced coffee."
            },
            {
                "id": 20,
                "title": "The Future of Coffee: Global Warming, The Extinction of Arabica, and Liberica's Rise",
                "tier": "Tier 4: Sommelier Mastery & Future Beverages",
                "angle": "future_horizons",
                "slug": "future_of_coffee_arabica_extinction_global_warming_coffea_liberica_lab_grown",
                "question": "With 50% of global Arabica farming land projected to become unviable by 2050 due to rising heat and rust fungus, will humanity drink wild Liberica or bean-less lab coffee?",
                "key_focus": "Coffea arabica heat sensitivity, climate belt shifts, revival of Coffea liberica and Coffea stenophylla (climate-resilient wild species with Arabica flavor profiles), and cellular molecular coffee synthesis fermenting agricultural waste in bioreactors.",
                "reason": "Capstones the master curriculum with the urgent ecological reality and high-tech future of humanity's favorite stimulant."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The James Hoffmann French Press Hack: Why You Should Never Plunge Your Coffee",
                "tier": "Trending / High Retention",
                "angle": "viral_coffee_hacks",
                "slug": "james_hoffmann_french_press_hack_no_plunge_crust_break_clean_cup",
                "trend_score": 98,
                "why_trending": "James Hoffmann's legendary French Press video has over 12 million views, revolutionizing how millions make coffee by skimming foam and never pressing the plunger.",
                "reason": "Immediate high-utility viral life hack that transforms cheap gritty French press coffee into a clean, smooth brew.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why You Should Never Put Tequila in the Freezer: How Cold Erases $100 of Agave Flavor",
                "tier": "Trending / High Retention",
                "angle": "drinking_mistakes",
                "slug": "never_freeze_tequila_or_whiskey_numbing_taste_buds_suppressing_volatiles",
                "trend_score": 97,
                "why_trending": "Viral mixology clips explaining that freezing high-end spirits numbs tongue taste receptors and prevents volatile aromatic esters from evaporating into your nose.",
                "reason": "Eye-opening consumer lesson that saves people from ruining expensive bottles while explaining why cheap vodka loves the freezer.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The $1 Water Hack That Makes Cheap Supermarket Wine Taste Twice as Expensive",
                "tier": "Trending / High Retention",
                "angle": "wine_hacks",
                "slug": "hyperdecanting_wine_blender_hack_nathan_myhrvold_aeration_tannins",
                "trend_score": 96,
                "why_trending": "Nathan Myhrvold's 'hyper-decanting' hack putting $8 wine in a kitchen blender for 30 seconds to simulate 2 hours of decanting continues to trend across social media.",
                "reason": "Shocking, hilarious, and scientifically valid hack that softens harsh young tannins with rapid oxygen shearing.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Why Soda from McDonald's Actually Tastes Better Than Cans: The 5 Secret Standards",
                "tier": "Trending / High Retention",
                "angle": "food_industry_secrets",
                "slug": "why_mcdonalds_coke_tastes_better_stainless_steel_tanks_pre_chilled_syrup",
                "trend_score": 98,
                "why_trending": "Evergreen viral obsession over why McDonald's Coca-Cola hits differently: stainless steel syrup tanks (not plastic bags), pre-chilled syrup loops, and wider straws.",
                "reason": "Universal everyday mystery explained with verified franchise engineering contracts.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "How to Make Crystal Clear Cocktail Ice at Home with an Ordinary $10 Cooler",
                "tier": "Trending / High Retention",
                "angle": "satisfying_diy_drink",
                "slug": "how_to_make_clear_ice_cooler_hack_directional_freezing_serrated_knife",
                "trend_score": 97,
                "why_trending": "Enormously satisfying ASMR tutorials showing people cutting flawless, diamond-clear cocktail ice cubes out of cheap Igloo coolers with bread knives.",
                "reason": "Deep visual satisfaction with immediate real-world payoff for home entertaining.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Red Bull Energy Formula: Why Taurine, B-Vitamins, and 80mg of Caffeine Hit So Hard",
                "tier": "Trending / High Retention",
                "angle": "energy_drink_science",
                "slug": "red_bull_formula_taurine_caffeine_synergy_krating_daeng_thai_origins",
                "trend_score": 95,
                "why_trending": "Deep dives into Dietrich Mateschitz discovering Krating Daeng in Thailand and the neurological truth about whether taurine really gives you wings.",
                "reason": "Captivating mix of sports marketing genius, Thai trucking history, and neurochemical stimulants.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why You Can't Drink Sea Water: The Horrifying Cellular Biology of Osmotic Dehydration",
                "tier": "Trending / High Retention",
                "angle": "survival_biology",
                "slug": "why_you_cant_drink_seawater_kidney_filtration_osmotic_cellular_shrinkage",
                "trend_score": 96,
                "why_trending": "Terrifying survival science explaining that human kidneys can only produce urine with 2% salinity—meaning drinking 3.5% seawater literally drains water out of your brain cells.",
                "reason": "High-stakes biological drama showing how salt water accelerates death from thirst rather than quenching it.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "093_agriculture_farming": {
        "id": "093",
        "slug": "agriculture_farming",
        "title": "Agriculture & Farming",
        "category": "Land_Outdoor",
        "audience": "Farmers, Agronomists, Permaculture Enthusiasts, Food Security Researchers, Homesteaders (Global)",
        "progression": [
            ("Tier 1: Soil Biology, Seed Germination & The N-P-K Trinity (Scratch / Beginner)",
             "Soil textures (sand, silt, clay), the soil food web (fungi, bacteria, mycorrhizae), Nitrogen-Phosphorus-Potassium macronutrients, and germination moisture and photoperiods."),
            ("Tier 2: Crop Rotation, Irrigation Engineering & Pest Management (Intermediate)",
             "Legume nitrogen fixation, drip irrigation vs. flood systems, integrated pest management (beneficial insects vs. targeted pesticides), and cover cropping and green manure."),
            ("Tier 3: Regenerative Agriculture, No-Till Farming & Livestock Integration (Upper Intermediate)",
             "No-till soil carbon sequestration, Gabe Brown's 5 soil health principles, mob grazing rotational livestock, perennial polycultures, and agroforestry shelterbelts."),
            ("Tier 4: Precision Agritech, Controlled Environment Agriculture & Global Food Security (Advanced / Expert)",
             "Autonomous GPS tractor swaths, NDVI satellite crop vigor monitoring, indoor vertical aeroponics/hydroponics, gene-edited drought-resistant crops (CRISPR), and global fertilizer supply chains.")
        ],
        "flagship": {
            "title": "The Living Soil: How the Soil Food Web Feeds Crops Better Than Synthetic Fertilizer",
            "angle": "soil_biology",
            "slug": "093_agriculture_farming_soil_biology_soil_food_web_mycorrhizal_fungi"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Living Soil: How the Soil Food Web Feeds Crops Better Than Synthetic Fertilizer",
                "tier": "Tier 1: Soil Biology & Nutrient Fundamentals",
                "angle": "soil_biology",
                "slug": "soil_food_web_dr_elaine_ingham_mycorrhizal_fungi_rhizosphere_exudates",
                "question": "How do plant roots pump liquid carbon sugars into the soil to hire billions of fungal hyphae and bacteria that mine minerals in exchange?",
                "key_focus": "Dr. Elaine Ingham's soil food web, the rhizosphere, root exudates, arbuscular mycorrhizal fungi extending root surface area by 1,000%, protozoa and nematode nutrient cycling, and why synthetic NPK fertilizer severs this biological alliance.",
                "reason": "Flagship launch episode; unlocks the paradigm shift from treating soil as an inert chemical sponge to a living biological super-organism."
            },
            {
                "id": 2,
                "title": "The N-P-K Trinity: Nitrogen, Phosphorus, Potassium, and Soil Chemistry",
                "tier": "Tier 1: Soil Biology & Nutrient Fundamentals",
                "angle": "plant_nutrition",
                "slug": "npk_fertilizer_macronutrients_nitrogen_leaf_phosphorus_roots_potassium",
                "question": "What is happening inside plant cells when you apply Nitrogen for lush green leaves, Phosphorus for root blooming, and Potassium for disease resistance?",
                "key_focus": "Nitrogen in chlorophyll and amino acids, Phosphorus in ATP energy transfer and DNA, Potassium in stomata cell regulation, cation exchange capacity (CEC) of soil, and Liebig's Law of the Minimum.",
                "reason": "The non-negotiable chemical nutrient foundation governing every garden, farm, and commercial greenhouse on Earth."
            },
            {
                "id": 3,
                "title": "Soil Texture and Structure: Sand, Silt, Clay, and The Humus Sponge",
                "tier": "Tier 1: Soil Biology & Nutrient Fundamentals",
                "angle": "soil_mechanics",
                "slug": "soil_texture_triangle_sand_silt_clay_humus_porosity_jar_test",
                "question": "How can you determine your soil type using an ordinary glass mason jar and water, and why does clay soil hold immense nutrients while suffocating roots?",
                "key_focus": "The USDA soil texture triangle, sand drainage vs. clay mineral charge holding cations, micropores vs. macropores, glomalin glue building aggregate crumbs, and the sponge-like water holding capacity of organic humus.",
                "reason": "Essential practical diagnostic skills every grower must master before planting seeds."
            },
            {
                "id": 4,
                "title": "Seed Germination: Imbibition, Gibberellins, and Breaking Seed Dormancy",
                "tier": "Tier 1: Soil Biology & Nutrient Fundamentals",
                "angle": "seed_physiology",
                "slug": "seed_germination_physiology_imbibition_gibberellic_acid_stratification_scarification",
                "question": "What triggers a hard, dry seed that has slept for years to suddenly crack open its shell and send a radicle root straight down against gravity?",
                "key_focus": "Water imbibition swelling seed tissues, gibberellin hormone activation triggering amylase enzymes to digest starch reserves, cold moist stratification breaking chemical dormancy, mechanical scarification, and gravitropism/phototropism.",
                "reason": "Explores the miraculous biophysical awakening of dormant plant life."
            },
            {
                "id": 5,
                "title": "Composting Thermodynamics: How Thermophilic Bacteria Cook Waste into Black Gold at 150°F",
                "tier": "Tier 1: Soil Biology & Nutrient Fundamentals",
                "angle": "compost_chemistry",
                "slug": "composting_thermodynamics_carbon_nitrogen_30_to_1_ratio_thermophilic_bacteria",
                "question": "Why does a pile of brown leaves and green grass clippings get so hot it steams in freezing snow without any fire or external heat source?",
                "key_focus": "The 30:1 Carbon-to-Nitrogen ratio, mesophilic vs. thermophilic bacteria (Bacillus, Actinobacteria), biological heat generation reaching 140–160°F to kill weed seeds and pathogens, turning for oxygenation, and curing into stable humic compost.",
                "reason": "A deeply practical, thermal biochemistry masterclass for recycling organic waste into fertility."
            },
            {
                "id": 6,
                "title": "Legume Nitrogen Fixation: The Secret Bacterial Nodules on Pea and Clover Roots",
                "tier": "Tier 2: Rotation, Irrigation & Integrated Pests",
                "angle": "biological_fixation",
                "slug": "rhizobium_nitrogen_fixation_legumes_root_nodules_nitrogenase_enzyme",
                "question": "How do clover, peas, and soybeans produce their own free nitrogen fertilizer using subterranean root tumors packed with pink symbiotic bacteria?",
                "key_focus": "Rhizobium bacteria infecting root hairs, leghemoglobin buffering oxygen (giving healthy nodules a red meat interior), the nitrogenase enzyme cracking triple-bonded N2 gas, green manure tilling, and crop rotation economics.",
                "reason": "Examines nature's biological fertilizer factory that sustained global agriculture for millennia before Haber-Bosch."
            },
            {
                "id": 7,
                "title": "Irrigation Engineering: Drip Systems, Evapotranspiration, and The Tragedy of Flood Basins",
                "tier": "Tier 2: Rotation, Irrigation & Integrated Pests",
                "angle": "water_management",
                "slug": "agricultural_irrigation_drip_tape_emitter_efficiency_evapotranspiration_salinization",
                "question": "Why does flood irrigation waste 50% of water to evaporation while poisoning farm soils with surface salt crusts, and how does Israeli drip tape save agriculture?",
                "key_focus": "Simcha Blass inventing drip emitters, pressure-compensating drip tape delivering water directly to root zones at 95% efficiency, Penman-Monteith evapotranspiration calculations, soil tensiometers, and preventing agricultural salinization.",
                "reason": "Crucial agricultural engineering masterclass on solving the world's looming freshwater crisis."
            },
            {
                "id": 8,
                "title": "Integrated Pest Management (IPM): Using Parasitic Wasps and Ladybugs Instead of Poison",
                "tier": "Tier 2: Rotation, Irrigation & Integrated Pests",
                "angle": "biological_pest_control",
                "slug": "integrated_pest_management_ipm_beneficial_insects_parasitic_wasps_aphids",
                "question": "Why does blanket spraying synthetic chemical pesticides kill the predators, make pest bugs resistant, and create worse super-infestations next season?",
                "key_focus": "Economic injury levels (EIL), scouting thresholds, beneficial insect biological warfare (ladybug larvae consuming 50 aphids a day, Trichogramma micro-wasps laying eggs inside hornworms), pheromone mating disruption traps, and targeted biopesticides (Bt / Bacillus thuringiensis).",
                "reason": "The intelligent ecological alternative to toxic chemical dependence in modern food production."
            },
            {
                "id": 9,
                "title": "Cover Crops and Green Manure: Armor-Plating Soil Against Wind and Drought",
                "tier": "Tier 2: Rotation, Irrigation & Integrated Pests",
                "angle": "cover_cropping",
                "slug": "cover_crops_cereal_rye_hairy_vetch_tillage_radish_erosion_control",
                "question": "How can planting deep Daikon 'tillage radishes' drill 3 feet through hardpan clay without a plow and leave aerated compost channels for spring roots?",
                "key_focus": "Cocktail cover crop mixes (grasses for carbon and erosion armor, legumes for nitrogen, brassicas for biological subsoil tillage), keeping living roots in the ground 365 days a year, weed suppression mats, and roller-crimping termination.",
                "reason": "Demonstrates the foundational soil-building practice of modern sustainable and organic farming."
            },
            {
                "id": 10,
                "title": "The Four-Field Crop Rotation: The 18th-Century Norfolk System That Fed the Industrial World",
                "tier": "Tier 2: Rotation, Irrigation & Integrated Pests",
                "angle": "historical_agronomy",
                "slug": "norfolk_four_course_rotation_townshend_wheat_turnips_barley_clover",
                "question": "How did Charles 'Turnip' Townshend's four-crop rotation (wheat, turnips, barley, clover) eliminate the wasteful medieval fallow year and double European food output?",
                "key_focus": "Medieval two-field and three-field fallow limitations, turnips providing winter livestock fodder, clover restoring soil fertility, continuous land utilization, breaking pest and weed life cycles, and fueling the British Agricultural Revolution.",
                "reason": "Documents the historic agronomic breakthrough that allowed human populations to urbanize and industrialize."
            },
            {
                "id": 11,
                "title": "Gabe Brown and The 5 Principles of Soil Health: The Regenerative Agriculture Blueprint",
                "tier": "Tier 3: Regenerative Agriculture & Livestock",
                "angle": "regenerative_systems",
                "slug": "gabe_brown_five_principles_soil_health_dirt_to_soil_regenerative_farming",
                "question": "How did a bankrupt North Dakota farmer eliminate all synthetic fertilizers, fungicides, and insecticides and quadruple his soil organic matter from 1.9% to 11%?",
                "key_focus": "The 5 principles: 1) Armor the soil surface, 2) Minimize soil disturbance, 3) Plant diversity, 4) Keep living roots continuously, 5) Integrate livestock; infiltration rate jumping from 0.5 inches/hour to 8 inches/hour.",
                "reason": "The inspiring, real-world case study driving the global regenerative agriculture revolution."
            },
            {
                "id": 12,
                "title": "No-Till Farming vs. Conventional Plowing: The Battle for the Dust Bowl's Soul",
                "tier": "Tier 3: Regenerative Agriculture & Livestock",
                "angle": "tillage_debates",
                "slug": "no_till_farming_vs_moldboard_plow_dust_bowl_erosion_microbiome_destruction",
                "question": "Why did John Deere's steel moldboard plow win the American West but cause the catastrophic 1930s Dust Bowl that choked North America?",
                "key_focus": "The physical destruction of soil fungal hyphae by plowing, rapid oxidation of soil organic matter releasing CO2 into the atmosphere, wind erosion stripping topsoil, modern no-till drill planters slicing through crop residue, and moisture retention.",
                "reason": "A profound historical and environmental showdown between industrial tractor horsepower and biological soil preservation."
            },
            {
                "id": 13,
                "title": "Mob Grazing and Holistic Management: Using Cattle to Reverse Desertification",
                "tier": "Tier 3: Regenerative Agriculture & Livestock",
                "angle": "rotational_grazing",
                "slug": "allan_savory_holistic_management_mob_grazing_reversing_desertification",
                "question": "How can packing hundreds of cows tightly together in daily moved electric-fenced paddocks restore dying grasslands instead of destroying them?",
                "key_focus": "Allan Savory's Holistic Management, mimicking wild buffalo herds bunched by predators, intense hoof action breaking soil crusts, trampling organic mulch, concentrated manure and urine fertilization, and long 90-day recovery rest periods.",
                "reason": "Challenges the conventional narrative that cattle are purely destructive, showcasing ruminants as vital grassland ecosystem engineers."
            },
            {
                "id": 14,
                "title": "Agroforestry and Silvopasture: Integrating Trees, Crops, and Animals on One Acre",
                "tier": "Tier 3: Regenerative Agriculture & Livestock",
                "angle": "multi_strata_systems",
                "slug": "silvopasture_agroforestry_tree_canopy_livestock_shelter_carbon_drawdown",
                "question": "Why do livestock gain weight faster and crops produce higher yields when planted directly beneath rows of walnut, oak, and apple trees?",
                "key_focus": "Silvopasture mechanics (livestock sheltered from wind and summer heat stress, fodder trees like willow providing natural aspirin/salicin), multi-strata food forests, windbreak erosion buffers, deep tree roots pumping subsoil minerals, and multi-tier revenue streams.",
                "reason": "Ranked by Project Drawdown as one of the single most powerful climate-cooling carbon sequestration practices on Earth."
            },
            {
                "id": 15,
                "title": "Biochar: The Amazonian Terra Preta Secret for 1,000-Year Soil Carbon Storage",
                "tier": "Tier 3: Regenerative Agriculture & Livestock",
                "angle": "ancient_soil_amendments",
                "slug": "terra_preta_biochar_amazonian_dark_earths_pyrolysis_carbon_sponge",
                "question": "How did pre-Columbian Amazonian indigenous civilizations turn infertile, leached tropical red clay into pitch-black fertile soil that remains rich 1,500 years later?",
                "key_focus": "Terra Preta do Indio (Amazonian Dark Earths), low-oxygen biomass pyrolysis producing porous recalcitrant biochar, immense microscopic surface area housing beneficial microbes, 'charging' biochar with compost tea and minerals, and permanent geological carbon storage.",
                "reason": "Connects ancient archaeological discoveries with cutting-edge negative-emissions carbon sequestration agronomy."
            },
            {
                "id": 16,
                "title": "Precision Agriculture: Autonomous GPS Tractors, RTK Steering, and Variable Rate Seeding",
                "tier": "Tier 4: Precision Agritech & Global Food Systems",
                "angle": "high_tech_farming",
                "slug": "precision_agriculture_rtk_gps_sub_inch_guidance_variable_rate_fertilizer",
                "question": "How do 500-horsepower combine harvesters steer themselves across fields with 1-inch satellite accuracy and adjust fertilizer application gram-by-gram on the fly?",
                "key_focus": "Real-Time Kinematic (RTK) satellite positioning correcting drift down to 2 centimeters, variable rate technology (VRT) prescription maps adjusting seed density based on sub-acre soil sensor data, section control on boom sprayers eliminating overspray, and autonomous farm swarms.",
                "reason": "Examines the cutting-edge fusion of aerospace satellite telemetry, robotics, and commercial agricultural equipment."
            },
            {
                "id": 17,
                "title": "Drones and NDVI Satellites: Spotting Crop Disease from Space Before the Human Eye Sees It",
                "tier": "Tier 4: Precision Agritech & Global Food Systems",
                "angle": "remote_sensing",
                "slug": "ndvi_satellite_drone_monitoring_multispectral_near_infrared_crop_vigor",
                "question": "How can multispectral cameras on agricultural drones detect fungal infections and nitrogen deficiencies in corn three weeks before leaves show any visible yellowing?",
                "key_focus": "Normalized Difference Vegetation Index (NDVI), healthy plant chlorophyll reflecting Near-Infrared (NIR) light while absorbing red light, multispectral drone mapping producing thermal water-stress indices, and targeted pinpoint tractor spraying.",
                "reason": "Showcases how space-age remote sensing prevents crop failures and cuts chemical usage by 80%."
            },
            {
                "id": 18,
                "title": "Indoor Vertical Farming: LED Light Recipes, Aeroponics, and The Real Economics",
                "tier": "Tier 4: Precision Agritech & Global Food Systems",
                "angle": "controlled_environment",
                "slug": "indoor_vertical_farming_aeroponics_led_light_recipes_energy_economics_appharvest",
                "question": "Can growing lettuce in 10-story warehouse towers using 95% less water and pink LED lights feed cities, or do staggering electricity bills doom vertical farms to bankruptcy?",
                "key_focus": "Photosynthetically Active Radiation (PAR) spectrum tuning, aeroponic misting delivering nutrient oxygenation directly to suspended bare roots, zero pesticides, eliminating 2,000-mile trucking, and the harsh energy-cost reality behind recent bankruptcies (AppHarvest, AeroFarms).",
                "reason": "A realistic, engineering-backed economic assessment of high-tech indoor urban farming."
            },
            {
                "id": 19,
                "title": "CRISPR and Gene-Edited Crops: Engineering Drought Resistance and Golden Rice",
                "tier": "Tier 4: Precision Agritech & Global Food Systems",
                "angle": "agricultural_biotechnology",
                "slug": "crispr_cas9_gene_editing_crops_drought_resistant_c4_photosynthesis_golden_rice",
                "question": "What is the crucial scientific difference between old transgenic GMOs and precision CRISPR gene editing that simply toggles a plant's own native drought-resistance genes?",
                "key_focus": "CRISPR-Cas9 targeted gene knockouts, editing stomatal density to survive 40-day droughts, converting C3 rice to hyper-efficient C4 photosynthesis, Golden Rice synthesizing Vitamin A to prevent childhood blindness, and global regulatory battles.",
                "reason": "Explores the molecular genetics frontier developing the crops humanity needs to survive accelerating climatic extremes."
            },
            {
                "id": 20,
                "title": "The Global Fertilizer Geopolitics: Phosphorus Peaks, Potash Cartels, and Food Sovereignty",
                "tier": "Tier 4: Precision Agritech & Global Food Systems",
                "angle": "geopolitical_agronomy",
                "slug": "global_fertilizer_geopolitics_peak_phosphorus_morocco_reserves_potash_cartels",
                "question": "Why does a single nation—Morocco—hold 70% of the entire world's remaining minable phosphate rock, and what happens when global agricultural reserves run dry?",
                "key_focus": "The Peak Phosphorus crisis (mined phosphate rock cannot be synthesized in factories like nitrogen), Canadian and Belarusian potash monopolies, natural gas pipelines controlling Haber-Bosch ammonia, and the vital national security imperative of local biological nutrient recycling.",
                "reason": "Capstones the master curriculum with the urgent macroeconomic and geopolitical reality underwriting modern global civilization's food supply."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The John Deere Right to Repair Revolt: Why Farmers Are Hacking Tractors with Ukrainian Firmware",
                "tier": "Trending / High Retention",
                "angle": "right_to_repair",
                "slug": "john_deere_right_to_repair_farmers_hacking_tractors_ukrainian_firmware",
                "trend_score": 98,
                "why_trending": "Massive viral outrage and legal battles as third-generation farmers are locked out of repairing their own $500,000 tractors due to proprietary digital DRM software locks.",
                "reason": "Incredible high-conflict hook uniting rural working-class autonomy, intellectual property battles, and underground software hacking.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why Clarkson's Farm Is the Most Accurate Farming Show Ever Made",
                "tier": "Trending / High Retention",
                "angle": "pop_culture_farming",
                "slug": "clarksons_farm_diddly_squat_jeremy_clarkson_kaleb_farming_brutal_realities",
                "trend_score": 97,
                "why_trending": "Jeremy Clarkson's hit Amazon show 'Clarkson's Farm' has drawn tens of millions of viewers, earning universal praise from actual farmers for showing weather ruin, bureaucracy, and £144 annual profit margins.",
                "reason": "Massive cultural touchpoint that humanizes the brutal, unglamorous economic struggles of food producers.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Can a 1-Acre Homestead Actually Feed a Family of Four? The Cold Hard Calorie Math",
                "tier": "Trending / High Retention",
                "angle": "homestead_reality_check",
                "slug": "can_one_acre_feed_family_of_four_calorie_math_potatoes_vs_cattle",
                "trend_score": 98,
                "why_trending": "Surging interest in homesteading and self-reliance clashing with reality-check videos breaking down the 2.9 million annual calories needed for a family of four.",
                "reason": "Fascinating caloric calculations: why you need calorie-dense staples (potatoes, dry beans, pigs) rather than trendy raised-bed salad greens.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "The Dutch Farmer Protests: Why the World's Most Efficient Agriculture Cut Nitrogen by 50%",
                "tier": "Trending / High Retention",
                "angle": "global_farmer_protests",
                "slug": "dutch_farmer_protests_netherlands_nitrogen_crisis_tractor_blockades",
                "trend_score": 96,
                "why_trending": "Thousands of Dutch tractors shutting down highways and government buildings over EU environmental nitrogen emissions mandates forcing livestock culls.",
                "reason": "High-stakes geopolitical conflict pitting extreme technological agricultural efficiency against EU ecological directives.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "Why Heirloom Tomatoes Taste 10 Times Better Than Supermarket Ones: The Ripening Gene Flaw",
                "tier": "Trending / High Retention",
                "angle": "food_taste_mysteries",
                "slug": "why_heirloom_tomatoes_taste_better_u_phenotype_uniform_ripening_gene",
                "trend_score": 95,
                "why_trending": "Fascinating genetic research revealing commercial breeders selected a mutation for uniform red color that accidentally deactivated sugar and aroma chloroplast genes.",
                "reason": "Universally shared consumer frustration solved with hard plant genetics explaining why grocery store tomatoes taste like cardboard water.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Great Dust Bowl of the 1930s: When American Topsoil Blackened the Skies of Washington D.C.",
                "tier": "Trending / High Retention",
                "angle": "historical_disasters",
                "slug": "dust_bowl_1930s_black_blizzard_hugh_bennett_soil_conservation_service",
                "trend_score": 96,
                "why_trending": "Terrifying archival footage of monstrous 7,000-foot 'Black Blizzard' dust storms that choked cattle, suffocated children, and caused the largest ecological migration in US history.",
                "reason": "Chilling cautionary tale of industrial soil mismanagement and the heroic birth of the Soil Conservation Service.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Korean Natural Farming (KNF): Cultivating Indigenous Microorganisms (IMO) with Leftover Rice",
                "tier": "Trending / High Retention",
                "angle": "natural_farming_hacks",
                "slug": "korean_natural_farming_knf_master_cho_indigenous_microorganisms_imo1_rice",
                "trend_score": 97,
                "why_trending": "Explosive viral wave among organic growers capturing wild white mycelium from forest bamboo groves using cedar boxes of cooked rice (IMO 1 to IMO 4).",
                "reason": "Accessible, zero-cost biological alchemy that lets growers manufacture their own elite microbial inoculants at home.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "094_rural_life_village_culture": {
        "id": "094",
        "slug": "rural_life_village_culture",
        "title": "Rural Life & Village Culture",
        "category": "Cultural_Heritage",
        "audience": "Countryside Dreamers, Cultural Anthropologists, Rural Historians, Slow Living Seekers (Global)",
        "progression": [
            ("Tier 1: Village Architecture, Seasonal Rhythms & Community Commons (Scratch / Beginner)",
             "Vernacular stone and timber building traditions, the agricultural calendar (plowing, sowing, harvest, wintering), common pastures and water management, and village squares."),
            ("Tier 2: Traditional Food Preservation & Cottage Economies (Intermediate)",
             "Root cellars, smokehouses, salting and drying, communal bread ovens, cottage industries (spinning, basketry, seasonal foraging), and livestock husbandry rhythms."),
            ("Tier 3: Folklore, Village Rituals & Intergenerational Knowledge (Upper Intermediate)",
             "Harvest festivals, seasonal solstices, oral storytelling traditions, traditional healing herbs and midwifery, and folk music instruments (fiddles, pipes, hand drums)."),
            ("Tier 4: Modern Rural Exodus, Village Revitalization & The Neo-Rural Renaissance (Advanced / Expert)",
             "Depopulation of European/Asian mountain villages, remote work reverse-migration, eco-villages and community land trusts, preserving disappearing rural dialects, and agrarian cultural preservation.")
        ],
        "flagship": {
            "title": "The Root Cellar Blueprint: How Ancient Villages Kept Food Fresh All Winter Without Electricity",
            "angle": "traditional_technologies",
            "slug": "094_rural_life_village_culture_traditional_technologies_root_cellar_blueprint"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Root Cellar Blueprint: How Ancient Villages Kept Food Fresh All Winter Without Electricity",
                "tier": "Tier 1: Village Architecture & Seasonal Rhythms",
                "angle": "traditional_technologies",
                "slug": "traditional_root_cellar_architecture_geothermal_humidity_storage_wintering",
                "question": "How did pre-electric villages build subterranean dirt-floor pantries that maintained an exact 32°F to 40°F temperature and 90% humidity to keep apples and potatoes crisp for 7 months?",
                "key_focus": "Geothermal earth berming below the frost line, natural convection two-pipe ventilation (low intake, high exhaust), dirt floors releasing moisture, separating ethylene-producing apples from potatoes, and packing root crops in damp sand.",
                "reason": "Flagship launch episode; unlocks the ingenious low-tech passive architecture that kept human settlements alive through harsh freezing winters."
            },
            {
                "id": 2,
                "title": "Vernacular Architecture: Dry Stone Walls, Timber Frames, and Thatch Roofs",
                "tier": "Tier 1: Village Architecture & Seasonal Rhythms",
                "angle": "vernacular_construction",
                "slug": "vernacular_architecture_dry_stone_walling_cotswold_thatched_roof_water_reed",
                "question": "Why do 400-year-old dry stone walls in Yorkshire and Cotswold cottages hold together without mortar, and why can water reed thatch roofs shed torrential rain for 60 years?",
                "key_focus": "Gravity and friction interlocking in dry stone walling (hearting stones and through stones), timber framing mortise-and-tenon wood peg joints flexing in earthquakes, and Norfolk water reed thatch density creating water-shedding capillary slopes.",
                "reason": "Celebrates the hyper-localized, zero-carbon building wisdom evolved over centuries in harmony with regional geology."
            },
            {
                "id": 3,
                "title": "The Agricultural Calendar: Equinoxes, Sowing Moons, and The Wintering Ritual",
                "tier": "Tier 1: Village Architecture & Seasonal Rhythms",
                "angle": "seasonal_rhythms",
                "slug": "traditional_agricultural_calendar_solar_terms_sowing_harvest_wintering",
                "question": "How did traditional villages without printed calendars organize communal labor around solar equinoxes, lunar phases, and natural phenological signals?",
                "key_focus": "The 24 solar terms in East Asia (Jieqi), European seasonal quarter days (Candlemas, May Day, Lammas, Martinmas), planting potatoes when oak leaves are the size of squirrel ears, and collective autumn butchering/curing before winter.",
                "reason": "Reconnects viewers with the biological clock that governed all human civilization before clocks and artificial lights."
            },
            {
                "id": 4,
                "title": "The Tragedy of the Commons: How Ancient Villages Managed Shared Water and Pastures",
                "tier": "Tier 1: Village Architecture & Seasonal Rhythms",
                "angle": "commons_governance",
                "slug": "managing_the_commons_elinor_ostrom_traditional_water_acequias_pasture_rights",
                "question": "Did traditional villagers really overgraze their common lands, or did Nobel laureate Elinor Ostrom prove communities managed shared resources sustainably for 1,000 years?",
                "key_focus": "Elinor Ostrom's 8 design principles for managing common pool resources, Spanish Acequia water-sharing canals, alpine Swiss common grazing stints, village assemblies, and social reputation enforcement vs. privatization.",
                "reason": "Crucial political and sociological history debunking Garrett Hardin's 'Tragedy of the Commons' myth."
            },
            {
                "id": 5,
                "title": "The Village Square: The Architecture of Community, Markets, and Gossip",
                "tier": "Tier 1: Village Architecture & Seasonal Rhythms",
                "angle": "spatial_sociology",
                "slug": "the_village_square_piazza_commons_spatial_sociology_weekly_market_gossip",
                "question": "Why does a cobblestone Italian piazza, an English village green, or an Indian choupai create deeper human connection than modern suburban strip malls?",
                "key_focus": "Human scale urban geography (pedestrian radius, enclosure ratio), public water fountains and wash houses as social communication hubs, weekly agricultural market days, and communal cohesion shielding against loneliness.",
                "reason": "An architectural and sociological look at the spatial design that fostered tight-knit human communities."
            },
            {
                "id": 6,
                "title": "The Communal Bread Oven: Le Four Banal and The Weekly Baking Ritual",
                "tier": "Tier 2: Food Preservation & Cottage Economies",
                "angle": "communal_foodways",
                "slug": "communal_bread_oven_four_banal_weekly_baking_thermal_cascade_community",
                "question": "Why did medieval European villages share a single massive masonry wood-fired oven, and how did its descending heat cascade cook bread, stews, and fruit over 3 days?",
                "key_focus": "Feudal oven rights (Le Four Banal), thermal mass retention of refractory stone, the heat cascade (baking sourdough at 500°F on day 1, slow stews and roasts at 300°F on day 2, drying herbs and fruit at 150°F on day 3), and village bonding.",
                "reason": "A heartwarming historical food culture study showing how thermal efficiency created community solidarity."
            },
            {
                "id": 7,
                "title": "The Traditional Smokehouse: Cold Smoking Hams, Bacon, and Sausage for Year-Round Survival",
                "tier": "Tier 2: Food Preservation & Cottage Economies",
                "angle": "preservation_craft",
                "slug": "traditional_smokehouse_cold_smoking_country_hams_phenols_bacteriostatic_smoke",
                "question": "How did farm families cure and smoke 400 lbs of pork in an uninsulated wooden shack so it would hang at room temperature through the heat of summer without spoiling?",
                "key_focus": "Salt curing extracting cellular moisture, cold smoking below 85°F (29°C) applying bacteriostatic formaldehyde and phenols without cooking fat, hickory and applewood smoke chemistry, protective pellicle formation, and the Appalachian country ham tradition.",
                "reason": "The essential traditional meat preservation science that made rural self-sufficiency possible."
            },
            {
                "id": 8,
                "title": "Foraging Wisdom: Wild Mushrooms, Spring Greens, and The Village Apothecary",
                "tier": "Tier 2: Food Preservation & Cottage Economies",
                "angle": "wild_foodways",
                "slug": "traditional_foraging_spring_greens_nettles_wild_mushrooms_chanterelles_ethics",
                "question": "Why did rural villagers eagerly forage stinging nettles and dandelion greens in early spring, and how did foraging knowledge pass seamlessly from grandmother to child?",
                "key_focus": "Nutritional medicine (spring greens replenishing Vitamin C after scurvy-prone winters), wild garlic (ramps), identifying mycorrhizal mushrooms (chanterelles, porcini) by symbiotic tree species, sustainable harvesting ethics, and avoiding poisonous lookalikes.",
                "reason": "Celebrates the deep botanical literacy and wild food traditions that supplemented rural garden plots."
            },
            {
                "id": 9,
                "title": "Cottage Industries: Wool Spinning, Willow Basketry, and Winter Income",
                "tier": "Tier 2: Food Preservation & Cottage Economies",
                "angle": "cottage_economics",
                "slug": "cottage_industries_wool_spinning_drop_spindle_willow_basketry_putting_out_system",
                "question": "What did farm families do during the dark, frozen winter months when fields were buried under snow? The putting-out system and domestic crafts.",
                "key_focus": "Carding and drop-spindle wool spinning by the hearth, willow coppicing and basketry for grain harvest containers, hand-carving wooden treen spoons, and early capitalist merchants providing raw wool and buying finished yarn.",
                "reason": "Explores the winter home workshop economy that sustained rural families between agricultural seasons."
            },
            {
                "id": 10,
                "title": "Traditional Beekeeping: Skeps, Log Hives, and The Sacred 'Telling the Bees'",
                "tier": "Tier 2: Food Preservation & Cottage Economies",
                "angle": "apiculture_heritage",
                "slug": "traditional_beekeeping_straw_skeps_log_hives_telling_the_bees_folklore",
                "question": "Why was a European villager obligated to walk out to the straw beehives and whisper family deaths, births, and marriages to prevent the bees from flying away or dying?",
                "key_focus": "Straw skep hive architecture, hollowed tree-trunk log hives, pollination value vs. honey harvesting, beeswax candle crafting, mead fermentation, and the ancient folklore of bees as messengers to the spirit world.",
                "reason": "Weaves natural apicultural history with the charming folklore that bound humans and insects together in rural life."
            },
            {
                "id": 11,
                "title": "Harvest Festivals: The Last Sheaf, Corn Dollies, and Feast Day Catharsis",
                "tier": "Tier 3: Folklore, Rituals & Oral History",
                "angle": "folk_rituals",
                "slug": "harvest_festivals_the_last_sheaf_corn_dolly_pagan_roots_michaelmas_feast",
                "question": "Why did villagers weave the very last cut sheaf of grain into a human doll and hang it over the kitchen hearth until spring planting?",
                "key_focus": "The spirit of the grain (Ceres / Corn Mother) trapped in the final stand of wheat, preserving the seed spirit through the dark winter, Michaelmas harvest feasts, community dancing, and releasing the pent-up tension of exhausting physical harvest labor.",
                "reason": "Examines the psychological, spiritual, and celebratory culmination of the entire rural year."
            },
            {
                "id": 12,
                "title": "The Hearth and The Storyteller: Oral Traditions and Fireside Lore",
                "tier": "Tier 3: Folklore, Rituals & Oral History",
                "angle": "oral_storytelling",
                "slug": "oral_storytelling_traditions_the_hearth_fairy_tales_cautionary_folklore",
                "question": "Why were fairy tales originally told around village peat fires to adults rather than children, and what survival warnings were coded into cautionary lore?",
                "key_focus": "The physical geography of the hearth as social theater, Irish Seanchaí and West African Griots, cautionary tales warning against wandering into bogs or dense forests at night (will-o'-the-wisps, wolves), and oral mnemonic memory structures.",
                "reason": "Explores the oral medium through which centuries of practical survival wisdom, morality, and culture were transmitted without books."
            },
            {
                "id": 13,
                "title": "Traditional Village Healing: Bone-Setters, Midwives, and Herbal Folklore",
                "tier": "Tier 3: Folklore, Rituals & Oral History",
                "angle": "folk_medicine",
                "slug": "traditional_village_healing_bone_setters_wise_women_willow_bark_chamomile",
                "question": "Before trained doctors and hospitals existed, who kept rural villagers alive through broken limbs, childbirth, and winter fevers?",
                "key_focus": "The village 'wise woman' and hereditary bone-setter, willow bark tea providing salicylic acid (aspirin), honey and elderberry for wounds and viral coughs, maternal midwifery knowledge, and the tragic 16th-century witch trials targeting female herbal practitioners.",
                "reason": "A respectful, evidence-based tribute to the folk medical practitioners who preserved human health for generations."
            },
            {
                "id": 14,
                "title": "Village Blacksmiths: The Sacred Alchemist at the Crossroads",
                "tier": "Tier 3: Folklore, Rituals & Oral History",
                "angle": "village_artisans",
                "slug": "village_blacksmith_crossroads_forge_horseshoeing_plowshares_spiritual_status",
                "question": "Why was the village blacksmith viewed as half-mechanic, half-sorcerer, and why did travelers come to the forge to get married over the anvil?",
                "key_focus": "The forge as the mechanical lifeblood of the village (shoeing draft horses, forging plowshares, sharpening scythes, shrinking wagon wheel iron tires), metallurgical mythology (Wayland the Smith, Hephaestus), and Gretna Green runaway anvil marriages.",
                "reason": "Spotlights the central artisan without whom rural agriculture, transport, and construction would grind to a halt."
            },
            {
                "id": 15,
                "title": "Folk Music and Dance: How Ceilidhs and Barn Dances Relieved Physical Labor",
                "tier": "Tier 3: Folklore, Rituals & Oral History",
                "angle": "folk_music_culture",
                "slug": "traditional_folk_music_ceilidh_barn_dance_fiddles_bagpipes_communal_catharsis",
                "question": "How did farmers who had spent 14 hours harvesting hay by hand still find the physical energy to dance all night to fiddles and pipes in a barn?",
                "key_focus": "Rhythmic synchronization inducing collective endorphin highs, Celtic Ceilidhs and American barn dances, work songs coordinating repetitive physical movement (waulking songs, sea shanties), and folk instruments built from farm materials.",
                "reason": "Celebrates the sonic joy and collective physical ecstasy that balanced the backbreaking hardships of rural life."
            },
            {
                "id": 16,
                "title": "The Rural Exodus: Why Millions Abandoned Villages for Industrial Megacities",
                "tier": "Tier 4: Rural Revitalization & Future Villages",
                "angle": "demographic_shifts",
                "slug": "rural_exodus_industrial_revolution_enclosure_acts_urbanization_flight",
                "question": "How did the British Parliamentary Enclosure Acts and mechanized tractors turn self-sufficient villagers into factory wage laborers in smoke-filled cities?",
                "key_focus": "Enclosure Acts fencing off the common lands, mechanization eliminating agricultural jobs, the lure of city wages vs. the loss of community autonomy, rural poverty, and the demographic hollowing out of the countryside.",
                "reason": "The defining historical transition that moved the human species from rural village existence into an urban species."
            },
            {
                "id": 17,
                "title": "The Ghost Villages of Europe and Asia: 1-Euro Houses in Italy and Akiya in Japan",
                "tier": "Tier 4: Rural Revitalization & Future Villages",
                "angle": "depopulation_crisis",
                "slug": "ghost_villages_one_euro_houses_italy_japan_akiya_depopulation_crisis",
                "question": "Why are charming medieval Italian hilltop towns selling stone villas for €1, and why are 10 million abandoned homes (Akiya) rotting in rural Japan?",
                "key_focus": "Aging populations and demographic collapse in the developed world, young people fleeing to Tokyo and Milan, the inheritance tax burden on abandoned properties, 1-Euro restoration clauses, and foreign buyers attempting village revivals.",
                "reason": "A fascinating, poignant look at the modern crisis of disappearing historic settlements."
            },
            {
                "id": 18,
                "title": "The Neo-Rural Renaissance: Digital Nomads, Eco-Villages, and Reverse Migration",
                "tier": "Tier 4: Rural Revitalization & Future Villages",
                "angle": "reverse_migration",
                "slug": "neo_rural_renaissance_remote_work_starlink_eco_villages_reverse_migration",
                "question": "How are high-speed satellite internet (Starlink) and remote knowledge work prompting young families to abandon $4,000/month city apartments for rural villages?",
                "key_focus": "The post-2020 urban flight, community-supported agriculture (CSA) subscriptions, co-housing eco-villages with shared permaculture gardens, rejuvenating closing village schools, and balancing modern technology with slow rural living.",
                "reason": "Explores the hopeful counter-trend breathing fresh youth and economic vitality back into dying rural regions."
            },
            {
                "id": 19,
                "title": "Preserving Disappearing Dialects: The Unique Accents Born in Isolated Valleys",
                "tier": "Tier 4: Rural Revitalization & Future Villages",
                "angle": "linguistic_heritage",
                "slug": "preserving_rural_dialects_linguistic_isolation_appalachian_english_patois",
                "question": "Why do isolated mountain valleys in Appalachia, the Swiss Alps, and northern Scotland preserve 400-year-old Elizabethan words and grammatical structures erased by modern TV?",
                "key_focus": "Geographic linguistic isolation preventing language leveling, Appalachian 'holler' speech keeping Elizabethan vowel shifts, French regional Patois, linguistic mapping initiatives, and the loss of cultural identity when rural accents die.",
                "reason": "A captivating linguistic journey into how geographic isolation acts as an acoustic time capsule."
            },
            {
                "id": 20,
                "title": "The 21st-Century Sustainable Village: Energy Autonomy, Local Food, and Human Scale Living",
                "tier": "Tier 4: Rural Revitalization & Future Villages",
                "angle": "future_villages",
                "slug": "future_sustainable_village_energy_independence_feldheim_microgrids_human_scale",
                "question": "What does a zero-emission, 100% self-sufficient modern village look like? The blueprint of Feldheim, Germany and Transition Towns.",
                "key_focus": "Feldheim, Germany (100% community-owned wind, biogas, and solar microgrid exporting surplus power), Rob Hopkins' Transition Town movement, localized food sovereignty, circular economy waste streams, and the enduring sanity of human-scale communities.",
                "reason": "Capstones the master curriculum with an inspiring, actionable model proving traditional village scale holds the answer to 21st-century ecological and psychological survival."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "I Bought a $1 House in Italy: The Hidden Costs and Bureaucratic Nightmares Exposed",
                "tier": "Trending / High Retention",
                "angle": "reality_check_vlogs",
                "slug": "buying_one_euro_house_italy_hidden_costs_renovation_permits_scam_or_deal",
                "trend_score": 98,
                "why_trending": "Massive viral curiosity across YouTube and social media following buyers who purchased €1 Sicilian houses only to face mandatory €50,000 restoration bonds and Byzantine Italian bureaucracy.",
                "reason": "High-conflict, eye-opening reality check that shatters romantic escapist fantasies with practical legal and financial realities.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "Why Japan Has 10 Million Free Abandoned Houses (Akiya) Nobody Wants",
                "tier": "Trending / High Retention",
                "angle": "international_housing_crisis",
                "slug": "japan_abandoned_akiya_houses_free_demographics_demolition_costs_superstitions",
                "trend_score": 97,
                "why_trending": "Viral documentaries showing gorgeous traditional wooden homes with tatami mats and tile roofs sitting abandoned in the Japanese countryside for zero dollars.",
                "reason": "Fascinating cultural and demographic breakdown: population aging, the 'Jiko Bukken' stigmatized death house superstition, and exorbitant demolition tax laws.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "The Cottagecore Fantasy vs. Brutal Farm Reality: Why So Many Homesteaders Quit in Year One",
                "tier": "Trending / High Retention",
                "angle": "cultural_critique",
                "slug": "cottagecore_aesthetic_vs_homestead_reality_burnout_mud_dead_animals",
                "trend_score": 98,
                "why_trending": "Widespread creator backlash against aesthetic TikTok 'Cottagecore' influencers showing pretty linen dresses, contrasting with the grueling 5:00 AM reality of frozen water buckets, sick goats, and relentless mud.",
                "reason": "Hilarious, deeply honest human interest hook celebrating real rural resilience over Instagram filters.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Inside the Amish Community: The Surprising Technology Rules You Never Knew",
                "tier": "Trending / High Retention",
                "angle": "cultural_deep_dive",
                "slug": "amish_technology_rules_ordnung_solar_panels_pneumatics_buggies_smartphones",
                "trend_score": 96,
                "why_trending": "Perennial fascination with Amish culture, debunking the myth that they hate technology by revealing they use solar power and air-powered pneumatic tools while rejecting grid ties to protect community cohesion.",
                "reason": "Thought-provoking sociological exploration of conscious technology adoption that challenges modern screen addiction.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "How to Build a Traditional Root Cellar with Cinder Blocks and Dirt: Step-by-Step",
                "tier": "Trending / High Retention",
                "angle": "diy_country_skills",
                "slug": "diy_cinder_block_root_cellar_earth_berm_ventilation_budget_build",
                "trend_score": 95,
                "why_trending": "High-utility DIY prepper and homestead builds racking up millions of views showing weekend warriors digging backyard hillside root cellars for $500.",
                "reason": "Practical, step-by-step masterclass with tangible food security payoff for homeowners.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The Lost Ancient Village of Hallstatt: The Salt Mine Town That Inspired Frozen's Arendelle",
                "tier": "Trending / High Retention",
                "angle": "storybook_villages",
                "slug": "hallstatt_austria_7000_year_salt_mine_arendelle_overtourism_backlash",
                "trend_score": 94,
                "why_trending": "Aesthetic travel videos of the 7,000-year-old Austrian salt village mirrored in pristine mountain lakes, clashing with local resident protests over 1 million annual tourists taking selfies.",
                "reason": "Gorgeous visuals combined with a timely debate on tourism destroying the very peaceful village charm it seeks.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Villagers Live Longer: The Secrets of the Ikaria and Sardinia 'Blue Zones'",
                "tier": "Trending / High Retention",
                "angle": "longevity_secrets",
                "slug": "blue_zones_sardinia_ikaria_village_longevity_centenarians_social_bonds",
                "trend_score": 97,
                "why_trending": "Massive global health interest following Netflix's 'Live to 100: Secrets of the Blue Zones', investigating isolated Greek and Sardinian mountain villages where people forget to die.",
                "reason": "Compelling lifestyle analysis showing that steep mountain walking, wild greens, daily wine with friends, and intergenerational respect beat expensive gym memberships.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    },

    "095_handicrafts_traditional_skills": {
        "id": "095",
        "slug": "handicrafts_traditional_skills",
        "title": "Handicrafts & Traditional Skills",
        "category": "Cultural_Heritage",
        "audience": "Artisans, Handcraft Lovers, Heritage Preservationists, Bushcrafters, Makers (Global)",
        "progression": [
            ("Tier 1: Natural Fibers, Basic Weaving & Traditional Clay Pottery (Scratch / Beginner)",
             "Drop spindles and spinning wheel physics, backstrap and floor looms, pinch and coil clay forming, pit firing earthenware, and basket weaving using willow and reeds."),
            ("Tier 2: Green Woodworking, Blacksmithing & Leather Tooling (Intermediate)",
             "Carving with drawknives and shavehorses, traditional anvil and forge heat colors (red to yellow), hand peening rivets, and vegetable-tanned leather carving and stamping."),
            ("Tier 3: Master Craft Guilds: Japanese Joinery, Stained Glass & Coppersmithing (Upper Intermediate)",
             "Japanese mortise joinery without nails (Kigumi), lead came stained glass soldering, repoussé and chasing on hammered copper, and natural indigo vat fermentation dyeing."),
            ("Tier 4: Endangered Crafts, Living National Treasures & The Handmade Revival (Advanced / Expert)",
             "UNESCO Intangible Cultural Heritage protocols, Japan's Living National Treasure system, apprentice-to-master lineage preservation, luxury artisanal valuation, and the digital creator craft boom.")
        ],
        "flagship": {
            "title": "Japanese Joinery: The Miracle of 1,000-Year-Old Wooden Temples Built Without a Single Nail",
            "angle": "heritage_mastery",
            "slug": "095_handicrafts_traditional_skills_heritage_mastery_japanese_joinery_kigumi"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "Japanese Joinery: The Miracle of 1,000-Year-Old Wooden Temples Built Without a Single Nail",
                "tier": "Tier 1: Natural Fibers, Weaving & Clay Pottery",
                "angle": "heritage_mastery",
                "slug": "japanese_joinery_kigumi_horyu_ji_temple_blind_mortise_earthquake_flex",
                "question": "How did ancient Japanese carpenters build Hōryū-ji—the world's oldest standing wooden structure—using intricate interlocking timber joints that flex during earthquakes without screws, nails, or glue?",
                "key_focus": "The philosophy of Kigumi (interlocking wood joinery), complex joints (Kanawa-tsugi, Ari-tsugi), surviving typhoons and seismic tremors through dynamic structural friction, the Kannna Japanese pull plane shaving wood down to 5-micron silk sheets, and sacred temple carpenter guilds.",
                "reason": "Flagship launch episode; the universal holy grail of traditional woodwork, cultural reverence, and mechanical structural genius."
            },
            {
                "id": 2,
                "title": "The Spinning Wheel and Drop Spindle: How Humans Turned Animal Hair into Cloth for 10,000 Years",
                "tier": "Tier 1: Natural Fibers, Weaving & Clay Pottery",
                "angle": "textile_craft_origins",
                "slug": "spinning_wheel_drop_spindle_physics_drafting_roving_wool_twist_tensile",
                "question": "How does spinning a weighted wooden whorl insert twist into fluffy sheared sheep wool fibers to create unbroken thread that can hoist weights?",
                "key_focus": "The physics of twist (S-twist vs. Z-twist), drafting roving fibers with fingers, drop spindle centrifugal momentum, the Great Wheel and flyer spinning wheels with foot treadles, and the transformation from raw wool fleece to spun yarn.",
                "reason": "The foundational ancient textile craft that clothed humanity and birthed global trade networks."
            },
            {
                "id": 3,
                "title": "Weaving on a Backstrap Loom: Ancient Mayan Geometry Woven from a Living Waist",
                "tier": "Tier 1: Natural Fibers, Weaving & Clay Pottery",
                "angle": "traditional_weaving",
                "slug": "backstrap_loom_mayan_weaving_warp_weft_shuttle_body_tension_geometry",
                "question": "How do indigenous weavers in Guatemala and the Andes weave museum-grade complex textiles using five sticks tied to a tree and anchored around their own hips?",
                "key_focus": "The portable backstrap loom, using body weight to dynamically regulate warp thread tension, string heddles and shed sticks creating the shed, flying shuttle mechanics, and ancient mathematical cosmological patterns passed down through generations without paper.",
                "reason": "Showcases one of humanity's most ingenious, lightweight, body-integrated handcraft technologies."
            },
            {
                "id": 4,
                "title": "Pit Firing and Primitive Pottery: Turning River Mud into Stone in an Open Fire",
                "tier": "Tier 1: Natural Fibers, Weaving & Clay Pottery",
                "angle": "primitive_ceramics",
                "slug": "primitive_pit_firing_pottery_river_clay_burnishing_sawdust_reduction",
                "question": "How did prehistoric potters dig clay straight out of riverbanks, coil it into pots, and bake them in wood pits without cracking them from thermal shock?",
                "key_focus": "Finding and processing wild clay (decanting and sieving), adding temper (sand or crushed pottery grog) to control shrinkage, stone burnishing for smooth water resistance, slow pre-heating beside the fire, and localized smoke reduction creating swirling carbon flash patterns.",
                "reason": "The quintessential primitive technology tutorial taking viewers straight back to the Stone Age roots of ceramics."
            },
            {
                "id": 5,
                "title": "Willow Basketry: The Ancient Architecture of Ribs, Stakes, and Weavers",
                "tier": "Tier 1: Natural Fibers, Weaving & Clay Pottery",
                "angle": "natural_weaving",
                "slug": "willow_basketry_stake_and_strand_coppicing_osier_slapping_waling_border",
                "question": "Why is basket weaving one of the few human crafts that can never be replicated by automated factory robots? The anatomy of a willow basket.",
                "key_focus": "Coppicing willow withies (Salix viminalis), soaking dried rods to restore flexibility, the slath base cross, staking up the uprights, three-rod waling weave for structural rigidity, and the woven rod border finish; why irregular natural branches defy industrial mechanization.",
                "reason": "Celebrates a pure handcraft requiring human tactile judgement and three-dimensional spatial improvisation."
            },
            {
                "id": 6,
                "title": "Green Woodworking: Carving Bowls and Spoons with a Drawknife and Shavehorse",
                "tier": "Tier 2: Green Wood, Forging & Leather",
                "angle": "green_woodworking",
                "slug": "green_woodworking_spoon_carving_drawknife_shavehorse_adzel_grain_direction",
                "question": "Why is freshly cut unseasoned 'green' wood as soft as cheese to carve with hand tools, and how do you prevent your carved wooden spoons from cracking as they dry?",
                "key_focus": "Working with green sapwood along natural split grain lines, the foot-powered shavehorse clamping bench, drawknives and scorp gouges, the curved spoon crook knife, reading fiber grain direction to prevent tear-out, and slow curing in wood shavings.",
                "reason": "The rapidly growing global craft movement connecting modern woodworkers to tactile, quiet hand tools."
            },
            {
                "id": 7,
                "title": "Traditional Blacksmithing: The Anvil, The Hammer, and Reading Steel at 2,000°F",
                "tier": "Tier 2: Green Wood, Forging & Leather",
                "angle": "blacksmithing_fundamentals",
                "slug": "traditional_blacksmithing_anvil_rebound_forge_colors_drawing_out_taper",
                "question": "How does a blacksmith read the color of glowing steel from dull red to lemon yellow to shape hot metal with the rebound of a hardened steel anvil?",
                "key_focus": "Anvil anatomy (face, horn, hardy and pritchel holes), 80%+ hammer rebound physics saving human elbows, the coal forge air blast, color temperature scale (cherry red 1,400°F to yellow 2,000°F), fundamental forging operations (drawing out, tapering, upsetting, punching, scrolling).",
                "reason": "The foundational metalworking craft that created all other craft tools throughout human history."
            },
            {
                "id": 8,
                "title": "Vegetable-Tanned Leather Tooling: Swivel Knives, Bevelers, and Carnauba Wax",
                "tier": "Tier 2: Green Wood, Forging & Leather",
                "angle": "leather_craftsmanship",
                "slug": "leather_tooling_casing_swivel_knife_carving_sheridan_style_beveling",
                "question": "How do Western leather masters carve intricate 3D floral scrollwork into cowhide using a swivel knife, brass stamping mallets, and moisture?",
                "key_focus": "Vegetable-tanned leather (bark tannin porosity) vs. chemically mineral chrome tan, 'casing' leather with water to achieve plastic memory state, freehand swivel knife incisions, background beveling creating depth illusion, antique paste dye highlighting cuts, and resolene water sealing.",
                "reason": "Examines the supreme decorative and functional leather carving tradition of the American West and Europe."
            },
            {
                "id": 9,
                "title": "Coppersmithing: Raising a Flat Copper Disc into a Seamless Kettle with a Mallet",
                "tier": "Tier 2: Green Wood, Forging & Leather",
                "angle": "metalsmithing_raising",
                "slug": "coppersmithing_raising_hammer_annealing_work_hardening_pitch_bowl",
                "question": "How can you take a flat 12-inch circle of red copper and hammer it over a steel stake until it rises into a deep, seamless water pitcher without tearing?",
                "key_focus": "Work hardening crystalline dislocations, torch annealing copper to dull red and water quenching to restore malleability, angle-raising hammer blows, planishing for mirror-smooth surfaces, and lining copper cooking pots with pure wiped molten tin.",
                "reason": "A dazzling demonstration of metallurgical plasticity and rhythmic hand-raising craft."
            },
            {
                "id": 10,
                "title": "Stained Glass Craftsmanship: Cartoons, Diamond Wheel Scoring, and Lead Came Soldering",
                "tier": "Tier 2: Green Wood, Forging & Leather",
                "angle": "stained_glass_craft",
                "slug": "stained_glass_craft_lead_came_louis_comfort_tiffany_copper_foil_glass_cutter",
                "question": "How do artisans cut fragile stained glass sheets into sharp curved puzzle pieces and fuse them together into cathedral rose windows that survive 800 years of storms?",
                "key_focus": "Full-scale pattern cartoons, tungsten carbide wheel glass scoring running along internal molecular fracture lines, H-channel lead came framing vs. Louis Comfort Tiffany's copper foil technique for lamp shades, 60/40 solder fluxing, and dark cement waterproofing.",
                "reason": "Explores the medieval architectural art form that turns sunlight into luminous sacred storytelling."
            },
            {
                "id": 11,
                "title": "Traditional Indigo Vat Dyeing: The Living Anaerobic Bacteria That Turn Green Leaves into Blue Cloth",
                "tier": "Tier 3: Master Guilds & Complex Techniques",
                "angle": "botanical_dyeing",
                "slug": "traditional_indigo_vat_dyeing_sukumo_fermentation_leuco_indigo_air_oxidation",
                "question": "Why is a natural indigo dye vat yellowish-green when submerged in the barrel, turning magical navy blue only when lifted out into the air?",
                "key_focus": "Indigofera and Polygonum tinctorium leaves, traditional Japanese Sukumo composting (100 days of water spraying), anaerobic fermentation reducing insoluble indigotin into soluble green 'leuco-indigo', dipping natural fibers, and atmospheric oxygen instantly oxidizing the dye to deep permanent blue.",
                "reason": "The most famous, magical, and chemically complex natural plant dye in global craft history."
            },
            {
                "id": 12,
                "title": "Repoussé and Chasing: Pushing Sheet Metal from Behind into 3D Sculptures",
                "tier": "Tier 3: Master Guilds & Complex Techniques",
                "angle": "sculptural_metalcraft",
                "slug": "repousse_and_chasing_pitch_bowl_chasing_hammers_punches_statue_of_liberty",
                "question": "How was the entire copper skin of the Statue of Liberty hammered into shape by hand over a tar-filled pitch bowl without casting molds?",
                "key_focus": "Repoussé (pushing metal from the reverse side to create relief volume), chasing (refining details and sharp outlines from the front face), chasers pitch (pine rosin, tallow, and plaster) providing yielding support, chasing hammer ergonomics, and micro-punches.",
                "reason": "The ancient Greek and Renaissance goldsmithing technique behind monumental copper sculptures and luxury armor."
            },
            {
                "id": 13,
                "title": "Dry Stone Masonry: The Celtic Clifftop Beehive Huts Built Without a Drop of Cement",
                "tier": "Tier 3: Master Guilds & Complex Techniques",
                "angle": "stone_craftsmanship",
                "slug": "dry_stone_corbeling_clochans_beehive_huts_skellig_michael_compression",
                "question": "How did early Christian monks on Ireland's storm-lashed Skellig Michael build beehive stone huts that remain bone-dry inside after 1,400 years without any mortar?",
                "key_focus": "Corbeling architecture (each stone layer stepping inward slightly toward the center until capped with a single stone), stones tilted slightly outward to shed wind-driven rainwater, gravitational compression locking dry stones, and seismic flexibility.",
                "reason": "Showcases extreme architectural endurance built purely from local rock, gravitational physics, and patient hand masonry."
            },
            {
                "id": 14,
                "title": "Traditional Papermaking: Japanese Washi from Mulberry Bark and Wild Tororo Aoi Mucilage",
                "tier": "Tier 3: Master Guilds & Complex Techniques",
                "angle": "papermaking_craft",
                "slug": "japanese_washi_papermaking_kozo_mulberry_bark_tororo_aoi_sugeta_deckle",
                "question": "Why can Japanese Washi paper survive for 1,000 years without yellowing or crumbling, while modern wood-pulp paper turns brittle in 50 years?",
                "key_focus": "Harvesting Kozo (paper mulberry) inner white bark, boiling with wood ash, beating long fibers with wooden mallets, Tororo-aoi plant root mucilage suspending fibers evenly, dipping and rocking the Sugeta bamboo screen mould, and natural sun drying on wooden boards.",
                "reason": "UNESCO-recognized mastercraft producing the most durable, delicate, and long-lasting paper on Earth."
            },
            {
                "id": 15,
                "title": "Loom Beaded Tapestries: The Huichol Yarn and Bead Masterpieces of the Sierra Madre",
                "tier": "Tier 3: Master Guilds & Complex Techniques",
                "angle": "indigenous_crafts",
                "slug": "huichol_yarn_painting_chaquira_glass_beads_campeche_wax_sacred_vision_art",
                "question": "How do Wixárika (Huichol) artisans in Mexico press millions of tiny glass seed beads one-by-one into beeswax on wooden boards without drawing outlines?",
                "key_focus": "Cera de Campeche (wild beeswax and pine resin adhesive mixture), pressing beads with needles, psychedelic spiritual vision symbolism (deer, peyote, corn, eagle), oral mythology encoded into visual tapestries, and preserving indigenous economic sovereignty.",
                "reason": "Celebrates one of the world's most vibrant, spiritually intense, and technically painstaking indigenous craft arts."
            },
            {
                "id": 16,
                "title": "The Japanese Urushi Lacquer Miracle: 40 Layers of Toxic Tree Sap Polished with Charcoal",
                "tier": "Tier 4: Endangered Crafts & Living Treasures",
                "angle": "luxury_craft_mastery",
                "slug": "urushi_lacquer_toxic_tree_sap_rhus_verniciflua_charcoal_polishing_kintsugi",
                "question": "Why will touching raw Urushi tree sap cause severe poison ivy blisters, but once cured, it creates an unbreakable, waterproof, acid-proof armor that lasts millennia?",
                "key_focus": "Tapping Toxicodendron vernicifluum trees, urushiol oxidation curing ONLY in high humidity (75–85% RH) and warm temperatures via laccase enzymes, applying 40 microscopic coats over zelkova wood, charcoal hand polishing, and Maki-e gold dust sprinkling.",
                "reason": "The pinnacle of East Asian organic polymer technology, producing lustrous finishes that defy time and chemical attack."
            },
            {
                "id": 17,
                "title": "Kintsugi: The Philosophy of Repairing Broken Ceramics with Real Gold",
                "tier": "Tier 4: Endangered Crafts & Living Treasures",
                "angle": "philosophical_craft",
                "slug": "kintsugi_golden_joinery_urushi_gold_powder_wabi_sabi_flaws_as_history",
                "question": "Why does the Japanese art of Kintsugi celebrate broken tea bowls by gluing ceramic shards back together with Urushi lacquer and dusting the crack with 24K gold powder?",
                "key_focus": "Wabi-sabi aesthetics (beauty in imperfection and impermanence), Mugi-urushi flour glue bonding shards, Kokuso sawdust filler rebuilding missing fragments, Bengara red lacquer primer, 24K pure gold powder dusting, and treating scars as the most beautiful part of an object's history.",
                "reason": "A profound philosophical and practical craft that turns brokenness into treasured heirloom value."
            },
            {
                "id": 18,
                "title": "Japan's Living National Treasures: The Government System That Pays Masters to Keep Crafts Alive",
                "tier": "Tier 4: Endangered Crafts & Living Treasures",
                "angle": "heritage_policy",
                "slug": "living_national_treasures_japan_ningen_kokuho_intangible_cultural_heritage",
                "question": "How does Japan's 'Ningen Kokuhō' system award annual state stipends to master sword-smiths, potters, and weavers to ensure centuries-old techniques are never lost?",
                "key_focus": "The 1950 Law for the Protection of Cultural Properties, identifying Intangible Cultural Properties, selecting master individual holders, documentation requirements, rigorous multi-year apprentice training, and inspiring UNESCO's global heritage charters.",
                "reason": "The world's most successful and admired institutional framework for preserving endangered human craftsmanship."
            },
            {
                "id": 19,
                "title": "The Global Disappearance of Master Crafts: The Looming Crisis of the Uninherited Workshop",
                "tier": "Tier 4: Endangered Crafts & Living Treasures",
                "angle": "endangered_crafts",
                "slug": "endangered_crafts_crisis_red_list_of_endangered_crafts_uninherited_workshops",
                "question": "Why are wooden clogs, hand-forged scythes, horse collar making, and copper distilling pots officially listed as 'critically endangered' with fewer than 5 masters left alive?",
                "key_focus": "Heritage Crafts Association Red List, the economic collapse of manual apprenticeships in the face of plastic imports, aging master demographics (average age over 65), the loss of physical muscle memory, and the urgent documentation race.",
                "reason": "An urgent, poignant investigative call to action exploring the tragic extinction of irreplaceable human knowledge."
            },
            {
                "id": 20,
                "title": "The Modern Handmade Renaissance: Why the Digital World Is Starving for Tactile Craft",
                "tier": "Tier 4: Endangered Crafts & Living Treasures",
                "angle": "future_horizons",
                "slug": "handmade_renaissance_digital_burnout_asmr_slow_craft_return_to_making",
                "question": "In a world of generative AI and sterile touchscreens, why are millions of young people flocking to pottery wheels, wood carving, and blacksmithing for mental sanity?",
                "key_focus": "Matthew Crawford's 'Shop Class as Soulcraft', neurobiology of tactile hand-brain feedback loops (proprioception and dopamine), ASMR craft YouTube channels pulling billions of views, luxury consumers rejecting mass factory sameness, and the triumphant future of the human handmade mark.",
                "reason": "Capstones the master curriculum with an inspiring, empowering vision: the irreplaceable soul of human craftsmanship in an automated world."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why Japanese Chisel Planes Cost $5,000: The Blacksmith Who Forges Paper-Thin Wood Ribbons",
                "tier": "Trending / High Retention",
                "angle": "extreme_craftsmanship",
                "slug": "japanese_kanna_plane_kezuroukai_competition_3_micron_wood_shavings",
                "trend_score": 98,
                "why_trending": "Viral Kezuroukai competition clips showing master carpenters shaving 3-micron transparent wood ribbons thinner than a human cell from cedar beams.",
                "reason": "Hypnotic visual perfectionism that leaves viewers stunned by manual sharpening and planing mastery.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 22,
                "title": "The Real Reason Kintsugi Takes 3 Months: Toxic Urushi Lacquer vs. Fake Epoxy Glue Hacks",
                "tier": "Trending / High Retention",
                "angle": "authenticity_debunk",
                "slug": "real_kintsugi_vs_fake_epoxy_gold_powder_toxic_urushi_three_months",
                "trend_score": 97,
                "why_trending": "Viral craft exposés warning viewers against $20 Amazon 'Kintsugi kits' containing toxic chemical epoxy glue that releases poison into hot tea, contrasting with real authentic Urushi.",
                "reason": "High-retention educational guide protecting consumer safety while celebrating authentic Japanese lacquer technique.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 23,
                "title": "Primitive Technology: Building a Complete Tiled-Roof Mud Brick Hut by Hand in the Woods",
                "tier": "Trending / High Retention",
                "angle": "primitive_bushcraft",
                "slug": "primitive_technology_tiled_roof_hut_charcoal_kiln_mud_bricks_silent_craft",
                "trend_score": 98,
                "why_trending": "John Plant's iconic 'Primitive Technology' YouTube channel commands hundreds of millions of views with zero speech, relying entirely on natural sound and raw stone-age craft.",
                "reason": "Pure mesmerizing ASMR satisfaction demonstrating what one human can build from soil, clay, fire, and stone.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 24,
                "title": "Why Forged Damascus Steel Knives Are Fake: Pattern Welding vs. Lost Crucible Wootz",
                "tier": "Trending / High Retention",
                "angle": "metallurgy_debunk",
                "slug": "damascus_steel_myth_modern_pattern_welding_vs_ancient_wootz_carbon_nanotubes",
                "trend_score": 96,
                "why_trending": "Enormous bladesmithing and knife community debate exposing that 99% of modern 'Damascus' knives are simply folded mild steels etched in acid—not ancient Indian Wootz steel.",
                "reason": "Fascinating historical forensics explaining carbon nanotubes discovered in 1,000-year-old ancient Damascus blades.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 25,
                "title": "The Swedish Spoon Carving Craze: Why Everyone Is Obsessed with the Mora 106 Knife",
                "tier": "Trending / High Retention",
                "angle": "craft_tools_cult",
                "slug": "swedish_spoon_carving_sloyd_tradition_mora_106_carving_knife_slöjd",
                "trend_score": 95,
                "why_trending": "Surge in popularity of Swedish 'Slöjd' educational handcraft, with millions of beginner carvers buying $20 laminated Swedish Mora carbon steel carving knives.",
                "reason": "Accessible, peaceful hobby that brings tactile woodworking into city apartments without power tools.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 26,
                "title": "The $10,000 Panama Hat Scam: Why Real Montecristi Hats Take 6 Months to Weave Under Moonlight",
                "tier": "Trending / High Retention",
                "angle": "luxury_craft_scams",
                "slug": "panama_hat_montecristi_ecuador_toquilla_palm_superfino_master_weavers",
                "trend_score": 97,
                "why_trending": "Shocking investigation showing 'Panama' hats are actually woven from Toquilla palm in Ecuador, where elderly master weavers work in high humidity at dawn to weave hats so fine they hold water.",
                "reason": "Captivating clash of tourist scams, Ecuadorian indigenous mastery, and million-dollar luxury menswear accessories.",
                "status": "READY FOR VIRAL EXPANSION"
            },
            {
                "id": 27,
                "title": "Why Handcrafted Goods Cost 'Too Much': The Math of 100 Hours vs. Fast Factory Junk",
                "tier": "Trending / High Retention",
                "angle": "craft_economics",
                "slug": "why_handcrafted_goods_cost_so_much_living_wage_math_artisans_vs_factories",
                "trend_score": 98,
                "why_trending": "Artisan creators going viral defending their $300 hand-turned bowls and $800 handwoven blankets against online commenters saying 'I can buy that at Target for $10'.",
                "reason": "High-empathy, relatable economic breakdown explaining hourly living wages, material sourcing, tool upkeep, and generational heritage value.",
                "status": "READY FOR VIRAL EXPANSION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 091-095...")
    for folder_name, meta in BATCH_091_095.items():
        process_niche(folder_name, meta)
    update_master_readme()
    print("Batch 091-095 complete!")

if __name__ == "__main__":
    main()
