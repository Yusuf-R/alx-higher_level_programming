#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tp_len = len(sentence)
        tp_0 = None
        tp_sen = (tp_len, tp_0)
        return (tp_sen)
    else:
        tp_len = len(sentence)
        tp_0 = sentence[0]
        tp_sen = (tp_len, tp_0)
        return (tp_sen)
