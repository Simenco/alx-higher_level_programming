#!/usr/bin/python3

"""
a function that returns a key with the biggest integer value
"""


def best_score(a_dictionary):
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return None

    result = list(a_dictionary.keys())[0]
    biggest = a_dictionary[result]
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            result = key
    return
