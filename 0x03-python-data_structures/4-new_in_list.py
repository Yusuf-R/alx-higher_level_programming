#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = my_list.copy()
    if idx < 0:
        return list_cpy
    elif idx > len(my_list) - 1:
        return list_cpy
    list_cpy[idx] = element
    return list_cpy
