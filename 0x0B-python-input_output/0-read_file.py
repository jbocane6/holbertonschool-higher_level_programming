#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it.
    Args:
        filename: Path and name of file.
    """
    with open(filename) as f:
        for line in f:
            print("{}".format(line), end="")
