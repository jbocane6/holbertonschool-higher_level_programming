#!/usr/bin/python3
"""Write a class BaseGeometry."""


class BaseGeometry():
    """Class BaseGeometry."""
    def area(self):
        """Raises an Exception with a message.
        Raises:
            Empty exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value.
        Args:
            name (string): String.
            value (int): Value associated to name.
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))

