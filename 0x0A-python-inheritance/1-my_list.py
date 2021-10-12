#!/usr/bin/python3
"""Write a class MyList that inherits from list."""


class Mylist(list):
    """Class MyList that inherits from list."""
    def print_sorted(self):
        """Prints the list, but sorted."""
        print(sorted(self))
