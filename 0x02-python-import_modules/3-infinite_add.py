#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    list_sum = 0
    cmd_argz = sys.argv
    print(cmd_argz)
    list_len = len(cmd_argz)
    print(list_len)
    for trav in range(1, list_len):
        list_sum += int(cmd_argz[trav])
    print(list_sum)
