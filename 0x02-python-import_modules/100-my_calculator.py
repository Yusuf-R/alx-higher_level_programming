#!/usr/bin/python3
import calculator_1 as xcal
import sys


if __name__ == '__main__':
    user_argz = sys.argv
    err = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    opt_err = "Unknown operator. Available operators: +, -, * and /"
    len_argz = len(user_argz)
    if len_argz == 4:
        a = int(user_argz[1])
        opt_sign = user_argz[2]
        b = int(user_argz[3])
        match opt_sign:
            case "+":
                cal_sum = xcal.add(a, b)
                print("{} + {} = {}".format(a, b, cal_sum))
            case "-":
                cal_sub = xcal.sub(a, b)
                print("{} - {} = {}".format(a, b, cal_sub))
            case "*":
                cal_mul = xcal.mul(a, b)
                print("{} * {} = {}".format(a, b, cal_mul))
            case "/":
                cal_div = xcal.div(a, b)
                print("{} / {} = {}".format(a, b, cal_div))
            case default:
                print(opt_err)
                exit(1)
    else:
        print(err)
        exit(1)
