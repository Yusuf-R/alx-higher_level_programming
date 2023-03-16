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

    def __str__(self):
        """
        This is a string representation of the class Square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, data):
        Rectangle.input_validator("width", data)
        self.width = data

    def update(self, *args, **kwargs):
        """
        This is a method that assigns an argument to each attribute
        using args and kwargs
        """
        sq_attrib = ["id", "size", "x", "y"]
        if args and len(args) > 0 and len(args) <= len(sq_attrib):
            for i in range(len(args)):
                setattr(self, sq_attrib[i], args[i])
        elif kwargs and len(kwargs) > 0 and len(kwargs) <= len(sq_attrib):
            for key, value in kwargs.items():
                if key not in sq_attrib:
                    pass
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This is a method that returns the dictionary representation
        of a Square's attributes
        """
        sq_attrib = ["id", "size", "x", "y"]
        sq_dict = {}
        for i in range(len(sq_attrib)):
            sq_dict[sq_attrib[i]] = getattr(self, sq_attrib[i])
        return sq_dict
