# Preparatory Session

## Machine Set Up

Check their OS, make sure they can run `nc-setup` etc.

Carlo: WSL, VSCode, ??Python install??(check how he did this)
Ahmad: ???

## Check if they've got access to l2c precourse

- If they do they can do a code along with me. If not I can share screen

## Very Brief DE Overview

> Essentially preparing data for analysis

To enable you to do that we teach the following:

- Python/Software Development Fundamentals
- Data and Databases
- Cloud Operations
- Bring it all together and work on a group project

## Intro to Python

Start purely on the command line

### repl

In the repl:

```py
>>> a = 6       ## set a variable in this interpreter session
>>> a           ## entering an expression prints its value
6
>>> a + 2
8
>>> a = 'hi'    ## 'a' can hold a string just as well
>>> a
'hi'
>>> len(a)      ## call the len() function on a string
2
>>> a + len(a)  ## try something that doesn't work
Traceback (most recent call last):
  File "", line 1, in
TypeError: can only concatenate str (not "int") to str
>>> a + str(len(a))  ## probably what you really wanted
'hi2'
>>> foo         ## try something else that doesn't work
Traceback (most recent call last):
  File "", line 1, in
NameError: name 'foo' is not defined
>>> ^D          ## type CTRL-d to exit (CTRL-z in Windows/DOS terminal)
```

### Create a python file

```sh
touch example.py

nano example.py

> print('hello!')

python example.py
```

## Coding in VSCode

VSCode installation: https://code.visualstudio.com/docs/remote/wsl - **make sure they have `code` command for ease of use**

recreate `example.py` and refactor existing code to create a function with an argument.

e.g:

```py
# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result
```

## Lists and Dictionaries
