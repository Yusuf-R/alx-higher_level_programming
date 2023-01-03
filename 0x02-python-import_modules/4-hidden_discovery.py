#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names_define = dir(hidden_4)
    for pref_name in names_define:
        if pref_name[0:2] != '__':
            print(pref_name)
