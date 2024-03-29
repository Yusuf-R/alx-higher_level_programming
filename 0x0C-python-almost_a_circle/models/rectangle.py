#!/usr/bin/python3
"""
This module contains a class that inherits from a superclass
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    Private instance attributes:
        width: int
        height: int
        x: int
        y: int
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation with width, height, x, y, id

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x coordinate of the rectangle
            y: y coordinate of the rectangle
            id: id of the rectangle

        Raises:
            TypeError: height/width/x/y must be an integer
            ValueError: height/width must be >= 0
            ValueError: x/y must be >= 0

        """
        super().__init__(id)

        Rectangle.input_validator("width", width)
        self.width = width

        Rectangle.input_validator("height", height)
        self.height = height

        Rectangle.input_validator("x", x)
        self.x = x

        Rectangle.input_validator("y", y)
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, data):
        """
        width setter
        """
        Rectangle.input_validator("width", data)
        self.__width = data

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, data):
        """
        height setter
        """
        Rectangle.input_validator("height", data)
        self.__height = data

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, data):
        """
        x setter
        """
        Rectangle.input_validator("x", data)
        self.__x = data

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, data):
        """
        y setter
        """
        Rectangle.input_validator("y", data)
        self.__y = data

    @staticmethod
    def input_validator(data_name, data_value):
        """
        Validates all the inputs data
        """
        if type(data_value) != int:
            raise TypeError("{:s} must be an integer".format(data_name))

        if (data_name == "width" or data_name == "height") and data_value <= 0:
            raise ValueError("{:s} must be > 0".format(data_name))

        if (data_name == "x" or data_name == "y") and data_value < 0:
            raise ValueError("{:s} must be >= 0".format(data_name))

    def area(self):
        """
        Calculates the area of a rectangle
        Area = width * height
        """
        return self.__width * self.height

    def display(self):
        """
        Give a 2-D representaton of the rectangle
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        String representation of a rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Using argument vector to udates the attributes of a rectangle
        """
        attr = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0 and len(args) <= len(attr):
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        elif kwargs and len(kwargs) > 0 and len(kwargs) <= len(attr):
            for key, value in kwargs.items():
                if key not in attr:
                    pass
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a rectangle
        attributes
        """
        attr = ["id", "width", "height", "x", "y"]
        dic = {}
        for i in range(len(attr)):
            dic[attr[i]] = getattr(self, attr[i])
        return dic
