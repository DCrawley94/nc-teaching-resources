from src.user_validator import UserValidator, ValidationError
import pytest


class TestUserValidatorAttributes:
    def test_attributes(self):
        user = UserValidator("Geoff", 57)
        assert user.name == "Geoff"
        assert user.age == 57
        assert not user.is_valid


class TestUserValidatorValidateMethod:
    # test if name is not a string: raise exception
    def test_validate_name_not_string(self):
        user = UserValidator(False, 57)

        with pytest.raises(TypeError, match="Name must be a string"):
            user.validate()

    # test if length of name < 1: raise exception
    def test_validate_invalid_string_length(self):
        user = UserValidator("", 57)

        with pytest.raises(
            ValidationError, match="Name must have a length of 1 or greater"
        ):
            user.validate()


# test if age is not integer: raise exception
# if int is not in accepted range: raise exception

# if user is valid: no exception raised


class TestUserValidatorSetIsValid:
    def test_sets_is_valid_to_true_if_user_data_is_valid(self):
        user = UserValidator("Jenny", 57)

        user.set_is_valid()

        assert user.is_valid is True

    def test_set_is_valid_to_false_if_user_data_is_not_valid(self):
        user = UserValidator(False, 57)

        user.set_is_valid()

        assert user.is_valid is False
