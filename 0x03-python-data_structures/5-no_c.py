#!/usr/bin/python3

"""
this function removes all characters c and C from a string
returns the new string.
"""


def no_c(my_string):
    n = len(my_string)
    for i in range(n):
        j = my_string[i]
        new_str = ''.join([j for i in range(n) if j not in 'cC'])
        return new_str
