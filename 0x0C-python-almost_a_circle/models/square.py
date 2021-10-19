#!/usr/bin/python3
"""Class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Inicialize the square
        Args:
            size (int): size of the square.
            x (int): x coordinate of the square.
            y (int): y coordinate of the square.
            id (int): Id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        """Setter of size.
        Args:
            size (int): Value to set.
        Raises:
            TypeError: Size must be an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """Return the square's identifier.
        Return:
            str: Square's identifier.
        """
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update values of the square.
        Args:
            args (tuple): Tuple of values.
            kwargs (dictionary): Dictionary of values."""
        if args:
            args_list = ["id", "size", "x", "y"]
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
        args_list = ["id", "size", "x", "y"]
        new = {}
        for key in args_list:
            new[key] = getattr(self, key)
        return new
