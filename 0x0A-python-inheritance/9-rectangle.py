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
        self.__width = width
        super().integer_validator(name="height", value=height)
        self.__height = height

    def area(self):
        area =  self.__width * self.__height
        return area

    def __str__(self):
        rec_name = self.__class__.__name__
        return "[{}] {}/{}".format(rec_name, self.__width, self.__height)
