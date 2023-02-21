#!/usr/bin/python3
"""
This module contains a class that inherits from a superclass
as defined
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class will inherit from Base_Geometry class
    Private Instance Attributes:
        width:  int
        height: int
    """
    def __init__(self, width, height):
        """
        Constructor object instance of the Rectangle class

        Parameters
        ----------
        width:  int
                width of the rectangle

        height: int
                height of the rectangle
        """
        super().integer_validator(name="width", value=width)
        super().integer_validator(name="height", value=height)

        self.__width = width
        self.__height = height
