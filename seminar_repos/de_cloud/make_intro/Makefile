#################################################################################
#
# Example Makefile
#
#################################################################################

# Useful Variables

PYTHON_INTERPRETER=python
PIP=pip
PYTHONPATH=$(shell pwd)
SHELL=/bin/bash # If this isn't set the shell will default to `sh`


# ~~~~~ Create python interpreter environment ~~~~~
create-environment:
	@echo ">>> Setting up VirtualEnv."
	python -m venv venv

# ~~~~~ Install requirements ~~~~~
install-requirements-simple: create-environment
	source venv/bin/activate && $(PIP) install -r ./requirements.txt

install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake coverage

# ~~~~~ Run unit tests ~~~~~
unit-test-simple:
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest -vvv

# ~~~~~ Define utility variable to help calling Python from the virtual environment - show this towards the end ~~~~~
ACTIVATE_ENV = source venv/bin/activate

define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

#  ~~~~~ Refactored rules to use utility var ~~~~~
install-requirements-better: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)

unit-test-better:
	$(call execute_in_env, PYTHONPATH=$(PYTHONPATH) pytest -vvv)
