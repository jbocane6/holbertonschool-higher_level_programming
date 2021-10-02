#!/usr/bin/python3
"""Class Rectangle:
Write an empty class Rectangle that defines a rectangle:
"""


class Rectangle:
    """A Rectangle class with 2 attributes: width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if not self.__width or not self.__height:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Stores a square of #'s and then return it as a string"""
        printstr = ""
        if self.__width == 0 or self.__height == 0:
            """if self.__width and self.__height == 0 stores a new line"""
            return printstr

        for i in range(self.__height):
            """Stores a new square made by spaces and #"""
            printstr += "#" * self.__width
            if i is not self.__height - 1:
                printstr += "\n"
        return printstr

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
