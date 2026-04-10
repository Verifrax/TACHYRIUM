PYTHON := python3

.PHONY: doctor validate-fixtures smoke install-smoke all

doctor:
	$(PYTHON) cli/check_python_runtime.py

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

install-smoke:
	$(PYTHON) tests/test_install_smoke.py

all: doctor validate-fixtures smoke install-smoke
