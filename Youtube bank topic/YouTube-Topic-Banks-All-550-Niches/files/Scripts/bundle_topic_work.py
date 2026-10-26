"""Build a self-contained topic-work checkpoint and verify two apply-ready patches.

Run render/check and index first. Pass the previous canonical Library archive
unchanged as --previous-archive, and its extracted reference/ as --reference-root.
The output archive is separate; replace the canonical Library identity only after
all checks succeed. No GitHub writes or credentials are used by this script.
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def unpack_files(archive, target):
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            if not name.startswith('files/') or name.endswith('/'):
                continue
            rel = Path(name[6:])
            assert not rel.is_absolute() and '..' not in rel.parts
            dest = target/rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(z.read(name))


def initialize(base):
    subprocess.run(['git', 'init', '-q'], cwd=base, check=True)
    subprocess.run(['git', 'add', '.'], cwd=base, check=True)
    subprocess.run(['git', '-c', 'user.name=Codex', '-c', 'user.email=codex@local', 'commit', '-qm', 'Known topic baseline'], cwd=base, check=True)


def patch(base, paths, destination, verification):
    for relative in paths:
        target = base/relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT/relative, target)
    subprocess.run(['git', 'add', '-N', '.'], cwd=base, check=True)
    subprocess.run(['git', 'diff', '--check'], cwd=base, check=True)
    destination.write_bytes(subprocess.check_output(['git', 'diff', '--binary'], cwd=base))
    for rel in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], cwd=base, text=True).splitlines():
        target = verification/rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(subprocess.check_output(['git', 'show', 'HEAD:'+rel], cwd=base))
    subprocess.run(['git', 'apply', '--check', str(destination)], cwd=verification, check=True)
    subprocess.run(['git', 'apply', str(destination)], cwd=verification, check=True)
    for relative in paths:
        assert (verification/relative).read_bytes() == (ROOT/relative).read_bytes(), relative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous-archive', type=Path, required=True)
    parser.add_argument('--reference-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    previous = args.previous_archive.resolve()
    reference = args.reference_root.resolve()
    output = args.output.resolve()
    assert previous.exists() and (reference/'main-baseline').is_dir()
    assert output != previous, 'Preserve the previous archive for patch generation and conflict recovery'
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['python3', str(ROOT/'Scripts/render_topic_banks.py'), '--check', '--require-all-niches'], check=True)
    with zipfile.ZipFile(previous) as z:
        paths = {Path(n[6:]) for n in z.namelist() if n.startswith('files/') and not n.endswith('/')}
    paths.update(p.relative_to(ROOT) for p in (ROOT/'Scripts').iterdir() if p.is_file())
    paths.update(p.relative_to(ROOT) for p in (ROOT/'topics').iterdir() if p.is_file() and p.suffix in {'.json', '.md'})
    paths.update(p.relative_to(ROOT) for p in ROOT.glob('topics/*/IN_DEPTH_TOPIC_BANK.*'))
    paths = sorted(paths)
    assert all((ROOT/p).is_file() for p in paths)
    status = json.loads((ROOT/'topics/DEPTH_COMPLETION_STATUS.json').read_text())
    progress = json.loads((ROOT/'topics/TOPIC_BANK_PROGRESS.json').read_text())
    focus_path = ROOT/'topics/FIRST_TEN_EXPANSION_STATUS.json'
    focus = json.loads(focus_path.read_text()) if focus_path.exists() else None
    assert len(status['prepared_niche_ids']) + len(status['pending_niche_ids']) == progress['totals']['niches_with_banks']
    assert set(status['prepared_niche_ids']).isdisjoint(status['pending_niche_ids'])
    questions, identities = set(), set()
    for p in ROOT.glob('topics/*/IN_DEPTH_TOPIC_BANK.json'):
        bank = json.loads(p.read_text())
        for category in bank['categories']:
            for topic in category['topics']:
                assert topic['id'] not in identities and topic['question'].casefold() not in questions
                identities.add(topic['id'])
                questions.add(topic['question'].casefold())
    assert len(identities) == progress['totals']['proposed_topics']
    with tempfile.TemporaryDirectory(prefix='topic_bundle_') as workdir:
        work = Path(workdir)
        incremental = work/'incremental'; incremental.mkdir()
        unpack_files(previous, incremental)
        initialize(incremental)
        main = work/'main'; shutil.copytree(reference/'main-baseline', main)
        initialize(main)
        verify_incremental = work/'verify_incremental'; verify_incremental.mkdir()
        verify_main = work/'verify_main'; verify_main.mkdir()
        patch_incremental = work/'latest-depth-update.patch'
        patch_main = work/'all-topic-work-from-original-main.patch'
        patch(incremental, paths, patch_incremental, verify_incremental)
        patch(main, paths, patch_main, verify_main)
        checks = {'overall_request': status['overall_request'], 'detailed_drafts_prepared': status['detailed_topic_drafts_prepared'],
                  'pending_depth_expansion': status['pending_depth_expansion'], 'next_pending_niche': status['next_pending_niche_id'],
                  'totals': progress['totals'], 'patch_checks': 'both patches apply to their respective baselines and reproduce all exported files byte for byte',
                  'active_ids_and_questions': 'unique', 'remote_changes': 'none', 'full_repository_tests': 'not claimed',
                  'canonical_previous_archive_sha256': hashlib.sha256(previous.read_bytes()).hexdigest()}
        if focus:
            checks['current_priority'] = {'niche_ids':focus['niche_priority'], 'status':focus['status'],
                                          'proposals':focus['current_proposals'], 'latest_extension':focus['latest_extension']}
        priority_note = (f'Current priority: further substantive expansion of niches 001–010. Their {focus["current_proposals"]:,} proposals are an open checkpoint, not a completion threshold. Read files/topics/FIRST_TEN_EXPANSION_STATUS.json before selecting work.\n' if focus else '')
        readme = f'''# YouTube topic-bank work: current checkpoint

Detailed topic drafts prepared: **{status['detailed_topic_drafts_prepared']} / {progress['totals']['niches_with_banks']}**.
Still pending depth expansion: **{status['pending_depth_expansion']}**. Next pending niche: **{status['next_pending_niche_id']}**.
The overall request is **{status['overall_request']}**. Folder coverage and proposal count are not completion.
{priority_note}

Start at files/topics/DEPTH_COMPLETION_STATUS.md. The all-niche index links the current banks.
Read files/topics/CONTINUATION_PLAN.md for the automatic continuation procedure and quality boundaries.

## Apply one patch

latest-depth-update.patch applies to the EXACT preceding canonical archive; its SHA256 is in VALIDATION.json.
all-topic-work-from-original-main.patch includes all topic work against inspected main commit 751dc234534e9eea18fe022b831ed0da5630fe53.
Do not apply both. Use git apply --check before applying the selected patch and reconcile newer changes rather than overwriting them.
If you skipped checkpoints, obtain the appropriate intermediate patches or inspect the final files and integrate the changes deliberately.

## Self-contained continuation

The reference/ directory contains unchanged source context and the original topic-file baseline; it is NOT part of either patch.
In a fresh extracted workspace run:

python3 files/Scripts/restore_reference_context.py --reference-root reference --write

Then work from files/ using the existing scripts. Do not copy reference files over differing current repository files.
Preserve the previous canonical archive unchanged when invoking bundle_topic_work.py.

## Limits

All topic records remain proposals. Source verification, current angle review, scripts, media and publication are separate.
No fixed topic cap applies. Earlier starter records are archived rather than counted again after depth expansion.
The GitHub integration previously denied writing; no remote commit or PR is included, and no access token is needed for content continuation.
'''
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for relative in paths:
                z.write(ROOT/relative, 'files/'+relative.as_posix())
            for p in sorted(reference.rglob('*')):
                if p.is_file():
                    z.write(p, 'reference/'+p.relative_to(reference).as_posix())
            z.write(patch_incremental, patch_incremental.name)
            z.write(patch_main, patch_main.name)
            z.writestr('README.md', readme)
            z.writestr('VALIDATION.json', json.dumps(checks, indent=2)+'\n')
            z.writestr('SHA256.json', json.dumps({p.as_posix(): hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}, indent=2)+'\n')
        with zipfile.ZipFile(output) as z:
            assert z.testzip() is None
        print(json.dumps({'archive': str(output), 'bytes': output.stat().st_size, 'files': len(paths), 'validation': checks}, indent=2))


if __name__ == '__main__':
    main()
