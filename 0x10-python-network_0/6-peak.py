#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.
    """
    size = len(list_of_integers)
    if (type(list_of_integers) != list or size < 1):
        return None
    return peak_cmp(list_of_integers, size)


def peak_cmp(list_of_integers, size):
    """Use recursion to find peak"""
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)

    mid_size = int(size / 2)
    peak = list_of_integers[mid_size]
    peak_left = list_of_integers[mid_size - 1]
    peak_right = list_of_integers[mid_size + 1]
    list_left = list_of_integers[:mid_size]
    list_right = list_of_integers[mid_size + 1:]

    if peak_left < peak > peak_right:
        return peak
    else:
        return max(peak_cmp(list_right, len(list_right)), peak_cmp(
                                            list_left, mid_size))
