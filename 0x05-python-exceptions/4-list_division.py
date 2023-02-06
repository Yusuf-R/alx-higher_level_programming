#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for idx in range(list_length):
        try:
            if type(my_list_1[idx]) == int or float:
                res.append(my_list_1[idx] / my_list_2[idx])
        except TypeError:
            res.append(0)
            print("wrong type")
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
        except IndexError:
            res.append(0)
            print("out of range")
        finally:
            res = res
    return res
