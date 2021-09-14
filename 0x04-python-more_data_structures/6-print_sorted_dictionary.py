#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))
"""We already know that .keys return a list of keys
   sorted() organize by int value, i use keys as iterator"""
