"""Build a stable, explicit 500-niche subject taxonomy from the master registry.

Run `python build_taxonomy.py`. Raises on an omitted or duplicate ID.
"""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Primary subject only. Story angle, audience and production format are orthogonal.
# Ranges are inclusive; each ID appears exactly once.
ASSIGNMENTS = {
    "Business_Economy": "8 21 51 70 103-108 112 136 230 293-317 456-462 464-465 467 485 497-500",
    "Technology_Engineering": "1 7 13 22 31 47-48 61-63 87-89 109-110 113 127-129 131 137-139 142 155 157-162 234 296-297 318-335 337-338 342 418-442 463 486-488 495",
    "Science_Nature": "6 12 26-30 32 55 65-68 114-116 118-121 152-154 156 163 191-217 241-242 336 343-367 413-416 478 483-484 491",
    "History_Civilizations": "2-3 35-40 46 49-50 86 96 143-144 150 173 175 177-179 243 245 253 264 283-285 288-289",
    "Religion_Philosophy": "4 23 54 57-60 75-76 222-223 240 268-280 282 286-287 290-292 450",
    "Society_Politics": "9-10 14 72 97-100 122 148-149 168-172 174 176 180 182-185 218-221 235-239 246 493-494 496",
    "Culture_Arts": "24 41-43 52 78-82 84 91-92 94-95 123-126 135 141 243-250 255-267 339-341 368 370 385 392-393 405-407 451-452",
    "Sports_Games": "25 44-45 56 117 130 132-134 138-140 251-254 386-391",
    "Travel_Places": "20 34 38 74 151 187-190 218-242 458",
    "Health_Wellness": "15-16 71 77 101 180-181 186 279-281 351-353 363 471-472",
    "Children_Education": "17 69 73 90 145 408 443-449 453-455 466",
    "Media_Creative": "5 18-19 80-81 85 119 125-127 146-147 164-167 369-384 379-384 392 401-412 417 445 467",
    "Lifestyle_Making": "64 83 85-86 93 102 111 115 128 135-137 141-142 187 191-192 229-232 316 393-412",
    "Future_Scenarios": "11 33 53 55 58-59 130 166-167 334-335 373-378 468-490 492",
}

# These titles can plausibly span subjects. The primary choice below is
# intentional; other candidates remain searchable secondary categories.
REVIEWED_AMBIGUOUS = """38 55 58 59 80 81 85 86 115 119 125 126 127 128 130 135 136
137 138 139 141 142 166 167 180 187 191 192 218 219 220 221 222 223
229 230 231 232 234 235 236 237 238 239 240 241 242 243 245 246
253 264 279 280 296 297 316 334 335 351 352 353 363 370 373
374 375 376 377 378 392 393 401 402 403 404 405 406 407 408
409 410 411 412 445 458 467 471 472 478 483 484 485 486 487 488"""

PRIMARY_OVERRIDES = {
    38: "Travel_Places", 55: "Future_Scenarios", 58: "Culture_Arts",
    59: "Culture_Arts", 85: "Lifestyle_Making", 86: "Lifestyle_Making",
    125: "Media_Creative", 127: "Media_Creative", 130: "Technology_Engineering",
    135: "Lifestyle_Making", 137: "Lifestyle_Making", 138: "Sports_Games",
    139: "Sports_Games", 142: "Lifestyle_Making", 166: "Future_Scenarios",
    167: "Future_Scenarios", 180: "Health_Wellness", 187: "Lifestyle_Making",
    191: "Lifestyle_Making", 192: "Lifestyle_Making", 218: "Travel_Places",
    219: "Travel_Places", 220: "Travel_Places", 221: "Travel_Places",
    222: "Travel_Places", 223: "Travel_Places", 234: "Travel_Places",
    241: "Travel_Places", 242: "Travel_Places", 243: "Culture_Arts",
    245: "Culture_Arts", 246: "Culture_Arts", 253: "Sports_Games",
    264: "Culture_Arts", 297: "Technology_Engineering",
    370: "Media_Creative", 393: "Lifestyle_Making", 401: "Lifestyle_Making",
    402: "Lifestyle_Making", 403: "Lifestyle_Making", 404: "Lifestyle_Making",
    406: "Lifestyle_Making", 407: "Lifestyle_Making", 409: "Lifestyle_Making",
    410: "Lifestyle_Making", 411: "Lifestyle_Making", 412: "Lifestyle_Making",
    445: "Children_Education", 458: "Travel_Places", 471: "Future_Scenarios",
    472: "Future_Scenarios", 478: "Future_Scenarios", 483: "Future_Scenarios",
    484: "Future_Scenarios", 485: "Future_Scenarios", 486: "Future_Scenarios",
    487: "Future_Scenarios", 488: "Future_Scenarios",
}


def expand(spec):
    result = []
    for part in spec.split():
        if "-" in part:
            a, b = map(int, part.split("-"))
            result.extend(range(a, b + 1))
        else:
            result.append(int(part))
    return result


def main():
    text = (ROOT / "REGISTRY" / "MASTER_REGISTRY.md").read_text(encoding="utf-8")
    titles = {int(i): name.strip() for i, name in re.findall(r"^## (\d+)\. (.+)$", text, re.M)}
    if set(titles) != set(range(1, 501)):
        raise ValueError("Master registry must contain exactly IDs 1–500")
    choices = {}
    for category, spec in ASSIGNMENTS.items():
        for i in expand(spec):
            choices.setdefault(i, []).append(category)
    missing = sorted(set(titles) - set(choices))
    extra = sorted(set(choices) - set(titles))
    if missing or extra:
        raise ValueError(f"Missing={missing}; extra={extra}")
    ambiguous = {i for i, categories in choices.items() if len(set(categories)) > 1}
    reviewed = set(expand(REVIEWED_AMBIGUOUS))
    if ambiguous != reviewed or set(PRIMARY_OVERRIDES) - reviewed:
        raise ValueError(f"Unreviewed={sorted(ambiguous-reviewed)}; stale review={sorted(reviewed-ambiguous)}")
    dirs = {}
    for folder in (ROOT / "REGISTRY" / "Topics").glob("*/*"):
        if folder.is_dir():
            index = next(folder.glob("[0-9][0-9][0-9]_*.md"), None)
            if index:
                niche_id = int(index.name[:3])
                dirs[niche_id] = folder.relative_to(ROOT).as_posix()
    if set(dirs) != set(titles):
        raise ValueError("Topic directories do not match registry IDs")
    target = ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv"
    with target.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "current_path", "primary_category", "secondary_categories", "slug", "review_status"])
        for i in sorted(titles):
            primary = PRIMARY_OVERRIDES.get(i, choices[i][0])
            secondary = [c for c in dict.fromkeys(choices[i]) if c != primary]
            status = "title_reviewed" if i in reviewed else "classified_from_registry_title"
            w.writerow([f"{i:03}", titles[i], dirs[i], primary, ";".join(secondary), Path(dirs[i]).name, status])
    print(f"Wrote {target.relative_to(ROOT)} with {len(titles)} IDs: {dict(Counter(PRIMARY_OVERRIDES.get(i, v[0]) for i, v in choices.items()))}")


if __name__ == "__main__":
    main()
