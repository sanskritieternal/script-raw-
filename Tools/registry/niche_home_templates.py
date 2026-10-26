"""Canonical renderers for one niche CAT, identity and output landing."""

def render_cat(row, values, schema):
    stem = f"{row['id']}_{row['slug']}"
    lines = [f"# CAT_{stem} - Niche Configuration", "",
             f"> Niche ID: {row['id']} | Subject category: {row['primary_category']}",
             f"> Schema: {schema['version']} | Editable Q1-Q42 defaults for this niche", "",
             "This is the only niche-level source of Q answers. The selected angle sets Q3; explicit episode answers have final precedence.", ""]
    for qid, definition in schema["questions"].items():
        lines.extend([f"## {qid}: {definition['label']}", f"**Default:** {values[qid]}"])
    return "\n".join(lines) + "\n"


def render_identity(row):
    stem = f"{row['id']}_{row['slug']}"
    visual_source = "MASTER_VISUAL_STYLE_EXTENSION.md" if int(row["id"]) > 500 else "MASTER_VISUAL_STYLE.md"
    topic_tracking = ("Topics covered & pending report: "
                      "[TOPICS_COVERED_REPORT.md](../../../topics/281_ayurveda/TOPICS_COVERED_REPORT.md)\n") if int(row["id"]) == 281 else ""
    return (f"# NICHE_{stem} - Identity and Planning\n\n"
            f"Niche ID: {row['id']}\nTitle: {row['title']}\nSubject category: {row['primary_category']}\n"
            f"Configuration: [CAT_{stem}.md](./CAT_{stem}.md)\n"
            "Angle index: [ALL_TOPICS_BY_NICHE.md](./Angles/ALL_TOPICS_BY_NICHE.md)\n"
            f"{topic_tracking}"
            f"Visual style source: `REGISTRY/{visual_source}` row {int(row['id'])}\n\n"
            "This file records identity and planning links. Q1-Q42 answers live only in the CAT file. "
            "Choose an angle and a specific story question before starting an episode.\n")


def render_output(row):
    stem = f"{row['id']}_{row['slug']}"
    topic_tracking = ("\n**Topic Tracking & Progress:**\n"
                      "- Topic status and master progress report: "
                      "[topics/281_ayurveda/TOPICS_COVERED_REPORT.md](../../topics/281_ayurveda/TOPICS_COVERED_REPORT.md)\n"
                      "- Master topic roadmap: "
                      "[AYURVEDA_CHANNEL_TOPIC_ROADMAP.md](./AYURVEDA_CHANNEL_TOPIC_ROADMAP.md)\n") if int(row["id"]) == 281 else ""
    return (f"# {row['id']} {row['title']}\n\n"
            f"Subject category: `{row['primary_category']}`. "
            f"Niche record: `REGISTRY/Niches/{stem}/NICHE_{stem}.md`. "
            f"Configuration: `REGISTRY/Niches/{stem}/CAT_{stem}.md`.\n\n"
            "Episode projects are created under this folder by `create_project.py`. "
            "This landing folder is not a completed episode.\n"
            f"{topic_tracking}")
