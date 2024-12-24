class ValidationError(Exception):
    pass


class UserValidator:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_valid = None

    def validate(self):
        if type(self.name) is not str:
            raise TypeError("Name must be a string")
        if len(self.name) < 1:
            raise ValidationError("Name must have a length of 1 or greater")

    def set_is_valid(self):
        try:
            self.validate()
            self.is_valid = True
        except Exception as e:
            print(e)
            self.is_valid = False


if __name__ == "__main__":
    user = UserValidator("", 57)
    user.set_is_valid()
    print(user.is_valid)


# Create a class: UserValidator
# UserValidator should be instantiated with a
# name and an age.

# The validate method should check the given
# name and age meets the requirements:
#  - name should be a string with a length > 0
#  - age should be a positive integer no larger than 120

# If the requirements aren’t satisfied then validate
#  should raise an appropriate Error

# The set_is_valid method should set the the
# is_valid attribute to a booelan value representing
#  the user’s validity.
