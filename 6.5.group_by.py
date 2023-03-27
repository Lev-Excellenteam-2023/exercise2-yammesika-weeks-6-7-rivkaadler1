def group_by(func, iterable):
    """Groups elements of an iterable based on the result of applying a given function
    to each element.
    Args:
    - func (callable): A function
    - iterable (iterable): A collection of elements to be grouped by the return value of func when accepting them as
    parameters .

    Returns:
    - (dict): A dictionary, where: the keys are the values returned from the function passed as the first parameter.
    The value corresponding to a particular key is a list of all members for which the value appearing in the key is
     returned.
    """
    return_values = [func(x) for x in iterable]
    keys = list(set(return_values))
    group_by_dict = {key: [x for x in iterable if func(x) == key] for key in keys}
    return group_by_dict


print(group_by(len, ["hi", "bye", "yo", "try"]))