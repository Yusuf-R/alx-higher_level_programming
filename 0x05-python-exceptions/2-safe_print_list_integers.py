#!/usr/bin/python3
def safe_print_list_integers(my2_list=[], x=0):
    idx_1 = 0
    try:
        for x_items in my2_list:
            if type(x_items) == int and idx_1 < x:
                print("{:d}".format(x_items), end="")
                idx_1 += 1
    except IndexError:
        print()
        return idx_1
    else:
        print()
        return idx_1
