#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    maxIdx = None
    if type(a_dictionary) is dict:
        for (k, v) in a_dictionary.items():
            if v > max:
                max = v
                maxIdx = k
    return maxIdx
