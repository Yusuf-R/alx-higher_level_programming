#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x_val = int(value)
    except Exception:
        return False
    else:
        print("{:d}".format(x_val))
        return True
