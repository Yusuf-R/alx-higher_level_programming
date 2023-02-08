#!/usr/bin/python3
""" A module with the class definatoin of a square"""


class Square:
    """
    This is a blueprint class template for defining
    an object square

    Private instance Attributes
    ---------------------------
    size (int) :    The sides of the square
                    This is the size of it sides
                    it is a private attribute

    Public Instnace Mehods:
    -----------------------
    area(self) :    return the area of the square with
                    the sides

    my_print(self) : return the prints in stdout the area
                     of the square with the character #

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

    @property
    def size(self):
        """
        This deocrator @property helps to set the function
        to behave like an attributes

        This helps to eliminate the () when calling it
            Example:
                my_square.size : This will return the value of size
                rather than calling it as my_square.size()

        Returns: the current value of the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This decorator helps to set a new value to our size

        It comes with an exception handling

            ValueError
            TypeError

        Returns: the value of the new set side of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        # if isinstance(int(size), int):
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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

    def my_print(self):
        """
        This function prints to stdout the area of the square using '#' graphics

        Parameters
        ----------
        __size (int) : The sides of the square

        Returns
        -------
        The graphics display of the area of the square for the given size
        """
        if self.__size == 0:
            print()
        else:
            for x_row in range(self.__size):
                for y_col in range(self.__size):
                    print("#", end="")
                print()
