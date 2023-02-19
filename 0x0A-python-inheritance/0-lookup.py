#!/usr/bin/python3
"""
This module contains a function that prints
out all the attributes and methods of an object
"""


def lookup(obj):
    """
    This function returns the list of all available
    attributes and mthods of an object
    """
    return (dir(obj))
