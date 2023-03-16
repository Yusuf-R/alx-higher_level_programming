#!/usr/bin/python3
"""
This is a module for describing the Square template
    it will inherits from the class Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    This is a class Square that inherits from the class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This is a constructor for the class Square
        """
        super().__init__(size, size, x, y, id)
        Rectangle.input_validator("size", size)
        self.size = size
        Rectangle.input_validator("x", x)
        self.x = x
        Rectangle.input_validator("y", y)
        self.y = y

    def __str__(self):
        """
        This is a string representation of the class Square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                          self.y, self.size)


