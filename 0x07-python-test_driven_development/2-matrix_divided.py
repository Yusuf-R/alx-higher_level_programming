#!/usr/bin/python3

"""
This is module for performing matrix division

Operation:
    it takes a matrix and divide each element
    by the divisor

Exceptions:
    This module raises the following exceptions

    TypeError:
        if div is not an int or float
        if any of the matrix element is not an int or a float
        if any rows of the matrix is nott of the same lenght
    ZeroDivisionError:

        if div equals to zero

Retunrs:
    A matrix of element in 2-d.p
"""


def matrix_divided(matrix, div):
    """
    A function that does scalar division of a matrix

    Args:
        matrix: list of (int or float):
    """

    te_1 = "Each row of the matrix must have the same size"
    te_2 = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(te_2)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for rows in range(len(matrix) - 1):
        if rows < len(matrix) - 1:
            if len(matrix[rows]) != len(matrix[rows + 1]):
                raise TypeError(te_1)
            else:
                pass
    for rows in matrix:
        for cols in rows:
            if not isinstance(cols, (int, float)):
                raise TypeError(te_2)
    mx_res = [
        [
            round(float(matrix[rows][cols]/div), 2)
            for cols in range(len(matrix[0]))
        ]
        for rows in range(len(matrix))
            ]
    return mx_res
