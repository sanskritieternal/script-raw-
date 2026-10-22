import json
from pathlib import Path

manifest_path = Path(r"H:\script-raw-\OUTPUT\017_kids_cartoon_stories\017_kids_cartoon_stories_creative_brief_backpack_black_hole\03_Phase2_PRODUCTION_BIBLE\PRODUCTION_MANIFEST.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Update document statuses
for doc in manifest["documents"]:
    if doc == "02_Financial_Data_Verified.md":
        manifest["documents"][doc]["status"] = "not_applicable"
        manifest["documents"][doc]["reason"] = "Original children's animated fiction; no corporate balance sheets or real-world financial figures are applicable."
    else:
        manifest["documents"][doc]["status"] = "complete"
        manifest["documents"][doc]["reason"] = ""

manifest["locks"] = {
    "Q3": "A Clear Story Promise",
    "Q15": "High-Impact Engineering Cinema",
    "Q16": "Playful Animated",
    "Q42": "FIXED 8-SECOND"
}

# Beats covering 1-75
manifest["beats"] = [
    {
        "beat": "BEAT_01",
        "title": "Morning Bus & The Cluttered Pouch",
        "start": 1,
        "end": 15,
        "claims": ["C001", "C005"]
    },
    {
        "beat": "BEAT_02",
        "title": "Homeroom Chaos & The Toast Eruption",
        "start": 16,
        "end": 30,
        "claims": ["C001", "C005"]
    },
    {
        "beat": "BEAT_03",
        "title": "The Hallway Stampede & The Squirrel Heist",
        "start": 31,
        "end": 45,
        "claims": ["C004"]
    },
    {
        "beat": "BEAT_04",
        "title": "Operation Magnet Grabber in the Science Lab",
        "start": 46,
        "end": 60,
        "claims": ["C002", "C003"]
    },
    {
        "beat": "BEAT_05",
        "title": "The Final Bell & The Tidy Desk Victory",
        "start": 61,
        "end": 75,
        "claims": ["C001", "C002", "C005"]
    }
]

# Assets
manifest["assets"] = [
    {"id": "AST_01", "status": "planned", "scenes": list(range(1, 76))},
    {"id": "AST_02", "status": "planned", "scenes": list(range(1, 76))},
    {"id": "AST_03", "status": "planned", "scenes": [10, 11, 12, 13, 14, 15, 68, 69, 70, 71, 72, 73, 74, 75]},
    {"id": "AST_04", "status": "planned", "scenes": list(range(31, 46))},
    {"id": "AST_05", "status": "planned", "scenes": list(range(1, 76))},
    {"id": "AST_06", "status": "planned", "scenes": list(range(46, 66))},
    {"id": "AST_07", "status": "planned", "scenes": list(range(1, 15)) + list(range(61, 76))},
    {"id": "AST_08", "status": "planned", "scenes": list(range(8, 31)) + list(range(68, 76))},
    {"id": "AST_09", "status": "planned", "scenes": list(range(31, 46))},
    {"id": "AST_10", "status": "planned", "scenes": list(range(46, 68))}
]

manifest["chapters"] = [
    {"title": "The Cluttered Morning & The Bus Stop Vortex", "start_seconds": 0},
    {"title": "Homeroom Chaos & The Toast Eruption", "start_seconds": 120},
    {"title": "The Hallway Stampede & The Squirrel Heist", "start_seconds": 240},
    {"title": "Operation Magnet Grabber in the Science Lab", "start_seconds": 360},
    {"title": "The Final Bell & The Tidy Desk Victory", "start_seconds": 480}
]

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print("PRODUCTION_MANIFEST.json updated and locked successfully.")
