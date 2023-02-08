#!/usr/bin/python3
""" A module with the class definatoin of a square"""

class Square:
    """
    This is a blueprint class template for defining
    an object square

    Private Instance Attributes
    ---------------------------
    size (int) :    The sides of the square
                    This is the size of it sides
                    it is a private attribute

    position (tuple:int) : This an attribute that
                           defines the coordinate of
                           the square in (x, y) position


    Public Instnace Mehods:
    -----------------------
    area(self) :    return the area of the square with
                    the sides

    my_print(self) : return the prints in stdout the area
                     of the square with the character #

    position(self) : This is cordinate in space that defines
                     the square via x-y axis

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor for all the necessary attributes for
        the square object.

        Asigns the size and positional parameters base on type checks
        and accepted values

        Instance Parameters:
        ----------
            size (int) : The side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """ Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position of the square """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        This function prints to stdout the area of
        the square using '#' graphics

        The output to stdout is positoned base on the
        coridinates of the x-y axis

        Parameters
        ----------
        __size (int) : The sides of the square

        __position(tuple:int) : The x-y axis in a tuple

        Returns
        -------
        The graphics display of the area of the square for the given size
        base on the cordinates to the stdout
        """
        if self.__size == 0:
            print()
        else:
            for y_axis in range(self.__position[1]):
                print()
            for x_row in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size)
