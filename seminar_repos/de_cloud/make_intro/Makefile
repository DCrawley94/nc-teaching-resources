#################################################################################
#
# Example Makefile
#
#################################################################################

# Variables
PYTHON_INTERPRETER=python
PIP=pip
SHELL=/bin/bash # If this isn't set the shell will default to `sh`
PYTHONPATH=$(shell pwd) # Using command substitution to create the PYTHONPATH

# 1: Create the virtual environment
create-environment:
	$(PYTHON_INTERPRETER) -m venv venv

# 2: Install project dependancies
install-requirements: create-environment
	source venv/bin/activate && $(PIP) install -r requirements.txt

# 3: Run unit tests
unit-test:
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest -vvv

# ~~~~~ Install code quality tools ~~~~~
install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake8

# ~~~~~ Run code quality checks ~~~~~
security-checks:
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance:
	source venv/bin/activate && flake8 src test

# Run unit tests, security checks and code compliance checks
run-checks: unit-test security-checks check-pep8-compliance