#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after each of these \
    characters: ., ? and :
"""


def text_indentation(text):
    """prints a text
    Args:
        text (str): must be a string.
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    for i in text:
        c = count - 1
        if i == " " and (text[c] == "." or text[c] == ":" or text[c] == "?"):
            pass
        elif i == "." or i == ":" or i == "?":
            print("{}\n".format(i))
        else:
            print("{}".format(i), end="")
        count += 1
