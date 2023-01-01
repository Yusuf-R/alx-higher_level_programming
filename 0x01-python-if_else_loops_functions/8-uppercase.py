#!/usr/bin/python3
def uppercase(str):
    for single_char in str:
        if 96 < ord(single_char) < 123:
            update = ord(single_char) - 32
            single_char = chr(update)
        print("{}".format(single_char), end="")
