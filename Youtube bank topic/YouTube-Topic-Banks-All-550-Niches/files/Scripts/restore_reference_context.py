"""Restore bundled, unchanged reference files into a fresh extracted work tree.

Preview by default; never overwrite a differing existing reference file.
"""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-root', type=Path, required=True)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    context = args.reference_root/'context'
    assert context.is_dir(), 'Missing bundled reference/context directory'
    count = 0
    for source in sorted(context.rglob('*')):
        if not source.is_file():
            continue
        assert not source.is_symlink()
        relative = source.relative_to(context)
        target = ROOT/relative
        if target.exists():
            assert target.read_bytes() == source.read_bytes(), f'Differing existing reference needs review: {relative}'
            continue
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        count += 1
    print(f'{count} missing reference files {"restored" if args.write else "would be restored"}; existing matching references preserved')


if __name__ == '__main__':
    main()
