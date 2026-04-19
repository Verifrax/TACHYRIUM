#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(rel: str):
    p = ROOT / rel
    if not p.exists():
        raise SystemExit(f"FAIL missing-file {rel}")
    try:
        return json.loads(p.read_text())
    except Exception as e:
        raise SystemExit(f"FAIL invalid-json {rel}: {e}")

def assert_true(cond: bool, msg: str):
    if not cond:
        raise SystemExit(f"FAIL {msg}")

policy = load("contracts/boundary-policy.json")
bp_schema = load("schemas/boundary-policy.schema.json")
out_schema = load("schemas/cognition-output.schema.json")
audit_schema = load("schemas/cognition-audit-record.schema.json")
out_fixture = load("fixtures/cognition-output.valid.json")
audit_fixture = load("fixtures/cognition-audit-record.valid.json")
release = load("schemas/release-manifest.json")
inventory = load("schemas/repository-inventory.json")

print("[VERIFY] files-present")

assert_true(policy["object_type"] == "BOUNDARY_POLICY", "boundary-policy object_type")
assert_true(policy["surface"] == "TACHYRIUM", "boundary-policy surface")
assert_true(policy["state_type"] == "ACTIVE_TRUTH", "boundary-policy state_type")
assert_true(policy["role"] == "bounded-sovereign-cognition", "boundary-policy role")

allowed = set(policy["allowed_output_classes"])
forbidden = set(policy["forbidden_output_classes"])
assert_true(allowed.isdisjoint(forbidden), "allowed/forbidden output overlap")

required_assertions = {
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
assert_true(required_assertions.issubset(set(policy["required_boundary_assertions"])),
            "missing required boundary assertions")

required_rejections = {
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
assert_true(required_rejections.issubset(set(policy["rejection_reasons"])),
            "missing rejection reasons")

print("[VERIFY] boundary-policy-core")

ba = out_fixture["boundary_assertions"]
for key in required_assertions:
    assert_true(ba.get(key) is True, f"fixture boundary assertion not true: {key}")

assert_true(out_fixture["object_type"] == "COGNITION_OUTPUT", "output fixture object_type")
assert_true(out_fixture["output_class"] in allowed, "output fixture class not allowed")
assert_true(out_fixture["status"] in {"subordinate", "review-required", "bounded"}, "output fixture status")
assert_true(out_fixture["downstream_review_surface"] in {
    "human-review", "SYNTAGMARIUM", "ORBISTIUM", "CONSONORIUM",
    "AUCTORISEAL", "CORPIFORM", "VERIFRAX", "ANAGNORIUM", "REGRESSORIUM"
}, "output fixture downstream review surface")

print("[VERIFY] cognition-output-core")

assert_true(audit_fixture["object_type"] == "COGNITION_AUDIT_RECORD", "audit fixture object_type")
assert_true(audit_fixture["decision"] == "rejected", "audit fixture decision")
assert_true(audit_fixture["requested_output_class"] == "verification-verdict",
            "audit fixture requested_output_class")
assert_true(audit_fixture["rejection_reason"] == "would-emit-verification-verdict",
            "audit fixture rejection_reason")
assert_true(audit_fixture["sovereign_collision_flags"]["verification"] is True,
            "audit fixture verification collision flag")
assert_true(audit_fixture["boundary_zone"] == "outside-tachyrium-boundary",
            "audit fixture boundary zone")

print("[VERIFY] cognition-audit-core")

machine_readable = set(inventory["inventory"]["machine_readable"])
validation = set(inventory["inventory"]["validation"])
boundary_objects = set(inventory["inventory"].get("boundary_objects", []))

for rel in {
    "schemas/boundary-policy.schema.json",
    "schemas/cognition-output.schema.json",
    "schemas/cognition-audit-record.schema.json"
}:
    assert_true(rel in machine_readable, f"inventory missing machine_readable {rel}")

for rel in {
    "tests/test_boundary_policy_schema_smoke.py",
    "tests/test_cognition_output_schema_smoke.py",
    "tests/test_cognition_audit_schema_smoke.py",
    "tests/test_cognition_boundary_negative_assertions.py"
}:
    assert_true(rel in validation, f"inventory missing validation {rel}")

assert_true("contracts/boundary-policy.json" in boundary_objects,
            "inventory missing boundary object")

print("[VERIFY] repository-inventory-wiring")

assert_true("bounded-cognition-audit" in release["allowed_functions"],
            "release manifest missing bounded-cognition-audit")

for item in {
    "terminal-recognition-of-record",
    "terminal-recourse-of-record",
    "proof-publication-of-record",
    "intake-decision-of-record"
}:
    assert_true(item in release["forbidden_functions"],
                f"release manifest missing forbidden function {item}")

print("[VERIFY] release-manifest-wiring")

try:
    import jsonschema  # type: ignore
except Exception:
    print("[VERIFY] jsonschema-module absent -> structural verification only")
else:
    from jsonschema import Draft202012Validator, FormatChecker  # type: ignore
    Draft202012Validator(bp_schema, format_checker=FormatChecker()).validate(policy)
    Draft202012Validator(out_schema, format_checker=FormatChecker()).validate(out_fixture)
    Draft202012Validator(audit_schema, format_checker=FormatChecker()).validate(audit_fixture)
    print("[VERIFY] full-jsonschema-validation")

print("[PASS] PHASE 2 / STEP 2 boundary-object minimum verified")
