"""
Core Topics Suite Generation Engine
Provides reusable functions for writing Roadmaps, Reports, status JSON, and updating topics/README.md.
"""

import os
import json
from pathlib import Path

ROOT_DIR = Path(r"h:\script-raw-")
TOPICS_DIR = ROOT_DIR / "topics"
REGISTRY_DIR = ROOT_DIR / "REGISTRY" / "Niches"
OUTPUT_DIR = ROOT_DIR / "OUTPUT"

def load_angle_plan(niche_folder_name):
    ap_path = REGISTRY_DIR / niche_folder_name / "ANGLE_PLAN.json"
    if not ap_path.exists():
        raise FileNotFoundError(f"Missing angle plan: {ap_path}")
    with open(ap_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_roadmap_md(meta, angle_plan):
    niche_id = meta["id"]
    niche_slug = meta["slug"]
    niche_title = meta["title"]
    category = meta["category"]
    audience = meta["audience"]
    progression = meta["progression"]
    flagship = meta["flagship"]
    curriculum = meta["curriculum"]

    roadmap_filename = f"{niche_id}_{niche_slug.upper()}_CHANNEL_TOPIC_ROADMAP.md"

    md = []
    md.append(f"# {niche_title} Channel Master Topic Roadmap (Scratch to Advanced)")
    md.append(f"**Niche:** {niche_id} {niche_title} ({category})  ")
    md.append(f"**Channel Language:** English (YouTube)  ")
    md.append(f"**Target Audience:** {audience}  ")
    format_text = meta.get("production_format", "10 to 30-Minute In-Depth Documentary Explainer Episodes (600s–1800s, 75–225 Fixed 8s Scenes)")
    md.append(f"**Production Format:** {format_text}  ")
    md.append(f"**Execution & Sync Report:** [topics/{niche_id}_{niche_slug}/TOPICS_COVERED_REPORT.md](./TOPICS_COVERED_REPORT.md)  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Channel Progression Strategy")
    md.append("")
    md.append(f"This curriculum organizes the core disciplines of {niche_title} across four progressive tiers:")
    for tier_name, tier_desc in progression:
        md.append(f"- **{tier_name}** — {tier_desc}")
    md.append("")
    md.append("---")
    md.append("")
    
    angles = angle_plan.get("angles", [])
    md.append(f"## 2. Topic Styles & Narrative Angles ({len(angles)} Curated Formats)")
    md.append("")
    md.append(f"Every episode is produced using one of the {len(angles)} niche angle presets defined in [`REGISTRY/Niches/{niche_id}_{niche_slug}/ANGLE_PLAN.json`](file:///h:/script-raw-/REGISTRY/Niches/{niche_id}_{niche_slug}/ANGLE_PLAN.json):")
    md.append("")
    md.append("| # | Angle Slug / Style | Primary Angle Focus | Core Story Question Formulated |")
    md.append("|---|---|---|---|")
    for idx, a in enumerate(angles, 1):
        slug = a.get("slug", "")
        angle_name = a.get("angle", "")
        q = a.get("question", "")
        md.append(f"| {idx} | `{slug}` | **{angle_name}** | *{q}* |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Topic Catalog (Scratch to Advanced Curriculum)")
    md.append("")

    current_tier = ""
    for item in curriculum:
        tier = item["tier"]
        if tier != current_tier:
            current_tier = tier
            md.append(f"### {current_tier}")
        question_text = item.get("question", item.get("core_question", ""))
        focus_text = item.get("key_focus", item.get("focus", ""))
        md.append(f"{item['id']}. **{item['title']}**")
        md.append(f"   - *Question:* {question_text}")
        md.append(f"   - *Key Focus:* {focus_text}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 4. Flagship Launch Episode")
    md.append(f"- **Niche ID:** {niche_id} ({niche_title})")
    md.append(f"- **Angle Preset:** `{flagship['angle']}`")
    md.append(f"- **Episode Title:** *{flagship['title']}*")
    md.append(f"- **Episode Slug:** `{flagship['slug']}`")
    flagship_duration = flagship.get("duration", "10 to 30 Minutes (600s–1800s / 75–225 Scenes @ 8s fixed, expandable to 20m & 30m deep dives)")
    md.append(f"- **Duration:** {flagship_duration}")
    md.append(f"- **Execution:** Full Phases 0–5 Autonomous Production Package inside `OUTPUT/{niche_id}_{niche_slug}/`.")
    md.append("")

    return "\n".join(md)

def generate_report_md(meta, angle_plan):
    niche_id = meta["id"]
    niche_slug = meta["slug"]
    niche_title = meta["title"]
    category = meta["category"]
    curriculum = meta["curriculum"]
    trending = meta["trending"]
    roadmap_filename = f"{niche_id}_{niche_slug.upper()}_CHANNEL_TOPIC_ROADMAP.md"

    md = []
    md.append(f"# {niche_id} {niche_title} -- Master Topic Execution & Roadmap Sync Report")
    md.append(f"> **Niche:** {niche_id} {niche_title} ({category})  ")
    md.append(f"> **Storage Directory:** `topics/{niche_id}_{niche_slug}/`  ")
    md.append(f"> **Synchronized With:** `OUTPUT/{niche_id}_{niche_slug}/`, `REGISTRY/Niches/{niche_id}_{niche_slug}/`, and `{roadmap_filename}`  ")
    md.append(f"> **Last Synced:** `2026-10-21 17:15:00`  ")
    report_format = meta.get("report_format", "10–30 Minute Deep-Dive Episodes (600s–1800s, 75–225 Fixed 8s Scenes, Strict 4.2–5.6s VO Ceiling)")
    md.append(f"> **Production Format:** {report_format}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Executive Progress Summary")
    md.append("")
    md.append("| Metric | Count | Percentage | Status |")
    md.append("|---|---|---|---|")
    md.append(f"| **Topics Completed & Produced (Phases 0-5)** | **0** | **0.0%** | `IN PIPELINE (Ready for Batch Production)` |")
    md.append(f"| **Curriculum Topics Pending Production** | **{len(curriculum)}** | **74.1%** | `QUEUED (Foundational 4-Tier Curriculum)` |")
    md.append(f"| **New High-Retention Trending Candidates** | **{len(trending)}** | **25.9%** | `READY FOR VIRAL / RETENTION EXPANSION` |")
    md.append(f"| **Total Tracked Master Catalog** | **{len(curriculum) + len(trending)}** | **100%** | `Active Production Pipeline` |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Covered Topics (Done / Produced in OUTPUT)")
    md.append(f"*Currently, {niche_id} is queued for batch script compilation. No episodes have finalized Phase 5 audit in OUTPUT directory yet.*")
    md.append("")
    md.append("| # | Topic Title | Curriculum Tier | Angle Preset | Associated Output Folder & Files | Status |")
    md.append("|---|---|---|---|---|---|")
    md.append(f"| - | *No episodes compiled yet* | - | - | [OUTPUT/{niche_id}_{niche_slug}](../../OUTPUT/{niche_id}_{niche_slug}) | `QUEUED FOR BATCH COMPILATION` |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Pending Master Curriculum Topics (Scratch to Advanced Roadmap)")
    md.append("")
    md.append("| # | Proposed Topic Title | Target Tier | Angle Preset | Recommended Slug | Why It Matters | Status |")
    md.append("|---|---|---|---|---|---|---|")
    for item in curriculum:
        status_tag = "`QUEUED (Priority #1 Launch)`" if item["id"] == 1 else "`QUEUED`"
        md.append(f"| {item['id']} | **{item['title']}** | {item['tier']} | `{item['angle']}` | `{item['slug']}` | {item['reason']} | {status_tag} |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Trending & High-Retention Topics (Algorithm & Search Optimized)")
    md.append("")
    md.append("| # | Trending Video Concept | Trend Velocity | Angle Preset | Recommended Slug | Retention Hook & Value | Status |")
    md.append("|---|---|---|---|---|---|---|")
    for idx, item in enumerate(trending, 21):
        item_id = item.get("id", idx)
        if item_id <= 7:
            item_id = idx
        title = item.get("title", "")
        trend_score = item.get("trend_score", item.get("estimated_views", "High Global Velocity"))
        angle = item.get("angle", "famous_examples")
        slug = item.get("slug", title.lower().replace(" ", "_").replace(":", "").replace("'", "").replace("?", "").replace(",", "").replace('"', ""))
        why_trending = item.get("why_trending", item.get("why_it_works", item.get("hook", "")))
        status = item.get("status", "TRENDING CANDIDATE")
        md.append(f"| {item_id} | **{title}** | **{trend_score}** | `{angle}` | `{slug}` | {why_trending} | `{status}` |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 4. Cross-Document Sync & File Linkages")
    md.append("This report is wired directly into the repository structure:")
    md.append(f"- **Master Channel Roadmap:** [`topics/{niche_id}_{niche_slug}/{roadmap_filename}`](./{roadmap_filename})")
    md.append(f"- **Machine Status File:** [`topics/{niche_id}_{niche_slug}/topics_status.json`](./topics_status.json)")
    md.append(f"- **Niche Registry Home:** [`REGISTRY/Niches/{niche_id}_{niche_slug}/NICHE_{niche_id}_{niche_slug}.md`](file:///h:/script-raw-/REGISTRY/Niches/{niche_id}_{niche_slug}/NICHE_{niche_id}_{niche_slug}.md)")
    md.append(f"- **Category Configuration:** [`REGISTRY/Niches/{niche_id}_{niche_slug}/CAT_{niche_id}_{niche_slug}.md`](file:///h:/script-raw-/REGISTRY/Niches/{niche_id}_{niche_slug}/CAT_{niche_id}_{niche_slug}.md)")
    md.append(f"- **Angle Plan Data:** [`REGISTRY/Niches/{niche_id}_{niche_slug}/ANGLE_PLAN.json`](file:///h:/script-raw-/REGISTRY/Niches/{niche_id}_{niche_slug}/ANGLE_PLAN.json)")
    md.append(f"- **Output Landing Directory:** [`OUTPUT/{niche_id}_{niche_slug}/`](file:///h:/script-raw-/OUTPUT/{niche_id}_{niche_slug}/)")
    md.append("")
    md.append("---")
    md.append("*Generated by Script-Raw Workspace Topic Tracking Engine.*")
    md.append("")

    return "\n".join(md)

def generate_status_json(meta):
    niche_id = meta["id"]
    niche_slug = meta["slug"]
    curriculum = meta["curriculum"]
    trending = meta["trending"]

    pending_list = []
    for item in curriculum:
        status_val = "QUEUED (Priority #1 Launch)" if item["id"] == 1 else "QUEUED"
        pending_list.append({
            "id": item["id"],
            "title": item["title"],
            "tier": item["tier"],
            "angle": item["angle"],
            "slug": item["slug"],
            "reason": item["reason"],
            "status": status_val
        })

    normalized_trending = []
    for idx, item in enumerate(trending, 21):
        item_id = item.get("id", idx)
        if item_id <= 7:
            item_id = idx
        title = item.get("title", "")
        slug = item.get("slug", title.lower().replace(" ", "_").replace(":", "").replace("'", "").replace("?", "").replace(",", "").replace('"', ""))
        normalized_trending.append({
            "id": item_id,
            "title": title,
            "trend_score": item.get("trend_score", item.get("estimated_views", "High Global Velocity")),
            "angle": item.get("angle", "famous_examples"),
            "slug": slug,
            "why_trending": item.get("why_trending", item.get("why_it_works", item.get("hook", ""))),
            "status": item.get("status", "TRENDING CANDIDATE")
        })

    data = {
        "niche_id": niche_id,
        "niche_name": niche_slug,
        "last_synced": "2026-10-21T18:50:00.000000",
        "summary": {
            "completed": 0,
            "pending": len(curriculum),
            "trending": len(normalized_trending),
            "total": len(curriculum) + len(normalized_trending)
        },
        "completed_topics": [],
        "pending_topics": pending_list,
        "trending_topics": normalized_trending
    }
    return data

def process_niche(folder_name, meta):
    niche_dir = TOPICS_DIR / folder_name
    niche_dir.mkdir(parents=True, exist_ok=True)

    angle_plan = load_angle_plan(folder_name)

    # 1. Roadmap markdown
    roadmap_filename = f"{meta['id']}_{meta['slug'].upper()}_CHANNEL_TOPIC_ROADMAP.md"
    roadmap_path = niche_dir / roadmap_filename
    roadmap_content = generate_roadmap_md(meta, angle_plan)
    with open(roadmap_path, "w", encoding="utf-8") as f:
        f.write(roadmap_content)

    # 2. Report markdown
    report_path = niche_dir / "TOPICS_COVERED_REPORT.md"
    report_content = generate_report_md(meta, angle_plan)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    # 3. Status JSON
    status_path = niche_dir / "topics_status.json"
    status_data = generate_status_json(meta)
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(status_data, f, indent=2)

    print(f"[OK] Generated suite for {folder_name}")

def update_master_readme():
    entries = []
    for d in sorted(os.listdir(TOPICS_DIR)):
        dp = TOPICS_DIR / d
        if not dp.is_dir() or not (dp / "topics_status.json").exists():
            continue
        with open(dp / "topics_status.json", "r", encoding="utf-8") as f:
            status = json.load(f)
        
        nid = status.get("niche_id", d.split("_")[0])
        name_map = {
            "001": "AI + Technology Explainers",
            "002": "History / Mystery Documentary",
            "003": "Ancient India / Civilization",
            "004": "Sanatan / Hindu Mythology",
            "005": "Documentary Storytelling",
            "006": "Science & Big Questions",
            "007": "AI Tools / AI Tutorials",
            "008": "Personal Finance",
            "009": "Psychology / Human Behavior",
            "010": "True Crime Documentary",
            "011": "Horror / Mystery Stories",
            "012": "Space / Universe",
            "013": "Ancient Technology / Lost Knowledge",
            "014": "Geopolitics / World History",
            "015": "Health / Wellness / Education",
            "016": "Motivational Stories",
            "017": "Kids Cartoon Stories",
            "018": "Mythological Animation",
            "019": "AI Cinematic Short Films",
            "020": "Travel / Hidden Places",
            "021": "Luxury / Rich Lifestyle",
            "022": "Cars / Automotive Stories",
            "023": "Spirituality / Meditation",
            "024": "Food / Cultural Stories",
            "025": "Gaming Stories / Lore",
            "026": "Medical / Human Science",
            "027": "Genetics / Evolution",
            "028": "Ocean / Deep Sea",
            "029": "Dinosaurs / Prehistoric World",
            "030": "Earth / Natural Mysteries",
            "031": "Megastructures / Engineering",
            "032": "Space Exploration",
            "033": "UFO / Extraterrestrial",
            "034": "Exploration / Adventure",
            "035": "Military History",
            "036": "Royalty / Dynasties",
            "037": "Castles / Forts / Palaces",
            "038": "Maps / Geography Mysteries",
            "039": "Archaeology",
            "040": "Ancient Manuscripts / Books",
            "041": "Languages / Linguistics",
            "042": "Art & Civilization",
            "043": "Music History",
            "044": "Sports History",
            "045": "Racing",
            "046": "Disaster Survival",
            "047": "Aviation",
            "048": "Maritime",
            "049": "Pirates & Outlaws",
            "050": "Treasure Hunting",
            "051": "Industrial / Manufacturing Stories",
            "052": "Architecture",
            "053": "Future Civilization",
            "054": "Consciousness & Philosophy",
            "055": "Time & Reality",
            "056": "Puzzles & Intellectual Mysteries",
            "057": "Secret Societies",
            "058": "Folklore & Legends",
            "059": "Mythical Creatures",
            "060": "Symbols & Hidden Meanings",
            "061": "Software & Programming",
            "062": "Computer & PC",
            "063": "Consumer Technology",
            "064": "Home & Lifestyle",
            "065": "Gardening & Plants",
            "066": "Wildlife & Animals",
            "067": "Nature Documentary",
            "068": "Pets",
            "069": "Education",
            "070": "Career & Jobs",
            "071": "Productivity & Self-Improvement",
            "072": "Relationships",
            "073": "Parenting & Child Development",
            "074": "Personal Travel",
            "075": "Pilgrimage & Sacred Places",
            "076": "World Religions & Civilization",
            "077": "Yoga & Wellness",
            "078": "Books & Literature",
            "079": "Creative Arts",
            "080": "Film & Entertainment Analysis",
            "081": "Theatre & Performing Arts",
            "082": "Fashion & Clothing",
            "083": "Jewelry & Precious Materials",
            "084": "Collectibles & Antiques",
            "085": "DIY & Making",
            "086": "Restoration",
            "087": "How Things Work",
            "088": "How It's Made",
            "089": "Inventions & Inventors",
            "090": "Why Channel",
            "091": "Cooking & Culinary",
            "092": "Beverage Culture",
            "093": "Agriculture & Farming",
            "094": "Rural Life & Village Culture",
            "095": "Handicrafts & Traditional Skills",
            "096": "Museums & Cultural Heritage",
            "097": "Government & Public Systems",
            "098": "Law & Justice",
            "099": "Intelligence & Espionage",
            "100": "Forensics & Investigation",
            "101": "Memory & Learning",
            "102": "Communication",
            "103": "Leadership & Management",
            "104": "Corporate & Workplace",
            "105": "Consumer Psychology",
            "106": "Marketing & Advertising",
            "107": "Retail & E-Commerce",
            "108": "Logistics & Supply Chain",
            "109": "Railways & Trains",
            "110": "Transportation",
            "111": "Cities & Urbanism",
            "112": "Real Estate",
            "113": "Energy & Power",
            "114": "Water",
            "115": "Forests & Ecology",
            "116": "Mountains",
            "117": "Adventure & Extreme Sports",
            "118": "Scientists & Discoverers",
            "119": "Mathematics",
            "120": "Logic & Critical Thinking",
            "121": "Statistics & Data",
            "122": "Journalism & Media History",
            "123": "Television History",
            "124": "Radio & Audio",
            "125": "Podcasting",
            "126": "Photography",
            "127": "Visual Effects",
            "128": "Virtual Reality & AR",
            "129": "Internet History",
            "130": "Internet Mysteries",
            "131": "Game Development",
            "132": "Retro Gaming",
            "133": "Board Games & Tabletop",
            "134": "Chess",
            "135": "Collecting",
            "136": "Shopping & Consumer Guides",
            "137": "Repair & Maintenance",
            "138": "Bicycles & Cycling",
            "139": "Motorcycles",
            "140": "Sailing & Yachting",
            "141": "Traditional Skills",
            "142": "Primitive Technology",
            "143": "Living History",
            "144": "History of Education",
            "145": "School & University Stories",
            "146": "Famous People",
            "147": "Biography Storytelling",
            "148": "Humanitarian Stories",
            "149": "Global Cultures",
            "150": "Nomadic Civilizations",
            "151": "Islands",
            "152": "Volcanoes",
            "153": "Ice & Polar Worlds",
            "154": "Microbiology",
            "155": "Biotechnology",
            "156": "Chemistry in Everyday Life",
            "157": "Materials Science",
            "158": "Batteries & Energy Storage",
            "159": "Satellites & Earth Observation",
            "160": "Data Centers & Infrastructure",
            "161": "Electricity & Electronics",
            "162": "Engineering Failures",
            "163": "Records & Extremes",
            "164": "Rankings & Comparisons",
            "165": "Then vs Now",
            "166": "Future Predictions",
            "167": "What If & Alternative Reality",
            "168": "Sociology",
            "169": "Community Stories",
            "170": "Human Relationships",
            "171": "Human Behavior",
            "172": "Social Experiments",
            "173": "Family History",
            "174": "Aging & Generations",
            "175": "Childhood History",
            "176": "Youth Culture",
            "177": "Women's History",
            "178": "Men's History",
            "179": "Disability History",
            "180": "Healthcare Systems",
            "181": "Hospital Stories",
            "182": "Emergency Services",
            "183": "Public Safety",
            "184": "Firefighting",
            "185": "Rescue Stories",
            "186": "Survival Psychology",
            "187": "Outdoor Life",
            "188": "Backpacking",
            "189": "Hiking",
            "190": "Camping",
            "191": "Fishing",
            "192": "Beekeeping",
            "193": "Insects",
            "194": "Arachnids",
            "195": "Reptiles",
            "196": "Birds",
            "197": "Marine Mammals",
            "198": "Marine Life",
            "199": "Coral Reefs",
            "200": "Botany",
            "201": "Flowers",
            "202": "Trees",
            "203": "Fungi",
            "204": "Plant Intelligence",
            "205": "Ecosystems",
            "206": "Deserts",
            "207": "Rainforests",
            "208": "Wetlands",
            "209": "Mangroves",
            "210": "Rivers",
            "211": "Waterfalls",
            "212": "Beaches",
            "213": "Glaciers",
            "214": "Snow & Ice",
            "215": "Extreme Weather",
            "216": "Lightning",
            "217": "Clouds & Atmosphere",
            "218": "World Geography",
            "219": "Indian Geography",
            "220": "Indian Cities",
            "221": "Indian Villages",
            "222": "Temple Tourism",
            "223": "Pilgrimage Travel",
            "224": "Himalayan Travel",
            "225": "Desert Travel",
            "226": "Island Travel",
            "227": "Train Travel",
            "228": "Road Trips",
            "229": "Hotel Stories",
            "230": "Hospitality",
            "231": "Resorts",
            "232": "Travel Hacks",
            "233": "Travel Systems",
            "234": "Airports",
            "235": "Borders",
            "236": "Territories",
            "237": "Microstates",
            "238": "Unrecognized Countries",
            "239": "Enclaves & Exclaves",
            "240": "Sacred Geography",
            "241": "Caves",
            "242": "National Parks",
            "243": "Cultural Traditions",
            "244": "Festivals Around the World",
            "245": "Festival Origins",
            "246": "Wedding Culture",
            "247": "Traditional Clothing",
            "248": "Folk Traditions",
            "249": "Folk Theatre",
            "250": "Dolls & Puppetry",
            "281": "Ayurveda"
        }
        pretty_name = name_map.get(nid)
        if not pretty_name:
            niche_file = REGISTRY_DIR / d / f"NICHE_{d}.md"
            if niche_file.exists():
                try:
                    with open(niche_file, "r", encoding="utf-8") as nf:
                        for line in nf:
                            if line.startswith("Title:"):
                                pretty_name = line.replace("Title:", "").strip()
                                break
                except Exception:
                    pass
        if not pretty_name:
            pretty_name = d.split("_", 1)[1].replace("_", " ").title()
        summary = status.get("summary", {})
        comp = summary.get("completed", 0)
        pend = summary.get("pending", 0)
        trend = summary.get("trending", 0)
        entries.append((nid, pretty_name, comp, pend, trend, d))

    entries.sort(key=lambda x: int(x[0]))

    lines = [
        "# Topics Master Registry",
        "",
        "Central index of topics covered, pending roadmap queues, and trending suggestions across all production niches.",
        "",
        "## Active Niches Tracked",
        "",
        "| Niche ID | Niche Name | Completed Episodes | Pending Queue | Trending Ideas | Report Link |",
        "|---|---|---|---|---|---|"
    ]

    for nid, name, comp, pend, trend, folder in entries:
        lines.append(f"| **{nid}** | **{name}** | **{comp}** | **{pend}** | **{trend}** | [{folder} Report](./{folder}/TOPICS_COVERED_REPORT.md) |")

    lines.extend([
        "",
        "### Structure",
        "Each niche under `topics/` mirrors the naming conventions of `OUTPUT/<niche>/`:",
        "- `topics/<niche_folder>/TOPICS_COVERED_REPORT.md` — Human-readable status & roadmap breakdown.",
        "- `topics/<niche_folder>/topics_status.json` — Machine-readable status synced with pipeline compilers.",
        ""
    ])

    with open(TOPICS_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Updated master registry at {TOPICS_DIR / 'README.md'} with {len(entries)} niches.")
