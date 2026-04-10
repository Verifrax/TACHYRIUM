PYTHON := python3

.PHONY: validate-fixtures smoke all

validate-fixtures:
	$(PYTHON) cli/validate_candidate_object.py fixtures/candidate-object.valid.json
	$(PYTHON) cli/validate_candidate_object.py fixtures/router-candidate.valid.json
	$(PYTHON) cli/validate_candidate_object.py fixtures/classification-summary.valid.json
	$(PYTHON) cli/validate_candidate_object.py fixtures/topology-summary.valid.json
	$(PYTHON) cli/validate_candidate_object.py fixtures/contradiction-analysis.valid.json
	$(PYTHON) cli/validate_candidate_object.py fixtures/briefing.valid.json
	$(PYTHON) cli/validate_candidate_object.py fixtures/pipeline-briefing.valid.json

smoke:
	$(PYTHON) tests/run_all_smoke.py

all: validate-fixtures smoke
