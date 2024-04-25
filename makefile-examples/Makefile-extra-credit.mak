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

# ~~~~~ Define utility variable to help calling Python from the virtual environment - show this towards the end ~~~~~
ACTIVATE_ENV = source venv/bin/activate

define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

#  ~~~~~ Refactored rules to use utility var ~~~~~
install-requirements: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)

install-dev-tools:
	$(call execute_in_env, $(PIP) install bandit safety flake8)

unit-test:
	$(call execute_in_env, PYTHONPATH=$(PYTHONPATH) pytest -vvv)

security-checks:
	$(call execute_in_env, safety check -r ./requirements.txt)
	$(call execute_in_env, bandit -lll */*.py *c/*.py)

check-pep8-compliance:
	$(call execute_in_env, flake8 src test)

# Run unit tests, security checks and code compliance checks
run-checks: unit-test-simple security-checks check-pep8-compliance