#!/usr/bin/python3
"""This is  module that contian the base definaton of a class Base"""
import json


class Base:
    """This is a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a constructor"""

        if id is not None and type(id) != int:
            raise TypeError("id must be an integer")

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This is a static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
