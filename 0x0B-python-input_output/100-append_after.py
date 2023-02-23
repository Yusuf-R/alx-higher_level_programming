#!/usr/bin/python3
"""This module contains a function for search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function searches for the specific string, when it matches,
    it will append or write a new string in a new line
    """
    with open(filename, mode="r", encoding="utf-8") as fd:
        data_list = fd.readlines()

    with open(filename, mode="w", encoding="utf-8") as fd:
        for line in data_list:
            fd.write(line)
            if search_string in line:
                fd.write(new_string)
