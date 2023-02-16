#!/usr/bin/python3
"""
This a module that contain a functons for
multiplying two given matrix

This module use the Numpy module

Operation:
    Given:
        Matrix_A of rowA x colA
        Matrix_B of rowB x colB
    Condition:
        colA == rowB
    Result:
        Matrix_N of rowA x colB


It handles several excceptions:
    Exceptions:
        TypeError:
            if the argument is not of type list
            if the argument is not a list of a list
            if any of the element is not an int or float
            if each matrix rows are not the same
        ValueError:
            if the argument passed is an empty list
            if both matrix does not satisfy the conditon
                for matrix multiplicaton
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two Matix:

        Args:
            m_a: int/float - row_a x col_a
            m_b: int/float - row_b x col_b

        Result:
            m_n: int/float - row_a x col_b

    """
    return np.matmul(m_a, m_b)
