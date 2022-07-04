#!/usr/bin/python3

"""
this function replaces an element of a list
at a specific position without modifying the original list
"""


def new_in_list(my_list, idx, element):
    ele = len(my_list)
    if (idx < 0) or (idx >= ele):
        return my_list
    else:
        my_new_list = my_list[:]
        my_new_list[idx] = element
        return my_new_list
