#!/usr/bin/python3
"""
This is a module that contains a rebel int
implementation of a class
"""


class MyInt(int):

    """
    This template will contain fliped behaviour of the
    class int
    """
    def __ne__(self, other):
        return True

    def __eq__(self, other):
        return False
