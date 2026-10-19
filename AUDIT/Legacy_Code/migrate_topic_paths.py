"""Move niche directories to taxonomy categories without deleting content.

Run `python migrate_topic_paths.py` for a preflight; add `--apply` to migrate.
Rerunning after interruption resumes already moved directories.
"""
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOPICS = (ROOT / "REGISTRY" / "Topics").resolve()
TAXONOMY = ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv"
LEGACY = ROOT / "REGISTRY" / "LEGACY_TOPIC_PATHS.csv"


def inside_topics(path):
    resolved = path.resolve()
    if resolved == TOPICS or TOPICS not in resolved.parents:
        raise ValueError(f"Unsafe topic path: {path}")
    return resolved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 500 or len({r["id"] for r in rows}) != 500:
        raise ValueError("Expected 500 unique taxonomy IDs")
    actions = []
    legacy = []
    for r in rows:
        old_rel = Path(r["current_path"])
        if old_rel.parts[:2] != ("REGISTRY", "Topics") or len(old_rel.parts) != 4:
            raise ValueError(f"Invalid current path: {old_rel}")
        src = inside_topics(ROOT / old_rel)
        dst = inside_topics(TOPICS / r["primary_category"] / r["slug"])
        if dst.parent.name != r["primary_category"] or dst.name != r["slug"]:
            raise ValueError(f"Invalid destination: {dst}")
        legacy.append((r["id"], old_rel.as_posix(), dst.relative_to(ROOT).as_posix()))
        if src == dst:
            if not src.is_dir():
                raise FileNotFoundError(src)
            continue
        if src.is_dir() and not dst.exists():
            actions.append((src, dst))
        elif dst.is_dir() and not src.exists():
            pass  # completed by an earlier interrupted run
        else:
            raise ValueError(f"Missing source or destination collision: {src} -> {dst}")
    print(f"Preflight: {len(rows)} IDs, {len(actions)} moves pending")
    if not args.apply:
        return
    for src, dst in actions:
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)
    # Commit the map only once all moves have succeeded.
    with LEGACY.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "old_path", "new_path"])
        writer.writerows(legacy)
    for r in rows:
        r["current_path"] = f"REGISTRY/Topics/{r['primary_category']}/{r['slug']}"
    with TAXONOMY.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Moved {len(actions)} directories; wrote {LEGACY.name}")


if __name__ == "__main__":
    main()
