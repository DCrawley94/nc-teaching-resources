# `Make` Seminar

## Intro

Remind students that we have recently seen Makefiles and used a tool called `make` to run commands from said file. Throwback to the start of last week where students were given a sample server to deploy.

What is `Make`?

> a language agnostic build tool and task runner

It's a old piece of software that can be used for a lot of complex things. However we're only going to be dipping our toes in the water and using it as a simple command runner.

## What do we mean by command runner?

> A tool we can use to save and run project specific commands.

## Ask for examples of commands me might run when working with a python project

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install` / `pip install -r requirements.txt`
- `pytest` - PYTHONPATH?

Other examples:

- `flake8`/ `security`/ `bandit`

**Explain that I have a Python repo pre-made and we're going to automate some of the regularly used commands**

## Creating a Makefile

**Switch to VSCode**

Show the Makefile with some pre-written boilerplate.

- `PYTHON_INTERPRETER` - defining this in a single place in case I need to change it in the future
- `PIP` - defining this in a single place in case I need to change it in the future
- `SHELL` - If I don't set this then the default shell it will use is `sh`. this might be fine but I'd rather stick with `bash` to be sure. The syntax here is similar to how we set it on the command line and it does the exact same

## Create the first rule

Talk through the syntax for writing a `makefile` rule.

```make
create-environment:
	python -m venv venv
```

**`** missing separator. Stop.`\*\* -> this happens when you use spaces instead of tabs.

Show that this would work if we just used `python` but re-iterate that if I want to change to executable to something else I'd prefer to only need to change it in one place:

```make
create-environment:
	$(PYTHON_INTERPRETER) -m venv venv
```

**switch back to figjam to breakdown the structure of a rule**

- Explain that `make` has it's own syntax so it might look weird but for what we need there only a few odd bits of syntax.

**pause and ask for thoughts**

## Second rule - introduce dependencies for rules

Ask students what the next job would be once we've set up an environment. Specifically what do I need to do before I can run my tests.

- they will likely say activating - can palm this off as something that we need for all subsequent commands.

Hopefully someone will say installing dependencies:

```make
install-requirements:
	source venv/bin/activate && $(PIP) install -r ./requirements.txt
```

Show that this now work by running `make install-requirements`.

Talk about how this is currently quite manual and we're still having to do things step by step. It would be nice if we can automate this a bit more.

**Ask students what might happen if we were to remove the venv and try to run** `make install-requirements` - try it and see it fail

Explain that the `create-environment` rule is therefore a dependency of the `install-requirements` - we need to run the first before we can run the second.

Show how to list a rule as a dependency and link back to figjam screenshot.

```make
install-requirements: create-environment
	source venv/bin/activate && $(PIP) install -r ./requirements.txt
```

**Can we see how this might make our lives easier?**

## Final rule - `shell` command expansion

I want to run my tests, what do I need to do?

- activate environment
- set PYTHONPATH

Activating the environment - we've seen that already

**How do we set the PYTHONPATH in the the command line - this is done with command substitution - `PYTHONPATH=$(pwd)`**

We can do the same kind of command substitution in our `makefile`. The syntax is slightly different but it achieves the same thing:

```make
PYTHONPATH=$(shell pwd)
```

Print the variable to show it working:

```make
$(info PYTHONPATH: $(PYTHONPATH))
```

**Now lets use it in a rule:**

```make
unit-test:
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest -vvv
```

**Highlight that when we run this it is all being handled by `make` as a _subprocess_ so there's no need to activate the environment in our terminal anymore. Make handles it all**

## Next step, bring it all together

After showing a few rules bring in some extras, Blue Peter style:

```make
# ~~~~~ Install code quality tools ~~~~~
install-dev-tools:
	source venv/bin/activate && $(PIP) install bandit safety flake8

# ~~~~~ Run code quality checks ~~~~~
security-checks:
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance:
	source venv/bin/activate && flake8 src test
```

**Can force pep 8 to fail by adding a couple of extra lines**

Briefly talk through what they're doing and then explain that we can bring together multiple rules - again with dependencies:

```make
run-checks: unit-test-simple security-checks check-pep8-compliance
```

Note that this has no logic of it's own it just exists to run multiple rules at once.

## Extra Time:

Finally if there's time we can have a look at syntax for creating a "function" to handle the virtual environment activation.

```make
ACTIVATE_ENV = source venv/bin/activate

define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

install-requirements-better: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)

install-dev-tools-better:
	$(call execute_in_env, $(PIP) install bandit safety)

unit-test-better:
	$(call execute_in_env, PYTHONPATH=$(PYTHONPATH) pytest -vvv)

security-checks-better:
	$(call execute_in_env, safety check -r ./requirements.txt)
	$(call execute_in_env, bandit -lll */*.py *c/*.py)

check-pep8-compliance-better:
	$(call execute_in_env, flake8 src test)
```

# Summary:

Explain that this can be useful when working on a project locally. It will also come in very handy when creating CI/CD pipelines which will be covered on Wednesday.
