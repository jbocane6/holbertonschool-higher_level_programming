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

    def area(self):
        """Calculates the area of the rectangle.
        Returns: int: The rectangle area.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the message [Rectangle] <width>/<height>"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
