#!/usr/bin/python3
"""2-square
Write a class Square that defines a square"""


class Square:
    """Instantiation with optional size: def __init__(self, size=0):"""
    def __init__(self, size = 0):
        """Size must be an integer"""
        if type(size) != int:
            """Otherwise raise a TypeError exception with the message"""
            raise TypeError("size must be an integer")
        """If size is less than 0"""
        if size < 0:
            """Raise a ValueError exception with the message"""
            raise ValueError("size must be >= 0")
        """Private instance attribute: size"""
        self.__size = size
