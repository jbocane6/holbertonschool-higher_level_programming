#!/usr/bin/python3
def best_score(a_dictionary):
    return None if not a_dictionary else max(a_dictionary, key = a_dictionary.get) 
"""get returns the value of the key, max returns the greater value"""
