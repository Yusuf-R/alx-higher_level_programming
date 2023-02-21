#!/usr/bin/python3
"""
This module contains a class that inherits from a superclass
as defined
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class will inherit from Base_Geometry class
    Private Instance Attributes:
        width:  int
        height: int
    """
    def __init__(self, size):
        """
        Constructor object instance of the Rectangle class

        Parameters:
        ----------
        size:   int
                sides of the square
        Methods:
        ----------
        area:   int
                area of the Square
        """

        super().integer_validator(name="size", value=size)
        self.__size = size

    def __str__(self):
        sq_name = Rectangle.__name__
        return "[{}] {}/{}".format(sq_name, self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
