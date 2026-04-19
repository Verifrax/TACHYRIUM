import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def test_cognition_minimum_contract():
    policy = load("contracts/boundary-policy.json")
    output_fixture = load("fixtures/cognition-output.valid.json")
    audit_fixture = load("fixtures/cognition-audit-record.valid.json")

    assert policy["object_type"] == "BOUNDARY_POLICY"
    assert policy["surface"] == "TACHYRIUM"
    assert policy["state_type"] == "ACTIVE_TRUTH"
    assert policy["role"] == "bounded-sovereign-cognition"

    required_assertions = {
        "not-law",
        "not-state",
        "not-authority",
        "not-verification",
        "not-recognition",
        "not-recourse",
        "reviewable-subordinate-output",
    }
    assert required_assertions.issubset(set(policy["required_boundary_assertions"]))

    forbidden = set(policy["forbidden_output_classes"])
    assert {
        "law-object",
        "accepted-state-object",
        "authority-object",
        "verification-verdict",
        "recognition-object",
        "recourse-object",
    }.issubset(forbidden)

    rejections = set(policy["rejection_reasons"])
    assert {
        "would-author-law",
        "would-mutate-accepted-state",
        "would-issue-authority",
        "would-emit-verification-verdict",
        "would-assign-terminal-recourse",
    }.issubset(rejections)

    assert output_fixture["object_type"] == "COGNITION_OUTPUT"
    assert output_fixture["output_class"] in set(policy["allowed_output_classes"])
    ba = output_fixture["boundary_assertions"]
    for key in [
        "not-law",
        "not-state",
        "not-authority",
        "not-verification",
        "not-recognition",
        "not-recourse",
    ]:
        assert ba[key] is True

    assert audit_fixture["decision"] == "rejected"
    assert audit_fixture["requested_output_class"] == "verification-verdict"
    assert audit_fixture["rejection_reason"] == "would-emit-verification-verdict"
    assert audit_fixture["sovereign_collision_flags"]["verification"] is True
