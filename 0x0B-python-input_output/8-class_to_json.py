#!/usr/bin/python3
"""Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object."""
import json


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj (object): Object to represe  nt as JSON.
    Return:
        type of return int: what return
    """
    return obj.__dict__
