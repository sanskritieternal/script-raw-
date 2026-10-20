"""Planning output timing, preservation and stale-index checks."""
import tempfile
from pathlib import Path
import unittest

from Tools.projects import planning_records as planning
from Tools.projects import production_workflow as workflow
from Tools.validation import validate_project
from tests.test_production_workflow import completed_copy


class PlanningRecordsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project = completed_copy(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_prepare_preview_and_non_overwrite(self):
        before = {p: p.read_bytes() for p in self.project.rglob('*') if p.is_file()}
        self.assertEqual(len(planning.prepare(self.project)['create']), 2)
        self.assertEqual(before, {p: p.read_bytes() for p in self.project.rglob('*') if p.is_file()})
        planning.prepare(self.project, write=True)
        planner = self.project / planning.SCENES / 'SCENE_PLANNER.md'
        self.assertIn('| 2 | 8 | 16 | 8 |', planner.read_text(encoding='utf-8'))
        planner.write_text('Custom existing plan.', encoding='utf-8')
        self.assertEqual(len(planning.prepare(self.project, write=True)['preserved']), 2)
        self.assertEqual(planner.read_text(encoding='utf-8'), 'Custom existing plan.')

    def test_index_tracks_actual_scenes_and_rejects_stale_or_manual(self):
        path = self.project / planning.SCENES / planning.INDEX
        preview = planning.build_index(self.project)
        self.assertFalse(path.exists())
        self.assertIn('| 2 | 8 | 16 | 8 |', preview['content'])
        planning.build_index(self.project, write=True)
        self.assertEqual(validate_project.validate(self.project, 3), [])
        path.write_text(path.read_text(encoding='utf-8') + 'Edited.', encoding='utf-8')
        self.assertTrue(any('stale or edited' in e for e in validate_project.validate(self.project, 3)))
        planning.build_index(self.project, write=True)
        self.assertEqual(validate_project.validate(self.project, 3), [])
        path.write_text('Handwritten index.', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'manual scene index preserved'):
            planning.build_index(self.project, write=True)

    def test_bad_scene_timing_cannot_generate_index(self):
        source = workflow.scene_paths(self.project)[0]
        source.write_text(source.read_text(encoding='utf-8').replace('**Duration:** 8 seconds', '**Duration:** 7 seconds', 1), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'do not match CONFIG'):
            planning.build_index(self.project, write=True)
        self.assertFalse((self.project / planning.SCENES / planning.INDEX).exists())

    def test_planner_placeholder_and_timing_checks_then_compile_optional_records(self):
        planning.prepare(self.project, write=True)
        self.assertTrue(any('Unfinished SCENE_PLANNER' in e for e in validate_project.validate(self.project, 3)))
        planner = self.project / planning.SCENES / 'SCENE_PLANNER.md'
        text = planner.read_text(encoding='utf-8').replace('[TBD]', 'Two-scene definition and distance example; existing evidence and manifest mappings retained. No additional review claimed.')
        planner.write_text(text.replace('| 2 | 8 | 16 | 8 |', '| 2 | 9 | 16 | 7 |'), encoding='utf-8')
        self.assertTrue(any('timing table differs' in e for e in validate_project.validate(self.project, 3)))
        planner.write_text(text, encoding='utf-8')
        planning.build_index(self.project, write=True)
        self.assertEqual(validate_project.validate(self.project, 3), [])
        workflow.compile_package(self.project, write=True)
        package = self.project / '05_Phase4_PRODUCTION_PACKAGE/Production_Package.md'
        result = package.read_text(encoding='utf-8')
        self.assertIn('Master scene index', result)
        self.assertIn('External generator profile', result)
        profile = self.project / workflow.PHASE / 'GENERATOR_PROFILE.md'
        profile.write_text(profile.read_text(encoding='utf-8')+'\nModel remains unselected.\n', encoding='utf-8')
        self.assertTrue(any('stale' in e for e in validate_project.validate(self.project, 4)))

    def test_sync_appends_without_overwriting_and_resets_status_for_review(self):
        path = self.project / workflow.PHASE / 'CAMERA_ANIMATION_GUIDE.md'
        original = path.read_bytes()
        self.assertIn(path.name, planning.sync_guides(self.project)['append_sections_to'])
        self.assertEqual(path.read_bytes(), original)
        planning.sync_guides(self.project, write=True)
        self.assertTrue(path.read_bytes().startswith(original))
        self.assertIn('## Reusable shot library', path.read_text(encoding='utf-8'))
        self.assertEqual(workflow.load_manifest(self.project)['documents'][path.name]['status'], 'draft')
        self.assertEqual(planning.sync_guides(self.project, write=True)['append_sections_to'], [])


if __name__ == '__main__':
    unittest.main()
