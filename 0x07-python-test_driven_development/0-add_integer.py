#!/usr/bin/python3
"""Prototype that writes a function that adds 2 integers."""


def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
        a (int): Integer or float term.
        b (int): Integer or float term.
    Return:
        int: The result of the sum.
    Raises:
        TypeError: Both terms must be integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
