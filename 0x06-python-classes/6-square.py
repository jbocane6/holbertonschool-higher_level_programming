#!/usr/bin/python3
class Square:
    def __init__(self, size = 0, position = (0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
    def position(self, value):
        if len(value != 2):
            raise IndexError("position must be a tuple of 2 positive integers")
    def area(self):
        return self.__size ** 2
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[1] > 0:
                for j in range(self.__position[0]):
                    print("_",end="")
            else:
                for j in range(self.__position[0]):
                    print(" ",end="")
            for j in range(self.__size):
                print("#",end="")
            print("")
