#!/usr/bin/env python3
"""
V6 Niche Populator — Master-Driven Generation (6-Folder Structure)
=====================================================================
500 niches distributed into 6 topic folders, using 11 CAT presets.

Topic folders: AI_Film, Business_Money, Cartoon_Animation,
               Documentary, Sanatan_Dharma, Science_Future
CAT presets:   11 files in Categories/
"""

import re
import csv
from pathlib import Path
from reconcile_config_presets import SCHEMA, answers

BASE = Path(__file__).resolve().parent
TOPICS_DIR = BASE / "REGISTRY" / "Topics"
CATEGORIES_DIR = BASE / "REGISTRY" / "Categories"
MASTER_REGISTRY = BASE / "REGISTRY" / "MASTER_REGISTRY.md"
MASTER_VISUAL = BASE / "REGISTRY" / "MASTER_VISUAL_STYLE.md"
TAXONOMY = BASE / "REGISTRY" / "NICHE_TAXONOMY.csv"

QUESTIONS = [
    ("Q2",  "Target Audience"),
    ("Q3",  "Story Angle"),
    ("Q4",  "Financial Detail Level"),
    ("Q5",  "Data Visualization Priority"),
    ("Q6",  "Interview/Expert Segments"),
    ("Q7",  "Controversy Level"),
    ("Q8",  "Legal Liability Concern"),
    ("Q9",  "Personality Focus"),
    ("Q10", "Controversial Facts Included"),
    ("Q11", "Industry Expertise Level Needed"),
    ("Q12", "Competitive/Comparative Content"),
    ("Q13", "Monetization Priority"),
    ("Q14", "Total Duration"),
    ("Q15", "Visual Style Primary"),
    ("Q16", "Voiceover Approach"),
    ("Q17", "Delivery Format"),
    ("Q18", "Primary Language"),
    ("Q19", "Additional Languages"),
    ("Q20", "On-Screen Text Strategy"),
    ("Q21", "Graphics Requirement"),
    ("Q22", "Ending Tone"),
    ("Q23", "Industry Accuracy Priority"),
    ("Q24", "Source Quality Requirements"),
    ("Q25", "Update Frequency"),
    ("Q26", "Platform Distribution"),
    ("Q27", "Production Quality Level"),
    ("Q28", "Audience Geographic Focus"),
    ("Q29", "Factual Verification Timeline"),
    ("Q30", "Expert Interview Access"),
    ("Q31", "Controversial Claim Inclusion"),
    ("Q32", "Competitor/Comparison Fairness"),
    ("Q33", "Current Events Included"),
    ("Q34", "Bias Prevention Strategy"),
    ("Q35", "Sponsored Content"),
    ("Q36", "Monetization Revenue Model"),
    ("Q37", "Series/Playlist Strategy"),
    ("Q38", "SEO Keyword Priority"),
    ("Q39", "Content Warning/Disclaimer Needed"),
    ("Q40", "Video Generation Method"),
    ("Q41", "Content Safety Level"),
    ("Q42", "Scene Duration Strategy"),
]

STATIC_DEFAULTS = {
    "Q2":  "General Public",
    "Q3":  "Education Focus",
    "Q4":  "Not Applicable",
    "Q5":  "Minimal",
    "Q6":  "Quotes Only (scholars/experts)",
    "Q7":  "Balanced",
    "Q8":  "Low",
    "Q9":  "Personality-Driven",
    "Q10": "No",
    "Q11": "General knowledge",
    "Q12": "Not Applicable",
    "Q13": "Secondary",
    "Q14": "10-15 minutes",
    "Q15": "Animated Explainers",
    "Q16": "Engaging Storytelling",
    "Q17": "Single video or Series",
    "Q18": "English",
    "Q19": "English subtitles",
    "Q20": "Moderate",
    "Q21": "Important",
    "Q22": "Forward-looking / Inspirational",
    "Q23": "Mixed audience",
    "Q24": "Standard",
    "Q25": "One-off videos",
    "Q26": "YouTube + Shorts",
    "Q27": "Premium",
    "Q28": "Global (India-first)",
    "Q29": "Thorough",
    "Q30": "Some (scholars)",
    "Q31": "No",
    "Q32": "Not Applicable",
    "Q33": "Historical only",
    "Q34": "Show perspectives",
    "Q35": "No sponsorships",
    "Q36": "AdSense + Sponsorship",
    "Q37": "Themed playlist",
    "Q38": "Specific names + long-tail",
    "Q39": "Educational disclaimer",
    "Q40": "AI Video (animation)",
    "Q41": "Standard",
    "Q42": "VARIABLE (per content type)",
}

SUBNICHE_OVERRIDES = {
    "History & Origins":          {"Q3": "History & Origins", "Q15": "Archive Footage",                       "Q16": "Professional Authoritative"},
    "Famous Examples":            {"Q3": "Famous Examples",   "Q15": "Stock Footage + Graphics",              "Q16": "Engaging Storytelling"},
    "Hidden Stories":             {"Q3": "Hidden Stories",    "Q15": "Documentary Realism",                   "Q16": "Documentary Calm"},
    "Beginner Explainers":        {"Q3": "Education Focus",   "Q15": "Animated Explainers",                   "Q16": "Engaging Storytelling"},
    "Advanced Concepts":          {"Q3": "Advanced Concepts", "Q15": "Data Viz Heavy",                        "Q16": "Professional Authoritative"},
    "Mysteries & Unsolved Cases": {"Q3": "Mystery",           "Q15": "Documentary Realism",                   "Q16": "Critical Analytical"},
    "Technology & Innovation":    {"Q3": "Innovation Focus",  "Q15": "Animation + Data Viz",                  "Q16": "Enthusiastic"},
    "People & Personalities":     {"Q3": "People Focus",      "Q15": "Stock Footage + Graphics",              "Q16": "Engaging Storytelling"},
    "Major Events":               {"Q3": "Major Events",      "Q15": "Archive Footage",                       "Q16": "Professional Authoritative"},
    "How It Works":               {"Q3": "Education Focus",   "Q15": "Animated Explainers",                   "Q16": "Engaging Storytelling"},
    "Rise & Fall":                {"Q3": "Rise/Fall Narrative","Q15": "Timeline Visualization",               "Q16": "Engaging Storytelling"},
    "Then vs Now":                {"Q3": "Then vs Now",       "Q15": "Data Viz Heavy",                        "Q16": "Professional Authoritative"},
    "Future Developments":        {"Q3": "Innovation Focus",  "Q15": "Animation + Data Viz",                  "Q16": "Enthusiastic"},
    "Myths vs Facts":             {"Q3": "Myths vs Facts",    "Q15": "Infographics + Text Overlay",           "Q16": "Critical Analytical"},
    "Documentary Stories":        {"Q3": "Documentary Focus", "Q15": "Documentary + Interview Hybrid",        "Q16": "Documentary Calm"},
}

QUESTION_OPTIONS = {
    "Q2":  "General Public / Specialized / Children / Students / Professionals / Scholars",
    "Q3":  "Mythology / History & Origins / Famous Examples / Hidden Stories / Beginner Explainers / Advanced Concepts / Mysteries & Unsolved / Technology & Innovation / People & Personalities / Major Events / Documentary Stories / Rise/Fall Narrative / Then vs Now / Future Developments / Myths vs Facts / Innovation Focus / Education Focus / Mystery / People Focus",
    "Q4":  "Not Applicable / Simple / Moderate / Heavy / Detailed",
    "Q5":  "Heavy / Moderate / Minimal / None",
    "Q6":  "Include Interviews / Quotes Only / Documentary Style / No Interviews",
    "Q7":  "Avoid / Balanced / Investigative / Expose",
    "Q8":  "No / Low / Moderate / High",
    "Q9":  "Personality-Driven / Business-Driven / Balanced / Not Applicable / People Focus",
    "Q10": "No / Some debated / Contested / Yes",
    "Q11": "General / Some background / Significant / Highly specialized",
    "Q12": "No competitors / One alternative / Multiple / Ranking / Not Applicable",
    "Q13": "Not important / Secondary / Important / Critical",
    "Q14": "5-8 min / 8-12 min / 12-15 min / 15-25+ min",
    "Q15": "Animation + Data Viz / Documentary Realism / Animated Explainers / Archive Footage / Infographics + Text Overlay / Minimalist / Live action / Stock Footage + Graphics / Data Viz Heavy / Timeline Visualization / Sacred Cinematic Devotional / Cinematic / 2D Animation / 3D Animation / Motion Graphics",
    "Q16": "Professional Authoritative / Engaging Storytelling / Documentary Calm / Enthusiastic / Critical Analytical / Calm Devotional / Sacred",
    "Q17": "Single video / Series / Season / Documentary series",
    "Q18": "English / Hindi / Sanskrit / Bilingual / Other / Tamil / Telugu / Bengali / Marathi / Gujarati",
    "Q19": "None / One / Multiple",
    "Q20": "Minimal / Moderate / Heavy / Captions + Graphics",
    "Q21": "Essential / Important / Secondary / Minimal",
    "Q22": "Happy/Success / Bittersweet / Failure/Cautionary / Unresolved/Mystery / Forward-looking / Inspirational",
    "Q23": "General audience / Professionals / Mixed / Expert-focused",
    "Q24": "Standard / High / Critical / Academic",
    "Q25": "One-off / Weekly / Bi-weekly / Monthly / As-needed",
    "Q26": "YouTube only / YouTube + Shorts / Multi-platform / Instagram / TikTok",
    "Q27": "Standard / Premium / Cinema / Documentary professional",
    "Q28": "Global / India / US / Other / UK / Europe / Asia / Middle East",
    "Q29": "Quick / Standard / Thorough / Investigative",
    "Q30": "No / Some (1-2) / Extensive",
    "Q31": "No / Minor / Major",
    "Q32": "No / Fair / Ranking / Critical / Not Applicable",
    "Q33": "Historical only / Some recent / Very current / Not Applicable",
    "Q34": "Acknowledge limits / Show perspectives / Cite sources / All three",
    "Q35": "No / Sponsored / Affiliate links",
    "Q36": "AdSense / Sponsorship / Patreon / Multiple",
    "Q37": "Standalone / Part of series / Themed playlist / Channel-wide universe",
    "Q38": "General / Specific names / Trending / Long-tail",
    "Q39": "No / Educational / Controversy / Investment / Disclaimer",
    "Q40": "AI Video / Standard animation / Live action / Data viz + interviews / AI Generated / Real Footage / Hybrid",
    "Q41": "Standard / Strict / Platform-specific",
    "Q42": "FIXED 8-SECOND / VARIABLE (per content type)",
}

SUBNICHE_TYPES = [
    "History & Origins",
    "Famous Examples",
    "Hidden Stories",
    "Beginner Explainers",
    "Advanced Concepts",
    "Mysteries & Unsolved Cases",
    "Technology & Innovation",
    "People & Personalities",
    "Major Events",
    "How It Works",
    "Rise & Fall",
    "Then vs Now",
    "Future Developments",
    "Myths vs Facts",
    "Documentary Stories",
]


# ─── Topic folder mapping (niche_id -> folder) ─────────────────────────────

TOPIC_FOLDER_MAP = {
    1:  "AI_Film",
    2:  "Documentary",
    3:  "Sanatan_Dharma",
    4:  "Sanatan_Dharma",
    6:  "Science_Future",
    7:  "AI_Film",
    10: "Documentary",
    11: "Documentary",
    12: "Science_Future",
    14: "Documentary",
    17: "Cartoon_Animation",
    18: "Cartoon_Animation",
    19: "AI_Film",
    23: "Sanatan_Dharma",
    25: "Cartoon_Animation",
    26: "Science_Future",
    27: "Science_Future",
    28: "Science_Future",
    29: "Science_Future",
    30: "Science_Future",
    31: "Science_Future",
    32: "Science_Future",
    33: "Documentary",
    35: "Documentary",
    36: "Documentary",
    38: "Documentary",
    39: "Documentary",
    57: "Sanatan_Dharma",
}

# ─── CAT mapping (niche_id -> cat_name) ────────────────────────────────────

CAT_NAME_MAP = {
    1:  "InnovationTech",
    2:  "ScienceExplainer",
    3:  "SanatanDevotional",
    4:  "SanatanDevotional",
    6:  "ScienceExplainer",
    7:  "AIDrama",
    10: "ScienceExplainer",
    11: "ScienceExplainer",
    12: "ScienceExplainer",
    14: "ScienceExplainer",
    17: "CartoonKids",
    18: "CartoonKids",
    19: "AIDrama",
    23: "SanatanDevotional",
    25: "CartoonKids",
    26: "ScienceExplainer",
    27: "ScienceExplainer",
    28: "ScienceExplainer",
    29: "ScienceExplainer",
    30: "ScienceExplainer",
    31: "ScienceExplainer",
    32: "ScienceExplainer",
    33: "ScienceExplainer",
    35: "ScienceExplainer",
    36: "ScienceExplainer",
    38: "ScienceExplainer",
    39: "ScienceExplainer",
    57: "SanatanDevotional",
}


# ─── Parsers ───────────────────────────────────────────────────────────────

def parse_master_registry():
    with open(MASTER_REGISTRY, "r", encoding="utf-8") as f:
        content = f.read()

    niches = []
    current_id = None
    current_name = None
    current_subniches = []

    for line in content.splitlines():
        m = re.match(r'^##\s+(\d+)\.\s+(.+)$', line)
        if m:
            if current_id is not None:
                niches.append((current_id, current_name, current_subniches))
            current_id = int(m.group(1))
            current_name = m.group(2).strip()
            current_subniches = []
            continue

        if current_id and line.strip():
            sm = re.match(r'^\d+\.\s+(.+?)\s+—\s+(.+)$', line.strip())
            if sm:
                current_subniches.append((sm.group(1).strip(), sm.group(2).strip()))

    if current_id is not None:
        niches.append((current_id, current_name, current_subniches))
    return niches


def parse_visual_style():
    with open(MASTER_VISUAL, "r", encoding="utf-8") as f:
        content = f.read()

    styles = {}
    for line in content.splitlines():
        m = re.match(r'^\|\s*(\d+)\s*\|(.+)$', line)
        if m:
            niche_id = int(m.group(1))
            cells = [c.strip() for c in m.group(2).split('|')]
            if len(cells) >= 11:
                styles[niche_id] = {
                    "niche":                cells[0],
                    "primary_visual_style": cells[1],
                    "visual_language":      cells[2],
                    "palette":              cells[3],
                    "lighting":             cells[4],
                    "camera":               cells[5],
                    "motion":               cells[6],
                    "thumbnail_direction":  cells[7],
                    "ai_keywords":          cells[8],
                    "avoid":                cells[9],
                }
    return styles


def load_cat_presets():
    """Load all CAT preset files. Returns dict: cat_name -> {qid: (default, options)}"""
    cats = {}
    for f in sorted(CATEGORIES_DIR.glob("CAT_*.md")):
        cat_name = f.stem.replace("CAT_", "")
        cats[cat_name] = parse_cat_file(f)
    return cats


def parse_cat_file(path):
    """Parse a CAT_*.md file. Returns dict: Q_id -> (default, options_string)."""
    cat = {}
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    for line in content.splitlines():
        m = re.match(r'^##\s+(Q\d+):\s+(.+)$', line)
        if m:
            qid = m.group(1)
            label = m.group(2).strip()
            # Next line is the default
            # Look ahead for Options line
            cat[qid] = {"label": label, "default": "", "options": ""}
        elif line.startswith("**Default:**"):
            # Find the last Q we saw
            last_q = None
            for q in reversed(list(cat.keys())):
                last_q = q
                break
            if last_q and cat[last_q]["default"] == "":
                cat[last_q]["default"] = line.replace("**Default:**", "").strip()
        elif line.startswith("Options:"):
            last_q = None
            for q in reversed(list(cat.keys())):
                last_q = q
                break
            if last_q and cat[last_q]["options"] == "":
                cat[last_q]["options"] = line.replace("Options:", "").strip()

    return cat


# ─── Helpers ───────────────────────────────────────────────────────────────

def slugify(name):
    slug = name.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_/]+', '_', slug)
    slug = re.sub(r'_+', '_', slug)
    return slug.strip('_')[:60]


# ─── CAT matching by keyword ───────────────────────────────────────────────

def build_cat_keyword_map():
    cat_keywords = {}
    for f in sorted(CATEGORIES_DIR.glob("CAT_*.md")):
        cat_name = f.stem.replace("CAT_", "")
        with open(f, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r'^>\s+Applies to:\s+(.+)$', line)
                if m:
                    kws = [kw.strip().lower() for kw in re.split(r',\s*', m.group(1))]
                    cat_keywords[cat_name] = kws
                    break
    return cat_keywords


def assign_cat(niche_id, niche_name, cat_keywords):
    # 1) Explicit ID mapping takes priority
    if niche_id in CAT_NAME_MAP:
        return CAT_NAME_MAP[niche_id]

    # 2) Keyword match against CAT "Applies to" lines
    name_lower = niche_name.lower()
    best_cat = "BusinessStories"
    best_len = 0
    for cat_name, kws in cat_keywords.items():
        for kw in kws:
            if kw in name_lower and len(kw) > best_len:
                best_cat = cat_name
                best_len = len(kw)
    return best_cat


# ─── Topic preset generation ───────────────────────────────────────────────

def generate_topic_preset(niche_id, niche_name, sub_niche_name, sub_niche_type,
                           cat_name, cat_presets, visual_style):
    slug = slugify(niche_name)
    type_slug = slugify(sub_niche_type)
    topic_id = f"{niche_id:03d}_{slug}_{type_slug}"

    # Canonical defaults < category override < topic angle and visual style.
    values = answers(cat_name, sub_niche_type,
                     visual_style.get("primary_visual_style") if visual_style else None)
    q_lines = []
    for qid, definition in list(SCHEMA["questions"].items())[1:]:
        q_lines.append(f"## {qid}: {definition['label']}\n**Default:** {values[qid]}\n")

    # Visual style block
    vs_block = ""
    if visual_style:
        vs_block = (
            f"\n---\n\n"
            f"## Visual Style (MASTER_VISUAL_STYLE.md row {niche_id})\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"| Primary Visual Style | {visual_style.get('primary_visual_style', 'N/A')} |\n"
            f"| Visual Language | {visual_style.get('visual_language', 'N/A')} |\n"
            f"| Palette | {visual_style.get('palette', 'N/A')} |\n"
            f"| Lighting | {visual_style.get('lighting', 'N/A')} |\n"
            f"| Camera / Lens | {visual_style.get('camera', 'N/A')} |\n"
            f"| Motion | {visual_style.get('motion', 'N/A')} |\n"
            f"| Thumbnail Direction | {visual_style.get('thumbnail_direction', 'N/A')} |\n"
            f"| AI Prompt Keywords | {visual_style.get('ai_keywords', 'N/A')} |\n"
            f"| Avoid | {visual_style.get('avoid', 'N/A')} |\n"
        )

    content = (
        f"# {topic_id}: \"{sub_niche_name}\" -- Topic Preset\n\n"
        f"> Domain: {niche_name} | Sub-type: {sub_niche_type}\n"
        f"> Category: {cat_name} | Topic Folder: {slug}\n"
        f"> Production Preset: CAT_{cat_name}.md\n"
        f"> Visual Style ID: {niche_id}\n\n"
        f"---\n\n"
        f"{''.join(q_lines)}"
        f"{vs_block}\n"
    )
    return topic_id, content


def generate_index(niche_name, niche_id, entries):
    lines = [
        f"# {niche_name} -- All Topics",
        "",
        f"> Niche ID: {niche_id} | {len(entries)} topic presets",
        "> Auto-generated from MASTER_REGISTRY.md + MASTER_VISUAL_STYLE.md",
        "",
        "---",
        "",
    ]
    for sn_name, sn_type, filename in entries:
        lines.append(f"- [{sn_name} ({sn_type})](./{filename})")
    lines.append("")
    return "\n".join(lines)


# ─── Main ──────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("V6 Niche Populator -- Master-Driven Generation")
    print("=" * 60)

    print("\n[1/6] Loading CAT presets...")
    cat_presets = load_cat_presets()
    cat_keywords = build_cat_keyword_map()
    print(f"  Loaded {len(cat_presets)}: {sorted(cat_presets.keys())}")

    print("\n[2/6] Parsing MASTER_REGISTRY.md...")
    niches = parse_master_registry()
    print(f"  Found {len(niches)} niches, {sum(len(sn) for _, _, sn in niches)} sub-niches")

    print("\n[3/6] Parsing MASTER_VISUAL_STYLE.md...")
    visual_styles = parse_visual_style()
    print(f"  Loaded {len(visual_styles)} visual style profiles")

    print("\n[4/6] Assigning categories...")
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        taxonomy = {int(row["id"]): row for row in csv.DictReader(fh)}
    if set(taxonomy) != {niche_id for niche_id, _, _ in niches}:
        raise ValueError("Taxonomy IDs must exactly match the master registry")
    topic_map = {}
    folder_counts = {}
    cat_counts = {}

    for niche_id, niche_name, sub_niches in niches:
        cat_name = taxonomy[niche_id]["primary_category"]
        if cat_name not in cat_presets:
            raise ValueError(f"Missing category preset CAT_{cat_name}.md")
        tf = taxonomy[niche_id]["primary_category"]
        folder_counts[tf] = folder_counts.get(tf, 0) + 1
        cat_counts[cat_name] = cat_counts.get(cat_name, 0) + 1
        topic_map.setdefault(tf, []).append(
            (niche_id, niche_name, sub_niches, cat_name)
        )

    for tf, count in sorted(folder_counts.items()):
        print(f"  {tf}: {count} niches")
    print(f"  CAT distribution: {cat_counts}")

    print("\n[5/6] Generating files...")
    total_files = 0
    for tf, entries in topic_map.items():
        folder = TOPICS_DIR / tf
        folder.mkdir(parents=True, exist_ok=True)

        for niche_id, niche_name, sub_niches, cat_name in entries:
            slug = taxonomy[niche_id]["slug"]
            domain_path = folder / slug
            domain_path.mkdir(parents=True, exist_ok=True)

            visual_style = visual_styles.get(niche_id)
            index_entries = []

            for sn_name, sn_type in sub_niches:
                topic_id, content = generate_topic_preset(
                    niche_id, niche_name, sn_name, sn_type,
                    cat_name, cat_presets, visual_style
                )
                type_slug = slugify(sn_type)
                filename = f"{topic_id}.md"
                target = domain_path / filename
                if not target.exists():
                    with open(target, "w", encoding="utf-8") as f:
                        f.write(content)
                index_entries.append((sn_name, sn_type, filename))
                total_files += 1

            index = domain_path / "ALL_TOPICS_BY_NICHE.md"
            if not index.exists():
                with open(index, "w", encoding="utf-8") as f:
                    f.write(generate_index(niche_name, niche_id, index_entries))

    print(f"\n  Generated {total_files} topic preset files")
    print(f"  Topic folders: {sorted(topic_map.keys())}")

    print("\n[6/6] Verifying...")
    actual_files = sum(1 for _ in TOPICS_DIR.rglob("*.md"))
    print(f"  Total .md files: {actual_files}")
    print("=" * 60)
    print("DONE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
