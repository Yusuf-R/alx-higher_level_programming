#!/usr/bin/python3
"""
This is a module that contains a function for
printing out the size of a square

Exceptoions:
    TypeError: if the arg is not an int of a float

    ValueError: if the arg is < 0
"""


def text_indentation(text):
    """
    This function prints out the size of square

    Args:
        size (int): the size of the square

    Returns:
        char: '#' denoting the size of the square
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    text_l = []
    for mod_char in text:
        if mod_char in ["?", ".", ":"]:
            new_text += mod_char + "\n\n"
        else:
            new_text += mod_char
    new_list = new_text.split("\n")
    for mod_str in new_list:
        text_l.append(mod_str.strip())
    final_text = "\n".join(text_l)
    print(final_text,end="")
