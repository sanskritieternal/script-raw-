"""Behavioral tests for the shared workflow, migration and compilation gates."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from Tools.projects import create_project
import Tools.projects.production_workflow as workflow
from Tools.validation import validate_project

PILOT = Path("AUDIT/PILOTS/343_physics/343_physics_beginner_explainers_si_light_speed_exact")


def completed_copy(root):
    """Use real pilot evidence; supporting decisions are explicitly text-stage."""
    project = root / PILOT.parent.name / PILOT.name
    shutil.copytree(PILOT, project)
    workflow.scaffold(project, write=True, adopt=True)
    folder = project / workflow.PHASE
    content = {
        "YOUTUBE_METADATA.md": "# YouTube metadata\n\n## Primary title\n\nThe exact speed of light\n\n## Description\n\nA scientific explanation of the SI light-speed definition and distance in vacuum; sources are in the episode ledger.\n\n## Chapters\n\n00:00 Definition\n00:08 Distance\n\n## Tags\n\nphysics, SI, light\n\n## Thumbnail\n\nOriginal definition graphic; not rendered.\n\n## Pinned comment\n\nRead the original SI definition.\n\n## Upload decisions\n\nPending; no upload authorized.\n\n## Publication record\n\nNot published.\n\n## Corrections\n\nNo published correction.\n",
        "STORY_BEAT_MAP.md": "# Story beat map\n\nScenes 1-2 cover the definition then the derived distance. Claim references are in the manifest and scenes. Timing: 16 seconds.\n",
        "CHARACTER_WORLD_GUIDE.md": "# Character/world\n\nNarrator only; scientific editorial graphics, no character reenactment. Period: SI definition context. Continuity retains vacuum and exact units.\n",
        "CAMERA_ANIMATION_GUIDE.md": "# Camera/animation\n\nFixed framing for exact unit labels; retain chart continuity. Transition within scene boundaries; no simulated measurement.\n",
        "MUSIC_SOUND_GUIDE.md": "# Music/sound\n\nExisting pilot scene music and sound cues are retained as direction only. Silence is the fallback until actual audio rights are documented. Mix: preserve narrator clarity, measure actual recording before export.\n",
        "ASSET_REGISTER.md": "# Asset register\n\nG01: original scientific graphic; scenes 1 and 2. Status: planned; no file rendered. Rights: actual font/creator evidence required before production.\n",
        "DELIVERY_CHECKLIST.md": "# Delivery checklist\n\nDeliver the two-scene 16-second text plan. Export and caption checks await actual media; release not authorized by this document.\n",
        "REVIEW_REVISION_LOG.md": "# Review and revision log\n\nMigration of a pilot copy only. Findings: no human or media approval added. Revision: shared production adoption; review actual media separately.\n",
        "VIEWER_GLOSSARY.md": "# Viewer glossary\n\nVacuum: the condition specified for the SI light-speed value. Source: the existing claim ledger. Deliver with the transcript.\n",
        "ORIGINALITY_REVIEW.md": "# Originality review\n\nScope: an internal 16-second workflow pilot, not a release. Overlap with public videos was not assessed; this limitation remains explicit.\n",
    }
    manifest = workflow.load_manifest(project)
    for name in set(workflow.specification()['documents']) - set(workflow.specification('1.0')['documents']):
        (folder / name).write_text('Not applicable: this SI definition episode depicts no cast, physical setting, costumes or story chronology. Scientific graphics remain specified in the visual guide.', encoding='utf-8')
        manifest['documents'][name] = {'status': 'not_applicable', 'reason': 'No depicted cast, setting, costumes or story chronology in this definition episode.'}
    for name, text in content.items():
        (folder / name).write_text(text, encoding="utf-8")
        manifest["documents"][name]["status"] = "complete"
    records = workflow.scene_records(project)
    manifest["beats"] = [{"start": 1, "end": 2, "claims": sorted({c for r in records for c in r["claims"]})}]
    manifest["assets"] = [{"id": "G01", "scenes": [1, 2], "status": "planned", "file": "graphics/G01.svg"}]
    manifest["chapters"] = [{"start_seconds": 0, "title": "Definition"}, {"start_seconds": 8, "title": "Distance"}]
    workflow.json_write(folder / workflow.MANIFEST, manifest)
    return project


class ExpandedWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def edit_manifest(self, project, change):
        value = workflow.load_manifest(project)
        change(value)
        workflow.json_write(project / workflow.PHASE / workflow.MANIFEST, value)

    def test_safe_migration_preview_and_existing_files_preserved(self):
        project = self.root / PILOT.parent.name / PILOT.name
        shutil.copytree(PILOT, project)
        before = {str(p.relative_to(project)): p.read_bytes() for p in project.rglob("*") if p.is_file()}
        workflow.scaffold(project)
        self.assertEqual(before, {str(p.relative_to(project)): p.read_bytes() for p in project.rglob("*") if p.is_file()})
        workflow.scaffold(project, write=True)
        for name, data in before.items():
            self.assertEqual((project / name).read_bytes(), data)
        self.assertTrue(any("draft" in e or "Unfinished" in e for e in validate_project.validate(project, 2)))

    def test_repeated_migration_cannot_reset_status(self):
        project = completed_copy(self.root)
        with self.assertRaises(FileExistsError):
            workflow.scaffold(project, write=True)

    def test_fresh_cli_project_scaffolds_all_documents_and_stays_draft(self):
        result = subprocess.run([sys.executable, "-m", "Tools.projects.create_project", "--id", "17", "--angle", "beginner_explainers",
                                 "--story-question", "How can a fictional cartoon explain a familiar classroom idea?",
                                 "--output-root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        manifests = list(self.root.rglob(workflow.MANIFEST))
        self.assertEqual(len(manifests), 1)
        project = manifests[0].parent.parent
        self.assertEqual(len(workflow.load_manifest(project)["documents"]), 32)
        self.assertEqual(validate_project.validate(project, 0), [])
        self.assertTrue(any("not complete" in e or "Unfinished" in e for e in validate_project.validate(project, 2)))

    def test_missing_new_manifest_cannot_bypass_requirement(self):
        project = completed_copy(self.root)
        config = project / "01_Phase0_Configuration/CONFIG.md"
        config.write_text(config.read_text(encoding="utf-8") + "\n" + workflow.MARKER + "\n", encoding="utf-8")
        (project / workflow.PHASE / workflow.MANIFEST).unlink()
        self.assertTrue(any("requires PRODUCTION_MANIFEST" in e for e in validate_project.validate(project, 2)))

    def test_completed_documents_and_mappings_pass(self):
        self.assertEqual(validate_project.validate(completed_copy(self.root), 3), [])

    def legacy_copy(self):
        project = completed_copy(self.root)
        manifest = workflow.load_manifest(project)
        old_names = set(workflow.specification('1.0')['documents'])
        for name in set(manifest['documents']) - old_names:
            (project / workflow.PHASE / name).unlink()
            del manifest['documents'][name]
        manifest['version'] = '1.0'
        workflow.json_write(project / workflow.PHASE / workflow.MANIFEST, manifest)
        return project

    def test_v1_episode_still_validates_and_compiles_without_new_files(self):
        project = self.legacy_copy()
        self.assertEqual(validate_project.validate(project, 3), [])
        workflow.compile_package(project, write=True)
        self.assertEqual(validate_project.validate(project, 4), [])

    def test_upgrade_preview_preserves_content_and_new_records_are_draft(self):
        project = self.legacy_copy()
        # A preexisting new document must be preserved but must not be auto-approved.
        extra = project / workflow.PHASE / 'MAIN_CHARACTERS.md'
        extra.write_text('Existing custom character decisions.', encoding='utf-8')
        before = {p: p.read_bytes() for p in project.rglob('*') if p.is_file()}
        result = workflow.upgrade(project)
        self.assertEqual(len(result['add_draft_records']), 6)
        self.assertEqual(before, {p: p.read_bytes() for p in project.rglob('*') if p.is_file()})
        workflow.upgrade(project, write=True)
        for path, content in before.items():
            if path.name != workflow.MANIFEST:
                self.assertEqual(path.read_bytes(), content)
        manifest = workflow.load_manifest(project)
        self.assertEqual(manifest['version'], '1.1')
        self.assertEqual(manifest['documents']['MAIN_CHARACTERS.md']['status'], 'draft')
        self.assertTrue(any('not complete' in e for e in validate_project.validate(project, 2)))
        self.assertEqual(workflow.upgrade(project, write=True)['add_draft_records'], [])

    def test_new_applicable_document_requires_sections_and_is_compiled(self):
        project = completed_copy(self.root)
        name = 'MAIN_CHARACTERS.md'
        path = project / workflow.PHASE / name
        self.edit_manifest(project, lambda m: m['documents'].update({name: {'status': 'complete', 'reason': ''}}))
        path.write_text('# Main cast\nA narrator.', encoding='utf-8')
        self.assertTrue(any('Required production field missing in MAIN_CHARACTERS' in e for e in validate_project.validate(project, 2)))
        path.write_text('# Main cast\n\n## Character profiles\nCHAR_001 is the illustrative narrator, with no biographical assertions.\n\n## Appearance and voice\nNo likeness; neutral explanatory voice.\n\n## Evidence and depiction\nFictional framing; SI claims remain in the claim ledger.\n\n## Scene and reference links\nNarrator in scenes 1 and 2; no media generated.\n', encoding='utf-8')
        self.assertEqual(validate_project.validate(project, 3), [])
        workflow.compile_package(project, write=True)
        package = project / '05_Phase4_PRODUCTION_PACKAGE/Production_Package.md'
        self.assertIn('CHAR_001 is the illustrative narrator', package.read_text(encoding='utf-8'))
        path.write_text(path.read_text(encoding='utf-8')+'\nRevised voice direction.\n', encoding='utf-8')
        self.assertTrue(any('stale' in e for e in validate_project.validate(project, 4)))

    def test_single_master_scene_file_validates_and_compiles(self):
        project = completed_copy(self.root)
        folder = project / "04_Phase3_SCENE_BREAKDOWN"
        batches = sorted(folder.glob("Batch_*_Scenes_*.md"))
        master = folder / workflow.SCENE_MASTER
        master.write_text("# Scene Breakdown\n\n" + "\n\n".join(
            path.read_text(encoding="utf-8") for path in batches), encoding="utf-8")
        for path in batches:
            path.unlink()
        self.assertEqual([p.name for p in workflow.scene_paths(project)], [workflow.SCENE_MASTER])
        self.assertEqual(validate_project.validate(project, 3), [])
        workflow.compile_package(project, write=True)
        self.assertEqual(validate_project.validate(project, 4), [])

    def test_master_and_legacy_batches_cannot_compete(self):
        project = completed_copy(self.root)
        folder = project / "04_Phase3_SCENE_BREAKDOWN"
        (folder / workflow.SCENE_MASTER).write_text("# Duplicate scene authority\n", encoding="utf-8")
        self.assertTrue(any("both Scene_Breakdown.md and batch" in e
                            for e in validate_project.validate(project, 3)))

    def test_justified_financial_na_passes_but_core_waiver_fails(self):
        project = completed_copy(self.root)
        def change(m):
            m["documents"]["02_Financial_Data_Verified.md"] = {"status": "not_applicable", "reason": "No financial claim appears in this scientific episode."}
        self.edit_manifest(project, change)
        (project / workflow.PHASE / "02_Financial_Data_Verified.md").write_text("Not applicable: no financial claim or currency comparison.", encoding="utf-8")
        self.assertEqual(validate_project.validate(project, 3), [])
        self.edit_manifest(project, lambda m: m["documents"].update({"00_Project_Consistency_Rules.md": {"status": "not_applicable", "reason": "An attempted waiver of required production locks."}}))
        self.assertTrue(any("disallowed" in e for e in validate_project.validate(project, 2)))

    def test_bad_beat_and_unknown_claim_are_blocked(self):
        project = completed_copy(self.root)
        self.edit_manifest(project, lambda m: m.update(beats=[{"start": 1, "end": 1, "claims": ["C999"]}]))
        errors = validate_project.validate(project, 3)
        self.assertTrue(any("unknown claim" in e for e in errors))
        self.assertTrue(any("cover each scene" in e for e in errors))

    def test_wrong_asset_scene_and_fictional_created_file_are_blocked(self):
        project = completed_copy(self.root)
        self.edit_manifest(project, lambda m: m.update(assets=[{"id": "G01", "scenes": [99], "status": "created", "file": "missing.svg"}]))
        errors = validate_project.validate(project, 3)
        self.assertTrue(any("Invalid scene references" in e for e in errors))
        self.assertTrue(any("Created asset file missing" in e for e in errors))

    def test_chapter_off_scene_boundary_is_blocked(self):
        project = completed_copy(self.root)
        self.edit_manifest(project, lambda m: m.update(chapters=[{"start_seconds": 1, "title": "Definition"}]))
        self.assertTrue(any("scene boundaries" in e for e in validate_project.validate(project, 3)))

    def test_missing_scene_source_field_blocks_phase_three(self):
        project = completed_copy(self.root)
        batch = next((project / "04_Phase3_SCENE_BREAKDOWN").glob("Batch_*.md"))
        text = batch.read_text(encoding="utf-8").replace("**Source Citation:**", "Source omitted:")
        batch.write_text(text, encoding="utf-8")
        self.assertTrue(any("missing production field: Source Citation" in e for e in validate_project.validate(project, 3)))

    def test_missing_metadata_field_and_broken_link_block(self):
        project = completed_copy(self.root)
        path = project / workflow.PHASE / "YOUTUBE_METADATA.md"
        path.write_text("# Metadata\n\n[Missing](does_not_exist.md)\n", encoding="utf-8")
        errors = validate_project.validate(project, 2)
        self.assertTrue(any("Required production field" in e for e in errors))
        self.assertTrue(any("Broken local link" in e for e in errors))

    def test_compiler_preserves_scenes_and_detects_stale_input_then_rebuilds(self):
        project = completed_copy(self.root)
        workflow.compile_package(project, write=True)
        self.assertEqual(validate_project.validate(project, 4), [])
        package = project / "05_Phase4_PRODUCTION_PACKAGE/Production_Package.md"
        text = package.read_text(encoding="utf-8")
        for record in workflow.scene_records(project):
            self.assertIn(record["text"], text)
        path = project / workflow.PHASE / "MUSIC_SOUND_GUIDE.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nContinue to use silence.\n", encoding="utf-8")
        self.assertTrue(any("stale" in e for e in validate_project.validate(project, 4)))
        workflow.compile_package(project, write=True)
        self.assertEqual(validate_project.validate(project, 4), [])
        self.assertTrue(list((package.parent / "History").glob("*/Production_Package.md")))

    def test_package_tampering_and_human_review_gate_remain_blocked(self):
        project = completed_copy(self.root)
        workflow.compile_package(project, write=True)
        config = project / "01_Phase0_Configuration/CONFIG.md"
        text = config.read_text(encoding="utf-8")
        text = text.replace("| Q8 | Legal/Accuracy Concern | Low |", "| Q8 | Legal/Accuracy Concern | High |")
        text = text.replace("- Human review required before publication: No", "- Human review required before publication: Yes")
        text = text.replace("- Human review status: Not required", "- Human review status: Pending")
        # The certificate gate independently requires a real approval record.
        text = text.replace("- Human review status: Approved", "- Human review status: Pending approval formerly recorded as Approved")
        config.write_text(text, encoding="utf-8")
        errors = []
        validate_project.audit_gate(project, errors)
        self.assertTrue(any("review approval" in e for e in errors))
        package = project / "05_Phase4_PRODUCTION_PACKAGE/Production_Package.md"
        package.write_text(package.read_text(encoding="utf-8") + "\nManual edit\n", encoding="utf-8")
        self.assertTrue(any("outside the compiler" in e for e in validate_project.validate(project, 4)))

    def test_compiler_collects_supplied_multiline_prompts_and_handoff_fields(self):
        project = completed_copy(self.root)
        batch = next((project / "04_Phase3_SCENE_BREAKDOWN").glob("Batch_*.md"))
        prompt = "Original abstract reference plate.\nKeep the unit illustration text-free."
        fields = ("**Generation Prompt ID:** P3-001\n"
                  "**AI Generation Prompt:**\n" + prompt + "\n"
                  "**Editorial Overlay Instructions:** Add the exact SI labels separately.\n"
                  "**Reference Inputs:** G01 planned original reference; no file generated.\n"
                  "**Execution Record:** Pending external generation.\n\n")
        batch.write_text(batch.read_text(encoding="utf-8").replace("**Scene 2**", fields + "**Scene 2**", 1), encoding="utf-8")
        workflow.compile_package(project, write=True)
        package = project / "05_Phase4_PRODUCTION_PACKAGE/Production_Package.md"
        text = package.read_text(encoding="utf-8")
        section = text.split("## 9. AI Generation Prompts (if using AI video tools)", 1)[1].split("## 10.", 1)[0]
        self.assertIn("### Generation prompt — scene 001", section)
        self.assertIn(prompt, section)
        self.assertIn("Add the exact SI labels separately.", section)
        self.assertIn("G01 planned original reference; no file generated.", section)
        self.assertNotIn("### Generation prompt — scene 002", section)
        self.assertIn("No prompt is invented", section)
        snapshot = json.loads((package.parent / "Package_Inputs.json").read_text(encoding="utf-8"))
        self.assertIn("@system/Tools/projects/production_workflow.py", snapshot["inputs"])
        self.assertEqual(validate_project.validate(project, 4), [])

    def test_variable_duration_mapping_uses_actual_boundaries(self):
        project = completed_copy(self.root)
        manifest = workflow.load_manifest(project)
        manifest["chapters"] = [{"start_seconds": 0, "title": "Definition"}, {"start_seconds": 5, "title": "Distance"}]
        metadata = project / workflow.PHASE / "YOUTUBE_METADATA.md"
        metadata.write_text(metadata.read_text(encoding="utf-8").replace("00:08 Distance", "00:05 Distance"), encoding="utf-8")
        batch = next((project / "04_Phase3_SCENE_BREAKDOWN").glob("Batch_*.md"))
        text = batch.read_text(encoding="utf-8")
        text = text.replace("**Duration:** 8 seconds", "**Duration:** 5 seconds", 1)
        text = text.replace("**Duration:** 8 seconds", "**Duration:** 11 seconds", 1)
        batch.write_text(text, encoding="utf-8")
        errors = []
        workflow.check_mappings(project, manifest, [5, 11], errors)
        self.assertEqual(errors, [])

    def test_historical_legacy_path_is_not_a_migration_target(self):
        with self.assertRaisesRegex(ValueError, "Legacy"):
            workflow.scaffold(self.root / "OUTPUT" / "legacy" / "episode", write=True)

    def test_historical_pilot_stays_compatible(self):
        self.assertEqual(validate_project.validate(PILOT, 5), [])


if __name__ == "__main__":
    unittest.main()
