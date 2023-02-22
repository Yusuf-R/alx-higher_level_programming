#!/usr/bin/python3
"""This module contains a class that defines a student"""


class Student:
    """This class is a template for its object instances"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the attribute in a dict form"""
        return self.__dict__
