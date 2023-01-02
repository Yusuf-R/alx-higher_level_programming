#!/usr/bin/python3
def remove_char_at(str, n):
    str_temp = str
    str_len = len(str_temp)
    if n > str_len:
        return str_temp
    for del_idx in range(str_len):
        if del_idx == n:
            continue
        print("{}".format(str_temp[del_idx]), end="")
    return ""
