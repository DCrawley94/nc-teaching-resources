#################################################################################
#
# Example Makefile
#
#################################################################################

# Useful Variables

PYTHON_INTERPRETER=python
PIP=pip
SHELL=/bin/bash # If this isn't set the shell will default to `sh`


# ~~~~~ Create python interpreter environment ~~~~~
create-environment:
	@echo ">>> Setting up VirtualEnv."
	$(PYTHON_INTERPRETER) -m venv venv

# ~~~~~ Install requirements ~~~~~
install-requirements-simple: create-environment
	@echo ">>> Installing requirements."
	source venv/bin/activate; $(PIP) install -r ./requirements.txt

# ~~~~~ Install code quality tools ~~~~~
install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake8

# ~~~~~ Run unit tests ~~~~~
unit-test-simple:
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest -vvv

security-checks:
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance:
	source venv/bin/activate && flake8 src test

run-checks: unit-test-simple security-checks check-pep8-compliance

# ~~~~~ Define utility variable to help calling Python from the virtual environment - show this towards the end ~~~~~
ACTIVATE_ENV = source venv/bin/activate

define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

#  ~~~~~ Refactored rules to use utility var ~~~~~
install-requirements-better: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)

install-dev-tools-better:
	$(call execute_in_env, $(PIP) install bandit safety flake8)

unit-test-better:
	$(call execute_in_env, PYTHONPATH=$(PYTHONPATH) pytest -vvv)

security-checks-better:
	$(call execute_in_env, safety check -r ./requirements.txt)
	$(call execute_in_env, bandit -lll */*.py *c/*.py)

check-pep8-compliance-better:
	$(call execute_in_env, flake8 src test)
