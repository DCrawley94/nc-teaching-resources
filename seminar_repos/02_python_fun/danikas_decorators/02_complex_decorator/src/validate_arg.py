def validate_arg(data_type):
    """
    Decorator should be applied to a function that accepts a single argument.
    It will check that the data type of the argument provided to the decorated
    function is correct and only invoke the function if that is the case. If
    the argument is the correct data type then return value of func should be
    returned. Otherwise a string of "Incorrect data type" should be returned.
    """
    def outer_wrapper(func):
        def inner_wrapper(arg):
            if isinstance(arg, data_type):
                return func(arg)
            else:
                return "Incorrect data type"
        return inner_wrapper
    return outer_wrapper
