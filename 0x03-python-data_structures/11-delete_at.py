#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return my_list
    len_list = len(my_list)
    if idx >= len_list or idx < 0:
        return my_list
    for n_idx in range(len_list):
        if n_idx != idx:
            continue
        else:
            del my_list[n_idx]
    return my_list
