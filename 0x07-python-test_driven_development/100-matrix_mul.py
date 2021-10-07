#!/usr/bin/python3
"""Write a function that multiplies 2 matrices."""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices.
    Args:
        m_a (list of int or float lists): first matrix.
        m_b (list of int or float lists): second matrix.
    Return:
        list of int or float lists: resulting matrix.
    Raises:
        TypeError: must be a list of lists
        ValueError: can't be empty
        TypeError: should contain only integers or floats
        TypeError: each row of m_a must be of the same size
        ValueError: can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not all(row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(row for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(val, (int, float)) for row in m_a for val in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[round(sum(a * b for a, b in zip(row_a, col_b)), 2)
             for col_b in zip(*m_b)] for row_a in m_a]
