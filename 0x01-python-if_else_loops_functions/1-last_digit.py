#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    y = number * -1
    test = y % 10
    test *= -1
else:
    test = number % 10
con5 = " and is greater than 5"
con_def = " and is less than 6 and not 0"
con0 = " and is 0"
if test > 5:
    print("Last digit of {} is {}{}".format(number, test, con5))
elif test == 0:
    print("Last digit of {} is {}{}".format(number, test, con0))
elif test < 6 or test < 0:
    print("Last digit of {} is {}{}".format(number, test, con_def))
