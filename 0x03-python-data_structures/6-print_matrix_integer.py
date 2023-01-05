#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_out in matrix:
        counter = 0
        m_len = len(matrix_out)
        for matrix_in in matrix_out:
            counter += 1
            if(counter == m_len):
                print("{}".format(matrix_in), end="")
            else:
                print("{:d}".format(matrix_in), end=" ")
        print()
