#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_list = my_list[0]
    for i in my_list:
        if i > max_list:
            max_list = i
    return max_list
