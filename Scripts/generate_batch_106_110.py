import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

BATCH_106_110 = {
    "106_marketing_advertising": {
        "id": "106",
        "slug": "marketing_advertising",
        "title": "Marketing & Advertising",
        "category": "Commerce_Industry",
        "audience": "Brand Strategists, Media Buyers, Creative Directors, Entrepreneurs, Growth Marketers (Global)",
        "progression": [
            ("Tier 1: Foundational Frameworks, Brand Positioning & Human Psychology (Beginner / Scratch)",
             "Core psychology of persuasion, Madison Avenue history, direct response vs brand building, Ries & Trout positioning, and neuromarketing cues."),
            ("Tier 2: Practical Media Buying, Copywriting & Channel Mechanics (Intermediate)",
             "Direct response copywriting frameworks (AIDA, PAS), programmatic ad bidding (DSPs/SSPs), guerrilla marketing stunts, Super Bowl economics, and influencer attribution models."),
            ("Tier 3: Attribution Modeling, Crisis Communications & Growth Loops (Upper Intermediate)",
             "Multi-touch attribution challenges post-cookies, PR crisis architecture, product-led growth loops, luxury marketing scarcity dynamics, and enterprise SEO engines."),
            ("Tier 4: Algorithmic Synthesis, AI Hyper-Personalization & Global Scale (Advanced / Masterclass)",
             "Generative AI ad creative, dark pattern ethics, international cross-cultural localization, political micro-targeting, and $100M brand equity architecture.")
        ],
        "flagship": {
            "title": "The Anatomy of a Viral Campaign: What Actually Sells?",
            "angle": "case_study",
            "slug": "106_marketing_advertising_case_study_anatomy_of_a_viral_campaign"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Anatomy of a Viral Campaign: What Actually Sells?",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "anatomy_of_a_viral_campaign",
                "question": "What separates ad campaigns that convert millions from those forgotten instantly?",
                "focus": "Core psychology of attention, persuasion triggers, and creative positioning.",
                "reason": "Crucial foundational episode breaking down classic advertising theory vs modern performance mechanics."
            },
            {
                "id": 2,
                "title": "From Mad Men to Algorithms: The History of Modern Advertising",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "history_of_modern_advertising",
                "question": "How did advertising evolve from print billboards on Madison Avenue to programmatic ad bidding?",
                "focus": "Pioneers like Ogilvy and Bernays, TV broadcast boom, digital search ad disruption.",
                "reason": "Establishes contextual timeline for modern media buying and messaging models."
            },
            {
                "id": 3,
                "title": "Brand Positioning: How to Own a Word in the Consumer's Mind",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "brand_positioning_strategies",
                "question": "Why does Volvo own 'Safety' while Apple owns 'Simplicity'?",
                "focus": "Al Ries & Jack Trout positioning methodology, perceptual mapping, and differentiation.",
                "reason": "Teaches fundamental branding mechanics before jumping into channels."
            },
            {
                "id": 4,
                "title": "Direct Response vs Brand Building: The Perpetual Agency War",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "direct_response_vs_brand_building",
                "question": "Should marketing spend target immediate click conversions or long-term brand equity?",
                "focus": "Les Binet and Peter Field 60/40 rule, CAC vs LTV curves, short-term vs long-term ROI.",
                "reason": "Clarifies the most hotly debated resource allocation dispute in advertising."
            },
            {
                "id": 5,
                "title": "The Neuromarketing Playbook: Subconscious Cues in Packaging and Color",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "psychological_breakdown",
                "slug": "neuromarketing_playbook",
                "question": "How do eye-tracking heatmaps and biometric fMRI studies influence supermarket shelf design?",
                "focus": "Sensory marketing, font weights, color psychology, and subconscious retail nudges.",
                "reason": "Connects biological cognitive triggers directly to customer purchase decisions."
            },
            {
                "id": 6,
                "title": "Copywriting Masterclass: Headlines That Force the Reader to Scroll",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "copywriting_masterclass",
                "question": "What structural frameworks produce high-converting direct response sales copy?",
                "focus": "AIDA, PAS (Problem-Agitate-Solution), curiosity gaps, and benefit-driven bullet points.",
                "reason": "Provides actionable copywriting principles applicable to email, video hooks, and landing pages."
            },
            {
                "id": 7,
                "title": "Programmatic Ad Networks and the Real-Time Bidding Machine",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "programmatic_ad_networks",
                "question": "What happens in the 100 milliseconds between requesting a webpage and displaying an auction ad?",
                "focus": "DSPs, SSPs, ad exchanges, cookie deprecation, and programmatic real-time bidding.",
                "reason": "Deconstructs the invisible multi-billion dollar technical plumbing of digital ads."
            },
            {
                "id": 8,
                "title": "Guerrilla Marketing: Low-Budget Tactics with Astronomical Reach",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "famous_examples",
                "slug": "guerrilla_marketing_tactics",
                "question": "How do bootstrapped startups generate Super Bowl level buzz without spending a fortune?",
                "focus": "Stunt marketing, ambient media, public installations, and organic social amplification.",
                "reason": "Inspires high-creativity solutions over sheer venture capital ad spend."
            },
            {
                "id": 9,
                "title": "The Super Bowl Effect: Is a $7 Million 30-Second Commercial Worth It?",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "super_bowl_ad_economics",
                "question": "How do Fortune 500 brands measure the true financial ROI of multi-million dollar broadcast slots?",
                "focus": "Cultural watermark value, PR press cascades, social media halo effects, and sales lift.",
                "reason": "Reveals the hidden accounting and enterprise strategy behind mega-event television buys."
            },
            {
                "id": 10,
                "title": "Influencer Marketing Decoded: Fake Followers vs Micro-Influencer Communities",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "influencer_marketing_economics",
                "question": "Why are brands firing celebrity endorsers in favor of 10,000-follower niche creators?",
                "focus": "Engagement rate economics, affiliate attribution models, fake bot detection, and trust transfer.",
                "reason": "Captures the fast-moving modern shift in creator economy media partnerships."
            },
            {
                "id": 11,
                "title": "Performance Marketing Attribution: The Multi-Touch Tracking Nightmare",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "failure_mode_analysis",
                "slug": "marketing_attribution_models",
                "question": "When a customer views an ad on TikTok, googles the brand, and buys via email, who gets credit?",
                "focus": "First-touch vs last-touch vs linear attribution, MMM (Media Mix Modeling), and iOS ATT privacy fallout.",
                "reason": "Essential for media planners struggling with broken digital tracking post-cookies."
            },
            {
                "id": 12,
                "title": "PR Disasters and Damage Control: How Brands Survive Public Boycotts",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "pr_disaster_damage_control",
                "question": "What separates brand blunders that sink stock prices from those defused within 48 hours?",
                "focus": "Crisis communications protocol, apology architecture, social outrage lifecycles, and brand recovery.",
                "reason": "Teaches reactive brand protection and stakeholder communications under fire."
            },
            {
                "id": 13,
                "title": "Growth Loops vs Funnels: The Modern SaaS User Acquisition Engine",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "growth_loops_vs_funnels",
                "question": "Why are traditional linear marketing funnels being replaced by self-reinforcing viral product loops?",
                "focus": "Product-led growth (PLG), referral flywheels, retention-driven acquisition, and viral coefficients.",
                "reason": "Explains how companies like Dropbox, Slack, and Figma scaled without massive sales teams."
            },
            {
                "id": 14,
                "title": "The Psychology of Luxury Marketing: Selling Exclusivity and Artificial Scarcity",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "philosophical_perspectives",
                "slug": "luxury_marketing_scarcity",
                "question": "Why does Hermès destroy excess inventory and make customers wait years for a Birkin bag?",
                "focus": "Veblen goods, anti-marketing laws, status signaling, and hermetic retail experiences.",
                "reason": "Analyzes the inverse economic laws governing high-end heritage prestige brands."
            },
            {
                "id": 15,
                "title": "Content Marketing and SEO Engines: Building Perpetual Inbound Organic Traffic",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "practical_playbook",
                "slug": "content_marketing_seo_engine",
                "question": "How do enterprise brands build media operations that capture millions of search intent visits monthly?",
                "focus": "Hub-and-spoke content architecture, topical authority, zero-click searches, and backlink networks.",
                "reason": "Deploys strategic framework for compound organic marketing assets."
            },
            {
                "id": 16,
                "title": "The Future of Advertising: AI Generated Creative and Hyper-Personalization",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "ai_generated_advertising",
                "question": "Will human creative agencies exist when generative AI can render 10,000 bespoke video variants per second?",
                "focus": "Dynamic creative optimization (DCO), synthetic voiceovers, real-time avatar ads, and algorithmic ethics.",
                "reason": "Explores the cutting-edge technological frontier reshaping marketing employment and scale."
            },
            {
                "id": 17,
                "title": "Dark Patterns in Digital Marketing: The Ethics of Manipulation",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "dark_patterns_in_marketing",
                "question": "Where is the line between persuasive conversion rate optimization and illegal predatory design?",
                "focus": "Roach motels, hidden fees, confirmshaming, regulatory crackdowns by FTC and EU GDPR.",
                "reason": "Provides vital ethical guardrails and regulatory compliance context for modern marketers."
            },
            {
                "id": 18,
                "title": "International Brand Localization: Why Global Campaigns Fail in New Markets",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "cross_disciplinary",
                "slug": "international_brand_localization",
                "question": "How did translation errors and cultural insensitivities cost western brands billions in Asia and Latin America?",
                "focus": "Cultural semiotics, naming adaptations, localized consumer rituals, and glocalization strategy.",
                "reason": "Crucial for global expansion managers and cross-border marketing directors."
            },
            {
                "id": 19,
                "title": "Political Advertising and Perception Engineering: The Mechanics of Influence",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "political_advertising_influence",
                "question": "How do political super-PACs apply commercial consumer targeting to swing national elections?",
                "focus": "Psychographic profiling, micro-targeted grievance messaging, dark money ads, and civic polarization.",
                "reason": "Unveils the highest-stakes application of advertising science in modern democracy."
            },
            {
                "id": 20,
                "title": "Building a $100M Brand Architecture: The Master Enterprise Blueprint",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "building_100m_brand_architecture",
                "question": "What overarching framework unites paid media, product storytelling, and community into enduring market dominance?",
                "focus": "End-to-end brand playbook, unit economics, omnichannel synergy, and corporate equity compounding.",
                "reason": "Synthesizes the entire 20-episode marketing curriculum into an executive-level strategic blueprint."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Death of Third-Party Cookies: What Marketers Must Do Now",
                "trend_score": "High Search Surge (Industry Shock)",
                "angle": "deep_dive",
                "slug": "death_of_third_party_cookies",
                "why_trending": "Google Privacy Sandbox rollout and Safari cookie elimination are forcing every ad buyer to pivot.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Duolingo's TikTok Strategy: How an Owl Mascot Broke Corporate Social Media",
                "trend_score": "Viral Phenomenon (High Retention)",
                "angle": "case_study",
                "slug": "duolingo_tiktok_marketing_strategy",
                "why_trending": "Unfiltered unhinged corporate mascot behavior became the gold standard for Gen-Z audience engagement.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why Liquid Death is Worth $1.4 Billion Selling Plain Canned Water",
                "trend_score": "Extremely High Curiosity Volume",
                "angle": "economic_breakdown",
                "slug": "liquid_death_marketing_genius",
                "why_trending": "Deconstructs how rebellious heavy-metal punk branding turned tap water into a retail juggernaut.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "The Rise of De-Influencing: When Audiences Turn Against Sponsored Products",
                "trend_score": "Cultural Trend Spike",
                "angle": "field_investigation",
                "slug": "rise_of_deinfluencing",
                "why_trending": "Explores the anti-consumerist pushback exposing overhyped viral beauty and lifestyle products.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Apple's 'Shot on iPhone' Campaign: The Decade-Long Masterclass in Social Proof",
                "trend_score": "Evergreen High Retention",
                "angle": "famous_examples",
                "slug": "apple_shot_on_iphone_analysis",
                "why_trending": "Shows how user-generated content turned billboard advertising into an aspirational cultural movement.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Why Fast-Food Brands Are Fighting on Twitter: Corporate Banter as Free Media",
                "trend_score": "Consistent Pop Culture Traffic",
                "angle": "mechanisms_and_systems",
                "slug": "fast_food_twitter_wars",
                "why_trending": "Analyzes the snarky brand persona era pioneered by Wendy's and imitated across retail.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The Super Bowl Ad That Never Aired: The Guerrilla Ambush of Nike and Red Bull",
                "trend_score": "High Curiosity Hook",
                "angle": "historical_evolution",
                "slug": "ambush_marketing_super_bowl",
                "why_trending": "Reveals the legally risky ambush marketing campaigns that hijacked official sponsorships for zero licensing cost.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "107_retail_e-commerce": {
        "id": "107",
        "slug": "retail_e-commerce",
        "title": "Retail & E-Commerce",
        "category": "Commerce_Industry",
        "audience": "E-Commerce Merchants, Retail Buyers, DTC Founders, Inventory Managers, Omnichannel Strategists (Global)",
        "progression": [
            ("Tier 1: Retail Foundations, Unit Economics & Store Psychology (Beginner / Scratch)",
             "Evolution from department store catalogs to 1-click checkout, CAC/LTV mathematics, conversion rate optimization (CRO), business model selection, and supermarket layout psychology."),
            ("Tier 2: Platform Channels, Reverse Logistics & Algorithmic Pricing (Intermediate)",
             "Shopify vs Amazon platform dynamics, liquidation of customer returns, dynamic yield pricing engines, subscription box churn curves, and BOPIS omnichannel logistics."),
            ("Tier 3: Ultra-Fast Supply Chains, Livestreaming & Retail Media (Upper Intermediate)",
             "Shein/Zara micro-batch agile apparel, Chinese Douyin livestream commerce vs Western friction, marketplace liquidity flywheels, retail media ad networks, and safety stock resilience."),
            ("Tier 4: Cashierless Automation, Mall Transformations & Global B2B (Advanced / Masterclass)",
             "Computer vision autonomous stores, suburban mall adaptive reuse, de minimis customs loopholes, multi-trillion B2B procurement portals, and omnichannel enterprise architecture.")
        ],
        "flagship": {
            "title": "The Retail Revolution: From Department Stores to 1-Click Checkout",
            "angle": "historical_evolution",
            "slug": "107_retail_e-commerce_historical_evolution_retail_revolution_history"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Retail Revolution: From Department Stores to 1-Click Checkout",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "retail_revolution_history",
                "question": "How did shopping transform from Montgomery Ward mail-order catalogs to frictionless algorithmic storefronts?",
                "focus": "Sears catalog era, suburban mall boom, barcode scanners, Amazon genesis, and direct-to-consumer waves.",
                "reason": "Establishes baseline context for how consumer purchasing expectations evolved over a century."
            },
            {
                "id": 2,
                "title": "The Economics of E-Commerce: Gross Margins, CAC, and the Returns Crisis",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "economic_breakdown",
                "slug": "economics_of_ecommerce",
                "question": "Why do digital commerce brands generating $100M in revenue frequently lose millions on the bottom line?",
                "focus": "Customer Acquisition Cost (CAC), Lifetime Value (LTV), 30% return rates in apparel, shipping overhead.",
                "reason": "Demystifies the harsh financial realities behind glamorous online storefronts."
            },
            {
                "id": 3,
                "title": "Conversion Rate Optimization (CRO): The Science of the Add-to-Cart Button",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "conversion_rate_optimization_basics",
                "question": "How does a 0.5% lift in checkout conversion generate millions in enterprise revenue?",
                "focus": "Cart friction removal, trust badges, sticky add-to-cart buttons, social proof, and mobile UX design.",
                "reason": "Equips creators with the tactical mechanics of digital storefront performance."
            },
            {
                "id": 4,
                "title": "Dropshipping vs Private Label vs Omnichannel: Business Models Deconstructed",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "ecommerce_business_models_compared",
                "question": "Which retail distribution model builds lasting enterprise value versus fleeting cash flow?",
                "focus": "Inventory risk, supply chain moats, white-labeling, wholesale, and direct-to-consumer trade-offs.",
                "reason": "Guides entrepreneurs on selecting the right infrastructure for their retail venture."
            },
            {
                "id": 5,
                "title": "Retail Store Psychology: Why Milk is Always at the Very Back of the Supermarket",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "psychological_breakdown",
                "slug": "retail_store_layout_psychology",
                "question": "How do physical supermarket floor plans manipulate shopper dwell time and cart value?",
                "focus": "Gruen effect, endcap promotions, eye-level shelf pricing, impulse buy registers, and sensory lighting.",
                "reason": "Examines the physical retail design tricks engineered to induce unplanned purchases."
            },
            {
                "id": 6,
                "title": "Shopify vs Amazon: The Duel for the Soul of Digital Commerce",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "shopify_vs_amazon_duel",
                "question": "Should independent brands build on Amazon's walled garden or own their customer data on Shopify?",
                "focus": "FBA logistics vs independent headless commerce, platform take-rates, brand equity ownership.",
                "reason": "Breaks down the defining platform divide facing modern product merchants."
            },
            {
                "id": 7,
                "title": "The Reverse Logistics Nightmare: Where Returned Products Actually Go",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "reverse_logistics_returned_products",
                "question": "Why is it often cheaper for retailers to throw returned electronics and clothes in landfills than restock them?",
                "focus": "Pallet liquidation auctions, return processing centers, freight costs, and sustainability impacts.",
                "reason": "Exposes the hidden operational and ecological underbelly of free-return shopping culture."
            },
            {
                "id": 8,
                "title": "Dynamic Pricing Algorithms: How Retailers Change Prices While You Browse",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "dynamic_pricing_algorithms",
                "question": "How do airlines, Amazon, and Uber adjust prices in real time based on your battery life and device type?",
                "focus": "Yield management, competitive scraping, elasticity modeling, and surge price triggers.",
                "reason": "Explains algorithmic price discrimination shaping the modern retail transaction."
            },
            {
                "id": 9,
                "title": "Subscription E-Commerce: Churn Rates, Box Fatigue, and Retention Strategies",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "failure_mode_analysis",
                "slug": "subscription_ecommerce_churn",
                "question": "Why did hundreds of meal-kit and beauty box startups collapse after explosive early customer signups?",
                "focus": "Monthly churn cliffs, cohort retention curves, diminishing perceived value, and replenishment models.",
                "reason": "Crucial post-mortem on the unsustainable economics of the subscription commerce craze."
            },
            {
                "id": 10,
                "title": "Omnichannel Retail: Uniting Physical Stores with Digital Inventory",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "omnichannel_retail_playbook",
                "question": "How did Walmart, Target, and Zara survive the 'Retail Apocalypse' by turning stores into fulfillment hubs?",
                "focus": "BOPIS (Buy Online, Pick Up In Store), unified POS systems, ship-from-store, and endless aisle concepts.",
                "reason": "Demonstrates how legacy brick-and-mortar players beat digital pure-plays at fulfillment."
            },
            {
                "id": 11,
                "title": "Fast Fashion Economics: How Shein and Zara Produce Clothes in 7 Days",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "fast_fashion_ultra_fast_economics",
                "question": "What agile manufacturing software allows ultra-fast fashion brands to test thousands of micro-batches daily?",
                "focus": "On-demand contract factories, algorithm-driven trend scraping, cross-border de minimis tax exemptions.",
                "reason": "Analyzes the hyper-efficient, disruptive supply chain upending global apparel."
            },
            {
                "id": 12,
                "title": "Livestream Shopping: Why China Sells Billions on TikTok and the West Still Struggles",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "livestream_shopping_china_vs_west",
                "question": "How did live commerce on Taobao and Douyin reach $500B while Western shoppers resisted video shopping?",
                "focus": "KOL influencer culture, gamified flash discounts, payment ecosystem integration, and Western checkout friction.",
                "reason": "Examines the geopolitical and cultural divergence in next-generation commerce interfaces."
            },
            {
                "id": 13,
                "title": "Marketplace Network Effects: Why Winner Takes Most in Digital Platforms",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "marketplace_network_effects",
                "question": "How do two-sided market dynamics create unassailable moats for platforms like eBay, Etsy, and MercadoLibre?",
                "focus": "Chicken-and-egg launch problem, buyer-seller liquidity, platform governance, and disintermediation defense.",
                "reason": "Foundational economic architecture for digital marketplace operators."
            },
            {
                "id": 14,
                "title": "Retail Media Networks: Why Supermarkets are Becoming Ad Agencies",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "emerging_trends",
                "slug": "retail_media_networks",
                "question": "Why are Walmart, Target, and Kroger generating billions in pure profit selling ads on their own search bars?",
                "focus": "First-party purchase intent data, offsite audience targeting, in-store digital screens, and 80% ad margins.",
                "reason": "Unveils the fastest-growing and most lucrative revenue stream in global retail."
            },
            {
                "id": 15,
                "title": "Supply Chain Resilience: From Just-In-Time to Just-In-Case Inventory",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "systemic_critique",
                "slug": "supply_chain_resilience_retail",
                "question": "What structural supply chain shifts occurred when global shipping bottlenecks crippled pandemic retail?",
                "focus": "Safety stock calculation, supplier diversification, nearshoring, and container freight volatility.",
                "reason": "Teaches risk management and buffer stock modeling for retail inventory executives."
            },
            {
                "id": 16,
                "title": "Autonomous Stores and Cashierless Checkout: The Computer Vision Future",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "mechanisms_and_systems",
                "slug": "autonomous_cashierless_stores",
                "question": "How do Amazon Go and smart cart sensors track hundreds of items without barcode scanning?",
                "focus": "Ceiling camera sensor fusion, weight-sensor shelving, shrinkage rates, and implementation capex.",
                "reason": "Assesses the viability, cost barriers, and future trajectory of automated physical retail."
            },
            {
                "id": 17,
                "title": "The Death of the Suburban Mall: What Happens to Millions of Square Feet of Dead Retail?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "historical_evolution",
                "slug": "death_of_suburban_malls",
                "question": "Why did iconic shopping malls across America become ghost towns, and what will replace them?",
                "focus": "Anchor tenant bankruptcies, adaptive reuse into data centers/apartments, and experiential luxury hubs.",
                "reason": "Examines the commercial real estate and socioeconomic fallout of shifting retail habits."
            },
            {
                "id": 18,
                "title": "The Ethics of De Minimis and Counterfeits in Cross-Border E-Commerce",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "counterfeits_and_cross_border_trade",
                "question": "How do loophole customs exemptions allow billions in untaxed, counterfeit goods to enter domestic markets?",
                "focus": "Intellectual property enforcement, safety recalls, customs inspection bottlenecks, and unfair domestic competition.",
                "reason": "Highlights urgent legal and ethical questions facing regulators and global trade bodies."
            },
            {
                "id": 19,
                "title": "B2B E-Commerce: The Multi-Trillion Dollar Wholesale Digital Modernization",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "comparative_analysis",
                "slug": "b2b_ecommerce_modernization",
                "question": "Why is business-to-business digital procurement growing twice as fast as consumer retail?",
                "focus": "Custom credit terms, ERP integrations, wholesale catalogs, punchout sites, and complex purchase orders.",
                "reason": "Highlights the massive, often overlooked enterprise counterpart to B2C e-commerce."
            },
            {
                "id": 20,
                "title": "Building a Modern Retail Empire: The Omnichannel Architecture Masterclass",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "building_modern_retail_empire",
                "question": "What comprehensive strategic framework unites product development, digital acquisition, and retail shelf presence?",
                "focus": "Unit economics, supply chain redundancy, unified customer database, and defensive retail moats.",
                "reason": "Synthesizes the entire 20-episode retail curriculum into an actionable enterprise playbook."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Temu's Gamified Super-Discounts: How PDD Holdings Conquered the App Store",
                "trend_score": "Massive Search Spike",
                "angle": "case_study",
                "slug": "temu_gamified_ecommerce_analysis",
                "why_trending": "Temu's relentless ad spending, factory-direct pricing, and wheel-spin coupons disrupted mobile shopping.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The Return Crisis: Why Amazon Now Gives Refunds Without Demanding the Item Back",
                "trend_score": "Viral Curiosity Hook",
                "angle": "economic_breakdown",
                "slug": "returnless_refunds_amazon",
                "why_trending": "Reveals the shocking algorithm calculations where throwing away returned goods saves shipping fees.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why Costco Sells Hot Dogs and Rotisserie Chickens at a Guaranteed Loss",
                "trend_score": "High Evergreen Engagement",
                "angle": "famous_examples",
                "slug": "costco_loss_leader_rotisserie_chicken",
                "why_trending": "Deconstructs Costco's legendary loss-leader strategy that locks in 90%+ annual membership renewals.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why DTC Brands Are Rushing Back to Target and Walmart Shelves",
                "trend_score": "Industry Realignment Trend",
                "angle": "root_cause_analysis",
                "slug": "dtc_brands_returning_to_wholesale",
                "why_trending": "Explains why Casper, Warby Parker, and Harry's abandoned pure digital models to survive.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Shein Supply Chain Secret: How 500 Garments Become 50,000 in Days",
                "trend_score": "High Search Interest",
                "angle": "mechanisms_and_systems",
                "slug": "shein_micro_batch_supply_chain",
                "why_trending": "Details the proprietary software connecting hundreds of small Guangzhou garment factories.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "TikTok Shop: Why Every Video on Your Feed is Suddenly Selling Sponge Mops",
                "trend_score": "Explosive Social Trend",
                "angle": "field_investigation",
                "slug": "tiktok_shop_affiliate_boom",
                "why_trending": "Analyzes the massive commission payouts driving creators to turn content feeds into infomercials.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The End of Cashier Lines: Did Amazon Just Abandon 'Just Walk Out' Grocery Stores?",
                "trend_score": "High Tech & Business Debate",
                "angle": "deep_dive",
                "slug": "amazon_just_walk_out_pivot",
                "why_trending": "Investigates the reality behind AI cashierless stores relying on human remote reviewers in India.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "108_logistics_supply_chain": {
        "id": "108",
        "slug": "logistics_supply_chain",
        "title": "Logistics & Supply Chain",
        "category": "Commerce_Industry",
        "audience": "Supply Chain Managers, Freight Operators, Procurement Executives, Warehouse Engineers, Global Traders (Global)",
        "progression": [
            ("Tier 1: Containerization, Bullwhip Dynamics & Global Chokepoints (Beginner / Scratch)",
             "Malcolm McLean container revolution, inventory bullwhip math, mega-port gantry mechanics, Toyota JIT principles, and Suez/Panama canal chokepoints."),
            ("Tier 2: Cold Chains, Automation Robotics & Last-Mile Delivery (Intermediate)",
             "Ultra-low reefer pharma chains, Kiva robot automated fulfillment, air cargo belly economics, last-mile doorstep density, and freight forwarder Incoterms."),
            ("Tier 3: Satellite Telematics, Semiconductor Fragility & Nearshoring (Upper Intermediate)",
             "Real-time IoT control towers, Taiwan semiconductor single-point-of-failure risks, closed-loop circular remanufacturing, hazmat logistics, and Mexico nearshoring."),
            ("Tier 4: Autonomous Highway Platooning, Green Fuel & Global Operations (Advanced / Masterclass)",
             "Level 4 autonomous trucking, green methanol container shipping, extreme Antarctic resupply logistics, global cold food networks, and antifragile supply chain architecture.")
        ],
        "flagship": {
            "title": "The Box That Changed the World: How Containerization Built Globalization",
            "angle": "historical_evolution",
            "slug": "108_logistics_supply_chain_historical_evolution_containerization_and_global_trade"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Box That Changed the World: How Containerization Built Globalization",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "containerization_and_global_trade",
                "question": "How did Malcolm McLean's standardized steel shipping container slash ocean freight costs by 90%?",
                "focus": "Break-bulk cargo history, intermodal transport, ISO container standards, and modern port cranes.",
                "reason": "Crucial foundational episode explaining the physical infrastructure enabling all world trade."
            },
            {
                "id": 2,
                "title": "Supply Chain Fundamentals: The Bullwhip Effect and Inventory Dynamics",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "bullwhip_effect_and_inventory",
                "question": "Why does a 5% bump in retail toilet paper sales cause a 40% manufacturing shock up the supply chain?",
                "focus": "Beer game simulation, demand signal distortion, lead time lags, and safety stock oscillations.",
                "reason": "Teaches the core mathematical challenge facing every supply chain planner."
            },
            {
                "id": 3,
                "title": "Inside the Mega-Port: How 20,000 TEU Ships Are Unloaded in 48 Hours",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "inside_the_mega_port",
                "question": "What coordinated logistical choreography turns around giant container vessels around the clock?",
                "focus": "Gantry crane throughput, berth scheduling, straddle carriers, customs inspection, and drayage trucking.",
                "reason": "Provides a vivid visual and operational breakdown of global trade chokepoints."
            },
            {
                "id": 4,
                "title": "Just-In-Time (JIT) vs Just-In-Case: The Toyota Production Legacy",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "jit_vs_just_in_case_logistics",
                "question": "How did Lean manufacturing eliminate factory warehouses, and why did it backfire during pandemic disruptions?",
                "focus": "Taiichi Ohno's Kanban system, zero-inventory philosophy, supplier co-location, and fragility trade-offs.",
                "reason": "Contrasts hyper-efficient inventory theory with real-world black swan vulnerabilities."
            },
            {
                "id": 5,
                "title": "The Geography of Global Chokepoints: Suez, Panama, Malacca, and Bab el-Mandeb",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "case_study",
                "slug": "geography_of_global_trade_chokepoints",
                "question": "Why can a single stuck cargo ship or maritime conflict shut down 12% of total global commerce?",
                "focus": "Canal lock systems, transit toll economics, maritime straits, geopolitical vulnerability, and detour costs.",
                "reason": "Links geographical bottlenecks directly to inflation, factory stoppages, and commodity prices."
            },
            {
                "id": 6,
                "title": "Cold Chain Logistics: How Ice Cream and Vaccines Cross Continents Frozen",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "cold_chain_logistics",
                "question": "What happens when temperature-controlled supply chains fail for single-digit minutes?",
                "focus": "Reefer containers, ultra-low temperature dry-ice shipping, IoT temperature loggers, and pharma compliance.",
                "reason": "Explores the most demanding, high-stakes segment of modern temperature-sensitive logistics."
            },
            {
                "id": 7,
                "title": "Warehouse Automation: Kiva Robots, AS/RS, and the Automated Fulfillment Center",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "warehouse_automation_systems",
                "question": "How do robotic fulfillment centers pick and pack an order within 15 minutes of an online purchase?",
                "focus": "Automated Storage and Retrieval Systems (AS/RS), autonomous mobile robots (AMRs), pick-to-light, and WMS software.",
                "reason": "Shows how robotics transformed dark warehouses into high-speed sorting engines."
            },
            {
                "id": 8,
                "title": "Air Freight Economics: Why Putting Cargo on Planes is Worth 5x the Cost",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "air_freight_economics",
                "question": "When does it make financial sense to fly fresh flowers, smartphones, and auto parts instead of shipping by sea?",
                "focus": "Belly cargo vs dedicated freighters, dimensional weight calculations, speed-to-market depreciation.",
                "reason": "Clarifies the pricing dynamics between maritime transit and high-value aviation cargo."
            },
            {
                "id": 9,
                "title": "Last-Mile Delivery: The Most Expensive and Inefficient Leg of Logistics",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "failure_mode_analysis",
                "slug": "last_mile_delivery_dilemma",
                "question": "Why does the final 5 miles from warehouse to residential doorstep consume over 50% of total delivery costs?",
                "focus": "Route density, failed deliveries, porch piracy, driver turnover, urban parking tickets, and parcel lockers.",
                "reason": "Deconstructs the intractable cost problem at the heart of modern parcel delivery."
            },
            {
                "id": 10,
                "title": "Freight Forwarding Decoded: The Unseen Middlemen Moving Global Freight",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "freight_forwarding_industry",
                "question": "How do freight forwarders navigate customs clearance, bills of lading, and multi-modal carrier contracts?",
                "focus": "Incoterms (FOB, CIF, EXW), ocean carrier consortiums, customs brokers, and digital forwarders.",
                "reason": "Provides vital industry mechanics for international importers and supply chain operators."
            },
            {
                "id": 11,
                "title": "Supply Chain Visibility and Track-and-Trace: Eliminating the Black Hole",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "supply_chain_visibility_tracking",
                "question": "How do satellite AIS tracking, cellular RFID sensors, and API integrations prevent cargo from disappearing?",
                "focus": "Real-time telematics, exception management, predictive ETA algorithms, and supply chain control towers.",
                "reason": "Examines the technological stack giving enterprise logistics managers end-to-end oversight."
            },
            {
                "id": 12,
                "title": "The Semiconductor Supply Chain: The Most Fragile Manufacturing Web on Earth",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "case_study",
                "slug": "semiconductor_supply_chain_fragility",
                "question": "Why does making a single microchip require raw materials and specialized machinery crossing 40 borders?",
                "focus": "ASML lithography monopolies, TSMC fabrication concentration, neon gas and silicon purity supply chains.",
                "reason": "Illustrates peak modern supply chain complexity and extreme geopolitical concentration."
            },
            {
                "id": 13,
                "title": "Circular Logistics and Reverse Material Flows: Industrial Recycling at Scale",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "circular_logistics_closed_loop",
                "question": "How do auto manufacturers and tech giants reclaim lithium batteries and rare earth metals from spent products?",
                "focus": "Closed-loop supply chains, core remanufacturing, scrap collection networks, and regulatory EPR rules.",
                "reason": "Bridges corporate sustainability mandates with profitable remanufacturing infrastructure."
            },
            {
                "id": 14,
                "title": "Dangerous Goods Logistics: Transporting Explosives, Toxins, and Lithium Batteries",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "root_cause_analysis",
                "slug": "dangerous_goods_transport_regulations",
                "question": "What rigid international hazmat protocols prevent cargo planes from catching fire and container ships from exploding?",
                "focus": "IMO IMDG Code, IATA DGR, Class 1-9 hazmat placards, packaging certifications, and catastrophic derailments.",
                "reason": "Teaches essential safety compliance and risk mitigation in hazardous cargo transit."
            },
            {
                "id": 15,
                "title": "Nearshoring and Friendshoring: The Great Supply Chain Decoupling",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "emerging_trends",
                "slug": "nearshoring_friendshoring_trends",
                "question": "Why are multinational corporations shifting production from China to Mexico, Vietnam, and India?",
                "focus": "Geopolitical risk hedging, Section 301 tariffs, labor cost convergence, and cross-border rail links.",
                "reason": "Explores the generational tectonic realignment reshaping international trade geography."
            },
            {
                "id": 16,
                "title": "Autonomous Trucking and Freight Drones: The Unmanned Transit Horizon",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "autonomous_trucking_and_drones",
                "question": "Will Level 4 self-driving semi-trucks solve the chronic global driver shortage on interstate highways?",
                "focus": "Transfer hub models, autonomous highway platooning, regulatory safety approvals, and drone medical deliveries.",
                "reason": "Assesses the real-world timeline and economic impact of unmanned transportation technology."
            },
            {
                "id": 17,
                "title": "Green Shipping Corridors: Decarbonizing Ocean Vessels with Methanol and Ammonia",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "green_shipping_decarbonization",
                "question": "How can the maritime shipping industry, burning 300 million tons of heavy fuel oil, reach net zero?",
                "focus": "Bunker fuel emissions, dual-fuel engines, green hydrogen derivatives, wind-assisted rotor sails, and IMO carbon taxes.",
                "reason": "Tackles the difficult engineering and economic puzzle of decarbonizing global oceanic freight."
            },
            {
                "id": 18,
                "title": "Logistics in Extreme Environments: Supplying Antarctica, Space Stations, and War Zones",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "extreme_environment_logistics",
                "question": "How do humans deliver food, fuel, and replacement parts to locations where failure means immediate death?",
                "focus": "Icebreaker resupply missions, ISS rocket payload constraints, military forward operating base logistics.",
                "reason": "Demonstrates the absolute pinnacle of logistical planning under hostile operating conditions."
            },
            {
                "id": 19,
                "title": "The Global Food Cold Chain: How 8 Billion People Eat Fresh Food Daily",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "ethical_dimensions",
                "slug": "global_food_cold_chain",
                "question": "How does fresh Chilean salmon reach Tokyo sushi counters in 48 hours without spoiling?",
                "focus": "Controlled atmosphere shipping, nitrogen purge preservation, grain silo networks, and food waste reduction.",
                "reason": "Reveals the miracle of agricultural distribution feeding modern urban civilization."
            },
            {
                "id": 20,
                "title": "Designing the Antifragile Supply Chain: The Global Operations Masterclass",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "antifragile_supply_chain_masterclass",
                "question": "How do world-class supply chain architects design networks that grow stronger during global crises?",
                "focus": "Digital twins, multi-echelon inventory optimization, supplier redundancy, and adaptive logistics execution.",
                "reason": "Master synthesis uniting all 20 episodes into an executive-level operational strategy."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "The Red Sea Crisis: How Houthi Missile Attacks Derailed Global Shipping",
                "trend_score": "Massive Geopolitical Spike",
                "angle": "case_study",
                "slug": "red_sea_shipping_crisis",
                "why_trending": "Ships diverting around the Cape of Good Hope added 14 days and billions in fuel costs.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "The Ever Given Suez Disaster: The 6 Days That Paralyzed World Commerce",
                "trend_score": "Extremely High Evergreen Curiosity",
                "angle": "root_cause_analysis",
                "slug": "ever_given_suez_canal_blockage",
                "why_trending": "Deconstructs the hydrodynamic bank suction effect and salvage operation of the stuck megaship.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Panama Canal Drought: Why Ships Paid $4 Million Just to Skip the Queue",
                "trend_score": "High Search Volume Spike",
                "angle": "economic_breakdown",
                "slug": "panama_canal_drought_queue_auction",
                "why_trending": "Freshwater shortages slashed daily transits, triggering crazy multi-million dollar bidding wars.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "How Amazon Built Its Own Cargo Airline to Destroy FedEx and UPS",
                "trend_score": "High Business Interest",
                "angle": "mechanisms_and_systems",
                "slug": "amazon_air_cargo_network",
                "why_trending": "Explains how Amazon built an 80+ jet airline to bypass commercial freight carriers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "Inside the World's Busiest Port: Shanghai's Fully Automated Deepwater Island",
                "trend_score": "High Visual Fascination",
                "angle": "field_investigation",
                "slug": "shanghai_yangshan_deepwater_port",
                "why_trending": "Showcases the unmanned Yangshan automated port operating 24/7 with zero human dockworkers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "Why Cargo Ships Keep Losing Containers at Sea: Rogue Waves and Lashing Failures",
                "trend_score": "High Curiosity Hook",
                "angle": "failure_mode_analysis",
                "slug": "cargo_containers_lost_at_sea",
                "why_trending": "Investigates parametric rolling and structural twist that dumps thousands of steel boxes into the ocean.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "The Baltimore Key Bridge Collapse: How a Container Ship Knocked Out a Port",
                "trend_score": "Global News Spike",
                "angle": "deep_dive",
                "slug": "baltimore_bridge_collapse_logistics",
                "why_trending": "Analyzes the vessel power failure, emergency channel clearing, and East Coast logistics diversion.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "109_railways_trains": {
        "id": "109",
        "slug": "railways_trains",
        "title": "Railways & Trains",
        "category": "Transport_Engineering",
        "audience": "Rail Enthusiasts, Civil Engineers, Transit Advocates, Commuters, Heavy Machinery Fans (Global)",
        "progression": [
            ("Tier 1: Steam Origins, Steel-on-Steel Physics & Track Mechanics (Beginner / Scratch)",
             "Stephenson's Rocket, rolling resistance physics, diesel-electric prime mover alternators, gauge wars, and block signaling safety fail-safes."),
            ("Tier 2: Bullet Trains, Heavy Freight & Underground Metros (Intermediate)",
             "Japanese Shinkansen aerodynamic nose design, 2-mile American distributed power freight, 25kV catenary electrification, TBM subway tunneling, and Trans-Siberian civil construction."),
            ("Tier 3: Derailment Forensics, Maglev Physics & Financial Precision (Upper Intermediate)",
             "Ultrasonic rail flaw detection, 600 km/h Maglev suspension, Precision Scheduled Railroading (PSR) wall street impacts, Swiss alpine rack railways, and European sleeper revival."),
            ("Tier 4: National Transit Policy, Hydrogen Horizons & Intermodal Systems (Advanced / Masterclass)",
             "Why America lacks high-speed rail, hydrogen/battery regional trains, Eurotunnel subsea engineering, historic train heist security forensics, and synchronized Taktfahrplan network design.")
        ],
        "flagship": {
            "title": "The Iron Horse: How the Steam Locomotive Forged the Modern World",
            "angle": "historical_evolution",
            "slug": "109_railways_trains_historical_evolution_history_of_steam_locomotives"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Iron Horse: How the Steam Locomotive Forged the Modern World",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "history_of_steam_locomotives",
                "question": "How did Stephenson's Rocket and early rail networks compress continental transit times from months to days?",
                "focus": "Boiler physics, flanged steel wheels on steel rails, standard gauge evolution, and economic transformation.",
                "reason": "Crucial foundational episode introducing the physics and history of rail transportation."
            },
            {
                "id": 2,
                "title": "The Physics of the Rail: Why Steel on Steel Beats Rubber on Asphalt",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "physics_of_rail_transport",
                "question": "Why can a single freight train move one ton of cargo over 400 miles on a single gallon of diesel?",
                "focus": "Rolling resistance coefficients, kinetic efficiency, track gradient limits, and adhesion physics.",
                "reason": "Teaches the core thermodynamic and mechanical advantages that make rail irreplaceable."
            },
            {
                "id": 3,
                "title": "Inside the Diesel-Electric Locomotive: The Giant Rolling Power Station",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "inside_diesel_electric_locomotive",
                "question": "Why don't modern diesel freight trains have mechanical transmissions or gearboxes?",
                "focus": "V16/V12 prime movers, traction alternators, dynamic braking grids, and AC traction motors.",
                "reason": "Deconstructs the brilliant electro-mechanical engineering powering world freight corridors."
            },
            {
                "id": 4,
                "title": "Rail Gauge Wars: Why the World Has Different Width Tracks",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "rail_gauge_wars_history",
                "question": "Why does standard gauge measure an odd 4 feet 8.5 inches, and why do Russia and Spain use broad gauge?",
                "focus": "Brunel's 7-foot broad gauge, military defense considerations, gauge break transfer points, and variable axles.",
                "reason": "Explains historical infrastructure lock-in and geopolitical track fragmentation."
            },
            {
                "id": 5,
                "title": "Signaling and Safety: From Semaphore Flags to Computerized Interlocking",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "root_cause_analysis",
                "slug": "rail_signaling_and_safety_systems",
                "question": "How do trains traveling 100 mph stop safely when their stopping distance exceeds the engineer's sightline?",
                "focus": "Block signaling, track circuits, Positive Train Control (PTC), European Train Control System (ETCS), and fail-safe logic.",
                "reason": "Demystifies the mission-critical signaling protocols preventing catastrophic train collisions."
            },
            {
                "id": 6,
                "title": "High-Speed Rail Engineering: The Secrets of the 300 km/h Shinkansen",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "high_speed_rail_shinkansen_engineering",
                "question": "How did Japan operate the Shinkansen for 60 years carrying 10 billion passengers with zero fatal derailments?",
                "focus": "Dedicated track alignment, pantograph aerodynamics, tunnel sonic boom countermeasures, and earthquake auto-braking.",
                "reason": "Masterclass on world-class precision engineering and safety culture in passenger rail."
            },
            {
                "id": 7,
                "title": "Heavy Haul Freight: Inside the 2-Mile-Long 20,000-Ton American Freight Trains",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "heavy_haul_freight_operations",
                "question": "How do engineers control slack action and in-train buff forces across 150 loaded railcars?",
                "focus": "Distributed power units (DPU), draft gear dynamics, hump yards, hot box detectors, and crew management.",
                "reason": "Shows the colossal scale and mechanical stress of modern North American and Australian freight operations."
            },
            {
                "id": 8,
                "title": "Electrification Systems: Third Rail, Catenary Wires, and 25kV AC Power",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "rail_electrification_systems",
                "question": "How do electric trains draw continuous megawatts of high-voltage power at high speeds without destroying wires?",
                "focus": "Overhead catenary tensioning, pantograph contact strips, 750V DC third rail, substations, and regenerative braking.",
                "reason": "Details the electrical infrastructure essential for zero-emission urban and intercity rail networks."
            },
            {
                "id": 9,
                "title": "Subway Engineering: How Underground Metros Carve Through Mega-Cities",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "deep_dive",
                "slug": "subway_engineering_tunneling",
                "question": "How do tunnel boring machines (TBMs) chew through bedrock beneath skyscrapers without collapsing streets?",
                "focus": "Earth pressure balance TBMs, cut-and-cover, slurry walls, station excavation, and subway ventilation.",
                "reason": "Explores the underground civil engineering enabling modern high-density metropolitan mobility."
            },
            {
                "id": 10,
                "title": "The Trans-Siberian Railway: Engineering the Longest Train Journey on Earth",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "historical_evolution",
                "slug": "trans_siberian_railway_history",
                "question": "How did tsarist engineers lay 5,700 miles of track across frozen permafrost, Lake Baikal, and taiga forests?",
                "focus": "Permafrost trackbed construction, bridge engineering across Siberian rivers, logistics, and geopolitical impact.",
                "reason": "Chronicles the ultimate endurance feat in railway construction history."
            },
            {
                "id": 11,
                "title": "Derailment Forensics: How Wheel Flanges, Rail Fractures, and Heat Cause Crashes",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "failure_mode_analysis",
                "slug": "train_derailment_forensics",
                "question": "What microscopic metal fatigue flaws or thermal track buckling cause freight cars to jump the rails?",
                "focus": "Sun kinks, ultrasonic rail testing, bearing burnouts, wheel climb dynamics, and NTSB investigation science.",
                "reason": "Rigorous forensic breakdown of rail mechanical failures and structural maintenance."
            },
            {
                "id": 12,
                "title": "Magnetic Levitation (Maglev): Flying on a Magnetic Cushion at 600 km/h",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "emerging_trends",
                "slug": "maglev_train_technology",
                "question": "Why hasn't frictionless magnetic levitation replaced conventional wheeled rail despite its blazing speed?",
                "focus": "Electromagnetic vs electrodynamic suspension (EMS vs EDS), superconducting magnets, guideway costs, and line incompatibility.",
                "reason": "Examines the cutting-edge promise and harsh economic barriers facing Maglev systems."
            },
            {
                "id": 13,
                "title": "Precision Scheduled Railroading (PSR): Wall Street vs Rail Safety and Service",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "economic_breakdown",
                "slug": "precision_scheduled_railroading_psr",
                "question": "How did Hunter Harrison's operating model maximize operating ratios while gutting rail maintenance and workforce?",
                "focus": "Operating ratio metrics, car dwell times, headcount reductions, deferred maintenance risks, and supply chain backlash.",
                "reason": "Exposes the contentious financial engineering that altered the modern freight industry."
            },
            {
                "id": 14,
                "title": "Mountain Rail Engineering: Racks, Pinions, Loops, and Spiral Tunnels",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "mountain_rail_engineering",
                "question": "How do trains conquer 6% mountain grades in the Swiss Alps and Rockies without sliding backward?",
                "focus": "Abt and Strub rack systems, horseshoe curves, spiral tunnels to gain altitude, and the Gotthard Base Tunnel.",
                "reason": "Showcases ingenious civil engineering triumphs over severe topographic barriers."
            },
            {
                "id": 15,
                "title": "Night Trains and Sleeper Service: The Renaissance of Slow Continental Travel",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "philosophical_perspectives",
                "slug": "night_trains_renaissance_europe",
                "question": "Why are European travelers abandoning short-haul airline flights in favor of vintage sleeper compartments?",
                "focus": "Flight shaming (flygskam), Nightjet revival economics, rolling stock refurbishment, and border interoperability.",
                "reason": "Assesses the cultural and environmental revival of comfortable sleeper rail travel."
            },
            {
                "id": 16,
                "title": "Why the United States Lacks High-Speed Rail: Politics, Land, and Freight Rights",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "systemic_critique",
                "slug": "why_us_lacks_high_speed_rail",
                "question": "Why can China build 40,000 km of high-speed rail while California struggles for decades to build a single line?",
                "focus": "Private freight track dispatching priority, eminent domain lawsuits, NEPA environmental reviews, and highway funding biases.",
                "reason": "Comprehensive policy and structural analysis of American transit infrastructure paralysis."
            },
            {
                "id": 17,
                "title": "Hydrogen and Battery Trains: Eliminating Diesel on Non-Electrified Branch Lines",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "hydrogen_battery_trains",
                "question": "Can fuel cell and battery multiple units (BMUs) economically replace diesel locomotives on rural feeder lines?",
                "focus": "Fuel cell power density, hydrogen fueling infrastructure, battery recharging catenaries, and lifecycle carbon emissions.",
                "reason": "Investigates the green transition for regional branch lines where full electrification is too expensive."
            },
            {
                "id": 18,
                "title": "The Channel Tunnel: Connecting Britain to Europe Beneath the Sea",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "case_study",
                "slug": "channel_tunnel_eurotunnel_engineering",
                "question": "How did British and French tunneling crews meet in the middle beneath 31 miles of ocean water with millimeter precision?",
                "focus": "Chalk marl geology, laser-guided TBMs, service tunnel drainage, Eurostar rolling stock, and fire safety systems.",
                "reason": "Celebrates one of the Seven Wonders of the Modern World and its operational mastery."
            },
            {
                "id": 19,
                "title": "The Great Train Robberies and Heists: When Rail Security Failed",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "great_train_robberies_history",
                "question": "How did the 1963 Great Train Robbery and Old West bandits exploit railway isolation to pull off legendary heists?",
                "focus": "Signal tampering, postal sorting cars, railway policing history, and modern armored rail transport security.",
                "reason": "Fascinating historical look at railway crime, physical vulnerabilities, and security evolution."
            },
            {
                "id": 20,
                "title": "The Master Railway Network: Building Integrated Global Rail Systems",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "master_railway_network_architecture",
                "question": "What overarching blueprint balances high-speed passenger corridors, heavy freight throughput, and urban metros?",
                "focus": "Intermodal hubs, timetable synchronization (Taktfahrplan), track maintenance automation, and continental corridor planning.",
                "reason": "Executive masterclass integrating the complete 20-episode railway curriculum into a systemic transit vision."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "China's 45,000 km High-Speed Rail Miracle: How Did They Build It in 15 Years?",
                "trend_score": "Massive Search Volume & Fascination",
                "angle": "case_study",
                "slug": "china_high_speed_rail_expansion",
                "why_trending": "The sheer scale of China's HSR network, viaducts, and CR400 Fuxing trains stuns global viewers.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "East Palestine Derailment: What Really Happened to Norfolk Southern Train 32",
                "trend_score": "Huge Investigative Traffic",
                "angle": "root_cause_analysis",
                "slug": "east_palestine_train_derailment_investigation",
                "why_trending": "Overheated wheel bearing alarms and the vinyl chloride vent-and-burn captivated the nation.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "Why Japan's Bullet Trains Clean 1,000 Seats in Exactly 7 Minutes",
                "trend_score": "Viral Fascination (High Retention)",
                "angle": "field_investigation",
                "slug": "shinkansen_7_minute_cleaning_miracle",
                "why_trending": "Showcases the lightning-fast, military-precision '7-Minute Shinkansen Theater' turnaround ritual.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Brightline Florida: Can America's Only Private Passenger Railroad Make a Profit?",
                "trend_score": "High US Interest & Debate",
                "angle": "economic_breakdown",
                "slug": "brightline_florida_private_rail_economics",
                "why_trending": "Assesses the viability of America's first new private higher-speed passenger line in a century.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Gotthard Base Tunnel: Inside the Deepest and Longest Rail Tunnel in the World",
                "trend_score": "High Engineering Curiosity",
                "angle": "deep_dive",
                "slug": "gotthard_base_tunnel_engineering",
                "why_trending": "Explores the 35-mile tunnel drilled beneath 7,500 feet of Alpine granite.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "India's Vande Bharat Express: The Make-in-India Semi-High-Speed Revolution",
                "trend_score": "Huge Search Volume in South Asia",
                "angle": "emerging_trends",
                "slug": "vande_bharat_express_transformation",
                "why_trending": "Documents Indian Railways' indigenous trainset modernization program replacing vintage locomotive-hauled coaches.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Why Trains Can't Climb Steep Hills: The Slippery Science of Steel on Steel",
                "trend_score": "Evergreen Curiosity Hook",
                "angle": "beginner_guide",
                "slug": "why_trains_cant_climb_steep_hills",
                "why_trending": "Reveals the physics of adhesion sanders, track gradients, and why trains take massive detours around hills.",
                "status": "READY FOR COMPILATION"
            }
        ]
    },

    "110_transportation": {
        "id": "110",
        "slug": "transportation",
        "title": "Transportation",
        "category": "Transport_Engineering",
        "audience": "Urban Planners, Commuters, Policy Makers, Transit Geeks, Automotive & Aviation Observers (Global)",
        "progression": [
            ("Tier 1: Mobility Anthropometrics, Marchetti's Constant & Flow Physics (Beginner / Scratch)",
             "From ancient Roman walking budgets to Marchetti's 60-minute travel law, modal capacity hierarchies (PPHPD), phantom jam shockwaves, and Braess's paradox of induced demand."),
            ("Tier 2: Surface Transit Innovations, Congestion Pricing & Aviation Hubs (Intermediate)",
             "Curitiba Bus Rapid Transit (BRT) mechanics, London/Singapore congestion toll zones, 15-minute city micromobility, airline hub-and-spoke geometry, and passenger ferry transit."),
            ("Tier 3: Mega-Fleet Electrification, Mode Competition & Autonomous Taxis (Upper Intermediate)",
             "Megawatt depot charging for municipal bus fleets, 4-hour HSR vs short-haul aviation tipping points, Waymo/Cruise robotaxi algorithms, runway separation safety, and transit desert equity."),
            ("Tier 4: Exotic Topographies, Speculative Transit & The Unified Metropolis (Advanced / Masterclass)",
             "Medellin urban aerial cable cars, vacuum tube hyperloop thermodynamic limits, eVTOL urban air mobility reality check, suborbital rocketry, and intermodal MaaS metropolitan architecture.")
        ],
        "flagship": {
            "title": "The Evolution of Human Mobility: From Walking Paths to Hypersonic Transit",
            "angle": "historical_evolution",
            "slug": "110_transportation_historical_evolution_evolution_of_human_mobility"
        },
        "curriculum": [
            {
                "id": 1,
                "title": "The Evolution of Human Mobility: From Walking Paths to Hypersonic Transit",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "historical_evolution",
                "slug": "evolution_of_human_mobility",
                "question": "How did human civilization transition from domestic animal pack trains to integrated global transit grids?",
                "focus": "Zahavi's Marchetti's constant, Roman roads, canal eras, motorized mobility, and intermodal transport.",
                "reason": "Crucial foundational episode establishing the universal constants governing human travel behavior."
            },
            {
                "id": 2,
                "title": "Marchetti's Constant: Why Humans Spend Exactly One Hour Traveling Every Day",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "beginner_guide",
                "slug": "marchettis_constant_travel_time",
                "question": "Why has the average human daily commute remained roughly 60 minutes from ancient Rome to modern Tokyo?",
                "focus": "Travel time budget theory, urban sprawl dynamics, speed vs distance trade-offs, and behavioral economics.",
                "reason": "Teaches the core anthropological and urban planning principle governing all transportation systems."
            },
            {
                "id": 3,
                "title": "The Hierarchy of Transit Modes: Speed, Capacity, Energy, and Infrastructure Cost",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "comparative_analysis",
                "slug": "transit_modes_hierarchy_comparison",
                "question": "When should an urban planner choose heavy metro rail over Bus Rapid Transit (BRT) or light rail?",
                "focus": "Passengers per hour per direction (PPHPD), capital expenditure per kilometer, energy efficiency, and lifecycle costs.",
                "reason": "Provides a clear quantitative evaluation framework across all transit modes."
            },
            {
                "id": 4,
                "title": "Traffic Flow Dynamics: The Phantom Traffic Jam and Wave Mechanics",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "mechanisms_and_systems",
                "slug": "phantom_traffic_jam_physics",
                "question": "Why do highways grind to a complete halt even when there is no accident or lane closure ahead?",
                "focus": "Shockwave propagation, driver reaction latency, Nagel-Schreckenberg cellular automata, and variable speed limits.",
                "reason": "Explains the counter-intuitive fluid dynamics and collective psychology of vehicular traffic."
            },
            {
                "id": 5,
                "title": "Induced Demand: Why Adding More Highway Lanes Never Solves Traffic Congestion",
                "tier": "Tier 1: Foundational Frameworks",
                "angle": "root_cause_analysis",
                "slug": "induced_demand_highway_expansion",
                "question": "How did the 26-lane Katy Freeway in Houston end up with longer commute times after a multi-billion dollar expansion?",
                "focus": "Braess's paradox, latent travel demand, triple convergence, and the futility of highway widening.",
                "reason": "Exposes the most pervasive planning myth in modern automobile infrastructure."
            },
            {
                "id": 6,
                "title": "Bus Rapid Transit (BRT): The High-Capacity Subway on Wheels",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "case_study",
                "slug": "bus_rapid_transit_brt_systems",
                "question": "How did Curitiba, Brazil and Bogota's TransMilenio achieve subway-level passenger volumes at 10% of the cost?",
                "focus": "Dedicated median busways, off-board fare collection, level platform boarding, and signal priority.",
                "reason": "Examines the high-efficiency surface transit system transforming developing and mid-sized cities."
            },
            {
                "id": 7,
                "title": "Congestion Pricing: How London, Singapore, and Stockholm Tamed City Traffic",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "economic_breakdown",
                "slug": "congestion_pricing_economics",
                "question": "How does charging drivers a dynamic toll to enter downtown zones revitalize public transit and reduce smog?",
                "focus": "Pigouvian taxes, license plate recognition gantries, revenue reinvestment, and political resistance.",
                "reason": "Deconstructs the most economically proven policy tool for urban traffic management."
            },
            {
                "id": 8,
                "title": "Micromobility and the 15-Minute City: E-Bikes, Scooters, and Walkable Infrastructure",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "practical_playbook",
                "slug": "micromobility_and_15_minute_city",
                "question": "Can lightweight electric bikes and protected bike lanes replace cars for short urban trips under 3 miles?",
                "focus": "First-mile/last-mile solutions, dockless fleet unit economics, street redesign, and Paris's 15-minute city model.",
                "reason": "Explores the explosive growth of low-carbon active transportation in modern cities."
            },
            {
                "id": 9,
                "title": "The Airline Hub-and-Spoke System: How Global Flight Networks Are Built",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "mechanisms_and_systems",
                "slug": "airline_hub_and_spoke_system",
                "question": "Why do airlines route millions of passengers through Atlanta, Dubai, or Doha instead of flying point-to-point?",
                "focus": "Network connectivity math, bank scheduling, fleet utilization, point-to-point budget carriers (Southwest), and alliance codeshares.",
                "reason": "Demystifies the operational logic of commercial aviation networks."
            },
            {
                "id": 10,
                "title": "Maritime Ferries and Water Transits: Moving Millions Across Oceans and Rivers",
                "tier": "Tier 2: Practical Mechanics & Channels",
                "angle": "field_investigation",
                "slug": "maritime_ferries_water_transit",
                "question": "How do commuter ferry networks like Hong Kong's Star Ferry and Staten Island Ferry integrate with city transit?",
                "focus": "Ro-Pax vessel design, pier boarding ergonomics, electric hydrofoil technology, and weather resilience.",
                "reason": "Details waterborne transit systems serving coastal and archipelagic populations."
            },
            {
                "id": 11,
                "title": "The Fleet Electrification Challenge: Charging Megawatts, Battery Degradation, and Grid Strain",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "deep_dive",
                "slug": "fleet_electrification_grid_strain",
                "question": "What happens to municipal power grids when 5,000 city buses and garbage trucks plug in simultaneously at night?",
                "focus": "Depot megawatt charging infrastructure, smart load balancing, vehicle-to-grid (V2G), and battery chemistry lifecycles.",
                "reason": "Tackles the difficult infrastructure reality of transitioning municipal fleets off fossil fuels."
            },
            {
                "id": 12,
                "title": "High-Speed Rail vs Short-Haul Flights: The Continental Mobility Duel",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "comparative_analysis",
                "slug": "high_speed_rail_vs_short_haul_flights",
                "question": "At what travel distance does high-speed rail decisively destroy airline market share?",
                "focus": "The 4-hour door-to-door tipping point, airport security delays, carbon intensity comparisons, and French short-haul flight bans.",
                "reason": "Quantifies the competitive boundary between commercial aviation and terrestrial bullet trains."
            },
            {
                "id": 13,
                "title": "Autonomous Robotaxis: Waymo, Cruise, and the Battle for Driverless Mobility",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "emerging_trends",
                "slug": "autonomous_robotaxis_urban_mobility",
                "question": "Will fleets of self-driving robotaxis eliminate personal car ownership, or will they flood streets with empty vehicles?",
                "focus": "LiDAR sensor suites, edge-case remote assistance, cost per mile economics, and municipal regulatory battles in San Francisco and Phoenix.",
                "reason": "Analyzes the technological reality, business models, and societal impacts of autonomous ride-hailing."
            },
            {
                "id": 14,
                "title": "Airport Design and Airspace Operations: Managing 2,000 Flights a Day",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "cross_disciplinary",
                "slug": "airport_design_airspace_operations",
                "question": "How do air traffic controllers and runway dispatchers orchestrate aircraft landings every 45 seconds?",
                "focus": "Runway separation minima, wake turbulence categories, NextGen satellite navigation, and airport terminal layouts.",
                "reason": "Reveals the complex civil engineering and air traffic coordination keeping world skies safe."
            },
            {
                "id": 15,
                "title": "Transit Deserts and Mobility Equity: Who Gets Left Behind Without a Car?",
                "tier": "Tier 3: Strategic & Advanced Architectures",
                "angle": "ethical_dimensions",
                "slug": "transit_deserts_mobility_equity",
                "question": "How does car-centric urban design trap low-income households in cycles of poverty and lengthy multi-bus commutes?",
                "focus": "Spatial mismatch hypothesis, transit accessibility mapping, fare-capping policies, and paratransit services.",
                "reason": "Examines the profound socioeconomic and moral dimensions of public transportation access."
            },
            {
                "id": 16,
                "title": "Urban Cable Cars and Aerial Gondolas: Transit Over Steep Mountains and Slums",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "famous_examples",
                "slug": "urban_cable_cars_gondolas_medellin",
                "question": "How did Medellin's Metrocable transform isolated, crime-ridden hillside barrios into thriving connected communities?",
                "focus": "Aerial ropeway engineering, top-station integration, low capex construction, and social urbanism impact.",
                "reason": "Inspiring case study on unconventional transit solutions overcoming severe topography."
            },
            {
                "id": 17,
                "title": "Hyperloop and Evacuated Tube Transit: Physics Triumph or Expensive Pipe Dream?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "failure_mode_analysis",
                "slug": "hyperloop_vacuum_tube_transit_critique",
                "question": "Why did Elon Musk's 700 mph vacuum-tube train collapse under the harsh realities of thermal expansion and safety vacuums?",
                "focus": "Kantrowitz limit, tube expansion joint leaks, emergency decompression risks, and astronomical tunneling capital costs.",
                "reason": "Rigorous engineering post-mortem separating sci-fi marketing from thermodynamic feasibility."
            },
            {
                "id": 18,
                "title": "Electric Vertical Takeoff and Landing (eVTOL): The Flying Car Reality Check",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "emerging_trends",
                "slug": "evtol_flying_cars_reality_check",
                "question": "Will urban air taxis ferry executives across congested cities, or are they unviable noise hazards for the ultra-rich?",
                "focus": "Distributed electric propulsion, acoustic noise signatures, vertiport airspace integration, and FAA certification hurdles.",
                "reason": "Provides a sober engineering evaluation of the emerging urban aviation sector."
            },
            {
                "id": 19,
                "title": "Spaceports and Suborbital Transit: 90 Minutes from London to Sydney?",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "philosophical_perspectives",
                "slug": "suborbital_spaceport_point_to_point_transit",
                "question": "Can Starship-style rocket point-to-point travel ever become commercially viable for regular human transportation?",
                "focus": "Atmospheric re-entry thermal loads, g-force physiological limits, sonic boom overland bans, and launch infrastructure economics.",
                "reason": "Explores the absolute outer boundary of human intercontinental speed and mobility."
            },
            {
                "id": 20,
                "title": "The Unified Intermodal Metropolis: The Master Urban Mobility Architecture",
                "tier": "Tier 4: Future Horizons & Masterclasses",
                "angle": "masterclass",
                "slug": "unified_intermodal_metropolis_masterclass",
                "question": "How do world-class cities like Tokyo, Zurich, and Singapore weave rail, bus, walking, and shared micro-mobility into a seamless web?",
                "focus": "Mobility-as-a-Service (MaaS), single-ticket integration, transit-oriented development (TOD), and zero-emission transit networks.",
                "reason": "Definitive capstone masterclass synthesizing all 20 episodes into an actionable masterplan for the future of transportation."
            }
        ],
        "trending": [
            {
                "id": 21,
                "title": "Why New York City's Congestion Pricing Toll Was Suddenly Paused",
                "trend_score": "Massive Political & Transit Debate",
                "angle": "deep_dive",
                "slug": "nyc_congestion_pricing_pause_controversy",
                "why_trending": "The dramatic last-minute halt of America's first congestion pricing zone sparked national fury and debate.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 22,
                "title": "Waymo vs Human Drivers: Inside San Francisco's Driverless Taxi Reality",
                "trend_score": "Viral Fascination Spike",
                "angle": "field_investigation",
                "slug": "waymo_san_francisco_robotaxi_experience",
                "why_trending": "Real rider reactions, safety statistics, and bizarre traffic standoff videos dominate social feeds.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 23,
                "title": "The Katy Freeway Paradox: Why Widening This Highway Made Traffic Worse",
                "trend_score": "Evergreen High Retention Hook",
                "angle": "case_study",
                "slug": "katy_freeway_widening_paradox",
                "why_trending": "The definitive visual example proving induced demand to millions of frustrated commuters.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 24,
                "title": "Why Tokyo's Rail System Never Has Delays: The Secret Behind Zero Accidents",
                "trend_score": "High Admiration & Curiosity",
                "angle": "mechanisms_and_systems",
                "slug": "tokyo_transit_efficiency_secrets",
                "why_trending": "Deconstructs point-and-call safety rituals, private railway competition, and station mega-hubs.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 25,
                "title": "The Death of the Hyperloop: How a $400 Million Dream Went Bankrupt",
                "trend_score": "High Tech Post-Mortem Traffic",
                "angle": "root_cause_analysis",
                "slug": "hyperloop_one_bankruptcy_post_mortem",
                "why_trending": "Investigates the closure of Hyperloop One and why vacuum tube transit couldn't overcome physical reality.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 26,
                "title": "How Paris Banned Cars and Created a Cycling Paradise in 4 Years",
                "trend_score": "Urban Design Viral Trend",
                "angle": "practical_playbook",
                "slug": "paris_cycling_transformation_anne_hidalgo",
                "why_trending": "Mayor Anne Hidalgo's radical conversion of traffic lanes into protected bike boulevards inspired cities worldwide.",
                "status": "READY FOR COMPILATION"
            },
            {
                "id": 27,
                "title": "Can Flying Taxis Replace Helicopters? Inside the Archer and Joby eVTOL Tests",
                "trend_score": "Futuristic Tech Surge",
                "angle": "emerging_trends",
                "slug": "evtol_air_taxis_joby_archer",
                "why_trending": "FAA test flights and airline partnerships with United and Delta bring electric air taxis to the brink of launch.",
                "status": "READY FOR COMPILATION"
            }
        ]
    }
}

def main():
    print("Generating suites for Batch 106-110...")
    for folder, meta in BATCH_106_110.items():
        process_niche(folder, meta)
    update_master_readme()
    print("Batch 106-110 complete!")

if __name__ == "__main__":
    main()
