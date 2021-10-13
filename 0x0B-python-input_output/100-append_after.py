#!/usr/bin/python3
"""Write a function that inserts a line of text to a file,
after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string.
    Args:
        filename : Path and name of file.
        search_string (str): String to find.
        new_string (str): String to write.
    """
    with open(filename, "r") as f:
        full_text = f.readlines()

    new_text = []
    s = ""
    for index, line in enumerate(full_text):
        new_text.append(line)
        if search_string in line:
            new_text.append(new_string)

    with open(filename, "w") as f:
        f.write(s.join(new_text))
