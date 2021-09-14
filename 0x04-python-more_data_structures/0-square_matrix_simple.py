#!/usr/bin/python3
def square(number):
    return number ** 2

new_matrix = []
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        new_matrix.append(list(map(square, matrix[i])))
    return new_matrix
