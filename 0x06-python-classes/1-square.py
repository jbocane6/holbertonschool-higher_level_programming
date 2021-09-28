#!/usr/bin/python3
"""1-square
Write a class Square that defines a square"""


class Square:
    """Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        """Private instance attribute: size"""
        self.__size = size
