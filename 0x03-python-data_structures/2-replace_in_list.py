#!/usr/bin/python3

"""
this function replaces an element of a list
at a specific position
"""


def replace_in_list(my_list, idx, element):
    ele = len(my_list)
    if (idx < 0) or (idx >= ele):
        return my_list
    else:
        my_list[idx] = element
        return my_list
