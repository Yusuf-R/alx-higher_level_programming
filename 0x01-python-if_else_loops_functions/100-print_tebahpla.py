#!/usr/bin/python3
z_lower = 122
A_upper = 89
while 96 < z_lower and 64 < A_upper:
    print("{}{}".format(chr(z_lower), chr(A_upper)), end="")
    z_lower -= 2
    A_upper -= 2
