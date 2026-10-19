"""Focused tests for production blockers and timing invariants."""
import unittest
from pathlib import Path
from unittest.mock import patch

import create_project
import validate_project


class ContractGateTests(unittest.TestCase):
    def test_unverified_material_claim_blocks_phase_one(self):
        ledger = (
            "| C001 | Proposed fact | https://example.org/source §1 | 2026-10-15 | "
            "Source reviewed | High | Unverified | No dispute | 1 |\n"
        )
        errors = []
        with patch.object(validate_project, "read_required", side_effect=lambda path, _: ledger if path.name == "Claim_Ledger.md" else "Research content"):
            validate_project.research_gate(Path("."), errors)
        self.assertTrue(any("not verified" in error for error in errors))

    def test_variable_plan_must_sum_to_runtime(self):
        values = {"Q14": "16 seconds", "Q42": "VARIABLE"}
        with self.assertRaisesRegex(ValueError, "sum exactly"):
            create_project.parse_duration(values, [5, 5, 5])
        self.assertEqual(create_project.parse_duration(values, [5, 6, 5]), (16, [5, 6, 5], 3))

    def test_high_risk_requires_pending_review(self):
        resolved = create_project.resolve(15, "history_origins")
        config = create_project.render(*resolved, "autonomous")
        self.assertIn("Human review required before publication: Yes", config)
        self.assertIn("Human review status: Pending", config)

    def test_niche_preset_routes_capitals(self):
        row, topic, values, sources, total, scene, count = create_project.resolve(448, "advanced_concepts")
        self.assertEqual(row["primary_category"], "Learning_Education")
        self.assertEqual(values["Q3"], "Capital Status and Sovereignty")
        self.assertEqual(sources["Q2"], "niche_cat")
        self.assertEqual(sources["Q3"], "angle_preset")
        config = create_project.render(row, topic, values, sources, total, scene, count, "interactive",
                                       story_question="How do national capitals change over time?",
                                       project_episode_slug="capitals_change")
        self.assertIn("NICHE_448_capitals.md", config)

    def test_retirement_education_uses_finance_lens(self):
        row, topic, values, sources, *_ = create_project.resolve(500, "product_terms")
        self.assertEqual(row["id"], "500")
        self.assertEqual(values["Q3"], "The Clause That Changes the Payout")
        self.assertEqual(sources["Q3"], "angle_preset")
        self.assertTrue(topic.is_file())

    def test_central_banking_uses_monetary_policy_question(self):
        row, topic, values, sources, *_ = create_project.resolve(298, "how_it_works")
        self.assertEqual(row["id"], "298")
        self.assertEqual(values["Q3"], "From Policy Rate to Borrowing Cost")
        self.assertEqual(sources["Q3"], "angle_preset")
        self.assertTrue(topic.is_file())

    def test_curated_ai_angle_routes_without_changing_cat_defaults(self):
        row, topic, values, sources, *_ = create_project.resolve(1, "evaluation_benchmarks")
        self.assertEqual(row["id"], "001")
        self.assertEqual(values["Q3"], "What AI Benchmarks Do and Do Not Measure")
        self.assertEqual(sources["Q3"], "angle_preset")
        self.assertEqual(sources["Q15"], "niche_cat")
        self.assertTrue(topic.is_file())

    def test_curated_sanatan_angle_routes_with_its_own_cat(self):
        row, topic, values, sources, *_ = create_project.resolve(4, "regional_oral_versions")
        self.assertEqual(row["id"], "004")
        self.assertEqual(values["Q3"], "A Regional Story in Its Own Voice")
        self.assertEqual(values["Q1"], "Hindu_Traditions")
        self.assertEqual(sources["Q3"], "angle_preset")
        self.assertEqual(sources["Q15"], "niche_cat")
        self.assertTrue(topic.is_file())

    def test_full_text_pilot_structural_contract(self):
        pilot = Path("AUDIT/PILOTS/343_physics/343_physics_beginner_explainers_si_light_speed_exact")
        self.assertEqual(validate_project.validate(pilot, 5), [])

    def test_selected_angle_scope_is_snapshotted_in_new_config(self):
        resolved = create_project.resolve(530, "field_teaching_transfer")
        scope = resolved[1].read_text(encoding="utf-8").split("## Editorial scope\n", 1)[1].strip()
        config = create_project.render(*resolved, "interactive",
                                       story_question="Can students check unfamiliar claims after a classroom lesson?",
                                       project_episode_slug="checking_unfamiliar_claims")
        self.assertIn("## Selected angle scope\n\n" + scope, config)
        self.assertIn("**Coverage:** Evaluate whether learners apply", config)
        self.assertIn("**Limits:**", config)
        self.assertEqual(config.count("| Q3 |"), 1)

    def test_project_creation_rejects_an_angle_without_scope(self):
        resolved = create_project.resolve(530, "field_teaching_transfer")
        with patch.object(Path, "read_text", return_value="# Angle without scope\n"):
            with self.assertRaisesRegex(ValueError, "needs editorial scope"):
                create_project.render(*resolved, "interactive")

    def test_reviewed_expansion_routes_agent_specific_angle(self):
        row, topic, values, sources, *_ = create_project.resolve(531, "field_tool_permission_boundaries")
        self.assertEqual(row["primary_category"], "Robotics_AI")
        self.assertEqual(values["Q3"], "Tool Permission Boundaries")
        self.assertEqual(sources["Q3"], "angle_preset")
        self.assertTrue(topic.is_file())

    def test_new_health_and_text_niches_keep_publication_review(self):
        for niche in (537, 538, 539, 540, 541, 542, 543):
            resolved = create_project.resolve(niche, "history_origins")
            config = create_project.render(*resolved, "autonomous")
            self.assertIn("Human review required before publication: Yes", config)
            self.assertIn("Human review status: Pending", config)

    def test_latest_creative_niche_has_distinct_curated_route(self):
        row, topic, values, sources, *_ = create_project.resolve(550, "field_session_and_delivery_provenance")
        self.assertEqual(row["title"], "Music Production & Sound Design")
        self.assertEqual(values["Q3"], "Session And Delivery Provenance")
        self.assertTrue(topic.is_file())


if __name__ == "__main__":
    unittest.main()
