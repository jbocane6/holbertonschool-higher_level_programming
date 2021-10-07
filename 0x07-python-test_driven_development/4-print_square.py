#!/usr/bin/python3
"""PWrite a function that prints a square with the character #."""


def print_square(size):
    """prints a square with the character #.
    Args:
        size (int): size length of the square.
    Raises:
        TypeError: must be an integer
        ValueError: must be >= 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
