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
    """

    def __init__(self, size):
        """
        Constructor for all the necessary attributes for
        the square object.

        Instance Parameters:
        ----------
            size (int) : The side of the square
        """

        self.__size = size
