#!/usr/bin/python3
def search_replace(my_list, search, replace):
    func_list = [x for x in my_list]
    for xyz in range(len(func_list)):
        if func_list[xyz] == search:
            func_list[xyz] = replace
        else:
            continue
    return func_list
