#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle."""
    def __init__(self, size):
        """Instantiation with size
        Args:
            size (int): Must be positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates the area of the rectangle.
        Returns: int: The rectangle area.
        """
        return self.__size ** 2

    def __str__(self):
        """Return the message [Square] <width>/<height>"""
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
