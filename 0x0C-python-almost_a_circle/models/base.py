#!/usr/bin/python3
"""This is  module that contian the base definaton of a class Base"""
import json
from os import path


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

    @classmethod
    def create(cls, **dictionary):
        """This is a class method that returns an instance with all attributes
        already set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(8, 5, 3, 6, 18)
        elif cls.__name__ == "Square":
            dummy_instance = cls(4, 2, 8, 10)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """This is a class method that returns a list of instances"""
        py_obj_inst = []
        files = ["Rectangle.json", "Square.json"]
        filename = cls.__name__ + ".json"
        if not path.exists(filename) or filename not in files:
            return py_obj_inst
        with open(filename, mode="r", encoding="utf-8") as f:
            js_obj = f.read()
        py_obj = cls.from_json_string(js_obj)
        for i in range(len(py_obj)):
            py_obj_inst[i] = cls.create(**py_obj_inst[i])
        return py_obj_inst
