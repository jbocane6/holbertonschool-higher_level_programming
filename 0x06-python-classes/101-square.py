#!/usr/bin/python3
"""6-square
Return a class Square that defines a square"""


class Square:
    """Square class.
    Attributes:
        __size (int): The size of the square."""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor of Square object with a size and a position args."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size.
        Args:
            value (int): Size of the square.
        Raises:
            TypeError: Size must be an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter of position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of position.
        Args:
            value: int tuple.
        Raises:
            TypeError: Position must be a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(i, int) for i in value) and
                all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area: returns the square's area"""
        return self.__size ** 2
