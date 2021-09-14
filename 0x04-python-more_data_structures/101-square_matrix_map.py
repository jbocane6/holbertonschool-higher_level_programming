#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda n: n**2, inner_list)) for inner_list in matrix]