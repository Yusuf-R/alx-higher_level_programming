#!/usr/bin/python3
"""A module that defines a class that inherits from a list"""


class MyList(list):
    """A class the set the objects to list attributes"""

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """Prints the object in a sorted order"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
