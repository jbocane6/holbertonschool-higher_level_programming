#!/usr/bin/python3
"""Write a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
        matrix (list): lists of integers or floats.
        div (int or float): Integer or float.
    Return:
        int or float: list with new values
    Raises:
        TypeError: div must be a number
        ZeroDivisionError: division by zero
        TypeError: matrix must be a matrix (list of lists) of \
            integers/floats
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not(isinstance(matrix, list) and len(matrix) > 0 and
            all(isinstance(row, list) and len(row) > 0 for row in matrix) and
            all(isinstance(val, (int, float)) for row in matrix
                for val in row)):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(val / div, 2) for val in row] for row in matrix]
