#!/usr/bin/python3
"""This module stores the attribute of an object"""


def class_to_json(obj):
    """
    This function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
    """
    py_obj = obj.__dict__
    return py_obj
