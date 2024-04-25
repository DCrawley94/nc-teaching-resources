#################################################################################
#
# Example Makefile
#
#################################################################################

# Useful Variables

# Vars set here in case we want to change the executables we're using
PYTHON_INTERPRETER=python
PIP=pip
# If this isn't set the shell will default to `sh`
SHELL=/bin/bash
# The shell function allows us to use command substitution
PYTHONPATH=$(shell pwd)


# ~~~~~ Create python interpreter environment ~~~~~
create-environment:
	$(PYTHON_INTERPRETER) -m venv venv

# ~~~~~ Install requirements ~~~~~
install-requirements: create-environment
	source venv/bin/activate && $(PIP) install -r ./requirements.txt

# ~~~~~ Install code quality tools ~~~~~
install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake8

# ~~~~~ Run unit tests ~~~~~
unit-test:
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest -vvv

# ~~~~~ Run code quality checks ~~~~~
security-checks:
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance:
	source venv/bin/activate && flake8 src test

# Run unit tests, security checks and code compliance checks
run-checks: unit-test-simple security-checks check-pep8-compliance