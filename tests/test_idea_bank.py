"""Idea readiness, non-destructive storage, routing and frozen snapshot checks."""
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from Tools.projects import create_project
from Tools.projects import idea_bank
from Tools.validation import validate_project


class IdeaBankTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.row = idea_bank.taxonomy()["531"]
        self.original = {
            "idea_id": "IDEA-531-0001", "niche_id": "531", "status": "proposed",
            "angle_slug": "field_workflow_or_agent", "topic": "Workflow and agent comparison",
            "working_title": "A documented workflow-versus-agent comparison",
            "story_question": "What can one documented architecture comparison establish about workflow and agent behavior?",
            "case": "One defined software-agent architecture comparison",
            "place_period_version": "Named technical documentation version for the test case",
            "intended_audience": "Technical learners", "purpose": "Separate architecture description from measured task reliability",
            "created_date": "2026-10-18", "updated_date": "2026-10-18",
            "evidence_gaps": ["Verify actual task outcomes in Phase 1."],
            "blocking_gaps": ["Source feasibility has not been checked."],
            "related_ideas": [], "readiness_note": "Test fixture proposal, not real source verification.",
            "source_candidates": [{"title": "Test-only source candidate", "url": "https://example.org/source", "status": "unverified", "checked_date": None, "check_note": "Unverified test fixture."}],
        }
        self.home = self.root / self.row["niche_path"]
        self.home.mkdir(parents=True)
        source = idea_bank.ROOT / self.row["niche_path"] / "ANGLE_PLAN.json"
        (self.home / "ANGLE_PLAN.json").write_bytes(source.read_bytes())
        registry = self.root / "REGISTRY"
        with (registry / "NICHE_TAXONOMY.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(self.row))
            writer.writeheader(); writer.writerow(self.row)

    def tearDown(self):
        self.temp.cleanup()

    def ready(self):
        value = deepcopy(self.original)
        value.update(status="ready_for_project", blocking_gaps=[], readiness_note="Test fixture only: source accessibility and bounded scope preflight recorded.")
        value["source_candidates"][0].update(status="checked", checked_date="2026-10-18", check_note="Test-only source feasibility record; not an episode fact or public review.")
        return value

    def config(self, idea):
        resolved = create_project.resolve(531, idea["angle_slug"])
        return create_project.render(*resolved, "autonomous", story_question=idea["story_question"],
                                     project_episode_slug="idea_snapshot_test", idea_snapshot=idea,
                                     idea_bank_ref=self.row["niche_path"] + "/IDEA_BANK.json")

    def fake_paths(self):
        return patch.multiple(idea_bank, ROOT=self.root, REGISTRY=self.root / "REGISTRY")

    def test_optional_catalog_and_generated_index_are_valid(self):
        catalog, errors = idea_bank.catalog()
        self.assertEqual(errors, [])
        self.assertEqual(idea_bank.index_text(), (idea_bank.REGISTRY / "IDEA_MASTER_LIST.md").read_text(encoding="utf-8"))

    def test_ready_needs_source_check_and_no_blocking_gap(self):
        idea = deepcopy(self.original); idea["status"] = "ready_for_project"
        self.assertTrue(any("Ready idea" in e for e in idea_bank.validate_idea(idea, self.row)))
        self.assertEqual(idea_bank.validate_idea(self.ready(), self.row), [])

    def test_wrong_niche_angle_and_malformed_status_are_rejected(self):
        idea = deepcopy(self.original)
        idea.update(idea_id="IDEA-001-0001", angle_slug=["not-a-slug"], status=[])
        errors = idea_bank.validate_idea(idea, self.row)
        self.assertTrue(any("bind to its niche" in e for e in errors))
        self.assertTrue(any("angle_slug" in e for e in errors))
        self.assertTrue(any("status" in e for e in errors))

    def test_invalid_calendar_check_date_is_rejected(self):
        idea = self.ready(); idea["source_candidates"][0]["checked_date"] = "2026-02-30"
        self.assertTrue(any("real date" in e for e in idea_bank.validate_idea(idea, self.row)))

    def test_init_preview_does_not_write_and_write_does_not_overwrite(self):
        with self.fake_paths(), redirect_stdout(io.StringIO()):
            with patch("sys.argv", ["idea_bank.py", "init", "--id", "531"]):
                idea_bank.main()
            self.assertFalse((self.home / "IDEA_BANK.json").exists())
            with patch("sys.argv", ["idea_bank.py", "init", "--id", "531", "--write"]):
                idea_bank.main()
            before = (self.home / "IDEA_BANK.json").read_bytes()
            with patch("sys.argv", ["idea_bank.py", "init", "--id", "531", "--write"]):
                with self.assertRaises(FileExistsError):
                    idea_bank.main()
            self.assertEqual(before, (self.home / "IDEA_BANK.json").read_bytes())

    def test_add_allocates_id_and_duplicate_question_does_not_write(self):
        source = self.root / "candidate.json"
        idea = deepcopy(self.original); del idea["idea_id"]
        source.write_text(json.dumps(idea), encoding="utf-8")
        argv = ["idea_bank.py", "add", "--id", "531", "--file", str(source), "--write"]
        with self.fake_paths(), redirect_stdout(io.StringIO()):
            with patch("sys.argv", argv):
                idea_bank.main()
            before = (self.home / "IDEA_BANK.json").read_bytes()
            with patch("sys.argv", argv):
                with self.assertRaisesRegex(ValueError, "Duplicate"):
                    idea_bank.main()
            self.assertEqual(before, (self.home / "IDEA_BANK.json").read_bytes())

    def test_unknown_related_reference_is_reported(self):
        idea = deepcopy(self.original); idea["related_ideas"] = ["IDEA-531-9999"]
        (self.home / "IDEA_BANK.json").write_text(json.dumps({"schema_version": "1.0", "niche_id": "531", "ideas": [idea]}), encoding="utf-8")
        with self.fake_paths():
            _, errors = idea_bank.catalog()
        self.assertTrue(any("Unknown or self-related" in e for e in errors))

    def test_snapshot_validates_without_a_live_bank_and_detects_tampering(self):
        config = self.config(self.ready())
        project = self.root / "531_ai_software_agents" / "531_ai_software_agents_field_workflow_or_agent_idea_snapshot_test"
        self.assertFalse((self.home / "IDEA_BANK.json").exists())
        with self.fake_paths():
            errors = []; idea_bank.validate_snapshot(config, project, errors)
            self.assertEqual(errors, [])
            changed = config.replace(self.original["working_title"], "Tampered title")
            errors = []; idea_bank.validate_snapshot(changed, project, errors)
            self.assertTrue(any("differs from snapshot" in e for e in errors))

    def test_proposed_idea_cannot_be_selected(self):
        (self.home / "IDEA_BANK.json").write_text(json.dumps({"schema_version": "1.0", "niche_id": "531", "ideas": [self.original]}), encoding="utf-8")
        with self.fake_paths(), self.assertRaisesRegex(ValueError, "Only ready_for_project"):
            idea_bank.select(531, "IDEA-531-0001")

    def test_cli_ready_selection_derives_question_and_angle(self):
        ready = self.ready()
        output = self.root / "OUTPUT"
        argv = ["create_project.py", "--id", "531", "--idea-id", ready["idea_id"], "--output-root", str(output)]
        with patch("Tools.projects.idea_bank.select", return_value=(ready, self.row["niche_path"] + "/IDEA_BANK.json")), patch("sys.argv", argv), redirect_stdout(io.StringIO()):
            create_project.main()
        configs = list(output.rglob("CONFIG.md"))
        self.assertEqual(len(configs), 1)
        self.assertIn("Idea ID: IDEA-531-0001", configs[0].read_text(encoding="utf-8"))
        self.assertEqual(validate_project.validate(configs[0].parent.parent, 0), [])
        self.assertTrue((configs[0].parent.parent / "03_Phase2_PRODUCTION_BIBLE/PRODUCTION_MANIFEST.json").exists())

    def test_conflicting_question_does_not_create_an_episode(self):
        ready = self.ready()
        argv = ["create_project.py", "--id", "531", "--idea-id", ready["idea_id"], "--story-question", "Why does this conflict with the selected question?", "--output-root", str(self.root / "OUTPUT")]
        with patch("Tools.projects.idea_bank.select", return_value=(ready, self.row["niche_path"] + "/IDEA_BANK.json")), patch("sys.argv", argv), redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                create_project.main()
        self.assertFalse((self.root / "OUTPUT").exists())


if __name__ == "__main__":
    unittest.main()
