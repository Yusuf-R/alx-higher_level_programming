#!/usr/bin/python3
"""This module contains a function for reading a file"""


def read_file(filename=""):
    """This function reads a text file and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as fd:
        print(fd.read(), end="")
