#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        sys.stdout.write("{:d}\n".format(value))
        return True
    except ValueError as x_te:
        sys.stderr.write("Exception: {}\n".format(x_te))
        return False
