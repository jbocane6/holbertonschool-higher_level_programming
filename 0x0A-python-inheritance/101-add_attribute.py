#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possible."""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object.
    Args:
        obj : Object to be added.
        name (str): Name of the new attribute.
        value (:obj:): Value of the new attribute.
    Raises:
        TypeError: can't add new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
