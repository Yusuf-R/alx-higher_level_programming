#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def append_write(filename="", text=""):
    """
    This function appends to an existing or new file

    Returns:
        int: the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as fd:
        return fd.write(text)
