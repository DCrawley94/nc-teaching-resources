# Thursday Code discussion

Start by looking at the first debugging problem - but focus on imports

Talk about how we can get the imports working - PYTHONPATH and sys.path.append

may need something like this:

```py
import sys

sys.path.append(
    '/Users/danika/nc/teaching/seminar_repos/de_intro/code_discussions/de-errors-and-debugging')

from src.exercises.debug_me_01 import say_hello
```

# **`CMD + K - S` to save without formatting**

Can show

```sh
pytest -k test_file_name
```

To match specific test files

## Focusing on reading and understanding error messages

- Task 1/2 - expected value is not the received one

- Task 3 NameError - what does this mean?

- Task 4 AttributeError - What does this mean?

- Task 5 TypeError - What does this mean?

- Extension 1 - Good for breaking down bugs in sequence and getting to a working solution

- Work through rest of the extensions - focus on the test output etc.
