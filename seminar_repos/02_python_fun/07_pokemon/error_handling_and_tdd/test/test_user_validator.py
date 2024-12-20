from src.user_validator_end import UserValidator


class TestUserValidatorAttributes:
    def test_attributes(self):
        user = UserValidator("Geoff", 57)
        assert user.name == "Geoff"
        assert user.age == 57
        assert not user.is_valid
