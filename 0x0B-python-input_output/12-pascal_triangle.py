#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a list
of lists of integersrepresenting the Pascal’s triangle of n."""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n.
    Args:
        n (int): Size of triangle.
    Return:
        list (list): List of lists of integers.
    """
    pascal_list = []
    pascal_temp = []
    pascal_new = []
    if n <= 0:
        return pascal_list
    for i in range(n):
        if i == 0:
            pascal_list.append([1])
        if i == 1:
            pascal_list.append([1, 1])
        if i > 1:
            pascal_temp = pascal_list[len(pascal_list) - 1]
            pascal_new.append(1)
            for j in range(len(pascal_temp) - 1):
                pascal_new.append(pascal_temp[j] + pascal_temp[j + 1])
            pascal_new.append(1)
            pascal_list.append(pascal_new)
            pascal_new = []
    return pascal_list
