#!/usr/bin/python3
def safe_print_list_integers(my2_list=[], x=0):
    idx_1 = 0
    try:
        while idx_1 < x:
            if type(my2_list[idx_1]) == int:
                print("{:d}".format(my2_list[idx_1]), end="")
                idx_1 += 1
            else:
                idx_1 += 1
                continue
    except (TypeError, ValueError):
        pass
    else:
        print()
        return idx_1
