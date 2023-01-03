#!/usr/bin/python3
import sys


if __name__ == '__main__':
    cmd_arg = sys.argv
    cmd_len = len(cmd_arg)
    if cmd_len < 2:
        print("{} arguments.".format(cmd_len - 1))
    elif cmd_len == 2:
        print("{} argument:".format(cmd_len - 1))
        for cmd_idx in range(1, cmd_len):
            print("{}: {}".format(cmd_idx, cmd_arg[cmd_idx]))
    elif cmd_len > 2:
        print("{} arguments:".format(cmd_len - 1))
        for cmd_idx in range(1, cmd_len):
            print("{}: {}".format(cmd_idx, cmd_arg[cmd_idx]))
