#!/usr/bin/python3
"""Function that returns True if the object is exactly an instance of the
specified class otherwise False."""


def is_same_class(obj, a_class):
    """Look if an object is exactly an instance of a specified class.
    Args:
        a (int): number.
    Return:
        True: If the object is exactly an instance of the specified class
        False: Otherwise.
    """
    return (True) if (type(obj) == a_class) else False
