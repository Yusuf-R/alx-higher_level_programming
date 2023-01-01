#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        temp = number * -1
        temp = temp % 10
        temp = temp * -1
    else:
        temp = number % 10
    return temp
