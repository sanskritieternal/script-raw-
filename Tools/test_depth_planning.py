"""Reference and progression gates for optional depth plans; no fixture files are written."""
import copy
from unittest import TestCase
from unittest.mock import patch
from Tools import depth_planning as depth


class DepthPlanningTests(TestCase):
    def changed_errors(self, change):
        original = depth.read
        def changed_read(path):
            value = copy.deepcopy(original(path))
            change(path, value)
            return value
        with patch.object(depth, 'read', changed_read):
            return depth.load_and_validate()[2]

    def test_current_plans_and_views_agree(self):
        self.assertEqual(depth.validate(), [])

    def test_prerequisite_cycle_is_blocked(self):
        def change(path, value):
            if path.name == 'DEPTH_PLAN.json' and value['niche_id'] == '001':
                value['topics'][0]['prerequisites'] = ['TOP-001-003']
        self.assertTrue(any('cycle' in e for e in self.changed_errors(change)))

    def test_missing_source_is_blocked(self):
        def change(path, value):
            if path.name == 'DEPTH_PLAN.json' and value['niche_id'] == '008':
                value['topics'][1]['source_ids'] = ['SRC-9999']
        self.assertTrue(any('unknown source' in e for e in self.changed_errors(change)))

    def test_unmapped_series_idea_is_blocked(self):
        def change(path, value):
            if path.name == 'DEPTH_PLAN.json' and value['niche_id'] == '343':
                value['series'][0]['idea_ids'].append('IDEA-531-0001')
        self.assertTrue(any('unmapped idea' in e for e in self.changed_errors(change)))

    def test_source_downgrade_cannot_leave_checked_idea(self):
        def change(path, value):
            if path.name == 'SOURCE_LIBRARY.json':
                value['sources'][0].update(status='unverified', checked_date=None)
        self.assertTrue(any('source not represented' in e for e in self.changed_errors(change)))
