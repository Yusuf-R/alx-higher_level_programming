#!/usr/bin/python3
""" A module with the class definatoin of a square"""


class Square:
    """
    This is a blueprint class template for defining
    an object square

    Attributes
    ----------
    size (int) :    The sides of the square
                    This is the size of it sides
                    it is a private attribute

    Mehods:
    ----------
    area(self) : xcal the area of the square with the sides
    """

    def __init__(self, size=0):
        """
        Constructor for all the necessary attributes for
        the square object.

        Asigns the size parameters base on type checks
        and accepted values

        Instance Parameters:
        ----------
            size (int) : The side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This calculates and returns the area of the square

        Parameters
        ----------
        size(int) : The side of the square

        Returns
        ----------
        The area of the square calculated
        """

        return self.__size ** 2
