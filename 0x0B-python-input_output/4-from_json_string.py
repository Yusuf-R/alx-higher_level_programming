#!/usr/bin/python3
"""
This module contains a function that deserialize
a json object to a python object"

In here we use the loads() since we are not dealing with a file
"""
import json


def from_json_string(my_str):
    """
    This function deserialises a json object to python object
        This process is called Decoding
    """
    py_obj = json.loads(my_str)
    return py_obj
