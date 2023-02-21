#!/usr/bin/python3
"""
This module contains a function that deserialize
a json object to a python object"

In here we use the load() since we are now dealing with a file
"""
import json


def load_from_json_file(filename):
    """
    This function deserialises a json object to python object
        This process is called Decoding
    """
    with open(filename, mode="r", encoding="utf-8") as fd:
        return json.load(fd)
