#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    return [replace if i == search else i for i in my_list]
"""Look how doesn't need to asigned the values to a new list,
   you can return a for in python"""
