#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n_tp1 = ()
    n_tp2 = ()
    l_tp1 = len(tuple_a)
    l_tp2 = len(tuple_b)

    if l_tp1 >= 2:
        for trv in tuple_a:
            if trv == ():
                trv = 0
                n_tp1 += (trv,)
                continue
            else:
                n_tp1 += (trv,)

    elif l_tp1 == 1:
        tuple_a += (0,)
        n_tp1 = tuple_a

    elif l_tp1 == 0:
        tuple_a += (0,)
        tuple_a += (0,)
        n_tp1 = tuple_a

    if l_tp2 >= 2:
        for trv in tuple_b:
            if trv == ():
                trv = 0
                n_tp2 += (trv,)
                continue
            else:
                n_tp2 += (trv,)

    elif l_tp2 == 1:
        tuple_b += (0,)
        n_tp2 = tuple_b

    elif l_tp2 == 0:
        tuple_b += (0,)
        tuple_b += (0,)
        n_tp2 = tuple_b

    ln_tp1 = list(n_tp1)
    ln_tp2 = list(n_tp2)
    s_l = [ln_tp1[0] + ln_tp2[0], ln_tp1[1] + ln_tp2[1]]
    s_l = tuple(s_l)
    return s_l
