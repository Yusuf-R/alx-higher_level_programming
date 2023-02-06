#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as x_te:
        sys.stderr.write("Exception: {}\n".format(x_te))
        return False
