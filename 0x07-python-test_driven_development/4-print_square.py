#!/usr/bin/python3
"""
This is a module that contains a function for 
printing out the size of a square

Exceptoions:
    TypeError: if the arg is not an int of a float

    ValueError: if the arg is < 0
"""


def print_square(size):
    """
    This function prints out the size of square

    Args:
        size (int): the size of the square

    Returns:
        char: '#' denoting the size of the square
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for _ in range(size):
        print("#" * size)
