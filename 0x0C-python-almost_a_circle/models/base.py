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

    @classmethod
    def save_to_file(cls, list_objs):
        """This is a class method that writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        py_list = [obj.to_dictionary() for obj in list_objs]

        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if len(list_objs) == 0:
                f.write("[]")
            else:
                f.write(cls.to_json_string(py_list))

    @staticmethod
    def from_json_string(json_string):
        """This is a static method that returns the list of the JSON string
        representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
