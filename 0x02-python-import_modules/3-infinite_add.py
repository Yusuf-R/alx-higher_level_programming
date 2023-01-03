#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    list_sum = 0
    cmd_argz = sys.argv
    list_len = len(cmd_argz)
    for trav in range(1, list_len):
        list_sum += int(cmd_argz[trav])
    print("{}".format(list_sum))
