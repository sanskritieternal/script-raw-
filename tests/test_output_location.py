"""Output root precedence and predictable path resolution."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from Tools.projects.output_location import resolve_output_root
from Tools.projects import create_project
from Tools.validation import validate_project


class OutputLocationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()

    def tearDown(self):
        self.temp.cleanup()

    def setting(self, text):
        (self.root / 'output.md').write_text(text, encoding='utf-8')

    def test_absent_blank_and_quoted_blank_keep_current_default(self):
        self.assertEqual(resolve_output_root(repository_root=self.root), self.root / 'OUTPUT')
        for text in ('```text\noutput_root:\n```\n', 'output_root: ""\n'):
            self.setting(text)
            self.assertEqual(resolve_output_root(repository_root=self.root), self.root / 'OUTPUT')

    def test_relative_spaces_and_absolute_destination(self):
        self.setting('output_root: "New Videos"\n')
        self.assertEqual(resolve_output_root(repository_root=self.root), self.root / 'New Videos')
        dest = self.root / 'External Video Files'
        self.setting(f'output_root: {dest}\n')
        self.assertEqual(resolve_output_root(repository_root=self.root), dest)
        self.assertFalse(dest.exists())  # resolution/preview does not create folders

    def test_explicit_override_wins_even_when_config_is_invalid(self):
        self.setting('invalid configuration\n')
        self.assertEqual(resolve_output_root('Override', repository_root=self.root), self.root / 'Override')

    def test_invalid_or_duplicate_setting_does_not_silently_fallback(self):
        for text in ('no setting\n', 'output_root: one\noutput_root: two\n', 'output_root: $env:HOME\n'):
            self.setting(text)
            with self.assertRaises(ValueError):
                resolve_output_root(repository_root=self.root)
        file = self.root / 'a_file';file.write_text('existing', encoding='utf-8')
        self.setting(f'output_root: {file}\n')
        with self.assertRaisesRegex(ValueError, 'file, not a folder'):
            resolve_output_root(repository_root=self.root)

    def test_creation_cli_uses_resolved_root_in_preview(self):
        output = self.root / 'Chosen Videos'
        with patch.object(create_project, 'resolve_output_root', return_value=output), patch('sys.argv', ['create_project', '--id', '540', '--angle', 'field_character_perspective', '--dry-run']), contextlib.redirect_stdout(io.StringIO()) as stream:
            create_project.main()
        self.assertIn(str(output / '540_ramayana'), stream.getvalue())
        self.assertFalse(output.exists())

    def test_configured_root_creates_all_project_records_outside_workspace(self):
        self.setting('output_root: New Videos\n')
        def resolve(override):
            return resolve_output_root(override, repository_root=self.root)
        with patch.object(create_project, 'resolve_output_root', side_effect=resolve), patch('sys.argv', ['create_project', '--id', '540', '--angle', 'field_character_perspective', '--story-question', 'How does the selected passage present recognition?', '--mode', 'autonomous']), contextlib.redirect_stdout(io.StringIO()):
            create_project.main()
        configs = list((self.root / 'New Videos').rglob('CONFIG.md'))
        self.assertEqual(len(configs), 1)
        project = configs[0].parent.parent
        self.assertEqual(validate_project.validate(project, 0), [])
        self.assertIn(str(self.root / 'New Videos'), configs[0].read_text(encoding='utf-8'))
        self.assertEqual(len(list((project / '03_Phase2_PRODUCTION_BIBLE').glob('*.md'))), 33)  # 32 canonical + optional profile
        self.assertTrue((project / '04_Phase3_SCENE_BREAKDOWN/SCENE_PLANNER.md').is_file())
        self.assertFalse((self.root / 'OUTPUT').exists())


if __name__ == '__main__':
    unittest.main()
