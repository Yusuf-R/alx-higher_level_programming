#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_out in matrix:
        for matrix_in in matrix_out:
            print("{:d}".format(matrix_in), end=" ")
        print()
