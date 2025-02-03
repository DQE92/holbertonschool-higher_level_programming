#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if the object `obj` is an instance of the class `a_class`.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        bool: True if `obj` is an instance of `a_class`, otherwise False.
    """
    return isinstance(obj, a_class)
