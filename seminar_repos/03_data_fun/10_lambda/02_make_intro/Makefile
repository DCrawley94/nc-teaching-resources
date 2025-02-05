#################################################################################
#
# Example Makefile
#
#################################################################################

# Useful Variables

PYTHON_INTERPRETER=python
PIP=pip
SHELL=/bin/bash # If this isn't set the shell will default to `sh`
PYTHONPATH=$(shell pwd)

# $(info PYTHONPATH: $(PYTHONPATH))

create-environment:
	$(PYTHON_INTERPRETER) -m venv venv

install-requirements: create-environment
	source venv/bin/activate && $(PIP) install -r requirements.txt

unit-test: install-requirements
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest

# ~~~~~ Install code quality tools ~~~~~
install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake8

# ~~~~~ Run code quality checks ~~~~~
security-checks: install-dev-tools
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance: install-dev-tools
	source venv/bin/activate && flake8 src test

run-checks: unit-test security-checks check-pep8-compliance


#  terraform 