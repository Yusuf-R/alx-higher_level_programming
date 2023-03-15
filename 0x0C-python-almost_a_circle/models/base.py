#!/usr/bin/pyhon3
"""This is  module that contian the base definaton of a class Base"""


class Base:
    """This is a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
