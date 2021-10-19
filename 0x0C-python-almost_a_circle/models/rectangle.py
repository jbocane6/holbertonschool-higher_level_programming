#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inicialize the rectangle.
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): x coordinate of the rectangle.
            y (int): y coordinate of the rectangle.
            id (int): Id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """Setter of width.
        Args:
            width (int): Value to set.
        Raises:
            TypeError: Width must be an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """Setter of height.
        Args:
            height (int): Value to set.
        Raises:
            TypeError: Height must be an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """Setter of x.
        Args:
            x (int): Value to set.
        Raises:
            TypeError: X must be an integer.
            ValueError: if x is less than 0.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """Setter of y.
        Args:
            y (int): Value to set.
        Raises:
            TypeError: Y must be an integer.
            ValueError: if y is less than 0.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates area of rectangle.
        Return:
            int: Total area.
        """
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle of #s depending x & y coordinates."""
        print("{}".format("\n" * self.__y), end="")
        for i in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            print("{}".format("#" * self.__width))

    def __str__(self):
        """Return the rectangle's identifier.
        Return:
            str: Rectangle's identifier.
        """
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update values of the rectangle.
        Args:
            args (tuple): Tuple of values.
            kwargs (dictionary): Dictionary of values."""
        if args:
            args_list = ["id", "width", "height", "x", "y"]
            for i, val in enumerate(args):
                setattr(self, args_list[i], val)
        elif kwargs:
            for val in kwargs:
                setattr(self, val, kwargs[val])

    def to_dictionary(self):
        """Use args to create a dictionary
        Return:
            new: Dictionary.
        """
        args_list = ["id", "width", "height", "x", "y"]
        new = {}
        for key in args_list:
            new[key] = getattr(self, key)
        return new
