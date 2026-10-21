import unittest
from pathlib import Path

from independent_eval.allocation import (
    add_assignment,
    assignment_for,
    normalize_publisher_id,
    pool,
    resolve_publisher_id,
    load_allocation,
    validate_allocation,
)


def empty_registry(aliases=None):
    return {"schema_version": 1, "aliases": aliases or {}, "publishers": []}


class AllocationTests(unittest.TestCase):
    def test_normalization_uses_nfkc_lowercase_and_removes_all_whitespace(self):
        self.assertEqual(normalize_publisher_id("  Ｃｉｔｙ　 OF\tTOKYO "), "cityoftokyo")


    def test_pool_is_deterministic_and_matches_protocol_vectors(self):
        self.assertEqual(pool("  ＪＰ "), "train")
        self.assertEqual(pool("fixture-0"), "eval2")
        self.assertEqual(pool("fixture-1"), "train")
        self.assertEqual(pool("fixture-2"), "eval3")
        self.assertEqual(pool("tokyo"), pool("tokyo"))


    def test_protocol_fixed_assignments_override_hash_for_existing_sources(self):
        registry = {
            "schema_version": 1,
            "aliases": {},
            "publishers": [
                {"publisher_id": "yokohama", "pool": "main", "date": "2026-10-21"},
                {"publisher_id": "jp", "pool": "train", "date": "2026-10-21"},
            ],
        }
        self.assertEqual(assignment_for("YOKOHAMA", registry)["pool"], "main")
        self.assertEqual(assignment_for("jp", registry)["pool"], "train")
        with self.assertRaisesRegex(ValueError, "fixed publisher pool cannot change"):
            validate_allocation(
                {
                    "schema_version": 1,
                    "aliases": {},
                    "publishers": [
                        {"publisher_id": "yokohama", "pool": "train", "date": "2026-10-21"}
                    ],
                }
            )

    def test_persisted_registry_contains_all_protocol_fixed_sources(self):
        registry = load_allocation(
            Path(__file__).resolve().parents[1] / "independent_eval" / "allocation.json"
        )
        actual = {entry["publisher_id"]: entry["pool"] for entry in registry["publishers"]}
        expected = {
            "australia": "train", "canada": "train", "canada2": "train",
            "datagov_uk": "train", "datagov_uk2": "train", "direct": "train",
            "egov": "train", "egov_biz": "train", "egov_biz2": "train",
            "gittables": "train", "ireland": "train", "jp": "train", "jp2": "train",
            "kobe": "main", "nyc": "main", "sapporo": "main", "yokohama": "main",
        }
        for publisher_id, pool_name in expected.items():
            self.assertEqual(actual[publisher_id], pool_name)
        self.assertEqual(len(actual), len(set(actual)))


    def test_aliases_resolve_before_assignment(self):
        registry = empty_registry({"CITY PORTAL": "city"})
        self.assertEqual(resolve_publisher_id("Ｃｉｔｙ　Portal", registry["aliases"]), "city")
        self.assertEqual(assignment_for("CITY PORTAL", registry)["publisher_id"], "city")


    def test_ambiguous_publisher_is_held_out_of_training_and_evaluation(self):
        self.assertEqual(assignment_for("unclear org", empty_registry(), ambiguous=True)["pool"], "hold")
        assigned = add_assignment(empty_registry(), "unclear org", "2026-10-21", ambiguous=True)
        self.assertEqual(assigned["publishers"][0]["pool"], "hold")


    def test_existing_assignment_is_immutable_and_add_is_idempotent(self):
        registry = empty_registry()
        assigned = add_assignment(registry, "publisher a", "2026-10-21")
        repeated = add_assignment(assigned, "PUBLISHER A", "2026-10-22", ambiguous=True)
        self.assertEqual(repeated, assigned)
        self.assertEqual(repeated["publishers"][0]["date"], "2026-10-21")


    def test_registered_publisher_cannot_later_become_an_alias(self):
        registry = add_assignment(empty_registry(), "mystery portal", "2026-10-21", ambiguous=True)
        registry["aliases"] = {"mystery portal": "egov"}
        with self.assertRaisesRegex(ValueError, "registered publisher cannot also be an alias"):
            validate_allocation(registry)

    def test_alias_cycles_and_duplicate_assignments_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "cycle"):
            resolve_publisher_id("a", {"a": "b", "b": "a"})
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_allocation(
                {
                    "schema_version": 1,
                    "aliases": {},
                    "publishers": [
                        {"publisher_id": "a", "pool": "train", "date": "2026-10-21"},
                        {"publisher_id": "A", "pool": "eval2", "date": "2026-10-21"},
                    ],
                }
            )
