#!/usr/bin/python3
"""
This module has a function that checks if an object
is a direct instance of a given class
"""


def is_same_class(obj, a_class):
    """
    This checks if the obj is a class of a_claas

    Returns:
        True: if obj is an instant of a_class
        Fase: otherwise
    """
    return type(obj).__name__ == a_class.__name__
