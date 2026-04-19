import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str):
    return json.loads((ROOT / relative_path).read_text())


def test_cognition_output_fixture_validates():
    schema = load_json("schemas/cognition-output.schema.json")
    data = load_json("fixtures/cognition-output.valid.json")
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(data)
