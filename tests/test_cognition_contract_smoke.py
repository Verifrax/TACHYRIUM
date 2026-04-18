from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_cognition_contract_surface_exists():
    text = (ROOT / "COGNITION.md").read_text()

    required = [
        "TACHYRIUM is the bounded cognition plane of the Verifrax stack.",
        "author constitutional law",
        "mutate accepted epoch truth",
        "issue authority objects",
        "authorize governed execution",
        "emit final verification verdicts",
        "recognize claims of record",
        "assign burden, remedy, escalation, or closure of record",
    ]

    for item in required:
        assert item in text
