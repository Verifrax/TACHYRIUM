import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str):
    return json.loads((ROOT / relative_path).read_text())


def test_forbidden_output_classes_do_not_overlap_allowed_output_classes():
    policy = load_json("contracts/boundary-policy.json")
    allowed = set(policy["allowed_output_classes"])
    forbidden = set(policy["forbidden_output_classes"])
    assert allowed.isdisjoint(forbidden)


def test_output_schema_hard_codes_non_sovereign_boundary_assertions():
    schema = load_json("schemas/cognition-output.schema.json")
    assertions = schema["properties"]["boundary_assertions"]["properties"]
    required_true = {
        "not-law",
        "not-state",
        "not-authority",
        "not-execution",
        "not-verification",
        "not-recognition",
        "not-recourse",
        "not-proof",
        "not-intake",
        "reviewable-subordinate-output"
    }
    for key in required_true:
        assert assertions[key]["const"] is True


def test_boundary_policy_rejection_reasons_cover_all_forbidden_sovereign_domains():
    policy = load_json("contracts/boundary-policy.json")
    reasons = set(policy["rejection_reasons"])
    expected = {
        "would-author-law",
        "would-mutate-accepted-state",
        "would-issue-authority",
        "would-execute-governed-action",
        "would-emit-verification-verdict",
        "would-recognize-terminal-truth",
        "would-assign-terminal-recourse",
        "would-publish-proof-authority",
        "would-operate-intake-authority"
    }
    assert expected.issubset(reasons)


def test_audit_fixture_proves_rejection_for_verification_of_record():
    record = load_json("fixtures/cognition-audit-record.valid.json")
    assert record["decision"] == "rejected"
    assert record["requested_output_class"] == "verification-verdict"
    assert record["rejection_reason"] == "would-emit-verification-verdict"
    assert record["sovereign_collision_flags"]["verification"] is True
