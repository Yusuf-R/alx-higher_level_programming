#!/usr/bin/python3
def safe_print_list_integers(my2_list=[], x=0):
    idx_1 = 0
    for i in range(x):
        try:
            print("{:d}".format(my2_list[i]), end="")
            idx_1 += 1
        except (TypeError, ValueError):
            pass
    print()
    return idx_1
