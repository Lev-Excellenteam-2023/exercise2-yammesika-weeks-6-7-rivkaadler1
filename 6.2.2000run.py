import time


def timer(f, *args, **kwargs):
    """
    Measures the execution time of a given function `f` and returns it.

    Args:
    - f (function): The function to measure the execution time of.
    - *args: Variable length argument list to be passed to the function `f`.
    - **kwargs: Arbitrary keyword arguments to be passed to the function `f`.

    Returns:
    - (float): The execution time of the function `f` in seconds.
    """
    start_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")
