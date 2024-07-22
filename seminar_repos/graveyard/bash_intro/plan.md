# Bash Intro

## Learning Objectives

- Understand what a shell is
- Know how to create and execute a simple shell script
- Identify some common tasks that might be suitable for automation

## What is a Shell?

> Ask for volunteers to explain their understanding of what a shell is.

Uncover description and talk through it.

We've been using the command-line a lot recently for various tasks.

> Ask for examples of students using commands in the shell.

Up to this point we've been entering these commands very manually but we're going to take a look at something that allows us to automate things a bit more.

## What is a Shell Script?

> Ask if anyone has heard of a shell script before.

**If yes, pick someone to describe what a shell script is.**

Again uncover description and talk through it.

## How can we use them?

Shell scripting is one of the simplest ways to set up automation.

If you find yourself regularly running a sequence of commands this can be a good candidate for automation.

> Are there any sequences of commands we've been running regularly that might be good candidates for a shell script?

**Hopefully someone mentions things like set up/venv/dependancy install and testing.**

## Examples to work through:

### Hello World script

- shebang
- chmod
- passing arguments

### Python Project Generator

Setup Steps:

- create venv

```sh
python -m venv venv
```

- create project structure

```sh
mkdir src
mkdir test
```

- activate venv and install pytest

```sh
source venv/bin/activate && pip install pytest
```

## Conclusion

When working on a Python project there's often jobs that you need to do that can be quite manual.

We've only seen a few things so for but as we progress in the course you'll see that there's a lot more we might need to do, especially when it come to deploying code into the cloud and ensuring good code quality.

You may wish to write short scripts to help with these steps
