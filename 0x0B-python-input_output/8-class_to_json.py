#!/usr/bin/python3
"""Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj (object): Object to represent as JSON.
    Return:
        dict: Dictionary.
    """
    return obj.__dict__
