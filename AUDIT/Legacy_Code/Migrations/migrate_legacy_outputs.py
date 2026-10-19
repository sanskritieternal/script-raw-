"""Archive pre-schema-3 output folders without rewriting historical content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = (ROOT / "OUTPUT").resolve()
LEGACY = OUTPUT / "Legacy"
OLD = ("AI_Film", "Business_Money", "Cartoon_Animation", "Documentary", "Sanatan_Dharma", "Science_Future")


def main():
    LEGACY.mkdir(exist_ok=True)
    moved = 0
    for name in OLD:
        source = (OUTPUT / name).resolve()
        target = (LEGACY / name).resolve()
        if source.parent != OUTPUT or target.parent != LEGACY:
            raise ValueError("Output move escaped the intended directory")
        if not source.exists():
            continue
        if target.exists():
            raise ValueError(f"Legacy output collision: {target}")
        source.rename(target)
        moved += 1
    (LEGACY / "README.md").write_text(
        "# Historical outputs\n\nThese projects and progress files predate subject taxonomy and configuration schema 3.0. "
        "Their internal paths and Q answers are preserved as historical content; they have not passed the current "
        "configuration or final audit contract. New projects belong under `OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/`.\n",
        encoding="utf-8",
    )
    print(f"Archived {moved} legacy output category folders")


if __name__ == "__main__":
    main()
