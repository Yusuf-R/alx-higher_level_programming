#!/usr/bin/python3

"""
This module sum of two input and returns the result

Operation:
    it takes an input which could be either an int or a float
    it returns the sum of the two input as in int

Exceptions:
    it raises a TypeError if any of the input is not an int or a float
"""


def add_integer(a, b=98):
    """
    A function that adds two integers

    Args:
        a (int) or (float) : The first integer or float
        b (int) or (float) : The second integer or float

    Returns:
        int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        return TypeError('a must be an integer')

    elif not isinstance(b, (int, float)):
        return TypeError('b must be an integer')

    else:
        return int(a) + int(b)
