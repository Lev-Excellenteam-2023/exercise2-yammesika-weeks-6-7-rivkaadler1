import functools


class InvalidArgumentTypeError(Exception):
    pass


def type_check(correct_type):
    """
    A decorator function that checks whether the input argument of a function is of the expected type.

    :param correct_type: The expected type of the input argument.
    :raises InvalidArgumentTypeError: If the input argument is not of the expected type.
    :return: The decorated function with input type-checking functionality.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(argument):
            if not isinstance(argument, correct_type):
                raise InvalidArgumentTypeError(
                    f"Invalid argument type.  Received {type(argument)} but Expected {correct_type}.")
            return func(argument)

        return wrapper

    return decorator
