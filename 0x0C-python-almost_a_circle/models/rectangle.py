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

        Rectangle.input_validator("heigth", height)
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

        if (data_name == "width" or data_name == "heigth") and data_value <= 0:
            raise ValueError("{:s} must be > 0".format(data_name))
        if (data_name == "x" or data_name == "y") and data_value < 0:
            raise ValueError("{:s} must be >= 0".format(data_name))
