#!/usr/bin/python3

"""
this function removes all characters c and C from a string
returns the new string.
"""


def no_c(my_string):
    n = len(my_string)
    j = my_string
    new_str = ''.join([j[i] for i in range(n) if j[i] not in 'cC'])
    return new_str
