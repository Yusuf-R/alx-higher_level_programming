#!/usr/bin/python3
def print_last_digit(number):
    temp = abs(number) % 10
    print("{:d}".format(temp), end="")
    return temp
