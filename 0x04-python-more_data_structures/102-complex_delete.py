#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = a_dictionary.copy()
    for k, v in new_dictionary.items():
        if value in v:
            del a_dictionary[k]
    return a_dictionary
"""copy() returns a copy of the dictionary
   items(return key & value as a tuple) with indexes key and value"""
