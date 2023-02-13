#!/usr/bin/python3
"""
This is a module that contains the function as defined

Operations:
    Exceptions:
        TypeError : if the type is not a string

    Returns:
        The printed name having first and last name concat'd
"""


def say_my_name(first_name, last_name=""):
    """
    This function retunrs the combined string of first name
    last name and last name together

    Args:
        first_name(str) : first name
        last_name(str)  : last name

    Return:
        "first_name last_name"

    Example:
        first_name is Abdulwasiu
        last_name is Yusuf
        function returns = Abdulwasiu Yusuf
    """
    te_1 = "first_name must be a string"
    te_2 = "second_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(te_1)
    if not isinstance(last_name, str):
        raise TypeError(te_2)
    print("My name is {} {}".format(first_name, last_name))
