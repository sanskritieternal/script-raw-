import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_201_205 = {
    "201_flowers": {
        "id": "201",
        "slug": "flowers",
        "title": "Flowers",
        "category": "Life_Biology",
        "audience": "Floriculturists, Botanical Enthusiasts, Plant Geneticists, Perfumers, Nature Documentary Viewers (Global)",
        "progression": [
            ("Tier 1: Floral Anatomy & The Angiosperm Revolution: Petals, Sepals, Pistil, Stamen & Pollination Biology (Beginner / Scratch)",
             "Floral morphology, angiosperm evolutionary explosion in the Cretaceous, the ABC model of floral organ development, pollination syndromes, and nectar biochemistry."),
            ("Tier 2: Floral Pigmentation, Scents & Deceptive Traps: Anthocyanins, Carotenoids, Terpenes & Sexual Deception (Intermediate)",
             "Biochemistry of floral colors, volatile scent release mechanisms, pseudocopulation and sexual deception in orchids, thermogenic snow-melting flowers, and herbarium pressing techniques."),
            ("Tier 3: Extreme & Rare Blooms: Rafflesia, Kadupul, Corpse Flowers & High-Altitude Alpine Blossoms (Upper Intermediate)",
             "Record-breaking floral wonders (Rafflesia, titan arum, night-blooming cereus), high-altitude Himalayan cushion flowers, desert superblooms from ancient seedbanks, and fragile ephemerals."),
            ("Tier 4: Global Floriculture, Cultural History & Biotechnology: The Dutch Tulip Mania, Blue Roses & Scent Synthesis (Advanced / Masterclass)",
             "Economic floral history (1637 Dutch Tulip Mania), CRISPR genetic engineering of true blue roses, the Dutch Aalsmeer cold-chain flower auction, saffron harvesting, and urban pollinator highways.")
        ],
        "flagship": {
            "title": "The Evolutionary Explosion: How Flowers Conquered the Cretaceous World",
            "angle": "historical_evolution",
            "slug": "201_flowers_historical_evolution_the_evolutionary_explosion"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Evolutionary Explosion: How Flowers Conquered the Cretaceous World",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "evolutionary_explosion_how_flowers_conquered_cretaceous_world",
                "question": "How did the sudden appearance and lightning radiation of flowering plants 130 million years ago completely transform Earth's land ecosystems?",
                "focus": "Darwin's 'abominable mystery', angiosperm co-evolution with insect pollinators, rapid seed production, enclosed carpels protecting ovules, and replacing gymnosperm fern forests.",
                "reason": "The quintessential floral masterclass establishing the macro-evolutionary revolution of flowering plants."
            },
            {
                "id": 2,
                "title": "Floral Anatomy 101: The Reproductive Engine of Pistils, Stamens, and Ovaries",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "floral_anatomy_101_reproductive_engine_pistils_stamens",
                "question": "How do sepals, petals, stamens, and carpels coordinate fertilization, double fertilization, and fruit formation?",
                "focus": "Four concentric whorls (calyx, corolla, androecium, gynoecium), pollen tube growth down the style, double fertilization creating embryo and triploid endosperm, and ovary swellings.",
                "reason": "Establishes the foundational biological and structural blueprint of angiosperm flowers."
            },
            {
                "id": 3,
                "title": "The ABC Model of Flower Development: Homeotic Genes Dictating Floral Architecture",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "abc_model_flower_development_homeotic_genes_mads_box",
                "question": "How do three simple classes of MADS-box homeotic genes dictate whether a plant cell becomes a green sepal, colored petal, or seed-bearing carpel?",
                "focus": "The Coen and Meyerowitz ABC/ABCDE genetic model, combinatorial transcription factors, mutant phenotypes (e.g. double-flowered mutant roses), and developmental gene switches.",
                "reason": "Technical deep dive into the genetic and molecular developmental programming of flowers."
            },
            {
                "id": 4,
                "title": "Pollination Syndromes: How Flower Shapes Target Specific Bees, Moths, Birds, and Bats",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "pollination_syndromes_how_flower_shapes_target_pollinators",
                "question": "Why are hummingbird flowers tubular and bright red without scent, while bat flowers are dull white, musky, and bell-shaped?",
                "focus": "Morphological co-adaptation suites: bee flowers (blue/yellow, landing pads, UV nectar guides), hawkmoth flowers (long spurs, sweet evening scents), and fly flowers (carrion colors).",
                "reason": "Foundational ecological guide explaining why wild flowers exhibit such dizzying variations in form and color."
            },
            {
                "id": 5,
                "title": "Nectar Chemistry: Sugars, Amino Acids, and Caffeine Addiction in Pollinators",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "scientific_phenomenon",
                "slug": "nectar_chemistry_sugars_amino_acids_caffeine_addiction",
                "question": "Why do citrus and coffee flowers spike their floral nectar with precise doses of psychoactive caffeine and nicotine?",
                "focus": "Sucrose vs glucose/fructose ratios, essential amino acids, secondary metabolites acting as neurological memory enhancers, ensuring pollinator floral fidelity, and toxic nectar defenses.",
                "reason": "Reveals the sophisticated chemical pharmacology and behavioral manipulation operating in floral rewards."
            },
            {
                "id": 6,
                "title": "The Biochemistry of Floral Color: Anthocyanins, Betalains, and Carotenoid Optics",
                "tier": "Tier 2: Floral Pigmentation & Scents",
                "angle": "materials_science",
                "slug": "biochemistry_of_floral_color_anthocyanins_carotenoids_optics",
                "question": "How do vacuolar pH shifts and metallic co-pigments turn identical anthocyanin pigments from fiery red to deep royal blue?",
                "focus": "Water-soluble anthocyanins, lipid-soluble yellow/orange carotenoids, unique betalains in cacti/beets, epidermal cell lens shapes focusing sunlight, and structural iridescence.",
                "reason": "Masterclass in organic chemistry and optical physics creating the brilliant rainbow palette of blooms."
            },
            {
                "id": 7,
                "title": "Floral Perfume Laboratories: Monoterpenes, Esters, and Night-Blooming Scent Release",
                "tier": "Tier 2: Floral Pigmentation & Scents",
                "angle": "sensory_science",
                "slug": "floral_perfume_laboratories_monoterpenes_esters_night_scents",
                "question": "How do jasmine and night-blooming tuberose synchronize their enzymatic synthesis to pump out intoxicating fragrances precisely after sunset?",
                "focus": "Linalool, geraniol, benzyl acetate, and indole volatility, circadian clock control of scent synthase enzymes, osmophores (scent glands), and the extraction of floral absolutes in luxury perfumery.",
                "reason": "Fascinating examination of plant biochemistry, circadian timing, and sensory perfume engineering."
            },
            {
                "id": 8,
                "title": "Sexual Deception in Orchids: Ophrys Flowers Mimicking Female Wasps in Shape and Pheromones",
                "tier": "Tier 2: Floral Pigmentation & Scents",
                "angle": "evolutionary_science",
                "slug": "sexual_deception_in_orchids_ophrys_pseudocopulation_wasps",
                "question": "How does a Mediterranean bee orchid synthesize the exact multi-chemical sex pheromone of a female solitary wasp to trick males into mating with petals?",
                "focus": "Pseudocopulation mechanism, hydrocarbon cuticular wax mimicking female insect scents, velvety hairy labellum matching female posture, glueing pollinia onto frustrated male heads, and evolutionary arms races.",
                "reason": "The most extreme and bizarre evolutionary example of sexual deception and morphological mimicry in plants."
            },
            {
                "id": 9,
                "title": "Heat-Generating Flowers: Sacred Lotus and Skunk Cabbage Melting Snow via Thermogenesis",
                "tier": "Tier 2: Floral Pigmentation & Scents",
                "angle": "extreme_scenarios",
                "slug": "heat_generating_flowers_sacred_lotus_skunk_cabbage_thermogenesis",
                "question": "How can eastern skunk cabbage burn stored starches to maintain a toasty 70°F inside its spathe, melting through 6 inches of frozen winter snow?",
                "focus": "Alternative Oxidase (AOX) respiratory pathway in mitochondria bypassing ATP synthesis to generate pure heat, volatilizing skunky scents in freezing air, and providing warm motels for pollinators.",
                "reason": "Mind-bending physiological marvel demonstrating that flowers can function as warm-blooded furnaces."
            },
            {
                "id": 10,
                "title": "Flower Pressing and Herbaria: Preserving Centuries of Botanical Holotypes for DNA",
                "tier": "Tier 2: Floral Pigmentation & Scents",
                "angle": "process_walkthrough",
                "slug": "flower_pressing_herbaria_preserving_botanical_holotypes_dna",
                "question": "How do 300-year-old dried pressed flowers inside Kew Gardens still yield intact genomic DNA and historical climate data?",
                "focus": "Cardboard and blotter paper wooden plant presses, archival 100% rag mounting paper, Linnaean holotype specimens, recovering historic stomatal density, and herbarium digitizing protocols.",
                "reason": "Celebrates the rigorous historical craftsmanship and vital scientific archival value of natural history herbaria."
            },
            {
                "id": 11,
                "title": "Rafflesia Arnoldii: The World's Largest Individual Flower, Zero Leaves, and Parasitic Roots",
                "tier": "Tier 3: Extreme & Rare Blooms",
                "angle": "natural_marvels",
                "slug": "rafflesia_arnoldii_worlds_largest_flower_zero_leaves_parasite",
                "question": "How does a 3-foot wide, 20-pound monster bloom erupt from the jungle floor without possessing any roots, stems, leaves, or chlorophyll?",
                "focus": "Endoparasitic lifestyle inside Tetrastigma jungle vines, horizontal gene transfer from host to parasite, rotting meat thermogenic odor, single 5-day bloom lifecycle, and conservation in Borneo.",
                "reason": "Spectacular examination of the largest, weirdest, and most elusive parasitic flower on planet Earth."
            },
            {
                "id": 12,
                "title": "The Kadupul Flower: The Mythical 'Queen of the Night' Blooming for Only Two Hours",
                "tier": "Tier 3: Extreme & Rare Blooms",
                "angle": "mystery_unsolved",
                "slug": "kadupul_flower_queen_of_night_blooming_two_hours_sri_lanka",
                "question": "Why is Sri Lanka's sacred Kadupul cactus bloom considered priceless, withering away before dawn and unable to be bought or sold?",
                "focus": "Epiphyllum oxypetalum ecology, blooming exclusively around midnight once a year, ethereal white multi-petaled architecture, intoxicating fleeting fragrance, and cultural reverence.",
                "reason": "Poetic, mesmerizing look at one of the rarest and most spiritually celebrated botanical events."
            },
            {
                "id": 13,
                "title": "High-Alpine Snow Blooms: Cushion Plants and Woolly Flowers Surviving Himalayan Blizzards",
                "tier": "Tier 3: Extreme & Rare Blooms",
                "angle": "extreme_scenarios",
                "slug": "high_alpine_snow_blooms_cushion_plants_woolly_himalayan_flowers",
                "question": "How do delicate edelweiss and Saussurea woolly snow lotuses bloom at 18,000 feet amid hurricane gales, freezing hail, and scorching UV rays?",
                "focus": "Dense woolly pubescence acting as greenhouse insulation and UV sunscreen, compact aerodynamic cushion morphology trapping warm micro-air, antifreeze glycoproteins, and rapid seed setting.",
                "reason": "Thrilling botanical journey into the extreme high-altitude limits of plant life."
            },
            {
                "id": 14,
                "title": "Desert Ephemerals: How Superblooms Erupt from Decades-Old Seed Banks After Flash Floods",
                "tier": "Tier 3: Extreme & Rare Blooms",
                "angle": "ecological_keystone",
                "slug": "desert_ephemerals_superblooms_decades_old_seed_banks",
                "question": "What chemical washes off ancient seeds in Death Valley to carpet hundreds of square miles of cracked salt flats in golden yellow blooms within days?",
                "focus": "Desert seed dormancy, chemical germination inhibitors (abscisic acid) washed away only by prolonged soaking rains, rapid 3-week life cycles, and satellite visibility of mega-blooms.",
                "reason": "Awe-inspiring showcase of nature's patience and the explosive regenerative power of desert seedbanks."
            },
            {
                "id": 15,
                "title": "The Night-Blooming Cereus: Desert Cacti Syncing Midnight Pollination with Hawk Moths",
                "tier": "Tier 3: Extreme & Rare Blooms",
                "angle": "field_guide",
                "slug": "night_blooming_cereus_desert_cacti_midnight_pollination_moths",
                "question": "How do spindly, dead-looking desert bushes synchronize across the Sonoran desert to open massive 8-inch luminous blooms on a single summer night?",
                "focus": "Peniocereus greggii massive subterranean turnip tuber storage, Sphinx hawk moth long proboscis co-evolution, bats feeding on nectar, and morning floral wilting.",
                "reason": "Captivating look at the nocturnal synchrony of the American desert wilderness."
            },
            {
                "id": 16,
                "title": "Tulip Mania 1637: The Mosaic Virus, Striped Petals, and History's First Economic Bubble",
                "tier": "Tier 4: Global Floriculture, History & Biotech",
                "angle": "historical_moment",
                "slug": "tulip_mania_1637_mosaic_virus_striped_petals_first_bubble",
                "question": "How did a viral plant infection that created fiery red-and-white feathered tulip petals cause single bulbs to trade for the price of grand Amsterdam mansions?",
                "focus": "The Tulip Breaking Virus (potyvirus) suppressing anthocyanin in stripes, Semper Augustus speculative contracts, the sudden February 1637 market crash, and early capitalism's obsession with floral rarity.",
                "reason": "The legendary historical intersection of plant virology, botanical art, and global economic history."
            },
            {
                "id": 17,
                "title": "The Quest for the True Blue Rose: Delphinidin Gene Editing and Synthetic Pathways",
                "tier": "Tier 4: Global Floriculture, History & Biotech",
                "angle": "biotechnology",
                "slug": "quest_for_true_blue_rose_delphinidin_gene_editing_biotech",
                "question": "Why has breeding a blue rose been considered biologically impossible for centuries, and how did CRISPR and pansy genes finally unlock it?",
                "focus": "Roses lacking the flavonoid 3',5'-hydroxylase enzyme, cloning delphinidin pigment genes from pansies and irises, balancing acidic vacuolar pH to prevent purple fading, and commercial release.",
                "reason": "Fascinating biotechnology investigation into solving horticulture's most elusive Holy Grail."
            },
            {
                "id": 18,
                "title": "The Modern Floriculture Highway: Aalsmeer Flower Auction and Cold-Chain Logistics",
                "tier": "Tier 4: Global Floriculture, History & Biotech",
                "angle": "industry_secrets",
                "slug": "modern_floriculture_highway_aalsmeer_flower_auction_cold_chain",
                "question": "How do roses cut on the equator in Kenya and Colombia reach Manhattan florist vases within 48 hours without a single petal dropping?",
                "focus": "Royal FloraHolland in Aalsmeer, reverse Dutch auction clocks, refrigerated Boeing 777 freighter charters, ethylene gas inhibitor treatments, and the massive carbon footprint of global cut flowers.",
                "reason": "Eye-opening look behind the scenes of the $35-billion global industrial floriculture supply chain."
            },
            {
                "id": 19,
                "title": "Edible and Medicinal Blossoms: Saffron Stigmas, Calendula, and Ancient Floral Gastronomy",
                "tier": "Tier 4: Global Floriculture, History & Biotech",
                "angle": "cultural_history",
                "slug": "edible_and_medicinal_blossoms_saffron_stigmas_calendula",
                "question": "Why does harvesting the crimson stigmas of 75,000 Crocus flowers by hand produce only one single pound of saffron spice?",
                "focus": "Crocus sativus triploid sterile genetics, crocin and safranal biochemistry, edible nasturtiums and borage, marigold lutein vision health, and traditional Roman and Persian floral feasts.",
                "reason": "Rich cultural and culinary exploration of the flowers humans cultivate for medicine and high dining."
            },
            {
                "id": 20,
                "title": "Urban Floral Corridors: Restoring Native Wildflower Highways for Endangered Pollinators",
                "tier": "Tier 4: Global Floriculture, History & Biotech",
                "angle": "conservation_action",
                "slug": "urban_floral_corridors_restoring_native_wildflower_highways",
                "question": "How can converting highway median grass and city lawns into native wildflower strips rescue collapsing wild bee and monarch butterfly migrations?",
                "focus": "Replacing sterile manicured turf with native milkweed and nectar perennials, B-Lines pollination corridors in the UK, seed bomb guerilla gardening, and urban biodiversity restoration.",
                "reason": "Empowering, forward-looking capstone showing how floral conservation directly preserves animal biodiversity."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Blue Roses Created by CRISPR: Japanese and Australian Geneticists Cracking True Blue",
                "trend_score": 96,
                "angle": "consumer_biotech",
                "slug": "blue_roses_created_by_crispr_geneticists_cracking_true_blue",
                "why_trending": "Massive ongoing fascination with genetic engineering breakthroughs producing previously impossible blue and purple pigment pathways.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "The 100-Year Century Plant Bloom: Agave Americana's Fatal 30-Foot Inflorescence",
                "trend_score": 95,
                "angle": "viral_nature",
                "slug": "100_year_century_plant_bloom_agave_americana_monocarpic_death",
                "why_trending": "Viral neighborhood spectacles tracking 30-foot asparagus-like stalks growing a foot a day before the plant dies in a final blaze of glory.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Aalsmeer Flower Auction: Inside the Building the Size of 200 Football Fields",
                "trend_score": 93,
                "angle": "industry_secrets",
                "slug": "aalsmeer_flower_auction_inside_building_200_football_fields",
                "why_trending": "Fascinating logistics documentaries exploring automated electric trains and millions of cut flowers traded in seconds at the world's floral capital.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Ghost Orchids of the Everglades: Poaching, Conservation, and Stalking Dendrophylax",
                "trend_score": 94,
                "angle": "investigative",
                "slug": "ghost_orchids_everglades_poaching_conservation_stalking",
                "why_trending": "Perennial intrigue inspired by Susan Orlean's The Orchid Thief following swamp biologists guarding endangered leafless root orchids.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Superbloom Crowds in Death Valley: Satellite Imagery Tracking Millions of Gold Poppies",
                "trend_score": 92,
                "angle": "natural_wonder",
                "slug": "superbloom_crowds_death_valley_satellite_imagery_gold_poppies",
                "why_trending": "Surging viral travel interest every time rare winter rains transform brown national park desert canyons into bright yellow carpets.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Saffron Harvesting: Why the Red Threads of Crocus Sativus Cost $5,000 per Pound",
                "trend_score": 95,
                "angle": "artisanal_food",
                "slug": "saffron_harvesting_why_red_threads_cost_5000_per_pound",
                "why_trending": "High-retention artisanal process videos showing dawn harvests in Kashmir and Iran plucking delicate red stigmas one by one.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Corpse Flower Midnight Live Streams: Tens of Thousands Watching Titan Arum Blooms",
                "trend_score": 91,
                "angle": "viral_event",
                "slug": "corpse_flower_midnight_livestreams_thousands_watching_titan_arum",
                "why_trending": "Botanical gardens drawing hundreds of thousands of concurrent YouTube livestream viewers awaiting the rare 24-hour bloom of Amorphophallus titanum.",
                "status": "Queued"
            }
        ]
    },
    "202_trees": {
        "id": "202",
        "slug": "trees",
        "title": "Trees",
        "category": "Life_Biology",
        "audience": "Dendrologists, Foresters, Arborists, Climate Scientists, Timber Engineers, Nature Lovers (Global)",
        "progression": [
            ("Tier 1: Dendrological Foundations: Wood Anatomy (Heartwood, Sapwood, Cambium), Bark Defense & Tree Ring Growth (Beginner / Scratch)",
             "Xylem and phloem cellular anatomy, vascular cambium secondary growth, tree ring climate proxies (dendrochronology), suberized bark defense, and hardwood vs softwood taxonomy."),
            ("Tier 2: The Hydraulic & Mechanical Limits of Trees: Redwoods at 380 Feet, Wind Shear Dampening & Root Anchorage (Intermediate)",
             "The 426-foot hydraulic cavitation ceiling, coast redwood fog foliar absorption, buttress root mechanics resisting hurricane torque, autumn pigment chemistry, and canopy epiphytes."),
            ("Tier 3: Ancient Immortals & Extreme Forests: Methuselah Bristlecone Pines, Pando Aspen Clones & Taiga Permafrost (Upper Intermediate)",
             "Ancient dendrology: 4,800-year-old White Mountain bristlecones, the 6,000-ton Pando clonal aspen organism, the circum-polar boreal taiga, baobab water storage, and mangrove salt exclusion."),
            ("Tier 4: Global Forest Ecology, Carbon Cycles & Mega-Deforestation: Old-Growth Canopies, Fire Ecology & Assisted Migration (Advanced / Masterclass)",
             "Amazon flying rivers and precipitation engines, natural old-growth vs flammable timber monocultures, urban forestry microclimates, carbon credit forestry critiques, and assisted tree migration.")
        ],
        "flagship": {
            "title": "The Hydraulic Ceiling: Why Trees Cannot Grow Taller Than 426 Feet",
            "angle": "deep_dive",
            "slug": "202_trees_deep_dive_the_hydraulic_ceiling"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Hydraulic Ceiling: Why Trees Cannot Grow Taller Than 426 Feet",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "hydraulic_ceiling_why_trees_cannot_grow_taller_than_426_feet",
                "question": "What fundamental physical and biological limits prevent even the mightiest giant redwoods from growing 500 feet into the air?",
                "focus": "Xylem water tension pulling against gravity, embolism and cavitation bubble risks at negative 2.0 MPa pressure, leaf turgor pressure drop, and stomatal shutdown at the tree crown.",
                "reason": "The quintessential dendrological masterclass deconstructing the physical limits of living architecture."
            },
            {
                "id": 2,
                "title": "Wood Anatomy: The Vascular Architecture of Xylem Vessels, Tracheids, and Heartwood",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "wood_anatomy_vascular_architecture_xylem_tracheids_heartwood",
                "question": "How does living vascular sapwood transform into dead, rock-hard heartwood packed with antimicrobial tannins to support massive trunks?",
                "focus": "Lignified cellulose cell walls, wide vessel elements in hardwoods vs narrow safety-valved tracheids in conifers, vascular rays transporting nutrients horizontally, and tyloses plugging old pipes.",
                "reason": "Establishes the anatomical, structural, and chemical baseline of wood formation."
            },
            {
                "id": 3,
                "title": "The Bark Armor: Cork Cambium, Suberin Wax, and Defending Against Insect Borers",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biological_guide",
                "slug": "bark_armor_cork_cambium_suberin_wax_defending_borers",
                "question": "How does a tree continuously expand its waterproof, fire-resistant outer armor without splitting its own living tissues?",
                "focus": "Phellogen (cork cambium) producing dead phellem cells saturated with suberin wax, lenticels allowing gas exchange through bark, resin canals pitching out bark beetles, and rhytidome shedding.",
                "reason": "Examines the resilient external defense system protecting trees from weather, fire, and pathogens."
            },
            {
                "id": 4,
                "title": "Dendrochronology: Reading Droughts, Volcanic Eruptions, and Sunspots in Rings",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "scientific_phenomenon",
                "slug": "dendrochronology_reading_droughts_volcanoes_sunspots_rings",
                "question": "How do climate scientists match overlapping tree ring patterns across thousands of years to reconstruct Earth's temperature history to the exact year?",
                "focus": "A.E. Douglass and cross-dating principles, earlywood spring growth vs dense latewood autumn bands, frost rings matching distant supervolcanoes (e.g. 1815 Tambora), and carbon-14 spikes.",
                "reason": "Fascinating examination of how trees serve as living, high-resolution historical libraries."
            },
            {
                "id": 5,
                "title": "Gymnosperms vs Angiosperms: Hardwoods vs Softwoods, Deciduous Abscission, and Evergreens",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "gymnosperms_vs_angiosperms_hardwoods_vs_softwoods_abscission",
                "question": "Why is balsa wood biologically a 'hardwood' while dense Douglas fir is a 'softwood', and why do broadleaf trees drop their leaves?",
                "focus": "Angiosperm vessel elements defining hardwoods vs gymnosperm naked tracheids defining softwoods, deciduous leaf abscission layer formation to prevent winter water loss, and evergreen needle waxy cones.",
                "reason": "Clarifies the fundamental taxonomic division of the world's commercial and wild forest trees."
            },
            {
                "id": 6,
                "title": "Coast Redwoods and Giant Sequoias: Fog Absorption and Fire Resistance",
                "tier": "Tier 2: Hydraulic & Mechanical Limits",
                "angle": "extreme_scenarios",
                "slug": "coast_redwoods_giant_sequoias_fog_absorption_fire_resistance",
                "question": "How do 300-foot coastal redwoods drink hundreds of gallons of water directly through their leaves from Pacific summer fog?",
                "focus": "Foliar water uptake bypassing roots, 2-foot-thick fire-resistant spongy fibrous bark lacking volatile pitch, serotinous sequoia cones, and Hyperion's sheltered canyon microclimate.",
                "reason": "Celebrates the towering giants of California and their incredible adaptations to fog and wildfire."
            },
            {
                "id": 7,
                "title": "Root Biomechanics: Taproots, Lateral Buttress Flanges, and Surviving Hurricane Winds",
                "tier": "Tier 2: Hydraulic & Mechanical Limits",
                "angle": "engineering_marvels",
                "slug": "root_biomechanics_taproots_buttress_flanges_hurricane_winds",
                "question": "Why don't 100-ton tropical rainforest trees with shallow 3-foot root systems blow over in 120-MPH cyclonic gales?",
                "focus": "Mechanical buttress flanges acting like architectural cathedral flying buttresses, sinker roots anchoring into soil bedrock, root grafting sharing stability with neighboring trees, and wind-dampening stem flex.",
                "reason": "Masterclass in natural civil engineering and structural stability."
            },
            {
                "id": 8,
                "title": "The Banyan and Strangler Fig: Aerial Prop Roots Smothering Host Trees from Canopies Down",
                "tier": "Tier 2: Hydraulic & Mechanical Limits",
                "angle": "botanical_guide",
                "slug": "banyan_and_strangler_fig_aerial_prop_roots_smothering_hosts",
                "question": "How does a tiny bird seed dropped in a canopy crevice grow a massive web of living roots that completely hollows out and kills a giant host tree?",
                "focus": "Hemiepiphytic lifecycle of Ficus species, aerial roots growing downward toward soil nutrients, root fusion creating an impenetrable lattice trunk, hollow-core living columns, and walking banyan tree groves.",
                "reason": "Gripping look at nature's most ruthless and architecturally astonishing arboreal usurper."
            },
            {
                "id": 9,
                "title": "Deciduous Autumn Colors: Chlorophyll Breakdown Revealing Carotenes and Anthocyanins",
                "tier": "Tier 2: Hydraulic & Mechanical Limits",
                "angle": "natural_marvels",
                "slug": "deciduous_autumn_colors_chlorophyll_breakdown_anthocyanins",
                "question": "Why do deciduous trees spend precious energy synthesizing brand new red anthocyanin pigments just weeks before dropping their leaves?",
                "focus": "Chlorophyll breakdown recovering valuable nitrogen and magnesium into woody stems, unmasking yellow/orange carotenoids, the photo-protection hypothesis of red anthocyanin sunscreens, and autumn tourism.",
                "reason": "Beautiful synthesis of plant physiology, optical beauty, and seasonal ecological strategy."
            },
            {
                "id": 10,
                "title": "Canopy Ecology: The Epiphyte Hanging Gardens Living 300 Feet Above the Forest Floor",
                "tier": "Tier 2: Hydraulic & Mechanical Limits",
                "angle": "field_guide",
                "slug": "canopy_ecology_epiphyte_hanging_gardens_above_forest_floor",
                "question": "What thrives inside the multi-ton hanging soil mats that form along redwood and tropical tree limbs hundreds of feet in the air?",
                "focus": "Canopy soil accumulation from decaying needles and moss, salamanders and endemic ferns living their entire lives in the sky without touching ground, and specialized canopy research climbing techniques.",
                "reason": "Explores the lush, newly discovered 'eighth continent' of life perched atop giant tree canopies."
            },
            {
                "id": 11,
                "title": "Methuselah and the Bristlecone Pines: Surviving 4,800 Years on High Dolomite Ridges",
                "tier": "Tier 3: Ancient Immortals & Extreme Forests",
                "angle": "prehistoric_deep_dive",
                "slug": "methuselah_bristlecone_pines_surviving_4800_years_dolomite",
                "question": "How do gnarled, mostly-dead Pinus longaeva trees survive 5,000 continuous years of freezing gale-force blizzards in California's White Mountains?",
                "focus": "Dense resinous wood impervious to fungi and insect rot, alkaline dolomite nutrient-poor soil deterring competitors and wild grass fires, strip-barking survival (one thin strip of living cambium nourishing one branch).",
                "reason": "Awe-inspiring profile of the oldest non-clonal individual trees on planet Earth."
            },
            {
                "id": 12,
                "title": "Pando the Trembling Giant: A Single 40,000-Year-Old Quaking Aspen Clone Weighing 6,000 Tons",
                "tier": "Tier 3: Ancient Immortals & Extreme Forests",
                "angle": "case_study",
                "slug": "pando_trembling_giant_40000_year_old_aspen_clone_utah",
                "question": "How is an entire forest of 47,000 genetically identical white-barked trees in Utah actually a single colossal living organism connected underground?",
                "focus": "Populus tremuloides clonal root suckering, interconnected root system sharing water and nutrients across 106 acres, triploid genetic longevity, and modern threats from overgrazing mule deer.",
                "reason": "Fascinating examination of clonal immortality and one of the heaviest living organisms on Earth."
            },
            {
                "id": 13,
                "title": "The Taiga Boreal Forest: The Largest Terrestrial Biome Encircling the Arctic",
                "tier": "Tier 3: Ancient Immortals & Extreme Forests",
                "angle": "ecological_keystone",
                "slug": "taiga_boreal_forest_largest_terrestrial_biome_arctic_ring",
                "question": "Why does a freezing coniferous forest stretching across Siberia, Scandinavia, and Canada hold more carbon in its permafrost soils than all tropical rainforests combined?",
                "focus": "Conical tree architecture shedding heavy snow loads without snapping branches, dark green needles absorbing low winter sun, acidic peatlands storing massive carbon reserves, and thawing permafrost risks.",
                "reason": "Essential ecological profile of the vast northern forest belt that regulates global climate."
            },
            {
                "id": 14,
                "title": "African Baobabs: Living Water Storage Towers, Hollow Trunks, and Radiocarbon Enigmas",
                "tier": "Tier 3: Ancient Immortals & Extreme Forests",
                "angle": "bizarre_trees",
                "slug": "african_baobabs_living_water_towers_hollow_trunks_radiocarbon",
                "question": "How does an Adansonia baobab tree store up to 30,000 gallons of water inside a swollen, spongy trunk to survive years of brutal drought?",
                "focus": "Multiple fused stem stems creating false hollow cavities, lack of traditional growth rings, radiocarbon dating showing 2,000+ year lifespans, the African 'Tree of Life' feeding dozens of species, and mysterious recent die-offs.",
                "reason": "Deep dive into one of Africa's most iconic, revered, and structurally unique botanical marvels."
            },
            {
                "id": 15,
                "title": "Mangrove Forests: Salt-Excreting Roots and Pneumatophores Breathing in Tidal Mud",
                "tier": "Tier 3: Ancient Immortals & Extreme Forests",
                "angle": "wetland_biology",
                "slug": "mangrove_forests_salt_excreting_roots_pneumatophores_mud",
                "question": "How do mangrove trees grow directly in suffocating anaerobic ocean mud, drinking pure salt water and surviving storm surges?",
                "focus": "Ultrafiltration membranes in roots excluding 90% of sea salt, salt-excreting leaves, stilt roots and vertical pencil-like pneumatophores with lenticels breathing air at low tide, and coastal tsunami dissipation.",
                "reason": "Incredible demonstration of coastal marine adaptation guarding tropical coastlines."
            },
            {
                "id": 16,
                "title": "The Amazon Rain Engine: How Billions of Trees Create Flying Rivers That Water South America",
                "tier": "Tier 4: Global Ecology & Future Frontiers",
                "angle": "meteorological_science",
                "slug": "amazon_rain_engine_how_trees_create_flying_rivers_south_america",
                "question": "How do 400 billion Amazonian trees pump 20 billion tons of water vapor into the atmosphere every single day, generating their own weather system?",
                "focus": "The Biotic Pump theory, transpirational atmospheric suction drawing moist Atlantic trade winds deep inland, 'flying rivers' carrying more moisture than the Amazon River itself, and tipping points from deforestation.",
                "reason": "Groundbreaking meteorological study showing that forests don't just grow where it rains—forests create the rain."
            },
            {
                "id": 17,
                "title": "Old-Growth Forest vs Monoculture Tree Plantations: Biodiversity, Fungi, and Flammability",
                "tier": "Tier 4: Global Ecology & Future Frontiers",
                "angle": "comparative_analysis",
                "slug": "old_growth_vs_monoculture_plantations_biodiversity_fungi_fire",
                "question": "Why are commercial pine plantations essentially biological deserts that burn like matchsticks compared to resilient ancient forests?",
                "focus": "Structural complexity (snags, fallen nurse logs, multi-tier canopies), intact subterranean mycorrhizal fungal networks, uniform spacing in timber farms fueling explosive wildfires, and real forest ecology.",
                "reason": "Critical comparative analysis exposing the profound difference between natural ecosystems and commercial timber crops."
            },
            {
                "id": 18,
                "title": "Urban Forestry: How Street Trees Cool Cities by 10°F and Mitigate Heat Islands",
                "tier": "Tier 4: Global Ecology & Future Frontiers",
                "angle": "environmental_action",
                "slug": "urban_forestry_how_street_trees_cool_cities_heat_islands",
                "question": "How does planting broadleaf canopy trees along asphalt streets save thousands of human lives during deadly summer heatwaves?",
                "focus": "Evapotranspiration cooling physics (equivalent to running 10 room-sized air conditioners continuously), shading black asphalt and concrete, particulate matter filtration, stormwater absorption, and tree equity.",
                "reason": "Practical, impactful exploration of urban ecology and civil climate adaptation."
            },
            {
                "id": 19,
                "title": "The Carbon Offset Dilemma: Can Massive Reforestation Projects Offset Fossil Emissions?",
                "tier": "Tier 4: Global Ecology & Future Frontiers",
                "angle": "investigative",
                "slug": "carbon_offset_dilemma_can_reforestation_offset_emissions",
                "question": "Are multi-billion dollar corporate tree-planting pledges real climate solutions or greenwashed accounting tricks on vulnerable land?",
                "focus": "Additionality and permanence issues, carbon offset certification scandals, planting wrong species in native grasslands, wildfire reversal risks, and prioritizing protecting existing intact old-growth.",
                "reason": "Hard-hitting investigative analysis addressing modern climate policy and ecological integrity."
            },
            {
                "id": 20,
                "title": "Assisted Tree Migration: Moving Tree Species Northward Ahead of Rapid Climate Shifts",
                "tier": "Tier 4: Global Ecology & Future Frontiers",
                "angle": "future_trends",
                "slug": "assisted_tree_migration_moving_species_northward_climate",
                "question": "When climate zones shift 10 times faster than trees can naturally disperse seeds, should foresters actively plant southern trees hundreds of miles north?",
                "focus": "Assisted population migration vs assisted range expansion, moving Torreya taxifolia and western larch, ecological invasion risks vs preventing catastrophic forest dieback, and 21st-century silviculture.",
                "reason": "Visionary capstone examining the active human stewardship required to preserve global forests in a changing climate."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Hyperion: The Secret Location of the Tallest Living Tree on Earth",
                "trend_score": 97,
                "angle": "viral_mystery",
                "slug": "hyperion_secret_location_tallest_living_tree_on_earth",
                "why_trending": "Massive intrigue and national park controversy after rangers issued $5,000 fines and jail time for hikers trying to visit the 380-foot coast redwood.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Pando Aspen Clone Collapse: How Mule Deer Are Stopping New Shoots in Utah",
                "trend_score": 94,
                "angle": "conservation_crisis",
                "slug": "pando_aspen_clone_collapse_mule_deer_stopping_new_shoots",
                "why_trending": "Ongoing high-profile ecological emergency as fencing and predator reintroduction efforts attempt to save the 106-acre ancient organism.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Bonsai Trees Worth Millions: 500-Year-Old Miniature Pines Surviving Hiroshima",
                "trend_score": 95,
                "angle": "cultural_art",
                "slug": "bonsai_trees_worth_millions_500_year_old_pines_hiroshima",
                "why_trending": "Huge cultural fascination and high view counts following the legendary Yamaki pine that survived the atomic blast and continues to thrive at the US National Arboretum.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "The Manchineel Tree: Why the 'Tree of Death' Blinds Anyone Standing Under It in Rain",
                "trend_score": 96,
                "angle": "thrill_seeker",
                "slug": "manchineel_tree_tree_of_death_blinds_rain_standing",
                "why_trending": "Ultra-viral warning videos covering the Guinness World Record deadliest tree in Florida and the Caribbean whose caustic sap blisters skin and burns eyes.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Mass Timber Skyscrapers: Cross-Laminated Timber (CLT) Replacing Steel and Concrete",
                "trend_score": 93,
                "angle": "tech_disruption",
                "slug": "mass_timber_skyscrapers_clt_replacing_steel_concrete",
                "why_trending": "Major architectural and engineering movement building 25-story carbon-negative high-rises from compressed fire-charring timber panels.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "The Great Green Wall of Africa: 8,000 Kilometers of Trees Halting the Sahara",
                "trend_score": 92,
                "angle": "global_megaproject",
                "slug": "great_green_wall_africa_8000_kilometers_halting_sahara",
                "why_trending": "Inspiring continental-scale reforestation project planting drought-resilient acacia trees across the Sahel to reverse desertification.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Drone Reforestation: Firing Seed Missiles into Deforested Mountain Slopes",
                "trend_score": 91,
                "angle": "innovations",
                "slug": "drone_reforestation_firing_seed_missiles_mountain_slopes",
                "why_trending": "High tech innovation using heavy-lift autonomous drone swarms to plant 40,000 seed pods a day across steep burned hillsides.",
                "status": "Queued"
            }
        ]
    },
    "203_fungi": {
        "id": "203",
        "slug": "fungi",
        "title": "Fungi",
        "category": "Life_Biology",
        "audience": "Mycologists, Mushroom Foragers, Biotech Researchers, Permaculturists, Science Documentary Viewers (Global)",
        "progression": [
            ("Tier 1: Fungal Biology & The Kingdom Fungi: Hyphae, Mycelium Networks, Chitin Walls & Spore Dispersal (Beginner / Scratch)",
             "Fungal cellular anatomy, chitinous cell walls, hyphal tip extension, spore aerodynamics, and the major taxonomic phyla (Basidiomycota, Ascomycota)."),
            ("Tier 2: Fungal Ecology & Biochemical Mastery: Saprophytic Wood Decay (Lignin Digestion), Mycorrhizae & Lichen Symbiosis (Intermediate)",
             "White-rot and brown-rot enzyme systems (the only degraders of lignin), ancient lichen pioneer rock weathering, fairy ring expansion geometry, and foraging safety protocols."),
            ("Tier 3: Extreme & Medicinal Fungi: Cordyceps Parasites, Bioluminescent Armillaria, Chaga, and Penicillin Breakthroughs (Upper Intermediate)",
             "Zombie ant entomopathogenic Ophiocordyceps, the 3.5-square-mile Oregon Humongous Fungus, Alexander Fleming's penicillin revolution, cold foxfire bioluminescence, and ergot poisoning history."),
            ("Tier 4: Myco-Materials, Bioremediation & Fungal Biotechnology: Mycelium Leather, Plastic Eating Fungi & Astromycology (Advanced / Masterclass)",
             "Fungal bioremediation digesting crude oil and plastics, grown mycelium architectural packaging and leather, psilocybin neuroplasticity clinical trials, and radiation-eating Chernobyl fungi.")
        ],
        "flagship": {
            "title": "The Hidden Kingdom: How Mycelial Networks Built the Foundations of Terrestrial Life",
            "angle": "deep_dive",
            "slug": "203_fungi_deep_dive_the_hidden_kingdom"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Hidden Kingdom: How Mycelial Networks Built the Foundations of Terrestrial Life",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "hidden_kingdom_how_mycelial_networks_built_terrestrial_life",
                "question": "How did ancient fungi colonize bare volcanic continents 500 million years ago, paving the way for every plant and animal on Earth?",
                "focus": "Prototaxites (20-foot tall prehistoric fungal spires), symbiotic root partnerships enabling the first aquatic plants to survive dry land, mineral extraction, and the planet's premier recycling system.",
                "reason": "The quintessential mycological masterclass revealing the vital, ancient subterranean foundation of terrestrial life."
            },
            {
                "id": 2,
                "title": "Hyphae and Mycelium: The Microscopic Thread Network Connecting the Forest Floor",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "hyphae_and_mycelium_microscopic_thread_network_forest_floor",
                "question": "How does a microscopic, one-cell-wide filament exert massive hydraulic pressure to punch through solid rock and living wood?",
                "focus": "Hyphal Spitzenkörper vesicle supply center directing tip growth, turgor pressure mechanics, septate vs coenocytic hyphae, external digestive enzyme secretion, and mycelial mats spanning miles.",
                "reason": "Technical breakdown of the fundamental vegetative growth unit of all macroscopic fungi."
            },
            {
                "id": 3,
                "title": "Neither Plant Nor Animal: Why Fungi Are Genetically Closer to Animals Than Plants",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "evolutionary_milestone",
                "slug": "neither_plant_nor_animal_why_fungi_are_genetically_closer",
                "question": "Why did DNA sequencing prove that mushrooms are more closely related to human beings than to the trees they grow on?",
                "focus": "Opisthokont clade evolution, shared chitinous cell structures (matching crab shells, not plant cellulose), glycogen energy storage (not starch), heterotrophic external digestion, and ergosterol cell membranes.",
                "reason": "Shatters common misconceptions and establishes the true evolutionary kinship of the Kingdom Fungi."
            },
            {
                "id": 4,
                "title": "Spore Dispersion Mechanics: Fluid Dynamics, Ballistospores, and Raindrop Splash Cups",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biomechanics",
                "slug": "spore_dispersion_mechanics_ballistospores_raindrop_cups",
                "question": "How do gilled mushrooms launch microscopic spores into the air with 25,000G acceleration using a single droplet of condensed water?",
                "focus": "Buller's drop surface tension catapult mechanism, thermal air drafts generated by evaporating mushroom moisture, puffball bellows physics, bird's nest fungi raindrop splash cups, and trillions of daily spores.",
                "reason": "Fascinating examination of microscopic fluid physics and ballistic biomechanical launching."
            },
            {
                "id": 5,
                "title": "The Major Fungal Phyla: Basidiomycota, Ascomycota, and Glomeromycota",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "major_fungal_phyla_basidiomycota_ascomycota_glomeromycota",
                "question": "How do shelf brackets, morels, single-celled brewer's yeasts, and microscopic root fungi map onto the fungal family tree?",
                "focus": "Basidiomycota (club fungi with basidiospores), Ascomycota (sac fungi including truffles, morels, and Penicillium), Glomeromycota (obligate endomycorrhizal plant symbionts), and sexual vs asexual life cycles.",
                "reason": "Essential taxonomic architecture organizing the diverse fungal kingdom."
            },
            {
                "id": 6,
                "title": "White Rot vs Brown Rot: The Only Organisms Capable of Deconstructing Insoluble Lignin",
                "tier": "Tier 2: Ecology & Biochemical Mastery",
                "angle": "biochemical_breakthrough",
                "slug": "white_rot_vs_brown_rot_deconstructing_insoluble_lignin",
                "question": "Why did the Earth stop forming massive coal beds 300 million years ago when white-rot fungi evolved to digest lignin?",
                "focus": "Lignin peroxidase and laccase free-radical oxidative enzymes bleaching wood white, brown-rot Fenton chemistry digesting cellulose while leaving brown cubical lignin, and ending the Carboniferous coal age.",
                "reason": "Pivotal evolutionary and geological breakthrough showing how fungi fundamentally altered the carbon cycle of Earth."
            },
            {
                "id": 7,
                "title": "Lichens: The Dual Organism Pioneer Species Blending Fungi and Algae on Bare Rock",
                "tier": "Tier 2: Ecology & Biochemical Mastery",
                "angle": "symbiosis_study",
                "slug": "lichens_dual_organism_pioneer_species_fungi_algae_rock",
                "question": "How does an obligate partnership between a fungus and a photosynthetic green alga dissolve bare volcanic rock to create the first soil?",
                "focus": "Mycobiont (fungal structural house) and photobiont (algal sugar factory) mutualism, Beatrix Potter's early lichen research, oxalic acid rock etching, extreme freeze-thaw survival, and bio-indicators of clean air.",
                "reason": "Inspiring study in cooperative symbiosis establishing the bedrock of terrestrial soil creation."
            },
            {
                "id": 8,
                "title": "The Wood Wide Web: Hyphal Carbon Trading, Nutrient Routing, and Soil Aggregation",
                "tier": "Tier 2: Ecology & Biochemical Mastery",
                "angle": "ecological_keystone",
                "slug": "wood_wide_web_hyphal_carbon_trading_glomalin_soil",
                "question": "How do fungal hyphae weave through millions of microscopic soil pores, producing the 'biological glue' that holds the Earth's soil together?",
                "focus": "Glomalin glycoprotein discovery storing 27% of all soil carbon, trading phosphorus and nitrogen for plant carbon, hyphal networks spanning forest stands, and preventing soil erosion.",
                "reason": "Deep dive into the critical underground pedological engineering performed by fungal mycelium."
            },
            {
                "id": 9,
                "title": "Fairy Rings: How Expanding Circular Mycelial Colonies Create Spontaneous Mushroom Rings",
                "tier": "Tier 2: Ecology & Biochemical Mastery",
                "angle": "natural_marvels",
                "slug": "fairy_rings_how_expanding_circular_mycelial_colonies_form",
                "question": "Why do perfect geometric circles of mushrooms sprout overnight in grassy meadows, surrounded by rings of lush dark green grass?",
                "focus": "Centrifugal radial mycelial growth from a central spore, enzymatic nutrient release at the advancing fringe fertilizing grass, central mycelial death creating expanding rings, and folklore myths of dancing fairies.",
                "reason": "Demystifies a famous natural phenomenon with clear ecological and geometrical science."
            },
            {
                "id": 10,
                "title": "Wild Mushroom Identification: Gills, Spore Prints, Volvas, and Deadly Amanita Lookalikes",
                "tier": "Tier 2: Ecology & Biochemical Mastery",
                "angle": "foraging_safety",
                "slug": "wild_mushroom_identification_gills_spore_prints_volvas_amanita",
                "question": "How do experienced foragers distinguish the delicious choice edible Meadow Mushroom from the lethal Death Cap in a few rigorous steps?",
                "focus": "Spore print color techniques on paper, examining subterranean volva cups and stem rings (annulus), free vs attached gills, staining reactions (KOH), and the golden rule: 'When in doubt, throw it out.'",
                "reason": "Indispensable practical field guide emphasizing rigorous safety, botany, and foraging discipline."
            },
            {
                "id": 11,
                "title": "Ophiocordyceps: The Fungal Parasite Hijacking Insect Nervous Systems",
                "tier": "Tier 3: Extreme & Medicinal Fungi",
                "angle": "extreme_scenarios",
                "slug": "ophiocordyceps_fungal_parasite_hijacking_insect_nervous_systems",
                "question": "How does a fungal spore enter an ant's brain, take over its walking motor neurons, and force it to climb a leaf at solar noon to die?",
                "focus": "Ophiocordyceps unilateralis cellular infiltration around muscle fibers (leaving the brain intact while controlling muscles directly), the 'death grip' bite into leaf veins, and fruiting bodies piercing the head.",
                "reason": "The defining real-life biological phenomenon inspiring pop culture zombie epics."
            },
            {
                "id": 12,
                "title": "The Humongous Fungus: A Single 2,400-Acre Armillaria Colony Dominating Oregon",
                "tier": "Tier 3: Extreme & Medicinal Fungi",
                "angle": "case_study",
                "slug": "humongous_fungus_single_2400_acre_armillaria_colony_oregon",
                "question": "How did foresters in Malheur National Forest discover that a root-rot fungus spreading across 3.5 square miles is a single individual organism?",
                "focus": "Armillaria ostoyae (honey mushroom) DNA fingerprinting across miles, black shoestring-like rhizomorph cables subterranean expansion, estimated 8,000-year age, and managing natural forest pathogens.",
                "reason": "Incredible showcase of the largest known living organism on planet Earth."
            },
            {
                "id": 13,
                "title": "The Penicillin Miracle: Alexander Fleming's Mold Contamination Rewriting Medicine",
                "tier": "Tier 3: Extreme & Medicinal Fungi",
                "angle": "historical_moment",
                "slug": "penicillin_miracle_alexander_fleming_mold_rewriting_medicine",
                "question": "How did an unwashed petri dish contaminated by green Penicillium notatum mold save hundreds of millions of human lives from bacterial infection?",
                "focus": "The 1928 St. Mary's Hospital discovery, Florey and Chain's Oxford purification breakthrough, mass-producing penicillin in fermented corn steep liquor for D-Day soldiers, and the dawn of the antibiotic era.",
                "reason": "The landmark medical revolution proving that fungi hold the ultimate chemical weaponry against bacterial pathogens."
            },
            {
                "id": 14,
                "title": "Bioluminescent Mushrooms: Foxfire, Luciferin Chemical Reactions, and Midnight Glow",
                "tier": "Tier 3: Extreme & Medicinal Fungi",
                "angle": "natural_marvels",
                "slug": "bioluminescent_mushrooms_foxfire_luciferin_midnight_glow",
                "question": "Why do over 80 species of forest mushrooms emit an eerie emerald green glow in pitch darkness?",
                "focus": "Hispidin-luciferin chemical pathway, circadian rhythmic light pulsing (glowing brightest at night when spore-dispersing insects are active), ancient Aristotle 'cold fire' observations, and ghost fungus in Australia.",
                "reason": "Magical visual journey into natural bioluminescent biochemistry."
            },
            {
                "id": 15,
                "title": "Ergot and History: The Rye Fungus Causing St. Anthony's Fire and the Salem Witch Trials",
                "tier": "Tier 3: Extreme & Medicinal Fungi",
                "angle": "cultural_history",
                "slug": "ergot_and_history_rye_fungus_st_anthonys_fire_salem_trials",
                "question": "How did Claviceps purpurea fungus growing on damp rye bread trigger medieval mass madness, gangrenous limb loss, and witchcraft accusations?",
                "focus": "Ergot alkaloids (ergotamine, ergometrine) causing intense vasoconstriction and hallucinations, historical epidemics of St. Anthony's Fire, Linnda Caporael's 1976 Salem hypothesis, and Albert Hofmann synthesizing LSD.",
                "reason": "Fascinating historical crossover between agricultural mycology, social hysteria, and neuropharmacology."
            },
            {
                "id": 16,
                "title": "Mycoremediation: Training Fungi to Decompose Crude Oil Spills, Heavy Metals, and Plastics",
                "tier": "Tier 4: Biotech, Materials & Frontiers",
                "angle": "environmental_action",
                "slug": "mycoremediation_training_fungi_decompose_oil_spills_plastics",
                "question": "Can oyster mushroom mycelium really break down carcinogenic petroleum hydrocarbons into non-toxic fungal sugars in 16 weeks?",
                "focus": "Paul Stamets' mycoremediation trials, Pestalotiopsis microspora digesting polyurethane plastics anaerobically, hyperaccumulating radioactive cesium in fruiting bodies, and cleaning contaminated toxic waste sites.",
                "reason": "Frontier environmental biotechnology deploying the earth's natural digestive engine to clean up industrial pollution."
            },
            {
                "id": 17,
                "title": "Mycelium Leather and Packaging: Growing Biodegradable Furniture, Styrofoam, and Shoes",
                "tier": "Tier 4: Biotech, Materials & Frontiers",
                "angle": "materials_science",
                "slug": "mycelium_leather_packaging_growing_biodegradable_products",
                "question": "How are biotechnology startups growing custom luxury leather purses and compostable computer packaging from mushroom roots in seven days?",
                "focus": "Agricultural waste (hemp/sawdust) inoculated with Ganoderma mycelium, baking mycelium foam into rigid insulating blocks, vegan mycelium leather (Mylo) tensile strength, and closing circular manufacturing loops.",
                "reason": "Examines the cutting-edge sustainable biomaterials revolution replacing petroleum plastics with living fungi."
            },
            {
                "id": 18,
                "title": "Psilocybin and Neuroplasticity: The Clinical Renaissance for Depression and Addiction",
                "tier": "Tier 4: Biotech, Materials & Frontiers",
                "angle": "neuroscience_medicine",
                "slug": "psilocybin_neuroplasticity_clinical_renaissance_depression",
                "question": "How does psilocin binding to 5-HT2A serotonin receptors temporarily dissolve the brain's Default Mode Network to rewire chronic mental illness?",
                "focus": "Johns Hopkins and Imperial College London clinical trials, resetting hyperactive rumination loops in treatment-resistant depression, rapid dendritic spine growth, and FDA breakthrough therapy designations.",
                "reason": "Rigorous neuroscientific analysis of the therapeutic revolution unlocking mental health healing from fungal compounds."
            },
            {
                "id": 19,
                "title": "Yeast (Saccharomyces Cerevisiae): The Domesticated Microbe That Built Human Civilization",
                "tier": "Tier 4: Biotech, Materials & Frontiers",
                "angle": "anthropological_history",
                "slug": "yeast_saccharomyces_cerevisiae_domesticated_microbe_civilization",
                "question": "Did humanity abandon nomadic hunter-gatherer life to settle in agricultural villages to farm barley for bread or for fermented beer?",
                "focus": "Anaerobic fermentation producing ethanol and CO2, domesticating wild single-celled fungi 10,000 years ago, brewing and baking history, and modern synthetic biology using yeast to brew insulin and spider silk.",
                "reason": "Appreciative tribute to the microscopic fungal workhorse of human culinary and industrial history."
            },
            {
                "id": 20,
                "title": "Astromycology: Fungi Surviving Cosmic Radiation and Martian Habitat Concepts",
                "tier": "Tier 4: Biotech, Materials & Frontiers",
                "angle": "future_frontiers",
                "slug": "astromycology_fungi_surviving_cosmic_radiation_martian_habitats",
                "question": "Can black fungal melanin absorb lethal space radiation to protect astronauts, and could we 'grow' living base stations on the Moon and Mars?",
                "focus": "Radiotrophic Cryptococcus neoformans thriving inside Chernobyl reactors, NASA Ames research on myco-architecture (growing mycelium bricks with lunar regolith), and testing fungal spores in vacuum.",
                "reason": "Visionary capstone taking the ancient Kingdom of Fungi to the final frontier of human space exploration."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Oregon Humongous Fungus: The Largest Living Organism on Earth Covering 3.5 Square Miles",
                "trend_score": 96,
                "angle": "biological_wonder",
                "slug": "oregon_humongous_fungus_largest_organism_3_point_5_square_miles",
                "why_trending": "Massive ongoing viral curiosity across YouTube and social media exploring the colossal 8,000-year-old subterranean mushroom mat.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Growing Your Own Mushrooms in 14 Days: Grain Spawn, Monotubs, and Lion's Mane",
                "trend_score": 95,
                "angle": "diy_hobby",
                "slug": "growing_mushrooms_in_14_days_grain_spawn_monotubs_lions_mane",
                "why_trending": "Enormous DIY home cultivation boom with millions learning sterile liquid culture, pressure cooking grain jars, and fruiting edible gourmet mushrooms.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Mycelium Bacon and Steaks: Fungal Meat Alternatives Mimicking Muscle Fibers",
                "trend_score": 93,
                "angle": "food_innovation",
                "slug": "mycelium_bacon_steaks_fungal_meat_alternatives_muscle_fibers",
                "why_trending": "Rapid venture funding and grocery retail expansion of whole-cut mycelium meats (Meati, MyForest Foods) offering zero-cholesterol, high-protein steaks.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Death Cap Mushroom Poisoning: Amatoxins Destroying Liver RNA Polymerase in 48 Hours",
                "trend_score": 94,
                "angle": "medical_mystery",
                "slug": "death_cap_mushroom_poisoning_amatoxins_liver_rna_polymerase",
                "why_trending": "High-retention medical drama documentaries covering the delayed deceptive recovery and lethal liver destruction caused by Amanita phalloides.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Fungal Radiation Shields: Melanin-Rich Chernobyl Molds Protecting Electronics from Space Rays",
                "trend_score": 97,
                "angle": "space_science",
                "slug": "fungal_radiation_shields_melanin_chernobyl_molds_space_rays",
                "why_trending": "Mind-blowing viral science news reporting how black mold growing on Chernobyl's reactor core uses gamma radiation like plants use sunlight.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "White-Nose Syndrome: The Cold-Loving Fungus Decimating Millions of Hibernating Bats",
                "trend_score": 91,
                "angle": "conservation_crisis",
                "slug": "white_nose_syndrome_cold_loving_fungus_decimating_bats",
                "why_trending": "Urgent wildlife biology investigation into Pseudogymnoascus destructans causing 95% mortality in North American bat winter hibernacula.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Chaga and Turkey Tail: The Science Behind Immune-Boosting Beta-Glucans in Teas",
                "trend_score": 92,
                "angle": "wellness_trend",
                "slug": "chaga_turkey_tail_science_immune_boosting_beta_glucans",
                "why_trending": "Huge functional mushroom beverage trend (Four Sigmatic, MudWtr) analyzing clinical studies on Polysaccharide-K (PSK) and immune modulation.",
                "status": "Queued"
            }
        ]
    },
    "204_plant_intelligence": {
        "id": "204",
        "slug": "plant_intelligence",
        "title": "Plant Intelligence",
        "category": "Life_Biology",
        "audience": "Cognitive Biologists, Plant Neurobiologists, Philosophers of Science, Bioethicists, Botany Lovers (Global)",
        "progression": [
            ("Tier 1: Sensory Perception in Plants: Photoreceptors, Gravitropism, Mechanoreception & Chemical Sensing (Beginner / Scratch)",
             "Plant multi-sensory awareness (over 15 non-visual sensory modalities), photoreceptive timing, amyloplast gravity statoliths, and Darwin's 'root-brain' hypothesis."),
            ("Tier 2: Bioelectrical Signaling & Memory: Action Potentials, Calcium Waves, Habituation & The Mimosa Experiments (Intermediate)",
             "Phloem bioelectrical action potentials, systemic calcium ion signaling, Monica Gagliano's habituation drop tests, acoustic detection of caterpillars, and epigenetic vernalization memory."),
            ("Tier 3: Adaptive Decision-Making & Kin Recognition: Root Competition, Foraging Strategies & Maternal Seed Provisioning (Upper Intermediate)",
             "Strategic root foraging avoiding competition, kin recognition sharing root zones with siblings, parasitic dodder vine volatile tracking, and canopy branch geometry game theory."),
            ("Tier 4: The Plant Neurobiology Debate: Stefano Mancuso vs The Skeptics, Consciousness & The Ethics of Plant Life (Advanced / Masterclass)",
             "The fierce debate over 'plant neurobiology', plant response to medical anesthetics, decentralized bio-computation (slime mold traveling salesman), and moral ethics of plant sentience.")
        ],
        "flagship": {
            "title": "The Mind Without a Brain: How Plants Compute, Remember, and Make Strategic Decisions",
            "angle": "deep_dive",
            "slug": "204_plant_intelligence_deep_dive_the_mind_without_a_brain"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Mind Without a Brain: How Plants Compute, Remember, and Make Strategic Decisions",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "mind_without_a_brain_how_plants_compute_remember_decide",
                "question": "How can an organism without a centralized brain or neurons integrate sensory data, learn from experience, and solve complex spatial problems?",
                "focus": "Decentralized cellular modular intelligence, comparing animal centralized computation to plant distributed network intelligence, plastic growth responses, and redefining what it means to 'think'.",
                "reason": "The quintessential masterclass establishing the philosophical and scientific paradigm of plant cognition."
            },
            {
                "id": 2,
                "title": "Sensory Overload: How Plants Possess Over 15 Sensory Channels Without Sense Organs",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "sensory_science",
                "slug": "sensory_overload_how_plants_possess_15_sensory_channels",
                "question": "How do plants sense humidity gradients, soil chemical toxins, electromagnetic fields, and mechanical vibrations across their entire bodies?",
                "focus": "Mechanosensitive ion channels (MSCs), hygroscopic sensing, heavy metal root avoidance, blue and red photoreceptor ratios detecting competitor shade, and chemical volatile receptors.",
                "reason": "Reveals the rich, multifaceted sensory reality through which plants continuously monitor their environment."
            },
            {
                "id": 3,
                "title": "The Root Apex Command Center: Darwin's 'Root-Brain' Hypothesis Re-evaluated",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "root_apex_command_center_darwin_root_brain_hypothesis",
                "question": "Did Charles Darwin foresee modern bioelectricity when he wrote that the tip of the root acts like the brain of a lower animal?",
                "focus": "The 1880 The Power of Movement in Plants, root apex transition zone (TZ) between cell division and elongation, high auxin flux and electrical rhythmic oscillations, and steering root caps.",
                "reason": "Grounds modern plant neurobiology in Darwin's visionary, pioneering evolutionary experiments."
            },
            {
                "id": 4,
                "title": "Photoreception Networks: Phytochromes Measuring Day Length to the Minute",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "photoreception_networks_phytochromes_measuring_day_length",
                "question": "How do plants know the exact day of spring to burst into bloom without ever looking at a calendar?",
                "focus": "Phytochrome red/far-red (Pr to Pfr) reversible conformational switching, night-break experiments, CONSTANS and Flowering Locus T (FT) 'Florigen' mobile protein messengers, and circadian gene loops.",
                "reason": "Technical breakdown of the precision astronomical chronometer operating inside every plant leaf."
            },
            {
                "id": 5,
                "title": "Gravitropism and Statoliths: How Dense Starch Grains Roll to Tell Up from Down",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "biomechanics",
                "slug": "gravitropism_and_statoliths_dense_starch_grains_up_down",
                "question": "What happens inside a root cap cell when a potted plant is tipped on its side, and how does it redirect roots downward within minutes?",
                "focus": "Heavy amyloplast starch statoliths settling along the lower endoplasmic reticulum membrane, triggering asymmetric PIN protein auxin efflux carriers, and contrasting shoot vs root auxin responses.",
                "reason": "Fascinating examination of cellular gravity detection and directional navigational growth."
            },
            {
                "id": 6,
                "title": "Electrical Signaling Along Phloem Cables: Action Potentials Matching Animal Nerves",
                "tier": "Tier 2: Bioelectrical Signaling & Memory",
                "angle": "scientific_phenomenon",
                "slug": "electrical_signaling_phloem_cables_action_potentials_plants",
                "question": "How do plants transmit rapid electrical action potentials through vascular sieve tubes at speeds of centimeters per second?",
                "focus": "Plasma membrane depolarization via chloride efflux and potassium influx, slow wave potentials (variation potentials), electrical transmission through plasmodesmata, and wound response coordination.",
                "reason": "Explores the bioelectrical neural-like signaling infrastructure hidden inside vascular plants."
            },
            {
                "id": 7,
                "title": "The Mimosa Pudica Habituation: Monica Gagliano's Drop Tests Demonstrating Memory",
                "tier": "Tier 2: Bioelectrical Signaling & Memory",
                "angle": "experimental_study",
                "slug": "mimosa_pudica_habituation_monica_gagliano_drop_tests",
                "question": "How did repeated mechanical dropping of sensitive Mimosa plants prove they can learn that a stimulus is harmless and retain the memory for 40 days?",
                "focus": "Non-associative learning (habituation), ruling out motor fatigue by shaking the plant after drops (causing immediate closure), persistence of memory in darkness, and challenging the brain-only paradigm.",
                "reason": "The landmark, provocative behavioral experiment that reignited global debate over plant learning and memory."
            },
            {
                "id": 8,
                "title": "Calcium Waves and Wound Signals: How a Bug Bite Warns the Entire Plant in Seconds",
                "tier": "Tier 2: Bioelectrical Signaling & Memory",
                "angle": "biochemical_breakthrough",
                "slug": "calcium_waves_wound_signals_bug_bite_warns_entire_plant",
                "question": "How do fluorescent GFP biosensors reveal glowing waves of calcium ions rushing through a plant's vascular veins after a caterpillar bites one leaf?",
                "focus": "Glutamate receptor-like (GLR) channels releasing cytosolic calcium spikes, propagating systemic systemic acquired resistance (SAR), and triggering distal leaves to synthesize defensive tannins.",
                "reason": "Spectacular visual and biochemical demonstration of high-speed whole-organism communication in plants."
            },
            {
                "id": 9,
                "title": "Acoustic Perception: How Roots Sense the Vibration of Water and Chewing Caterpillars",
                "tier": "Tier 2: Bioelectrical Signaling & Memory",
                "angle": "cutting_edge_science",
                "slug": "acoustic_perception_roots_sense_vibration_water_caterpillars",
                "question": "Can plants actually hear? How do pea seedling roots grow toward acoustic recordings of running water inside sealed plastic tubes?",
                "focus": "Acoustic mechanoreception, Arabidopsis plants priming chemical toxins when exposed to audio recordings of caterpillars chewing leaves (but ignoring wind sounds), and phonotropism.",
                "reason": "Mind-bending frontier research uncovering the acoustic vibrational sensory world of plants."
            },
            {
                "id": 10,
                "title": "Epigenetic Memory: How Plants 'Remember' Winter Cold and Heatwaves for Future Seasons",
                "tier": "Tier 2: Bioelectrical Signaling & Memory",
                "angle": "genetic_phenomenon",
                "slug": "epigenetic_memory_how_plants_remember_winter_vernalization",
                "question": "How does a winter wheat seed 'remember' that it was exposed to 40 days of sub-zero cold months after the blizzard ends?",
                "focus": "Vernalization genetics, histone methylation and chromatin remodeling turning off the flowering repressor FLC (Flowering Locus C), passing stress memories to offspring via small RNAs.",
                "reason": "In-depth molecular genetics breakdown of non-neural long-term biological memory."
            },
            {
                "id": 11,
                "title": "Intelligent Foraging: How Roots Navigate Toward Nutrients While Avoiding Obstacles",
                "tier": "Tier 3: Adaptive Decision-Making & Kin Recognition",
                "angle": "behavioral_habits",
                "slug": "intelligent_foraging_roots_navigate_nutrients_avoid_obstacles",
                "question": "How do underground root tips assess cost-benefit trade-offs, investing energy into dense root branching only when encountering high-grade compost?",
                "focus": "Economic foraging theory applied to root systems, detecting nutrient gradient patches (nitrate and phosphate hotspots), altering growth angles before physical collisions, and root competition.",
                "reason": "Reveals the strategic, resource-optimizing decision-making performed continuously beneath our feet."
            },
            {
                "id": 12,
                "title": "Kin Recognition in Plants: Sharing Root Zones with Siblings While Strangling Strangers",
                "tier": "Tier 3: Adaptive Decision-Making & Kin Recognition",
                "angle": "ecological_keystone",
                "slug": "kin_recognition_in_plants_sharing_root_zones_siblings",
                "question": "How does a plant tell whether an adjacent root in the dark soil belongs to its own seed sibling or a genetic competitor?",
                "focus": "Root exudate chemical signatures, Cakile edentula (sea rocket) growing polite restrained roots beside siblings vs aggressive competitive proliferation beside strangers, and altruism.",
                "reason": "Fascinating examination of non-animal social behavior, kinship altruism, and competitive territoriality."
            },
            {
                "id": 13,
                "title": "Parasitic Stalking: How the Dodder Vine (Cuscuta) Sniffs Out Tomato Hosts",
                "tier": "Tier 3: Adaptive Decision-Making & Kin Recognition",
                "angle": "predatory_botany",
                "slug": "parasitic_stalking_how_dodder_vine_sniffs_out_tomato_hosts",
                "question": "How does a leafless, rootless parasitic vine slither across soil toward the scent of a tomato seedling like a hunting predator?",
                "focus": "Volatile chemical chemoreception (sniffing beta-phellandrene and beta-myrcene), rejecting poor host wheat plants, coiling around nutrient-rich tomato stems, and driving haustoria into phloem veins.",
                "reason": "Thrilling showcase of active botanical predation through airborne olfactory tracking."
            },
            {
                "id": 14,
                "title": "Game Theory in the Canopy: Branch Growth Adjusting Angles to Avoid Shading Neighbors",
                "tier": "Tier 3: Adaptive Decision-Making & Kin Recognition",
                "angle": "mathematical_biology",
                "slug": "game_theory_canopy_branch_growth_angles_avoid_shading",
                "question": "Why do forest trees adjust their branch growth to leave mysterious gaps called 'crown shyness' where canopies never touch?",
                "focus": "Crown shyness mutual boundary avoidance, Far-red light reflection from leaf edges warning of impending shade, minimizing wind collision branch breakage, and evolutionary game theory equilibria.",
                "reason": "Spectacular aerial botanical phenomenon explained through mathematical game theory and optics."
            },
            {
                "id": 15,
                "title": "Maternal Care in Plants: How Mother Trees Preferentially Route Carbon to Saplings",
                "tier": "Tier 3: Adaptive Decision-Making & Kin Recognition",
                "angle": "human_interest",
                "slug": "maternal_care_in_plants_mother_trees_route_carbon_saplings",
                "question": "How do old-growth Douglas firs use fungal networks to recognize their own genetic offspring and feed them life-saving sugars in deep forest shade?",
                "focus": "Suzanne Simard's isotope labeling experiments (tracing Carbon-13 and Carbon-14 between trees), preferential kin carbon allocation, reducing root competition near offspring, and intergenerational forest legacy.",
                "reason": "Deeply moving ecological research revealing parental care and familial networks in ancient forests."
            },
            {
                "id": 16,
                "title": "Stefano Mancuso vs The Skeptics: The Fierce Scientific War Over 'Plant Neurobiology'",
                "tier": "Tier 4: The Neurobiology Debate & Ethics",
                "angle": "controversial_debate",
                "slug": "stefano_mancuso_vs_skeptics_scientific_war_plant_neurobiology",
                "question": "Why does calling plant behavior 'intelligence' or 'neurobiology' provoke furious pushback from prominent mainstream plant scientists?",
                "focus": "The 2006 founding of the Society for Plant Neurobiology, Lincoln Taiz and skeptics arguing against neuro-anthropomorphism, the semantics of 'intelligence', and redefining cognition without neurons.",
                "reason": "Rigorous, balanced deconstruction of the most contentious scientific debate in modern botany."
            },
            {
                "id": 17,
                "title": "Can Plants Feel Anesthesia? Diethyl Ether Silencing Venus Flytrap Action Potentials",
                "tier": "Tier 4: The Neurobiology Debate & Ethics",
                "angle": "medical_science",
                "slug": "can_plants_feel_anesthesia_diethyl_ether_silencing_action_potentials",
                "question": "Why do the exact same general anesthetics that put human surgical patients to sleep completely paralyze Venus flytraps and sensitive plants?",
                "focus": "Diethyl ether, lidocaine, and xenon gas experiments, silencing electrical action potentials, fluidizing plasma membranes, immobilizing trigger hairs, and universal bio-membrane excitability.",
                "reason": "Profound biological experiment demonstrating that the cellular basis of electrical excitability is shared across all kingdoms of life."
            },
            {
                "id": 18,
                "title": "Decentralized Computing: How Slime Molds and Plants Solve Traveling Salesman Problems",
                "tier": "Tier 4: The Neurobiology Debate & Ethics",
                "angle": "computational_biology",
                "slug": "decentralized_computing_slime_molds_plants_traveling_salesman",
                "question": "How do brainless biological networks compute optimal mathematical paths that rival multi-million-dollar supercomputer algorithms?",
                "focus": "Physarum polycephalum recreating Tokyo's rail map between oat-flake stations, self-reinforcing tubular cytoplasmic flow, minimal Steiner tree optimization, and biomimetic communication routing.",
                "reason": "Fascinating bridge between biological self-organization, computer science, and non-neural computational intelligence."
            },
            {
                "id": 19,
                "title": "Plant Ethics and Rights: If Plants Are Sentient, How Does That Reshape Human Morality?",
                "tier": "Tier 4: The Neurobiology Debate & Ethics",
                "angle": "philosophical_ethics",
                "slug": "plant_ethics_and_rights_sentience_reshaping_human_morality",
                "question": "If plants possess memory, perceive damage, and communicate distress, what does that mean for ethical agriculture, animal diets, and legal standing?",
                "focus": "The Swiss Federal Ethics Committee on Non-Human Biotechnology 'Dignity of Living Beings with Regard to Plants', moral standing of flora, indigenous animist worldviews, and respectful ecosystem stewardship.",
                "reason": "Deeply reflective philosophical examination challenging human moral assumptions and our relationship with the living world."
            },
            {
                "id": 20,
                "title": "Plant-Machine Interfaces: Bionic Plants Sending Text Messages on Soil Contaminants",
                "tier": "Tier 4: The Neurobiology Debate & Ethics",
                "angle": "future_frontiers",
                "slug": "plant_machine_interfaces_bionic_plants_sending_text_messages",
                "question": "How are engineers embedding carbon nanotubes into spinach leaves to create living sensors that detect groundwater explosives and email researchers?",
                "focus": "Plant nanobionics at MIT, infrared optical sensors reading fluorescent single-walled carbon nanotubes in leaf mesophyll, cyborg trees monitoring wildfire smoke, and living biological environmental sentinels.",
                "reason": "Visionary capstone merging plant bio-intelligence with cutting-edge cybernetic technology."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Anesthetizing a Venus Flytrap: Watch What Happens When Plants Inhale Anesthetic Gas",
                "trend_score": 97,
                "angle": "viral_experiment",
                "slug": "anesthetizing_a_venus_flytrap_inhaling_medical_gas_experiment",
                "why_trending": "Ultra-viral science demonstration showing unresponsive flytraps failing to snap shut after exposure to medical anesthesia vapors.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "The Pea Plant Maze Test: How Climbing Vines Anticipate Trellis Locations",
                "trend_score": 95,
                "angle": "cognitive_experiment",
                "slug": "pea_plant_maze_test_climbing_vines_anticipate_trellis",
                "why_trending": "Fascinating time-lapse experiments showing tendrils reaching for artificial supports before physically touching them.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Do Plants Feel Pain? Deconstructing Damage Pathways vs Subjective Suffering",
                "trend_score": 96,
                "angle": "philosophical_debate",
                "slug": "do_plants_feel_pain_damage_pathways_vs_subjective_suffering",
                "why_trending": "Perennial multi-million view philosophical debate crossing neuroscience, vegetarianism, and botanical sensory science.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Monica Gagliano's Experiments: The Scientist Proving Plants Can Hear and Learn",
                "trend_score": 94,
                "angle": "scientist_profile",
                "slug": "monica_gagliano_experiments_scientist_proving_plants_hear",
                "why_trending": "High-profile biographical and scientific profiles exploring the rebel biologist challenging conventional academic dogmas.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "Slime Mold Replicating Tokyo's Subway: The Network That Defeats Human Engineers",
                "trend_score": 95,
                "angle": "computational_nature",
                "slug": "slime_mold_replicating_tokyo_subway_defeating_engineers",
                "why_trending": "Legendary viral science demonstration where yellow Physarum slime mold builds optimal transport grids more resilient than human designs.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Plant Electrical Music: Translating Leaf Bio-Voltages into Synthesizer Melodies",
                "trend_score": 93,
                "angle": "viral_art",
                "slug": "plant_electrical_music_translating_leaf_voltages_synthesizers",
                "why_trending": "Explosive TikTok/Instagram music trend using galvanic sensors on monstera and mushroom caps to trigger modular synthesizers.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Bio-Sensor Plants: Spinach Engineered to Detect Landmines and Signal Cameras",
                "trend_score": 92,
                "angle": "defense_biotech",
                "slug": "bio_sensor_plants_spinach_engineered_detect_landmines",
                "why_trending": "Fascinating MIT engineering story of bionic plants communicating via infrared lasers to detect chemical groundwater explosives.",
                "status": "Queued"
            }
        ]
    },
    "205_ecosystems": {
        "id": "205",
        "slug": "ecosystems",
        "title": "Ecosystems",
        "category": "Earth_Environment",
        "audience": "Ecology Students, Environmental Scientists, Wildlife Managers, Climate Activists, Documentary Lovers (Global)",
        "progression": [
            ("Tier 1: Principles of Ecosystem Science: Biomes, Trophic Pyramids, Nutrient Cycling (Carbon/Nitrogen) & Energy Flow (Beginner / Scratch)",
             "Ecosystem fundamentals, Lindeman's 10% trophic efficiency rule, biogeochemical cycles (carbon, nitrogen, phosphorus), global biomes, and carrying capacity dynamics."),
            ("Tier 2: Keystone Species & Ecological Cascades: Trophic Cascades, Wolves of Yellowstone, Sea Otters & Beaver Hydrology (Intermediate)",
             "Top-down vs bottom-up trophic cascades, the Yellowstone wolf reintroduction hydrology impact, beaver landscape engineering, sea otter kelp defense, and apex African herbivores."),
            ("Tier 3: Disturbance Ecology & Succession: Primary vs Secondary Succession, Wildfire Regimes & Island Biogeography (Upper Intermediate)",
             "Primary volcanic vs secondary succession, fire-adapted disturbance regimes, Wilson and MacArthur's Theory of Island Biogeography, invasive species disruptions, and coastal dead zones."),
            ("Tier 4: Planetary Boundaries, Rewilding & Ecosystem Restoration: Ecological Tipping Points, Rewilding Europe & Earth Stewardship (Advanced / Masterclass)",
             "The Stockholm Resilience Centre 9 planetary boundaries, large-scale European and American rewilding projects, Amazon savannization tipping points, and China's Loess Plateau recovery.")
        ],
        "flagship": {
            "title": "The Web of Life: How Trophic Cascades Reshape Continents and Rivers",
            "angle": "deep_dive",
            "slug": "205_ecosystems_deep_dive_the_web_of_life"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Web of Life: How Trophic Cascades Reshape Continents and Rivers",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "deep_dive",
                "slug": "web_of_life_how_trophic_cascades_reshape_continents_rivers",
                "question": "How can the presence of a single apex predator in an ecosystem alter the physical shape and course of rivers?",
                "focus": "Robert Paine's keystone species concept, green world hypothesis (Hairston, Smith, and Slobodkin), top-down predatory control vs bottom-up resource limitation, and ecological interconnectedness.",
                "reason": "The quintessential ecological masterclass introducing the transformative concept of trophic cascades."
            },
            {
                "id": 2,
                "title": "The Laws of Energy Flow: Lindeman's 10% Trophic Efficiency and Ecological Pyramids",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "technical_breakdown",
                "slug": "laws_of_energy_flow_lindeman_10_percent_trophic_efficiency",
                "question": "Why can an ecosystem support millions of plants, thousands of deer, but only a handful of mountain lions?",
                "focus": "Second law of thermodynamics in ecology, Raymond Lindeman's 1942 trophic-dynamic aspect, 90% metabolic heat loss between trophic levels, and biomass vs energy pyramids.",
                "reason": "Technical breakdown of the fundamental thermodynamic laws governing all living ecosystems on Earth."
            },
            {
                "id": 3,
                "title": "Biogeochemical Cycles: How Carbon, Nitrogen, and Phosphorus Flow from Rocks to Cells",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "foundational_framework",
                "slug": "biogeochemical_cycles_carbon_nitrogen_phosphorus_rocks_cells",
                "question": "How do nitrogen-fixing bacteria in soil transform inert atmospheric gas into the DNA and proteins of living organisms?",
                "focus": "The nitrogen cycle (ammonification, nitrification, denitrification, Haber-Bosch human disruption), the slow geologic phosphorus cycle, and the deep carbon cycle exchanging with oceans.",
                "reason": "Establishes the indispensable chemical circulation systems that sustain biological life."
            },
            {
                "id": 4,
                "title": "The World's Major Biomes: Tropical Rainforests, Savannas, Tundras, and Deserts",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "environmental_guide",
                "slug": "worlds_major_biomes_rainforests_savannas_tundras_deserts",
                "question": "How do latitude, atmospheric Hadley cells, and precipitation patterns partition the planet into distinct ecological zones?",
                "focus": "Whittaker biome diagram (temperature vs precipitation), tropical rainforest hyper-diversity, Mediterranean sclerophyll chaparral, temperate deciduous forests, and permafrost tundra limits.",
                "reason": "Comprehensive macro-geographic tour of Earth's great ecological biomes."
            },
            {
                "id": 5,
                "title": "Carrying Capacity and Population Dynamics: J-Curves, S-Curves, and Predator-Prey Loops",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mathematical_biology",
                "slug": "carrying_capacity_population_dynamics_j_curves_s_curves",
                "question": "What happens when a population overshoots the carrying capacity of its habitat, and why do lynx and snowshoe hare numbers cycle every 10 years?",
                "focus": "Logistic growth equation (K = carrying capacity), density-dependent vs density-independent factors, Lotka-Volterra predator-prey mathematical oscillations, and the Isle Royale wolf-moose study.",
                "reason": "Deconstructs the mathematical rhythms and population bounds governing ecological balance."
            },
            {
                "id": 6,
                "title": "How Wolves Change Rivers: The 1995 Yellowstone Reintroduction and River Bank Stabilization",
                "tier": "Tier 2: Keystone Species & Ecological Cascades",
                "angle": "case_study",
                "slug": "how_wolves_change_rivers_yellowstone_reintroduction_hydrology",
                "question": "How did reintroducing 31 grey wolves into Yellowstone National Park after 70 years of absence cause eroded river banks to stabilize and forests to return?",
                "focus": "Ecology of fear altering elk grazing behavior, willows and aspens regenerating along rivers, beaver recolonization building dams, songbird and trout habitat recovery, and geomorphic river stabilization.",
                "reason": "The most famous, widely studied real-world case study of an apex predator restoring a damaged ecosystem."
            },
            {
                "id": 7,
                "title": "Beaver Engineering: How Rodents Build Wetlands, Fight Droughts, and Create Wildfire Refugia",
                "tier": "Tier 2: Keystone Species & Ecological Cascades",
                "angle": "keystone_species",
                "slug": "beaver_engineering_how_rodents_build_wetlands_fight_droughts",
                "question": "How does a 40-pound rodent with orange teeth construct ecological oases that stay lush green even during mega-wildfires and historic droughts?",
                "focus": "Castor canadensis hydrology engineering, beaver pond groundwater recharge, slowing peak floodwaters, creating emerald wildfire refugia where animals survive blazes, and beaver restoration economics.",
                "reason": "Celebrates nature's greatest non-human civil engineer and its indispensable role in climate resilience."
            },
            {
                "id": 8,
                "title": "Sea Otters and Kelp Forests: Eliminating Urchin Barrens to Protect Coastal Marine Carbon Sinks",
                "tier": "Tier 2: Keystone Species & Ecological Cascades",
                "angle": "marine_ecology",
                "slug": "sea_otters_kelp_forests_eliminating_urchin_barrens_carbon",
                "question": "What happens to coastal California and Alaska marine ecosystems when sea otters are removed, and how do purple sea urchins turn giant kelp into deserts?",
                "focus": "Trophic cascade in marine kelp forests, sea otters devouring herbivorous urchins, giant Macrocystis kelp growing 2 feet a day, carbon sequestration in ocean sediment, and nursery habitats for fish.",
                "reason": "Clear, iconic marine ecological study demonstrating the profound downstream impacts of predator presence."
            },
            {
                "id": 9,
                "title": "The Pollinator Crisis: How Losing Wild Bees Collapses Terrestrial Food Systems",
                "tier": "Tier 2: Keystone Species & Ecological Cascades",
                "angle": "ecological_crisis",
                "slug": "pollinator_crisis_losing_wild_bees_collapses_food_systems",
                "question": "What would happen to the world's fruit, vegetable, and wild plant ecosystems if wild pollinating insects vanished?",
                "focus": "87% of all flowering plants requiring animal pollinators, economic value of wild pollination ($577 billion/year), nutritional security impacts (loss of vitamin-rich crops), and multiple stressors (pesticides, habitat loss, climate).",
                "reason": "Urgent examination of the keystone insect guild that underpins global terrestrial biodiversity."
            },
            {
                "id": 10,
                "title": "Apex Herbivores: How Elephants Prevent Savanna Encroachment and Create Water Holes",
                "tier": "Tier 2: Keystone Species & Ecological Cascades",
                "angle": "field_guide",
                "slug": "apex_herbivores_how_elephants_prevent_savanna_encroachment",
                "question": "How do African savanna elephants act as geological and botanical bulldozers that keep grasslands open for millions of grazing animals?",
                "focus": "Knocking down mature acacia trees to prevent woody bush encroachment, digging dry riverbeds with tusks to create water sources, dispersing large seeds through dung over 40 miles, and megaherbivore ecology.",
                "reason": "Showcase of how terrestrial megaherbivores physically engineer entire continental landscapes."
            },
            {
                "id": 11,
                "title": "Primary vs Secondary Succession: From Bare Volcanic Basalt to Climax Ancient Forest",
                "tier": "Tier 3: Disturbance Ecology & Succession",
                "angle": "ecological_succession",
                "slug": "primary_vs_secondary_succession_volcanic_basalt_climax_forest",
                "question": "How does sterile, freshly cooled volcanic lava on an island transform over 500 years into a towering, multi-layered ancient rainforest?",
                "focus": "Primary succession without soil (lichens and mosses creating initial organic matter), pioneer annual weeds, shade-intolerant fast pines, secondary succession following forest fires (intact seedbanks), and climax forest equilibria.",
                "reason": "Foundational ecological concept detailing the orderly temporal process of habitat formation."
            },
            {
                "id": 12,
                "title": "Fire Ecology: Why Suppressing All Wildfires Causes Catastrophic Megafires",
                "tier": "Tier 3: Disturbance Ecology & Succession",
                "angle": "environmental_dilemma",
                "slug": "fire_ecology_why_suppressing_wildfires_causes_megafires",
                "question": "How did 100 years of Smokey Bear fire suppression policies accidentally create explosive fuel tinderboxes across Western North America?",
                "focus": "The fire deficit, historical low-intensity indigenous burns clearing understory brush, dense tree overcrowding, catastrophic crown fire transitions, and restoring prescribed fire stewardship.",
                "reason": "Crucial paradigm shift demonstrating that fire is not a destructive enemy, but an essential ecological tool."
            },
            {
                "id": 13,
                "title": "The Theory of Island Biogeography: Wilson and MacArthur's Math on Area Size and Extinction",
                "tier": "Tier 3: Disturbance Ecology & Succession",
                "angle": "scientific_phenomenon",
                "slug": "theory_of_island_biogeography_wilson_macarthur_extinction_math",
                "question": "Why does a 10-acre fragment of isolated rainforest lose half its species within a decade of being surrounded by soybean fields?",
                "focus": "E.O. Wilson and Robert MacArthur's 1967 equilibrium model (immigration rates vs extinction rates based on island area and distance), habitat fragmentation turning nature reserves into virtual islands, and wildlife corridors.",
                "reason": "The defining mathematical foundation of modern conservation biology and nature reserve design."
            },
            {
                "id": 14,
                "title": "Invasive Species Disruptions: Cane Toads, Kudzu, Zebra Mussels, and Ecological Disarray",
                "tier": "Tier 3: Disturbance Ecology & Succession",
                "angle": "challenges_obstacles",
                "slug": "invasive_species_disruptions_cane_toads_kudzu_zebra_mussels",
                "question": "Why do non-native species flourish so uncontrollably when introduced to new continents, devastating native species?",
                "focus": "The enemy release hypothesis (escaping native co-evolved predators and parasites), Australia's catastrophic cane toad release, zebra mussels clogging Great Lakes municipal water intake pipes, and mechanical vs biological control.",
                "reason": "In-depth examination of the second leading cause of global biodiversity loss."
            },
            {
                "id": 15,
                "title": "Eutrophication and Dead Zones: How Farm Fertilizer Creates Suffocated Coastal Seas",
                "tier": "Tier 3: Disturbance Ecology & Succession",
                "angle": "investigative",
                "slug": "eutrophication_dead_zones_farm_fertilizer_suffocated_seas",
                "question": "How does synthetic nitrogen fertilizer applied to Midwest cornfields create a 6,000-square-mile dead zone in the Gulf of Mexico where no fish can breathe?",
                "focus": "Agricultural runoff flowing down the Mississippi River, massive marine algal blooms, bacterial decomposition consuming all dissolved oxygen (hypoxia under 2 mg/L), fish kills, and regenerative cover-crop solutions.",
                "reason": "Vital investigative breakdown connecting continental agricultural practices to oceanic hypoxia."
            },
            {
                "id": 16,
                "title": "Planetary Boundaries: The Nine Environmental Thresholds Humanity Must Not Cross",
                "tier": "Tier 4: Planetary Boundaries & Rewilding",
                "angle": "framework_analysis",
                "slug": "planetary_boundaries_nine_environmental_thresholds_humanity",
                "question": "What are the nine critical biophysical guardrails that keep planet Earth in the stable, hospitable Holocene state that allowed civilization to arise?",
                "focus": "Johan Rockström and the Stockholm Resilience Centre framework: climate change, biodiversity integrity, biogeochemical flows (N/P), land system change, freshwater use, ocean acidification, and crossing critical tipping thresholds.",
                "reason": "The paramount scientific framework used by global institutions to evaluate systemic planetary health."
            },
            {
                "id": 17,
                "title": "The Rewilding Revolution: Bringing Back Bison, Wolves, and Wild Horses to Europe",
                "tier": "Tier 4: Planetary Boundaries & Rewilding",
                "angle": "innovations",
                "slug": "rewilding_revolution_bringing_back_bison_wolves_wild_horses",
                "question": "How is the modern rewilding movement restoring abandoned farmland in Romania, Spain, and Scotland by reintroducing lost megafauna?",
                "focus": "European bison reintroduction in the Southern Carpathians, Konik wild horses managing scrublands, restoring natural disturbance processes rather than manicured gardening, and community eco-tourism benefits.",
                "reason": "Inspiring, progressive vision for large-scale nature recovery and hands-off ecological restoration."
            },
            {
                "id": 18,
                "title": "Ecological Tipping Points: Amazon Savannization, Coral Reef Collapse, and Boreal Thawing",
                "tier": "Tier 4: Planetary Boundaries & Rewilding",
                "angle": "extreme_scenarios",
                "slug": "ecological_tipping_points_amazon_savannization_coral_collapse",
                "question": "What happens when an ecosystem crosses a non-linear threshold where self-reinforcing feedback loops make recovery impossible?",
                "focus": "Amazon rainforest crossing 20-25% deforestation threshold flipping into dry degraded savanna, irreversible permafrost carbon release feedback, hysteresis in ecological state shifts, and early warning indicators.",
                "reason": "Urgent, cutting-edge systems-ecology analysis of non-linear catastrophic environmental regime shifts."
            },
            {
                "id": 19,
                "title": "Ecosystem Services Valuation: Why Mangroves and Wetlands Save Trillions in Flood Damage",
                "tier": "Tier 4: Planetary Boundaries & Rewilding",
                "angle": "economic_ecological_capstone",
                "slug": "ecosystem_services_valuation_mangroves_wetlands_flood_savings",
                "question": "What is the financial dollar value of clean drinking water, coastal storm buffering, pollination, and soil creation provided free by nature?",
                "focus": "Robert Costanza's landmark valuation studies ($125+ trillion/year in global natural services), natural capital accounting on corporate and national balance sheets, and investing in green infrastructure over concrete sea walls.",
                "reason": "Compelling bridge uniting ecological conservation with hard economic financial reality."
            },
            {
                "id": 20,
                "title": "Ecological Restoration at Scale: The Loess Plateau Transformation in China",
                "tier": "Tier 4: Planetary Boundaries & Rewilding",
                "angle": "inspiring_restoration",
                "slug": "ecological_restoration_scale_loess_plateau_transformation_china",
                "question": "How did local communities and the World Bank transform 35,000 square kilometers of eroded, desertified wasteland into lush green terraced farmland?",
                "focus": "The cradle of Chinese civilization ruined by centuries of overgrazing, banning goats on hillsides, building terraced check-dams, restoring perennial vegetation, lifting 2.5 million people out of poverty, and hope for global drylands.",
                "reason": "Magnificent, inspiring masterclass capstone demonstrating that degraded continental ecosystems can be healed at immense scale."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Pleistocene Park Experiment: Reintroducing Megafauna to Siberia to Stop Permafrost Thawing",
                "trend_score": 97,
                "angle": "radical_rewilding",
                "slug": "pleistocene_park_experiment_reintroducing_megafauna_siberia",
                "why_trending": "Massive global documentary fascination following Sergey Zimov's radical Arctic project using bison, muskoxen, and yakut horses to recreate the mammoth steppe.",
                "status": "Queued"
            },
            {
                "id": 22,
                "title": "Beaver Analogs (BDAs): Western Ranchers Hand-Building Fake Beaver Dams to Restore Creeks",
                "trend_score": 94,
                "angle": "grassroots_ecology",
                "slug": "beaver_analogs_bdas_ranchers_building_fake_beaver_dams",
                "why_trending": "Rapidly spreading low-cost restoration method across Idaho, Utah, and Nevada driving water table recovery and creek revitalization.",
                "status": "Queued"
            },
            {
                "id": 23,
                "title": "Wolves in Colorado: The Controversial Rancher vs Conservationist Reintroduction Ballot Battle",
                "trend_score": 95,
                "angle": "controversial_debate",
                "slug": "wolves_in_colorado_controversial_rancher_conservationist_battle",
                "why_trending": "High-tension contemporary news drama covering the historic voter-mandated release of wild Oregon wolves into Colorado cattle country.",
                "status": "Queued"
            },
            {
                "id": 24,
                "title": "Chernobyl Wildlife Eden: How Radiation Exclusion Became Europe's Largest Animal Sanctuary",
                "trend_score": 96,
                "angle": "natural_recovery",
                "slug": "chernobyl_wildlife_eden_radiation_exclusion_largest_sanctuary",
                "why_trending": "Astounding documentary spectacle showing Przewalski's horses, brown bears, lynx, and wolves thriving in the absence of human interference.",
                "status": "Queued"
            },
            {
                "id": 25,
                "title": "The Great Green Wall of China: Millions of Trees Planted to Halt the Gobi Desert",
                "trend_score": 92,
                "angle": "global_megaproject",
                "slug": "great_green_wall_china_millions_trees_halting_gobi_desert",
                "why_trending": "Massive satellite-visible geopolitical reforestation project creating a 2,800-mile shelterbelt forest to suppress Beijing spring dust storms.",
                "status": "Queued"
            },
            {
                "id": 26,
                "title": "Artificial Coral Reefs from Aircraft Carriers: Sinking Warships to Create Habitats",
                "trend_score": 93,
                "angle": "engineering_marvels",
                "slug": "artificial_coral_reefs_aircraft_carriers_sinking_warships",
                "why_trending": "Spectacular controlled demolition footage of decommissioned navy ships sinking to become flourishing artificial marine sanctuaries.",
                "status": "Queued"
            },
            {
                "id": 27,
                "title": "Ghost Forests of the Atlantic Coast: Sea Level Rise and Saltwater Intrusion Killing Pines",
                "trend_score": 91,
                "angle": "climate_impact",
                "slug": "ghost_forests_atlantic_coast_sea_level_rise_saltwater_intrusion",
                "why_trending": "Eerie drone imagery capturing thousands of acres of skeletal bleached pine trunks killed by encroaching saltwater tides along the US East Coast.",
                "status": "Queued"
            }
        ]
    }
}

if __name__ == "__main__":
    print("Generating suites for Batch 201-205 with flexible 10 to 30-minute duration architecture...")
    for folder, meta in BATCH_201_205.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 201-205 complete!")
