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

    def __eq__(self, other):
        """Ret: True if both instance area is same"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Ret: True if the both instance area are not the same"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Ret: True is insatance1 is less than instance2"""
        return self.area() < other.area()

    def __ge__(self, other):
        """Ret: True if instance1 is greater or equal to instance2"""
        return self.area() >= other.area()

    def __gt__(self, other):
        """Ret: True if instance1 is greater than instance2"""
        return self.area() > other.area()

    def __le__(self, other):
        """Ret: True if instance1 is less or equal to instance2"""
        return self.area() <= other.area()
