"""Resolve the single editable project-output setting in root output.md."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def resolve_output_root(override=None, *, repository_root=ROOT):
    root = Path(repository_root).resolve()
    value = override
    if value is None:
        setting = root / 'output.md'
        if not setting.exists():
            return root / 'OUTPUT'
        text = setting.read_text(encoding='utf-8-sig')
        matches = re.findall(r'^output_root:[ \t]*([^\r\n]*)$', text, re.M)
        if len(matches) != 1:
            raise ValueError('output.md must contain exactly one output_root: setting')
        value = matches[0].strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1].strip()
        if not value:
            return root / 'OUTPUT'
    value = str(value).strip()
    if not value:
        raise ValueError('Explicit output destination must not be empty')
    if any(c in value for c in ('\n', '\r', '\x00')) or value.startswith('$') or re.search(r'%[^%]+%', value):
        raise ValueError('Output destination must be a folder path, not an environment-variable expression')
    path = Path(value).expanduser()
    if path.anchor and not path.is_absolute():
        raise ValueError('Use a complete absolute path or a path relative to the system folder')
    path = (path if path.is_absolute() else root / path).resolve()
    if path.exists() and not path.is_dir():
        raise ValueError(f'Output destination is a file, not a folder: {path}')
    return path
