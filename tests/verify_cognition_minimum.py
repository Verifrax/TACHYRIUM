#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def need(cond: bool, label: str):
    if cond:
        print(f"[VERIFY] {label}")
    else:
        print(f"[FAIL] {label}")
        errors.append(label)

required_files = [
    "README.md",
    "COGNITION.md",
    "VERSION",
    "contracts/boundary-policy.json",
    "schemas/boundary-policy.schema.json",
    "schemas/cognition-output.schema.json",
    "schemas/cognition-audit-record.schema.json",
    "docs/contracts/INPUT_CONTRACT.md",
    "docs/contracts/OUTPUT_CONTRACT.md",
    "prompts/PROMPT_CONTRACT.md",
    "fixtures/cognition-output.valid.json",
    "fixtures/cognition-audit-record.valid.json",
    "tests/test_cognition_boundary_negative_assertions.py",
    "tests/test_cognition_minimum.py",
]

for rel in required_files:
    need((ROOT / rel).is_file(), f"file-present {rel}")

policy = load("contracts/boundary-policy.json")
out_fixture = load("fixtures/cognition-output.valid.json")
audit_fixture = load("fixtures/cognition-audit-record.valid.json")

need(policy.get("object_type") == "BOUNDARY_POLICY", "boundary-policy object_type")
need(policy.get("surface") == "TACHYRIUM", "boundary-policy surface")
need(policy.get("state_type") == "ACTIVE_TRUTH", "boundary-policy state_type")
need(policy.get("role") == "bounded-sovereign-cognition", "boundary-policy role")

required_assertions = {
    "not-law",
    "not-state",
    "not-authority",
    "not-verification",
    "not-recognition",
    "not-recourse",
    "reviewable-subordinate-output",
}
need(required_assertions.issubset(set(policy.get("required_boundary_assertions", []))),
     "required-boundary-assertions")

forbidden_classes = set(policy.get("forbidden_output_classes", []))
need({
    "law-object",
    "accepted-state-object",
    "authority-object",
    "verification-verdict",
    "recognition-object",
    "recourse-object",
}.issubset(forbidden_classes), "forbidden-output-classes")

rejection_reasons = set(policy.get("rejection_reasons", []))
need({
    "would-author-law",
    "would-mutate-accepted-state",
    "would-issue-authority",
    "would-emit-verification-verdict",
    "would-assign-terminal-recourse",
}.issubset(rejection_reasons), "rejection-reasons")

need(out_fixture.get("object_type") == "COGNITION_OUTPUT", "output-fixture object_type")
need(out_fixture.get("output_class") in set(policy.get("allowed_output_classes", [])),
     "output-fixture allowed-class")
need(out_fixture.get("status") in {"subordinate", "review-required", "bounded"},
     "output-fixture status")

boundary_assertions = out_fixture.get("boundary_assertions", {})
for key in [
    "not-law",
    "not-state",
    "not-authority",
    "not-verification",
    "not-recognition",
    "not-recourse",
]:
    need(boundary_assertions.get(key) is True, f"output boundary-assertion {key}")

need(audit_fixture.get("decision") == "rejected", "audit-fixture decision")
need(audit_fixture.get("requested_output_class") == "verification-verdict",
     "audit-fixture requested_output_class")
need(audit_fixture.get("rejection_reason") == "would-emit-verification-verdict",
     "audit-fixture rejection_reason")

collisions = audit_fixture.get("sovereign_collision_flags", {})
need(collisions.get("verification") is True, "audit-fixture verification collision")
need(collisions.get("recognition") is False, "audit-fixture recognition collision")
need(collisions.get("recourse") is False, "audit-fixture recourse collision")

if errors:
    print("[FAIL] PHASE 4 / STEP 87 cognition minimum verification failed")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)

print("[PASS] PHASE 4 / STEP 87 cognition minimum verified")
