#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
    using a JSON representation.
    Args:
        my_obj (object): Object to represent as JSON.
        filename: filename: Path and name of file.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
