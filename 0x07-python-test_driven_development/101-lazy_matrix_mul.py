#!/usr/bin/python3
"""Write a function that multiplies 2 matrices by using the module NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices.
    Args:
        m_a (list of int or float lists): first matrix.
        m_b (list of int or float lists): second matrix.
    Return:
        list of int or float lists: resulting matrix.
    """
    return np.dot(m_a, m_b)
