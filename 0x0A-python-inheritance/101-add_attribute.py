#!/usr/bin/python3
"""
This module contains a funtion that tries to implement
adding an attribute to a class
"""


def add_attribute(attr_obj, attr_name, attr_val):
    """Sets an attribute to an object"""
    if hasattr(attr_obj, '__dict__'):
        attr_obj.__setattr__(attr_name, attr_val)
    else:
        raise TypeError("can't add new attribute")
