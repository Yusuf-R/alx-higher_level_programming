#!/usr/bin/python3
"""
This module contains a class that operates
only when the instnace attributes matches the
slot parameter
""""


class LockedClass:
    """
    This object to this class will only be instantiated
    when the attributes matches the content of the slots
    parameters
    """
    __slots__ = ["first_name"]