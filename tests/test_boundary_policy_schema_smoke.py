import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str):
    return json.loads((ROOT / relative_path).read_text())


def test_boundary_policy_contract_validates():
    schema = load_json("schemas/boundary-policy.schema.json")
    data = load_json("contracts/boundary-policy.json")
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(data)
