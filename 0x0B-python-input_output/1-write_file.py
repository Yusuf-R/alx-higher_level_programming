#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """
    This function write into a file

    Returns:
        int: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as fd:
        return fd.write(text)
