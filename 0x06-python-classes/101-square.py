#!/usr/bin/python3
"""101-square
Write a class Square that defines a square"""


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

    def __str__(self):
        """Stores a square of #'s and then return it as a string to method print"""
        str = ""
        if self.__size != 0:
            """if self.__size != 0 stores a new line"""
            for i in range(self.__position[1]):
                str += "\n"
            for j in range(self.__size):
                """Stores a new square made by spaces and #"""
                str += " " * self.__position[0] + "#" * self.__size
                if j < self.__size - 1:
                    str += "\n" 
        return str
