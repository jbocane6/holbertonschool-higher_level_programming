#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for inner_list in matrix:
        for i in range(len(inner_list)):
            print("{:d}".format(inner_list[i]), end="")
            if i < len(inner_list) - 1:
                print(" ", end="")
        print("")
