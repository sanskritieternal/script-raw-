# Project output location

Edit the value after `output_root:` below. Leave it empty to use the current default: `F:\The Script of 1\OUTPUT`.

```text
output_root:
```

## Examples of values

- `D:\My Videos`
- `E:\Production Projects`
- `OUTPUT` (relative to this system folder)

Paste a folder path, including the drive when using an absolute Windows path. Spaces and backslashes are supported; quotation marks are optional. Relative paths are resolved from the system folder, not the terminal's current folder. Use a real folder path rather than an environment-variable expression.

## How it works

New projects use: explicit `--output-root` or an explicit requested destination, then this file, then the current system's `OUTPUT` folder when the value/file is empty or absent. Invalid configuration reports an error rather than silently selecting another location.

The system adds the niche and specific project folders beneath this root. For example, a value of `D:\My Videos` produces `D:\My Videos\540_ramayana\<specific_project>\` with all phase folders inside. Do not add the niche or project name to this setting unless you intentionally want another parent level.

Read this setting before creating a new project and use the resulting project path for all research, production bible, scenes, package, audit and project status records. Ongoing projects continue at their actual existing path. Changing this setting does not relocate or recreate earlier work. System templates and registry/catalog documents are maintained in this workspace.
