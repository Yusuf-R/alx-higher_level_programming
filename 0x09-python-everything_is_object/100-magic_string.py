#!/usr/bin/python3
"""Returns a strig using memory of the previous call"""


def magic_string(var=[]):
    """returns the string with the appended string"""
    var.append("BestSchool")
    return ", ".join(var)
