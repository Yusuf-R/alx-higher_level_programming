#!/usr/bin/python3
"""A module with a function that creates a Pascal Triangle"""


def pascal_triangle(n):
    """This function creates a pascal triangle of nth rows"""
    pascal = []
    if n <= 0:
        return pascal
    for r in range(n):
        inner_list = []
        for c in range(r + 1):
            if c == 0 or c == r:
                inner_list.append(1)
            else:
                inner_list.append(pascal[r - 1][c - 1] + pascal[r - 1][c])
        pascal.append(inner_list)
    return pascal
