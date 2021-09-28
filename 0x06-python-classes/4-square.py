#!/usr/bin/python3
"""4-square
Write a class Square that defines a square"""


class Square:
    """Square class.
    Attributes:
        __size (int): The size of the square."""
    def __init__(self, size=0):
        """Constructor of Square object with a size arg."""
        self.__size = size

    @property
    def size(self):
        """Getter of size."""
        return self.__size
        
    @size.setter
    def size(self, size):
        """Setter of size.
        Args:
            size (int): Size of the square.
        Raises:
            TypeError: Size must be an integer.
            ValueError: if size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area: returns the square's area"""
        return self.__size ** 2
