#!/usr/bin/python3
"""Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
otherwise False."""


def inherits_from(obj, a_class):
    """Look if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    Args:
        obj : Number.
    Return:
        True : If the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
        False : Otherwise.
    """
    return (type(obj) == a_class or isinstance(obj, a_class))
