#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for data in reversed(my_list):
        if data == int(data):
            print("{:d}".format(data))
        else:
            return None
