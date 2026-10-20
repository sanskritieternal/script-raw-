import os
import subprocess
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
files = []
for base, dirs, names in os.walk(root):
    dirs[:] = [d for d in dirs if d not in {'.git', 'tmp', '__pycache__'}]
    for name in names:
        if name.endswith(('.pyc', '.pyo', '.pyd')):
            continue
        path = Path(base) / name
        files.append(path)

files.sort()
proc = subprocess.Popen(['git', 'fast-import', '--quiet'], cwd=root, stdin=subprocess.PIPE)
out = proc.stdin
stamp = int(time.time())
out.write(b'commit refs/heads/main\n')
out.write(f'committer Sanskriti Eternal <sanskritieternal@users.noreply.github.com> {stamp} +0530\n'.encode())
out.write(b'data 24\nInitial project snapshot\n')
out.write(b'deleteall\n')
for i, path in enumerate(files, 1):
    data = path.read_bytes()
    rel = path.relative_to(root).as_posix().encode('utf-8')
    rel = rel.replace(b'\\', b'\\\\').replace(b'"', b'\\"')
    out.write(b'M 100644 inline "' + rel + b'"\n')
    out.write(f'data {len(data)}\n'.encode())
    out.write(data)
    out.write(b'\n')
    if i % 5000 == 0:
        print(f'Imported {i}/{len(files)} files', flush=True)
out.write(b'\n')
out.close()
code = proc.wait()
print(f'Files: {len(files)}, git fast-import exit: {code}', flush=True)
raise SystemExit(code)
