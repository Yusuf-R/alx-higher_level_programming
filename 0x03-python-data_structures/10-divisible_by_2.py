#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    test_list = []
    for num in range(len(my_list)):
        if my_list[num] % 2 != 0:
            test_list.append(False)
        else:
            test_list.append(True)
    return test_list
