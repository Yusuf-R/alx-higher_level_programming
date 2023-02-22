#!/usr/bin/python3
"""This module contains a class that defines a student"""


class Student:
    """This class is a template for its object instances"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the attribute in a dict form for the exact attribute"""
        if attrs is None:
            return self.__dict__
        else:
            exact_attrib = {}
            obj_dict = self.__dict__
            l_keys = obj_dict.keys()
            for ky in l_keys:
                if ky in attrs:
                    exact_attrib[ky] = obj_dict[ky]
            return exact_attrib

    def reload_from_json(self, json):
        """will reload the json to overite at dict attribute of the object"""
        self.__dict__ = json
        return self.__dict__
