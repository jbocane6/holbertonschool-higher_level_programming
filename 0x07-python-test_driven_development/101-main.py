#!/usr/bin/python3
from numpy.matrixlib.defmatrix import matrix


lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

matrix_a = [
    [1, 2],
    [3, 4]
]
matrix_b = [
    [5, 6],
    [7, 8]
]
""" print(lazy_matrix_mul()) """
print(lazy_matrix_mul(["School", 123], matrix_b))
