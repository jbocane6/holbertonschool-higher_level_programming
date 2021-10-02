#!/usr/bin/python3
"""LockedClass to prevent atribute creation"""


class LockedClass:
    """Class that prevent attribute ceation"""
    __slots__ = ['first_name']
