#!/usr/bin/python3
"""
This module contains a class defination

Attributes:
==========
    None

"""


class BaseGeometry:
    """
    An empty class at the moment

    Attributes:
    -----------
        None

    Methods:
    -----------
        area:   this returns an exception upon
                calling
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
