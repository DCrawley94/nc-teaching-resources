# Make

## Learning Objectives

- Identify certain project tasks that could be more automated
- Know how to use Make/Makefile to create a 'recipe' for automating these steps

## Flow

Start off by asking students what steps they take after cloning down a new repo:

**Disregard `git` steps**

Initial setup:

- create venv
- activate venv
- install dependancies

Development:

- Set PYTHONPATH
- Running tests

---

- Currently these are all done separately one by one

- Also things like activating venv/setting PYTHONPATH need to be done each time a new shell session is opened

We're going to look at a tool that is useful for automating these steps a bit more.

## Introduce Make

`make` is a piece of software that is useful for compiling/recompiling programs. It is commonly used in `C` programs but can also be used a a command runner.

Let's take a look at an example Makefile and see if we can decipher what's going on.
