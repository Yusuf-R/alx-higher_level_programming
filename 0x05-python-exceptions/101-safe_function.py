#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        solv = fct(*args)
        return solv
    except Exception as x_te:
        sys.stderr.write("Exception: {}\n".format(x_te))
        return None
