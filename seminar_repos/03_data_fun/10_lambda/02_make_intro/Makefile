#################################################################################
#
# Example Makefile
#
#################################################################################

# Variables
PYTHON_INTERPRETER=python
PIP=pip
# This is how you do command substituion in Makefiles
# It is the equivalent to `PYTHONPATH=$(pwd)` in the terminal
PYTHONPATH=$(shell pwd) 

# SHELL is an environment variable that tells make which sheel to use. 
# If you don't set it it then it will default to using /bin/sh which may not be desirable
SHELL=/bin/bash

# This is how you create a function in Makefiles
# You can reference arguments passed with the $1 syntax similar to shell scripts
define execute_in_env
	source venv/bin/activate && $1
endef


# A simple rule that makes use of a variable - no pre-requisites
create-environment:
	$(PYTHON_INTERPRETER) -m venv venv

# This rule has `create-environment` as a pre-requisite
# Therefore if we run `make install-requirements` it will run `create-environment` first before
# 	steps inside the `install-requirements` recipe
install-requirements: create-environment
	$(call execute_in_env, $(PIP) install -r requirements.txt)

# Using && to ensure that the virtual environment is activated for the `pytest` command
unit-test:
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest -v

install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake8

security-checks:
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance:
	source venv/bin/activate && flake8 src test

# An 'umbrella' rule that will combine the functionality of several other rules by setting 
# 	them as pre-requisites
run-checks: unit-test security-checks check-pep8-compliance