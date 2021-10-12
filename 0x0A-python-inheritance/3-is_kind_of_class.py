#!/usr/bin/python3
"""Function that returns True if the object is an instance of, or if
the object is an instance of a class that inherited from,
the specified class otherwise False."""


def is_kind_of_class(obj, a_class):
    """Look if the object is an instance of, or if
    the object is an instance of a class that inherited from.
    Args:
        obj : Number.
    Return:
        True : If the object is an instance of, or if
        the object is an instance of a class that inherited from.
        False : Otherwise.
    """
    return issubclass(obj, a_class)
