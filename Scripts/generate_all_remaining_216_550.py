import os
import sys
import json
import re
from pathlib import Path

# Add script directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent))
from generate_topics_suite_helper import process_niche, update_master_readme

ROOT_DIR = Path(r"h:\script-raw-")
REGISTRY_DIR = ROOT_DIR / "REGISTRY" / "Niches"
TOPICS_DIR = ROOT_DIR / "topics"

def clean_slug(text):
    s = text.lower()
    for ch in [' ', ':', '-', '—', '/', '\\', '(', ')', ',', '.', '?', '!', '\'', '"', '&', '%', ';', '@', '#']:
        s = s.replace(ch, '_')
    while '__' in s:
        s = s.replace('__', '_')
    return s.strip('_')[:60]

def parse_niche_metadata(folder_name):
    reg_dir = REGISTRY_DIR / folder_name
    nid, nslug = folder_name.split('_', 1)
    
    # 1. NICHE file for official Title and Subject category
    niche_file = reg_dir / f"NICHE_{folder_name}.md"
    title = nslug.replace('_', ' ').title()
    category = "General"
    if niche_file.exists():
        with open(niche_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("Title:"):
                    title = line.replace("Title:", "").strip()
                elif line.startswith("Subject category:"):
                    category = line.replace("Subject category:", "").strip()
    
    # 2. CAT file for Target Audience default
    cat_file = reg_dir / f"CAT_{folder_name}.md"
    base_aud = "General Public"
    if cat_file.exists():
        c = cat_file.read_text(encoding="utf-8")
        m = re.search(r'## Q2: Target Audience\s*\n\*\*Default:\*\*\s*(.+)', c)
        if m:
            base_aud = m.group(1).strip()
    audience = f"{title} Researchers, Domain Specialists, Documentary Viewers, {base_aud} (Global)"

    # 3. ANGLE_PLAN.json
    ap_file = reg_dir / "ANGLE_PLAN.json"
    if not ap_file.exists():
        raise FileNotFoundError(f"Missing ANGLE_PLAN.json in {reg_dir}")
    with open(ap_file, "r", encoding="utf-8") as f:
        angle_plan = json.load(f)

    angles = angle_plan.get("angles", [])
    purpose = angle_plan.get("purpose", f"{title} comprehensive documentary and analytical studies.")

    # 4. Progression tiers
    progression = [
        (f"Tier 1: {title} Foundations & Core Mechanisms (Beginner / Scratch)",
         f"Core physical and conceptual fundamentals, terminology, primary mechanisms, and foundational observation methods in {title}."),
        (f"Tier 2: {title} Methodological Deep Dives & Empirical Evidence (Intermediate)",
         f"Detailed instrumentation, measurement metrics, classification systems, and documented case studies of {title}."),
        (f"Tier 3: {title} Advanced Systemic Paradigms & Comparative Dynamics (Upper Intermediate)",
         f"Complex systemic interactions, historical shifts, anomalous patterns, and comparative analyses across different contexts in {title}."),
        (f"Tier 4: {title} Frontier Technologies, Global Impact & Future Horizons (Advanced / Masterclass)",
         f"Emerging technological breakthroughs, policy frameworks, environmental and human impact, and long-term evolutionary projections for {title}.")
    ]

    tier_names = [
        "Tier 1: Foundational Frameworks",
        "Tier 2: Methodological Deep Dives",
        "Tier 3: Advanced Analytical Paradigms",
        "Tier 4: Frontier Systems & Interdisciplinary Paradigms"
    ]

    # 5. Curriculum: exactly 20 topics across 4 tiers (5 per tier)
    curriculum = []
    used_angle_indices = set()
    for idx in range(1, 21):
        tier_idx = (idx - 1) // 5
        tier_label = tier_names[tier_idx]
        
        # Pick angle from angle_plan
        a_idx = (idx - 1) % len(angles)
        used_angle_indices.add(a_idx)
        a = angles[a_idx]
        
        a_slug = a.get("slug", "explainer")
        a_name = a.get("angle", f"Core Principles of {title}")
        q_text = a.get("question", f"What are the defining characteristics and mechanisms of {a_name}?")
        scope = a.get("scope", "")
        evidence = a.get("evidence", "")
        
        # Clean angle name to avoid duplicating Title if already present
        clean_a_name = a_name
        if clean_a_name.lower().startswith(title.lower() + ":"):
            clean_a_name = clean_a_name[len(title) + 1:].strip()
        elif clean_a_name.lower().startswith(title.lower() + " -"):
            clean_a_name = clean_a_name[len(title) + 2:].strip()
        elif clean_a_name.lower().startswith(title.lower() + " —"):
            clean_a_name = clean_a_name[len(title) + 2:].strip()
        elif clean_a_name.lower().startswith(title.lower()):
            clean_a_name = clean_a_name[len(title):].strip()
        if not clean_a_name:
            clean_a_name = a_name
        
        if idx == 1:
            t_title = f"The Architecture of {title}: {clean_a_name}"
        else:
            t_title = f"{title}: {clean_a_name}"
        
        focus_text = f"{scope} Evidence base: {evidence}." if evidence else scope
        if not focus_text:
            focus_text = f"Primary focus on {clean_a_name.lower()} through empirical data and verifiable observations."
            
        reason_text = f"A rigorous pedagogical investigation exploring {clean_a_name.lower()} through documented evidence."
        
        topic_slug = clean_slug(f"{title}_{clean_a_name}")
        curriculum.append({
            "id": idx,
            "title": t_title,
            "tier": tier_label,
            "angle": a_slug,
            "slug": topic_slug,
            "question": q_text,
            "focus": focus_text,
            "reason": reason_text
        })

    # 6. Flagship launch episode
    flagship = {
        "title": curriculum[0]["title"],
        "angle": curriculum[0]["angle"],
        "slug": f"{nid}_{nslug}_deep_dive_{clean_slug(curriculum[0]['title'])}",
        "duration": "10 to 30 Minutes (600s–1800s / 75–225 Scenes @ 8s fixed, expandable to 20m & 30m deep dives)"
    }

    # 7. Trending candidates: exactly 7 topics (IDs 21 to 27)
    trending_presets = [
        (21, 98, "extreme_case", "Record Extremes & Superlatives", "Extreme boundary conditions and anomalous phenomena recorded across the domain."),
        (22, 96, "mysteries_unsolved_cases", "Unsolved Mysteries & Enigmas", "Perplexing anomalies, unexplained occurrences, and contested findings under scientific review."),
        (23, 95, "technology_innovation", "Technological Breakthroughs & Modern Sensors", "Next-generation instrumentation, cutting-edge mapping, and computational modeling innovations."),
        (24, 94, "myths_vs_facts", "Debunking Myths & Common Misconceptions", "Popular misconceptions, viral fallacies, and empirical reality tested against primary data."),
        (25, 93, "major_events", "Catastrophes, Turning Points & Historical Milestones", "High-impact historical events, crises, and watershed discoveries that reshaped understanding."),
        (26, 92, "hidden_stories", "The Untold Human Stories & Behind-the-Scenes Pioneers", "Overlooked researchers, field observers, and frontline specialists whose labor shaped the field."),
        (27, 91, "documentary_stories", "Investigative Exposés & Global Transformations", "Deep forensic investigations into emerging crises, environmental shifts, and structural transformations.")
    ]

    # Map available angles by slug
    angles_by_slug = {a.get("slug"): a for a in angles}

    trending = []
    for t_id, score, pref_slug, fallback_angle, fallback_scope in trending_presets:
        if pref_slug in angles_by_slug:
            match = angles_by_slug[pref_slug]
            m_angle = match.get("angle", fallback_angle)
            if m_angle.lower().startswith(title.lower() + ":"):
                m_angle = m_angle[len(title) + 1:].strip()
            elif m_angle.lower().startswith(title.lower() + " -"):
                m_angle = m_angle[len(title) + 2:].strip()
            elif m_angle.lower().startswith(title.lower() + " —"):
                m_angle = m_angle[len(title) + 2:].strip()
            elif m_angle.lower().startswith(title.lower()):
                m_angle = m_angle[len(title):].strip()
            if not m_angle:
                m_angle = fallback_angle
            m_q = match.get("question", "")
            t_title = f"{title}: {m_angle}"
            why_text = f"High viral search interest exploring {m_q.rstrip('?').lower()} backed by field records." if m_q else f"High audience retention curiosity regarding {fallback_scope.lower()}."
            a_slug = pref_slug
        else:
            t_title = f"{title}: {fallback_angle}"
            why_text = f"High audience retention curiosity regarding {fallback_scope.lower()}."
            a_slug = pref_slug
            
        trending.append({
            "id": t_id,
            "title": t_title,
            "trend_score": score,
            "angle": a_slug,
            "slug": clean_slug(f"{title}_{pref_slug}"),
            "why_trending": why_text,
            "status": "Queued"
        })

    meta = {
        "id": nid,
        "slug": nslug,
        "title": title,
        "category": category,
        "audience": audience,
        "production_format": "10 to 30-Minute In-Depth Documentary Explainer Episodes (600s–1800s, 75–225 Fixed 8s Scenes)",
        "report_format": "10–30 Minute Deep-Dive Episodes (600s–1800s, 75–225 Fixed 8s Scenes, Strict 4.2–5.6s VO Ceiling)",
        "progression": progression,
        "flagship": flagship,
        "curriculum": curriculum,
        "trending": trending
    }
    return meta

def run_master_generation():
    print("=" * 70)
    print("STARTING MASTER TOPIC SUITE GENERATION ENGINE (NICHES 216 TO 550)")
    print("=" * 70)

    # Collect target niches 216 to 550
    niche_dirs = sorted([
        d for d in os.listdir(REGISTRY_DIR)
        if os.path.isdir(REGISTRY_DIR / d)
        and d[:3].isdigit()
        and 216 <= int(d[:3]) <= 550
    ])

    total = len(niche_dirs)
    print(f"Targeting {total} niches for autonomous generation...")

    success_count = 0
    errors = []

    for idx, folder in enumerate(niche_dirs, 1):
        try:
            meta = parse_niche_metadata(folder)
            process_niche(folder, meta)
            success_count += 1
            if idx % 25 == 0 or idx == total:
                print(f"[{idx:03d}/{total:03d}] Progress: Processed {folder} (Total success: {success_count})")
        except Exception as e:
            errors.append((folder, str(e)))
            print(f"[ERROR] Failed to process {folder}: {e}")

    print("-" * 70)
    print(f"Compilation finished. Successfully generated suites for {success_count} / {total} niches.")
    if errors:
        print(f"Encountered {len(errors)} errors:")
        for err_folder, err_msg in errors:
            print(f"  - {err_folder}: {err_msg}")
    else:
        print("All target niches generated with zero errors!")

    print("Updating master registry index at topics/README.md...")
    update_master_readme()
    print("=" * 70)
    print("MASTER GENERATION COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    run_master_generation()
