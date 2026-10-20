"""Episode planning helpers; no media generation or editorial approval."""
from pathlib import Path
import re

from Tools.projects import production_workflow as workflow

SCENES = '04_Phase3_SCENE_BREAKDOWN'
INDEX = 'MASTER_SCENES_INDEX.md'
SIGNATURE = '<!-- generated-scene-index-v1 -->'
CORE = workflow.ROOT / 'CORE/PIPELINE'


def configuration(project):
    from Tools.validation.validate_project import config_gate
    errors = []
    result = config_gate(project, errors)
    if errors or result is None:
        raise ValueError('Valid CONFIG required: ' + '; '.join(errors))
    return result


def guard(project):
    project = Path(project).resolve()
    if any(p.lower() == 'legacy' for p in project.parts):
        raise ValueError('Historical OUTPUT/Legacy projects are not planning targets')
    return project


def timing_rows(durations):
    elapsed = 0
    rows = []
    for number, duration in enumerate(durations, 1):
        rows.append(f'| {number} | {elapsed} | {elapsed + duration} | {duration} |')
        elapsed += duration
    return rows


def prepare(project, *, write=False):
    """Create missing planning/profile drafts; never overwrite episode records."""
    project = guard(project)
    answers, total, durations = configuration(project)
    planner = (CORE / SCENES / 'SCENE_PLANNER_TEMPLATE.md').read_text(encoding='utf-8')
    planner = planner.replace('CONFIG_TIMING_ROWS', '\n'.join(timing_rows(durations)))
    planner = planner.replace('CONFIG_RUNTIME', str(total)).replace('CONFIG_SCENE_COUNT', str(len(durations)))
    profile = (workflow.TEMPLATES / 'GENERATOR_PROFILE_TEMPLATE.md').read_text(encoding='utf-8')
    contents = {project / SCENES / 'SCENE_PLANNER.md': planner,
                project / workflow.PHASE / 'GENERATOR_PROFILE.md': profile}
    created, preserved = [], []
    for path, text in contents.items():
        if path.exists():
            preserved.append(path.name)
        else:
            created.append(path.name)
            if write:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding='utf-8')
    return {'project': project.name, 'create': created, 'preserved': preserved, 'write': write}


def scene_index_text(project):
    _, total, durations = configuration(project)
    records = workflow.scene_records(project)
    if ([r['id'] for r in records] != list(range(1, len(durations)+1)) or
            [r['duration'] for r in records] != durations):
        raise ValueError('Cannot index: actual scene IDs/durations do not match CONFIG')
    def cell(value):
        return value.replace('|', '&#124;').replace('\n', ' ').strip()
    rows, elapsed = [], 0
    sources = {}
    for path in workflow.scene_paths(project):
        for number in re.findall(r'^\*\*Scene (\d+)\*\*', path.read_text(encoding='utf-8'), re.M):
            sources[int(number)] = path.name
    for r in records:
        chapter = cell(workflow.scene_field(r['text'], 'Chapter')) or 'Unspecified'
        claims = ', '.join(r['claims']) or cell(workflow.scene_field(r['text'], 'Claim IDs'))
        rows.append(f"| {r['id']} | {elapsed} | {elapsed+r['duration']} | {r['duration']} | {chapter} | {claims} | [{sources[r['id']]}]({sources[r['id']]}) |")
        elapsed += r['duration']
    return (f'# Master scene index\n\n{SIGNATURE}\n\n'
            f'Project: {project.name}\n\nRuntime: {total} seconds; scenes: {len(records)}.\n\n'
            'Derived from CONFIG and actual scene records. This index records structure only; it does not approve research, scenes or media. Rebuild after scene changes.\n\n'
            '| Scene | Start seconds | End seconds | Duration seconds | Chapter | Claim references | Source file |\n'
            '|---|---|---|---|---|---|---|\n' + '\n'.join(rows) + '\n')


def build_index(project, *, write=False):
    project = guard(project)
    text = scene_index_text(project)
    path = project / SCENES / INDEX
    if path.exists() and SIGNATURE not in path.read_text(encoding='utf-8'):
        raise ValueError('Existing manual scene index preserved; reconcile it before generating an index')
    if write:
        path.write_text(text, encoding='utf-8')
    return {'project': project.name, 'index': INDEX, 'write': write, 'content': text}


def check(project, errors):
    """Validate optional planning records if an episode opted into them."""
    planner = project / SCENES / 'SCENE_PLANNER.md'
    index = project / SCENES / INDEX
    profile = project / workflow.PHASE / 'GENERATOR_PROFILE.md'
    try:
        if planner.is_file():
            text = planner.read_text(encoding='utf-8')
            if workflow.PLACEHOLDERS.search(text):
                errors.append('Unfinished SCENE_PLANNER.md: complete chapter/beat, purpose and review planning')
            _, _, durations = configuration(project)
            rows = re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$', text, re.M)
            actual = ['| ' + ' | '.join(row) + ' |' for row in rows]
            if actual != timing_rows(durations):
                errors.append('SCENE_PLANNER.md timing table differs from CONFIG')
            workflow.local_links(planner, text, project, errors)
        if index.is_file():
            text = index.read_text(encoding='utf-8')
            if SIGNATURE not in text:
                errors.append('Manual MASTER_SCENES_INDEX.md needs reconciliation with the generated index')
            elif text != scene_index_text(project):
                errors.append('MASTER_SCENES_INDEX.md is stale or edited; rebuild with scene-index --write')
        if profile.is_file():
            text = profile.read_text(encoding='utf-8')
            for heading in ('Selection status', 'Generator and model', 'Verified capabilities', 'Reference inputs', 'Clip assembly', 'Execution and review'):
                if f'## {heading}' not in text:
                    errors.append(f'GENERATOR_PROFILE.md missing section: {heading}')
            if workflow.PLACEHOLDERS.search(text):
                errors.append('Unfinished GENERATOR_PROFILE.md')
            workflow.local_links(profile, text, project, errors)
    except (ValueError, OSError, KeyError) as exc:
        errors.append(f'Invalid planning record: {exc}')


def sync_guides(project, *, write=False):
    """Append missing shared guide sections while preserving all existing text."""
    project = guard(project)
    configuration(project)
    changed = []
    for name in workflow.specification()['documents']:
        path = project / workflow.PHASE / name
        if not path.is_file():
            continue
        original = path.read_text(encoding='utf-8')
        template = (workflow.TEMPLATES / name).read_text(encoding='utf-8')
        sections = re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', template, re.M | re.S)
        existing = set(re.findall(r'^## ([^\n]+)', original, re.M))
        additions = ['## ' + title + '\n' + body.rstrip() for title, body in sections if title not in existing]
        if additions:
            changed.append(name)
            if write:
                # Append bytes; no newline or encoding rewrite of existing content.
                with path.open('ab') as stream:
                    stream.write(('\n\n<!-- Shared guide additions: review for this episode; no approval implied. -->\n\n' + '\n\n'.join(additions) + '\n').encode('utf-8'))
                manifest_path = project / workflow.PHASE / workflow.MANIFEST
                if manifest_path.is_file():
                    manifest = workflow.load_manifest(project)
                    if name in manifest['documents']:
                        manifest['documents'][name] = {'status': 'draft', 'reason': ''}
                        workflow.json_write(manifest_path, manifest)
    return {'project': project.name, 'append_sections_to': changed, 'write': write}
