#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.
    """
    if (type(list_of_integers) != list or len(list_of_integers) == 0):
        return None
    return peak_cmp(list_of_integers, len(list_of_integers))


def peak_cmp(list_of_integers, size):
    """Use recursion to find peak"""
    if size <= 2:
        return max(list_of_integers)

    mid_size = int(size / 2)
    peak = list_of_integers[mid_size]
    peak_left = list_of_integers[:mid_size]
    peak_right = list_of_integers[mid_size + 1:]

    if list_of_integers[mid_size - 1] < peak > list_of_integers[mid_size + 1]:
        return peak
    else:
        return peak_cmp(peak_left, mid_size) if peak_cmp(
                        peak_left, mid_size) > peak_cmp(
                            peak_right, len(peak_right)) else peak_cmp(
                                peak_right, len(peak_right))
