#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [1, 2],
        [3, float('inf')]
    ]
print(matrix_divided(matrix, -2))
print(matrix)
