#!/usr/bin/python3
"""
This module contains a function that serialize
a python object to a json obj and saves it in a file

In here we use the dump() function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function serialises a python object to json object
        This process is called Encoding
    """
    with open(filename, "w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)
