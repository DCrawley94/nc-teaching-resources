# Error Handling and TDD

https://www.figma.com/board/WbUhRleyEmdCEOaJlgMKuO/Error-Handling-and-TDD?node-id=0-1&t=Z3z7w12KMFhTYoJw-1

## Learning Objectives

- Create a method that raises both built in and custom Exceptions.
- Test these methods with TDD to ensure that correct errors are raised depending on certain conditions.
- Investigate how methods that raise errors can be used inside a try/except

## Intro

Introduce task + make sure students are clear on the purpose of the `validate` and `set_is_valid` methods.

## `validate`

Ask students what we could test for the `validate` methods. Hopefully we'll get some of the following:

name:

- raise error for invalid data type
- raise error for short length

age:

- raise error for invalid data type
- raise error if age isn't in accepted range

### Tests

```py
def test_validate_name_not_string(self):
    user = UserValidator(123, 25)
    with pytest.raises(TypeError, match="Name must be a string."):
        user.validate()

def test_validate_age_not_integer(self):
    user = UserValidator("John Doe", "twenty-five")
    with pytest.raises(TypeError, match="Age must be an integer."):
        user.validate()

def test_validate_name_empty(self):
    user = UserValidator("", 25)
    with pytest.raises(ValidationError, match="Name cannot be empty."):
        user.validate()

def test_validate_age_out_of_range(self):
    user = UserValidator("John Doe", -1)
    with pytest.raises(ValidationError, match="Age must be between 0 and 120."):
        user.validate()

    user = UserValidator("John Doe", 121)
    with pytest.raises(ValidationError, match="Age must be between 0 and 120."):
        user.validate()
```

### Solution

```py
class ValidationError(Exception):
    """Custom exception for User validation errors."""

    pass


def validate(self):
    # name must be a string
    if not isinstance(self.name, str):
        raise TypeError("Name must be a string.")

    # age must be an integer
    if not isinstance(self.age, int):
        raise TypeError("Age must be an integer.")

    # name cannot be empty
    if not self.name:
        raise ValidationError("Name cannot be empty.")

    # age must be within a valid range
    if not (0 <= self.age <= 120):
        raise ValidationError("Age must be between 0 and 120.")
```

## `set_is_valid`

This function should set the `is_valid` attribute depending on whether the `validate` method raises an error or not.

### Tests

```py
def test_set_is_valid_valid_user(self):
    user = UserValidator("John Doe", 25)
    user.set_is_valid()
    assert user.is_valid

def test_set_is_valid_invalid_name(self):
    user = UserValidator(123, 25)
    user.set_is_valid()
    assert user.is_valid == False

def test_set_is_valid_invalid_age(self):
    user = UserValidator("John Doe", "twenty-five")
    user.set_is_valid()
    assert user.is_valid == False

def test_set_is_valid_empty_name(self):
    user = UserValidator("", 25)
    user.set_is_valid()
    assert user.is_valid == False

def test_set_is_valid_age_out_of_range_low(self):
    user = UserValidator("John Doe", -1)
    user.set_is_valid()
    assert user.is_valid == False

def test_set_is_valid_age_out_of_range_high(self):
    user = UserValidator("John Doe", 121)
    user.set_is_valid()
    assert user.is_valid == False
```

### Solution

```py
def set_is_valid(self):
    try:
        self.validate()
        self.is_valid = True
    except (TypeError, ValidationError):
        self.is_valid = False
    except Exception:
        print("Something has gone very wrong :(")
```
