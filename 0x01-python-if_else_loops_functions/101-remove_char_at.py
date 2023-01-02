#!/usr/bin/python3
def remove_char_at(str, n):
    str_ret = ""
    str_len = len(str)
    if n > str_len:
        return str
    for del_idx in range(str_len):
        if del_idx == n:
            continue
        str_ret += str[del_idx]
    return str_ret
