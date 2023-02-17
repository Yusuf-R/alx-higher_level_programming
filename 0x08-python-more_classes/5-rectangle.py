#!/usr/bin/python3
"""
This is a module that contains the template for the class Rectangle
"""


class Rectangle:
    """
    This is a template for the class Rectangle

    Attributes:
    -----------
        width : int
                defines the width of the rectangle

        height: int
                defines the height of the rectangle

    Methods:
    -----------
        static method:
            input_check: ensures the input is strictly an integer
            value_check: ensures the value is not less than 0

        decorators:
            get_width: returns the width of the rectangle
            set_width: sets the width of the rectangle

            get_height: returns the height of the rectangle
            set_height: sets the height of the rectangle

    Exceptions
    -----------
        TypeError: if the input is not an integer
        ValueError: if the input is less than zero
    """
    pass

    def __init__(self, width=0, height=0):
        """
        This instantiates the object of the class with
        the given width and height

        Private Instance Attributes:
        ----------------------------
        width : int
                defines the width of the rectangle

        height: int
                defines the height of the rectangle

        Exceptions:
        -----------
            TypeError:
                if arg is not of type int or float
            ValueError:
                if the arg is less than zero
        """
        if Rectangle.check_input(width) is False:
            raise TypeError("width must be an integer")
        if Rectangle.check_input(height) is False:
            raise TypeError("height must be an integer")

        if Rectangle.check_value(width) is False:
            raise ValueError("width must be >= 0")
        if Rectangle.check_value(height) is False:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ This gets the  width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width base on the data passed """
        if Rectangle.check_input(width) is False:
            raise TypeError("width must be an integer")
        if Rectangle.check_value(width) is False:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ This gets the  width"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the width base on the data passed """
        if Rectangle.check_input(height) is False:
            raise TypeError("height must be an integer")
        if Rectangle.check_value(height) is False:
            raise ValueError("height must be >= 0")
        self.__height = height

    @staticmethod
    def check_input(data):
        if type(data) in [int]:
            pass
        else:
            return False

    @staticmethod
    def check_value(data):
        if data < 0:
            return False
        else:
            pass

    def __str__(self):
        """This print the rectangle with the character #"""
        disp_rect = ""
        if self.__width == 0 or self.__height == 0:
            return disp_rect
        for _ in range(self.__height):
            disp_rect += "#" * self.__width + "\n"
        disp_rect = disp_rect[:-1]
        disp_rect = disp_rect.split("\n")
        disp_rect = "\n".join(disp_rect)
        return disp_rect

    def __repr__(self):
        """
        It returns a string representation of the rectangle.
        This can be passed as an argument to eval() to create this instance
        """
        repr_rect = "Rectangle({}, {})".format(self.__width, self.__height)
        return repr_rect

    def __del__(self):
        """
        It deletes the instance of the class
        """
        # del self.__width
        # del self.__height
        # # del Rectangle
        print("Bye rectangle...")
    
    def area(self):
        """Returns the area of the rectangle: width * height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter: 2 * (width + height)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height
