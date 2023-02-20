#!/usr/bin/python3
"""
This module has a function that checks if an object
is an instance of anothoer class strictly
"""


def inherits_from(obj, a_class):
    """
    This checks if the obj is an instance of another class
    and not the direct class

    Returns:
        True: if obj is an instance of another class
        Fase: if the obj is direct instace of the class
    """
    obj_cls = type(obj)
    obj_mro = obj_cls.mro()
    if a_class in obj_mro and obj_mro.index(a_class) != 0:
        return True
    else:
        return False
