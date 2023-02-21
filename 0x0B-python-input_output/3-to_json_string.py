#!/usr/bin/python3
"""
This module contains a function that serialize a python object"

In here we use the dumps() since we are not dealing with a file
"""
import json


def to_json_string(my_obj):
    """
    This function serialises a python object to a json
        This process is called Encoding
    """
    obj_json = json.dumps(my_obj)
    return obj_json
