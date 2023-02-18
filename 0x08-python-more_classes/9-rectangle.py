#!/usr/bin/python3
"""
This is a module that contains the template for the class Rectangle
"""


class Rectangle:
    """
    This is a template for the class Rectangle

    Private Instance Attributes:
    ----------------------------
        width : int
                defines the width of the rectangle

        height: int
                defines the height of the rectangle

    Public Class Attributes:
    ------------------------
        number_of_instances : int
                              increments upon every instance
                              decrement upon evry deleting of an instance

        print_symbol:   str
                        This is used to print of the rectangel base
                        on user define settings

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
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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
            disp_rect += str(self.print_symbol) * self.__width + "\n"
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
        Rectangle.number_of_instances -= 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        It checks if the two rectangles are bigger or equal

        Parameters:
        -----------
            rect_1: Rectangle
                defines the first rectangle

            rect_2: Rectangle
                defines the second rectangle

        Returns:
        --------
            Rectangle:
                returns the bigger or equal rectangle
        """
        if isinstance(rect_1, Rectangle):
            pass
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle):
            pass
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        r1 = rect_1.area()
        r2 = rect_2.area()
        if r1 > r2:
            return rect_1
        elif r1 < r2:
            return rect_2
        if r1 == r2:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        It creates a square of the given size

        Parameters:
        -----------
            size: int
                defines the size of the square

        Returns:
        --------
            Rectangle:
                returns a square of the given size
        """
        if Rectangle.check_input(size) is False:
            raise TypeError("size must be an integer")
        if Rectangle.check_value(size) is False:
            raise ValueError("size must be >= 0")
        return Rectangle(size, size)
