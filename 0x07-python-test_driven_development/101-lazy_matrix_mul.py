#!/usr/bin/python3
"""
This a module that contain a functons for
multiplying two given matrix

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

    te_a_msg = "m_a should contain only integers or floats"
    te_b_msg = "m_b should contain only integers or floats"

    te_ra = "each row of m_a must be of the same size"
    te_rb = "each row of m_b must be of the same size"

    if matrix_type_check(m_a):
        pass
    else:
        raise TypeError("m_a must be a list")

    if matrix_type_check(m_b):
        pass
    else:
        raise TypeError("m_b must be a list")

    if is_matrix_list_of_list(m_a):
        pass
    else:
        raise TypeError("m_a must be a list of lists")

    if is_matrix_list_of_list(m_b):
        pass
    else:
        raise TypeError("m_b must be a list of lists")

    if is_matrix_empty(m_a):
        pass
    else:
        raise TypeError("m_a can't be empty")

    if is_matrix_empty(m_b):
        pass
    else:
        raise TypeError("m_b can't be empty")

    if is_list_of_list_strict_int_or_float(m_a) is False:
        raise TypeError(te_a_msg)

    if is_list_of_list_strict_int_or_float(m_b) is False:
        raise TypeError(te_b_msg)

    if is_list_list_rectangle(m_a) is False:
        raise TypeError(te_ra)

    if is_list_list_rectangle(m_b) is False:
        raise TypeError(te_rb)

    row_a = get_row(m_a)
    col_a = get_col(m_a)

    row_b = get_row(m_b)
    col_b = get_col(m_b)

    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    ma = np.array(m_a)
    mb = np.array(m_b)
    new_matrix = ma.dot(mb)
    return new_matrix


def matrix_type_check(a_mx):
    """Checks the type of the arg must be a type list"""
    if type(a_mx) is list:
        return True
    else:
        return False


def is_matrix_list_of_list(a_mx):
    """Ensure the arg is list of a list"""
    check_list_list = all(isinstance(g, list) for g in a_mx)
    if check_list_list:
        return True
    else:
        return False


def is_matrix_empty(a_mx):
    """Checks if the arg is empty"""
    if any(a_mx):
        return True
    else:
        return False


def is_list_of_list_strict_int_or_float(a_mx):
    """Checks if all element is of type int or flaot"""
    for i in range(len(a_mx)):
        for j in range(len(a_mx[i])):
            if type(a_mx[i][j]) in [int, float]:
                pass
            else:
                return False


def is_list_list_rectangle(a_mx):
    """Checks if all the rows in each matrix are equal"""
    for _, elem in enumerate(a_mx):
        if len(elem) == len(a_mx[0]):
            pass
        else:
            return False


def get_row(a_mx):
    """Returns the number of rows in the matrix"""
    return len(a_mx)


def get_col(a_mx):
    """Returns the number of cols in the matrix"""
    return len(a_mx[0])


def new_matrix(r, c):
    """Intantiate the new_matrix with zeroes"""
    m = []
    for _ in range(r):
        z = []
        for _ in range(c):
            z.append(0)
        m.append(z)
    return m
