#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary
"""In pop if key is not found and the second argument is not given
   it will return a KeyError"""
