#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    Args:
        filename : Path and name of file.
        text (str): String to write.
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
