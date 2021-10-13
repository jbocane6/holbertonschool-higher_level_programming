#!/usr/bin/python3
"""Write a function that returns an object (Python data structure)
represented by a JSON string."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.
    Args:
        my_str (String): JSON String.
    Return:
        object: Object represented.
    """
    return json.loads(my_str)
