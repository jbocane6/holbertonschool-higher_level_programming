#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.
    Args:
        filename: filename: Path and name of file.
    Return:
        Object obtained.
    """
    obj = ""
    with open(filename, "r") as f:
        for line in f:
            obj = json.loads(line)
    return obj
