#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Instantiation with width and height
        Args:
            width (int): Must be positive integer.
            height (int): Must be positive integer.
        self.__size = size
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
