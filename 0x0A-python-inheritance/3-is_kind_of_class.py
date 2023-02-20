#!/usr/bin/python3
"""
This module has a function that checks if an object
is a direct or indirect instance of a given class
"""


def is_kind_of_class(obj, a_class):
    """
    This checks if the obj is a class of a_class
    or a subclass of a_claas

    Returns:
        True: if obj direct instance or indirect instacne
        of a_class
        Fase: otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
